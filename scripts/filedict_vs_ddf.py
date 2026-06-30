"""
Cross-reference FILEDICT tables vs PSQL DDF tables.
Identify:
  1. Tables in FILEDICT but NOT in DDF (Btrieve-only tables)
  2. Tables in DDF but NOT in FILEDICT (DDF-only tables, no TAS Pro field dict)
  3. Tables in both (confirmed both ways)

Also produce a combined table: DDF field count vs FILEDICT field count vs field aliases.
"""
import pyodbc
import csv
from pathlib import Path
from collections import defaultdict

SAMPLES = Path(r"C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\samples")


def load_filedict():
    rows = []
    with open(SAMPLES / 'filedict_fields.csv', encoding='utf-8') as f:
        for row in csv.DictReader(f):
            rows.append(row)
    by_table = defaultdict(list)
    for r in rows:
        by_table[r['table']].append(r['field_path'])
    return by_table


def load_ddf_tables():
    conn = pyodbc.connect("DSN=DBA", timeout=30)
    cur = conn.cursor()
    cur.execute("SELECT Xf$Name FROM X$File")
    tables = {r[0].strip() for r in cur.fetchall()}
    conn.close()
    return tables


def main():
    print("Loading FILEDICT data...")
    filedict = load_filedict()
    fd_tables = set(filedict.keys())

    print("Loading DDF tables via ODBC...")
    ddf_tables = load_ddf_tables()

    print(f"\nFILEDICT tables: {len(fd_tables)}")
    print(f"DDF tables:      {len(ddf_tables)}")

    in_fd_not_ddf = fd_tables - ddf_tables
    in_ddf_not_fd = ddf_tables - fd_tables
    in_both = fd_tables & ddf_tables

    print(f"\nIn FILEDICT but NOT in DDF: {len(in_fd_not_ddf)} (Btrieve-only access)")
    for t in sorted(in_fd_not_ddf):
        fields = filedict[t]
        print(f"  {t:16}: {len(fields)} field aliases — {', '.join(fields[:4])}" +
              (f", ..." if len(fields) > 4 else ""))

    print(f"\nIn DDF but NOT in FILEDICT: {len(in_ddf_not_fd)} tables (no TAS Pro field dict)")
    print(f"  (not shown — {len(in_ddf_not_fd)} tables without FILEDICT registration)")

    print(f"\nIn BOTH DDF and FILEDICT: {len(in_both)} tables (fully registered)")

    # Summary for OPEN_QUESTIONS update
    print("\n=== BK* pattern in Btrieve-only set ===")
    bk_only = sorted(t for t in in_fd_not_ddf if t.startswith('BK'))
    is_only = sorted(t for t in in_fd_not_ddf if t.startswith('IS'))
    mt_only = sorted(t for t in in_fd_not_ddf if t.startswith('MT'))
    other_only = sorted(t for t in in_fd_not_ddf if not t.startswith(('BK', 'IS', 'MT')))
    print(f"  BK* ({len(bk_only)}): {bk_only}")
    print(f"  IS* ({len(is_only)}): {is_only}")
    print(f"  MT* ({len(mt_only)}): {mt_only}")
    print(f"  Other ({len(other_only)}): {other_only}")


if __name__ == '__main__':
    main()
