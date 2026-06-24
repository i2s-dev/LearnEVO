# PA — Paperless DC / Shop Floor Control

Status: verified | Pass 233

EvoERP module code: **PA**

Programs:
- `T7Paperless.RWN` — main shop floor control (205 procs, src=LISTG60.LIB, 50 DB tables)
- `T7PACKMENU.RWN` — reindex utility (5 procs, src=t7packmenu.SRC, 0 direct tables)
- `T7PASS.RWN` — password authentication sub (3 procs, src=t7pass.SRC, 45 tables)

PA is the touchscreen-optimized shop-floor data collection system. Operators scan WO barcodes,
log labor time (start/finish), report quantities (completed/scrapped), receive outside-process
POs, and view routing operations and instructions in real time.

LISTG60.LIB = touchscreen-optimized grid/list UI framework.

---

## Database tables (T7Paperless — 50 tables)

| Table | Purpose |
|-------|---------|
| WORKORD | WO header |
| MTICMSTR | Estimating inventory master |
| BKICMSTR | Production inventory master |
| WOROUT | WO routing operations |
| ROUTING | Standard routing templates |
| BKICLOC | Inventory by location |
| ISBINLOC | Bin-level inventory (no lot) |
| ISWOEX | WO extension UDFs |
| WORECV | WO finished goods receipts |
| BKAPPOL | AP PO line (outside process receiving) |
| ISWOTRAY | WO tray/container tracking |
| BKDCLAB | DC labor entries |
| BKARCUST | AR customer master |
| BKAPVEND | AP vendor master |
| BKYSMSTR | System master |
| WOBOM | WO BOM (planned components) |
| WOMAT | WO material issues |
| INVTXN | Inventory transactions |
| CLASS | Item class codes |
| LOT | Lot master |
| ISBINLOT | Bin + lot inventory |
| SERIAL | Serial master |
| BKAPPO | AP PO header |
| WODATE | WO scheduled dates |
| BKSYHELP | System help |
| DBAHLPID | Help ID map |
| TASCOLOR | Color configuration |
| ISIS | Global settings |
| BKPSUSER | Password security users |
| ISLOG | Event log |
| ISDRILL | Drill-down menu config |
| BKCMACCN | CM account codes |
| ISLINKS | Document links |
| BKAPDESC | AP descriptions |
| BKSYMSTR | Symbol master |
| ISACCESS | Security access control |
| LANGDICT | Language dictionary |
| ISNOTES | Notes |
| ISNTYPE | Note type codes |
| ISICMSTR | Estimating inventory master |
| BKARINV | AR invoice header |
| BKGLTRAN | GL transactions |
| BKARINVL | AR invoice lines |
| BKBMMSTR | BOM master |
| BKGLX | GL extended |
| MKAHIST | Session history |
| DBAFIFO | FIFO cost |
| ISTRIGRS | Email notification triggers |
| ISREMIND | Reminders |
| ISNCR | Nonconformance records |

T7PASS opens the same 45 tables (minus ISWOEX, WORECV, ISICMSTR, ISACCESS, ISNCR) for the
password authentication session init.

---

## MTWO.WIP.* namespace — WORKORD header (76 vars total)

The complete WORKORD access namespace confirmed from T7Paperless var extraction:

