# Menu Code → Program → Database Table Mapping

Status: **verified** — built from `BKMENUSU.TXT` (870 entries) cross-referenced against
`rwn_symbols.json` (1,122 decrypted RWN programs). Last updated: 2026-06-19. DFM column added 2026-06-19 (723/870 resolved from rwn_dfm_map.json).

Columns: **Code** | **Label** | **Program** | **DFM** | **Key DB Tables** (up to 4 primary)

> **BU / GR entries** are navigation groups (no program to launch).

---

## Module: AD

| Code | Label | Program | DFM | Key Tables |
|------|-------|---------|-----|------------|
| ADA | &A - General Ledger Defaults | T7DSGL.rwn | STUB.DFM | ISDROP, BKSYHELP, DBAHLPID, ISIS |
| ADB | &B - Checking Accounts Defaults | T7DSCK.rwn | STUB.DFM | ISDROP, BKSYHELP, DBAHLPID, ISIS |
| ADC | &C - Accounts Payable Defaults | T7DSAP.rwn | STUB.DFM | ISDROP, BKSYHELP, DBAHLPID, ISIS |

## Module: AM

| Code | Label | Program | DFM | Key Tables |
|------|-------|---------|-----|------------|
| AMA | &A - Reset Period-End Close Date | t7ama.rwn | T7AMA.DFM | BKSYMSTR, MKAHIST, BKYSMSTR, BKGLTRAN |
| AMB | &B - Fiscal Year End Routines | t7amb.rwn | T7AMB.DFM | BKGLCOA, ISGLCOA, BKSYMSTR, ISGLDATE |
| AMC | &C - Enter General Ledger Accounts | T7AMC.RWN | T7AMC.DFM | BKGLCOA, ISGLDATE, ISGLCOA, BKGLTRAN |
| AMD | &D - Enter General Ledger Departments | t7amd.rwn | T7AMD.DFM | BKGLCOA, ISGLCOA, BKSYHELP, DBAHLPID |
| AME | &E - Format Standard Financial Statement | t7ame.rwn | T7AME.DFM | BKGLSTMT, BKSYHELP, DBAHLPID, ISIS |
| AMF | &F - Format Custom Financial Statements | t6amf.run |  |  |
| AMG | &G - Consolidate Financials | t7amg.rwn | T7AMG.DFM | BKSYMSTR, FILELOC, ISMCF, BKGLCOA |
| AMH | &H - Change GL Account Codes | t7amh.rwn | T7AMH.DFM | BKGLCOA, ISGLCOA, ISGLNBGT, BKGLTRAN |
| AMI | &I - Consolidate General Ledger Detail | t7ami.rwn | T7AMI.DFM | BKGLCOA, BKGLTRAN, ISGLDATE, BKSYMSTR |
| AMJ | &J - Purge/Archive AP History | t7amj.rwn | T7AMJ.DFM | BKAPCHKF, BKAPINVT, BKAPINVL, BKISTAX |
| AMK | &K - Purge/Archive AR History | t7amk.rwn | T7AMK.DFM | BKARINVT, BKART, BKAPCHKF, BKARINVI |
| AMN | &N - Maintain GL Fiscal Periods | T7AMN.RWN | T7AMN.DFM | ISGLDATE, BKSYMSTR, BKSYHELP, DBAHLPID |
| AMO | &O - Purge/Archive Vendor Data | t7amo.rwn | T7AMO.DFM | BKSYMSTR, BKAPPO, BKAPPOL, BKAPVEND |
| AMP | &P - Purge/Archive Customer Data | t7amp.rwn | T7AMP.DFM | BKSYMSTR, BKARINV, BKARINVL, BKARCUST |
| AMQ | &Q - Enter Budget Amounts | t7amq.rwn | T7AMQ.DFM | ISGLCOA, ISGLDATE, BKGLCOA, ISGLNBGT |
| AMR | &R - Out of Balance Report | T7GLOOB.RWN | T7GLOOB.DFM | BKGLTRAN, BKSYHELP, DBAHLPID, ISIS |
| AMS | &S - Purge/Archive GL Journals | t7ams.rwn | T7AMS.DFM | BKSYMSTR, BKGLGJRN, BKGLGJLN, BKSYHELP |
| AMT | &T - Archive GL Transaction Detail | T7GLARCH.RWN | T7GLARCH.DFM | BKSYMSTR, ISGLDATE, BKGLTRAN, BKSYHELP |

## Module: AP

| Code | Label | Program | DFM | Key Tables |
|------|-------|---------|-----|------------|
| APA | &A - Enter Vendors | t7apa.rwn | T7APA.DFM | BKAPVEND, BKAPVND2, ISTAXGRP, ISEXUSER |
| APB | &B - Enter Vouchers | t7apb.rwn | T7APB.DFM | BKAPINVL, BKAPINVT, BKAPVEND, BKYSMSTR |
| APC | &C - Enter Purchase Order Invoices | t7apc.rwn | T7APC.DFM | BKAPVEND, BKQCMSTR, BKAPPOL, BKAPPO |
| APD | &D - Enter Scheduled Payment Dates | t7apd.rwn | T7APD.DFM | BKAPVEND, BKAPINVT, ISTERMS, BKSYHELP |
| APE | &E - Print Vouchers/Invoices Due by Date | t7ape.rwn | T7APE.DFM | BKSYMSTR, BKAPINVT, ISMCF, BKAPVEND |
| APF | &F - Pick Vouchers/Invoices to Pay | t7apf.rwn | T7APF.DFM | BKAPVEND, BKYSMSTR, BKAPCHKF, BKAPINVT |
| APG | &G - Print Pro Forma Check Register | t7apg.rwn | T7APG.DFM | BKSYMSTR, BKYSMSTR, BKAPCHKF, BKAPVEND |
| APH | &H - Print Checks | t7aph.rwn | T7APH.DFM | BKYSMSTR, BKAPCHKF, ISBANKS, ISMCF |
| API | &I - Print Aging | t7api.rwn | T7API.DFM | BKSYMSTR, BKYSMSTR, BKAPINVT, BKAPVEND |
| APJ | &J - Print Vendor Code and Name | t7apj.rwn | T7APJ.DFM | BKAPVEND, ISAPEX, BKSYHELP, DBAHLPID |
| APK | &K - Print Vendor General Info | t7apk.rwn | T7APK.DFM | BKSYMSTR, BKAPVEND, BKAPVND2, CLASMSTR |
| APL | &L - Print Vendor Purchase Info | t7apl.rwn | T7APL.DFM | BKSYMSTR, BKAPVEND, BKSYHELP, DBAHLPID |
| APM | &M - Print Vendor Labels | t7apm.rwn | T7APM.DFM | BKAPVEND, BKSYHELP, DBAHLPID, BKYSMSTR |
| APN | &N - Enter Vouchers (Edit Address) | t7apn.rwn | STUB.DFM | MKAHIST, BKSYHELP, DBAHLPID, BKYSMSTR |
| APO | &O - Enter Recurring Vouchers | t7apo.rwn | STUB.DFM | MKAHIST, BKSYHELP, DBAHLPID, BKYSMSTR |
| APP | &P - Generate Recurring Vouchers | t7app.rwn | T7APP.DFM | BKAPINVL, BKSYMSTR, BKAPVEND, BKYSMSTR |
| APQ | &Q - Void AP Check | t7apq.rwn | T7APQ.DFM | BKAPVEND, BKSYMSTR, BKYSMSTR, BKAPCHKF |
| APR | &R - Print AP Payment History | t7apr.rwn | T7APR.DFM | BKYSMSTR, ISBANKS, ISBUILD, BKAPCHKF |
| APS | &S - Print 1099 Forms | t7aps.rwn | T7APS.DFM | BKSYMSTR, BKAPVEND, BKAPVND2, BKAPCHKF |
| APT | &T - AP Check Inquiry | T7APT.RWN | T7APT.DFM | BKAPVEND, BKAPCHKF, BKAPINVT, BKAPPO |
| APU | &U - View Vendor Information | T7APU.RWN | STUB.DFM | MKAHIST, BKAPCHKF, BKAPINVT, BKAPPO |
| APV | &V - Enter Vendor Deposit | T7APV.RWN | T7APV.DFM | BKARDEP, BKAPINVT, BKAPVEND, BKAPPO |
| APW | &W - Accounts Payable Defaults | T7DSAP.RWN | STUB.DFM | ISDROP, BKSYHELP, DBAHLPID, ISIS |
| APX | &X - Print Invoice Details | T7APX.RWN | T7APX.DFM | BKAPINVT, ISLINKS, BKAPPOL, BKAPPO |
| APY | &Y - Remittance Options | *(group)* |  |  |
| APYA | &A - Print Remittance Advice | T7APY.RWN | T7APY.DFM | BKSYMSTR, ISBANKS, BKGLCHK, BKYSMSTR |
| APYB | &B - Positive Pay | T7APYB.RWN | T7APYB.DFM | BKSYMSTR, ISBANKS, BKPRCURP, BKPRMSTR |
| APYC | &C - NACHA Upload | T7APYC.RWN | T7APYC.DFM | BKSYMSTR, ISBANKS, BKGLCHK, BKAPVEND |
| APZ | &Z - Reports | *(group)* |  |  |
| APZA | &A - Top Vendor Listing | t7apza.rwn | T7APZA.DFM | BKSYMSTR, CLASMSTR, BKCMTERR, ISBUILD |

## Module: AR

| Code | Label | Program | DFM | Key Tables |
|------|-------|---------|-----|------------|
| ARA | &A - Enter Customers | t7ara.rwn | T7ARA.DFM | BKARCUST, ISAREX, ISTAXGRP, BKCMDUNH |
| ARB | &B - Enter Vouchers | t7arb.rwn | T7ARB.DFM | BKARCUST, BKARINVV, ISNOTES, BKSYMSTR |
| ARC | &C - Record Payments | t7arc.rwn | T7ARC.DFM | BKARCUST, BKSYMSTR, BKARINV, BKARINVT |
| ARD | &D - Charge Interest on Invoices | t7ard.rwn | T7ARD.DFM | BKSYMSTR, ISMCF, BKARCUST, BKARINVT |
| ARE | &E - Print Statements | t7are.rwn | T7ARE.DFM | BKSYMSTR, ISMCF, BKYSMSTR, BKARCUST |
| ARF | &F - Print Aging | t7arf.rwn | T7ARF.DFM | BKSYMSTR, BKART, BKYSMSTR, BKARCUST |
| ARG | &G - Print Customer Code and Name | t7arg.rwn | T7ARG.DFM | ISTERMS, BKARCUST, BKARINV, BKPRSALE |
| ARH | &H - Print Customer General Info | t7arh.rwn | T7ARH.DFM | BKARCUST, BKARINV, ISTERMS, BKSYHELP |
| ARI | &I - Print Customer Mail Labels | t7ari.rwn | T7ARI.DFM | BKARCUST, BKARINV, BKSYHELP, DBAHLPID |
| ARK | &K - Print Sales Tax Report | t7ark.rwn | T7ARK.DFM | BKSYMSTR, BKISTAX, ISTAXFIL, BKARINV |
| ARL | &L - Transfer Sales Taxes | T7ARL.RWN | T7ARL.DFM | BKISTAX, ISTAXFIL, BKYSMSTR, BKAPVEND |
| ARM | &M - Enter Customer Refund | t7arm.rwn | T7ARM.DFM | BKAPINVT, BKGLCHK, BKARCUST, BKAPVEND |
| ARN | &N - Enter/Print Customer Deposits | t7arn.rwn | T7ARN.DFM | BKARDEP, BKARINV, BKARCUST, BKARINVT |
| ARP | &P - Customer Payment Notification | t7arp.rwn | T7ARP.DFM | BKSYMSTR, BKARINVT, BKARCUST, ISTERMS |
| ARQ | &Q - View Customer Information | T7arq.rwn | STUB.DFM | MKAHIST, BKARINV, BKARCUST, BKARINVT |
| ARR | &R - Print AR Payment History | t7arr.rwn | T7ARR.DFM | BKYSMSTR, ISBANKS, BKAPCHKF, BKARINV |
| ARS | &S - Accounts Receivable Defaults | t7dsar.rwn | STUB.DFM | ISDROP, BKSYHELP, DBAHLPID, ISIS |
| ARU | &U - Update Credit Hold Status | T7ARU.RWN | T7ARU.DFM | BKARCUST, BKARINVT, BKSYMSTR, BKSYHELP |

## Module: BM

| Code | Label | Program | DFM | Key Tables |
|------|-------|---------|-----|------------|
| BMA | &A - Enter Bills of Material | t7bma.rwn | T7BMA.DFM | BKBMREMK, BKBMMSTR, BKYSMSTR, BKPSUSER |
| BMB | &B - Print Bills of Material | t7bmb.rwn | T7BMB.DFM | BKYSMSTR, MTICMSTR, BKICMSTR, BKBMMSTR |
| BMC | &C - Print Where Used | t7bmc.rwn | T7BMC.DFM | BKYSMSTR, BKICMSTR, BKBMMSTR, MTICMSTR |
| BMD | &D - Print BOM Availability | t7bmd.rwn | T7BMD.DFM | BKYSMSTR, BKSYMSTR, BKICMSTR, BKBMMSTR |
| BME | &E - Global Replace | t7bme.rwn | T7BME.DFM | BKSYMSTR, BKICMSTR, BKBMMSTR, BKBMREMK |
| BMF | &F - Global Delete | t7bmf.rwn | T7BMF.DFM | BKICMSTR, BKBMMSTR, BKSYHELP, DBAHLPID |
| BMG | &G - Print/Rollup Standard Costs | t7bmg.rwn | T7BMG.DFM | BKSYMSTR, MTICMSTR, ISCATMST, BKBMMSTR |
| BMH | &H - Print BOM at Average Cost | t7bmh.rwn | T7BMH.DFM | BKYSMSTR, MTICMSTR, BKICMSTR, ISICMSTR |
| BMI | &I - Print Summarized BOM | t7bmi.rwn | T7BMI.DFM | BKYSMSTR, BKICMSTR, MTICMSTR, BKBMMSTR |
| BMJ | &J - Enter Approved Substitutes | t7bmj.rwn | T7BMJ.DFM | BKARCUST, BKSBPART, BKICMSTR, BKSYHELP |
| BMK | &K - Enter Approved Vendors | t7bmk.rwn | T7BMK.DFM | BKAPVEND, BKARCUST, BKSBVEND, BKSYMSTR |
| BML | &L - Enter Approved Manufacturers | t7bml.rwn | T7BML.DFM | BKARCUST, BKSBMFG, BKSYMSTR, BKICMSTR |
| BMM | &M - Bill of Materials Defaults | T7DSBOM.RWN | STUB.DFM | ISDROP, BKSYHELP, DBAHLPID, ISIS |
| BMN | &N - BOM Availability - Tree View | BOMTREE.RWN |  | BKSYHELP, DBAHLPID, BKPSUSER, ISDRILL |
| BMO | &O - Create/Edit BOM - Tree View | EDITBOMTREE.RWN |  | BKSYHELP, DBAHLPID, BKPSUSER, ISDRILL |
| BMP | &P - Print BOM Pick List | T7BMP.RWN | T7BMP.DFM | BKICMSTR, BKSYMSTR, BKYSMSTR, BKBMMSTR |
| BMQ | &Q - Roll Up Where Used | T7BMQ.RWN | T7BMQ.DFM | BKICMSTR, BKBMMSTR, MTICMSTR, BKSYHELP |
| BMR | &R - Print BOM for Quoting | T7BMR.RWN | T7BMR.DFM | BKSYMSTR, BKICMSTR, BKARINVL, ISBUILD |

## Module: BU

| Code | Label | Program | DFM | Key Tables |
|------|-------|---------|-----|------------|
| BUTTONS | Accounting Defaults | AD |  |  |
| BUTTONS | Accounting Maintenance | AM |  |  |
| BUTTONS | Accounts Payable | AP |  |  |
| BUTTONS | Accounts Receivable | AR |  |  |
| BUTTONS | Bill of Materials | BM |  |  |
| BUTTONS | Commissions | CS |  |  |
| BUTTONS | Contact Master | CM |  |  |
| BUTTONS | Contract Review | CR |  |  |
| BUTTONS | Data Collection | DC |  |  |
| BUTTONS | Data Exchange | DE |  |  |
| BUTTONS | Estimates | ES |  |  |
| BUTTONS | Features and Options | FO |  |  |
| BUTTONS | Fixed Assets | FA |  |  |
| BUTTONS | General Ledger | GL |  |  |
| BUTTONS | Hand Held Programs | HH |  |  |
| BUTTONS | International Module | IM |  |  |
| BUTTONS | Inventory | IN |  |  |
| BUTTONS | Job Costing | JC |  |  |
| BUTTONS | Lot Control | LC |  |  |
| BUTTONS | MRP | MR |  |  |
| BUTTONS | New Programs | NE |  |  |
| BUTTONS | Password Security | PS |  |  |
| BUTTONS | Payroll | PR |  |  |
| BUTTONS | Physical Inventory | PI |  |  |
| BUTTONS | Purchase Orders | PO |  |  |
| BUTTONS | Quality Control | QC |  |  |
| BUTTONS | Queries & Reports | QU |  |  |
| BUTTONS | Query & Report Setup | SU |  |  |
| BUTTONS | RMA | RM |  |  |
| BUTTONS | Routings | RO |  |  |
| BUTTONS | Sales Analysis | SA |  |  |
| BUTTONS | Sales Orders | SO |  |  |
| BUTTONS | Scheduling | SH |  |  |
| BUTTONS | Serial Control | SC |  |  |
| BUTTONS | Service and Repair | SR |  |  |
| BUTTONS | System Configuration | TAS |  |  |
| BUTTONS | System Defaults | SD |  |  |
| BUTTONS | System Maintenance | SM |  |  |
| BUTTONS | User Settings | US |  |  |
| BUTTONS | Utilities | UT |  |  |
| BUTTONS | Warehouse Control | WC |  |  |
| BUTTONS | Work Orders | WO |  |  |

