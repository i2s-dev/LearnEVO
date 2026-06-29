"""
analyze_branch_targets2.py — Pass 378 Phase 2
Look at pool bytes at poff for COND_BRANCH, GOSUB, and GOTO instructions.
The goal: understand how branch targets are encoded inside compound pool records.
"""

import struct
import sys
import os

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
        instrs.append((i, off, op, b1, b2, sub, poff))
    return instrs

def pool_peek(data, pool_start, poff, nbytes=24):
    abs_off = pool_start + poff
    if abs_off >= len(data):
        return None
    return data[abs_off:min(abs_off + nbytes, len(data))]

def decode_pool_bytes(raw):
    """Try to decode pool bytes as compound expression components."""
    parts = []
    i = 0
    while i < len(raw):
        b = raw[i]
        if b == 0x41:  # String entry: [0x41][flags:1][len:2LE][content...]
            if i + 4 > len(raw):
                parts.append(f"<TRUNC:0x41>")
                break
            flags = raw[i+1]
            slen = struct.unpack_from('<H', raw, i+2)[0]
            content_end = i + 4 + slen
            content = raw[i+4:min(content_end, len(raw))].decode('latin-1', errors='replace')
            parts.append(f"STR({slen},f={flags:#x})={content!r}")
            i = content_end
        elif b == 0x46:  # F-type: var reference, [0x46][flags:1][size:2LE][content...]
            if i + 4 > len(raw):
                parts.append(f"<TRUNC:0x46>")
                break
            flags = raw[i+1]
            slen = struct.unpack_from('<H', raw, i+2)[0]
            content = raw[i+4:min(i+4+slen, len(raw))].hex()
            try:
                ctext = raw[i+4:min(i+4+slen, len(raw))].decode('latin-1', errors='replace')
            except:
                ctext = '?'
            parts.append(f"F-type({slen},f={flags:#x})={content}={ctext!r}")
            i = i + 4 + slen
        elif b == 0x43:  # C-type: pool pointer/context
            if i + 4 > len(raw):
                parts.append(f"<TRUNC:0x43>")
                break
            flags = raw[i+1]
            slen = struct.unpack_from('<H', raw, i+2)[0]
            content = raw[i+4:min(i+4+slen, len(raw))].hex()
            parts.append(f"C-type({slen},f={flags:#x})={content}")
            i = i + 4 + slen
        elif b == 0x4E:  # N-type: numeric
            if i + 4 > len(raw):
                parts.append(f"<TRUNC:0x4E>")
                break
            flags = raw[i+1]
            slen = struct.unpack_from('<H', raw, i+2)[0]
            content = raw[i+4:min(i+4+slen, len(raw))].hex()
            parts.append(f"N-type({slen})={content}")
            i = i + 4 + slen
        elif b == 0x00:
            # skip nulls
            i += 1
        elif b in (0xFF, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0A):
            parts.append(f"ctrl:0x{b:02X}")
            i += 1
        else:
            # Unknown byte
            parts.append(f"?{b:02X}")
            i += 1
        if len(parts) > 8:
            parts.append("...")
            break
    return " | ".join(parts) if parts else "(empty)"

