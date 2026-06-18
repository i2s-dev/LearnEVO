import re, os, sys
sys.stdout.reconfigure(encoding='utf-8')

dfm_dir = r'C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\samples\dfm'

targets = [
    # J7 - i2 Systems customer customizations
    'J7ABISHIPRPT.DFM','J7ADTNACHA.DFM','J7APPVEND.DFM','J7AUTOAPC.DFM',
    'J7BEFWEB.DFM','J7BEFWEBINV.DFM','J7CCPIC.DFM','J7CIWEB.DFM',
    'J7CIWEBIMPORT.DFM','J7CJBUSAGE.DFM','J7CRSOW.DFM',
    'J7DCMATLABELS.DFM','J7DCSSOE.DFM','J7DCSSOEVERIFY.DFM',
    'J7EBSERIAL.DFM','J7EIMDCREV.DFM',
    'J7HHEBINC.DFM','J7HHEBXFER.DFM','J7HHEBXFERVERIFY.DFM',
    'J7HHLITN.DFM','J7HHPTSSOE.DFM','J7HHPTSSOELABELS.DFM',
    'J7HHPTSSOEVERIFY.DFM','J7HHRTSSOE.DFM',
    'J7I2SACH.DFM','J7I2SYSTEMSOOE.DFM',
    'J7LAPCOSO.DFM','J7MCDSAREPORT.DFM','J7MPIMPORTAR.DFM',
    'J7NMBINS.DFM','J7NMRTMPRINTER.DFM',
    'J7PEDCB.DFM','J7POAIMP.DFM','J7POAIMPLINES.DFM',
    'J7PTRECPOLINE.DFM','J7PTWOKI.DFM',
    'J7SMJCT.DFM','J7SOAIMPLINES.DFM',
    'J7SYNCWOTOSO.DFM','J7TMCKANBAN.DFM','J7WOLL.DFM',
    # EVO* infrastructure
    'CRMDASHBOARD.DFM','EvoCSI.DFM','EVOENOTES.DFM',
    'EvoELinks.DFM','EvoEMsg.DFM','EVOFUP.DFM',
    'EvoFNO.DFM','EvoFNOPO.DFM','EvoFNOQty.DFM','EvoFNOSO.DFM','EvoFNOWO.DFM',
    'EvoNoteSearch.DFM','EvoNotes.DFM','EvoNotesARCH.DFM','EvoNotesPrt.DFM',
    'EvoNoteSearch.DFM','EvoNotesRpt.DFM',
    'EvoBS.DFM','EvoBSCash.DFM','EvoBSWO.DFM','EVOBSR.DFM',
    'EvoScheduler.DFM','EvoSchedsetup.DFM','evoERPsched.DFM',
    'evoCSR.DFM','evoalerts.DFM','evoreminders.DFM','EVOMESSAGE.DFM',
    'EvoDCmenu.DFM','EvoDCmenu2.DFM','EvoDCsetup.DFM',
    'EVOCHANGEPASS.DFM','EVOERROR.DFM','EVOFILTERS.DFM',
    'EVODCS.DFM','EVOERPUPDW.DFM','EVOSERVICESETUP.DFM',
    # Utility/reporting
    'BOMTREE.DFM','EDITBOMTREE.DFM',
    'CASHFLOW.DFM','CASHFLOWREPORT.DFM',
    'COMMISSIONRPT.DFM','ISCCREP.DFM',
    'INVCHANGE.DFM','MACHINEVIEW.DFM','WORKCENTERLOAD.DFM',
    'SQLEXPORT.DFM','QUERYEXECUTE.DFM',
    'SSS.DFM','SSSFD.DFM','ROP.DFM',
    'PURCHITEM.DFM','PURCHVEND.DFM',
    'autoT7POJC.DFM','PTWOKI.DFM',
    'REMREM.DFM','GetFileName.DFM','GetAlphaGen.DFM',
    'udfedit.DFM','GRIDPLAY.DFM',
    # T6 era legacy forms
    'T6EVOINB.DFM','T6ISINB.DFM','T6ISINB2.DFM',
    'T6ISINBECO.DFM','T6ISINBLNK.DFM','T6ISINBMFG.DFM',
    'T6ISINBMRP.DFM','T6ISINBSPC.DFM','T6ISINBVND.DFM',
    'T6ISSTDCST.DFM','T6EVOART.DFM',
    # WBK web interface
    'WBKHHLOOKUP.DFM','WBKLOOKUP.DFM','WBKLPRINT.DFM',
    'WBKMENUBUTT.DFM','WBKMENUSETUP.DFM',
    # WTAS integration
    'WTASDATAM.DFM','WTASDMGR.DFM','WTASDMGR2.DFM',
    'WTASINIT.DFM','WTASMERGE2.DFM',
    # Calendar/scheduling
    'CALDRILL.DFM','calDDsel.DFM','calrem.DFM','dayrem.DFM',
    # Misc
    'ACT7SHKNOTE.DFM','ENPM.DFM','NUMEMP.DFM',
    'DFMALTS.DFM','DDFilters.DFM',
    'nzemail.DFM','nzedefs.DFM',
    'EMAILREL4.DFM','REPORT.DFM',
    'dbamenu_LOGIN.Dfm','dbamenu_SELCOMP.Dfm',
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
        print('  FIELDS:', ' | '.join(fields[:40]))
    print()