### Basic WO identity and scheduling
| Var | Meaning |
|-----|---------|
| MTWO.WIP.WOPRE | WO prefix |
| MTWO.WIP.WOSUF | WO suffix |
| MTWO.WIP.BLANK | Blank/clear flag |
| MTWO.WIP.MULT | Multiple WO mode flag |
| MTWO.WIP.SQTY | Scheduled quantity |
| MTWO.WIP.PRTY | Priority |
| MTWO.WIP.SSTART | Scheduled start |
| MTWO.WIP.SFIN | Scheduled finish |
| MTWO.WIP.ASTART | Actual start |
| MTWO.WIP.AFIN | Actual finish |
| MTWO.WIP.COMQTY | Completed quantity |
| MTWO.WIP.STATUS | WO status |
| MTWO.WIP.LOCK | Concurrent-entry lock |
| MTWO.WIP.CODE | WO type/class code |
| MTWO.WIP.SONUM | Linked SO number |
| MTWO.WIP.CUSORD | Customer order number |
| MTWO.WIP.DDATE | Due date |
| MTWO.WIP.SCHED | Schedule flag |
| MTWO.WIP.SOLINE | Linked SO line number |
| MTWO.WIP.SCRAP | Scrap quantity |
| MTWO.WIP.SCONV | Standard conversion factor |
| MTWO.WIP.QCONV | Quantity conversion factor |
| MTWO.WIP.INSTR | Work instructions |
| MTWO.WIP.DESC | Item description |
| MTWO.WIP.PPRCE | Price |
| MTWO.WIP.USERCD | User code |
| MTWO.WIP.PROJ | Project code |
| MTWO.WIP.LOC | Location |
| MTWO.WIP.CONTAT | Contact at customer |
| MTWO.WIP.CHGORD | Change order number |
| MTWO.WIP.EST | Estimate flag |

### Cost breakdown — Estimated / Actual / Variance / %
| Cost category | E (est) | A (actual) | V (variance) | % |
|---------------|---------|-----------|-------------|---|
| Setup | ESETUP | ASETUP | SETUPV | SETUP% |
| Material | EMAT | AMAT | MATV | MAT% |
| Outside-process | EOUTPR | AOUTPR | OUTPRV | OUTPR% |
| Labor | ELABOR | ALABOR | LABORV | LABOR% |
| Variable overhead | VOVHD | AVOVHD | VOVHDV | VOVHD% |
| Fixed overhead | EFOVHD | AFOVHD | FOVHDV | FOVHD% |
| Other | EOTH | AOTH | OTHV | OTHPER |
| Misc | EMISC | AMISC | MISCV | MISC% |
| Extra | EEXTRA | AEXTRA | EXTRAV | EXTRA% |
| Total | ETOT | ATOTAL | TOTV | TOT% |

### Additional MTWO.* vars (non-WIP prefix)
| Var | Meaning |
|-----|---------|
| MTWO.CUSTCODE | Customer code |
| MTWO.CUSTNAME | Customer name |
| MTWO.MISC.COST | Misc cost amount |
| MTWO.MISC.DESC | Misc cost description |
| MTWO.PRODCODE | Finished goods item code |

---

## MTWORO.* namespace — WOROUT WO routing operations (44 vars)

Per-operation routing detail for the active WO (WOROUT table access):

