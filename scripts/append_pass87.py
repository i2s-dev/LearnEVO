import sys
sys.stdout.reconfigure(encoding='utf-8')

path = r'C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\HELP-RESOURCES.md'

content = r"""

---

## Pass 87 — HH/Handheld, WO Extended, IN Compliance/UDF/2D, DI Digital Signatures (2026-06-18)

### DI — Digital Signatures

**T7DIGSIG — Digitally Sign Purchase Order** (`T7DIGSIG.DFM`)
- Full PO display: BKAP.PO.NUM, BKAP.PO.ORDDTE, BKAP.PO.VNDCOD, BKAP.PO.VNDNME, BKAP.PO.DESC, BKAP.PO.ENTBY, BKAP.PO.OBYCUS (ordered-by customer)
- PO line display: BKAP.POL.PCODE/PDESC/PQTY/PPRCE/PEXT, ERD/ARD (estimated/actual receipt dates)
- **5-level approval categories**: `emp.cat[1..5]`, `emp.position[1..5]`, `emp.signoff[1..5]`
- Fields: `PO Threshold`, `PO-A Ent By ID`, `Signoff Category`, `Cat` per line
- Settings: Password, Signature File path, Signature Image Preview (image control)
- Actions: &Sign PO, &Category, &Settings, &View PO, &Send (email), &Reset

**T7DigSigChgPSWD — Change Digital Signature Password**
- Fields: `oldpass`, `newpass`, `reentpass`

**Confirmed tables:**
- `EMAIL.TAG/NAME/LEVEL/ADDRESS` — email recipient list for signature notifications
- The digital signature approver table uses `emp.cat[1..5]` / `emp.signoff[1..5]` arrays
  stored in an employee/signoff table (not yet named from DFMs alone)

---

### HH — Handheld Terminal System (Full Coverage)

EvoERP's handheld system is a complete warehouse execution layer built on barcode scanners.
The `ETBcomboval` field appears on every HH form — it is the barcode scan input box (a
combined entry/combo field). All forms use class `TEditForm1..4/10`.

**Architecture:**
- HH forms use a 5-button toolbar (ETB1..ETB5) with programmable functions
- Form sizes are designed for small-screen handheld devices
- `T7HH.DFM` = main HH menu hub; routes to function-specific sub-forms

#### HH — Shipping / SO Dispatch (T7HHSSOE/T7HHSODD)

**T7HHSSOE — Shipping (SO Scan-and-Ship)**
- Scan items into boxes by SO number, print packing slip
- Fields: `scan.qty.char`, `scan.item`, `curr.boxnum`, `print.ps`, `curr.skid.ucc`, `sonum.char`
- Shows: SO Number, Cust, Item Code, Description, Box No, Std Pack, Emp
- Actions: &Rel SO (release), Verify, Std Pk

**t7hhssoeLabels — Print Box Content Labels**
- Per-box label: `RTM_NAME`, `Incl.Lot`, `Incl.Serial`, `Box.Number`, `Box.Total`, `Lab.printer`, `labelQty`
- Option: Start New Box flag

**t7hhssoeLverify / T7HHSSOESVerify / T7HHSSOEVerify — SO Line Verification**
- Grid fields: `LINE.VPART`, `LINE.DESC`, `LINE.ORDERQTY`, `LINE.VBOXQTY`, `LINE.STDPK`
- `T7HHSSOEVerify` adds `LINE.V.PART`, `LINE.V.ORDQTY`, `LINE.V.PQTY` (packed qty)

**T7HHSODD — Shipping/DD dispatch screen**
- SO dispatch finalization: `reprint` (invoice), `prt.sr` (service/repair), `RTM_NAME`, `cert.per.box`
- Shows: Cust Name, SO Number, Cust Code; Last SO/Invoice Scanned

**T7HHSOLookup — SO Lookup grid**
- Columns: BKAR.INV.SONUM, BKAR.INV.CUSCOD, BKAR.INV.CUSNME

**T7HHNDTE — Enter Shipping Details**
- Ship Date, Ship Via, Tracking#, SO#, Freight
- Fields: `ship.date`, `BKAR.INV.SHPVIA`, `BKAR.INV.TRACK`, `BKAR.INV.SONUM`, `BKAR.INV.SHPCOD`, `BKAR.INV.SHPNME`, `BKAR.INV.FRGHT`

**T7HHN / T7HHN2 / T7HHNREL — HH-N SO Picking Queue**

`T7HHN` (Settings):
- `incl.crhold` — include customers on credit hold
- `incl.released` — include released SO lines
- `incl.zero.dates` — include lines with 00/00/00 ESD
- `limit.days` / `limit.date` — limit shipments to N working days
- `incl.kit.comps` — include kit components
- `item.type [RFAMNLBTKO]` — filter by inventory type
- `refresh.timer` (seconds) — auto-refresh interval
- `ship.early.only` / `incl.early`

`T7HHN2` (picking grid):
- Columns: GET.CRHOLD, GET.CUSCOD, GET.CUSNME, BKAR.INVL.INVNM, GET.CUSORD, BKAR.INVL.PCODE, BKAR.INVL.PDESC, BKAR.INVL.PQTY, GET.UOH, BKAR.INVL.ESD, BKAR.INVL.RTS
- Actions: &Lot, S&erial, Release SOs

`T7HHNREL` — same + `incl.bo` (include back orders) + LINES.* grid columns (same as N2)

#### HH — WO Material Issue and Scrap (T7HHWOx)

**t7hhwog — Issue Material to WO**
- Scan WO + component; issue qty to bin/location
- Fields: `scan.wo`, `COMPONENT`, `binloc`, `process.loc`, `scan.qty.char`
- Settings: `RTM_NAME`, `showPrtBox`, `prt.labels [Y/N/Ask]`, `prt.per.comp`, `Label.qty`, `large.lookups`

**T7HHWOIBIN — WC Bin Selection for WO component**
- Shows: Component code/desc, qty, WO number
- Scan bin: `default.bin`

**T7HHWOLabel — WO Label Printing**
- Filter by fin/semi-fin sequence range and class
- Fields: `sfrom.oper.fin`, `sthru.oper.fin`, `fin.class`, `nfin.class`, `sfrom.oper.nfin`, `sthru.oper.nfin`
- Settings: `one.label` (always qty=1), `ship.box.rtm`, `showPrtBox`, `full.lookups`
- Fields on scan: `scan.wo`, `RTM_NAME`, `scan.serial`, `partial.qty`, `full.qty`, `prt.ship.label`

**T7HHWOLookup — WO Lookup grid**
- Columns: MTWO.WIP.WOPRE, MTWO.WIP.WOSUF, MTWO.WIP.CODE (item number)

**T7HHWOLOT — WO Lot Number Release**
- Scan lot: `inp.lot`; fields: `qty.char`, `default.bin`, `scrap.code`, `ret.exp.date`, `Remaining Qty`
- Shows: On Hand qty per lot

**t7hhwop — Finish Production (WO-P)**
- Scan WO + final qty; record completion
- Settings: `final.qty.dflt [Y]`, `prompt.date [YNOnce]`, `wo.status [FRXI]`, `large.lookups`
- Fields: `scan.wo`, `scan.qty.char`, `default.bin`, `inp.oper`

**T7HHWOSCRAP — Report Scrap Material**
- Scan WO + component + scrap code; optionally scan lot/serial
- Fields: `scan.wo`, `COMPONENT`, `SCRAPCD`, `scan.lot`, `scan.Serial`, `prio`
- Settings: `RTM_NAME`, `prt.labels`, `prt.per.comp`, `Label.qty`, `showPrtBox`

**t7hhwoser — Enter Serial Number for WO completion**
- Fields: `inp.serial`, `scrap.code`, `filter.by.loc`
- Options: Auto Gen, CFG Ser

**T7HHWOIBIN / T7HHWOIProcess** — bin selection and processing spinner for WO issue

#### HH — PO Receiving (T7HHPOCx)

**t7hhpoc — Receive PO** (main PO receiving form)
- Scan PO# → vendor/item appear
- Fields: `bkap.po.num`, `RCVD_QTY`, `item`, `recv.into`, `binloc`
- Shows: Vendor Name, Item/Desc, PO Type, Ordered Qty, UM, Unit Cost/Price
- Manufacturer fields: `BKSB.MFG.MANUF`, `BKSB.MFG.MPART`
- Alert options: `vendor.alerts`, `item.alerts`, `large.lookups`
- Options: QC Inspect, Lot Controlled
- Wizard fields (from BKAP.POL): WORD/WSTAT/WREQ/WREM/WPART (on-hand/requisition/remaining)
- Actions: &Notes, &Settings

**T7HHPOCBIN** — bin selection during PO receipt

**T7HHPOCLot — Receive Lot Numbers**
- Scan lots: `inp.lot`, `lot.qty`; shows Last Lot Scanned, Item Code/Description, Qty

**T7HHPOCSER — Receive Serial Numbers**
- Fields: `inp.lot`, `inp.serial`; shows last serial scanned, lot, quantities

**T7HHPOCNotes** — notes per PO/line/item/vendor (4-tab form)

#### HH — Inventory Operations

**t7hhINGA — Print Inventory Labels**
- Scan item, enter qty, lot, serial, bin
- Fields: `scanitem`, `labelQty`, `ScanSerial`, `ScanLot`, `binloc`, `RTM_NAME`, `MISC`, `MISC2`
- Options: `prt.2d.labels` (print 2D barcode), `use.lot.qty`, `use.PO.qty`

**t7hhinlj — Transfer Inventory (HH)**
- Scan item, from loc/bin → to loc/bin, enter qty + date
- Fields: `scan.item`, `from.loc`, `to.loc`, `from.dflt.bin`, `to.dflt.bin`, `tsfr.uoh`, `tsfr.date`
- Shows: OH, From WC, To WC
- Option: `use.same.locs [YNA]` — same location code for all transfers

**T7HHINLJLot — Transfer Lot Numbers**
- Scan lot: `inp.lot`; fields: `lot.qty`, `mtlot.onhand`

**T7HHINLJSer — Transfer Serial Numbers**
- Scan serial: `inp.ser`; shows remaining-to-transfer

**T7HHItemLU — Inventory Item Lookup**
- Search by item or description: `MTIC.PROD.SUBST[1]`, `MTIC.PROD.DESC`

**T7HHO — Bin Transfer**
- From/To bin within a location: `tsfr.item`, `tsfr.qty`, `TO.BIN`, `FROM.BIN`, `tsfr.loc`
- Grid: ITEM.LIST, QTY.LIST

**t7hhinbins — WC Item Lookup (bin)** — lookup items in a work center's bins

#### HH — Physical Inventory

**T7HHPIC — PI-C Enter Tag Counts (settings)**
- `CountDate`, `qtr`, `year`, `location`, `empno`

**t7hhpictags — PI-C tags entry**
- Scan item: `scan.partnum`, `tagnum`, `countqty`, `lotno`, `serialno`, `binloc`, `hold.bin`, `comment`

#### HH — DC Labor (T7HHDCA)

**T7HHDCA — DC Labor Entry (Shipping/Production)**
- Record: Emp Name + No, Work Order, Sequence
- Actions: Start/Stop Shift, Shift Start/Stop
- Fields: `OPER`, `scan.wo`, `scan.emp`

**t7hhdcb / t7hhdcc** — DC loading screen spinners (TEditForm4/3)

#### HH — Tracking Numbers

**T7HHH — Enter Tracking Numbers**
- `track.num`, `ship.co`, `frt.charge`, `BOX.ID`
- Shows: Customer Name, SO Number, Box Number, Ship CO Name, Freight

#### HH — Alerts and Housekeeping

**T7HHALERTMSG** — alert notification popup (AlertMsgLabel displayed)
**T7HHProcess / T7HHWOIProcess** — processing data spinner dialogs

**Confirmed HH tables touched:**
- `BKAR.INV.*` / `BKAR.INVL.*` — SO header and lines
- `MTWO.WIP.*` — WO header
- `MTWOR.*` — WO receipt
- `MTWORO.*` — WO routing/operation
- `BKAP.PO.*` / `BKAP.POL.*` — PO header and lines
- `BKSB.MFG.*` — manufacturer cross-reference
- `MTIC.PROD.*` / `BKIC.PROD.*` — inventory item master
- `MTLOT.*` — lot master
- `EMAIL.*` — email tag/name/level/address list

---

### WO — Work Orders Extended (DFMs T7WOAK through T7WOKM)

Previously confirmed: WO-A header, WO-F labor, WO-G issue, WO-I receipt, WO-J close.
Pass 87 fills in the rest.

#### MTWO.WIP — WO Header Table (confirmed fields from T7WOAC/T7WOAE)

| Field | Meaning |
|---|---|
| MTWO.WIP.WOPRE | WO prefix |
| MTWO.WIP.WOSUF | WO suffix |
| MTWO.WIP.CODE | Parent item number |
| MTWO.WIP.DESC | WO description |
| MTWO.WIP.STATUS | Status (F=Released, R=Completed, C=Closed, S=Scheduled, I=In Process, X=On Hold) |
| MTWO.WIP.USERCD | User-defined class code |
| MTWO.WIP.LOC | Location |
| MTWO.WIP.SQTY | Standard qty to make |
| MTWO.WIP.COMQTY | Qty completed |
| MTWO.WIP.SSTART | Scheduled start date |
| MTWO.WIP.SFIN | Scheduled finish date |
| MTWO.WIP.DDATE | Due date |
| MTWO.WIP.ASTART | Actual start date |
| MTWO.WIP.AFIN | Actual finish date |
| MTWO.WIP.PRTY | Priority |
| MTWO.WIP.CUSTCODE | Customer code |
| MTWO.WIP.CUSTNAME | Customer name |
| MTWO.WIP.CONTAT | Contact/attention |
| MTWO.WIP.CUSORD | Customer PO# |
| MTWO.WIP.PROJ | Project/Job# |
| MTWO.WIP.EST | Quote/estimate# |
| MTWO.WIP.PPRCE | Price |
| MTWO.WIP.CHGORD | Change order number |
| MTWO.WIP.SOLINE | SO line reference |
| IS.OECO.DRAW | Drawing number |
| IS.OECO.REVLVL | Revision level |
| NCR.QTY | NCR (non-conformance report) quantity |

Extended cost fields (from T7WOIASK):
- `MTWO.WIP.EMAT/ESETUP/ETOT/EEXTRA/EMISC/VOVHD/EFOVHD/EOUTPR/ELABOR` — expected costs
- `MTWO.WIP.AMAT/ASETUP/ALABOR/AOUTPR/AFOVHD/AVOVHD/AMISC` — actual costs

#### MTWORO — WO Routing Table (T7WOKA confirmed)

| Field | Meaning |
|---|---|
| MTWORO.TYPE | Operation type |
| MTWORO.OPERDESC | Operation description |
| MTWORO.WC | Work center code |
| MTWORO.NUM | Routing line number |
| MTWORO.NUM.PROC | Number to process at once |
| MTWORO.TIMEPART | Time per part |
| MTWORO.PARTSHR | Parts per hour |
| MTWORO.OVERLAP | Overlap hours (start next op before this finishes) |
| MTWORO.NEGOVLP | Negative overlap flag |
| MTWORO.STD.TIME | Delay before next op (percentage of parts completed) |
| MTWORO.NUM.PERS | Number of persons |
| MTWORO.MACHNO | Machine number |
| MTWORO.TOOL | Tool code |
| MTWORO.VEND | Outside processing vendor code |
| MTWORO.VENDNAME | Vendor name |
| MTWORO.EOUTCST | Estimated outside processing cost |
| MTRO.LEAD | Lead time |
| MTWORO.PRINT | First Off Inspection flag |
| MTWORO.ESETHRS | Estimated setup hours |
| mtworo.longtime | Long-time flag |
| MTWORO.OPER | Sequence/operation number |
| MTWORO.STARTED | Sequence actual start time (T7WOKF) |
| MTWORO.FINISHED | Sequence actual finish time |
| MTWORO.%COMP | Percent complete (from MTWORO display) |

#### MTWOLA — WO Labor Table (T7WOF confirmed)

| Field | Meaning |
|---|---|
| MTWOLA.DATE | Labor date |
| MTWOLA.PARTS | Qty completed |
| MTWOLA.ASSY | WO item (assembly) |
| MTWOLA.ASSYDESC | Item description |
| MTWOLA.MACH | Machine used |
| MTWOLA.REGOVER | Reg/Over/Dbl/Sick/Hol/Vac type |
| MTWOLA.SHIFT | Shift |
| MTWOLA.NOJOBS | Number of jobs worked |
| MTWOLA.REWORK | Rework flag |
| MTWOLA.QCCODE | QC code |
| MTWOLA.QCDESC | QC description |
| MTWOLA.SCRAPCD | Scrap code |

Additional from WO-K-K reverse: `LAB.EMP`, `LAB.DATE`, `LAB.WOPRE`, `LAB.WOSUF`, `LAB.OPER`, `LAB.START`, `LAB.FINISH`, `LAB.PARTS`, `LAB.SCRAPPED`, `LAB.RUNHRS`, `LAB.SETUPHRS`

#### WOBOM — WO Bill of Materials (T7WOKB)

| Field | Meaning |
|---|---|
| WOBOM.COMPCODE | Component item code |
| WOBOM.COMPDESC | Component description |
| WOBOM.QTYPER | Quantity per assembly |
| WOBOM.OPER | Sequence/operation number |
| WOBOM.UM | Unit of measure |
| WOBOM.SCRAPQTY | Scrap quantity |
| WOBOM.QTYISSUED | Quantity already issued |

Also: `remark.replace` / `remark.origin` (edit.remark[1..15] — 15 BOM remarks)

#### WOMAT — WO Material Issues (T7WOG)

| Field | Meaning |
|---|---|
| WOMAT.DATE | Issue date |
| WOMAT.REF | Reference |
| WOMAT.PCODE | Component item code |
| WOMAT.PDESC | Component description |
| WOMAT.SERIAL | Serial number |
| WOMAT.LOT | Lot number |
| WOMAT.SCRAPCD | Scrap code |
| WOMAT.SCDESC | Scrap code description |
| WOMAT.QTYISSUED | Qty issued |
| WOMAT.QTYSCRAP | Qty scrapped |
| WOMAT.COST | Actual cost |

#### WODATE — Multi-Date WO Scheduling (T7WOAMDT)

- `WODATE.START`, `WODATE.FINISH`, `WODATE.QTY`, `WODATE.PRIO` — arrays per split date

#### MTWO.EX — WO Extra Charges (T7WOH)

| Field | Meaning |
|---|---|
| MTWO.EX.PROD | Item charged to |
| MTWO.EX.DESC | Description |
| MTWO.EX.CHGDESC | Charge description |
| MTWO.EX.GLACCT | GL account |
| MTWO.EX.GLDPT | GL department |
| MTWO.EX.CHG | Charge amount |
| MTWO.EX.DATE | Charge date |
| MTWO.EX.OP | Sequence/operation |
| MTWO.EX.WOPRE/WOSUF | WO prefix/suffix |

Cost type: `E` = estimated, `M` = material

#### MTWOR — WO Receipt (T7WOI)

| Field | Meaning |
|---|---|
| MTWOR.DATE | Receipt date |
| MTWOR.ASSY | Item received |
| MTWOR.DESC | Description |
| MTWOR.REF | Reference |
| MTWOR.USESTD | Use standard cost (vs avg) |
| MTWOR.AVGC | Average cost |

#### WO Sub-Program Summary

| Code | Form | Function |
|---|---|---|
| WO-A | T7WOAC/T7WOAE | Create/edit WO header |
| WO-B | T7WOB | Release WOs, import, set status/approval |
| WO-C | T7WOC | Print WO traveler (BOM, routing, labels, serials) |
| WO-D | T7WOD | Print pick list (bin locations, consolidated, RoHS) |
| WO-E | T7WOE | Print labor cards / adhesive labels |
| WO-F | T7WOF | Labor entry (DC time posting) |
| WO-G | T7WOG | Issue/scrap material |
| WO-H | T7WOH | Post extra charges |
| WO-I | T7WOI | WO receipt (close individual WO line) |
| WO-J | T7WOJ | Close or cancel WOs, handle unused serials |
| WO-K-A | T7WOKA | Edit WO routing |
| WO-K-B | T7WOKB | Edit WO BOM |
| WO-K-C | T7WOKC | WO completion/receipt lookup |
| WO-K-D | T7WOKD | Auto-create sub-WOs (explode BOM into WOs) |
| WO-K-E | T7WOKE | Substitute component |
| WO-K-F | T7WOKF | Record sequence start/finish times |
| WO-K-G | T7WOKG | WO list / gantt view filter |
| WO-K-J | T7WOKJ | Sync WO BOM/routing to standard, update ECO |
| WO-K-K | T7WOKK | Reverse DC labor posting |
| WO-K-L | T7WOKL | Mass WO creation (grid entry or file import) |
| WO-K-M | T7WOKM | Material request (non-BOM component) |

WO-K-D (`T7WOKD`) creates sub-WOs by exploding BOM sub-assemblies. Options:
- Match parent due date / est ship date [YNEB]
- Match parent job number [Y/N/W]
- Combine duplicate items into single WOs
- Use shop calendar for start date
- Max BOM explosion levels

WO-K-J (`T7WOKJ`) syncs live WOs after BOM/routing changes:
- Update WO class from item WO class
- Sync in-process WOs (BOM only)
- Update sequences after last sequence
- Update ECO revision level

---

### IN — Inventory Extended (T7INAACDOC through T7INGimport)

#### New Confirmed Tables

**IS.PROD.FLAGS[1..19] — Item Compliance Flags (T7INACMP/T7INBCMP)**

| Index | Field | Meaning |
|---|---|---|
| 1 | IS.PROD.FLAGS[1] | Conflict Free Material [Y/N/P/E] |
| 2 | IS.PROD.FLAGS[2] | RoHS [Y/N/P/E] |
| 3 | IS.PROD.FLAGS[3] | (warehouse control — from t7inbc) |
| 4 | IS.PROD.FLAGS[4] | (shelf control — from t7inbc) |
| 5 | IS.PROD.FLAGS[5] | (pick flag — from t7inbc) |
| 6 | IS.PROD.FLAGS[6] | WEEE [Y/N] |
| 7 | IS.PROD.FLAGS[7] | Certificate of Conformance Required [YNW] |
| 8 | IS.PROD.FLAGS[8] | REACH [Y/N/P/E] |
| 9 | IS.PROD.FLAGS[9] | CA Prop 65 [Y/N/P/E] |
| 10 | IS.PROD.FLAGS[10] | China RoHS [Y/N] |
| 11 | IS.PROD.FLAGS[11] | European RoHS [Y/N] |
| 12 | IS.PROD.FLAGS[12] | Consumer Electronics [Y/N] |
| 13 | IS.PROD.FLAGS[13] | Proprietary Item |
| 14 | IS.PROD.FLAGS[14] | UK Conformity Assessed (UKCA) [Y/N] |
| 15 | IS.PROD.FLAGS[15] | LDPE Recycle [Y/N] |
| 16 | IS.PROD.FLAGS[16] | UL Certification [Y/N] |
| 17 | IS.PROD.FLAGS[17] | Safety Data Sheet (SDS) required |
| 18 | IS.PROD.FLAGS[18] | Hazardous Material (HM) |
| 19 | IS.PROD.FLAGS[19] | Controlled Unclassified Information (CUI) |

Additional compliance fields:
- `CAPROP65` — CA Prop 65 flag
- `REACH` — REACH flag
- `ROHS` — RoHS [Y/N/P/E]
- `ROHS3` — RoHS 3 [Y/N/P/E]
- `CFM` — Conflict Free Material
- `COC.doc.reqd` — COC documentation required
- `rohs.doc.reqd` — RoHS documentation required
- `Prop.item` — Proprietary item flag
- `IS.PROD.ALPHA2[1..7]` — 2-character codes (country of origin, harmony code, control reg, etc.)
- `MTIC.PROD.VNAM[7]` — Moisture Sensitivity level (per IPC/JEDEC J-STD-033)
- `coo.2char` / `CofO.Alpha2` — Country of Origin 2-char ISO code
- Harmony Code, Control Classification Code (ECCN), Control Reg, NMFC, Shipping Class

Export control fields: `EAR99`, `EAR`, `ITAR`
QPL: `IS.PROD.FLAGS[?]` = Qualified Products List

**IS.PROD.NUM[1..N] — Item numeric flags**
- `IS.PROD.NUM[1]` — Reserve Stock Qty (from T7INBMRP)
- `IS.PROD.NUM[3]` — Bin Refill Quantity (from t7inbc)

**UDFi1..UDFi30 — 30 User-Defined Fields per item** (T7INAUDF/T7INBUDF)
- Displayed as UDF1..UDF30
- All named `UDFi1` through `UDFi30` in the DFM

**IS2D.BAR — 2D Barcode Layout Table** (T7INB2DB)
- `IS2D.BAR.DESC` — layout description
- `IS2D.BAR.CHAR` — character literal (or ASCII code)
- `IS2D.BAR.ASCII` — ASCII value
- `IS2D.BAR.FIELD` — field name to embed
- `IS2D.BAR.ORDER` — print order
- `IS2D.BAR.DOC.NAME` — associated document name
- Allows custom per-item 2D barcode composition

**IS.ECO — ECO (Engineering Change Order) Table** (T7INBECO/T7WOAECO)
- `IS.ECO.REVLVL` — current revision level
- `IS.ECO.DRAW` — drawing number
- `IS.ECO.ENTDATE` — ECO entry date
- `IS.ECO.DATE` — ECO effective date
- `IS.ECO.ENTBY` — entered by
- `IS.ECO.ECO` — ECO number
- `IS.ECO.CURRENT` — current ECO flag
- (Also stored per-WO as IS.OECO.* — open ECO for the WO)

**IS.PROD.SLEAD** — Shipping lead time (from t7inbc)
**IS.PROD.RCODE** — Refurbished item code
**IS.PROD.ITP** — Item type pointer (to IS.ITP.DESC)
**IS.ITP.DESC** — Item type description

**IN-A Sub-Tabs (T7INAA* forms — item inquiry sub-tabs)**

| Form | Tab name | Key fields |
|---|---|---|
| T7INAACDOC | Accutron Documentation | Doc types: COR/DR/VAR/MIN/SPR/ECN/ECN C/QC/VAR C/MIN C/QUAL |
| T7INAALO | Item Allocations | PO allocs (APPO/VNDCOD/VNDNME/APPQTY/APERD/APARD/APLOC) + WO allocs (WORD/WSTAT/WPART/WREQ/WISSU/WREM/WDATE/WLOC) |
| T7INACMP | Compliance | IS.PROD.FLAGS[1..19], REACH, CAPROP65, ROHS, CFM |
| T7INAFORECAST | Forecast | USAGE.MONTH/CURRENT/YEAR1..5 |
| T7INAPRC | Customer Pricing | qty/disc/cust/cname/prce per line |
| T7INASPC | Specifications | MTIC.PROD.SPECS[1..12] |
| T7INAUDF | User Defined Fields | UDFi1..UDFi30 |
| T7INAUSG | Item Usage | 5 years usage history |
| T7INAWIP | Item in WIP | Active WOs using this item |

**IN-B Sub-Tabs (T7INBA/T7INB* forms — item master entry sub-tabs)**

| Form | Tab | Key new fields |
|---|---|---|
| T7INB2DB | 2D Barcode Layout | IS2D.BAR.* array |
| t7inbc | Characteristics | lot/serial control, cycle.code, SLEAD, mapping.reqd, supersede.item, WH.CONTROL, WO.MAT |
| T7INBCMP | Compliance | same as INACMP |
| T7INBECO | ECO | IS.ECO.* |
| T7INBLNK | Item Links | I.ORDER/LINK/GPATH, IMAGE.TL[1..10], IMAGE.PCB[1..10] |
| T7INBMFG | Manufacturer XRef | BKSB.MFG.MANUF/MPART/CUST |
| T7INBMRP | MRP Settings | MTIC.PROD.MRPSW (MRP switch), EXPBF/DELBF, planner code, reserve stock |
| T7INBSPC | Specifications | MTIC.PROD.SPECS[1..12] |
| T7INBUDF | User Defined | UDFi1..UDFi30 |
| T7INBVND | Vendor XRef | BKSB.VEND.VEND/VPART, imp.vend.* |

**MTIC.PROD Extended fields (new from Pass 87):**
- `MTIC.PROD.MRPSW` — MRP include switch (per-item MRP override)
- `MTIC.PROD.MRP` — MRP flag (from T7INBMRP label "Include in MRP Generation?")
- `BKIC.PROD.AVFO` — Average forecast (avg forecast qty)
- `bkic.prod.avvo` — Average vendor order qty (?)
- `IS.PROD.NUM[1]` = Reserve Stock Qty (buffer)
- `MTIC.PROD.VEND[1]` — Primary approved vendor code
- `MTIC.PROD.CUST` — Customer code cross-reference
- `MTIC.PROD.ABC` — ABC classification (A/B/C)
- `MTIC.PROD.WIPDP` — WIP display flag
- `IS.PROD.GDATES[1]` — Product good/expiry date (from t7inaE)

**IN Program Summary:**

| Code | Form | Function |
|---|---|---|
| IN-A | T7INA/t7inaC/t7inaE | Item inquiry / lookup |
| IN-B | T7INB/t7INBE | Item master entry/edit |
| IN-C | T7INC | Inventory adjustments + import |
| IN-D | T7IND | Print record report (stock status, BOM, usage) |
| IN-E | T7INE/T7WOE | Print inventory transactions |
| IN-F | T7INF | Print inventory value (as-of date, export CSV) |
| IN-G | T7ING/T7INGimport | Print inventory labels (compliance links, import) |

**IN-F inventory value report** can export to CSV file (`expt.filename`), filter by:
- Item, class, category, vendor, GL account (glacct/gldpt), customer
- Active status [YNODEPSQR], sort by item/class/customer [P/C/U]
- As-of date (historical snapshot), include FIFO option
- Qty YTD / last year ranges

**IN-G label program** prints compliance symbols as links on labels:
- CE, WEEE, European RoHS, China RoHS, UL, LDPE Recycle, UKCA, REACH, User Defined 1/2
- Company logo

**IN-C adjustments** can import from comma-delimited file:
- Fields: item, qty, PO#, vendor, reference, PO price, WC bin, location
- Or lot-on-hand: item + location + lot + lot qty
- Cost basis: A=avg, S=standard, L=last cost

"""

with open(path, 'a', encoding='utf-8') as f:
    f.write(content)

print('Pass 87 appended.')