## Module: CM

| Code | Label | Program | DFM | Key Tables |
|------|-------|---------|-----|------------|
| CMA | &A - Enter Contact Accounts | t7cma.rwn | T7CMA.DFM | BKARCUST, ISTAXGRP, BKCMACCL, BKCMACTD |
| CMB | &B - Contact Account Reports | *(group)* |  |  |
| CMBB | &B - Print Accounts Listing & Labels | t7cmbb.rwn | T7CMBB.DFM | BKCMMHST, BKARCUST, BKCMACTD, BKCMACCL |
| CMBC | &C - Print Reminders | T7REMINDRPT.RWN | T7REMINDRPT.DFM | BKSYMSTR, ISREMIND, BKARCUST, BKCMACCN |
| CMBF | &F - Print Notes | evonotesrpt.rwn | EVONOTESRPT.DFM | BKSYMSTR, ISNOTES, BKARCUST, BKAPVEND |
| CMC | &C - CRM Dashboard | t7jcrm.rwn | T7JCRM.DFM | ISBUILD, FILEDICT, BKSYHELP, DBAHLPID |
| CMJ | &J - Change Account Codes | t7cmj.rwn | STUB.DFM | MKAHIST, ISNOTES, BKSYHELP, DBAHLPID |
| CMK | &K - Add Customers to Account File | t7cmk.rwn | T7CMK.DFM | BKARCUST, BKSYHELP, DBAHLPID, ISIS |
| CMM | &M - Contact Manager Defaults | T7DSCM.RWN | STUB.DFM | ISDROP, BKSYHELP, DBAHLPID, ISIS |

## Module: CR

| Code | Label | Program | DFM | Key Tables |
|------|-------|---------|-----|------------|
| CRA | &A - Assign Departments to SO | T7SOREVUADMIN.RWN | STUB.DFM | BKARINV, ISCTREVU, ISSOREVU, BKSYHELP |
| CRB | &B - Enter SO Approvals | T7SOREVU.RWN | T7SOREVU.DFM | BKARINV, ISCTREVU, ISSOREVU, BKSYHELP |

## Module: CS

| Code | Label | Program | DFM | Key Tables |
|------|-------|---------|-----|------------|
| CSA | &A - Enter Salespersons | T7CSA.RWN | T7CSA.DFM | BKPRAGNT, BKPRSALE, BKPRMSTR, BKAPVEND |
| CSB | &B - View Salespersons Info | t7csb.rwn | T7CSB.DFM | BKPRSALE, BKPRMSTR, BKPRAGNT, BKSYHELP |
| CSC | &C - Print Salespersons Info | t7csc.rwn | T7CSC.DFM | BKPRSALE, BKPRMSTR, BKSYHELP, DBAHLPID |
| CSD | &D - Transfer Sales Commissions | t7csd.rwn | STUB.DFM | MKAHIST, BKPRMSTR, BKSYHELP, DBAHLPID |
| CSE | &E - Print Commission Detail | t7cse.rwn | T7CSE.DFM | BKICMSTR, BKPRSALE, BKARINV, BKARINVL |
| CSF | &F - Print Commission Summary | t7csf.rwn | T7CSF.DFM | BKPRSALE, BKARINV, BKARINVL, BKSYHELP |
| CSG | &G - Enter Sales Rep Links | T7replnk.rwn | T7REPLNK.DFM | ISREPLNK, BKPRSALE, BKARCUST, BKICMSTR |
| CSH | &H - Import Sales Rep Links | T7CSDE.RWN | T7CSDE.DFM | ISREPLNK, BKPRSALE, BKICMSTR, BKARCUST |
| CSK | &K - Enter Price Code Commissions | t7csk.rwn | STUB.DFM | MKAHIST, DBAHLPID, TASCOLOR, ISDRILL |
| CSL | &L - Print Price Code Commissions | t7csl.rwn | STUB.DFM | MKAHIST, DBAHLPID, TASCOLOR, ISDRILL |
| CSM | &M - Enter Contract Commissions | t7csm.rwn | STUB.DFM | MKAHIST, DBAHLPID, TASCOLOR, ISDRILL |
| CSN | &N - Print Contract Commissions | t7csn.rwn | STUB.DFM | MKAHIST, DBAHLPID, TASCOLOR, ISDRILL |
| CSO | &O - Print Commissions Earned Detail | t7cso.rwn | T7CSO.DFM | BKSYMSTR, BKPRCOMM, BKPRSALE, BKPRAGNT |
| CSP | &P - Print Commissions Due Summary | t7csp.rwn | T7CSP.DFM | BKPRSALE, BKARINV, BKARINVL, BKSYHELP |
| CSQ | &Q - Commission Year End Routine | t7csq.rwn | T7FIX.DFM | BKPRSALE, BKSYHELP, DBAHLPID, ISIS |
| CSR | &R - Sales Commission Defaults | T7DSCS.RWN | STUB.DFM | ISDROP, BKSYHELP, DBAHLPID, ISIS |

## Module: DC

| Code | Label | Program | DFM | Key Tables |
|------|-------|---------|-----|------------|
| DCA | &A - Enter Labor/Production | t7dca.rwn | T7DCA.DFM | BKDCLAB, WORKORD, BKPRMSTR, ISWOEX |
| DCB | &B - Enter Production Only | t7dcb.rwn | T7DCB.DFM | BKICMSTR, BKDCLAB, BKPRMSTR, WORKORD |
| DCC | &C - Enter Labor Only | t7dcc.rwn | STUB.DFM | MKAHIST |
| DCD | &D - Print Labor Status | t7dcd.rwn | T7DCD.DFM | BKSYMSTR, BKPRMSTR, BKPRINFO, BKCPMSTR |
| DCE | &E - Print Labor Tickets | t7dce.rwn | T7DCE.DFM | WOROUT, WORKORD, BKSYHELP, DBAHLPID |
| DCF | &F - Print Employee Tickets | t7dcf.rwn | T7DCF.DFM | BKPRMSTR, BKSYHELP, DBAHLPID, ISIS |
| DCG | &G - Edit Labor Transactions | t7dcg.rwn | T7DCG.DFM | BKDCLAB, WORKORD, MACHINE, TASCOLOR |
| DCH | &H - Post Labor Transactions | t7dch.rwn | T7DCH.DFM | BKDCLAB, BKDCCFG, BKPRMSTR, WORKORD |
| DCI | &I - Work Order Inquiry | T7WOT.rwn | STUB.DFM | MKAHIST, WORKORD, BKSYHELP, DBAHLPID |
| DCJ | &J - Data Collection Defaults | T7DSDC.RWN | STUB.DFM | ISDROP, BKSYHELP, DBAHLPID, ISIS |
| DCK | &K - Archive Shift Data | T7DCK.RWN | T7DCK.DFM | BKDCLAB, BKPRMSTR, BKSYHELP, DBAHLPID |
| DCL | &L - Shift Clock In/Out | T7DCL.RWN | T7DCL.DFM | BKPRMSTR, MKAHIST, BKDCLAB, BKPRINFO |
| DCM | &M - Employee Dashboard | T7DCM.RWN | T7DCM.DFM | BKPRMSTR, BKDCLAB, BKSYHELP, DBAHLPID |
| DCN | &N - Generate Holiday Shift Records | T7DCN.RWN | T7DCN.DFM | BKPRMSTR, CALENDAR, BKDCLAB, CLASMSTR |

## Module: DE

| Code | Label | Program | DFM | Key Tables |
|------|-------|---------|-----|------------|
| DEA | &A - Export Data | sqlexport.rwn |  | BKSYHELP, DBAHLPID, BKPSUSER, ISDRILL |
| DEB | &B - Import Inventory | *(group)* |  |  |
| DEBA | &A - Generate Import Header | T7DEBA.RWN | STUB.DFM | FILEDICT, FILEKEY, FILELOC, BKSYHELP |
| DEBB | &B - Import Inventory | T7DEBB.RWN | STUB.DFM | FILEDICT, FILEKEY, FILELOC, BKSYHELP |
| DEBC | &C - Inventory Error Report | T7DEBC.RWN | STUB.DFM | FILEDICT, FILEKEY, FILELOC, BKSYHELP |
| DEBD | &D - Edit Imported Inventory | T7DEBD.RWN | STUB.DFM | BKSYHELP, DBAHLPID, MKAHIST, BKSYHELP |
| DEBE | &E - Transfer Inventory to Master Files | T7DEBE.RWN | STUB.DFM | BKSYHELP, DBAHLPID, MKAHIST, BKSYHELP |
| DEC | &C - Import Bills of Material | *(group)* |  |  |
| DECA | &A - Generate Import Header | T7DECA.RWN | STUB.DFM | BKSYHELP, DBAHLPID, MKAHIST, BKSYHELP |
| DECB | &B - Import Bills of Material | T7DECB.RWN | STUB.DFM | BKSYHELP, DBAHLPID, MKAHIST, BKSYHELP |
| DECC | &C - Bills of Material Error Report | T7DECC.RWN | STUB.DFM | BKSYHELP, DBAHLPID, MKAHIST, BKSYHELP |
| DECD | &D - Edit Imported Bills of Material | T7DECD.RWN | STUB.DFM | BKSYHELP, DBAHLPID, MKAHIST, BKSYHELP |
| DECE | &E - Transfer Bills of Material to Master Files | T7DECE.RWN | STUB.DFM | BKSYHELP, DBAHLPID, MKAHIST, BKSYHELP |
| DED | &D - Import Routings | *(group)* |  |  |
| DEDA | &A - Generate Import Header | T7DEDA.RWN | STUB.DFM | BKSYHELP, DBAHLPID, MKAHIST, BKSYHELP |
| DEDB | &B - Import Routings | T7DEDB.RWN | STUB.DFM | BKSYHELP, DBAHLPID, MKAHIST, BKSYHELP |
| DEDC | &C - Routings Error Report | T7DEDC.RWN | STUB.DFM | BKSYHELP, DBAHLPID, MKAHIST, BKSYHELP |
| DEDD | &D - Edit Imported Routings | T7DEDD.RWN | STUB.DFM | BKSYHELP, DBAHLPID, MKAHIST, BKSYHELP |
| DEDE | &E - Transfer Routings to Master Files | T7DEDE.RWN | STUB.DFM | BKSYHELP, DBAHLPID, MKAHIST, BKSYHELP |
| DEE | &E - Import Customers | *(group)* |  |  |
| DEEA | &A - Generate Import Header | T7DEEA.RWN | STUB.DFM | BKSYHELP, DBAHLPID, MKAHIST, BKSYHELP |
| DEEB | &B - Import Customers | T7DEEB.RWN | STUB.DFM | BKSYHELP, DBAHLPID, MKAHIST, BKSYHELP |
| DEEC | &C - Customer Error Report | T7DEEC.RWN | STUB.DFM | BKSYHELP, DBAHLPID, MKAHIST, BKSYHELP |
| DEED | &D - Edit Imported Customers | T7DEED.RWN | STUB.DFM | BKSYHELP, DBAHLPID, MKAHIST, BKSYHELP |
| DEEE | &E - Transfer Customers to Master Files | T7DEEE.RWN | STUB.DFM | BKSYHELP, DBAHLPID, MKAHIST, BKSYHELP |
| DEF | &F - Import Vendors | *(group)* |  |  |
| DEFA | &A - Generate Import Header | T7DEFA.RWN | STUB.DFM | BKICMSTR, BKBMMSTR, ROUTING, BKARCUST |
| DEFB | &B - Import Vendors | T7DEFB.RWN | STUB.DFM | BKICMSTR, BKBMMSTR, ROUTING, BKARCUST |
| DEFC | &C - Vendor Error Report | T7DEFC.RWN | STUB.DFM | BKICMSTR, BKBMMSTR, ROUTING, BKARCUST |
| DEFD | &D - Edit Imported Vendors | T7DEFD.RWN | STUB.DFM | BKSYHELP, DBAHLPID, MKAHIST, BKARCUST |
| DEFE | &E - Transfer Vendors to Master Files | T7DEFE.RWN | STUB.DFM | BKSYHELP, DBAHLPID, MKAHIST, BKARCUST |
| DEG | &G - Import Chart of Accounts | *(group)* |  |  |
| DEGA | &A - Generate Import Header | T7DEGA.RWN | STUB.DFM | BKSYHELP, DBAHLPID, ISIS, MKAHIST |
| DEGB | &B - Import Chart of Accounts | T7DEGB.RWN | STUB.DFM | BKSYHELP, DBAHLPID, ISIS, MKAHIST |
| DEGC | &C - Chart of Accounts Error Report | T7DEGC.RWN | STUB.DFM | BKSYHELP, DBAHLPID, ISIS, MKAHIST |
| DEGD | &D - Edit Imported Chart of Accoutns | T7DEGD.RWN | STUB.DFM | BKSYHELP, DBAHLPID, MKAHIST, MKAHIST |
| DEGE | &E - Transfer Chart of Accounts to Master Files | T7DEGE.RWN | STUB.DFM | BKSYHELP, DBAHLPID, MKAHIST, MKAHIST |
| DEH | &H - Global Field Change | T7DEK.RWN | T7DEK.DFM | BKICMSTR, MTICMSTR, BKBMMSTR, ROUTING |
| DEI | &I - Erase Files | t7del.rwn | T7DEL.DFM | BKSYHELP, DBAHLPID, ISIS, MKAHIST |
| DEJ | &J - Import and Post Labor | *(group)* |  |  |
| DEJA | &A - Create Import Header | t7deja.rwn | STUB.DFM | BKSYHELP, DBAHLPID, ISIS, MKAHIST |
| DEJB | &B - Import Labor | t7dejb.rwn | STUB.DFM | BKSYHELP, DBAHLPID, ISIS, MKAHIST |
| DEJC | &C - Imported Labor Error Report | t7dejc.rwn | STUB.DFM | BKSYHELP, DBAHLPID, ISIS, MKAHIST |
| DEJD | &D - Edit Imported Labor | t7dejd.rwn | STUB.DFM | BKSYHELP, DBAHLPID, MKAHIST, MKAHIST |
| DEJE | &E - Transfer Imported Labor | t7deje.rwn | STUB.DFM | BKSYHELP, DBAHLPID, MKAHIST, MKAHIST |
| DEK | &K - Import and Post Material Issues | t7dejh.rwn | T7DEJH.DFM | WOMAT, WORKORD, WOBOM, BKICMSTR |
| DEL | &L - Import and Post Finished Production | T7WOP.RWN | T7WOP.DFM | WORKORD, BKYSMSTR, WOBOM, BKICMSTR |
| DEM | &M - Import Physical Inventory Count | T7PIC.RWN | T7PIC.DFM | BKPIPHYS, BKYSMSTR, BKSYMSTR, BKPIMSTR |
| DEP | &P - EDI Interface | *(group)* |  |  |
| DEPB | &B - Import EDI Orders | t7depb.rwn | T7DEPB.DFM | BKARINV, BKYSMSTR, BKEDMSTR, BKEDIDUN |
| DEPC | &C - Edit EDI Orders | t7depc.rwn | STUB.DFM | MKAHIST, BKYSMSTR, BKEDMSTR, BKEDIDUN |
| DEPD | &D - Convert EDI Orders to Sales Orders | t7depd.rwn | T7DEPD.DFM | BKARINVL, BKICLOCM, BKARINV, BKYSMSTR |
| DEPE | &E - Export EDI Invoice/Acknowledgement | t7depe.rwn | T7DEPE.DFM | BKARINV, BKARCUST, ISAREX, ISBUILD |
| DEPF | &F - Export EDI ASN | t7depf.rwn | T7DEPF.DFM | BKARCUST, BKARINV, ISAREX, BKEDMSTR |
| DEPH | &H - EDI Error Report | t7deph.rwn | T7DEPH.DFM | BKSYMSTR, BKARINV, BKICREF, BKARINVL |
| DEQ | &Q - Import open Accounts Receivable | t7deq.rwn | T7DEQ.DFM | BKARINVT, BKARCUST, BKART, BKARTNOT |
| DER | &R - Import open Accounts Payable | t7der.rwn | T7DER.DFM | BKAPINVT, ISTERMS, BKSYHELP, DBAHLPID |
| DET | &T - Import Sales Orders | *(group)* |  |  |
| DETA | A - FTP Web Storefront Orders | T7DET.RWN | T7DET.DFM | BKYSMSTR, ISMCF, ISBANKS, BKARCUST |
| DETB | B - SHOPIFY Web Storefront Orders | T7DETB.RWN | T7DETB.DFM | BKYSMSTR, BKSYMSTR, ISMCF, BKARCUST |
| DETC | C - File Web Storefront Orders | T7DETC.RWN | STUB.DFM |  |
| DEU | &U - Upload Stock Balance to Web Storefront | J7BEFWEBINV.RWN | STUB.DFM |  |

