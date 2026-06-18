#!/usr/bin/env python3
"""Disassemble the function containing the validate_func call at 0xB4321C.
Find its prologue, trace [ebp-4], and see where IV comes from."""
import capstone, struct
cs = capstone.Cs(capstone.CS_ARCH_X86, capstone.CS_MODE_32)
cs.detail = False
data = open(r'C:\ISTS\evoerp.exe', 'rb').read()
DELTA = 0x400C00

# The call to validate_func is at file 0x74261C (VA 0xB4321C)
# Look backwards from 0x74261C for PUSH EBP prologue
call_file = 0x74261C
print(f'Searching for function prologue before call at file 0x{call_file:X}...')

# Scan backwards for PUSH EBP (0x55) + MOV EBP,ESP (0x8B 0xEC)
func_start = None
for off in range(call_file, max(0, call_file - 0x2000), -1):
    if data[off] == 0x55 and data[off+1] == 0x8B and data[off+2] == 0xEC:
        func_start = off
        break

if func_start:
    print(f'Function prologue at file 0x{func_start:X}  VA 0x{func_start+DELTA:X}')
    print()
    # Disassemble 400 bytes from function start
    code = data[func_start:func_start+400]
    va = func_start + DELTA
    for ins in list(cs.disasm(code, va))[:80]:
        marker = ' <<<' if ins.address == call_file + DELTA else ''
        print(f'  0x{ins.address:08X}  {ins.mnemonic:8s} {ins.op_str}{marker}')
else:
    print('No prologue found')

# Also look at what comes right after the validate_func call
print()
print('Code after validate_func call (0xB4321C+5):')
after_off = call_file + 5
code2 = data[after_off:after_off+150]
for ins in list(cs.disasm(code2, after_off + DELTA))[:35]:
    print(f'  0x{ins.address:08X}  {ins.mnemonic:8s} {ins.op_str}')

# Also: look for where cipher+0x3C gets set to IV_dcy
# The IV_dcy = cd47af18e0d1c38cf1d8a067fc3dda28
# Search for these bytes (or significant sub-sequences) in evoerp.exe
iv_dcy = bytes.fromhex('cd47af18e0d1c38c')  # first 8 bytes
print(f'\nSearching for IV_dcy first 8 bytes {iv_dcy.hex()} in binary...')
pos = 0
while True:
    pos = data.find(iv_dcy, pos)
    if pos < 0:
        break
    print(f'  Found at file 0x{pos:X}  VA 0x{pos+DELTA:X}')
    pos += 1

# Search for IV_rwn
iv_rwn = bytes.fromhex('9cdac345a5f01c2c')  # first 8 bytes
print(f'\nSearching for IV_rwn first 8 bytes {iv_rwn.hex()} in binary...')
pos = 0
while True:
    pos = data.find(iv_rwn, pos)
    if pos < 0:
        break
    print(f'  Found at file 0x{pos:X}  VA 0x{pos+DELTA:X}')
    pos += 1
