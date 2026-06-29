#!/usr/bin/env python3
"""
wog_correlate.py — Compare WOBOM/WORKORD data across freezing vs working WOs.
Includes 54552-1 as a new candidate. Goal: find the freeze-predicting variable.
"""
import pyodbc, sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

DSN = "DSN=DBA"
con = pyodbc.connect(DSN, autocommit=True)
cur = con.cursor()

WOPRES = ['54552', '75338', '75405']
WOSUF_MAP = {
    '75338': ['1','2','3','4','5'],
    '75405': ['3'],
    '54552': ['1'],
}

# ── 1. WORKORD summary ──────────────────────────────────────────────────────
print("=" * 80)
print("WORKORD STATUS / COST SUMMARY")
print("=" * 80)
print(f"{'WO':<14} {'STATUS':<8} {'COMQTY':<10} {'AMAT':>12}  NOTES")
print("-" * 80)

for wopre, sufs in WOSUF_MAP.items():
    for wosuf in sufs:
        cur.execute("""
            SELECT MTWO_WIP_STATUS, MTWO_WIP_COMQTY, MTWO_WIP_AMAT
            FROM WORKORD
            WHERE MTWO_WIP_WOPRE=? AND MTWO_WIP_WOSUF=?
        """, wopre, wosuf)
        row = cur.fetchone()
        if row:
            note = "FREEZES" if (wopre, wosuf) in [
                ('75338','2'),('75338','4'),('75405','3'),('54552','1')
            ] else "works"
            print(f"{wopre+'-'+wosuf:<14} {str(row[0]).strip():<8} {str(row[1]):<10} {float(row[2] or 0):>12.2f}  {note}")
        else:
            print(f"{wopre+'-'+wosuf:<14} (no WORKORD row)")

# ── 2. WOBOM OPTION distribution ────────────────────────────────────────────
print()
print("=" * 80)
print("WOBOM OPTION DISTRIBUTION  (N=mandatory, 1/2/3/4=optional groups)")
print("=" * 80)
print(f"{'WO':<14} {'N':>5} {'1':>5} {'2':>5} {'3':>5} {'4':>5} {'other':>7}  STATUS")
print("-" * 80)

for wopre, sufs in WOSUF_MAP.items():
    for wosuf in sufs:
        cur.execute("""
            SELECT WOBOM_OPTION, COUNT(*) AS CNT
            FROM WOBOM
            WHERE WOBOM_WOPRE=? AND WOBOM_WOSUF=?
            GROUP BY WOBOM_OPTION
            ORDER BY WOBOM_OPTION
        """, wopre, wosuf)
        rows = cur.fetchall()
        counts = {str(r[0]).strip(): r[1] for r in rows}
        n = counts.get('N', 0)
        o1 = counts.get('1', 0)
        o2 = counts.get('2', 0)
        o3 = counts.get('3', 0)
        o4 = counts.get('4', 0)
        other_keys = set(counts) - {'N','1','2','3','4'}
        other = sum(counts[k] for k in other_keys)
        note = "FREEZES" if (wopre, wosuf) in [
            ('75338','2'),('75338','4'),('75405','3'),('54552','1')
        ] else "works"
        print(f"{wopre+'-'+wosuf:<14} {n:>5} {o1:>5} {o2:>5} {o3:>5} {o4:>5} {other:>7}  {note}")
        if other_keys:
            print(f"  (other OPTION values: {other_keys})")

# ── 3. WOBOM issue state for mandatory (OPTION='N') items ───────────────────
print()
print("=" * 80)
print("MANDATORY ITEMS (OPTION='N') — ISSUE STATE")
print("=" * 80)
print(f"{'WO':<14} {'total_N':>8} {'fully_issued':>13} {'unissued':>9} {'partial':>8}")
print("-" * 80)

