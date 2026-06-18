#!/usr/bin/env python3
"""Disassemble full SetKey (VMT[0x40] = 0x74F8A4) and trace where cipher+0x3C gets set."""
import capstone
cs = capstone.Cs(capstone.CS_ARCH_X86, capstone.CS_MODE_32)
cs.detail = False
data = open(r'C:\ISTS\evoerp.exe', 'rb').read()
DELTA = 0x400C00

# Full SetKey body
file_off = 0x74F8A4 - DELTA
va = 0x74F8A4
code = data[file_off:file_off+400]
print('='*70)
print(f'SetKey VMT[0x40] = 0x74F8A4  file=0x{file_off:X}')
print('='*70)
for ins in list(cs.disasm(code, va))[:80]:
    print(f'  0x{ins.address:08X}  {ins.mnemonic:8s} {ins.op_str}')

# Also disassemble Twofish_PrepareKey (likely called from SetKey)
# Find calls within SetKey to see what's called
print()
print('Looking for CALL instructions in SetKey...')
for ins in cs.disasm(data[file_off:file_off+300], va):
    if ins.mnemonic == 'call':
        print(f'  CALL at 0x{ins.address:08X}: {ins.op_str}')
