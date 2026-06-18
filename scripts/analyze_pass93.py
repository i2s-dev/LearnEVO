import re, os, sys
sys.stdout.reconfigure(encoding='utf-8')

dfm_dir = r'C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\samples\dfm'

targets = [
    # SH - Shipping module (MH / Shipping Order)
    'T7SHA.DFM','T7SHB.DFM','T7SHC.DFM','T7SHE.DFM','T7SHF.DFM',
    'T7SHG.DFM','T7SHH.DFM','T7SHI.DFM','T7SHJ.DFM','T7SHM.DFM',
    'T7SHN.DFM','T7SHO.DFM','T7SHP.DFM','T7SHIPRTM.DFM',
    # POA - PO Approval module
    'T7POA.DFM','T7POA2.DFM','T7POAC.DFM','T7POACPY.DFM',
    'T7POAE.DFM','T7POAPrBrk.DFM','T7POAVITEM.DFM','T7POAIMPLINES.DFM',
    # RFQ module
    'T7RFQ.DFM',
    # TC - Treasury Control
    'T7TCC.DFM',
    # US - Triggers / Notifications
    'T7USG.DFM',
    # Digital Signature
    'T7DSIG.DFM',
    # EDI Inbound
    'T7EDII.DFM',
    # Audit log setup
    'T7ALOGSETUP.DFM',
    # Auto DC
    'T7AUTODCH.DFM',
    # Customs / Import
    'T7CUSTOMS.DFM','T7CUSTCO.DFM',
    # Misc unanalyzed
    'T7BZFIX.DFM','T7BOMSCRAPFIX.DFM',
    'T7CHARGBK.DFM','T7EMGL.DFM',
    'T7STTYPE.DFM','T7STYPE.DFM',
    'T7NEWINIT.DFM',
    'T7MULTIYIELD.DFM',
    'T7SELLOC.DFM',
    'T7STDCST.DFM',
    'T7VSCHED.DFM',
    'T7BRANDS.DFM',
    'T7ISMCC.DFM',
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

for fname in targets:
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
        print('  FIELDS:', ' | '.join(fields[:50]))
    print()
