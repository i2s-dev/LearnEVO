"""Decode dBASE IV .mdx compound index file format."""
import struct
import sys

def decode_mdx(path):
    with open(path, 'rb') as f:
        data = f.read()

    print(f"=== {path} ({len(data)} bytes) ===\n")

    # MDX header is 544 bytes (first page = 512 bytes + possible extension)
    # Byte 0: version (01 = dBASE IV)
    # Bytes 1-3: year, month, day of last update
    # Bytes 4-11: base filename (8 chars, NUL-padded)
    # Bytes 12-13: block factor (512 * blockfactor = page size)
    # Bytes 14-15: reserved
    # Bytes 16-17: number of tag slots (max 47)
    # Bytes 18-19: tag entry size (always 32)
    # Bytes 20-21: reserved
    # Byte 22: production flag (01 = production index)
    # Bytes 24-27: number of pages used
    # Bytes 28-31: number of pages allocated
    # After header: tag table starts at offset 544? No...

    # dBASE IV MDX layout (standard):
    # Offset 0:   version (1 byte)
    # Offset 1-3: date (year-1900, month, day)
    # Offset 4-11: filename (8 bytes, space-padded)
    # Offset 12-13: block factor (LE word) — page_size = 512 * block_factor
    # Offset 14-15: reserved
    # Offset 16-17: tag count (LE word)
    # Offset 18-19: tag slot size (LE word, =32)
    # Offset 20-21: reserved
    # Offset 22:  production flag (byte)
    # Offset 23:  code page
    # Offset 24-27: page count (LE dword)

    version = data[0]
    year = 1900 + data[1]
    month = data[2]
    day = data[3]
    filename = data[4:12].rstrip(b'\x00 ').decode('ascii', errors='replace')
    block_factor = struct.unpack_from('<H', data, 12)[0]
    tag_count = struct.unpack_from('<H', data, 16)[0]
    tag_slot_size = struct.unpack_from('<H', data, 18)[0]
    production = data[22]
    code_page = data[23]
    page_count = struct.unpack_from('<I', data, 24)[0]

    page_size = 512 * block_factor if block_factor else 512

    print(f"Version:      {version}")
    print(f"Last update:  {year}-{month:02d}-{day:02d}")
    print(f"Base file:    '{filename}'")
    print(f"Block factor: {block_factor}  (page size = {page_size} bytes)")
    print(f"Tag count:    {tag_count}")
    print(f"Tag slot size:{tag_slot_size}")
    print(f"Production:   {production}")
    print(f"Code page:    {code_page}")
    print(f"Page count:   {page_count}")
    print()

    # Tag directory: starts at offset 28 (or 32?)
    # Each tag entry is 32 bytes:
    #   0-1:  page number of root page for this index
    #   2-3:  page number of key count / statistics page
    #   4-15: tag name (11 chars + NUL)
    #   16:   key format (0=calculated, 1=data)
    #   17:   key type ('C'=char, 'N'=numeric, 'D'=date)
    #   18-19: reserved
    #   20-21: key length
    #   22:   index options (bits: unique, descending)
    #   23:   reserved
    #   24-27: key expression start offset in expression block
    #   28-31: for condition start offset

    # Actually let me try offset 28 for tag table
    TAG_OFFSET = 28
    TAG_SIZE = 32

    print(f"--- Tag Directory (at offset {TAG_OFFSET}) ---")
    for i in range(min(tag_count, 47)):
        off = TAG_OFFSET + i * TAG_SIZE
        if off + TAG_SIZE > len(data):
            break
        root_page = struct.unpack_from('<H', data, off)[0]
        stats_page = struct.unpack_from('<H', data, off + 2)[0]
        tag_name = data[off+4:off+15].rstrip(b'\x00 ').decode('ascii', errors='replace')
        key_format = data[off+15]
        key_type = chr(data[off+16]) if 32 <= data[off+16] <= 127 else f'0x{data[off+16]:02X}'
        key_len = struct.unpack_from('<H', data, off+18)[0]
        idx_opts = data[off+20]
        expr_off = struct.unpack_from('<H', data, off+24)[0]

        print(f"  [{i}] name='{tag_name}' type={key_type} len={key_len} "
              f"root_page={root_page} opts={idx_opts:08b} expr_off={expr_off}")

    # Try to find key expressions — they're stored as NUL-terminated strings
    # after the tag directory
    expr_block_start = TAG_OFFSET + tag_count * TAG_SIZE
    print(f"\n--- Expression block (starting at offset {expr_block_start}) ---")
    pos = expr_block_start
    expr_idx = 0
    while pos < min(expr_block_start + 2048, len(data)):
        end = data.index(b'\x00', pos) if b'\x00' in data[pos:pos+256] else pos+256
        expr = data[pos:end].decode('ascii', errors='replace').strip()
        if expr:
            print(f"  expr[{expr_idx}] @{pos}: '{expr}'")
            expr_idx += 1
        pos = end + 1
        if pos > expr_block_start + 2048:
            break

    print()


if __name__ == '__main__':
    import os
    samples = r"c:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\samples"
    for fn in ['BKMENUSU.mdx', 'filedict.mdx', 'filedfld.mdx', 'fileloc.mdx']:
        path = os.path.join(samples, fn)
        if os.path.exists(path):
            decode_mdx(path)
