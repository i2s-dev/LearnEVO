import re, os, sys
sys.stdout.reconfigure(encoding='utf-8')

dfm_dir = r'C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\samples\dfm'

targets = [
    # WC - Warehouse/Work Center
    'T7WCD.DFM','T7WCE.DFM','T7WCF.DFM','T7WCG.DFM','T7WCH.DFM',
    'T7WCBinLot.DFM','T7WCBK.DFM','T7WCLOCFIX.DFM',
    # SR - Service Repair remaining
    'T7SRB.DFM','T7SRBK.DFM','T7SRD.DFM','T7SRE.DFM','T7SRF.DFM',
    'T7SRG.DFM','T7SRGA.DFM','T7SRI.DFM','T7SRINFO.DFM','T7SRS.DFM',
    # AM - Accounting Maintenance
    'T7AMA.DFM','T7AMB.DFM','T7AMC.DFM','T7AMD.DFM','T7AME.DFM',
    'T7AMH.DFM','T7AMI.DFM','T7AMJ.DFM','T7AMK.DFM','T7AMN.DFM',
    'T7AMO.DFM','T7AMP.DFM','T7AMQ.DFM','T7AMS.DFM',
    # MR - MRP (Material Requirements Planning)
    'T7MRA.DFM','T7MRADE.DFM','T7MRB.DFM','T7MRC.DFM','T7MRD.DFM',
    'T7MRE.DFM','T7MRF.DFM','T7MRG.DFM','T7MRH.DFM','T7MRI.DFM',
    'T7MRIR.DFM','T7MRIX.DFM','T7MRJ.DFM','T7MRJR.DFM','T7MRJX.DFM',
    'T7MRL.DFM','T7MRN.DFM','T7MRO.DFM',
    # GF - GL Finance
    'T7GFCB.DFM','t7GFdept.DFM','t7GFdiv.DFM','T7GFPRICE.DFM',
    'T7GFR.DFM','T7GFTEST.DFM','T7GFV.DFM','T7GFVS.DFM',
    # SM - System Maintenance / Item Inquiry
    'T7SMC.DFM','T7SMD.DFM','T7SME.DFM','T7SMG.DFM','T7SMH.DFM',
    'T7SMIA.DFM','T7SMIB.DFM','T7SMIC.DFM','T7SMID.DFM','T7SMIE.DFM',
    'T7SMIF.DFM','T7SMJA.DFM','T7SMJB.DFM','T7SMJC.DFM','T7SMJD.DFM',
    'T7SMJE.DFM','T7SMJF.DFM','T7SMJG.DFM','T7SMJH.DFM',
    # INA - Inventory A
    'T7INA.DFM',
    # Additional utility/misc
    'T7ACDATE.DFM','T7ACRDTYPE.DFM','T7ACTION.DFM','T7ALERTMSG.DFM',
    'T7ALTPART.DFM','T7BRANDS.DFM','T7BS.DFM','T7BSR.DFM','T7BOL.DFM',
    'T7BOLMSO.DFM','T7KIT.DFM','T7LOADING.DFM','T7CLoading.DFM',
    'T7ISMCC.DFM','T7ITMCFG.DFM','T7STOCK.DFM','T7STTYPE.DFM',
    'T7STYPE.DFM','T7NEWINIT.DFM','T7MULTIYIELD.DFM','T7PUTAWAY.DFM',
    'T7SELLOC.DFM','T7MDEFAULTS.DFM','T7MDefBanks.DFM','T7MDefNDC.DFM',
    'T7RFQ.DFM','T7QSOA.DFM','T7QSOALINES.DFM','T7QTINFO.DFM',
    'T7VSCHED.DFM','T7CUSTOMS.DFM','T7USG.DFM','T7GDM.DFM',
    'T7STDCST.DFM','T7BZFIX.DFM','T7BOMSCRAPFIX.DFM',
    'T7CHARGBK.DFM','T7EMGL.DFM','T7MAPDEPO.DFM',
    'T7ALOGSETUP.DFM','T7AUTODCH.DFM','T7EDII.DFM',
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
