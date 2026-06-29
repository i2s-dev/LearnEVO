#!/usr/bin/env python3
"""
decompile_wog.py — Targeted decompiler for T7WOG.RWN.dec

Focuses on:
  - Full variable name table (indexed by var_index)
  - Procedure table with dispatch offsets
  - Pool section string/value extraction
  - All instructions with decoded operands
  - Highlighted: WOBOM.OPTION references and LOAD.KIT / KIT.LIST sections

Usage:
    python scripts/decompile_wog.py > out.txt
"""

import struct
import sys
import re
import os

DEC_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                        'samples', 'rwn_decrypted', 'T7WOG.RWN.dec')

# Opcode names (from rwn-binary-format.md)
OP_NAMES = {
    0x0F: 'ASSIGN',
    0x8A: 'ASSIGN2',
    0x37: 'ASSIGN_EXPR',
    0x56: 'ASSIGN_V',
    0x42: 'GOSUB',
    0x45: 'CALL_LIB2',
    0x16: 'CALL_LIB',
    0xC0: 'CALL_V',
    0x3B: 'COND_BRANCH',
    0x6A: 'GOTO_LABEL',
    0xD2: 'GOTO',
    0x19: 'LOOP',
    0x93: 'FIELD_ENTER',
    0x20: 'CREATE_BIND',
    0x57: 'EXEC_FORM',
    0xD1: 'FORM_OP',
    0x29: 'FORM_OP2',
    0x44: 'FORM_OP3',
    0x1A: 'EVAL',
    0x40: 'EXIT',
    0x71: 'EXIT2',
    0x49: 'READ_PROP',
    0x0C: 'READ_V',
    0xCC: 'READ_V2',
    0xC6: 'READ_V3',
    0x06: 'FIELD_READ',
    0x08: 'FIELD_WRITE',
    0xB7: 'FIELD_V',
    0xBD: 'FIELD_V2',
    0x2B: 'FIELD_V3',
    0x31: 'GET_STATUS',
    0xD3: 'STATUS_V',
    0x11: 'STATUS_CHK',
    0xCD: 'STATUS_V2',
    0x48: 'PUSH',
    0xDC: 'POP',
    0xC7: 'PUSH_V',
    0x4B: 'OPEN_FORM',
    0x4A: 'READ_V4',
    0x43: 'ARRAY_SUB',
    0x47: 'ARRAY_ITER',
    0x46: 'HANDLE_V',
    0x89: 'GET_FIELD',
    0xB9: 'SET_FIELD',
    0x30: 'RETURN',
    0x34: 'RETURN_V',
    0x15: 'TERMINATE',
    0x9A: 'DB_READ',
    0x5C: 'DB_V',
    0x2A: 'CALC',
    0x1D: 'CALC_V',
    0xA1: 'SPECIAL',
    0x38: 'UNKNOWN_38',
    0x5A: 'UNKNOWN_5A',
    0x5B: 'UNKNOWN_5B',
    0xDA: 'ASSIGN_DA',
    0x0B: 'ASSIGN_0B',
    0x12: 'ASSIGN_12',
    0x6D: 'UNKNOWN_6D',
    0xD9: 'UNKNOWN_D9',
    0x2C: 'UNKNOWN_2C',
    # From Pass 367-371 Rosetta Stone analysis
    0x25: 'PFMT',
    0x22: 'PBLNK',
    0x0C: 'DEL_REC',
    0x29: 'ARRAY_ITER_INIT',
    0x65: 'DATA_STRUCT',
    0x44: 'ENTER_EXEC_BEGIN',
    0xC1: 'BLOCK_CLOSE',
    0x19: 'OP_19_GROUP',  # groups
    0x5C: 'OP_5C_DUAL',
}

def le32(b, off):
    if off + 4 > len(b): return 0
    return struct.unpack_from('<I', b, off)[0]

def le16(b, off):
    if off + 2 > len(b): return 0
    return struct.unpack_from('<H', b, off)[0]

def read_file():
    raw = open(DEC_FILE, 'rb').read()
    # Strip 8-byte validation prefix
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

DISPATCH_START = 0x6C0  # always 0x6C0 from program body start

def read_variables(data, hdr):
    """Returns list of variable names indexed by var_index."""
    vt_off = len(data) - hdr['var_table_size']
    count  = hdr['var_count']
    names  = []
    for i in range(count):
        off = vt_off + i * 77
        if off + 77 > len(data): break
        b0 = data[off]
        if b0 < 0x20:
            raw = data[off+1:off+15]
        else:
            raw = data[off:off+15]
        name = raw.rstrip(b'\x00 ').decode('ascii', errors='replace')
        names.append(name)
    return names

