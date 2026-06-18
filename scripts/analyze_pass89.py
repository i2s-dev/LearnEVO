import re, os, sys
sys.stdout.reconfigure(encoding='utf-8')

dfm_dir = r'C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\samples\dfm'

targets = [
    # SO remaining
    'T7SONQTY.DFM','T7SOOA.DFM','T7SOOB.DFM','T7SOOD.DFM','T7SOOE.DFM',
    'T7SOOF.DFM','T7SOOG.DFM','T7SOOH.DFM','T7SOOI.DFM','T7SOOM.DFM',
    'T7SOON.DFM','T7SOPB.DFM','T7SOPC.DFM','T7SOPF.DFM','T7SOPI.DFM',
    'T7SOPJ.DFM','T7SOPK.DFM','T7SOPM.DFM','T7SOPO.DFM','T7SOPOR.DFM',
    'T7SOPP.DFM','T7SOQA.DFM','T7SOQB.DFM','T7SOQC.DFM','T7SOQH.DFM',
    'T7SOQI.DFM','T7SOQJ.DFM','T7SOQK.DFM','T7SOQL.DFM','T7SOR.DFM',
    'T7SORevu.DFM','T7SORevuPSWD.dfm','T7SOS.DFM','T7SOSER.DFM','T7SOV.DFM',
    # PO remaining
    'T7POLINEHIST.DFM','T7POLP.DFM','T7POM.DFM','T7POMAST.DFM','T7POP.DFM',
    'T7POPGET.DFM','t7POQ.DFM','T7POS.DFM','T7POSCD.DFM','T7POSI.DFM','T7POSX.DFM',
    # AP
    'T7APA.DFM','T7APABANK.DFM','t7apaC.DFM','T7APACH.DFM','T7APACON.DFM',
    't7apae.DFM','T7APAPRC.DFM','T7APASTA.DFM','T7APB.DFM','T7APC.DFM',
    'T7APD.DFM','T7APE.DFM','t7apf.dfm','t7apg.dfm','T7APH.DFM',
    'T7APHASK.DFM','T7API.DFM','T7APINFO.DFM','T7APJ.DFM','T7APK.DFM',
    't7apl.DFM','T7APM.DFM','T7APO.DFM','T7APP.DFM','T7APPVND.DFM',
    'T7APQ.DFM','T7APR.DFM','T7APS.DFM','T7APT.DFM','T7APV.DFM',
    'T7APX.DFM','T7APY.DFM','T7APYB.DFM','T7APYC.DFM','T7APZA.DFM',
    # AR
    'T7ARA2DB.DFM','T7ARAC.DFM','T7ARACON.DFM','T7ARACRE.DFM','T7ARAE.DFM',
    'T7ARAPRC.DFM','T7ARASTA.DFM','T7ARB.DFM','T7ARC.DFM','T7ARD.DFM',
    'T7ARE.DFM','T7ARF.DFM','T7ARG.DFM','T7ARH.DFM','T7ARI.DFM',
    'T7ARK.DFM','T7ARL.DFM','T7ARM.DFM','T7ARN.DFM','T7ARP.DFM',
    'T7ARR.DFM','T7ART.DFM','T7ARU.DFM',
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
