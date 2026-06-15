#!/usr/bin/env python3
"""
scripts/rwn_decrypt.py

Batch decryptor for EvoERP .RWN (and optionally .DCY) files.

CIPHER SCHEME (confirmed by disassembly of mode2_handler at file 0x34DF50)
---------------------------------------------------------------------------
Twofish-CFB with 192-bit key and uninitialized heap IV.  Slightly unusual
CFB because the .RWN header has an 8-byte validation block (partial block),
which shifts the CFB state before the body begins.

Key derivation (confirmed at file 0x75D154):
    key = SHA1('mabufoju')[0:20] + b'\\x00' * 4    # 24 bytes (192-bit)

Per-file decryption:
  1. ct[0:8]  = validation block (stored as ciphertext in file)
     K0       = Twofish_ECB_Encrypt(key, IV)
     pt[0:8]  = ct[0:8] XOR K0[0:8]
     check:   pt[0:4] == pt[4:8]  (EVO integrity check)

  2. After validation, CFB state is the MIX of partial feedback:
     block_buf = ct[0:8] + K0[8:16]
     (first 8 bytes of block_buf replaced with ciphertext; upper half unchanged)

  3. Body (16-byte blocks, or partial last block):
     K_n      = Twofish_ECB_Encrypt(key, block_buf)
     pt_n     = ct_n XOR K_n[:len(ct_n)]
     block_buf = ct_n  (full CFB: next block_buf = current ciphertext)

USAGE
-----
    # Decrypt all .RWN files from the network share:
    python scripts/rwn_decrypt.py

    # Dry-run validation (no output files written):
    python scripts/rwn_decrypt.py --validate-only

    # Limit to N files (for spot-checking):
    python scripts/rwn_decrypt.py --limit 20

    # Decrypt a single file:
    python scripts/rwn_decrypt.py --file "\\\\server\\share\\DBAMFG$\\T7INA.RWN"

    # Specify custom IV (overrides iv_bytes.bin):
    python scripts/rwn_decrypt.py --iv-hex "9c da c3 45 a5 f0 1c 2c 96 57 92 d9 0b 1a bc 1e"

    # Output directory (default: samples/rwn_decrypted/):
    python scripts/rwn_decrypt.py --out-dir samples/rwn_decrypted

Decrypted files are written with the same filename + '.dec' extension.
A summary CSV (decrypt_summary.csv) is written to the output directory.
"""

import sys
import os
import hashlib
import struct
import csv
import argparse
import time
import multiprocessing

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

_here  = os.path.dirname(os.path.abspath(__file__))
_repo  = os.path.dirname(_here)
sys.path.insert(0, _here)

from twofish_pure import Twofish

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
_KEY = hashlib.sha1(b'mabufoju').digest() + b'\x00' * 4   # 24 bytes (192-bit)

_RWN_ROOTS = [
    r'\\i2s109-solidcrm\DBAMFG$',
    r'C:\ISTS',
]

_DEFAULT_OUT  = os.path.join(_repo, 'samples', 'rwn_decrypted')
_DEFAULT_IV   = os.path.join(_here, 'iv_bytes.bin')
_KNOWN_XOR    = 0x3E0A37C5


# ---------------------------------------------------------------------------
# Core decryption logic
# ---------------------------------------------------------------------------

def _le32(b, off):
    return struct.unpack_from('<I', b, off)[0]