## Module: ES

| Code | Label | Program | DFM | Key Tables |
|------|-------|---------|-----|------------|
| ESA | &A - Enter Estimates | t7esa.rwn | STUB.DFM | MKAHIST, BKSYHELP, DBAHLPID, ISIS |
| ESB | &B - Print Customer Quotes | T7ESB.RWN | T7ESB.DFM | MTICMSTR, BKYSMSTR, BKARINV, BKARCUST |
| ESC | &C - Print Estimate Cost Rollup | t7esc.rwn | T7ESC.DFM | ISESTDTL, BKARINV, BKARCUST, BKICMSTR |
| ESD | &D - Quick Estimate | T7EST.RWN | T7EST.DFM | ISESTDTL, BKARINVL, MTEXCHG, MTICMSTR |
| ESE | &E - Convert Estimates | T7ese.RWN | T7ESE.DFM | ISESTDTL, BKYSMSTR, BKARINV, WORKORD |
| ESH | &H - Enter Material Costs | T7ESH.RWN | T7ESH.DFM | BKMATCST, BKICMSTR, MTICMSTR, BKAPVEND |
| ESI | &I - Print Material Costs | t7esi.rwn | T7ESI.DFM | BKICMSTR, BKMATCST, BKSYHELP, DBAHLPID |
| ESJ | &J - Estimating Defaults | T7DSEST.RWN | STUB.DFM | ISDROP, BKSYHELP, DBAHLPID, ISIS |
| ESK | &K - Update Estimating Inventory from Production | T7IC2EST.RWN | T7IC2EST.DFM | BKICMSTR, MTICMSTR |
| ESL | &L - Edit Estimating Inventory | T7ESL.RWN | STUB.DFM | MKAHIST, BKMATCST, BKSYHELP, DBAHLPID |
| ESM | &M - Estimating Inventory Inquiry | T7ESM.RWN | STUB.DFM | MKAHIST, BKMATCST, BKSYHELP, DBAHLPID |

## Module: FA

| Code | Label | Program | DFM | Key Tables |
|------|-------|---------|-----|------------|
| FAA | &A - Enter Assets | T7FAA.RWN | T7FAA.DFM | ISFXASST, ISFXATRN, BKGLCOA, BKSYHELP |
| FAB | &B - Post Depreciation | T7FAB.RWN | T7FAB.DFM | ISFXATRN, ISFXASST, BKGLCOA, BKSYMSTR |
| FAC | &C - List Depreciation Transactions | UT7GFAC.RWN |  | BKLUGRID, BKSYHELP, DBAHLPID, BKPSUSER |
| FAD | &D - List Assets | UT7GFAD.RWN |  | BKLUGRID, BKSYHELP, DBAHLPID, BKPSUSER |
| FAE | &E - Import Assets | T7FAE.RWN | T7FAE.DFM | ISFXASST, BKGLCOA, BKSYHELP, DBAHLPID |

## Module: FO

| Code | Label | Program | DFM | Key Tables |
|------|-------|---------|-----|------------|
| FOA | &A - Set up Features and Options | T7FOA.RWN | STUB.DFM | FILELOC, FILEDICT, BKSYHELP, DBAHLPID |
| FOB | &B - Print Features and Options | T7FOB.RWN | STUB.DFM | FILELOC, FILEDICT, BKSYHELP, DBAHLPID |
| FOC | &C - Enter Option Prices | T7FOC.RWN | T7FOC.DFM | BKBMMSTR, BKICMSTR, MTICMSTR, BKSYHELP |
| FOD | &D - Print Option Prices | T7FOD.RWN | T7FOD.DFM | BKICMSTR, MTICMSTR, BKBMMSTR, BKICLOCM |
| FOE | &E - Print Option Where Used | T7FOE.RWN | T7FOE.DFM | BKICMSTR, MTICMSTR, BKBMMSTR, BKICLOCM |
| FOF | &F - Feature and Option Defaults | T7DSFO.RWN | STUB.DFM | ISDROP, BKSYHELP, DBAHLPID, ISIS |
| FOG | &G - Configure Item | EvoFNO.RWN | EVOFNO.DFM | ISFOHEAD, ISFOLINE, BKICMSTR, BKBMMSTR |

## Module: GL

| Code | Label | Program | DFM | Key Tables |
|------|-------|---------|-----|------------|
| GLA | &A - View Chart of Accounts | T7GLA.RWN | T7GLA.DFM | BKGLCOA, ISGLCOA, ISGLDATE, ISGLNBGT |
| GLB | &B - Enter/Post General Journal Trxns | t7glb.rwn | T7GLB.DFM | BKGLGJRN, BKYSMSTR, ISBANKS, ISAPPROJ |
| GLC | &C - Print GL Transactions | t7glc.rwn | T7GLC.DFM | BKYSMSTR, BKGLCOA, BKGLTRAN, BKARCUST |
| GLD | &D - Print Journals | T7GLD.RWN | T7GLD.DFM | BKSYMSTR, BKYSMSTR, BKGLTRAN, BKARCUST |
| GLE | &E - Print Detailed Trial Balance | t7gle.rwn | T7GLE.DFM | BKYSMSTR, ISGLDATE, BKSYMSTR, BKGLCOA |
| GLF | &F - Print Financial Statements | t7glf.rwn | T7GLF.DFM | BKSYMSTR, BKGLSTMT, ISGLDATE, BKGLCOA |
| GLG | &G - Print GL Code and Description | t7glg.rwn | T7GLG.DFM | BKSYMSTR, BKGLCOA, BKSYHELP, DBAHLPID |
| GLH | &H - Print Chart of Accounts | T7GLH.RWN | T7GLH.DFM | BKSYMSTR, BKGLCOA, ISGLCOA, ISGLNBGT |
| GLI | &I - Print Check Register | t7gli.rwn | T7GLI.DFM | BKSYMSTR, BKGLCHK, ISBANKS, BKAPVEND |
| GLJ | &J - Reconcile Check Register | t7glj.rwn | T7GLJ.DFM | ISBANKS, BKGLCHK, BKGLCOA, BKSYMSTR |
| GLK | &K - Transfer Bank Account Funds | t7glk.rwn | T7GLK.DFM | BKYSMSTR, ISBANKS, BKGLCOA, BKAPDESC |
| GLL | &L - Credit Card Reconciliation | T7GLL.RWN | T7GLL.DFM | BKGLCHK, ISBANKS, BKAPCHKF, BKAPINVL |
| GLN | &N - Print Custom Statements | t7gln.rwn | T7GLN.DFM | BKSYMSTR, ISGLDATE, BKGLFSTL, BKGLCOA |
| GLO | &O - Print/Post General Ledger Batches | t7glo.rwn | T7GLO.DFM | BKSYMSTR, BKYSMSTR, BKGLTRAN, BKGLCOA |
| GLP | &P - Edit General Ledger Batch Entries | t7glp.rwn | T7GLP.DFM | BKGLTRAN, BKGLCOA, BKSYMSTR, BKSYHELP |
| GLQ | &Q - Enter Payroll Checks | t7glq.rwn | T7GLQ.DFM | BKGLGJRN, BKGLCOA, BKSYMSTR, ISBANKS |
| GLR | &R - Business Status | T7JBS.rwn | T7JBS.DFM | BKSYHELP, DBAHLPID, ISIS, ISLOG |
| GLS | &S - View Journal Notes | t7gls.rwn | T7GLS.DFM | ISNOTES, BKGLGJRN, BKSYHELP, DBAHLPID |
| GLT | &T - Import GL Transactions | T7GLT.RWN | T7GLT.DFM | BKGLTRAN, ISBANKS, BKGLCOA, BKGLCHK |

## Module: GR

| Code | Label | Program | DFM | Key Tables |
|------|-------|---------|-----|------------|
| GROUPS | Accounting | AD |  |  |
| GROUPS | Accounting | AM |  |  |
| GROUPS | Accounting | AP |  |  |
| GROUPS | Accounting | FA |  |  |
| GROUPS | Accounting | GL |  |  |
| GROUPS | Hand Held | HH |  |  |
| GROUPS | Items | BM |  |  |
| GROUPS | Items | FO |  |  |
| GROUPS | Items | IN |  |  |
| GROUPS | Items | LC |  |  |
| GROUPS | Items | PI |  |  |
| GROUPS | Items | RO |  |  |
| GROUPS | Items | SC |  |  |
| GROUPS | Items | WC |  |  |
| GROUPS | Mfg | DC |  |  |
| GROUPS | Mfg | ES |  |  |
| GROUPS | Mfg | JC |  |  |
| GROUPS | Mfg | MR |  |  |
| GROUPS | Mfg | PO |  |  |
| GROUPS | Mfg | QC |  |  |
| GROUPS | Mfg | SH |  |  |
| GROUPS | Mfg | WO |  |  |
| GROUPS | Pay Link | PL |  |  |
| GROUPS | Payroll | PR |  |  |
| GROUPS | Queries | QU |  |  |
| GROUPS | Queries | SU |  |  |
| GROUPS | Sales | AR |  |  |
| GROUPS | Sales | CM |  |  |
| GROUPS | Sales | CR |  |  |
| GROUPS | Sales | CS |  |  |
| GROUPS | Sales | RM |  |  |
| GROUPS | Sales | SA |  |  |
| GROUPS | Sales | SO |  |  |
| GROUPS | Sales | SR |  |  |
| GROUPS | Settings | US |  |  |
| GROUPS | System Mgr | DE |  |  |
| GROUPS | System Mgr | IM |  |  |
| GROUPS | System Mgr | PS |  |  |
| GROUPS | System Mgr | SD |  |  |
| GROUPS | System Mgr | SM |  |  |
| GROUPS | System Mgr | TAS |  |  |
| GROUPS | System Mgr | UT |  |  |

## Module: HH

| Code | Label | Program | DFM | Key Tables |
|------|-------|---------|-----|------------|
| HHA | &A - Scan & Ship | t7hhssoe.rwn | T7HHSSOE.DFM | ISSOBOX, BKARINV, BKARINVL, MTICMSTR |
| HHB | &B - Print Labels | T7HHinga.rwn | T7HHINGA.DFM | BKAPPO, BKYSMSTR, BKAPPOL, BKICMSTR |
| HHC | &C - Issue Materials | T7HHWOG.RWN | T7HHWOG.DFM | BKSHORT, BKYSMSTR, BKSYMSTR, WOMAT |
| HHD | &D - Enter Finished Production | T7HHWOP.RWN | T7HHWOP.DFM | BKYSMSTR, BKSYMSTR, WORKORD, BKICMSTR |
| HHE | &E - Enter Physical Counts | T7HHPIC.RWN | T7HHPIC.DFM | BKYSMSTR, BKSYMSTR, BKPIMSTR, BKPRMSTR |
| HHF | &F - Enter Labor | T7HHDCA.RWN | T7HHDCA.DFM | BKDCLAB, BKDCSHFT, BKYSMSTR, BKPRMSTR |
| HHG | &G - Receive PO | T7HHPOC.RWN | T7HHPOC.DFM | BKSBMFG, BKAPPO, MTICMSTR, ISDIGSIG |
| HHH | &H - Enter Shipping Information | J7HHLITN.RWN | STUB.DFM |  |
| HHI | &I - Paperless Shop Floor Tracking | t7dcpsf.rwn | T7DCPSF.DFM | BKDCLAB, WOROUT, WORKORD, BKICMSTR |
| HHJ | &J - Print WO Label | t7hhwolabel.rwn | T7HHWOLABEL.DFM | WORKORD, BKICMSTR, MTICMSTR, WORECV |
| HHK | &K - Transfer Inventory | t7hhinlj.rwn | T7HHINLJ.DFM | BKICLOCM, BKYSMSTR, BKICMSTR, SERIAL |
| HHL | &L - Multi-User Paperless Shop Floor | t7paperless.rwn | T7PAPERLESS.DFM | WORKORD, MTICMSTR, BKICMSTR, WOROUT |
| HHM | &M - Issue Scrap Component | t7hhwoscrap.rwn | T7HHWOSCRAP.DFM | BKSHORT, BKYSMSTR, WOBOM, BKICMSTR |

## Module: IM

| Code | Label | Program | DFM | Key Tables |
|------|-------|---------|-----|------------|
| IMA | &A - International Configuration | T7DSIM.RWN | STUB.DFM | ISDROP, BKSYHELP, DBAHLPID, ISIS |
| IMB | &B - Enter Multiple Currencies | t7imb.rwn | T7IMB.DFM | ISMCF, BKSYMSTR, ISIS, BKSYHELP |
| IMC | &C - Enter Currency Exchange Rates | t7imc.rwn | T7IMC.DFM | ISMCR, ISMCF, BKSYHELP, DBAHLPID |
| IMD | &D - Enter Landed Cost Defaults | t7imd.rwn | T7IMD.DFM | ISLANDF, BKSYHELP, DBAHLPID, BKYSMSTR |
| IME | &E - Enter Landed Cost Duty Codes | t7ime.rwn | T7IME.DFM | ISDUTY, BKSYHELP, DBAHLPID, ISIS |
| IMF | &F - Enter Landed Cost Customs Fees | t7imf.rwn | T7IMF.DFM | ISBROKER, BKSYHELP, DBAHLPID, ISIS |
| IMH | &H - International Defaults | T7DSIM.RWN | STUB.DFM | ISDROP, BKSYHELP, DBAHLPID, ISIS |

## Module: IN

| Code | Label | Program | DFM | Key Tables |
|------|-------|---------|-----|------------|
| INA | &A - Inventory Inquiry | t7ina.rwn | T7INA.DFM | BKICMSTR, CLASMSTR, MTICMSTR, ISICMSTR |
| INB | &B - Enter Inventory | T7inb.rwn | T7INB.DFM | BKICMSTR, MTICMSTR, CLASMSTR, ISICMSTR |
| INC | &C - Enter Inventory Adjustments | t7inc.rwn | T7INC.DFM | INVTXN, BKICMSTR, BKICLOC, MTICMSTR |
| IND | &D - Print Reorder Report | t7ind.rwn | T7IND.DFM | BKSYMSTR, BKICMSTR, BKYSMSTR, BKICLOCM |
| INE | &E - Print Inventory Transactions | t7ine.rwn | T7INE.DFM | BKSYMSTR, BKYSMSTR, MKAHIST, BKICMSTR |
| INF | &F - Print Inventory Value | t7inf.rwn | T7INF.DFM | BKYSMSTR, MTICMSTR, CLASMSTR, BKARCUST |
| ING | &G - Print Inventory Labels | t7ing.rwn | T7ING.DFM | MTICMSTR, BKPSUSER, BKPRMSTR, BKAPPO |
| INH | &H - Print Inventory Listing | t7inh.rwn | T7INH.DFM | BKICMSTR, MTICMSTR, BKYSMSTR, BKSYMSTR |
| INI | &I - Print Inventory General Info | t7ini.rwn | T7INI.DFM | MTICMSTR, BKICMSTR, BKARCUST, BKAPVEND |
| INJ | &J - Print Physical Check | t7inj.rwn | T7INJ.DFM | BKSYMSTR, ISBUILD, BKICMSTR, MTICMSTR |
| INK | &K - Adjust Physical Levels | t7ink.rwn | T7INK.DFM | BKICMSTR, MTICMSTR, BKYSMSTR, BKICLOC |
| INL | &L - Inventory Maintenance Programs | *(group)* |  |  |
| INLA | &A - Enter Standard Costs | t7inla.rwn | T7INLA.DFM | BKICMSTR, MTICMSTR, ISICMSTR, BKSYHELP |
| INLB | &B - Enter/Assign Locations | t7inlb.rwn | T7INLB.DFM | BKICLOCM, BKICMSTR, BKICLOC, FILELOC |
| INLC | &C - Enter Customer Cross-Reference | t7inlc.rwn | T7INLC.DFM | BKICMSTR, BKICREF, BKARCUST, FILELOC |
| INLD | &D - Print Customer Cross-Reference | t7inld.rwn | T7INLD.DFM | BKSYMSTR, BKICREF, BKICMSTR, MTICMSTR |
| INLE | &E - Update Material Standard Costs | t7inle.rwn | T7INLE.DFM | BKICMSTR, MTICMSTR, BKAPPOL, BKAPPO |
| INLH | &H - Edit FIFO/LIFO Buckets | t7inlh.rwn | T7INLH.DFM | BKICMSTR, MTICMSTR, BKYSMSTR, DBAFIFO |
| INLI | &I - Change Costing Method | t7inli.rwn | T7INLI.DFM | BKYSMSTR, BKSYMSTR, BKICMSTR, BKICLOC |
| INLJ | &J - Transfer Inventory | t7inlj.rwn | T7INLJ.DFM | BKICMSTR, SERIAL, LOT, ISBINLOC |
| INLK | &K - Inventory Exceptions Report | t7inlk.rwn | T7INLK.DFM | BKSYMSTR, BKYSMSTR, BKICMSTR, MTICMSTR |
| INLL | &L - Inactive BOM Component Report | t7inll.rwn | T7INLL.DFM | BKSYMSTR, MTICMSTR, BKICMSTR, BKBMMSTR |
| INLM | &M - Batch Location Transfers | T7INLM.RWN | T7INLM.DFM | BKICMSTR, INVTXN, MTICMSTR, LOT |
| INLN | &N - Copy Item Number | t7inln.rwn | T7INLN.DFM | BKICMSTR, BKYSMSTR, BKICLOC, ISICMSTR |
| INLO | &O - Inactive Item Utility | t7inlo.rwn | T7INLO.DFM | BKACTRPT, BKICMSTR, BKSYMSTR, BKYSMSTR |
| INLQ | &Q - Enter Inspection & Test Procedures | t7inlq.rwn | T7INLQ.DFM | ISITP, BKSYMSTR, ISNOTES, ISLINKS |
| INLR | &R - Intercompany Inventory Transfer | T7INLR.RWN | T7INLR.DFM | BKICMSTR, ISMCF, FILELOC, BKSYMSTR |
| INLS | &S - Rebuild Stock Status | t7inls.rwn | T7INLS.DFM | BKICMSTR, MTICMSTR, BKSYHELP, DBAHLPID |
| INLT | &T - Reset Cycle Code | T7INLT.RwN | T7INLT.DFM | BKSYMSTR, MTICMSTR, BKICMSTR, INVTXN |
| INLU | &U - Item Number Configurator | T7ITMCFG.RWN | T7ITMCFG.DFM | ISSERCNT, BKICMSTR, BKSYHELP, DBAHLPID |
| INM | &M - Summary Reorder Report | T7INM.RWN | T7INM.DFM | BKICMSTR, MTICMSTR, BKYSMSTR, WORKORD |
| INN | &N - Month End Reports | *(group)* |  |  |
| INNA | &A - Print Month End Inventory Costing | t7inna.rwn | T7INNA.DFM | BKSYMSTR, CLASMSTR, INVTXN, BKICMSTR |
| INNB | &B - Print Shipments Costing | t7innb.rwn | T7INNB.DFM | BKSYMSTR, CLASMSTR, INVTXN, BKICMSTR |
| INNC | &C - Print Closed Work Orders Costing | t7innc.rwn | T7INNC.DFM | BKSYMSTR, WORKORD, MTICMSTR, BKICMSTR |
| INND | &D - Print Inventory to GL Exceptions | t7innd.rwn | T7INND.DFM | BKSYMSTR, BKYSMSTR, INVTXN, BKICMSTR |
| INO | &O - User Defined Inventory Transactions | t7ino.rwn | T7INO.DFM | BKACTRPT, INVTXN, MTICMSTR, BKYSMSTR |
| INP | &P - Inventory Usage Report | t7inp.rwn | T7INP.DFM | BKYSMSTR, BKSYMSTR, BKICMSTR, ISBUILD |
| INQ | &Q - Import & Print Inventory Labels | T7ingimport.rwn | T7INGIMPORT.DFM | MTICMSTR, BKICMSTR, BKARCUST, CLASMSTR |
| INR | &R - Inventory Defaults | T7DSIC.RWN | STUB.DFM | ISDROP, BKSYHELP, DBAHLPID, ISIS |
| INS | &S - View Stock Status | T7INS.RWN | T7INS.DFM | BKICMSTR, MTICMSTR, BKICLOCM, BKICLOC |

