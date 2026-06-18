import sys
sys.stdout.reconfigure(encoding='utf-8')

path = r'C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\EVO-DECOMPILE-TODO.md'

with open(path, encoding='utf-8') as f:
    content = f.read()

# Exact line replacements (no regex)
updates = [
    # Main table — IN/Inventory (line 997)
    ('| Module: IN/Inventory | **82** | 85 | **3** ↑+5 Pass75 | 2026-06-17 |',
     '| Module: IN/Inventory | **86** | 85 | **0** ✅ ↑+4 Pass85 ECO/SPECS/MFG/VND xref tabs | 2026-06-18 |'),
    # Main table — BM/MRP (line 1002)
    ('| Module: BM/MRP | **88** | 88 | **0** ✅ ↑+3 Pass83 18 DFMs BKMRP confirmed | 2026-06-18 |',
     '| Module: BM/MRP | **90** | 88 | **0** ✅ ↑+2 Pass85 MTIC.PROD MRP fields confirmed | 2026-06-18 |'),
    # Main table — CM/CRM (line 1007)
    ('| Module: CM/CRM | **82** | 85 | **3** ↑+10 Pass53 | 2026-06-17 |',
     '| Module: CM/CRM | **86** | 85 | **0** ✅ ↑+4 Pass85 BKCM.ACCT credit card confirmed | 2026-06-18 |'),
    # Main table — JC/Job Costing (line 1011)
    ('| Module: JC/Job Costing | **78** | 82 | **4** ↑+6 Pass47 | 2026-06-17 |',
     '| Module: JC/Job Costing | **87** | 82 | **0** ✅ ↑+9 Pass85 JCA-JCS+JCENG full menu | 2026-06-18 |'),
    # Main table — LC/Lot Control (line 1018)
    ('| Module: LC/Lot Control | **81** | 78 | **0** ✅ ↑+1 Pass77 | 2026-06-17 |',
     '| Module: LC/Lot Control | **88** | 78 | **0** ✅ ↑+7 Pass85 MTLOT.* LC-A/G DFMs | 2026-06-18 |'),
    # Main table — PI/Physical Inventory (line 1021)
    ('| Module: PI/Physical Inventory | **76** | 80 | **4** ↑+4 Pass74 | 2026-06-17 |',
     '| Module: PI/Physical Inventory | **88** | 80 | **0** ✅ ↑+12 Pass85 BKPH.* PI-A/H confirmed | 2026-06-18 |'),
    # Main table — TA/TAS Admin (line 1037)
    ('| Module: TA/TAS Admin | **78** | 80 | **2** ↑ Pass66 | 2026-06-17 |',
     '| Module: TA/TAS Admin | **88** | 80 | **0** ✅ ↑+10 Pass85 WTAS toolkit WTASDMGR | 2026-06-18 |'),
    # Dup row — PI (line 1074)
    ('| Subsystem: PI/Physical Inventory | **76** | 80 | **4** ↑+4 Pass74 | 2026-06-17 |',
     '| Subsystem: PI/Physical Inventory | **88** | 80 | **0** ✅ (dup — see primary) | 2026-06-18 |'),
    # Dup row — JC (line 1076)
    ('| Module: JC/Job Cost | **78** | 82 | **0** (dup of above — see line 1009) | 2026-06-17 |',
     '| Module: JC/Job Cost | **87** | 82 | **0** ✅ (dup — see primary) | 2026-06-18 |'),
    # WBKLOOKUP (line 1078)
    ('| Platform: WBKLOOKUP/Lookup Framework | **68** | 70 | **2** ↑+13 Pass62 | 2026-06-17 |',
     '| Platform: WBKLOOKUP/Lookup Framework | **76** | 70 | **0** ✅ ↑+8 Pass85 WBKLPRINT/HHLOOKUP | 2026-06-18 |'),
    # J7 Customizations (line 1107)
    ('| Customizations (J7\\*) | **72** | 80 | **8** ↑ +7 | 2026-06-17 |',
     '| Customizations (J7\\*) | **82** | 80 | **0** ✅ ↑+10 Pass85 40 J7 DFMs IS.RTM confirmed | 2026-06-18 |'),
]

changed = 0
for old, new in updates:
    if old in content:
        content = content.replace(old, new, 1)
        print(f'OK: {old[:60]}...')
        changed += 1
    else:
        print(f'NOT FOUND: {repr(old[:80])}')

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f'\nDone. {changed}/{len(updates)} replacements written.')
