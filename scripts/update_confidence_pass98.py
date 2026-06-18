import sys
sys.stdout.reconfigure(encoding='utf-8')

path = r'C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\EVO-DECOMPILE-TODO.md'

with open(path, encoding='utf-8') as f:
    content = f.read()

updates = [
    # PROJECT-STRUCTURE: 72->80 (Pass 19 adds 16 new tables, module code corrections,
    # SM-I/J form catalog, SO additional forms, scheduler/backup infrastructure DFMs)
    ('| PROJECT-STRUCTURE.md | **72** | 90 | **18** ↑ | 2026-06-11 |',
     '| PROJECT-STRUCTURE.md | **80** | 90 | **10** ↑+8 Pass98 Pass19: 16 new tables, SH/MH/JS/GF module corrections, SM-I/J forms, SO/sched/backup DFMs | 2026-06-18 |'),
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
