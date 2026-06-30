"""
Parse BKSLEVEL.B and BKSLMSTR.B for security level data.
Also try DBAHLPID.B for help ID → menu code mapping.

BKSLEVEL structure (from FILEDICT):
  BKSL.KEY       - record key
  BKSL.LEVEL     - security level code
  BKSL.MENU      - base menu access mask
  BKSL.MENU1     - menu group 1 value
  BKSL.MENU1.YN  - menu group 1 Y/N flag
  ... (through MENU19)

From binary analysis: records contain level_code + long 'N' string
  'N' = 0x4E (ASCII 78), likely Y/N access flags.
  The record structure is probably:
  [key][level_code][packed menu access bits or Y/N array]
"""
import struct
from pathlib import Path

SAMPLES = Path(r"C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\samples")
PAGE_SIZE = 4096


def hex_dump_area(data, start, length=128):
    for off in range(start, min(start + length, len(data)), 16):
        chunk = data[off:off + 16]
        hex_part = ' '.join(f'{b:02X}' for b in chunk)
        asc_part = ''.join(chr(b) if 32 <= b < 127 else '.' for b in chunk)
        print(f"  [{off:06X}] {hex_part:<48} {asc_part}")


def analyze_bkslevel():
    data = (SAMPLES / 'BKSLEVEL.B').read_bytes()
    print(f"=== BKSLEVEL.B ({len(data):,} bytes) ===")
    n_pages = len(data) // PAGE_SIZE

    # Show first non-FCR data page
    for pg in range(n_pages):
        offset = pg * PAGE_SIZE
        page = data[offset:offset + PAGE_SIZE]
        # Look for pages with non-null, non-FF content
        nz = sum(1 for b in page if b not in (0x00, 0xFF))
        if nz > 50:
            print(f"\nPage {pg} (offset {offset:06X}):")
            hex_dump_area(data, offset, 256)
            break

    # Find the 'N' string pattern
    pos = 0
    records = []
    while pos < len(data) - 10:
        # Look for long runs of 'N' (0x4E)
        if data[pos] == 0x4E and data[pos + 1] == 0x4E and data[pos + 2] == 0x4E:
            # Count the length
            length = 0
            while pos + length < len(data) and data[pos + length] == 0x4E:
                length += 1
            if length >= 50:
                # Look backwards for level code
                pre_start = max(0, pos - 20)
                pre = data[pre_start:pos]
                hex_pre = ' '.join(f'{b:02X}' for b in pre)
                asc_pre = ''.join(chr(b) if 32 <= b < 127 else '.' for b in pre)
                records.append((pos, length, asc_pre, hex_pre))
        pos += 1

    print(f"\n  Long 'N' runs (>=50) found: {len(records)}")
    for pos, length, asc_pre, hex_pre in records[:20]:
        print(f"  [{pos:06X}] length={length} | pre_asc={asc_pre!r} | pre_hex={hex_pre}")


def analyze_dbahlpid():
    data = (SAMPLES / 'DBAHLPID.B').read_bytes()
    print(f"\n=== DBAHLPID.B ({len(data):,} bytes) ===")

    # Extract all printable strings
    strings = []
    current = []
    start = 0
    for i, b in enumerate(data):
        if 32 <= b < 127:
            if not current:
                start = i
            current.append(chr(b))
        else:
            if len(current) >= 4:
                strings.append((start, ''.join(current)))
            current = []

    # Find module-style codes
    import re
    menu_codes = [(pos, s) for pos, s in strings
                  if re.match(r'^\d[A-Z]{2}-', s) or re.match(r'^[A-Z]{2}-', s)]
    print(f"  Menu code strings: {len(menu_codes)}")
    for pos, s in sorted(menu_codes, key=lambda x: x[1])[:60]:
        print(f"  [{pos:06X}] {s!r}")


if __name__ == '__main__':
    analyze_bkslevel()
    analyze_dbahlpid()
