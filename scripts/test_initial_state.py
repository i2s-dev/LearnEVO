#!/usr/bin/env python3
"""Test: what if cipher block_buf starts as all zeros before first use?"""
import hashlib, sys
sys.path.insert(0, 'scripts')
from twofish_pure import Twofish

KEY = hashlib.sha1(b'mabufoju').digest() + b'\x00'*4
tf = Twofish(KEY)

CT_val = bytes.fromhex('7fb8c42cfb649125')
emp_ks0 = bytes.fromhex('0f73767aa296137875eaa22d6fc64b54')
IV_dcy = bytes.fromhex('cd47af18e0d1c38cf1d8a067fc3dda28')

# If block_buf = zeros initially:
K0_zeros = tf.encrypt(bytes(16))
PT_zeros = bytes(a^b for a,b in zip(CT_val, K0_zeros[:8]))
print('Hypothesis: block_buf starts as all zeros')
print(f'  Encrypt(zeros) = {K0_zeros.hex()}')
print(f'  CT_val XOR Enc(zeros)[0:8] = {PT_zeros.hex()} (want d484de56...)')
print(f'  Match: {PT_zeros.hex() == "d484de56d484de56"}')
print()

# After validation partial block: block_buf = K0_zeros
# Body block 0: K_body0 = Encrypt(K0_zeros)
K_body0 = tf.encrypt(K0_zeros)
print(f'  Encrypt(K0_zeros) = {K_body0.hex()}')
print(f'  emp_ks0           = {emp_ks0.hex()}')
print(f'  Match: {K_body0 == emp_ks0}')
print()

# Standard IV_dcy hypothesis (our current model):
K0_iv = tf.encrypt(IV_dcy)
PT_iv = bytes(a^b for a,b in zip(CT_val, K0_iv[:8]))
print('Current model: block_buf starts as IV_dcy')
print(f'  Encrypt(IV_dcy) = {K0_iv.hex()}')
print(f'  CT_val XOR Enc(IV)[0:8] = {PT_iv.hex()} (want d484de56...)')
print(f'  Match: {PT_iv.hex() == "d484de56d484de56"}')
print()
K_body0_iv = tf.encrypt(K0_iv)
print(f'  Encrypt(K0_iv) = {K_body0_iv.hex()}')
print(f'  emp_ks0        = {emp_ks0.hex()}')
print(f'  Match: {K_body0_iv == emp_ks0}')
print()

# New hypothesis: what if the cipher uses IV_dcy AND the body also uses a fresh
# cipher object initialized with a DIFFERENT IV (body IV)?
# The body IV would be X = Decrypt(emp_ks0) = 7a3dd882c134e5fb254a87b2f5f79625
# What produces X? What if there's a second cipher with block_buf=all-zeros
# after some different key setup?
X = tf.decrypt(emp_ks0)
print(f'Empirical body X = {X.hex()}')
print(f'  Is X = Enc^n(IV_dcy)? checked 11 iterations: no match')
print(f'  Is X hardcoded? No (not found in binary)')
print()

# Key insight search: what if 'mabufoju' is NOT the passphrase for the KEY?
# What if it's used differently?
# Try: key = 'mabufoju' directly as ASCII (not SHA1)
mabufoju_bytes = b'mabufoju'  # 8 bytes only
# Can't use as Twofish key (need 16/24/32 bytes)

# Try: key = SHA1('mabufoju') XOR SHA1(something else)?
# Or: key = SHA1(SHA1('mabufoju') + something)?

# What if the FIRST 8 bytes of MDUMMY.DCY (CT_val) = Encrypt(zeros) XOR val_PT?
# i.e., what if IV is derived from the file content?
# val_PT would be d484de56d484de56 if CT_val ^ Enc(X_initial) = d484de56...
# We need Enc(X_initial)[0:8] = CT_val[0:8] XOR d484de56d484de56
target_K0_first8 = bytes(a^b for a,b in zip(CT_val, bytes.fromhex('d484de56d484de56')))
print(f'Required Enc(initial)[0:8] = {target_K0_first8.hex()}')
print(f'This is Enc(IV_dcy)[0:8]   = {K0_iv[:8].hex()}')
print(f'Match: {target_K0_first8 == K0_iv[:8]}')  # Should be True since IV_dcy was found this way
