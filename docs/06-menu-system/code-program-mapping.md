# Menu Code → Program → Database Table Mapping

Status: **verified** — built from `BKMENUSU.TXT` (870 entries) cross-referenced against
`rwn_symbols.json` (1,122 decrypted RWN programs). Last updated: 2026-06-19.

Columns: **Code** | **Label** | **Program** | **Key DB Tables** (up to 4 primary)

> **BU / GR entries** are navigation groups (no program to launch).

---

## Module: AD

| Code | Label | Program | Key Tables |
|------|-------|---------|------------|
| ADA | &A - General Ledger Defaults | T7DSGL.rwn | ISDROP, BKSYHELP, DBAHLPID, ISIS |
| ADB | &B - Checking Accounts Defaults | T7DSCK.rwn | ISDROP, BKSYHELP, DBAHLPID, ISIS |
| ADC | &C - Accounts Payable Defaults | T7DSAP.rwn | ISDROP, BKSYHELP, DBAHLPID, ISIS |

## Module: AM

| Code | Label | Program | Key Tables |
|------|-------|---------|------------|
| AMA | &A - Reset Period-End Close Date | t7ama.rwn | BKSYMSTR, MKAHIST, BKYSMSTR, BKGLTRAN |
| AMB | &B - Fiscal Year End Routines | t7amb.rwn | BKGLCOA, ISGLCOA, BKSYMSTR, ISGLDATE |
| AMC | &C - Enter General Ledger Accounts | T7AMC.RWN | BKGLCOA, ISGLDATE, ISGLCOA, BKGLTRAN |
| AMD | &D - Enter General Ledger Departments | t7amd.rwn | BKGLCOA, ISGLCOA, BKSYHELP, DBAHLPID |
| AME | &E - Format Standard Financial Statement | t7ame.rwn | BKGLSTMT, BKSYHELP, DBAHLPID, ISIS |
| AMF | &F - Format Custom Financial Statements | t6amf.run |  |
| AMG | &G - Consolidate Financials | t7amg.rwn | BKSYMSTR, FILELOC, ISMCF, BKGLCOA |
| AMH | &H - Change GL Account Codes | t7amh.rwn | BKGLCOA, ISGLCOA, ISGLNBGT, BKGLTRAN |
| AMI | &I - Consolidate General Ledger Detail | t7ami.rwn | BKGLCOA, BKGLTRAN, ISGLDATE, BKSYMSTR |
| AMJ | &J - Purge/Archive AP History | t7amj.rwn | BKAPCHKF, BKAPINVT, BKAPINVL, BKISTAX |
| AMK | &K - Purge/Archive AR History | t7amk.rwn | BKARINVT, BKART, BKAPCHKF, BKARINVI |
| AMN | &N - Maintain GL Fiscal Periods | T7AMN.RWN | ISGLDATE, BKSYMSTR, BKSYHELP, DBAHLPID |
| AMO | &O - Purge/Archive Vendor Data | t7amo.rwn | BKSYMSTR, BKAPPO, BKAPPOL, BKAPVEND |
| AMP | &P - Purge/Archive Customer Data | t7amp.rwn | BKSYMSTR, BKARINV, BKARINVL, BKARCUST |
| AMQ | &Q - Enter Budget Amounts | t7amq.rwn | ISGLCOA, ISGLDATE, BKGLCOA, ISGLNBGT |
| AMR | &R - Out of Balance Report | T7GLOOB.RWN | BKGLTRAN, BKSYHELP, DBAHLPID, ISIS |
| AMS | &S - Purge/Archive GL Journals | t7ams.rwn | BKSYMSTR, BKGLGJRN, BKGLGJLN, BKSYHELP |
| AMT | &T - Archive GL Transaction Detail | T7GLARCH.RWN | BKSYMSTR, ISGLDATE, BKGLTRAN, BKSYHELP |

## Module: AP

| Code | Label | Program | Key Tables |
|------|-------|---------|------------|
| APA | &A - Enter Vendors | t7apa.rwn | BKAPVEND, BKAPVND2, ISTAXGRP, ISEXUSER |
| APB | &B - Enter Vouchers | t7apb.rwn | BKAPINVL, BKAPINVT, BKAPVEND, BKYSMSTR |
| APC | &C - Enter Purchase Order Invoices | t7apc.rwn | BKAPVEND, BKQCMSTR, BKAPPOL, BKAPPO |
| APD | &D - Enter Scheduled Payment Dates | t7apd.rwn | BKAPVEND, BKAPINVT, ISTERMS, BKSYHELP |
| APE | &E - Print Vouchers/Invoices Due by Date | t7ape.rwn | BKSYMSTR, BKAPINVT, ISMCF, BKAPVEND |
| APF | &F - Pick Vouchers/Invoices to Pay | t7apf.rwn | BKAPVEND, BKYSMSTR, BKAPCHKF, BKAPINVT |
| APG | &G - Print Pro Forma Check Register | t7apg.rwn | BKSYMSTR, BKYSMSTR, BKAPCHKF, BKAPVEND |
| APH | &H - Print Checks | t7aph.rwn | BKYSMSTR, BKAPCHKF, ISBANKS, ISMCF |
| API | &I - Print Aging | t7api.rwn | BKSYMSTR, BKYSMSTR, BKAPINVT, BKAPVEND |
| APJ | &J - Print Vendor Code and Name | t7apj.rwn | BKAPVEND, ISAPEX, BKSYHELP, DBAHLPID |
| APK | &K - Print Vendor General Info | t7apk.rwn | BKSYMSTR, BKAPVEND, BKAPVND2, CLASMSTR |
| APL | &L - Print Vendor Purchase Info | t7apl.rwn | BKSYMSTR, BKAPVEND, BKSYHELP, DBAHLPID |
| APM | &M - Print Vendor Labels | t7apm.rwn | BKAPVEND, BKSYHELP, DBAHLPID, BKYSMSTR |
| APN | &N - Enter Vouchers (Edit Address) | t7apn.rwn | MKAHIST, BKSYHELP, DBAHLPID, BKYSMSTR |
| APO | &O - Enter Recurring Vouchers | t7apo.rwn | MKAHIST, BKSYHELP, DBAHLPID, BKYSMSTR |
| APP | &P - Generate Recurring Vouchers | t7app.rwn | BKAPINVL, BKSYMSTR, BKAPVEND, BKYSMSTR |
| APQ | &Q - Void AP Check | t7apq.rwn | BKAPVEND, BKSYMSTR, BKYSMSTR, BKAPCHKF |
| APR | &R - Print AP Payment History | t7apr.rwn | BKYSMSTR, ISBANKS, ISBUILD, BKAPCHKF |
| APS | &S - Print 1099 Forms | t7aps.rwn | BKSYMSTR, BKAPVEND, BKAPVND2, BKAPCHKF |
| APT | &T - AP Check Inquiry | T7APT.RWN | BKAPVEND, BKAPCHKF, BKAPINVT, BKAPPO |
| APU | &U - View Vendor Information | T7APU.RWN | MKAHIST, BKAPCHKF, BKAPINVT, BKAPPO |
| APV | &V - Enter Vendor Deposit | T7APV.RWN | BKARDEP, BKAPINVT, BKAPVEND, BKAPPO |
| APW | &W - Accounts Payable Defaults | T7DSAP.RWN | ISDROP, BKSYHELP, DBAHLPID, ISIS |
| APX | &X - Print Invoice Details | T7APX.RWN | BKAPINVT, ISLINKS, BKAPPOL, BKAPPO |
| APY | &Y - Remittance Options | *(group)* |  |
| APYA | &A - Print Remittance Advice | T7APY.RWN | BKSYMSTR, ISBANKS, BKGLCHK, BKYSMSTR |
| APYB | &B - Positive Pay | T7APYB.RWN | BKSYMSTR, ISBANKS, BKPRCURP, BKPRMSTR |
| APYC | &C - NACHA Upload | T7APYC.RWN | BKSYMSTR, ISBANKS, BKGLCHK, BKAPVEND |
| APZ | &Z - Reports | *(group)* |  |
| APZA | &A - Top Vendor Listing | t7apza.rwn | BKSYMSTR, CLASMSTR, BKCMTERR, ISBUILD |

## Module: AR

| Code | Label | Program | Key Tables |
|------|-------|---------|------------|
| ARA | &A - Enter Customers | t7ara.rwn | BKARCUST, ISAREX, ISTAXGRP, BKCMDUNH |
| ARB | &B - Enter Vouchers | t7arb.rwn | BKARCUST, BKARINVV, ISNOTES, BKSYMSTR |
| ARC | &C - Record Payments | t7arc.rwn | BKARCUST, BKSYMSTR, BKARINV, BKARINVT |
| ARD | &D - Charge Interest on Invoices | t7ard.rwn | BKSYMSTR, ISMCF, BKARCUST, BKARINVT |
| ARE | &E - Print Statements | t7are.rwn | BKSYMSTR, ISMCF, BKYSMSTR, BKARCUST |
| ARF | &F - Print Aging | t7arf.rwn | BKSYMSTR, BKART, BKYSMSTR, BKARCUST |
| ARG | &G - Print Customer Code and Name | t7arg.rwn | ISTERMS, BKARCUST, BKARINV, BKPRSALE |
| ARH | &H - Print Customer General Info | t7arh.rwn | BKARCUST, BKARINV, ISTERMS, BKSYHELP |
| ARI | &I - Print Customer Mail Labels | t7ari.rwn | BKARCUST, BKARINV, BKSYHELP, DBAHLPID |
| ARK | &K - Print Sales Tax Report | t7ark.rwn | BKSYMSTR, BKISTAX, ISTAXFIL, BKARINV |
| ARL | &L - Transfer Sales Taxes | T7ARL.RWN | BKISTAX, ISTAXFIL, BKYSMSTR, BKAPVEND |
| ARM | &M - Enter Customer Refund | t7arm.rwn | BKAPINVT, BKGLCHK, BKARCUST, BKAPVEND |
| ARN | &N - Enter/Print Customer Deposits | t7arn.rwn | BKARDEP, BKARINV, BKARCUST, BKARINVT |
| ARP | &P - Customer Payment Notification | t7arp.rwn | BKSYMSTR, BKARINVT, BKARCUST, ISTERMS |
| ARQ | &Q - View Customer Information | T7arq.rwn | MKAHIST, BKARINV, BKARCUST, BKARINVT |
| ARR | &R - Print AR Payment History | t7arr.rwn | BKYSMSTR, ISBANKS, BKAPCHKF, BKARINV |
| ARS | &S - Accounts Receivable Defaults | t7dsar.rwn | ISDROP, BKSYHELP, DBAHLPID, ISIS |
| ARU | &U - Update Credit Hold Status | T7ARU.RWN | BKARCUST, BKARINVT, BKSYMSTR, BKSYHELP |

## Module: BM

| Code | Label | Program | Key Tables |
|------|-------|---------|------------|
| BMA | &A - Enter Bills of Material | t7bma.rwn | BKBMREMK, BKBMMSTR, BKYSMSTR, BKPSUSER |
| BMB | &B - Print Bills of Material | t7bmb.rwn | BKYSMSTR, MTICMSTR, BKICMSTR, BKBMMSTR |
| BMC | &C - Print Where Used | t7bmc.rwn | BKYSMSTR, BKICMSTR, BKBMMSTR, MTICMSTR |
| BMD | &D - Print BOM Availability | t7bmd.rwn | BKYSMSTR, BKSYMSTR, BKICMSTR, BKBMMSTR |
| BME | &E - Global Replace | t7bme.rwn | BKSYMSTR, BKICMSTR, BKBMMSTR, BKBMREMK |
| BMF | &F - Global Delete | t7bmf.rwn | BKICMSTR, BKBMMSTR, BKSYHELP, DBAHLPID |
| BMG | &G - Print/Rollup Standard Costs | t7bmg.rwn | BKSYMSTR, MTICMSTR, ISCATMST, BKBMMSTR |
| BMH | &H - Print BOM at Average Cost | t7bmh.rwn | BKYSMSTR, MTICMSTR, BKICMSTR, ISICMSTR |
| BMI | &I - Print Summarized BOM | t7bmi.rwn | BKYSMSTR, BKICMSTR, MTICMSTR, BKBMMSTR |
| BMJ | &J - Enter Approved Substitutes | t7bmj.rwn | BKARCUST, BKSBPART, BKICMSTR, BKSYHELP |
| BMK | &K - Enter Approved Vendors | t7bmk.rwn | BKAPVEND, BKARCUST, BKSBVEND, BKSYMSTR |
| BML | &L - Enter Approved Manufacturers | t7bml.rwn | BKARCUST, BKSBMFG, BKSYMSTR, BKICMSTR |
| BMM | &M - Bill of Materials Defaults | T7DSBOM.RWN | ISDROP, BKSYHELP, DBAHLPID, ISIS |
| BMN | &N - BOM Availability - Tree View | BOMTREE.RWN | BKSYHELP, DBAHLPID, BKPSUSER, ISDRILL |
| BMO | &O - Create/Edit BOM - Tree View | EDITBOMTREE.RWN | BKSYHELP, DBAHLPID, BKPSUSER, ISDRILL |
| BMP | &P - Print BOM Pick List | T7BMP.RWN | BKICMSTR, BKSYMSTR, BKYSMSTR, BKBMMSTR |
| BMQ | &Q - Roll Up Where Used | T7BMQ.RWN | BKICMSTR, BKBMMSTR, MTICMSTR, BKSYHELP |
| BMR | &R - Print BOM for Quoting | T7BMR.RWN | BKSYMSTR, BKICMSTR, BKARINVL, ISBUILD |

## Module: BU

| Code | Label | Program | Key Tables |
|------|-------|---------|------------|
| BUTTONS | Accounting Defaults | AD |  |
| BUTTONS | Accounting Maintenance | AM |  |
| BUTTONS | Accounts Payable | AP |  |
| BUTTONS | Accounts Receivable | AR |  |
| BUTTONS | Bill of Materials | BM |  |
| BUTTONS | Commissions | CS |  |
| BUTTONS | Contact Master | CM |  |
| BUTTONS | Contract Review | CR |  |
| BUTTONS | Data Collection | DC |  |
| BUTTONS | Data Exchange | DE |  |
| BUTTONS | Estimates | ES |  |
| BUTTONS | Features and Options | FO |  |
| BUTTONS | Fixed Assets | FA |  |
| BUTTONS | General Ledger | GL |  |
| BUTTONS | Hand Held Programs | HH |  |
| BUTTONS | International Module | IM |  |
| BUTTONS | Inventory | IN |  |
| BUTTONS | Job Costing | JC |  |
| BUTTONS | Lot Control | LC |  |
| BUTTONS | MRP | MR |  |
| BUTTONS | New Programs | NE |  |
| BUTTONS | Password Security | PS |  |
| BUTTONS | Payroll | PR |  |
| BUTTONS | Physical Inventory | PI |  |
| BUTTONS | Purchase Orders | PO |  |
| BUTTONS | Quality Control | QC |  |
| BUTTONS | Queries & Reports | QU |  |
| BUTTONS | Query & Report Setup | SU |  |
| BUTTONS | RMA | RM |  |
| BUTTONS | Routings | RO |  |
| BUTTONS | Sales Analysis | SA |  |
| BUTTONS | Sales Orders | SO |  |
| BUTTONS | Scheduling | SH |  |
| BUTTONS | Serial Control | SC |  |
| BUTTONS | Service and Repair | SR |  |
| BUTTONS | System Configuration | TAS |  |
| BUTTONS | System Defaults | SD |  |
| BUTTONS | System Maintenance | SM |  |
| BUTTONS | User Settings | US |  |
| BUTTONS | Utilities | UT |  |
| BUTTONS | Warehouse Control | WC |  |
| BUTTONS | Work Orders | WO |  |

