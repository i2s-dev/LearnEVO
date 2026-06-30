"""
Extract the complete EvoERP field dictionary from FILEDICT.UPD.

Record format (derived from hex analysis):
  [table_name: 8 bytes, space-padded] + [field_path: TAS Pro dot-notation]

The field path uses dot notation: TABLE_ALIAS.FIELD_NAME or
TABLE_ALIAS.SUB.FIELD_NAME (e.g. AHSY.USER.CTRL, BKAB.EXP).

Output: CSV with columns: table, field_path, record_offset
"""
import re
import csv
from pathlib import Path
from collections import defaultdict

SAMPLES = Path(r"C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\samples")
OUT_CSV = SAMPLES / "filedict_fields.csv"
PAGE_SIZE = 4096


def is_table_name(s):
    """Check if 8-byte string looks like an EvoERP table name."""
    stripped = s.rstrip()
    if len(stripped) < 3:
        return False
    # Must start with uppercase letter
    if not (65 <= ord(stripped[0]) <= 90):
        return False
    # All chars must be uppercase, digits, or spaces
    return all(c.isdigit() or (c.isupper()) or c == ' ' for c in s)


def is_field_path(s):
    """Check if string looks like a TAS Pro field path (has a dot)."""
    return '.' in s and len(s) >= 4 and all(
        c.isalnum() or c in '._- ' for c in s.rstrip()
    )


def extract_records(data):
    """
    Extract table+field records from FILEDICT data.
    Strategy: find positions where 8 bytes look like a table name
    immediately followed by a dot-notation field path.
    """
    records = []
    i = 0
    n = len(data)

    while i < n - 16:
        # Check for 8-byte table name pattern
        chunk8 = data[i:i + 8]
        try:
            s8 = chunk8.decode('ascii')
        except Exception:
            i += 1
            continue

        if not is_table_name(s8):
            i += 1
            continue

        # What follows must be a field path (with dot notation)
        rest_end = min(i + 8 + 60, n)
        rest = data[i + 8:rest_end]
        try:
            rest_str = rest.decode('ascii')
        except Exception:
            i += 1
            continue

        # Extract up to first non-printable or null
        field = ''
        for c in rest_str:
            if 32 <= ord(c) < 127:
                field += c
            else:
                break

        field = field.strip()

        if is_field_path(field) and len(field) >= 4:
            table = s8.rstrip()
            # Filter out garbage (too many special chars)
            dot_count = field.count('.')
            alpha_count = sum(1 for c in field if c.isalpha())
            if dot_count >= 1 and alpha_count >= 3:
                records.append((i, table, field))
                # Skip ahead past this record to avoid duplicates
                i += 8 + len(field) + 1
                continue

        i += 1

    return records


def deduplicate(records):
    """Remove duplicate (table, field) pairs, keeping first occurrence."""
    seen = set()
    unique = []
    for offset, table, field in records:
        key = (table, field)
        if key not in seen:
            seen.add(key)
            unique.append((offset, table, field))
    return unique


def main():
    path = SAMPLES / "FILEDICT.UPD"
    data = path.read_bytes()
    print(f"FILEDICT.UPD: {len(data):,} bytes")

    records = extract_records(data)
    print(f"Raw records found: {len(records)}")

    unique = deduplicate(records)
    print(f"Unique (table, field) pairs: {len(unique)}")

    # Group by table
    by_table = defaultdict(list)
    for offset, table, field in unique:
        by_table[table].append((offset, field))

    print(f"Unique tables: {len(by_table)}")

    # Sort by table name, then field
    rows = []
    for table in sorted(by_table):
        for offset, field in sorted(by_table[table], key=lambda x: x[1]):
            rows.append({'table': table, 'field_path': field, 'offset': hex(offset)})

    # Write CSV
    with open(OUT_CSV, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['table', 'field_path', 'offset'])
        writer.writeheader()
        writer.writerows(rows)
    print(f"Written to {OUT_CSV}")

    # Print sample by table (first 30 tables, up to 10 fields each)
    print("\n=== SAMPLE OUTPUT (first 30 tables) ===")
    shown = 0
    for table in sorted(by_table)[:30]:
        fields = sorted(by_table[table], key=lambda x: x[1])
        print(f"\n  {table} ({len(fields)} fields):")
        for _, field in fields[:10]:
            print(f"    {field}")
        if len(fields) > 10:
            print(f"    ... ({len(fields) - 10} more)")
        shown += 1

    # Tables with most fields
    print("\n=== TOP 20 TABLES BY FIELD COUNT ===")
    top = sorted(by_table.items(), key=lambda x: len(x[1]), reverse=True)[:20]
    for table, fields in top:
        print(f"  {table:12}: {len(fields)} fields")

    # Show specific interesting tables
    print("\n=== SECURITY TABLE: AHSYLOG ===")
    for _, field in sorted(by_table.get('AHSYLOG', []), key=lambda x: x[1]):
        print(f"  {field}")

    print("\n=== BK.SHORT / BK.DESC VIRTUAL FIELDS ===")
    for table in sorted(by_table):
        if table.startswith('BK.') or table in ('BK', 'BKAB', 'BKAC'):
            print(f"  {table}:")
            for _, field in sorted(by_table[table], key=lambda x: x[1])[:20]:
                print(f"    {field}")


if __name__ == '__main__':
    main()
