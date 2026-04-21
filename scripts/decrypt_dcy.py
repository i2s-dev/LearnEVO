"""
Partial decryption of EvoERP / TAS Pro 7 encrypted files (.RWN / .DCY).

What we can do:
  (a) **Decrypt the first 16 bytes (block 0) of any file.** We derived the
      first-block keystream from known-plaintext DFM/DCY pairs. This tells
      us how each encrypted file begins.
  (b) **Decrypt entire DCY files that have a matching plaintext DFM on
      the share.** Thirteen such pairs exist. We extract the full
      per-file keystream and use it to "verify" or reconstruct the DCY's
      original DFM content.

What we cannot do (yet):
  (c) Decrypt .RWN (compiled TAS program) files past byte 16 — subsequent
      blocks in Twofish-CFB mode depend on the ciphertext of the prior
      block, which in turn encodes unknown plaintext. Without the key,
      we can't compute those further keystream blocks.

Background:
  - Cipher: Twofish (16-byte block) in CFB mode, via DCPcrypt library.
  - Keystream block 0: `0f 73 76 7a a2 96 13 78 75 ea a2 2d 6f c6 4b 54`.
  - IV: zero block (inferred from CFB-mode behaviour across files).
  - Key: UNKNOWN. Must be 16 / 24 / 32 bytes for Twofish. Brute-forced
    against every printable string and registered class name inside
    `tp7runtime.exe` (474k candidates), and every high-entropy 16-byte
    window inside the encrypt-related code regions — no match.

Usage:
    python decrypt_dcy.py block0  <file>        # decrypt first 16 bytes
    python decrypt_dcy.py diff    <file> <dfm>  # derive full per-file keystream

See docs/02-file-formats/decryption-findings.md for the full story.
"""
import sys
from pathlib import Path

# Empirically derived first keystream block (Twofish(K, IV=0) where K is
# the runtime-compiled-in passphrase hash). Works for every .RWN and .DCY
# on the share tested.
STREAM_0 = bytes.fromhex('0f73767aa296137875eaa22d6fc64b54')


def decrypt_block0(path: Path) -> bytes:
    data = path.read_bytes()
    if len(data) < 24:
        raise ValueError("file too short — needs at least 8-byte salt + 16-byte block")
    cipher_block = data[8:24]
    return bytes(c ^ k for c, k in zip(cipher_block, STREAM_0))


def derive_keystream(dcy_path: Path, dfm_path: Path) -> bytes:
    """For a DCY with a known-plaintext DFM counterpart, return the full
    per-file keystream. All DCYs encrypt DFM_size bytes."""
    dcy = dcy_path.read_bytes()
    dfm = dfm_path.read_bytes()
    n = min(len(dcy) - 8, len(dfm))
    return bytes(dcy[8 + i] ^ dfm[i] for i in range(n))


def cmd_block0(path):
    p = Path(path)
    try:
        plain = decrypt_block0(p)
    except Exception as e:
        print(f"ERR: {p.name}: {e}", file=sys.stderr)
        return 2
    printable = "".join(chr(b) if 32 <= b < 127 else "." for b in plain)
    print(f"{p.name}  bytes 0..15 (plaintext):")
    print(f"  hex:   {plain.hex()}")
    print(f"  ascii: {printable}")
    return 0


def cmd_diff(dcy, dfm):
    ks = derive_keystream(Path(dcy), Path(dfm))
    print(f"Per-file keystream derived ({len(ks)} bytes): {ks[:64].hex()}...")
    # Check that block-0 keystream matches the global Stream[0] we already have
    matches = ks[:16] == STREAM_0
    print(f"Block-0 keystream matches global Stream[0]: {matches}")
    if not matches:
        print("WARNING: DCY and DFM may not correspond (different versions).")
    return 0 if matches else 1


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    cmd = sys.argv[1]
    if cmd == "block0" and len(sys.argv) == 3:
        return cmd_block0(sys.argv[2])
    elif cmd == "diff" and len(sys.argv) == 4:
        return cmd_diff(sys.argv[2], sys.argv[3])
    else:
        print(__doc__)
        return 2


if __name__ == "__main__":
    sys.exit(main())
