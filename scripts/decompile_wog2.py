#!/usr/bin/env python3
"""
decompile_wog2.py -- Targeted decompiler for T7WOG.RWN.dec
Outputs UTF-8 text to stdout (pipe to file for full output).

Approach:
  1. Read var table, proc table
  2. Binary-scan pool for WOBOM.OPTION reference pattern (0x46 + LE32(14938))
  3. For each dispatch instruction pointing to a pool blob containing WOBOM.OPTION,
     dump the surrounding 10 instructions with full decoded operands
  4. Also scan string pool for label names (LOAD.KIT, KIT.LIST, etc.)
     to find where those sections live in the dispatch table
  5. Dump proc table metadata to diagnose offset encoding
"""

import struct, sys, os

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
sys.stderr.reconfigure(encoding='utf-8', errors='replace')

DEC_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                        'samples', 'rwn_decrypted', 'T7WOG.RWN.dec')

PROC_ENTRY_SIZE = 53
VAR_ENTRY_SIZE  = 77
SRCNAME_SIZE    = 60
DISPATCH_START  = 0x6C0

def le32(b, off):
    if off + 4 > len(b): return 0
    return struct.unpack_from('<I', b, off)[0]

def le16(b, off):
    if off + 2 > len(b): return 0
    return struct.unpack_from('<H', b, off)[0]

def read_file():
    raw = open(DEC_FILE, 'rb').read()
    if len(raw) >= 8 and raw[0:4] == raw[4:8]:
        return raw[8:]
    return raw

def read_header(data):
    return {
        'dispatch_size': le32(data, 0x00),
        'proc_size':     le32(data, 0x0C),
        'var_count':     le32(data, 0x14),
        'var_table_size':le32(data, 0x20),
    }

def read_variables(data, hdr):
    vt_off = len(data) - hdr['var_table_size']
    names = []
    for i in range(hdr['var_count']):
        off = vt_off + i * VAR_ENTRY_SIZE
        if off + VAR_ENTRY_SIZE > len(data): break
        b0 = data[off]
        raw = data[off+1:off+15] if b0 < 0x20 else data[off:off+15]
        names.append(raw.rstrip(b'\x00 ').decode('ascii', errors='replace'))
    return names

def read_procedures_raw(data, hdr):
    """Returns list of (name, raw_53_bytes) for each proc entry."""
    vt_off   = len(data) - hdr['var_table_size']
    src_off  = vt_off - SRCNAME_SIZE
    proc_off = src_off - hdr['proc_size']
    count    = hdr['proc_size'] // PROC_ENTRY_SIZE
    procs = []
    for i in range(count):
        eoff = proc_off + i * PROC_ENTRY_SIZE
        if eoff + PROC_ENTRY_SIZE > len(data): break
        nlen = data[eoff]
        name = data[eoff+1:eoff+1+min(nlen, 15)].decode('ascii', errors='replace').rstrip('\x00 ')
        raw  = data[eoff:eoff+PROC_ENTRY_SIZE]
        procs.append((name, raw))
    return procs

def pool_decode_blob(pool, off, var_names):
    """Walk a pool blob from offset `off`, return list of decoded tokens."""
    results = []
    pos = off
    limit = min(off + 256, len(pool))
    while pos < limit:
        t = pool[pos]
        if t == 0xFF: break
        if t == 0xFD:
            pos += 1; continue
        if t == 0x46:  # var ref
            vi = le32(pool, pos+1) // VAR_ENTRY_SIZE
            vn = var_names[vi] if vi < len(var_names) else f'var{vi}'
            results.append(f'V:{vn}')
            pos += 5
        elif t == 0x41:  # string
            slen = le16(pool, pos+2)
            s = pool[pos+4:pos+4+slen].rstrip(b'\x00 ').decode('ascii', errors='replace')
            results.append(f'S:"{s}"')
            pos += 4 + slen
        elif t == 0x43:  # pool ptr
            pi = le32(pool, pos+1)
            results.append(f'P@{pi}')
            pos += 5
        elif t == 0x4E:  # numeric
            results.append(f'N:{le32(pool, pos+1)}')
            pos += 5
        elif t == 0x52:  # real
            results.append(f'R:0x{pool[pos+1:pos+5].hex()}')
            pos += 5
        elif t == 0x4C:  # logical
            results.append(f'L:{le32(pool, pos+1)}')
            pos += 5
        elif t == 0x44:  # date?
            results.append(f'D:{le32(pool, pos+1)}')
            pos += 5
        elif t == 0x49:  # int?
            results.append(f'I:{le32(pool, pos+1)}')
            pos += 5
        elif t == 0x4D:
            results.append(f'M:{le32(pool, pos+1)}')
            pos += 5
        elif t == 0x53:
            results.append(f'X:{le32(pool, pos+1)}')
            pos += 5
        else:
            results.append(f'?{t:02X}')
            pos += 1
    return results

