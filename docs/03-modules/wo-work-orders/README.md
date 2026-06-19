# Work Orders (WO)

Status: verified (auto-generated from the extracted schema, menu-code dump, and DFM inventory).

- **Module code**: `WO`
- **Tables**: 30 (prefixes `WO`, `WORK`)
- **UI forms**: 68 (prefixes `T7WO`, `T6WO`, `BKWO`)
- **Menu operations**: 31

## Narrative / vendor help

**→ [help-content.md](help-content.md)** — consolidated write-up of
all 52 help topics from `EvoHELP.CHM` (overview + WO-A through WO-T +
every WO-K-\* and WO-L-\* sub-program, with life-cycle diagram,
status-code table, save-time processing, and cross-links).

## Menu operations

| Code | Operation | Legacy module file(s) |
| ---- | --------- | --------------------- |
| `WO-A` | Enter Work Orders | BKWOA;ISTECH;ISWORPT1 |
| `WO-A-A` | Enter Work Orders - ECO Drawing Entry | BKWOA |
| `WO-B` | Change WO Status | BKWOB;ISWORPT2 |
| `WO-C` | Special Work Order Report | J5SMRPT3 |
| `WO-D` | Print Pick Lists | BKWOD |
| `WO-E` | Print Labor Cards/Labels | BKWOE;T6WOE |
| `WO-F` | Enter Labor | BKWOF |
| `WO-G` | Enter WO BOM | BKWOG;BKWOKB;ISWOG |
| `WO-H` | Enter Misc/Extra Costs | BKWOH |
| `WO-I` | Enter Finished Production | BKWOFA;BKWOI;BKWOIP~1;ISMULTIY;ISTECH |
| `WO-J` | Rebuild Work Orders | BKREBWO;BKWOJ;ISTECH |
| `WO-K-A` | Enter Work Order Routings | BKWOKA |
| `WO-K-B` | Enter WO BOM | BKWOKB |
| `WO-K-C` | Create Multi-Date Work Orders | BKWOKC |
| `WO-K-D` | Create Multi-Assy Work Orders | BKWOKD |
| `WO-K-E` | Swap Substitute Parts | BKWOKE |
| `WO-K-F` | Edit Sequence Started/Finished Dates | BKWOKF |
| `WO-K-G` | Recalculate Projected Hours | BKWOKG |
| `WO-K-L` | Quick Work Orders | NZQWO |
| `WO-L-A` | Print Work Order Status | t6wola |
| `WO-L-C` | Print Work Center Backlog | BKWOLC |
| `WO-L-D` | Print Projected Shipments | BKWOLD |
| `WO-L-E` | Print/Post Labor to Payroll | BKWOLE |
| `WO-L-F` | Print Work Order Shortage | BKWOLF;t6wolf |
| `WO-L-G` | Print Work Center by Key Component | BKWOLG |
| `WO-L-H` | Print Projected Hours Report | BKWOLH |
| `WO-L-I` | Print Allocations | BKWOLI |
| `WO-L-J` | Print Finished Work Order Report | ISWOLJ |
| `WO-M` | Batch Labor Entry | BKDCG;BKDCGMSG;CBKWOM;J5HDWOM |
| `WO-N` | Post Labor Batches | AUTODCH;BKDCH;UMCDCP |
| `WO-Q` | Convert Work Orders to Purchase Orders | CAWOPO;ISWOPO |

## UI forms (68)

