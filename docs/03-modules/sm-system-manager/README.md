# System Manager / Setup (SM)

Status: verified (auto-generated from the extracted schema, menu-code dump, and DFM inventory).

- **Module code**: `SM`
- **Tables**: 10 (prefixes `BKSY`, `BKYS`, `AHSY`)
- **UI forms**: 109 (prefixes `T7SM`, `T6SM`, `EVO`)
- **Menu operations**: 34

## Menu operations

| Code | Operation | Legacy module file(s) |
| ---- | --------- | --------------------- |
| `SM-D` | Enter Terms Table | BKAME |
| `SM-E` | Enter Tax Codes | BKAMF |
| `SM-F` | Enter Tax Groups | BKAMG |
| `SM-G` | Enter Employees | BKMMB |
| `SM-H` | Enter Shop Calendar | BKMMC |
| `SM-I-A` | Enter Lead Source Codes | BKAMLA |
| `SM-I-B` | Enter Territory Codes | BKAMLB |
| `SM-I-C` | Enter History Codes | BKAMLC |
| `SM-I-D` | Enter Account Follow-up Codes | BKAMLD |
| `SM-I-E` | Enter Vendor Follow-up Codes | BKAMLE |
| `SM-I-F` | Enter Personal Contact Follow-up Codes | BKAMLF |
| `SM-I-G` | Enter Class Codes | BKAMLG |
| `SM-I-H` | Enter Key Date Codes | BKAMLH |
| `SM-I-I` | Enter Reps and Passwords | BKAMLI |
| `SM-I-J` | Purge Account History | BKAMLJ |
| `SM-I-K` | Purge Account Follow-ups | BKAMLK |
| `SM-I-L` | Purge Vendor Contact History | BKAMLL |
| `SM-I-M` | Purge Vendor Follow-ups | BKAMLM |
| `SM-I-N` | Purge Personal Contact History | BKAMLN |
| `SM-I-O` | Purge Personal Contact Follow-ups | BKAMLO |
| `SM-J-A` | Work Order File Maintenance | BKMMF |
| `SM-J-H` | Purge Data Collection File | BKMML |
| `SM-J-I` | Purge Estimates | BKMMM |
| `SM-J-J` | Purge Closed Sales Orders | BKAMPD;ISSMJJ |
| `SM-J-K` | Purge Invoice History | BKAMPE;ISSMJJ |
| `SM-J-M` | Change Customer Codes | BKAMM |
| `SM-J-N` | Change Vendor Codes | BKAMN |
| `SM-J-O` | Rebuild Customer/Vendor Totals | BKAMK |
| `SM-J-P` | Purge AR Vouchers | BKAMPC;ISSMJJ |
| `SM-J-Q` | Bill of Material Recursion Utility | BKBMM |
| `SM-J-R` | Archive Purchase Order History | ISSMJR |
| `SM-J-S` | Purge Inventory Audit Info. | ISSMJS |
| `SM-J-T` | Archive/Restore Quotes | ISSMJJ |
| `SM-P-F` | Description Entry | ISJOBS |

## UI forms (109)

