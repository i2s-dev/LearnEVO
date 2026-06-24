#!/usr/bin/env python3
"""Extract STRING pool entries from a decrypted RWN .dec file."""
import struct, sys, os

path = sys.argv[1] if len(sys.argv) > 1 else \
    r"C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\samples\rwn_decrypted\suwin6t.rwn.dec"

with open(path, "rb") as f:
    data = f.read()

DISP = 0x6C8
# Detect pool start: count instructions until b1 != 0x00
POOL_TYPES = {0x41, 0x46, 0x43, 0x4E, 0x52}
n = 0
off = DISP
while off + 8 <= len(data) and data[off+1] == 0x00:
    n += 1; off += 8
# Walk back if last instructions look like pool entries
while n > 0 and data[DISP + (n-1)*8] in POOL_TYPES:
    n -= 1
POOL = DISP + n * 8

print(f"File: {os.path.basename(path)} ({len(data)} bytes)")
print(f"Instructions: {n}, Pool at file 0x{POOL:04X} (program-rel 0x{POOL-8:04X})")
print()

OP_NAMES = {0x20:"CREATE/BIND", 0x49:"READ_PROP", 0x6A:"GOTO_LABEL", 0xD2:"GOTO",
            0x42:"GOSUB", 0x0F:"ASSIGN", 0x3B:"COND_BRANCH", 0x40:"EXIT",
            0x57:"EXEC_FORM", 0x15:"OP_15", 0x16:"OP_16"}

results = []
for i in range(n):
    ioff = DISP + i * 8
    op = data[ioff]
    sub = data[ioff+3]
    poff = struct.unpack_from("<I", data, ioff+4)[0]
    pabs = POOL + poff
    if pabs + 4 < len(data) and data[pabs] == 0x41 and data[pabs+1] == 0x00:
        strlen = struct.unpack_from("<H", data, pabs+2)[0]
        if 0 < strlen < 200 and pabs + 4 + strlen <= len(data):
            s = data[pabs+4:pabs+4+strlen].decode("latin-1", errors="replace")
            is_print = all(0x20 <= ord(c) <= 0x7E for c in s)
            nm = OP_NAMES.get(op, f"OP_{op:02X}")
            results.append((i, nm, poff, s, is_print))

print(f"Instructions referencing STRING pool entries: {len(results)}")
print()
print("=== Printable strings ===")
for i, nm, poff, s, is_print in results:
    if is_print:
        print(f"  [{i:3d}] {nm:<14} poff={poff:<6}  \"{s}\"")
