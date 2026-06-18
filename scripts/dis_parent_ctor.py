#!/usr/bin/env python3
"""Disassemble parent constructor 0x74EE30 and also 0x74EFBC (SetKey/SetIV?).
Find where cipher+0x44 (block_size divisor) and cipher+0x3C/0x40 (P/Q ptrs) are set."""
import capstone, struct
cs = capstone.Cs(capstone.CS_ARCH_X86, capstone.CS_MODE_32)
cs.detail = False
data = open(r'C:\ISTS\evoerp.exe', 'rb').read()
DELTA = 0x400C00

targets = [
    (0x34E230, 250, '74EE30  parent_ctor'),
    (0x34E3BC, 200, '74EFBC  SetStream or SetKey'),
    (0x34E26B, 200, '74E26B  cipher_init tail'),
    (0x34E71C, 50, '74F31C  VMT[0x30] = returns 6?'),
    (0x34E76C, 60, '74F36C  VMT[0x38] = GetKeySize?'),
    (0x34ECA4, 100, '74F8A4  VMT[0x40] = SetKey?'),
]

for file_off, size, label in targets:
    va = file_off + DELTA
    code = data[file_off:file_off+size]
    print(f'\n{"="*70}')
    print(f'{label}  file=0x{file_off:X}  VA=0x{va:X}')
    print('='*70)
    for ins in list(cs.disasm(code, va))[:50]:
        print(f'  0x{ins.address:08X}  {ins.mnemonic:8s} {ins.op_str}')