| DFM file | Caption | fields | controls | tabs |
| -------- | ------- | -----: | -------: | ---: |
| `T7WOA.DFM` | New Screen | 69 | 171 | 3 |
| `T7WOAC.DFM` | New Screen | 78 | 183 | 0 |
| `T7WOACFG.DFM` | WO-A  Settings | 3 | 9 | 0 |
| `T7WOACPY.DFM` | New Screen | 3 | 13 | 0 |
| `T7WOAE.DFM` | New Screen | 100 | 247 | 4 |
| `T7WOAECO.DFM` |  Eco | 9 | 24 | 0 |
| `T7WOAMDT.DFM` |  | 0 | 8 | 0 |
| `T7WOASOLINES.DFM` |  | 0 | 2 | 0 |
| `T7WOB.DFM` | WO-B | 15 | 46 | 0 |
| `T7WOC.DFM` | WOC | 51 | 93 | 0 |
| `T7WOD.DFM` | WO-D | 28 | 59 | 0 |
| `T7WODATES.DFM` |  | 0 | 1 | 0 |
| `T7WOE.DFM` | IN-E Print Inventory Transactions | 5 | 26 | 0 |
| `T7WOF.DFM` | WO-F | 40 | 98 | 0 |
| `T7WOFA.DFM` | WO-F Backflush Material | 1 | 22 | 0 |
| `T7WOG.DFM` |  | 0 | 1 | 0 |
| `T7WOH.DFM` |  | 0 | 1 | 0 |
| `T7WOI.DFM` |  | 0 | 1 | 0 |
| `T7WOIASK.DFM` | Change Location | 18 | 43 | 0 |
| `T7WOJ.DFM` | WO-J | 11 | 38 | 0 |
| `T7WOJPRESERIALS.DFM` | WO-J Pre-Assigned Serial Numbers | 7 | 25 | 0 |
| `T7WOKA.DFM` | WO-K-A | 35 | 100 | 0 |
| `T7WOKACOPYROUT.DFM` | WO-K-A | 4 | 14 | 0 |
| `T7WOKAOPTS.DFM` | WO-K-A | 3 | 12 | 0 |
| `T7WOKB.DFM` |  | 0 | 1 | 0 |
| `T7WOKC.DFM` | WO-K-C | 4 | 21 | 0 |
| `T7WOKD.DFM` | WO-K-D | 30 | 60 | 0 |
| `T7WOKDQTY.DFM` | Enter Qty to Make | 16 | 34 | 0 |
| `T7WOKE.DFM` |  | 0 | 1 | 0 |
| `T7WOKF.DFM` | New Screen | 5 | 24 | 0 |
| `T7WOKG.DFM` | WO-K-G | 13 | 41 | 0 |
| `T7WOKJ.DFM` | WO-K-J | 11 | 32 | 0 |
| `T7WOKK.DFM` |  | 0 | 1 | 0 |
| `T7WOKL.DFM` |  | 0 | 1 | 0 |
| `T7WOKM.DFM` |  | 0 | 1 | 0 |
| `T7WOKMA.DFM` | New Screen | 3 | 21 | 0 |
| `T7WOKNA.DFM` | Live Work Center Schedule | 4 | 22 | 0 |
| `T7WOKNB.DFM` |  | 0 | 1 | 0 |
| `T7WOKNC.DFM` | Issue Part from Request | 18 | 50 | 0 |
| `T7WOKP.DFM` |  | 0 | 1 | 0 |
| `T7WOKS.DFM` |  | 0 | 1 | 0 |
| `T7WOKSA.DFM` | WO-K-SA | 10 | 33 | 0 |
| `T7WOKT.DFM` | New Screen | 11 | 36 | 0 |
| `T7WOLA.DFM` | WO-L-A | 61 | 116 | 0 |
| `T7WOLB.DFM` | WO-L-B | 48 | 99 | 0 |
| `T7WOLC.DFM` | WO-L-C | 22 | 56 | 0 |
| `T7WOLD.DFM` | WO-L-D | 26 | 65 | 0 |
| `T7WOLE.DFM` | WO-L-E | 7 | 31 | 0 |
| `T7WOLF.DFM` | WO-L-F | 48 | 99 | 0 |
| `T7WOLG.DFM` | WO-L-G | 32 | 65 | 0 |
| `T7WOLH.DFM` | WO-L-H | 15 | 43 | 0 |
| `T7WOLI.DFM` | WO-L-I | 32 | 71 | 0 |
| `T7WOLJ.DFM` | WO-L-J  Print Finished Work Order Report | 19 | 53 | 0 |
| `T7WOLK.DFM` | WO-L-K  Print WO Bill of Material | 23 | 48 | 0 |
| `T7WOLL.DFM` | WO-L-L | 11 | 38 | 0 |
| `T7WOLM.DFM` |  | 0 | 1 | 0 |
| `T7WOLN.DFM` | WO-L-N | 4 | 23 | 0 |
| `T7WOLO.DFM` | WC by Customer | 5 | 24 | 0 |
| `T7WONoteTLL.DFM` | WO Notes | 0 | 17 | 0 |
| `T7WOP.DFM` |  | 0 | 1 | 0 |
| `T7WOPO.DFM` | WO-PO | 13 | 36 | 0 |
| `T7WOPOR.DFM` | WO-PO Review | 8 | 20 | 0 |
| `T7WOS.DFM` |  | 0 | 1 | 0 |
| `T7WOTRWK.DFM` | Rework TO Stock WO | 8 | 30 | 0 |
| `T7woko.DFM` |  | 0 | 1 | 0 |
| `t7wogimp.DFM` | Import Material Issues | 4 | 17 | 0 |
| `t7woprio.DFM` |  | 0 | 1 | 0 |
| `t7woprio2.DFM` |  | 0 | 1 | 0 |

