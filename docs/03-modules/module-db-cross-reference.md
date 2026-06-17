# Module ↔ Database File Cross-Reference
Status: verified | C:95/100 — derived from rwn_extract_symbols.py against 1,122 RWN files, 2026-06-16

For each major EvoERP module, the complete list of Btrieve tables it opens, extracted
from the DB file table in the decrypted RWN binary. DB file names appear at offset 0x80
in the decrypted body as 16-byte null-padded entries.

**Source:** `samples/rwn_symbols.json` — batch-extracted 2026-06-16 (K_B confirmed key)

---

## How to read this table

- **Module file**: the `.RWN` program file (one program = one screen/workflow)
- **Source lib**: compilation source (LIB = no procedure names; SRC = names available)
- **# DB files**: count of unique Btrieve tables opened by this module
- **Key tables**: most significant business tables (IS* helper tables omitted for brevity)

---

## Major module cross-reference

### Sales Order (SO) — T7SOA.RWN

**Source:** T7DBA.LIB | Procs: 606 | Vars: 5,669 | DB files: 86

**Key tables (business):**
BKARCUST, BKARINV, BKARINVL, BKARINVT, BKARINVV, BKARTXN — AR invoices and customers
BKICMSTR, BKICLOC, BKICLOCM, BKICPMAT, BKICREF — Inventory items
BKBMMSTR, BKBMDIM, BKBMNOTE, BKBMREMK — Bill of Materials
BKAPVEND, BKAPDESC — AP vendors (cross-ref for ship-to/vendor items)
BKGLCOA, BKGLTRAN — GL accounts and transactions
BKMRPFC — MRP forecast
WORKORD, WOBOM — Work orders (SO can generate WOs)
LOT, SERIAL, ROUTING — Lot/serial tracking, routings
BKPRSALE — Price book
BKRFQ — RFQ (request for quote)
BKRTSPEC — Routing specs

**IS* helpers:** ISACCESS, ISARCHG, ISAREX, ISARINVX, ISARTXNB, ISCHAINM, ISCNTRY,
ISDRILL, ISECO, ISESTDTL, ISFSPROJ, ISFSPS, ISICMSTR, ISIS, ISJAVA, ISJOB, ISLINKS,
ISNCR, ISNOTES, ISNTYPE, ISNUMBER, ISORDDSC, ISORDECO, ISPRINFO, ISREMIND, ISREPORD,
ISRMAC, ISRMAI, ISRTLOAD, ISSHIPCO, ISSHPVIA, ISSOBOX, ISSRINFO, ISSRMMS, ISTAXFIL,
ISTAXGRP, ISTERMS, ISTRIGRS

---

### Accounts Receivable (AR) — T7ARA.RWN

**Source:** LISTG60.LIB | Procs: 274 | Vars: 5,323 | DB files: 45

**Key tables (business):**
BKARCUST — Customer master
BKAPDESC, BKAPVEND — AP vendor cross-ref
BKGLCOA — GL chart of accounts
BKICMSTR, BKICLOCM, BKICPMAT, BKICREF — Inventory items
BKCMACCN, BKCMDUNH, BKCMLEAD, BKCMTERR — Contact manager (accounts, leads, territories)
BKPRSALE — Price book
CLASMSTR — Classification master

**IS* helpers:** IS2DBAR, ISACCESS, ISAREX, ISCHAINM, ISCNTRY, ISDRILL, ISEXUSER,
ISIS, ISLINKS, ISNCR, ISNOTES, ISNTYPE, ISREMIND, ISRTMS, ISSHIPCO, ISSHPVIA,
ISTAXGRP, ISTERMS, ISTRIGRS, LOT, SERIAL

---

### Accounts Payable Vendor Master (AP) — T7APA.RWN

**Source:** LISTG60.LIB | Procs: 216 | Vars: 2,675 | DB files: 39

**Key tables (business):**
BKAPVEND, BKAPVND2 — Vendor master (2 tables: current + extended)
BKAPDESC — AP description lookup
BKGLCOA — GL chart of accounts
BKICMSTR — Inventory items
BKCMACCN, BKCMTERR — Contact manager
BKPRSALE — Price book
CLASMSTR — Classification
BKAPPO — PO cross-reference

**IS* helpers:** ISACCESS, ISAPEX, ISCHAINM, ISDRILL, ISEXUSER, ISIS, ISLINKS, ISNCR,
ISNOTES, ISNTYPE, ISREMIND, ISSHIPCO, ISTAXGRP, ISTERMS, ISTRIGRS, ISVNDADT,
LOT, SERIAL

---

### AP Purchase Orders — T7POA.RWN

**Source:** LISTG60.LIB | Procs: 499 | Vars: 4,401 | DB files: 61

**Key tables (business):**
BKAPPO, BKAPPOL — PO header + lines
BKAPVEND, BKAPDESC — Vendor master
BKICMSTR, BKICLOC, BKICLOCM — Inventory
BKBMMSTR — BOM reference
BKGLCOA, BKGLTRAN — GL
BKSBMFG, BKSBVEND — Subcontract MFG + vendor
BKRFQ — RFQ
BKPRMSTR — Price master
BKARCUST, BKARINV, BKARINVL — AR cross-ref (for ship-to)
BKSYAP — AP system parameters
WORKORD, WOBOM, WOROUT — WO cross-ref (PO can link to WO)
CALENDAR, CLASS — Calendar, classification

**IS* helpers:** ISACCESS, ISAPCHG, ISAPEX, ISDIGSIG, ISDRILL, ISECO, ISICMSTR,
ISIS, ISJOB, ISLINKS, ISMCF, ISMCR, ISNCR, ISNOTES, ISNTYPE, ISNUMBER, ISORDDSC,
ISORDECO, ISREMIND, ISSHIPCO, ISTAXFIL, ISTAXGRP, ISTERMS, ISTRIGRS, LOT, SERIAL

---

### Inventory (IN) — T7INA.RWN

**Source:** LISTG60.LIB | Procs: 352 | Vars: 3,917 | DB files: 53

**Key tables (business):**
BKICMSTR, BKICLOC, BKICLOCM, BKICPMAT — Item master + location data
BKMRPFC — MRP forecast
BKBMMSTR — BOM
BKSBMFG, BKSBPART, BKSBVEND — Subcontract tables
BKGLTRAN, BKGLCOA — GL transactions
INVTXN — Inventory transaction log
DBAFIFO — FIFO costing buckets
BKARCUST, BKARINV, BKARINVL — AR (for shipments)
BKAPPOL, BKAPPO, BKAPVEND — AP (for receipts)
WOBOM, WORKORD — WO (for WO material issues)
LOT, SERIAL, ROUTING — Lot/serial tracking, routings
CLASMSTR, MTMRP — Classification, multi-company MRP

**IS* helpers:** ISACCESS, ISBINLOC, ISDRILL, ISECO, ISGLDATE, ISICMSTR, ISIS, ISITP,
ISLINKS, ISNCR, ISNOTES, ISNTYPE, ISREMIND, ISREPLNK, ISTRIGRS, ISUDFINV, ISUSAGE

---

### Work Orders (WO) — T7WOA.RWN

**Source:** LISTG60.LIB | Procs: 413 | Vars: 4,434 | DB files: 61

**Key tables (business):**
WORKORD — Work order header
WOBOM, WODATE, WOLABOR, WOMAT, WORECV, WORKCHG, WORKCTR, WOROUT — WO sub-tables
BKICMSTR, BKICLOC, BKICLOCM — Inventory (items for WO materials)
BKBMMSTR — BOM
BKGLTRAN — GL transactions
BKMRPFC — MRP forecast
BKAPPO, BKAPPOL, BKAPVEND — AP (for outside processing POs)
BKARCUST, BKARINV, BKARINVL — AR (for ship-to on WO)
BKAPDESC — AP descriptions
BKRFQ — RFQ
INVTXN — Inventory transactions
DBAFIFO — FIFO costing
ROUTING — Routings
LOT, SERIAL — Lot/serial tracking
CALENDAR — Work calendar
BKDCLAB — DC labor entries
BKPSUSER — Password/user security

**IS* helpers:** ISACCESS, ISCHAINM, ISDRILL, ISECO, ISICMSTR, ISIS, ISITP, ISJOB,
ISLINKS, ISNCR, ISNOTES, ISNTYPE, ISNUMBER, ISORDECO, ISREMIND, ISTRIGRS, ISWOEX,
ISWOPRIO, ISWOROEX

---

### System Manager Journals — T7SMJL.RWN

**Source:** LISTG60.LIB | Procs: 459 | Vars: 3,836 | DB files: 92 (most of any module)

**Key tables (business):**
All AR, AP, IN, WO, SO tables (see above)
BKICDIM, BKICVAL — Inventory dimension + valuation
BKMATCST — Material cost table
BKQCMSTR, BKQCTRAN — Quality Control master + transactions
BKPIFROZ, BKPILOT, BKPIPHYS, BKPISER — Physical inventory (frozen, lot, physical, serial)
BKRTCST, BKRTSPEC — Routing cost + specs
ESTSUM — Estimating summary
BUCKETS — Cost buckets
OUTPROC — Outside processing
BKMRPPO, BKMRPSW — MRP POs and signals
BKSHORT — Shortage tracking
BKGLX — GL extended
PIBINLOC, PIBINLOT — Physical inventory bin loc + lot

**Summary:** T7SMJL is the hub-of-hubs — the System Manager journal program touches
nearly every table in the system. It likely provides the global data migration / period-end
journaling functions.

---

### AP Miscellaneous / Vendor Labels — T7APM.RWN

**Source:** LISTG60.LIB | Procs: 105 | Vars: 1,511 | DB files: 35

**Key tables (business):**
BKAPVEND, BKARCUST — Vendor/customer address data (for label printing)
BKGLTRAN, BKGLX — GL transactions
BKPRMSTR — Price master
BKRFQ — RFQ
BKICMSTR — Inventory
OUTPROC, WOBOM, WORECV, WOROUT — WO outside processing
ISBROKER, ISDUTY — Broker/duty (international module)

**Summary:** Vendor label printing + miscellaneous AP functions. The `ISBROKER`/`ISDUTY`
references confirm international import/customs support.

---

### Sales Analysis (SA) — T7SAA/T7SAM/T7SAN/T7SAO.RWN

**T7SAA.RWN** (LISTG60.LIB, procs=212, vars=2123) — main SA screen
**T7SAM.RWN** (EVO.LIB, procs=238, vars=2505) — SA report manager
**T7SAN.RWN** (EVO.LIB, procs=220, vars=2300) — SA report variant
**T7SAO.RWN** (LISTG60.LIB, procs=169, vars=1988) — SA with CM integration

T7SAB through T7SAL (except T7SAM/N/O): SRC stubs (only `STUB` variable) — security level or terminal variants

**Key tables:** BKACTRPT (activity reports), BKSAREPT (SA report templates), BKARINV, BKARINVL (invoice data), BKARCUST, BKICMSTR, BKPRSALE, BKCMTERR (territories), BKCMLEAD (leads)

T7SAO adds: BKCMACCC (CM contacts), BKCMACCL (CM account levels)

**Key variables (T7SAA):** `FROM_CUR/THRU_CUR` (currency range), `DATE_FROM/DATE_THRU`, `FROM.SLSP.TXT/THRU.SLSP.TXT` (salesperson range), `TERR.FROM/TERR.THRU` (territory range), `SELECT_FROM3/THRU3` (filter ranges), `BASE` (base currency), `ANSWER`, `INCLUDE.TAX.FRT` (include tax/freight flag)

**Key variables (T7SAM/SAN):** `BKSA.TYPE`, `BKSA.NAME`, `BKSA.RTM` (report template), `BKSA.FROM1..6/THRU1..6` (up to 6 filter range pairs per report definition) — confirms SA report templates are stored in BKSAREPT with up to 6 range filters

---

### Features & Options (FO) — T7FOC/T7FOD/T7FOE.RWN

**T7FOC.RWN** (LISTG60.LIB, procs=60, vars=1370) — FO BOM record entry
**T7FOD.RWN** (EVO.LIB, procs=103, vars=1479) — FO report (item range filters)
**T7FOE.RWN** (LISTG60.LIB, procs=86, vars=1456) — FO component listing

