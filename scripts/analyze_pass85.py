import re, os, sys
sys.stdout.reconfigure(encoding='utf-8')

dfm_dir = r'C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\samples\dfm'

targets = [
    # SL/MH candidates
    'MACHINEVIEW.DFM','WORKCENTERLOAD.DFM',
    # J7
    'J7ABISHIPRPT.DFM','J7ADTNACHA.DFM','J7APPVEND.DFM','J7AUTOAPC.DFM',
    'J7BEFWEB.DFM','J7BEFWEBINV.DFM','J7CCPIC.DFM','J7CIWEB.DFM',
    'J7CIWEBIMPORT.DFM','J7CJBUSAGE.DFM','J7CRSOW.DFM','J7DCMATLABELS.DFM',
    'J7DCSSOE.DFM','J7DCSSOEVERIFY.DFM','J7EBSERIAL.DFM','J7EIMDCREV.DFM',
    'J7HHEBINC.DFM','J7HHEBXFER.DFM','J7HHEBXFERVERIFY.DFM',
    'J7HHLITN.DFM','J7HHPTSSOE.DFM','J7HHPTSSOELABELS.DFM',
    'J7HHPTSSOEVERIFY.DFM','J7HHRTSSOE.DFM','J7I2SACH.DFM',
    'J7I2SYSTEMSOOE.DFM','J7LAPCOSO.DFM','J7MCDSAREPORT.DFM',
    'J7MPIMPORTAR.DFM','J7NMBINS.DFM','J7NMRTMPRINTER.DFM',
    'J7PEDCB.DFM','J7POAIMP.DFM','J7POAIMPLINES.DFM',
    'J7PTRECPOLINE.DFM','J7PTWOKI.DFM','J7SMJCT.DFM',
    'J7SOAIMPLINES.DFM','J7SYNCWOTOSO.DFM','J7TMCKANBAN.DFM','J7WOLL.DFM',
    # T6
    'T6EVOART.DFM','T6EVOINB.DFM','T6ISINB.DFM','T6ISINB2.DFM',
    'T6ISINBECO.DFM','T6ISINBLNK.DFM','T6ISINBMFG.DFM','T6ISINBMRP.DFM',
    'T6ISINBSPC.DFM','T6ISINBVND.DFM','T6ISSTDCST.DFM','T6MENUUTIL.DFM',
    # JC
    'T7JCA.DFM','T7JCB.DFM','T7JCE.DFM','T7JCENG.DFM','T7JCF.DFM',
    'T7JCH.DFM','T7JCL.DFM','T7JCM.DFM','T7JCN.DFM','T7JCP.DFM',
    'T7JCQ.DFM','T7JCR.DFM','T7JCRM.DFM','T7JCS.DFM',
    # PI
    'T7PIA.DFM','T7PIB.DFM','T7PIC.DFM','T7PICA.DFM','T7PID.DFM',
    'T7PIE.DFM','T7PIF.DFM','T7PIG.DFM','T7PIH.DFM','T7PILOC.DFM',
    # LC
    'T7LCA.DFM','T7LCB.DFM','T7LCC.DFM','T7LCC2.DFM','T7LCE.DFM','T7LCF.DFM','T7LCG.DFM',
    # WTAS
    'WTASINIT.DFM','WTASDATAM.DFM','WTASDMGR.DFM','WTASDMGR2.DFM',
    'WTASDMGR3.DFM','WTASDMS2.DFM','WTASDMS3.DFM','WTASDMS4.DFM','WTASDMS5.DFM',
    'WTASFLLKUP.DFM','WTASFLOC.DFM','WTASFLOCUPD.DFM','WTASMERGE2.DFM',
    'WTASCHKINT.DFM','WTASCHKINTCOMPANY.DFM','WTASCVTDICT.DFM',
    # WBK additional
    'WBKHHLOOKUP.DFM','WBKLKPMEMO.DFM','WBKLPRINT.DFM',
    'WBKMENUSUMVEBTN.DFM','WBKMENUSUEU.DFM','WBKMENUSUNEWAC.DFM',
]

boring = {'OK','Cancel','Close','&OK','&Cancel','&Close','Help','&Help','Yes','No','Save','Exit',
          'Print','Edit','Add','Delete','New','Find','Search','Clear','Select','Update','Apply',
          'Back','Next','Finish','Browse','&Yes','&No','&Save','&Exit','&Print','&Edit','&Add',
          '&Delete','&New','&Find','&Clear','&Select','&Update','&Apply','&Back','&Next',
          'Process','&Process','Go','&Go','Post','&Post','Tag','Untag','Tag All','Untag All'}

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
    caps = [c for c in captions if c not in boring and not re.match(r'^[\d\-\+\*\/\s]+$', c)]
    print(f'=== {fname} ({cls}) ===')
    if caps:
        print('  CAPTIONS:', ' | '.join(caps[:25]))
    if fields:
        print('  FIELDS:', ' | '.join(fields[:25]))
    print()
