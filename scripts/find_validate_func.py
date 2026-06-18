#!/usr/bin/env python3
"""Find validate_func and disassemble it to see the body-load call setup."""
import capstone, sys

cs = capstone.Cs(capstone.CS_ARCH_X86, capstone.CS_MODE_32)
data = open(r'C:\ISTS\evoerp.exe','rb').read()
DELTA = 0x400C00

# Search for PUSH EBP prologues near expected range 0x742000-0x743000
print('Function prologues in range 0x742000-0x743000:')
for off in range(0x742000, 0x743000, 1):
    if data[off] == 0x55 and data[off+1] == 0x8b and data[off+2] == 0xec:
        print(f'  file 0x{off:X}  VA 0x{off+DELTA:X}')

print()
# Disassemble from file 0x742654
print('From doc file offset 0x742654:')
for offset in [0x742654, 0x742250, 0x742260, 0x742270]:
    code = data[offset:offset+8]
    ins_list = list(cs.disasm(code, offset + DELTA))
    first = ins_list[0] if ins_list else None
    mn = first.mnemonic if first else '???'
    print(f'  0x{offset:X}: {code[:4].hex()} -> {mn}')