## Database tables (30 + 2 routing templates)

Full field details are in `../../../samples/ddf/schema.md` (see per-table heading).

### Naming convention

EvoERP uses a consistent 3-tier naming pattern across all WO transaction tables:

| Prefix | Tier | Meaning |
|--------|------|---------|
| (none / `WO*`) | Active | Current / live data |
| `WOE*` | Estimated | Pre-posting estimated values or edited-but-not-posted |
| `WOH*` | History | Archived / closed WO data |

Routing tables follow a similar pattern: `WOROUT` (active), `WOHROUT` (history), `WOROUTMP` (temporary/scheduling working copy), `WOSROUT` (scheduled routing).

### Functional cross-reference (all 30 WO tables)

| Group | Table | F | Purpose | PK fields |
|-------|-------|---|---------|-----------|
| **WO Master** | `WORKORD` | 74 | Active WO header — qty, dates, status, 7-category E/A costs, instructions | WOPRE+WOSUF |
| | `WORKHORD` | 74 | History/closed WO master — identical schema to WORKORD | WOPRE+WOSUF |
| | `WORKSORD` | 74 | Scheduled WO master — identical schema, used by MRP scheduling | WOPRE+WOSUF |
| **BOM** | `WOBOM` | 24 | Active WO BOM — component list with QTYPER, scrap, qty issued, E/A material cost | OPER+WOPRE+WOSUF+COMPCODE |
| | `WOHBOM` | 24 | History BOM — identical schema to WOBOM | OPER+WOPRE+WOSUF+COMPCODE |
| | `WOBOMCHG` | 17 | BOM change audit log — A/B pairs for comp add/delete, qty, reference, scrap | WOPRE+WOSUF+PARENT+COMP+UID |
| | `WOBOMHRM` | 7 | BOM remark lines — per-component text remarks | WOPRE+WOSUF+PARENT+LINE+COMP |
| | `WOBOMREM` | 7 | BOM remark archive — identical schema to WOBOMHRM | WOPRE+WOSUF+PARENT+LINE+COMP |
| **Routing** | `WOROUT` | 81 | Active WO routing — per-operation with WC, vendor, E/A costs (setup/labor/machine/OH), 15×60-char instructions, scheduling fields | WOPRE+WOSUF+OPER |
| | `WOHROUT` | 81 | History routing — identical schema to WOROUT | WOPRE+WOSUF+OPER |
| | `WOROUTMP` | 81 | Routing temp/working copy — used during scheduling or MRP recalculation | WOPRE+WOSUF+OPER |
| | `WOSROUT` | 81 | Scheduled routing — identical schema, holds MRP-committed schedule | WOPRE+WOSUF+OPER |
| | `WOROCHG` | 24 | Routing change audit — A/B pairs for long-time, setup, machine, tool, WC, standard-date, num-persons | WOPRE+WOSUF+PART+OPER |
| **Labor** | `WOLABOR` | 58 | Active labor transactions — emp+date+oper, run/setup hrs, parts, scrap, QC, machine, tool, WC, cycle-time | POSTED+DATE+EMP+WOPRE+WOSUF+OPER+TRXN |
| | `WOELABOR` | 58 | Estimated/edited labor — identical schema to WOLABOR | same |
| | `WOHLABOR` | 58 | History labor — identical schema | same |
| | `WOLABRPT` | 58 | Labor report staging — identical schema, used for payroll/report generation | same |
| **Material** | `WOMAT` | 17 | Active material issues — qty issued, scrap, lot, serial, prod code, cost | DATE+WOPRE+WOSUF |
| | `WOEMAT` | 17 | Estimated material — identical schema to WOMAT | same |
| | `WOHMAT` | 17 | History material — identical schema | same |
| **Receipts** | `WORECV` | 11 | WO completion receipts to stock — assy, qty, avg cost, lot, serial | WOPRE+WOSUF+DATE |
| | `WOERECV` | 11 | Estimated/edited receipts — identical schema to WORECV | same |
| | `WOHRECV` | 11 | History receipts — identical schema | same |
| **Scheduling** | `WODATE` | 13 | WO date windows — start/finish dates, qty, parent/top/delivery WO refs (hierarchy for multi-level MRP) | WOPRE+WOSUF |
| | `WOHDATE` | 13 | History date windows — identical schema to WODATE | WOPRE+WOSUF |
| **Extra charges** | `WOEXCHG` | 10 | WO extra charge transactions — misc adjustments with GL acct, charge desc, operation | WOPRE+WOSUF+DATE |
| | `WOHEXCHG` | 10 | History extra charges — identical schema | WOPRE+WOSUF+DATE |
| **Change audit** | `WORKACHG` | 25 | WO assembly change log — A/B pairs for priority, status, class, description, qty, start/finish/due dates | WOPRE+WOSUF+CODE+CDATE |
| | `WORKCHG` | 25 | WO change log (duplicate schema to WORKACHG — likely split by change type) | same |
| **Work Centers** | `WORKCTR` | 47 | Work center master — WC code, dept, hours/week, labor/machine/OH rates, queue times, cycle times, parent-child hierarchy | MTWC_WC |

