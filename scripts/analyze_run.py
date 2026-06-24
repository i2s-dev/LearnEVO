#!/usr/bin/env python3
"""
analyze_run.py — TAS Pro 6 .RUN bytecode analyzer
Parses the binary structure and builds a Rosetta Stone from .SRC files.

Usage: python analyze_run.py <file.RUN> [--disasm] [--stats]
"""

import struct
import sys
import os
import collections

def read_cstr(data, off, max_len=16):
    """Read null-terminated string from data."""
    end = data.find(b'\x00', off, off + max_len)
    if end == -1:
        end = off + max_len
    return data[off:end].decode('latin-1', errors='replace').strip()

def parse_run(path):
    with open(path, 'rb') as f:
        data = f.read()

    n = len(data)
    print(f"=== {os.path.basename(path)} ({n} bytes) ===")

    # Locate "TAS32" magic
    magic_off = data.find(b'TAS32')
    if magic_off == -1:
        # Try TAS-32 or other variants
        magic_off = data.find(b'TAS')
        print(f"  TAS32 not found; TAS at 0x{magic_off:04x}" if magic_off != -1 else "  No TAS magic found")
    else:
        print(f"  Magic TAS32 at 0x{magic_off:04x}")

    # Header region: table names at 0x80, 16-byte slots
    TABLE_BASE = 0x80
    tables = []
    off = TABLE_BASE
    while off + 16 <= n:
        name = read_cstr(data, off, 16)
        if not name or name.startswith('\x00'):
            break
        tables.append(name)
        off += 16
        # Stop at first all-zero or unlikely table name
        if len(name) < 2 or not name[0].isalpha():
            break

    # Better: scan for table names until we hit a non-name pattern
    tables = []
    off = TABLE_BASE
    while off + 16 <= n:
        chunk = data[off:off+16]
        # Table names are ASCII uppercase letters + digits
        name_bytes = []
        for b in chunk:
            if 0x20 <= b <= 0x7E and chr(b) not in '\x00':
                name_bytes.append(chr(b))
            else:
                break
        name = ''.join(name_bytes).strip()
        if not name or len(name) < 2:
            break
        tables.append(name)
        off += 16

    print(f"  Tables ({len(tables)}): {tables}")
    num_tables = len(tables)

    # var section starts right after table area
    # code_start = TABLE_BASE + N*16 + var_size
    # var_size is in the header; look for the pattern
    # From docs: preamble at 0x35 = "TAS32"; 0x3A = version
    # var section: [0..0x045F] zero-init; [0x0460..] = var descriptor table
    # BUT: runtime_base varies (0x0460 for var_size=1440, 0x02D0 for var_size=2640)

    # Try to find code start: after table names
    var_table_start = TABLE_BASE + num_tables * 16

    # The 2-byte preamble precedes instruction stream
    # Instructions: [op:1][0x00:1][b2:1][addr_LE4:4] = 7 bytes each

    # From previous analysis: code area has recognizable patterns
    # Let's find instruction-like patterns: byte, 0x00, byte, then 4-byte LE addr

    # First: understand the var section layout
    # Var descriptors: 7-byte entries [type_tag][0x00][storage_size][runtime_offset_LE4]
    # Known runtime_base values: 0x0460 or 0x02D0

    # Let's try to find the code section by looking for the 2-byte preamble
    # and then sequential 7-byte instructions

    return data, tables, num_tables

def find_code_section(data, num_tables):
    """Locate instruction stream: find first 7-byte-aligned region with no zero-ops
    and at least MIN_RUN consecutive valid instructions. Prefers earliest entry point
    (the program start) over function bodies deeper in the file."""
    TABLE_BASE = 0x80
    var_table_start = TABLE_BASE + num_tables * 16
    MIN_RUN = 30  # must see this many consecutive non-zero-op instructions

    best_off = None

    for start_off in range(var_table_start, min(var_table_start + 0x2000, len(data) - 200)):
        count = 0
        off = start_off
        ok = True
        while off + 7 <= len(data) and count < MIN_RUN:
            op = data[off]
            b1 = data[off + 1]
            if b1 != 0x00 or op == 0x00:
                ok = False
                break
            count += 1
            off += 7
        if ok and count >= MIN_RUN:
            best_off = start_off
            break  # take the FIRST qualifying region (program entry)

    if best_off is None:
        return None, 0

    # Count full instruction run from best_off
    best_count = 0
    off = best_off
    while off + 7 <= len(data):
        if data[off + 1] != 0x00:
            break
        best_count += 1
        off += 7

    return best_off, best_count

def disassemble(data, code_off, max_instr=200, labels=None):
    """Disassemble instruction stream."""
    INSTR_SIZE = 7
    instructions = []
    off = code_off

    # Build address-to-index map for branch targets
    addr_map = {}

    count = 0
    while off + INSTR_SIZE <= len(data) and count < max_instr:
        op = data[off]
        b1 = data[off + 1]  # always 0x00
        b2 = data[off + 2]
        addr = struct.unpack_from('<I', data, off + 3)[0]

        if b1 != 0x00:
            break  # no longer in instruction stream

        instructions.append((off, op, b2, addr))
        addr_map[off - code_off] = count  # map file offset → instruction index
        off += INSTR_SIZE
        count += 1

    return instructions, addr_map