## Module: CM

| Code | Label | Program | Key Tables |
|------|-------|---------|------------|
| CMA | &A - Enter Contact Accounts | t7cma.rwn | BKARCUST, ISTAXGRP, BKCMACCL, BKCMACTD |
| CMB | &B - Contact Account Reports | *(group)* |  |
| CMBB | &B - Print Accounts Listing & Labels | t7cmbb.rwn | BKCMMHST, BKARCUST, BKCMACTD, BKCMACCL |
| CMBC | &C - Print Reminders | T7REMINDRPT.RWN | BKSYMSTR, ISREMIND, BKARCUST, BKCMACCN |
| CMBF | &F - Print Notes | evonotesrpt.rwn | BKSYMSTR, ISNOTES, BKARCUST, BKAPVEND |
| CMC | &C - CRM Dashboard | t7jcrm.rwn | ISBUILD, FILEDICT, BKSYHELP, DBAHLPID |
| CMJ | &J - Change Account Codes | t7cmj.rwn | MKAHIST, ISNOTES, BKSYHELP, DBAHLPID |
| CMK | &K - Add Customers to Account File | t7cmk.rwn | BKARCUST, BKSYHELP, DBAHLPID, ISIS |
| CMM | &M - Contact Manager Defaults | T7DSCM.RWN | ISDROP, BKSYHELP, DBAHLPID, ISIS |

## Module: CR

| Code | Label | Program | Key Tables |
|------|-------|---------|------------|
| CRA | &A - Assign Departments to SO | T7SOREVUADMIN.RWN | BKARINV, ISCTREVU, ISSOREVU, BKSYHELP |
| CRB | &B - Enter SO Approvals | T7SOREVU.RWN | BKARINV, ISCTREVU, ISSOREVU, BKSYHELP |

## Module: CS

| Code | Label | Program | Key Tables |
|------|-------|---------|------------|
| CSA | &A - Enter Salespersons | T7CSA.RWN | BKPRAGNT, BKPRSALE, BKPRMSTR, BKAPVEND |
| CSB | &B - View Salespersons Info | t7csb.rwn | BKPRSALE, BKPRMSTR, BKPRAGNT, BKSYHELP |
| CSC | &C - Print Salespersons Info | t7csc.rwn | BKPRSALE, BKPRMSTR, BKSYHELP, DBAHLPID |
| CSD | &D - Transfer Sales Commissions | t7csd.rwn | MKAHIST, BKPRMSTR, BKSYHELP, DBAHLPID |
| CSE | &E - Print Commission Detail | t7cse.rwn | BKICMSTR, BKPRSALE, BKARINV, BKARINVL |
| CSF | &F - Print Commission Summary | t7csf.rwn | BKPRSALE, BKARINV, BKARINVL, BKSYHELP |
| CSG | &G - Enter Sales Rep Links | T7replnk.rwn | ISREPLNK, BKPRSALE, BKARCUST, BKICMSTR |
| CSH | &H - Import Sales Rep Links | T7CSDE.RWN | ISREPLNK, BKPRSALE, BKICMSTR, BKARCUST |
| CSK | &K - Enter Price Code Commissions | t7csk.rwn | MKAHIST, DBAHLPID, TASCOLOR, ISDRILL |
| CSL | &L - Print Price Code Commissions | t7csl.rwn | MKAHIST, DBAHLPID, TASCOLOR, ISDRILL |
| CSM | &M - Enter Contract Commissions | t7csm.rwn | MKAHIST, DBAHLPID, TASCOLOR, ISDRILL |
| CSN | &N - Print Contract Commissions | t7csn.rwn | MKAHIST, DBAHLPID, TASCOLOR, ISDRILL |
| CSO | &O - Print Commissions Earned Detail | t7cso.rwn | BKSYMSTR, BKPRCOMM, BKPRSALE, BKPRAGNT |
| CSP | &P - Print Commissions Due Summary | t7csp.rwn | BKPRSALE, BKARINV, BKARINVL, BKSYHELP |
| CSQ | &Q - Commission Year End Routine | t7csq.rwn | BKPRSALE, BKSYHELP, DBAHLPID, ISIS |
| CSR | &R - Sales Commission Defaults | T7DSCS.RWN | ISDROP, BKSYHELP, DBAHLPID, ISIS |

## Module: DC

| Code | Label | Program | Key Tables |
|------|-------|---------|------------|
| DCA | &A - Enter Labor/Production | t7dca.rwn | BKDCLAB, WORKORD, BKPRMSTR, ISWOEX |
| DCB | &B - Enter Production Only | t7dcb.rwn | BKICMSTR, BKDCLAB, BKPRMSTR, WORKORD |
| DCC | &C - Enter Labor Only | t7dcc.rwn | MKAHIST |
| DCD | &D - Print Labor Status | t7dcd.rwn | BKSYMSTR, BKPRMSTR, BKPRINFO, BKCPMSTR |
| DCE | &E - Print Labor Tickets | t7dce.rwn | WOROUT, WORKORD, BKSYHELP, DBAHLPID |
| DCF | &F - Print Employee Tickets | t7dcf.rwn | BKPRMSTR, BKSYHELP, DBAHLPID, ISIS |
| DCG | &G - Edit Labor Transactions | t7dcg.rwn | BKDCLAB, WORKORD, MACHINE, TASCOLOR |
| DCH | &H - Post Labor Transactions | t7dch.rwn | BKDCLAB, BKDCCFG, BKPRMSTR, WORKORD |
| DCI | &I - Work Order Inquiry | T7WOT.rwn | MKAHIST, WORKORD, BKSYHELP, DBAHLPID |
| DCJ | &J - Data Collection Defaults | T7DSDC.RWN | ISDROP, BKSYHELP, DBAHLPID, ISIS |
| DCK | &K - Archive Shift Data | T7DCK.RWN | BKDCLAB, BKPRMSTR, BKSYHELP, DBAHLPID |
| DCL | &L - Shift Clock In/Out | T7DCL.RWN | BKPRMSTR, MKAHIST, BKDCLAB, BKPRINFO |
| DCM | &M - Employee Dashboard | T7DCM.RWN | BKPRMSTR, BKDCLAB, BKSYHELP, DBAHLPID |
| DCN | &N - Generate Holiday Shift Records | T7DCN.RWN | BKPRMSTR, CALENDAR, BKDCLAB, CLASMSTR |

## Module: DE

| Code | Label | Program | Key Tables |
|------|-------|---------|------------|
| DEA | &A - Export Data | sqlexport.rwn | BKSYHELP, DBAHLPID, BKPSUSER, ISDRILL |
| DEB | &B - Import Inventory | *(group)* |  |
| DEBA | &A - Generate Import Header | T7DEBA.RWN | FILEDICT, FILEKEY, FILELOC, BKSYHELP |
| DEBB | &B - Import Inventory | T7DEBB.RWN | FILEDICT, FILEKEY, FILELOC, BKSYHELP |
| DEBC | &C - Inventory Error Report | T7DEBC.RWN | FILEDICT, FILEKEY, FILELOC, BKSYHELP |
| DEBD | &D - Edit Imported Inventory | T7DEBD.RWN | BKSYHELP, DBAHLPID, MKAHIST, BKSYHELP |
| DEBE | &E - Transfer Inventory to Master Files | T7DEBE.RWN | BKSYHELP, DBAHLPID, MKAHIST, BKSYHELP |
| DEC | &C - Import Bills of Material | *(group)* |  |
| DECA | &A - Generate Import Header | T7DECA.RWN | BKSYHELP, DBAHLPID, MKAHIST, BKSYHELP |
| DECB | &B - Import Bills of Material | T7DECB.RWN | BKSYHELP, DBAHLPID, MKAHIST, BKSYHELP |
| DECC | &C - Bills of Material Error Report | T7DECC.RWN | BKSYHELP, DBAHLPID, MKAHIST, BKSYHELP |
| DECD | &D - Edit Imported Bills of Material | T7DECD.RWN | BKSYHELP, DBAHLPID, MKAHIST, BKSYHELP |
| DECE | &E - Transfer Bills of Material to Master Files | T7DECE.RWN | BKSYHELP, DBAHLPID, MKAHIST, BKSYHELP |
| DED | &D - Import Routings | *(group)* |  |
| DEDA | &A - Generate Import Header | T7DEDA.RWN | BKSYHELP, DBAHLPID, MKAHIST, BKSYHELP |
| DEDB | &B - Import Routings | T7DEDB.RWN | BKSYHELP, DBAHLPID, MKAHIST, BKSYHELP |
| DEDC | &C - Routings Error Report | T7DEDC.RWN | BKSYHELP, DBAHLPID, MKAHIST, BKSYHELP |
| DEDD | &D - Edit Imported Routings | T7DEDD.RWN | BKSYHELP, DBAHLPID, MKAHIST, BKSYHELP |
| DEDE | &E - Transfer Routings to Master Files | T7DEDE.RWN | BKSYHELP, DBAHLPID, MKAHIST, BKSYHELP |
| DEE | &E - Import Customers | *(group)* |  |
| DEEA | &A - Generate Import Header | T7DEEA.RWN | BKSYHELP, DBAHLPID, MKAHIST, BKSYHELP |
| DEEB | &B - Import Customers | T7DEEB.RWN | BKSYHELP, DBAHLPID, MKAHIST, BKSYHELP |
| DEEC | &C - Customer Error Report | T7DEEC.RWN | BKSYHELP, DBAHLPID, MKAHIST, BKSYHELP |
| DEED | &D - Edit Imported Customers | T7DEED.RWN | BKSYHELP, DBAHLPID, MKAHIST, BKSYHELP |
| DEEE | &E - Transfer Customers to Master Files | T7DEEE.RWN | BKSYHELP, DBAHLPID, MKAHIST, BKSYHELP |
| DEF | &F - Import Vendors | *(group)* |  |
| DEFA | &A - Generate Import Header | T7DEFA.RWN | BKICMSTR, BKBMMSTR, ROUTING, BKARCUST |
| DEFB | &B - Import Vendors | T7DEFB.RWN | BKICMSTR, BKBMMSTR, ROUTING, BKARCUST |
| DEFC | &C - Vendor Error Report | T7DEFC.RWN | BKICMSTR, BKBMMSTR, ROUTING, BKARCUST |
| DEFD | &D - Edit Imported Vendors | T7DEFD.RWN | BKSYHELP, DBAHLPID, MKAHIST, BKARCUST |
| DEFE | &E - Transfer Vendors to Master Files | T7DEFE.RWN | BKSYHELP, DBAHLPID, MKAHIST, BKARCUST |
| DEG | &G - Import Chart of Accounts | *(group)* |  |
| DEGA | &A - Generate Import Header | T7DEGA.RWN | BKSYHELP, DBAHLPID, ISIS, MKAHIST |
| DEGB | &B - Import Chart of Accounts | T7DEGB.RWN | BKSYHELP, DBAHLPID, ISIS, MKAHIST |
| DEGC | &C - Chart of Accounts Error Report | T7DEGC.RWN | BKSYHELP, DBAHLPID, ISIS, MKAHIST |
| DEGD | &D - Edit Imported Chart of Accoutns | T7DEGD.RWN | BKSYHELP, DBAHLPID, MKAHIST, MKAHIST |
| DEGE | &E - Transfer Chart of Accounts to Master Files | T7DEGE.RWN | BKSYHELP, DBAHLPID, MKAHIST, MKAHIST |
| DEH | &H - Global Field Change | T7DEK.RWN | BKICMSTR, MTICMSTR, BKBMMSTR, ROUTING |
| DEI | &I - Erase Files | t7del.rwn | BKSYHELP, DBAHLPID, ISIS, MKAHIST |
| DEJ | &J - Import and Post Labor | *(group)* |  |
| DEJA | &A - Create Import Header | t7deja.rwn | BKSYHELP, DBAHLPID, ISIS, MKAHIST |
| DEJB | &B - Import Labor | t7dejb.rwn | BKSYHELP, DBAHLPID, ISIS, MKAHIST |
| DEJC | &C - Imported Labor Error Report | t7dejc.rwn | BKSYHELP, DBAHLPID, ISIS, MKAHIST |
| DEJD | &D - Edit Imported Labor | t7dejd.rwn | BKSYHELP, DBAHLPID, MKAHIST, MKAHIST |
| DEJE | &E - Transfer Imported Labor | t7deje.rwn | BKSYHELP, DBAHLPID, MKAHIST, MKAHIST |
| DEK | &K - Import and Post Material Issues | t7dejh.rwn | WOMAT, WORKORD, WOBOM, BKICMSTR |
| DEL | &L - Import and Post Finished Production | T7WOP.RWN | WORKORD, BKYSMSTR, WOBOM, BKICMSTR |
| DEM | &M - Import Physical Inventory Count | T7PIC.RWN | BKPIPHYS, BKYSMSTR, BKSYMSTR, BKPIMSTR |
| DEP | &P - EDI Interface | *(group)* |  |
| DEPB | &B - Import EDI Orders | t7depb.rwn | BKARINV, BKYSMSTR, BKEDMSTR, BKEDIDUN |
| DEPC | &C - Edit EDI Orders | t7depc.rwn | MKAHIST, BKYSMSTR, BKEDMSTR, BKEDIDUN |
| DEPD | &D - Convert EDI Orders to Sales Orders | t7depd.rwn | BKARINVL, BKICLOCM, BKARINV, BKYSMSTR |
| DEPE | &E - Export EDI Invoice/Acknowledgement | t7depe.rwn | BKARINV, BKARCUST, ISAREX, ISBUILD |
| DEPF | &F - Export EDI ASN | t7depf.rwn | BKARCUST, BKARINV, ISAREX, BKEDMSTR |
| DEPH | &H - EDI Error Report | t7deph.rwn | BKSYMSTR, BKARINV, BKICREF, BKARINVL |
| DEQ | &Q - Import open Accounts Receivable | t7deq.rwn | BKARINVT, BKARCUST, BKART, BKARTNOT |
| DER | &R - Import open Accounts Payable | t7der.rwn | BKAPINVT, ISTERMS, BKSYHELP, DBAHLPID |
| DET | &T - Import Sales Orders | *(group)* |  |
| DETA | A - FTP Web Storefront Orders | T7DET.RWN | BKYSMSTR, ISMCF, ISBANKS, BKARCUST |
| DETB | B - SHOPIFY Web Storefront Orders | T7DETB.RWN | BKYSMSTR, BKSYMSTR, ISMCF, BKARCUST |
| DETC | C - File Web Storefront Orders | T7DETC.RWN |  |
| DEU | &U - Upload Stock Balance to Web Storefront | J7BEFWEBINV.RWN |  |

