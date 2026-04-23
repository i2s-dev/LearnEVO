# File Names — Complete Table Index

Status: verified (verbatim from vendor help file).

Source: [file_names.htm](../../samples/chm/extracted/file_names.htm) in
the decompiled [EvoHELP.CHM](../../samples/chm/EvoHELP.CHM). Extracted
via [scripts/chm_to_md.py](../../scripts/chm_to_md.py).

All data files end in `*.B` (default company) or `*.Bxx` where `xx` is
the 2-char company code. Per-field layout of any table is printable
via [UT-H Print File Layouts](../../samples/chm/extracted/ut-h_print_file_layouts.htm).

For a deeper explanation of the data-dictionary system as a whole see
[overview.md](overview.md). For how to connect external software to
these tables, see
[external-odbc-connections.md](../01-architecture/external-odbc-connections.md).

---

## Accounts Payable

| File | Description |
|---|---|
| BKAPCHKH | AP payment history |
| BKSYAP | AP default master |
| BKAPINVT | AP invoice |
| MKICLASS | AP invoice cross-reference |
| ISAPPROJ | AP link to job |
| BKAPINVL | AP voucher |
| ISVNDADT | Approved vendor control |
| ISAPAINT | Archived AP invoices |
| ISAPAINL | Archived AP vouchers |
| ISAPACHK | Archived check history |
| BKAPADSC | Archived DBA vendor & PO notes |
| ISAPAVND | Archived vendor master |
| BKAPCHKF | Pro-forma check register |
| BKAPVEND | Vendor master |
| BKAPVND2 | Vendor tax ID |
| BKAPDESC | Vendor website |
| BKAPRIVL | Voucher template / recurring voucher |

## Accounts Receivable

| File | Description |
|---|---|
| IS2DBAR | 2D bar-code parameters |
| BKART | Aging transaction detail |
| BKARTNOT | Aging transaction notes |
| BKARINVT | AR aging invoice |
| MKECLASS | AR customer check cross-reference |
| BKSYAR | AR default master |
| BKARINVV | AR voucher |
| ISISATAX | Archive sales tax |
| ISARAIVV | Archived AR vouchers |
| ISARAINT | Archived customer invoices |
| ISARACST | Archived customer master |
| ISARACHK | Archived customer payment history |
| ISARAHTX | Archived sales tax |
| ISARAT | Archived transaction detail |
| ISARATNT | Archived transaction notes |
| ISCC | Credit-card listing |
| CUSTCLAS | Customer class master |
| BKARDEP | Customer deposits |
| BKARCUST | Customer master |
| BKARCHKF | Customer payment history |
| BKARDESC | Customer website |
| BKCMDUN | Dun letter header |
| BKCMDUNH | Dun letter history |
| BKCMFORM | Form & dun letter template |
| BKISHTAX | Paid sales tax detail |
| BKARHTAX | Sales tax |
| BKISTAX | Sales tax detail |
| BKARSHIP | Ship-to customer master (not used) |
| ISTAXFIL | Tax codes |
| ISTAXGRP | Tax groups |

## Bills of Material

| File | Description |
|---|---|
| BKSBMFG | Approved manufacturers |
| BKSBPART | Approved substitute parts |
| BKSBVEND | Approved vendors |
| BKBMAMTR | Archived BOM |
| BKBMMSTR | BOM master |
| BKBMNOTE | BOM notes |
| BKBMREMK | BOM remarks |
| BKBMSUMM | Temp file for summarized BOM |
| BKBMAVAL | Temp file used by BOM Availability report |

## Contact Manager

| File | Description |
|---|---|
| BKCMACCC | Account class codes |
| BKCMACCL | Account classes |
| BKCMACCN | Account contacts |
| BKCMACTD | Account dates |
| BKCMDTCD | Date codes |
| BKCMCUST | Contact account master |
| BKCMLEAD | Lead source codes |
| BKCMTERR | Territory master |

## Contract Review

