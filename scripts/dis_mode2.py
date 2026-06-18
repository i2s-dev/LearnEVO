#!/usr/bin/env python3
"""Disassemble mode2_handler (0x74EB50) in detail to understand CFB feedback."""
import capstone
cs = capstone.Cs(capstone.CS_ARCH_X86, capstone.CS_MODE_32)
cs.detail = False
data = open(r'C:\ISTS\evoerp.exe', 'rb').read()
DELTA = 0x400C00

file_off = 0x34DF50  # 0x74EB50 - DELTA
va = file_off + DELTA
code = data[file_off:file_off+350]
print(f'mode2_handler  file=0x{file_off:X}  VA=0x{va:X}')
print('='*70)
for ins in cs.disasm(code, va):
    print(f'  0x{ins.address:08X}  {ins.mnemonic:8s} {ins.op_str}')
