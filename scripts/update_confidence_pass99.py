import sys
sys.stdout.reconfigure(encoding='utf-8')

path = r'C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\EVO-DECOMPILE-TODO.md'

with open(path, encoding='utf-8') as f:
    content = f.read()

updates = [
    # Platform Subsystems main summary row: 72->79
    ('| Platform Subsystems | **72** | 82 | **10** ↑ +7 | 2026-06-17 |',
     '| Platform Subsystems | **79** | 82 | **3** ↑+7 Pass99 EvoLinks/FNO/CAL/Update/EvoBackup/EVOBSR DFMs confirmed | 2026-06-18 |'),
    # Platform Subsystems in-section row: 75->79 (bring in sync)
    ('| Platform Subsystems | **75** | 82 | **7** ↑ +3 | 2026-06-17 |',
     '| Platform Subsystems | **79** | 82 | **3** ↑+4 Pass99 EvoLinks ISLINKS/FNO ISFO.HDR/CAL/Update/EvoBackup/EVOBSR | 2026-06-18 |'),
    # HELP-RESOURCES: 84->87 (Pass99: EvoLinks/FNO/CAL/customs/update/infra)
    ('| HELP-RESOURCES.md | **84** | 90 | **6** ↑+4 Pass97 Recipes10-14 GL/archive/backup/new-user/inv-adj + workflow blocks | 2026-06-18 |',
     '| HELP-RESOURCES.md | **87** | 90 | **3** ↑+3 Pass99 EvoLinks/FNO/CAL/T7CUSTOMS/EvoUpdate/EVOBSR/EvoMobile infra documented | 2026-06-18 |'),
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
