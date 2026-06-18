"""
Pass 103 — DFM batch analysis for AP/AR/PO/SO module forms.
Reads DFM files in samples/dfm/ and extracts:
 - Caption strings (form title, field labels)
 - DataField names (table field references)
 - TableName references (database table bindings)
 - Name properties (component names)
Output: scripts/dfm_ap_ar_po_so_analysis.txt
"""
import sys, os, re
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')

DFM_DIR = Path(r'C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\samples\dfm')
OUT = Path(r'C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\scripts\dfm_ap_ar_po_so_analysis.txt')

# Patterns to extract
RE_CAPTION = re.compile(r"Caption\s*=\s*'([^']+)'", re.IGNORECASE)
RE_DATAFIELD = re.compile(r"DataField\s*=\s*'([^']+)'", re.IGNORECASE)
RE_TABLENAME = re.compile(r"TableName\s*=\s*'([^']+)'", re.IGNORECASE)
RE_OBJECT_NAME = re.compile(r"^object\s+(\w+)\s*:", re.IGNORECASE | re.MULTILINE)
RE_SQL = re.compile(r"(?:SQL|CommandText)\s*=\s*\([\s\S]*?\)", re.IGNORECASE)
RE_HINT = re.compile(r"Hint\s*=\s*'([^']+)'", re.IGNORECASE)

# Target prefixes
PREFIXES = ['T7AP', 'T7AR', 'T7PO', 'T7SO']

def analyze_dfm(path):
    try:
        raw = path.read_bytes()
        try:
            text = raw.decode('utf-8', errors='replace')
        except Exception:
            text = raw.decode('latin-1', errors='replace')
    except Exception as e:
        return None

    result = {
        'file': path.name,
        'tables': sorted(set(RE_TABLENAME.findall(text))),
        'datafields': sorted(set(RE_DATAFIELD.findall(text))),
        'captions': sorted(set(RE_CAPTION.findall(text))),
        'hints': sorted(set(RE_HINT.findall(text))),
        'component_count': len(RE_OBJECT_NAME.findall(text)),
    }
    return result

lines = []
counts = {p: 0 for p in PREFIXES}
all_files = []

for path in sorted(DFM_DIR.glob('*.DFM')):
    for pfx in PREFIXES:
        if path.name.upper().startswith(pfx):
            all_files.append((pfx, path))
            counts[pfx] += 1
            break

lines.append(f'DFM Analysis — AP/AR/PO/SO Module Forms')
lines.append(f'Generated: Pass 103, 2026-06-18')
lines.append(f'Total forms analyzed: {len(all_files)}')
for pfx, n in counts.items():
    lines.append(f'  {pfx}*: {n} files')
lines.append('=' * 80)

for pfx, path in all_files:
    r = analyze_dfm(path)
    if r is None:
        lines.append(f'\n[{path.name}] ERROR: could not read')
        continue
    lines.append(f'\n### {r["file"]}')
    lines.append(f'  Components: {r["component_count"]}')
    if r['tables']:
        lines.append(f'  Tables: {", ".join(r["tables"])}')
    if r['datafields']:
        top = r['datafields'][:60]
        lines.append(f'  DataFields ({len(r["datafields"])}): {", ".join(top)}{"..." if len(r["datafields"]) > 60 else ""}')
    # Only show captions that look like field labels (short, not pure boilerplate)
    useful_caps = [c for c in r['captions'] if len(c) < 60 and c not in ('', ' ', '&')
                   and not c.startswith('{') and not c.startswith('http')]
    if useful_caps:
        lines.append(f'  Captions ({len(useful_caps)}): {", ".join(useful_caps[:40])}')

OUT.write_text('\n'.join(lines), encoding='utf-8')
print(f'Wrote {len(lines)} lines to {OUT}')
print(f'Files analyzed: {len(all_files)} ({", ".join(f"{n} {p}*" for p, n in counts.items())})')
