"""Extract symbols from locally-copied EvoERPmenu.RWN."""
import sys
sys.path.insert(0, 'scripts')
from rwn_extract_symbols import extract_symbols

r = extract_symbols('samples/rwn/EvoERPmenu.RWN', decrypt=True)
print(f"Size: {r['size_bytes']:,}  Marker: {r['header']['format_marker']}  Source: {r['source_file']}")
print(f"Procs: {r['header']['proc_table_size']//53}  Vars: {r['header']['var_count']}  DB files: {len(r['db_files'])}")
print(f"\nFirst 30 procedures:")
for p in r['procedures'][:30]: print(f"  {p}")
print(f"\nDB files:")
for f in r['db_files'][:20]: print(f"  {f}")
print(f"\nFirst 40 named variables:")
named = [v for v in r['variables'] if v['type'] >= 0x20]
for v in named[:40]: print(f"  {v['name']}")
