"""Query X$File for FILE* tables and then query each one."""
import pyodbc

conn = pyodbc.connect("DSN=DBA", timeout=30)
cur = conn.cursor()

# Check what FILE* tables are in the DDF
cur.execute("SELECT Xf$Id, Xf$Name, Xf$Loc FROM X$File ORDER BY Xf$Name")
all_tables = [(r[0], r[1].strip(), r[2].strip()) for r in cur.fetchall()]

file_tables = [(fid, name, loc) for fid, name, loc in all_tables if name.upper().startswith('FILE')]
print(f"FILE* tables in X$File ({len(file_tables)}):")
for fid, name, loc in file_tables:
    print(f"  [{fid}] {name:30} -> {loc}")

print()

# Try querying FILEDICT if it exists
dict_tables = [name for _, name, _ in file_tables]
print(f"All FILE* table names: {dict_tables}")

conn.close()