## Module: JC

| Code | Label | Program | DFM | Key Tables |
|------|-------|---------|-----|------------|
| JCA | &A - Print Job Cost Report | t7jca.rwn | T7JCA.DFM | BKSYMSTR, BKICMSTR, WORKORD, ISWOEX |
| JCB | &B - Print Profit Projection | t7jcb.rwn | T7JCB.DFM | WORKORD, WOROUT, WOBOM, WOEXCHG |
| JCC | &C - Print Labor Transactions | t7jcc.rwn | STUB.DFM | WORKORD, WOROUT, WOBOM, WOEXCHG |
| JCD | &D - Print Overhead Transactions | t7jcd.rwn | STUB.DFM | WORKORD, WOROUT, WOBOM, WOEXCHG |
| JCE | &E - Print Material Issues | t7jce.rwn | T7JCE.DFM | BKSYMSTR, BKICMSTR, WOMAT, WORKORD |
| JCF | &F - Print Outside Purchases | t7jcf.rwn | T7JCF.DFM | BKSYMSTR, BKICMSTR, OUTPROC, BKAPPO |
| JCG | &G - Print Labor Efficiency | t7jcg.rwn | STUB.DFM | BKSYMSTR, BKICMSTR, OUTPROC, BKAPPO |
| JCH | &H - Print Work Order History | t7jch.rwn | T7JCH.DFM | BKSYMSTR, BKICMSTR, WOROUT, WORKORD |
| JCI | &I - Print Production by Work Center | t7jci.rwn | STUB.DFM | BKSYMSTR, BKICMSTR, WOROUT, WORKORD |
| JCJ | &J - Print Production by Machine | t7jcj.rwn | STUB.DFM | BKSYMSTR, BKICMSTR, WOROUT, WORKORD |
| JCK | &K - Print Production by Tool | t7jck.rwn | STUB.DFM | BKSYMSTR, BKICMSTR, WOROUT, WORKORD |
| JCL | &L - Print Job Cost Summary | t7jcl.rwn | T7JCL.DFM | BKSYMSTR, WORKORD, MTICMSTR, BKICMSTR |
| JCM | &M - Print WIP Summary | t7jcm.rwn | T7JCM.DFM | BKSYMSTR, WORKCTR, WORKORD, ISWOEX |
| JCN | &N - Print WIP Percent Completion | T7jcn.rwn | T7JCN.DFM | BKICMSTR, WORKORD, MTICMSTR, WOMAT |
| JCO | &O - Print Standard Labor Hours | t7jco.rwn | STUB.DFM | BKICMSTR, WORKORD, MTICMSTR, WOMAT |
| JCP | &P - Print Materials in WIP | t7jcp.rwn | T7JCP.DFM | BKSYMSTR, BKICMSTR, WOBOM, WORKORD |
| JCQ | &Q - Print Work Order Receipts | t7jcq.rwn | T7JCQ.DFM | BKICMSTR, MTICMSTR, BKARCUST, BKAPPO |
| JCR | &R - Print Multi-Assembly Cost Rollup | T7JCR.RWN | T7JCR.DFM | BKICMSTR, MTICMSTR, BKARCUST, BKAPPO |
| JCS | &S - Work Order Detail Report | T7JCS.RWN | T7JCS.DFM | WOLABOR, OUTPROC, BKSYMSTR, ISBUILD |
| JCT | &T - Scrap Yield Report | T7JCT.RWN | STUB.DFM |  |

## Module: LC

| Code | Label | Program | DFM | Key Tables |
|------|-------|---------|-----|------------|
| LCA | &A - Edit Lot Numbers | t7lca.rwn | T7LCA.DFM | LOT, MTICMSTR, BKYSMSTR, BKSYMSTR |
| LCB | &B - Assign Lot Control | t7lcb.rwn | T7LCB.DFM | BKICMSTR, MTICMSTR, BKSYHELP, DBAHLPID |
| LCC | &C - Print Lot Availability | t7lcc.rwn | T7LCC.DFM | BKSYMSTR, BKICMSTR, LOT, MTICMSTR |
| LCD | &D - Print Lot History | T7LCD.RWN | STUB.DFM | BKSYMSTR, BKICMSTR, LOT, MTICMSTR |
| LCE | &E - Lot Control On Hand Report | t7lce.rwn | T7LCE.DFM | BKSYMSTR, BKICMSTR, LOT, BKICLOC |
| LCF | &F - Lot Traceability Report | t7lcf.rwn | T7LCF.DFM | BKSYMSTR, BKICMSTR, MTICMSTR, LOT |

## Module: MR

| Code | Label | Program | DFM | Key Tables |
|------|-------|---------|-----|------------|
| MRA | &A - Enter Forecast | T7MRA.RWN | T7MRA.DFM | BKMRPFC, BKICMSTR, BKSYHELP, DBAHLPID |
| MRB | &B - Print Forecast | t7mrb.rwn | T7MRB.DFM | BKSYMSTR, BKMRPFC, BKICMSTR, MTICMSTR |
| MRC | &C - Reset Forecast | T7MRC.RWN | T7MRC.DFM | BKICMSTR, BKMRPFC, MTICMSTR, BKARINVL |
| MRD | &D - Enter MRP Parameters | t7mrd.rwn | T7MRD.DFM | BKICMSTR, MTICMSTR, BKYSMSTR, BKICLOC |
| MRE | &E - Print MRP Parameters | T7MRE.RWN | T7MRE.DFM | BKSYMSTR, BKICMSTR, BKICLOCM, MTICMSTR |
| MRF | &F - Generate Material Requirements | T7MRF.RWN | T7MRF.DFM | MTICMSTR, BKMRPFC, BKARINVL, BKAPPOL |
| MRG | &G - Print Material Requirements | t7mrg.rwn | T7MRG.DFM | BKSYMSTR, BKICMSTR, MTMRP, MTICMSTR |
| MRH | &H - Print Order Action Report | t7mrh.rwn | T7MRH.DFM | BKSYMSTR, BKICMSTR, ISBUILD, MTMRP |
| MRI | &I - Generate Work Orders | t7mri.rwn | T7MRI.DFM | BKYSMSTR, MTICMSTR, BKICMSTR, BKICLOCM |
| MRJ | &J - Generate Purchase Orders | T7MRJ.RWN | T7MRJ.DFM | MTICMSTR, BKYSMSTR, BKICMSTR, BKICLOCM |
| MRK | &K - Generate RFQs | t7mrk.rwn | STUB.DFM | BKMRPPO, BKAPPO, MTICMSTR, BKAPVEND |
| MRL | &L - Print Planned Orders Report | t7mrl.rwn | T7MRL.DFM | BKSYMSTR, MTMRP, BKSYHELP, DBAHLPID |
| MRM | &M - MRP Defaults | T7DSMRP.RWN | STUB.DFM | ISDROP, BKSYHELP, DBAHLPID, ISIS |
| MRN | &N - Apply Delay Action to POs | t7mrn.rwn | T7MRN.DFM | BKSYMSTR, ISBUILD, MTMRP, BKAPPO |

## Module: PI

| Code | Label | Program | DFM | Key Tables |
|------|-------|---------|-----|------------|
| PIA | &A - Capture Frozen Inventory | t7pia.rwn | T7PIA.DFM | BKYSMSTR, BKSYMSTR, BKPIMSTR, BKICMSTR |
| PIB | &B - Frozen Inventory Report | T7PIB.RWN | T7PIB.DFM | BKPIMSTR, BKSYMSTR, BKPIFROZ, BKICMSTR |
| PIC | &C - Enter Tag Counts | t7pic.rwn | T7PIC.DFM | BKPIPHYS, BKYSMSTR, BKSYMSTR, BKPIMSTR |
| PID | &D - Missing Tags Report | t7pid.rwn | T7PID.DFM | BKPIPHYS, BKPIMSTR, BKSYMSTR, BKSYHELP |
| PIE | &E - Edit Frozen Inventory Costs | t7pie.rwn | T7PIE.DFM | BKPIFROZ, BKYSMSTR, BKSYMSTR, BKPIMSTR |
| PIF | &F - Physical Inventory Report | t7pif.rwn | T7PIF.DFM | BKPIMSTR, BKYSMSTR, ISBUILD, BKSYMSTR |
| PIG | &G - Update Actual Inventory | t7pig.rwn | T7PIG.DFM | BKPIMSTR, BKYSMSTR, BKPIPHYS, BKICLOC |
| PIH | &H - Purge Physical Inventory | t7pih.rwn | T7PIH.DFM | BKPIMSTR, BKSYHELP, DBAHLPID, ISIS |

## Module: PL

| Code | Label | Program | DFM | Key Tables |
|------|-------|---------|-----|------------|
| PLA | &A - Run Checkmark Payroll | T6PLA.RUN |  |  |
| PLB | &B - Import Employee Checks | BKPLB.RUN |  |  |
| PLC | &C - Import Employer Vouchers | BKPLC.RUN |  |  |
| PLD | &D - Payroll Link Setup | BKPLD.RUN |  |  |

## Module: PO

| Code | Label | Program | DFM | Key Tables |
|------|-------|---------|-----|------------|
| POA | &A - Enter Purchase Orders | t7poa.rwn | T7POA.DFM | BKAPPO, BKAPVEND, BKAPDESC, BKAPPOL |
| POB | &B - Print Purchase Orders | t7pob.rwn | T7POB.DFM | MTICMSTR, BKAPVEND, BKSYMSTR, BKYSMSTR |
| POC | &C - Receive Purchase Orders | t7poc.rwn | T7POC.DFM | BKAPPOL, BKAPPO, BKAPDESC, MTICMSTR |
| POD | &D - View PO Receivers | t7pod.rwn | STUB.DFM | MKAHIST, BKAPPOL, BKSYAP, MTICMSTR |
| POE | &E - Enter/Print RFQs | t7poe.rwn | STUB.DFM | MKAHIST, BKAPPOL, BKSYAP, MTICMSTR |
| POF | &F - Enter Verbal RFQs | t7pof.rwn | T7POF.DFM | BKRFQ, BKARINVL, ISESTDTL, BKESTCFG |
| POG | &G - Convert RFQs | t7pog.rwn | T7POG.DFM | MTICMSTR, BKAPPO, BKAPPOL, BKICMSTR |
| POH | &H - Enter Vendor Prices | t7poh.rwn | T7POH.DFM | BKRFQ, BKAPDESC, BKICMSTR, MTICMSTR |
| POI | &I - Reports | *(group)* |  |  |
| POIA | &A - Print Open Purchase Orders Listing | t7poia.rwn | STUB.DFM | BKRFQ, BKAPDESC, BKICMSTR, MTICMSTR |
| POIB | &B - Print Closed Purchase Orders Listin | t7poib.rwn | STUB.DFM | BKRFQ, BKAPDESC, BKICMSTR, MTICMSTR |
| POIC | &C - Print RFQ Status | t7poic.rwn | T7POIC.DFM | BKRFQ, BKSYHELP, DBAHLPID, ISIS |
| POID | &D - Print Vendor Prices | t7poid.rwn | T7POID.DFM | BKSYMSTR, BKRFQ, MTICMSTR, BKICMSTR |
| POIE | &E - Print Receiving Report | t7poie.rwn | STUB.DFM | BKSYMSTR, BKRFQ, MTICMSTR, BKICMSTR |
| POIF | &F - Print Received not Invoiced | t7poif.rwn | STUB.DFM | BKSYMSTR, BKRFQ, MTICMSTR, BKICMSTR |
| POIG | &G - Print Purch Order Items by Due Date | t7poig.rwn | T7POIG.DFM | BKSYMSTR, ISNTYPE, ISBUILD, BKAPVEND |
| POIH | &H - Print On Time Delivery Report | T7POIH.RwN | T7POIH.DFM | BKAPPO, BKQCMSTR, BKAPPOL, BKAPVEND |
| POII | &I - Print Purchase Order Changes | t7POIi.RwN | T7POII.DFM | BKSYMSTR, ISAPCHG, MTICMSTR, BKAPPO |
| POIJ | &J - Print/Export Purchases by Item/Item Class | purchitem.rwn |  | BKSYHELP, DBAHLPID, BKPSUSER, ISDRILL |
| POIK | &K - Print/Export Purchases by Vendor | purchvend.rwn |  | BKSYHELP, DBAHLPID, BKPSUSER, ISDRILL |
| POIL | &L - Print Digital Signature Status | t7poil.rwn | T7POIL.DFM | BKAPPO, BKPRMSTR, BKSYHELP, DBAHLPID |
| POJ | &J - QC Inspection Programs | *(group)* |  |  |
| POJA | &A - Print Receipt Travelers | t7poja.rwn | T7POJA.DFM | BKSYMSTR, BKQCMSTR, BKAPPOL, BKICMSTR |
| POJB | &B - Print Inventory in QC | t7pojb.rwn | T7POJB.DFM | MTICMSTR, BKSYMSTR, BKQCMSTR, BKAPPO |
| POJC | &C - Enter Inspection Buyoffs | t7pojc.rwn | T7POJC.DFM | BKQCMSTR, BKQCTRAN, BKAPPOL, BKAPPO |
| POJD | &D - Vendor Quality Performance Report | t7pojd.rwn | T7POJD.DFM | BKQCTRAN, BKAPVEND, BKQCMSTR, BKSYHELP |
| POK | &K - Close Purchase Orders | t7pok.rwn | T7POK.DFM | MTICMSTR, BKSYMSTR, BKAPPO, BKAPPOL |
| POL | &L - Assign Vendors to Items | t7pol.rwn | T7POL.DFM | BKSBVEND, BKAPVEND, BKICMSTR, MTICMSTR |
| PON | &N - Reconcile PO Invoices | t7pon.run |  |  |
| POO | &O - View Open Purchase Orders | t7poo.rwn | STUB.DFM | MKAHIST, BKSYHELP, DBAHLPID, BKAPPO |
| POP | &P - View Vendor Information | T7APU.rwn | STUB.DFM | MKAHIST, BKAPCHKF, BKAPINVT, BKAPPO |
| POQ | &Q - Maintain PO Delivery Dates | T7poQ.RWN | T7POQ.DFM | BKAPPO, BKAPPOL, MTICMSTR, BKICMSTR |
| POR | &R - Print Receiving Slip | T7por.rwn | STUB.DFM | BKAPPO, BKAPPOL, MTICMSTR, BKICMSTR |
| POS | &S - Purchase Order Defaults | T7DSPO.RWN | STUB.DFM | ISDROP, BKSYHELP, DBAHLPID, ISIS |
| POT | &T - Electronically Approve PO | T7DIGSIGPO.RWN | STUB.DFM | BKAPPO, BKAPPOL, ISDIGSIG, BKPRMSTR |

