#!/usr/bin/env python3
"""
Test: what P_initial gives correct validation for MDUMMY.DCY?

cipher_init pushes 0 as IV → SetKey tail does:
  FillChar(buffer1, 16, 0)
  EncryptBlock(buffer1) in-place  → buffer1 = Encrypt_K(zeros)
  vtable[0x48]: P = buffer1 = Encrypt_K(zeros)

After cipher_init: P = Encrypt_K(zeros).
Validation (partial block, 8 bytes):
  EncryptBlock(P) in-place → P = Encrypt_K(Encrypt_K(zeros)) = K_sq
  validation_PT = CT_val XOR K_sq[0:8]
  expected_PT = d484de56 d484de56

So: K_sq[0:8] = CT_val XOR d484de56d484de56 should hold IF our model is correct.

Let's check.
"""
import hashlib, sys
sys.path.insert(0, 'scripts')
from twofish_pure import Twofish

KEY = hashlib.sha1(b'mabufoju').digest() + b'\x00'*4
tf = Twofish(KEY)

CT_val = bytes.fromhex('7fb8c42cfb649125')
expected_val_PT_first4 = bytes.fromhex('d484de56')  # repeating pattern
IV_dcy = bytes.fromhex('cd47af18e0d1c38cf1d8a067fc3dda28')
emp_ks0 = bytes.fromhex('0f73767aa296137875eaa22d6fc64b54')

print('=== Model A: P_initial = IV_dcy (our original assumption) ===')
P_A = IV_dcy
K_A = tf.encrypt(P_A)
val_PT_A = bytes(a^b for a,b in zip(CT_val, K_A[:8]))
print(f'  P_initial   = {P_A.hex()}')
print(f'  K0 = Enc(P) = {K_A.hex()}')
print(f'  val_PT[0:8] = {val_PT_A.hex()} (need first4 = d484de56)')
print(f'  Match: {val_PT_A[:4] == expected_val_PT_first4}')
print()

print('=== Model B: P_initial = Encrypt(zeros) (per cipher_init analysis) ===')
P_B = tf.encrypt(bytes(16))
K_B = tf.encrypt(P_B)  # second encrypt for validation
val_PT_B = bytes(a^b for a,b in zip(CT_val, K_B[:8]))
print(f'  P_initial       = {P_B.hex()}')
print(f'  K0 = Enc^2(0)   = {K_B.hex()}')
print(f'  val_PT[0:8]     = {val_PT_B.hex()} (need first4 = d484de56)')
print(f'  Match: {val_PT_B[:4] == expected_val_PT_first4}')
print()

# In Model B, after validation partial block: P = K_B
# Body block 0: EncryptBlock(K_B) → K_body0
K_body0_B = tf.encrypt(K_B)
print(f'  Body K0 = Enc(K_B) = {K_body0_B.hex()}')
print(f'  emp_ks0            = {emp_ks0.hex()}')
print(f'  Match: {K_body0_B == emp_ks0}')
print()

print('=== Model C: P_initial = zeros (no SetKey tail run?) ===')
P_C = bytes(16)
K_C = tf.encrypt(P_C)  # first encrypt for validation
val_PT_C = bytes(a^b for a,b in zip(CT_val, K_C[:8]))
print(f'  P_initial   = {P_C.hex()}')
print(f'  K0 = Enc(0) = {K_C.hex()}')
print(f'  val_PT[0:8] = {val_PT_C.hex()} (need first4 = d484de56)')
print(f'  Match: {val_PT_C[:4] == expected_val_PT_first4}')
print()

# Now: what P_initial makes validation work?
# We need: Enc(P_initial)[0:8] XOR CT_val[0:8] = d484de56 d484de56
# => Enc(P_initial)[0:8] = CT_val XOR d484de56d484de56
req_K0_first8 = bytes(a^b for a,b in zip(CT_val, bytes.fromhex('d484de56d484de56')))
print(f'=== Required: Enc(P_initial)[0:8] = {req_K0_first8.hex()} ===')
print(f'  With Model A: Enc(IV_dcy)[0:8] = {K_A[:8].hex()}  match={K_A[:8] == req_K0_first8}')
print(f'  With Model B: Enc^2(0)[0:8]    = {K_B[:8].hex()}  match={K_B[:8] == req_K0_first8}')
print(f'  Enc(zeros)[0:8]                = {P_B[:8].hex()}')
print()

# What is required P_initial?
# P_initial = Decrypt(value_whose_encrypt_is_req_K0_first8...)
# We need to find the full 16-byte K0 value whose first 8 bytes = req_K0_first8
# But there are many such K0 values (the last 8 bytes can be anything)
# IV_dcy is one such P_initial that gives Enc(IV_dcy)[0:8] = req_K0_first8 ✓

print('=== Body check: after validation, P = Enc(P_initial) ===')
print('=== Then body block 0 uses Enc(Enc(P_initial)) as keystream ===')
# For Model A:
body_K_A = tf.encrypt(K_A)  # Enc(Enc(IV_dcy))
print(f'  Model A body_K0 = {body_K_A.hex()}')
print(f'  emp_ks0         = {emp_ks0.hex()}')
print(f'  Match: {body_K_A == emp_ks0}')
print()

# So: neither Model A nor Model B explains the body!
# The body requires X = Decrypt(emp_ks0) as the P state going into body
# Let's confirm:
X = tf.decrypt(emp_ks0)
print(f'  X = Decrypt(emp_ks0) = {X.hex()}  (required P for body block 0)')
print(f'  X == P_A (IV_dcy)?   {X == P_A}')
print(f'  X == K_A (Enc(IV))?  {X == K_A}')
print(f'  X == P_B?            {X == P_B}')
print(f'  X == K_B?            {X == K_B}')
print()

# KEY HYPOTHESIS: what if the cipher is RE-INITIALIZED before body_load?
# Or what if body_load uses a fresh cipher?
# If body uses P_initial = X (directly), then:
print('=== If body_load uses fresh cipher with P_initial_body = X ===')
val_PT_if_X = bytes(a^b for a,b in zip(CT_val, tf.encrypt(X)[:8]))
print(f'  Enc(X)[0:8]  = {tf.encrypt(X)[:8].hex()}')
print(f'  val_PT if X  = {val_PT_if_X.hex()} (need d484de56...)')
# X as block0 of body makes NO sense for validation.

# KEY HYPOTHESIS 2: cipher reinit with different IV before body
# Specifically: P_body_initial = IV_rwn?
iv_rwn = bytes.fromhex('9cdac345a5f01c2c965792d90b1abc1e')
K_rwn = tf.encrypt(iv_rwn)
body_match = K_rwn == emp_ks0
print()
print(f'=== If body cipher reset with IV_rwn = {iv_rwn.hex()} ===')
print(f'  Enc(IV_rwn)  = {K_rwn.hex()}')
print(f'  emp_ks0      = {emp_ks0.hex()}')
print(f'  Match: {body_match}')
