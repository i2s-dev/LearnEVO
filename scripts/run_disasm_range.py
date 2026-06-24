#!/usr/bin/env python3
"""Show instruction range from a .RUN disassembly — useful for Rosetta Stone alignment."""
import struct, sys, collections

path = sys.argv[1] if len(sys.argv) > 1 else "samples/BKAWLB.RUN"
start_i = int(sys.argv[2]) if len(sys.argv) > 2 else 0
end_i = int(sys.argv[3]) if len(sys.argv) > 3 else 200

# --- read file ---
with open(path, "rb") as f:
    data = f.read()

# locate tables (16-byte slots at 0x80)
TABLE_BASE = 0x80
tables = []
off = TABLE_BASE
while off + 16 <= len(data):
    chunk = data[off:off+16]
    name_bytes = []
    for b in chunk:
        if 0x20 <= b <= 0x7E:
            name_bytes.append(chr(b))
        else:
            break
    name = "".join(name_bytes).strip()
    if not name or len(name) < 2:
        break
    tables.append(name)
    off += 16

# find code section
TABLE_BASE = 0x80
var_table_start = TABLE_BASE + len(tables) * 16
MIN_RUN = 30
best_off = None
for start_off in range(var_table_start, min(var_table_start + 0x2000, len(data) - 200)):
    count = 0; off = start_off; ok = True
    while off + 7 <= len(data) and count < MIN_RUN:
        op = data[off]; b1 = data[off + 1]
        if b1 != 0x00 or op == 0x00: ok = False; break
        count += 1; off += 7
    if ok and count >= MIN_RUN:
        best_off = start_off; break

code_off = best_off

# collect all instructions
instr = []
addr_map = {}
off = code_off
while off + 7 <= len(data):
    op = data[off]; b1 = data[off+1]
    if b1 != 0x00: break
    b2 = data[off+2]
    addr = struct.unpack_from("<I", data, off+3)[0]
    instr.append((off, op, b2, addr))
    addr_map[off - code_off] = len(instr) - 1
    off += 7

# opcode table (confirmed .RUN)
KNOWN_OPS = {
    0x0F: "ASSIGN",     0x0E: "ENTER",     0x37: "TRAP",
    0x20: "RET_FUNC",   0x08: "TRAP_DFLT", 0xC0: "SET_PROP_CTX",
    0xC1: "ENT_BLOCK",  0x4B: "CALL_LIB",  0x39: "FUNC_PREPOST",
    0x01: "ARG_DESC",   0x1F: "OPEN_TBL",  0x13: "FIND_KEY",
    0x06: "CLR_REC",    0x1C: "MOUNT",     0x21: "MENU",
    0x73: "PRG_HDR",    0x49: "READ_PROP", 0x6A: "GOTO_LABEL",
    0x42: "GOSUB",      0x3B: "COND_JMP",
    # 0x53/0x65/0x93 cluster together (0x93+0x65x2+0x53+GOSUB per enter block); pfmt/pblnk are declarative (zero bytecode)
    0x53: "OP_53",      0x93: "OP_93",     0x65: "OP_65",
    0xBE: "PMSG?",      0x45: "FOR_OP",    0x8D: "OP_8D",
}

# opcode frequency in range
freq = collections.Counter()
for i, (off, op, b2, addr) in enumerate(instr[start_i:end_i]):
    freq[op] += 1

print(f"File: {path}  Code at 0x{code_off:04X}  Total: {len(instr)} instrs")
print(f"Showing instructions [{start_i}..{end_i})")
print()
print("Opcode freq in range:", dict(sorted(freq.items(), key=lambda x: -x[1])[:15]))
print()

for i in range(start_i, min(end_i, len(instr))):
    off, op, b2, addr = instr[i]
    rel = off - code_off
    nm = KNOWN_OPS.get(op, f"OP_{op:02X}")
    tgt = addr_map.get(addr)
    tgt_str = f"->I#{tgt}" if tgt is not None else f"addr=0x{addr:08X}"
    print(f"  [{i:4d}] +{rel:05X}  {op:02X} 00 {b2:02X}  {addr:08X}  {nm:<16}  {tgt_str}")
