"""
analyze_branch_targets3.py — Pass 378 Phase 3
THEORY E: All branch instructions are LABEL-BASED (symbolic), not address-based.

Hypothesis:
  - GOTO_LABEL (0x6A): defines a label position; poff -> pool string = label name
  - GOTO (0xD2): jumps to a named label; poff -> pool string (or compound) = label name
  - GOSUB (0x42): calls a proc by name; poff -> pool string = proc name
  - COND_BRANCH (0x3B): "if condition then goto label"; poff -> compound record with condition+label

If label-based:
  - GOTO pool poff should contain the SAME strings as GOTO_LABEL pool poffs
  - A GOTO for label "X" should have a corresponding GOTO_LABEL for label "X"

Steps:
  1. Extract all GOTO_LABEL poffs, read pool strings -> build label_definitions dict
  2. Extract all GOTO poffs, read pool strings/bytes -> extract readable text -> check in label_definitions
  3. Extract all GOSUB poffs, read pool strings -> should be proc names (no GOTO_LABEL equivalent)
  4. Extract COND_BRANCH poffs, read compound bytes -> look for embedded label name strings
"""

import struct
import sys
import os
from collections import defaultdict

DEC_FILE = r"c:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\samples\src\T7FOD.RWN.dec"

def parse_header(data):
    hdr_start = 8
    fields = {}
    for i in range(32):
        offset = hdr_start + i*4
        fields[i] = struct.unpack_from('<I', data, offset)[0]
    return fields

def parse_dispatch(data, dispatch_start, n):
    instrs = []
    for i in range(n):
        off = dispatch_start + i * 8
        op, b1, b2, sub = struct.unpack_from('4B', data, off)
        poff = struct.unpack_from('<I', data, off + 4)[0]
        instrs.append((i, op, b1, b2, sub, poff))
    return instrs

def read_pool_string(data, pool_start, poff):
    """Read pool entry at poff. If it's a 0x41 string entry, return the string.
    Otherwise return None."""
    abs_off = pool_start + poff
    if abs_off >= len(data):
        return None
    b = data[abs_off]
    if b == 0x41:
        if abs_off + 4 > len(data):
            return None
        flags = data[abs_off + 1]
        slen = struct.unpack_from('<H', data, abs_off + 2)[0]
        if abs_off + 4 + slen > len(data):
            return None
        return data[abs_off + 4:abs_off + 4 + slen].decode('latin-1', errors='replace')
    return None

def find_strings_in_pool(data, pool_start, poff, max_bytes=128):
    """Scan pool bytes at poff, extract all 0x41 strings found within."""
    abs_off = pool_start + poff
    if abs_off >= len(data):
        return []
    raw = data[abs_off:min(abs_off + max_bytes, len(data))]
    strings = []
    i = 0
    while i < len(raw):
        b = raw[i]
        if b == 0x41:
            if i + 4 <= len(raw):
                slen = struct.unpack_from('<H', raw, i+2)[0]
                end = i + 4 + slen
                if end <= len(raw):
                    s = raw[i+4:end].decode('latin-1', errors='replace')
                    strings.append(s)
                i = end
            else:
                i += 1
        elif b in (0x46, 0x43, 0x4E):
            if i + 4 <= len(raw):
                slen = struct.unpack_from('<H', raw, i+2)[0]
                i = i + 4 + slen
            else:
                i += 1
        elif b == 0x00:
            i += 1
        else:
            i += 1
    return strings

def pool_hex(data, pool_start, poff, nbytes=24):
    abs_off = pool_start + poff
    if abs_off >= len(data):
        return "(OOB)"
    return data[abs_off:min(abs_off+nbytes, len(data))].hex()

