#!/usr/bin/env python3
"""
scripts/verify_iv.py

Cross-checks the IV stored in scripts/iv_bytes.bin against known .RWN files.

Validation logic:
    - Decrypt first 8 bytes of each .RWN with the given IV and key.
    - The decrypted plaintext must satisfy pt[0:4] == pt[4:8].
    - This is the integrity check embedded in every .RWN by the TAS Pro 7 compiler.
    - All 20+ RWN files share the fixed ciphertext XOR: ct[0:4]^ct[4:8] = 0x3E0A37C5
      (equiv. ks[0:4]^ks[4:8] = 0x3E0A37C5 where ks = Encrypt(IV)).

Also tries the empirical keystream cross-check:
    - Encrypting the IV with the confirmed key should yield the first 16-byte
      keystream block ks1 = Twofish_Encrypt(key, IV).
    - Earlier analysis derived ks1 = 0f 73 76 7a a2 96 13 78 75 ea a2 2d 6f c6 4b 54
      from DCY/DFM pairs (consistent across 11 files).
    - If these match, the IV is doubly confirmed.

Usage:
    python scripts/verify_iv.py [path/to/iv_bytes.bin]

    Default IV path: scripts/iv_bytes.bin  (written by get_iv_frida.py)
    You can also pass IV bytes as a hex string:
        python scripts/verify_iv.py --hex "de ad be ef ..."
"""

import sys
import os
import hashlib
import struct

# Make sure twofish_pure is importable from this script's directory
_here = os.path.dirname(os.path.abspath(__file__))
if _here not in sys.path:
    sys.path.insert(0, _here)
from twofish_pure import Twofish, ofb_decrypt, cfb_decrypt

# ---------------------------------------------------------------------------
# Key (confirmed by disassembly)
# ---------------------------------------------------------------------------
_KEY = hashlib.sha1(b'mabufoju').digest() + b'\x00' * 4  # 24 bytes (192-bit)

# ---------------------------------------------------------------------------
# Known RWN files to test against (on-disk read-only)
# ---------------------------------------------------------------------------
_TEST_RWNS = [
    r'\\i2s109-solidcrm\DBAMFG$\T7INA.RWN',
    r'\\i2s109-solidcrm\DBAMFG$\EvoERPmenu.RWN',
    r'C:\ISTS\suwin7.rwn',
]
# First 8 bytes of T7INA.RWN (confirmed in analysis): F8 13 B6 7B 3D 24 BC 45
# XOR: C5 37 0A 3E → LE value 0x3E0A37C5 ✓
_KNOWN_XOR = 0x3E0A37C5

# Empirical ks1 from DCY/DFM XOR analysis (used for cross-check, may or may not match
# depending on whether DCY byte 0 is the validation block or an unencrypted header)
_EMPIRICAL_KS1 = bytes.fromhex('0f73767aa296137875eaa22d6fc64b54')


def _le32(b, off): return struct.unpack_from('<I', b, off)[0]


def check_validation_block(iv: bytes, ct8: bytes) -> tuple:
    """
    Decrypt 8-byte validation block using OFB mode.
    Returns (passed_ofb, passed_cfb, pt_ofb, pt_cfb).
    """
    # OFB: ks1 = Encrypt(IV); pt = ct XOR ks1[0:8]
    tf = Twofish(_KEY)
    ks1 = tf.encrypt(iv)
    pt_ofb = bytes(a ^ b for a, b in zip(ct8, ks1[:8]))
    passed_ofb = pt_ofb[:4] == pt_ofb[4:]

    # CFB: same first block (CFB and OFB are identical for the FIRST block)
    # After first block, CFB feeds ciphertext; OFB feeds keystream.
    # For the 8-byte validation check, both modes produce the same pt (same ks1).
    pt_cfb  = pt_ofb
    passed_cfb = passed_ofb

    return passed_ofb, passed_cfb, pt_ofb, pt_cfb, ks1


