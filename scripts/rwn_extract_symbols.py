#!/usr/bin/env python3
"""
rwn_extract_symbols.py — extract procedure names, variable names, and source
filename from any decrypted TAS Pro 7 .RWN file (or from an encrypted .RWN
on the network share, decrypting with K_B automatically).

Usage:
    python rwn_extract_symbols.py <file.RWN>  [--encrypted] [--json]
    python rwn_extract_symbols.py --batch <dir> [--json]

Options:
    --encrypted   Decrypt first using K_B before parsing.
    --json        Output JSON instead of human-readable text.
    --batch <dir> Process every .RWN file in <dir> (recursively).

Confidence:
    Procedure table : 95/100
    Variable table  : 100/100
    Source filename : 100/100
    File ref table  : 100/100
"""

import struct
import sys
import os
import json
import argparse

# K_B — the runtime key for .RWN files (captured live via Frida 2026-06-16)
K_B_HEX = 'a898d21e2fd6ca294026e5d633d9047f91f7ed35'

PROC_ENTRY_SIZE = 53
VAR_ENTRY_SIZE  = 77
SRCNAME_SIZE    = 60
HEADER_SIZE     = 128   # 0x80
FILE_TABLE_OFF  = 0x80
FILE_ENTRY_SIZE = 16


# ── Decrypt ───────────────────────────────────────────────────────────────────

def decrypt_evo_file(raw_bytes, key_raw_20):
    """Canonical Twofish-192-CFB-128 decrypt (see decryption-findings.md)."""
    try:
        from twofish_pure import Twofish
    except ImportError:
        raise SystemExit("ERROR: twofish_pure.py not found. "
                         "Place scripts/twofish_pure.py next to this script.")
    key_192 = key_raw_20 + b'\x00' * 4
    tf = Twofish(key_192)
    P_init = tf.encrypt(bytes(16))
    K0     = tf.encrypt(P_init)

    header_ct = raw_bytes[0:8]
    header_pt = bytes(a ^ b for a, b in zip(header_ct, K0[:8]))
    if header_pt[0:4] != header_pt[4:8]:
        raise ValueError("Decryption failed — validation bytes don't match. "
                         "Wrong key or not a valid .RWN file.")

    P      = K0
    body   = raw_bytes[8:]
    result = bytearray()
    for i in range(0, len(body), 16):
        blk = body[i:i+16]
        K   = tf.encrypt(P)
        result.extend(a ^ b for a, b in zip(blk, K))
        if len(blk) == 16:
            P = blk
    return bytes(result)


# ── Header parsing ─────────────────────────────────────────────────────────────

def read_header(data):
    """Return dict of the meaningful header DWORDs."""
    def dw(off):
        return struct.unpack_from('<I', data, off)[0]
    return {
        'dispatch_table_size': dw(0x00),   # bytes
        'proc_table_size':     dw(0x0C),   # bytes; proc_count = this / 53
        'var_count':           dw(0x14),   # number of variable entries
        'srcname_size':        dw(0x1C),   # always 60
        'var_table_size':      dw(0x20),   # bytes; should == var_count * 77
        'format_marker':       data[0x35:0x3A].decode('ascii', errors='replace'),
    }


# ── File reference table (offset 0x80) ────────────────────────────────────────

def read_file_table(data):
    """Return list of database file names the program opens."""
    names = []
    off = FILE_TABLE_OFF
    while off + FILE_ENTRY_SIZE <= len(data):
        entry = data[off:off + FILE_ENTRY_SIZE]
        if entry == b'\x00' * FILE_ENTRY_SIZE:
            break
        name = entry.rstrip(b'\x00 ').decode('ascii', errors='replace')
        if name:
            names.append(name)
        off += FILE_ENTRY_SIZE
    return names


# ── Procedure table ───────────────────────────────────────────────────────────

def read_procedures(data, hdr):
    """Return list of procedure name strings."""
    var_table_off = len(data) - hdr['var_table_size']
    src_off       = var_table_off - SRCNAME_SIZE
    proc_off      = src_off - hdr['proc_table_size']

    if proc_off < 0 or hdr['proc_table_size'] % PROC_ENTRY_SIZE != 0:
        return []   # malformed

    count = hdr['proc_table_size'] // PROC_ENTRY_SIZE
    procs = []
    for i in range(count):
        entry_off  = proc_off + i * PROC_ENTRY_SIZE
        name_len   = data[entry_off]
        raw_name   = data[entry_off + 1 : entry_off + 1 + min(name_len, 15)]
        procs.append(raw_name.decode('ascii', errors='replace').rstrip('\x00'))
    return procs


# ── Source filename ───────────────────────────────────────────────────────────

def read_source_filename(data, hdr):
    """Return the original .SRC filename embedded in the compiled binary."""
    var_table_off = len(data) - hdr['var_table_size']
    src_off       = var_table_off - SRCNAME_SIZE
    raw = data[src_off : src_off + SRCNAME_SIZE]
    return raw.rstrip(b'\x00 ').decode('ascii', errors='replace')