| File | Description |
|---|---|
| ISCTREVU | Contract review approver list |
| ISSOREVU | Contract review status |

## Data Collection

| File | Description |
|---|---|
| BKDCLAB | Posted DC labor transactions |
| BKDCSHFT | DC shifts |
| BKDCPLAB | Unposted DC labor transactions |

## Data Import

| File | Description |
|---|---|
| BKGLECOA | DI chart of accounts |
| WOEMAT | DI material issues |
| WOERECV | DI WO receipts |
| BKBMEMTR | DI BOM master |
| BKBMERMK | DI BOM remarks |
| BKARECST | DI customer |
| BKGLETRN | DI GL transactions |
| BKICEMTR | DI inventory |
| BKICELOC | DI inventory location |
| BKAPEIVT | DI open AP |
| BKAREIVT | DI open AR |
| BKRTEMTR | DI routings |
| BKAPEVND | DI vendor |
| WOELABOR | DI labor |
| MTICEMTR | DI inventory |

## EDI

| File | Description |
|---|---|
| BKEDIDUN | Customer ID / EDI enablement file |
| BKEDMSTR | EDI master setup file |
| BKEDNOTE | EDI notes |
| BKEDPOST | Invoices subject to EDI |
| BKEDIL | Temporary SO line items |
| BKEDIH | Temporary SO headers |

## Estimating

| File | Description |
|---|---|
| BKESTCFG | Estimating configuration |
| BKMATCST | Material cost file |
| ESTSUM | Estimate master |
| MTEXCHG | Extra charges |

## Fixed Assets

| File | Description |
|---|---|
| ISFXASST | Fixed asset master |
| ISFXATRN | Fixed asset transactions |

## Features & Options

| File | Description |
|---|---|
| ISFOHIST | Configuration history |
| ISFOBMRM | Configuration line remarks |
| ISFOLINE | Configuration lines |
| ISFOORDL | Configuration order-line conversion |
| ISFOHEAD | Configuration header |
| BKFOCFG | Features & Options configuration |

## General Ledger

| File | Description |
|---|---|
| ISBANKS | Bank master |
| BKGLCOA | Chart of accounts |
| ISGLCOA | Chart of accounts 3–6 yr past |
| BKGLCHK | Checking account register |
| BKGLCCOA | Consolidated chart of accounts |
| BKGLFCOA | Consolidated financials |
| BKGLFSTL | Custom financial statements |
| ISJBSF | Business status |
| BKGLSTMT | Financial statement setup |
| ISGLDATE | Fiscal period dates |
| BKGLGJRN | General journal header |
| BKGLGJLN | General journal line items |
| ISGLHDAT | Historical fiscal period dates |
| BKGLTGJR | Journal template header |
| BKGLTGJL | Journal template line |
| ISGLBDGT | Multi-year budget |
| ISGLNBGT | Next-year budget |
| BKGLTRAN | Posted GL transactions |
| BKGLRGJR | Recurring general journal header |
| BKGLRGJL | Recurring general journal lines |
| BKGLX | Transaction detail |
| BKGLXH | Transaction detail history |
| BKGLTEMP | Unposted GL transactions |

## International Module

| File | Description |
|---|---|
| ISBROKER | Customs broker fees |
| ISDUTY | Duty codes |
| ISIS | International master settings |
| ISLANDF | Landed cost defaults |
| ISMCF | Multi-currency master file |
| ISMCR | Currency conversion factors |

## Inventory

| File | Description |
|---|---|
| BKICAMTR | Archive inventory master |
| ISICAMTR | Archive inventory master file 3 |
| INVATXN | Archive inventory transactions |
| MTICAMTR | Archived inventory master 2 |
| ISITMCFG | Auto part generator |
| DBAFIFO | FIFO / LIFO buckets |
| BKACTRPT | IN-L-O report layout |
| BKICREF | Customer cross-reference |
| BKQTTEMP | Inventory links |
| BKICLOCM | Inventory location master |
| BKICLOC | Inventory locations |
| BKICMSTR | Inventory master |
| MTICMSTR | Inventory master 2 |
| ISICMSTR | Inventory master 3 |
| ISICADT | Inventory master audit file |
| ISMICADT | Inventory master audit file 2 |
| INVTXN | Inventory transactions |
| ISUDFINV | Inventory user-defined definitions |
| ISUDMSTR | Inventory user-defined master list |
| ISCATMST | Item category master list |
| CLASMSTR | Item class master |
| CLASS | Item classes |
| ISECO | Item ECO listing |
| ISITP | ITP master listing |
| ISORDECO | Order-specific ECO |

