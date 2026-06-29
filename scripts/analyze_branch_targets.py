"""
analyze_branch_targets.py — Pass 378
Investigate RWN branch target encoding for COND_BRANCH(0x3B), GOTO(0xD2), GOSUB(0x42).

The pool_offset field in branch instructions is unknown — it might be:
  (A) byte offset from start of dispatch table
  (B) instruction index (instr# * 8 = byte offset)
  (C) byte offset from pool start (as in data ops)
  (D) absolute file offset

Strategy: parse the dispatch table, find all branch instructions, check if
pool_offset values land on valid instruction boundaries (multiple of 8 from
dispatch start). If theory B is correct, pool_offset should equal instr_index * 8.
If theory A, pool_offset should be divisible by 8 AND land within the dispatch range.
"""

import struct
import sys
import os
from collections import defaultdict

DEC_FILE = r"c:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\samples\src\T7FOD.RWN.dec"

# Branch opcodes
BRANCH_OPS = {0x3B: "COND_BRANCH", 0xD2: "GOTO", 0x42: "GOSUB/CALL", 0x6A: "GOTO_LABEL", 0x19: "LOOP"}
DATA_OPS = {0x0F: "ASSIGN", 0x20: "CREATE/BIND", 0x57: "EXECUTE_FORM"}

def parse_header(data):
    """Parse 128-byte RWN header (from decrypted .dec file — 8-byte prefix first)."""
    # .dec files have 8-byte validation prefix
    hdr_start = 8
    fields = {}
    for i in range(32):
        offset = hdr_start + i*4
        fields[i] = struct.unpack_from('<I', data, offset)[0]
    return fields, hdr_start

def find_dispatch_start(data):
    """Dispatch table starts at file offset 8 + 0x6C0 = 0x6C8 in .dec files."""
    return 8 + 0x6C0  # = 0x6C8

def parse_dispatch(data, dispatch_start, dispatch_size_bytes):
    """Parse dispatch table: each entry = [op,b1,b2,sub, poff:4LE]."""
    instrs = []
    n = dispatch_size_bytes // 8
    for i in range(n):
        off = dispatch_start + i * 8
        op, b1, b2, sub = struct.unpack_from('4B', data, off)
        poff = struct.unpack_from('<I', data, off + 4)[0]
        instrs.append((i, off, op, b1, b2, sub, poff))
    return instrs

def find_pool_start(data, dispatch_start, dispatch_size_bytes):
    """Pool starts immediately after dispatch table."""
    return dispatch_start + dispatch_size_bytes

