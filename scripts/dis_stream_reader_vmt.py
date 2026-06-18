#!/usr/bin/env python3
"""
Trace the stream reader VMT fully, focusing on vtable[0x40] (step called in cipher_init
at 0x74E223), vtable[0x44] (Read called at 0x74E235), and vtable[0x4C] (SetStream).
Also check 0x4809EC (cipher-back-ref setup in stream reader ctor).
"""
import capstone, struct
cs = capstone.Cs(capstone.CS_ARCH_X86, capstone.CS_MODE_32)
cs.detail = False
data = open(r'C:\ISTS\evoerp.exe', 'rb').read()
DELTA = 0x400C00

# Stream reader class VMT base = 0x74C6E4
vmt_sr = 0x74C6E4
vmt_sr_file = vmt_sr - DELTA
print('='*70)
print(f'Stream reader VMT  base=0x{vmt_sr:X}  file=0x{vmt_sr_file:X}')
print('='*70)
for i in range(30):
    slot_va = vmt_sr + i*4
    fn_va = struct.unpack_from('<I', data, vmt_sr_file + i*4)[0]
    label = ''
    if i*4 == 0x40: label = ' <-- called from cipher_init at 0x74E223 (after stream_reader created)'
    if i*4 == 0x44: label = ' <-- Read (called from cipher_init at 0x74E235)'
    if i*4 == 0x4C: label = ' <-- vtable[0x4C] (called from SetStream at 0x74EFD8)'
    print(f'  VMT[0x{i*4:02X}] = 0x{fn_va:08X}{label}')
print()

# Disassemble the key stream reader methods
# vtable[0x40] at sr_VMT+0x40
fn_40 = struct.unpack_from('<I', data, vmt_sr_file + 0x40)[0]
fn_44 = struct.unpack_from('<I', data, vmt_sr_file + 0x44)[0]
fn_4c = struct.unpack_from('<I', data, vmt_sr_file + 0x4c)[0]

for va_target, label in [
    (fn_40, f'SR.vtable[0x40] = 0x{fn_40:X} (called right after ctor in cipher_init)'),
    (fn_44, f'SR.vtable[0x44] = 0x{fn_44:X} (Read — reads key bytes into stack buffer)'),
    (fn_4c, f'SR.vtable[0x4C] = 0x{fn_4c:X} (SetStream — called from 0x74EFBC)'),
]:
    file_off = va_target - DELTA
    code = data[file_off:file_off+200]
    print('='*70)
    print(label)
    for ins in list(cs.disasm(code, va_target))[:40]:
        highlight = ''
        if ins.mnemonic == 'ret': highlight = '  <-- RETURN'
        if ins.mnemonic == 'call': highlight = f'  [CALL -> {ins.op_str}]'
        op = ins.op_str
        if '0x3c' in op.lower(): highlight += '  *** cipher+0x3C'
        if '0x38' in op.lower(): highlight += '  *** cipher+0x38'
        if '0x48' in op.lower(): highlight += '  *** vtable[0x48]?'
        print(f'  0x{ins.address:08X}  {ins.mnemonic:8s} {ins.op_str}{highlight}')
    print()

# 0x4809EC — called from stream reader ctor with (stream_reader, cipher)
print('='*70)
print('0x4809EC (stream reader ctor call — stores cipher ref?):')
va = 0x4809EC
file_off = va - DELTA
code = data[file_off:file_off+100]
for ins in list(cs.disasm(code, va))[:25]:
    highlight = ''
    if ins.mnemonic == 'ret': highlight = '  <-- RETURN'
    if ins.mnemonic == 'call': highlight = f'  [CALL -> {ins.op_str}]'
    print(f'  0x{ins.address:08X}  {ins.mnemonic:8s} {ins.op_str}{highlight}')
print()

# Also check: what function is at 0x74EFDE (the function adjacent to SetStream)?
print('='*70)
print('Function at 0x74EFDE (calls vtable[0x48] on cipher):')
va = 0x74EFDE
file_off = va - DELTA
code = data[file_off:file_off+80]
for ins in list(cs.disasm(code, va))[:20]:
    highlight = ''
    if ins.mnemonic == 'ret': highlight = '  <-- RETURN'
    if ins.mnemonic == 'call': highlight = f'  [CALL -> {ins.op_str}]'
    op = ins.op_str
    if '0x48' in op.lower(): highlight += '  *** vtable[0x48]=InitVector!'
    if '0x30' in op.lower(): highlight += '  *** initialized_flag'
    print(f'  0x{ins.address:08X}  {ins.mnemonic:8s} {ins.op_str}{highlight}')
