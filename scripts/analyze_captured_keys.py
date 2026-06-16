#!/usr/bin/env python3
"""
Analyze the keys captured live by frida_capture_key_and_iv.py.

FINDINGS:
  key_bits = 160 for ALL SetKey calls (not 192).
  The actual runtime key for RWN cipher ≠ sha1("mabufoju").

This script:
  1. Tests which padding (192 or 256-bit) makes Twofish(K_B).encrypt(zeros) == IV_rwn
  2. Identifies which key is DCY vs RWN
  3. Attempts DCY decryption with correct key
"""
import sys, os, struct, hashlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from twofish_pure import Twofish

# --- Live-captured keys (first 20 bytes = SHA1 hash of actual passphrase) ---
# key_bits=160 means ECX=160; first 20 bytes are the actual key material
K_A_raw = bytes.fromhex('d97f05679438037073c30628734764020859f77e')  # calls #1,5,8,10
K_B_raw = bytes.fromhex('a898d21e2fd6ca294026e5d633d9047f91f7ed35')  # calls #2,7,9
K_C_raw = bytes.fromhex('fdc2883f6d6537dd667270406d0a4c85969295ac')  # call #3
K_D_raw = bytes.fromhex('691e8041ab265b4e6ee052ccc946dba4caac60da')  # calls #4,6

# From EncryptBlock output right after each SetKey (= Encrypt(K, zeros) = P_initial):
P_init_A = bytes.fromhex('1d2d4abbf61b016b8e00ba5ce87cdcfe')  # after SetKey#1 (K_A)
P_init_B = bytes.fromhex('0e6fbff653a28a70d102874c6b1825ad')  # after SetKey#2 (K_B)

# Known constants
IV_rwn   = bytes.fromhex('0e6fbff653a28a70d102874c6b1825ad')
IV_dcy_old = bytes.fromhex('cd47af18e0d1c38cf1d8a067fc3dda28')  # derived with WRONG key

print("=" * 65)
print("STEP 1: Verify padding scheme using K_B (RWN cipher confirmed)")
print("=" * 65)
print(f"P_init_B from live capture: {P_init_B.hex()}")
print(f"IV_rwn (known):             {IV_rwn.hex()}")
print(f"Match: {P_init_B == IV_rwn}")
print()

for pad_bytes, label in [
    (b'\x00' * 4,  '192-bit (K_B + 4 zeros)'),
    (b'\x00' * 12, '256-bit (K_B + 12 zeros)'),
    (b'\x00' * 4 + K_B_raw[:8],  '192-bit then extend'),
]:
    key = K_B_raw + pad_bytes
    if len(key) not in (16, 24, 32):
        continue
    try:
        tf = Twofish(key)
        enc_zeros = tf.encrypt(bytes(16))
        match = enc_zeros == IV_rwn
        print(f"  Twofish({label}): Enc(zeros) = {enc_zeros.hex()}")
        print(f"    IV_rwn match: {match}  {'*** CONFIRMED ***' if match else ''}")
    except Exception as e:
        print(f"  Twofish({label}): ERROR {e}")
print()

print("=" * 65)
print("STEP 2: Identify DCY key (K_A is the prime candidate)")
print("=" * 65)
print(f"P_init_A from live capture: {P_init_A.hex()}")
print(f"Old IV_dcy (derived w/ wrong key): {IV_dcy_old.hex()}")
print()

for pad_bytes, label in [
    (b'\x00' * 4,  '192-bit (K_A + 4 zeros)'),
    (b'\x00' * 12, '256-bit (K_A + 12 zeros)'),
]:
    key = K_A_raw + pad_bytes
    if len(key) not in (16, 24, 32):
        continue
    try:
        tf = Twofish(key)
        enc_zeros = tf.encrypt(bytes(16))
        match_old_dcy = enc_zeros == IV_dcy_old
        print(f"  Twofish({label}): Enc(zeros) = {enc_zeros.hex()}")
        print(f"    == old IV_dcy: {match_old_dcy}")
        print(f"    == P_init_A:   {enc_zeros == P_init_A}")
    except Exception as e:
        print(f"  ERROR {e}")
print()

print("=" * 65)
print("STEP 3: Attempt DCY decryption with K_A")
print("=" * 65)

# Only attempt if we can figure out the padding from STEP 1.
# Try both padding sizes for K_A against MDUMMY.DCY.
DCY_FILE = r'\\i2s109-solidcrm\DBAMFG$\BKARHINV.DCY'
ALT_DCY  = r'\\i2s109-solidcrm\DBAMFG$\MDUMMY.DCY'

def try_dcy_decrypt(dcy_path, key_raw, pad, key_label):
    try:
        raw = open(dcy_path, 'rb').read()
    except:
        print(f"  Cannot open {dcy_path}")
        return False

    key = key_raw + pad
    if len(key) not in (16, 24, 32):
        return False

    header = raw[:8]    # validation ciphertext
    body   = raw[8:]    # body ciphertext

    tf = Twofish(key)
    P  = tf.encrypt(bytes(16))   # P_initial = Encrypt(zeros)

    # Decrypt validation block (CFB-128: PT = CT XOR Encrypt(P))
    K0  = tf.encrypt(P)
    pt0 = bytes(a ^ b for a, b in zip(header, K0[:8]))

    w0 = struct.unpack_from('<I', pt0, 0)[0]
    w1 = struct.unpack_from('<I', pt0, 4)[0]
    xor_val = w0 ^ w1
    match = (xor_val == 0x0955DC84)

    print(f"  File: {os.path.basename(dcy_path)}  Key: {key_label}")
    print(f"    Header CT:    {header.hex()}")
    print(f"    P_initial:    {P.hex()}")
    print(f"    K0 = Enc(P):  {K0.hex()}")
    print(f"    val PT[0:8]:  {pt0.hex()}")
    print(f"    XOR[0:4]^[4:8] = 0x{xor_val:08X}  (exp 0x0955DC84)  {'*** MATCH ***' if match else 'FAIL'}")
    print()
    return match

for dcypath in [ALT_DCY, DCY_FILE]:
    for pad, plabel in [(b'\x00'*4, '192-bit'), (b'\x00'*12, '256-bit')]:
        ok = try_dcy_decrypt(dcypath, K_A_raw, pad, f'K_A+{plabel}')
        if ok:
            print("    *** DECRYPTION KEY CONFIRMED ***")
            break

print("=" * 65)
print("STEP 4: Also check sha1 of passphrase candidates")
print("=" * 65)
candidates = [b'mabufoju', b'MABUFOJU', b'evoDB', b'EvoERP', b'TASPro', b'taspro7']
for c in candidates:
    h = hashlib.sha1(c).digest()
    print(f"  sha1({c!r}) = {h.hex()}")
    for raw in [K_A_raw, K_B_raw, K_C_raw, K_D_raw]:
        if h == raw:
            print(f"    *** MATCHES one of the captured keys! ***")
print()
print("Captured key hashes (for reverse-lookup):")
for name, raw in [('K_A',K_A_raw),('K_B',K_B_raw),('K_C',K_C_raw),('K_D',K_D_raw)]:
    print(f"  {name} = {raw.hex()}")
