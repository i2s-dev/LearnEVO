#!/usr/bin/env python3
"""
scripts/dcy_decrypt.py

Batch decryptor for EvoERP .DCY (data dictionary) files.

CIPHER PARAMETERS (confirmed 2026-06-16 via live Frida capture + Python verification)
---------------------------------------------------------------------------------------
  Algorithm  : Twofish-192, CFB-128 mode
  Key        : K_D = 691e8041ab265b4e6ee052ccc946dba4caac60da (raw 20 bytes)
               K_D_192 = K_D + 00000000 (24 bytes)
  IV param   : always 0  →  P_initial = Encrypt_K(all-zeros block)
  Body P_start: K0 = Encrypt_K(P_initial)  — NOT P_initial itself
  Validation : header_pt[0:4] == header_pt[4:8]

Verified: K_D decrypts MDUMMY.DCY → "object EditForm1: TEditForm1..." ✓

Per-file decryption (see docs/02-file-formats/decryption-findings.md):
  tf        = Twofish(K_D_192)
  P_initial = tf.encrypt(bytes(16))
  K0        = tf.encrypt(P_initial)
  header_pt = header_ct XOR K0[0:8]
  assert header_pt[0:4] == header_pt[4:8]
  P = K0
  for each 16-byte body block:
      K = tf.encrypt(P)
      pt_block = ct_block XOR K
      P = ct_block  (CFB-128 feedback)

Note on suwin*.DCY files: 7 of 48 files use a different format (unknown key/IV).
They will fail validation — this is expected.

USAGE
-----
    python scripts/dcy_decrypt.py                      # all .DCY files from share
    python scripts/dcy_decrypt.py --validate-only      # check only, no output
    python scripts/dcy_decrypt.py --limit 10           # spot-check
    python scripts/dcy_decrypt.py --file PATH.DCY      # single file
    python scripts/dcy_decrypt.py --out-dir DIR        # override output dir
"""

import sys, os, struct, csv, argparse, time

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

_here = os.path.dirname(os.path.abspath(__file__))
_repo = os.path.dirname(_here)
sys.path.insert(0, _here)
from twofish_pure import Twofish

# ---------------------------------------------------------------------------
# Key constants (confirmed 2026-06-16)
# ---------------------------------------------------------------------------
_K_D_RAW  = bytes.fromhex('691e8041ab265b4e6ee052ccc946dba4caac60da')
_KEY      = _K_D_RAW + b'\x00' * 4    # 24 bytes (192-bit Twofish key)

_DCY_ROOTS   = [r'\\i2s109-solidcrm\DBAMFG$']
_DEFAULT_OUT = os.path.join(_repo, 'samples', 'dcy_decrypted')
_KNOWN_XOR   = 0x0955DC84    # le32(K0,0) XOR le32(K0,4) for K_D


def _le32(b, off):
    return struct.unpack_from('<I', b, off)[0]


# ---------------------------------------------------------------------------
# Core decryption
# ---------------------------------------------------------------------------

def decrypt_dcy(data: bytes, key: bytes = _KEY) -> tuple:
    """
    Decrypt a .DCY file.  Returns (ok, plaintext, error_msg).
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

    # Body — CFB-128, P starts at K0
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
    printable = sum(1 for b in pt[:128] if 0x20 <= b < 0x7F or b in (9, 10, 13))
    if printable > 100:
        return 'text'
    try:
        head = pt[:256].decode('latin-1')
        if 'object ' in head or 'TForm' in head or 'TEdit' in head:
            return 'delphi_form'
    except Exception:
        pass
    if pt[0:4] == pt[4:8]:
        return f'dcy_hdr_0x{pt[0:4].hex()}'
    return f'binary_0x{pt[0]:02x}{pt[1]:02x}'


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description='EvoERP .DCY batch decryptor (K_D key, P_start=K0)')
    ap.add_argument('--validate-only', action='store_true')
    ap.add_argument('--limit', type=int, default=None)
    ap.add_argument('--file', default=None)
    ap.add_argument('--out-dir', default=_DEFAULT_OUT)
    ap.add_argument('--roots', nargs='+', default=_DCY_ROOTS)
    args = ap.parse_args()

    # Confirm K0 constant at startup
    tf0    = Twofish(_KEY)
    P_init = tf0.encrypt(bytes(16))
    K0     = tf0.encrypt(P_init)
    xor4   = _le32(K0, 0) ^ _le32(K0, 4)
    if xor4 == _KNOWN_XOR:
        print(f'K_D verified: K0 XOR = 0x{xor4:08X}  OK')
    else:
        print(f'WARNING: K0 XOR = 0x{xor4:08X}, expected 0x{_KNOWN_XOR:08X}')
    print(f'K_D raw: {_K_D_RAW.hex()}')
    print(f'K0:      {K0.hex()}')
    print()

    # Collect files
    if args.file:
        files = [args.file]
    else:
        roots = args.roots
        print(f'Searching {roots} ...')
        files = _find_dcy(roots, limit=args.limit)
        if not files:
            print('No .DCY files found.'); sys.exit(1)
        print(f'Found {len(files)} .DCY files')
        if args.limit:
            print(f'(limited to {args.limit})')
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

        ok, pt, err = decrypt_dcy(data)
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
    print(f'  FAIL      : {fail_count}  (suwin*.DCY use different format — expected)')
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
