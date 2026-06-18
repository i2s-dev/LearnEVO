import re, os, sys
sys.stdout.reconfigure(encoding='utf-8')

dfm_dir = r'C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\samples\dfm'

targets = [
    # ES - Estimating (C: 72->?)
    'T7ESB.DFM','T7ESC.DFM','T7ESD.DFM','T7ESE.DFM','T7EST.DFM',
    # JC - Job Costing (C: 78->?)
    'T7JCA.DFM','T7JCB.DFM','T7JCE.DFM','T7JCENG.DFM','T7JCF.DFM',
    'T7JCH.DFM','T7JCL.DFM','T7JCM.DFM','T7JCN.DFM','T7JCP.DFM',
    'T7JCQ.DFM','T7JCR.DFM','T7JCRM.DFM','T7JCS.DFM',
    # QC - Quality Control (C: 78->?)
    'T7QCA.DFM','T7QCB.DFM','T7QCC.DFM','T7QCD.DFM',
    'T7QCFA.DFM','T7QCMTHD.DFM','T7QCRESULTS.DFM','T7QCRSLT.DFM','T7QCSPEC.DFM',
    # CS - Commissions/Salesperson (C: 80->?)
    'T7CSA.DFM','T7CSB.DFM','T7CSC.DFM','T7CSD.DFM','T7CSE.DFM',
    'T7CSF.DFM','T7CSI.DFM','T7CSO.DFM','T7CSP.DFM',
    # CC - Credit Card Processing (C: 72->?)
    'T7CCCITM.DFM','T7CCCWOT.DFM','T7CCDE.DFM','T7CCP.DFM',
    'T7CCPO.DFM','T7ccr1.DFM',
    # DE - Data Entry / EDI (C: 78->?)
    'T7DEER.DFM','T7DEFECT.DFM','T7DEHD.DFM','T7DEJH.DFM','T7DEK.DFM',
    'T7DEL.DFM','T7DEM.DFM','T7DEP860.DFM','T7DEPB.DFM','T7DEPD.DFM',
    'T7DEPE.DFM','T7DEPF.DFM','T7DEPH.DFM','T7DEQ.DFM','T7DER.DFM',
    'T7DET.DFM','T7DETB.DFM','T7DEU.DFM','T7DEV.DFM','T7DEX.DFM',
    # PS - Program Security (C: 72->?)
    'T7PSA.DFM','T7PSE.DFM','T7PSF.DFM','T7PSK.DFM',
    # FA - Fixed Assets (C: 82->?)
    'T7FAA.DFM','T7FAB.DFM','T7FAE.DFM',
    # IM - Import/Landed Cost (C: 78->?)
    'T7IMB.DFM','T7IMC.DFM','T7IMD.DFM','T7IME.DFM','T7IMF.DFM',
    # LC - Lot Control (C: 80->?)
    'T7LCA.DFM','T7LCB.DFM','T7LCC.DFM','T7LCC2.DFM',
    'T7LCE.DFM','T7LCF.DFM','T7LCG.DFM',
    # AC - Activity Control / NCR (C: 68->?)
    'T7ACDATE.DFM','T7ACRDTYPE.DFM','T7ACTION.DFM',
    # Misc low-confidence single DFMs
    'T7RMAWHY.DFM',
    'T7ISMCC.DFM',
    'T7MAPDEPO.DFM',
    'T7DIGSIG.DFM','T7DigSigChgPSWD.DFM',
    'T7QTINFO.DFM',
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
