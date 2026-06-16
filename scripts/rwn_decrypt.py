#!/usr/bin/env python3
"""
scripts/rwn_decrypt.py

Batch decryptor for EvoERP .RWN (TAS Pro 7 compiled program) files.

CIPHER PARAMETERS (confirmed 2026-06-16 via live Frida capture + Python verification)
---------------------------------------------------------------------------------------
  Algorithm  : Twofish-192, CFB-128 mode
  Key        : K_B = a898d21e2fd6ca294026e5d633d9047f91f7ed35 (raw 20 bytes)
               K_B_192 = K_B + 00000000 (24 bytes)
  IV param   : always 0  →  P_initial = Encrypt_K(all-zeros block)
  Body P_start: K0 = Encrypt_K(P_initial)  — NOT P_initial itself
  Validation : header_pt[0:4] == header_pt[4:8]

Per-file decryption (see docs/02-file-formats/decryption-findings.md):
  tf       = Twofish(K_B_192)
  P_initial = tf.encrypt(bytes(16))       # Encrypt_K(zeros)
  K0        = tf.encrypt(P_initial)       # header keystream
  header_pt = header_ct XOR K0[0:8]
  assert header_pt[0:4] == header_pt[4:8]
  P = K0                                  # body starts here
  for each 16-byte body block:
      K = tf.encrypt(P)
      pt_block = ct_block XOR K
      P = ct_block  (CFB-128 feedback)

USAGE
-----
    python scripts/rwn_decrypt.py                      # all .RWN files from share
    python scripts/rwn_decrypt.py --validate-only      # check only, no output
    python scripts/rwn_decrypt.py --limit 20           # spot-check
    python scripts/rwn_decrypt.py --file PATH.RWN      # single file
    python scripts/rwn_decrypt.py --out-dir DIR        # override output dir
"""

import sys
import os
import struct
import csv
import argparse
import time
import multiprocessing

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

_here = os.path.dirname(os.path.abspath(__file__))
_repo = os.path.dirname(_here)
sys.path.insert(0, _here)

from twofish_pure import Twofish

# ---------------------------------------------------------------------------
# Key constants (confirmed 2026-06-16)
# ---------------------------------------------------------------------------
_K_B_RAW = bytes.fromhex('a898d21e2fd6ca294026e5d633d9047f91f7ed35')
_KEY     = _K_B_RAW + b'\x00' * 4    # 24 bytes (192-bit Twofish key)

_RWN_ROOTS   = [r'\\i2s109-solidcrm\DBAMFG$', r'C:\ISTS']
_DEFAULT_OUT = os.path.join(_repo, 'samples', 'rwn_decrypted')
_KNOWN_XOR   = 0x3E0A37C5    # le32(K0,0) XOR le32(K0,4) for K_B


def _le32(b, off):
    return struct.unpack_from('<I', b, off)[0]


# ---------------------------------------------------------------------------
# Core decryption (no external IV file needed)
# ---------------------------------------------------------------------------

def decrypt_rwn(data: bytes, key: bytes = _KEY) -> tuple:
    """
    Decrypt a .RWN file.  Returns (ok, plaintext, error_msg).
    Raises no exceptions — all errors returned as (False, None, msg).
    """
    if len(data) < 8:
        return False, None, f'File too small ({len(data)} bytes)'

    tf = Twofish(key)
    P_initial = tf.encrypt(bytes(16))     # Encrypt_K(zeros)
    K0        = tf.encrypt(P_initial)     # header keystream

    # Validate 8-byte header
    header_ct = data[0:8]
    header_pt = bytes(a ^ b for a, b in zip(header_ct, K0[:8]))
    if header_pt[:4] != header_pt[4:]:
        return False, None, (
            f'Validation failed: pt[0:4]={header_pt[:4].hex()} '
            f'!= pt[4:8]={header_pt[4:].hex()}'
        )

    # Body — CFB-128, P starts at K0 (not P_initial)
    P      = K0
    body   = data[8:]
    result = bytearray()
    for i in range(0, len(body), 16):
        blk = body[i:i+16]
        K   = tf.encrypt(P)
        result.extend(a ^ b for a, b in zip(blk, K[:len(blk)]))
        if len(blk) == 16:
            P = blk    # CFB-128: feedback = ciphertext block

    plaintext = header_pt + bytes(result)
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
# Content sniff
# ---------------------------------------------------------------------------
_TEXT_CHARS = set(range(0x20, 0x7F)) | {0x09, 0x0A, 0x0D}


