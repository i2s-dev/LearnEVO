"""
rwn_scan.py - Broad-spectrum scan to locate "TAS" signature in decrypted T7INA.RWN.

Tries:
  - Multiple key derivations: SHA1, MD5, SHA256 (all zero-padded to key size)
  - Key lengths: 128, 192, 256-bit
  - Modes: ECB, CBC (IV=zeros, IV=file[0:16], IV=file[16:32]), OFB, CFB-128
  - Encrypted-data start offsets: 0, 8, 16, 32, 64, 128
  - Searches the entire decrypted buffer for the bytes "TAS" (and specifically "TAS32")

Reports any hit.
"""
import hashlib
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from twofish_pure import Twofish, cbc_decrypt, ecb_decrypt, ofb_decrypt, cfb_decrypt

PASSPHRASE = "mabufoju"  # confirmed: hardcoded in tp7runtime.exe at file offset 0x75D154

def sha1_key(n): return (hashlib.sha1(PASSPHRASE.encode('latin-1')).digest() + b'\x00'*n)[:n]
def md5_key(n):  return (hashlib.md5(PASSPHRASE.encode('latin-1')).digest()  + b'\x00'*n)[:n]
def sha256_key(n): return (hashlib.sha256(PASSPHRASE.encode('latin-1')).digest() + b'\x00'*n)[:n]

KEY_FNS = [('SHA1', sha1_key), ('MD5', md5_key), ('SHA256', sha256_key)]
KEY_LENS = [16, 24, 32]
START_OFFSETS = [0, 8, 16, 32, 64, 128]

# What we're looking for
TARGET_EXACT = b'TAS32'
TARGET_PREFIX = b'TAS'

def try_decrypt(mode_label, key, iv, payload):
    """Returns decrypted bytes or None on error."""
    try:
        if mode_label == 'ECB':
            return ecb_decrypt(key, payload)
        elif mode_label.startswith('CBC'):
            return cbc_decrypt(key, iv, payload)
        elif mode_label == 'OFB':
            return ofb_decrypt(key, iv, payload)
        elif mode_label == 'CFB':
            return cfb_decrypt(key, iv, payload)
    except Exception:
        return None
    return None

def scan(pt: bytes, label: str):
    """Scan decrypted output for TAS-family signatures."""
    idx = 0
    found = False
    while True:
        pos = pt.find(TARGET_PREFIX, idx)
        if pos < 0:
            break
        snippet = pt[pos:pos+8]
        print(f"  HIT {label}: 'TAS' at dec_offset 0x{pos:X} -> {snippet!r}")
        found = True
        idx = pos + 1
    return found

def main():
    rwn_path = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'samples', 'rosetta', 'T7INA.RWN'))
    with open(rwn_path, 'rb') as f:
        data = f.read(0x2000)  # read first 8 KB

    print(f"File: {rwn_path}")
    print(f"First 32 bytes: {data[:32].hex()}")
    print(f"SHA1(passphrase): {hashlib.sha1(PASSPHRASE.encode('latin-1')).hexdigest()}")
    print()

    any_hit = False

    for start in START_OFFSETS:
        if start >= len(data):
            continue
        payload = data[start:]
        # Trim to multiple of 16
        payload = payload[:len(payload) - len(payload) % 16]
        if len(payload) < 16:
            continue

        iv_zeros = bytes(16)
        iv_file0 = data[0:16]
        iv_file1 = data[16:32] if len(data) >= 32 else iv_zeros

        for hash_name, key_fn in KEY_FNS:
            for key_len in KEY_LENS:
                key = key_fn(key_len)

                modes = [
                    ('ECB', iv_zeros),
                    ('CBC', iv_zeros),
                    ('CBC', iv_file0),
                    ('CBC', iv_file1),
                    ('OFB', iv_zeros),
                    ('OFB', iv_file0),
                    ('CFB', iv_zeros),
                    ('CFB', iv_file0),
                ]

                for mode, iv in modes:
                    pt = try_decrypt(mode, key, iv, payload)
                    if pt is None or len(pt) < 0x40:
                        continue
                    if TARGET_PREFIX in pt:
                        iv_label = 'iv=0' if iv == iv_zeros else ('iv=file0' if iv == iv_file0 else 'iv=file1')
                        label = f"start=0x{start:X} {hash_name}-{key_len*8} {mode} {iv_label}"
                        any_hit = scan(pt, label)

    if not any_hit:
        print("No 'TAS' found in any combination.")
        print()
        # Show what we DO get at offset 0x35 and 0xC5 for the most likely combo (SHA1-128 ECB, no header)
        key = sha1_key(16)
        for start in [0, 16]:
            payload = data[start:]
            payload = payload[:len(payload) - len(payload) % 16]
            pt = try_decrypt('ECB', key, iv_zeros, payload)
            if pt:
                print(f"ECB SHA1-128 start=0x{start:X}: offset 0x35 = {pt[0x35:0x40].hex()!r}")
                print(f"ECB SHA1-128 start=0x{start:X}: offset 0xC5 = {pt[0xC5:0xD0].hex()!r}")

if __name__ == '__main__':
    main()
