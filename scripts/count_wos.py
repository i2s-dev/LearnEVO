import pyodbc

conn = pyodbc.connect('DSN=DBA;UID=;PWD=', autocommit=True)
cur = conn.cursor()

# Item type field is single-char BKIC_PROD_TYPE
# "RFAM" in the filter = include types R, F, A, M
# Find the key column in BKICMSTR
cur.execute("SELECT TOP 1 * FROM BKICMSTR")
cols = [d[0] for d in cur.description]
code_cols = [c for c in cols if 'CODE' in c.upper() or 'PART' in c.upper() or 'ITEM' in c.upper() or 'PROD' in c.upper()]
print("Item master key-candidate columns:", code_cols[:10])

# Most likely the item code field
# Check if BKIC_PROD_CODE exists
if 'BKIC_PROD_CODE' in cols:
    print("Join key: BKIC_PROD_CODE")
    key = 'BKIC_PROD_CODE'
else:
    print("Cols:", cols[:10])
    key = None

if key:
    # Full count: status S/F/R + priority 1/2/3 + item type R/F/A/M
    cur.execute(f"""
        SELECT COUNT(*) FROM WORKORD W
        JOIN BKICMSTR I ON RTRIM(W.MTWO_WIP_CODE) = RTRIM(I.{key})
        WHERE W.MTWO_WIP_STATUS IN ('S','F','R')
          AND W.MTWO_WIP_PRTY IN ('1','2','3')
          AND I.BKIC_PROD_TYPE IN ('R','F','A','M')
    """)
    print(f"\nFull filter (S/F/R + prio 1/2/3 + type R/F/A/M): {cur.fetchone()[0]}")

    # Without item type filter for comparison
    cur.execute(f"""
        SELECT COUNT(*) FROM WORKORD W
        JOIN BKICMSTR I ON RTRIM(W.MTWO_WIP_CODE) = RTRIM(I.{key})
        WHERE W.MTWO_WIP_STATUS IN ('S','F','R')
          AND W.MTWO_WIP_PRTY IN ('1','2','3')
    """)
    joined_all = cur.fetchone()[0]
    print(f"Same but all item types: {joined_all}")

    # Count WOs with no matching item in BKICMSTR (rework/special WOs)
    cur.execute(f"""
        SELECT COUNT(*) FROM WORKORD W
        WHERE W.MTWO_WIP_STATUS IN ('S','F','R')
          AND W.MTWO_WIP_PRTY IN ('1','2','3')
          AND NOT EXISTS (SELECT 1 FROM BKICMSTR I WHERE RTRIM(I.{key}) = RTRIM(W.MTWO_WIP_CODE))
    """)
    no_item = cur.fetchone()[0]
    print(f"WOs with no item master record: {no_item}")

    # Breakdown by item type
    cur.execute(f"""
        SELECT I.BKIC_PROD_TYPE, COUNT(*) as cnt
        FROM WORKORD W
        JOIN BKICMSTR I ON RTRIM(W.MTWO_WIP_CODE) = RTRIM(I.{key})
        WHERE W.MTWO_WIP_STATUS IN ('S','F','R')
        GROUP BY I.BKIC_PROD_TYPE
        ORDER BY cnt DESC
    """)
    print("\nActive WO breakdown by item type:")
    for row in cur.fetchall():
        print(f"  Type '{row[0]}': {row[1]}")

    # Breakdown by priority
    cur.execute("""
        SELECT MTWO_WIP_PRTY, COUNT(*) as cnt
        FROM WORKORD
        WHERE MTWO_WIP_STATUS IN ('S','F','R')
        GROUP BY MTWO_WIP_PRTY
        ORDER BY cnt DESC
    """)
    print("\nActive WO breakdown by priority:")
    for row in cur.fetchall():
        print(f"  Priority '{row[0]}': {row[1]}")

conn.close()
