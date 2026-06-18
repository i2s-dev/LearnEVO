import re, os, sys
sys.stdout.reconfigure(encoding='utf-8')

dfm_dir = r'C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\samples\dfm'

targets = [
    # T7DE (EDI)
    'T7DEER.DFM','T7DEFECT.DFM','T7DEHD.DFM','T7DEJH.DFM','T7DEK.DFM',
    'T7DEL.DFM','T7DEM.DFM','T7DEP860.DFM','T7DEPB.DFM','T7DEPD.DFM',
    'T7DEPE.DFM','T7DEPF.DFM','T7DEPH.DFM','T7DEQ.DFM','T7DER.DFM',
    'T7DET.DFM','T7DETB.DFM','T7DEU.DFM','T7DEV.DFM','T7DEX.DFM',
    # EVO system tools
    'EVOENOTES.DFM','EvoELinks.DFM','EvoEMsg.DFM','EvoDCmenu.DFM',
    'EvoDCmenu2.DFM','EVODCS.DFM','EvoDCsetup.DFM','CRMDASHBOARD.DFM',
    'EvoERPbackup.DFM','EvoERPDrillM.DFM','evoERPsched.DFM','EvoERPupd.DFM',
    'EVOCHANGEPASS.DFM','EVORESETPASS.DFM','Evopass.DFM','EVOUPASS.DFM',
    'EvoSchedsetup.DFM','EvoUPDsetup.DFM','Evowkssetup.DFM','EvoMobilesetup.DFM',
    'EvocfgSave.DFM','EVOFILTERS.DFM','EVOERROR.DFM','EVOLOGO.DFM',
    'EvoFNO.DFM','EvoFNOPO.DFM','EvoFNOQty.DFM','EvoFNOSO.DFM','EvoFNOWO.DFM',
    'EvoLinkCVT.DFM','EvoNotesARCH.DFM','EvoNoteSearch.DFM','EvoNotesPrt.DFM',
    'EvoNotesRpt.DFM','EVOSERVICESETUP.DFM','EvoForceUpd.DFM',
    'EVOERPUPDW.DFM','EVOFUP.DFM','evogetdate.DFM',
    'EvoMobilsetup.DFM','Evocnvtb.DFM','EvoCSI.DFM','evoCSR.DFM',
    'EVOSERVICEREMOVE.DFM',
    # Calendar/Reminders
    'CALDRILL.DFM','caldrillbt.DFM','CALGRIDDRILL.DFM','calrem.DFM',
    'CALREMGC.DFM','dayrem.DFM','evorereminders.DFM','REMREM.DFM','T7RemindRpt.DFM',
    # T7RM (RMA)
    'T7RMAWHY.DFM','T7RMD.DFM','T7RMDASK.DFM','T7RME.DFM','T7RMG.DFM',
    # T7IM (Landed Cost)
    'T7IMB.DFM','T7IMC.DFM','T7IMD.DFM','T7IME.DFM','T7IMF.DFM',
    # T7GF (AR Charges)
    't7GFdept.DFM','t7GFdiv.DFM','T7GFTEST.DFM','T7GFV.DFM','T7GFVS.DFM',
    # ht6 (handheld T6)
    'ht6close.DFM','ht6inc.DFM','ht6so.DFM','ht6wo.DFM',
    # Misc
    'PURCHITEM.DFM','PURCHVEND.DFM','NascoPAYex.DFM','ROP.DFM',
    'NUMEMP.DFM','nzedefs.DFM','nzemail.DFM','nzemailtll.DFM',
    'SSS.DFM','SSSFD.DFM','SQLEXPORT.DFM','ACT7SHKNOTE.DFM',
    'COMMISSIONRPT.DFM','autoT7POJC.DFM','PTWOKI.DFM',
    'DDFilters.DFM','DFMALTS.DFM','ENPM.DFM','GetAlphaGen.DFM',
    'GetFileName.DFM','GRIDPLAY.DFM','imageinfo.DFM','Imageprint.DFM',
    'printtll.DFM','REPORT.DFM','classic2evonts.DFM',
    'chartBarModal.DFM','chartLineModal.DFM','ChartPieModal.DFM','EMAILREL4.DFM',
]

boring = {'OK','Cancel','Close','&OK','&Cancel','&Close','Help','&Help','Yes','No','Save','Exit',
          'Print','Edit','Add','Delete','New','Find','Search','Clear','Select','Update','Apply',
          'Back','Next','Finish','Browse','&Yes','&No','&Save','&Exit','&Print','&Edit','&Add',
          '&Delete','&New','&Find','&Clear','&Select','&Update','&Apply','&Back','&Next',
          'Process','&Process','Go','&Go','Post','&Post','Tag','Untag','Tag All','Untag All',
          'True','False','None','','None'}

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
        print('  CAPTIONS:', ' | '.join(caps[:30]))
    if fields:
        print('  FIELDS:', ' | '.join(fields[:30]))
    print()