def opcode_stats(instructions):
    """Count opcode frequencies."""
    counts = collections.Counter(op for _, op, _, _ in instructions)
    return counts

def print_disasm(instructions, code_off, addr_map, max_show=100):
    """Print disassembly using confirmed .RUN opcode table (Pass 240/243)."""
    KNOWN_OPS = {
        # Confirmed by positional Rosetta Stone alignment (Pass 240)
        0x0F: 'ASSIGN',      # b2=0x0A
        0x0E: 'ENTER',       # b2=0x61 — enter field
        0x37: 'TRAP',        # b2=0x0A — trap key handler
        0x20: 'RET_FUNC',    # b2=0x05 — return from function (ret .t. / ret .f.)
        0x08: 'TRAP_DFLT',   # b2=0x06 — trap key dflt
        0xC0: 'SET_PROP_CTX',# b2=0x04 — set property context
        0xC1: 'ENT_BLOCK',   # b2=0x00 — enter block marker
        0x4B: 'CALL_LIB',    # b2=0x09 — call library function (fnc_list, GOSUB lib)
        0x39: 'FUNC_PREPOST',# b2=0x51 — function pre/post hook setup
        0x01: 'ARG_DESC',    # b2=0x1D — argument descriptor
        # Confirmed in preamble (Pass 240)
        0x1F: 'OPEN_TBL',   # b2=0x35 — open table (TABLE_HANDLE)
        0x13: 'FIND_KEY',    # b2=0x21 — find F srch
        0x06: 'CLR_REC',     # b2=0x06 — clr table rec
        0x1C: 'MOUNT',       # b2=0x11 — mount SELECT2 type S
        0x21: 'MENU',        # b2=0x59 — menu at x,y
        0x73: 'PRG_HDR',     # b2=0x07 — prg_hdr
        # Confirmed from Rosetta Stone context
        0x49: 'READ_PROP',   # b2=0x09 — read property (e.g. SETUP_COLOR)
        0x6A: 'GOTO_LABEL',  # — goto label
        0x42: 'GOSUB',       # — gosub subroutine
        0x3B: 'COND_JMP',    # — conditional jump (if/endif branches)
        # Unknown — cluster together as 0x93+0x65x2+0x53+GOSUB per enter block
        # pfmt/pblnk are DECLARATIVE (zero bytecode) — these are NOT pfmt/pblnk
        0x53: 'OP_53',       # — unknown; b2=0x7D
        0x93: 'OP_93',       # — unknown; b2=0x14
        0x65: 'OP_65',       # — unknown; b2=0x0A
        0xBE: 'PMSG',        # — print message
    }

    for i, (off, op, b2, addr) in enumerate(instructions[:max_show]):
        rel_off = off - code_off
        op_name = KNOWN_OPS.get(op, f'OP_{op:02X}')
        # Check if addr points into instruction stream
        target_instr = addr_map.get(addr, None)
        target_str = f'->I#{target_instr}' if target_instr is not None else f'addr=0x{addr:08X}'
        print(f"  [{i:4d}] +{rel_off:05X}  {op:02X} 00 {b2:02X}  {addr:08X}  {op_name}  {target_str}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python analyze_run.py <file.RUN> [--disasm] [--stats]")
        sys.exit(1)

    path = sys.argv[1]
    do_disasm = '--disasm' in sys.argv
    do_stats = '--stats' in sys.argv or not do_disasm

    data, tables, num_tables = parse_run(path)

    code_off, code_count = find_code_section(data, num_tables)
    if code_off:
        print(f"  Code section at 0x{code_off:04X} ({code_count} instructions found)")
    else:
        print("  Could not locate code section")
        return

    instructions, addr_map = disassemble(data, code_off, max_instr=2000)
    print(f"  Total instructions decoded: {len(instructions)}")

    if do_stats:
        counts = opcode_stats(instructions)
        print(f"\n  Opcode frequency (top 30):")
        KNOWN_OPS = {
            0x0F: 'ASSIGN', 0x3B: 'COND_BRANCH', 0x40: 'EXIT', 0x42: 'GOSUB',
            0x48: 'PUSH', 0x49: 'READ_PROP', 0x57: 'EXEC_FORM', 0x6A: 'GOTO_LABEL',
            0x71: 'EXIT2', 0xDC: 'POP',
        }
        for op, cnt in counts.most_common(30):
            name = KNOWN_OPS.get(op, f'OP_{op:02X}')
            print(f"    {op:02X}  {name:<20}  {cnt:5d}")

    if do_disasm:
        print(f"\n  Disassembly (first 150 instructions):")
        print_disasm(instructions, code_off, addr_map, max_show=150)

if __name__ == '__main__':
    main()
