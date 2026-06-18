import sys
sys.stdout.reconfigure(encoding='utf-8')

path = r'C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\EVO-DECOMPILE-TODO.md'

with open(path, encoding='utf-8') as f:
    content = f.read()

updates = [
    ('| Java Integration | 73 | 85 | 12 | 2026-06-11 |',
     '| Java Integration | **85** | 88 | **3** ↑+12 Pass102 TASKS/sql/Main+ISJAVA schema; jdbc.ini; 260+ table model inventory; ISLINKS/ROUTING/WORKCTR/ISBSF/BKSYMSTR schemas | 2026-06-18 |'),
    ('| HELP-RESOURCES.md | **87** | 90 | **3** ↑+3 Pass99 EvoLinks/FNO/CAL/T7CUSTOMS/EvoUpdate/EVOBSR/EvoMobile infra documented | 2026-06-18 |',
     '| HELP-RESOURCES.md | **90** | 92 | **2** ↑+3 Pass102 Java Integration doc: EvoPVT.jar arch, ISJAVA schema, jdbc.ini, 260+ table inventory, key schemas | 2026-06-18 |'),
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
