import sys
sys.stdout.reconfigure(encoding='utf-8')

path = r'C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\EVO-DECOMPILE-TODO.md'

with open(path, encoding='utf-8') as f:
    content = f.read()

updates = [
    # SO: 90->94
    ('| Module: SO | **90** | 85 | **0** ✅ ↑+8 Pass88 BKAR.INV/INVL ISAR.CHG/TXN/INFO BKIC.PMAT full | 2026-06-18 |',
     '| Module: SO | **94** | 85 | **0** ✅ ↑+4 Pass89 serial-alloc contract-review quote-conv SO-V SO-O full | 2026-06-18 |'),
    # PO: 90->93
    ('| Module: PO | **90** | 85 | **0** ✅ ↑+10 Pass88 BKAP.PO/POL BKRFQ RFQ->PO flow DPAS buyoff | 2026-06-18 |',
     '| Module: PO | **93** | 85 | **0** ✅ ↑+3 Pass89 ISAP.CHG POS-module vendor-master T7POQ delivery | 2026-06-18 |'),
    # AP: 93->96
    ('| Module: AP | **93** | 92 | **0** ✅ ↑+1 Pass76 | 2026-06-17 |',
     '| Module: AP | **96** | 92 | **0** ✅ ↑+3 Pass89 ISAPEX BKAP2-UDF BKAP.CHK BKQC recurring ACH/1099 | 2026-06-18 |'),
    # AR: 88->93
    ('| Module: AR | **88** | 92 | **4** ↑+3 Pass74 | 2026-06-17 |',
     '| Module: AR | **93** | 92 | **0** ✅ ↑+5 Pass89 BKAR full ISAREX BKAR.INVV IS.CC tax-transfer stats | 2026-06-18 |'),
]

changed = 0
for old, new in updates:
    if old in content:
        content = content.replace(old, new, 1)
        print(f'OK: {old[:70]}...')
        changed += 1
    else:
        print(f'NOT FOUND: {repr(old[:90])}')

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f'\nDone. {changed}/{len(updates)} replacements written.')
