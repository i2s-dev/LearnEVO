#!/usr/bin/env python3
"""Test OFB vs CFB for the body after the empirical X-seeded first block."""
import hashlib, sys
sys.path.insert(0, 'scripts')
from twofish_pure import Twofish

KEY = hashlib.sha1(b'mabufoju').digest() + b'\x00'*4
IV_dcy = bytes.fromhex('cd47af18e0d1c38cf1d8a067fc3dda28')
tf = Twofish(KEY)
K0_dcy = tf.encrypt(IV_dcy)

# Empirical K1 (verified to decrypt block 1 to "object EditForm1")
emp_ks = bytes.fromhex('0f73767aa296137875eaa22d6fc64b54')
X = tf.decrypt(emp_ks)  # block_buf state that gives K1=emp_ks

dcy = open('samples/MDUMMY.DCY','rb').read()
dfm = open('samples/mDummy.DFM','rb').read()

print(f'DFM first 64 bytes: {repr(dfm[:64])}')
print()

# Mode CFB: feedback = CT
print('=== Mode CFB (bb = CT after each block) ===')
bb = bytearray(X)
out = bytearray()
for i in range(8, len(dcy), 16):
    chunk = dcy[i:i+16]
    K = tf.encrypt(bytes(bb))
    out.extend(a^b for a,b in zip(chunk, K[:len(chunk)]))
    if len(chunk) == 16:
        bb = bytearray(chunk)
print(f'CFB PT[0:64]:  {repr(bytes(out[:64]))}')
print()

# Mode OFB: feedback = K (keystream, not CT)
print('=== Mode OFB (bb = K after each block) ===')
bb = bytearray(X)
out2 = bytearray()
for i in range(8, len(dcy), 16):
    chunk = dcy[i:i+16]
    K = tf.encrypt(bytes(bb))
    out2.extend(a^b for a,b in zip(chunk, K[:len(chunk)]))
    bb = bytearray(K)  # OFB: feedback = keystream
print(f'OFB PT[0:64]:  {repr(bytes(out2[:64]))}')
print()

# Mode Hybrid: first block = X→K1 (OFB-like), then CFB from K1
print('=== Mode Hybrid: first block OFB-seeded, then switch to CFB ===')
bb = bytearray(X)
out3 = bytearray()
K1 = tf.encrypt(bytes(bb))
out3.extend(a^b for a,b in zip(dcy[8:24], K1))
bb = bytearray(K1)  # after first block, use K1 as next feedback
for i in range(24, len(dcy), 16):
    chunk = dcy[i:i+16]
    K = tf.encrypt(bytes(bb))
    out3.extend(a^b for a,b in zip(chunk, K[:len(chunk)]))
    if len(chunk) == 16:
        bb = bytearray(chunk)  # CFB from block 2 onwards
print(f'Hybrid PT[0:64]:  {repr(bytes(out3[:64]))}')
print()

# Compare all against DFM
print('=== Comparison vs DFM ===')
for name, result in [('CFB', out), ('OFB', out2), ('Hybrid', out3)]:
    match_bytes = sum(a==b for a,b in zip(bytes(result), dfm[:len(result)]))
    total = min(len(result), len(dfm))
    print(f'{name}: {match_bytes}/{total} bytes match DFM ({100*match_bytes/total:.1f}%)')
    print(f'  PT[0:32]: {repr(bytes(result[:32]))}')
    print(f'  DFM[0:32]:{repr(dfm[:32])}')
    print()