## Module: PR

| Code | Label | Program | DFM | Key Tables |
|------|-------|---------|-----|------------|
| PRA | &A - Enter Employees | t7pra.rwn | T7PRA.DFM | BKPRMSTR, BKPRINFO, BKPRGLFL, BKGLCOA |
| PRB | &B - Enter Pay Info | T7PRB.RWN | T7PRB.DFM | BKPRCURP, BKPRMSTR, BKPRGLFL, BKSYMSTR |
| PRC | &C - Print Payroll Register | T7PRC.RWN | T7PRC.DFM | BKSYMSTR, BKPRCURP, ISBUILD, BKPRMSTR |
| PRD | &D - Print Payroll Checks | T7PRD.RWN | T7PRD.DFM | BKSYMSTR, BKYSMSTR, BKPRMSTR, BKPRCURP |
| PRE | &E - Print Employee Info | T7PRE.RWN | T7PRE.DFM | BKSYMSTR, BKYSMSTR, BKPRMSTR, BKPRGLFL |
| PRF | &F - Maintain Tax Tables | T7PRF.RWN | T7PRF.DFM | BKPRFTAX, BKSYHELP, DBAHLPID, ISIS |
| PRG | &G - Void Payroll Checks | T7PRG.RWN | T7PRG.DFM | BKPRCURP, BKPRMSTR, BKSYMSTR, ISBANKS |
| PRH | &H - Transfer Liabilities to AP | T7PRH.RWN | T7PRH.DFM | BKPRGLFL, BKYSMSTR, BKAPINVT, ISMCF |
| PRI | &I - Print Pay History | t7pri.rwn | T7PRI.DFM | BKSYMSTR, BKPRCURP, BKPRMSTR, BKPRINFO |
| PRJ | &J - Enter Time Cards | T7PRJ.RWN | T7PRJ.DFM | BKPRMSTR, BKYSMSTR, BKPRTC, BKSYHELP |
| PRK | &K - Print/Post Time Cards | T7PRK.RWN | T7PRK.DFM | BKSYMSTR, BKYSMSTR, BKPRMSTR, BKPRTC |
| PRL | &L - Reports | *(group)* |  |  |
| PRLA | &A - Print Quarterly Info | T7PRLA.RWN | T7PRLA.DFM | BKSYMSTR, BKPRMSTR, BKPRGLFL, BKSYHELP |
| PRLB | &B - Print QTD Earnings Register | T7PRLB.RWN | T7PRLB.DFM | BKSYMSTR, BKPRMSTR, BKPRINFO, BKPRCURP |
| PRLC | &C - Print QTD Taxable Earnings | T7PRLC.RWN | T7PRLC.DFM | BKSYMSTR, BKPRMSTR, BKPRCURP, BKPRGLFL |
| PRLD | &D - Print Detail Earnings Ledger | T7PRLD.RWN | T7PRLD.DFM | BKSYMSTR, BKPRCURP, BKPRMSTR, BKPRINFO |
| PRLE | &E - Print Detail Deductions Ledger | t7prle.rwn | T7PRLE.DFM | BKSYMSTR, BKYSMSTR, BKPRGLFL, BKPRCURP |
| PRLF | &F - Print Subject To Report | T7PRLF.RWN | T7PRLF.DFM | BKSYMSTR, BKPRGLFL, ISBUILD, BKPRMSTR |
| PRLG | &G - Print 941 and Schedule B Reports | T7PRLG.RWN | T7PRLG.DFM | BKPRGLFL, BKSYMSTR, BKPRCURP, BKPRMSTR |
| PRLH | &H - Print 940 Report | T7PRLH.RWN | T7PRLH.DFM | BKPRGLFL, BKPRCURP, BKPRMSTR, BKSYHELP |
| PRLI | &I - Print W-2 Forms | T7PRLI.RWN | T7PRLI.DFM | BKPRMSTR, BKPRGLFL, BKSYMSTR, BKYSMSTR |
| PRLJ | &J - Print Calif DE6 Form | T7PRLJ.RWN | T7PRLJ.DFM | BKSYMSTR, BKPRMSTR, BKPRSALE, BKPRGLFL |
| PRLK | &K - Print Payroll Hours | t7prlk.rwn | T7PRLK.DFM | BKSYMSTR, BKYSMSTR, BKPRCURP, BKPRMSTR |
| PRLL | &L - Print 941B Forms | T7PRLL.RWN |  |  |
| PRLM | &M - Print Employer Contributions | T7PRLM.RWN | T7PRLM.DFM | BKSYMSTR, BKPRGLFL, BKPRCURP, BKPRMSTR |
| PRLN | &N - Print Payroll Wages Detail | t7prln.rwn | T7PRLN.DFM | BKSYMSTR, BKYSMSTR, BKPRCURP, BKPRMSTR |
| PRLO | &O - Reprint Payroll Check Stub | t7prlo.rwn | T7PRLO.DFM | BKSYMSTR, BKYSMSTR, BKPRMSTR, BKPRCURP |
| PRLP | &P - Print Vacation & Sick Due | t7prlp.rwn | T7PRLP.DFM | BKSYMSTR, ISBUILD, BKPRMSTR, BKPRCURP |
| PRM | &M - Payroll Divisions | T7PRM.RWN | T7PRM.DFM | BKPRGLFL, BKYSMSTR, BKPRMSTR, BKSYHELP |
| PRN | &N - Purge Payroll History | T7PRN.RWN | T7PRN.DFM | BKSYMSTR, BKYSMSTR, BKPRCURP, BKPRMSTR |
| PRO | &O - Payroll Year End Routine | T7PRO.RWN | T7PRO.DFM | BKSYMSTR, BKYSMSTR, BKPRMSTR, FILELOC |
| PRP | &P - Enter Raise Information | T7PRP.RWN | T7PRP.DFM | BKPRMSTR, BKSYMSTR, BKYSMSTR, BKPRINFO |
| PRQ | &Q - Enter Review Information | T7PRQ.RWN | T7PRQ.DFM | BKPRMSTR, BKSYMSTR, BKYSMSTR, BKPRINFO |
| PRR | &R - Payroll Defaults | T7DSPR.RWN | STUB.DFM | ISDROP, BKSYHELP, DBAHLPID, ISIS |
| PRS | &S - Assign Password to Employee | T7PRS.RWN | T7PRS.DFM | BKPRMSTR, BKPRINFO, BKSYHELP, DBAHLPID |
| PRT | &T - Archive Pay History | T7SMJV.RWN | T7SMJV.DFM | BKPRCURP, BKPRMSTR, BKPRINFO, BKPRGLFL |

## Module: PS

| Code | Label | Program | DFM | Key Tables |
|------|-------|---------|-----|------------|
| PSA | &A - System Users/Passwords | t7psa.rwn | T7PSA.DFM | BKPSUSER, ISEXUSER, FILELOC, BKSYMSTR |
| PSB | &B - DBA System Security Levels | bkpsb.run |  |  |
| PSC | &C - DBA Company Logon Access | bkpsc.run |  |  |
| PSE | &E - Evo Menu Access by User Report | t7pse.rwn | T7PSE.DFM | BKMENUSU, BKSYHELP, DBAHLPID, ISLOG |
| PSF | &F - Evo Menu Access by Program | t7psf.rwn | T7PSF.DFM | BKMENUSU, BKSYHELP, DBAHLPID, ISLOG |
| PSG | &G - Maintain Menu Access Records | WBKMENUSETUP.RWN | WBKMENUSETUP.DFM | BKPSUSER, BKMENUSU, BKSYHELP, DBAHLPID |
| PSH | &H - Configure Auto-Chain Programs | T7CHAIN.RWN | T7CHAIN.DFM | ISCHAINM, BKPSUSER, BKSYHELP, DBAHLPID |
| PSI | &I - Enter Approved Signers for Purchase Orders | T7DIGSIGADMIN.RWN | STUB.DFM | BKAPPO, BKAPPOL, ISDIGSIG, BKPRMSTR |
| PSJ | &J - Enter Contract Review Signers | T7CTREVUADMIN.RWN | STUB.DFM | ISCTREVU, BKARINV, ISSOREVU, BKSYHELP |
| PSK | &K - Enter Vendor Approval | J7appvend.rwn | STUB.DFM |  |
| PSL | &L - Enter Field Specific Access | T7LIMACC.rwn | T7LIMACC.DFM | ISACCESS, BKSYHELP, DBAHLPID, MKAHIST |

## Module: QC

| Code | Label | Program | DFM | Key Tables |
|------|-------|---------|-----|------------|
| QCA | &A - Quality Control Receiving Report | T7QCA.RWN | T7QCA.DFM | BKICMSTR, MTICMSTR, CLASS, BKAPVEND |
| QCB | &B - Quality Control Materials Report | T7QCB.RWN | T7QCB.DFM | BKICMSTR, MTICMSTR, CLASS, WORKORD |
| QCC | &C - Production Scrap Report | T7QCC.RWN | T7QCC.DFM | BKICMSTR, MTICMSTR, CLASS, WORKORD |
| QCD | &D - Quality Control Labor Report | T7QCD.RWN | T7QCD.DFM | BKICMSTR, MTICMSTR, CLASS, WORKORD |
| QCE | &E - Vendor Quality Performance | t7pojd.rwn | T7POJD.DFM | BKQCTRAN, BKAPVEND, BKQCMSTR, BKSYHELP |
| QCF | &F - Non-Conformance Reporting | *(group)* |  |  |
| QCFA | &A - Enter NCR | T7QCFA.RWN | T7QCFA.DFM | ISNCR, MTICMSTR, BKICMSTR, BKARCUST |
| QCFB | &B - Print NCR | T7QCFB.RWN | T7QCFB.DFM | BKSYMSTR, BKICMSTR, MTICMSTR, BKARCUST |
| QCFC | &C - Disposition NCR | T7QCFC.RWN | STUB.DFM | BKSYMSTR, BKICMSTR, MTICMSTR, BKARCUST |
| QCFD | &D - Close NCR | T7QCFD.RWN | T7QCFD.DFM | BKICMSTR, MTICMSTR, ISNCR, ISNOTES |
| QCFE | &E - View NCR | T7QCFE.RWN | STUB.DFM | BKICMSTR, MTICMSTR, ISNCR, ISNOTES |
| QCFF | &F - NCR Listing | T7QCFF.RWN | T7QCFF.DFM | BKICMSTR, MTICMSTR, BKICLOCM, ISNCR |
| QCG | &G - Corrective Action | *(group)* |  |  |
| QCGA | &A - Enter CAR | T7QCGA.RWN | T7QCGA.DFM | ISNCR, ISCACT, ISCARDTE, BKAPDESC |
| QCGB | &B - Print CAR | T7QCGB.RWN | T7QCGB.DFM | BKICMSTR, MTICMSTR, BKARCUST, BKAPVEND |
| QCGC | &C - View CAR | T7QCGC.RWN | STUB.DFM | BKICMSTR, MTICMSTR, BKARCUST, BKAPVEND |
| QCGD | &D - List CAR | T7QCGD.RWN | T7QCGD.DFM | BKICMSTR, MTICMSTR, BKICLOCM, ISNCR |
| QCH | &H - QC Defaults | T7DSQC.RWN | STUB.DFM |  |

## Module: QU

| Code | Label | Program | DFM | Key Tables |
|------|-------|---------|-----|------------|
| QUA | &A - Master Inquiry | t7csi.rwn | T7CSI.DFM | BKSYHELP, DBAHLPID, TASCOLOR, ISDRILL |
| QUB | &B - Calendar Drill Down | caldrillbt.rwn | CALDRILLBT.DFM | BKSYHELP, DBAHLPID, TASCOLOR, ISLOG |
| QUC | &C - Calendar Summary Report | isshpcal2.rwn | EVOCSR.DFM | BKARINVL, BKARINV, BKSYHELP, DBAHLPID |
| QUD | &D - Business Status | t7jbs.rwn | T7JBS.DFM | BKSYHELP, DBAHLPID, ISIS, ISLOG |
| QUE | &E - Quick Grid Lookup | t7qgrid.rwn | T7QGRID.DFM | BKLUGRID, BKSYHELP, DBAHLPID, ISLOG |
| QUF | &F - Query Executor | queryexecute.rwn |  | BKSYHELP, DBAHLPID, BKPSUSER, ISDRILL |

## Module: RM

| Code | Label | Program | DFM | Key Tables |
|------|-------|---------|-----|------------|
| RMA | &A - Enter RMA | t7rma.rwn | STUB.DFM | MKAHIST, MTICMSTR, BKBMMSTR, BKICMSTR |
| RMB | &B - Print RMA | T7RMB.RWN | STUB.DFM | BKARINV, BKARINVL, ISRMAI, BKICMSTR |
| RMC | &C - Receive RMA | T7RMC.RWN | STUB.DFM | BKARINV, BKARINVL, ISRMAI, BKICMSTR |
| RMD | &D - Disposition RMA | T7RMD.RWN | T7RMD.DFM | BKARINVL, ISRMAI, ISRMAC, BKARINV |
| RME | &E - Enter RMA Return Codes | T7RME.RWN | T7RME.DFM | ISRMAC, BKSYHELP, DBAHLPID, ISIS |
| RMF | &F - RMA/Service & Repair Defaults | T7DSRMA.RWN | STUB.DFM | ISDROP, BKSYHELP, DBAHLPID, ISIS |
| RMG | &G - Reason Codes Report | t7rmg.rwn | T7RMG.DFM | BKSYMSTR, BKARINV, BKARINVL, ISRMAI |

## Module: RO

| Code | Label | Program | DFM | Key Tables |
|------|-------|---------|-----|------------|
| ROA | &A - Enter Routings | t7roa.rwn | T7ROA.DFM | ROUTING, BKRTCST, MTICMSTR, BKYSMSTR |
| ROB | &B - Print/Rollup Routings Costs | t7rob.rwn | T7ROB.DFM | BKSYMSTR, MTICMSTR, BKICMSTR, ROUTING |
| ROC | &C - Work Centers | t7roc.rwn | T7ROC.DFM | WORKCTR, DPTMENT, ROUTING, ISROUTEX |
| ROD | &D - Enter Machines | t7rod.rwn | T7ROD.DFM | MACHINE, BKMATRIM, WORKCTR, ROUTING |
| ROE | &E - Enter Tools | t7roe.rwn | T7ROE.DFM | TOOL, MACHINE, BKARCUST, ISBNMSTR |
| ROF | &F - Enter QC Codes | t7rof.rwn | T7ROF.DFM | QCCODES, BKSYHELP, DBAHLPID, ISIS |
| ROG | &G - Enter Scrap Codes | T7ROG.RWN | T7ROG.DFM | SCRAP, BKGLCOA, BKSYHELP, DBAHLPID |
| ROH | &H - Enter Departments | t7roh.rwn | T7ROH.DFM | DPTMENT, BKSYHELP, DBAHLPID, ISIS |
| ROI | &I - Enter Operation Templates | t7roi.rwn | T7ROI.DFM | ROUTING, WORKCTR, BKAPVEND, BKYSMSTR |
| ROJ | &J - Reports | *(group)* |  |  |
| ROJA | &A - Print Routings | t7roja.rwn | T7ROJA.DFM | BKSYMSTR, WORKORD, WOROUT, WOBOM |
| ROJB | &B - Print Work Centers | t7rojb.rwn | T7ROJB.DFM | WORKCTR, BKSYHELP, DBAHLPID, ISIS |
| ROJC | &C - Print Machines | t7rojc.rwn | T7ROJC.DFM | MACHINE, BKSYHELP, DBAHLPID, ISIS |
| ROJD | &D - Print Tools | T7ROJD.RWN | T7ROJD.DFM | BKSYMSTR, TOOL, BKARCUST, MACHINE |
| ROJE | &E - Print QC Codes | t7roje.rwn | T7ROJE.DFM | QCCODES, BKSYHELP, DBAHLPID, ISIS |
| ROJF | &F - Print Scrap Codes | t7rojf.rwn | T7ROJF.DFM | SCRAP, BKSYHELP, DBAHLPID, ISIS |
| ROJG | &G - Print Departments | t7rojg.rwn | T7ROJG.DFM | DPTMENT, BKSYHELP, DBAHLPID, ISIS |
| ROJH | &H - Print Operation Templates | t7rojh.rwn | T7ROJH.DFM | WORKCTR, ROUTING, BKSYHELP, DBAHLPID |
| ROK | &K - Enter Specifications Templates | t7rok.rwn | T7ROK.DFM | BKRTTEMP, BKSYHELP, DBAHLPID, ISIS |
| ROL | &L - Enter Sequence Print Control | t7rol.rwn | T7ROL.DFM | ROUTING, BKSYHELP, DBAHLPID, ISIS |
| ROM | &M - Enter Testing Method | t7qcmthd.rwn | T7QCMTHD.DFM | ISQCMTHD, ISNOTES, ISLINKS, BKSYHELP |
| RON | &N - Enter Testing Requirements | t7qcspec.rwn | T7QCSPEC.DFM | ISQCSPEC, MTICMSTR, ISQCMTHD, ROUTING |
| ROO | &O - Routings Defaults | T7DSRO.RWN | STUB.DFM | ISDROP, BKSYHELP, DBAHLPID, ISIS |
| ROP | &P - Update Processing Cost Standards | t7rop.rwn | T7ROP.DFM | ROUTING, BKAPPOL, BKAPPO, BKSYHELP |