def main():
    with open(DEC_FILE, 'rb') as f:
        data = f.read()

    hdr = parse_header(data)
    dispatch_size = hdr[0]
    dispatch_start = 8 + 0x6C0
    pool_start = dispatch_start + dispatch_size
    n_instrs = dispatch_size // 8

    instrs = parse_dispatch(data, dispatch_start, n_instrs)

    print(f"dispatch_start=0x{dispatch_start:04X}  pool_start=0x{pool_start:04X}  n={n_instrs}")
    print()

    op_names = {
        0x0F: "ASSIGN", 0x42: "GOSUB", 0x3B: "COND_BRANCH",
        0xD2: "GOTO", 0x6A: "GOTO_LABEL", 0x19: "LOOP",
        0x20: "CREATE", 0x57: "EXEC_FORM", 0x40: "EXIT",
        0x48: "PUSH", 0xDC: "POP", 0x45: "CALL_LIB2"
    }

    # ANALYSIS 1: Look at all COND_BRANCH pool data and look for patterns
    # Specifically: does the poff point to a multi-word compound record that
    # might end with a 4-byte LE integer (the branch target address)?
    print("=== COND_BRANCH pool bytes (first 20 occurrences) ===")
    cb_instrs = [(i, op, sub, poff) for i, off, op, b1, b2, sub, poff in instrs if op == 0x3B]
    for idx, (i, op, sub, poff) in enumerate(cb_instrs[:20]):
        raw = pool_peek(data, pool_start, poff)
        if raw is None:
            print(f"  [{i:4d}] poff={poff:6d} OUT_OF_RANGE")
            continue
        hex_raw = raw.hex()
        desc = decode_pool_bytes(raw)
        print(f"  [{i:4d}] poff={poff:6d}=0x{poff:05X}  {hex_raw[:48]}")
        print(f"         {desc}")

    print()
    print("=== GOSUB pool bytes — is poff a proc name or compound? ===")
    gs_instrs = [(i, op, sub, poff) for i, off, op, b1, b2, sub, poff in instrs if op == 0x42]
    for idx, (i, op, sub, poff) in enumerate(gs_instrs[:15]):
        raw = pool_peek(data, pool_start, poff)
        if raw is None:
            print(f"  [{i:4d}] poff={poff:6d} OUT_OF_RANGE")
            continue
        hex_raw = raw.hex()
        desc = decode_pool_bytes(raw)
        print(f"  [{i:4d}] poff={poff:6d}=0x{poff:05X}  {hex_raw[:48]}")
        print(f"         {desc}")

    print()
    print("=== GOTO pool bytes ===")
    goto_instrs = [(i, op, sub, poff) for i, off, op, b1, b2, sub, poff in instrs if op == 0xD2]
    for idx, (i, op, sub, poff) in enumerate(goto_instrs[:10]):
        raw = pool_peek(data, pool_start, poff, 32)
        if raw is None:
            print(f"  [{i:4d}] poff={poff:6d} OUT_OF_RANGE")
            continue
        hex_raw = raw.hex()
        desc = decode_pool_bytes(raw)
        print(f"  [{i:4d}] poff={poff:6d}=0x{poff:05X}  {hex_raw[:48]}")
        print(f"         {desc}")

    print()
    print("=== COND_BRANCH: look for pattern where poff+offset = small integer ===")
    print("    Testing: does poff point to compound expr that has a 4-byte target at the end?")
    for idx, (i, op, sub, poff) in enumerate(cb_instrs[:30]):
        raw = pool_peek(data, pool_start, poff, 64)
        if raw is None: continue
        # Find the first 0x41 string entry and skip past it — branch target might follow
        j = 0
        while j < len(raw):
            b = raw[j]
            if b == 0x41:
                if j + 4 <= len(raw):
                    slen = struct.unpack_from('<H', raw, j+2)[0]
                    j = j + 4 + slen
                else:
                    j += 1
            elif b == 0x46:
                if j + 4 <= len(raw):
                    slen = struct.unpack_from('<H', raw, j+2)[0]
                    j = j + 4 + slen
                else:
                    j += 1
            elif b == 0x43:
                if j + 4 <= len(raw):
                    slen = struct.unpack_from('<H', raw, j+2)[0]
                    j = j + 4 + slen
                else:
                    j += 1
            elif b == 0x4E:
                if j + 4 <= len(raw):
                    slen = struct.unpack_from('<H', raw, j+2)[0]
                    j = j + 4 + slen
                else:
                    j += 1
            else:
                break
        # At offset j, what do we have?
        if j < len(raw) - 3:
            val4 = struct.unpack_from('<I', raw, j)[0]
            val2 = struct.unpack_from('<H', raw, j)[0]
            print(f"  [{i:4d}] poff={poff:6d} after_expr_offset={j} bytes4=0x{val4:08X}={val4} (is it a branch target?)")

if __name__ == '__main__':
    main()
