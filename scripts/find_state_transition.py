#!/usr/bin/env python3
"""Derive the full keystream from MDUMMY.DCY XOR mDummy.DFM and find the state transition rule."""
import hashlib, sys
sys.path.insert(0, 'scripts')
from twofish_pure import Twofish

KEY = hashlib.sha1(b'mabufoju').digest() + b'\x00'*4
tf = Twofish(KEY)

dcy = open('samples/MDUMMY.DCY','rb').read()
dfm = open('samples/mDummy.DFM','rb').read()

print(f'DCY size: {len(dcy)}, DFM size: {len(dfm)}')
body_dcy = dcy[8:]     # skip 8-byte validation
body_dfm = dfm         # DFM starts at 0
n_blocks  = min(len(body_dcy), len(body_dfm)) // 16
print(f'Blocks to analyze: {n_blocks}')
print()

# Derive keystream and "input state" for each block
keystreams = []
states     = []  # state_n = Decrypt(K_n) = input to EncryptBlock for block n
for i in range(n_blocks):
    ct = body_dcy[i*16:(i+1)*16]
    pt = body_dfm[i*16:(i+1)*16]
    ks = bytes(a^b for a,b in zip(ct, pt))
    state = tf.decrypt(ks)
    keystreams.append(ks)
    states.append(state)

# For each block transition, check what rule maps state_n to state_{n+1}
print('=== State transition analysis ===')
hits = {'CFB': 0, 'OFB': 0, 'PT-fb': 0, 'K-fb': 0, 'unknown': 0}
for i in range(n_blocks - 1):
    s_n   = states[i]
    s_n1  = states[i+1]
    k_n   = keystreams[i]
    ct_n  = body_dcy[i*16:(i+1)*16]
    pt_n  = body_dfm[i*16:(i+1)*16]

    if s_n1 == ct_n:   hits['CFB'] += 1
    elif s_n1 == k_n:  hits['OFB'] += 1
    elif s_n1 == pt_n: hits['PT-fb'] += 1
    elif s_n1 == bytes(a^b for a,b in zip(k_n, s_n)): hits['K-fb'] += 1
    else:              hits['unknown'] += 1

print(f'Transition counts over {n_blocks-1} pairs:')
for k,v in hits.items():
    print(f'  {k}: {v}')

print()
# If unknown > 0, check deeper for first few unknowns
unk_count = 0
for i in range(n_blocks - 1):
    s_n   = states[i]
    s_n1  = states[i+1]
    k_n   = keystreams[i]
    ct_n  = body_dcy[i*16:(i+1)*16]
    pt_n  = body_dfm[i*16:(i+1)*16]

    # Check many candidates
    found = None
    for candidate, label in [
        (ct_n, 'CT'),
        (k_n, 'K'),
        (pt_n, 'PT'),
        (tf.encrypt(ct_n), 'Enc(CT)'),
        (tf.decrypt(ct_n), 'Dec(CT)'),
        (tf.encrypt(k_n), 'Enc(K)'),
        (tf.decrypt(k_n), 'Dec(K)'),
        (tf.encrypt(pt_n), 'Enc(PT)'),
        (bytes(a^b for a,b in zip(ct_n, s_n)), 'CT XOR s_n'),
        (bytes(a^b for a,b in zip(k_n, s_n)), 'K XOR s_n'),
    ]:
        if candidate == s_n1:
            found = label
            break

    if found is None:
        if unk_count < 5:
            print(f'Block {i} -> {i+1}: UNKNOWN transition')
            print(f'  s_{i}   = {s_n.hex()}')
            print(f'  CT_{i}  = {ct_n.hex()}')
            print(f'  PT_{i}  = {pt_n.hex()}')
            print(f'  K_{i}   = {k_n.hex()}')
            print(f'  s_{i+1} = {s_n1.hex()}')
        unk_count += 1
    elif unk_count == 0 and i < 5:
        print(f'Block {i}: transition rule = {found}')

print()
# Verify: if CFB (s_{n+1} = CT_n) holds for all, do a full decrypt
if hits['CFB'] == n_blocks - 1:
    print('CFB confirmed! Doing full CFB decrypt to verify against DFM...')
    bb = bytearray(states[0])
    out = bytearray()
    for i in range(n_blocks):
        ct = body_dcy[i*16:(i+1)*16]
        K = tf.encrypt(bytes(bb))
        out.extend(a^b for a,b in zip(ct, K))
        bb = bytearray(ct)
    match = bytes(out) == body_dfm[:len(out)]
    print(f'  Full CFB vs DFM: {match}')
    print(f'  First 32 PT: {repr(bytes(out[:32]))}')
elif hits['OFB'] == n_blocks - 1:
    print('OFB confirmed!')
else:
    print(f'Mixed or unknown mode. Distribution: {hits}')