## Module: SA

| Code | Label | Program | DFM | Key Tables |
|------|-------|---------|-----|------------|
| SAA | &A - Print Daily Sales/Bookings | t7saa.rwn | T7SAA.DFM | ISBUILD, BKYSMSTR, BKARINV, BKARCUST |
| SAB | &B - Print Profit by Invoice | T7SAB.RWN | STUB.DFM | BKYSMSTR, BKARINV, BKARCUST, ISARCHG |
| SAC | &C - Print Customer Detail | T7SAC.RWN | STUB.DFM | BKYSMSTR, BKARINV, BKARCUST, ISARCHG |
| SAD | &D - Print Customer Summary | T7SAD.RWN | STUB.DFM | BKYSMSTR, BKARINV, BKARCUST, ISARCHG |
| SAE | &E - Print Customer Class Detail | T7SAE.RWN | STUB.DFM | BKYSMSTR, BKARINV, BKARCUST, ISARCHG |
| SAF | &F - Charts and Export | *(group)* |  |  |
| SAFA | &A - Profit by Invoice | t7jsapbi.rwn | T7JSAPBI.DFM | BKSYHELP, DBAHLPID, ISIS, MKAHIST |
| SAFB | &B - Sales by Customer | t7jsacc.rwn | T7JSACC.DFM | BKSYHELP, DBAHLPID, ISIS, MKAHIST |
| SAFC | &C - Sales by Salesperson | t7jsasrs.rwn | T7JSASRS.DFM | BKSYHELP, DBAHLPID, ISIS, MKAHIST |
| SAFD | &D - Sales by Item/Class | t7jsaic.rwn | T7JSAIC.DFM | BKSYHELP, DBAHLPID, ISIS, MKAHIST |
| SAG | &G - Print Customer Class Summary | T7SAG.RWN | STUB.DFM | BKYSMSTR, BKARINV, BKARCUST, ISARCHG |
| SAH | &H - Print Salesperson Detail | T7SAH.RWN | STUB.DFM | BKYSMSTR, BKARINV, BKARCUST, ISARCHG |
| SAI | &I - Print Salesperson Summary | T7SAI.RWN | STUB.DFM | BKYSMSTR, BKARINV, BKARCUST, ISARCHG |
| SAJ | &J - Print Inventory Detail | T7SAJ.RWN | STUB.DFM | BKYSMSTR, BKARINV, BKARCUST, ISARCHG |
| SAL | &L - Print Product Class | T7SAL.RWN | STUB.DFM | BKYSMSTR, BKARINV, BKARCUST, ISARCHG |
| SAM | &M - Print User-Defined Detail | t7sam.rwn | T7SAM.DFM | BKSAREPT, BKACTRPT, ISBUILD, BKARINVL |
| SAN | &N - Print User-Defined Summary | t7san.rwn | T7SAN.DFM | BKSAREPT, BKACTRPT, ISBUILD, BKARINVL |
| SAO | &O - Top Customer Report | T7SAO.RWN | T7SAO.DFM | BKSYMSTR, BKICMSTR, BKARCUST, BKPRSALE |
| SAP | &P - Print Sales With Surcharge Rolled Up | t7sap.rwn | T7SAP.DFM | BKSYMSTR, BKARINVL, BKARINV, MTICMSTR |

## Module: SC

| Code | Label | Program | DFM | Key Tables |
|------|-------|---------|-----|------------|
| SCA | &A - Edit Serial Numbers | t7sca.rwn | T7SCA.DFM | SERIAL, MTICMSTR, BKYSMSTR, WORKORD |
| SCB | &B - Assign Serial Control | t7scb.rwn | T7SCB.DFM | BKICMSTR, MTICMSTR, BKSYHELP, DBAHLPID |
| SCC | &C - Print Serial Availability | t7scc.rwn | T7SCC.DFM | BKSYMSTR, BKICMSTR, SERIAL, MTICMSTR |
| SCD | &D - Print Serial History | T7SCD.RWN | STUB.DFM | BKSYMSTR, BKICMSTR, SERIAL, MTICMSTR |
| SCE | &E - Archive Serial Numbers | t7sce.rwn | T7SCE.DFM | BKICMSTR, SERIAL, BKSYHELP, DBAHLPID |
| SCF | &F - Serial Control Exception Report | t7scf.rwn | T7SCF.DFM | BKSYMSTR, SERIAL, BKICMSTR, MTICMSTR |
| SCG | &G - Enter Serial Generation Parameters | t7scg.rwn | T7SCG.DFM | ISSERCNT, MTICMSTR, CLASMSTR, BKSYHELP |
| SCH | &H - Serial Traceability Report | t7sch.rwn | T7SCH.DFM | BKSYMSTR, MTICMSTR, SERIAL, INVTXN |

## Module: SD

| Code | Label | Program | DFM | Key Tables |
|------|-------|---------|-----|------------|
| SDA | &A - Company Defaults | T7DSCO.rwn | STUB.DFM | ISDROP, BKSYHELP, DBAHLPID, ISIS |
| SDB | &B - Work Order Defaults | t7dswo.rwn | STUB.DFM | ISDROP, BKSYHELP, DBAHLPID, ISIS |
| SDC | &C - Purchase Order Defaults | t7dspo.rwn | STUB.DFM | ISDROP, BKSYHELP, DBAHLPID, ISIS |
| SDD | &D - MRP Defaults | t7dsmrp.rwn | STUB.DFM | ISDROP, BKSYHELP, DBAHLPID, ISIS |
| SDE | &E - Scheduling Defaults | t7dssh.rwn | STUB.DFM | ISDROP, BKSYHELP, DBAHLPID, ISIS |
| SDF | &F - Data Collection Defaults | t7dsdc.rwn | STUB.DFM | ISDROP, BKSYHELP, DBAHLPID, ISIS |
| SDG | &G - Estimating Defaults | t7dsest.rwn | STUB.DFM | ISDROP, BKSYHELP, DBAHLPID, ISIS |
| SDH | &H - Inventory Defaults | t7dsic.rwn | STUB.DFM | ISDROP, BKSYHELP, DBAHLPID, ISIS |
| SDI | &I - Routings Defaults | t7dsro.rwn | STUB.DFM | ISDROP, BKSYHELP, DBAHLPID, ISIS |
| SDJ | &J - Bills of Material Defaults | t7dsbom.rwn | STUB.DFM | ISDROP, BKSYHELP, DBAHLPID, ISIS |
| SDL | &L - Features and Options Defaults | t7dsfo.rwn | STUB.DFM | ISDROP, BKSYHELP, DBAHLPID, ISIS |
| SDM | &M - Sales Orders Defaults | t7dsso.rwn | STUB.DFM | ISDROP, BKSYHELP, DBAHLPID, ISIS |
| SDN | &N - Sales Commissions Defaults | t7dscs.rwn | STUB.DFM | ISDROP, BKSYHELP, DBAHLPID, ISIS |
| SDO | &O - Contact Manager Defaults | t7dscm.rwn | STUB.DFM | ISDROP, BKSYHELP, DBAHLPID, ISIS |
| SDP | &P - Customer/AR Defaults | t7dsar.rwn | STUB.DFM | ISDROP, BKSYHELP, DBAHLPID, ISIS |
| SDQ | &Q - Master Default Settings | t7mdefaults.rwn | T7MDEFAULTS.DFM | FILELOC, BKSYMSTR, BKYSMSTR, MTICMSTR |
| SDR | &R - Assign Next Document Numbers | t7numdef.rwn | T7NUMDEF.DFM | BKYSMSTR, ISNUMBER, MKAHIST, BKSYAP |
| SDS | &S - Warehouse Control Defaults | t7dswc.rwn | STUB.DFM | ISDROP, BKSYHELP, DBAHLPID, ISIS |
| SDT | &T - Service/RMA Defaults | t7dsrma.rwn | STUB.DFM | ISDROP, BKSYHELP, DBAHLPID, ISIS |
| SDU | &U - Hand-Held Defaults | t7dshh.rwn | STUB.DFM | ISDROP, BKSYHELP, DBAHLPID, ISIS |
| SDV | &V - International Setting Defaults | T7DSIM.RWN | STUB.DFM | ISDROP, BKSYHELP, DBAHLPID, ISIS |

## Module: SH

| Code | Label | Program | DFM | Key Tables |
|------|-------|---------|-----|------------|
| SHA | &A - Edit WO Start/Finish/Due Dates | t7sha.rwn | T7SHA.DFM | WORKORD, BKICMSTR, MTICMSTR, BKARINVL |
| SHB | &B - Manually Schedule Work Orders | t7shb.rwn | T7SHB.DFM | WORKORD, MTICMSTR, WOROUT, WORKCTR |
| SHC | &C - Manually Schedule Work Centers | t7shc.rwn | T7SHC.DFM | WORKCTR, WOROUT, WORKORD, BKSYHELP |
| SHD | &D - Manually Schedule Machines | machineview.rwn |  | BKSYHELP, DBAHLPID, BKPSUSER, ISDRILL |
| SHE | &E - Finite Scheduling | t7she.rwn | T7SHE.DFM | SCHWO, WORKORD, BKSYMSTR, SCHEDCAL |
| SHF | &F - Infinite Scheduling | t7shf.rwn | T7SHF.DFM | WORKORD, MTICMSTR, WOROUT, CALENDAR |
| SHG | &G - Print Work Order Schedule | t7shg.rwn | T7SHG.DFM | BKSYMSTR, BKICMSTR, WORKORD, MTICMSTR |
| SHH | &H - Print Work Order Status | t7shh.rwn | T7SHH.DFM | BKSYMSTR, BKICMSTR, MTICMSTR, WORKORD |
| SHI | &I - Print Work Center Schedule | t7shi.rwn | T7SHI.DFM | BKSYMSTR, MTICMSTR, ISBUILD, WORKCTR |
| SHJ | &J - Print Machine Schedule | t7shj.rwn | T7SHJ.DFM | BKSYMSTR, MACHINE, WOROUT, WORKORD |
| SHK | &K - View Work Center Load | t7shk.rwn | STUB.DFM | MKAHIST, MACHINE, WOROUT, WORKORD |
| SHL | &L - View or Calculate Work Center Load | workcenterload.rwn |  | BKSYHELP, DBAHLPID, BKPSUSER, ISDRILL |
| SHM | &M - Lead Time Estimator | t7shm.rwn | T7SHM.DFM | BKICMSTR, CALENDAR, BKSYHELP, DBAHLPID |
| SHN | &N - Generate Lead Times | t7shn.rwn | T7SHN.DFM | BKSYMSTR, BKYSMSTR, BKICMSTR, MTICMSTR |
| SHO | &O - Finite Schedule Bucket Report | t7sho.rwn | T7SHO.DFM | BKSYMSTR, WORKORD, BUCKETS, WORKCTR |
| SHP | &P - Lead Time Scheduling | t7shp.rwn | T7SHP.DFM | WORKORD, WOBOM, MTICMSTR, WOROUT |
| SHQ | &Q - Scheduling Defaults | T7DSSH.RWN | STUB.DFM | ISDROP, BKSYHELP, DBAHLPID, ISIS |
| SHR | &R - Work Center Scheduler | T7VSCHED.RWN | T7VSCHED.DFM | BKICMSTR, FILELOC, WORKORD, WOROUT |

## Module: SM

