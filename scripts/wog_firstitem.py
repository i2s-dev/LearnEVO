#!/usr/bin/env python3
"""
wog_firstitem.py — For each WO, find the FIRST mandatory WOBOM item
by COMPCODE sort (Btrieve default key order), check its REMAINING qty.
Hypothesis: if first item has REMAINING=0, WINPOS passes 0 to T7WOG4 → freeze.
"""
import pyodbc, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

con = pyodbc.connect("DSN=DBA", autocommit=True)
cur = con.cursor()

WOS = [
    ('75338','1','works'),
    ('75338','2','FREEZES'),
    ('75338','3','works'),
    ('75338','4','FREEZES'),
    ('75338','5','works'),
    ('75405','3','FREEZES'),
    ('54552','1','FREEZES'),
]

print("=" * 90)
print("FIRST MANDATORY WOBOM ITEM BY COMPCODE — is REMAINING = 0?")
print("=" * 90)
print(f"{'WO':<14} {'STATUS':<10} {'FIRST_COMPCODE':<28} {'TOTQTY':>8} {'QTYISSUED':>10} {'REMAINING':>10}  PREDICTION")
print("-" * 90)

for wopre, wosuf, status in WOS:
    cur.execute("""
        SELECT WOBOM_COMPCODE, WOBOM_TOTQTY, WOBOM_QTYISSUED,
               WOBOM_TOTQTY - WOBOM_QTYISSUED AS remaining
        FROM WOBOM
        WHERE WOBOM_WOPRE=? AND WOBOM_WOSUF=? AND WOBOM_OPTION='N'
        ORDER BY WOBOM_COMPCODE
    """, wopre, wosuf)
    rows = cur.fetchall()
    if not rows:
        print(f"{wopre+'-'+wosuf:<14} {status:<10} {'(no mandatory items)':<28} {'':>8} {'':>10} {'':>10}  → TERMINATE (no records)")
        continue
    first = rows[0]
    comp = str(first[0]).strip()
    totqty = float(first[1] or 0)
    qtyissued = float(first[2] or 0)
    remaining = float(first[3] or 0)
    prediction = "→ FREEZE (REMAINING=0)" if remaining <= 0 else "→ OK (REMAINING>0)"
    print(f"{wopre+'-'+wosuf:<14} {status:<10} {comp:<28} {totqty:>8.1f} {qtyissued:>10.1f} {remaining:>10.1f}  {prediction}")

# Also show all mandatory items for each WO sorted by COMPCODE to see the full picture
print()
print("=" * 90)
print("FULL MANDATORY LIST SORTED BY COMPCODE — first item drives WINPOS")
print("=" * 90)
for wopre, wosuf, status in WOS:
    cur.execute("""
        SELECT WOBOM_COMPCODE, WOBOM_TOTQTY, WOBOM_QTYISSUED,
               WOBOM_TOTQTY - WOBOM_QTYISSUED AS remaining
        FROM WOBOM
        WHERE WOBOM_WOPRE=? AND WOBOM_WOSUF=? AND WOBOM_OPTION='N'
        ORDER BY WOBOM_COMPCODE
    """, wopre, wosuf)
    rows = cur.fetchall()
    print(f"\n{wopre}-{wosuf} ({status}) — {len(rows)} mandatory items:")
    for i, r in enumerate(rows):
        marker = " ← FIRST (drives WINPOS)" if i == 0 else ""
        issue_flag = " [FULLY ISSUED]" if float(r[1] or 0) > 0 and float(r[3] or 0) <= 0 else \
                     " [PARTIAL]" if 0 < float(r[2] or 0) < float(r[1] or 0) else \
                     " [ZERO QTY]" if float(r[1] or 0) == 0 else ""
        print(f"  {str(r[0]).strip():<28} rem={float(r[3] or 0):>8.1f}{issue_flag}{marker}")

con.close()