for wopre, sufs in WOSUF_MAP.items():
    for wosuf in sufs:
        cur.execute("SELECT COUNT(*) FROM WOBOM WHERE WOBOM_WOPRE=? AND WOBOM_WOSUF=? AND WOBOM_OPTION='N'", wopre, wosuf)
        total = cur.fetchone()[0]
        cur.execute("SELECT COUNT(*) FROM WOBOM WHERE WOBOM_WOPRE=? AND WOBOM_WOSUF=? AND WOBOM_OPTION='N' AND WOBOM_QTYISSUED >= WOBOM_TOTQTY AND WOBOM_TOTQTY > 0", wopre, wosuf)
        fully = cur.fetchone()[0]
        cur.execute("SELECT COUNT(*) FROM WOBOM WHERE WOBOM_WOPRE=? AND WOBOM_WOSUF=? AND WOBOM_OPTION='N' AND WOBOM_QTYISSUED = 0", wopre, wosuf)
        unissued = cur.fetchone()[0]
        cur.execute("SELECT COUNT(*) FROM WOBOM WHERE WOBOM_WOPRE=? AND WOBOM_WOSUF=? AND WOBOM_OPTION='N' AND WOBOM_QTYISSUED > 0 AND WOBOM_QTYISSUED < WOBOM_TOTQTY", wopre, wosuf)
        partial = cur.fetchone()[0]
        print(f"{wopre+'-'+wosuf:<14} {total:>8} {fully:>13} {unissued:>9} {partial:>8}")

# ── 4. Full WOBOM detail for 54552-1 ────────────────────────────────────────
print()
print("=" * 80)
print("54552-1 WOBOM DETAIL")
print("=" * 80)
cur.execute("""
    SELECT WOBOM_COMPCODE, WOBOM_OPTION, WOBOM_TOTQTY, WOBOM_QTYISSUED,
           WOBOM_TOTQTY - WOBOM_QTYISSUED AS remaining
    FROM WOBOM
    WHERE WOBOM_WOPRE='54552' AND WOBOM_WOSUF='1'
    ORDER BY WOBOM_OPTION, WOBOM_COMPCODE
""")
rows = cur.fetchall()
print(f"{'COMPCODE':<25} {'OPT':<5} {'TOTQTY':>10} {'QTYISSUED':>10} {'REMAINING':>10}")
print("-" * 65)
for r in rows:
    flag = " *** FULLY ISSUED" if r[1]=='N' and r[4] <= 0 else ""
    flag = flag or (" *** PARTIAL" if r[1]=='N' and 0 < r[3] < r[2] else "")
    print(f"{str(r[0]):<25} {str(r[1]):<5} {r[2]:>10.4f} {r[3]:>10.4f} {r[4]:>10.4f}{flag}")
print(f"\nTotal WOBOM rows for 54552-1: {len(rows)}")

# ── 5. Identify the "freeze predictor" variable ──────────────────────────────
print()
print("=" * 80)
print("FREEZE PREDICTOR ANALYSIS")
print("=" * 80)
print("Checking: unissued mandatory count, partial-issue state, no-mandatory")
print()

all_wos = []
for wopre, sufs in WOSUF_MAP.items():
    for wosuf in sufs:
        freeze = (wopre, wosuf) in [('75338','2'),('75338','4'),('75405','3'),('54552','1')]

        # mandatory count
        cur.execute("SELECT COUNT(*) FROM WOBOM WHERE WOBOM_WOPRE=? AND WOBOM_WOSUF=? AND WOBOM_OPTION='N'", wopre, wosuf)
        total_n = cur.fetchone()[0]
        cur.execute("SELECT COUNT(*) FROM WOBOM WHERE WOBOM_WOPRE=? AND WOBOM_WOSUF=? AND WOBOM_OPTION='N' AND WOBOM_QTYISSUED >= WOBOM_TOTQTY AND WOBOM_TOTQTY > 0", wopre, wosuf)
        fully_issued_n = cur.fetchone()[0]
        cur.execute("SELECT COUNT(*) FROM WOBOM WHERE WOBOM_WOPRE=? AND WOBOM_WOSUF=? AND WOBOM_OPTION='N' AND WOBOM_QTYISSUED=0", wopre, wosuf)
        unissued_n = cur.fetchone()[0]

        # OPTION='1' count
        cur.execute("""
            SELECT COUNT(*) FROM WOBOM WHERE WOBOM_WOPRE=? AND WOBOM_WOSUF=? AND WOBOM_OPTION='1'
        """, wopre, wosuf)
        opt1_count = cur.fetchone()[0]

        print(f"WO {wopre}-{wosuf}: {'FREEZE' if freeze else 'works  '} | "
              f"total_N={total_n} fully_issued={fully_issued_n} unissued_N={unissued_n} "
              f"OPTION='1'={opt1_count}")
        print(f"  → REMAINING unissued mandatory: {unissued_n}")
        if unissued_n == 0:
            print(f"  *** ZERO unissued mandatory items — likely freeze trigger ***")

con.close()
