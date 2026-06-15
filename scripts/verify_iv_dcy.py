#!/usr/bin/env python3
"""
scripts/verify_iv_dcy.py

Verify that iv_dcy_bytes.bin correctly decrypts a .DCY file header.
Usage:  python scripts/verify_iv_dcy.py [path_to_dcy_file]
        python scripts/verify_iv_dcy.py --hex "xx xx xx ..."
"""
import sys
import os
import struct
import hashlib

_here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _here)
from twofish_pure import Twofish

KEY = hashlib.sha1(b'mabufoju').digest() + b'\x00' * 4

# A known .DCY file on the network share (read-only)
DEFAULT_DCY = r'\\i2s109-solidcrm\DBAMFG$\BKWOMSTR.DCY'


def decrypt_block(iv_bytes: bytes, ct: bytes) -> bytes:
    tf  = Twofish(KEY)
    ks  = tf.encrypt(iv_bytes)
    pt0 = bytes(a ^ b for a, b in zip(ct[:16], ks))
    return pt0


def main():
    # Parse args
    iv_hex = None
    dcy_path = DEFAULT_DCY

    args = sys.argv[1:]
    i = 0
    while i < len(args):
        if args[i] == '--hex' and i + 1 < len(args):
            iv_hex = bytes(int(x, 16) for x in args[i+1].split())
            i += 2
        else:
            dcy_path = args[i]
            i += 1

    # Load IV
    if iv_hex:
        IV = iv_hex
        print(f"IV (from --hex): {IV.hex(' ')}")
    else:
        iv_path = os.path.join(_here, 'iv_dcy_bytes.bin')
        if not os.path.exists(iv_path):
            print(f"ERROR: {iv_path} not found.  Run get_iv_dcy_frida.py first.")
            sys.exit(1)
        with open(iv_path, 'rb') as f:
            IV = f.read(16)
        print(f"IV (from iv_dcy_bytes.bin): {IV.hex(' ')}")

    if len(IV) != 16:
        print(f"ERROR: IV must be 16 bytes, got {len(IV)}")
        sys.exit(1)

    # Read first 16 bytes of a .DCY file
    print(f"DCY file: {dcy_path}")
    try:
        with open(dcy_path, 'rb') as f:
            ct = f.read(16)
    except FileNotFoundError:
        print(f"ERROR: Cannot open {dcy_path}")
        print("       Pass a different .DCY path as argument.")
        sys.exit(1)

    if len(ct) < 16:
        print(f"ERROR: File too short ({len(ct)} bytes)")
        sys.exit(1)

    print(f"CT[0:16]: {ct.hex(' ')}")

    pt = decrypt_block(IV, ct)
    print(f"PT[0:16]: {pt.hex(' ')}")

    w0 = struct.unpack_from('<I', pt, 0)[0]
    w1 = struct.unpack_from('<I', pt, 4)[0]
    ok = (w0 == w1)

    print()
    print(f"PT[0:4] = 0x{w0:08X}")
    print(f"PT[4:8] = 0x{w1:08X}")
    print(f"Validation (PT[0:4]==PT[4:8]): {'PASS' if ok else 'FAIL'}")

    if ok:
        print()
        print("=" * 50)
        print("  DCY IV VERIFIED CORRECT")
        print(f"  IV = {IV.hex(' ')}")
        print("=" * 50)
    else:
        print()
        print("FAIL: IV does not decrypt this .DCY file correctly.")
        print("      The IV may be file-specific (not global) — try another .DCY.")


if __name__ == '__main__':
    main()
