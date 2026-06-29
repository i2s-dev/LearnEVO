#!/usr/bin/env python3
"""
wog_deep2.py — Second-pass decode: all DB_READ, WHATSON, VLD_QTYISSUED, KIT.LIST chain.
Goal: identify the kit-list builder, the QTYISSUED validator, and how OPTION-key is passed.
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

def pool_decode_blob(pool, off, var_names, limit=500):
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

def fmt_tokens(tokens, max_tokens=14):
    parts = []
    for tk in tokens[:max_tokens]:
        if tk[0] == 'VAR':
            parts.append(f'V:{tk[2]}')
        elif tk[0] == 'STR':
            s = tk[1][:30].replace('\r','\\r').replace('\n','\\n')
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
    for idx in range(start, min(end, n_instr)):
        base = idx * 8
        op   = disp[base]; sub = disp[base+3]; poff = le32(disp, base+4)
        opn  = OP_NAMES.get(op, f'OP_{op:02X}')
        tokens = pool_decode_blob(pool, poff, var_names, 500) if poff < len(pool) else []
        tok_s  = fmt_tokens(tokens, 14)
        marker = ''
        if op in DB_OPS:   marker += ' <DB>'
        if op in FLOW_OPS: marker += ' <FLOW>'
        refs = [tk[2] for tk in tokens if tk[0]=='VAR' and
                any(f in tk[2] for f in ['WOBOM.','WOMAT.','MTWO.','WO.','BKWOG'])]
        if refs:
            marker += '  [' + ','.join(refs[:5]) + ']'
        if idx in proc_by_start:
            print(f"\n  --- PROC: {proc_by_start[idx]} ---")
        print(f"  [{idx:5d}] {op:02X}.{sub:02X}  {opn:12s}  p@{poff:<8d}  {tok_s}{marker}")

def main():
    data = read_file()
    hdr  = read_header(data)
    n_instr = hdr['dispatch_size'] // 8
    pstart  = DISPATCH_START + hdr['dispatch_size']
    pool    = data[pstart:]
    disp    = data[DISPATCH_START:DISPATCH_START + hdr['dispatch_size']]

    var_names = read_variables(data, hdr)
    procs     = read_procedures(data, hdr)
    proc_list = sorted(procs, key=lambda p: p['m12'])
    proc_by_start = {p['m12']: p['name'] for p in procs}

    # Build a name→range map
    proc_ranges = {}
    for i, p in enumerate(proc_list):
        end = proc_list[i+1]['m12'] if i+1 < len(proc_list) else n_instr
        proc_ranges[p['name']] = (p['m12'], end)

    def cur_proc(idx):
        nm = '?'
        for p in proc_list:
            if p['m12'] <= idx:
                nm = p['name']
            else:
                break
        return nm

    # ----------------------------------------------------------------
    # 1. ALL DB_READ (0x9A) INSTRUCTIONS
    # ----------------------------------------------------------------
    print("=" * 80)
    print("ALL DB_READ (0x9A) INSTRUCTIONS — table, key, WOBOM fields")
    print("=" * 80)
    db_read_count = 0
    for idx in range(n_instr):
        base = idx * 8
        op = disp[base]
        if op != 0x9A: continue
        sub  = disp[base+3]
        poff = le32(disp, base+4)
        tokens = pool_decode_blob(pool, poff, var_names, 500) if poff < len(pool) else []
        tok_s  = fmt_tokens(tokens, 16)
        pname  = cur_proc(idx)
        refs   = [tk[2] for tk in tokens if tk[0]=='VAR']
        str_ts = [tk[1] for tk in tokens if tk[0]=='STR']
        print(f"  [{idx:5d}] DB_READ sub={sub:02X}  proc={pname:25s}  {tok_s}")
        db_read_count += 1
    print(f"\nTotal DB_READ instructions: {db_read_count}")

    # ----------------------------------------------------------------
    # 2. ALL DB_V (0x5C) INSTRUCTIONS (navigate/read)
    # ----------------------------------------------------------------
    print("\n" + "=" * 80)
    print("ALL DB_V (0x5C) INSTRUCTIONS — with sub-opcode")
    print("=" * 80)
    dbv_count = 0
    for idx in range(n_instr):
        base = idx * 8
        op = disp[base]
        if op != 0x5C: continue
        sub  = disp[base+3]
        poff = le32(disp, base+4)
        tokens = pool_decode_blob(pool, poff, var_names, 500) if poff < len(pool) else []
        tok_s  = fmt_tokens(tokens, 14)
        pname  = cur_proc(idx)
        refs   = [tk[2] for tk in tokens if tk[0]=='VAR' and
                  any(f in tk[2] for f in ['WOBOM.','WOMAT.','MTWO.','WO.'])]
        marker = ('  ['+','.join(refs[:4])+']') if refs else ''
        print(f"  [{idx:5d}] DB_V sub={sub:02X}  proc={pname:25s}  {tok_s}{marker}")
        dbv_count += 1
    print(f"\nTotal DB_V instructions: {dbv_count}")

    # ----------------------------------------------------------------
    # 3. Decode WHATSON (strong candidate for kit list builder)
    # ----------------------------------------------------------------
    if 'WHATSON' in proc_ranges:
        s, e = proc_ranges['WHATSON']
        decode_range(disp, pool, var_names, proc_by_start, s, e, n_instr, "WHATSON")
    else:
        print("\nWHATSON not found")

    # ----------------------------------------------------------------
    # 4. Decode VLD_QTYISSUED (qty validator, may be 75405-3 freeze)
    # ----------------------------------------------------------------
    if 'VLD_QTYISSUED' in proc_ranges:
        s, e = proc_ranges['VLD_QTYISSUED']
        decode_range(disp, pool, var_names, proc_by_start, s, e, n_instr, "VLD_QTYISSUED")
    else:
        print("\nVLD_QTYISSUED not found")

    # ----------------------------------------------------------------
    # 5. Decode KIT.LIST (348-365) and show its GOSUB targets
    # ----------------------------------------------------------------
    if 'KIT.LIST' in proc_ranges:
        s, e = proc_ranges['KIT.LIST']
        decode_range(disp, pool, var_names, proc_by_start, s, e, n_instr, "KIT.LIST")
        # Resolve GOSUB targets
        print("\n  KIT.LIST GOSUB targets:")
        for idx in range(s, min(e, n_instr)):
            base = idx * 8
            op = disp[base]
            if op != 0x42: continue  # GOSUB
            poff = le32(disp, base+4)
            tokens = pool_decode_blob(pool, poff, var_names, 100)
            lbls = [tk for tk in tokens if tk[0]=='LBL']
            if lbls:
                target = lbls[0][1]
                tname  = proc_by_start.get(target, f'instr_{target}')
                print(f"    [{idx}] GOSUB -> {target} ({tname})")
    else:
        print("\nKIT.LIST not found")

    # ----------------------------------------------------------------
    # 6. Decode LINESGRID.SELEC (3300-3350) — selected line handler
    # ----------------------------------------------------------------
    if 'LINESGRID.SELEC' in proc_ranges:
        s, e = proc_ranges['LINESGRID.SELEC']
        decode_range(disp, pool, var_names, proc_by_start, s, e, n_instr, "LINESGRID.SELEC")
    else:
        print("\nLINESGRID.SELEC not found")

    # ----------------------------------------------------------------
    # 7. Decode LINESGRID.DISPL (3654-3676) — grid display proc
    # ----------------------------------------------------------------
    if 'LINESGRID.DISPL' in proc_ranges:
        s, e = proc_ranges['LINESGRID.DISPL']
        decode_range(disp, pool, var_names, proc_by_start, s, e, n_instr, "LINESGRID.DISPL")
    else:
        print("\nLINESGRID.DISPL not found")

    # ----------------------------------------------------------------
    # 8. Find procedures that contain LOOP (0x19) — any infinite-loop risk?
    # ----------------------------------------------------------------
    print("\n" + "=" * 80)
    print("ALL PROCEDURES CONTAINING LOOP (0x19) INSTRUCTIONS")
    print("=" * 80)
    loop_procs = {}
    for idx in range(n_instr):
        base = idx * 8
        if disp[base] != 0x19: continue
        pname = cur_proc(idx)
        if pname not in loop_procs:
            loop_procs[pname] = []
        loop_procs[pname].append(idx)
    for pname, idxs in sorted(loop_procs.items(), key=lambda kv: kv[1][0]):
        r = proc_ranges.get(pname, ('?','?'))
        print(f"  {pname:25s} (range {r[0]}-{r[1]-1 if isinstance(r[1],int) else '?'})  LOOP@{idxs}")

    # ----------------------------------------------------------------
    # 9. Decode WINPOS fully with expanded token output
    # ----------------------------------------------------------------
    if 'WINPOS' in proc_ranges:
        s, e = proc_ranges['WINPOS']
        decode_range(disp, pool, var_names, proc_by_start, s, e, n_instr, "WINPOS (full)")

    # ----------------------------------------------------------------
    # 10. Show JIT.WOBOM and NO.KIT* procedures if present
    # ----------------------------------------------------------------
    for pn in ('JIT.WOBOM', 'NO.KIT', 'NO.KIT.2', 'NO.KIT2', 'NO.KIT.Z'):
        if pn in proc_ranges:
            s, e = proc_ranges[pn]
            decode_range(disp, pool, var_names, proc_by_start, s, e, n_instr, pn)

if __name__ == '__main__':
    main()
