#!/usr/bin/env python3
"""
scripts/dcy_decrypt.py

Batch decryptor for EvoERP .DCY (data dictionary) files.

Same Twofish-CFB cipher as .RWN, but different IV.

IV_dcy = cd 47 af 18 e0 d1 c3 8c f1 d8 a0 67 fc 3d da 28
         (captured 2026-06-15 via Frida spawn hook on evoerp.exe)
         Verified: Twofish_ECB_Encrypt(key, IV_dcy)[0:4]^[4:8] = 0x0955DC84
         Matches all 41 of 41 "standard" .DCY files on the share.

USAGE
-----
    # Decrypt all .DCY files:
    python scripts/dcy_decrypt.py

    # Validate only (no output files written):
    python scripts/dcy_decrypt.py --validate-only

    # Single file:
    python scripts/dcy_decrypt.py --file "\\\\server\\share\\DBAMFG$\\DBAMENU_FLEX.DCY"

    # Custom IV:
    python scripts/dcy_decrypt.py --iv-hex "cd 47 af 18 e0 d1 c3 8c f1 d8 a0 67 fc 3d da 28"

    # Output directory (default: samples/dcy_decrypted/):
    python scripts/dcy_decrypt.py --out-dir samples/dcy_decrypted
"""

import sys, os, hashlib, struct, csv, argparse, time

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

_here = os.path.dirname(os.path.abspath(__file__))
_repo = os.path.dirname(_here)
sys.path.insert(0, _here)
from twofish_pure import Twofish

_KEY         = hashlib.sha1(b'mabufoju').digest() + b'\x00' * 4
_DCY_ROOTS   = [r'\\i2s109-solidcrm\DBAMFG$']
_DEFAULT_OUT = os.path.join(_repo, 'samples', 'dcy_decrypted')
_DEFAULT_IV  = os.path.join(_here, 'iv_dcy_bytes.bin')
_KNOWN_XOR   = 0x0955DC84


def _le32(b, off):
    return struct.unpack_from('<I', b, off)[0]


def decrypt_dcy(data: bytes, iv: bytes, key: bytes = _KEY) -> tuple:
    """
    Decrypt a .DCY file's raw bytes.
    Same CFB structure as .RWN (8-byte validation block then body).
    Returns (ok, plaintext, error_msg).
    """
    if len(data) < 8:
        return False, None, f'File too small ({len(data)} bytes)'

    tf = Twofish(key)

    # Validation block
    ct_val = data[0:8]
    K0     = tf.encrypt(iv)
    pt_val = bytes(a ^ b for a, b in zip(ct_val, K0[:8]))

    if pt_val[:4] != pt_val[4:]:
        return False, None, (
            f'Validation failed: pt[0:4]={pt_val[:4].hex()} != pt[4:8]={pt_val[4:].hex()}'
        )

    # CFB state after partial validation block
    block_buf = ct_val + K0[8:16]

    # Body
    body_ct = data[8:]
    body_pt = bytearray()
    for i in range(0, len(body_ct), 16):
        chunk = body_ct[i:i+16]
        K = tf.encrypt(block_buf)
        body_pt.extend(a ^ b for a, b in zip(chunk, K[:len(chunk)]))
        if len(chunk) == 16:
            block_buf = chunk
        else:
            block_buf = chunk + block_buf[len(chunk):]

    return True, pt_val + bytes(body_pt), ''


def _find_dcy(roots, limit=None):
    found = []
    for root in roots:
        if not os.path.isdir(root):
            continue
        for dirpath, _dirs, files in os.walk(root):
            for fn in files:
                if fn.upper().endswith('.DCY'):
                    found.append(os.path.join(dirpath, fn))
                    if limit and len(found) >= limit:
                        return found
    return found


def _sniff(pt: bytes) -> str:
    if len(pt) < 8:
        return 'too_short'
    printable = sum(1 for b in pt[:128] if 0x20 <= b < 0x7F or b in (9,10,13))
    if printable > 100:
        return 'text'
    # Look for TAS data dictionary magic
    if pt[0:4] == pt[4:8]:  # validation pattern visible in PT
        return f'dcy_hdr_0x{pt[0:4].hex()}'
    return f'binary_0x{pt[0]:02x}{pt[1]:02x}'


