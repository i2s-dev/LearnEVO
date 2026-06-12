#!/usr/bin/env python3
"""
scripts/rwn_decrypt.py

Batch-decrypts all .RWN and .DCY files on the network share using the IV
extracted by get_iv_frida.py (stored in scripts/iv_bytes.bin).

CIPHER DETAILS (all confirmed by disassembly of tp7runtime.exe)
    Algorithm : Twofish, 128-bit block
    Key size  : 192-bit (24 bytes)
    Mode      : OFB-like (DCPcrypt's "CFB mode=2" uses keystream output feedback)
    Passphrase: 'mabufoju'  (hardcoded at file offset 0x75D154)
    Key       : SHA1('mabufoju')[0:20] + 0x00*4
    IV        : block_buf at cipher+0x3C (uninitialized heap; read by get_iv_frida.py)

FILE LAYOUT
    .RWN:
        bytes  0-7  : validation block (Encrypt(IV)[0:8] XOR'd with known sentinel;
                       decrypted pt[0:4] must equal pt[4:8])
        bytes  8-N  : TAS Pro 7 bytecode (OFB-decrypted continuation)
    .DCY:
        same encryption model; decrypted content is Delphi VCL form text

USAGE
    python scripts/rwn_decrypt.py [options]

    Options:
      --iv PATH         IV file (default: scripts/iv_bytes.bin)
      --src DIR         Source directory to scan (default: network share root)
      --out DIR         Output directory for decrypted files (default: samples/rwn_decrypted/)
      --file FILE       Decrypt a single file instead of batch mode
      --mode {ofb,cfb}  Force a specific mode (default: try OFB, fall back to CFB)
      --validate-only   Only check validation blocks; do not write output files
      --limit N         Stop after N files (for testing)

NOTES
    - Read-only access to the network share is enforced by scope rules (CLAUDE.md §1).
    - All output lands in the workspace under samples/rwn_decrypted/.
    - Decrypted bytecode is raw TAS Pro 7 virtual machine instructions.
      Further analysis requires the .RUN Rosetta Stone opcode mapping.
    - If validation fails for all files with the IV from iv_bytes.bin,
      run verify_iv.py to diagnose.

PREREQUISITES
    1. Run get_iv_frida.py (or x64dbg_get_iv.txt) to populate iv_bytes.bin.
    2. Network share \\\\i2s109-solidcrm\\DBAMFG$\\ must be accessible (read-only).
"""

import sys
import os
import hashlib
import struct
import argparse
import glob

_here = os.path.dirname(os.path.abspath(__file__))
if _here not in sys.path:
    sys.path.insert(0, _here)
from twofish_pure import Twofish

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
_KEY = hashlib.sha1(b'mabufoju').digest() + b'\x00' * 4  # 24-byte 192-bit key

_SHARE_ROOT  = r'\\i2s109-solidcrm\DBAMFG$'
_DEFAULT_OUT = os.path.join(os.path.dirname(_here), 'samples', 'rwn_decrypted')

# Expected keystream XOR for validation block (all RWN files share this)
_EXPECTED_XOR = 0x3E0A37C5


# ---------------------------------------------------------------------------
# Decryption core
# ---------------------------------------------------------------------------
def _ofb_decrypt(tf: Twofish, iv: bytes, data: bytes) -> bytes:
    """
    OFB (output feedback) decryption.
    Matches DCPcrypt TDCP_blockcipher mode=2 behaviour:
      ks = Encrypt(IV); pt = ct XOR ks; next IV = ks (not ct)
    """
    out = bytearray()
    ks  = iv
    for i in range(0, len(data), 16):
        ks    = tf.encrypt(ks)
        chunk = data[i:i + 16]
        for j in range(min(16, len(chunk))):
            out.append(chunk[j] ^ ks[j])
    return bytes(out)


def _cfb_decrypt(tf: Twofish, iv: bytes, data: bytes) -> bytes:
    """
    Standard CFB-128 decryption (feedback = ciphertext block).
    Tried as fallback if OFB validation fails.
    """
    out  = bytearray()
    prev = iv
    for i in range(0, len(data), 16):
        ks    = tf.encrypt(prev)
        chunk = data[i:i + 16]
        pt    = bytes(chunk[j] ^ ks[j] for j in range(min(16, len(chunk))))
        out  += pt
        prev  = bytes(chunk) + bytes(16 - len(chunk))  # pad for short last block
    return bytes(out)


def _check_validation(pt8: bytes) -> bool:
    return pt8[:4] == pt8[4:]


def decrypt_file(path: str, iv: bytes, mode: str = 'auto') -> tuple:
    """
    Decrypt a single .RWN or .DCY file.
    Returns (plaintext_bytes, mode_used, validation_passed).
    plaintext_bytes includes the 8-byte validation block at the start;
    actual bytecode starts at offset 8.
    """
    with open(path, 'rb') as f:
        data = f.read()

    if len(data) < 8:
        return None, None, False

    tf   = Twofish(_KEY)
    ks1  = tf.encrypt(iv)

    # Validation block check (same for OFB and CFB — only first 8 bytes differ by mode
    # after the first 16-byte block, but the validation uses only the first block's ks1)
    pt8_ofb = bytes(data[i] ^ ks1[i] for i in range(8))
    val_ofb = _check_validation(pt8_ofb)

    if mode == 'ofb' or (mode == 'auto' and val_ofb):
        plaintext = _ofb_decrypt(tf, iv, data)
        return plaintext, 'ofb', val_ofb

    if mode == 'cfb' or mode == 'auto':
        # CFB and OFB are identical for the first 16-byte block;
        # the distinction only matters for blocks 2+ of the body.
        # For validation, OFB and CFB give the same result.
        # Try CFB for body decryption if mode was forced.
        plaintext = _cfb_decrypt(tf, iv, data)
        return plaintext, 'cfb', val_ofb

    return _ofb_decrypt(tf, iv, data), 'ofb', val_ofb