| Var | Meaning |
|-----|---------|
| MTWORO.WOPRE/WOSUF | WO identity |
| MTWORO.OPER | Operation number |
| MTWORO.PROJ | Project code |
| MTWORO.START/FINISH | Scheduled start/finish |
| MTWORO.CODE | Routing step code |
| MTWORO.OPER2 | Secondary operation reference |
| MTWORO.%COMP | Percent complete |
| MTWORO.ESTHRS/ACTHRS | Estimated/actual run hours |
| MTWORO.ESETHRS/ASETHRS | Estimated/actual setup hours |
| MTWORO.ESSTHRS | Estimated setup standard hours |
| MTWORO.OPERDESC | Operation description |
| MTWORO.VEND/VENDNAME | Outside-process vendor |
| MTWORO.MACHNO | Machine number |
| MTWORO.TOOL | Tool number |
| MTWORO.PARTSHR | Part-share flag (shared operation) |
| MTWORO.TIMEPART | Time partition factor |
| MTWORO.WC/WCDESC | Work center code/description |
| MTWORO.PRIORITY | Operation priority |
| MTWORO.FINISH2 | Actual finish (alternate) |
| MTWORO.DEPT | Department |
| MTWORO.TYPE | Routing step type |
| MTWORO.INSTR | Step instructions |
| MTWORO.QTYCOM | Quantity completed at this step |
| MTWORO.SCRAPPED | Quantity scrapped at this step |
| MTWORO.STQTY | Standard quantity |
| MTWORO.PO | Outside-process PO number |
| MTWORO.LEAD | Lead time |
| MTWORO.SQTY | Scheduled quantity |
| MTWORO.DESC | Item description |
| MTWORO.STARTED/FINISHED | Status flags |
| MTWORO.CONTNTN | Contention flag |
| MTWORO.SCHED.WC | Scheduled work center |
| MTWORO.NEGOVLP | Negative overlap allowed flag |
| MTWORO.NUM | Number of concurrent workers |
| MTWORO.NUM.PERS | Number of persons per operation |
| MTWORO.NUM.PROC | Number of processes |
| MTWORO.TIME.PPR / MTWORO.MD.PR.HR / MTWORO.PR.PERHR | Time-per-process parameters |
| MTWORO.STD.TIME | Standard time |
| MTWORO.MIN.CHG | Minimum charge |
| MTWORO.OVERLAP | Overlap with next operation |
| MTWORO.PIECE.RT | Piece rate |
| MTWORO.LONGTIME | Long-run time flag |
| MTWORO.PRINT | Print this operation flag |
| MTWORO.MISCCOST/MISCDESC/MISCACST | Operation misc cost |

### Routing operation cost detail
| E (estimated) | A (actual) |
|---------------|-----------|
| MTWORO.ESETCST | MTWORO.ASETCST |
| MTWORO.ELABCST | MTWORO.ALABCST |
| MTWORO.EMCHCST | MTWORO.AMCHCST |
| MTWORO.EOUTCST | MTWORO.AOUTCST |
| MTWORO.EFOHCST | MTWORO.AFOHCST |
| MTWORO.EVOHCST | MTWORO.AVOHCST |

---

## MTRO.* namespace — ROUTING master routing templates (47 vars)

Standard routing template definitions (not WO-specific):

| Var | Meaning |
|-----|---------|
| MTRO.CODE/KEY | Routing key |
| MTRO.OPER | Operation number |
| MTRO.DESC/OPERDESC | Routing/operation descriptions |
| MTRO.TYPE | Routing type |
| MTRO.LEAD | Lead time |
| MTRO.VENDCOST/VENDCODE/VENDNAME | Outside-process vendor info |
| MTRO.PARTSHR/TIMEPART | Part-share/time-partition |
| MTRO.SETUPHRS | Standard setup hours |
| MTRO.LOTSIZE | Lot size |
| MTRO.INSTR | Instructions |
| MTRO.WC/WCDESC | Work center |
| MTRO.LABOR/MACHINE/FOVHD/VOVHD/SETUP | Standard cost rates |
| MTRO.TMACHINE/TMACHDESC | Template machine |
| MTRO.TOOL/TOOLDESC | Tool and description |
| MTRO.NUM/NUM.PERSON | Workers |
| MTRO.MISC.ACOST | Misc actual cost |
| MTRO.OP.TEMP.NO | Operation template number |
| MTRO.NUM.PROCES/TIME.PERPR/MD.PROC.HR/PROC.PERHR | Process time params |
| MTRO.STD.TIME/MIN.CHG/OVERLAP/PIECE.RATE/LONGTIME | Time standards |
| MTRO.PRINT/CLASS/EXTRA | Output/class/UDF |
| MTRO.NEGOVLP | Negative overlap flag |
| MTRO.DEF.TIME | Default time |
| MTRO.R.TYPE | Rate type |
| MTRO.EST.LINE/EST.TAG | Estimating link fields |

---

## MTWOR.* namespace — WORECV finished goods receipts (10 vars)

