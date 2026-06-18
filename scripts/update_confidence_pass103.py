"""Pass 103 confidence updates — PROJECT-STRUCTURE.md and Per-Table"""
import sys
sys.stdout.reconfigure(encoding='utf-8')

path = r'C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\EVO-DECOMPILE-TODO.md'

with open(path, encoding='utf-8') as f:
    content = f.read()

updates = [
    # Per-Table: 83 -> 87 (tier9: 19 more Java-confirmed table schemas)
    ('| Per-Table Narrative Docs | **83** | 88 | **5** ↑+7 Pass100 tier8-tables.md: 18 DDF-exact schemas (BKAPPO/BKAPPOL/BKGLTRAN/BKGLCOA/BKDCSHFT/WORKORD/BKICMSTR/BKARCUST/BKARINV/BKAPPOL/BKBMMSTR/etc 1240 fields) | 2026-06-18 |',
     '| Per-Table Narrative Docs | **87** | 88 | **1** ↑+4 Pass103 tier9-tables.md: 19 Java-confirmed schemas (BKSLEVEL/BKSYMSTR/ROUTING/WORKCTR/ISBSF/BKICLOC/BKBMMSTR/ISFOHEAD/ISFOLINE/ISSHIPCO/ISREMIND/CALENDAR/MACHINE/AHSYLOG/BKLOGON/etc) | 2026-06-18 |'),
    # PROJECT-STRUCTURE.md: 80 -> 86 (AP 6→26, AR 5→17, PO 0→30, SO 1→21 entries)
    ('| PROJECT-STRUCTURE.md | **80** | 90 | **10** ↑+8 Pass98 Pass19: 16 new tables, SH/MH/JS/GF module corrections, SM-I/J forms, SO/sched/backup DFMs | 2026-06-18 |',
     '| PROJECT-STRUCTURE.md | **86** | 90 | **4** ↑+6 Pass103 AP 6→26 entries, AR 5→17, PO 0→30 (full new section), SO 1→21; 171 DFM forms cataloged | 2026-06-18 |'),
]

changed = 0
for old, new in updates:
    if old in content:
        content = content.replace(old, new, 1)
        print(f'OK: {old[:80]}...')
        changed += 1
    else:
        print(f'NOT FOUND: {repr(old[:100])}')

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f'\nDone. {changed}/{len(updates)} replacements written.')