## Lot Control

| File | Description |
|---|---|
| LOT | Lot number master |

## Material Requirements

| File | Description |
|---|---|
| MTMRP | Material requirements (MRP) master |
| SUMPNCUS | MRP temp file |
| BKMRPPO | MRP-to-PO conversion file (temporary) |
| BKMRPSW | Temp file used by MRP |

## Payroll

| File | Description |
|---|---|
| BKPRCURP | Current payroll information (temporary) |
| BKPRGLFL | Payroll division master |
| ISPRMSTR | Payroll employee master |
| BKPRHIST | Payroll history |
| BKPRFTAX | Payroll tax tables |
| BKPRW2 | Payroll W-2 file |
| BKPRINFO | Supplemental employee master |
| ISPRTEMP | Temp file for consolidating payroll detail |
| BKPRTC | Time cards |
| BKCPMSTR | CheckMark payroll master |
| BKCPEC | CheckMark payroll transfer |

## Physical Inventory

| File | Description |
|---|---|
| BKPILCNT | Counted lots |
| BKPISCNT | Counted serial numbers |
| BKPIFROZ | Frozen physical inventory |
| BKPILOT | Frozen PI lots |
| BKPISER | Frozen serial numbers |
| BKPIMSTR | Physical inventory master |
| PIBINLOC | PI bin location |
| PIBINLOT | PI lot bin location |
| BKPIPHYS | Tag file |

## Purchase Orders

| File | Description |
|---|---|
| ISARFQ | Archive RFQ |
| ISAPHQT | Archive vendor pricing |
| BKAPAPO | Archived PO header |
| BKAPAPOL | Archived PO lines |
| ISAPARFQ | Archived RFQ header |
| ISAPARFL | Archived RFQ line |
| ISAPCHG | Changes to purchase orders |
| BKAPPO | Open PO header |
| BKAPPOL | Open PO lines |
| ISDIGSIG | PO digital signature |
| BKAPHPO | PO receiver header |
| BKAPHPOL | PO receiver lines |
| ISPODESC | Purchase order description list |
| BKQCMSTR | Quality Control master |
| BKQCTRAN | Quality Control transaction |
| BKAPRFQ | RFQ header |
| BKAPRFQL | RFQ lines |
| BKSOPO | Temp file for convert SO to PO |
| BKWOPO | Temp file for convert WO to PO |
| BKAPQUOT | Vendor pricing |
| BKRFQ | Verbal for quotes |

## RMA

| File | Description |
|---|---|
| ISRMAINV | RMA header |
| ISRMINVL | RMA lines |
| ISRMAI | RMA status & reason for return |
| ISRMAC | RMA reason-for-return codes |

## Routings

| File | Description |
|---|---|
| ROUTAING | Archived routing master |
| DPTMENT | Departments |
| MACHINE | Machines |
| BKRTCST | Routing costs |
| ROUTING | Routing master |
| BKRTSPEC | Routing specifications |
| ROUTTEMP | Routing templates |
| BKRTTEMP | Specification templates |
| TOOL | Tool master |
| WORKCTR | Work center |

## Sales Analysis

| File | Description |
|---|---|
| BKSAREPT | Report names for SA-M & SA-N |

## Sales Commissions