## Module: ES

| Code | Label | Program | Key Tables |
|------|-------|---------|------------|
| ESA | &A - Enter Estimates | t7esa.rwn | MKAHIST, BKSYHELP, DBAHLPID, ISIS |
| ESB | &B - Print Customer Quotes | T7ESB.RWN | MTICMSTR, BKYSMSTR, BKARINV, BKARCUST |
| ESC | &C - Print Estimate Cost Rollup | t7esc.rwn | ISESTDTL, BKARINV, BKARCUST, BKICMSTR |
| ESD | &D - Quick Estimate | T7EST.RWN | ISESTDTL, BKARINVL, MTEXCHG, MTICMSTR |
| ESE | &E - Convert Estimates | T7ese.RWN | ISESTDTL, BKYSMSTR, BKARINV, WORKORD |
| ESH | &H - Enter Material Costs | T7ESH.RWN | BKMATCST, BKICMSTR, MTICMSTR, BKAPVEND |
| ESI | &I - Print Material Costs | t7esi.rwn | BKICMSTR, BKMATCST, BKSYHELP, DBAHLPID |
| ESJ | &J - Estimating Defaults | T7DSEST.RWN | ISDROP, BKSYHELP, DBAHLPID, ISIS |
| ESK | &K - Update Estimating Inventory from Production | T7IC2EST.RWN | BKICMSTR, MTICMSTR |
| ESL | &L - Edit Estimating Inventory | T7ESL.RWN | MKAHIST, BKMATCST, BKSYHELP, DBAHLPID |
| ESM | &M - Estimating Inventory Inquiry | T7ESM.RWN | MKAHIST, BKMATCST, BKSYHELP, DBAHLPID |

## Module: FA

| Code | Label | Program | Key Tables |
|------|-------|---------|------------|
| FAA | &A - Enter Assets | T7FAA.RWN | ISFXASST, ISFXATRN, BKGLCOA, BKSYHELP |
| FAB | &B - Post Depreciation | T7FAB.RWN | ISFXATRN, ISFXASST, BKGLCOA, BKSYMSTR |
| FAC | &C - List Depreciation Transactions | UT7GFAC.RWN | BKLUGRID, BKSYHELP, DBAHLPID, BKPSUSER |
| FAD | &D - List Assets | UT7GFAD.RWN | BKLUGRID, BKSYHELP, DBAHLPID, BKPSUSER |
| FAE | &E - Import Assets | T7FAE.RWN | ISFXASST, BKGLCOA, BKSYHELP, DBAHLPID |

## Module: FO

| Code | Label | Program | Key Tables |
|------|-------|---------|------------|
| FOA | &A - Set up Features and Options | T7FOA.RWN | FILELOC, FILEDICT, BKSYHELP, DBAHLPID |
| FOB | &B - Print Features and Options | T7FOB.RWN | FILELOC, FILEDICT, BKSYHELP, DBAHLPID |
| FOC | &C - Enter Option Prices | T7FOC.RWN | BKBMMSTR, BKICMSTR, MTICMSTR, BKSYHELP |
| FOD | &D - Print Option Prices | T7FOD.RWN | BKICMSTR, MTICMSTR, BKBMMSTR, BKICLOCM |
| FOE | &E - Print Option Where Used | T7FOE.RWN | BKICMSTR, MTICMSTR, BKBMMSTR, BKICLOCM |
| FOF | &F - Feature and Option Defaults | T7DSFO.RWN | ISDROP, BKSYHELP, DBAHLPID, ISIS |
| FOG | &G - Configure Item | EvoFNO.RWN | ISFOHEAD, ISFOLINE, BKICMSTR, BKBMMSTR |

## Module: GL

| Code | Label | Program | Key Tables |
|------|-------|---------|------------|
| GLA | &A - View Chart of Accounts | T7GLA.RWN | BKGLCOA, ISGLCOA, ISGLDATE, ISGLNBGT |
| GLB | &B - Enter/Post General Journal Trxns | t7glb.rwn | BKGLGJRN, BKYSMSTR, ISBANKS, ISAPPROJ |
| GLC | &C - Print GL Transactions | t7glc.rwn | BKYSMSTR, BKGLCOA, BKGLTRAN, BKARCUST |
| GLD | &D - Print Journals | T7GLD.RWN | BKSYMSTR, BKYSMSTR, BKGLTRAN, BKARCUST |
| GLE | &E - Print Detailed Trial Balance | t7gle.rwn | BKYSMSTR, ISGLDATE, BKSYMSTR, BKGLCOA |
| GLF | &F - Print Financial Statements | t7glf.rwn | BKSYMSTR, BKGLSTMT, ISGLDATE, BKGLCOA |
| GLG | &G - Print GL Code and Description | t7glg.rwn | BKSYMSTR, BKGLCOA, BKSYHELP, DBAHLPID |
| GLH | &H - Print Chart of Accounts | T7GLH.RWN | BKSYMSTR, BKGLCOA, ISGLCOA, ISGLNBGT |
| GLI | &I - Print Check Register | t7gli.rwn | BKSYMSTR, BKGLCHK, ISBANKS, BKAPVEND |
| GLJ | &J - Reconcile Check Register | t7glj.rwn | ISBANKS, BKGLCHK, BKGLCOA, BKSYMSTR |
| GLK | &K - Transfer Bank Account Funds | t7glk.rwn | BKYSMSTR, ISBANKS, BKGLCOA, BKAPDESC |
| GLL | &L - Credit Card Reconciliation | T7GLL.RWN | BKGLCHK, ISBANKS, BKAPCHKF, BKAPINVL |
| GLN | &N - Print Custom Statements | t7gln.rwn | BKSYMSTR, ISGLDATE, BKGLFSTL, BKGLCOA |
| GLO | &O - Print/Post General Ledger Batches | t7glo.rwn | BKSYMSTR, BKYSMSTR, BKGLTRAN, BKGLCOA |
| GLP | &P - Edit General Ledger Batch Entries | t7glp.rwn | BKGLTRAN, BKGLCOA, BKSYMSTR, BKSYHELP |
| GLQ | &Q - Enter Payroll Checks | t7glq.rwn | BKGLGJRN, BKGLCOA, BKSYMSTR, ISBANKS |
| GLR | &R - Business Status | T7JBS.rwn | BKSYHELP, DBAHLPID, ISIS, ISLOG |
| GLS | &S - View Journal Notes | t7gls.rwn | ISNOTES, BKGLGJRN, BKSYHELP, DBAHLPID |
| GLT | &T - Import GL Transactions | T7GLT.RWN | BKGLTRAN, ISBANKS, BKGLCOA, BKGLCHK |

## Module: GR

| Code | Label | Program | Key Tables |
|------|-------|---------|------------|
| GROUPS | Accounting | AD |  |
| GROUPS | Accounting | AM |  |
| GROUPS | Accounting | AP |  |
| GROUPS | Accounting | FA |  |
| GROUPS | Accounting | GL |  |
| GROUPS | Hand Held | HH |  |
| GROUPS | Items | BM |  |
| GROUPS | Items | FO |  |
| GROUPS | Items | IN |  |
| GROUPS | Items | LC |  |
| GROUPS | Items | PI |  |
| GROUPS | Items | RO |  |
| GROUPS | Items | SC |  |
| GROUPS | Items | WC |  |
| GROUPS | Mfg | DC |  |
| GROUPS | Mfg | ES |  |
| GROUPS | Mfg | JC |  |
| GROUPS | Mfg | MR |  |
| GROUPS | Mfg | PO |  |
| GROUPS | Mfg | QC |  |
| GROUPS | Mfg | SH |  |
| GROUPS | Mfg | WO |  |
| GROUPS | Pay Link | PL |  |
| GROUPS | Payroll | PR |  |
| GROUPS | Queries | QU |  |
| GROUPS | Queries | SU |  |
| GROUPS | Sales | AR |  |
| GROUPS | Sales | CM |  |
| GROUPS | Sales | CR |  |
| GROUPS | Sales | CS |  |
| GROUPS | Sales | RM |  |
| GROUPS | Sales | SA |  |
| GROUPS | Sales | SO |  |
| GROUPS | Sales | SR |  |
| GROUPS | Settings | US |  |
| GROUPS | System Mgr | DE |  |
| GROUPS | System Mgr | IM |  |
| GROUPS | System Mgr | PS |  |
| GROUPS | System Mgr | SD |  |
| GROUPS | System Mgr | SM |  |
| GROUPS | System Mgr | TAS |  |
| GROUPS | System Mgr | UT |  |

## Module: HH

| Code | Label | Program | Key Tables |
|------|-------|---------|------------|
| HHA | &A - Scan & Ship | t7hhssoe.rwn | ISSOBOX, BKARINV, BKARINVL, MTICMSTR |
| HHB | &B - Print Labels | T7HHinga.rwn | BKAPPO, BKYSMSTR, BKAPPOL, BKICMSTR |
| HHC | &C - Issue Materials | T7HHWOG.RWN | BKSHORT, BKYSMSTR, BKSYMSTR, WOMAT |
| HHD | &D - Enter Finished Production | T7HHWOP.RWN | BKYSMSTR, BKSYMSTR, WORKORD, BKICMSTR |
| HHE | &E - Enter Physical Counts | T7HHPIC.RWN | BKYSMSTR, BKSYMSTR, BKPIMSTR, BKPRMSTR |
| HHF | &F - Enter Labor | T7HHDCA.RWN | BKDCLAB, BKDCSHFT, BKYSMSTR, BKPRMSTR |
| HHG | &G - Receive PO | T7HHPOC.RWN | BKSBMFG, BKAPPO, MTICMSTR, ISDIGSIG |
| HHH | &H - Enter Shipping Information | J7HHLITN.RWN |  |
| HHI | &I - Paperless Shop Floor Tracking | t7dcpsf.rwn | BKDCLAB, WOROUT, WORKORD, BKICMSTR |
| HHJ | &J - Print WO Label | t7hhwolabel.rwn | WORKORD, BKICMSTR, MTICMSTR, WORECV |
| HHK | &K - Transfer Inventory | t7hhinlj.rwn | BKICLOCM, BKYSMSTR, BKICMSTR, SERIAL |
| HHL | &L - Multi-User Paperless Shop Floor | t7paperless.rwn | WORKORD, MTICMSTR, BKICMSTR, WOROUT |
| HHM | &M - Issue Scrap Component | t7hhwoscrap.rwn | BKSHORT, BKYSMSTR, WOBOM, BKICMSTR |

## Module: IM

| Code | Label | Program | Key Tables |
|------|-------|---------|------------|
| IMA | &A - International Configuration | T7DSIM.RWN | ISDROP, BKSYHELP, DBAHLPID, ISIS |
| IMB | &B - Enter Multiple Currencies | t7imb.rwn | ISMCF, BKSYMSTR, ISIS, BKSYHELP |
| IMC | &C - Enter Currency Exchange Rates | t7imc.rwn | ISMCR, ISMCF, BKSYHELP, DBAHLPID |
| IMD | &D - Enter Landed Cost Defaults | t7imd.rwn | ISLANDF, BKSYHELP, DBAHLPID, BKYSMSTR |
| IME | &E - Enter Landed Cost Duty Codes | t7ime.rwn | ISDUTY, BKSYHELP, DBAHLPID, ISIS |
| IMF | &F - Enter Landed Cost Customs Fees | t7imf.rwn | ISBROKER, BKSYHELP, DBAHLPID, ISIS |
| IMH | &H - International Defaults | T7DSIM.RWN | ISDROP, BKSYHELP, DBAHLPID, ISIS |

## Module: IN

