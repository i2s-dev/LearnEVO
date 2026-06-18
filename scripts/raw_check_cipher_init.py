#!/usr/bin/env python3
"""Check raw bytes around cipher_init's SetKey call and trace IV precisely."""
import hashlib, struct
data = open(r'C:\ISTS\evoerp.exe', 'rb').read()
DELTA = 0x400C00

# Check bytes at cipher_init's push 0 (0x74E265)
offs = [0x74E24D, 0x74E265]
for va in offs:
    file_off = va - DELTA
    raw = data[file_off:file_off+16]
    print(f'Bytes at VA 0x{va:X} (file 0x{file_off:X}): {raw.hex()}')
    print(f'  push_byte={raw[0]:02x}  arg={raw[1]:08x} (if 4-byte imm32)')
    print()

# Also: check what's in the global [0xb8b0cc] at static init time
# The global at 0xb8b0cc — what's stored there in the file?
global_va = 0xb8b0cc
global_file = global_va - DELTA
print(f'Static value at [0xb8b0cc] (file 0x{global_file:X}):')
if global_file < len(data):
    val = struct.unpack_from('<I', data, global_file)[0]
    print(f'  = 0x{val:08X}')
else:
    print('  (beyond file size — BSS/runtime-initialized)')
print()

# Search for code that writes to 0xb8b0cc (mov [0xb8b0cc], ...)
print('Searching for writes to [0xb8b0cc] in binary...')
target_bytes = struct.pack('<I', 0xb8b0cc)
found = []
for off in range(0, len(data)-10):
    if data[off:off+4] == target_bytes:
        # Check if there's an instruction at a small offset before that writes to this addr
        context = data[max(0,off-3):off+8]
        found.append((off, context))
if found:
    for off, ctx in found[:20]:
        print(f'  Ref at file 0x{off:X}  VA 0x{off+DELTA:X}: {ctx.hex()}')
else:
    print('  (not found as constant in binary)')
print()

# Verify Twofish result with SHA1("mabufoju")+4zeros key
import sys
sys.path.insert(0, 'scripts')
from twofish_pure import Twofish
key = hashlib.sha1(b'mabufoju').digest() + b'\x00'*4
tf = Twofish(key)
enc_zeros = tf.encrypt(bytes(16))
IV_dcy = bytes.fromhex('cd47af18e0d1c38cf1d8a067fc3dda28')
print(f'Key (sha1+4z): {key.hex()}')
print(f'Encrypt(zeros) = {enc_zeros.hex()}')
print(f'IV_dcy         = {IV_dcy.hex()}')
print(f'Equal? {enc_zeros == IV_dcy}')
print()

# The root question: if P_initial = Encrypt(zeros) != IV_dcy, something sets it to IV_dcy
# Let me search for IV_dcy as a hardcoded constant now that we know the file layout
print('Searching for full IV_dcy bytes in binary...')
idx = data.find(IV_dcy)
if idx >= 0:
    print(f'  FOUND at file 0x{idx:X}  VA 0x{idx+DELTA:X}')
    print(f'  Context: {data[idx-16:idx+32].hex()}')
else:
    print('  NOT FOUND')

# Also search for enc_zeros
print()
print('Searching for Encrypt(zeros) bytes in binary...')
idx = data.find(enc_zeros)
if idx >= 0:
    print(f'  FOUND at file 0x{idx:X}  VA 0x{idx+DELTA:X}')
    print(f'  Context: {data[idx-16:idx+32].hex()}')
else:
    print('  NOT FOUND (expected)')