def verify(iv: bytes):
    print(f"IV         : {iv.hex(' ')}")
    print(f"Key        : {_KEY.hex(' ')}")
    print()

    # 1. Keystream XOR constraint
    tf   = Twofish(_KEY)
    ks1  = tf.encrypt(iv)
    xor4 = _le32(ks1, 0) ^ _le32(ks1, 4)
    print(f"ks1 = Encrypt(IV) = {ks1.hex(' ')}")
    print(f"ks1[0:4] ^ ks1[4:8] = 0x{xor4:08X}  (expected 0x{_KNOWN_XOR:08X})")
    xor_ok = (xor4 == _KNOWN_XOR)
    print(f"  → {'PASS ✓' if xor_ok else 'FAIL ✗  (IV is wrong, or XOR constant is wrong)'}")
    print()

    # 2. Empirical ks1 cross-check
    emp_match = (ks1 == _EMPIRICAL_KS1)
    print(f"Empirical ks1 (from DCY/DFM XOR): {_EMPIRICAL_KS1.hex(' ')}")
    print(f"Computed  ks1 (Encrypt(IV))      : {ks1.hex(' ')}")
    print(f"  → {'MATCH ✓' if emp_match else 'no match (expected if DCY validation offset differs)'}")
    print()

    # 3. Test against RWN files
    print("RWN file validation checks:")
    print("-" * 60)
    any_file_tested = False
    for path in _TEST_RWNS:
        if not os.path.isfile(path):
            print(f"  SKIP (not found): {path}")
            continue
        try:
            with open(path, 'rb') as f:
                ct8 = f.read(8)
        except PermissionError:
            print(f"  SKIP (no read access): {path}")
            continue

        if len(ct8) < 8:
            print(f"  SKIP (too small): {path}")
            continue

        any_file_tested = True
        # Validation block check (OFB and CFB give same result for first 8 bytes)
        ks1_check = tf.encrypt(iv)
        pt = bytes(a ^ b for a, b in zip(ct8, ks1_check[:8]))
        ct_xor = _le32(ct8, 0) ^ _le32(ct8, 4)
        passed  = (pt[:4] == pt[4:])

        print(f"  {os.path.basename(path)}")
        print(f"    ct[0:8]  = {ct8.hex(' ')}")
        print(f"    ct XOR   = 0x{ct_xor:08X}  (all files share 0x{_KNOWN_XOR:08X})")
        print(f"    pt[0:8]  = {pt.hex(' ')}")
        print(f"    pt[0:4] == pt[4:8]: {'YES → valid ✓' if passed else 'NO  → invalid ✗'}")
        print()

    if not any_file_tested:
        print("  (no RWN files found on expected paths)")
        print("  The network share or C:\\ISTS\\ may not be accessible.")
        print("  XOR constraint check above is the primary indicator.")

    # 4. Summary
    print("=" * 60)
    if xor_ok:
        print("RESULT: IV appears CORRECT (ks1 XOR constraint satisfied).")
        print("        Run rwn_decrypt.py to decrypt all .RWN files.")
    else:
        print("RESULT: IV does NOT satisfy the keystream XOR constraint.")
        print("        The IV is likely wrong, or block_buf was read too late")
        print("        (after it was updated by the first Encrypt call).")
        print()
        print("        FALLBACK: break at TDCP_blockcipher constructor instead:")
        print("          x64dbg: bp 0x74EE30  (constructor entry, file 0x34E230)")
        print("          Read [EAX+0x3C] there — immediately after GetMem.")


def main():
    # Parse args
    iv = None
    args = sys.argv[1:]

    if args and args[0] == '--hex':
        if len(args) < 2:
            print("Usage: verify_iv.py --hex \"de ad be ef ...\"")
            sys.exit(1)
        hex_str = args[1].replace(' ', '')
        iv = bytes.fromhex(hex_str)
    else:
        iv_path = args[0] if args else os.path.join(_here, 'iv_bytes.bin')
        if not os.path.isfile(iv_path):
            print(f"ERROR: IV file not found: {iv_path}")
            print("Run get_iv_frida.py first, or use --hex to supply bytes manually.")
            sys.exit(1)
        iv = open(iv_path, 'rb').read()

    if len(iv) != 16:
        print(f"ERROR: IV must be 16 bytes, got {len(iv)}.")
        sys.exit(1)

    verify(iv)


if __name__ == '__main__':
    main()