T7FOA/T7FOB: ISTS.SRC stubs (same pattern as T7AUTOWOLA — 663 vars of EVO.CFG.* keys)

**Key tables:** BKBMMSTR (BOM master — FO options are BOM variants), BKICMSTR, BKICLOCM, CLASMSTR

**Key BKBM.* variables (from T7FOC):**

| Variable | Meaning |
|----------|---------|
| BKBM.KEY | BOM key (parent + line) |
| BKBM.PARENT | Parent item code |
| BKBM.PROD.LINE# | BOM line number |
| BKBM.COMPONENT | Component item code |
| BKBM.QTY.REQD | Quantity required |
| BKBM.REFERENCE | Reference designator |
| BKBM.PROD.TYPE | Component type (M/P/R/etc.) |
| BKBM.PROD.SCRAP | Scrap factor |
| BKBM.PROD.OP | Operation number |
| BKBM.PROD.OPYN | Include in operation flag |
| BKBM.PROD.PRICE | Component price |
| BKBM.PROD.RTNUM | Routing number |

**Summary:** FO options are implemented as BOM variants — configuring a product with options means selecting which BOM line components to include.

---

### Commissions / Sales Reps (CS) — T7CSA/T7CSB.RWN

**T7CSA.RWN** (LISTG60.LIB, procs=99, vars=1807) — agent + salesperson master
**T7CSB.RWN** (LISTG60.LIB, procs=138, vars=1421) — commission tracking + CM integration

**Key tables:** BKPRAGNT (agent master), BKPRMSTR (price master), BKPRSALE (price book), BKCMACCC (CM contacts), BKCMDTCD (CM date codes), BKPSUSER

**Key BKPR.* variables (from T7CSA):**

| Variable | Meaning |
|----------|---------|
| BKPR.AGNT.NUM | Agent number |
| BKPR.AGNT.CODE | Agent code |
| BKPR.AGNT.GLACT | Agent GL account |
| BKPR.AGNT.GLDPT | Agent GL department |
| BKPR.SLS.EMPNUM | Salesperson employee number |
| BKPR.SLS.CLASS | Salesperson class |
| BKPR.SLS.RATE | Commission rate |
| BKPR.SLS.HOW | Calculation method (gross/net/etc.) |
| BKPR.SLS.WHEN | Payment timing (on invoice/on payment) |
| BKPR.SLS.QUOTA | Sales quota |
| BKPR.SLS.GROSS | Gross sales (period) |
| BKPR.SLS.COGS | Cost of goods sold (period) |
| BKPR.SLS.RCPTS | Receipts (period) |
| BKPR.SLS.COMM | Commission earned |
| BKPR.SLS.PAID | Commission paid |
| BKPR.SLS.FNMI | First/middle name initial |
| BKPR.SLS.LNME | Last name |
| BKPR.SLS.EXPACT | Expense account |

---

### DC Activity (T7ADCA) — Data Collection Labor Entry

**T7ADCA.RWN** (ISTECH.LIB, procs=290, vars=3683) — DC labor / activity entry

**Note on module code:** The "AD" prefix does NOT correspond to "Accounting Defaults" in this RWN. T7ADCA appears to be an advanced/activity Data Collection program (ISTECH.LIB = same developer as the DC module). The variables and DB files all point to shop floor DC.

**Key tables:** BKDCCFG (DC configuration), BKDCLAB (DC labor transactions), BKDCSHFT (DC shifts), BKSYMSTR, INVTXN, EIMCOLST (EIM column status — new table)

**Key LAB.* variables:**

| Variable | Meaning |
|----------|---------|
| LAB.DATE | Labor entry date |
| LAB.EMP | Employee number |
| LAB.WOPRE / LAB.WOSUF | Work order prefix / suffix |
| LAB.WOKEY | Work order key |
| LAB.OPER | Operation number |
| LAB.POSTED | Posted flag |
| LAB.SHIFT | Shift code |
| LAB.START / LAB.FINISH | Start / finish times |
| LAB.PARTS | Parts completed |
| LAB.SCRAPPED | Scrap quantity |
| LAB.NOJOBS | Number of jobs on this entry |
| LAB.RUNHRS / LAB.SETUPHRS | Run hours / setup hours |
| LAB.REGOVER | Regular vs. overtime flag |
| LAB.EXTRA | Extra field |
| LAB.APPROVAL / LAB.ADT.SUPER | Approval / audit supervisor |
| LAB.ADT.IN / LAB.ADT.OUT | Audit in/out times |
| LAB.ESSDATE | ESS (employee self-service) date |
| LAB.DATE1 / LAB.DATE2 | Auxiliary dates |
| LAB.SCRAPCD | Scrap code |

---

---

### Activity Control (T7AC) — NCR / Action Items

**T7ACTION.RWN** (EVO.LIB, procs=53, vars=1183) — action item entry
**T7ACRDTYPE.RWN** (EVO.LIB, procs=58, vars=1240) — record type codes
**T7ACDET.RWN** (ISTECH.LIB, procs=18, vars=815) — AC detail records
**T7ACDATE.RWN** (LISTG60.LIB, procs=64, vars=1376) — WO date tracking

**Key tables:** ISACTION (action items), ACRDTYPE (record/reason types), ACDETAIL (AC detail)

**Key variables (T7ACTION):**
`IS.ACTION.TYPE` — action type code
`IS.ACTION.DESC` — action description
`IS.ACTION.MISC` — miscellaneous field

**Key variables (T7ACRDTYPE):**
`AC.RD.TYPE` — record type code
`AC.RD.REASON` — reason code
`AC.RD.DISPO` — disposition code (what happens to the part: rework/scrap/use-as-is)
`AC.RD.EXTRA1/2` — extra fields

**Key variables (T7ACDATE):**
`WODATE.WOPRE/WOSUF` — WO prefix/suffix
`WODATE.START/FINISH` — scheduled start/finish dates
`WODATE.QTY` — scheduled quantity
`WODATE.PARPRE/PARSUF` — parent WO prefix/suffix
`WODATE.TOPPRE/TOPSUF` — top-level WO
`WODATE.DELPRE` — delete prefix (for cascade)

**Summary:** AC is the Non-Conformance Report (NCR) and action item tracking module. An NCR is raised when a product fails quality inspection; the AC module records the disposition (rework, scrap, use-as-is), reason code, and tracks follow-up actions via ISACTION.

---

### Bill of Lading (T7BOL)

**T7BOL.RWN** (LISTG60.LIB, procs=178, vars=2227) — BOL entry and print
**T7BOLMSO.RWN** (LISTG60.LIB, procs=174, vars=2137) — SO-linked BOL edit

**Key tables:** BKARINV (AR invoices/SOs for shipment), BKARINVL (lines), BKARCUST

**Key BOL variables (T7BOL):**
`LOAD.NUMBER` — load reference number
`SEAL.NUMBER` — trailer seal number
`TRAILER.NUMBER` — trailer identifier
`AUTHOR.NUMBER` — authorization number
`CONTROL.NUMBER` — BOL control number
`PICKUP.TIME` — scheduled pickup time
`DRIVER.ARRIVED` — driver arrival timestamp
`LOADING.START/END` — loading start/end times
`DRIVER.DEPARTED` — departure timestamp

**Key SO-BOL variables (T7BOLMSO):**
`BILLING.LINE` — billing line on BOL
`EDIT.DESC` — item description
`EDIT.PQTY` — packed quantity
`EDIT.ITEM` — item code
`EDIT.SSONUM` — source SO number
`EDIT.PACKS` — number of packages
`EDIT.CLASS` — freight class (LTL classification)
`EDIT.WEIGHT` — shipment weight
`EDIT.UNITS` — units of measure
`EDIT.HM` — hazardous materials flag

**Summary:** T7BOL generates Bills of Lading for outbound shipments. It links to the SO/invoice records and records carrier, load, seal, and timing data. T7BOLMSO provides editing of individual line items on the BOL.

---

### Contract Review / SO Approval (T7CTREVU)

**T7CTREVU.RWN** (LISTG60.LIB, procs=96, vars=1447) — contract review with password protection
**T7CTREVUADMIN.RWN** (T7CTRevuAdmin.SRC stub) — admin access variant

**Key tables:** BKARINV (SO/invoices for review), BKGLTRAN

**Key variables:**
`ENTER.PSWD/CONF.PSWD` — password entry/confirmation fields
`CT.DEPT` — department code for review
`CT.ADMIN` — admin flag
`CT.EMPNAME` — approving employee name
`SFROM.SONUM/STHRU.SONUM` — SO number range to review
`FROM.ORDDTE/THRU.ORDDTE` — order date range

**Summary:** The CR/CT module provides password-protected SO approval workflows. Managers must enter a password to approve orders in the selected SO/date range. This corresponds to the "Contract Review" functionality in the menu system (CR module code).

---

### Data Sync Stubs (T7DS*) — Multi-Company Sync Architecture

All 25 T7DS* files are SRC stubs with only `STUB` as the variable and the same core DB file set. Each corresponds to one EvoERP module:

T7DSAP (AP), T7DSAR (AR), T7DSBOM (BOM), T7DSCK (Check), T7DSCM (CM), T7DSCO (??), T7DSCS (CS/Commissions), T7DSDC (DC), T7DSEST (Estimating), T7DSFO (FO), T7DSGEN (General), T7DSGL (GL), T7DSHH (HH/Handheld), T7DSIC (IC/Inventory), T7DSIM (IM), T7DSMRP (MRP), T7DSPO (PO), T7DSPR (Payroll), T7DSQC (QC), T7DSRMA (RMA), T7DSRO (Routing), T7DSSH (SH/Scheduling), T7DSSO (SO), T7DSWC (WC), T7DSWO (WO)

**DB files:** All share the same base set (BKARINV, BKARCUST, BKAPPO, BKAPVEND, BKGLTRAN, BKGLX, BKICMSTR, BKSYAR) + module-specific additions.

**Architecture:** These are the data synchronization layer for multi-company EvoERP installations. The shared BKSYAR (AP system parameters) confirms these interact with inter-company AP transactions. Each stub pre-opens the relevant module tables for the sync process.

---

### Automation Modules (T7AU*) — Automated Processing

**T7AUTODCH.RWN** (ISTECH.LIB, procs=183, vars=2696) — DC labor automation/validation
**T7AUTOMRF.RWN** (EVO.LIB, procs=132, vars=1889) — MRP firm order automation
**T7AUTOREBSS.RWN** (ISTECH2.LIB, procs=79, vars=2004) — back-order re-scheduling

**T7AUTOMRF key variables (MTMRP.*):**

| Variable | Meaning |
|----------|---------|
| MTMRP.PARTNO | Part number |
| MTMRP.KEY | MRP record key |
| MTMRP.DATE | Planned order date |
| MTMRP.QTY | Planned order quantity |
| MTMRP.ONHAND | On-hand at planning time |
| MTMRP.PEGTO | Pegged-to order (demand trace) |
| MTMRP.ORDER | Firmed order reference |
| MTMRP.STARTDT | Planned start date |

**Summary:** MTMRP is the multi-company MRP working table — used during MRP calculation runs to store planned orders with pegging info before they are firmed or released.

---

### Kitting (T7KIT)

**T7KIT.RWN** (EVO.LIB, procs=153) — kit assembly
**Key tables:** BKICMSTR, MTICMSTR, WOBOM, WOMAT, WORKORD, WOROUT, BKICLOC, LOT, ISBINLOC
**Summary:** Kitting creates pre-assembled kit sub-WOs. Opens the full WO material tables alongside inventory and bin locations to stage kit components for WO consumption. LOT table confirms lot-tracked component support.

---

### Work Center Entry (T7EWC)

**T7EWC.RWN** (LISTG60.LIB, procs=68) — work center master maintenance
**Key tables:** WORKCTR (work center master), WORKORD, WOROUT, ROUTING
**Summary:** Creates and edits WORKCTR records. ROUTING confirms routing operations reference these work centers.

---

### Cash Receipts / Deposit Mapping (T7TCC, T7MAPDEPO)

