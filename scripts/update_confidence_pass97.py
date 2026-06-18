import sys
sys.stdout.reconfigure(encoding='utf-8')

path = r'C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\EVO-DECOMPILE-TODO.md'

with open(path, encoding='utf-8') as f:
    content = f.read()

updates = [
    # Business Workflows: 75->82 (+5 recipes: GL journal, period-end archive, backup/restore, new user, inv adjustment)
    ('| Business Workflows | **75** | 85 | **10** ↑+13 Pass58 | 2026-06-17 |',
     '| Business Workflows | **82** | 85 | **3** ↑+7 Pass97 Recipes10-14: GL-journal/period-end-archive/backup/new-user/inv-adjustment | 2026-06-18 |'),
    # HELP-RESOURCES: 80->84 (recipes 10-14 + Pass 97 workflow block)
    ('| HELP-RESOURCES.md | **80** | 90 | **10** ↑+5 Pass93-96 SH/POA/TRIG/GF/JS/UTK/approval/BOL/KIT/SM-I/SM-J all documented | 2026-06-18 |',
     '| HELP-RESOURCES.md | **84** | 90 | **6** ↑+4 Pass97 Recipes10-14 GL/archive/backup/new-user/inv-adj + workflow blocks | 2026-06-18 |'),
    # Also update the inline note in §13
    ('Pass 58 (2026-06-17): 8 workflow recipes fully written in HELP-RESOURCES.md — **C: 75/100**',
     'Pass 58 + Pass 97 (2026-06-18): 14 workflow recipes written — **C: 82/100**'),
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
