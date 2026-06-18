import re, os, sys
sys.stdout.reconfigure(encoding='utf-8')

dfm_dir = r'C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\samples\dfm'

targets = sorted([
    'T7RTMVALID.DFM',
    'T7FOC.DFM','T7FOD.DFM','T7FOE.DFM',
    'T7QSOA.DFM','T7QSOALINES.DFM',
    'T7VSCHED.DFM',
    'T7SHA.DFM','T7SHB.DFM','T7SHC.DFM','T7SHE.DFM','T7SHF.DFM','T7SHG.DFM',
    'T7SHH.DFM','T7SHI.DFM','T7SHJ.DFM','T7SHM.DFM','T7SHN.DFM','T7SHO.DFM','T7SHP.DFM',
    'T7SHIPRTM.DFM',
    'T7QCA.DFM','T7QCB.DFM','T7QCC.DFM','T7QCD.DFM',
    'T7QCFA.DFM','T7QCMTHD.DFM','T7QCRSLT.DFM','T7QCSPEC.DFM','T7QCRESULTS.DFM',
    'T7SMA.DFM','T7SMC.DFM','T7SMD.DFM','T7SME.DFM','T7SMG.DFM','T7SMH.DFM',
    'T7SMJA.DFM','T7SMJB.DFM','T7SMJC.DFM','T7SMJD.DFM','T7SMJE.DFM','T7SMJF.DFM',
    'T7SMJG.DFM','T7SMJH.DFM',
    'T7SMIA.DFM','T7SMIB.DFM','T7SMIC.DFM','T7SMID.DFM','T7SMIE.DFM','T7SMIF.DFM',
    'T7PRA.DFM','T7PRB.DFM','T7PRC.DFM','T7PRD.DFM','T7PRM.DFM','T7PRLA.DFM','T7PRLB.DFM',
    'T7CSA.DFM','T7CSB.DFM','T7CSC.DFM','T7CSD.DFM','T7CSE.DFM','T7CSF.DFM','T7CSI.DFM','T7CSO.DFM','T7CSP.DFM',
    'T7ESB.DFM','T7ESC.DFM','T7ESD.DFM','T7ESE.DFM','T7EST.DFM',
    'T7SAA.DFM','T7SAM.DFM','T7SAN.DFM','T7SAO.DFM','T7SAQ.DFM',
    'T7FAA.DFM','T7FAB.DFM','T7FAE.DFM',
    'INVCHANGE.DFM','ISCCREP.DFM','T7CUSTOMS.DFM','T7CUSTCO.DFM','T7BZFIX.DFM',
    'T7CHARGBK.DFM','T7GFCB.DFM','T7GFPRICE.DFM','T7GFR.DFM',
    'T7SPCLIVEGRID.DFM','T7SPCLIVEREP.DFM','T7SPCREP2.DFM','T7SPCREPPPM.DFM',
    'T7SRB.DFM','T7SRBK.DFM','T7SRD.DFM','T7SRE.DFM','T7SRF.DFM','T7SRG.DFM',
    'T7SRGA.DFM','T7SRI.DFM','T7SRS.DFM','T7SRINFO.DFM',
    'WBKMENUBUTT.DFM','WBKMENUSETUP.DFM','WBKMENUSUCPRG.DFM','WBKMENUSUNEWAC.DFM','WBKMENUPICS.DFM',
    'EVOBSR.DFM','EVOBSCASH.DFM','EVOBSWO.DFM',
    'T7SMJL.DFM','T7SMJL2.DFM','T7SMJM.DFM','T7SMJN.DFM','T7SMJO.DFM','T7SMJQ.DFM','T7SMJR.DFM','T7SMJS.DFM','T7SMJV.DFM',
    'T7SMK.DFM','T7SML.DFM','T7SMN.DFM','T7SMNA.DFM','T7SMNF.DFM','T7SMO.DFM','T7SMT.DFM','T7SMTEND.DFM','T7SMTSET.DFM',
    'T7SMU.DFM','T7SMW.DFM','T7SMPA.DFM','T7SMPB.DFM','T7SMPF.DFM','T7SMPH.DFM','T7SMPI.DFM','T7SMPJ.DFM',
    'T7SMSB.DFM','T7SMSC.DFM','T7SMSD.DFM',
    'T7SMHMRK.DFM','T7SMGA.DFM','T7SMBB.DFM',
])

boring = {'OK','Cancel','Close','&OK','&Cancel','&Close','Help','&Help','Yes','No','Save','Exit',
          'Print','Edit','Add','Delete','New','Find','Search','Clear','Select','Update','Apply',
          'Back','Next','Finish','Browse','&Yes','&No','&Save','&Exit','&Print','&Edit','&Add',
          '&Delete','&New','&Find','&Clear','&Select','&Update','&Apply','&Back','&Next'}

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
