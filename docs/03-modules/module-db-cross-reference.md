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