| Code | Label | Program | Key Tables |
|------|-------|---------|------------|
| INA | &A - Inventory Inquiry | t7ina.rwn | BKICMSTR, CLASMSTR, MTICMSTR, ISICMSTR |
| INB | &B - Enter Inventory | T7inb.rwn | BKICMSTR, MTICMSTR, CLASMSTR, ISICMSTR |
| INC | &C - Enter Inventory Adjustments | t7inc.rwn | INVTXN, BKICMSTR, BKICLOC, MTICMSTR |
| IND | &D - Print Reorder Report | t7ind.rwn | BKSYMSTR, BKICMSTR, BKYSMSTR, BKICLOCM |
| INE | &E - Print Inventory Transactions | t7ine.rwn | BKSYMSTR, BKYSMSTR, MKAHIST, BKICMSTR |
| INF | &F - Print Inventory Value | t7inf.rwn | BKYSMSTR, MTICMSTR, CLASMSTR, BKARCUST |
| ING | &G - Print Inventory Labels | t7ing.rwn | MTICMSTR, BKPSUSER, BKPRMSTR, BKAPPO |
| INH | &H - Print Inventory Listing | t7inh.rwn | BKICMSTR, MTICMSTR, BKYSMSTR, BKSYMSTR |
| INI | &I - Print Inventory General Info | t7ini.rwn | MTICMSTR, BKICMSTR, BKARCUST, BKAPVEND |
| INJ | &J - Print Physical Check | t7inj.rwn | BKSYMSTR, ISBUILD, BKICMSTR, MTICMSTR |
| INK | &K - Adjust Physical Levels | t7ink.rwn | BKICMSTR, MTICMSTR, BKYSMSTR, BKICLOC |
| INL | &L - Inventory Maintenance Programs | *(group)* |  |
| INLA | &A - Enter Standard Costs | t7inla.rwn | BKICMSTR, MTICMSTR, ISICMSTR, BKSYHELP |
| INLB | &B - Enter/Assign Locations | t7inlb.rwn | BKICLOCM, BKICMSTR, BKICLOC, FILELOC |
| INLC | &C - Enter Customer Cross-Reference | t7inlc.rwn | BKICMSTR, BKICREF, BKARCUST, FILELOC |
| INLD | &D - Print Customer Cross-Reference | t7inld.rwn | BKSYMSTR, BKICREF, BKICMSTR, MTICMSTR |
| INLE | &E - Update Material Standard Costs | t7inle.rwn | BKICMSTR, MTICMSTR, BKAPPOL, BKAPPO |
| INLH | &H - Edit FIFO/LIFO Buckets | t7inlh.rwn | BKICMSTR, MTICMSTR, BKYSMSTR, DBAFIFO |
| INLI | &I - Change Costing Method | t7inli.rwn | BKYSMSTR, BKSYMSTR, BKICMSTR, BKICLOC |
| INLJ | &J - Transfer Inventory | t7inlj.rwn | BKICMSTR, SERIAL, LOT, ISBINLOC |
| INLK | &K - Inventory Exceptions Report | t7inlk.rwn | BKSYMSTR, BKYSMSTR, BKICMSTR, MTICMSTR |
| INLL | &L - Inactive BOM Component Report | t7inll.rwn | BKSYMSTR, MTICMSTR, BKICMSTR, BKBMMSTR |
| INLM | &M - Batch Location Transfers | T7INLM.RWN | BKICMSTR, INVTXN, MTICMSTR, LOT |
| INLN | &N - Copy Item Number | t7inln.rwn | BKICMSTR, BKYSMSTR, BKICLOC, ISICMSTR |
| INLO | &O - Inactive Item Utility | t7inlo.rwn | BKACTRPT, BKICMSTR, BKSYMSTR, BKYSMSTR |
| INLQ | &Q - Enter Inspection & Test Procedures | t7inlq.rwn | ISITP, BKSYMSTR, ISNOTES, ISLINKS |
| INLR | &R - Intercompany Inventory Transfer | T7INLR.RWN | BKICMSTR, ISMCF, FILELOC, BKSYMSTR |
| INLS | &S - Rebuild Stock Status | t7inls.rwn | BKICMSTR, MTICMSTR, BKSYHELP, DBAHLPID |
| INLT | &T - Reset Cycle Code | T7INLT.RwN | BKSYMSTR, MTICMSTR, BKICMSTR, INVTXN |
| INLU | &U - Item Number Configurator | T7ITMCFG.RWN | ISSERCNT, BKICMSTR, BKSYHELP, DBAHLPID |
| INM | &M - Summary Reorder Report | T7INM.RWN | BKICMSTR, MTICMSTR, BKYSMSTR, WORKORD |
| INN | &N - Month End Reports | *(group)* |  |
| INNA | &A - Print Month End Inventory Costing | t7inna.rwn | BKSYMSTR, CLASMSTR, INVTXN, BKICMSTR |
| INNB | &B - Print Shipments Costing | t7innb.rwn | BKSYMSTR, CLASMSTR, INVTXN, BKICMSTR |
| INNC | &C - Print Closed Work Orders Costing | t7innc.rwn | BKSYMSTR, WORKORD, MTICMSTR, BKICMSTR |
| INND | &D - Print Inventory to GL Exceptions | t7innd.rwn | BKSYMSTR, BKYSMSTR, INVTXN, BKICMSTR |
| INO | &O - User Defined Inventory Transactions | t7ino.rwn | BKACTRPT, INVTXN, MTICMSTR, BKYSMSTR |
| INP | &P - Inventory Usage Report | t7inp.rwn | BKYSMSTR, BKSYMSTR, BKICMSTR, ISBUILD |
| INQ | &Q - Import & Print Inventory Labels | T7ingimport.rwn | MTICMSTR, BKICMSTR, BKARCUST, CLASMSTR |
| INR | &R - Inventory Defaults | T7DSIC.RWN | ISDROP, BKSYHELP, DBAHLPID, ISIS |
| INS | &S - View Stock Status | T7INS.RWN | BKICMSTR, MTICMSTR, BKICLOCM, BKICLOC |

## Module: JC

| Code | Label | Program | Key Tables |
|------|-------|---------|------------|
| JCA | &A - Print Job Cost Report | t7jca.rwn | BKSYMSTR, BKICMSTR, WORKORD, ISWOEX |
| JCB | &B - Print Profit Projection | t7jcb.rwn | WORKORD, WOROUT, WOBOM, WOEXCHG |
| JCC | &C - Print Labor Transactions | t7jcc.rwn | WORKORD, WOROUT, WOBOM, WOEXCHG |
| JCD | &D - Print Overhead Transactions | t7jcd.rwn | WORKORD, WOROUT, WOBOM, WOEXCHG |
| JCE | &E - Print Material Issues | t7jce.rwn | BKSYMSTR, BKICMSTR, WOMAT, WORKORD |
| JCF | &F - Print Outside Purchases | t7jcf.rwn | BKSYMSTR, BKICMSTR, OUTPROC, BKAPPO |
| JCG | &G - Print Labor Efficiency | t7jcg.rwn | BKSYMSTR, BKICMSTR, OUTPROC, BKAPPO |
| JCH | &H - Print Work Order History | t7jch.rwn | BKSYMSTR, BKICMSTR, WOROUT, WORKORD |
| JCI | &I - Print Production by Work Center | t7jci.rwn | BKSYMSTR, BKICMSTR, WOROUT, WORKORD |
| JCJ | &J - Print Production by Machine | t7jcj.rwn | BKSYMSTR, BKICMSTR, WOROUT, WORKORD |
| JCK | &K - Print Production by Tool | t7jck.rwn | BKSYMSTR, BKICMSTR, WOROUT, WORKORD |
| JCL | &L - Print Job Cost Summary | t7jcl.rwn | BKSYMSTR, WORKORD, MTICMSTR, BKICMSTR |
| JCM | &M - Print WIP Summary | t7jcm.rwn | BKSYMSTR, WORKCTR, WORKORD, ISWOEX |
| JCN | &N - Print WIP Percent Completion | T7jcn.rwn | BKICMSTR, WORKORD, MTICMSTR, WOMAT |
| JCO | &O - Print Standard Labor Hours | t7jco.rwn | BKICMSTR, WORKORD, MTICMSTR, WOMAT |
| JCP | &P - Print Materials in WIP | t7jcp.rwn | BKSYMSTR, BKICMSTR, WOBOM, WORKORD |
| JCQ | &Q - Print Work Order Receipts | t7jcq.rwn | BKICMSTR, MTICMSTR, BKARCUST, BKAPPO |
| JCR | &R - Print Multi-Assembly Cost Rollup | T7JCR.RWN | BKICMSTR, MTICMSTR, BKARCUST, BKAPPO |
| JCS | &S - Work Order Detail Report | T7JCS.RWN | WOLABOR, OUTPROC, BKSYMSTR, ISBUILD |
| JCT | &T - Scrap Yield Report | T7JCT.RWN |  |

## Module: LC

| Code | Label | Program | Key Tables |
|------|-------|---------|------------|
| LCA | &A - Edit Lot Numbers | t7lca.rwn | LOT, MTICMSTR, BKYSMSTR, BKSYMSTR |
| LCB | &B - Assign Lot Control | t7lcb.rwn | BKICMSTR, MTICMSTR, BKSYHELP, DBAHLPID |
| LCC | &C - Print Lot Availability | t7lcc.rwn | BKSYMSTR, BKICMSTR, LOT, MTICMSTR |
| LCD | &D - Print Lot History | T7LCD.RWN | BKSYMSTR, BKICMSTR, LOT, MTICMSTR |
| LCE | &E - Lot Control On Hand Report | t7lce.rwn | BKSYMSTR, BKICMSTR, LOT, BKICLOC |
| LCF | &F - Lot Traceability Report | t7lcf.rwn | BKSYMSTR, BKICMSTR, MTICMSTR, LOT |

## Module: MR

| Code | Label | Program | Key Tables |
|------|-------|---------|------------|
| MRA | &A - Enter Forecast | T7MRA.RWN | BKMRPFC, BKICMSTR, BKSYHELP, DBAHLPID |
| MRB | &B - Print Forecast | t7mrb.rwn | BKSYMSTR, BKMRPFC, BKICMSTR, MTICMSTR |
| MRC | &C - Reset Forecast | T7MRC.RWN | BKICMSTR, BKMRPFC, MTICMSTR, BKARINVL |
| MRD | &D - Enter MRP Parameters | t7mrd.rwn | BKICMSTR, MTICMSTR, BKYSMSTR, BKICLOC |
| MRE | &E - Print MRP Parameters | T7MRE.RWN | BKSYMSTR, BKICMSTR, BKICLOCM, MTICMSTR |
| MRF | &F - Generate Material Requirements | T7MRF.RWN | MTICMSTR, BKMRPFC, BKARINVL, BKAPPOL |
| MRG | &G - Print Material Requirements | t7mrg.rwn | BKSYMSTR, BKICMSTR, MTMRP, MTICMSTR |
| MRH | &H - Print Order Action Report | t7mrh.rwn | BKSYMSTR, BKICMSTR, ISBUILD, MTMRP |
| MRI | &I - Generate Work Orders | t7mri.rwn | BKYSMSTR, MTICMSTR, BKICMSTR, BKICLOCM |
| MRJ | &J - Generate Purchase Orders | T7MRJ.RWN | MTICMSTR, BKYSMSTR, BKICMSTR, BKICLOCM |
| MRK | &K - Generate RFQs | t7mrk.rwn | BKMRPPO, BKAPPO, MTICMSTR, BKAPVEND |
| MRL | &L - Print Planned Orders Report | t7mrl.rwn | BKSYMSTR, MTMRP, BKSYHELP, DBAHLPID |
| MRM | &M - MRP Defaults | T7DSMRP.RWN | ISDROP, BKSYHELP, DBAHLPID, ISIS |
| MRN | &N - Apply Delay Action to POs | t7mrn.rwn | BKSYMSTR, ISBUILD, MTMRP, BKAPPO |

## Module: PI

| Code | Label | Program | Key Tables |
|------|-------|---------|------------|
| PIA | &A - Capture Frozen Inventory | t7pia.rwn | BKYSMSTR, BKSYMSTR, BKPIMSTR, BKICMSTR |
| PIB | &B - Frozen Inventory Report | T7PIB.RWN | BKPIMSTR, BKSYMSTR, BKPIFROZ, BKICMSTR |
| PIC | &C - Enter Tag Counts | t7pic.rwn | BKPIPHYS, BKYSMSTR, BKSYMSTR, BKPIMSTR |
| PID | &D - Missing Tags Report | t7pid.rwn | BKPIPHYS, BKPIMSTR, BKSYMSTR, BKSYHELP |
| PIE | &E - Edit Frozen Inventory Costs | t7pie.rwn | BKPIFROZ, BKYSMSTR, BKSYMSTR, BKPIMSTR |
| PIF | &F - Physical Inventory Report | t7pif.rwn | BKPIMSTR, BKYSMSTR, ISBUILD, BKSYMSTR |
| PIG | &G - Update Actual Inventory | t7pig.rwn | BKPIMSTR, BKYSMSTR, BKPIPHYS, BKICLOC |
| PIH | &H - Purge Physical Inventory | t7pih.rwn | BKPIMSTR, BKSYHELP, DBAHLPID, ISIS |

## Module: PL

| Code | Label | Program | Key Tables |
|------|-------|---------|------------|
| PLA | &A - Run Checkmark Payroll | T6PLA.RUN |  |
| PLB | &B - Import Employee Checks | BKPLB.RUN |  |
| PLC | &C - Import Employer Vouchers | BKPLC.RUN |  |
| PLD | &D - Payroll Link Setup | BKPLD.RUN |  |

## Module: PO

| Code | Label | Program | Key Tables |
|------|-------|---------|------------|
| POA | &A - Enter Purchase Orders | t7poa.rwn | BKAPPO, BKAPVEND, BKAPDESC, BKAPPOL |
| POB | &B - Print Purchase Orders | t7pob.rwn | MTICMSTR, BKAPVEND, BKSYMSTR, BKYSMSTR |
| POC | &C - Receive Purchase Orders | t7poc.rwn | BKAPPOL, BKAPPO, BKAPDESC, MTICMSTR |
| POD | &D - View PO Receivers | t7pod.rwn | MKAHIST, BKAPPOL, BKSYAP, MTICMSTR |
| POE | &E - Enter/Print RFQs | t7poe.rwn | MKAHIST, BKAPPOL, BKSYAP, MTICMSTR |
| POF | &F - Enter Verbal RFQs | t7pof.rwn | BKRFQ, BKARINVL, ISESTDTL, BKESTCFG |
| POG | &G - Convert RFQs | t7pog.rwn | MTICMSTR, BKAPPO, BKAPPOL, BKICMSTR |
| POH | &H - Enter Vendor Prices | t7poh.rwn | BKRFQ, BKAPDESC, BKICMSTR, MTICMSTR |
| POI | &I - Reports | *(group)* |  |
| POIA | &A - Print Open Purchase Orders Listing | t7poia.rwn | BKRFQ, BKAPDESC, BKICMSTR, MTICMSTR |
| POIB | &B - Print Closed Purchase Orders Listin | t7poib.rwn | BKRFQ, BKAPDESC, BKICMSTR, MTICMSTR |
| POIC | &C - Print RFQ Status | t7poic.rwn | BKRFQ, BKSYHELP, DBAHLPID, ISIS |
| POID | &D - Print Vendor Prices | t7poid.rwn | BKSYMSTR, BKRFQ, MTICMSTR, BKICMSTR |
| POIE | &E - Print Receiving Report | t7poie.rwn | BKSYMSTR, BKRFQ, MTICMSTR, BKICMSTR |
| POIF | &F - Print Received not Invoiced | t7poif.rwn | BKSYMSTR, BKRFQ, MTICMSTR, BKICMSTR |
| POIG | &G - Print Purch Order Items by Due Date | t7poig.rwn | BKSYMSTR, ISNTYPE, ISBUILD, BKAPVEND |
| POIH | &H - Print On Time Delivery Report | T7POIH.RwN | BKAPPO, BKQCMSTR, BKAPPOL, BKAPVEND |
| POII | &I - Print Purchase Order Changes | t7POIi.RwN | BKSYMSTR, ISAPCHG, MTICMSTR, BKAPPO |
| POIJ | &J - Print/Export Purchases by Item/Item Class | purchitem.rwn | BKSYHELP, DBAHLPID, BKPSUSER, ISDRILL |
| POIK | &K - Print/Export Purchases by Vendor | purchvend.rwn | BKSYHELP, DBAHLPID, BKPSUSER, ISDRILL |
| POIL | &L - Print Digital Signature Status | t7poil.rwn | BKAPPO, BKPRMSTR, BKSYHELP, DBAHLPID |
| POJ | &J - QC Inspection Programs | *(group)* |  |
| POJA | &A - Print Receipt Travelers | t7poja.rwn | BKSYMSTR, BKQCMSTR, BKAPPOL, BKICMSTR |
| POJB | &B - Print Inventory in QC | t7pojb.rwn | MTICMSTR, BKSYMSTR, BKQCMSTR, BKAPPO |
| POJC | &C - Enter Inspection Buyoffs | t7pojc.rwn | BKQCMSTR, BKQCTRAN, BKAPPOL, BKAPPO |
| POJD | &D - Vendor Quality Performance Report | t7pojd.rwn | BKQCTRAN, BKAPVEND, BKQCMSTR, BKSYHELP |
| POK | &K - Close Purchase Orders | t7pok.rwn | MTICMSTR, BKSYMSTR, BKAPPO, BKAPPOL |
| POL | &L - Assign Vendors to Items | t7pol.rwn | BKSBVEND, BKAPVEND, BKICMSTR, MTICMSTR |
| PON | &N - Reconcile PO Invoices | t7pon.run |  |
| POO | &O - View Open Purchase Orders | t7poo.rwn | MKAHIST, BKSYHELP, DBAHLPID, BKAPPO |
| POP | &P - View Vendor Information | T7APU.rwn | MKAHIST, BKAPCHKF, BKAPINVT, BKAPPO |
| POQ | &Q - Maintain PO Delivery Dates | T7poQ.RWN | BKAPPO, BKAPPOL, MTICMSTR, BKICMSTR |
| POR | &R - Print Receiving Slip | T7por.rwn | BKAPPO, BKAPPOL, MTICMSTR, BKICMSTR |
| POS | &S - Purchase Order Defaults | T7DSPO.RWN | ISDROP, BKSYHELP, DBAHLPID, ISIS |
| POT | &T - Electronically Approve PO | T7DIGSIGPO.RWN | BKAPPO, BKAPPOL, ISDIGSIG, BKPRMSTR |