| Code | Label | Program | DFM | Key Tables |
|------|-------|---------|-----|------------|
| SMA | &A - Enter Customers | t7ara.rwn | T7ARA.DFM | BKARCUST, ISAREX, ISTAXGRP, BKCMDUNH |
| SMB | &B - Enter Vendors | t7apa.rwn | T7APA.DFM | BKAPVEND, BKAPVND2, ISTAXGRP, ISEXUSER |
| SMC | &C - Enter Classes | *(group)* |  |  |
| SMCA | &A - Enter Item Classes | T7SMCA.RWN | T7SMCA.DFM | CLASMSTR, BKICLOCM, CLASS, BKYSMSTR |
| SMCB | &B - Enter Customer Classes | T7SMCB.RWN | T7SMCB.DFM | CLASMSTR, BKSYHELP, DBAHLPID, ISIS |
| SMCC | &C - Enter Vendor Classes | T7SMCC.RWN | T7SMCC.DFM | CLASMSTR, BKSYHELP, DBAHLPID, ISIS |
| SMD | &D - Enter Terms Table | t7smd.rwn | T7SMD.DFM | ISTERMS, BKSYHELP, DBAHLPID, ISIS |
| SME | &E - Enter Tax Codes | t7sme.rwn | T7SME.DFM | ISTAXFIL, BKAPVEND, BKGLCOA, BKSYMSTR |
| SMF | &F - Enter Tax Groups | T7SMF.RWN | T7SMF.DFM | ISTAXGRP, ISTAXFIL, BKSYHELP, DBAHLPID |
| SMG | &G - Enter Employees | t7smg.rwn | T7SMG.DFM | BKPRMSTR, ISLINKS, BKSYMSTR, BKPRINFO |
| SMH | &H - Enter Shop Calendar | t7smh.rwn | T7SMH.DFM | CALENDAR, SCHEDCAL, CALTEMP, BKSYHELP |
| SMI | &I - Contact Manager Maintenance | *(group)* |  |  |
| SMIA | &A - Enter Lead Source Codes | t7smia.rwn | T7SMIA.DFM | BKCMLEAD, BKSYHELP, DBAHLPID, ISIS |
| SMIB | &B - Enter Territory Codes | t7smib.rwn | T7SMIB.DFM | BKCMTERR, BKSYHELP, DBAHLPID, ISIS |
| SMIC | &C - Enter Reminder Types | t7smic.rwn | T7SMIC.DFM | BKCMACFC, BKSYHELP, DBAHLPID, ISIS |
| SMID | &D - Enter Class Codes | t7smid.rwn | T7SMID.DFM | BKCMACCC, BKSYHELP, DBAHLPID, ISIS |
| SMIE | &E - Enter Key Date Codes | t7smie.rwn | T7SMIE.DFM | BKCMDTCD, BKSYHELP, DBAHLPID, ISIS |
| SMIF | &F - Enter Reasons for Quote Loss | t7smif.rwn | T7SMIF.DFM | ISCATMST, BKSYHELP, DBAHLPID, ISIS |
| SMJ | &J - File Maintenance Programs | *(group)* |  |  |
| SMJA | &A - Work Order File Maintenance | t7smja.rwn | T7SMJA.DFM | BKSYMSTR, WORKORD, WORECV, BKDCLAB |
| SMJB | &B - Archive Work Orders | t7smjb.rwn | T7SMJB.DFM | WORKORD, BKICMSTR, BKSYMSTR, WODATE |
| SMJC | &C - Reconcile Inventory On-Hand | t7smjc.rwn | T7SMJC.DFM | BKICLOCM, BKICMSTR, BKSYMSTR, BKYSMSTR |
| SMJD | &D - Consolidate Inventory Transactions | t7smjd.rwn | T7SMJD.DFM | BKICMSTR, INVTXN, BKYSMSTR, MTICMSTR |
| SMJE | &E - Purge Work Orders | t7smje.rwn | STUB.DFM | BKICMSTR, INVTXN, BKYSMSTR, MTICMSTR |
| SMJF | &F - Purge Purchase Order History | t7smjf.rwn | T7SMJF.DFM | BKAPPO, BKAPDESC, ISNOTES, BKAPPOL |
| SMJG | &G - Purge/Archive QC Receipts | T7SMJG.RWN | T7SMJG.DFM | BKQCMSTR, BKQCTRAN, ISNOTES, ISLINKS |
| SMJH | &H - Purge Data Collection File | t7smjh.rwn | T7SMJH.DFM | BKDCLAB, BKSYHELP, DBAHLPID, ISIS |
| SMJI | &I - Purge/Archive Estimates | T7SMJI.RWN | T7SMJI.DFM | ISESTDTL, BKARINV, BKARINVL, BKBMMSTR |
| SMJJ | &J - Purge or Archive Closed Sales Orders | T7smjj.rwn | T7SMJJ.DFM | BKARINV, BKARINVT, BKARINVL, BKAPDESC |
| SMJK | &K - Purge or Archive Invoice History | t7smjk.rwn | STUB.DFM | MKAHIST, BKARINVT, BKARINVL, BKAPDESC |
| SMJL | &L - Change/Merge Item Numbers | t7smjl.rwn | T7SMJL.DFM | MTICMSTR, SERIAL, BKAPPOL, BKARINVL |
| SMJM | &M - Change/Merge Customer Codes | t7smjm.rwn | T7SMJM.DFM | BKARCUST, BKARINVT, BKARINVV, BKICPMAT |
| SMJN | &N - Change/Merge Vendor Codes | t7smjn.rwn | T7SMJN.DFM | BKAPVEND, BKCMVNDH, BKCMVNDF, BKICTAX |
| SMJO | &O - Rebuild Customer/Vendor Credit Info | t7smjo.rwn | T7SMJO.DFM | BKAPVEND, BKARCUST, BKAPCHKF, BKARINVT |
| SMJP | &P - Purge or Archive Service RMA Orders | t7smjp.rwn | STUB.DFM | MKAHIST, BKARCUST, BKAPCHKF, BKARINVT |
| SMJQ | &Q - BOM Recursion Utility | t7smjq.rwn | T7SMJQ.DFM | BKSYMSTR, BKICMSTR, BKBMMSTR, BKSYHELP |
| SMJR | &R - Archive Purchase Orders | t7smjr.rwn | T7SMJR.DFM | BKAPPO, BKAPDESC, ISNOTES, BKAPPOL |
| SMJS | &S - Purge Inventory Audit Info | t7smjs.rwn | T7SMJS.DFM | BKICMSTR, MTICMSTR, BKSYHELP, DBAHLPID |
| SMJT | &T - Purge or Archive Sales Quotes | t7smjt.rwn | STUB.DFM | MKAHIST, MTICMSTR, BKSYHELP, DBAHLPID |
| SMJU | &U - Configure Vendor User Defined | T7APINFO.RWN | T7APINFO.DFM | BKAPVND2, BKAPVEND, BKSYHELP, DBAHLPID |
| SMJV | &V - Archive Inventory Transactions | T7INVARCH.RWN | T7INVARCH.DFM | ISGLDATE, INVTXN, BKICMSTR, BKSYHELP |
| SMK | &K - Evo User Settings | T7SMK.RWN | T7SMK.DFM | LANGDICT, ISNUMBER, BKSYMSTR, MKAHIST |
| SMN | &N - Evo Notes Maintenance | *(group)* |  |  |
| SMNA | &A - Enter Note Types | T7SMN.RWN | T7SMNA.DFM | ISNTYPE, ISNOTES, BKSYHELP, DBAHLPID |
| SMNB | &B - Enter System Notes | EVONOTES.RWN | EVONOTES.DFM | ISNOTES, ISNTYPE, BKYSMSTR, BKARCUST |
| SMNC | &C - Synchronize Classic Notes to Evo | T7DBA2EVO.RWN | T7DBA2EVO.DFM | BKARCUST, ISNOTES, BKAPVEND, WORKORD |
| SMND | &D - Synchronize Evo Notes to Classic | T7EVO2DBA.RWN | T7EVO2DBA.DFM | BKARCUST, ISNOTES, BKAPVEND, WORKORD |
| SMNE | &E - Archive Evo Notes | EVONOTESARCH.RWN | EVONOTESARCH.DFM | BKSYMSTR, ISNOTES, BKARCUST, BKAPVEND |
| SMNF | &F - Update Evo Notes | T7SMNF.RWN | T7SMNF.DFM | ISNTYPE, ISNOTES, CLASMSTR, ISCATMST |
| SMO | &O - Enter Ship Via Codes | T7SMO.RWN | T7SMO.DFM | ISSHIPCO, BKSYMSTR, CLASMSTR, ISCATMST |
| SMP | &P - Inventory Parameters | *(group)* |  |  |
| SMPA | &A - Category Master Maintenance | t7smpa.rwn | T7SMPA.DFM | ISCATMST, BKSYHELP, DBAHLPID, ISIS |
| SMPB | &B - User Defined Master Maintenance | t7smpb.rwn | T7SMPB.DFM | ISUDMSTR, BKSYHELP, DBAHLPID, ISIS |
| SMPC | &C - Enter QC Codes | T7ROF.RWN | T7ROF.DFM | QCCODES, BKSYHELP, DBAHLPID, ISIS |
| SMPD | &D - Enter Scrap Codes | T7ROG.RWN | T7ROG.DFM | SCRAP, BKGLCOA, BKSYHELP, DBAHLPID |
| SMPE | &E - Define Inventory User Defined Fields | T7UDFINV.RWN | STUB.DFM | ISUDFINV, BKSYHELP, DBAHLPID, ISDRILL |
| SMPF | &F - Enter Job Listing | T7SMPF.RWN | T7SMPF.DFM | ISJOB, BKSYHELP, DBAHLPID, ISIS |
| SMPG | &G - Enter WO Priorities | T7WOPRIO2.RWN | T7WOPRIO2.DFM | ISWOPRIO, BKSYHELP, DBAHLPID, ISIS |
| SMPH | &H - Enter Cycle Codes | T7SMPH.RWN | T7SMPH.DFM | ISCYCLCD, BKSYMSTR, BKSYHELP, DBAHLPID |
| SMPI | &I - Enter Defect Codes | T7SMPI.RWN | T7DEFECT.DFM | ISDEFECT, BKSYHELP, DBAHLPID, ISIS |
| SMR | &R - Multi-Language Maintenance | T7MLC.RWN | T7MLC.DFM | LANGDICT, BKSYHELP, DBAHLPID, MKAHIST |
| SMS | &S - Evo Links | *(group)* |  |  |
| SMSA | &A - Enter Evo Links | EVOLINKS.RWN | EVOLINKS.DFM | ISLINKS, BKYSMSTR, BKICMSTR, BKSYHELP |
| SMSB | &B - Broken Links Report | T7SMSB.RWN | T7SMSB.DFM | ISLINKS, BKSYHELP, DBAHLPID, ISIS |
| SMSC | &C - Vendor Invoice Links Defaults | T7SMSC.RWN | T7SMSC.DFM | ISLINKS, CLASMSTR, ISCATMST, BKSYHELP |
| SMSD | &D - Vendor Invoice Links | T7SMSD.RWN | T7SMSD.DFM | BKAPINVT, ISLINKS, BKAPVEND, CLASMSTR |
| SMT | &T - Enter Java Settings | T7JSETTINGS.RWN | T7JSETTINGS.DFM | FILELOC, BKSYHELP, DBAHLPID, ISIS |
| SMU | &U - Enter Customer Ship Via | T7SMU.RWN | T7SMU.DFM | ISSHPVIA, BKSYMSTR, BKARCUST, BKSYHELP |
| SMV | &V - Download Updates | T7JUPD.RWN |  | FILELOC, BKSYHELP, DBAHLPID, BKPSUSER |

## Module: SO

| Code | Label | Program | DFM | Key Tables |
|------|-------|---------|-----|------------|
| SOA | &A - Enter Sales Orders | T7SOA.RWN | T7SOA.DFM | BKARINV, ISTAXGRP, ISSHPVIA, ISORDECO |
| SOB | &B - Print Acknowledgements | t7sob.rwn | T7SOB.DFM | MTICMSTR, BKARCUST, BKYSMSTR, BKARINV |
| SOC | &C - Print Packing Slips | t7soc.rwn | T7SOC.DFM | MTICMSTR, BKARCUST, BKYSMSTR, BKARINV |
| SOD | &D - Print Shipping Labels | t7sod.rwn | T7SOD.DFM | ISARJDLP, BKARINV, BKARINVL, BKARCUST |
| SOE | &E - Release Sales Orders | t7soe.rwn | T7SOE.DFM | BKARINV, BKARINVL, BKICMSTR, ISSRINFO |
| SOF | &F - Print Invoices | t7sof.rwn | T7SOF.DFM | MTICMSTR, BKARCUST, BKSYMSTR, BKYSMSTR |
| SOG | &G - Post Invoices | t7sog.rwn | T7SOG.DFM | BKYSMSTR, BKARINV, BKARINVL, BKICMSTR |
| SOH | &H - Display Invoice History | t7soh.rwn | STUB.DFM | MKAHIST, BKARINV, BKARINVL, BKICMSTR |
| SOI | &I - Customer Service Inquiry | t7jsoi.rwn | T7JSOI.DFM | BKSYHELP, DBAHLPID, ISIS, MKAHIST |
| SOJ | &J - Enter Recurring Sales Orders | t7soj.rwn | STUB.DFM | MKAHIST, BKYSMSTR, BKARINVL, ISPRINFO |
| SOK | &K - Generate Recurring Sales Orders | t7sok.rwn | T7SOK.DFM | BKARINV, BKARINVL, BKICLOC, BKICMSTR |
| SON | &N - Convert Sales Orders to Work Orders | t7son.rwn | T7SON.DFM | WORKORD, CALENDAR, BKYSMSTR, BKARINV |
| SOO | &O - Reports | *(group)* |  |  |
| SOOA | &A - Print Open Sales Order Listing | t7sooa.rwn | T7SOOA.DFM | BKSYMSTR, BKARINV, BKARINVL, WORKORD |
| SOOB | &B - Print Backorder Listing | t7soob.rwn | T7SOOB.DFM | BKICMSTR, BKARINVL, BKARINV, BKSYHELP |
| SOOC | &C - Reprint Invoice | T7sooc.rwn | STUB.DFM | BKICMSTR, BKARINVL, BKARINV, BKSYHELP |
| SOOD | &D - Print Commissions by Sales Order | t7sood.rwn | T7SOOD.DFM | BKSYMSTR, BKARINV, BKARINVL, BKSYHELP |
| SOOE | &E - Print Shipping Schedule | t7sooe.rwn | T7SOOE.DFM | BKSYMSTR, ISBUILD, BKARINV, BKARINVL |
| SOOF | &F - Print Available to Ship | t7soof.rwn | T7SOOF.DFM | BKSYMSTR, BKARINVL, BKICMSTR, BKICLOC |
| SOOG | &G - Print Sales Order/Work Order Schedu | t7soog.rwn | T7SOOG.DFM | BKSYMSTR, BKARINV, BKARINVL, BKICMSTR |
| SOOH | &H - Print Invoice Listing | t7sooh.rwn | T7SOOH.DFM | BKSYMSTR, BKARINV, BKISTAX, BKARCUST |
| SOOI | &I - Print Released Sales Orders | t7sooi.rwn | T7SOOI.DFM | BKSYMSTR, BKARINV, BKARINVL, BKICMSTR |
| SOOJ | &J - Print User-Defined Detail | t7sooj.rwn | STUB.DFM | BKSYMSTR, BKARINV, BKARINVL, BKICREF |
| SOOK | &K - Print User-Defined Summary | t7sook.rwn | STUB.DFM | BKSYMSTR, BKARINV, BKARINVL, BKICREF |
| SOOM | &M - Print Changes to Sales Orders | t7soom.rwn | T7SOOM.DFM | BKSYMSTR, ISARCHG, BKARINV, BKSYHELP |
| SOON | &N - Print On Time Delivery Performance | t7soon.rwn | T7SOON.DFM | BKSYMSTR, ISBUILD, ISARCHG, BKARINV |
| SOP | &P - Sales Quotes and Misc. | *(group)* |  |  |
| SOPA | &A - Enter Sales Quotations | t7sopa.rwn | STUB.DFM | MKAHIST, ISBUILD, ISARCHG, BKARINV |
| SOPB | &B - Print Sales Quotations | t7sopb.rwn | T7SOPB.DFM | MTICMSTR, BKARCUST, BKYSMSTR, BKARINV |
| SOPC | &C - Convert Sales Quotations | t7sopc.rwn | T7SOPC.DFM | BKYSMSTR, BKARINV, BKARINVL, ISICMSTR |
| SOPD | &D - Sales Quotation Detail Report | t7sopd.rwn | STUB.DFM | BKYSMSTR, BKARINV, BKARINVL, ISICMSTR |
| SOPE | &E - Sales Quotation Summary Report | t7sope.rwn | STUB.DFM | BKYSMSTR, BKARINV, BKARINVL, ISICMSTR |
| SOPF | &F - Release Blanket Order | T7SOPF.RWN | T7SOPF.DFM | BKARINV, BKARINVL, BKMRPFC, BKICMSTR |
| SOPI | &I - Enter Freight & Tracking Information | t7sopi.rwn | T7SOPI.DFM | BKARINV, ISSOBOX, BKAPDESC, BKARCUST |
| SOPJ | &J - Post Shipped Items | t7sopj.rwn | T7SOPJ.DFM | INVTXN, BKICMSTR, BKICLOC, MTICMSTR |
| SOPK | &K - Edit Posted Invoice | t7sopk.rwn | T7SOPK.DFM | BKARINV, BKARCUST, ISSHPVIA, ISTAXGRP |
| SOPL | &L - Print Changes to Quotes | t7sopl.rwn | STUB.DFM | BKARINV, BKARCUST, ISSHPVIA, ISTAXGRP |
| SOPM | &M - Converted Quote Report | t7sopm.rwn | T7SOPM.DFM | BKSYMSTR, BKARINV, BKARCUST, BKSYHELP |
| SOPN | &N - Convert SO to PO | t7sopo.rwn | T7SOPO.DFM | MTICMSTR, BKYSMSTR, BKARINV, BKARINVL |
| SOPP | &P - Edis Estimated Ship Dates | t7sopp.rwn | T7SOPP.DFM | BKARCUST, BKARINV, ISBUILD, BKARINVL |
| SOQ | &Q - Pricing | *(group)* |  |  |
| SOQA | &A - Enter Base Prices | t7soqa.rwn | T7SOQA.DFM | BKICMSTR, MTICMSTR, ISICMSTR, BKICPMAT |
| SOQB | &B - Print Base Prices | t7soqb.rwn | T7SOQB.DFM | BKSYMSTR, BKICMSTR, MTICMSTR, BKSYHELP |
| SOQC | &C - Global Price Change | t7soqc.rwn | T7SOQC.DFM | BKICMSTR, MTICMSTR, ISICMSTR, BKICPMAT |
| SOQD | &D - Enter Price Codes | t7soqd.rwn | STUB.DFM | MKAHIST, MTICMSTR, ISICMSTR, BKICPMAT |
| SOQE | &E - Print Price Codes | t7soqe.rwn | STUB.DFM | MKAHIST, MTICMSTR, ISICMSTR, BKICPMAT |
| SOQF | &F - Enter Discount Codes | t7soqf.rwn | STUB.DFM | MKAHIST, MTICMSTR, ISICMSTR, BKICPMAT |
| SOQG | &G - Print Discount Codes | t7soqg.rwn | STUB.DFM | MKAHIST, MTICMSTR, ISICMSTR, BKICPMAT |
| SOQH | &H - Enter Contract Prices | t7soqh.rwn | T7SOQH.DFM | BKICPMAT, BKARCUST, BKICMSTR, BKYSMSTR |
| SOQI | &I - Print Contract Prices | t7soqi.rwn | T7SOQI.DFM | BKSYMSTR, BKICMSTR, BKICPMAT, MTICMSTR |
| SOQJ | &J - Generate Base Prices | t7soqj.rwn | T7SOQJ.DFM | BKSYMSTR, BKICMSTR, MTICMSTR, BKICPMAT |
| SOQK | &K - Print Catalog | t7soqk.rwn | T7SOQK.DFM | BKICMSTR, MTICMSTR, BKSYMSTR, ISBUILD |
| SOQL | &L - SO Price Change | t7soql.rwn | T7SOQL.DFM | BKSYMSTR, BKICMSTR, BKARINVL, BKARINV |
| SOR | &R - Void Invoice | t7sor.rwn | T7SOR.DFM | BKARINV, BKSOLOCK, BKARINVL, MTICMSTR |
| SOS | &S - Mass Release Sales Orders | T7sos.rwn | T7SOS.DFM | BKICMSTR, BKARINV, BKARCUST, BKARINVL |
| SOT | &T - Sales Order Inquiry | T7SOT.rwn | STUB.DFM | MKAHIST, BKARINV, SERIAL, BKICLOC |
| SOU | &U - Sales Order Defaults | T7DSSO.RWN | STUB.DFM | ISDROP, BKSYHELP, DBAHLPID, ISIS |

## Module: SR

| Code | Label | Program | DFM | Key Tables |
|------|-------|---------|-----|------------|
| SRA | &A - Enter Service/Repair | T7SRA.RWN | STUB.DFM | MKAHIST, ISSDET, WORKORD, ISSPC |
| SRB | &B - Print Service/Repair | T7SRB.RWN | T7SRB.DFM | MTICMSTR, BKARCUST, BKYSMSTR, BKARINV |
| SRC | &C - Convert S/R to Work Order | T7SRC.RWN | STUB.DFM | BKARINV, BKARINVL, MTICMSTR, BKSYHELP |
| SRD | &D - Print S/R Packing Slips | T7SRD.RWN | T7SRD.DFM | BKSYMSTR, MTICMSTR, BKYSMSTR, BKARINV |
| SRE | &E - Release Service/Repairs | T7SRE.RWN | T7SRE.DFM | BKARINV, BKARINVL, BKYSMSTR, BKSYMSTR |
| SRF | &F - Print S/R Invoices | T7SRF.RWN | T7SRF.DFM | MTICMSTR, BKSYMSTR, BKYSMSTR, BKARINV |
| SRG | &G - Post S/R Invoices | T7SRG.RWN | T7SRG.DFM | BKYSMSTR, BKARINV, BKSYHELP, DBAHLPID |
| SRH | &H - RMA & Service & Repair Defaults | T7DSRMA.RWN | STUB.DFM | ISDROP, BKSYHELP, DBAHLPID, ISIS |
| SRI | &I - Void S/R Invoice | T7SRI.RWN | T7SRI.DFM | BKARINV, BKSOLOCK, BKARINVL, MTICMSTR |