**T7TCC.RWN** (LISTG60.LIB, procs=119) — cash receipts entry
**T7MAPDEPO.RWN** (LISTG60.LIB, procs=97) — deposit-to-invoice mapping
**Key tables:** ISTERMS, ISBANKS, BKARDEP, ISARDEPL, BKARCUST, BKARINV, BKARINVL, BKARINVT, BKGLCOA, BKGLCHK, BKART, BKAPCHKF, BKARINVI
**Summary:** T7TCC enters cash receipts against ISBANKS/BKARDEP. T7MAPDEPO maps deposits to AR invoices via ISARDEPL. Together: enter receipt → map to invoices → post to GL. This is the cash receipts workflow.

---

### Grid / Drill-Down Manager (T7GDM, T7QGRID)

**T7GDM.RWN** (NZLICE.LIB, procs=31) — lookup grid + drill-down config
**T7QGRID.RWN** (LISTG60.LIB, procs=62) — Quick Grid Lookup UI
**Key tables:** BKLUGRID (lookup grid definitions), ISDRILLM (IS drill-down master), BKPSUSER, ISACCESS
**Summary:** UI infrastructure. BKLUGRID stores column layouts for all browse grids; ISDRILLM defines drill-down menus. Backs QU-E (Quick Grid Lookup) and SU-A/SU-B (Maintain Grid/Drill-Down) menu ops.

---

### Module Defaults — Central Configuration (T7MDEFAULTS, T7MDEFBANKS, T7MDEFNDC)

**T7MDEFAULTS.RWN** (ISTECH.LIB, procs=435) — central module defaults (largest config module)
**T7MDEFBANKS.RWN** (LISTG60.LIB, procs=79) — bank account defaults
**T7MDEFNDC.RWN** (ISTECH.LIB, procs=252) — non-default config
**Key tables:** BKSYMSTR, BKYSMSTR, MTICMSTR, CLASMSTR, ISBANKS, ISCC, ISBINLOC, BKSYAP, BKESTCFG, BKFOCFG, BKCPMSTR, BKCMCNTD
**Summary:** At 435 procs, T7MDEFAULTS is one of the largest modules in EVO — covers all company-level defaults: inventory classes (CLASMSTR), banking (ISBANKS), CC (ISCC), bin locations (ISBINLOC), and module config tables (BKESTCFG = Estimating defaults, BKFOCFG = FO defaults).

---

### Visual Scheduler (T7VSCHED)

**T7VSCHED.RWN** (EVO.LIB, procs=94) — visual production scheduling board
**Key tables:** WORKORD, WOROUT, WCTRLOAD, BKICMSTR, BKARINV, BKARINVL, FILELOC
**Summary:** Visual scheduling board for work center capacity. WCTRLOAD aggregates WO operations into capacity buckets per work center. Displays capacity-loaded production schedule from open WOs + SO demand.

---

### Alternate Parts / Substitutes (T7ALTPART)

**T7ALTPART.RWN** (LISTG60.LIB, procs=104) — alternate/substitute item maintenance
**Key tables:** BKSBPART (substitute part master), BKICMSTR
**Summary:** BKSBPART links a primary item code to acceptable substitute items. Used in SO and WO to offer or auto-substitute components when primary item is out of stock.

---

### Bin Setup / Warehouse Locations (T7BINSET)

**T7BINSET.RWN** (LISTG60.LIB, procs=102) — bin and location configuration
**Key tables:** BKICLOC, MTICMSTR, ISBNMSTR, ISBINLOC, BKPIPHYS, BKPIFROZ
**Summary:** Configures warehouse bin/location structure. ISBNMSTR = bin master, ISBINLOC = bin-to-item assignments. Integration with BKPIPHYS/BKPIFROZ confirms bins are used in PI freeze/count cycles.

---

### Quick SO Entry (T7QSOA)

**T7QSOA.RWN** (EVO.LIB, procs=72) — rapid sales order entry
**T7QSOALINES.RWN** (LISTG60.LIB, procs=70) — QSO line items
**Key tables:** BKARCUST, ISQSOA, BKARINVL, BKARINV, BKICMSTR, MTICMSTR, BKICLOC, BKICPMAT
**Summary:** Quick SO entry bypasses the full T7SOA workflow. ISQSOA is the quick-order staging table. BKICPMAT live price lookup included. Used for fast phone/counter orders.

---

### Multi-Company Chain Management (T7CHAIN, T7CHAINM)

**T7CHAIN.RWN** (EVO.LIB, procs=62) — chain entry
**T7CHAINM.RWN** (EVO.LIB, procs=40) — chain manager
**Key tables:** ISCHAINM, BKPSUSER, BKSYMSTR, FILEDICT
**Summary:** Links multiple company databases into a "chain" for inter-company transactions. ISCHAINM = chain master. Architecture: one company is the "home"; others are in the chain for intercompany PO/AR flows.

---

### Corrective Action Request Follow-Up (T7CARFUP)

**T7CARFUP.RWN** (EVO.LIB, procs=53) — CAR follow-up tracking
**Key tables:** ISFUTYPE
**Summary:** Tracks follow-up actions on Corrective Action Requests. ISFUTYPE = follow-up type codes. Linked to the AC (NCR) module.

---

### Paperless Shop Floor / WO Dispatch (T7PAPERLESS)

**T7PAPERLESS.RWN** (LISTG60.LIB, procs=205) — paperless WO dispatch
**Key tables:** WORKORD, MTICMSTR, WOROUT, ROUTING, BKICLOC, ISBINLOC, ISWOEX
**Summary:** Paperless Shop Floor dispatch for PC terminals (see HH module for handheld variant). ISWOEX = IS WO Extensions (operator notes, dispatch status per operation). Dispatches WO operations without paper traveler documents.

---

### Service/Repair Type Code Setup

6 modules managing type-code master tables for the SR module, all using ISSTYPE as the primary table:

| Module | Table | Purpose |
|--------|-------|---------|
| T7SERR.RWN | ISSTYPE | Service error types |
| T7SETYPE.RWN | ISSETYPE | Service event types |
| T7SEPROC.RWN | ISSEPROC | Service process types |
| T7STTYPE.RWN | ISSTYPE | Service ticket types |
| T7STEQUIP.RWN | ISSTYPE | Equipment types |
| T7STYPE.RWN | ISSTYPE | Service types (generic) |

All are 52-proc EVO.LIB CRUD screens over SR reference tables.

---

### User-Defined Invoice Fields (T7UDFINV)

**T7UDFINV.RWN** (LISTG60.LIB, procs=16)
**Key tables:** ISUDFINV
**Summary:** Custom field definitions for AR invoices. ISUDFINV stores the field definitions. Allows per-site custom invoice data without core table changes.

---

### NACHA / ACH Payment Files (T7TESTNACHA)

**T7TESTNACHA.RWN** (LISTG60.LIB, procs=103)
**Key tables:** ISBANKS, BKGLCHK, BKAPVEND
**Summary:** Generates and validates NACHA ACH payment files for AP check runs. ISBANKS provides routing numbers, BKGLCHK = GL check register.

---

### DBA ↔ EVO Migration Utilities (T7DBA2EVO, T7EVO2DBA)

