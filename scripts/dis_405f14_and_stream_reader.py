#!/usr/bin/env python3
"""
Disassemble:
1. 0x405f14 — called before cipher_init in validate_func, may replace [ebp+8]
2. 0x74C698 — class pointer for stream reader used in cipher_init
3. What vtable[0x44] of stream_reader does (the Read method)
"""
import capstone, struct
cs = capstone.Cs(capstone.CS_ARCH_X86, capstone.CS_MODE_32)
cs.detail = False
data = open(r'C:\ISTS\evoerp.exe', 'rb').read()
DELTA = 0x400C00

for va_target, size, label in [
    (0x405f14, 120, '0x405f14 (called before cipher_init)'),
    (0x477520, 100, '0x477520 (outer_func stream initializer)'),
]:
    file_off = va_target - DELTA
    code = data[file_off:file_off+size]
    print(f'{"="*70}')
    print(f'{label}  file=0x{file_off:X}')
    for ins in list(cs.disasm(code, va_target))[:30]:
        highlight = ''
        if ins.mnemonic == 'ret': highlight = '  <-- RETURN'
        if ins.mnemonic == 'call': highlight = f'  [CALL -> {ins.op_str}]'
        print(f'  0x{ins.address:08X}  {ins.mnemonic:8s} {ins.op_str}{highlight}')
    print()

# What is at 0x74C698 (class pointer for stream reader)?
print('='*70)
class_at_74c698 = struct.unpack_from('<I', data, 0x74C698 - DELTA)[0]
print(f'[0x74C698] = 0x{class_at_74c698:08X}  (class_ptr for stream reader)')
# Usually the class pointer points to an object descriptor or VMT
# Let's dump what's there
for off in range(0, 12):
    val = struct.unpack_from('<I', data, class_at_74c698 - DELTA + off*4)[0]
    print(f'  [{class_at_74c698+off*4:08X}] = 0x{val:08X}')
print()

# Disassemble the stream reader constructor (0x48074c)
print('='*70)
print('Stream reader ctor (0x48074c):')
va = 0x48074c
file_off = va - DELTA
code = data[file_off:file_off+150]
for ins in list(cs.disasm(code, va))[:35]:
    highlight = ''
    if ins.mnemonic == 'ret': highlight = '  <-- RETURN'
    if ins.mnemonic == 'call': highlight = f'  [CALL -> {ins.op_str}]'
    print(f'  0x{ins.address:08X}  {ins.mnemonic:8s} {ins.op_str}{highlight}')
print()

# 0x74EFBC — SetStream for stream reader (called from cipher_init)
# This sets up the stream to read from. Does it also look at the source stream
# for an IV?
print('='*70)
print('0x74EFBC (SetStream / StreamReader init from cipher_init):')
va = 0x74EFBC
file_off = va - DELTA
code = data[file_off:file_off+200]
for ins in list(cs.disasm(code, va))[:45]:
    highlight = ''
    if ins.mnemonic == 'ret': highlight = '  <-- RETURN'
    if ins.mnemonic == 'call': highlight = f'  [CALL -> {ins.op_str}]'
    print(f'  0x{ins.address:08X}  {ins.mnemonic:8s} {ins.op_str}{highlight}')