## Module: PR

| Code | Label | Program | Key Tables |
|------|-------|---------|------------|
| PRA | &A - Enter Employees | t7pra.rwn | BKPRMSTR, BKPRINFO, BKPRGLFL, BKGLCOA |
| PRB | &B - Enter Pay Info | T7PRB.RWN | BKPRCURP, BKPRMSTR, BKPRGLFL, BKSYMSTR |
| PRC | &C - Print Payroll Register | T7PRC.RWN | BKSYMSTR, BKPRCURP, ISBUILD, BKPRMSTR |
| PRD | &D - Print Payroll Checks | T7PRD.RWN | BKSYMSTR, BKYSMSTR, BKPRMSTR, BKPRCURP |
| PRE | &E - Print Employee Info | T7PRE.RWN | BKSYMSTR, BKYSMSTR, BKPRMSTR, BKPRGLFL |
| PRF | &F - Maintain Tax Tables | T7PRF.RWN | BKPRFTAX, BKSYHELP, DBAHLPID, ISIS |
| PRG | &G - Void Payroll Checks | T7PRG.RWN | BKPRCURP, BKPRMSTR, BKSYMSTR, ISBANKS |
| PRH | &H - Transfer Liabilities to AP | T7PRH.RWN | BKPRGLFL, BKYSMSTR, BKAPINVT, ISMCF |
| PRI | &I - Print Pay History | t7pri.rwn | BKSYMSTR, BKPRCURP, BKPRMSTR, BKPRINFO |
| PRJ | &J - Enter Time Cards | T7PRJ.RWN | BKPRMSTR, BKYSMSTR, BKPRTC, BKSYHELP |
| PRK | &K - Print/Post Time Cards | T7PRK.RWN | BKSYMSTR, BKYSMSTR, BKPRMSTR, BKPRTC |
| PRL | &L - Reports | *(group)* |  |
| PRLA | &A - Print Quarterly Info | T7PRLA.RWN | BKSYMSTR, BKPRMSTR, BKPRGLFL, BKSYHELP |
| PRLB | &B - Print QTD Earnings Register | T7PRLB.RWN | BKSYMSTR, BKPRMSTR, BKPRINFO, BKPRCURP |
| PRLC | &C - Print QTD Taxable Earnings | T7PRLC.RWN | BKSYMSTR, BKPRMSTR, BKPRCURP, BKPRGLFL |
| PRLD | &D - Print Detail Earnings Ledger | T7PRLD.RWN | BKSYMSTR, BKPRCURP, BKPRMSTR, BKPRINFO |
| PRLE | &E - Print Detail Deductions Ledger | t7prle.rwn | BKSYMSTR, BKYSMSTR, BKPRGLFL, BKPRCURP |
| PRLF | &F - Print Subject To Report | T7PRLF.RWN | BKSYMSTR, BKPRGLFL, ISBUILD, BKPRMSTR |
| PRLG | &G - Print 941 and Schedule B Reports | T7PRLG.RWN | BKPRGLFL, BKSYMSTR, BKPRCURP, BKPRMSTR |
| PRLH | &H - Print 940 Report | T7PRLH.RWN | BKPRGLFL, BKPRCURP, BKPRMSTR, BKSYHELP |
| PRLI | &I - Print W-2 Forms | T7PRLI.RWN | BKPRMSTR, BKPRGLFL, BKSYMSTR, BKYSMSTR |
| PRLJ | &J - Print Calif DE6 Form | T7PRLJ.RWN | BKSYMSTR, BKPRMSTR, BKPRSALE, BKPRGLFL |
| PRLK | &K - Print Payroll Hours | t7prlk.rwn | BKSYMSTR, BKYSMSTR, BKPRCURP, BKPRMSTR |
| PRLL | &L - Print 941B Forms | T7PRLL.RWN |  |
| PRLM | &M - Print Employer Contributions | T7PRLM.RWN | BKSYMSTR, BKPRGLFL, BKPRCURP, BKPRMSTR |
| PRLN | &N - Print Payroll Wages Detail | t7prln.rwn | BKSYMSTR, BKYSMSTR, BKPRCURP, BKPRMSTR |
| PRLO | &O - Reprint Payroll Check Stub | t7prlo.rwn | BKSYMSTR, BKYSMSTR, BKPRMSTR, BKPRCURP |
| PRLP | &P - Print Vacation & Sick Due | t7prlp.rwn | BKSYMSTR, ISBUILD, BKPRMSTR, BKPRCURP |
| PRM | &M - Payroll Divisions | T7PRM.RWN | BKPRGLFL, BKYSMSTR, BKPRMSTR, BKSYHELP |
| PRN | &N - Purge Payroll History | T7PRN.RWN | BKSYMSTR, BKYSMSTR, BKPRCURP, BKPRMSTR |
| PRO | &O - Payroll Year End Routine | T7PRO.RWN | BKSYMSTR, BKYSMSTR, BKPRMSTR, FILELOC |
| PRP | &P - Enter Raise Information | T7PRP.RWN | BKPRMSTR, BKSYMSTR, BKYSMSTR, BKPRINFO |
| PRQ | &Q - Enter Review Information | T7PRQ.RWN | BKPRMSTR, BKSYMSTR, BKYSMSTR, BKPRINFO |
| PRR | &R - Payroll Defaults | T7DSPR.RWN | ISDROP, BKSYHELP, DBAHLPID, ISIS |
| PRS | &S - Assign Password to Employee | T7PRS.RWN | BKPRMSTR, BKPRINFO, BKSYHELP, DBAHLPID |
| PRT | &T - Archive Pay History | T7SMJV.RWN | BKPRCURP, BKPRMSTR, BKPRINFO, BKPRGLFL |

## Module: PS

| Code | Label | Program | Key Tables |
|------|-------|---------|------------|
| PSA | &A - System Users/Passwords | t7psa.rwn | BKPSUSER, ISEXUSER, FILELOC, BKSYMSTR |
| PSB | &B - DBA System Security Levels | bkpsb.run |  |
| PSC | &C - DBA Company Logon Access | bkpsc.run |  |
| PSE | &E - Evo Menu Access by User Report | t7pse.rwn | BKMENUSU, BKSYHELP, DBAHLPID, ISLOG |
| PSF | &F - Evo Menu Access by Program | t7psf.rwn | BKMENUSU, BKSYHELP, DBAHLPID, ISLOG |
| PSG | &G - Maintain Menu Access Records | WBKMENUSETUP.RWN | BKPSUSER, BKMENUSU, BKSYHELP, DBAHLPID |
| PSH | &H - Configure Auto-Chain Programs | T7CHAIN.RWN | ISCHAINM, BKPSUSER, BKSYHELP, DBAHLPID |
| PSI | &I - Enter Approved Signers for Purchase Orders | T7DIGSIGADMIN.RWN | BKAPPO, BKAPPOL, ISDIGSIG, BKPRMSTR |
| PSJ | &J - Enter Contract Review Signers | T7CTREVUADMIN.RWN | ISCTREVU, BKARINV, ISSOREVU, BKSYHELP |
| PSK | &K - Enter Vendor Approval | J7appvend.rwn |  |
| PSL | &L - Enter Field Specific Access | T7LIMACC.rwn | ISACCESS, BKSYHELP, DBAHLPID, MKAHIST |

## Module: QC

| Code | Label | Program | Key Tables |
|------|-------|---------|------------|
| QCA | &A - Quality Control Receiving Report | T7QCA.RWN | BKICMSTR, MTICMSTR, CLASS, BKAPVEND |
| QCB | &B - Quality Control Materials Report | T7QCB.RWN | BKICMSTR, MTICMSTR, CLASS, WORKORD |
| QCC | &C - Production Scrap Report | T7QCC.RWN | BKICMSTR, MTICMSTR, CLASS, WORKORD |
| QCD | &D - Quality Control Labor Report | T7QCD.RWN | BKICMSTR, MTICMSTR, CLASS, WORKORD |
| QCE | &E - Vendor Quality Performance | t7pojd.rwn | BKQCTRAN, BKAPVEND, BKQCMSTR, BKSYHELP |
| QCF | &F - Non-Conformance Reporting | *(group)* |  |
| QCFA | &A - Enter NCR | T7QCFA.RWN | ISNCR, MTICMSTR, BKICMSTR, BKARCUST |
| QCFB | &B - Print NCR | T7QCFB.RWN | BKSYMSTR, BKICMSTR, MTICMSTR, BKARCUST |
| QCFC | &C - Disposition NCR | T7QCFC.RWN | BKSYMSTR, BKICMSTR, MTICMSTR, BKARCUST |
| QCFD | &D - Close NCR | T7QCFD.RWN | BKICMSTR, MTICMSTR, ISNCR, ISNOTES |
| QCFE | &E - View NCR | T7QCFE.RWN | BKICMSTR, MTICMSTR, ISNCR, ISNOTES |
| QCFF | &F - NCR Listing | T7QCFF.RWN | BKICMSTR, MTICMSTR, BKICLOCM, ISNCR |
| QCG | &G - Corrective Action | *(group)* |  |
| QCGA | &A - Enter CAR | T7QCGA.RWN | ISNCR, ISCACT, ISCARDTE, BKAPDESC |
| QCGB | &B - Print CAR | T7QCGB.RWN | BKICMSTR, MTICMSTR, BKARCUST, BKAPVEND |
| QCGC | &C - View CAR | T7QCGC.RWN | BKICMSTR, MTICMSTR, BKARCUST, BKAPVEND |
| QCGD | &D - List CAR | T7QCGD.RWN | BKICMSTR, MTICMSTR, BKICLOCM, ISNCR |
| QCH | &H - QC Defaults | T7DSQC.RWN |  |

## Module: QU

| Code | Label | Program | Key Tables |
|------|-------|---------|------------|
| QUA | &A - Master Inquiry | t7csi.rwn | BKSYHELP, DBAHLPID, TASCOLOR, ISDRILL |
| QUB | &B - Calendar Drill Down | caldrillbt.rwn | BKSYHELP, DBAHLPID, TASCOLOR, ISLOG |
| QUC | &C - Calendar Summary Report | isshpcal2.rwn | BKARINVL, BKARINV, BKSYHELP, DBAHLPID |
| QUD | &D - Business Status | t7jbs.rwn | BKSYHELP, DBAHLPID, ISIS, ISLOG |
| QUE | &E - Quick Grid Lookup | t7qgrid.rwn | BKLUGRID, BKSYHELP, DBAHLPID, ISLOG |
| QUF | &F - Query Executor | queryexecute.rwn | BKSYHELP, DBAHLPID, BKPSUSER, ISDRILL |

## Module: RM

| Code | Label | Program | Key Tables |
|------|-------|---------|------------|
| RMA | &A - Enter RMA | t7rma.rwn | MKAHIST, MTICMSTR, BKBMMSTR, BKICMSTR |
| RMB | &B - Print RMA | T7RMB.RWN | BKARINV, BKARINVL, ISRMAI, BKICMSTR |
| RMC | &C - Receive RMA | T7RMC.RWN | BKARINV, BKARINVL, ISRMAI, BKICMSTR |
| RMD | &D - Disposition RMA | T7RMD.RWN | BKARINVL, ISRMAI, ISRMAC, BKARINV |
| RME | &E - Enter RMA Return Codes | T7RME.RWN | ISRMAC, BKSYHELP, DBAHLPID, ISIS |
| RMF | &F - RMA/Service & Repair Defaults | T7DSRMA.RWN | ISDROP, BKSYHELP, DBAHLPID, ISIS |
| RMG | &G - Reason Codes Report | t7rmg.rwn | BKSYMSTR, BKARINV, BKARINVL, ISRMAI |

## Module: RO

| Code | Label | Program | Key Tables |
|------|-------|---------|------------|
| ROA | &A - Enter Routings | t7roa.rwn | ROUTING, BKRTCST, MTICMSTR, BKYSMSTR |
| ROB | &B - Print/Rollup Routings Costs | t7rob.rwn | BKSYMSTR, MTICMSTR, BKICMSTR, ROUTING |
| ROC | &C - Work Centers | t7roc.rwn | WORKCTR, DPTMENT, ROUTING, ISROUTEX |
| ROD | &D - Enter Machines | t7rod.rwn | MACHINE, BKMATRIM, WORKCTR, ROUTING |
| ROE | &E - Enter Tools | t7roe.rwn | TOOL, MACHINE, BKARCUST, ISBNMSTR |
| ROF | &F - Enter QC Codes | t7rof.rwn | QCCODES, BKSYHELP, DBAHLPID, ISIS |
| ROG | &G - Enter Scrap Codes | T7ROG.RWN | SCRAP, BKGLCOA, BKSYHELP, DBAHLPID |
| ROH | &H - Enter Departments | t7roh.rwn | DPTMENT, BKSYHELP, DBAHLPID, ISIS |
| ROI | &I - Enter Operation Templates | t7roi.rwn | ROUTING, WORKCTR, BKAPVEND, BKYSMSTR |
| ROJ | &J - Reports | *(group)* |  |
| ROJA | &A - Print Routings | t7roja.rwn | BKSYMSTR, WORKORD, WOROUT, WOBOM |
| ROJB | &B - Print Work Centers | t7rojb.rwn | WORKCTR, BKSYHELP, DBAHLPID, ISIS |
| ROJC | &C - Print Machines | t7rojc.rwn | MACHINE, BKSYHELP, DBAHLPID, ISIS |
| ROJD | &D - Print Tools | T7ROJD.RWN | BKSYMSTR, TOOL, BKARCUST, MACHINE |
| ROJE | &E - Print QC Codes | t7roje.rwn | QCCODES, BKSYHELP, DBAHLPID, ISIS |
| ROJF | &F - Print Scrap Codes | t7rojf.rwn | SCRAP, BKSYHELP, DBAHLPID, ISIS |
| ROJG | &G - Print Departments | t7rojg.rwn | DPTMENT, BKSYHELP, DBAHLPID, ISIS |
| ROJH | &H - Print Operation Templates | t7rojh.rwn | WORKCTR, ROUTING, BKSYHELP, DBAHLPID |
| ROK | &K - Enter Specifications Templates | t7rok.rwn | BKRTTEMP, BKSYHELP, DBAHLPID, ISIS |
| ROL | &L - Enter Sequence Print Control | t7rol.rwn | ROUTING, BKSYHELP, DBAHLPID, ISIS |
| ROM | &M - Enter Testing Method | t7qcmthd.rwn | ISQCMTHD, ISNOTES, ISLINKS, BKSYHELP |
| RON | &N - Enter Testing Requirements | t7qcspec.rwn | ISQCSPEC, MTICMSTR, ISQCMTHD, ROUTING |
| ROO | &O - Routings Defaults | T7DSRO.RWN | ISDROP, BKSYHELP, DBAHLPID, ISIS |
| ROP | &P - Update Processing Cost Standards | t7rop.rwn | ROUTING, BKAPPOL, BKAPPO, BKSYHELP |