**T7DBA2EVO.RWN** (NZLICE.LIB, procs=36) — DBA Manufacturing → EvoERP
**T7EVO2DBA.RWN** (EVO.LIB, procs=51) — EvoERP → DBA Manufacturing
**Key tables (both):** BKARCUST, BKAPVEND, WORKORD, BKICMSTR, ISNOTES, BKARINV, BKAPPO
**Summary:** Data migration between DBA Manufacturing (EVO's predecessor) and EvoERP. Used during upgrades and for sites running both systems in parallel.

---

---

### EvoDrillDown Panels (T7SMJ* family)

The T7SMJ* modules are the **EvoDrillDown analysis panels** — specialized read-only drill-down views that appear when a user clicks into a record from any context in EVO. Each panel is optimized for one entity type and opens the complete set of related tables.

| Module | Entity | Key tables |
|--------|--------|-----------|
| T7SMJA | Work Orders (full) | WORKORD, WORECV, BKDCLAB, WOEXCHG, WODATE, WOROUT, WOBOM, WOMAT, OUTPROC, WOBOMREM, WOLABOR |
| T7SMJB | Work Orders (alt) | WORKORD, WODATE, WOBOM, WOMAT, WOLABOR, WOROUT, ISWOROEX, OUTPROC, WORECV, WOEXCHG |
| T7SMJC | Inventory items | BKICLOCM, BKICMSTR, CLASMSTR, CLASS, MTICMSTR, BKICLOC, INVTXN, DBAFIFO |
| T7SMJD | Inventory transactions | BKICMSTR, INVTXN, BKYSMSTR, MTICMSTR, BKICLOC |
| T7SMJF | Purchase Orders | BKAPPO, BKAPDESC, ISNOTES, BKAPPOL |
| T7SMJG | QC records | BKQCMSTR, BKQCTRAN, ISNOTES, ISLINKS |
| T7SMJH | DC Labor | BKDCLAB |
| T7SMJI | Estimates | ISESTDTL, BKARINV, BKARINVL, BKBMMSTR, ROUTING, ISNOTES |
| T7SMJJ | SO/Invoice | BKARINV, BKARINVT, BKARINVL, BKAPDESC, ISSOBOX, BKARHTAX, ISSRINFO, ISARCHG, ISSRMMS |
| T7SMJK | SO/Invoice (NZ locale) | Same as SMJJ |
| T7SMJL | Master (all entities) | 459 procs, 92 tables — universal hub |
| T7SMJM | Customers | BKARCUST, BKARINVT, BKARINVV, BKICPMAT, BKICREF, BKPRCOMM, ESTSUM, INVTXN, WORKORD, SERIAL, BKCMACCL |
| T7SMJN | Vendors | BKAPVEND, BKCMVNDH, BKCMVNDF, BKICTAX, ISTAXFIL, ISBROKER, BKCPEC, ROUTING, BKAPINVT, BKAPCHKF, BKAPINVL |
| T7SMJO | AR/AP combined | BKAPVEND, BKARCUST, BKAPCHKF, BKARINVT, BKARDEP, BKARINV, BKARINVL, BKARINVV, BKAPINVT |
| T7SMJQ | Item/BOM | BKSYMSTR, BKICMSTR, BKBMMSTR |
| T7SMJR | PO (variant) | BKAPPO, BKAPDESC, ISNOTES, BKAPPOL |
| T7SMJS | Item (simple) | BKICMSTR, MTICMSTR |
| T7SMJV | Payroll | BKPRCURP, BKPRMSTR, BKPRINFO, BKPRGLFL |

**New tables discovered in this family:**
- `WOEXCHG` — WO Exchange (inter-company WO transfer)
- `ISWOROEX` — IS WO Routing Operations Extensions
- `BKICLOCM` — IC Location Master
- `DBAFIFO` — DBA FIFO cost layers (inventory costing)
- `ISESTDTL` — IS Estimating Detail
- `ISSOBOX` — IS SO Box/packing data
- `BKARHTAX` — AR Head Tax
- `ISSRMMS` — IS SR Maintenance Management System data
- `BKCMVNDH/BKCMVNDF` — CM Vendor History/Footer
- `ISBROKER` — IS Broker (customs/freight broker)
- `BKCPEC` — Compliance/customs data
- `BKPRCURP` — PR Current Payroll
- `BKPRINFO` — PR Employee Info
- `BKCMACCL` — CM Account Links
- `ESTSUM` — Estimate Summary
- `BKPRCOMM` — PR Commissions

---

---

### Inventory Lookup Sub-Modules (T7INL* — 23 files)

T7INL* = Inventory item lookup panels used across modules for item selection:

| Module | Focus | Key new tables |
|--------|-------|---------------|
| T7INLA | Basic item lookup | ISICMSTR (IS IC extended data) |
| T7INLB | Location/bin lookup | BKICLOCM, ISBINLOT |
| T7INLC | Item cross-reference | BKICREF |
| T7INLD | Reference lookup | BKICREF |
| T7INLE | Item + PO + class | ISCATMST (IS Category Master), CLASS |

**New tables confirmed:** BKICREF = IC item cross-reference (alternate item codes, vendor part numbers); ISICMSTR = IS IC Master extended (additional item fields beyond BKICMSTR); ISCATMST = IS Category Master; CLASS = item class table.

---

### SO Open Orders Sub-Modules (T7SOO* — 13 files)

T7SOO* = SO Open Order processing panels. "OO" = Open Orders.

| Module | Focus | Key tables |
|--------|-------|-----------|
| T7SOOA | Open orders + WO + labor | BKARINV, BKARINVL, WORKORD, WOROUT, BKDCLAB, ISSRINFO |
| T7SOOB/C | SO lines | BKICMSTR, BKARINVL |
| T7SOOD | SO header | BKARINV |
| T7SOOE | DBA-era open orders | Full SO + customer + WO |

---

### SO Picking / Processing Sub-Modules (T7SOP* — 13 files)

T7SOP* = SO pick/pack/ship processing. "OP" = Order Processing.

| Module | Focus | Key tables |
|--------|-------|-----------|
| T7SOPA | AR charges on SO | ISARCHG |
| T7SOPB | Picking with SR info | ISSRINFO, BKARCUST |
| T7SOPC | Picking with decorations | ISICMSTR, BKICLOC, ISORDECO |
| T7SOPD/E | ISTS stubs | ISORDECO |

**New table:** ISORDECO = IS Order Decoration — records custom decoration/processing instructions per SO line item (e.g., engraving, custom packaging). Used in manufacturing-to-order environments.

---

### SO Quotation / Pricing Sub-Modules (T7SOQ* — 12 files)

T7SOQ* = SO quotation and pricing lookup panels. "Q" = Quotation.

| Module | Focus | Key tables |
|--------|-------|-----------|
| T7SOQA | Pricing matrix | BKICPMAT (IC pricing matrix) |
| T7SOQB | Item lookup | BKICMSTR |
| T7SOQC | Item + class + price | CLASMSTR, ISCATMST, BKICPMAT |
| T7SOQD/E | NZ locale | Same as C |

---

### WO Sub-Modules: Operations and BOM (T7WOK* — 19 files)

T7WOK* = WO operations and kit/BOM management panels.

| Module | Focus | Key tables |
|--------|-------|-----------|
| T7WOKA | WO routing operations | WORKCTR, MACHINE, TOOL, ROUTING, ISWOROEX |
| T7WOKB | WO BOM view | WOBOM, BKBMMSTR, BKICLOC |
| T7WOKC | WO with dates + exchange | WODATE, WOEXCHG, ISNOTES |
| T7WOKD | WO with extensions | ISWOEX, ISICMSTR |
| T7WOKE | WO BOM with substitutes | BKSBPART, WOBOMREM, ISWOEX |

**New tables confirmed:** MACHINE = Machine master (routing resources — specific machines within work centers); TOOL = Tool master (cutting tools, fixtures, jigs tracked per routing operation).

---

### WO Labor Sub-Modules (T7WOL* — 15 files)

T7WOL* = WO labor entry, reporting, and payroll integration panels.

| Module | Focus | Key tables |
|--------|-------|-----------|
| T7WOLA | DBA-era WO list | Full WO set |
| T7WOLB | WO + labor + SO | BKDCLAB, BKARINVL |
| T7WOLC | WO + work center + PO | WORKCTR, BKAPPOL |
| T7WOLD | WO + inventory txn | INVTXN, ISCATMST |
| T7WOLE | WO labor → Payroll | WOLABOR, BKPRCURP, BKPRMSTR, BKCPMSTR |

**T7WOLE confirms WO→PR bridge:** WOLABOR (WO labor transactions) flows to BKPRCURP (PR current payroll batch) for payroll processing. BKCPMSTR = Cost Period Master (tracks cost periods for labor absorption).

---

### Payroll List Sub-Modules (T7PRL* — 16 files)

T7PRL* = Payroll report/list panels. All open the same core PR tables:
- BKPRMSTR = PR employee master
- BKPRCURP = PR current payroll batch
- BKPRINFO = PR employee detailed info
- BKPRGLFL = PR GL flags (deduction/tax GL accounts)

Each T7PRL variant focuses on a different PR report or subset (pay period, department, GL distribution, etc.).

---

### Routing Operations Sub-Modules (T7ROJ* — 8 files)

T7ROJ* = Routing operations maintenance and related master data.

| Module | Focus | Key tables |
|--------|-------|-----------|
| T7ROJA | Routing + SPC | WOROUT, WOBOM, ROUTING, ISSPC, BKRTSPEC |
| T7ROJB | Work center master | WORKCTR |
| T7ROJC | Machine master | MACHINE |
| T7ROJD | Tool master | TOOL, MACHINE |
| T7ROJE | QC codes master | QCCODES |

**New tables confirmed:** ISSPC = IS SPC link (ties routing operations to SPC data collection — direct ERP→SPC data feed); QCCODES = QC codes master (defect classification codes, distinct from BKQCMSTR inspection records); BKRTSPEC = Routing Spec (operation specifications detail).

---

### PO RFQ Sub-Modules (T7POI* — 10 files)

T7POI* = RFQ (Request for Quote) modules accessed from within the PO workflow.

**Key tables:** BKRFQ (BK Request for Quote), BKICMSTR, BKAPVEND, BKAPPOL, BKAPPO

**Summary:** Vendor RFQ workflow initiated from PO. BKRFQ = RFQ master table — stores quote requests sent to vendors for pricing. Cross-links to BKAPPOL (PO lines) when quotes are accepted and converted to POs.

---

### PO Receiving QC Sub-Modules (T7POJ* — 4 files)

T7POJ* = Quality inspection performed when receiving PO items.

| Module | Focus | Key tables |
|--------|-------|-----------|
| T7POJA | Receiving inspection | BKQCMSTR, BKAPPOL, BKAPPO, ISORDECO, BKQCTRAN |
| T7POJB | Receiving QC + WO | BKQCMSTR, BKAPPO, WORKORD, BKQCTRAN |
| T7POJC | DBA-era QC receiving | 323 procs — full QC receive |
| T7POJD | QC by vendor | BKQCTRAN, BKAPVEND |

**Summary:** Receiving QC bridges PO (BKAPPO/BKAPPOL) with QC (BKQCMSTR/BKQCTRAN). Items received on a PO are inspected; failures generate QC transactions. T7POJC at 323 procs is the full-featured version.

---

---

### SM Sub-Module Families — Reference Data Setup

The T7SM* sub-modules are the SM (System Manager) setup screens for reference data.
Each 52-53 proc EVO.LIB screen is a CRUD UI over one master table:

| Module | Table | Content |
|--------|-------|---------|
| T7SMIA | BKCMLEAD | CRM Lead Source codes |
| T7SMIB | BKCMTERR | CRM Territory codes |
| T7SMIC | BKCMACFC | CRM Account Financial Category |
| T7SMID | BKCMACCC | CRM Account Contact Category |
| T7SMIE | BKCMDTCD | CRM Document Type codes |
| T7SMIF | ISCATMST | IS Category Master |
| T7SMPA | ISCATMST | Category (alternate view) |
| T7SMPB | ISUDMSTR | User-Defined Master field definitions |
| T7SMPF | ISJOB | IS Job master (job cost numbers) |
| T7SMCA | CLASMSTR + BKGLCOA | Class master with GL account mapping |
| T7SMCB | CLASMSTR | Class master simple |
| T7SMT | ISSHPVIA | Ship Via / freight carrier codes |
| T7SMU | ISSHPVIA + BKARCUST | Ship Via with customer defaults |
| T7SMW | ISORDDSC | Order Discount codes |
| T7SMK | ISNUMBER + LANGDICT | Auto-number counters + language |
| T7SMNA | ISNTYPE + ISNOTES | EvoNotes note type setup |

**New tables confirmed:** ISUDMSTR (IS UD Master — user-defined field type definitions), ISJOB (IS Job master — job cost numbers), ISORDDSC (IS Order Discount codes), ISSHPVIA (IS Ship Via — carrier/method codes), BKCMLEAD (CRM lead sources), BKCMTERR (CRM territories), BKCMACFC/BKCMACCC (CRM categories), BKCMDTCD (CRM doc type codes).

---

### SMT — Surface Mount Technology Integration (T7SMTEND, T7SMTSET)

**T7SMTEND.RWN** (LISTG60.LIB, procs=97) — SMT run end
**T7SMTSET.RWN** (LISTG60.LIB, procs=128) — SMT setup

**Key tables:** ISSMTCFG, MACHINE, WORKORD, WOBOM, BKICMSTR, ISLINKS, ISSERIAL

**Summary:** EvoERP includes an SMT (Surface Mount Technology) integration module for PCB assembly manufacturers. T7SMTSET configures the SMT machine (ISSMTCFG = machine program / component placement config). T7SMTEND records run completion, linking back to WORKORD + WOBOM (WO BOM for PCB assembly). MACHINE = the pick-and-place machine. ISSERIAL tracks assembled PCB serial numbers.

This is a highly specialized module for electronics/PCB contract manufacturers — rare ERP capability confirming EvoERP's electronics industry penetration.

---

### GL Journal Entry Sub-Modules (T7GLO, T7GLE, T7GLS, T7GLP)

**T7GLO.RWN** (EVO.LIB, procs=165) — GL journal entry (main)
**T7GLE/T7GLE2/T7GLESPEED.RWN** (LISTG60.LIB) — GL entry variants (191/156/164 procs)
**T7GLP.RWN** (ISTECH.LIB, procs=87) — GL posting
**T7GLS.RWN** (EVO.LIB, procs=78) — GL journal summary/notes

**Key tables:** BKGLTRAN, BKGLCOA, BKSYMSTR, BKYSMSTR, ISGLCOA, ISGLDATE, BKARCUST, BKAPVEND

**New tables confirmed:**
- `ISGLCOA` — IS GL COA (extension to chart of accounts — multi-year account history or budget data)
- `ISGLDATE` — IS GL Date (current GL period/year-end dates per company/module)
- `BKGLTRAN` = core GL transaction register

**Summary:** T7GLO = main GL journal entry; T7GLE/GLESPEED = alternative/fast entry UIs; T7GLP = posting GL transactions to BKGLTRAN; T7GLS = GL journal with notes. All read ISGLDATE for current period validation. ISGLCOA extends BKGLCOA with additional per-account historical data.

---

## Module table ownership matrix

Quick reference — which module is the PRIMARY owner of each core table:

| Table | Owner module | Also used by |
|-------|-------------|-------------|
| BKARCUST | T7ARA (AR Customer) | T7SOA, T7POA, T7WOA, T7INA |
| BKARINV | T7SOA (Sales Orders) | T7WOA, T7INA |
| BKAPVEND | T7APA (AP Vendors) | T7POA, T7SOA, T7APM |
| BKAPPO | T7POA (Purchase Orders) | T7WOA, T7INA, T7SOA |
| BKICMSTR | T7INA (Inventory) | Every module |
| WORKORD | T7WOA (Work Orders) | T7INA, T7POA, T7SOA |
| WOBOM/WOMAT/WOLABOR | T7WOA (Work Orders) | T7INA, T7POA |
| BKBMMSTR | BM module (T7BMA) | T7WOA, T7INA, T7SOA, T7POA |
| BKGLTRAN | GL module (T7GLA) | Every module |
| INVTXN | T7INA (Inventory) | T7WOA |
| ROUTING | RO module | T7WOA, T7INA, T7SOA |
| LOT/SERIAL | LC/SC modules | T7INA, T7WOA, T7ARA, T7SOA |
| BKQCMSTR/BKQCTRAN | QC module | T7SMJL |
| BKPIFROZ/BKPIPHYS | PI module | T7SMJL |
| FILELOC/FILEDICT | TAS infrastructure | wtasdmgr, wtasdatam, wtasinit |
| BKSAREPT | SA module (T7SAM) | T7SAN |
| BKACTRPT | SA module (T7SAM) | T7SAN |
| BKPRAGNT | CS module (T7CSA) | T7CSB |
| BKCMACCC | SA module (T7SAO) | T7CSB |
| BKCMACCL | SA module (T7SAO) | — |
| BKCMDTCD | CS module (T7CSB) | — |
| BKDCCFG/BKDCLAB/BKDCSHFT | DC module (T7DCA/T7ADCA) | T7DE* stubs |
| BKBMMSTR | BM module | T7WOA, T7INA, T7SOA, T7FOC, T7POA |

---

## Pass 9 — Newly Discovered Subsystems (2026-06-17)

### Field Service (FS) — T7FSCLASS / T7FSINFO / T7FSEMP

**Purpose:** Field Service module — tracks service classes, field service information records, and employee-to-class assignments. Optional add-on; no CHM entries found in this install.

| Module file | Procs | Key tables | Purpose |
|-------------|-------|-----------|---------|
| T7FSCLASS.RWN | 62 | ISFSCLAS, ISPRINFO | Service class master + employee info |
| T7FSINFO.RWN | 61 | ISFSINFO | Field service information records |
| T7FSEMP.RWN | 59 | ISFSCLAS, BKPRSALE | Employee-to-service-class assignments |

**New tables:** ISFSCLAS (field service class master), ISFSINFO (FS info records), ISPRINFO (PR employee profile info)

---

### Global Finance / AR Charges (GF) — T7GFPRICE / T7GFV / T7GFVS / T7GFR

**Purpose:** Global Finance charges system — applies extra AR charges to invoices beyond line items. GFV/GFVS browse existing charge records; GFPRICE is the pricing/charge entry form; GFR is the report.

| Module file | Procs | Key tables | Purpose |
|-------------|-------|-----------|---------|
| T7GFPRICE.RWN | 116 | BKARCUST, BKICPMAT, BKICMSTR, MTICMSTR, ISICMSTR | Customer + item pricing/charge entry |
| T7GFV.RWN | 82 | BKARINV, ISARCHG, BKARINVL, BKICPMAT | Invoice charge viewer |
| T7GFVS.RWN | 81 | BKARINVL, BKARINV, BKICPMAT | Invoice lines + charges summary |
| T7GFR.RWN | 46 | (standard tables only) | Report |

**New tables:** ISARCHG (IS AR extra charges added to invoices), ISICMSTR (IS secondary item master — alternate item config)

---

### Reminders & Rebuild Utilities (RE family)

**Purpose:** Mixed group of reminder/scheduling tools and data-integrity rebuild utilities.

| Module file | Procs | Key tables | Purpose |
|-------------|-------|-----------|---------|
| T7RemindRpt.RWN | 125 | ISREMIND, BKARCUST, BKCMACCN | CRM/AR reminder report |
| t7rebwo.RWN | 123 | WORKORD, WOBOM, WORECV, WOROUT, WOMAT, WOLABOR | WO data rebuild utility |
| T7REPLNK.RWN | 67 | ISREPLNK, BKPRSALE, BKARCUST, BKICMSTR, CLASMSTR | Replace links (record-link replace tool) |
| T7REBQC.RWN | 62 | BKICMSTR | QC data rebuild utility |
| T7REPDEF.RWN | 52 | ISREPDEF | Saved report parameter defaults |
| T7REINDEX.RWN | 36 | FILELOC | Btrieve file reindex utility |
| t7redindexDD.RWN | 5 | WORKORD, WOBOM, WOMAT, WOLABOR | Data dictionary reindex (WO set) |
| t7ResetDFM.RWN | 5 | ISREPLNK | Reset DFM form layouts to defaults |

**New tables:** ISREMIND (reminder/follow-up records — date + contact + trigger), ISREPLNK (replace-link records), ISREPDEF (saved report defaults/parameters)

---

### Service Code Tables (SE / ST families)

**Purpose:** Code/master tables supporting the SR (Service/Repair) module. All share the ISSTYPE shared-type table; SE = service error process/type codes; ST = service/storage/equipment type codes.

| Module file | Procs | Key tables | Purpose |
|-------------|-------|-----------|---------|
| T7SEPROC.RWN | 52 | ISSEPROC | Service error process codes |
| T7SERR.RWN | 52 | ISSTYPE | Service error type codes |
| T7SETYPE.RWN | 52 | ISSETYPE | Service error category types |
| T7STEQUIP.RWN | 52 | ISSTYPE | Equipment type codes |
| T7sttype.RWN | 52 | ISSTYPE | Storage/service type codes |
| T7STYPE.RWN | 52 | ISSTYPE | Service type master |
| T7STOCK.RWN | 53 | BKCMACCC | CRM stock/account classification |

**New tables:** ISSTYPE (shared service/storage/equipment type code table), ISSEPROC (SE process codes), ISSETYPE (SE category types)

---

### Warehouse Put-Away (PU) — T7PUTAWAY

**Purpose:** Warehouse put-away operation — places received items into bin locations after PO receipt. 105 procs; updates item master with bin location assignments.

**Key tables:** BKICMSTR, MTICMSTR (item master bin update)

---

### Multi-Yield Work Orders (MU) — T7MULTIYIELD

**Purpose:** Multi-yield / co-products WO processing — records multiple output part numbers from a single work order (co-products and by-products). 150 procs; opens the full WO + inventory transaction chain.

**Key tables:** WORKORD, WOROUT, WOBOM, WORECV, INVTXN, BKICMSTR, BKICLOC, ISBINLOC, BKARINVL, MTICMSTR, BKYSMSTR

**New tables:** ISBINLOC (bin location master — distinct from BKICLOC item locations)

---

### Audit Log Setup (AL) — T7ALOGSETUP

**Purpose:** Configures which tables and events are written to the system audit log. Opens FILELOC (all registered DB files) + BKSYMSTR (system master) + BKPSUSER (PS user list) to define what gets logged and for which users.

**Key tables:** FILELOC, BKSYMSTR, BKPSUSER

---

### Module Access / License Control (LI) — T7LIMACC

**Purpose:** License and module access control — ISACCESS table determines which EvoERP modules are enabled/licensed for this installation. 42 procs; the access-control gatekeeper for optional modules.

**New tables:** ISACCESS (module access/license flags)

---

### Multi-Language Configuration (ML) — T7MLC

**Purpose:** Multi-language/localization support for AR invoices. Opens LANGDICT (language dictionary) + BKARINV/BKARINVL + MTICMSTR + ISREPORD (repeat order records) + BKICLOC.

**New tables:** ISREPORD (IS repeat/standing order records — recurring AR orders)

---

### Shipping Configuration (MH) — T7MHOPE

**Purpose:** Shipping and carrier configuration tool — 98 procs. Opens ISSHIPCO (shipping company/carrier master), ISSHPVIA (ship-via methods), BKCMTERR (CRM territory), BKARINV/BKARINVL, ISREPORD. Configures carrier–territory–ship-via relationships for outbound shipments.

**New tables:** ISSHIPCO (shipping company/carrier master — carrier names, codes, contact info)

---

### EDI Invoice Import (ED) — T7EDII

**Purpose:** Inbound EDI invoice processing — 183 procs. Creates AR invoices from EDI data. Opens the full AR invoice chain: BKARINV + BKARINVL + BKARCUST + ISTERMS + BKICPMAT + BKICLOC + ISARCHG + CLASMSTR.

**Key tables:** BKYSMSTR, MTICMSTR, BKARINV, BKARINVL, ISARCHG, BKARCUST, BKSYMSTR, ISTERMS, BKICMSTR, BKICPMAT, BKICLOC, CLASMSTR

Related: `t7ediftp.RWN` (5 procs, BKEDMSTR — EDI FTP transfer); `t7edudf.RWN` (8 procs, ROUTING — EDI UDF/routing)

---

### Brands Master (BR) — T7BRANDS

**Purpose:** Product brand master linked to CRM account classifications. 53 procs; opens BKCMACCC (CRM Account Class). Brands are stored as CRM account class codes.

Related: `T7BROWSER.RWN` (4 procs) — HTML browser window embedded in EvoERP UI.

---

### Auto FX Currency Update (AU extension) — T7AUTOFX

**Purpose:** Automated foreign exchange rate update via Java integration. Opens ISMCF (multi-currency foreign exchange config) + ISJAVA (Java task queue) + ISMCR (exchange rates). Queues a Java task to fetch/update live exchange rates.

**New tables:** ISMCF (IS multi-currency foreign exchange config — base currency, conversion settings); ISMCR confirmed as exchange rate table (also used by T7IMC)

---

### New Company Initialization (NE) — T7NEWINIT

**Purpose:** Creates and initializes all required Btrieve data files for a new company. Opens FILELOC (file registry) + FILEDES (file descriptions) to enumerate and create the full table set.

**New tables:** FILEDES (file descriptions/purpose strings for each DB file in the registry)

---

### WO Cut Sheet / Material List (CU) — T7CUTSHEET2

**Purpose:** Generates a material cut sheet for shop floor — lists WO materials with lot and bin assignments. 75 procs; opens WOMAT + LOT + WORKORD + WOBOM + ISBINLOT + BKPSUSER.

**New tables:** ISBINLOT (bin + lot cross-reference — which lots are in which bins), LOT (lot master — distinct from MTLOT)

---

### Jobs / Department Management (JO) — t7jobs

**Purpose:** HR-like job positions and department management. 21 procs; opens ISDEPT (department master) + BKARCUST + BKAPVEND + WOEXCHG + CLASMSTR + ISCATMST.

**New tables:** ISDEPT (department master — dept codes, names, GL accounts)

---

### File Navigator / Report (FN) — T7FNR

**Purpose:** Btrieve file/data dictionary browser and report. 104 procs; opens FILELOC + FILEDICT to enumerate all registered database files and their dictionary definitions. Likely a TA (System Administration) sub-tool.

---

### CC Cross-Reference Utility (XC) — T7XCUTIL

**Purpose:** Credit card cross-reference/cleanup utility. 29 procs; opens BKCMACCT (CRM Account) + BKYSMSTR + ISCC (credit card records) + LANGDICT. Reconciles CC data across CRM and billing.

---

### LGS Customer Module (LG) — t7lgssoe / T7LGSSOEVerify

**Purpose:** Customer-specific customization for "LGS" customer (similar to J7* pattern but with LGS prefix). Processes AR invoices with tax/customs — opens BKARINV + BKARCUST + BKARINVL + BKYSMSTR + BKICMSTR + BKARTXN + BKSYMSTR + BKICTAX + BKICLOC. "SOE" may = Statement of Entry (customs compliance).

| Module file | Procs | Purpose |
|-------------|-------|---------|
| t7lgssoe.RWN | 170 | Main SOE invoice processing |
| T7LGSSOEVerify.RWN | 41 | SOE data verification |

**New tables:** BKICTAX (IC Tax codes — item-level tax classification), BKARTXN (AR transactions log)

---

### JS Integration Settings (JS family)

**Purpose:** JavaScript/Java integration layer — settings, SQL access, and data bridge modules for external reporting tools (Power BI, SQL Reporting Services, etc.).

| Module file | Procs | Key tables | Purpose |
|-------------|-------|-----------|---------|
| t7jsettings.RWN | 70 | FILELOC | JS integration settings manager |
| T7jsql.RWN | 52 | (standard only) | Internal SQL query tool |
| t7jsacc.RWN | 50 | (standard only) | JS Accounting data bridge |
| t7jsaIc.RWN | 50 | (standard only) | JS Inventory Control bridge |
| t7jsaPBI.RWN | 50 | (standard only) | JS Power BI data bridge |
| t7jsaSRS.RWN | 50 | (standard only) | JS SQL Reporting Services bridge |
| t7jsoi.RWN | 50 | (standard only) | JS Open Items bridge |

---

### AP Extra Charges (MSG utility) — T7MSG

**Purpose:** Message/notification utility stub. 0 procs (stub). Opens ISBUILD + MTMRP + BKAPPO + BKAPPOL + ISAPCHG + BKAPVEND.

**New tables:** ISBUILD (IS build/kit record — links to BOM build operations), ISAPCHG (IS AP extra charges — parallel to ISARCHG for AP side)

---

### Job File Transfer (JF) — t7jftrans

**Purpose:** WO/labor job file transfer to external system. 27 procs; opens FILELOC + BKPSUSER + WOLABOR + WOROUT + BKPRMSTR + WOEXCHG. Transfers WO labor and routing data with payroll integration.

---

### Additional Pass-9 Module Table Ownership

| Table | Owner module | Also used by |
|-------|-------------|-------------|
| ISFSCLAS | T7FSCLASS (FS) | T7FSEMP |
| ISFSINFO | T7FSINFO (FS) | — |
| ISARCHG | T7EDII (ED) | T7GFV, T7GFVS |
| ISAPCHG | T7MSG | — |
| ISREMIND | T7RemindRpt (RE) | — |
| ISREPLNK | T7REPLNK (RE) | T7ResetDFM |
| ISREPDEF | T7REPDEF (RE) | — |
| ISSTYPE | T7SERR/T7STEQUIP/T7sttype/T7STYPE | shared code table |
| ISSEPROC | T7SEPROC (SE) | — |
| ISSETYPE | T7SETYPE (SE) | — |
| ISBINLOC | T7MULTIYIELD (MU) | — |
| ISBINLOT | T7CUTSHEET2 (CU) | — |
| ISACCESS | T7LIMACC (LI) | — |
| ISSHIPCO | T7MHOPE (MH) | — |
| ISREPORD | T7MLC (ML) | T7MHOPE |
| ISDEPT | t7jobs (JO) | — |
| ISMCF | T7AUTOFX (AU) | — |
| ISBUILD | T7MSG | — |
| BKICTAX | t7lgssoe (LG) | — |
| BKARTXN | t7lgssoe (LG) | — |
| FILEDES | T7NEWINIT (NE) | T7FNR |
| LOT | T7CUTSHEET2 (CU) | T7SMJC, T7WOKA |
| ISSCHED | EvoScheduler | EvoSched, EVOSERVICE, evoremind |
| SCHEDCAL | T7SHE (SH-E) | T7SMH |
| ISLINKS | EvoLinks | T7SMSB, T7SMSC, T7SMTEND |

---

## Pass 10 — Additional Subsystems (2026-06-17)

### BS Business Score/Summary — T7BS

**Purpose:** Business Intelligence dashboard — 162 procs. Combines GL (BKGLTRAN, ISGLDATE, BKSYMSTR) + WO (WORKORD, WOMAT, WOLABOR) + item (MTICMSTR, BKICMSTR). Primary table ISBSF = IS Business Score File — cross-module business performance summary.

**New tables:** ISBSF (IS Business Score/Summary — cross-module KPI aggregation)

---

### Advanced Data Collection (AD) — T7ADCA

**Purpose:** Advanced/main Data Collection module — 290 procs (largest DC module). Opens BKDCLAB + WORKORD + BKPRMSTR + BKDCSHFT + ISWOEX + EIMCOLST. Full automatic data collection entry module for shop floor; ISWOEX = WO extension data.

**New tables:** EIMCOLST (EIM Column List — column configuration for EIM/DC integration)

---

### Request for Quote from Estimates (RF) — T7RFQ

**Purpose:** Generates vendor RFQs from estimate data — 103 procs. Bridges ES (Estimating) and PO modules for vendor price solicitation. Opens ISESTDTL (estimate line items) + BKMRPPO (MRP PO recommendations) + BKBMMSTR + BKICMSTR + BKAPVEND + BKAPPO + BKSBVEND.

**New tables:** ISESTDTL (IS Estimate Detail — estimate line items), BKMRPPO (BK MRP PO — MRP-generated PO recommendations), BKSBVEND (BK Sub-contract Vendor — sub-contracting vendor table)

---

### Item Serial Counter Configuration (IT) — T7ITMCFG

**Purpose:** Configures serial number generation counters per item — 66 procs. Opens ISSERCNT (serial number counter master) + BKICMSTR. Sets up how serial numbers are auto-generated for each serialized item.

**New tables:** ISSERCNT (IS Serial Count — serial number counter/sequence control per item)

---

### Standard Detail Codes (SD) — T7SDET

**Purpose:** Standard Detail maintenance — 58 procs. Opens ISSDET (standard detail records) + ISSTYPE. Maintains type-value code pairs used across modules (flexible code-value lookup system).

**New tables:** ISSDET (IS Standard Detail — type/detail code pairs; paired with ISSTYPE)

---

### Emergency GL Account Maintenance (EM) — T7EMGL

**Purpose:** Emergency GL account maintenance utility — 62 procs. Opens BKGLCOA (Chart of Accounts). Provides raw edit mode for GL accounts bypassing normal workflow restrictions.

---

### Reminder System (EvoRemind) — evoremind.RWN

**Purpose:** CRM/transaction reminder system — 46 procs. Opens ISREMIND + BKYSMSTR + BKSYUSER + ISTRIGRS + BKPSUSER + BKAPPOL + BKICMSTR + BKAPPO + BKARINVL. Reminders link to active PO lines, AR lines, and items.

**New tables:** BKSYUSER (BK SY User — additional session/user table, complement to BKLOGON), ISTRIGRS (IS Trigger Results — automated trigger execution log)

---

### Lookup Grid Configuration (GT) — t7gtemp

**Purpose:** Grid template / lookup grid configuration — 27 procs. Opens BKLUGRID (BK Lookup Grid config) + BKPSUSER.

**New tables:** BKLUGRID (BK Lookup Grid — lookup grid column/layout configuration)

---

### Java Integration Setup (JA) — T7JAVASET / T7JAVARUN

**Purpose:** Java integration configuration and launcher.
- T7JAVASET (57 procs): FILELOC + ISACCESS + LANGDICT + BKSYMSTR — configures EvoPVT.jar; checks ISACCESS for Java module license.
- T7JAVARUN (11 procs): BKICMSTR + MKAHIST — lightweight launcher for Java tasks.

---

### Pass-10 Table Ownership Additions

| Table | Owner module | Also used by |
|-------|-------------|-------------|
| ISBSF | T7BS (BS) | — |
| EIMCOLST | T7ADCA (AD) | — |
| ISESTDTL | T7RFQ (RF) | — |
| BKMRPPO | T7RFQ (RF) | — |
| BKSBVEND | T7RFQ (RF) | — |
| ISSERCNT | T7ITMCFG (IT) | — |
| ISSDET | T7SDET (SD) | — |
| BKSYUSER | evoremind | — |
| ISTRIGRS | evoremind | — |
| BKLUGRID | t7gtemp (GT) | — |

---

## Pass 11 — SA, JC, ES, PI, BO, PS, RM, FO, DE, MD, WBKLOOKUP

New families identified from rwn_symbols.json DB fingerprint analysis.

---

### Sales Analysis (SA) — T7SAM / T7SAN / T7SAO + 12 others (15 files total)

**Purpose:** Sales reporting and analysis — trends, sales rep performance, customer profitability. 15 files, ~1,110 procs.
- T7SAM (238 procs, 35 DBs): Uses BKSAREPT (SA report definitions), BKCMLEAD, BKCMTERR, BKPRSALE, BKICREF, ISAREX, ISBUILD, ISRMAI, ISSRINFO, ISMCF, ISMCR.
- T7SAN (220 procs, 31 DBs): Similar to T7SAM (report variant).
- T7SAO: Summary/overview variant.

**Key proc names** (T7SAM): SMSTR, T.CLICK, ONSTART, KUP_TLL, LBAR, LOGIN, ONDISP, LANG, ONCLOSE, NEXTPAGE.PRE, RT_TYPE, AR.CLICK — confirms interactive browsing form.

**New tables:** BKSAREPT (SA report templates/saved report definitions), ISAREX (AR extras — extended AR info), ISRMAI (RMA invoice/auto-invoice records)

---

### Job Cost (JC) — T7JCENG / T7JCA / T7JCM + 11 others (22 files total)

**Purpose:** Job Cost module — project-level cost tracking against customer jobs, separate from standard WO cost. 22 files, ~2,033 procs.
- T7JCENG (211 procs): Engineering/routing side of JC. Uses BKRTSPEC, BKPRMSTR — job cost linked to routing specs and payroll.
- T7JCA (163 procs): JC admin/setup. Uses BKPSUSER (personal settings).
- T7JCM (188 procs): JC master entry — main form. Uses BKPRMSTR, BKARINVL, BKICLOCM.
- T7JCR (167 procs): JC reports.
- T7JCB / T7JCE / T7JCN / T7JCP / T7JCH (119–153 procs each): JC sub-screens. All use BKSBPART (sub-contracted parts) and BKMRPFC.
- T7JCF (137 procs): Uses BKQCTRAN — JC quality transaction linkage.
- T7JCL / T7JCQ (138 procs each): JC list/query screens.
- T7JCRM (62 procs): JC return/RMA sub-screen.

**New tables:** BKSBPART (sub-contracted parts — components sourced from outside processes), BKSBMFG (sub-contracted manufacturing records)

---

### Estimating (ES) — T7ESB / T7ESE / T7EST + 8 others (11 files total)

**Purpose:** Quoting and estimating module — build cost estimates for customer RFQs, generate WOs/SOs from estimates. 11 files, ~1,063 procs.
- T7ESB (213 procs): Main estimate entry form. Uses BKICREF, BKPRSALE, BKPSUSER, ISORDECO, ISECO — can link estimate to ECOs and orders.
- T7ESE (194 procs): Estimate entry variant 2.
- T7EST (163 procs): Estimate templates (uses BKESTCFG — estimate config table).
- T7ESD (162 procs): Estimate defaults/setup (uses BKESTCFG, BKCMACCT).
- T7ESC (124 procs): Estimate cost (uses BKMATCST, BKRFQ, BKRTCST — material cost, RFQ vendor quotes, routing cost).
- T7ESH / T7ESI (60/94 procs): Estimate header/items sub-forms (BKMATCST, BKRFQ, BKRTCST, BKICPMAT).

**New tables:**
- BKESTCFG — estimate configuration settings (method, markup defaults, numbering)
- BKMATCST — material cost records per estimate line (cost + pricing detail)
- BKRFQ — RFQ master (vendor RFQ records tied to estimates)
- BKRTCST — routing cost records (labor/machine cost detail per estimate)
- ESTSUM — estimate summary totals (rolled-up cost/price per estimate)
- BKICPMAT — IC purchase material (item-level purchase material category or config)

---

### Physical Inventory (PI) — T7PIA / T7PIC / T7PIF + 6 others (9 files total)

**Purpose:** Periodic physical inventory count process — freeze inventory, record counts by location/lot/serial, post adjustments. 9 files, ~1,056 procs.
- T7PIA (159 procs): Main PI entry form — freeze/count cycle.
- T7PIC (152 procs): PI count entry variant.
- T7PIF (137 procs): PI freeze/finalize.
- T7PIB / T7PICA (114/97 procs): PI posting (uses BKGLTRAN, BKGLX) — posts count variances to GL.
- T7PID / T7PIE (98/76 procs): PI discrepancy and adjustment entry.
- T7PIG (155 procs): PI report/print.
- T7PIH (68 procs): PI history review.

**New tables:**
- BKPIMSTR — PI master (one record per PI run: start date, status — Open/Posted)
- BKPILOT — PI lot count records (lot#, counted qty, location)
- BKPIPHYS — PI physical count records (item, location, count qty)
- BKPISER — PI serial number count records (serial#, item, found/not-found)
- BKPIFROZ — PI frozen snapshot (inventory snapshot taken at freeze time; baseline for variance calc)
- PIBINLOC — PI bin location records (duplicate of BKICLOC frozen at PI start)
- PIBINLOT — PI bin lot records (duplicate of ISBINLOT frozen at PI start)

---

### Bill of Lading (BO) — T7BOL / T7BOLMSO (3 files)

**Purpose:** Bill of Lading (shipping document) generation for customer shipments. 3 files, ~432 procs.
- T7BOL (178 procs): Main BOL entry — generates shipping document from SO/AR invoice. Uses BKARCUST, BKARINV, BKARINVL, ISAREX, ISACCESS.
- T7BOLMSO (174 procs): BOL from multiple SOs variant. Uses BKPRMSTR (for carrier/truck details?).
- T7BOMSCRAPFIX (80 procs): Utility to fix BOM scrap rates — unrelated name, uses BKBMMSTR only.

---

### Personal Settings (PS) — T7PSF / T7PSA / T7PSK / T7PSE (5 files total)

**Purpose:** Per-user personal settings — printer defaults, menu customization, column preferences. 5 files, ~300 procs.
- T7PSF (63 procs): Main PS form. Uses BKMENUSU (menu user settings), procs include MENULINES, T7TLL, CLEANUP — confirms menu/toolbar personalization.
- T7PSA / T7PSK (90/96 procs): PS admin and setup screens.
- T7PSE (50 procs): Uses BKMENUSU, BKCMACCT — personal settings with CRM account type filtering.

**New tables:** BKMENUSU (menu user settings — saved menu layout per user), BKPSUSER (PS user settings — printer/preference records per user)

---

### Return Merchandise Authorization (RM) — T7RMD / T7RME / T7RMG + 3 others (6 files)

**Purpose:** RMA (Return Merchandise Authorization) processing — customer returns, credit notes, inventory receipt of returned goods. 6 files, ~427 procs.
- T7RMD (216 procs): Main RMA entry — large form. Uses BKARCUST, BKARINV, BKARINVL, BKARINVT, BKARTXN, BKICLOC, BKICLOCM, BKPRSALE.
- T7RMG (132 procs): RMA management/list view.
- T7RME (54 procs): RMA entry sub-form.

**New tables:** ISRMAC (RMA credit note records), ISRMAI (RMA auto-invoice / return invoice records)

---

### Field Order (FO) — T7FOD / T7FOE / T7FOA + 2 others (5 files)

**Purpose:** Field Order (FO) — customer field service/repair orders distinct from standard SOs. Creates service orders with BOM and labor components. 5 files, ~259 procs.
- T7FOD (103 procs): Main FO entry (uses BKBMMSTR, BKICLOCM, CLASMSTR).
- T7FOE (86 procs): FO entry variant.
- T7FOC (60 procs): FO completion/close.

**New tables:**
- ISFOHEAD — FO header (order#, customer, dates, status)
- ISFOLINE — FO line items (product, qty, price)
- ISFOORDL — FO order list (multi-FO management)
- ISFOHIST — FO history records
- ISFOBMRM — FO BOM remark

---

### Data Entry / DC Terminal Stubs (DE) — T7DExx family (64 files)

**Purpose:** Mixed family of two distinct sub-groups:

**Sub-group 1: DC terminal entry stubs** (T7DEBA..DEBE, T7DECA..DECE, T7DEDA..DEDE, etc.)
- 5-proc stub modules: STUB.ONOPENFILES, STUB.ONSTART, STUB.ONDISPLAY, STUB.ONCLOSE, TIMER.CALL
- All open BKDCCFG (DC config) + BKDCLAB + BKGLTRAN + BKGLX
- Pattern: T7DE + [screen-letter][company-letter] — one stub per company per DC screen
- Purpose: per-company/per-station DC terminal entry points calling into ISTECH.LIB

**Sub-group 2: EDI processing modules (T7DEP*)** — Uses BKEDMSTR, BKEDIDUN
- T7DEPB (111 procs): EDI PO processing. Proc names: EVO_CFG, DITSTART, YMSTR, SMSTR
- T7DEPD (132 procs): EDI invoice (uses BKEDNOTE)
- T7DEPE (114 procs): EDI ASN/acknowledgment
- T7DEPF (104 procs): EDI transmit
- T7DEPH (116 procs): EDI PO release (uses BKICPMAT)
- T7DEP860 (82 procs): EDI 850/860 PO transaction
- T7DEM (92 procs): EDI manufacturing sub (uses BKSBVEND, BKDCLAB)

**Sub-group 3: Data entry/detail screens (T7DET, T7DEQ, etc.)**
- T7DET (178 procs): Main detail entry — BKAPCHKF, BKARDEP, BKART → AR deposit/check detail
- T7DEX (82 procs): Export/extract — procs include KEY_FLDS, NI_FLDS, EY_FLDS → data export utility
- T7DEHD (131 procs): PI hand-held entry — BKPIMSTR, BKPILOT, BKPIPHYS, BKPISER
- T7DEER (132 procs): DC labor entry/report — BKDCLAB, BKGLCOA
- T7DEJH (147 procs): GL date/period entry — ISGLDATE

**New tables:** BKDCCFG (DC configuration), BKDCLAB (DC labor records), BKEDMSTR (EDI master), BKEDIDUN (EDI data elements), BKEDNOTE (EDI notes), BKEDPOST (EDI post log)

---

### Module Defaults (MD) — T7MDEFAULTS / T7MDEFNDC / T7MDEFBANKS (3 files)

**Purpose:** System-wide module defaults setup — sets defaults per module for all users. 3 files, ~766 procs.
- T7MDEFAULTS (435 procs, 42 DBs): The main "set all module defaults" form. Touches every major subsystem's config table including ISBANKS (bank master), ISBNMSTR, ISCC (credit card), ISEXUSER (external/web user), ISNUMBER (number sequence definitions), ISSERCNT (serial counter).
- T7MDEFNDC (252 procs, 29 DBs): NDC (non-default company?) variant. Uses BKESTCFG, BKFOCFG, BKSYAP (system AP config), BKCMCNTD, BKCPMSTR.
- T7MDEFBANKS (79 procs): Bank-specific defaults.

**New tables:** ISBANKS (bank account master), ISBNMSTR (bank name master), ISCC (credit card master), ISEXUSER (external/web user access), ISNUMBER (number sequence definitions — auto-increment configs), BKFOCFG (FO config), BKSYAP (system AP configuration)

---

### Universal Lookup Framework (WBKLOOKUP) — 413 procs / 76 DBs

**Purpose:** The F3 lookup framework used by ALL data-entry forms in EVO. When a user presses F3 in any field, this module opens and displays a configurable list from any table. It reads from 76 different tables — essentially every major table in the system.

**Key proc names:** LOSE (.CLOSE), .START, ERS (filters), DATA, .DISP, ANGE (.CHANGE), .ONCLOSE, _VIEW, .CLICK, _DRILL, TING (sorting), LFUNC (lookup function)

**Unique tables in WBKLOOKUP (not in typical modules):**
- FILEDFLD, FILEDICT, FILEKEY, FILEKNUM — file dictionary metadata (used for dynamic field-lookup configuration)
- BKLUGRID — reads user's saved grid layout for this lookup
- ISQSOA — quick search SO access
- ISDRILLM — drill-down definition master
- BKSBPART, BKSBMFG — sub-contractor parts/manufacturing
- BKQCMSTR, BKQCTRAN — QC master/transaction tables accessible via F3

---

### Pass-11 Table Ownership Additions

| Table | Owner module | Also used by |
|-------|-------------|-------------|
| BKSAREPT | T7SAM/T7SAN (SA) | — |
| ISAREX | T7SAM (SA) | T7BOL, T7SRB |
| ISRMAI | T7SAM (SA) | T7SRF, T7RMD |
| BKSBPART | T7JCB (JC) | WBKLOOKUP, T7SMJL |
| BKSBMFG | T7JCH (JC) | T7MRG, T7MRH, WBKLOOKUP |
| BKESTCFG | T7EST/T7ESD (ES) | T7MDEFNDC |
| BKMATCST | T7ESC (ES) | T7ESH, T7ESI |
| BKRFQ | T7ESC (ES) | T7SOA, T7SMJL |
| BKRTCST | T7ESC (ES) | T7ESH |
| ESTSUM | T7ESB/T7ESH (ES) | T7SMJL |
| BKICPMAT | T7ESH (ES) | T7SOA, T7WOA, T7SMJL |
| BKPIMSTR | T7PIA (PI) | T7DEHD |
| BKPILOT | T7PIA (PI) | T7DEHD, T7SMJL |
| BKPIPHYS | T7PIA (PI) | T7DEHD |
| BKPISER | T7PIA (PI) | T7DEHD |
| BKPIFROZ | T7PIF (PI) | T7DEHD, T7PID, T7PIE, T7PIB |
| PIBINLOC | T7PIA (PI) | T7SMJL |
| PIBINLOT | T7PIA (PI) | T7SMJL |
| ISFOHEAD | T7FOD (FO) | WBKLOOKUP |
| ISFOLINE | T7FOD (FO) | WBKLOOKUP, T7SMJL |
| ISFOORDL | T7FOD (FO) | WBKLOOKUP, T7SMJL |
| BKMENUSU | T7PSF (PS) | T7PSE |
| BKPSUSER | T7PSA (PS) | T7ESB, T7JCA, T7MDEFAULTS |
| ISRMAC | T7RMD (RM) | — |
| BKDCCFG | T7DExx stubs (DC) | T7DCPSF, T7DCA |
| BKDCLAB | T7DCA (DC) | T7DEER, T7DEM |
| BKEDMSTR | T7DEPB (ED/DE) | T7DEPD, T7DEPE |
| ISBANKS | T7MDEFAULTS (MD) | T7SRF, WBKLOOKUP |
| ISNUMBER | T7MDEFAULTS (MD) | T7SOA, T7SRD |

---

## Pass 12 — GL sub-modules, SC, PR, misc single-file discoveries

---

### GL Sub-Module Breakdown (22 files, 2,914 total procs)

Confirmed function per GL sub-module from DB fingerprints:

| Module | Procs | Key tables | Inferred function |
|--------|-------|-----------|-------------------|
| T7GLB | 215 | BKGLGJRN, BKGLGJLN, BKGLCHK | GL general journal entry (GL-B) |
| T7GLE | 191 | BKGLTRAN, BKGLCOA | GL entry (direct transaction posting) |
| T7GLF | 189 | BKGLSTMT, BKGLCOA | GL financial statements (GL-F) |
| T7GLN | 182 | BKGLFSTL, BKGLCOA | GL new/maintain budget (GL-N, uses statement layouts) |
| T7GLJ | 171 | BKGLCHK, BKGLTRAN | GL journal review (GL-J) |
| T7GLL | 166 | BKAPCHKF, BKGLCHK, BKGLTRAN | GL check listing / AP check register |
| T7GLO | 165 | BKGLTRAN, BKGLCOA | GL overview / open transactions |
| T7GLESPEED | 164 | BKGLTRAN, BKGLCOA | GL speed/fast entry (abbreviated posting) |
| T7GLE2 | 156 | BKGLTRAN, BKARINVL | GL entry variant 2 (with AR invoice lines) |
| T7GLD | 132 | BKGLTRAN, BKGLCOA | GL department entry (GL-D) |
| T7GLC | 129 | BKGLTRAN, BKGLCOA | GL close (period close function) |
| T7GLT | 120 | BKGLCHK, BKGLTRAN, BKGLCOA | GL trial balance |

**New GL tables:** BKGLSTMT (GL statement templates), BKGLFSTL (GL financial statement layouts — user-defined financial report formats), BKGLGJRN (GL general journal header), BKGLGJLN (GL general journal lines)

---

### SC — Cycle Count / Serial Control (9 files, 741 procs)

**Purpose:** Stock count / cycle count — partial physical inventory by item class, location, or category. Complement to the full PI (Physical Inventory) module. Also handles serial number control per stock location.

- T7SCF (131 procs): Main cycle count entry (BKICLOC, BKICLOCM) — count items in a location
- T7SCC (121 procs): SC with AR transaction link (BKARTXN) — adjustments post to AR
- T7SCH (113 procs): SC history (BKARINV) — count history report
- T7SCA (78 procs): SC adjustments (BKICLOC, BKARINV)
- T7SCB/SCE (59/88 procs): Sub-screens (BKICLOCM)
- T7SCOMP (54 procs): SC company-level variant
- T7SCG (92 procs): SC class/category filter entry

**Tables used:** BKICLOC, BKICLOCM, INVTXN, ISBINLOC, ISCATMST, BKARCUST, CLASMSTR

---

### PR Extended Tables (42 files, 4,297 procs)

Building on existing PR documentation with newly confirmed tables:

| Table | Purpose | Key modules |
|-------|---------|-------------|
| BKPRCURP | PR current period data — YTD and current-period amounts per employee | T7PRB, T7PRD, T7PRG, T7PRK |
| BKPRFTAX | PR federal tax tables — tax rate schedules | T7PRB, T7PRA |
| BKPRGLFL | PR GL flags/accounts — maps each payroll expense type to GL accounts | All PR modules |
| BKPRINFO | PR employee additional info — supplemental fields beyond BKPRMSTR | T7PRB, T7PRA, T7PRD, T7PRLO |
| BKPRTC | PR time card records — individual time card entries | T7PRK (time card entry module) |
| BKPRAGNT | PR agent/agency records — payroll agency links (garnishments, union dues) | T7NZEMAIL |
| BKDCLAB | DC labor records — DC terminal labor entries imported into PR via T7PRK | T7PRK, T7WC, T7DC |

---

### Miscellaneous Single-File Module Discoveries

#### CH — Chain / Multi-Location (T7CHAIN / T7CHAINM)
Chain master module. ISCHAINM = chain/multi-location master records. Allows EVO to manage multiple business locations under one company code, sharing customer/vendor data. Procs: DRILLM.ONSTART, DRILLM.ONCLOSE.

**New table:** ISCHAINM (chain/multi-location master — location codes, names, relationships)

---

#### TC — Treasury Control (T7TCC, 119 procs)
Multi-function treasury control: AP checks (BKAPCHKF), AR deposits (BKARDEP), AR inventory invoices (BKARINVI), AR transactions (BKART), GL check history (BKGLCHK). Likely implements the bank reconciliation and cash management functions.

**New tables:** BKARINVI (AR invoice inventory — links AR invoices to inventory transactions), BKART (AR transaction short-form records — condensed transaction log)

---

#### TE — Test NACHA / ACH (T7TESTNACHA, 103 procs)
ACH (Automated Clearing House / NACHA standard) electronic payment testing module. Uses ISBANKS (bank account master), BKGLCHK (check history) — generates or validates NACHA-format direct deposit files for payroll or AR collections.

---

#### MA — Map Deposits / AR Deposit Application (T7MAPDEPO, 97 procs)
AR deposit mapping: applies customer deposits (BKARDEP) to open invoices (BKARINV, BKARINVL, BKARINVT). This is the "apply cash" function.

---

#### DD — Data Dictionary Check (T7DDCHECK, 92 procs)
Admin utility: FILEDICT, FILEKEY — validates the Btrieve data dictionary (DDF files) for consistency. Checks file/field/key definitions.

---

#### VS — Visual Scheduler (T7VSCHED, 94 procs)
Interactive visual scheduling display. Uses BKARINV, BKARINVL — likely shows upcoming SO delivery dates on a calendar/Gantt view. Procs: TINGS.CLICK, ED.ONSTART, KUP_TLL.

---

#### KI — Kit Assembly (T7KIT, 153 procs)
Kit building / assembly module (KI = Kit). Uses BKICLOC (inventory locations), BKICMSTR, BKPRMSTR (labor). Builds kits from components into a parent item — assembly posting that reduces component quantities and creates parent item stock.

---

#### QS — Quick Search Sales Orders (T7QSOA / T7QSOALINES, 142 procs)
Quick search overlay for Sales Order browsing. T7QSOA: opens BKARCUST, BKARINV, BKARINVL, BKICPMAT, BKPRSALE — customer+SO fast lookup. T7QSOALINES: line-level browse. ISQSOA = saved QS access state.

---

#### NU — Number Definitions (T7NUMDEF, 38 procs)
Manages all auto-increment number sequences. Uses ISNUMBER (number sequence definitions), ISBANKS (bank account numbering), BKESTCFG (estimate numbering), BKSYAP (AP numbering). One record per entity type (SO#, WO#, PO#, invoice#, check#, etc.).

---

#### GD — Grid/Drill Master (T7GDM, 31 procs)
Admin tool: manages drill-down menu definitions (ISDRILLM) and lookup grid layouts (BKLUGRID). The SU-B menu function that configures the drill-down menus.

---

#### DR — Dropdown Menus (T7DROPDOWN / T7DRAG, 53 procs)
User-configurable dropdown list manager. ISDROP = dropdown option master. Allows ERP admins to define custom picklists for configurable fields.

---

#### BI — Bin Setup (T7BINSET, 102 procs)
Bin location setup + counts (BI = Bin). Bridges WC (Warehouse Control) and PI (Physical Inventory): uses BKPIFROZ, BKPILOT, BKPIPHYS, BKPISER alongside BKICLOC, BKICLOCM. Allows counting by bin location as part of physical inventory.

---

#### PA — Paperless DC (T7PAPERLESS, 205 procs)
Paperless manufacturing workflow: uses BKDCLAB, BKGLTRAN, BKGLX — DC labor posted without paper travelers. Large module (205 procs) suggesting full DC paperless form suite.

---

#### EW — External Work Cost? (T7EWC, 68 procs)
Uses BKMATCST, BKRTCST, BKSBMFG, BKICTAX, BKPRSALE. Context: estimating/costing with sub-contract manufacturing. Likely "External Work Cost" calculation linking sub-contracted operations to estimate cost records.

---

### Pass-12 Table Ownership Additions

| Table | Owner module | Also used by |
|-------|-------------|-------------|
| BKGLSTMT | T7GLF (GL) | — |
| BKGLFSTL | T7GLN (GL) | — |
| BKGLGJRN | T7GLB (GL) | T7AME |
| BKGLGJLN | T7GLB (GL) | T7AME |
| BKPRCURP | T7PRB (PR) | T7PRD, T7PRK, T7PRLO |
| BKPRFTAX | T7PRB (PR) | T7PRA |
| BKPRGLFL | T7PRB (PR) | T7PRLI, T7PRA, T7PRK |
| BKPRINFO | T7PRB (PR) | T7PRA, T7PRD |
| BKPRTC | T7PRK (PR) | — |
| BKARINVI | T7TCC (TC) | T7AME |
| BKART | T7TCC (TC) | T7DEQ, T7DET |
| ISCHAINM | T7CHAIN (CH) | T7CHAINM |
| ISDROP | T7DROPDOWN (DR) | — |
| ISCTREVU | T7CTREVU (CR) | — |

---

## Pass 13 — MR (MRP Engine), GE (Generic Tools), infrastructure tables

---

### MR — MRP Planning Engine (17 files, 2,087 procs)

**Critical distinction: BM ≠ MR**
- **BM module** = Bill of Materials *entry and maintenance* (define BOM structure, components, yield)
- **MR module** = MRP *calculation engine* (reads BOMs, calculates supply/demand, generates orders)

The MR family implements the full Material Requirements Planning cycle: demand netting,
BOM explosion, planned order generation, user review, and release.

#### MRP Cycle — module-by-module

| Module | Procs | MRP phase | Key tables |
|--------|-------|-----------|-----------|
| T7MRA | 65 | Item demand view / demand analysis | BKMRPFC, BKICMSTR, MKAHIST |
| T7MRADE | 75 | MRP demand edit (firm change to a planned order) | BKMRPFC, BKICMSTR |
| T7MRB | 117 | MRP by item class — browse planned orders by class | BKSYMSTR, BKMRPFC, BKICMSTR, CLASS |
| T7MRC | 108 | MRP demand from SO lines | BKICMSTR, BKMRPFC, BKARINVL |
| T7MRD | 121 | MRP by inventory location | BKICMSTR, MTICMSTR, BKICLOC, INVTXN |
| T7MRE | 120 | MRP location master view | BKICMSTR, BKICLOCM, MTICMSTR |
| T7MRF | 172 | MRP supply from open PO lines + WO BOM demands | BKMRPFC, BKARINVL, BKAPPOL, WOBOM |
| T7MRG | 188 | MRP calculated order review — browse MTMRP output | MTMRP, MTICMSTR, WORKORD, BKAPPO, BKARINV, BKBMMSTR |
| T7MRH | 193 | MRP planned builds view (with build schedule) | ISBUILD, MTMRP, MTICMSTR, BKAPPO, WORKORD |
| T7MRI | 171 | MRP by item/location — multi-location netting | MTICMSTR, BKICLOCM, MTMRP, ISICMSTR |
| T7MRIX | 130 | MRP WO routing output — routing linkage to planned WOs | WORKORD, WOROUT, ISICMSTR, MTMRP |
| T7MRJ | 206 | MRP planned PO generation — creates BKMRPPO records | MTICMSTR, MTMRP, BKMRPPO, BKAPVEND |
| T7MRJX | 123 | MRP planned PO → actual PO conversion | BKMRPPO, BKAPPO, BKAPPOL, BKSBVEND |
| T7MRK | 5 | LIB stub (entry point per company code) | BKMRPPO, BKAPPO |
| T7MRL | 85 | MRP summary listing / report | BKSYMSTR, MTMRP |
| T7MRN | 95 | MRP build + AP charges integration | ISBUILD, MTMRP, BKAPPO, ISAPCHG |
| T7MRO | 113 | MRP by class — order review filtered by class | ISBUILD, MTMRP, MTICMSTR, CLASMSTR |

**MRP-specific tables (confirmed):**

| Table | Role in MRP |
|-------|------------|
| MTMRP | MRP output — calculated planned order recommendations (buy/make qty, due date) |
| MTICMSTR | MRP shadow item master — a snapshot of BKICMSTR used during the MRP run |
| BKMRPFC | MRP firm changes — user edits/overrides to planned orders (firmed = won't regenerate) |
| BKMRPPO | MRP planned purchase orders — unconfirmed buy recommendations before release |
| ISBUILD | Build schedule — manually entered production targets input to MRP demand |
| ISICMSTR | IS item configuration master — extended item config used in multi-location MRP |

**MRP data flow:**
1. Demand: SO lines (BKARINVL) + ISBUILD targets
2. Supply: on-hand (BKICLOC), open POs (BKAPPOL), open WOs (WORKORD)
3. BOM explosion: BKBMMSTR → nets component demand recursively
4. Output: MTMRP (planned orders), filtered/browsed by T7MRG/H/I/O/B/L
5. User firms changes: T7MRADE → BKMRPFC
6. Release planned POs: T7MRJX → BKMRPPO → BKAPPO (actual PO)
7. Release planned WOs: T7MRIX → WORKORD (actual WO via WO module)

---

### GE — Generic Utilities (5 files)

Small family of generic/shared utility modules:

| Module | Procs | Function | Key tables |
|--------|-------|---------|-----------|
| T7GENAED | 42 | Generic add/edit/delete for service/type tables | ISSTYPE |
| T7GENGET | 10 | Generic get/lookup for service types | ISSTYPE |
| T7GENIMP | 106 | Generic import — schema-aware CSV/data import using DDF | FILELOC, ISSERCNT, FILEKEY, ISFIELDS, FILEDICT |
| T7GETDEP | 18 | Get AR deposit details | BKARDEP, BKARINVT, ISARDEPL, BKARINVL |
| T7GETWEB | 6 | Web deposit retrieval (thin wrapper) | BKARDEP, BKARINVT |

**T7GENIMP** is notable: it uses FILEDICT, FILEKEY, ISFIELDS (the Pervasive DDF schema tables) for dynamic schema-aware import — can import data into any table by reading the schema at runtime.

**New table:** ISARDEPL = AR deposit lines — line-level detail of an AR deposit record, linking deposits to specific invoice payments.

---

### Infrastructure / LIB tables (universal — opened by 900–1,100 modules)

These tables are opened by nearly every module via the shared ISTECH.LIB:

| Table | Count | Purpose |
|-------|-------|---------|
| MKAHIST | 1,076/1,122 | MKA audit history — system-wide change/event log; likely "Make A History" |
| ISLOG | 999/1,122 | IS activity log — user action audit trail |
| BKAPDESC | 993/1,122 | AP description lookup — shared description/memo text table |
| ISIS | 962/1,122 | IS image/icon system — UI icon mapping or general image lookup table |
| BKCMACCN | 954/1,122 | CM account number lookup — shared account code cross-reference |

These should NOT be used as fingerprints for module identification; they appear everywhere.

---

### Pass-13 Table Ownership Additions

| Table | Owner | Also used by |
|-------|-------|-------------|
| MTMRP | T7MRG (MR) | T7MRH, T7MRI, T7MRIX, T7MRJ, T7MRL, T7MRN, T7MRO |
| MTICMSTR | T7MRD (MR) | T7MRE, T7MRF, T7MRG, T7MRH, T7MRI, T7MRIX, T7MRJ, T7MRJX |
| BKMRPFC | T7MRADE (MR) | T7MRA, T7MRB, T7MRC, T7MRF |
| BKMRPPO | T7MRJ (MR) | T7MRJX, T7MRK |
| ISBUILD | T7MRH (MR) | T7MRN, T7MRO |
| ISICMSTR | T7MRI (MR) | T7MRIX |
| ISARDEPL | T7ARN (AR) | T7GETDEP, T7MAPDEPO, T7SOGA |
| MKAHIST | ISTECH.LIB (infra) | 1,076 modules |
| ISLOG | ISTECH.LIB (infra) | 999 modules |
| ISIS | ISTECH.LIB (infra) | 962 modules |
| BKCMACCN | ISTECH.LIB (infra) | 954 modules |
| BKAPDESC | ISTECH.LIB (infra) | 993 modules |

