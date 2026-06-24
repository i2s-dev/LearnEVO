#!/usr/bin/env python3
"""Full analysis of a decrypted RWN .dec file — all instructions + pool layout."""
import struct, sys, os, collections

path = sys.argv[1] if len(sys.argv) > 1 else \
    r"C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\samples\rwn_decrypted\suwin6t.rwn.dec"

with open(path, "rb") as f:
    data = f.read()

DISP = 0x6C8
POOL_TYPE_NAMES = {0x41:"STRING", 0x46:"FLOAT", 0x43:"INT", 0x4E:"NAME", 0x52:"REAL"}

# Count instructions (walk back trailing pool-type ops)
POOL_TYPES = {0x41, 0x46, 0x43, 0x4E, 0x52}
n = 0
off = DISP
while off + 8 <= len(data) and data[off+1] == 0x00:
    n += 1; off += 8
while n > 0 and data[DISP + (n-1)*8] in POOL_TYPES:
    n -= 1
POOL = DISP + n * 8

print(f"File: {os.path.basename(path)} ({len(data)} bytes)")
print(f"Instructions: {n}, Pool offset file=0x{POOL:04X}")
print()

OP_NAMES = {
    0x20:"CREATE/BIND", 0x49:"READ_PROP", 0x6A:"GOTO_LABEL", 0xD2:"GOTO",
    0x42:"GOSUB", 0x0F:"ASSIGN", 0x3B:"COND_BRANCH", 0x40:"EXIT",
    0x57:"EXEC_FORM", 0x71:"EXIT2", 0x4B:"CALL_LIB", 0x4A:"OP_4A",
    0x15:"OP_15", 0x16:"OP_16",
}

# --- Instruction frequency ---
ops = []
for i in range(n):
    ioff = DISP + i * 8
    op = data[ioff]; b1 = data[ioff+1]; b2 = data[ioff+2]; sub = data[ioff+3]
    poff = struct.unpack_from("<I", data, ioff+4)[0]
    ops.append((i, op, b1, b2, sub, poff))

freq = collections.Counter(op for _,op,_,_,_,_ in ops)
print("=== Opcode frequency ===")
for op, cnt in freq.most_common():
    nm = OP_NAMES.get(op, f"OP_{op:02X}")
    print(f"  {op:02X}  {nm:<18}  {cnt:4d}")
print()

# --- Pool layout scan ---
pool_entries = []  # (prel_offset, type_byte, size_or_payload)
ppos = 0
pool_data = data[POOL:]
while ppos + 2 <= len(pool_data):
    t = pool_data[ppos]
    if t not in POOL_TYPES:
        break
    if t == 0x41:  # STRING: [41][00][len_LE2][bytes]
        if ppos + 4 > len(pool_data): break
        slen = struct.unpack_from("<H", pool_data, ppos+2)[0]
        if slen > 1000 or ppos + 4 + slen > len(pool_data): break
        s = pool_data[ppos+4:ppos+4+slen].decode("latin-1", errors="replace")
        pool_entries.append((ppos, t, slen, s[:80]))
        ppos += 4 + slen
    elif t == 0x46:  # FLOAT: [46][00][4 bytes]
        v = struct.unpack_from("<f", pool_data, ppos+2)[0] if ppos+6 <= len(pool_data) else 0
        pool_entries.append((ppos, t, 6, f"{v:.6g}"))
        ppos += 6
    elif t == 0x43:  # INT: [43][00][2 bytes]
        v = struct.unpack_from("<h", pool_data, ppos+2)[0] if ppos+4 <= len(pool_data) else 0
        pool_entries.append((ppos, t, 4, str(v)))
        ppos += 4
    elif t == 0x4E:  # NAME: [4E][00][len_LE2][bytes]
        if ppos + 4 > len(pool_data): break
        slen = struct.unpack_from("<H", pool_data, ppos+2)[0]
        if slen > 1000 or ppos + 4 + slen > len(pool_data): break
        s = pool_data[ppos+4:ppos+4+slen].decode("latin-1", errors="replace")
        pool_entries.append((ppos, t, slen, s[:80]))
        ppos += 4 + slen
    elif t == 0x52:  # REAL: [52][00][8 bytes]
        v = struct.unpack_from("<d", pool_data, ppos+2)[0] if ppos+10 <= len(pool_data) else 0
        pool_entries.append((ppos, t, 10, f"{v:.10g}"))
        ppos += 10
    else:
        break

print(f"=== Pool layout ({len(pool_entries)} entries, pool data {len(pool_data)} bytes) ===")
for prel, t, sz, val in pool_entries[:100]:
    tn = POOL_TYPE_NAMES.get(t, f"T{t:02X}")
    print(f"  pool[{prel:5d}]  {tn:<7}  {val}")
print()

# --- All instructions that have pool-byte-offset pointing to a valid pool entry ---
pool_entry_offsets = {e[0] for e in pool_entries}
print("=== Instructions with poff matching a pool entry boundary ===")
for i, op, b1, b2, sub, poff in ops:
    if poff in pool_entry_offsets:
        nm = OP_NAMES.get(op, f"OP_{op:02X}")
        pabs = POOL + poff
        t = data[pabs] if pabs < len(data) else 0
        tn = POOL_TYPE_NAMES.get(t, f"T{t:02X}")
        # Get value string
        val = ""
        for pe in pool_entries:
            if pe[0] == poff:
                val = str(pe[3])[:60]; break
        print(f"  [{i:3d}] OP_{op:02X} {nm:<18} poff={poff:<6}  {tn}: {val}")
print()

# --- Dump first 80 instructions raw ---
print("=== First 80 instructions (raw) ===")
for i, op, b1, b2, sub, poff in ops[:80]:
    nm = OP_NAMES.get(op, f"OP_{op:02X}")
    print(f"  [{i:3d}] {op:02X} {b1:02X} {b2:02X} {sub:02X}  poff={poff:<8}  {nm}")
