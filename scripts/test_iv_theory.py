#!/usr/bin/env python3
"""Test the theory: empirical_ks1 = Encrypt(Encrypt(IV)) so IV = Decrypt^2(empirical_ks1)."""
import hashlib, struct, sys, os
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from twofish_pure import Twofish

key = hashlib.sha1(b'mabufoju').digest() + b'\x00'*4
tf = Twofish(key)
EXP = 0x3E0A37C5

def le32(b, o): return struct.unpack_from('<I', b, o)[0]
def ofb(iv, ct):
    out = bytearray()
    ks = iv
    for i in range(0, len(ct), 16):
        ks = tf.encrypt(ks)
        out.extend(c ^ k for c, k in zip(ct[i:i+16], ks))
    return bytes(out)

emp = bytes.fromhex('0f73767aa296137875eaa22d6fc64b54')

# IV = Decrypt(Decrypt(emp))
K0_val = tf.decrypt(emp)
IV     = tf.decrypt(K0_val)
K0_check = tf.encrypt(IV)
xor4 = le32(K0_check, 0) ^ le32(K0_check, 4)

print(f'empirical : {emp.hex(" ")}')
print(f'K0_val    : {K0_val.hex(" ")}')
print(f'IV        : {IV.hex(" ")}')
print(f'Encrypt(IV): {K0_check.hex(" ")}')
print(f'XOR check : 0x{xor4:08X}  expected 0x{EXP:08X}  {"PASS" if xor4==EXP else "FAIL"}')
print()

with open(r'\\i2s109-solidcrm\DBAMFG$\MDUMMY.DCY', 'rb') as f: dcy = f.read()
with open(r'\\i2s109-solidcrm\DBAMFG$\mDummy.DFM', 'rb') as f: dfm = f.read()

pt   = ofb(IV, dcy)
body = pt[8:8+len(dfm)]
val  = pt[0:4] == pt[4:8]

print(f'MDUMMY.DCY: val_ok={val}  body==DFM: {body==dfm}')
print(f'body[:40]: {body[:40].decode("latin-1", errors=".")}')
print()

# Also try the RWN validation check
with open(r'\\i2s109-solidcrm\DBAMFG$\T7INA.RWN', 'rb') as f: rwn = f.read()
pt_rwn = ofb(IV, rwn[:16])
rwn_val = pt_rwn[0:4] == pt_rwn[4:8]
print(f'T7INA.RWN val_ok: {rwn_val}  pt[0:8]={pt_rwn[0:8].hex()}')

if val and rwn_val:
    iv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'iv_bytes.bin')
    with open(iv_path, 'wb') as f:
        f.write(IV)
    print(f'\nSAVED iv_bytes.bin: {IV.hex(" ")}')
