#!/usr/bin/env python3
"""Full disassembly of cipher_init (0x74E1F8) to see what IV it passes to SetKey."""
import capstone, struct
cs = capstone.Cs(capstone.CS_ARCH_X86, capstone.CS_MODE_32)
cs.detail = False
data = open(r'C:\ISTS\evoerp.exe', 'rb').read()
DELTA = 0x400C00

# cipher_init = 0x74E1F8
va = 0x74E1F8
file_off = va - DELTA
code = data[file_off:file_off+300]
print('='*70)
print(f'cipher_init  VA=0x{va:X}  file=0x{file_off:X}')
print('='*70)
for ins in list(cs.disasm(code, va))[:70]:
    highlight = ''
    op = ins.op_str
    if '0x3c' in op.lower(): highlight = '  *** P/block_buf'
    if '0x38' in op.lower(): highlight = '  *** buffer1'
    if ins.mnemonic == 'push': highlight = f'  <-- PUSH {op}'
    if ins.mnemonic == 'call': highlight = f'  [CALL -> {op}]'
    if ins.mnemonic == 'ret': highlight = '  <-- RETURN'
    print(f'  0x{ins.address:08X}  {ins.mnemonic:8s} {ins.op_str}{highlight}')

# Also disassemble validate_func (0xB43254) more fully to see cipher_init call
# From context: file offset = 0xB43254 - 0x400C00 = 0x742654
print()
print('='*70)
print('validate_func (0xB43254, file 0x742654):')
va2 = 0xB43254
file_off2 = 0x742654
code2 = data[file_off2:file_off2+250]
for ins in list(cs.disasm(code2, va2))[:55]:
    highlight = ''
    op = ins.op_str
    if '0x3c' in op.lower(): highlight = '  *** P/block_buf'
    if ins.mnemonic == 'push': highlight = f'  <-- PUSH {op}'
    if ins.mnemonic == 'call': highlight = f'  [CALL -> {op}]'
    if ins.mnemonic == 'ret': highlight = '  <-- RETURN'
    print(f'  0x{ins.address:08X}  {ins.mnemonic:8s} {ins.op_str}{highlight}')

# Also check: does the outer function (0xB4319C, file 0xB4319C - DELTA = 0x74259C)
# call cipher_init or some init function on the cipher object?
print()
print('='*70)
print('outer function (0xB4319C, file 0x74259C):')
va3 = 0xB4319C
file_off3 = va3 - DELTA
code3 = data[file_off3:file_off3+400]
for ins in list(cs.disasm(code3, va3))[:80]:
    highlight = ''
    op = ins.op_str
    if '0x3c' in op.lower(): highlight = '  *** P/block_buf'
    if ins.mnemonic == 'push': highlight = f'  <-- PUSH {op}'
    if ins.mnemonic == 'call': highlight = f'  [CALL -> {op}]'
    if ins.mnemonic == 'ret': highlight = '  <-- RETURN'
    print(f'  0x{ins.address:08X}  {ins.mnemonic:8s} {ins.op_str}{highlight}')
