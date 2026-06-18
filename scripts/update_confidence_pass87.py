import sys
sys.stdout.reconfigure(encoding='utf-8')

path = r'C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\EVO-DECOMPILE-TODO.md'

with open(path, encoding='utf-8') as f:
    content = f.read()

updates = [
    # WO: 91->94
    ('| Module: WO | **91** | 90 | **0** ✅ ↑+1 Pass74 | 2026-06-17 |',
     '| Module: WO | **94** | 90 | **0** ✅ ↑+3 Pass87 MTWORO/MTWOLA/WOBOM/MTWOR full schema | 2026-06-18 |'),
    # IN: 86->93
    ('| Module: IN/Inventory | **86** | 85 | **0** ✅ ↑+4 Pass85 ECO/SPECS/MFG/VND xref tabs | 2026-06-18 |',
     '| Module: IN/Inventory | **93** | 85 | **0** ✅ ↑+7 Pass87 IS.PROD.FLAGS[1..19] UDFi30 IS2D.BAR IS.ECO | 2026-06-18 |'),
    # HH: 80->93
    ('| Module: HH/Handheld | **80** | 85 | **5** ↑+12 Pass48 | 2026-06-17 |',
     '| Module: HH/Handheld | **93** | 85 | **0** ✅ ↑+13 Pass87 43 DFMs WO/SO/PO/PI/INV full handheld system | 2026-06-18 |'),
    # DI: 78->90
    ('| Module: DI/Digital Signatures | **78** | 80 | **2** ↑+6 Pass72 | 2026-06-17 |',
     '| Module: DI/Digital Signatures | **90** | 80 | **0** ✅ ↑+12 Pass87 T7DIGSIG PO approval 5-level emp.signoff | 2026-06-18 |'),
]

changed = 0
for old, new in updates:
    if old in content:
        content = content.replace(old, new, 1)
        print(f'OK: {old[:70]}...')
        changed += 1
    else:
        print(f'NOT FOUND: {repr(old[:80])}')

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f'\nDone. {changed}/{len(updates)} replacements written.')
