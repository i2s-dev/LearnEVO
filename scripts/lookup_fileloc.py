"""Look up physical file names for specific tables in FILELOC."""
import csv
from pathlib import Path

SAMPLES = Path(r"C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\samples")

rows = list(csv.DictReader(open(SAMPLES / 'fileloc_mappings.csv', encoding='utf-8')))
targets = {
    'BKSLEVEL', 'BKSLMSTR', 'BKSYUSER', 'BKUPDATE', 'MENUFILE', 'PRGFILE',
    'PRGFILE2', 'DBAHELP', 'DBAHLPID', 'ISNOTESC', 'DEFAULTS', 'FIELDDEF',
    'FIELDS', 'FILEDEF', 'INDEXDEF', 'WBTRVMEM', 'DBAUSRMN',
    # Also check a few known tables for comparison
    'AHSYLOG', 'BKCMACCC', 'BKACTRPT'
}

found = [r for r in rows if r['logical_table'] in targets]
if found:
    for r in sorted(found, key=lambda x: (x['logical_table'], x['location'])):
        diff = ' (ALIAS!)' if r['logical_table'] != r['physical_file'] else ''
        print(f"{r['logical_table']:16} -> {r['physical_file']:16} [{r['location']}]{diff}")
else:
    print("None found in fileloc_mappings.csv")

# Also check which targets are NOT in fileloc at all
found_tables = {r['logical_table'] for r in found}
not_found = targets - found_tables
if not_found:
    print(f"\nNOT found in FILELOC: {sorted(not_found)}")
