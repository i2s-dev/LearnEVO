#!/usr/bin/env python3
"""Disassemble validate_func to see the body-load call setup."""
import capstone
cs = capstone.Cs(capstone.CS_ARCH_X86, capstone.CS_MODE_32)
cs.detail = False
data = open(r'C:\ISTS\evoerp.exe','rb').read()
DELTA = 0x400C00

offset = 0x742654  # validate_func
code = data[offset:offset+300]
base_va = offset + DELTA
print(f'validate_func @ file 0x{offset:X}  VA 0x{base_va:X}')
print('='*70)
for ins in list(cs.disasm(code, base_va))[:80]:
    print(f'  0x{ins.address:08X}  {ins.mnemonic:8s} {ins.op_str}')
