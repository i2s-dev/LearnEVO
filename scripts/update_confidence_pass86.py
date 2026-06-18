import sys
sys.stdout.reconfigure(encoding='utf-8')

path = r'C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\EVO-DECOMPILE-TODO.md'

with open(path, encoding='utf-8') as f:
    content = f.read()

updates = [
    # DE/EDI: 78->86
    ('| Module: DE/EDI/Imports | **78** | 80 | **2** ↑ | 2026-06-17 |',
     '| Module: DE/EDI/Imports | **86** | 80 | **0** ✅ ↑+8 Pass86 T7DE* full suite IS.DEF/ISAP.QPO confirmed | 2026-06-18 |'),
    # IM/Multi-Currency: 78->88
    ('| Module: IM/Landed Cost | **78** | 82 | **4** ↑+8 Pass46 | 2026-06-17 |',
     '| Module: IM/Landed Cost | **88** | 82 | **0** ✅ ↑+10 Pass86 ISIS.MCF/MCR multi-currency + landed confirmed | 2026-06-18 |'),
    # RM/RMA: 78->85
    ('| Module: RM/RMA | **78** | 82 | **4** ↑ Pass66 | 2026-06-17 |',
     '| Module: RM/RMA | **85** | 82 | **0** ✅ ↑+7 Pass86 SRMA/IS.RMA RMD disposition confirmed | 2026-06-18 |'),
    # GF/AR Charges: 75->82
    ('| Subsystem: GF/AR Charges | **75** | 80 | **5** ↑+13 Pass57 | 2026-06-17 |',
     '| Subsystem: GF/AR Charges | **82** | 80 | **0** ✅ ↑+7 Pass86 IS.GF.DEPT/DIV GFV confirmed | 2026-06-18 |'),
    # FO/Features Options: 83->87 (main entry)
    ('| Module: FO/Features Options | **83** | 83 | **0** ✅ ↑+2 Pass84 BKBM.PROD.OPYN[4/5]+PRICE | 2026-06-18 |',
     '| Module: FO/Features Options | **87** | 83 | **0** ✅ ↑+4 Pass86 ISFO.HDR.* EvoFNO confirmed | 2026-06-18 |'),
    # FO dup row: 83->87
    ('| Module: FO/Features+Options | **83** | 83 | **0** ✅ (dup row — see primary entry) | 2026-06-18 |',
     '| Module: FO/Features+Options | **87** | 83 | **0** ✅ (dup row — see primary) | 2026-06-18 |'),
    # RE/Reminders: 75->83
    ('| Subsystem: RE/Reminders+Rebuild | **75** | 78 | **3** ↑+13 Pass61 | 2026-06-17 |',
     '| Subsystem: RE/Reminders+Rebuild | **83** | 78 | **0** ✅ ↑+8 Pass86 IS.REM.* Google Calendar export | 2026-06-18 |'),
    # Notes/EVONOTES: 72->82
    ('| System: Notes/EVONOTES | **72** | 78 | **6** ↑+14 Pass56 | 2026-06-17 |',
     '| System: Notes/EVONOTES | **82** | 78 | **0** ✅ ↑+10 Pass86 IS.NOTE/LNK/REM tables confirmed | 2026-06-18 |'),
    # QC: 88->90
    ('| Module: QC/Quality Control | **88** | 88 | **0** ✅ ↑+6 Pass84 IS.NCR/ISQC.MTD/SPC DFMs | 2026-06-18 |',
     '| Module: QC/Quality Control | **90** | 88 | **0** ✅ ↑+2 Pass86 BKQC.TRN.*/RoHS confirmed | 2026-06-18 |'),
    # DC: 87->89
    ('| Module: DC/Data Collection | **87** | 85 | **0** ✅ ↑+2 Pass72 | 2026-06-17 |',
     '| Module: DC/Data Collection | **89** | 85 | **0** ✅ ↑+2 Pass86 EvoDCmenu/ht6 confirmed | 2026-06-18 |'),
    # DE dup row if exists
    ('| Module: DE/DC stubs+EDI processing | **72** | 75 | **3** ↑ Pass68 | 2026-06-17 |',
     '| Module: DE/DC stubs+EDI processing | **86** | 75 | **0** ✅ (dup of DE/EDI -- see primary) | 2026-06-18 |'),
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
