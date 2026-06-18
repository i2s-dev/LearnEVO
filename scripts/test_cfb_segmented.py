#!/usr/bin/env python3
"""
Test CFB with segment size = block_size from cipher object.
The Move(Q->P, block_size) in mode2_handler only updates P[0:block_size],
leaving P[block_size:16] = leftover from EncryptBlock output.
Test block_size = 8 (CFB-64) and block_size = 1 (CFB-8).
"""
import hashlib, sys
sys.path.insert(0, 'scripts')
from twofish_pure import Twofish

KEY = hashlib.sha1(b'mabufoju').digest() + b'\x00'*4
IV_dcy = bytes.fromhex('cd47af18e0d1c38cf1d8a067fc3dda28')
tf = Twofish(KEY)

dcy = open('samples/MDUMMY.DCY', 'rb').read()
dfm = open('samples/mDummy.DFM', 'rb').read()

print(f'DCY size={len(dcy)}, DFM size={len(dfm)}')
print(f'IV_dcy = {IV_dcy.hex()}')

K0_dcy = tf.encrypt(IV_dcy)
print(f'K0_dcy = Encrypt(IV) = {K0_dcy.hex()}')
print()

def simulate_cfb_segmented(seg_size, iv, dcy, dfm):
    """
    Simulate mode2_handler with given segment size.
    P starts as iv (16 bytes). EncryptBlock writes all 16 bytes.
    Move(Q->P, seg_size) only updates P[0:seg_size].
    """
    P = bytearray(iv)
    plaintext = bytearray()
    i = 0  # position in dcy[0:] (includes validation)
    total = len(dcy)

    while i < total:
        remaining = total - i
        n_full = remaining // seg_size

        for _ in range(n_full):
            Q = bytearray(dcy[i:i+seg_size])  # CT
            K = bytearray(tf.encrypt(bytes(P)))  # Encrypt(P) -> K (full 16 bytes)
            # XOR first seg_size bytes
            pt = bytes(a^b for a,b in zip(Q, K[:seg_size]))
            plaintext.extend(pt)
            # Update P: P[0:seg_size] = Q (CT), P[seg_size:16] unchanged (= K[seg_size:16])
            P[0:seg_size] = Q
            # P[seg_size:16] stays = K[seg_size:16]
            P[seg_size:16] = K[seg_size:16]
            i += seg_size

        remainder = remaining % seg_size
        if remainder > 0:
            K = bytearray(tf.encrypt(bytes(P)))
            pt = bytes(a^b for a,b in zip(dcy[i:i+remainder], K[:remainder]))
            plaintext.extend(pt)
            # After partial: P[0:16] = K (EncryptBlock wrote all 16 bytes, no Move Q->P)
            P[0:16] = K
            i += remainder
            break

    return bytes(plaintext)

# Try block_size = 8
print('=== CFB seg_size=8 (CFB-64) ===')
# We want to skip validation (first 8 bytes) and check body
# But first: simulate JUST the state after validation
P = bytearray(IV_dcy)
K_val = tf.encrypt(bytes(P))
print(f'K_val (full) = {K_val.hex()}')
CT_val = dcy[0:8]
PT_val = bytes(a^b for a,b in zip(CT_val, K_val[:8]))
print(f'CT_val = {CT_val.hex()}')
print(f'PT_val = {PT_val.hex()} = {repr(PT_val)}')
# After full block with seg_size=8: P[0:8] = CT_val, P[8:16] = K_val[8:16]
P[0:8] = CT_val
P[8:16] = K_val[8:16]
print(f'P after validation = {P.hex()}')
print(f'X (empirical) = 7a3dd882c134e5fb254a87b2f5f79625')
print()

# Encrypt(P) -> should be emp_ks[0]
emp_ks0 = bytes(a^b for a,b in zip(dcy[8:24], dfm[0:16]))
print(f'emp_ks[0] = {emp_ks0.hex()}')
K_body0 = tf.encrypt(bytes(P))
print(f'Enc(P)    = {K_body0.hex()}')
print(f'Match: {K_body0 == emp_ks0}')
print()

# Full simulation for body (seg_size=8), starting from P after validation
print('=== Full body decrypt with seg_size=8 ===')
body_dcy = dcy[8:]   # body starts after 8-byte validation
body_dfm = dfm

P_body = bytearray(P)  # P after validation
out = bytearray()
i = 0
seg = 8
while i < len(body_dcy):
    remaining = len(body_dcy) - i
    n_full = remaining // seg
    for _ in range(n_full):
        ct = body_dcy[i:i+seg]
        K = tf.encrypt(bytes(P_body))
        pt = bytes(a^b for a,b in zip(ct, K[:seg]))
        out.extend(pt)
        P_body[0:seg] = ct
        P_body[seg:16] = K[seg:16]
        i += seg
    rem = remaining % seg
    if rem > 0:
        ct = body_dcy[i:i+rem]
        K = tf.encrypt(bytes(P_body))
        pt = bytes(a^b for a,b in zip(ct, K[:rem]))
        out.extend(pt)
        i += rem
        break

out = bytes(out)
match = sum(a==b for a,b in zip(out, body_dfm[:len(out)]))
print(f'Decrypted {len(out)} bytes, {match}/{len(out)} match DFM')
print(f'First 64 bytes: {repr(out[:64])}')
print(f'Expected:       {repr(body_dfm[:64])}')
print()

# Also try seg_size = 1 for completeness
print('=== Quick check seg_size=1 (CFB-8) ===')
P1 = bytearray(IV_dcy)
out1 = bytearray()
for i in range(min(len(dcy), len(dfm)+8)):
    K = tf.encrypt(bytes(P1))
    ct_byte = dcy[i:i+1]
    pt_byte = bytes(a^b for a,b in zip(ct_byte, K[:1]))
    out1.extend(pt_byte)
    P1[0:15] = P1[1:16]  # shift left 1 byte
    P1[15:16] = ct_byte    # shift in CT byte
    if i >= 8 + 64: break

body_out1 = bytes(out1[8:])  # skip validation
match1 = sum(a==b for a,b in zip(body_out1[:64], dfm[:64]))
print(f'First 64 body bytes: {repr(body_out1[:64])}')
print(f'Match with DFM: {match1}/64')
