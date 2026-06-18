#!/usr/bin/env python3
"""
Check 0x40613c and 0x40633c - called on global object in SetStream.
These likely return (data_pointer, data_size) for the passphrase to SHA1-hash.
Also check 0x74F1D8 (called many times from SHA1_GetDigest) - likely byte swap.
Also look at 0x74C760 (called from SHA1_GetDigest).
Also find callers of 0x74EFDE (the function that calls vtable[0x48]=InitVector).
"""
import capstone, struct
cs = capstone.Cs(capstone.CS_ARCH_X86, capstone.CS_MODE_32)
cs.detail = False
data = open(r'C:\ISTS\evoerp.exe', 'rb').read()
DELTA = 0x400C00

for va_target, size, label in [
    (0x40613C, 60, '0x40613C (first call on global obj from SetStream)'),
    (0x40633C, 60, '0x40633C (second call on global obj from SetStream)'),
    (0x74F1D8, 30, '0x74F1D8 (called from SHA1_GetDigest — byte swap?)'),
    (0x74C760, 80, '0x74C760 (called from SHA1_GetDigest/Read)'),
]:
    file_off = va_target - DELTA
    code = data[file_off:file_off+size]
    print('='*70)
    print(f'{label}  file=0x{file_off:X}')
    for ins in list(cs.disasm(code, va_target))[:18]:
        highlight = ''
        if ins.mnemonic == 'ret': highlight = '  <-- RETURN'
        if ins.mnemonic == 'call': highlight = f'  [CALL]'
        print(f'  0x{ins.address:08X}  {ins.mnemonic:8s} {ins.op_str}{highlight}')
    print()

# Full SHA1_GetDigest (SR.vtable[0x44] = 0x74DAF4) continuation
# We saw it uses SR+0x40..0x50 (H0..H4) and SR+0x54 buffer
# Let's get more of it to understand what it outputs
print('='*70)
print('SHA1_GetDigest continued (0x74DAF4 + 80 bytes):')
va = 0x74DAF4
file_off = va - DELTA
code = data[file_off:file_off+350]
for ins in list(cs.disasm(code, va))[:80]:
    highlight = ''
    op = ins.op_str
    if ins.mnemonic == 'ret': highlight = '  <-- RETURN'
    if ins.mnemonic == 'call': highlight = f'  [CALL -> {op}]'
    if 'esp' in op and '+' in op:
        # Track what gets written to stack (= output buffer)
        highlight = '  ← writes to output buf?'
    print(f'  0x{ins.address:08X}  {ins.mnemonic:8s} {ins.op_str}{highlight}')

# Also: search for callers of 0x74EFDE (sets IV via vtable[0x48])
# Search for call 0x74EFDE in the binary
print()
print('='*70)
print('Searching for callers of 0x74EFDE (InitVector caller):')
target_bytes = b'\xe8'  # CALL opcode
target_va = 0x74EFDE
found = []
for off in range(0, len(data)-5):
    if data[off] == 0xe8:
        rel = struct.unpack_from('<i', data, off+1)[0]
        call_va = off + DELTA + 5 + rel
        if call_va == target_va:
            found.append(off + DELTA)
for caller_va in found:
    print(f'  Caller at VA 0x{caller_va:08X}  file 0x{caller_va - DELTA:X}')
if not found:
    print('  (none found — might be called via indirect call)')
