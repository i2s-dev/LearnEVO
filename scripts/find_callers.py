#!/usr/bin/env python3
"""
Find callers of validate_func (VA 0xB43254 / file 0x742654).
Also disassemble cipher_init tail to see how IV gets into cipher+0x3C.
"""
import capstone, struct
cs = capstone.Cs(capstone.CS_ARCH_X86, capstone.CS_MODE_32)
cs.detail = False
data = open(r'C:\ISTS\evoerp.exe', 'rb').read()
DELTA = 0x400C00

target_va = 0xB43254   # validate_func VA
target_file = 0x742654 # file offset

print(f'Searching for callers of validate_func (VA 0x{target_va:X})...')
callers = []
# Search for CALL rel32 (0xE8) instructions
for i in range(0, len(data) - 5):
    if data[i] == 0xE8:
        rel = struct.unpack_from('<i', data, i + 1)[0]
        call_va = (i + DELTA) + 5 + rel
        if call_va == target_va:
            callers.append(i)

print(f'Found {len(callers)} direct CALL sites:')
for off in callers:
    va = off + DELTA
    print(f'  file 0x{off:X}  VA 0x{va:X}')
    # Disassemble context: 40 bytes before the call
    start = max(0, off - 60)
    for ins in cs.disasm(data[start:off+10], start + DELTA):
        marker = ' <-- CALL validate_func' if ins.address == va else ''
        print(f'    0x{ins.address:08X}  {ins.mnemonic:8s} {ins.op_str}{marker}')
    print()

# Also check for indirect calls or JMP to target
print('\nSearching for JMP to validate_func...')
for i in range(0, len(data) - 5):
    if data[i] == 0xE9:
        rel = struct.unpack_from('<i', data, i + 1)[0]
        jmp_va = (i + DELTA) + 5 + rel
        if jmp_va == target_va:
            print(f'  JMP at file 0x{i:X}  VA 0x{i+DELTA:X}')

# Disassemble cipher_init continuation after 0x74E26B (which is in parent_ctor)
# The ACTUAL cipher_init is at 0x74E1F8 (file 0x34D5F8)
# Let me show more of it
print('\n' + '='*70)
print('cipher_init (0x74E1F8) extended disassembly:')
print('='*70)
file_off = 0x34D5F8
va = file_off + DELTA
for ins in list(cs.disasm(data[file_off:file_off+300], va))[:70]:
    print(f'  0x{ins.address:08X}  {ins.mnemonic:8s} {ins.op_str}')
