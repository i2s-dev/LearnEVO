#!/usr/bin/env python3
"""
wog_winpos_decode.py — Decode WINPOS and LOAD.DO.POH fully, plus procedure list in order.
Focus: understand how partially-issued items affect the kit display flow.
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

def pool_decode_blob(pool, off, var_names, limit=400):
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
        if tk[0] == 'VAR':
            parts.append(f'V:{tk[2]}')
        elif tk[0] == 'STR':
            s = tk[1][:25].replace('\r','\\r').replace('\n','\\n')
            parts.append(f'S:"{s}"')
        elif tk[0] == 'PTR': parts.append(f'P@{tk[1]}')
        elif tk[0] == 'NUM': parts.append(f'N:{tk[1]}')
        elif tk[0] == 'LBL': parts.append(f'L:{tk[1]}')
        elif tk[0] == 'REC': parts.append(f'R:{tk[1]}')
        else: parts.append(f'{tk[0]}:{tk[1]}')
    return ' '.join(parts)

def decode_range(disp, pool, var_names, proc_by_start, start, end, n_instr, label):
    print(f"\n{'='*80}")
    print(f"{label} (instructions {start}-{end-1})")
    print(f"{'='*80}")
    wobom_fields = ['WOBOM.', 'WOMAT.', 'MTWO.']
    for idx in range(start, min(end, n_instr)):
        base = idx * 8
        op   = disp[base]; sub = disp[base+3]; poff = le32(disp, base+4)
        opn  = OP_NAMES.get(op, f'OP_{op:02X}')
        tokens = pool_decode_blob(pool, poff, var_names, 500) if poff < len(pool) else []
        tok_s  = fmt_tokens(tokens, 12)
        marker = ''
        if op in DB_OPS:   marker += ' <DB>'
        if op in FLOW_OPS: marker += ' <FLOW>'
        # Highlight WOBOM/WOMAT references
        refs = [tk[2] for tk in tokens if tk[0]=='VAR' and any(f in tk[2] for f in wobom_fields)]
        if refs:
            marker += '  [' + ','.join(refs[:4]) + ']'
        if idx in proc_by_start:
            print(f"\n  --- PROC: {proc_by_start[idx]} ---")
        print(f"  [{idx:5d}] {op:02X}.{sub:02X}  {opn:10s}  p@{poff:<8d}  {tok_s}{marker}")

def main():
    data = read_file()
    hdr  = read_header(data)
    n_instr = hdr['dispatch_size'] // 8
    pstart  = DISPATCH_START + hdr['dispatch_size']
    pool    = data[pstart:]
    disp    = data[DISPATCH_START:DISPATCH_START + hdr['dispatch_size']]

    var_names = read_variables(data, hdr)
    procs     = read_procedures(data, hdr)

    # Build sorted proc list
    proc_list = sorted(procs, key=lambda p: p['m12'])
    proc_by_start = {p['m12']: p['name'] for p in procs}

    # --- Print ALL procedures sorted by start, showing range ---
    print("=" * 80)
    print("ALL PROCEDURES SORTED BY START INSTRUCTION")
    print("=" * 80)
    for i, p in enumerate(proc_list):
        end = proc_list[i+1]['m12'] if i+1 < len(proc_list) else n_instr
        span = end - p['m12']
        print(f"  {p['m12']:6d}-{end-1:6d} ({span:4d}i)  {p['name']}")

    # --- Find WINPOS and LOAD.DO.POH ranges ---
    winpos_start = winpos_end = None
    loaddopoh_start = loaddopoh_end = None
    listgrid_start = listgrid_end = None
    nokitstart = nokitend = None

    for i, p in enumerate(proc_list):
        end = proc_list[i+1]['m12'] if i+1 < len(proc_list) else n_instr
        if p['name'] == 'WINPOS':
            winpos_start, winpos_end = p['m12'], end
        elif p['name'] == 'LOAD.DO.POH':
            loaddopoh_start, loaddopoh_end = p['m12'], end
        elif p['name'] == 'LIST_GRID':
            listgrid_start, listgrid_end = p['m12'], end
        elif p['name'] in ('NO.KIT', 'NO.KIT.2', 'NO.KIT2'):
            nokitstart, nokitend = p['m12'], end

    # --- Decode LOAD.DO.POH ---
    if loaddopoh_start is not None:
        decode_range(disp, pool, var_names, proc_by_start,
                     loaddopoh_start, loaddopoh_end, n_instr,
                     f"LOAD.DO.POH")
    else:
        print("\nLOAD.DO.POH not found in procedure table")

    # --- Decode WINPOS ---
    if winpos_start is not None:
        decode_range(disp, pool, var_names, proc_by_start,
                     winpos_start, winpos_end, n_instr,
                     f"WINPOS")
    else:
        print("\nWINPOS not found in procedure table")

    # --- Decode LIST_GRID ---
    if listgrid_start is not None:
        decode_range(disp, pool, var_names, proc_by_start,
                     listgrid_start, listgrid_end, n_instr,
                     f"LIST_GRID")
    else:
        print("\nLIST_GRID not found in procedure table")

    # --- Decode ISSU.KIT (the actual issue procedure) ---
    issukit_start = issukit_end = None
    for i, p in enumerate(proc_list):
        end = proc_list[i+1]['m12'] if i+1 < len(proc_list) else n_instr
        if p['name'] == 'ISSU.KIT':
            issukit_start, issukit_end = p['m12'], end
    if issukit_start:
        decode_range(disp, pool, var_names, proc_by_start,
                     issukit_start, issukit_end, n_instr,
                     f"ISSU.KIT")

    # --- Show all procedures in the 1400-2000 instruction range ---
    print("\n" + "=" * 80)
    print("PROCEDURES IN INSTRUCTION RANGE 1400-2200 (around WINPOS and LOAD.DO.POH)")
    print("=" * 80)
    for i, p in enumerate(proc_list):
        end = proc_list[i+1]['m12'] if i+1 < len(proc_list) else n_instr
        if p['m12'] >= 1400 and p['m12'] <= 2200:
            print(f"  {p['m12']:6d}-{end-1:6d} ({end-p['m12']:4d}i)  {p['name']}")

    # --- Look for procedures that reference WOBOM.QTYISSUED or WOBOM.OPTION ---
    print("\n" + "=" * 80)
    print("WHICH PROCEDURES CONTAIN DB_READ/DB_V TOUCHING WOBOM?")
    print("=" * 80)
    # Find WOBOM var indices
    option_vi  = next((i for i,v in enumerate(var_names) if v == 'WOBOM.OPTION'), None)
    qty_vi     = next((i for i,v in enumerate(var_names) if v == 'WOBOM.QTYISSUED'), None)
    totqty_vi  = next((i for i,v in enumerate(var_names) if v == 'WOBOM.TOTQTY'), None)
    pct_vi     = next((i for i,v in enumerate(var_names) if v == 'WOBOM.%ISSUED'), None)

    def cur_proc(idx):
        nm = '?'
        for p in proc_list:
            if p['m12'] <= idx:
                nm = p['name']
            else:
                break
        return nm

    interesting_procs = set()
    for idx in range(n_instr):
        base = idx * 8
        op = disp[base]
        if op not in DB_OPS: continue
        poff = le32(disp, base+4)
        if poff >= len(pool): continue
        tokens = pool_decode_blob(pool, poff, var_names, 300)
        var_ids = [tk[1] for tk in tokens if tk[0]=='VAR']
        if any(vi in var_ids for vi in [option_vi, qty_vi, totqty_vi, pct_vi] if vi is not None):
            pname = cur_proc(idx)
            interesting_procs.add(pname)
            opn = OP_NAMES.get(op, f'OP_{op:02X}')
            refs = [var_names[vi] for vi in var_ids if var_names[vi].startswith('WOBOM.')]
            print(f"  [{idx:5d}] {opn:10s}  proc={pname:25s}  WOBOM:{refs}")

    # --- Look for DB_READ instructions anywhere that might use OPTION as filter ---
    print("\n" + "=" * 80)
    print("ALL DB_READ (0x9A) INSTRUCTIONS — which table, which key?")
    print("=" * 80)
    for idx in range(n_instr):
        base = idx * 8
        op = disp[base]; sub = disp[base+3]; poff = le32(disp, base+4)
        if op != 0x9A: continue
        tokens = pool_decode_blob(pool, poff, var_names, 400) if poff < len(pool) else []
        pname = cur_proc(idx)
        tok_s = fmt_tokens(tokens, 10)
        print(f"  [{idx:5d}] DB_READ sub={sub:02X}  proc={pname:25s}  {tok_s}")

if __name__ == '__main__':
    main()