### Related routing template tables (not WO-prefixed)

| Table | F | Purpose |
|-------|---|---------|
| `ROUTING` | 62 | Standard routing template per part+operation — defines WC, times, costs before WO creation; 15×60 instruction lines |
| `ROUTTEMP` | 62 | Routing template working copy — identical schema to ROUTING; used during routing edits or MRP explosion |

### Raw DDF table list

| Table | File on disk | Fields | Key fields (first 3) |
| ----- | ------------ | -----: | -------------------- |
| **WOBOM** | `WOBOM.B` | 24 | `WOBOM_OPER`, `WOBOM_WOPRE`, `WOBOM_WOSUF` |
| **WOBOMCHG** | `WOBOMCHG.B` | 17 | `WBOM_CHG_WOPRE`, `WBOM_CHG_WOSUF`, `WBOM_CHG_PARENT` |
| **WOBOMHRM** | `WOBOMHRM.B` | 7 | `WOBOM_RM_WOPRE`, `WOBOM_RM_WOSUF`, `WOBOM_RM_PARENT` |
| **WOBOMREM** | `WOBOMREM.B` | 7 | `WOBOM_RM_WOPRE`, `WOBOM_RM_WOSUF`, `WOBOM_RM_PARENT` |
| **WODATE** | `WODATE.B` | 13 | `WODATE_WOPRE`, `WODATE_WOSUF`, `WODATE_START` |
| **WOELABOR** | `WOELABOR.B` | 58 | `MTWOLA_POSTED`, `MTWOLA_DATE`, `MTWOLA_EMP` |
| **WOEMAT** | `WOEMAT.B` | 17 | `WOMAT_DATE`, `WOMAT_WOPRE`, `WOMAT_WOSUF` |
| **WOERECV** | `WOERECV.B` | 11 | `MTWOR_WOPRE`, `MTWOR_WOSUF`, `MTWOR_DATE` |
| **WOEXCHG** | `WOEXCHG.B` | 10 | `MTWO_EX_WOPRE`, `MTWO_EX_WOSUF`, `MTWO_EX_DATE` |
| **WOHBOM** | `WOHBOM.B` | 24 | `WOBOM_OPER`, `WOBOM_WOPRE`, `WOBOM_WOSUF` |
| **WOHDATE** | `WOHDATE.B` | 13 | `WODATE_WOPRE`, `WODATE_WOSUF`, `WODATE_START` |
| **WOHEXCHG** | `WOHEXCHG.B` | 10 | `MTWO_EX_WOPRE`, `MTWO_EX_WOSUF`, `MTWO_EX_DATE` |
| **WOHLABOR** | `WOHLABOR.B` | 58 | `MTWOLA_POSTED`, `MTWOLA_DATE`, `MTWOLA_EMP` |
| **WOHMAT** | `WOHMAT.B` | 17 | `WOMAT_DATE`, `WOMAT_WOPRE`, `WOMAT_WOSUF` |
| **WOHRECV** | `WOHRECV.B` | 11 | `MTWOR_WOPRE`, `MTWOR_WOSUF`, `MTWOR_DATE` |
| **WOHROUT** | `WOHROUT.B` | 81 | `MTWORO_WOPRE`, `MTWORO_WOSUF`, `MTWORO_OPER` |
| **WOLABOR** | `WOLABOR.B` | 58 | `MTWOLA_POSTED`, `MTWOLA_DATE`, `MTWOLA_EMP` |
| **WOLABRPT** | `WOLABRPT.B` | 58 | `MTWOLA_POSTED`, `MTWOLA_DATE`, `MTWOLA_EMP` |
| **WOMAT** | `WOMAT.B` | 17 | `WOMAT_DATE`, `WOMAT_WOPRE`, `WOMAT_WOSUF` |
| **WORECV** | `WORECV.B` | 11 | `MTWOR_WOPRE`, `MTWOR_WOSUF`, `MTWOR_DATE` |
| **WORKACHG** | `WORKACHG.B` | 25 | `WO_CHG_WOPRE`, `WO_CHG_WOSUF`, `WO_CHG_CODE` |
| **WORKCHG** | `WORKCHG.B` | 25 | `WO_CHG_WOPRE`, `WO_CHG_WOSUF`, `WO_CHG_CODE` |
| **WORKCTR** | `WORKCTR.B` | 47 | `MTWC_WC`, `MTWC_WCDESC`, `MTWC_DEPT` |
| **WORKHORD** | `WORKHORD.B` | 74 | `MTWO_WIP_WOPRE`, `MTWO_WIP_WOSUF`, `MTWO_WIP_BLANK` |
| **WORKORD** | `WORKORD.B` | 74 | `MTWO_WIP_WOPRE`, `MTWO_WIP_WOSUF`, `MTWO_WIP_BLANK` |
| **WORKSORD** | `WORKSORD.B` | 74 | `MTWO_WIP_WOPRE`, `MTWO_WIP_WOSUF`, `MTWO_WIP_BLANK` |
| **WOROCHG** | `WOROCHG.B` | 24 | `WORO_CHG_WOPRE`, `WORO_CHG_WOSUF`, `WORO_CHG_PART` |
| **WOROUT** | `WOROUT.B` | 81 | `MTWORO_WOPRE`, `MTWORO_WOSUF`, `MTWORO_OPER` |
| **WOROUTMP** | `WOROUTMP.B` | 81 | `MTWORO_WOPRE`, `MTWORO_WOSUF`, `MTWORO_OPER` |
| **WOSROUT** | `WOSROUT.B` | 81 | `MTWORO_WOPRE`, `MTWORO_WOSUF`, `MTWORO_OPER` |

