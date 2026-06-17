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
