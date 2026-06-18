#!/usr/bin/env python3
"""Check the 192-bit key branch in SetKey (0x74FBDE) and look for IV init."""
import capstone
cs = capstone.Cs(capstone.CS_ARCH_X86, capstone.CS_MODE_32)
cs.detail = False
data = open(r'C:\ISTS\evoerp.exe', 'rb').read()
DELTA = 0x400C00

# 192-bit branch = 0x74FBDE
# Also check what's at 0x74FE2A (256-bit) and 0x7501B7 (fallthrough)
for va_target, size, label in [
    (0x74FBDE, 300, '192-bit key branch'),
    (0x7501B7, 80, 'SetKey tail / fallthrough'),
]:
    file_off = va_target - DELTA
    code = data[file_off:file_off+size]
    print(f'{"="*70}')
    print(f'{label}  VA=0x{va_target:X}  file=0x{file_off:X}')
    for ins in list(cs.disasm(code, va_target))[:60]:
        highlight = ''
        op = ins.op_str
        if '0x3c' in op.lower(): highlight = '  *** cipher+0x3C'
        if '0x40' in op and 'eax' in op: highlight = '  *** obj+0x40?'
        if ins.mnemonic == 'ret': highlight = '  <-- RETURN'
        print(f'  0x{ins.address:08X}  {ins.mnemonic:8s} {ins.op_str}{highlight}')
    print()

# Also let me check: is there a SetIV (or SetBlock) VMT slot we haven't looked at?
# VMT layout: [0x2C]=ctor, [0x38]=GetKeySize, [0x40]=SetKey, [0x50]=Decrypt, [0x54]=returns128, [0x58]=EncryptBlock
# What about [0x44], [0x48], [0x4C]?
print('='*70)
print('VMT slots between SetKey (0x40) and Decrypt (0x50):')
file_off = 0x74F2A8 - DELTA  # VMT base found in prior session
code = data[file_off:file_off+16*4]
import struct
for i in range(16):
    slot_va = 0x74F2A8 + i*4
    fn_va = struct.unpack_from('<I', data, file_off + i*4)[0]
    print(f'  VMT[0x{i*4:02X}] = 0x{fn_va:08X}  (slot at 0x{slot_va:X})')
    if i*4 == 0x5C:
        print('  -- end of mapped VMT --')
