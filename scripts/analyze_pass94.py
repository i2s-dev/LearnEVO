import re, os, sys
sys.stdout.reconfigure(encoding='utf-8')

dfm_dir = r'C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\samples\dfm'

targets = [
    # GF module - completely unknown
    'T7GFCB.DFM','T7GFPRICE.DFM','T7GFR.DFM','T7GFTEST.DFM',
    'T7GFV.DFM','T7GFVS.DFM','t7GFdept.DFM','t7GFdiv.DFM',
    # JS module - completely unknown
    'T7JSACC.DFM','T7JSAIC.DFM','T7JSAPBI.DFM','T7JSASRS.DFM',
    'T7JSOI.DFM','T7JSQL.DFM','T7JSettings.DFM',
    # UTK module - completely unknown
    'T7UTKA.DFM','T7UTKD.DFM','T7UTKE.DFM','T7UTKF.DFM','T7UTKG.DFM','T7UTKH.DFM',
    # SP/SPC module - Statistical Process Control
    'T7SPC.DFM','T7SPCLIVEGRID.DFM','T7SPCLIVEREP.DFM',
    'T7SPCREP.DFM','T7SPCREP2.DFM','T7SPCREPPPM.DFM',
    # Approval suite - cross-module approval routing
    'T7SOAC.DFM','T7SOACITEM.DFM','T7SOACPY.DFM',
    'T7APACH.DFM','T7APACON.DFM','t7apaC.DFM',
    'T7ARAC.DFM','T7ARACON.DFM','T7ARACRE.DFM',
    'T7WOAC.DFM','T7WOACFG.DFM','T7WOACPY.DFM',
    # SOGC - SO gross/commission analysis
    'T7SOGCG.DFM','T7SOGCM.DFM','T7SOGCogs.DFM','T7SOGComm.DFM',
    # F&O additional forms
    'T7FOC.DFM','T7FOD.DFM','T7FOE.DFM',
    # FS module - field service?
    'T7FSCLASS.DFM','T7FSEMP.DFM','T7FSINFO.DFM',
    # Kit and BOL
    'T7KIT.DFM','T7BOL.DFM','T7BOLMSO.DFM',
    # Misc single forms
    'T7FNR.DFM','T7ALTPART.DFM','T7QGRID.DFM',
    'T7SDET.DFM','T7STOCK.DFM','T7MLC.DFM','T7MLE.DFM',
    'T7ALERTMSG.DFM','T7RTMVALID.DFM','T7XCUTIL.DFM',
    'T7PUTAWAY.DFM','T7LIMACC.DFM','T7WCBK.DFM',
    # EVO infrastructure extras
    'EvoDCmenu.DFM','EvoDCmenu2.DFM','EvoDCsetup.DFM',
    'EvoELinks.DFM','EvoEMsg.DFM','EvoERPDrillM.DFM',
    'EvoNotesARCH.DFM','EvoNotesPrt.DFM','EvoNoteSearch.DFM',
    'EvoMobilesetup.DFM','evoCSR.DFM','evoalerts.DFM',
    # Misc standalone DFMs
    'CRMDASHBOARD.DFM','CASHFLOW.DFM','COMMISSIONRPT.DFM',
    'MACHINEVIEW.DFM','WORKCENTERLOAD.DFM',
    'BOMTREE.DFM','EDITBOMTREE.DFM',
    'PURCHITEM.DFM','PURCHVEND.DFM',
    'ROP.DFM','INVCHANGE.DFM','NUMEMP.DFM',
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