def _le32(b, off): return struct.unpack_from('<I', b, off)[0]


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(description='Decrypt EvoERP .RWN and .DCY files')
    parser.add_argument('--iv',            default=os.path.join(_here, 'iv_bytes.bin'),
                        help='Path to IV file (16 bytes, from get_iv_frida.py)')
    parser.add_argument('--src',           default=_SHARE_ROOT,
                        help='Source directory to scan for .RWN and .DCY files')
    parser.add_argument('--out',           default=_DEFAULT_OUT,
                        help='Output directory for decrypted files')
    parser.add_argument('--file',          default=None,
                        help='Decrypt a single file')
    parser.add_argument('--mode',          choices=['ofb', 'cfb', 'auto'], default='auto',
                        help='Cipher mode (default: auto-detect via validation block)')
    parser.add_argument('--validate-only', action='store_true',
                        help='Check validation blocks only; do not write files')
    parser.add_argument('--limit',         type=int, default=None,
                        help='Stop after N files')
    args = parser.parse_args()

    # Load IV
    if not os.path.isfile(args.iv):
        print(f"ERROR: IV file not found: {args.iv}")
        print("Run get_iv_frida.py first, or use x64dbg_get_iv.txt.")
        sys.exit(1)
    iv = open(args.iv, 'rb').read()
    if len(iv) != 16:
        print(f"ERROR: IV must be 16 bytes, got {len(iv)}.")
        sys.exit(1)

    print(f"IV  : {iv.hex(' ')}")
    print(f"Key : {_KEY.hex(' ')}")
    print()

    # Quick validation sanity check
    tf   = Twofish(_KEY)
    ks1  = tf.encrypt(iv)
    xor4 = _le32(ks1, 0) ^ _le32(ks1, 4)
    print(f"Keystream XOR check: ks1[0:4]^ks1[4:8] = 0x{xor4:08X}  "
          f"(expected 0x{_EXPECTED_XOR:08X}) "
          f"{'✓' if xor4 == _EXPECTED_XOR else '✗ MISMATCH — IV may be wrong'}")
    print()

    # Single-file mode
    if args.file:
        if not os.path.isfile(args.file):
            print(f"ERROR: file not found: {args.file}")
            sys.exit(1)
        plaintext, mode_used, valid = decrypt_file(args.file, iv, args.mode)
        print(f"File   : {args.file}")
        print(f"Mode   : {mode_used}")
        print(f"Valid  : {'PASS ✓' if valid else 'FAIL ✗'}")
        if plaintext:
            print(f"Size   : {len(plaintext)} bytes decrypted ({len(plaintext)-8} body bytes)")
            if not args.validate_only:
                os.makedirs(args.out, exist_ok=True)
                out_path = os.path.join(args.out, os.path.basename(args.file) + '.dec')
                with open(out_path, 'wb') as f:
                    f.write(plaintext[8:])   # skip 8-byte validation header
                print(f"Output : {out_path}")
                print(f"  (first 32 bytes of body: {plaintext[8:40].hex(' ')})")
        return

    # Batch mode
    if not os.path.isdir(args.src):
        print(f"ERROR: source directory not found: {args.src}")
        print("Make sure the network share is accessible.")
        sys.exit(1)

    if not args.validate_only:
        os.makedirs(args.out, exist_ok=True)
        print(f"Output dir: {args.out}")

    patterns = [
        os.path.join(args.src, '*.RWN'),
        os.path.join(args.src, '*.rwn'),
        os.path.join(args.src, '*.DCY'),
        os.path.join(args.src, '*.dcy'),
        os.path.join(args.src, 'DFM', '*.RWN'),
    ]
    files = []
    for pat in patterns:
        files.extend(glob.glob(pat))
    files = sorted(set(files))

    if args.limit:
        files = files[:args.limit]

    print(f"Files found : {len(files)} (.RWN + .DCY)")
    print()

    ok = 0; fail = 0; skipped = 0
    for path in files:
        try:
            plaintext, mode_used, valid = decrypt_file(path, iv, args.mode)
        except Exception as e:
            print(f"  ERROR  {os.path.basename(path)}: {e}")
            skipped += 1
            continue

        status = 'PASS' if valid else 'FAIL'
        if valid:
            ok += 1
        else:
            fail += 1

        print(f"  {status}  [{mode_used}]  {os.path.basename(path)}"
              f"  ({len(plaintext)} bytes)")

        if valid and not args.validate_only and plaintext:
            rel   = os.path.relpath(path, args.src)
            out_p = os.path.join(args.out, rel + '.dec')
            os.makedirs(os.path.dirname(out_p), exist_ok=True)
            with open(out_p, 'wb') as f:
                f.write(plaintext[8:])   # strip 8-byte validation header

    print()
    print("=" * 50)
    print(f"  PASS   : {ok}")
    print(f"  FAIL   : {fail}")
    print(f"  SKIPPED: {skipped}")
    print(f"  TOTAL  : {ok+fail+skipped}")
    print("=" * 50)

    if fail > 0 and ok == 0:
        print()
        print("All files failed validation.  Likely causes:")
        print("  1. The IV in iv_bytes.bin was read at the wrong point")
        print("     (block_buf may have been updated before the breakpoint).")
        print("  2. Try breaking at the CONSTRUCTOR instead: VA 0x74EE30")
        print("     Read [EAX+0x3C] there (immediately after GetMem).")
        print("  3. Run verify_iv.py for more details.")


if __name__ == '__main__':
    main()
