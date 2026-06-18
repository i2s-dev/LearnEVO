#!/usr/bin/env python3
"""Disassemble body_load (0x74E374) and cipher-init (0x74E1F8) to see if a new cipher
is created for the body with a different IV, or if the feedback state is manipulated."""
import capstone
cs = capstone.Cs(capstone.CS_ARCH_X86, capstone.CS_MODE_32)
cs.detail = False
data = open(r'C:\ISTS\evoerp.exe', 'rb').read()
DELTA = 0x400C00

targets = [
    (0x34D5F8, 120, '74E1F8  cipher_init / SetStream'),
    (0x34D774, 300, '74E374  body_load'),
]

for file_off, size, label in targets:
    va = file_off + DELTA
    code = data[file_off:file_off+size]
    print(f'\n{"="*70}')
    print(f'{label}  file=0x{file_off:X}  VA=0x{va:X}')
    print('='*70)
    for ins in cs.disasm(code, va):
        print(f'  0x{ins.address:08X}  {ins.mnemonic:8s} {ins.op_str}')