## Module: SA

| Code | Label | Program | Key Tables |
|------|-------|---------|------------|
| SAA | &A - Print Daily Sales/Bookings | t7saa.rwn | ISBUILD, BKYSMSTR, BKARINV, BKARCUST |
| SAB | &B - Print Profit by Invoice | T7SAB.RWN | BKYSMSTR, BKARINV, BKARCUST, ISARCHG |
| SAC | &C - Print Customer Detail | T7SAC.RWN | BKYSMSTR, BKARINV, BKARCUST, ISARCHG |
| SAD | &D - Print Customer Summary | T7SAD.RWN | BKYSMSTR, BKARINV, BKARCUST, ISARCHG |
| SAE | &E - Print Customer Class Detail | T7SAE.RWN | BKYSMSTR, BKARINV, BKARCUST, ISARCHG |
| SAF | &F - Charts and Export | *(group)* |  |
| SAFA | &A - Profit by Invoice | t7jsapbi.rwn | BKSYHELP, DBAHLPID, ISIS, MKAHIST |
| SAFB | &B - Sales by Customer | t7jsacc.rwn | BKSYHELP, DBAHLPID, ISIS, MKAHIST |
| SAFC | &C - Sales by Salesperson | t7jsasrs.rwn | BKSYHELP, DBAHLPID, ISIS, MKAHIST |
| SAFD | &D - Sales by Item/Class | t7jsaic.rwn | BKSYHELP, DBAHLPID, ISIS, MKAHIST |
| SAG | &G - Print Customer Class Summary | T7SAG.RWN | BKYSMSTR, BKARINV, BKARCUST, ISARCHG |
| SAH | &H - Print Salesperson Detail | T7SAH.RWN | BKYSMSTR, BKARINV, BKARCUST, ISARCHG |
| SAI | &I - Print Salesperson Summary | T7SAI.RWN | BKYSMSTR, BKARINV, BKARCUST, ISARCHG |
| SAJ | &J - Print Inventory Detail | T7SAJ.RWN | BKYSMSTR, BKARINV, BKARCUST, ISARCHG |
| SAL | &L - Print Product Class | T7SAL.RWN | BKYSMSTR, BKARINV, BKARCUST, ISARCHG |
| SAM | &M - Print User-Defined Detail | t7sam.rwn | BKSAREPT, BKACTRPT, ISBUILD, BKARINVL |
| SAN | &N - Print User-Defined Summary | t7san.rwn | BKSAREPT, BKACTRPT, ISBUILD, BKARINVL |
| SAO | &O - Top Customer Report | T7SAO.RWN | BKSYMSTR, BKICMSTR, BKARCUST, BKPRSALE |
| SAP | &P - Print Sales With Surcharge Rolled Up | t7sap.rwn | BKSYMSTR, BKARINVL, BKARINV, MTICMSTR |

## Module: SC

| Code | Label | Program | Key Tables |
|------|-------|---------|------------|
| SCA | &A - Edit Serial Numbers | t7sca.rwn | SERIAL, MTICMSTR, BKYSMSTR, WORKORD |
| SCB | &B - Assign Serial Control | t7scb.rwn | BKICMSTR, MTICMSTR, BKSYHELP, DBAHLPID |
| SCC | &C - Print Serial Availability | t7scc.rwn | BKSYMSTR, BKICMSTR, SERIAL, MTICMSTR |
| SCD | &D - Print Serial History | T7SCD.RWN | BKSYMSTR, BKICMSTR, SERIAL, MTICMSTR |
| SCE | &E - Archive Serial Numbers | t7sce.rwn | BKICMSTR, SERIAL, BKSYHELP, DBAHLPID |
| SCF | &F - Serial Control Exception Report | t7scf.rwn | BKSYMSTR, SERIAL, BKICMSTR, MTICMSTR |
| SCG | &G - Enter Serial Generation Parameters | t7scg.rwn | ISSERCNT, MTICMSTR, CLASMSTR, BKSYHELP |
| SCH | &H - Serial Traceability Report | t7sch.rwn | BKSYMSTR, MTICMSTR, SERIAL, INVTXN |

## Module: SD

| Code | Label | Program | Key Tables |
|------|-------|---------|------------|
| SDA | &A - Company Defaults | T7DSCO.rwn | ISDROP, BKSYHELP, DBAHLPID, ISIS |
| SDB | &B - Work Order Defaults | t7dswo.rwn | ISDROP, BKSYHELP, DBAHLPID, ISIS |
| SDC | &C - Purchase Order Defaults | t7dspo.rwn | ISDROP, BKSYHELP, DBAHLPID, ISIS |
| SDD | &D - MRP Defaults | t7dsmrp.rwn | ISDROP, BKSYHELP, DBAHLPID, ISIS |
| SDE | &E - Scheduling Defaults | t7dssh.rwn | ISDROP, BKSYHELP, DBAHLPID, ISIS |
| SDF | &F - Data Collection Defaults | t7dsdc.rwn | ISDROP, BKSYHELP, DBAHLPID, ISIS |
| SDG | &G - Estimating Defaults | t7dsest.rwn | ISDROP, BKSYHELP, DBAHLPID, ISIS |
| SDH | &H - Inventory Defaults | t7dsic.rwn | ISDROP, BKSYHELP, DBAHLPID, ISIS |
| SDI | &I - Routings Defaults | t7dsro.rwn | ISDROP, BKSYHELP, DBAHLPID, ISIS |
| SDJ | &J - Bills of Material Defaults | t7dsbom.rwn | ISDROP, BKSYHELP, DBAHLPID, ISIS |
| SDL | &L - Features and Options Defaults | t7dsfo.rwn | ISDROP, BKSYHELP, DBAHLPID, ISIS |
| SDM | &M - Sales Orders Defaults | t7dsso.rwn | ISDROP, BKSYHELP, DBAHLPID, ISIS |
| SDN | &N - Sales Commissions Defaults | t7dscs.rwn | ISDROP, BKSYHELP, DBAHLPID, ISIS |
| SDO | &O - Contact Manager Defaults | t7dscm.rwn | ISDROP, BKSYHELP, DBAHLPID, ISIS |
| SDP | &P - Customer/AR Defaults | t7dsar.rwn | ISDROP, BKSYHELP, DBAHLPID, ISIS |
| SDQ | &Q - Master Default Settings | t7mdefaults.rwn | FILELOC, BKSYMSTR, BKYSMSTR, MTICMSTR |
| SDR | &R - Assign Next Document Numbers | t7numdef.rwn | BKYSMSTR, ISNUMBER, MKAHIST, BKSYAP |
| SDS | &S - Warehouse Control Defaults | t7dswc.rwn | ISDROP, BKSYHELP, DBAHLPID, ISIS |
| SDT | &T - Service/RMA Defaults | t7dsrma.rwn | ISDROP, BKSYHELP, DBAHLPID, ISIS |
| SDU | &U - Hand-Held Defaults | t7dshh.rwn | ISDROP, BKSYHELP, DBAHLPID, ISIS |
| SDV | &V - International Setting Defaults | T7DSIM.RWN | ISDROP, BKSYHELP, DBAHLPID, ISIS |

## Module: SH

| Code | Label | Program | Key Tables |
|------|-------|---------|------------|
| SHA | &A - Edit WO Start/Finish/Due Dates | t7sha.rwn | WORKORD, BKICMSTR, MTICMSTR, BKARINVL |
| SHB | &B - Manually Schedule Work Orders | t7shb.rwn | WORKORD, MTICMSTR, WOROUT, WORKCTR |
| SHC | &C - Manually Schedule Work Centers | t7shc.rwn | WORKCTR, WOROUT, WORKORD, BKSYHELP |
| SHD | &D - Manually Schedule Machines | machineview.rwn | BKSYHELP, DBAHLPID, BKPSUSER, ISDRILL |
| SHE | &E - Finite Scheduling | t7she.rwn | SCHWO, WORKORD, BKSYMSTR, SCHEDCAL |
| SHF | &F - Infinite Scheduling | t7shf.rwn | WORKORD, MTICMSTR, WOROUT, CALENDAR |
| SHG | &G - Print Work Order Schedule | t7shg.rwn | BKSYMSTR, BKICMSTR, WORKORD, MTICMSTR |
| SHH | &H - Print Work Order Status | t7shh.rwn | BKSYMSTR, BKICMSTR, MTICMSTR, WORKORD |
| SHI | &I - Print Work Center Schedule | t7shi.rwn | BKSYMSTR, MTICMSTR, ISBUILD, WORKCTR |
| SHJ | &J - Print Machine Schedule | t7shj.rwn | BKSYMSTR, MACHINE, WOROUT, WORKORD |
| SHK | &K - View Work Center Load | t7shk.rwn | MKAHIST, MACHINE, WOROUT, WORKORD |
| SHL | &L - View or Calculate Work Center Load | workcenterload.rwn | BKSYHELP, DBAHLPID, BKPSUSER, ISDRILL |
| SHM | &M - Lead Time Estimator | t7shm.rwn | BKICMSTR, CALENDAR, BKSYHELP, DBAHLPID |
| SHN | &N - Generate Lead Times | t7shn.rwn | BKSYMSTR, BKYSMSTR, BKICMSTR, MTICMSTR |
| SHO | &O - Finite Schedule Bucket Report | t7sho.rwn | BKSYMSTR, WORKORD, BUCKETS, WORKCTR |
| SHP | &P - Lead Time Scheduling | t7shp.rwn | WORKORD, WOBOM, MTICMSTR, WOROUT |
| SHQ | &Q - Scheduling Defaults | T7DSSH.RWN | ISDROP, BKSYHELP, DBAHLPID, ISIS |
| SHR | &R - Work Center Scheduler | T7VSCHED.RWN | BKICMSTR, FILELOC, WORKORD, WOROUT |

## Module: SM

