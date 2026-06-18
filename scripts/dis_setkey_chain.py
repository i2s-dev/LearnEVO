#!/usr/bin/env python3
"""Disassemble SetKey internals (0x74E18C) and look for where cipher+0x3C gets set."""
import capstone, struct
cs = capstone.Cs(capstone.CS_ARCH_X86, capstone.CS_MODE_32)
cs.detail = False
data = open(r'C:\ISTS\evoerp.exe', 'rb').read()
DELTA = 0x400C00

# 0x74E18C = file 0x34D58C
targets = [
    (0x34D58C, 350, '74E18C  SetKey_core (called from VMT[0x40])'),
    (0x34D774, 50, '74E374  body_load start (check for init code before main loop)'),
]

for file_off, size, label in targets:
    va = file_off + DELTA
    code = data[file_off:file_off+size]
    print(f'\n{"="*70}')
    print(f'{label}  file=0x{file_off:X}  VA=0x{va:X}')
    print('='*70)
    for ins in list(cs.disasm(code, va))[:70]:
        print(f'  0x{ins.address:08X}  {ins.mnemonic:8s} {ins.op_str}')

# Also: disassemble mode0 handler (0x74E7FC) to understand what "mode 0" does
# And mode1 handler (0x74E9AC) - these may reveal what the different modes mean
print('\n' + '='*70)
print('Mode handlers:')
for file_off, size, label in [
    (0x34DBFC - DELTA + DELTA, 80, '74E7FC mode0_handler'),
    (0x34DDAC - DELTA + DELTA, 80, '74E9AC mode1_handler'),
]:
    # These VAs need to be corrected
    pass

for va_target, size, label in [
    (0x74E7FC, 80, 'mode0 decrypt (vtable[0x50] mode=0)'),
    (0x74E9AC, 80, 'mode1 decrypt (vtable[0x50] mode=1)'),
    (0x74EA58, 80, 'mode2 encrypt (vtable[0x4C] mode=2)'),
]:
    file_off = va_target - DELTA
    va = va_target
    code = data[file_off:file_off+size]
    print(f'\n{label}  file=0x{file_off:X}  VA=0x{va:X}')
    for ins in list(cs.disasm(code, va))[:20]:
        print(f'  0x{ins.address:08X}  {ins.mnemonic:8s} {ins.op_str}')