| Var | Meaning |
|-----|---------|
| MTWOR.WOPRE/WOSUF | WO identity |
| MTWOR.DATE | Receipt date |
| MTWOR.ASSY | Assembled item code |
| MTWOR.DESC | Description |
| MTWOR.QTY | Received quantity |
| MTWOR.USESTD | Use standard cost flag |
| MTWOR.AVGC | Average cost |
| MTWOR.LOT | Finished goods lot |
| MTWOR.SERIAL | Finished goods serial |
| MTWOR.REF | Reference |

---

## IS.WOEX.* namespace — ISWOEX WO extension UDFs (27 vars)

| Var | Type | Meaning |
|-----|------|---------|
| IS.WOEX.WOPRE/WOSUF | Key | WO identity |
| IS.WOEX.ITP/ITPP | Code | Inspection type/phase |
| IS.WOEX.RF | Flag | Reference flag |
| IS.WOEX.EXTRA | — | UDF extra |
| IS.WOEX.MCLASS/MNUM | Code | Machine class/number |
| IS.WOEX.CDATE | Date | Change date |
| IS.WOEX.DATE1..DATE5 | Date | UDF date fields 1-5 |
| IS.WOEX.INT1..INT5 | Int | UDF integer fields 1-5 |
| IS.WOEX.NUM1..NUM2 | Num | UDF numeric fields 1-2 |
| IS.WOEX.ALPHA1..ALPHA5 | Text | UDF alpha fields 1-5 |
| IS.WOEX.DESC1..DESC5 | Text | UDF description fields 1-5 |
| IS.WOEX.WC | Code | Work center UDF |
| IS.WOEX.CAUSE | Code | Cause code |
| IS.WOEX.GDATE | Date | Good-through date |
| IS.WOEX.NOTE | Text | Note |
| IS.WOEX.FLAGS/GNUMS/ALPHAS | — | Flag/number/alpha arrays |

---

## IS.TRAY.* namespace — ISWOTRAY WO tray tracking (21 vars)

| Var | Meaning |
|-----|---------|
| IS.TRAY.NUM | Tray number |
| IS.TRAY.WOPRE/WOSUF | WO identity |
| IS.TRAY.OPER | Associated operation |
| IS.TRAY.OPDESC | Operation description |
| IS.TRAY.CODE | Tray code |
| IS.TRAY.SQTY | Scheduled quantity in tray |
| IS.TRAY.COMQTY | Completed quantity |
| IS.TRAY.SCRPQTY | Scrapped quantity |
| IS.TRAY.QCREQD | QC inspection required flag |
| IS.TRAY.QCQTY | QC inspection quantity |
| IS.TRAY.LOC/BIN/BIN2 | Location and bin |
| IS.TRAY.BINQTY | Bin quantity |
| IS.TRAY.ALPHA | Alpha UDF |
| IS.TRAY.DATE | Date |
| IS.TRAY.EXTRA | Extra UDF |
| IS.TRAY.STATUS | Tray status |
| IS.TRAY.WHO | Who created/modified |
| IS.TRAY.CDATE | Create/change date |

---

## LAB.* namespace — BKDCLAB posting buffer (15 vars)

The LAB.* vars are the DC labor record being assembled before posting to BKDCLAB:

| Var | Meaning |
|-----|---------|
| LAB.DATE | Labor date |
| LAB.EMP | Employee ID |
| LAB.WOPRE/WOKEY/WOSUF | WO identity |
| LAB.OPER | Operation |
| LAB.POSTED | Posted flag |
| LAB.SHIFT | Shift |
| LAB.START/FINISH | Start/finish times |
| LAB.PARTS | Parts completed |
| LAB.SCRAPPED | Parts scrapped |
| LAB.NOJOBS | Number of concurrent jobs |
| LAB.RUNHRS | Run hours |
| LAB.SETUPHRS | Setup hours |

---

## BKAP.POL.* namespace — AP PO line (outside-process receiving) (38 vars)

Used when operator receives an outside-process PO from the shop floor:

