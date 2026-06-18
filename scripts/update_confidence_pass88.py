import sys
sys.stdout.reconfigure(encoding='utf-8')

path = r'C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\EVO-DECOMPILE-TODO.md'

with open(path, encoding='utf-8') as f:
    content = f.read()

updates = [
    # WO: 94->97
    ('| Module: WO | **94** | 90 | **0** ✅ ↑+3 Pass87 MTWORO/MTWOLA/WOBOM/MTWOR full schema | 2026-06-18 |',
     '| Module: WO | **97** | 90 | **0** ✅ ↑+3 Pass88 IS.PREQ/IS.SER/IS.TRAY/IS.WOPRIO ISSO.BOX WO-L suite | 2026-06-18 |'),
    # SO: 82->90
    ('| Module: SO | **82** | 85 | **3** ↑+7 Pass76 | 2026-06-17 |',
     '| Module: SO | **90** | 85 | **0** ✅ ↑+8 Pass88 BKAR.INV/INVL ISAR.CHG/TXN/INFO BKIC.PMAT full | 2026-06-18 |'),
    # PO: 80->90
    ('| Module: PO | **80** | 85 | **5** ↑+8 Pass52 | 2026-06-17 |',
     '| Module: PO | **90** | 85 | **0** ✅ ↑+10 Pass88 BKAP.PO/POL BKRFQ RFQ->PO flow DPAS buyoff | 2026-06-18 |'),
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