def read_procedures(data, hdr):
    """Returns list of (name, metadata_bytes) for each procedure."""
    vt_off   = len(data) - hdr['var_table_size']
    src_off  = vt_off - 60
    proc_off = src_off - hdr['proc_size']
    count    = hdr['proc_size'] // 53
    procs    = []
    for i in range(count):
        eoff = proc_off + i * 53
        nlen = data[eoff]
        name = data[eoff+1:eoff+1+min(nlen,15)].decode('ascii', errors='replace').rstrip('\x00')
        meta = data[eoff+16:eoff+53]  # 37 bytes of metadata
        procs.append((name, meta))
    return procs

def pool_start(data, hdr):
    return DISPATCH_START + hdr['dispatch_size']

def read_pool_string(pool, off):
    """Try to read a string from pool at byte offset `off`.
    Returns decoded string or None."""
    if off < 0 or off + 4 > len(pool): return None
    if pool[off] == 0x41:
        slen = le16(pool, off+2)
        raw  = pool[off+4:off+4+slen]
        try:
            return raw.decode('ascii', errors='replace').rstrip('\x00 ')
        except:
            return repr(raw[:40])
    if pool[off] == 0x4E:
        val = le32(pool, off+1)
        return f"NUM({val})"
    if pool[off] == 0x52:
        raw = pool[off+1:off+5]
        return f"REAL(0x{raw.hex()})"
    if pool[off] == 0x46:
        vi = le32(pool, off+1) // 77
        return f"VAR[{vi}]"
    if pool[off] == 0x43:
        pi = le32(pool, off+1)
        return f"POOL@{pi}"
    if pool[off] == 0x4C:
        val = le32(pool, off+1)
        return f"LOGICAL({val})"
    return None

def find_pool_var(pool, var_names, off):
    """Walk pool from `off`, collecting var refs and strings in a blob."""
    results = []
    pos = off
    while pos < len(pool):
        t = pool[pos]
        if t == 0xFF:  # sentinel
            break
        if t == 0xFD:  # begin marker
            pos += 1
            continue
        if t == 0x46:  # variable ref
            vi = le32(pool, pos+1) // 77
            vname = var_names[vi] if vi < len(var_names) else f'var{vi}'
            results.append(f'VAR:{vname}')
            pos += 5
        elif t == 0x41:  # string
            slen = le16(pool, pos+2)
            s = pool[pos+4:pos+4+slen].decode('ascii', errors='replace').rstrip('\x00 ')
            results.append(f'STR:"{s}"')
            pos += 4 + slen
        elif t == 0x43:  # pool pointer
            pi = le32(pool, pos+1)
            sub = read_pool_string(pool, pi)
            results.append(f'PTR->{sub or f"@{pi}"}')
            pos += 5
        elif t in (0x4E, 0x52, 0x4C, 0x44, 0x49, 0x4D, 0x53):
            val = le32(pool, pos+1)
            results.append(f'CONST({t:02X}:{val})')
            pos += 5
        else:
            results.append(f'??{t:02X}')
            pos += 1
    return results

