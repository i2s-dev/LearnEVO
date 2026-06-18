import sys
sys.stdout.reconfigure(encoding='utf-8')

path = r'C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\EVO-DECOMPILE-TODO.md'

with open(path, encoding='utf-8') as f:
    content = f.read()

updates = [
    # SO: 94->96 (Pass95 FRGHT/SUBTOT/TOTAL/sobookdate/ASD/rts/recurring-SO/SOAXCOM/ISSR.INFO dual-use confirmed)
    ('| Module: SO | **94** | 85 | **0** ✅ ↑+4 Pass89 serial-alloc contract-review quote-conv SO-V SO-O full | 2026-06-18 |',
     '| Module: SO | **96** | 85 | **0** ✅ ↑+2 Pass95 FRGHT/SUBTOT/TOTAL/sobookdate/ASD/rts/recurring-SO/SOAXCOM/ISSR.INFO header+line confirmed | 2026-06-18 |'),
    # SM: 91->94 (Pass95 SM-I BKCM.LEAD/TERR/ACFC/DTCD/CATM + SM-J 8 archive/purge programs all confirmed)
    ('| Module: SM/System Maintenance+Item Inquiry | **91** | 86 | **0** ✅ ↑+5 Pass90 ISIS.TXF-full BKCM-codes ISTS.CFG BKYS.YN SM-J | 2026-06-18 |',
     '| Module: SM/System Maintenance+Item Inquiry | **94** | 86 | **0** ✅ ↑+3 Pass95 SM-I BKCM.LEAD/TERR/ACFC/DTCD/CATM + SM-J SMJA-SMJH 8 archive-purge programs | 2026-06-18 |'),
    # CM/CRM: 86->90 (Pass95 5 BKCM code tables fully confirmed: LEAD/TERR/ACFC/DTCD/CATM)
    ('| Module: CM/CRM | **86** | 85 | **0** ✅ ↑+4 Pass85 BKCM.ACCT credit card confirmed | 2026-06-18 |',
     '| Module: CM/CRM | **90** | 85 | **0** ✅ ↑+4 Pass95 BKCM.LEAD/TERR/ACFC/DTCD/CATM 5 code tables fully confirmed | 2026-06-18 |'),
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
