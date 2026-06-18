import sys
sys.stdout.reconfigure(encoding='utf-8')

path = r'C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\EVO-DECOMPILE-TODO.md'

with open(path, encoding='utf-8') as f:
    content = f.read()

updates = [
    # MA/AR Deposits: 76->82 (ISAR.DEPL SO/AMT/GLACT confirmed)
    ('| Module: MA/AR Deposits | **76** | 75 | **0** ✅ ↑+6 Pass82 DFM+ISARDEPL confirmed | 2026-06-18 |',
     '| Module: MA/AR Deposits | **82** | 75 | **0** ✅ ↑+6 Pass92 ISAR.DEPL.SO/AMT/GLACT BKAR.DEP.DEPNO/CUST confirmed | 2026-06-18 |'),
    # CC/Credit Card: 84->87, close gap (IS.CC.* all 8 fields + CCYY/CCMM/CVV confirmed)
    ('| Module: CC/Credit Card ⚠️ | **84** | 85 | **1** ↑+6 Pass82 6 DFMs | 2026-06-18 |',
     '| Module: CC/Credit Card ⚠️ | **87** | 85 | **0** ✅ ↑+3 Pass92 IS.CC.* all 8 fields + CCYY/CCMM/CVV confirmed | 2026-06-18 |'),
    # AC/Activity Control: 78->83 (all 3 tables fully confirmed from DFMs)
    ('| Module: AC/Activity Control | **78** | 78 | **0** ✅ ↑+4 Pass83 8D CAR+ISCACT+ISCTEAM | 2026-06-18 |',
     '| Module: AC/Activity Control | **83** | 78 | **0** ✅ ↑+5 Pass92 WODATE/AC.RD/IS.ACTION all fields confirmed | 2026-06-18 |'),
    # MA duplicate row: close gap (70->76, note merged)
    ('| Module: MA/AR Deposit Apply | **70** | 75 | **5** ↑ Pass50 (merged with MA/AR Deposits) | 2026-06-17 |',
     '| Module: MA/AR Deposit Apply | **82** | 75 | **0** ✅ (merged with MA/AR Deposits — see primary) | 2026-06-18 |'),
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
