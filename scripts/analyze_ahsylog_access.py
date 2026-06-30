"""
Analyze AHSYLOG access flags to determine which ACCES_1..20 index maps to which module.

Strategy:
1. Query AHSYLOG schema from X$Field to get all field names + types
2. Pull all user records (anonymized — just look at Y/N patterns)
3. Cross-reference known user roles against flag patterns
4. Look at BKSLEVEL (security level) to see if levels define the same flag layout
5. Compare DBAHLPID module codes against flag count (20 flags vs 43 modules = 20 groups)
"""
import pyodbc
import csv
from pathlib import Path
from collections import Counter

DSN = "DBA"
SAMPLES = Path(r"C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\samples")

def get_connection():
    return pyodbc.connect(f"DSN={DSN}", timeout=10)


def get_table_id(cursor, table_name):
    cursor.execute("SELECT Xf$Id FROM X$File WHERE Xf$Name = ?", table_name)
    row = cursor.fetchone()
    return row[0] if row else None


def get_fields(cursor, table_id):
    cursor.execute(
        "SELECT Xe$Name, Xe$DataType, Xe$Offset, Xe$Size "
        "FROM X$Field WHERE Xe$File = ? ORDER BY Xe$Offset",
        table_id
    )
    return cursor.fetchall()


def main():
    print("Connecting to DSN=DBA...")
    conn = get_connection()
    cursor = conn.cursor()

    # ── 1. AHSYLOG schema ──────────────────────────────────────────────
    print("\n=== AHSYLOG schema ===")
    tid = get_table_id(cursor, "AHSYLOG")
    if not tid:
        print("AHSYLOG not found in DDF")
    else:
        fields = get_fields(cursor, tid)
        print(f"Table ID: {tid}, Field count: {len(fields)}")
        acces_fields = []
        for name, dtype, offset, size in fields:
            print(f"  {name:35} dtype={dtype} offset={offset} size={size}")
            if name.upper().startswith("AHSY_USER_ACCES"):
                acces_fields.append(name)
        print(f"\nACCES fields found: {acces_fields}")

    # ── 2. Pull actual AHSYLOG records ────────────────────────────────
    print("\n=== AHSYLOG user records ===")
    try:
        cursor.execute("SELECT * FROM AHSYLOG")
        rows = cursor.fetchall()
        col_names = [d[0] for d in cursor.description]
        print(f"Columns: {col_names}")
        print(f"Records: {len(rows)}")

        # Find ACCES column indices
        acces_idx = [i for i, c in enumerate(col_names) if c.upper().startswith("AHSY_USER_ACCES")]
        user_idx = next((i for i, c in enumerate(col_names) if "USER" in c.upper() and "CODE" in c.upper()), None)
        level_idx = next((i for i, c in enumerate(col_names) if "LEVL" in c.upper()), None)

        print(f"\nACCES column indices: {acces_idx}")
        print(f"User code column index: {user_idx}")
        print(f"Level column index: {level_idx}")

        if rows and acces_idx:
            print("\n--- Per-user access flag patterns ---")
            for row in rows:
                user = row[user_idx] if user_idx is not None else "?"
                level = row[level_idx] if level_idx is not None else "?"
                flags = [str(row[i]) if row[i] is not None else '?' for i in acces_idx]
                print(f"  User={str(user).strip():15} Level={str(level).strip():5} flags=[{' '.join(flags)}]")

            # Aggregate: for each flag position, count Y vs N vs other
            print("\n--- Flag position summary (all users) ---")
            flag_values = [[] for _ in acces_idx]
            for row in rows:
                for j, i in enumerate(acces_idx):
                    flag_values[j].append(str(row[i]).strip() if row[i] is not None else '')

            for j, vals in enumerate(flag_values):
                count = Counter(vals)
                print(f"  ACCES_{j+1:02d}: {dict(count)}")

        # Save raw records to CSV
        if rows:
            out = SAMPLES / 'ahsylog_records.csv'
            with open(out, 'w', newline='', encoding='utf-8') as f:
                w = csv.writer(f)
                w.writerow(col_names)
                for row in rows:
                    w.writerow([str(v).strip() if v is not None else '' for v in row])
            print(f"\nSaved {len(rows)} rows to {out}")

    except Exception as e:
        print(f"Error querying AHSYLOG: {e}")

    # ── 3. Also check BKPSUSER (authorization table) ──────────────────
    print("\n=== BKPSUSER schema ===")
    tid2 = get_table_id(cursor, "BKPSUSER")
    if not tid2:
        print("BKPSUSER not found in DDF (likely Btrieve-only)")
    else:
        fields2 = get_fields(cursor, tid2)
        print(f"Table ID: {tid2}, Field count: {len(fields2)}")
        for name, dtype, offset, size in fields2:
            print(f"  {name:35} dtype={dtype} offset={offset} size={size}")

    # ── 4. Try ISJAVA to see task command IDs ──────────────────────────
    print("\n=== ISJAVA task records ===")
    tid3 = get_table_id(cursor, "ISJAVA")
    if tid3:
        fields3 = get_fields(cursor, tid3)
        print(f"Table ID: {tid3}, Field count: {len(fields3)}")
        for name, dtype, offset, size in fields3:
            print(f"  {name:35} dtype={dtype}")
        try:
            cursor.execute("SELECT * FROM ISJAVA ORDER BY 1")
            jrows = cursor.fetchall()
            jcols = [d[0] for d in cursor.description]
            print(f"\nIJSAVA records: {len(jrows)}")
            for r in jrows[:30]:
                print(f"  {dict(zip(jcols, [str(v).strip() if v else '' for v in r]))}")
            if len(jrows) > 30:
                print(f"  ... ({len(jrows)-30} more)")
            # Save
            out2 = SAMPLES / 'isjava_records.csv'
            with open(out2, 'w', newline='', encoding='utf-8') as f:
                w2 = csv.writer(f)
                w2.writerow(jcols)
                for r in jrows:
                    w2.writerow([str(v).strip() if v else '' for v in r])
            print(f"Saved {len(jrows)} rows to {out2}")
        except Exception as e:
            print(f"Error querying ISJAVA: {e}")
    else:
        print("ISJAVA not found in DDF")

    conn.close()
    print("\nDone.")


if __name__ == '__main__':
    main()
