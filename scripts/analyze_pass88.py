import re, os, sys
sys.stdout.reconfigure(encoding='utf-8')

dfm_dir = r'C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\samples\dfm'

targets = [
    # Remaining WO
    'T7WOKMA.DFM','T7WOKNA.DFM','T7WOKNB.DFM','T7WOKNC.DFM','T7woko.DFM',
    'T7WOKP.DFM','T7WOKS.DFM','T7WOKSA.DFM','T7WOKT.DFM',
    'T7WOLA.DFM','T7WOLB.DFM','T7WOLC.DFM','T7WOLD.DFM','T7WOLE.DFM',
    'T7WOLF.DFM','T7WOLG.DFM','T7WOLH.DFM','T7WOLI.DFM','T7WOLJ.DFM',
    'T7WOLK.DFM','T7WOLL.DFM','T7WOLM.DFM','T7WOLN.DFM','T7WOLO.DFM',
    'T7WONoteTLL.DFM','T7WOP.DFM','T7WOPO.DFM','T7WOPOR.DFM',
    't7woprio.DFM','t7woprio2.DFM','T7WOS.DFM','T7WOTRWK.DFM',
    # SO
    't7Soa2.DFM','T7SOABKD.DFM','T7SOAC.DFM','T7SOACITEM.DFM','T7SOACPY.DFM',
    'T7SOAE.DFM','T7SOAFRT.DFM','T7SOAIMPLINES.DFM','T7SOAPRC.DFM','T7SOAXCOM.DFM',
    'T7SOB.DFM','T7SOBIN.DFM','T7SOC.DFM','T7SOD.DFM','T7SODDesc.DFM',
    'T7SODPallet.DFM','T7SOE.DFM','T7SOF.DFM','T7SOFDEP.DFM','T7SOG.DFM',
    'T7SOGA.DFM','T7SOGACHK.DFM','T7SOGCG.DFM','T7SOGCM.DFM','T7SOGCogs.DFM',
    'T7SOGComm.DFM','T7SOHINFO.DFM','T7SOINFO.DFM','T7SOJINFO.DFM','T7SOK.DFM',
    'T7SOLINEHIST.DFM','T7SOLINFO.DFM','T7SOLOT.DFM','T7SON.DFM','t7sondte.DFM',
    # PO
    'T7POA.DFM','T7POA2.DFM','T7POAC.DFM','T7POACPY.DFM','T7POAE.DFM',
    'T7POAIMPLINES.DFM','T7POAPrBrk.DFM','T7POAVITEM.DFM','T7POB.DFM',
    't7poc.DFM','T7POEA.DFM','T7POENG.DFM','T7POF.DFM','T7POG.DFM',
    'T7POH.DFM','T7POIC.DFM','T7POID.DFM','T7POIG.DFM','T7POIH.DFM',
    'T7POII.DFM','T7POIL.DFM','T7POJA.DFM','T7POJB.DFM','T7POJC.DFM',
    'T7pojcqc.DFM','T7pojcsc.DFM','T7POJD.DFM','T7POK.DFM','T7POL.DFM','T7POLA.DFM',
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
