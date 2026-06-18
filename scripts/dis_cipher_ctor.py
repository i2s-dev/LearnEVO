#!/usr/bin/env python3
"""Disassemble cipher constructor (0x750818) and find vtable[0x50] target.
Also scan for mode2_handler reference from vtable area near 0x74EB50."""
import capstone, struct
cs = capstone.Cs(capstone.CS_ARCH_X86, capstone.CS_MODE_32)
cs.detail = False
data = open(r'C:\ISTS\evoerp.exe', 'rb').read()
DELTA = 0x400C00

# Disassemble constructor at 0x750818 (file: 0x750818 - DELTA = 0x350218)
ctor_file = 0x750818 - DELTA
print('='*70)
print(f'Constructor 0x750818  file=0x{ctor_file:X}')
print('='*70)
for ins in list(cs.disasm(data[ctor_file:ctor_file+150], 0x750818))[:40]:
    print(f'  0x{ins.address:08X}  {ins.mnemonic:8s} {ins.op_str}')

# The class pointer lives at 0x74F25C
# In Delphi, a class reference IS the VMT pointer (points to VMT table)
# Read the VMT pointer from the binary's data section:
class_ptr_file = 0x74F25C - DELTA  # file offset of the global class reference word
print(f'\nclass_ptr global @ file 0x{class_ptr_file:X}  VA 0x74F25C')
class_ptr_val = struct.unpack_from('<I', data, class_ptr_file)[0]
print(f'  value = 0x{class_ptr_val:08X}  (this is the VMT base)')

# VMT[0x50] = 4-byte pointer at VMT_base + 0x50
vmt_file = class_ptr_val - DELTA
vmt_50_file = vmt_file + 0x50
method_va = struct.unpack_from('<I', data, vmt_50_file)[0]
method_file = method_va - DELTA
print(f'  VMT base file = 0x{vmt_file:X}')
print(f'  VMT[0x50] @ file 0x{vmt_50_file:X}  → VA 0x{method_va:08X}  file 0x{method_file:X}')
print(f'  This is the decrypt/read virtual method')

# Disassemble the virtual method at VMT[0x50]
print(f'\n{"="*70}')
print(f'vtable[0x50] method  VA=0x{method_va:08X}  file=0x{method_file:X}')
print('='*70)
for ins in list(cs.disasm(data[method_file:method_file+200], method_va))[:50]:
    print(f'  0x{ins.address:08X}  {ins.mnemonic:8s} {ins.op_str}')
