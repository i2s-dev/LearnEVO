import re, os, sys
sys.stdout.reconfigure(encoding='utf-8')

dfm_dir = r'C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\samples\dfm'

targets = [
    # SOA additional forms (SO is at 94% but confirms more SO fields)
    'T7SOA.DFM','t7Soa2.DFM','T7SOABKD.DFM','T7SOAE.DFM','T7SOAFRT.DFM',
    'T7SOAIMPLINES.DFM','T7SOAPRC.DFM','T7SOAXCOM.DFM',
    'T7SOINFO.DFM','T7SOHINFO.DFM','T7SOJINFO.DFM',
    # EVO infrastructure remaining
    'EVOBSR.DFM','EVOCHANGEPASS.DFM','EVODCS.DFM',
    'EVOERPUPDW.DFM','EVOFILTERS.DFM','EVOFUP.DFM',
    'EVOSERVICEREMOVE.DFM','EVOSERVICESETUP.DFM','EVOUPASS.DFM',
    'EvoERPbackup.DFM','EvoERPupd.DFM','EvoForceUpd.DFM',
    'EvoLinkCVT.DFM','EvoLinks.DFM','EvoSchedsetup.DFM',
    'EvoUPDsetup.DFM','EvocfgSave.DFM','Evocnvtb.DFM',
    'Evopass.DFM','Evowkssetup.DFM','evoERPsched.DFM',
    'evogetdate.DFM','evoreminders.DFM','evorereminders.DFM',
    'EvoFNOPO.DFM','EvoFNOQty.DFM','EvoFNOSO.DFM','EvoFNOWO.DFM',
    # CAL module (calendar)
    'CALDRIVE.DFM','CALREM.DFM','CALREMSET.DFM',
    'dayrem.DFM','REMREM.DFM',
    # WBK remaining forms
    'WBKHHLOOKUP.DFM','WBKLKPMEMO.DFM','WBKLPRINT.DFM',
    'WBKLUGRID.DFM','WBKMENUPICS.DFM','WBKMENUBUTT.DFM',
    'WBKMENUSUCPRG.DFM','WBKMENUSUMVEBTN.DFM','WBKMENUSUNEWAC.DFM',
    'WBKMENUSUEU.DFM','WBKMENU_LOGIN.DFM',
    # WTAS remaining
    'WTASCHKINT.DFM','WTASCHKINTCOMPANY.DFM','WTASCVTDICT.DFM',
    'WTASDMS2.DFM','WTASDMS3.DFM','WTASDMS4.DFM','WTASDMS5.DFM',
    'WTASFLLKUP.DFM','WTASFLOC.DFM','WTASFLOCUPD.DFM',
    'WTASINIT.DFM','WTASMERGE2.DFM',
    # Misc forms
    'EMAILREL4.DFM','ENPM.DFM','GetAlphaGen.DFM','GetFileName.DFM',
    'ISCCREP.DFM','NascoPAYex.DFM','PTWOKI.DFM',
    'QUERYEXECUTE.DFM','REPORT.DFM','SSS.DFM','SSSFD.DFM',
    'SQLEXPORT.DFM','GRIDPLAY.DFM','ACT7SHKNOTE.DFM',
    'classic2evonts.DFM','autoT7POJC.DFM',
    'imageinfo.DFM','Imageprint.DFM',
    'nzedefs.DFM','nzemail.DFM','nzemailtll.DFM','printtll.DFM',
    # SM sub-forms (most SM is at 91% but SMIA-SMJH sub-forms may add detail)
    'T7SMIA.DFM','T7SMIB.DFM','T7SMIC.DFM','T7SMID.DFM',
    'T7SMIE.DFM','T7SMIF.DFM',
    'T7SMJA.DFM','T7SMJB.DFM','T7SMJC.DFM','T7SMJD.DFM',
    'T7SMJE.DFM','T7SMJF.DFM','T7SMJG.DFM','T7SMJH.DFM',
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
