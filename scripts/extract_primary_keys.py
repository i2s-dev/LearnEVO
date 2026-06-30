"""
Extract primary key (index 0, segment order) for every table in DSN=DBA.

X$Index columns (Pervasive PSQL DDF):
  Xi$File    — FK to X$File.Xf$Id
  Xi$Number  — index number (0 = primary key)
  Xi$Field   — FK to X$Field.Xf$Id
  Xi$Part    — segment order within the index

X$File columns:
  Xf$Id, Xf$Name (table name), Xf$Loc (file path)

X$Field columns:
  Xf$Id, Xf$Name (field name), Xf$Type, Xf$Size
"""
import pyodbc
import csv
from pathlib import Path
from collections import defaultdict

DSN = "DBA"
OUT_CSV = Path(r"C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\samples\primary_keys.csv")

def main():
    conn = pyodbc.connect(f"DSN={DSN}", timeout=30)
    cur = conn.cursor()

    # Build table-id → name map
    cur.execute("SELECT Xf$Id, Xf$Name FROM X$File")
    tables = {row[0]: row[1].strip() for row in cur.fetchall()}

    # Build field-id → (table_name, field_name, type, size) map
    cur.execute("SELECT Xe$Id, Xe$File, Xe$Name, Xe$DataType, Xe$Size FROM X$Field")
    fields = {}
    for row in cur.fetchall():
        fields[row[0]] = (tables.get(row[1], '?'), row[2].strip(), row[3], row[4])

    # Query all index segments
    cur.execute("""
        SELECT Xi$File, Xi$Number, Xi$Field, Xi$Part, Xi$Flags
        FROM X$Index
        ORDER BY Xi$File, Xi$Number, Xi$Part
    """)
    idx_rows = cur.fetchall()
    conn.close()

    # Group by (table_file_id, index_number)
    idx_map = defaultdict(list)
    for row in idx_rows:
        file_id, idx_num, field_id, part, flags = row
        idx_map[(file_id, idx_num)].append((part, field_id, flags))

    # Collect primary keys (index 0) per table
    pk_by_table = {}
    for (file_id, idx_num), segs in sorted(idx_map.items()):
        table_name = tables.get(file_id, f'?{file_id}')
        if idx_num == 0:
            seg_fields = []
            for part, field_id, flags in sorted(segs, key=lambda x: x[0]):
                fname = fields.get(field_id, ('?', '?', '?', '?'))[1]
                ftype = fields.get(field_id, ('?', '?', '?', '?'))[2]
                fsize = fields.get(field_id, ('?', '?', '?', '?'))[3]
                desc = ''
                if flags & 0x08:
                    desc += 'DESC '
                if flags & 0x01:
                    desc += 'DUP '
                seg_fields.append((fname, ftype, fsize, desc.strip()))
            pk_by_table[table_name] = seg_fields

    # Also find tables with NO index 0 (no primary key defined in DDF)
    all_file_ids_with_pk = {file_id for (file_id, idx_num) in idx_map if idx_num == 0}
    no_pk_tables = [tables[fid] for fid in tables if fid not in all_file_ids_with_pk]

    # Write CSV
    rows = []
    for table, segs in sorted(pk_by_table.items()):
        for i, (fname, ftype, fsize, desc) in enumerate(segs):
            rows.append({
                'table': table,
                'pk_segment': i + 1,
                'pk_field': fname,
                'field_type': ftype,
                'field_size': fsize,
                'flags': desc,
            })

    with open(OUT_CSV, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['table', 'pk_segment', 'pk_field', 'field_type', 'field_size', 'flags'])
        writer.writeheader()
        writer.writerows(rows)

    print(f"Written {len(rows)} rows to {OUT_CSV}")
    print(f"Tables with primary key: {len(pk_by_table)}")
    print(f"Tables with NO primary key in DDF: {len(no_pk_tables)}")
    if no_pk_tables:
        print(f"  No-PK tables: {sorted(no_pk_tables)[:20]}")

    # Summary: single-field vs compound PKs
    single_pk = sum(1 for segs in pk_by_table.values() if len(segs) == 1)
    compound_pk = sum(1 for segs in pk_by_table.values() if len(segs) > 1)
    print(f"\nPrimary key breakdown:")
    print(f"  Single-field PKs: {single_pk}")
    print(f"  Compound PKs (2+ fields): {compound_pk}")

    # Show first 30 tables with their PK
    print("\nSample (first 30 tables):")
    for table, segs in sorted(pk_by_table.items())[:30]:
        pk_str = ' + '.join(f[0] for f in segs)
        print(f"  {table}: {pk_str}")


if __name__ == '__main__':
    main()