| Var | Meaning |
|-----|---------|
| BKAP.POL.PONM | PO number |
| BKAP.POL.KEY/CNTR | PO line key/counter |
| BKAP.POL.ERD/ARD | Estimated/actual receipt date |
| BKAP.POL.PCODE/PDESC | Part code/description |
| BKAP.POL.PQTY/PPRCE/PDISC/PEXT | Quantity/price/discount/extended |
| BKAP.POL.PCOGS | Cost of goods |
| BKAP.POL.ITYPE | Item type |
| BKAP.POL.GLA/GLDPTA | GL account/dept |
| BKAP.POL.TXBLE | Taxable flag |
| BKAP.POL.RQTY/IQTY | Received/invoiced quantity |
| BKAP.POL.LOC | Location |
| BKAP.POL.OPER | Routing operation |
| BKAP.POL.WOPRE/WOKEY/WOSUF | Linked WO |
| BKAP.POL.EST | Estimate flag |
| BKAP.POL.OO.QTY | Outstanding order quantity |
| BKAP.POL.ITM.NO | Line item number |
| BKAP.POL.QC.QTY | QC inspection quantity at receiving |
| BKAP.POL.BUYOFF | QC buy-off flag |
| BKAP.POL.SCRAP | Scrap at receiving |
| BKAP.POL.PRTDIM | Part dimensions |
| BKAP.POL.PARENT | Parent PO line |
| BKAP.POL.RECNUM | Receipt number |
| BKAP.POL.EXTRA | UDF |
| BKAP.POL.INVNUM/INVDTE/PSTDTE | AP invoice integration |
| BKAP.POL.PCONV/PKSQTY | Pack conversion/pack quantity |

---

## T7PACKMENU — Reindex utility

T7PACKMENU is a standalone reindex tool for the PA module's database files.

| Var/Handle | Meaning |
|------------|---------|
| FMENU / MENU_HNDL | Menu form/handle |
| FGRID / GRID_HNDL | Grid form/handle |
| FD | FILEDES handle |
| FL | FILELOC handle |
| FK | FILEKEY handle |
| FKN | FILEKNUM handle |
| FDBF | FILEDBF handle |
| DICT_HNDL | FILEDICT handle |
| KEY_HNDL | FILEKEY (second) |
| LOC_HNDL | FILELOC (second) |
| KNUM_HNDL | FILEKNUM (second) |
| DBF_HNDL | FILEDBF (second) |
| DES_HNDL | FILEDES (second) |

Procs: T7REDINDEXDD.ONSTART, REINDEX.CLICK, EXIT.CLICK — simple reindex/exit UI.

---

## T7PASS — Password authentication sub

T7PASS.SRC provides the password gate before T7Paperless starts. 3 procs:
`T7PASS.ONOPENFILE`, `T7PASS.ONSTART`, `T7PASS.ONCLOSE`

Only 3 own vars: PASSWORD / BAD.PASS / XDEL (delete flag). Opens 45 tables (session init).

---

## Additional namespaces (from T7Paperless)

| Namespace | Table | Count |
|-----------|-------|-------|
| MTIC.PROD.* | MTICMSTR | 53 vars — estimating inventory |
| BKIC.PROD.* | BKICMSTR | 65 vars — production inventory |
| BKIC.LOC.* | BKICLOC | 33 vars — inventory by location |
| ISBIN.LOC.* | ISBINLOC | 9 vars — bin-level inventory |

See IC module doc for full BKIC.PROD.* and BKIC.LOC.* definitions.

---

## Control variables (T7Paperless)