def main():
    with open(DEC_FILE, 'rb') as f:
        data = f.read()

    hdr = parse_header(data)
    dispatch_size = hdr[0]
    dispatch_start = 8 + 0x6C0
    pool_start = dispatch_start + dispatch_size
    n_instrs = dispatch_size // 8

    print(f"File: {os.path.basename(DEC_FILE)}")
    print(f"dispatch_start=0x{dispatch_start:04X}  pool_start=0x{pool_start:04X}  n_instrs={n_instrs}")
    print()

    instrs = parse_dispatch(data, dispatch_start, n_instrs)

    # === STEP 1: Extract GOTO_LABEL definitions ===
    print("=== GOTO_LABEL (0x6A) definitions — label positions ===")
    label_defs = {}  # label_name -> instr_index
    label_defs_by_poff = {}
    goto_label_instrs = [(i, poff) for i, op, b1, b2, sub, poff in instrs if op == 0x6A]
    print(f"  Total GOTO_LABELs: {len(goto_label_instrs)}")
    for i, poff in goto_label_instrs:
        s = read_pool_string(data, pool_start, poff)
        pool_bytes = pool_hex(data, pool_start, poff, 20)
        if s:
            label_defs[s.strip()] = i
            label_defs_by_poff[poff] = s.strip()
            print(f"  instr[{i:4d}]  poff={poff:6d}  label={s.strip()!r}")
        else:
            strings_found = find_strings_in_pool(data, pool_start, poff)
            print(f"  instr[{i:4d}]  poff={poff:6d}  NOT a direct string  bytes={pool_bytes}  embedded_strings={strings_found}")

    # === STEP 2: Extract GOTO targets ===
    print()
    print("=== GOTO (0xD2) targets — should reference defined labels ===")
    goto_instrs = [(i, poff) for i, op, b1, b2, sub, poff in instrs if op == 0xD2]
    print(f"  Total GOTOs: {len(goto_instrs)}")
    match_count = 0
    for i, poff in goto_instrs:
        s = read_pool_string(data, pool_start, poff)
        if s:
            s_stripped = s.strip()
            matched = s_stripped in label_defs
            if matched:
                match_count += 1
                target_instr = label_defs[s_stripped]
                direction = "FWD" if target_instr > i else "BWD"
                print(f"  instr[{i:4d}] GOTO poff={poff:6d} -> label={s_stripped!r} -> GOTO_LABEL instr[{target_instr}] ({direction}) MATCHED")
            else:
                print(f"  instr[{i:4d}] GOTO poff={poff:6d} -> label={s_stripped!r} -- NOT in label_defs")
        else:
            pool_bytes = pool_hex(data, pool_start, poff, 32)
            strings_found = find_strings_in_pool(data, pool_start, poff)
            print(f"  instr[{i:4d}] GOTO poff={poff:6d} NOT direct string  bytes={pool_bytes[:48]}  found_strings={strings_found}")
    print(f"  GOTO label matches: {match_count}/{len(goto_instrs)}")

    # === STEP 3: GOSUB proc names ===
    print()
    print("=== GOSUB (0x42) proc name check — first 20 ===")
    gosub_instrs = [(i, poff) for i, op, b1, b2, sub, poff in instrs if op == 0x42]
    print(f"  Total GOSUBs: {len(gosub_instrs)}")
    proc_names = set()
    for i, poff in gosub_instrs[:20]:
        s = read_pool_string(data, pool_start, poff)
        if s:
            proc_names.add(s.strip())
            print(f"  instr[{i:4d}] GOSUB poff={poff:6d} -> proc={s.strip()!r}")
        else:
            strings_found = find_strings_in_pool(data, pool_start, poff)
            pool_bytes = pool_hex(data, pool_start, poff, 24)
            print(f"  instr[{i:4d}] GOSUB poff={poff:6d} NOT direct string  bytes={pool_bytes}  found_strings={strings_found}")

    # === STEP 4: COND_BRANCH — look for embedded label name within compound record ===
    print()
    print("=== COND_BRANCH (0x3B) — extract all strings in compound record ===")
    cond_instrs = [(i, poff) for i, op, b1, b2, sub, poff in instrs if op == 0x3B]
    print(f"  Total COND_BRANCHes: {len(cond_instrs)}")
    cb_match = 0
    cb_no_label_string = 0
    for i, poff in cond_instrs[:50]:
        strings_found = find_strings_in_pool(data, pool_start, poff)
        # Check if any found string matches a defined label
        matches = [s for s in strings_found if s.strip() in label_defs]
        if matches:
            cb_match += 1
            print(f"  instr[{i:4d}] COND_BRANCH poff={poff:6d} strings={strings_found} LABEL_MATCHES={matches}")
        else:
            cb_no_label_string += 1
            if len(strings_found) > 0:
                print(f"  instr[{i:4d}] COND_BRANCH poff={poff:6d} strings={strings_found} (no label match)")
            else:
                pool_bytes = pool_hex(data, pool_start, poff, 24)
                print(f"  instr[{i:4d}] COND_BRANCH poff={poff:6d} NO_STRINGS  bytes={pool_bytes}")

    print()
    print(f"COND_BRANCH summary (first 50): {cb_match} with label string, {cb_no_label_string} without")

    # === STEP 5: Check if GOTO poffs that didn't match directly have embedded label strings ===
    print()
    print("=== GOTO with non-direct-string poffs: check embedded strings ===")
    for i, poff in goto_instrs:
        s = read_pool_string(data, pool_start, poff)
        if s is None:
            strings_found = find_strings_in_pool(data, pool_start, poff)
            matches = [s for s in strings_found if s.strip() in label_defs]
            if matches:
                print(f"  instr[{i:4d}] GOTO poff={poff:6d} embedded label={matches}")

if __name__ == '__main__':
    main()