# ── Variable table ────────────────────────────────────────────────────────────

def read_variables(data, hdr):
    """Return list of {'type': int, 'name': str} dicts.

    Variable entry layout (77 bytes):
      Bytes 0-14: 15-byte name field, space-padded.
                  Byte 0 is either:
                    - A control char (< 0x20): a type-category code (compiler-generated
                      temp vars have 0x05 here); actual name starts at byte 1.
                    - A printable char: the first character of the variable name;
                      name spans bytes 0-14.
      Byte 15:    null terminator.
      Bytes 16-76: metadata (61 bytes, meaning not fully decoded).
    """
    var_table_off = len(data) - hdr['var_table_size']
    count         = hdr['var_count']
    vars_out      = []
    for i in range(count):
        entry_off  = var_table_off + i * VAR_ENTRY_SIZE
        if entry_off + VAR_ENTRY_SIZE > len(data):
            break
        type_byte = data[entry_off]
        if type_byte < 0x20:
            # Non-printable type code: name starts at byte 1
            raw_name = data[entry_off + 1 : entry_off + 15]
        else:
            # Printable first char: name starts at byte 0
            raw_name = data[entry_off : entry_off + 15]
        name = raw_name.rstrip(b'\x00 ').decode('ascii', errors='replace')
        vars_out.append({'type': type_byte, 'name': name})
    return vars_out


# ── Main extractor ─────────────────────────────────────────────────────────────

def _strip_validation_header(data):
    """
    rwn_decrypt.py prepends the 8-byte validation header (header_pt) to every
    .dec file.  header_pt[0:4] == header_pt[4:8], so detect and strip it.
    """
    if len(data) >= 8 and data[0:4] == data[4:8]:
        return data[8:]
    return data


def extract_symbols(path, decrypt=False):
    raw = open(path, 'rb').read()
    if decrypt:
        raw = decrypt_evo_file(raw, bytes.fromhex(K_B_HEX))
    else:
        raw = _strip_validation_header(raw)

    hdr        = read_header(raw)
    file_refs  = read_file_table(raw)
    source_fn  = read_source_filename(raw, hdr)
    procs      = read_procedures(raw, hdr)
    variables  = read_variables(raw, hdr)

    return {
        'path':         path,
        'size_bytes':   len(raw),
        'header':       hdr,
        'source_file':  source_fn,
        'db_files':     file_refs,
        'procedures':   procs,
        'variables':    variables,
    }


# ── Output formatters ─────────────────────────────────────────────────────────

def print_human(result):
    h = result['header']
    print(f"\n{'='*60}")
    print(f"File  : {result['path']}")
    print(f"Size  : {result['size_bytes']:,} bytes")
    print(f"Marker: {h['format_marker']}")
    print(f"Source: {result['source_file']}")
    print(f"\nProcedures ({len(result['procedures'])}):")
    for p in result['procedures']:
        print(f"  {p}")
    print(f"\nDB files opened ({len(result['db_files'])}):")
    for f in result['db_files']:
        print(f"  {f}")
    print(f"\nVariables ({h['var_count']}):")
    for v in result['variables']:
        t = v['type']
        tag = f"0x{t:02X}" if t < 0x20 else chr(t)
        print(f"  [{tag}] {v['name']}")


# ── Batch mode ────────────────────────────────────────────────────────────────

def batch(directory, as_json, decrypt):
    results = []
    for root, _dirs, files in os.walk(directory):
        for fname in files:
            if not fname.upper().endswith('.RWN'):
                continue
            fpath = os.path.join(root, fname)
            try:
                r = extract_symbols(fpath, decrypt=decrypt)
                results.append(r)
                if not as_json:
                    print_human(r)
            except Exception as e:
                msg = f"ERROR processing {fpath}: {e}"
                if as_json:
                    results.append({'path': fpath, 'error': str(e)})
                else:
                    print(msg, file=sys.stderr)

    if as_json:
        print(json.dumps(results, indent=2))
    else:
        print(f"\nProcessed {len(results)} files.")
    return results


# ── CLI entry point ───────────────────────────────────────────────────────────

def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('file', nargs='?', help='.RWN file to process')
    ap.add_argument('--encrypted', action='store_true',
                    help='Decrypt with K_B before parsing')
    ap.add_argument('--json', action='store_true', help='Output JSON')
    ap.add_argument('--batch', metavar='DIR',
                    help='Recursively process all .RWN files in DIR')
    args = ap.parse_args()

    if args.batch:
        batch(args.batch, args.json, args.encrypted)
    elif args.file:
        try:
            result = extract_symbols(args.file, decrypt=args.encrypted)
        except Exception as e:
            print(f"ERROR: {e}", file=sys.stderr)
            sys.exit(1)
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print_human(result)
    else:
        ap.print_help()


if __name__ == '__main__':
    main()
