"""
rwn_validate.py - Test the candidate passphrase against T7INA.RWN.

Known plaintext: decrypted offset 0xC5-0xC9 (= file offset 0xD5-0xD9) must be "TAS32".
File layout: bytes 0-15 = header (possible IV), encrypted data starts at byte 16.

Tries all combinations of:
  key lengths: 128-bit (16 bytes), 192-bit (24 bytes), 256-bit (32 bytes)
  modes: ECB, CBC (IV = file bytes 0-15), OFB, CFB-128
"""
import hashlib
import struct
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from twofish_pure import Twofish, cbc_decrypt, ecb_decrypt, ofb_decrypt, cfb_decrypt

PASSPHRASE = "mabufoju"  # confirmed: hardcoded in tp7runtime.exe at file offset 0x75D154
TARGET = b"TAS32"
ENCRYPTED_START = 0x10      # encrypted payload starts at byte 16
DECRYPT_OFFSET  = 0xC5      # target string position in the decrypted payload

def sha1_key(passphrase: str, key_bytes: int) -> bytes:
    raw = hashlib.sha1(passphrase.encode('latin-1')).digest()  # 20 bytes
    return (raw + b'\x00' * key_bytes)[:key_bytes]

def check(label: str, plaintext: bytes) -> bool:
    found = plaintext[DECRYPT_OFFSET:DECRYPT_OFFSET + 5]
    if found == TARGET:
        print(f"  *** HIT: {label} -> TAS32 at decrypted offset 0x{DECRYPT_OFFSET:X} ***")
        return True
    # Also show what we got for debugging
    print(f"  {label}: offset 0x{DECRYPT_OFFSET:X} = {found.hex()} ({found!r})")
    return False

def main():
    rwn_path = os.path.join(os.path.dirname(__file__), '..', 'samples', 'rosetta', 'T7INA.RWN')
    rwn_path = os.path.normpath(rwn_path)
    with open(rwn_path, 'rb') as f:
        data = f.read(0x1000)  # read first 4 KB — more than enough for offset 0xD5

    header = data[:ENCRYPTED_START]
    iv     = data[:16]          # first 16 bytes as IV for CBC/OFB/CFB
    payload = data[ENCRYPTED_START:]

    print(f"RWN header (hex): {header.hex()}")
    print(f"File byte 0xD5-0xD9 (encrypted): {data[0xD5:0xDA].hex()}")
    print(f"Passphrase SHA1: {hashlib.sha1(PASSPHRASE.encode('latin-1')).hexdigest()}")
    print()

    found_any = False
    for key_bits in (128, 192, 256):
        key_bytes = key_bits // 8
        key = sha1_key(PASSPHRASE, key_bytes)
        print(f"Key ({key_bits}-bit): {key.hex()}")

        try:
            # ECB
            pt = ecb_decrypt(key, payload)
            if check(f"ECB-{key_bits}", pt): found_any = True

            # CBC with IV = file bytes 0-15
            pt = cbc_decrypt(key, iv, payload)
            if check(f"CBC-{key_bits} IV=file[0:16]", pt): found_any = True

            # OFB with IV = file bytes 0-15
            pt = ofb_decrypt(key, iv, payload)
            if check(f"OFB-{key_bits} IV=file[0:16]", pt): found_any = True

            # CFB-128 with IV = file bytes 0-15
            pt = cfb_decrypt(key, iv, payload)
            if check(f"CFB128-{key_bits} IV=file[0:16]", pt): found_any = True

            # Also try zero IV (in case IV is not from the header)
            zero_iv = bytes(16)
            pt = cbc_decrypt(key, zero_iv, payload)
            if check(f"CBC-{key_bits} IV=zeros", pt): found_any = True

            pt = ofb_decrypt(key, zero_iv, payload)
            if check(f"OFB-{key_bits} IV=zeros", pt): found_any = True

        except Exception as e:
            print(f"  Error ({key_bits}-bit): {e}")

        print()

    if not found_any:
        print("No match found. Passphrase may be wrong, or mode/offset differs from expectation.")
        print("\nTrying alternate data offsets:")
        # Try if encrypted data starts at byte 8
        payload8 = data[8:]
        iv8 = data[:16]
        key = sha1_key(PASSPHRASE, 16)
        # If start=8, TAS32 should be at decrypted offset 0xC5 in payload8, which is
        # data[8 + 0xC5] = data[0xCD]
        for mode_fn, label in [(cbc_decrypt, "CBC"), (ecb_decrypt, "ECB"), (ofb_decrypt, "OFB")]:
            try:
                if mode_fn == ecb_decrypt:
                    pt = mode_fn(key, payload8)
                else:
                    pt = mode_fn(key, iv8, payload8)
                found = pt[0xC5:0xCA]
                print(f"  128-bit {label} start=8: offset 0xC5 = {found.hex()} ({found!r})")
                if found == TARGET:
                    print(f"  *** HIT: encrypted start at byte 8, {label}-128 ***")
            except Exception as e:
                print(f"  Error: {e}")

if __name__ == '__main__':
    main()