| File | Description |
|---|---|
| BKPRAGNT | Agents |
| BKPRACOM | Archived commission detail |
| ISARAIVI | Archived commission detail |
| BKARINVI | Commissions |
| BKPRCOMM | Commissions |
| ISREPORD | Extended commission line-item commissions |
| ISREPLNK | Extended commission rep assignment |
| BKPRHCOM | Posted commission detail |
| BKPRSALE | Salesperson master |

## Sales Orders

| File | Description |
|---|---|
| BKICAPMA | Archive price code |
| ISESTAQT | Archive quote header |
| ISESTAQL | Archive quote lines |
| ISARAINV | Archived closed sales order headers |
| ISARAIVL | Archived closed sales order lines |
| ISARADSC | Archived closed sales order notes |
| ISSOAHBX | Archived invoice box allocation |
| ISARAHIN | Archived invoice headers |
| ISARAHIL | Archived invoice lines |
| ISSOALOT | Archived invoice lot control |
| ISARAHDS | Archived invoice notes |
| ISSOASER | Archived invoice serial control |
| ISARATXN | Archived lot link to invoice line |
| ISSRAINV | Archived sales order header |
| ISSRAIVL | Archived sales order line |
| ISARATXS | Archived serial link to invoice line |
| ISSOABOX | Archived shipping detail |
| ISARTXNB | Bin allocation to SO line |
| ISARCHG | Changes to sales orders |
| DISCOUNT | Discount table master |
| BKARHINV | Invoice header |
| BKARHIVL | Invoice line |
| BKSOHLOT | Invoice lot control |
| BKSOHSER | Invoice serial control |
| BKSOLOCK | Lock file for SO invoice posting |
| ISARHCHG | On-time delivery |
| BKICPMAT | Price matrix |
| BKARRINV | Recurring order header |
| BKARRIVL | Recurring order line |
| BKSAREPT | Report names for SA-M & SA-N |
| BKSONOTE | Sales order assigned templates |
| ISORDDSC | Sales order description list |
| BKARINV | Sales order header |
| BKARINVL | Sales order lines |
| ISSOINFO | Sales order supplemental info |
| BKESTQT | Sales quotation header |
| BKESTQTL | Sales quotation line items |
| ISQTCODE | Reason for quote loss |
| ISSOHBOX | Shipped box ID |
| ISSOBOX | Shipping detail |
| ISQTINFO | Supplemental quote info |
| ISQSOA | Temp file for quick SO entry |
| INVETXN | Temp file for unposted inventory transactions |
| BKARTXN | Unposted lot allocation to order lines |
| BKARTXNS | Unposted serial allocation to order lines |

## Scheduling

| File | Description |
|---|---|
| BUCKETS | Finite schedule buckets |
| SCHWO | Finite scheduling temp file |
| WCCTL | Finite scheduling temp file |
| SCHEDCAL | Scheduling shop calendar |
| CALENDAR | Shop calendar |
| WCTRSLOD | Temp work-center load % for Visual Scheduler |
| WORKSORD | Temp work order header for Visual Scheduler |
| WOSROUT | Temp work order routing for Visual Scheduler |

## Serial Control

| File | Description |
|---|---|
| SERIALH | Archived serial numbers |
| ISSERCNT | Serial number generation master |
| SERIAL | Serial number master |
| ISSERIAL | Serial component-to-parent map |
| ISLOTS | Lot component-to-serial parent map |

## Service & Repair

| File | Description |
|---|---|
| ISSRINV | S/R order header |
| ISSRINVL | S/R order lines |
| ISSRINFO | S/R supplemental info |

## System Manager

| File | Description |
|---|---|
| ISLOG | Active user list |
| ISCHAINM | Auto-chain program master |
| ISCHAIN | Auto-chain programs |
| ISNUMBER | Document counters |
| ISLINKS | Links |
| ISNTYPE | Note types |
| ISNOTES | Notes |
| ISREMIND | Reminders |
| ISJOB | Job master listing |
| ISSCHED | List of programs to run by EVO Scheduler |
| ISDLCK2 | Lock file for master default program |
| ISDLCK1 | Lock file for next-number program |
| ISDRILLM | Master drill-down file |
| ISEREM | Notifications |
| ISTERMS | Payment terms |
| DBAHLPID | Program-specific help reference |
| ISSHIPCO | Ship-via company |
| ISSHPVIA | Ship-via listing |
| BKSYMSTR | System default master file |
| BKYSMSTR | System default master file 2 |
| MKAHIST | System default master file 3 |
| CALTEMP | Temp file for generating shop calendar |
| LANGDICT | Translation master |
| ISTRIGRS | Triggers |

