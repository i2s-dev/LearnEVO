#!/usr/bin/env python3
"""Derive the full actual keystream from MDUMMY.DCY XOR mDummy.DFM and identify the mode."""
import hashlib, sys, math
from collections import Counter
sys.path.insert(0, 'scripts')
from twofish_pure import Twofish

KEY = hashlib.sha1(b'mabufoju').digest() + b'\x00'*4
IV_dcy = bytes.fromhex('cd47af18e0d1c38cf1d8a067fc3dda28')
tf = Twofish(KEY)
K0_dcy = tf.encrypt(IV_dcy)
emp_ks = bytes.fromhex('0f73767aa296137875eaa22d6fc64b54')  # K1: Encrypt(X)
X = tf.decrypt(emp_ks)

dcy = open('samples/MDUMMY.DCY','rb').read()
dfm = open('samples/mDummy.DFM','rb').read()

# Extract empirical keystream blocks from DCY body XOR DFM
print('=== Empirical keystream blocks (DCY body XOR DFM) ===')
ks_blocks = []
body = dcy[8:]   # skip 8-byte validation
min_len = min(len(body), len(dfm))
for i in range(0, min_len, 16):
    ct_blk = body[i:i+16]
    pt_blk = dfm[i:i+16]
    ks_blk = bytes(a^b for a,b in zip(ct_blk, pt_blk))
    ks_blocks.append(ks_blk)
    pt_check = bytes(a^b for a,b in zip(ct_blk, ks_blk))
    print(f'Block {i//16:3d}: ks={ks_blk.hex()}  PT={repr(pt_check[:16])}')
    if i >= 16*6: break

print()
# Now check which cipher mode generates these keystream blocks
# OFB: Kn = Encrypt^n(X)
print('=== OFB check: does Kn = Encrypt(K_{n-1}) hold? ===')
bb = bytearray(X)
for n, ks_blk in enumerate(ks_blocks[:8]):
    K = tf.encrypt(bytes(bb))
    match = 'OK' if K[:len(ks_blk)] == ks_blk else 'FAIL'
    print(f'  Block {n}: OFB K={K.hex()}  expected={ks_blk.hex()}  {match}')
    bb = bytearray(K)  # OFB: advance feedback by K

print()
# CFB: Kn = Encrypt(CT_{n-1})
print('=== CFB check: does Kn = Encrypt(CT_{n-1}) hold? ===')
bb = bytearray(X)
for n, ks_blk in enumerate(ks_blocks[:8]):
    K = tf.encrypt(bytes(bb))
    match = 'OK' if K[:len(ks_blk)] == ks_blk else 'FAIL'
    ct_blk = body[n*16:(n+1)*16]
    print(f'  Block {n}: CFB K={K.hex()}  expected={ks_blk.hex()}  {match}')
    if len(ct_blk) == 16:
        bb = bytearray(ct_blk)  # CFB: advance by CT

print()
# Try: counter mode, Kn = Encrypt(X + n) for various counter schemes
print('=== Counter (CTR) mode check ===')
import struct
for n, ks_blk in enumerate(ks_blocks[:4]):
    for ctr_pos in [0, 4, 8, 12]:  # try counter at different positions
        xb = bytearray(X)
        struct.pack_into('<I', xb, ctr_pos, n)
        K = tf.encrypt(bytes(xb))
        if K[:len(ks_blk)] == ks_blk:
            print(f'  Block {n}: CTR match at pos={ctr_pos} LE! K={K.hex()}')
        xb = bytearray(X)
        struct.pack_into('>I', xb, ctr_pos, n)
        K = tf.encrypt(bytes(xb))
        if K[:len(ks_blk)] == ks_blk:
            print(f'  Block {n}: CTR match at pos={ctr_pos} BE! K={K.hex()}')

print()
# What if the cipher is RE-INITIALIZED for the body with a different IV?
# Try: body_IV = some function of validation PT or CT
val_pt = bytes(a^b for a,b in zip(dcy[:8], K0_dcy[:8]))
print(f'Validation PT: {val_pt.hex()} = {repr(val_pt)}')
# Try body_IV = val_pt repeated / extended to 16 bytes
for iv_candidate, label in [
    (val_pt + val_pt, 'val_pt x2'),
    (val_pt + bytes(8), 'val_pt + zeros'),
    (bytes(8) + val_pt, 'zeros + val_pt'),
    (dcy[0:16], 'CT[0:16]'),
    (dcy[0:8] + val_pt, 'CT[0:8]+val_pt'),
]:
    if len(iv_candidate) == 16:
        K_try = tf.encrypt(bytes(iv_candidate))
        if K_try == ks_blocks[0]:
            print(f'BODY IV FOUND: {label} = {iv_candidate.hex()}')