OP_NAMES = {
    0x0F: 'ASSIGN',   0x8A: 'ASSIGN2',  0x37: 'ASSIGN_EXPR', 0x56: 'ASSIGN_V',
    0x42: 'GOSUB',    0x45: 'CALL_LIB2',0x16: 'CALL_LIB',    0xC0: 'CALL_V',
    0x3B: 'IF',       0x6A: 'LABEL',    0xD2: 'GOTO',        0x19: 'LOOP',
    0x93: 'FIELD_ENT',0x20: 'CREATE',   0x57: 'EXEC_FORM',   0xD1: 'FORM_OP',
    0x1A: 'EVAL',     0x40: 'EXIT',     0x71: 'EXIT2',       0x48: 'PUSH',
    0xDC: 'POP',      0x30: 'RETURN',   0x34: 'RETURN_V',    0x15: 'TERMINATE',
    0x9A: 'DB_READ',  0x5C: 'DB_V',     0x2A: 'CALC',        0x1D: 'CALC_V',
    0x0C: 'DEL_REC',  0x25: 'PFMT',     0x22: 'PBLNK',
    0x29: 'ARRAY_INIT',0x43: 'ARRAY_SUB',0x47: 'ARRAY_ITER',
    0x44: 'EXEC_BGN', 0xC1: 'BLK_CLOSE',0x65: 'DATA_STRUCT',
    0x06: 'FLD_READ', 0x08: 'FLD_WRITE',0x31: 'GET_STAT',    0x11: 'STAT_CHK',
    0x49: 'READ_PROP',0x89: 'GET_FIELD',0xB9: 'SET_FIELD',
}


def decode_instr(disp, idx, pool, var_names):
    base = idx * 8
    if base + 8 > len(disp): return None
    op   = disp[base]
    b1   = disp[base+1]
    b2   = disp[base+2]
    sub  = disp[base+3]
    poff = le32(disp, base+4)
    opn  = OP_NAMES.get(op, f'OP_{op:02X}')
    blob = pool_decode_blob(pool, poff, var_names) if poff < len(pool) else []
    return (idx, op, b1, b2, sub, poff, opn, blob)

def fmt_instr(t):
    idx, op, b1, b2, sub, poff, opn, blob = t
    blob_s = ' '.join(blob[:8])
    return f"  [{idx:5d}] {op:02X}.{sub:02X}  {opn:12s}  pool@{poff:<7d} {blob_s}"