## Module: SU

| Code | Label | Program | DFM | Key Tables |
|------|-------|---------|-----|------------|
| SUA | &A - Maintain Grid Lookups | wbklugrid.rwn | WBKLUGRID.DFM | BKLUGRID, FILELOC, FILEKNUM, FILEDICT |
| SUB | &B - Maintain Drill Down Menus | evoerpdrillm.rwn | EVOERPDRILLM.DFM | ISDRILLM, BKLUGRID, FILELOC, FILEDICT |
| SUC | &C - Forms Editor | reports.int |  |  |
| SUD | &D - Grid Maintenance | t7gdm.rwn | T7GDM.DFM | BKLUGRID, ISDRILLM, BKSYHELP, DBAHLPID |

## Module: TA

| Code | Label | Program | DFM | Key Tables |
|------|-------|---------|-----|------------|
| TAA | &A - Run TAS Program | RUNPRG.INT |  |  |
| TAB | &B - Change Company Code | GETCO.INT |  |  |
| TAC | &C - Set Configuration | CONFIG.INT |  |  |
| TAD | &D - Maintain Database | WTASDATAM.RWN | WTASDATAM.DFM | FILELOC, FILEDICT, FILEKNUM, FILEKEY |
| TAE | &E - Initialize Database | WTASINIT.RWN | WTASINIT.DFM | FILELOC, FILEDICT, FILEKNUM, FILEKEY |
| TAF | &F - Maintain Location File | WTASFLOC.RWN | WTASFLOC.DFM | FILELOC, FILEDICT, FILEKEY, FILEKNUM |
| TAG | &G - Maintain Menu Access Records | WBKMENUSETUP.RWN | WBKMENUSETUP.DFM | BKPSUSER, BKMENUSU, BKSYHELP, DBAHLPID |
| TAH | &H - Maint Menu Access - End User | WBKMENUSUEU.RWN | WBKMENUSUEU.DFM | BKMENUSU, BKSYHELP, DBAHLPID, ISLOG |
| TAI | &I - Update File Structures | WTASMERGE.RWN | WTASMERGE2.DFM | FILELOC, FILEDICT, FILEDBF, FILEKEY |
| TAM | &M - RTM Editor | REPORTS.INT |  |  |
| TAN | &N - Program Scheduler | evoscheduler.rwn | EVOSCHEDULER.DFM | ISSCHED, FILELOC, BKSYMSTR, BKSYHELP |
| TAO | &O - Backup Utility | EvoERPbackup.rwn | EVOERPBACKUP.DFM | MKAHIST, FILELOC, BKSYMSTR, BKSYHELP |
| TAP | &P - Change Password | PASSWORD.INT |  |  |
| TAQ | &Q - Change Logo Image | Evologo.rwn | EVOLOGO.DFM | BKSYMSTR, BKSYHELP, DBAHLPID, LANGDICT |
| TAR | &R - SQL Editor | T7JSQL.RWN | T7JSQL.DFM | BKSYHELP, DBAHLPID, ISIS, MKAHIST |
| TAS | &S - Data Dictionary Check | T7DDCHECK.RWN | T7DDCHECK.DFM | FILEDICT, FILEKEY, FILELOC, BKSYHELP |

## Module: US

| Code | Label | Program | DFM | Key Tables |
|------|-------|---------|-----|------------|
| USA | &A - Customize Settings | T7SMK.RWN | T7SMK.DFM | LANGDICT, ISNUMBER, BKSYMSTR, MKAHIST |
| USB | &B - Customize Menu | WBKMENUSUEU.RWN | WBKMENUSUEU.DFM | BKMENUSU, BKSYHELP, DBAHLPID, ISLOG |
| USC | &C - Reset Screen Size/Locations | t7resetdfm.RWN | T7RESETDFM.DFM | ISREPLNK, BKPRSALE, BKARCUST, BKICMSTR |
| USD | &D - Change Password | PASSWORD.INT |  |  |
| USE | &E - Update PO Electronic Signature Info | T7DIGSIG.RWN | T7DIGSIG.DFM | BKAPPO, BKAPPOL, ISDIGSIG, BKPRMSTR |
| USF | &F - Enter Reminders | calrem.rwn | CALREM.DFM | BKYSMSTR, ISREMIND, BKARCUST, BKAPVEND |
| USG | &G - Enter Triggers | T7USG.RWN | T7USG.DFM | ISTRIGRS, BKPSUSER, BKSYUSER, BKICMSTR |
| USH | &H - Update Contract Review Password | T7CTREVU.RWN | T7CTREVU.DFM | ISCTREVU, BKARINV, ISSOREVU, BKSYHELP |

## Module: UT

| Code | Label | Program | DFM | Key Tables |
|------|-------|---------|-----|------------|
| UTA | &A - Run a DBA Program | runprg.int |  |  |
| UTC | &C - Re-Index File | t7reindex.rwn | T7REINDEX.DFM | FILELOC, BKSYHELP, DBAHLPID, ISIS |
| UTD | &D - Edit Data Location File | wtasfloc.rwn | WTASFLOC.DFM | FILELOC, FILEDICT, FILEKEY, FILEKNUM |
| UTE | &E - Set System Configuration | config.int |  |  |
| UTH | &H - Print File Layouts | t7uth.rwn | T7UTH.DFM | FILELOC, FILEDICT, FILEKEY, BKSYHELP |
| UTI | &I - Create/Delete Company | t7uti.rwn | T7UTI.DFM | BKPSUSER, BKSYUSER, FILELOC, BKSYAP |
| UTK | &K - File Maintenence Programs | *(group)* |  |  |
| UTKA | &A - Clear Data | t7utka.rwn | T7UTKA.DFM | FILELOC, BKSYMSTR, ISIS, BKSYAP |
| UTKB | &B - Search and Replace | T7FNR.RWN | T7FNR.DFM | FILELOC, FILEDICT, BKSYHELP, DBAHLPID |
| UTKD | &D - Recalc GL Chart of Accounts | t7utkd.rwn | T7UTKD.DFM | BKICMSTR, BKGLCOA, BKSYMSTR, ISGLDATE |
| UTKE | &E - Consolidate Inventory Locations | T7UTKE.RWN | T7UTKE.DFM | BKYSMSTR, BKICLOCM, BKICLOC, BKICMSTR |
| UTKF | &F - Set Avg and Last Cost to Std Cost | t7utkf.rwn | T7UTKF.DFM | BKSYMSTR, BKICMSTR, MTICMSTR, INVTXN |
| UTKG | &G - Recalc Inventory Book Value | t7utkg.rwn | T7UTKG.DFM | BKSYMSTR, BKICMSTR, MTICMSTR, BKYSMSTR |
| UTKH | &H - Recalc Avg Cost fr FIFO/LIFO Bucket | T7UTKH.RWN | T7UTKH.DFM | BKSYMSTR, BKYSMSTR, BKICMSTR, MTICMSTR |
| UTKI | &I - Fix Binary Zeroes | t7bzfix.rwn | T7BZFIX.DFM | FILELOC, FILEDICT, BKSYHELP, DBAHLPID |

## Module: WC

| Code | Label | Program | DFM | Key Tables |
|------|-------|---------|-----|------------|
| WCA | &A - Enter Warehouse Bin Locations | T7WCA.RWN | T7WCA.DFM | BKICLOCM, ISBNMSTR, BKYSMSTR, ISBINLOC |
| WCB | &B - Assign Warehouse Control | T7WCB.RWN | T7WCB.DFM | BKYSMSTR, BKICLOCM, BKICLOC, BKICMSTR |
| WCC | &C - Assign Bins to Items | T7WCC.RWN | T7WCC.DFM | SERIAL, BKICMSTR, BKICLOCM, ISBINLOT |
| WCE | &E - Print Bin Inventory Listing | T7WCE.RWN | T7WCE.DFM | BKSYMSTR, BKYSMSTR, ISBINLOC, MTICMSTR |
| WCF | &F - Print Bin Inventory Exceptions | T7WCF.RWN | T7WCF.DFM | BKSYMSTR, BKYSMSTR, BKICMSTR, MTICMSTR |
| WCG | &G - Warehouse Control Defaults | T7DSWC.RWN | STUB.DFM | ISDROP, BKSYHELP, DBAHLPID, ISIS |

## Module: WO

| Code | Label | Program | DFM | Key Tables |
|------|-------|---------|-----|------------|
| WOA | &A - Enter Work Orders | t7woa.rwn | T7WOA.DFM | WORKORD, MTICMSTR, ISWOEX, ISWOPRIO |
| WOB | &B - Release Work Orders | t7wob.rwn | T7WOB.DFM | ISWOPRIO, WORKORD, ISWOEX, BKICMSTR |
| WOC | &C - Print Travelers | t7woc.rwn | T7WOC.DFM | BKSYMSTR, MTICMSTR, WORKORD, WOROUT |
| WOD | &D - Print Pick Lists | t7wod.rwn | T7WOD.DFM | BKYSMSTR, WORKORD, BKICMSTR, BKSYMSTR |
| WOE | &E - Print Labor Cards/Labels | t7woe.rwn | T7WOE.DFM | WOROUT, WORKORD, BKSYHELP, DBAHLPID |
| WOF | &F - Enter Labor | T7WOF.RWN | T7WOF.DFM | WOLABOR, WOROUT, BKPSUSER, BKYSMSTR |
| WOG | &G - Issue Materials | t7wog.rwn | T7WOG.DFM | WOMAT, WORKORD, WOBOM, MTICMSTR |
| WOH | &H - Enter Misc/Extra Costs | T7WOH.RWN | T7WOH.DFM | WOEXCHG, WORKORD, BKSYMSTR, BKYSMSTR |
| WOI | &I - Enter Finished Production | t7woi.rwn | T7WOI.DFM | WORECV, WORKORD, BKICMSTR, MTICMSTR |
| WOJ | &J - Close/Cancel Work Orders | t7woj.rwn | T7WOJ.DFM | MTICMSTR, WORKORD, WOROUT, BKYSMSTR |
| WOK | &K - Work Order Maintenance Programs | *(group)* |  |  |
| WOKA | &A - Enter Work Order Routings | T7WOKA.RWN | T7WOKA.DFM | WORKORD, WOROUT, WORKCTR, MACHINE |
| WOKB | &B - Enter Work Order Bills of Material | t7wokb.rwn | T7WOKB.DFM | WOBOM, BKICMSTR, WORKORD, MTICMSTR |
| WOKC | &C - Create Multi-Date Work Orders | t7wokc.rwn | T7WOKC.DFM | WORKORD, WODATE, WOEXCHG, WOBOM |
| WOKD | &D - Create Multi-Assy Work Orders | t7wokd.rwn | T7WOKD.DFM | MTICMSTR, WORKORD, ISWOEX, BKICMSTR |
| WOKE | &E - Swap Substitute Parts | T7WOKE.RWN | T7WOKE.DFM | BKICMSTR, MTICMSTR, BKICLOC, WORKORD |
| WOKF | &F - Edit Sequence Started/Finished Date | t7wokf.rwn | T7WOKF.DFM | WOROUT, BKSYHELP, DBAHLPID, ISIS |
| WOKG | &G - Recalculate Projected Hours | t7wokg.rwn | T7WOKG.DFM | BKYSMSTR, WORKORD, WOROUT, WORKCTR |
| WOKH | &H - Rebuild Work Order Costs | t7rebwo.rwn | T7REBWO.DFM | WORKORD, WOBOM, WORECV, WOROUT |
| WOKI | &I - Kitting System | t7kit.rwn | T7KIT.DFM | BKICMSTR, MTICMSTR, WOBOM, BKICLOC |
| WOKJ | &J - Synch WO BOM and Routing | j7ptwoki.rwn | STUB.DFM |  |
| WOKK | &K - Edit Posted DC Labor | t7wokk.rwn | T7WOKK.DFM | BKDCLAB, WORKORD, BKPRMSTR, WOROUT |
| WOKL | &L - Quick Work Order | T7WOKL.RWN | T7WOKL.DFM | BKYSMSTR, BKSYMSTR, BKARINVL, BKICMSTR |
| WOKM | &M - Parts Requester | t7wokm.rwn | T7WOKM.DFM | SCRAP, WORKORD, ISPREQ, WOROUT |
| WOKN | &N - Stockroom Program | t7wokn.rwn | STUB.DFM | MKAHIST, BKSYHELP, DBAHLPID, ISIS |
| WOKO | &O - Map Component Serial to Parent | T7WOKO.RWN | T7WOKO.DFM | ISSERIAL, BKICMSTR, WORKORD, MTICMSTR |
| WOKP | &P - Map Component Lot to Parent | T7WOKP.RWN | T7WOKP.DFM | ISSERIAL, BKICMSTR, WORKORD, MTICMSTR |
| WOKQ | &Q - Convert WO to PO | T7WOPO.RWN | T7WOPO.DFM | MTICMSTR, BKYSMSTR, WOBOM, BKICMSTR |
| WOKR | &R - Issue Scrap Component | t7hhwoscrap.rwn | T7HHWOSCRAP.DFM | BKSHORT, BKYSMSTR, WOBOM, BKICMSTR |
| WOKS | &S - Assign WO to Bin | t7woks.rwn | T7WOKS.DFM | WORKORD, WOROUT, ISWOTRAY, BKSYMSTR |
| WOKT | &T - Print Issued Part Requests | t7wokt.rwn | T7WOKT.DFM | BKICMSTR, MTICMSTR, WORKORD, BKPRMSTR |
| WOL | &L - Reports | *(group)* |  |  |
| WOLA | &A - Print Work Order Status | t7wola.rwn | T7WOLA.DFM | BKSYMSTR, BKYSMSTR, MTICMSTR, WORKORD |
| WOLB | &B - Print Work Order Schedule | t7wolb.rwn | T7WOLB.DFM | BKSYMSTR, MTICMSTR, ISNTYPE, WORKORD |
| WOLC | &C - Print Work Center Backlog | t7wolc.rwn | T7WOLC.DFM | ISBUILD, WORKCTR, WOROUT, WORKORD |
| WOLD | &D - Print Projected Shipments | t7wold.rwn | T7WOLD.DFM | BKSYMSTR, WORKORD, BKICMSTR, MTICMSTR |
| WOLE | &E - Print/Post Labor to Payroll | t7wole.rwn | T7WOLE.DFM | BKSYMSTR, BKYSMSTR, BKCPMSTR, WOLABOR |
| WOLF | &F - Print Work Order Shortages | t7wolf.rwn | T7WOLF.DFM | BKSYMSTR, MTICMSTR, WORKORD, BKICMSTR |
| WOLG | &G - Print Work Center by Key Component | bkwolg.run |  |  |
| WOLH | &H - Print Projected vrs Estimated hrs | t7wolh.rwn | T7WOLH.DFM | BKSYMSTR, BKYSMSTR, WORKORD, WOROUT |
| WOLI | &I - Print Allocations | T7woli.rwn | T7WOLI.DFM | BKSYMSTR, BKICMSTR, ISBUILD, MTICMSTR |
| WOLJ | &J - Print Work Order Completions | t7wolj.rwn | T7WOLJ.DFM | BKSYMSTR, WORKORD, BKICMSTR, WOROUT |
| WOLK | &K - Print Work Order Bill of Materials | t7wolk.rwn | T7WOLK.DFM | BKSYMSTR, BKYSMSTR, WORKORD, WOBOM |
| WOLL | &L - Print Work Order Component Labels | j7woll.rwn | STUB.DFM |  |
| WOLM | &M - Print Material Summary | t7wolm.rwn | T7WOLM.DFM | BKSYMSTR, BKARINV, BKARINVL, WORKORD |
| WOLN | &N - WO BOM for Purchasing | t7woln.rwn | T7WOLN.DFM | BKSYMSTR, WOBOM, BKAPPOL, WORKORD |
| WOM | &M - Batch Labor Entry | t7wom.rwn | STUB.DFM | MKAHIST, WOBOM, BKAPPOL, WORKORD |
| WON | &N - Post Labor Batches | t7dch.rwn | T7DCH.DFM | BKDCLAB, BKDCCFG, BKPRMSTR, WORKORD |
| WOO | &O - Post Material Issues | t7dejh.rwn | T7DEJH.DFM | WOMAT, WORKORD, WOBOM, BKICMSTR |
| WOP | &P - Batch Finished Production | t7wop.rwn | T7WOP.DFM | WORKORD, BKYSMSTR, WOBOM, BKICMSTR |
| WOQ | &Q - Work Order Inquiry | T7WOT.rwn | STUB.DFM | MKAHIST, WORKORD, BKSYHELP, DBAHLPID |
| WOR | &R - Work Order Defaults | T7DSWO.RWN | STUB.DFM | ISDROP, BKSYHELP, DBAHLPID, ISIS |
| WOS | &S - Print WOrk Order Labels | T7WOS.RWN | T7WOS.DFM | ISSOBOX, WORKORD, MTICMSTR, WORECV |
| WOT | &T - Enter Rework Work Order | T7WOTRWK.RWN | T7WOTRWK.DFM | BKYSMSTR, BKSYMSTR, BKICMSTR, MTICMSTR |

