#!/usr/bin/env python3
"""Disassemble full SetKey body after subkey generation, looking for writes to cipher+0x3C."""
import capstone
cs = capstone.Cs(capstone.CS_ARCH_X86, capstone.CS_MODE_32)
cs.detail = False
data = open(r'C:\ISTS\evoerp.exe', 'rb').read()
DELTA = 0x400C00

# SetKey = 0x74F8A4, disassemble 800 bytes to see full function
file_off = 0x74F8A4 - DELTA
va = 0x74F8A4
code = data[file_off:file_off+800]
print('='*70)
print(f'Full SetKey  file=0x{file_off:X}  VA=0x{va:X}')
print('='*70)
insts = list(cs.disasm(code, va))[:150]
for ins in insts:
    # Highlight writes to cipher+0x3C or cipher+0x40 or cipher+0x38
    highlight = ''
    op = ins.op_str
    if '0x3c' in op or '0x3C' in op: highlight = '  *** cipher+0x3C'
    if '0x40' in op and 'ebx' in op: highlight = '  *** cipher+0x40'
    if '0x38' in op and 'ebx' in op: highlight = '  *** cipher+0x38'
    print(f'  0x{ins.address:08X}  {ins.mnemonic:8s} {ins.op_str}{highlight}')

# Also: disassemble 0x74f5b4 and 0x74f6b8 to understand key generation
print('\n' + '='*70)
for target_va, label in [(0x74F5B4, '74F5B4 (RS_row?)'), (0x74F6B8, '74F6B8 (subkey_gen?)')]:
    file_off = target_va - DELTA
    code = data[file_off:file_off+150]
    print(f'\n{label}  file=0x{file_off:X}')
    for ins in list(cs.disasm(code, target_va))[:30]:
        highlight = ''
        if '0x3c' in ins.op_str.lower(): highlight = ' ***'
        print(f'  0x{ins.address:08X}  {ins.mnemonic:8s} {ins.op_str}{highlight}')
    print()