def main():
    data = read_file()
    hdr  = read_header(data)
    n_instr = hdr['dispatch_size'] // 8

    print(f"File: {DEC_FILE}")
    print(f"Size: {len(data):,} bytes (stripped)")
    print(f"dispatch_size={hdr['dispatch_size']} => {n_instr} instructions")
    print(f"proc_size={hdr['proc_size']} => {hdr['proc_size']//53} procs")
    print(f"var_count={hdr['var_count']}, var_table_size={hdr['var_table_size']}")
    pstart = DISPATCH_START + hdr['dispatch_size']
    print(f"pool starts at file offset 0x{pstart:X} ({pstart})")
    print()

    var_names = read_variables(data, hdr)
    procs_raw = read_procedures_raw(data, hdr)

    print(f"Variables loaded: {len(var_names)}")
    print(f"Procedures loaded: {len(procs_raw)}")
    print()

    # Confirm WOBOM.OPTION index
    option_vi = None
    for i, vn in enumerate(var_names):
        if vn == 'WOBOM.OPTION':
            option_vi = i
            break
    option_pool_bytes = option_vi * VAR_ENTRY_SIZE if option_vi else 0
    print(f"WOBOM.OPTION = var[{option_vi}]  pool_ref_offset = {option_pool_bytes} (0x{option_pool_bytes:X})")
    print()

    # --- Section 1: Dump all proc entries with ALL metadata bytes ----------
    print("=" * 80)
    print("PROCEDURE TABLE -- all entries matching KIT/BOM/WOBOM")
    print("Format: [idx] name | meta bytes (hex)")
    print("=" * 80)
    kit_proc_indices = {}
    for i, (pname, raw53) in enumerate(procs_raw):
        kw = any(k in pname for k in ['KIT','BOM','WOBOM','VLD_K','LOAD','ISSU',
                                       'PROC.KIT','EXPLODE','EXP.BOM','NO.KIT',
                                       'SORT','XLOOP','ELOOP','PH.LOOP'])
        if kw or True:  # dump all to understand metadata layout
            meta = raw53[16:53]
            m_hex = ' '.join(f'{b:02X}' for b in meta)
            m0 = le32(meta, 0)
            m4 = le32(meta, 4)
            m8 = le32(meta, 8)
            if kw:
                print(f"[{i:3d}] {pname:20s}  m0={m0:8d} m4={m4:8d} m8={m8:8d}  hex={m_hex}")
                kit_proc_indices[pname] = i

    print()

    # --- Section 2: FIRST FEW proc entries full dump to calibrate layout --
    print("=" * 80)
    print("FIRST 10 PROCEDURE ENTRIES -- raw hex to calibrate metadata layout")
    print("=" * 80)
    for i, (pname, raw53) in enumerate(procs_raw[:10]):
        hex_str = ' '.join(f'{b:02X}' for b in raw53)
        print(f"[{i:2d}] {pname:20s}  {hex_str}")
    print()

    # --- Section 3: Find WOBOM.OPTION pattern in pool --------------------
    pool = data[pstart:]
    disp = data[DISPATCH_START:DISPATCH_START + hdr['dispatch_size']]

    # Pattern: 0x46 followed by LE32 of (option_vi * 77)
    opt_pattern = bytes([0x46]) + struct.pack('<I', option_pool_bytes)
    print("=" * 80)
    print(f"WOBOM.OPTION pattern search in pool: {opt_pattern.hex()}")
    print("=" * 80)

    # Find all pool offsets containing this pattern
    option_pool_hits = []
    pos = 0
    while pos < len(pool) - 5:
        if pool[pos:pos+5] == opt_pattern:
            option_pool_hits.append(pos)
        pos += 1
    print(f"Pattern found {len(option_pool_hits)} times in pool at offsets: {option_pool_hits[:30]}")
    print()

    # For each dispatch instruction, check if its pool blob contains any of these offsets
    # A blob starting at poff that contains the pattern at poff+k
    # We need: poff <= hit_pos < poff + ~200
    # Faster: build set of pool offsets that lead to a blob with WOBOM.OPTION
    option_poffs = set()
    for i in range(n_instr):
        base  = i * 8
        poff  = le32(disp, base+4)
        if poff >= len(pool): continue
        # Scan the blob from poff for the pattern
        limit = min(poff + 300, len(pool) - 5)
        found = False
        for p in option_pool_hits:
            if poff <= p < limit:
                found = True
                break
        if found:
            option_poffs.add(poff)

    # Now find all instructions with those poffs
    option_instrs = []
    for i in range(n_instr):
        poff = le32(disp, i*8+4)
        if poff in option_poffs:
            option_instrs.append(i)

    print(f"Instructions referencing WOBOM.OPTION: {len(option_instrs)}")
    print(f"  indices: {option_instrs[:50]}")
    print()

    # --- Section 4: Dump instructions around each WOBOM.OPTION reference --
    print("=" * 80)
    print("WOBOM.OPTION REFERENCE CONTEXT -- +/-8 instructions around each hit")
    print("=" * 80)
    shown = set()
    for hit_idx in option_instrs:
        lo = max(0, hit_idx - 8)
        hi = min(n_instr, hit_idx + 12)
        if lo in shown: continue
        print(f"\n  --- Context around instr [{hit_idx}] ---")
        for idx in range(lo, hi):
            t = decode_instr(disp, idx, pool, var_names)
            if t:
                marker = " <<<<< WOBOM.OPTION" if idx in option_instrs else ""
                print(fmt_instr(t) + marker)
            shown.add(idx)

    # --- Section 5: Find label strings in pool ----------------------------
    print()
    print("=" * 80)
    print("LABEL / KEYWORD STRINGS IN POOL")
    print("=" * 80)
    label_targets = [
        'LOAD.KIT', 'LOAD.KIT2', 'LOAD.KITA', 'KIT.LIST',
        'ISSU.KIT', 'ISSU.KITA', 'ISSU.KIT2', 'VLD_KITISSUE',
        'PROC.KIT', 'JIT.WOBOM', 'EXPLODE_BOM', 'EXP.BOM',
        'PH.LOOP.TEST', 'NO.KIT.2', 'NO.KIT.Z', 'SORT_LIST',
        'WOBOM.OPTION', '1', '',
    ]
    for label in label_targets:
        # Search pool for string entry containing this label
        lb = label.encode('ascii')
        pos = 0
        while pos < len(pool) - len(lb) - 4:
            if pool[pos] == 0x41:
                slen = le16(pool, pos+2)
                s_raw = pool[pos+4:pos+4+slen]
                if s_raw.rstrip(b'\x00 ') == lb:
                    pool_off = pos
                    # Find instructions referencing this pool offset
                    ref_instrs = []
                    for i in range(n_instr):
                        poff = le32(disp, i*8+4)
                        # Check if any blob from poff reaches this string
                        if poff <= pool_off < poff + 200:
                            ref_instrs.append(i)
                    print(f"  String '{label}' @ pool+{pool_off}: referenced by instrs {ref_instrs[:10]}")
                    break
            pos += 1
        else:
            # Also search as raw substring (in case no 0x41 header)
            idx2 = pool.find(lb)
            if idx2 > 0:
                print(f"  String '{label}' found raw @ pool+{idx2} (no 0x41 header)")

    # --- Section 6: Scan for GOSUB to known labels -----------------------
    print()
    print("=" * 80)
    print("ALL GOSUB (0x42) instructions -- show target")
    print("=" * 80)
    gosub_count = 0
    for i in range(n_instr):
        base = i * 8
        op   = disp[base]
        if op == 0x42:  # GOSUB
            poff = le32(disp, base+4)
            blob = pool_decode_blob(pool, poff, var_names) if poff < len(pool) else []
            bs   = ' '.join(blob[:5])
            print(f"  [{i:5d}] GOSUB  pool@{poff:<7d}  {bs}")
            gosub_count += 1
    print(f"Total GOSUB: {gosub_count}")

if __name__ == '__main__':
    main()
