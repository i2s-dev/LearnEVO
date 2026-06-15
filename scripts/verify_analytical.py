#!/usr/bin/env python3
"""Test IV candidates by decrypting MDUMMY.DCY and comparing to MDUMMY.DFM."""
import hashlib, struct, sys, os
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from twofish_pure import Twofish

key = hashlib.sha1(b'mabufoju').digest() + b'\x00'*4
tf  = Twofish(key)

DCY_PATH = r'\\i2s109-solidcrm\DBAMFG$\MDUMMY.DCY'
DFM_PATH = r'\\i2s109-solidcrm\DBAMFG$\mDummy.DFM'

with open(DCY_PATH, 'rb') as f: dcy = f.read()
with open(DFM_PATH, 'rb') as f: dfm = f.read()
print(f'DCY={len(dcy)} DFM={len(dfm)}')
print(f'DFM[0:32] hex: {dfm[:32].hex()}')
print(f'DFM[0:32] txt: {dfm[:32].decode("ascii", errors=".")}')
print()

def ofb_dec(iv, ct):
    out = bytearray()
    ks = iv
    for i in range(0, len(ct), 16):
        ks = tf.encrypt(ks)
        out.extend(c ^ k for c, k in zip(ct[i:i+16], ks))
    return bytes(out)

# T7INA.RWN ct[0:8] + empirical K0[8:16]
t7ina_ct8 = bytes([0xF8,0x13,0xB6,0x7B,0x3D,0x24,0xBC,0x45])
k0_hi = bytes.fromhex('0f73767aa296137875eaa22d6fc64b54')[:8]

for X in [0x00000000, 0x01000000, 0xFFFFFFFF, 0x54415350]:
    Xb = struct.pack('<I', X)
    k0_lo = bytes(a ^ b for a, b in zip(t7ina_ct8, Xb * 2))
    k0 = k0_lo + k0_hi
    iv = tf.decrypt(k0)
    pt = ofb_dec(iv, dcy)          # decrypt WHOLE DCY from byte 0
    val_ok = pt[0:4] == pt[4:8]
    body = pt[8:8+len(dfm)]
    match = (body == dfm)
    print(f'X=0x{X:08X}: val={val_ok} match={match} body[:24]={body[:24].hex()}')
    if match:
        print(f'  *** MATCH ***  IV={iv.hex(" ")}')
        with open(os.path.join(os.path.dirname(__file__), 'iv_bytes.bin'), 'wb') as f2:
            f2.write(iv)
        print(f'  Saved iv_bytes.bin')

print()
# Also show what the DCY decrypts to with each candidate (first 40 bytes of body)
print('Body first 40 chars for X=0x00000000:')
Xb = b'\x00\x00\x00\x00'
k0_lo = bytes(a ^ b for a, b in zip(t7ina_ct8, Xb * 2))
k0 = k0_lo + k0_hi
iv0 = tf.decrypt(k0)
pt0 = ofb_dec(iv0, dcy)
print(f'  hex: {pt0[8:48].hex()}')
print(f'  txt: {pt0[8:48].decode("ascii", errors=".")}')
