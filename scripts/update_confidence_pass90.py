import sys
sys.stdout.reconfigure(encoding='utf-8')

path = r'C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\EVO-DECOMPILE-TODO.md'

with open(path, encoding='utf-8') as f:
    content = f.read()

updates = [
    # WC: 80->86
    ('| Module: WC/Warehouse Control ⚠️ | **80** | 80 | **0** ✅ ↑+5 Pass81 DFMs | 2026-06-17 |',
     '| Module: WC/Warehouse Control ⚠️ | **86** | 80 | **0** ✅ ↑+6 Pass90 WCE/F/G/H/BK/LOCfix bin-assign cycle | 2026-06-18 |'),
    # SR: 82->88
    ('| Module: SR/Service Repair | **82** | 82 | **0** ✅ ↑+10 Pass84 SRE/F/G/I/SRINFO DFMs ISSR.INFO | 2026-06-18 |',
     '| Module: SR/Service Repair | **88** | 82 | **0** ✅ ↑+6 Pass90 SRB/D/E/F/G/I/S full invoice+release | 2026-06-18 |'),
    # AM: 83->93
    ('| Module: AM (Accounting Maint.) | **83** | 85 | **2** ↑+8 Pass80 all DFMs | 2026-06-17 |',
     '| Module: AM (Accounting Maint.) | **93** | 85 | **0** ✅ ↑+10 Pass90 14-period GL BKGL.STC/STI fin-stmt archive | 2026-06-18 |'),
    # MRP: 80->90
    ('| Module: MR/MRP Engine | **80** | 85 | **5** ↑+18 Pass45 | 2026-06-17 |',
     '| Module: MR/MRP Engine | **90** | 85 | **0** ✅ ↑+10 Pass90 BKMRP.FC/PO MTMRP 4-stage-run MBEDORC WO/PO gen | 2026-06-18 |'),
    # SM: 86->91
    ('| Module: SM/System Maintenance+Item Inquiry | **86** | 86 | **0** ✅ ↑+4 Pass84 IS.TERMS/ISIS.TXF/BKCM.* DFMs | 2026-06-18 |',
     '| Module: SM/System Maintenance+Item Inquiry | **91** | 86 | **0** ✅ ↑+5 Pass90 ISIS.TXF-full BKCM-codes ISTS.CFG BKYS.YN SM-J | 2026-06-18 |'),
    # GL: 93->95
    ('| Module: GL | **93** | 92 | **0** ↑+3 Pass70 | 2026-06-17 |',
     '| Module: GL | **95** | 92 | **0** ✅ ↑+2 Pass90 14-period confirmed BKGL.STC/STI fin-stmt config | 2026-06-18 |'),
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
