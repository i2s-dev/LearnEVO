import re, os, sys
sys.stdout.reconfigure(encoding='utf-8')

dfm_dir = r'C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\samples\dfm'

targets = [
    # EvoLinks
    'EvoLinks.DFM',
    # EvoFNO suite
    'EvoFNO.DFM', 'EvoFNOSO.DFM', 'EvoFNOPO.DFM', 'EvoFNOWO.DFM', 'EvoFNOQty.DFM',
    # Calendar
    'CALREMGC.DFM', 'CALREM.DFM', 'CALREMSET.DFM',
    # EvoScheduler / service setup (check for any we missed)
    'EvoSchedsetup.DFM', 'EVOSERVICEREMOVE.DFM', 'EVOSERVICESETUP.DFM',
    # EvoUpdate
    'EvoERPupd.DFM', 'EvoForceUpd.DFM', 'EvoUPDsetup.DFM',
    # Drill-down / analysis
    'EvoERPDrillM.DFM', 'CRMDASHBOARD.DFM', 'CASHFLOW.DFM', 'BOMTREE.DFM',
    # Customs / compliance
    'T7CUSTOMS.DFM', 'BKCPEC.DFM',
    # DC handheld / setup
    'EvoDCmenu.DFM', 'EvoDCsetup.DFM', 'EVODCS.DFM',
    # More infrastructure
    'EVOBSR.DFM', 'EVOFUP.DFM', 'EVOUPASS.DFM', 'Evopass.DFM',
    'EvocfgSave.DFM', 'Evowkssetup.DFM', 'Evocnvtb.DFM',
    # EvoLinks update forms
    'EvoLinkCVT.DFM',
    # MH shipping
    'T7BOL.DFM', 'T7BOLMSO.DFM', 'T7MHA.DFM', 'T7MHABOX.DFM',
    # Extra FNO / features
    'EvoFNOPO.DFM',
    # Reminder forms we haven't seen yet
    'REMREM.DFM', 'evorereminders.DFM',
    # Mobile setup
    'EvoMobilesetup.DFM',
    # EvoCSR
    'evoCSR.DFM',
]

boring = {'OK','Cancel','Close','&OK','&Cancel','&Close','Help','&Help','Yes','No','Save','Exit',
          'Print','Edit','Add','Delete','New','Find','Search','Clear','Select','Update','Apply',
          'Back','Next','Finish','Browse','&Yes','&No','&Save','&Exit','&Print','&Edit','&Add',
          '&Delete','&New','&Find','&Clear','&Select','&Update','&Apply','&Back','&Next',
          'Process','&Process','Go','&Go','Post','&Post','Tag','Untag','Tag All','Untag All',
          'True','False','None','','None','Submit','&Submit','Refresh','&Refresh','View','&View',
          'Import','&Import','Export','&Export','Copy','&Copy','Paste','&Paste','Move','&Move',
          'List','Grid','Detail','Summary','Report','Run','&Run','Filter','&Filter','Reset',
          'Scan','&Scan','Receive','&Receive','Ship','&Ship','Post','Lookup','Zoom'}

seen = set()
for fname in targets:
    if fname in seen:
        continue
    seen.add(fname)
    path = os.path.join(dfm_dir, fname)
    if not os.path.exists(path):
        for actual in os.listdir(dfm_dir):
            if actual.upper() == fname.upper():
                path = os.path.join(dfm_dir, actual)
                break
        else:
            print(f'MISSING: {fname}')
            continue
    with open(path, encoding='utf-8', errors='replace') as f:
        txt = f.read()
    captions = re.findall(r"Caption = '([^']{2,80})'", txt)
    fields = re.findall(r"FieldName = '([^']+)'", txt)
    form_cls = re.search(r'^object\s+\w+:\s*(\w+)', txt, re.M)
    cls = form_cls.group(1) if form_cls else 'unknown'
    caps = [c for c in captions if c not in boring and not re.match(r'^[\d\-\+\*\/\s\.]+$', c)]
    print(f'=== {fname} ({cls}) ===')
    if caps:
        print('  CAPTIONS:', ' | '.join(caps[:40]))
    if fields:
        print('  FIELDS:', ' | '.join(fields[:60]))
    print()
