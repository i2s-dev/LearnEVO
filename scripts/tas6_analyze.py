"""
tas6_analyze.py - TAS Pro 6 .RUN bytecode analysis tool.

Usage:
    python scripts/tas6_analyze.py [--file PATH] [--offset HEX] [--length N]

Prints annotated hex dump of .RUN binary with known opcode annotations.
"""
import struct, sys, os, argparse

# ── Known opcodes (accumulated from BKAWLB.RUN vs BKAWLB.SRC analysis) ───────
# Format: opcode_byte: (name, arg_format)
# arg_format:
#   None   = no argument
#   'b'    = 1-byte arg
#   'w'    = 2-byte LE arg
#   'dw'   = 4-byte LE arg
#   'str'  = 2-byte LE length, then that many bytes
#   'str0' = 2-byte prefix (00 XX), 2-byte length, then data  (for 0x41 00 LL LL)
OPCODES = {
    0x41: ('PUSH_STR',   'str_pfx'),  # 0x41 0x00 <len2> <data>
    0x46: ('LOAD_VAR',   'dw'),        # 0x46 <addr4>
    0x4E: ('ARRAY_IDX',  'dw'),        # 0x4E <index4>
    0x0A: ('PUSH_ADDR',  'dw'),        # 0x0A <addr4>
    0x0F: ('NOP?',       'b'),         # 0x0F <1byte> (often 00)
    0x4B: ('CALL?',      'dw_pfx'),    # 0x4B <00> <addr4>
    0x49: ('PUSH_VAR?',  'dw_pfx'),    # 0x49 <00 00> <addr4>
    0x35: ('FIELD_REF?', 'dw'),        # 0x35 <addr4>
    0x1F: ('OP_1F?',     'dw'),        # 0x1F <addr4>
    0x4C: ('OP_4C?',     'dw'),        # 0x4C <addr4>
}


def read_run(path):
    with open(path, 'rb') as f:
        return f.read()


def parse_header(data):
    if len(data) < 0x40:
        return {}
    fields = {}
    for i, name in [(0x00,'code_section_offset'), (0x04,'h04'), (0x08,'h08'),
                    (0x0C,'var_table_size'), (0x10,'table_count'),
                    (0x14,'h14'), (0x18,'var_storage_size'), (0x1C,'h1C'),
                    (0x20,'h20'), (0x24,'h24'), (0x28,'h28'), (0x30,'h30')]:
        fields[name] = struct.unpack_from('<I', data, i)[0]
    # Magic
    if len(data) > 0x3A:
        fields['magic'] = data[0x35:0x3A].decode('ascii', errors='replace')
        fields['version'] = data[0x3A]
    return fields


def find_table_names(data):
    """Table names at 0x80, 16-byte slots, up to 30 slots."""
    names = []
    for i in range(30):
        off = 0x80 + i * 16
        if off + 16 > len(data):
            break
        slot = data[off:off+8]
        name = slot.rstrip(b'\x00')
        if not name:
            continue
        try:
            names.append((i, name.decode('ascii')))
        except Exception:
            pass
    return names


def find_strings(data, start=0, end=None):
    """Find all 0x41 0x00 <len2> <str> patterns."""
    if end is None:
        end = len(data)
    strings = []
    i = start
    while i < end - 4:
        if data[i] == 0x41 and data[i+1] == 0x00:
            length = struct.unpack_from('<H', data, i+2)[0]
            if 0 < length < 500 and i + 4 + length <= end:
                s = data[i+4:i+4+length]
                printable = all(0x20 <= b <= 0x7E for b in s)
                strings.append((i, length, s, printable))
                i += 4 + length
                continue
        i += 1
    return strings


def hex_line(offset, data_slice):
    hex_part = ' '.join(f'{b:02x}' for b in data_slice)
    ascii_part = ''.join(chr(b) if 0x20 <= b <= 0x7E else '.' for b in data_slice)
    return f'{offset:06X}: {hex_part:<48}  {ascii_part}'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', default='samples/rosetta/BKAWLB.RUN')
    parser.add_argument('--offset', default=None, help='Start offset (hex)')
    parser.add_argument('--length', type=int, default=256)
    parser.add_argument('--strings', action='store_true', help='List all strings')
    parser.add_argument('--header', action='store_true', help='Print header')
    parser.add_argument('--tables', action='store_true', help='Print table names')
    args = parser.parse_args()

    data = read_run(args.file)
    print(f"File: {args.file}  Size: {len(data):,} bytes")

    hdr = parse_header(data)
    if args.header or True:
        print("\nHeader:")
        for k, v in hdr.items():
            if isinstance(v, int):
                print(f"  {k:25s} = {v:8d}  0x{v:X}")
            else:
                print(f"  {k:25s} = {v!r}")

    if args.tables or True:
        print("\nTable names (0x80+):")
        for idx, name in find_table_names(data):
            print(f"  slot[{idx:2d}] @ 0x{0x80+idx*16:04X}: {name}")

    if args.strings or True:
        print(f"\nString pool (0x41 00 <len> <data> pattern):")
        # Find code section start
        var_store_start = 0x80 + 30 * 16  # max table area
        # find first non-zero after table area
        actual_code_start = var_store_start
        for i in range(var_store_start, len(data)):
            if data[i] != 0:
                actual_code_start = i
                break
        print(f"  Code/data starts at: 0x{actual_code_start:X}")
        strings = find_strings(data, actual_code_start)
        for off, length, s, printable in strings[:60]:
            s_repr = s.decode('ascii', errors='replace') if printable else s.hex()
            print(f"  0x{off:06X}: len={length:4d}  {s_repr!r}")

    if args.offset:
        start = int(args.offset, 16)
        end = min(start + args.length, len(data))
        print(f"\nDump @ 0x{start:X} - 0x{end:X}:")
        for i in range(start, end, 16):
            chunk = data[i:min(i+16, end)]
            print(hex_line(i, chunk))


if __name__ == '__main__':
    main()
