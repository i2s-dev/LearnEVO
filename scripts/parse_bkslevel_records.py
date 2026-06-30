"""
Parse BKSLEVEL.B Btrieve file — security level access masks.

From binary analysis:
  - File: FC magic, 50,176 bytes, 12 pages × 4096
  - FCR at offset 0: header bytes give record size
  - Data: level code ('1','2'...'9') + space + 420 bytes of 'N'/'Y' access flags
  - Record structure is ~422 bytes of visible content

Goal: extract all security level records with their full access masks.
Also analyze BKSLMSTR.B if present.
"""
import struct
from pathlib import Path
from collections import defaultdict

SAMPLES = Path(r"C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\samples")
PAGE_SIZE = 4096


def read_fcr_fields(data):
    """Extract key fields from a Btrieve FCR (File Control Record) at page 0."""
    fcr = data[:PAGE_SIZE]
    print("FCR header analysis:")
    # Scan for potential record-size values (should be 100-2000 range)
    for off in range(0, 128, 2):
        val = struct.unpack_from('<H', fcr, off)[0]
        if 100 <= val <= 2000:
            print(f"  FCR[{off:02X}] = {val} (possible record size or related)")
    # Also check 4-byte values
    for off in range(0, 64, 4):
        val = struct.unpack_from('<I', fcr, off)[0]
        if 100 <= val <= 5000:
            print(f"  FCR[{off:02X}] 4B = {val}")


def find_data_pages(data):
    """Identify non-FCR pages that contain actual record data."""
    n_pages = len(data) // PAGE_SIZE
    data_pages = []
    for pg in range(n_pages):
        offset = pg * PAGE_SIZE
        page = data[offset:offset + PAGE_SIZE]
        # Skip pages that are mostly 0x00 or 0xFF (empty/index)
        content = sum(1 for b in page if b not in (0x00, 0xFF))
        if content > 200 and pg > 0:
            data_pages.append((pg, offset, content))
    return data_pages


def extract_security_levels(data):
    """
    Extract security level records by scanning for the 'N' run pattern.
    Each record appears to be: [binary prefix] + [level: '0'-'9' or letters] + [space] + [420 'N'/'Y' bytes]

    We'll look for unique occurrences: find first occurrence of each level+mask combo.
    """
    print("\n=== BKSLEVEL.B Security Levels ===")

    # The run at 0x642A shows: byte 0x35='5', 0x20=' ', then 420x 0x4E='N'
    # Try to identify record boundaries by looking for sequences of:
    #   [1-2 byte level code] [420 bytes of Y/N flags]
    # where level code is printable ASCII digit or letter

    # Strategy: find all positions where a printable char is followed by a space,
    # followed by 200+ bytes of 'N' (0x4E) or 'Y' (0x59)
    records = []
    pos = 0
    while pos < len(data) - 430:
        b0 = data[pos]
        b1 = data[pos + 1]
        b2 = data[pos + 2]
        # Look for: [printable digit/letter] [space] [N/Y N/Y N/Y ...]
        if (32 <= b0 < 127 and b1 == 0x20 and b2 in (0x4E, 0x59)):
            # Count the Y/N run
            n_flags = 0
            while pos + 2 + n_flags < len(data) and data[pos + 2 + n_flags] in (0x4E, 0x59):
                n_flags += 1
            if n_flags >= 100:  # real record
                level_code = chr(b0)
                mask = bytes(data[pos + 2:pos + 2 + n_flags])
                y_count = mask.count(0x59)
                n_count = mask.count(0x4E)
                records.append({
                    'offset': pos,
                    'level': level_code,
                    'mask_len': n_flags,
                    'y_flags': y_count,
                    'n_flags': n_count,
                    'mask': mask
                })
                pos += 2 + n_flags
                continue
        pos += 1

    # Deduplicate by level code (keep longest mask per level)
    by_level = {}
    for r in records:
        if r['level'] not in by_level or r['mask_len'] > by_level[r['level']]['mask_len']:
            by_level[r['level']] = r

    print(f"Unique security levels found: {len(by_level)}")
    for level in sorted(by_level.keys()):
        r = by_level[level]
        print(f"\n  Level '{level}' (offset {r['offset']:06X}):")
        print(f"    Mask length: {r['mask_len']} bytes")
        print(f"    Y (allow): {r['y_flags']}  N (deny): {r['n_flags']}")
        # Show positions of any 'Y' flags
        y_positions = [i for i, b in enumerate(r['mask']) if b == 0x59]
        if y_positions:
            print(f"    Y positions: {y_positions[:30]}")
        else:
            print(f"    All N (full deny)")
        # Show full mask as text (first 100 chars)
        print(f"    Mask[0:100]: {r['mask'][:100].decode('ascii')}")

    return by_level


def analyze_bkslmstr():
    """BKSLMSTR.B — the security level MASTER table (name + description per level)."""
    bkslmstr = SAMPLES / 'BKSLMSTR.B'
    if not bkslmstr.exists():
        print("\n  BKSLMSTR.B: not found in samples/")
        return
    data = bkslmstr.read_bytes()
    print(f"\n=== BKSLMSTR.B ({len(data):,} bytes) ===")
    # Extract strings
    strings = []
    current = []
    start = 0
    for i, b in enumerate(data):
        if 32 <= b < 127:
            if not current:
                start = i
            current.append(chr(b))
        else:
            if len(current) >= 3:
                strings.append((start, ''.join(current)))
            current = []
    print(f"  Printable strings: {len(strings)}")
    for pos, s in strings[:40]:
        print(f"  [{pos:06X}] {s!r}")


if __name__ == '__main__':
    data = (SAMPLES / 'BKSLEVEL.B').read_bytes()
    read_fcr_fields(data)
    extract_security_levels(data)
    analyze_bkslmstr()