def main():
    with open(DEC_FILE, 'rb') as f:
        data = f.read()

    print(f"File: {os.path.basename(DEC_FILE)}")
    print(f"Size: {len(data):,} bytes")

    hdr, hdr_start = parse_header(data)
    dispatch_size = hdr[0]  # hdr[0x00]
    proc_table_size = hdr[3]  # hdr[0x0C]
    var_count = hdr[5]  # hdr[0x14]
    var_table_size = hdr[8]  # hdr[0x20]
    proc_count = proc_table_size // 53

    print(f"\n=== HEADER ===")
    print(f"  dispatch_size_bytes = {dispatch_size} ({dispatch_size//8} instructions)")
    print(f"  proc_count          = {proc_count}")
    print(f"  var_count           = {var_count}")

    dispatch_start = find_dispatch_start(data)
    pool_start = find_pool_start(data, dispatch_start, dispatch_size)
    n_instrs = dispatch_size // 8

    print(f"\n=== LAYOUT ===")
    print(f"  dispatch_start = 0x{dispatch_start:04X} ({dispatch_start})")
    print(f"  pool_start     = 0x{pool_start:04X} ({pool_start})")
    print(f"  n_instrs       = {n_instrs}")

    instrs = parse_dispatch(data, dispatch_start, dispatch_size)

    # Frequency count
    freq = defaultdict(int)
    for _, _, op, b1, b2, sub, poff in instrs:
        freq[op] += 1

    print(f"\n=== TOP OPCODES ===")
    for op, cnt in sorted(freq.items(), key=lambda x: -x[1])[:20]:
        name = BRANCH_OPS.get(op, DATA_OPS.get(op, f"OP_0x{op:02X}"))
        print(f"  0x{op:02X}  {cnt:5d}  {name}")

    # Analyze branch target encoding
    print(f"\n=== BRANCH TARGET ANALYSIS ===")

    # Theory A: poff is byte offset from dispatch_start
    # Theory B: poff is instruction index (poff * 8 = byte offset from dispatch_start)
    # Theory C: poff is byte offset from pool_start (unlikely for branches)
    # Theory D: poff is absolute file offset

    for target_op in [0x3B, 0xD2, 0x42]:
        branch_instrs = [(i, off, op, poff) for i, off, op, b1, b2, sub, poff in instrs if op == target_op]
        if not branch_instrs:
            print(f"\n  0x{target_op:02X}: no occurrences")
            continue

        name = BRANCH_OPS.get(target_op, f"OP_{target_op:02X}")
        print(f"\n  0x{target_op:02X} {name}: {len(branch_instrs)} occurrences")

        # Sample first 20
        sample = branch_instrs[:20]

        # Check theory A: poff is byte offset from dispatch_start → target instr = poff/8
        # Valid if: poff % 8 == 0 AND 0 <= poff < dispatch_size
        a_valid = sum(1 for _, _, _, poff in branch_instrs if poff % 8 == 0 and 0 <= poff < dispatch_size)
        # Check theory B: poff is instruction index → target byte offset = poff * 8
        # Valid if: 0 <= poff < n_instrs
        b_valid = sum(1 for _, _, _, poff in branch_instrs if 0 <= poff < n_instrs)
        # Check theory D: absolute file offset
        # Valid if: dispatch_start <= poff < dispatch_start + dispatch_size AND poff % 8 == 0
        d_valid = sum(1 for _, _, _, poff in branch_instrs
                     if dispatch_start <= poff < dispatch_start + dispatch_size and
                     (poff - dispatch_start) % 8 == 0)

        print(f"    Theory A (byte offset from dispatch_start): {a_valid}/{len(branch_instrs)} consistent")
        print(f"    Theory B (instruction index):                {b_valid}/{len(branch_instrs)} consistent")
        print(f"    Theory D (absolute file offset):             {d_valid}/{len(branch_instrs)} consistent")

        print(f"    Sample (instr_idx, poff, theory_A_target, theory_B_target, theory_D_target):")
        for i, off, op, poff in sample:
            ta = poff // 8 if poff % 8 == 0 else "INVALID"
            tb = poff  # instruction index IS the target
            td = (poff - dispatch_start) // 8 if dispatch_start <= poff < dispatch_start + dispatch_size and (poff - dispatch_start) % 8 == 0 else "INVALID"
            print(f"      instr[{i:4d}]  poff=0x{poff:06X}={poff:7d}  A->{ta}  B->{tb}  D->{td}")

    # Additional: for GOTO_LABEL (0x6A), poff should point to a string in pool
    print(f"\n=== GOTO_LABEL POOL CHECK ===")
    label_instrs = [(i, poff) for i, off, op, b1, b2, sub, poff in instrs if op == 0x6A]
    if label_instrs:
        print(f"  0x6A GOTO_LABEL: {len(label_instrs)} occurrences")
        for i, poff in label_instrs[:10]:
            pool_abs = pool_start + poff
            if pool_abs < len(data) - 4:
                byte_at = data[pool_abs]
                # String entries start with 0x41
                if byte_at == 0x41:
                    # [0x41][flag][len_lo][len_hi][content]
                    flags = data[pool_abs + 1]
                    slen = struct.unpack_from('<H', data, pool_abs + 2)[0]
                    content = data[pool_abs + 4:pool_abs + 4 + min(slen, 40)].decode('latin-1', errors='replace')
                    print(f"    instr[{i:4d}]  poff=0x{poff:06X}  pool[{poff}] = 0x41 string({slen})={content!r}")
                else:
                    print(f"    instr[{i:4d}]  poff=0x{poff:06X}  pool[{poff}] = 0x{byte_at:02X} (NOT a string entry)")

    # ASSIGN pool check — should point to operand data
    print(f"\n=== ASSIGN OPERAND POOL CHECK (first 10) ===")
    assign_instrs = [(i, poff) for i, off, op, b1, b2, sub, poff in instrs if op == 0x0F][:10]
    for i, poff in assign_instrs:
        pool_abs = pool_start + poff
        if pool_abs < len(data) - 8:
            peek = data[pool_abs:pool_abs + 8].hex()
            print(f"    instr[{i:4d}]  poff=0x{poff:06X}={poff:7d}  pool bytes: {peek}")

if __name__ == '__main__':
    main()