## WORKORD — Work Order Master (74 fields, confirmed from DDF, Pass 110e 2026-06-19)

Primary key: `MTWO_WIP_WOPRE` (FLOAT 8) + `MTWO_WIP_WOSUF` (UBINARY 2)

Note: The WO prefix is stored as a FLOAT (not a string). This is a TAS Pro convention — WO numbers are numeric sequences stored as floats for sort performance.

| # | Field | Type | Size | Meaning |
|---|-------|------|------|---------|
| 1 | `MTWO_WIP_WOPRE` | FLOAT | 8 | WO prefix / number (PK part 1) |
| 2 | `MTWO_WIP_WOSUF` | UBINARY | 2 | WO suffix (PK part 2; 0 = main WO, 1+ = sub-WOs) |
| 3 | `MTWO_WIP_BLANK` | STRING | 1 | Blank / spacer flag |
| 4 | `MTWO_WIP_MULT` | STRING | 1 | Multiple-issue flag |
| 5 | `MTWO_WIP_SQTY` | FLOAT | 8 | Scheduled quantity to produce |
| 6 | `MTWO_WIP_PRTY` | STRING | 1 | Priority code (1=high … 9=low) |
| 7 | `MTWO_WIP_SSTART` | DATE | 4 | Scheduled start date |
| 8 | `MTWO_WIP_SFIN` | DATE | 4 | Scheduled finish date |
| 9 | `MTWO_WIP_ASTART` | DATE | 4 | Actual start date |
| 10 | `MTWO_WIP_AFIN` | DATE | 4 | Actual finish date |
| 11 | `MTWO_WIP_COMQTY` | FLOAT | 8 | Completed quantity |
| 12 | `MTWO_WIP_STATUS` | STRING | 1 | Status: R=Released, C=Closed, H=Hold, I=In-Process, X=Cancelled |
| 13 | `MTWO_WIP_LOCK` | STRING | 1 | Edit lock flag |
| 14 | `MTWO_WIP_ESETUP` | FLOAT | 8 | Estimated setup cost |
| 15 | `MTWO_WIP_EMAT` | FLOAT | 8 | Estimated material cost |
| 16 | `MTWO_WIP_EOUTPR` | FLOAT | 8 | Estimated outside processing cost |
| 17 | `MTWO_WIP_ELABOR` | FLOAT | 8 | Estimated labor cost |
| 18 | `MTWO_WIP_ASETUP` | FLOAT | 8 | Actual setup cost |
| 19 | `MTWO_WIP_AMAT` | FLOAT | 8 | Actual material cost |
| 20 | `MTWO_WIP_AOUTPR` | FLOAT | 8 | Actual outside processing cost |
| 21 | `MTWO_WIP_ALABOR` | FLOAT | 8 | Actual labor cost |
| 22 | `MTWO_WIP_ETOT` | FLOAT | 8 | Estimated total cost |
| 23 | `MTWO_WIP_ATOTAL` | FLOAT | 8 | Actual total cost |
| 24 | `MTWO_WIP_EST` | FLOAT | 8 | Estimate number (FK → Estimating module) |
| 25 | `MTWO_WIP_CODE` | STRING | 15 | Item / part code being produced |
| 26 | `MTWO_WIP_SONUM` | FLOAT | 8 | Linked SO number |
| 27 | `MTWO_WIP_SETUPV` | FLOAT | 8 | Setup cost variance (est − actual) |
| 28 | `MTWO_WIP_MATV` | FLOAT | 8 | Material cost variance |
| 29 | `MTWO_WIP_OUTPRV` | FLOAT | 8 | Outside processing cost variance |
| 30 | `MTWO_WIP_LABORV` | FLOAT | 8 | Labor cost variance |
| *(gap)* | *(unregistered 32 bytes)* | — | — | 4 unregistered fields (offset 190–221) |
| 31 | `MTWO_WIP_CUSORD` | STRING | 25 | Customer PO / order reference |
| 32 | `MTWO_CUSTCODE` | STRING | 10 | Customer code |
| 33 | `MTWO_CUSTNAME` | STRING | 25 | Customer name (denormalized) |
| 34 | `MTWO_WIP_DESC` | STRING | 30 | WO description |
| 35 | `MTWO_WIP_PPRCE` | FLOAT | 8 | Sell price per unit |
| 36 | `MTWO_WIP_TOTV` | FLOAT | 8 | Total cost variance |
| 37–46 | `MTWO_WIP_INSTR_1..10` | STRING | 60 | Work instructions (10 × 60 char = 600 chars) |
| 47 | `MTWO_WIP_SCONV` | STRING | 1 | Schedule conversion flag |
| 48 | `MTWO_WIP_QCONV` | STRING | 1 | Quantity conversion flag |
| 49 | `MTWO_WIP_DDATE` | DATE | 4 | Customer due date |
| 50 | `MTWO_WIP_VOVHD` | FLOAT | 8 | Estimated variable overhead |
| 51 | `MTWO_WIP_AVOVHD` | FLOAT | 8 | Actual variable overhead |
| 52 | `MTWO_WIP_VOVHDV` | FLOAT | 8 | Variable overhead variance |
| 53 | `MTWO_WIP_EFOVHD` | FLOAT | 8 | Estimated fixed overhead |
| 54 | `MTWO_WIP_AFOVHD` | FLOAT | 8 | Actual fixed overhead |
| 55 | `MTWO_WIP_FOVHDV` | FLOAT | 8 | Fixed overhead variance |
| 56 | `MTWO_WIP_USERCD` | STRING | 1 | User-defined code |
| 57 | `MTWO_WIP_PROJ` | STRING | 15 | Project code (Job Cost integration) |
| 58 | `MTWO_WIP_LOC` | STRING | 10 | Production location |
| 59 | `MTWO_WIP_CONTAT` | STRING | 25 | Customer contact name |
| 60 | `MTWO_WIP_CHGORD` | UBINARY | 2 | Change order counter |
| 61 | `MTWO_WIP_EOTH` | FLOAT | 8 | Estimated other cost |
| 62 | `MTWO_WIP_AOTH` | FLOAT | 8 | Actual other cost |
| 63 | `MTWO_WIP_OTHV` | FLOAT | 8 | Other cost variance |
| 64 | `MTWO_WIP_OTHPER` | FLOAT | 8 | Other cost percentage |
| 65 | `MTWO_WIP_EMISC` | FLOAT | 8 | Estimated miscellaneous cost |
| 66 | `MTWO_WIP_AMISC` | FLOAT | 8 | Actual miscellaneous cost |
| 67 | `MTWO_WIP_MISCV` | FLOAT | 8 | Misc cost variance |
| 68 | `MTWO_WIP_EEXTRA` | FLOAT | 8 | Estimated extra cost |
| 69 | `MTWO_WIP_AEXTRA` | FLOAT | 8 | Actual extra cost |
| 70 | `MTWO_WIP_EXTRAV` | FLOAT | 8 | Extra cost variance |
| 71 | `MTWO_WIP_SCHED_1` | STRING | 1 | Schedule flag 1 |
| 72 | `MTWO_WIP_SCHED_2` | STRING | 1 | Schedule flag 2 |
| 73 | `MTWO_WIP_SOLINE` | FLOAT | 8 | SO line number |
| 74 | `MTWO_WIP_SCRAP` | FLOAT | 8 | Scrap quantity |

