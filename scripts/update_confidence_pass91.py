import sys
sys.stdout.reconfigure(encoding='utf-8')

path = r'C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\EVO-DECOMPILE-TODO.md'

with open(path, encoding='utf-8') as f:
    content = f.read()

updates = [
    # J7* customizations: 82->90
    ('| Customizations (J7\\*) | **82** | 80 | **0** ✅ ↑+10 Pass85 40 J7 DFMs IS.RTM confirmed | 2026-06-18 |',
     '| Customizations (J7\\*) | **90** | 80 | **0** ✅ ↑+8 Pass91 41 J7 DFMs: Lapco/PTS/ACH/kanban/sync/web-export all documented | 2026-06-18 |'),
    # IN/Inventory: 93->95
    ('| Module: IN/Inventory | **93** | 85 | **0** ✅ ↑+7 Pass87 IS.PROD.FLAGS[1..19] UDFi30 IS2D.BAR IS.ECO | 2026-06-18 |',
     '| Module: IN/Inventory | **95** | 85 | **0** ✅ ↑+2 Pass91 T6-IN-B 10-tab: IS.ECO/BKSB.MFG/BKSB.VEND/SPECS[12]/RCOST[14] confirmed | 2026-06-18 |'),
    # TA/TAS Admin: 88->91
    ('| Module: TA/TAS Admin | **88** | 80 | **0** ✅ ↑+10 Pass85 WTAS toolkit WTASDMGR | 2026-06-18 |',
     '| Module: TA/TAS Admin | **91** | 80 | **0** ✅ ↑+3 Pass91 WTASDATAM/DMGR/INIT DFMs: FLD/KEY/FILE descriptors confirmed | 2026-06-18 |'),
    # QU/Query Tools: 74->75, close gap
    ('| Module: QU/Query Tools | **74** | 75 | **1** ↑+4 Pass78 | 2026-06-17 |',
     '| Module: QU/Query Tools | **75** | 75 | **0** ✅ ↑+1 Pass91 WBKLOOKUP/DDFilters/SSS/SSSFD DFMs confirmed | 2026-06-18 |'),
    # EvoNotes section: 72->82
    ('- [x] ✅ Files: EvoNotes.RWN, EvoNotesARCH.RWN, EvoNoteSearch.RWN, EvoNotesPrt.RWN, EvoNotesRpt.RWN — **C: 72/100**',
     '- [x] ✅ Files: EvoNotes.RWN, EvoNotesARCH.RWN, EvoNoteSearch.RWN, EvoNotesPrt.RWN, EvoNotesRpt.RWN — **C: 82/100**'),
    # EvoScheduler section: 70->80
    ('- [x] ✅ Files: EvoScheduler.RWN, EvoSched.RWN, EvoSchedSetup.RWN — **C: 70/100**',
     '- [x] ✅ Files: EvoScheduler.RWN, EvoSched.RWN, EvoSchedSetup.RWN — **C: 80/100**'),
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
