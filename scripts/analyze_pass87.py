import re, os, sys
sys.stdout.reconfigure(encoding='utf-8')

dfm_dir = r'C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\samples\dfm'

targets = [
    # Login / Security
    'dbamenu_LOGIN.Dfm','dbamenu_SELCOMP.Dfm','WBKMENU_LOGIN.DFM',
    'T7DIGSIG.DFM','T7DigSigChgPSWD.DFM',
    # T7HH -- Handheld (all 43)
    'T7HH.DFM','T7HHALERTMSG.DFM','T7HHDCA.DFM','t7hhdcb.DFM','t7hhdcc.DFM',
    'T7HHH.DFM','t7hhinbins.DFM','t7hhINGA.DFM','t7hhinlj.DFM','T7HHINLJLot.DFM',
    'T7HHINLJSer.DFM','T7HHItemLU.DFM','T7HHN.DFM','T7HHN2.DFM','T7HHNDTE.DFM',
    'T7HHNREL.DFM','T7HHO.DFM','T7HHPIC.DFM','t7hhpictags.DFM','t7hhpoc.DFM',
    'T7HHPOCBIN.DFM','T7HHPOCLot.DFM','T7HHPOCNotes.DFM','T7HHPOCSER.DFM',
    'T7HHProcess.DFM','T7HHSOBIN.DFM','T7HHSODD.DFM','T7HHSOLookup.DFM',
    'T7HHSOLOT.DFM','T7HHSOSER.DFM','T7HHSSOE.DFM','t7hhssoeLabels.DFM',
    't7hhssoeLverify.DFM','T7HHSSOESVerify.DFM','T7HHSSOEVerify.DFM','t7hhwog.DFM',
    'T7HHWOIBIN.DFM','T7HHWOIProcess.DFM','T7HHWOLabel.DFM','T7HHWOLookup.DFM',
    'T7HHWOLOT.DFM','t7hhwop.DFM','T7HHWOSCRAP.DFM','t7hhwoser.DFM',
    # T7WO -- Work Orders (first 35)
    'T7WOAC.DFM','T7WOACFG.DFM','T7WOACPY.DFM','T7WOAE.DFM','T7WOAECO.DFM',
    'T7WOAMDT.DFM','T7WOASOLINES.DFM','T7WOB.DFM','T7WOC.DFM','T7WOD.DFM',
    'T7WODATES.DFM','T7WOE.DFM','T7WOF.DFM','T7WOFA.DFM','T7WOG.DFM',
    't7wogimp.DFM','T7WOH.DFM','T7WOI.DFM','T7WOIASK.DFM','T7WOJ.DFM',
    'T7WOJPRESERIALS.DFM','T7WOKA.DFM','T7WOKACOPYROUT.DFM','T7WOKAOPTS.DFM',
    'T7WOKB.DFM','T7WOKC.DFM','T7WOKD.DFM','T7WOKDQTY.DFM','T7WOKE.DFM',
    'T7WOKF.DFM','T7WOKG.DFM','T7WOKJ.DFM','T7WOKK.DFM','T7WOKL.DFM','T7WOKM.DFM',
    # T7IN -- Inventory (first 30)
    'T7INAACDOC.DFM','T7INAALO.DFM','t7inaC.DFM','T7INACMP.DFM','t7inaE.DFM',
    'T7INAFORECAST.DFM','T7INAPRC.DFM','T7INASPC.DFM','T7INAUDF.DFM','T7INAUSG.DFM',
    'T7INAWIP.DFM','T7INB.DFM','T7INB2DB.DFM','t7inbc.DFM','T7INBCMP.DFM',
    't7INBE.DFM','T7INBECO.DFM','T7INBLNK.DFM','T7INBMFG.DFM','T7INBMRP.DFM',
    'T7INBSPC.DFM','T7INBUDF.DFM','T7INBVND.DFM','T7INC.DFM','T7IND.DFM',
    'T7INDPO.DFM','T7INE.DFM','T7INF.DFM','T7ING.DFM','T7INGimport.DFM',
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
        print('  CAPTIONS:', ' | '.join(caps[:35]))
    if fields:
        print('  FIELDS:', ' | '.join(fields[:35]))
    print()
