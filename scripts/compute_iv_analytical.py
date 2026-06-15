#!/usr/bin/env python3
"""
Analytically compute IV candidates from:
1. T7INA.RWN ct[0:8] (known validation block ciphertext)
2. Empirical ks1[8:16] = 0f737676a2961378 (from 11 DCY/DFM pairs)

Assumption: pt[0:4] = pt[4:8] = X (validation sentinel)
Trying X = 0 as the most common case.

Then verify: decrypt .DCY file body and check for DFM header text.
"""
import hashlib, struct, sys, os, glob
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from twofish_pure import Twofish

key = hashlib.sha1(b'mabufoju').digest() + b'\x00'*4
tf  = Twofish(key)

def le32(b, o): return struct.unpack_from('<I', b, o)[0]

# T7INA.RWN first 8 bytes (confirmed)
t7ina_ct8 = bytes([0xF8, 0x13, 0xB6, 0x7B, 0x3D, 0x24, 0xBC, 0x45])

# Empirical keystream from 11 DCY/DFM pairs
# = ks1[8:16] || ks2[0:8]  (first 8 bytes = ks1[8:16])
emp = bytes.fromhex('0f73767aa296137875eaa22d6fc64b54')
ks1_hi = emp[:8]   # = ks1[8:16]

print('=== Analytical IV computation ===')
print()
print('Assumption: pt[0:4] = pt[4:8] = X (validation block sentinel)')
print('            ks1[8:16] = 0f 73 76 7a a2 96 13 78 (empirical, 11 files)')
print()

candidates = []
for X in [0x00000000, 0x01000000, 0xFFFFFFFF, 0x54415350, 0x12345678]:
    Xb = struct.pack('<I', X)
    pt8 = Xb * 2
    ks1_lo = bytes(a ^ b for a, b in zip(t7ina_ct8, pt8))
    ks1 = ks1_lo + ks1_hi
    iv = tf.decrypt(ks1)
    ks1_back = tf.encrypt(iv)
    xor4 = le32(ks1_back, 0) ^ le32(ks1_back, 4)
    ok = (ks1_back == ks1)
    candidates.append((X, iv, ks1))
    print(f'  X=0x{X:08X}: IV={iv.hex()}  round-trip={ok}  ks1[0:4]^[4:8]=0x{xor4:08X}')

print()

# Attempt DCY/DFM verification for each candidate
# DFM files start with "object " (known plaintext)
print('=== DCY/DFM verification ===')
print()

dcy_paths = glob.glob(r'\\i2s109-solidcrm\DBAMFG$\*.DCY')
verified = {}
for dcy_path in sorted(dcy_paths)[:10]:
    dfm_path = dcy_path[:-4] + '.DFM'
    if not os.path.isfile(dfm_path):
        continue
    try:
        with open(dcy_path, 'rb') as f:
            dcy = f.read()
        with open(dfm_path, 'rb') as f:
            dfm = f.read()
        if len(dcy) < 24 or len(dfm) < 16:
            continue

        for X, iv, ks1 in candidates:
            # OFB decrypt: ks=IV, then for each 16-byte block: ks=Encrypt(ks), pt=ct^ks
            ks = iv
            body_ct = dcy[8:]   # skip 8-byte validation block
            pt_body = bytearray()
            for i in range(0, min(64, len(body_ct)), 16):
                ks = tf.encrypt(ks)
                chunk = body_ct[i:i+16]
                pt_body.extend(c ^ k for c, k in zip(chunk, ks))
            # Check: does pt_body start with "object " ?
            pt_str = bytes(pt_body[:16])
            starts_ok = pt_str.startswith(b'object ')
            dfm_match = (bytes(pt_body[:len(dfm[:32])]) == dfm[:len(dfm[:32])])
            if starts_ok or dfm_match:
                fname = os.path.basename(dcy_path)
                print(f'  X=0x{X:08X}  {fname}: MATCH! pt_body[:16]={pt_str!r}')
                if X not in verified:
                    verified[X] = iv
            # else: silent
    except Exception as e:
        pass

print()
if verified:
    print('=== VERIFIED IV ===')
    for X, iv in verified.items():
        print(f'  X=0x{X:08X}: IV = {iv.hex(" ")}')
    best_iv = list(verified.values())[0]
    iv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'iv_bytes.bin')
    with open(iv_path, 'wb') as f:
        f.write(best_iv)
    print(f'  Saved to {iv_path}')
else:
    print('No DCY/DFM pair confirmed the IV.')
    print('Candidates (X=0 is most likely):')
    for X, iv, ks1 in candidates:
        print(f'  X=0x{X:08X}: {iv.hex(" ")}')
