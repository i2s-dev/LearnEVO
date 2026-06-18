import sys
sys.stdout.reconfigure(encoding='utf-8')

path = r'C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\EVO-DECOMPILE-TODO.md'

with open(path, encoding='utf-8') as f:
    content = f.read()

updates = [
    # QT/Service Quote: 74->82, close gap (ISSR.INFO.DATE[5]+AL[20] confirmed in Pass 92/93)
    ('| Module: QT/Service Quote | **74** | 75 | **1** ↑+2 Pass80 DFM | 2026-06-17 |',
     '| Module: QT/Service Quote | **82** | 75 | **0** ✅ ↑+8 Pass93 ISSR.INFO.DATE[5]+AL[20] confirmed | 2026-06-18 |'),
    # US/Triggers: 74->85, close gap (IS.TRIG.* all 23 fields confirmed from T7USG)
    ('| Module: US/Triggers | **74** | 75 | **1** ↑+9 Pass82 DFM confirmed | 2026-06-18 |',
     '| Module: US/Triggers | **85** | 75 | **0** ✅ ↑+11 Pass93 IS.TRIG.* all 23 fields confirmed | 2026-06-18 |'),
    # SL/Shop Loading: 65->85, close gap (T7SHA-SHP 13 DFMs: full dispatch/sched/WC-load suite)
    ('| Module: SL/Shop Loading | **65** | 70 | **5** ↑+7 Pass59 | 2026-06-17 |',
     '| Module: SL/Shop Loading | **85** | 70 | **0** ✅ ↑+20 Pass93 T7SHA-SHP MTWC.*/MTWORO.*/SWO.CRATIO/RUN.DAYS fully confirmed | 2026-06-18 |'),
    # RF/RFQ: 75->84, close gap (BKRFQ.EXP/ISSUE/QTY/COST/PROD/LCDATE confirmed)
    ('| Module: RF/RFQ | **75** | 78 | **3** ↑+13 Pass61 | 2026-06-17 |',
     '| Module: RF/RFQ | **84** | 78 | **0** ✅ ↑+9 Pass93 BKRFQ.EXP/ISSUE/QTY/COST/PROD/LCDATE confirmed | 2026-06-18 |'),
    # TC/Treasury Control: 72->80, close gap (T7TCC terms.num+CHK_NAME confirmed)
    ('| Module: TC/Treasury Control | **72** | 75 | **3** ↑ Pass65 | 2026-06-17 |',
     '| Module: TC/Treasury Control | **80** | 75 | **0** ✅ ↑+8 Pass93 T7TCC terms.num+CHK_NAME[1] confirmed | 2026-06-18 |'),
    # TPOA/PO Processing Hub: 72->84, close gap (T7POA full suite: header+lines+RITEC+CONFIRM[1]/[2])
    ('| Module: TPOA/PO Processing Hub | **72** | 75 | **3** ↑ Pass68 | 2026-06-17 |',
     '| Module: TPOA/PO Processing Hub | **84** | 75 | **0** ✅ ↑+12 Pass93 T7POA/POA2/POAC/POAE/POACPY BKAP.PO full header+RITEC risk.assess[6]+CONFIRM[1]/[2] | 2026-06-18 |'),
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