| Var | Meaning |
|-----|---------|
| SCAN.WO | WO number from barcode scan |
| SCAN.OPER | Operation from barcode scan |
| WOPRE / WOSUF / OPER | Current WO/operation |
| POS | Position in routing list |
| LOGIN.EMP / LOGIN.NAME | Logged-in employee |
| LOGIN.DATE | Login date |
| TMP.EMP | Temp employee buffer |
| TMP.NOJOBS / NO.JOBS | Number of concurrent jobs |
| ITEM.LOC / BIN.LOC / BINLOC | Location tracking |
| CWH.CONTROL / WH.CONTROL | Warehouse control codes |
| HAND.HELD | Handheld device mode |
| CLOCKED.IN | Employee clocked-in flag |
| LABOR.TYPE | Labor type code |
| SHIFTSS / SHFTR | Shift selection |
| MAX.QTY / CUR.QTY | Quantity validation |
| ALLOK | All validations passed flag |
| T.* (16 vars) | DC labor transaction buffer (same fields as LAB.*) |
| TRAY.NUM / MAX.TRAY.QTY / TRAY.RCN | Tray management |
| QC.TESTING.REQD / TOT.QC.QTY / QC.PARTS / QC.SCRAPPED | QC tracking |
| BOM.DRILL.A / WU.DRILL.A | Drill-down modes |
| BACK.TO.BOM / BACK.TO.WU | Navigation back flags |
| N.ALERT1/2 / L.ALERT1/2 | Alerts |
| PASSWORD / BAD.PASS | Auth result vars (embedded from T7PASS) |
| ARCHACT | Archive action mode |
| ACCUTRON | Accumulate/tron flag |
| ACHOT / ACMOVE / ACROHS | Action flags |
| NOTE.OR.LINK | Notes vs links mode |
| PO.RECV | PO receiving mode |
| IC.REC | Inventory receipt mode |
| LASER.DEVICES | Laser scanner present |
| CFROM | Company from (multi-company) |
| UID | User ID |

---

## File handles in T7Paperless (40+ handles)

Includes dual-copy handles for comparison mode (current vs. archive):

| Pattern | Example | Purpose |
|---------|---------|---------|
| Standard | WORKORD.H, WOROUT.H | Current WO data |
| A-prefix | AWORKORD.H, AWOROUT.H | Alternate/archive WO data (comparison) |
| H-prefix | HLAB.H, HMAT.H, HROUT.H | History data (closed WO records) |
| DCSHFT.H | — | BKDCSHFT shift schedule |
| QCSPEC.H / QCRSLT.H | — | QC specifications / results |
| DBAFIFO.H | — | FIFO cost |
| BINMSTR.H | — | Bin location master |
| WOEX.H | — | ISWOEX WO extension |

---

## Architecture

T7Paperless is a real-time WO tracking hub:
1. T7PASS authenticates the operator (PASSWORD/BAD.PASS)
2. Operator scans SCAN.WO + SCAN.OPER → loads MTWO.WIP.* (WO header) + MTWORO.* (operation)
3. Operator records labor: T.*/LAB.* buffer → posts to BKDCLAB
4. For outside-process: BKAP.POL.* → receives PO line → updates WOROUT + INVTXN
5. For tray tracking: IS.TRAY.* → assigns components to ISWOTRAY trays
6. QC.TESTING.REQD triggers QC inspection entry via QCSPEC/QCRSLT handles
7. History mode: H* handles load closed WO records for comparison
8. Comparison mode: A* handles open alternate WO version alongside current

---

## Confidence notes

- MTWO.WIP.* 76-var namespace: confirmed from T7Paperless var extraction (Pass 233)
- MTWORO.* 44-var routing ops namespace: confirmed (Pass 233) — entirely new finding
- MTRO.* 47-var routing master namespace: confirmed (Pass 233) — entirely new finding
- IS.TRAY.* 21-var namespace: confirmed (Pass 233)
- BKAP.POL.* 38-var namespace: confirmed (Pass 233)
- LAB.* 15-var DC labor buffer: confirmed (Pass 233)
- MTWOR.* 10-var WORECV namespace: confirmed (Pass 233)
- T7PACKMENU = reindex utility: confirmed from proc name T7REDINDEXDD.ONSTART (Pass 233)
- A*/H* dual-handle comparison mode: inferred from naming pattern
- QC integration via QCSPEC.H/QCRSLT.H: confirmed from handle var names