def main():
    ap = argparse.ArgumentParser(description='EvoERP .DCY batch decryptor')
    ap.add_argument('--validate-only', action='store_true')
    ap.add_argument('--limit', type=int, default=None)
    ap.add_argument('--file', default=None)
    ap.add_argument('--out-dir', default=_DEFAULT_OUT)
    ap.add_argument('--iv-hex', default=None)
    args = ap.parse_args()

    # Load IV
    if args.iv_hex:
        iv = bytes.fromhex(args.iv_hex.replace(' ', ''))
    elif os.path.isfile(_DEFAULT_IV):
        iv = open(_DEFAULT_IV, 'rb').read()
    else:
        print(f'ERROR: {_DEFAULT_IV} not found.  Run get_iv_dcy_spawn.py first.')
        sys.exit(1)

    if len(iv) != 16:
        print(f'ERROR: IV must be 16 bytes, got {len(iv)}'); sys.exit(1)

    # Sanity check
    tf0 = Twofish(_KEY)
    K0  = tf0.encrypt(iv)
    xor4 = _le32(K0, 0) ^ _le32(K0, 4)
    if xor4 == _KNOWN_XOR:
        print(f'IV verified (XOR = 0x{xor4:08X})  OK')
    else:
        print(f'WARNING: IV XOR = 0x{xor4:08X}, expected 0x{_KNOWN_XOR:08X} -- may be wrong')
    print(f'IV: {iv.hex(" ")}')
    print()

    # Collect files
    if args.file:
        files = [args.file]
    else:
        print(f'Searching {_DCY_ROOTS} ...')
        files = _find_dcy(_DCY_ROOTS, limit=args.limit)
        if not files:
            print('No .DCY files found.'); sys.exit(1)
        print(f'Found {len(files)} .DCY files')
    print()

    if not args.validate_only:
        os.makedirs(args.out_dir, exist_ok=True)

    ok_count = fail_count = 0
    results  = []
    t0       = time.time()
    n        = len(files)

    for idx, fpath in enumerate(files, 1):
        bn = os.path.basename(fpath)
        try:
            data = open(fpath, 'rb').read()
        except Exception as e:
            print(f'[{idx:3d}/{n}] READ_ERROR  {bn}: {e}')
            results.append((fpath, 'READ_ERROR', 0, '-', str(e), None))
            fail_count += 1
            continue

        ok, pt, err = decrypt_dcy(data, iv)
        if ok:
            sniff = _sniff(pt)
            print(f'[{idx:3d}/{n}] OK    {bn}  ({len(data):,} B)  [{sniff}]')
            ok_count += 1
            results.append((fpath, 'OK', len(data), sniff, '', len(pt)))
            if not args.validate_only:
                out = os.path.join(args.out_dir, bn + '.dec')
                with open(out, 'wb') as f:
                    f.write(pt)
        else:
            print(f'[{idx:3d}/{n}] FAIL  {bn}: {err}')
            fail_count += 1
            results.append((fpath, 'FAIL', len(data), '-', err, None))

    elapsed = time.time() - t0
    print()
    print('=' * 60)
    print(f'  Processed : {n}')
    print(f'  OK        : {ok_count}')
    print(f'  FAIL      : {fail_count}')
    print(f'  Time      : {elapsed:.1f}s')
    if not args.validate_only and ok_count:
        print(f'  Output    : {args.out_dir}')
    print('=' * 60)

    if not args.validate_only:
        csv_path = os.path.join(args.out_dir, 'dcy_summary.csv')
        with open(csv_path, 'w', newline='', encoding='utf-8') as f:
            w = csv.writer(f)
            w.writerow(['path', 'status', 'size_bytes', 'content_sniff', 'error', 'pt_len'])
            for r in results:
                w.writerow(r)
        print(f'  Summary   : {csv_path}')


if __name__ == '__main__':
    main()