| DFM file | Caption | fields | controls | tabs |
| -------- | ------- | -----: | -------: | ---: |
| `EVODCS.DFM` | New Screen | 0 | 2 | 0 |
| `EVOENOTES.DFM` |  Entering Notes | 8 | 35 | 0 |
| `EVOERPUPDW.DFM` | Archive Work Orders | 1 | 6 | 0 |
| `EVOERROR.DFM` | File Open Error | 0 | 7 | 0 |
| `EVOFILTERS.DFM` | New Screen | 106 | 270 | 11 |
| `EVOFUP.DFM` | UpLoad Files | 5 | 21 | 0 |
| `EVOMESSAGE.DFM` |  Evo Message | 0 | 4 | 0 |
| `EVORESETPASS.DFM` |  Reset Password | 3 | 10 | 0 |
| `EVOSERVICEREMOVE.DFM` | Remove EvoService from your Server | 0 | 6 | 0 |
| `EVOSERVICESETUP.DFM` | Create EvoService for your Server | 11 | 29 | 0 |
| `EVOUPASS.DFM` | Password | 2 | 7 | 0 |
| `EvoBS.DFM` |  Business Status | 24 | 110 | 4 |
| `EvoBSCash.DFM` |  Business Status Cash Detail | 10 | 24 | 0 |
| `EvoBSR.DFM` | Business Status Rebuild | 0 | 3 | 0 |
| `EvoBSWO.DFM` |  Business Status Work Orders | 10 | 25 | 0 |
| `EvoCSI.DFM` | Evo Master Inquiry | 9 | 29 | 0 |
| `EvoDCmenu.DFM` |  | 0 | 1 | 0 |
| `EvoDCmenu2.DFM` |  | 0 | 7 | 0 |
| `EvoDCsetup.DFM` | Create Workstation Setup | 3 | 11 | 0 |
| `EvoELinks.DFM` |  | 0 | 1 | 0 |
| `EvoEMsg.DFM` |  Evo Message | 2 | 6 | 0 |
| `EvoERPDrillM.DFM` | ToolBar1 | 0 | 7 | 0 |
| `EvoERPbackup.DFM` |  | 0 | 1 | 0 |
| `EvoERPupd.DFM` |  Evo ~ ERP  Update | 2 | 24 | 0 |
| `EvoFNO.DFM` |  | 0 | 1 | 0 |
| `EvoFNOPO.DFM` | Converting to Purchase Order | 0 | 3 | 0 |
| `EvoFNOQty.DFM` | F&O Qty | 4 | 13 | 0 |
| `EvoFNOSO.DFM` | Converting to Sales Order | 0 | 3 | 0 |
| `EvoFNOWO.DFM` | Converting to Work Order | 0 | 3 | 0 |
| `EvoForceUpd.DFM` |  Evo ~ ERP  Force Update | 2 | 21 | 0 |
| `EvoLinkCVT.DFM` | Evo Links CVT | 0 | 4 | 0 |
| `EvoLinks.DFM` |  | 0 | 1 | 0 |
| `EvoMobilesetup.DFM` |  Create Mobile Reminders Setup | 8 | 25 | 0 |
| `EvoMobilsetup.DFM` |  Create Mobil Reminders Setup | 1 | 6 | 0 |
| `EvoNoteSearch.DFM` | Evo Notes Search | 4 | 21 | 0 |
| `EvoNotes.DFM` |  | 0 | 1 | 0 |
| `EvoNotesARCH.DFM` | Evo Notes | 35 | 72 | 0 |
| `EvoNotesPrt.DFM` |  Evo Notes Selection | 6 | 24 | 0 |
| `EvoNotesRpt.DFM` | Evo Notes | 33 | 70 | 0 |
| `EvoSchedsetup.DFM` |  Create Evo Scheduler as a Service | 8 | 25 | 0 |
| `EvoScheduler.DFM` |  | 0 | 1 | 0 |
| `EvoUPDATE.DFM` | Update EvoERP | 0 | 3 | 0 |
| `EvoUPDsetup.DFM` |  Create Update Setup | 1 | 6 | 0 |
| `EvocfgSave.DFM` | Save or Restore Program Defaults  | 1 | 7 | 0 |
| `Evocnvtb.DFM` |  Synchronize Data Dictionary with Btreive | 1 | 8 | 0 |
| `Evopass.DFM` | Password | 1 | 5 | 0 |
| `Evowkssetup.DFM` | Create Workstation Setup | 3 | 13 | 0 |
| `T7SMC.DFM` |  | 0 | 1 | 0 |
| `T7SMCA.DFM` |  | 0 | 1 | 0 |
| `T7SMCB.DFM` |  | 0 | 1 | 0 |
| `T7SMCC.DFM` |  | 0 | 1 | 0 |
| `T7SMD.DFM` |  | 0 | 1 | 0 |
| `T7SME.DFM` |  | 0 | 1 | 0 |
| `T7SMF.DFM` |  | 0 | 1 | 0 |
| `T7SMG.DFM` | New Screen | 37 | 94 | 0 |
| `T7SMGA.DFM` |  | 0 | 1 | 0 |
| `T7SMH.DFM` | caldrillbt | 0 | 50 | 0 |
| `T7SMHMRK.DFM` | New Screen | 8 | 29 | 0 |
| `T7SMIA.DFM` |  | 0 | 1 | 0 |
| `T7SMIB.DFM` |  | 0 | 1 | 0 |
| `T7SMIC.DFM` |  | 0 | 1 | 0 |
| `T7SMID.DFM` |  | 0 | 1 | 0 |
| `T7SMIE.DFM` |  | 0 | 1 | 0 |
| `T7SMIF.DFM` |  | 0 | 1 | 0 |
| `T7SMJA.DFM` | SM-JA | 2 | 21 | 0 |
| `T7SMJB.DFM` | SM-JB | 17 | 46 | 0 |
| `T7SMJC.DFM` | SM-JC | 12 | 47 | 2 |
| `T7SMJD.DFM` | SM-JD | 7 | 30 | 0 |
| `T7SMJE.DFM` | SM-JE | 7 | 29 | 0 |
| `T7SMJF.DFM` | SM-JF | 7 | 28 | 0 |
| `T7SMJG.DFM` | SM-J-G | 8 | 30 | 0 |
| `T7SMJH.DFM` | SM-JH | 2 | 18 | 0 |
| `T7SMJI.DFM` | SM-J-I | 8 | 30 | 0 |
| `T7SMJJ.DFM` | SM-JJ | 10 | 33 | 0 |
| `T7SMJL.DFM` | SM-JL | 11 | 37 | 0 |
| `T7SMJL2.DFM` | Merge Options | 4 | 12 | 0 |
| `T7SMJM.DFM` |  | 0 | 1 | 0 |
| `T7SMJN.DFM` | SM-JN | 26 | 60 | 0 |
| `T7SMJO.DFM` | T7AMK | 25 | 63 | 0 |
| `T7SMJQ.DFM` | New Screen | 15 | 34 | 0 |
| `T7SMJR.DFM` | SM-JR | 8 | 30 | 0 |
| `T7SMJS.DFM` | SM-JS | 15 | 34 | 0 |
| `T7SMJV.DFM` | BASE Blank T7 SCREEN | 10 | 34 | 0 |
| `T7SMK.DFM` |  Evo User Settings | 67 | 164 | 10 |
| `T7SML.DFM` |  | 0 | 1 | 0 |
| `T7SMN.DFM` | E&xit | 0 | 1 | 0 |
| `T7SMNA.DFM` |  | 0 | 1 | 0 |
| `T7SMNF.DFM` | BASE Blank T7 SCREEN | 4 | 24 | 0 |
| `T7SMO.DFM` |  | 0 | 1 | 0 |
| `T7SMPA.DFM` |  | 0 | 1 | 0 |
| `T7SMPB.DFM` |  | 0 | 1 | 0 |
| `T7SMPF.DFM` |  | 0 | 1 | 0 |
| `T7SMPH.DFM` |  | 0 | 1 | 0 |
| `T7SMPI.DFM` |  | 0 | 1 | 0 |
| `T7SMPJ.DFM` |  | 0 | 1 | 0 |
| `T7SMSB.DFM` | New Screen | 7 | 25 | 0 |
| `T7SMSC.DFM` | SMSC | 6 | 25 | 0 |
| `T7SMSD.DFM` | BASE Blank T7 SCREEN | 9 | 38 | 0 |
| `T7SMT.DFM` |  | 0 | 1 | 0 |
| `T7SMTEND.DFM` | New Screen | 6 | 33 | 0 |
| `T7SMTSET.DFM` |  | 0 | 1 | 0 |
| `T7SMU.DFM` |  | 0 | 1 | 0 |
| `T7SMW.DFM` | BASE Blank T7 SCREEN | 3 | 24 | 0 |
| `evoCSR.DFM` | Calandar Summary Report | 10 | 23 | 0 |
| `evoERPsched.DFM` | Evo ~ ERP Scheduler | 11 | 20 | 0 |
| `evoalerts.DFM` |  Evo Alerts | 0 | 6 | 0 |
| `evogetdate.DFM` | Evo ~ ERP | 1 | 9 | 0 |
| `evoreminders.DFM` |  | 0 | 1 | 0 |
| `evorereminders.DFM` | Reschedule | 3 | 9 | 0 |