def decrypt_rwn(data: bytes, iv: bytes, key: bytes = _KEY) -> tuple:
    """
    Decrypt a .RWN file's raw bytes.

    Returns (ok, plaintext, error_msg).
      ok        -- True if validation passed
      plaintext -- bytes (validation block + decrypted body), or None on failure
      error_msg -- description of failure, or '' on success
    """
    if len(data) < 8:
        return False, None, f'File too small ({len(data)} bytes)'

    tf = Twofish(key)

    # --- Validation block (8 bytes) ---
    ct_val  = data[0:8]
    K0      = tf.encrypt(iv)
    pt_val  = bytes(a ^ b for a, b in zip(ct_val, K0[:8]))

    if pt_val[:4] != pt_val[4:]:
        return False, None, (
            f'Validation failed: pt[0:4]={pt_val[:4].hex()} '
            f'!= pt[4:8]={pt_val[4:].hex()}'
        )

    # --- CFB state after partial validation block ---
    # mode2_handler: EncryptBlock in-place -> block_buf = K0
    # Then copies ct[0:8] back into block_buf[0:8] (CFB partial-block feedback)
    block_buf = ct_val + K0[8:16]

    # --- Body (rest of file) ---
    body_ct  = data[8:]
    body_pt  = bytearray()

    for i in range(0, len(body_ct), 16):
        chunk = body_ct[i : i + 16]
        K = tf.encrypt(block_buf)
        pt_chunk = bytes(a ^ b for a, b in zip(chunk, K[:len(chunk)]))
        body_pt.extend(pt_chunk)

        # CFB feedback: block_buf <- ciphertext chunk
        if len(chunk) == 16:
            block_buf = chunk
        else:
            # Partial last block: copy chunk bytes, leave upper bytes unchanged
            block_buf = chunk + block_buf[len(chunk):]

    plaintext = pt_val + bytes(body_pt)
    return True, plaintext, ''


# ---------------------------------------------------------------------------
# File discovery
# ---------------------------------------------------------------------------

def _find_rwn_files(roots, limit=None):
    found = []
    for root in roots:
        if not os.path.isdir(root):
            continue
        for dirpath, _dirs, filenames in os.walk(root):
            for fn in filenames:
                if fn.upper().endswith('.RWN'):
                    found.append(os.path.join(dirpath, fn))
                    if limit and len(found) >= limit:
                        return found
    return found


# ---------------------------------------------------------------------------
# Sniff plaintext type
# ---------------------------------------------------------------------------
_TEXT_CHARS = set(range(0x20, 0x7F)) | {0x09, 0x0A, 0x0D}


def _sniff(pt: bytes) -> str:
    """Return a short label describing the decrypted content."""
    if len(pt) < 8:
        return 'too_short'
    printable = sum(1 for b in pt[:128] if b in _TEXT_CHARS)
    if printable > 100:
        return 'text'
    if pt[0:4] == b'\x00\x00\x00\x01':
        return 'tas6_magic'
    if pt[0:3] == b'TAS':
        return 'TAS_header'
    # Look for common string patterns in first 256 bytes
    try:
        head = pt[:256].decode('latin-1')
        if 'object ' in head or 'TForm' in head or 'TPanel' in head:
            return 'delphi_form'
    except Exception:
        pass
    return f'binary_0x{pt[0]:02x}{pt[1]:02x}'


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def _print_result(idx, total, r):
    fpath, status, size, sniff, err, pt_len = r
    basename = os.path.basename(fpath)
    if status == 'OK':
        print(f'[{idx:4d}/{total}] OK    {basename}  ({size:,} B -> {pt_len:,} pt)  [{sniff}]')
    else:
        print(f'[{idx:4d}/{total}] {status:<5} {basename}: {err}')


def _worker(task):
    """Multiprocessing worker: (fpath, iv, out_dir, validate_only) -> result tuple."""
    fpath, iv_hex, out_dir, validate_only = task
    iv = bytes.fromhex(iv_hex)
    basename = os.path.basename(fpath)
    try:
        data = open(fpath, 'rb').read()
    except Exception as e:
        return (fpath, 'READ_ERROR', 0, '-', str(e), None)

    size = len(data)
    ok, pt, err = decrypt_rwn(data, iv)
    if ok:
        sniff = _sniff(pt)
        if not validate_only:
            out_path = os.path.join(out_dir, basename + '.dec')
            with open(out_path, 'wb') as f:
                f.write(pt)
        return (fpath, 'OK', size, sniff, '', len(pt))
    else:
        return (fpath, 'FAIL', size, '-', err, None)


