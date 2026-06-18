import sys
sys.stdout.reconfigure(encoding='utf-8')

path = r'C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\EVO-DECOMPILE-TODO.md'

with open(path, encoding='utf-8') as f:
    content = f.read()

updates = [
    # Java Integration: 73->85 (Pass102: full JAR class inventory 260+ tables, ISJAVA schema,
    # TASKS/sql architecture, jdbc.ini config, WinRegistry, process monitor, all key table schemas)
    ('| Java Integration | 73 | 88 | 15 | 2026-06-11 |',
     '| Java Integration | **85** | 88 | **3** ↑+12 Pass102 TASKS/sql/Main dispatch+ISJAVA schema; jdbc.ini config; 260+ table model inventory; ISLINKS/ROUTING/WORKCTR/ISBSF/BKSYMSTR/BKSLEVEL full schemas | 2026-06-18 |'),
    # HELP-RESOURCES: 87->90 (Pass102: Java integration full doc appended ~18k chars)
    ('| HELP-RESOURCES.md | **87** | 92 | **5** ↑+3 Pass99 Platform Subsystems: EvoLinks/FNO/CAL/Update/Infra DFM analysis; ISLINKS/ISFO/CAL/infra schemas | 2026-06-18 |',
     '| HELP-RESOURCES.md | **90** | 92 | **2** ↑+3 Pass102 Java Integration: EvoPVT.jar architecture, ISJAVA schema, jdbc.ini, 260+ table inventory, key schemas (ISLINKS/ROUTING/WORKCTR/ISBSF/BKSYMSTR) | 2026-06-18 |'),
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
