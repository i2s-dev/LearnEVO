import sys
sys.stdout.reconfigure(encoding='utf-8')

path = r'C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\HELP-RESOURCES.md'

content = r"""

---

## Pass 88 — WO K-M/L/P/S series, SO full suite, PO full suite (2026-06-18)

### WO — New Tables Discovered

#### IS.PREQ — Production Material Request Table (T7WOKNB/C)

Live material request system used at work centers.

| Field | Meaning |
|---|---|
| IS.PREQ.EMP | Requesting employee |
| IS.PREQ.WOPRE | Work order prefix |
| IS.PREQ.WOSUF | Work order suffix |
| IS.PREQ.OPER | Sequence/operation number |
| IS.PREQ.RDATE | Request date |
| IS.PREQ.PART | Item/part requested |
| IS.PREQ.QTY | Quantity requested |
| IS.PREQ.REASON | Reason code |
| IS.PREQ.NOB | (not-on-BOM flag?) |
| IS.PREQ.NOTE | Request notes |
| IS.PREQ.NOTE2 | Secondary notes |
| IS.PREQ.LCOST | Last cost |
| IS.PREQ.IQTY | Issue quantity |
| IS.PREQ.INOTE | Issue notes |
| IS.PREQ.LOC | Location |

Sub-programs: T7WOKNA (live WC schedule), T7WOKNB (open requests grid — substitute/restore/print),
T7WOKNC (issue part from request), T7WOKT (print request report)

#### IS.SER — Serial Number Parent-Component Link (T7woko/T7WOKP)

Tracks serial numbers assembled into parent serial numbers.

| Field | Meaning |
|---|---|
| IS.SER.PSERIAL | Parent serial number |
| IS.SER.PARENT | Parent item code |
| IS.SER.PDESC | Parent item description |
| IS.SER.COMP | Component item code |
| IS.SER.CDESC | Component item description |
| IS.SER.CSERIAL | Component serial number |
| POSTED | Posted flag |

T7woko = parent serial → component serial lookup
T7WOKP = parent serial → component Lot lookup (fields: AWOP/AWOS/APPRT/APSER/ACOMP/ALOT)

#### IS.TRAY — WIP Tray/Bin Tracking (T7WOKS/T7WOKSA)

Tracks physical WIP containers (trays, bins) at work centers during WO processing.

| Field | Meaning |
|---|---|
| IS.TRAY.WOPRE | Work order prefix |
| IS.TRAY.WOSUF | Work order suffix |
| IS.TRAY.WHO | Employee who updated |
| IS.TRAY.CDATE | Change date |
| IS.TRAY.STATUS | WO status |
| IS.TRAY.OPER | Sequence/operation |
| IS.TRAY.CODE | Item code |
| IS.TRAY.BIN | Bin location |
| IS.TRAY.BINQTY | Qty in bin |
| IS.TRAY.DATE[1] | Date array |
| IS.TRAY.ALPHA[1] | Alpha array (description/notes) |
| IS.TRAY.ALPHA[3] | Secondary alpha |

T7WOKS edits individual bin assignments; T7WOKSA prints the WIP bin location report.

#### IS.WOPRIO — WO Priority Color Table (t7woprio/t7woprio2)

| Field | Meaning |
|---|---|
| IS.WOPRIO.PRIO | Priority code (1-9) |
| IS.WOPRIO.DESC | Priority description |
| IS.WOPRIO.COLOR | Display color for Gantt/list views |

#### ISSO.BOX — SO Box/UCC Label Table (T7WOS)

| Field | Meaning |
|---|---|
| ISSO.BOX.UCC | UCC-128 barcode number |
| ISSO.BOX.CODE | Item code |
| ISSO.BOX.QTY | Quantity in box |

#### WO Sub-Program Extensions

**T7WOS — WO Label / Serial Number Assignment**
- Assigns serial numbers to WOs and prints labels
- Fields: `scan.serial`, `assign.cntr`, `from.serial`, `thru.serial`
- Per-label: `edit.lbl.boxno`, `edit.lbl.misc`, `edit.lbl.qty`, `edit.lbl.total`, `edit.lbl.copy`
- Options: `gen.bar` (2D barcode), `one.per` (one lot entry per component), `mfg.date`
- Print modes: stock/index/regular labels (`adt.option`), blank labels (`BLANK.LABELS`)
- Print lot range: `from.lot`/`thru.lot`, WO receipt serials (`PRT.WORECV.SER`)

**T7WOP — Finish Production (WO-P)**
- Finalize WO production quantity and optionally close the WO
- Grid mode: WO#, item, qty, close WO flag
- Import mode: WO prefix, suffix, qty, close WO from CSV
- Fields: `m.date`, `from.wonum/thru.wonum`, `from.job/thru.job`

**T7WOPO/T7WOPOR — Create POs from WO Shortages**
- T7WOPO generates PO lines for open WO material shortages
- Options: `make.po`, `JOBNO`, `INC.SPECS`, order/receipt dates, offset, tie lines to WOs
- T7WOPOR reviews proposed PO lines before creating: BKIC.PROD.CODE, MTIC.PROD.DESC, PO.DATE, ER.DATE, QTY, BKMRP.PO.VEND, price

**T7WOTRWK — Rework to Stock WO**
- Creates a special rework WO to put reworked assemblies back into stock
- Fields: item, desc, quantity, location, sstart.date, sfin.date, issue.parent

**T7WOKNA — Live Work Center Schedule (monitor)**
- Real-time WC production schedule display (like a digital board)
- `location` filter, `timer` (refresh every N seconds), `audio` (audible cue when updated)

**WO-L Report Suite (T7WOLA through T7WOLO)**

| Code | Form | Report |
|---|---|---|
| WO-L-A | T7WOLA | WO open order list (by item, WO, customer, class, routing) |
| WO-L-B | T7WOLB | WO status report (by status/priority/class, multiple) |
| WO-L-C | T7WOLC | WC time utilization (by WC/machine, dept break) |
| WO-L-D | T7WOLD | WO completion status by sequence |
| WO-L-E | T7WOLE | Export labor hours to payroll file (optional post to PR) |
| WO-L-F | T7WOLF | WO shortage/need-by report (need.so/po/wo.date, alloc.date) |
| WO-L-G | T7WOLG | WC schedule by component (key.component[1..15]) |
| WO-L-H | T7WOLH | WO labor hours summary |
| WO-L-I | T7WOLI | Inventory stock status with WO status filter |
| WO-L-J | T7WOLJ | Finished WO report (early/late/on-time details) |
| WO-L-K | T7WOLK | WO BOM print (specs, dwg, subs, vendors, mfgs, phantoms, SMT) |
| WO-L-L | T7WOLL | WO component label print |
| WO-L-M | T7WOLM | Material summary report for SOs (uses WO BOM) |
| WO-L-N | T7WOLN | WO notes print |
| WO-L-O | T7WOLO | WC by customer report |

---

### SO — Sales Order Full Suite

#### BKAR.INV — SO Header Table (T7SOAC/T7SOAE confirmed)

Key previously unconfirmed fields:

| Field | Meaning |
|---|---|
| BKAR.INV.SONUM | SO number |
| BKAR.INV.ORDDTE | Order date |
| BKAR.INV.CUSCOD | Customer code |
| BKAR.INV.CUSNME | Customer name |
| BKAR.INV.CUSA1 | Customer ship-from address 1 |
| BKAR.INV.CUSA2[1..2] | Customer address lines 2+ |
| BKAR.INV.CUSCTY | Customer city |
| BKAR.INV.CUSST | Customer state |
| BKAR.INV.CUSZIP | Customer zip |
| BKAR.INV.CUSCNT | Customer country |
| BKAR.INV.CUSATT | Customer attention |
| BKAR.INV.SHPA1 | Ship-to address 1 |
| BKAR.INV.SHPA2 | Ship-to address 2 |
| BKAR.INV.SHPCTY | Ship-to city |
| BKAR.INV.SHPST | Ship-to state |
| BKAR.INV.SHPZIP | Ship-to zip |
| BKAR.INV.SHPCNT | Ship-to country |
| BKAR.INV.SHPATN | Ship-to attention |
| BKAR.INV.SHPNME | Ship-to name |
| BKAR.INV.SHPCOD | Ship via code |
| BKAR.INV.SHPVIA | Ship via description |
| BKAR.INV.TRACK | Tracking number |
| BKAR.INV.FRGHT | Freight amount |
| BKAR.INV.NUM | SO last invoice number |
| BKAR.INV.DESC | SO description |
| BKAR.INV.JOBNUM | Job number |
| BKAR.INV.FOB | FOB |
| BKAR.INV.ENTBY | Entered by |
| BKAR.INV.SUBTOT | Subtotal |
| BKAR.INV.TAXAMT | Tax amount |
| BKAR.INV.RTS | Release-to-ship date |
| BKAR.INV.TAXABL | Taxable flag |
| BKAR.INV.GLDPT | GL department |
| BKAR.INV.SLSP | Salesperson code |
| BKAR.INV.NL | Non-linked flag |
| BKAR.INV.CUSORD | Customer PO/order# |

SRTYPE — service/repair type (controls SO-E service/repair workflow)
SONUM.CHAR — SO number display field

#### BKAR.INVL — SO Line Table (t7Soa2/T7SOE confirmed)

| Field | Meaning |
|---|---|
| BKAR.INVL.PCODE | Item code |
| BKAR.INVL.PDESC | Item description |
| BKAR.INVL.LOC | Location |
| BKAR.INVL.TAX | Tax code |
| BKAR.INVL.RTS | Release-to-ship date |
| BKAR.INVL.PQTY | Ship quantity |
| BKAR.INVL.UBO | Back order quantity |
| BKAR.INVL.PPRCE | Unit price |
| BKAR.INVL.PEXT | Price extension |
| BKAR.INVL.UM | Unit of measure |
| BKAR.INVL.DISC | Discount % |
| BKAR.INVL.ESD | Estimated ship date |
| BKAR.INVL.ASD | Actual ship date (customer due date) |
| BKAR.INVL.STAT | Line status |
| BKAR.INVL.LONGP | Extended description |
| BKAR.INVL.HIDE | Hide on document flag |
| BKAR.INVL.INVNM | Invoice number |
| BKAR.INVL.FATD | (confirmed/fill-and-tie to date?) |
| line.prod.comm1/comm2 | Commission rates per line |
| line.prod.oqty | Original quantity ordered |
| line.prod.ipext | (invoiced price extension?) |

#### ISAR.CHG — SO Line Change History (T7SOLINEHIST)

Audit trail for every change to SO line fields.

| Field | Meaning |
|---|---|
| ISAR.CHG.CDATE | Change date |
| ISAR.CHG.BPRICE | Price before |
| ISAR.CHG.APRICE | Price after |
| ISAR.CHG.BDISC | Discount before |
| ISAR.CHG.ADISC | Discount after |
| ISAR.CHG.BOOQTY | Qty before |
| ISAR.CHG.AOOQTY | Qty after |
| ISAR.CHG.BASD | ASD before |
| ISAR.CHG.AASD | ASD after |
| ISAR.CHG.BESD | ESD before |
| ISAR.CHG.AESD | ESD after |
| ISAR.CHG.BCOMPR[1..2] | Commission rate before |
| ISAR.CHG.ACOMPR[1..2] | Commission rate after |
| ISAR.CHG.BLOC | Location before |
| ISAR.CHG.ALOC | Location after |
| ISAR.CHG.USER | User who made the change |

#### ISSR.INFO — SO User-Defined Fields (T7SOINFO/T7SOHINFO/T7SOLINFO)

20 alpha + 5 date UDF fields at SO header level, SO line level, and SO header misc level.

| Field | Meaning |
|---|---|
| ISSR.INFO.AL1..AL20 | Alpha user-defined fields 1-20 |
| ISSR.INFO.DATE1..DATE5 | Date user-defined fields 1-5 |
| ISSR.INFO.SRNUM | SO number (linking key) |

Labels for AL1..20 and DATE1..5 are configured in system setup (displayed as soAlpha1..20, soDate1..5 etc.)

Three separate sub-forms use this same table:
- T7SOINFO — SO-level "Sales Misc. Information"
- T7SOHINFO — SO-level "Sales Header Misc. Information"
- T7SOLINFO — SO-line-level "Sales Line Misc. Information"

#### BKIC.PMAT — Item Price Matrix (T7SOAPRC)

| Field | Meaning |
|---|---|
| BKIC.PMAT.QTY | Quantity break |
| BKIC.PMAT.RATE | Price at this quantity |
| BKIC.PMAT.PDESC | Price description |

Shown alongside BKIC.PROD.PRICE (base price) for item pricing lookup during SO entry.

#### ISAR.TXN — SO Bin Allocation Transactions (T7SOBIN)

| Field | Meaning |
|---|---|
| ISAR.TXN.QTY | Allocated quantity |
| ISAR.TXN.BIN | Bin location |
| ISAR.TXN.DATE | Transaction date |

T7SOBIN shows item/bin/qty/SO/customer/line qty/qty allocated/qty left.

#### BKAR.TXN — SO Lot Allocation Transactions (T7SOLOT)

| Field | Meaning |
|---|---|
| BKAR.TXN.QTY | Allocated quantity |
| BKAR.TXN.LOT | Lot number |
| BKAR.TXN.DATE | Transaction date |
| BKAR.TXN.BIN | Bin location |

#### BKAR.DEP — Customer Deposits (T7SOFDEP)

| Field | Meaning |
|---|---|
| BKAR.DEP.CUST | Customer code |
| BKAR.DEP.DATE | Deposit date |
| BKAR.DEP.DEPNO | Deposit number |
| BKAR.INVT.AMTRM | Amount remaining |

#### ISAR.JD — John Deere Label Fields (T7SOD)

Specialized EDI/label fields for John Deere supplier compliance:

| Field | Meaning |
|---|---|
| ISAR.JD.SONUM | SO number |
| ISAR.JD.INVNUM | Invoice number |
| ISAR.JD.PCODE | Item code |
| ISAR.JD.LINE# | Line number |
| ISAR.JD.QTYND | Quantity needed |
| ISAR.JD.PLATE# | Pallet license plate number |

T7SOD also supports: DUNS number, Kanban ID, country of origin, customer routing 1+2, supplier area 1-4, unloading point, delivery note, batch number, packaging type, supplier ID.
John Deere label types: I=individual, M=mixed, X=???, S=???

#### Recurring Orders (T7SOK/T7SOJINFO)

- `mem.group` — recurring group code
- `bkar.inv.invdte` — invoice date
- `mem.freq` — frequency
- `mem.max` — maximum invoices

T7SOK manages recurring templates: view next due dates, tag all in date range, set next order/ESD/CDD, customer PO#.

#### SO Program Summary

| Code | Form | Function |
|---|---|---|
| SO-A | T7SOAC/T7SOAE | Create/edit SO header + lines |
| SO-B | T7SOB | Print SO (quote/acknowledgment) |
| SO-BIN | T7SOBIN | SO bin allocation |
| SO-C | T7SOC | Print packing slip + C of C |
| SO-D | T7SOD | Print shipping labels (standard + JD EDI) |
| SO-E | T7SOE | Release/ship SO lines |
| SO-F | T7SOF | Print invoice |
| SO-G | T7SOG | Post invoice (COGS + commissions) |
| SO-K | T7SOK | Recurring order processing |
| SO-LOT | T7SOLOT | SO lot allocation |
| SO-N | T7SON | Create work orders from SO lines |

**SO-G posting flow:** print → post COGS → post commissions → update GL.
SOG-A shows live posting progress; SOGACHK handles cash terms deposits.

**SO-N options (create WOs from SO):**
- Match WO suffix to SO line number
- Auto-generate serial numbers
- Create WOs for kit components / make-from items / non-inventory types
- Multi-assembly WO option
- Offset start/finish dates
- Use shop calendar / inventory lead time for start dates
- Combine duplicate items into single WOs

---

### PO — Purchase Orders Full Suite

#### BKAP.PO — PO Header Table (T7POA confirmed)

| Field | Meaning |
|---|---|
| BKAP.PO.NUM | PO number |
| BKAP.PO.ORDDTE | Order date |
| BKAP.PO.VNDCOD | Vendor code |
| BKAP.PO.VNDNME | Vendor name |
| BKAP.PO.VNDA1 | Vendor address 1 |
| BKAP.PO.VNDA2 | Vendor address 2 |
| BKAP.PO.VNDCTY | Vendor city |
| BKAP.PO.VNDST | Vendor state |
| BKAP.PO.VNDZIP | Vendor zip |
| BKAP.PO.VNDCNT | Vendor country |
| BKAP.PO.VNDATN | Vendor attention |
| BKAP.PO.SHPA1 | Ship-to address 1 |
| BKAP.PO.SHPA2 | Ship-to address 2 |
| BKAP.PO.SHPCTY | Ship-to city |
| BKAP.PO.SHPST | Ship-to state |
| BKAP.PO.SHPZIP | Ship-to zip |
| BKAP.PO.SHPCNT | Ship-to country |
| BKAP.PO.SHPATN | Ship-to attention |
| BKAP.PO.SHPNME | Ship-to name |
| BKAP.PO.SHPCOD | Ship via code |
| BKAP.PO.SUBTOT | Subtotal |
| BKAP.PO.TAXAMT | Tax amount |
| BKAP.PO.TOTAL | Total |
| BKAP.PO.DESC | Description |
| BKAP.PO.TERMNM | Terms name |
| BKAP.PO.OBYCUS | Ordered-by customer (SO customer driving the PO) |
| BKAP.PO.FOB | FOB |
| BKAP.PO.ENTBY | Entered by |
| BKAP.PO.ISCUR | Currency code |
| BKAP.PO.LOC | Receiving location |
| BKAP.PO.GLDPT | GL department |
| BKAP.PO.EMPNUM | Employee number (signer) |
| BKAP.PO.ISBROKE | Customs broker flag |
| BKAP.PO.CONFIRM[2] | PO type / confirmation code |
| BKAP.PO.NL | Non-linked flag |
| BKAP.TELEPHONE[1] | Phone 1 |
| BKAP.TELEPHONE[3] | Fax |

Risk Assessment fields (T7POAC — aerospace/defense POs):
- `risk.assess[1..6]` — Schedule risks, obsolescence, first article, NADCAP certs, tooling, test reports
- `ritec.dpas` — DPAS (Defense Priority Allocations System) rating
- `ritec.contract` — Contract number

#### BKAP.POL — PO Line Table (T7POA2/t7poc confirmed)

| Field | Meaning |
|---|---|
| BKAP.POL.PCODE | Item code |
| BKAP.POL.PDESC | Item description |
| BKAP.POL.QTY | Order quantity |
| BKAP.POL.OO.QTY | Original order quantity |
| BKAP.POL.ERD | Estimated receipt date |
| BKAP.POL.ARD | Actual receipt date |
| BKAP.POL.PRCE | Unit price |
| BKAP.POL.UM | Unit of measure |
| BKAP.POL.PCON | Purchase conversion factor |
| BKAP.POL.TAX | Tax code |
| BKAP.POL.DISC | Discount % |
| BKAP.POL.EST | Estimate number |
| BKAP.POL.WOPRE | WO prefix |
| BKAP.POL.WOSUF | WO suffix |
| BKAP.POL.OPER | WO sequence |
| BKAP.POL.GLDEPT | GL department override |
| BKAP.POL.LOC | Line location |
| NKAP.POL.UM.LIN[1..2] | Unit of measure array |
| BKAP.POL.RQTY | Received quantity |
| enter.prod.conf | Confirmed flag |
| enter.prod.long | Extended description |

#### BKRFQ — RFQ / Price Quote Table (T7POF/T7POH)

| Field | Meaning |
|---|---|
| BKRFQ.PROD | Item code |
| BKRFQ.PRODDESC | Item description |
| BKRFQ.VEND | Vendor code |
| BKRFQ.VENDNAME | Vendor name |
| BKRFQ.PARENT | Parent item (WO assembly) |
| BKRFQ.PARNTDESC | Parent description |
| BKRFQ.EST | Estimate number |
| BKRFQ.OPER | WO operation/sequence |
| BKRFQ.ISSUE | Issue/RFQ date |
| BKRFQ.EXP | Expiry date |
| BKRFQ.PUM | Purchase unit of measure |
| BKRFQ.PCONV | PO conversion factor |
| BKRFQ.LEAD | Lead time |
| BKRFQ.QTY[1..10] | Quantity breaks (up to 10) |
| BKRFQ.COST[1..10] | Price at each quantity break |
| BKRFQ.MIN | Minimum quantity |
| BKRFQ.MINCST | Minimum cost |
| BKRFQ.LCDATE | Last change date |
| BKRFQ.CWHO | Changed by |
| BKRFQ.EXTRA | Extra notes |
| BKRFQ.FLAG | Flag (archive/active status) |
| BKRFQ.USE | Use in estimation flag |

RFQ workflow: PO-F (enter RFQ) → PO-G (convert to PO) → PO-H (vendor price history/archive)
PO-I-C (print open RFQs) → PO-I-D (print vendor price lists, expired/current)
T7POAPrBrk verifies price breaks at PO entry time.

#### PO Receipt (t7poc — PO-C)

Full receipt form fields:
- `RCVD_QTY` — received qty
- `PKSLIP.QTY` — packing slip qty
- `ENTER.PRICE` — entered unit cost
- `RINTO` / `RCVINTO.TXT` — receive into (QC, stock, location)
- `RCVD_WT` — received weight
- `POL.JOB` — job number per line
- `no.work.done` — flag: received but no work performed (outside processing return)
- `DTS` — dock to stock (skip QC and put directly into stock)
- `BKAP.PO.ISBROKE` — customs broker involved
- `BKAP.PO.EMPNUM` — employee receiving
- `PACKING.SLIPNUM` — packing slip number
- `PO.CONFIRM.TXT` — PO type text
- `BKAP.PO.ISCUR` — currency code

#### PO QC Buyoff (T7POJC — PO-J-C)

| Field | Meaning |
|---|---|
| BKQC.QTY.RECVD | Total received qty |
| BKQC.QTY.BUYOFF | Total bought off qty |
| BKQC.QTY.REJECT | Total rejected qty |
| BUYOFF.REMAIN | Qty remaining to buy off |
| BKQC.TRN.GQTY | Good qty this buyoff |
| BKQC.TRN.BQTY | Bought-off qty |
| BKQC.TRN.UQTY | Use-as-is qty |
| BKQC.TRN.SCRAP | Scrap qty |
| BKQC.TRN.REWORK | Rework qty |
| BKQC.TRN.NQTY | NCR qty |
| BKQC.QTY.NCR | NCR accumulated qty |
| BKQC.PKSLIP.NUM | Packing slip number |
| BKQC.VEND.CODE | Vendor code |
| BKQC.RECV.DATE | Receipt date |
| BKQC.PO.NUM | PO number |
| DEFAULT.BING | Default bin for good parts |
| DEFAULT.BINU | Default bin for use-as-is parts |
| rohs | RoHS flag |
| sampl | Sample size |
| mpart | Manufacturer part number |

Sub-dialogs: T7pojcqc (multi use-as-is codes), T7pojcsc (multi scrap codes)

#### PO Vendor On-Time Delivery (T7POIH/T7POJD)

- PO-I-H: evaluates vendor on-time delivery for a date range
- Date basis options: scheduled (ERD), actual receipt date, or defined cutoff
- Allowable early/late days tolerance
- Base on: total dollars, item quantities, or line count
- Option to save results to vendor history

#### POENG — PO Engineering Report (T7POENG)

User-defined sort/break report with up to 10 index fields:
- `index.text[1..10]` — index labels
- `UDBRK.ARRAY[1..10]` — user-defined break arrays
- `REPORT.TITLE` — custom report title
- Filters: PO range, ship-to range, vendor state range, and more (`ZBKSA.*` fields)

#### PO Program Summary

| Code | Form | Function |
|---|---|---|
| PO-A | T7POA/T7POAC/T7POAE | Create/edit PO (standard, risk assessment, enhanced) |
| PO-B | T7POB | Print PO (with digital signature option) |
| PO-C | t7poc | Receive PO (dock-to-stock, customs broker, customs) |
| PO-E-A | T7POEA | Print RFQs |
| PO-ENG | T7POENG | User-defined sort/break report |
| PO-F | T7POF | Enter RFQ (10 qty/cost break tiers) |
| PO-G | T7POG | Convert RFQ to PO |
| PO-H | T7POH | Vendor price history and archive |
| PO-I-C | T7POIC | Print open RFQs by range |
| PO-I-D | T7POID | Print vendor price lists |
| PO-I-G | T7POIG | PO expedite report (rush/expedite colors) |
| PO-I-H | T7POIH | Vendor on-time delivery analysis |
| PO-I-I | T7POII | PO change report |
| PO-J-A | T7POJA | Print QC receipt travelers |
| PO-J-B | T7POJB | PO receipt value/expedite report |
| PO-J-C | T7POJC | QC buyoff form |
| PO-J-D | T7POJD | Vendor on-time delivery report |
| PO-K | T7POK | Close POs |
| PO-L | T7POL | Vendor XRef list (primary vendor indicator) |
| PO-L-A | T7POLA | Approved vendors report |

**Digital Signature integration:** T7POB has "Enter Digital Signature (Y/N/Ask)" option;
T7POAE has "&Sign PO" button — these invoke T7DIGSIG.

"""

with open(path, 'a', encoding='utf-8') as f:
    f.write(content)

print('Pass 88 appended.')