**Cost structure summary:** WO tracks 7 cost categories: Setup, Material, Outside Processing, Labor, Variable Overhead, Fixed Overhead, Other, Misc, Extra — each with Estimated, Actual, and Variance. Total = ATOTAL. Variance = ETOT − ATOTAL.

## WORKCTR — Work Center Master (47 fields, confirmed from DDF, Pass 110e 2026-06-19)

Primary key: `MTWC_WC` (12)

| Field(s) | Type | Size | Meaning |
|----------|------|------|---------|
| `MTWC_WC` | STRING | 12 | Work center code (PK) |
| `MTWC_WCDESC` | STRING | 30 | Work center description |
| `MTWC_DEPT` | STRING | 4 | Department code |
| `MTWC_DEPTDESC` | STRING | 30 | Department description (denormalized) |
| `MTWC_HRSWEEK` | UBINARY | 2 | Available hours per week |
| `MTWC_SETUP` | FLOAT | 8 | Standard setup rate ($/hr) |
| `MTWC_LABOR` | FLOAT | 8 | Standard labor rate ($/hr) |
| `MTWC_MACHINE` | FLOAT | 8 | Standard machine rate ($/hr) |
| `MTWC_AVGQTIME` | UBINARY | 2 | Average queue time (days) |
| `MTWC_QPR1/2/3` | UBINARY×3 | 2 | Queue priority thresholds 1–3 |
| `MTWC_VOVHD` | FLOAT | 8 | Variable overhead rate ($/hr) |
| `MTWC_FOVHD` | FLOAT | 8 | Fixed overhead rate ($/hr) |
| `MTWC_LEAD` | UBINARY | 2 | Lead time (days) |
| `MTWC_OUTPROC` | STRING | 1 | Outside processing flag (Y=vendor operation) |
| `MTWC_EST_VOVHD` | FLOAT | 8 | Estimated variable overhead rate |
| `MTWC_HRS_SHIFT` | UBINARY | 2 | Hours per shift |
| `MTWC_MIN_CHG` | FLOAT | 8 | Minimum charge per operation |
| `MTWC_COST_LB` | FLOAT | 8 | Cost per lb (for weight-based billing) |
| `MTWC_EXTRA` | STRING | 100 | User-defined extra field |
| `MTWC_PARENT_YN` | STRING | 1 | Is parent work center flag |
| `MTWC_PARENT_WC` | STRING | 12 | Parent work center code (group hierarchy) |
| `MTWC_LEVEL_YN` | STRING | 1 | Level flag |
| `MTWC_CYCLE_TIME_1..10` | UBINARY×10 | 2 | Cycle time per shift (10 shifts) |
| `MTWC_GDATE_1/2` | DATE×2 | 4 | Generic date fields 1–2 |
| `MTWC_FLAGS_1..5` | STRING×5 | 1 | User-defined flags 1–5 |
| `MTWC_GNUM` | FLOAT | 8 | Generic number field |
| `MTWC_ALPHA_1..5` | STRING×5 | 30 | User-defined alpha fields 1–5 |

