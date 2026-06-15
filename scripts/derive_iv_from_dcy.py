#!/usr/bin/env python3
"""
Derive the EvoERP Twofish IV analytically from MDUMMY.DCY / mDummy.DFM.

Method:
  K0 = Encrypt(IV)   -- first OFB keystream block
  K1 = Encrypt(K0)   -- second OFB keystream block

  From the file data (no plaintext assumptions):
    K1[0:8]  = DCY[16:24] XOR DFM[8:16]
    K1[8:16] = DCY[24:32] XOR DFM[16:24]
    K0       = Decrypt(K1)
    IV       = Decrypt(K0)
"""
import hashlib, sys, os, struct
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from twofish_pure import Twofish

key = hashlib.sha1(b'mabufoju').digest() + b'\x00'*4
tf  = Twofish(key)

DCY = r'\\i2s109-solidcrm\DBAMFG$\MDUMMY.DCY'
DFM = r'\\i2s109-solidcrm\DBAMFG$\mDummy.DFM'

with open(DCY, 'rb') as f: dcy = f.read()
with open(DFM, 'rb') as f: dfm = f.read()

print(f'DCY size={len(dcy)}  DFM size={len(dfm)}')
print(f'DCY[0:48]: {dcy[0:48].hex()}')
print(f'DFM[0:48]: {dfm[0:48].hex()}')
print(f'DFM text : {dfm[0:48].decode("latin-1")}')
print()

# Derive K1 from known-plaintext in body
K1_lo = bytes(a ^ b for a, b in zip(dcy[16:24], dfm[8:16]))
K1_hi = bytes(a ^ b for a, b in zip(dcy[24:32], dfm[16:24]))
K1 = K1_lo + K1_hi
K0 = tf.decrypt(K1)
IV = tf.decrypt(K0)

print(f'K1       : {K1.hex(" ")}')
print(f'K0       : {K0.hex(" ")}')
print(f'IV       : {IV.hex(" ")}')
print()

# Cross-checks
K0_c = tf.encrypt(IV)
K1_c = tf.encrypt(K0)
print(f'Encrypt(IV)  == K0 : {K0_c == K0}')
print(f'Encrypt(K0)  == K1 : {K1_c == K1}')
XOR = struct.unpack_from('<I', K0_c, 0)[0] ^ struct.unpack_from('<I', K0_c, 4)[0]
print(f'K0[0:4]^K0[4:8]    : 0x{XOR:08X}  (expected 0x3E0A37C5) {"OK" if XOR==0x3E0A37C5 else "FAIL"}')
print()

# Decrypt MDUMMY.DCY and compare body to DFM
def ofb(iv, ct):
    out = bytearray()
    ks = iv
    for i in range(0, len(ct), 16):
        ks = tf.encrypt(ks)
        out.extend(c ^ k for c, k in zip(ct[i:i+16], ks))
    return bytes(out)

pt = ofb(IV, dcy)
body = pt[8:8 + len(dfm)]
val_ok = (pt[0:4] == pt[4:8])
match  = (body == dfm)
print(f'Validation block: {pt[0:8].hex()}  pt[0:4]==pt[4:8]: {val_ok}')
print(f'Body == DFM:      {match}')
print(f'Body[:64]:        {body[:64].decode("latin-1")}')
print()

if match and val_ok:
    iv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'iv_bytes.bin')
    with open(iv_path, 'wb') as f:
        f.write(IV)
    print(f'SAVED: {iv_path}')
    print('Run: python scripts/verify_iv.py')
    print('Run: python scripts/rwn_decrypt.py --validate-only --limit 20')
