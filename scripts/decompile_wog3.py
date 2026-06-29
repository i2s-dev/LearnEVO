#!/usr/bin/env python3
"""
decompile_wog3.py — Fixed procedure layout + wide WOBOM.OPTION search
Outputs UTF-8.
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

def read_procedures(data, hdr):
    """
    Corrected procedure entry layout (53 bytes each):
      Bytes  0-11: zeros (3 DWORDs = 0)
      Bytes 12-15: DWORD m12 (proc start instruction index)
      Bytes 16-19: DWORD m16 (usually 02 00 00 00)
      Bytes 20-23: DWORD m20 (proc end instruction index?)
      Bytes 24-31: 8 bytes (2 more DWORDs)
      Byte  32:    name_length
      Bytes 33-47: name (up to 15 chars)
      Bytes 48-52: trailing bytes
    """
    vt_off   = len(data) - hdr['var_table_size']
    src_off  = vt_off - SRCNAME_SIZE
    proc_off = src_off - hdr['proc_size']
    count    = hdr['proc_size'] // PROC_ENTRY_SIZE
    procs    = []
    for i in range(count):
        eoff = proc_off + i * PROC_ENTRY_SIZE
        if eoff + PROC_ENTRY_SIZE > len(data): break
        raw53 = data[eoff:eoff+PROC_ENTRY_SIZE]
        nlen  = raw53[32]
        name  = raw53[33:33+min(nlen,15)].decode('ascii', errors='replace').rstrip('\x00 ')
        m12   = le32(raw53, 12)   # likely: start instruction index
        m16   = le32(raw53, 16)
        m20   = le32(raw53, 20)   # likely: instruction count or end index
        procs.append({'name': name, 'm12': m12, 'm16': m16, 'm20': m20, 'raw': raw53})
    return procs

OP_NAMES = {
    0x0F: 'ASSIGN',   0x8A: 'ASSIGN2',  0x37: 'ASGN_EX', 0x56: 'ASSIGN_V',
    0x42: 'GOSUB',    0x45: 'CALL_LIB2',0x16: 'CALL_LIB', 0xC0: 'CALL_V',
    0x3B: 'IF',       0x6A: 'LABEL',    0xD2: 'GOTO',    0x19: 'LOOP',
    0x93: 'FLD_ENTR', 0x20: 'CREATE',   0x57: 'EXEC_FRM',0xD1: 'FORM_OP',
    0x1A: 'EVAL',     0x40: 'EXIT',     0x71: 'EXIT2',   0x48: 'PUSH',
    0xDC: 'POP',      0x30: 'RETURN',   0x34: 'RETURN_V',0x15: 'TERMINATE',
    0x9A: 'DB_READ',  0x5C: 'DB_V',     0x2A: 'CALC',    0x1D: 'CALC_V',
    0x0C: 'DEL_REC',  0x25: 'PFMT',     0x22: 'PBLNK',
    0x29: 'ARR_INIT', 0x43: 'ARR_SUB',  0x47: 'ARR_ITER',
    0x44: 'EXEC_BGN', 0xC1: 'BLK_CLOSE',0x65: 'DATA_STR',
    0x06: 'FLD_READ', 0x08: 'FLD_WRIT', 0x31: 'GET_STAT',0x11: 'STAT_CHK',
    0x49: 'READ_PROP',0x89: 'GET_FLD',  0xB9: 'SET_FLD',
}

def pool_decode_blob(pool, off, var_names, limit=2000):
    results = []
    pos = off
    end = min(off + limit, len(pool))
    while pos < end:
        t = pool[pos]
        if t == 0xFF: break
        if t == 0xFD: pos += 1; continue
        if t == 0x46:
            vi = le32(pool, pos+1) // VAR_ENTRY_SIZE
            vn = var_names[vi] if vi < len(var_names) else f'v{vi}'
            results.append(f'V:{vn}')
            pos += 5
        elif t == 0x41:
            slen = le16(pool, pos+2)
            s = pool[pos+4:pos+4+slen].rstrip(b'\x00 ').decode('ascii', errors='replace')
            results.append(f'S:"{s[:30]}"')
            pos += 4 + slen
        elif t == 0x43:
            pi = le32(pool, pos+1)
            results.append(f'P@{pi}')
            pos += 5
        elif t == 0x4E:
            results.append(f'N:{le32(pool, pos+1)}')
            pos += 5
        elif t == 0x52:
            results.append(f'R:{pool[pos+1:pos+5].hex()}')
            pos += 5
        elif t == 0x4C:
            results.append(f'L:{le32(pool, pos+1)}')
            pos += 5
        elif t in (0x44, 0x49, 0x4D, 0x53):
            results.append(f'K{t:02X}:{le32(pool, pos+1)}')
            pos += 5
        else:
            results.append(f'?{t:02X}')
            pos += 1
    return results

def fmt_instr(idx, op, sub, poff, opn, blob_items, marker=''):
    blob_s = ' '.join(blob_items[:10])[:70]
    return f"  [{idx:5d}] {op:02X}.{sub:02X}  {opn:10s}  pool@{poff:<8d}  {blob_s}  {marker}"

def main():
    data = read_file()
    hdr  = read_header(data)
    n_instr = hdr['dispatch_size'] // 8
    pstart  = DISPATCH_START + hdr['dispatch_size']
    pool    = data[pstart:]
    disp    = data[DISPATCH_START:DISPATCH_START + hdr['dispatch_size']]

    var_names = read_variables(data, hdr)
    procs     = read_procedures(data, hdr)

    print(f"File: {DEC_FILE}")
    print(f"dispatch_size={hdr['dispatch_size']} => {n_instr} instructions, pool@0x{pstart:X}")
    print(f"Procedures: {len(procs)},  Variables: {len(var_names)}")
    print()

    # --- WOBOM.OPTION index ---
    option_vi = next((i for i, v in enumerate(var_names) if v == 'WOBOM.OPTION'), None)
    option_ref_val = option_vi * VAR_ENTRY_SIZE if option_vi else 0
    opt_pat = bytes([0x46]) + struct.pack('<I', option_ref_val)
    print(f"WOBOM.OPTION = var[{option_vi}], pool_ref = {option_ref_val} (0x{option_ref_val:X})")
    print(f"Search pattern: {opt_pat.hex()}")
    print()

    # Find all pool hits for WOBOM.OPTION
    pool_hits = []
    pos = 0
    while pos < len(pool) - 5:
        if pool[pos:pos+5] == opt_pat:
            pool_hits.append(pos)
        pos += 1
    print(f"WOBOM.OPTION pattern hits in pool: {pool_hits}")
    print()

    # For each hit, find instructions whose poff is in [hit-2000, hit]
    print("=" * 80)
    print("INSTRUCTIONS THAT COULD REFERENCE WOBOM.OPTION  (poff within 2000 bytes before hit)")
    print("=" * 80)
    candidate_instrs = set()
    for hit in pool_hits:
        for i in range(n_instr):
            poff = le32(disp, i*8+4)
            if hit - 2000 <= poff <= hit:
                candidate_instrs.add(i)
    print(f"Candidate instructions: {sorted(candidate_instrs)[:30]}")
    print()

    # Dump those instructions with wide blob scan
    for idx in sorted(candidate_instrs):
        base = idx * 8
        op   = disp[base]; sub = disp[base+3]; poff = le32(disp, base+4)
        opn  = OP_NAMES.get(op, f'OP_{op:02X}')
        blob = pool_decode_blob(pool, poff, var_names, limit=2000)
        # Show only up to and including first WOBOM.OPTION mention
        short = []
        for item in blob:
            short.append(item)
            if 'WOBOM.OPTION' in item:
                short.append('  <<< WOBOM.OPTION <<<')
                break
        print(fmt_instr(idx, op, sub, poff, opn, short))

    # --- Corrected procedure table ---
    print()
    print("=" * 80)
    print("PROCEDURE TABLE (fixed layout — name at byte 32)")
    print("m12 = start instr, m20 = likely end instr or count")
    print("=" * 80)
    proc_by_start = {}
    kit_proc_starts = {}
    for p in procs:
        proc_by_start[p['m12']] = p['name']
        if any(k in p['name'] for k in ['KIT','BOM','VLD_K','LOAD','ISSU','PROC.K',
                                          'EXPLODE','EXP.','NO.KIT','SORT_LIST',
                                          'PH.LOOP','JIT.WO','IS.WOBOM']):
            kit_proc_starts[p['m12']] = p
            print(f"  {p['name']:20s}  start={p['m12']:6d}  m16={p['m16']:6d}  m20={p['m20']:6d}")

    # --- Dump kit-section instructions ---
    print()
    print("=" * 80)
    print("KIT SECTION DISASSEMBLY")
    print("=" * 80)
    # Collect all kit instr ranges
    kit_ranges = set()
    sorted_starts = sorted(kit_proc_starts.keys())
    for i, st in enumerate(sorted_starts):
        p = kit_proc_starts[st]
        # End = next proc start OR start + m20 OR start + 200
        if i + 1 < len(sorted_starts):
            end = sorted_starts[i+1]
        elif p['m20'] > 0 and p['m20'] < n_instr:
            end = p['m20']
        else:
            end = st + 300
        for j in range(st, min(end, n_instr)):
            kit_ranges.add(j)

    for idx in sorted(kit_ranges):
        base = idx * 8
        op   = disp[base]; sub = disp[base+3]; poff = le32(disp, base+4)
        opn  = OP_NAMES.get(op, f'OP_{op:02X}')
        if poff < len(pool):
            blob = pool_decode_blob(pool, poff, var_names, limit=400)
        else:
            blob = []
        in_opt = idx in candidate_instrs
        marker = ' <<<OPTION>>>' if in_opt else ''
        # Mark proc boundaries
        if idx in proc_by_start:
            print(f"\n  --- [{idx}] PROC: {proc_by_start[idx]} ---")
        print(fmt_instr(idx, op, sub, poff, opn, blob, marker))

    # --- Raw pool dump around first WOBOM.OPTION hit ---
    print()
    print("=" * 80)
    if pool_hits:
        hit0 = pool_hits[0]
        lo = max(0, hit0 - 64)
        hi = min(len(pool), hit0 + 32)
        print(f"RAW POOL BYTES around hit at pool+{hit0} (pool+{lo} .. pool+{hi})")
        print("=" * 80)
        for row in range(lo, hi, 16):
            rend = min(row+16, hi)
            hex_s = ' '.join(f'{pool[b]:02X}' for b in range(row, rend))
            asc_s = ''.join(chr(pool[b]) if 0x20 <= pool[b] < 0x7F else '.' for b in range(row, rend))
            print(f"  pool+{row:6d}:  {hex_s:<47s}  {asc_s}")

    # Also dump raw pool around instruction 531 (known WOBOM.WOPRE reference)
    print()
    print("=" * 80)
    print("INSTR 531 (V:WOBOM.WOPRE context) — raw pool around pool@8827")
    print("=" * 80)
    ref531 = 8827
    for row in range(ref531, min(ref531+64, len(pool)), 16):
        rend = min(row+16, len(pool))
        hex_s = ' '.join(f'{pool[b]:02X}' for b in range(row, rend))
        asc_s = ''.join(chr(pool[b]) if 0x20 <= pool[b] < 0x7F else '.' for b in range(row, rend))
        print(f"  pool+{row:6d}:  {hex_s:<47s}  {asc_s}")

    # --- Dump all proc names to verify correctness ---
    print()
    print("=" * 80)
    print("ALL 330 PROCEDURE NAMES (fixed layout)")
    print("=" * 80)
    for p in procs:
        print(f"  {p['name']:25s}  start={p['m12']:6d}  m20={p['m20']:6d}")

if __name__ == '__main__':
    main()