def main():
    ap = argparse.ArgumentParser(description='EvoERP .RWN batch decryptor')
    ap.add_argument('--validate-only', action='store_true',
                    help='Check validation only; do not write decrypted files')
    ap.add_argument('--limit', type=int, default=None,
                    help='Process at most N files')
    ap.add_argument('--file', default=None,
                    help='Decrypt a single file (ignores --limit and search roots)')
    ap.add_argument('--out-dir', default=_DEFAULT_OUT,
                    help='Output directory (default: samples/rwn_decrypted/)')
    ap.add_argument('--iv-hex', default=None,
                    help='IV as hex string (overrides iv_bytes.bin)')
    ap.add_argument('--roots', nargs='+', default=_RWN_ROOTS,
                    help='Search roots for .RWN files')
    ap.add_argument('--jobs', type=int, default=max(1, multiprocessing.cpu_count() - 1),
                    help='Parallel worker processes (default: cpu_count-1)')
    args = ap.parse_args()

    # Load IV
    if args.iv_hex:
        iv = bytes.fromhex(args.iv_hex.replace(' ', ''))
    elif os.path.isfile(_DEFAULT_IV):
        iv = open(_DEFAULT_IV, 'rb').read()
    else:
        print(f'ERROR: IV file not found: {_DEFAULT_IV}')
        print('Run scripts/get_iv_frida.py first.')
        sys.exit(1)

    if len(iv) != 16:
        print(f'ERROR: IV must be 16 bytes, got {len(iv)}.')
        sys.exit(1)

    # Quick sanity: verify IV constraint
    tf0  = Twofish(_KEY)
    K0   = tf0.encrypt(iv)
    xor4 = _le32(K0, 0) ^ _le32(K0, 4)
    if xor4 != _KNOWN_XOR:
        print(f'WARNING: IV XOR check failed (0x{xor4:08X} != 0x{_KNOWN_XOR:08X})')
        print('IV may be wrong; continuing anyway.')
    else:
        print(f'IV verified: XOR = 0x{xor4:08X}  OK')
    print(f'IV: {iv.hex(" ")}')
    print()

    # Collect files
    if args.file:
        files = [args.file]
    else:
        print(f'Searching for .RWN files in: {args.roots}')
        files = _find_rwn_files(args.roots, limit=args.limit)
        if not files:
            print('No .RWN files found.  Check --roots or network share access.')
            sys.exit(1)
        print(f'Found {len(files)} .RWN file(s)')
        if args.limit:
            print(f'(limited to {args.limit})')
    print()

    # Output dir
    if not args.validate_only:
        os.makedirs(args.out_dir, exist_ok=True)

    jobs      = min(args.jobs, len(files))
    iv_hex    = iv.hex()
    tasks     = [(f, iv_hex, args.out_dir, args.validate_only) for f in files]

    print(f'Workers: {jobs}')
    print()

    results    = []
    ok_count   = 0
    fail_count = 0
    t0         = time.time()

    n = len(files)
    if jobs == 1:
        # Single-process (easier debugging)
        for idx, task in enumerate(tasks, 1):
            r = _worker(task)
            _print_result(idx, n, r)
            results.append(r)
            if r[1] == 'OK':
                ok_count += 1
            else:
                fail_count += 1
    else:
        with multiprocessing.Pool(jobs) as pool:
            for idx, r in enumerate(pool.imap_unordered(_worker, tasks), 1):
                _print_result(idx, n, r)
                results.append(r)
                if r[1] == 'OK':
                    ok_count += 1
                else:
                    fail_count += 1

    elapsed = time.time() - t0

    # Summary
    print()
    print('=' * 70)
    print(f'  Processed : {len(files)}')
    print(f'  OK        : {ok_count}')
    print(f'  FAIL      : {fail_count}')
    print(f'  Time      : {elapsed:.1f}s')
    if not args.validate_only and ok_count:
        print(f'  Output    : {args.out_dir}')
    print('=' * 70)

    if fail_count and ok_count == 0:
        print()
        print('All files FAILED validation.  The IV is likely wrong.')
        print('Re-run scripts/get_iv_frida.py to capture a fresh IV.')

    # Write CSV
    if not args.validate_only:
        csv_path = os.path.join(args.out_dir, 'decrypt_summary.csv')
        with open(csv_path, 'w', newline='', encoding='utf-8') as f:
            w = csv.writer(f)
            w.writerow(['path', 'status', 'size_bytes', 'content_sniff', 'error', 'pt_len'])
            for r in results:
                w.writerow(r)
        print(f'  Summary   : {csv_path}')


if __name__ == '__main__':
    main()
