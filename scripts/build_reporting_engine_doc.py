"""
Parse rtm_callers.csv to build a comprehensive RTM cross-reference.
Append to docs/05-reports/overview.md.
"""
import sys, csv, re
from collections import defaultdict
sys.stdout.reconfigure(encoding='utf-8')

CSV_PATH = r'C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\samples\rtm_callers.csv'
OUT_PATH = r'C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\docs\05-reports\overview.md'

# Module prefix → module name
MODULE_MAP = {
    'BKAP': 'AP', 'T6AP': 'AP', 'APS': 'AP (1099)',
    'BKAR': 'AR', 'T6AR': 'AR',
    'BKGL': 'GL', 'T6GL': 'GL',
    'BKSO': 'SO', 'T6SO': 'SO', 'T6ALSO': 'SO (legacy)',
    'BKWO': 'WO', 'T6WO': 'WO',
    'BKIN': 'IN', 'T6IN': 'IN',
    'BKPO': 'PO', 'T6PO': 'PO',
    'BKPR': 'PR', 'T6PR': 'PR',
    'BKBM': 'BM', 'T6BM': 'BM',
    'BKCM': 'CM', 'T6CM': 'CM',
    'BKDC': 'DC', 'T6DC': 'DC',
    'BKRO': 'RO', 'T6RO': 'RO',
    'BKMR': 'MR', 'T6MR': 'MR', 'AUTOT7MRF': 'MR',
    'BKPI': 'PI', 'T6PI': 'PI',
    'BKSH': 'SH', 'T6SH': 'SH',
    'BKSA': 'SA', 'T6SA': 'SA',
    'BKJC': 'JC', 'T6JC': 'JC',
    'BKLW': 'LW', 'T6LW': 'LW',
    'BKWC': 'WC', 'T6WC': 'WC',
    'BKQC': 'QC', 'T6QC': 'QC',
    'BKAM': 'AM', 'T6AM': 'AM',
    'BKGF': 'GF', 'T6GF': 'GF',
    'BKMH': 'MH', 'T6MH': 'MH',
    'BKUT': 'UT', 'T6UT': 'UT', 'UTKA': 'UT',
    'ISREP': 'IS Reports', 'ISSRD': 'SR', 'ISSREP': 'SR',
    'ISLC': 'LC', 'ISSC': 'SC',
    'J6': 'J7 (custom)', 'J7': 'J7 (custom)',
    'cfg': 'platform', 'ent': 'platform', 'temp': 'platform',
    'bk': 'generic', 'dflt': 'generic',
}

def get_module(caller):
    caller_upper = caller.upper()
    for prefix, mod in MODULE_MAP.items():
        if caller_upper.startswith(prefix.upper()):
            return mod
    # T7 prefix — look at 4th char onward
    if caller_upper.startswith('T7'):
        rest = caller_upper[2:4]
        for prefix, mod in MODULE_MAP.items():
            if rest == prefix.upper()[:2]:
                return mod + ' (T7)'
    return 'Other'

# Read CSV
rtm_to_callers = {}
with open(CSV_PATH, newline='', encoding='utf-8', errors='replace') as f:
    reader = csv.DictReader(f)
    for row in reader:
        rtm = row['rtm'].strip()
        callers = [c.strip() for c in row['callers'].split(';') if c.strip()]
        rtm_to_callers[rtm] = callers

# Group RTMs by module
module_rtms = defaultdict(list)
for rtm, callers in sorted(rtm_to_callers.items()):
    # Assign to the most-common module among callers
    mod_counts = defaultdict(int)
    for c in callers:
        mod_counts[get_module(c)] += 1
    primary_mod = max(mod_counts, key=mod_counts.get)
    module_rtms[primary_mod].append((rtm, len(callers), callers))

# Sort modules
sorted_mods = sorted(module_rtms.keys())

# Build output block
lines = [
    '',
    '---',
    '',
    '## Pass 101 — RTM Cross-Reference by Module (2026-06-18)',
    '',
    f'Total: **{len(rtm_to_callers)} RTMs** mapped from `rtm_callers.csv`.',
    '',
    'Each RTM is listed under its primary calling module. "Callers" are the RWN/RUN',
    'program names that invoke each RTM via `EXEC_RB` / `RTM_FN`.',
    '',
]

# Summary table — RTMs per module
lines += [
    '### RTM Count by Module',
    '',
    '| Module | RTM Count |',
    '|--------|-----------|',
]
for mod in sorted_mods:
    lines.append(f'| {mod} | {len(module_rtms[mod])} |')
lines.append('')
lines.append('---')
lines.append('')

# Detail section per module
for mod in sorted_mods:
    rtm_list = sorted(module_rtms[mod])
    if len(rtm_list) > 50:
        # Only list top entries for large modules
        lines.append(f'### {mod} Module RTMs ({len(rtm_list)} total — showing first 30)')
        rtm_list = rtm_list[:30]
    else:
        lines.append(f'### {mod} Module RTMs ({len(rtm_list)} total)')
    lines.append('')
    lines.append('| RTM File | Callers |')
    lines.append('|----------|---------|')
    for rtm, cnt, callers in rtm_list:
        caller_str = ', '.join(callers[:8])
        if len(callers) > 8:
            caller_str += f' (+{len(callers)-8} more)'
        lines.append(f'| `{rtm}` | {caller_str} |')
    lines.append('')

lines.append('---')
lines.append('')
lines.append('*RTM cross-reference auto-generated from `samples/rtm_callers.csv` (Pass 101, 2026-06-18).*')
lines.append('')

block = '\n'.join(lines)

# Read existing doc and append
with open(OUT_PATH, encoding='utf-8') as f:
    existing = f.read()

with open(OUT_PATH, 'w', encoding='utf-8') as f:
    f.write(existing + block)

print(f'Appended {len(block)} chars to overview.md')
print(f'{len(rtm_to_callers)} RTMs across {len(sorted_mods)} module groups')
