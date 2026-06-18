import sys
sys.stdout.reconfigure(encoding='utf-8')

path = r'C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\EVO-DECOMPILE-TODO.md'

with open(path, encoding='utf-8') as f:
    content = f.read()

updates = [
    # Reporting Engine: 75->82 (Pass101: 403 RTMs module-mapped from rtm_callers.csv; complete cross-reference added)
    ('| Reporting Engine | 75 | 88 | 13 | 2026-06-11 |',
     '| Reporting Engine | **82** | 88 | **6** ↑+7 Pass101 403 RTMs module-mapped from rtm_callers.csv; 23 module groups cross-reference | 2026-06-18 |'),
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