def _sniff(pt: bytes) -> str:
    if len(pt) < 8:
        return 'too_short'
    printable = sum(1 for b in pt[:128] if b in _TEXT_CHARS)
    if printable > 100:
        return 'text'
    if pt[0:4] == b'\x00\x00\x00\x01':
        return 'tas6_magic'
    if pt[0:3] == b'TAS':
        return 'TAS_header'
    try:
        head = pt[:256].decode('latin-1')
        if 'object ' in head or 'TForm' in head or 'TPanel' in head:
            return 'delphi_form'
    except Exception:
        pass
    return f'binary_0x{pt[0]:02x}{pt[1]:02x}'


# ---------------------------------------------------------------------------
# Worker (multiprocessing)
# ---------------------------------------------------------------------------

def _worker(task):
    fpath, out_dir, validate_only = task
    basename = os.path.basename(fpath)
    try:
        data = open(fpath, 'rb').read()
    except Exception as e:
        return (fpath, 'READ_ERROR', 0, '-', str(e), None)
    size = len(data)
    ok, pt, err = decrypt_rwn(data)
    if ok:
        sniff = _sniff(pt)
        if not validate_only:
            out_path = os.path.join(out_dir, basename + '.dec')
            with open(out_path, 'wb') as f:
                f.write(pt)
        return (fpath, 'OK', size, sniff, '', len(pt))
    else:
        return (fpath, 'FAIL', size, '-', err, None)


def _print_result(idx, total, r):
    fpath, status, size, sniff, err, pt_len = r
    basename = os.path.basename(fpath)
    if status == 'OK':
        print(f'[{idx:4d}/{total}] OK    {basename}  ({size:,} B -> {pt_len:,} pt)  [{sniff}]')
    else:
        print(f'[{idx:4d}/{total}] {status:<10} {basename}: {err}')


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description='EvoERP .RWN batch decryptor (K_B key, P_start=K0)')
    ap.add_argument('--validate-only', action='store_true',
                    help='Validate only; do not write decrypted files')
    ap.add_argument('--limit', type=int, default=None)
    ap.add_argument('--file', default=None, help='Decrypt a single file')
    ap.add_argument('--out-dir', default=_DEFAULT_OUT)
    ap.add_argument('--roots', nargs='+', default=_RWN_ROOTS)
    ap.add_argument('--jobs', type=int,
                    default=max(1, multiprocessing.cpu_count() - 1))
    args = ap.parse_args()

    # Confirm K0 constant at startup
    tf0 = Twofish(_KEY)
    P_init = tf0.encrypt(bytes(16))
    K0     = tf0.encrypt(P_init)
    xor4   = _le32(K0, 0) ^ _le32(K0, 4)
    if xor4 == _KNOWN_XOR:
        print(f'K_B verified: K0 XOR = 0x{xor4:08X}  OK')
    else:
        print(f'WARNING: K0 XOR = 0x{xor4:08X}, expected 0x{_KNOWN_XOR:08X}')
    print(f'K_B raw: {_K_B_RAW.hex()}')
    print(f'K0:      {K0.hex()}')
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

    if not args.validate_only:
        os.makedirs(args.out_dir, exist_ok=True)

    jobs  = min(args.jobs, len(files))
    tasks = [(f, args.out_dir, args.validate_only) for f in files]
    print(f'Workers: {jobs}')
    print()

    results    = []
    ok_count   = 0
    fail_count = 0
    t0         = time.time()
    n          = len(files)

    if jobs == 1:
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
    print()
    print('=' * 70)
    print(f'  Processed : {n}')
    print(f'  OK        : {ok_count}')
    print(f'  FAIL      : {fail_count}')
    print(f'  Time      : {elapsed:.1f}s')
    if not args.validate_only and ok_count:
        print(f'  Output    : {args.out_dir}')
    print('=' * 70)

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