def disassemble(data, hdr, var_names, procs, focus_procs=None, option_highlight=True):
    """
    Disassemble the dispatch table.
    focus_procs: set of procedure names to show (show surrounding context).
    option_highlight: flag any instruction referencing WOBOM.OPTION.
    """
    pstart = pool_start(data, hdr)
    pool   = data[pstart:]
    disp   = data[DISPATCH_START:DISPATCH_START + hdr['dispatch_size']]
    n_instr = hdr['dispatch_size'] // 8

    # Build reverse lookup: instruction_index -> proc_name
    # Procedure metadata bytes 16-52. Based on known structure, bytes 16-19 likely = start instr index.
    proc_at_instr = {}
    for pname, meta in procs:
        # Try treating meta[0:4] as start instruction index (LE32)
        start_raw = le32(meta, 0)
        end_raw   = le32(meta, 4)
        if start_raw < n_instr:
            if start_raw not in proc_at_instr:
                proc_at_instr[start_raw] = []
            proc_at_instr[start_raw].append(pname)

    # Find var index for WOBOM.OPTION
    option_vi = None
    for i, vn in enumerate(var_names):
        if 'WOBOM.OPTION' in vn or vn == 'WOBOM.OPTION':
            option_vi = i
            break
    # The variable reference byte pattern for WOBOM.OPTION
    option_var_offset = option_vi * 77 if option_vi is not None else -1

    # Scan for WOBOM.OPTION references in pool
    option_pool_offsets = set()
    pos = 0
    while pos < len(pool) - 5:
        if pool[pos] == 0x46:
            vi_bytes = le32(pool, pos+1)
            if vi_bytes == option_var_offset:
                option_pool_offsets.add(pstart + pos)  # absolute file offset (not used yet)
                option_pool_offsets.add(pos)            # pool-relative offset
        pos += 1

    # Focus procedure instruction ranges
    focus_ranges = set()  # set of instruction indices to show

    # Find kit-related procedure instruction boundaries
    kit_proc_names = {'LOAD.KIT', 'LOAD.KIT2', 'LOAD.KITA', 'KIT.LIST',
                      'ISSU.KIT', 'ISSU.KITA', 'ISSU.KIT2', 'VLD_KITISSUE',
                      'PROC.KIT', 'JIT.WOBOM', 'EXPLODE_BOM', 'EXP.BOM',
                      'PH.LOOP.TEST', 'NO.KIT.2', 'NO.KIT.Z', 'IS.WOBOM.OUT',
                      'SORT_LIST'}

    # Collect all instructions that touch WOBOM.OPTION
    option_instrs = set()
    for idx in range(n_instr):
        base  = idx * 8
        op    = disp[base]
        poff  = le32(disp, base+4)
        # Check if pool offset is within or near WOBOM.OPTION references
        # Try reading pool at poff and scan the blob for WOBOM.OPTION ref
        if poff < len(pool):
            scan = find_pool_var(pool, var_names, poff)
            for s in scan:
                if 'WOBOM.OPTION' in s or (option_vi is not None and f'VAR[{option_vi}]' in s):
                    option_instrs.add(idx)
                    # Add surrounding context
                    for j in range(max(0,idx-5), min(n_instr, idx+20)):
                        focus_ranges.add(j)
                    break

    output = []
    output.append(f"T7WOG.RWN disassembly — {n_instr} instructions, pool@0x{pstart:X}")
    output.append(f"WOBOM.OPTION = var[{option_vi}], pool-offset-pattern = 0x{option_var_offset:X}")
    output.append(f"WOBOM.OPTION referenced at instructions: {sorted(option_instrs)}")
    output.append("=" * 80)

    prev_op = None
    in_kit_section = False

    for idx in range(n_instr):
        base = idx * 8
        op   = disp[base]
        b1   = disp[base+1]
        sub  = disp[base+3]
        poff = le32(disp, base+4)

        # Mark procedure start
        if idx in proc_at_instr:
            pnames = proc_at_instr[idx]
            for pn in pnames:
                in_kit_section = any(kp in pn for kp in ['KIT', 'BOM', 'WOBOM', 'OPTION', 'VLD_K'])
                output.append(f"\n{'━'*60}")
                output.append(f"PROC [{idx:4d}]: {pn}")
                output.append(f"{'━'*60}")
                if pn in kit_proc_names or in_kit_section:
                    for j in range(idx, min(n_instr, idx+200)):
                        focus_ranges.add(j)

        # Decode pool operand
        pool_decoded = ""
        if poff < len(pool):
            blob_items = find_pool_var(pool, var_names, poff)
            if blob_items:
                pool_decoded = ' '.join(blob_items[:6])
            else:
                s = read_pool_string(pool, poff)
                if s:
                    pool_decoded = f'"{s}"'

        is_option_ref = idx in option_instrs
        in_focus = idx in focus_ranges or in_kit_section or is_option_ref

        if not in_focus:
            continue

        opname = OP_NAMES.get(op, f'OP_{op:02X}')
        marker = ">>> OPTION <<<" if is_option_ref else ""
        line = f"  [{idx:4d}] {op:02X} sub={sub:02X} poff={poff:6d}  {opname:14s}  {pool_decoded[:60]}  {marker}"
        output.append(line)

    return '\n'.join(output)


def main():
    print(f"Reading {DEC_FILE}...", file=sys.stderr)
    data = read_file()
    hdr  = read_header(data)
    print(f"Header: dispatch={hdr['dispatch_size']}, procs={hdr['proc_size']//53}, "
          f"vars={hdr['var_count']}", file=sys.stderr)

    var_names = read_variables(data, hdr)
    procs     = read_procedures(data, hdr)

    print(f"Variables: {len(var_names)}, Procedures: {len(procs)}", file=sys.stderr)

    # Print procedure list with metadata
    print("\n=== PROCEDURE TABLE (name + first 8 bytes of metadata) ===", file=sys.stderr)
    for i, (pname, meta) in enumerate(procs):
        m0 = le32(meta, 0)
        m4 = le32(meta, 4)
        m8 = le32(meta, 8)
        if any(k in pname for k in ['KIT','BOM','WOBOM','VLD_K','LOAD','ISSU','PROC','EXPLODE','EXP','NO.KIT','OPTION','LIST']):
            print(f"  [{i:3d}] {pname:20s}  meta[0:12]= {m0:6d} {m4:6d} {m8:6d}", file=sys.stderr)

    # Print variable index for WOBOM.OPTION
    print("\n=== WOBOM-related variables ===", file=sys.stderr)
    for i, vn in enumerate(var_names):
        if 'WOBOM' in vn or 'KIT' in vn or 'BOM' in vn or 'OPTION' in vn:
            print(f"  var[{i:4d}] = {vn}", file=sys.stderr)

    # Full disassembly focused on kit sections
    out = disassemble(data, hdr, var_names, procs)
    print(out)


if __name__ == '__main__':
    main()
