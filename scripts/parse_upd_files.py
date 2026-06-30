"""
Parse EvoERP FILE*.UPD Btrieve data files.
These are Btrieve direct-access files (no DDF entries) forming EvoERP's
proprietary file dictionary system.

Btrieve file structure:
  - FCR (File Control Record) at offset 0 — one page
  - Data pages follow
  - Page size is stored in the FCR

FCR structure (Btrieve 6.x/7.x):
  0x00  2 bytes  page type / usage
  0x02  2 bytes  logical page size (in bytes)
  ...
"""
import struct
import re
from pathlib import Path

SAMPLES = Path(r"C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\samples")


def read_uint16(data, offset):
    return struct.unpack_from('<H', data, offset)[0]


def read_uint32(data, offset):
    return struct.unpack_from('<I', data, offset)[0]


def hex_dump(data, offset, length=64, label=''):
    chunk = data[offset:offset + length]
    hex_part = ' '.join(f'{b:02X}' for b in chunk)
    asc_part = ''.join(chr(b) if 32 <= b < 127 else '.' for b in chunk)
    print(f"  {label}[{offset:06X}] {hex_part}")
    print(f"  {'':10} {asc_part}")


def extract_strings(data, min_len=4):
    """Extract printable ASCII strings from binary data."""
    result = []
    current = []
    start = 0
    for i, b in enumerate(data):
        if 32 <= b < 127:
            if not current:
                start = i
            current.append(chr(b))
        else:
            if len(current) >= min_len:
                result.append((start, ''.join(current)))
            current = []
    if len(current) >= min_len:
        result.append((start, ''.join(current)))
    return result


def analyze_upd(filename):
    path = SAMPLES / filename
    data = path.read_bytes()
    size = len(data)
    print(f"\n{'=' * 60}")
    print(f"FILE: {filename}  ({size:,} bytes)")
    print('=' * 60)

    # FCR header
    hex_dump(data, 0, 64, 'FCR[0]: ')
    hex_dump(data, 64, 64, 'FCR[64]: ')

    # The Btrieve page size — typically at offset 0x04 or 0x08
    # Let's check multiple candidate locations
    for off in [2, 4, 6, 8, 10, 12]:
        val = read_uint16(data, off)
        if val in (512, 1024, 2048, 4096, 8192, 16384, 32768):
            print(f"  Possible page size @ offset {off}: {val}")

    # The first 'FC' magic = Btrieve 6.x FCR
    magic = data[0:2]
    print(f"  Magic bytes: {magic[0]:02X} {magic[1]:02X} ({chr(magic[0])}{chr(magic[1])})")

    # Find meaningful strings
    strings = extract_strings(data, min_len=5)
    print(f"\n  Printable strings (len>=5), first 60:")
    for offset, s in strings[:60]:
        print(f"    [{offset:06X}] {s!r}")


def compare_headers(f1, f2):
    """Compare headers of two UPD files to find structural constants vs variable fields."""
    d1 = (SAMPLES / f1).read_bytes()
    d2 = (SAMPLES / f2).read_bytes()
    print(f"\n--- Header diff: {f1} vs {f2} ---")
    for i in range(min(256, len(d1), len(d2))):
        if d1[i] != d2[i]:
            print(f"  offset {i:3d} (0x{i:02X}): {d1[i]:02X} vs {d2[i]:02X}")


if __name__ == '__main__':
    # Analyze small files first (skip evo.upd — it's only 3 bytes)
    for fname in ['FILECHSP.upd', 'FILEDEF.UPD', 'FILES.UPD', 'FILEREL.UPD']:
        analyze_upd(fname)

    print("\n\n--- HEADER COMPARISON: FILES.UPD vs FILEREL.UPD ---")
    compare_headers('FILES.UPD', 'FILEREL.UPD')

    print("\n\n--- HEADER COMPARISON: FILES.UPD vs FILEDEF.UPD ---")
    compare_headers('FILES.UPD', 'FILEDEF.UPD')
