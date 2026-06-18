#!/usr/bin/env python3
"""
Search evoerp.exe for hardcoded IVs and the empirical body state X.
Also check if X is Encrypt^n(IV_dcy) for small n (double-encrypt chain).
Also check cipher_init (0x74E1F8) more carefully for where IV/key comes from.
"""
import hashlib, struct, sys
sys.path.insert(0, 'scripts')
from twofish_pure import Twofish

KEY = hashlib.sha1(b'mabufoju').digest() + b'\x00'*4
IV_dcy = bytes.fromhex('cd47af18e0d1c38cf1d8a067fc3dda28')
IV_rwn = bytes.fromhex('9cdac345a5f01c2c965792d90b1abc1e')
tf = Twofish(KEY)

X = bytes.fromhex('7a3dd882c134e5fb254a87b2f5f79625')  # empirical body[0] block_buf
emp_ks0 = bytes.fromhex('0f73767aa296137875eaa22d6fc64b54')

data = open(r'C:\ISTS\evoerp.exe', 'rb').read()
print(f'EXE size: {len(data)}')

# Search for X in the binary
print(f'\nSearching for X={X.hex()} in binary...')
pos = 0
count = 0
while True:
    pos = data.find(X, pos)
    if pos < 0:
        break
    print(f'  Found X at file offset 0x{pos:X}')
    count += 1
    pos += 1
if count == 0:
    print('  Not found')

# Search for emp_ks0
print(f'\nSearching for emp_ks0={emp_ks0.hex()} in binary...')
pos = 0
count = 0
while True:
    pos = data.find(emp_ks0, pos)
    if pos < 0:
        break
    print(f'  Found emp_ks0 at file offset 0x{pos:X}')
    count += 1
    pos += 1
if count == 0:
    print('  Not found')

# Check: is X = Encrypt^n(IV_dcy) for n = 1..10?
print('\nEncrypt chain from IV_dcy:')
state = IV_dcy
for n in range(1, 12):
    state = tf.encrypt(state)
    print(f'  Enc^{n}(IV_dcy) = {state.hex()}  {"<== X!" if state == X else ""}')

# Check: is X = Decrypt^n(IV_dcy) for n = 1..10?
print('\nDecrypt chain from IV_dcy:')
state = IV_dcy
for n in range(1, 12):
    state = tf.decrypt(state)
    print(f'  Dec^{n}(IV_dcy) = {state.hex()}  {"<== X!" if state == X else ""}')

# Check: is emp_ks0 = Encrypt^n(IV_dcy)?
print('\nIs emp_ks0 reachable from IV_dcy?')
state = IV_dcy
for n in range(1, 20):
    state = tf.encrypt(state)
    if state == emp_ks0:
        print(f'  emp_ks0 = Enc^{n}(IV_dcy) !')
        break
else:
    print('  No match in 20 iterations')

# Try: different IV candidates - maybe the body IV is derived from validation PT
val_PT = bytes.fromhex('d484de56d484de56')
CT_val = bytes.fromhex('7fb8c42cfb649125')
K0_dcy = tf.encrypt(IV_dcy)

print('\nCheck various IV candidates:')
for iv_candidate, label in [
    (val_PT * 2, 'val_PT repeated'),
    (val_PT + bytes(8), 'val_PT + zeros'),
    (bytes(8) + val_PT, 'zeros + val_PT'),
    (CT_val + CT_val, 'CT_val repeated'),
    (K0_dcy[:8] + CT_val, 'K0_dcy[0:8] + CT_val'),
    (CT_val + K0_dcy[8:16], 'CT_val + K0_dcy[8:16]'),  # this was P after CFB-64
    (bytes(16), 'all zeros'),
    (bytes.fromhex('0'*32), 'all zeros'),
]:
    if isinstance(iv_candidate, bytes) and len(iv_candidate) == 16:
        K = tf.encrypt(iv_candidate)
        if K == emp_ks0:
            print(f'  MATCH! IV = {label} = {iv_candidate.hex()}')
        else:
            print(f'  {label} -> Enc = {K.hex()[:16]}... (emp={emp_ks0.hex()[:16]}...)')

# Look for IV_dcy-like 16-byte blocks near mode2_handler in the binary
print('\nSearch for IV_dcy in binary:')
pos = data.find(IV_dcy)
if pos >= 0:
    print(f'  IV_dcy found at 0x{pos:X}')
    # Show context
    start = max(0, pos-32)
    end = min(len(data), pos+48)
    for off in range(start, end, 16):
        mark = ' <-- IV_dcy' if off <= pos < off+16 else ''
        print(f'  0x{off:08X}: {data[off:off+16].hex()}{mark}')
else:
    print('  Not found in binary')
