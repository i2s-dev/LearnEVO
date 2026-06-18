#!/usr/bin/env python3
"""Check vtable[0x48], extended VMT, and full body_load prologue."""
import capstone, struct
cs = capstone.Cs(capstone.CS_ARCH_X86, capstone.CS_MODE_32)
cs.detail = False
data = open(r'C:\ISTS\evoerp.exe', 'rb').read()
DELTA = 0x400C00

# Dump extended VMT (more slots)
print('='*70)
print('Extended VMT dump (VMT base = 0x74F2A8):')
vmt_base = 0x74F2A8
vmt_file = vmt_base - DELTA
for i in range(26):  # 0x00..0x64
    slot_va = vmt_base + i*4
    fn_va = struct.unpack_from('<I', data, vmt_file + i*4)[0]
    label = ''
    if i*4 == 0x2C: label = ' <-- ctor'
    if i*4 == 0x38: label = ' <-- GetKeySize'
    if i*4 == 0x40: label = ' <-- SetKey'
    if i*4 == 0x44: label = ' <-- ???'
    if i*4 == 0x48: label = ' <-- vtable[0x48] (called from SetKey tail)'
    if i*4 == 0x50: label = ' <-- Decrypt dispatcher'
    if i*4 == 0x54: label = ' <-- returns 128'
    if i*4 == 0x58: label = ' <-- EncryptBlock'
    print(f'  VMT[0x{i*4:02X}] = 0x{fn_va:08X}{label}')

# Now disassemble vtable[0x48]
vtable_48_ptr = struct.unpack_from('<I', data, vmt_file + 0x48)[0]
print(f'\n{"="*70}')
print(f'vtable[0x48] = 0x{vtable_48_ptr:08X}')
file_off = vtable_48_ptr - DELTA
code = data[file_off:file_off+150]
for ins in list(cs.disasm(code, vtable_48_ptr))[:35]:
    highlight = ''
    op = ins.op_str
    if '0x3c' in op.lower(): highlight = '  *** cipher+0x3C (P / block_buf)'
    if '0x38' in op.lower(): highlight = '  *** cipher+0x38 (buffer1)'
    if '0x40' in op.lower() and 'e' in op: highlight = '  *** cipher+0x40 (Q)'
    if ins.mnemonic == 'ret': highlight = '  <-- RETURN'
    print(f'  0x{ins.address:08X}  {ins.mnemonic:8s} {ins.op_str}{highlight}')

# Also check vtable[0x44]
vtable_44_ptr = struct.unpack_from('<I', data, vmt_file + 0x44)[0]
print(f'\n{"="*70}')
print(f'vtable[0x44] = 0x{vtable_44_ptr:08X}')
file_off = vtable_44_ptr - DELTA
code = data[file_off:file_off+100]
for ins in list(cs.disasm(code, vtable_44_ptr))[:25]:
    print(f'  0x{ins.address:08X}  {ins.mnemonic:8s} {ins.op_str}')

# Now: full body_load (0x74E374) prologue — check if it re-initializes cipher
print(f'\n{"="*70}')
print('Full body_load prologue (0x74E374):')
va = 0x74E374
file_off = va - DELTA
code = data[file_off:file_off+300]
for ins in list(cs.disasm(code, va))[:60]:
    highlight = ''
    op = ins.op_str
    if '0x3c' in op.lower(): highlight = '  *** P/block_buf'
    if '0x38' in op.lower(): highlight = '  *** buffer1'
    if ins.mnemonic in ('call',): highlight = f'  [CALL -> {op}]'
    print(f'  0x{ins.address:08X}  {ins.mnemonic:8s} {ins.op_str}{highlight}')

# And SetKey tail continued past 0x750202
print(f'\n{"="*70}')
print('SetKey tail continued (0x750202):')
va = 0x750202
file_off = va - DELTA
code = data[file_off:file_off+80]
for ins in list(cs.disasm(code, va))[:20]:
    highlight = ''
    op = ins.op_str
    if '0x3c' in op.lower(): highlight = '  *** P/block_buf'
    if '0x38' in op.lower(): highlight = '  *** buffer1'
    if ins.mnemonic == 'ret': highlight = '  <-- RETURN'
    print(f'  0x{ins.address:08X}  {ins.mnemonic:8s} {ins.op_str}{highlight}')
