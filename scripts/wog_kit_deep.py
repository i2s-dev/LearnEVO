#!/usr/bin/env python3
"""
wog_kit_deep.py — Deep analysis of LOAD.KIT and KIT.LIST in T7WOG.RWN

Goals:
1. Find ALL WOBOM variable indices (QTYISSUED, ^ISSUED, OPTION, TOTQTY, etc.)
2. Scan entire program for instructions referencing any WOBOM variable
3. Fully decode LOAD.KIT (3351-3413) with variable name resolution
4. Decode GOSUB targets one level deep
5. Find all DB_READ/DB_V + LOOP + IF + GOTO in kit-related procedures
6. Classify pool hits as code-blob vs form-binding-table
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

# Opcodes of interest
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

FLOW_OPS = {0x42, 0x3B, 0xD2, 0x19, 0x40, 0x71, 0x30, 0x34, 0x6A}
DB_OPS   = {0x9A, 0x5C, 0x0C}

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
        m12   = le32(raw53, 12)
        m16   = le32(raw53, 16)
        m20   = le32(raw53, 20)
        procs.append({'name': name, 'm12': m12, 'm16': m16, 'm20': m20})
    return procs

def pool_decode_blob(pool, off, var_names, limit=500):
    """Decode a pool blob into typed tokens. Returns list of (type, value) tuples."""
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
            results.append(('VAR', vi, vn))
            pos += 5
        elif t == 0x41:
            slen = le16(pool, pos+2)
            s = pool[pos+4:pos+4+slen].rstrip(b'\x00 ').decode('ascii', errors='replace')
            results.append(('STR', s))
            pos += 4 + slen
        elif t == 0x43:
            pi = le32(pool, pos+1)
            results.append(('PTR', pi))
            pos += 5
        elif t == 0x4E:
            results.append(('NUM', le32(pool, pos+1)))
            pos += 5
        elif t == 0x4C:
            results.append(('LBL', le32(pool, pos+1)))
            pos += 5
        elif t == 0x52:
            results.append(('REC', pool[pos+1:pos+5].hex()))
            pos += 5
        elif t in (0x44, 0x49, 0x4D, 0x53):
            results.append((f'K{t:02X}', le32(pool, pos+1)))
            pos += 5
        else:
            results.append(('RAW', f'{t:02X}'))
            pos += 1
    return results

def fmt_tokens(tokens, max_tokens=12):
    parts = []
    for tk in tokens[:max_tokens]:
        if tk[0] == 'VAR': parts.append(f'V:{tk[2]}')
        elif tk[0] == 'STR': parts.append(f'S:"{tk[1][:25]}"')
        elif tk[0] == 'PTR': parts.append(f'P@{tk[1]}')
        elif tk[0] == 'NUM': parts.append(f'N:{tk[1]}')
        elif tk[0] == 'LBL': parts.append(f'L:{tk[1]}')
        elif tk[0] == 'REC': parts.append(f'R:{tk[1]}')
        else: parts.append(f'{tk[0]}:{tk[1]}')
    return ' '.join(parts)

def find_wobom_vars(var_names):
    """Return dict of WOBOM.fieldname -> var_index for all WOBOM vars."""
    result = {}
    for i, name in enumerate(var_names):
        if name.startswith('WOBOM.') or name.startswith('WOBOM_'):
            result[name] = i
    return result

def build_var_pool_pattern(vi):
    ref = vi * VAR_ENTRY_SIZE
    return bytes([0x46]) + struct.pack('<I', ref)

def scan_pool_for_var(pool, vi):
    """Find all pool offsets where var vi is referenced."""
    pat = build_var_pool_pattern(vi)
    hits = []
    pos = 0
    while pos < len(pool) - 5:
        if pool[pos:pos+5] == pat:
            hits.append(pos)
        pos += 1
    return hits

def find_instrs_near_pool_offset(disp, n_instr, target_pool_off, window=3000):
    """Find all instruction indices whose poff is within `window` bytes before target."""
    result = []
    lo = max(0, target_pool_off - window)
    for i in range(n_instr):
        poff = le32(disp, i*8+4)
        if lo <= poff <= target_pool_off:
            result.append((i, poff))
    return result

def is_form_binding_blob(pool, poff):
    """
    Heuristic: form field-binding entries are 14-byte sequences:
      4E xx xx xx xx  (counter/seq NUM)
      46 xx xx xx xx  (var ref)
      43 xx xx xx xx  (pool ptr)
    If the blob at poff matches this pattern, it's likely a form binding, not code.
    """
    if poff + 14 > len(pool): return False
    return (pool[poff] == 0x4E and
            pool[poff+5] == 0x46 and
            pool[poff+10] == 0x43)

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
    print(f"Total instructions: {n_instr},  Variables: {len(var_names)},  Procedures: {len(procs)}")
    print(f"Pool starts at file offset 0x{pstart:X} ({pstart})")
    print()

    # --- Build procedure lookup maps ---
    proc_by_start = {}
    proc_list_sorted = []
    for p in procs:
        proc_by_start[p['m12']] = p['name']
        proc_list_sorted.append((p['m12'], p['name'], p))
    proc_list_sorted.sort()

    def proc_name_for_instr(idx):
        """Return the procedure name that contains instruction idx."""
        name = '?'
        for (st, nm, _) in proc_list_sorted:
            if st <= idx:
                name = nm
            else:
                break
        return name

    def next_proc_start(cur_start):
        """Return the start of the next procedure after cur_start."""
        for (st, nm, _) in proc_list_sorted:
            if st > cur_start:
                return st
        return n_instr

    # --- Find all WOBOM variables ---
    wobom_vars = find_wobom_vars(var_names)
    print("=" * 80)
    print("ALL WOBOM VARIABLES IN VAR TABLE")
    print("=" * 80)
    for name in sorted(wobom_vars.keys()):
        vi = wobom_vars[name]
        ref = vi * VAR_ENTRY_SIZE
        hits = scan_pool_for_var(pool, vi)
        print(f"  [{vi:4d}] {name:35s}  pool_ref={ref:6d}  pool_hits={len(hits):3d}  at={hits[:6]}")
    print()

    # --- For each WOBOM var, find which instructions reference it and in what context ---
    print("=" * 80)
    print("WOBOM VARIABLE REFERENCES BY INSTRUCTION (code blobs vs form bindings)")
    print("=" * 80)
    print()

    key_vars = ['WOBOM.OPTION', 'WOBOM.QTYISSUED', 'WOBOM.^ISSUED',
                'WOBOM.TOTQTY', 'WOBOM.WOPRE', 'WOBOM.WOSUF', 'WOBOM.COMPCODE',
                'WOBOM.ASSY', 'WOBOM.SEQ', 'WOBOM.OPER', 'WOBOM.FLAGS.1',
                'WOBOM.LOC', 'WOBOM.BINLOC']
    for vname in key_vars:
        if vname not in wobom_vars:
            # Try underscore variant
            alt = vname.replace('.', '_')
            if alt in wobom_vars:
                vname = alt
            else:
                print(f"  {vname}: NOT FOUND in var table")
                print()
                continue
        vi = wobom_vars[vname]
        hits = scan_pool_for_var(pool, vi)
        if not hits:
            print(f"  {vname}: 0 pool hits")
            print()
            continue

        print(f"  {vname} (var[{vi}]) — {len(hits)} pool hits:")
        for hit in hits:
            nearby = find_instrs_near_pool_offset(disp, n_instr, hit, window=2000)
            # Take the instruction whose poff is closest and <= hit
            if not nearby:
                print(f"    pool+{hit}: no nearby instruction")
                continue
            # Best = highest poff (closest)
            best_i, best_poff = max(nearby, key=lambda x: x[1])
            op    = disp[best_i*8]
            sub   = disp[best_i*8+3]
            opn   = OP_NAMES.get(op, f'OP_{op:02X}')
            pname = proc_name_for_instr(best_i)
            is_fb = is_form_binding_blob(pool, best_poff)
            context = "FORM-BINDING" if is_fb else "CODE"
            tokens = pool_decode_blob(pool, best_poff, var_names, limit=300)
            tok_s  = fmt_tokens(tokens, 8)
            print(f"    pool+{hit:6d}  instr[{best_i:5d}]  {opn:10s} sub={sub:02X}  proc={pname:20s}  [{context}]  {tok_s}")
        print()

    # --- Full decode of KIT.LIST (348-365) ---
    print("=" * 80)
    print("KIT.LIST FULL DECODE (instructions 348-365)")
    print("=" * 80)
    for idx in range(348, min(366, n_instr)):
        base = idx * 8
        op   = disp[base]; sub = disp[base+3]; poff = le32(disp, base+4)
        opn  = OP_NAMES.get(op, f'OP_{op:02X}')
        tokens = pool_decode_blob(pool, poff, var_names, limit=400) if poff < len(pool) else []
        tok_s  = fmt_tokens(tokens, 10)
        marker = ' <-- FLOW' if op in FLOW_OPS else (' <-- DB' if op in DB_OPS else '')
        if idx in proc_by_start:
            print(f"\n  --- PROC: {proc_by_start[idx]} ---")
        print(f"  [{idx:5d}] {op:02X}.{sub:02X}  {opn:10s}  pool@{poff:<8d}  {tok_s}{marker}")
    print()

    # --- Full decode of LOAD.KIT (3351-3413) ---
    print("=" * 80)
    print("LOAD.KIT FULL DECODE (instructions 3351-3413)")
    print("=" * 80)
    load_kit_end = next_proc_start(3351)
    print(f"  (next procedure starts at instr {load_kit_end})")
    for idx in range(3351, min(load_kit_end, n_instr)):
        base = idx * 8
        op   = disp[base]; sub = disp[base+3]; poff = le32(disp, base+4)
        opn  = OP_NAMES.get(op, f'OP_{op:02X}')
        tokens = pool_decode_blob(pool, poff, var_names, limit=600) if poff < len(pool) else []
        tok_s  = fmt_tokens(tokens, 12)
        marker = ''
        if op in DB_OPS:   marker = ' <-- DB'
        elif op in FLOW_OPS: marker = ' <-- FLOW'
        # Check if any token references a WOBOM var
        wobom_refs = [tk for tk in tokens if tk[0]=='VAR' and var_names[tk[1]].startswith('WOBOM')]
        if wobom_refs:
            marker += '  [WOBOM: ' + ','.join(var_names[tk[1]] for tk in wobom_refs) + ']'
        if idx in proc_by_start:
            print(f"\n  --- PROC: {proc_by_start[idx]} ---")
        print(f"  [{idx:5d}] {op:02X}.{sub:02X}  {opn:10s}  pool@{poff:<8d}  {tok_s}{marker}")

        # For GOSUB, try to follow one level deep
        if op == 0x42:
            # Look for a STR token in the blob — that would be the target proc name
            str_toks = [tk for tk in tokens if tk[0]=='STR']
            ptr_toks = [tk for tk in tokens if tk[0]=='PTR']
            lbl_toks = [tk for tk in tokens if tk[0]=='LBL']
            if str_toks:
                print(f"         => GOSUB target string: '{str_toks[0][1]}'")
            if ptr_toks:
                # Decode the pointed-to pool blob
                ptarget = ptr_toks[0][1]
                ptoks = pool_decode_blob(pool, ptarget, var_names, limit=200)
                print(f"         => GOSUB pool ptr P@{ptarget} -> {fmt_tokens(ptoks, 6)}")
    print()

    # --- Full decode of LOAD.KITA (2093-?) ---
    load_kita_start = None
    load_kita_end   = None
    for (st, nm, _) in proc_list_sorted:
        if nm == 'LOAD.KITA':
            load_kita_start = st
            load_kita_end   = next_proc_start(st)
            break
    if load_kita_start:
        print("=" * 80)
        print(f"LOAD.KITA FULL DECODE (instructions {load_kita_start}-{load_kita_end-1})")
        print("=" * 80)
        for idx in range(load_kita_start, min(load_kita_end, n_instr)):
            base = idx * 8
            op   = disp[base]; sub = disp[base+3]; poff = le32(disp, base+4)
            opn  = OP_NAMES.get(op, f'OP_{op:02X}')
            tokens = pool_decode_blob(pool, poff, var_names, limit=400) if poff < len(pool) else []
            tok_s  = fmt_tokens(tokens, 10)
            marker = ''
            if op in DB_OPS:   marker = ' <-- DB'
            elif op in FLOW_OPS: marker = ' <-- FLOW'
            wobom_refs = [tk for tk in tokens if tk[0]=='VAR' and var_names[tk[1]].startswith('WOBOM')]
            if wobom_refs:
                marker += '  [WOBOM: ' + ','.join(var_names[tk[1]] for tk in wobom_refs) + ']'
            if idx in proc_by_start:
                print(f"\n  --- PROC: {proc_by_start[idx]} ---")
            print(f"  [{idx:5d}] {op:02X}.{sub:02X}  {opn:10s}  pool@{poff:<8d}  {tok_s}{marker}")
    print()

    # --- Find ALL DB_READ (0x9A) and DB_V (0x5C) instructions that touch WOBOM ---
    print("=" * 80)
    print("ALL DB_READ / DB_V / DEL_REC INSTRUCTIONS REFERENCING WOBOM FIELDS")
    print("=" * 80)
    for idx in range(n_instr):
        base = idx * 8
        op   = disp[base]; sub = disp[base+3]; poff = le32(disp, base+4)
        if op not in DB_OPS: continue
        if poff >= len(pool): continue
        tokens = pool_decode_blob(pool, poff, var_names, limit=400)
        wobom_refs = [tk for tk in tokens if tk[0]=='VAR' and var_names[tk[1]].startswith('WOBOM')]
        if not wobom_refs: continue
        opn   = OP_NAMES.get(op, f'OP_{op:02X}')
        pname = proc_name_for_instr(idx)
        tok_s = fmt_tokens(tokens, 8)
        wobom_s = ','.join(var_names[tk[1]] for tk in wobom_refs)
        print(f"  [{idx:5d}] {opn:10s} sub={sub:02X}  proc={pname:22s}  WOBOM:[{wobom_s}]")
        print(f"         {tok_s}")
    print()

    # --- Find ALL LOOP (0x19) instructions in kit-related procedures ---
    print("=" * 80)
    print("ALL LOOP (0x19) INSTRUCTIONS — full program")
    print("=" * 80)
    for idx in range(n_instr):
        base = idx * 8
        op   = disp[base]; sub = disp[base+3]; poff = le32(disp, base+4)
        if op != 0x19: continue
        tokens = pool_decode_blob(pool, poff, var_names, limit=300) if poff < len(pool) else []
        opn   = OP_NAMES.get(op, f'OP_{op:02X}')
        pname = proc_name_for_instr(idx)
        tok_s = fmt_tokens(tokens, 8)
        print(f"  [{idx:5d}] {opn:10s} sub={sub:02X}  proc={pname:22s}  {tok_s}")
    print()

    # --- Find ALL GOTO (0xD2) and IF (0x3B) in LOAD.KIT and LOAD.KITA ---
    print("=" * 80)
    print("FLOW CONTROL (IF/GOTO/LABEL) IN LOAD.KIT + LOAD.KITA")
    print("=" * 80)
    kit_ranges = list(range(3351, min(load_kit_end, n_instr)))
    if load_kita_start and load_kita_end:
        kit_ranges += list(range(load_kita_start, min(load_kita_end, n_instr)))
    for idx in sorted(kit_ranges):
        base = idx * 8
        op   = disp[base]; sub = disp[base+3]; poff = le32(disp, base+4)
        if op not in (0x3B, 0xD2, 0x6A): continue
        tokens = pool_decode_blob(pool, poff, var_names, limit=300) if poff < len(pool) else []
        opn   = OP_NAMES.get(op, f'OP_{op:02X}')
        tok_s = fmt_tokens(tokens, 8)
        if idx in proc_by_start:
            print(f"\n  --- PROC: {proc_by_start[idx]} ---")
        print(f"  [{idx:5d}] {opn:10s} sub={sub:02X}  pool@{poff}  {tok_s}")
    print()

    # --- VLD_KITISSUE (1030-?) — validate kit issue ---
    vki_start = None
    for (st, nm, _) in proc_list_sorted:
        if nm == 'VLD_KITISSUE':
            vki_start = st
            break
    if vki_start:
        vki_end = next_proc_start(vki_start)
        print("=" * 80)
        print(f"VLD_KITISSUE FULL DECODE (instructions {vki_start}-{vki_end-1})")
        print("=" * 80)
        for idx in range(vki_start, min(vki_end, n_instr)):
            base = idx * 8
            op   = disp[base]; sub = disp[base+3]; poff = le32(disp, base+4)
            opn  = OP_NAMES.get(op, f'OP_{op:02X}')
            tokens = pool_decode_blob(pool, poff, var_names, limit=400) if poff < len(pool) else []
            tok_s  = fmt_tokens(tokens, 10)
            marker = ''
            if op in DB_OPS:   marker = ' <-- DB'
            elif op in FLOW_OPS: marker = ' <-- FLOW'
            wobom_refs = [tk for tk in tokens if tk[0]=='VAR' and var_names[tk[1]].startswith('WOBOM')]
            if wobom_refs:
                marker += '  [WOBOM: ' + ','.join(var_names[tk[1]] for tk in wobom_refs) + ']'
            if idx in proc_by_start:
                print(f"\n  --- PROC: {proc_by_start[idx]} ---")
            print(f"  [{idx:5d}] {op:02X}.{sub:02X}  {opn:10s}  pool@{poff:<8d}  {tok_s}{marker}")
    print()

    # --- Summary: WOBOM.QTYISSUED and WOBOM.^ISSUED referenced in code? ---
    print("=" * 80)
    print("SUMMARY: KEY WOBOM FIELDS — CODE vs FORM-BINDING CLASSIFICATION")
    print("=" * 80)
    key_interest = ['WOBOM.QTYISSUED', 'WOBOM.^ISSUED', 'WOBOM.OPTION', 'WOBOM.TOTQTY']
    for vname in key_interest:
        vi = wobom_vars.get(vname)
        if vi is None:
            print(f"  {vname}: NOT IN VAR TABLE")
            continue
        hits = scan_pool_for_var(pool, vi)
        code_hits = [(h, find_instrs_near_pool_offset(disp, n_instr, h, 2000))
                     for h in hits]
        code_count = 0
        form_count = 0
        for (h, nearby) in code_hits:
            if not nearby:
                continue
            best_i, best_poff = max(nearby, key=lambda x: x[1])
            if is_form_binding_blob(pool, best_poff):
                form_count += 1
            else:
                code_count += 1
        print(f"  {vname:35s}  total={len(hits):3d}  code_blobs={code_count:3d}  form_bindings={form_count:3d}")
    print()

if __name__ == '__main__':
    main()
