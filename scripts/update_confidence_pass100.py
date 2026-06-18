import sys
sys.stdout.reconfigure(encoding='utf-8')

path = r'C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\EVO-DECOMPILE-TODO.md'

with open(path, encoding='utf-8') as f:
    content = f.read()

updates = [
    # Per-Table Narrative Docs: 76->83 (tier8: 18 DDF-exact schemas — BKAPPO/BKAPPOL/BKGLTRAN/BKGLCOA/BKDCSHFT/WORKORD/BKICMSTR/etc)
    ('| Per-Table Narrative Docs | **76** | 88 | **12** ↑+8 Pass96 tier7-tables.md: MTWC/MTWORO/IS.TRIG/BKRFQ/BKICPMAT/BKAP.REM/TMC/MTWO.WIP/IS.SPC/DRILLM/IS.FIB/CFFLOC/BKCM-codes/ISSR.INFO/IS.REM | 2026-06-18 |',
     '| Per-Table Narrative Docs | **83** | 88 | **5** ↑+7 Pass100 tier8-tables.md: 18 DDF-exact schemas (BKAPPO/BKAPPOL/BKGLTRAN/BKGLCOA/BKDCSHFT/WORKORD/BKICMSTR/BKARCUST/BKARINV/BKAPPOL/BKBMMSTR/etc 1240 fields) | 2026-06-18 |'),
]

changed = 0
for old, new in updates:
    if old in content:
        content = content.replace(old, new, 1)
        print(f'OK: {old[:80]}...')
        changed += 1
    else:
        print(f'NOT FOUND: {repr(old[:90])}')

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f'\nDone. {changed}/{len(updates)} replacements written.')