## Work Orders

| File | Description |
|---|---|
| WOROUTMP | Aggregate WO routings (temporary) |
| BKDCHLAB | Archived DC labor transactions |
| MTEXCHG | Extra charges |
| WOLABOR | Labor transactions |
| WOHLABOR | Labor transactions — archive |
| ISMACS | Machine schedule |
| WOMAT | Material transactions |
| WOHMAT | Material transactions — archive |
| OUTPROC | Outside processing transactions |
| OUTHPROC | Outside processing transactions — archive |
| ISWOTRAY | Paperless batch tracking |
| ISLSMAP | Paperless shop-floor batch tracker |
| ISQCMTHD | Paperless shop-floor test methods |
| ISQCSPEC | Paperless shop-floor test requirements |
| ISQCRSLT | Paperless shop-floor test results |
| BKDCLAB | Posted DC labor transactions |
| QCCODES | QC codes |
| SCRAP | Scrap codes |
| OPQCDESC | QC codes by serial number |
| BKSHORT | Temp file for shortage report |
| BKDCPLAB | Unposted DC labor transactions |
| WOBOMREM | WO bill of material remarks |
| WOBOMHRM | WO bill of material remarks — archive |
| WCTRLOAD | Work-center load % |
| WORKCTR | Work centers |
| WOBOM | Work order bill of material |
| WOHBOM | Work order bill of material — archive |
| WODATE | Work order dates |
| WOHDATE | Work order dates — archive |
| WOEXCHG | Work order extra charges |
| WOHEXCHG | Work order extra charges — archive |
| WORKORD | Work order header |
| WORKHORD | Work order header — archive |
| ISWOEX | Work order header 2 |
| ISWOPRIO | Work order priority master |
| WORECV | Work order receipts |
| WOHRECV | Work order receipts — archive |
| WOROUT | Work order routing |
| WOHROUT | Work order routing — archive |
| ISWOROEX | Work order routing adjunct file |

---

## Observations

- **Three-letter prefix conventions** match the TAS-era module
  prefixes documented in CLAUDE.md §4 — with an extra layer:
  - `BK*` — legacy DBA Manufacturing base tables (most core data).
  - `IS*` — newer "IS Tech" extensions added by the current vendor.
  - `MT*` — "multi" / supplemental tables (often "master 2", DI helpers).
  - `MK*` — cross-reference tables (e.g. `MKICLASS`, `MKECLASS`).
  - Module-root names (`CALENDAR`, `ROUTING`, `LOT`, `SERIAL`,
    `WORKORD`, `MACHINE`, `TOOL`, `CLASS`) — oldest, pre-prefix
    tables carried over from DBA.

- **Archive tables shadow active tables** — any `BK*` or `IS*` active
  table often has an `A` or `H` inserted to give the archive
  equivalent (`BKAPPO`/`BKAPAPO`, `WOROUT`/`WOHROUT`).

- **Temp files are still in the namespace** — `BKBMSUMM`, `BKBMAVAL`,
  `BKMRPSW`, `WCCTL`, `SCHWO`, `INVETXN`, `BKSOPO`, `BKWOPO`, etc.
  Expect these to be transient; don't rely on their contents being
  stable between program runs.

- **Some files are flagged "not used"** — e.g. `BKARSHIP` (ship-to
  customer master). Worth checking before assuming a table is
  authoritative.

- **This list is 2024.1-era.** If EVO is upgraded, re-run
  `python scripts/chm_to_md.py file_names.htm` against the newer CHM
  to diff.
