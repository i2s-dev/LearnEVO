"""
Extract usable data from FILE*.UPD — EvoERP proprietary data dictionary.

These are Btrieve files (magic FC) with 4096-byte pages.
Record structure derived from hex analysis of FILEREL.UPD:
  - Page header: 16 bytes at page start
  - Per-record prefix: 8 bytes (4-byte slot descriptor + 4-byte key)
  - Record data: fixed-width field area (varies per file)

Strategy: look for repeating patterns of printable data after the FC header.
"""
import struct
import re
from pathlib import Path
from collections import Counter

SAMPLES = Path(r"C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\samples")
PAGE_SIZE = 4096


def read_data_pages(filename):
    """Yield (page_num, page_data) for all non-FCR non-empty pages."""
    path = SAMPLES / filename
    data = path.read_bytes()
    n_pages = len(data) // PAGE_SIZE
    for pg in range(1, n_pages):  # skip page 0 (FCR)
        offset = pg * PAGE_SIZE
        page = data[offset:offset + PAGE_SIZE]
        if sum(1 for b in page if b != 0 and b != 0xFF) > 20:
            yield pg, page


def extract_fixed_records(filename, rec_size, data_offset_in_rec=8, min_printable=4):
    """
    Extract fixed-size records from a Btrieve file.
    rec_size: total bytes per record (including prefix)
    data_offset_in_rec: bytes before actual data starts
    """
    path = SAMPLES / filename
    data = path.read_bytes()
    n_pages = len(data) // PAGE_SIZE

    records = []
    for pg in range(n_pages):
        offset = pg * PAGE_SIZE
        # Skip if page is empty/FCR
        page = data[offset:offset + PAGE_SIZE]
        if page[0:2] != b'FC' and pg == 0:
            pass
        # Scan for record starts using the known record size
        # Records appear to start at page+16 (after 16-byte page header)
        pos = 16  # skip page header
        while pos + rec_size <= PAGE_SIZE:
            chunk = page[pos:pos + rec_size]
            rec_data = chunk[data_offset_in_rec:]
            # Check if this looks like a real record (printable data)
            printable = sum(1 for b in rec_data[:30] if 32 <= b < 127)
            if printable >= min_printable and rec_data[0] not in (0x00, 0xFF):
                records.append((pg * PAGE_SIZE + pos, rec_data))
            pos += rec_size

    return records


def extract_filerel(filename='FILEREL.UPD'):
    """Extract relationship records from FILEREL.UPD."""
    print(f"\n{'=' * 60}")
    print(f"RELATIONSHIPS FROM {filename}")
    print('=' * 60)

    # From hex analysis: data at 0xD014, next at 0xD08C → gap = 120 bytes
    # Record prefix = 8 bytes (at 0xD00C and 0xD084)
    # So record = 8 (prefix) + 112 (data) = 120 bytes? Let's try
    # But page header seems to be 12-16 bytes...
    # Let's just scan for records by looking for 8-char uppercase table names

    path = SAMPLES / filename
    data = path.read_bytes()

    relationships = []
    # Scan for pattern: 8-byte uppercase table name (first char A-Z)
    i = 0
    while i < len(data) - 50:
        # Check for 8 uppercase or space bytes starting with uppercase
        chunk = data[i:i + 8]
        if (chunk[0] in range(65, 91) and  # starts with A-Z
                all(b in range(65, 91) or b == 32 for b in chunk)):
            # Possible table name
            table1 = chunk.decode('ascii').rstrip()
            # Check what follows — should be a field name
            rest = data[i + 8:i + 120]
            printable = ''.join(chr(b) if 32 <= b < 127 else '\x00' for b in rest[:90])
            if '\x00' not in printable[:20] and len(printable.split()[0]) > 2:
                # Looks like real data — extract the record
                rec_str = chunk.decode('ascii') + printable
                relationships.append((i, table1, printable.rstrip()))
        i += 1

    # Deduplicate and show unique relationship descriptions
    seen = set()
    unique = []
    for pos, t1, rest in relationships:
        key = t1 + rest[:80]
        if key not in seen:
            seen.add(key)
            unique.append((pos, t1, rest))

    print(f"  Found {len(unique)} unique relationship records:")
    for pos, t1, rest in unique[:50]:
        print(f"  [{pos:06X}] {t1!r:12} + {rest[:80]!r}")

    return unique


def extract_files_table(filename='FILES.UPD'):
    """Extract table name records from FILES.UPD."""
    print(f"\n{'=' * 60}")
    print(f"TABLE NAMES FROM {filename}")
    print('=' * 60)

    path = SAMPLES / filename
    data = path.read_bytes()

    tables = []
    i = 0
    while i < len(data) - 50:
        chunk = data[i:i + 8]
        if (chunk[0] in range(65, 91) and
                all(b in range(65, 91) or b == 32 for b in chunk)):
            name = chunk.decode('ascii').rstrip()
            if len(name) >= 4:
                # Get the next ~50 bytes for context
                ctx = data[i + 8:i + 60]
                ctx_str = ''.join(chr(b) if 32 <= b < 127 else '.' for b in ctx)
                tables.append((i, name, ctx_str))
        i += 1

    # Deduplicate
    seen = set()
    unique = []
    for pos, name, ctx in tables:
        if name not in seen:
            seen.add(name)
            unique.append((pos, name, ctx))

    print(f"  Found {len(unique)} unique table names:")
    for pos, name, ctx in sorted(unique, key=lambda x: x[1])[:100]:
        print(f"  {name:12} | {ctx[:50]!r}")

    return unique


def extract_filedict_sample(filename='FILEDICT.UPD', max_strings=100):
    """Extract strings from the file dictionary — the biggest and most valuable file."""
    print(f"\n{'=' * 60}")
    print(f"FIELD DICTIONARY SAMPLE FROM {filename}")
    print('=' * 60)

    path = SAMPLES / filename
    data = path.read_bytes()

    # Extract all meaningful printable strings
    strings = []
    current = []
    start = 0
    for i, b in enumerate(data):
        if 32 <= b < 127:
            if not current:
                start = i
            current.append(chr(b))
        else:
            if len(current) >= 6:
                s = ''.join(current).strip()
                if s and len(s) >= 6:
                    strings.append((start, s))
            current = []
    if len(current) >= 6:
        strings.append((start, ''.join(current).strip()))

    print(f"  Total strings (>=6 chars): {len(strings)}")
    print(f"  First 80 strings:")
    for pos, s in strings[:80]:
        print(f"  [{pos:07X}] {s!r}")

    # Find strings that look like table.field references
    field_refs = [(pos, s) for pos, s in strings if '.' in s and len(s) < 50]
    print(f"\n  Strings with dots (field refs?): {len(field_refs)}")
    for pos, s in field_refs[:50]:
        print(f"  [{pos:07X}] {s!r}")


if __name__ == '__main__':
    extract_filerel()
    extract_files_table()
    extract_filedict_sample()
