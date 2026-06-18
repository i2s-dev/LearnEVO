#!/usr/bin/env python3
"""
Test CFB mode directly: does Encrypt(CT[n]) == K[n+1]?
This avoids using Decrypt() entirely, sidestepping any potential bug in it.
"""
import hashlib, sys
sys.path.insert(0, 'scripts')
from twofish_pure import Twofish

KEY = hashlib.sha1(b'mabufoju').digest() + b'\x00'*4
tf = Twofish(KEY)

dcy = open('samples/MDUMMY.DCY','rb').read()
dfm = open('samples/mDummy.DFM','rb').read()

body_dcy = dcy[8:]   # skip 8-byte validation
body_dfm = dfm       # full DFM

n_blocks = min(len(body_dcy), len(body_dfm)) // 16
print(f'Blocks: {n_blocks}')
print()

# Derive empirical keystream blocks: K[n] = body_dcy[n*16:(n+1)*16] XOR body_dfm[n*16:(n+1)*16]
emp_ks = []
for i in range(n_blocks):
    ct = body_dcy[i*16:(i+1)*16]
    pt = body_dfm[i*16:(i+1)*16]
    ks = bytes(a^b for a,b in zip(ct, pt))
    emp_ks.append(ks)

print('=== Direct CFB check: does Encrypt(CT[n]) == K[n+1]? ===')
# For this we need initial block_buf = X such that Encrypt(X) = K[0]
# X is unknown, but we can check transitions n -> n+1 starting from block 0
cfb_hits = 0
for i in range(n_blocks - 1):
    ct_n = body_dcy[i*16:(i+1)*16]
    k_n1 = emp_ks[i+1]
    got  = tf.encrypt(ct_n)
    if got == k_n1:
        cfb_hits += 1
    elif i < 6:
        print(f'  Block {i}->{i+1}: Enc(CT[{i}])={got.hex()}')
        print(f'                   emp_K[{i+1}] ={k_n1.hex()}  MISMATCH')

print(f'CFB hits: {cfb_hits}/{n_blocks-1}')
print()

print('=== Direct OFB check: does Encrypt(K[n]) == K[n+1]? ===')
ofb_hits = 0
for i in range(n_blocks - 1):
    k_n  = emp_ks[i]
    k_n1 = emp_ks[i+1]
    got  = tf.encrypt(k_n)
    if got == k_n1:
        ofb_hits += 1
    elif i < 6:
        print(f'  Block {i}->{i+1}: Enc(K[{i}])={got.hex()}')
        print(f'                  emp_K[{i+1}]={k_n1.hex()}  MISMATCH')

print(f'OFB hits: {ofb_hits}/{n_blocks-1}')
print()

# Verify: first 7 empirical XOR blocks decode to valid DFM text
print('=== Empirical plaintext check (should see DFM text) ===')
for i in range(7):
    ct = body_dcy[i*16:(i+1)*16]
    ks = emp_ks[i]
    pt = bytes(a^b for a,b in zip(ct, ks))
    print(f'  Block {i}: {repr(pt)}')

print()
# What is CT[0] and does Enc(CT[0]) = anything useful?
CT0 = body_dcy[0:16]
K1  = emp_ks[1]
print(f'CT[0]        = {CT0.hex()}')
print(f'Enc(CT[0])   = {tf.encrypt(CT0).hex()}')
print(f'emp_K[1]     = {K1.hex()}')
print(f'Match: {tf.encrypt(CT0) == K1}')
