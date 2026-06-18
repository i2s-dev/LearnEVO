import sys
sys.stdout.reconfigure(encoding='utf-8')

path = r'C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\EVO-DECOMPILE-TODO.md'

with open(path, encoding='utf-8') as f:
    content = f.read()

updates = [
    # Per-Table Narrative Docs: 68->76 (tier7-tables.md: 15 new tables documented)
    ('| Per-Table Narrative Docs | **68** | 88 | **20** ↑ +10 | 2026-06-17 |',
     '| Per-Table Narrative Docs | **76** | 88 | **12** ↑+8 Pass96 tier7-tables.md: MTWC/MTWORO/IS.TRIG/BKRFQ/BKICPMAT/BKAP.REM/TMC/MTWO.WIP/IS.SPC/DRILLM/IS.FIB/CFFLOC/BKCM-codes/ISSR.INFO/IS.REM | 2026-06-18 |'),
    # HELP-RESOURCES.md: 75->80 (Passes 93-95 significantly expanded it)
    ('| HELP-RESOURCES.md | **75** | 90 | **15** ↑ +10 | 2026-06-15 |',
     '| HELP-RESOURCES.md | **80** | 90 | **10** ↑+5 Pass93-96 SH/POA/TRIG/GF/JS/UTK/approval/BOL/KIT/SM-I/SM-J all documented | 2026-06-18 |'),
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
