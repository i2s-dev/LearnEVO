"""
Detailed analysis of FILE*.UPD Btrieve structure.
Goal: decode record format to extract table relationships and schema data.
"""
import struct
from pathlib import Path

SAMPLES = Path(r"C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\samples")


def hex_dump_range(data, start, end, width=16, label=''):
    for off in range(start, min(end, len(data)), width):
        chunk = data[off:off + width]
        hex_part = ' '.join(f'{b:02X}' for b in chunk)
        asc_part = ''.join(chr(b) if 32 <= b < 127 else '.' for b in chunk)
        print(f"  {label}[{off:06X}] {hex_part:<{width*3}} {asc_part}")


def analyze_page_structure(filename, page_size=4096, pages_to_show=3):
    path = SAMPLES / filename
    data = path.read_bytes()
    n_pages = len(data) // page_size

    print(f"\n{'=' * 60}")
    print(f"FILE: {filename}  ({len(data):,} bytes = {n_pages} pages x {page_size})")
    print('=' * 60)

    # Show non-zero pages
    shown = 0
    for pg in range(n_pages):
        offset = pg * page_size
        page = data[offset:offset + page_size]
        # Skip empty/nearly-empty pages
        nz = sum(1 for b in page if b != 0)
        if nz < 10:
            continue
        print(f"\n  --- Page {pg} (offset {offset:06X}) ---")
        hex_dump_range(data, offset, offset + min(128, page_size))
        shown += 1
        if shown >= pages_to_show:
            print(f"  ... ({n_pages - pg - 1} more pages)")
            break


def find_record_boundaries_files(filename, page_size=4096):
    """Try to extract records from FILES.UPD — contains table names."""
    path = SAMPLES / filename
    data = path.read_bytes()

    print(f"\n{'=' * 60}")
    print(f"RECORD ANALYSIS: {filename}")
    print('=' * 60)

    # Look at the first non-FCR data page with content
    for pg in range(len(data) // page_size):
        offset = pg * page_size
        page = data[offset:offset + page_size]
        nz = sum(1 for b in page if b != 0)
        if nz < 100:
            continue
        # Check for repeating patterns suggesting fixed-length records
        print(f"\n  Page {pg} at offset {offset:06X}:")
        hex_dump_range(data, offset, offset + 128)
        break


def extract_files_records(filename='FILES.UPD', page_size=4096):
    """Extract table name records from FILES.UPD."""
    path = SAMPLES / filename
    data = path.read_bytes()
    n_pages = len(data) // page_size

    print(f"\n{'=' * 60}")
    print(f"TABLE RECORDS FROM {filename}")
    print('=' * 60)

    # The strings we saw: BKCMACCC at 0xD014, next at 0xD043 — spacing = 47 bytes
    # Let me check the spacing between records
    prev_pos = None
    spacings = []
    for pg in range(n_pages):
        offset = pg * page_size
        page = data[offset:offset + page_size]
        # Find 8-char uppercase table name patterns
        for i in range(0, page_size - 8):
            chunk = page[i:i + 8]
            # Check if it looks like a BK* or similar table name (all uppercase alpha)
            if all((65 <= b <= 90 or b == 32) for b in chunk) and chunk[0] != 32:
                name = chunk.decode('ascii')
                abs_pos = offset + i
                if prev_pos is not None:
                    spacings.append(abs_pos - prev_pos)
                prev_pos = abs_pos

    # Find most common spacing (= record size)
    from collections import Counter
    common_spacings = Counter(spacings).most_common(10)
    print(f"Most common spacings between BK* names: {common_spacings}")


def extract_filerel_records(filename='FILEREL.UPD', page_size=4096):
    """Extract FK relationship records from FILEREL.UPD."""
    path = SAMPLES / filename
    data = path.read_bytes()
    n_pages = len(data) // page_size

    print(f"\n{'=' * 60}")
    print(f"RELATIONSHIP RECORDS FROM {filename}")
    print('=' * 60)

    # We saw: 'FILEDICTDICT_BUFF_NAME FILELOC LOC_BUFF_NAME'
    # Let me find all similar records
    records_found = []
    for pg in range(n_pages):
        offset = pg * page_size
        page = data[offset:offset + page_size]
        for i in range(0, page_size - 48):
            chunk = page[i:i + 96]
            # Look for 8-char table name start
            if (all(32 <= b < 127 or b == 0 for b in chunk) and
                    chunk[0] not in (0, 32) and
                    all((65 <= b <= 90 or b == 32) for b in chunk[:8])):
                # Looks like a record start
                name = bytes(b if b != 0 else 32 for b in chunk).decode('ascii', errors='replace')
                if 'BTRVFLD' in name or 'BTRVFILE' in name or 'BTRVINDX' in name or 'FILEDICT' in name or 'FILEKNUM' in name or 'FILELOC' in name:
                    abs_pos = offset + i
                    records_found.append((abs_pos, name[:80]))

    for pos, rec in records_found[:30]:
        print(f"  [{pos:06X}] {rec!r}")


def hex_dump_area(filename, start, length=256):
    path = SAMPLES / filename
    data = path.read_bytes()
    hex_dump_range(data, start, start + length, label=f'{filename}:')


if __name__ == '__main__':
    # Check page structure for FILES.UPD
    analyze_page_structure('FILES.UPD', page_size=4096, pages_to_show=4)

    # Extract table names
    extract_files_records('FILES.UPD', page_size=4096)

    # Extract relationship records
    extract_filerel_records('FILEREL.UPD', page_size=4096)

    # Detailed hex around the FK relationship area in FILEREL.UPD
    print("\n\n--- FILEREL.UPD detail around 0xD014 ---")
    hex_dump_area('FILEREL.UPD', 0xD000, 512)
