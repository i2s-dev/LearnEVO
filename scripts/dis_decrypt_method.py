#!/usr/bin/env python3
"""Disassemble vtable[0x50] = 0x74E6BC - the actual decrypt method."""
import capstone
cs = capstone.Cs(capstone.CS_ARCH_X86, capstone.CS_MODE_32)
cs.detail = False
data = open(r'C:\ISTS\evoerp.exe', 'rb').read()
DELTA = 0x400C00

targets = [
    (0x34DABC, 300, '74E6BC  vtable[0x50] = main decrypt method'),
    (0x34D9E4, 200, '74E5E4  vtable[0x48]'),
    (0x34DA74, 150, '74E674  vtable[0x4C]'),
    (0x34E71C, 150, '74F31C  vtable[0x70]'),
    (0x34E740, 100, '74F340  vtable[0x30]'),
]

for file_off, size, label in targets:
    va = file_off + DELTA
    code = data[file_off:file_off+size]
    print(f'\n{"="*70}')
    print(f'{label}  file=0x{file_off:X}  VA=0x{va:X}')
    print('='*70)
    for ins in list(cs.disasm(code, va))[:50]:
        print(f'  0x{ins.address:08X}  {ins.mnemonic:8s} {ins.op_str}')
