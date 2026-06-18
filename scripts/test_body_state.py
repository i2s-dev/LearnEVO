#!/usr/bin/env python3
"""Back-derive the correct block_buf state after 8-byte validation from the empirical DCY keystream."""
import hashlib, sys
sys.path.insert(0, 'scripts')
from twofish_pure import Twofish

KEY = hashlib.sha1(b'mabufoju').digest() + b'\x00'*4
IV_dcy = bytes.fromhex('cd47af18e0d1c38cf1d8a067fc3dda28')
IV_rwn = bytes.fromhex('9cdac345a5f01c2c965792d90b1abc1e')
tf = Twofish(KEY)
K0_dcy = tf.encrypt(IV_dcy)
K0_rwn = tf.encrypt(IV_rwn)

# MDUMMY.DCY raw bytes from hex dump
dcy_raw = bytes.fromhex(
    '7FB8C42CFB649125'   # validation CT[0:8]
    '60111C1FC1E2333D'   # body CT[8:16]
    '1183D66B00B42665'   # body CT[16:24]
    'AC3433BB2255EC07'   # body CT[24:32]
)

val_ct  = dcy_raw[0:8]
body_ct = dcy_raw[8:24]

# Validation check
val_pt = bytes(a^b for a,b in zip(val_ct, K0_dcy[:8]))
print(f'MDUMMY.DCY Validation PT: {val_pt.hex()}  match={val_pt[0:4]==val_pt[4:8]}')

# Copy mDummy.DFM
import shutil, os
dfm_src = r'\\i2s109-solidcrm\DBAMFG$\mDummy.DFM'
dfm_dst = 'samples/mDummy.DFM'
if not os.path.exists(dfm_dst):
    shutil.copy2(dfm_src, dfm_dst)
dfm = open(dfm_dst, 'rb').read()
print(f'mDummy.DFM first 32 bytes: {dfm[:32].hex()}')
print(f'As text: {repr(dfm[:32])}')
print()

# Empirical keystream = DCY_body[0:16] XOR DFM[0:16]
emp_ks = bytes(a^b for a,b in zip(body_ct, dfm[:16]))
print(f'Empirical K1 (DCY[8:24] XOR DFM[0:16]) = {emp_ks.hex()}')
plaintext_check = bytes(a^b for a,b in zip(body_ct, emp_ks))
print(f'PT check: {repr(plaintext_check)}')
print()

# THE KEY: what X gives Encrypt(X) = emp_ks?
X = tf.decrypt(emp_ks)
print(f'X = Decrypt(empirical_K1) = {X.hex()}')
print(f'This IS block_buf after 8-byte partial validation.')
print()

# Compare to known candidates
print(f'K0_dcy                     = {K0_dcy.hex()}')
mode_a_dcy = bytes(val_ct) + bytes(K0_dcy[8:])
print(f'CT[0:8]+K0_dcy[8:16]       = {mode_a_dcy.hex()}')
print(f'IV_dcy                     = {IV_dcy.hex()}')
print()

if X == K0_dcy:
    print('==> MATCH: block_buf = K0_dcy (Encrypt(IV))')
elif X == mode_a_dcy:
    print('==> MATCH: block_buf = CT[0:8]+K0_dcy[8:16] (Mode A)')
elif X == IV_dcy:
    print('==> MATCH: block_buf = IV_dcy (unchanged IV)')
else:
    print('==> NO known match')
    print(f'   X XOR K0_dcy      = {bytes(a^b for a,b in zip(X,K0_dcy)).hex()}')
    print(f'   X XOR Mode_A_dcy  = {bytes(a^b for a,b in zip(X,mode_a_dcy)).hex()}')
    print(f'   X XOR IV_dcy      = {bytes(a^b for a,b in zip(X,IV_dcy)).hex()}')
    print(f'   X[0:8] = {X[:8].hex()}')
    print(f'   X[8:]  = {X[8:].hex()}')
    print(f'   val_ct = {val_ct.hex()}')
    print(f'   K0[0:8]= {K0_dcy[:8].hex()}')
    print(f'   K0[8:] = {K0_dcy[8:].hex()}')

# Now check: use X as initial block_buf, decrypt DCY body in CFB
print()
print('=== Decrypting MDUMMY.DCY body using X as initial block_buf ===')
dcy_full = open('samples/MDUMMY.DCY','rb').read()
bb = bytearray(X)
out = bytearray()
for i in range(8, len(dcy_full), 16):
    chunk = dcy_full[i:i+16]
    K = tf.encrypt(bytes(bb))
    out.extend(a^b for a,b in zip(chunk, K[:len(chunk)]))
    if len(chunk) == 16:
        bb = bytearray(chunk)  # CFB feedback
print(f'First 128 decrypted bytes:')
print(f'  hex: {bytes(out[:128]).hex()}')
print(f'  text: {repr(bytes(out[:128]))}')
