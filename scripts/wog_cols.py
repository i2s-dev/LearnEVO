#!/usr/bin/env python3
import pyodbc, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
con = pyodbc.connect("DSN=DBA", autocommit=True)
cur = con.cursor()

# Get WORKORD columns
cur.execute("SELECT TOP 1 * FROM WORKORD WHERE MTWO_WIP_WOPRE='75338' AND MTWO_WIP_WOSUF='3'")
cols = [c[0] for c in cur.description]
print("WORKORD columns:")
for c in cols:
    print(f"  {c}")

print()
# Get WOBOM columns
cur.execute("SELECT TOP 1 * FROM WOBOM WHERE WOBOM_WOPRE='75338' AND WOBOM_WOSUF='1'")
cols2 = [c[0] for c in cur.description]
print("WOBOM columns (first 30):")
for c in cols2[:30]:
    print(f"  {c}")
con.close()