**Design notes:** Parent-child WC hierarchy (PARENT_WC) allows grouping multiple WCs under a department head. CYCLE_TIME_1..10 holds per-shift capacity in minutes. OUTPROC=Y means this WC is an outside vendor operation; the routing will reference a vendor (MTRO_VENDCODE in ROUTING).

## ROUTING — Part Routing Template (62 fields, confirmed from DDF, Pass 110e 2026-06-19)

Primary key: `MTRO_CODE` (15) + `MTRO_OPER` (UBINARY 2)

This is the *standard routing library*, not a WO-specific routing. When a WO is created, the routing is copied from ROUTING → WOROUT. ROUTING records are defined at the part level; WOROUT records are copies per WO instance.

| Field(s) | Type | Size | Meaning |
|----------|------|------|---------|
| `MTRO_CODE` | STRING | 15 | Part/item code (PK part 1) |
| `MTRO_OPER` | UBINARY | 2 | Operation sequence number (PK part 2) |
| `MTRO_DESC` | STRING | 30 | Part description (denormalized) |
| `MTRO_OPERDESC` | STRING | 30 | Operation description |
| `MTRO_TYPE` | STRING | 1 | Operation type (L=Labor, M=Machine, O=Outside) |
| `MTRO_LEAD` | UBINARY | 2 | Operation lead time (days) |
| `MTRO_VENDCOST` | FLOAT | 8 | Outside vendor cost per unit |
| `MTRO_PARTSHR` | FLOAT | 8 | Parts per hour |
| `MTRO_TIMEPART` | TIME | 4 | Time per part (TIME field) |
| `MTRO_SETUPHRS` | TIME | 4 | Setup hours |
| `MTRO_LOTSIZE` | FLOAT | 8 | Standard lot size |
| `MTRO_INSTR_1..15` | STRING×15 | 60 | Work instructions (15 × 60 char = 900 chars) |
| `MTRO_WC` | STRING | 12 | Work center code |
| `MTRO_WCDESC` | STRING | 30 | Work center description (denormalized) |
| `MTRO_VENDCODE` | STRING | 10 | Outside vendor code |
| `MTRO_VENDNAME` | STRING | 25 | Outside vendor name (denormalized) |
| `MTRO_LABOR` | FLOAT | 8 | Labor rate ($/hr) |
| `MTRO_MACHINE` | FLOAT | 8 | Machine rate ($/hr) |
| `MTRO_FOVHD` | FLOAT | 8 | Fixed overhead rate |
| `MTRO_VOVHD` | FLOAT | 8 | Variable overhead rate |
| `MTRO_SETUP` | FLOAT | 8 | Setup rate ($/hr) |
| `MTRO_TMACHINE` | STRING | 4 | Machine code |
| `MTRO_TMACHDESC` | STRING | 30 | Machine description |
| `MTRO_TOOL` | STRING | 15 | Tool code |
| `MTRO_TOOLDESC` | STRING | 30 | Tool description |
| `MTRO_NUM` | UBINARY | 2 | Number of machines |
| `MTRO_NUM_PERSON` | FLOAT | 8 | Number of persons |
| `MTWO_MISC_COST` | FLOAT | 8 | Misc cost per operation |
| `MTWO_MISC_DESC` | STRING | 30 | Misc cost description |
| `MTRO_MISC_ACOST` | FLOAT | 8 | Actual misc cost |
| `MTRO_OP_TEMP_NO` | UBINARY | 2 | Operation template number |
| `MTRO_NUM_PROCES` | UBINARY | 2 | Number of processes |
| `MTRO_TIME_PERPR` | TIME | 4 | Time per process |
| `MTRO_MD_PROC_HR` | STRING | 1 | Mode: processes per hour vs time per process |
| `MTRO_PROC_PERHR` | FLOAT | 8 | Processes per hour |
| `MTRO_STD_TIME` | STRING | 1 | Standard time mode flag |
| `MTRO_MIN_CHG` | FLOAT | 8 | Minimum charge |
| `MTRO_OVERLAP` | UBINARY | 2 | Overlap with next operation (%) |
| `MTRO_PIECE_RATE` | FLOAT | 8 | Piece rate ($/piece) |
| `MTRO_LONGTIME` | FLOAT | 8 | Long run time (hours, high precision) |
| `MTRO_PRINT` | STRING | 1 | Print flag |
| `MTRO_CLASS` | STRING | 15 | Operation class code |
| `MTRO_EXTRA` | STRING | 150 | User-defined extra field |
| `MTRO_NEGOVLP` | FLOAT | 8 | Negative overlap (queue time before this op) |
| `MTRO_DEF_TIME` | TIME | 4 | Default time |
| `MTRO_R_TYPE` | STRING | 10 | Routing type code |
| `MTRO_EST_LINE` | FLOAT | 8 | Estimate line number (FK → Estimating) |
| `MTRO_EST_TAG` | STRING | 10 | Estimate tag |

**Design notes:** ROUTTEMP has identical schema — used as a scratch copy during routing edits. The WO routing (WOROUT) is a copy of ROUTING stamped at WO creation time; subsequent changes to ROUTING do not retroactively affect open WOs.

## Notes & open questions

- WORKACHG vs WORKCHG: both have identical 25-field schema with WO_CHG_ prefix. Likely split between assembly-level changes (WORKACHG) and general WO header changes (WORKCHG), but the actual split criterion is not confirmed from schema alone — would need RWN source to verify.
- WORKSORD: identical 74-field schema to WORKORD. Likely MRP-generated "scheduled" WO proposals that haven't been formally released; confirmed from the module name pattern but not from RWN logic.
- WOELABOR: identical schema to WOLABOR. The "E" prefix here likely means "entered but not posted" (pending labor) rather than "estimated."
