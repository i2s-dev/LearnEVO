import sys
sys.stdout.reconfigure(encoding='utf-8')

path = r'C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\EVO-DECOMPILE-TODO.md'

with open(path, encoding='utf-8') as f:
    content = f.read()

updates = [
    # MH/Shipping Order: 68->80, close gap 4->0 (T7BOL+BOLMSO fully confirmed)
    ('| Module: MH/Shipping Order | **68** | 72 | **4** ↑+13 Pass46 | 2026-06-17 |',
     '| Module: MH/Shipping Order | **80** | 72 | **0** ✅ ↑+12 Pass94 T7BOL+BOLMSO full BOL structure confirmed | 2026-06-18 |'),
    # UT/Utilities: 78->84 (UTKA-UTKH: data-deletion/GL-transfer/location-rename/item-print all confirmed)
    ('| Module: UT/Utilities | **78** | 75 | **0** ✅ ↑+6 Pass79 DFM-confirmed | 2026-06-17 |',
     '| Module: UT/Utilities | **84** | 75 | **0** ✅ ↑+6 Pass94 UTKA-UTKH data-deletion/GL-transfer/location-rename/item-type-reports | 2026-06-18 |'),
    # KI/Kit Assembly: 72->83 (T7KIT BOM component arrays + lot + scan + bin confirmed)
    ('| Module: KI/Kit Assembly | **72** | 72 | **0** ✅ | 2026-06-17 |',
     '| Module: KI/Kit Assembly | **83** | 72 | **0** ✅ ↑+11 Pass94 T7KIT BOM-component/lot/scan/bin arrays confirmed | 2026-06-18 |'),
    # Database Schema: 83->86 (many new fields: BKIC.PMAT, IS.SPC/SERR/STRACK, BKAP.REM/TMC, ISAREX.EXTADD, MTWO.WIP.E*/A*)
    ('| Database Schema (field meaning) | **83** | 88 | **5** ↑+5 Pass77 100%coverage | 2026-06-17 |',
     '| Database Schema (field meaning) | **86** | 88 | **2** ↑+3 Pass94 BKIC.PMAT/IS.SPC.ESTE[3]/BKAP.REM.*/TMC.*/ISAREX.EXTADD[8]/MTWO.WIP.E*+A* confirmed | 2026-06-18 |'),
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