## Database tables (10)

Full field details are in `../../../samples/ddf/schema.md` (see per-table heading).

| Table | File on disk | Fields | Key fields (first 3) |
| ----- | ------------ | -----: | -------------------- |
| **AHSYLOG** | `AHSYLOG.B` | 23 | `AHSY_USER_LEVL`, `AHSY_USER_MENU`, `AHSY_USER_CTRL` |
| **BKSYAP** | `BKSYAP.B` | 11 | `BKSY_AP_RECVNUM`, `BKSY_AP_REOPEN`, `BKSY_AP_RQSCRAP` |
| **BKSYAR** | `BKSYAR.B` | 2 | `BKSY_AR_TRXN`, `BKSY_AR_DEPNO` |
| **BKSYCFG** | `BKSYCFG.B` | 4 | `BKSY_CFG_ACCTG`, `BKSY_CFG_SALES`, `BKSY_CFG_LITEWO` |
| **BKSYHELP** | `BKSYHELP.B` | 1 | `BKSY_HELP_PATH` |
| **BKSYLOG** | `BKSYLOG.B` | 215 | `BKSY_LOGON_CHR`, `BKSY_LOGON_CODE`, `BKSY_LOGON_PSWD` |
| **BKSYMSTR** | `BKSYMSTR.B` | 286 | `BKSY_ARINV_NUM`, `BKSY_APINV_NUM`, `BKSY_APPO_NUM` |
| **BKSYPRTR** | `BKSYPRTR.B` | 11 | `BKSY_PRTR_NAME`, `BKSY_PRTR_EXEC`, `BKSY_PRTR_TAS` |
| **BKSYUSER** | `BKSYUSER.B` | 5 | `BKSY_USER_CHR`, `BKSY_USER_CODE`, `BKSY_USER_PSWD` |
| **BKYSMSTR** | `BKYSMSTR.B` | 355 | `BKYS_WONUM`, `BKYS_YN_1`, `BKYS_YN_2` |

## Notes & open questions

- *(populated per-module manually as deeper reading happens.)*