| Code | Label | Program | Key Tables |
|------|-------|---------|------------|
| SMA | &A - Enter Customers | t7ara.rwn | BKARCUST, ISAREX, ISTAXGRP, BKCMDUNH |
| SMB | &B - Enter Vendors | t7apa.rwn | BKAPVEND, BKAPVND2, ISTAXGRP, ISEXUSER |
| SMC | &C - Enter Classes | *(group)* |  |
| SMCA | &A - Enter Item Classes | T7SMCA.RWN | CLASMSTR, BKICLOCM, CLASS, BKYSMSTR |
| SMCB | &B - Enter Customer Classes | T7SMCB.RWN | CLASMSTR, BKSYHELP, DBAHLPID, ISIS |
| SMCC | &C - Enter Vendor Classes | T7SMCC.RWN | CLASMSTR, BKSYHELP, DBAHLPID, ISIS |
| SMD | &D - Enter Terms Table | t7smd.rwn | ISTERMS, BKSYHELP, DBAHLPID, ISIS |
| SME | &E - Enter Tax Codes | t7sme.rwn | ISTAXFIL, BKAPVEND, BKGLCOA, BKSYMSTR |
| SMF | &F - Enter Tax Groups | T7SMF.RWN | ISTAXGRP, ISTAXFIL, BKSYHELP, DBAHLPID |
| SMG | &G - Enter Employees | t7smg.rwn | BKPRMSTR, ISLINKS, BKSYMSTR, BKPRINFO |
| SMH | &H - Enter Shop Calendar | t7smh.rwn | CALENDAR, SCHEDCAL, CALTEMP, BKSYHELP |
| SMI | &I - Contact Manager Maintenance | *(group)* |  |
| SMIA | &A - Enter Lead Source Codes | t7smia.rwn | BKCMLEAD, BKSYHELP, DBAHLPID, ISIS |
| SMIB | &B - Enter Territory Codes | t7smib.rwn | BKCMTERR, BKSYHELP, DBAHLPID, ISIS |
| SMIC | &C - Enter Reminder Types | t7smic.rwn | BKCMACFC, BKSYHELP, DBAHLPID, ISIS |
| SMID | &D - Enter Class Codes | t7smid.rwn | BKCMACCC, BKSYHELP, DBAHLPID, ISIS |
| SMIE | &E - Enter Key Date Codes | t7smie.rwn | BKCMDTCD, BKSYHELP, DBAHLPID, ISIS |
| SMIF | &F - Enter Reasons for Quote Loss | t7smif.rwn | ISCATMST, BKSYHELP, DBAHLPID, ISIS |
| SMJ | &J - File Maintenance Programs | *(group)* |  |
| SMJA | &A - Work Order File Maintenance | t7smja.rwn | BKSYMSTR, WORKORD, WORECV, BKDCLAB |
| SMJB | &B - Archive Work Orders | t7smjb.rwn | WORKORD, BKICMSTR, BKSYMSTR, WODATE |
| SMJC | &C - Reconcile Inventory On-Hand | t7smjc.rwn | BKICLOCM, BKICMSTR, BKSYMSTR, BKYSMSTR |
| SMJD | &D - Consolidate Inventory Transactions | t7smjd.rwn | BKICMSTR, INVTXN, BKYSMSTR, MTICMSTR |
| SMJE | &E - Purge Work Orders | t7smje.rwn | BKICMSTR, INVTXN, BKYSMSTR, MTICMSTR |
| SMJF | &F - Purge Purchase Order History | t7smjf.rwn | BKAPPO, BKAPDESC, ISNOTES, BKAPPOL |
| SMJG | &G - Purge/Archive QC Receipts | T7SMJG.RWN | BKQCMSTR, BKQCTRAN, ISNOTES, ISLINKS |
| SMJH | &H - Purge Data Collection File | t7smjh.rwn | BKDCLAB, BKSYHELP, DBAHLPID, ISIS |
| SMJI | &I - Purge/Archive Estimates | T7SMJI.RWN | ISESTDTL, BKARINV, BKARINVL, BKBMMSTR |
| SMJJ | &J - Purge or Archive Closed Sales Orders | T7smjj.rwn | BKARINV, BKARINVT, BKARINVL, BKAPDESC |
| SMJK | &K - Purge or Archive Invoice History | t7smjk.rwn | MKAHIST, BKARINVT, BKARINVL, BKAPDESC |
| SMJL | &L - Change/Merge Item Numbers | t7smjl.rwn | MTICMSTR, SERIAL, BKAPPOL, BKARINVL |
| SMJM | &M - Change/Merge Customer Codes | t7smjm.rwn | BKARCUST, BKARINVT, BKARINVV, BKICPMAT |
| SMJN | &N - Change/Merge Vendor Codes | t7smjn.rwn | BKAPVEND, BKCMVNDH, BKCMVNDF, BKICTAX |
| SMJO | &O - Rebuild Customer/Vendor Credit Info | t7smjo.rwn | BKAPVEND, BKARCUST, BKAPCHKF, BKARINVT |
| SMJP | &P - Purge or Archive Service RMA Orders | t7smjp.rwn | MKAHIST, BKARCUST, BKAPCHKF, BKARINVT |
| SMJQ | &Q - BOM Recursion Utility | t7smjq.rwn | BKSYMSTR, BKICMSTR, BKBMMSTR, BKSYHELP |
| SMJR | &R - Archive Purchase Orders | t7smjr.rwn | BKAPPO, BKAPDESC, ISNOTES, BKAPPOL |
| SMJS | &S - Purge Inventory Audit Info | t7smjs.rwn | BKICMSTR, MTICMSTR, BKSYHELP, DBAHLPID |
| SMJT | &T - Purge or Archive Sales Quotes | t7smjt.rwn | MKAHIST, MTICMSTR, BKSYHELP, DBAHLPID |
| SMJU | &U - Configure Vendor User Defined | T7APINFO.RWN | BKAPVND2, BKAPVEND, BKSYHELP, DBAHLPID |
| SMJV | &V - Archive Inventory Transactions | T7INVARCH.RWN | ISGLDATE, INVTXN, BKICMSTR, BKSYHELP |
| SMK | &K - Evo User Settings | T7SMK.RWN | LANGDICT, ISNUMBER, BKSYMSTR, MKAHIST |
| SMN | &N - Evo Notes Maintenance | *(group)* |  |
| SMNA | &A - Enter Note Types | T7SMN.RWN | ISNTYPE, ISNOTES, BKSYHELP, DBAHLPID |
| SMNB | &B - Enter System Notes | EVONOTES.RWN | ISNOTES, ISNTYPE, BKYSMSTR, BKARCUST |
| SMNC | &C - Synchronize Classic Notes to Evo | T7DBA2EVO.RWN | BKARCUST, ISNOTES, BKAPVEND, WORKORD |
| SMND | &D - Synchronize Evo Notes to Classic | T7EVO2DBA.RWN | BKARCUST, ISNOTES, BKAPVEND, WORKORD |
| SMNE | &E - Archive Evo Notes | EVONOTESARCH.RWN | BKSYMSTR, ISNOTES, BKARCUST, BKAPVEND |
| SMNF | &F - Update Evo Notes | T7SMNF.RWN | ISNTYPE, ISNOTES, CLASMSTR, ISCATMST |
| SMO | &O - Enter Ship Via Codes | T7SMO.RWN | ISSHIPCO, BKSYMSTR, CLASMSTR, ISCATMST |
| SMP | &P - Inventory Parameters | *(group)* |  |
| SMPA | &A - Category Master Maintenance | t7smpa.rwn | ISCATMST, BKSYHELP, DBAHLPID, ISIS |
| SMPB | &B - User Defined Master Maintenance | t7smpb.rwn | ISUDMSTR, BKSYHELP, DBAHLPID, ISIS |
| SMPC | &C - Enter QC Codes | T7ROF.RWN | QCCODES, BKSYHELP, DBAHLPID, ISIS |
| SMPD | &D - Enter Scrap Codes | T7ROG.RWN | SCRAP, BKGLCOA, BKSYHELP, DBAHLPID |
| SMPE | &E - Define Inventory User Defined Fields | T7UDFINV.RWN | ISUDFINV, BKSYHELP, DBAHLPID, ISDRILL |
| SMPF | &F - Enter Job Listing | T7SMPF.RWN | ISJOB, BKSYHELP, DBAHLPID, ISIS |
| SMPG | &G - Enter WO Priorities | T7WOPRIO2.RWN | ISWOPRIO, BKSYHELP, DBAHLPID, ISIS |
| SMPH | &H - Enter Cycle Codes | T7SMPH.RWN | ISCYCLCD, BKSYMSTR, BKSYHELP, DBAHLPID |
| SMPI | &I - Enter Defect Codes | T7SMPI.RWN | ISDEFECT, BKSYHELP, DBAHLPID, ISIS |
| SMR | &R - Multi-Language Maintenance | T7MLC.RWN | LANGDICT, BKSYHELP, DBAHLPID, MKAHIST |
| SMS | &S - Evo Links | *(group)* |  |
| SMSA | &A - Enter Evo Links | EVOLINKS.RWN | ISLINKS, BKYSMSTR, BKICMSTR, BKSYHELP |
| SMSB | &B - Broken Links Report | T7SMSB.RWN | ISLINKS, BKSYHELP, DBAHLPID, ISIS |
| SMSC | &C - Vendor Invoice Links Defaults | T7SMSC.RWN | ISLINKS, CLASMSTR, ISCATMST, BKSYHELP |
| SMSD | &D - Vendor Invoice Links | T7SMSD.RWN | BKAPINVT, ISLINKS, BKAPVEND, CLASMSTR |
| SMT | &T - Enter Java Settings | T7JSETTINGS.RWN | FILELOC, BKSYHELP, DBAHLPID, ISIS |
| SMU | &U - Enter Customer Ship Via | T7SMU.RWN | ISSHPVIA, BKSYMSTR, BKARCUST, BKSYHELP |
| SMV | &V - Download Updates | T7JUPD.RWN | FILELOC, BKSYHELP, DBAHLPID, BKPSUSER |

## Module: SO

| Code | Label | Program | Key Tables |
|------|-------|---------|------------|
| SOA | &A - Enter Sales Orders | T7SOA.RWN | BKARINV, ISTAXGRP, ISSHPVIA, ISORDECO |
| SOB | &B - Print Acknowledgements | t7sob.rwn | MTICMSTR, BKARCUST, BKYSMSTR, BKARINV |
| SOC | &C - Print Packing Slips | t7soc.rwn | MTICMSTR, BKARCUST, BKYSMSTR, BKARINV |
| SOD | &D - Print Shipping Labels | t7sod.rwn | ISARJDLP, BKARINV, BKARINVL, BKARCUST |
| SOE | &E - Release Sales Orders | t7soe.rwn | BKARINV, BKARINVL, BKICMSTR, ISSRINFO |
| SOF | &F - Print Invoices | t7sof.rwn | MTICMSTR, BKARCUST, BKSYMSTR, BKYSMSTR |
| SOG | &G - Post Invoices | t7sog.rwn | BKYSMSTR, BKARINV, BKARINVL, BKICMSTR |
| SOH | &H - Display Invoice History | t7soh.rwn | MKAHIST, BKARINV, BKARINVL, BKICMSTR |
| SOI | &I - Customer Service Inquiry | t7jsoi.rwn | BKSYHELP, DBAHLPID, ISIS, MKAHIST |
| SOJ | &J - Enter Recurring Sales Orders | t7soj.rwn | MKAHIST, BKYSMSTR, BKARINVL, ISPRINFO |
| SOK | &K - Generate Recurring Sales Orders | t7sok.rwn | BKARINV, BKARINVL, BKICLOC, BKICMSTR |
| SON | &N - Convert Sales Orders to Work Orders | t7son.rwn | WORKORD, CALENDAR, BKYSMSTR, BKARINV |
| SOO | &O - Reports | *(group)* |  |
| SOOA | &A - Print Open Sales Order Listing | t7sooa.rwn | BKSYMSTR, BKARINV, BKARINVL, WORKORD |
| SOOB | &B - Print Backorder Listing | t7soob.rwn | BKICMSTR, BKARINVL, BKARINV, BKSYHELP |
| SOOC | &C - Reprint Invoice | T7sooc.rwn | BKICMSTR, BKARINVL, BKARINV, BKSYHELP |
| SOOD | &D - Print Commissions by Sales Order | t7sood.rwn | BKSYMSTR, BKARINV, BKARINVL, BKSYHELP |
| SOOE | &E - Print Shipping Schedule | t7sooe.rwn | BKSYMSTR, ISBUILD, BKARINV, BKARINVL |
| SOOF | &F - Print Available to Ship | t7soof.rwn | BKSYMSTR, BKARINVL, BKICMSTR, BKICLOC |
| SOOG | &G - Print Sales Order/Work Order Schedu | t7soog.rwn | BKSYMSTR, BKARINV, BKARINVL, BKICMSTR |
| SOOH | &H - Print Invoice Listing | t7sooh.rwn | BKSYMSTR, BKARINV, BKISTAX, BKARCUST |
| SOOI | &I - Print Released Sales Orders | t7sooi.rwn | BKSYMSTR, BKARINV, BKARINVL, BKICMSTR |
| SOOJ | &J - Print User-Defined Detail | t7sooj.rwn | BKSYMSTR, BKARINV, BKARINVL, BKICREF |
| SOOK | &K - Print User-Defined Summary | t7sook.rwn | BKSYMSTR, BKARINV, BKARINVL, BKICREF |
| SOOM | &M - Print Changes to Sales Orders | t7soom.rwn | BKSYMSTR, ISARCHG, BKARINV, BKSYHELP |
| SOON | &N - Print On Time Delivery Performance | t7soon.rwn | BKSYMSTR, ISBUILD, ISARCHG, BKARINV |
| SOP | &P - Sales Quotes and Misc. | *(group)* |  |
| SOPA | &A - Enter Sales Quotations | t7sopa.rwn | MKAHIST, ISBUILD, ISARCHG, BKARINV |
| SOPB | &B - Print Sales Quotations | t7sopb.rwn | MTICMSTR, BKARCUST, BKYSMSTR, BKARINV |
| SOPC | &C - Convert Sales Quotations | t7sopc.rwn | BKYSMSTR, BKARINV, BKARINVL, ISICMSTR |
| SOPD | &D - Sales Quotation Detail Report | t7sopd.rwn | BKYSMSTR, BKARINV, BKARINVL, ISICMSTR |
| SOPE | &E - Sales Quotation Summary Report | t7sope.rwn | BKYSMSTR, BKARINV, BKARINVL, ISICMSTR |
| SOPF | &F - Release Blanket Order | T7SOPF.RWN | BKARINV, BKARINVL, BKMRPFC, BKICMSTR |
| SOPI | &I - Enter Freight & Tracking Information | t7sopi.rwn | BKARINV, ISSOBOX, BKAPDESC, BKARCUST |
| SOPJ | &J - Post Shipped Items | t7sopj.rwn | INVTXN, BKICMSTR, BKICLOC, MTICMSTR |
| SOPK | &K - Edit Posted Invoice | t7sopk.rwn | BKARINV, BKARCUST, ISSHPVIA, ISTAXGRP |
| SOPL | &L - Print Changes to Quotes | t7sopl.rwn | BKARINV, BKARCUST, ISSHPVIA, ISTAXGRP |
| SOPM | &M - Converted Quote Report | t7sopm.rwn | BKSYMSTR, BKARINV, BKARCUST, BKSYHELP |
| SOPN | &N - Convert SO to PO | t7sopo.rwn | MTICMSTR, BKYSMSTR, BKARINV, BKARINVL |
| SOPP | &P - Edis Estimated Ship Dates | t7sopp.rwn | BKARCUST, BKARINV, ISBUILD, BKARINVL |
| SOQ | &Q - Pricing | *(group)* |  |
| SOQA | &A - Enter Base Prices | t7soqa.rwn | BKICMSTR, MTICMSTR, ISICMSTR, BKICPMAT |
| SOQB | &B - Print Base Prices | t7soqb.rwn | BKSYMSTR, BKICMSTR, MTICMSTR, BKSYHELP |
| SOQC | &C - Global Price Change | t7soqc.rwn | BKICMSTR, MTICMSTR, ISICMSTR, BKICPMAT |
| SOQD | &D - Enter Price Codes | t7soqd.rwn | MKAHIST, MTICMSTR, ISICMSTR, BKICPMAT |
| SOQE | &E - Print Price Codes | t7soqe.rwn | MKAHIST, MTICMSTR, ISICMSTR, BKICPMAT |
| SOQF | &F - Enter Discount Codes | t7soqf.rwn | MKAHIST, MTICMSTR, ISICMSTR, BKICPMAT |
| SOQG | &G - Print Discount Codes | t7soqg.rwn | MKAHIST, MTICMSTR, ISICMSTR, BKICPMAT |
| SOQH | &H - Enter Contract Prices | t7soqh.rwn | BKICPMAT, BKARCUST, BKICMSTR, BKYSMSTR |
| SOQI | &I - Print Contract Prices | t7soqi.rwn | BKSYMSTR, BKICMSTR, BKICPMAT, MTICMSTR |
| SOQJ | &J - Generate Base Prices | t7soqj.rwn | BKSYMSTR, BKICMSTR, MTICMSTR, BKICPMAT |
| SOQK | &K - Print Catalog | t7soqk.rwn | BKICMSTR, MTICMSTR, BKSYMSTR, ISBUILD |
| SOQL | &L - SO Price Change | t7soql.rwn | BKSYMSTR, BKICMSTR, BKARINVL, BKARINV |
| SOR | &R - Void Invoice | t7sor.rwn | BKARINV, BKSOLOCK, BKARINVL, MTICMSTR |
| SOS | &S - Mass Release Sales Orders | T7sos.rwn | BKICMSTR, BKARINV, BKARCUST, BKARINVL |
| SOT | &T - Sales Order Inquiry | T7SOT.rwn | MKAHIST, BKARINV, SERIAL, BKICLOC |
| SOU | &U - Sales Order Defaults | T7DSSO.RWN | ISDROP, BKSYHELP, DBAHLPID, ISIS |

## Module: SR

| Code | Label | Program | Key Tables |
|------|-------|---------|------------|
| SRA | &A - Enter Service/Repair | T7SRA.RWN | MKAHIST, ISSDET, WORKORD, ISSPC |
| SRB | &B - Print Service/Repair | T7SRB.RWN | MTICMSTR, BKARCUST, BKYSMSTR, BKARINV |
| SRC | &C - Convert S/R to Work Order | T7SRC.RWN | BKARINV, BKARINVL, MTICMSTR, BKSYHELP |
| SRD | &D - Print S/R Packing Slips | T7SRD.RWN | BKSYMSTR, MTICMSTR, BKYSMSTR, BKARINV |
| SRE | &E - Release Service/Repairs | T7SRE.RWN | BKARINV, BKARINVL, BKYSMSTR, BKSYMSTR |
| SRF | &F - Print S/R Invoices | T7SRF.RWN | MTICMSTR, BKSYMSTR, BKYSMSTR, BKARINV |
| SRG | &G - Post S/R Invoices | T7SRG.RWN | BKYSMSTR, BKARINV, BKSYHELP, DBAHLPID |
| SRH | &H - RMA & Service & Repair Defaults | T7DSRMA.RWN | ISDROP, BKSYHELP, DBAHLPID, ISIS |
| SRI | &I - Void S/R Invoice | T7SRI.RWN | BKARINV, BKSOLOCK, BKARINVL, MTICMSTR |

## Module: SU

| Code | Label | Program | Key Tables |
|------|-------|---------|------------|
| SUA | &A - Maintain Grid Lookups | wbklugrid.rwn | BKLUGRID, FILELOC, FILEKNUM, FILEDICT |
| SUB | &B - Maintain Drill Down Menus | evoerpdrillm.rwn | ISDRILLM, BKLUGRID, FILELOC, FILEDICT |
| SUC | &C - Forms Editor | reports.int |  |
| SUD | &D - Grid Maintenance | t7gdm.rwn | BKLUGRID, ISDRILLM, BKSYHELP, DBAHLPID |

## Module: TA

| Code | Label | Program | Key Tables |
|------|-------|---------|------------|
| TAA | &A - Run TAS Program | RUNPRG.INT |  |
| TAB | &B - Change Company Code | GETCO.INT |  |
| TAC | &C - Set Configuration | CONFIG.INT |  |
| TAD | &D - Maintain Database | WTASDATAM.RWN | FILELOC, FILEDICT, FILEKNUM, FILEKEY |
| TAE | &E - Initialize Database | WTASINIT.RWN | FILELOC, FILEDICT, FILEKNUM, FILEKEY |
| TAF | &F - Maintain Location File | WTASFLOC.RWN | FILELOC, FILEDICT, FILEKEY, FILEKNUM |
| TAG | &G - Maintain Menu Access Records | WBKMENUSETUP.RWN | BKPSUSER, BKMENUSU, BKSYHELP, DBAHLPID |
| TAH | &H - Maint Menu Access - End User | WBKMENUSUEU.RWN | BKMENUSU, BKSYHELP, DBAHLPID, ISLOG |
| TAI | &I - Update File Structures | WTASMERGE.RWN | FILELOC, FILEDICT, FILEDBF, FILEKEY |
| TAM | &M - RTM Editor | REPORTS.INT |  |
| TAN | &N - Program Scheduler | evoscheduler.rwn | ISSCHED, FILELOC, BKSYMSTR, BKSYHELP |
| TAO | &O - Backup Utility | EvoERPbackup.rwn | MKAHIST, FILELOC, BKSYMSTR, BKSYHELP |
| TAP | &P - Change Password | PASSWORD.INT |  |
| TAQ | &Q - Change Logo Image | Evologo.rwn | BKSYMSTR, BKSYHELP, DBAHLPID, LANGDICT |
| TAR | &R - SQL Editor | T7JSQL.RWN | BKSYHELP, DBAHLPID, ISIS, MKAHIST |
| TAS | &S - Data Dictionary Check | T7DDCHECK.RWN | FILEDICT, FILEKEY, FILELOC, BKSYHELP |

## Module: US

| Code | Label | Program | Key Tables |
|------|-------|---------|------------|
| USA | &A - Customize Settings | T7SMK.RWN | LANGDICT, ISNUMBER, BKSYMSTR, MKAHIST |
| USB | &B - Customize Menu | WBKMENUSUEU.RWN | BKMENUSU, BKSYHELP, DBAHLPID, ISLOG |
| USC | &C - Reset Screen Size/Locations | t7resetdfm.RWN | ISREPLNK, BKPRSALE, BKARCUST, BKICMSTR |
| USD | &D - Change Password | PASSWORD.INT |  |
| USE | &E - Update PO Electronic Signature Info | T7DIGSIG.RWN | BKAPPO, BKAPPOL, ISDIGSIG, BKPRMSTR |
| USF | &F - Enter Reminders | calrem.rwn | BKYSMSTR, ISREMIND, BKARCUST, BKAPVEND |
| USG | &G - Enter Triggers | T7USG.RWN | ISTRIGRS, BKPSUSER, BKSYUSER, BKICMSTR |
| USH | &H - Update Contract Review Password | T7CTREVU.RWN | ISCTREVU, BKARINV, ISSOREVU, BKSYHELP |

## Module: UT

| Code | Label | Program | Key Tables |
|------|-------|---------|------------|
| UTA | &A - Run a DBA Program | runprg.int |  |
| UTC | &C - Re-Index File | t7reindex.rwn | FILELOC, BKSYHELP, DBAHLPID, ISIS |
| UTD | &D - Edit Data Location File | wtasfloc.rwn | FILELOC, FILEDICT, FILEKEY, FILEKNUM |
| UTE | &E - Set System Configuration | config.int |  |
| UTH | &H - Print File Layouts | t7uth.rwn | FILELOC, FILEDICT, FILEKEY, BKSYHELP |
| UTI | &I - Create/Delete Company | t7uti.rwn | BKPSUSER, BKSYUSER, FILELOC, BKSYAP |
| UTK | &K - File Maintenence Programs | *(group)* |  |
| UTKA | &A - Clear Data | t7utka.rwn | FILELOC, BKSYMSTR, ISIS, BKSYAP |
| UTKB | &B - Search and Replace | T7FNR.RWN | FILELOC, FILEDICT, BKSYHELP, DBAHLPID |
| UTKD | &D - Recalc GL Chart of Accounts | t7utkd.rwn | BKICMSTR, BKGLCOA, BKSYMSTR, ISGLDATE |
| UTKE | &E - Consolidate Inventory Locations | T7UTKE.RWN | BKYSMSTR, BKICLOCM, BKICLOC, BKICMSTR |
| UTKF | &F - Set Avg and Last Cost to Std Cost | t7utkf.rwn | BKSYMSTR, BKICMSTR, MTICMSTR, INVTXN |
| UTKG | &G - Recalc Inventory Book Value | t7utkg.rwn | BKSYMSTR, BKICMSTR, MTICMSTR, BKYSMSTR |
| UTKH | &H - Recalc Avg Cost fr FIFO/LIFO Bucket | T7UTKH.RWN | BKSYMSTR, BKYSMSTR, BKICMSTR, MTICMSTR |
| UTKI | &I - Fix Binary Zeroes | t7bzfix.rwn | FILELOC, FILEDICT, BKSYHELP, DBAHLPID |

## Module: WC

| Code | Label | Program | Key Tables |
|------|-------|---------|------------|
| WCA | &A - Enter Warehouse Bin Locations | T7WCA.RWN | BKICLOCM, ISBNMSTR, BKYSMSTR, ISBINLOC |
| WCB | &B - Assign Warehouse Control | T7WCB.RWN | BKYSMSTR, BKICLOCM, BKICLOC, BKICMSTR |
| WCC | &C - Assign Bins to Items | T7WCC.RWN | SERIAL, BKICMSTR, BKICLOCM, ISBINLOT |
| WCE | &E - Print Bin Inventory Listing | T7WCE.RWN | BKSYMSTR, BKYSMSTR, ISBINLOC, MTICMSTR |
| WCF | &F - Print Bin Inventory Exceptions | T7WCF.RWN | BKSYMSTR, BKYSMSTR, BKICMSTR, MTICMSTR |
| WCG | &G - Warehouse Control Defaults | T7DSWC.RWN | ISDROP, BKSYHELP, DBAHLPID, ISIS |

## Module: WO

| Code | Label | Program | Key Tables |
|------|-------|---------|------------|
| WOA | &A - Enter Work Orders | t7woa.rwn | WORKORD, MTICMSTR, ISWOEX, ISWOPRIO |
| WOB | &B - Release Work Orders | t7wob.rwn | ISWOPRIO, WORKORD, ISWOEX, BKICMSTR |
| WOC | &C - Print Travelers | t7woc.rwn | BKSYMSTR, MTICMSTR, WORKORD, WOROUT |
| WOD | &D - Print Pick Lists | t7wod.rwn | BKYSMSTR, WORKORD, BKICMSTR, BKSYMSTR |
| WOE | &E - Print Labor Cards/Labels | t7woe.rwn | WOROUT, WORKORD, BKSYHELP, DBAHLPID |
| WOF | &F - Enter Labor | T7WOF.RWN | WOLABOR, WOROUT, BKPSUSER, BKYSMSTR |
| WOG | &G - Issue Materials | t7wog.rwn | WOMAT, WORKORD, WOBOM, MTICMSTR |
| WOH | &H - Enter Misc/Extra Costs | T7WOH.RWN | WOEXCHG, WORKORD, BKSYMSTR, BKYSMSTR |
| WOI | &I - Enter Finished Production | t7woi.rwn | WORECV, WORKORD, BKICMSTR, MTICMSTR |
| WOJ | &J - Close/Cancel Work Orders | t7woj.rwn | MTICMSTR, WORKORD, WOROUT, BKYSMSTR |
| WOK | &K - Work Order Maintenance Programs | *(group)* |  |
| WOKA | &A - Enter Work Order Routings | T7WOKA.RWN | WORKORD, WOROUT, WORKCTR, MACHINE |
| WOKB | &B - Enter Work Order Bills of Material | t7wokb.rwn | WOBOM, BKICMSTR, WORKORD, MTICMSTR |
| WOKC | &C - Create Multi-Date Work Orders | t7wokc.rwn | WORKORD, WODATE, WOEXCHG, WOBOM |
| WOKD | &D - Create Multi-Assy Work Orders | t7wokd.rwn | MTICMSTR, WORKORD, ISWOEX, BKICMSTR |
| WOKE | &E - Swap Substitute Parts | T7WOKE.RWN | BKICMSTR, MTICMSTR, BKICLOC, WORKORD |
| WOKF | &F - Edit Sequence Started/Finished Date | t7wokf.rwn | WOROUT, BKSYHELP, DBAHLPID, ISIS |
| WOKG | &G - Recalculate Projected Hours | t7wokg.rwn | BKYSMSTR, WORKORD, WOROUT, WORKCTR |
| WOKH | &H - Rebuild Work Order Costs | t7rebwo.rwn | WORKORD, WOBOM, WORECV, WOROUT |
| WOKI | &I - Kitting System | t7kit.rwn | BKICMSTR, MTICMSTR, WOBOM, BKICLOC |
| WOKJ | &J - Synch WO BOM and Routing | j7ptwoki.rwn |  |
| WOKK | &K - Edit Posted DC Labor | t7wokk.rwn | BKDCLAB, WORKORD, BKPRMSTR, WOROUT |
| WOKL | &L - Quick Work Order | T7WOKL.RWN | BKYSMSTR, BKSYMSTR, BKARINVL, BKICMSTR |
| WOKM | &M - Parts Requester | t7wokm.rwn | SCRAP, WORKORD, ISPREQ, WOROUT |
| WOKN | &N - Stockroom Program | t7wokn.rwn | MKAHIST, BKSYHELP, DBAHLPID, ISIS |
| WOKO | &O - Map Component Serial to Parent | T7WOKO.RWN | ISSERIAL, BKICMSTR, WORKORD, MTICMSTR |
| WOKP | &P - Map Component Lot to Parent | T7WOKP.RWN | ISSERIAL, BKICMSTR, WORKORD, MTICMSTR |
| WOKQ | &Q - Convert WO to PO | T7WOPO.RWN | MTICMSTR, BKYSMSTR, WOBOM, BKICMSTR |
| WOKR | &R - Issue Scrap Component | t7hhwoscrap.rwn | BKSHORT, BKYSMSTR, WOBOM, BKICMSTR |
| WOKS | &S - Assign WO to Bin | t7woks.rwn | WORKORD, WOROUT, ISWOTRAY, BKSYMSTR |
| WOKT | &T - Print Issued Part Requests | t7wokt.rwn | BKICMSTR, MTICMSTR, WORKORD, BKPRMSTR |
| WOL | &L - Reports | *(group)* |  |
| WOLA | &A - Print Work Order Status | t7wola.rwn | BKSYMSTR, BKYSMSTR, MTICMSTR, WORKORD |
| WOLB | &B - Print Work Order Schedule | t7wolb.rwn | BKSYMSTR, MTICMSTR, ISNTYPE, WORKORD |
| WOLC | &C - Print Work Center Backlog | t7wolc.rwn | ISBUILD, WORKCTR, WOROUT, WORKORD |
| WOLD | &D - Print Projected Shipments | t7wold.rwn | BKSYMSTR, WORKORD, BKICMSTR, MTICMSTR |
| WOLE | &E - Print/Post Labor to Payroll | t7wole.rwn | BKSYMSTR, BKYSMSTR, BKCPMSTR, WOLABOR |
| WOLF | &F - Print Work Order Shortages | t7wolf.rwn | BKSYMSTR, MTICMSTR, WORKORD, BKICMSTR |
| WOLG | &G - Print Work Center by Key Component | bkwolg.run |  |
| WOLH | &H - Print Projected vrs Estimated hrs | t7wolh.rwn | BKSYMSTR, BKYSMSTR, WORKORD, WOROUT |
| WOLI | &I - Print Allocations | T7woli.rwn | BKSYMSTR, BKICMSTR, ISBUILD, MTICMSTR |
| WOLJ | &J - Print Work Order Completions | t7wolj.rwn | BKSYMSTR, WORKORD, BKICMSTR, WOROUT |
| WOLK | &K - Print Work Order Bill of Materials | t7wolk.rwn | BKSYMSTR, BKYSMSTR, WORKORD, WOBOM |
| WOLL | &L - Print Work Order Component Labels | j7woll.rwn |  |
| WOLM | &M - Print Material Summary | t7wolm.rwn | BKSYMSTR, BKARINV, BKARINVL, WORKORD |
| WOLN | &N - WO BOM for Purchasing | t7woln.rwn | BKSYMSTR, WOBOM, BKAPPOL, WORKORD |
| WOM | &M - Batch Labor Entry | t7wom.rwn | MKAHIST, WOBOM, BKAPPOL, WORKORD |
| WON | &N - Post Labor Batches | t7dch.rwn | BKDCLAB, BKDCCFG, BKPRMSTR, WORKORD |
| WOO | &O - Post Material Issues | t7dejh.rwn | WOMAT, WORKORD, WOBOM, BKICMSTR |
| WOP | &P - Batch Finished Production | t7wop.rwn | WORKORD, BKYSMSTR, WOBOM, BKICMSTR |
| WOQ | &Q - Work Order Inquiry | T7WOT.rwn | MKAHIST, WORKORD, BKSYHELP, DBAHLPID |
| WOR | &R - Work Order Defaults | T7DSWO.RWN | ISDROP, BKSYHELP, DBAHLPID, ISIS |
| WOS | &S - Print WOrk Order Labels | T7WOS.RWN | ISSOBOX, WORKORD, MTICMSTR, WORECV |
| WOT | &T - Enter Rework Work Order | T7WOTRWK.RWN | BKYSMSTR, BKSYMSTR, BKICMSTR, MTICMSTR |

