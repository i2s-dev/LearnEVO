import sys
sys.stdout.reconfigure(encoding='utf-8')

path = r'C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\HELP-RESOURCES.md'

block = r'''

---

## Pass 91 — J7 Customizations, EVO* Infrastructure, T6 IN-B, WBK/WTAS (2026-06-18)

### J7* Customization Suite — i2 Systems Customer-Specific Forms

All 41 J7* DFMs confirmed from Pass 91 analysis. The J7* namespace is i2 Systems' reserved prefix for customer-specific customizations layered on top of standard EvoERP.

#### J7 Form Index

| Form | Caption / Purpose | Key Fields |
|------|------------------|-----------|
| J7ABISHIPRPT | Lapco Fulfillment Report | from.cust, thru.cust, from/thru.orddte, from/thru.item |
| J7ADTNACHA | ACH (extended) | (unknown — empty DFM) |
| J7APPVEND | Approve Vendor | app.vend, from.vend, bkap.vendname, max.chk.amt |
| J7AUTOAPC | Auto Enter PO Invoices | from/thru.date, from/thru.vclass, from/thru.vend, Use.ARD, inv.date |
| J7BEFWEB | Web Export (legacy) | (unknown — empty DFM) |
| J7BEFWEBINV | Web Item Export (CSV/FTP) | ftp.FileName, from/thru.item, item.type, from/thru.class, PRT.ACTIVE, ftp.password/userName/hostName, WebItems.only, all.loc, on.so.days, incl.stock.qty, incl.bo, print.by.loc |
| J7CCPIC | PI-C Physical Count Tag Entry | CountDate, qtr, year, location, empno |
| J7CIWEB | CI Web (legacy) | (unknown) |
| J7CIWEBIMPORT | Web Order Import | auto.mode, use.imp.sonum, import.to.edi, bank.name, downloadfile, ftp.FileName/password/userName/hostName, add.kit.comps, imp.FileName |
| J7CJBUSAGE | Print Inventory Usage | from/thru.date/class/cat/item/cust, PRT.ACTIVE |
| J7CRSOW | Custom SO-W Report | sFROM/sTHRU.SONUM, from/thru.orddte/cust, sFROM/sTHRU.INVNUM, incl.backorders |
| J7DCMATLABELS | Print Mattress Labels (DC) | SCAN.WO, SCAN.EMP1, SCAN.EMP2, oper1, oper2, inp.serial |
| J7DCSSOE | Shipping Data Collection | inp.serial, SCAN.WO, sonum.char |
| J7DCSSOEVERIFY | Verify SO Lines (DC) | LINE.VPART, LINE.SHIP.QTY, LINE.ORDERQTY, LINE.DESC |
| J7EBSERIAL | Enter Serial Number | scan.serial, SERIAL.LIST |
| J7EIMDCREV | WO Labor DC Review | LAB.DATE, scan.wonum, scan.emp, scan.oper, MTWO.WIP.CODE/DESC, rshrs, lab.parts/scrapped/scrap.code, force.close, nojobs.dec, lab.setuphrs/runhrs/start/finish/wc |
| J7HHEBINC | Handheld Inventory Adjustment | inp.Serial (serial-based) |
| J7HHEBXFER | Handheld Transfer Inventory | inp.Serial, from→to location |
| J7HHEBXFERVERIFY | Handheld Verify Transfer | PART.ARRAY, SHIPQ.ARRAY, DESC.ARRAY |
| J7HHLITN | Enter Tracking Numbers | track.num, ship.co, frt.charge, BOX.ID |
| J7HHPTSSOE | Handheld Shipping (PTS) | scan.qty.char, item, WONUM, Lot.No, from.cust |
| J7HHPTSSOELABELS | Print Box Content Labels | RTM_NAME, MISC, from.box, thru.box, labelQty |
| J7HHPTSSOEVERIFY | Verify SO (handheld) | LINE.VBOX, LINE.VPART, LINE.VBOXQTY, LINE.VSONUM, LINE.VDESC, LINE.VWONUM, LINE.VLOT |
| J7HHRTSSOE | RT London Shipping | scan.qty.char, scan.item, truck.no, sload.num, sonum.char |
| J7I2SACH | ACH Export | CHKACT.TXT, from/thru.chknum, from/thru.chkdate, ach.filename, wells.id, date.format, delimiter, eff.date |
| J7I2SYSTEMSOOE | Custom SOOE Filter | from/thru.cust, from/thru.esd, from/thru.class/cat/cclass |
| J7LAPCOSO | Lapco Print Inventory Usage | from/thru.cust/item/class/cat, item.type, PRT.ACTIVE |
| J7MCDSAREPORT | Sales Analysis Report | from/thru.date, from/thru.cust, from/thru.cclass |
| J7MPIMPORTAR | Import AR | FileName |
| J7NMBINS | Bin Inquiry | item, BKIC.PROD.DESC, BKIC.PROD.UOH, MTIC.PROD.LOC |
| J7NMRTMPRINTER | RTM Printer Setup | rtm.printer, rtm.program, rtm.rtm; stores to IS.RTM.PROGRAM/RTM/PRINTER |
| J7PEDCB | Production Status (DC) | scan.wonum, MTWO.WIP.CODE/DESC, from.wc, SCAN.PARTS, SCAN.SCRAPPED, MAX.QTY, CUR.QTY |
| J7POAIMP | Import PO (legacy) | (unknown) |
| J7POAIMPLINES | Import PO Lines | imp.filename, sPONUM, BKAP.PO.VNDCOD, FIELD.NUMBER[1..8], date.format, incl.mfgs, incl.2nd.desc, incl.vend.part, incl.specs |
| J7PTRECPOLINE | Receive PO Line | BKAP.POL.PCODE/PQTY/PPRCE/PEXT, BKIC.PROD.DESC/NOTE, BKAP.PO.VNDCOD/VNDNME/NUM |
| J7PTWOKI | WO-K-J Sync | from/thru.item, excepts.only, sync.ip.wos, upd.wo.class, from/thru.wonum |
| J7SMJCT | Closed Job Cost Report | from/thru.orddte, item, sSONUM |
| J7SOAIMPLINES | Import SO Lines (multi-company) | company.code/name/path, sponum, vend.name/code, incl.mf.comps, CC_CODE/CC_NAME, imp.filename, sSONUM, BKAR.INV.CUSCOD/CUSNME, FIELD.NUMBER[1..6], date.format, incl.2nd.desc/specs |
| J7SYNCWOTOSO | Synchronize WO to SO | SO.PARENT, SO.LINENO, SO.CODE, SO.DESC, SO.PQTY/ESD/ASD; edit.esd/asd/sstart/sfin/ddate/pqty/sqty; MTWO.WIP.WOPRE/WOSUF; BKAR.INVL.PCODE/PDESC; issued.mat, cost.msg |
| J7TMCKANBAN | Kanban Orders | edit.item/rqty/price/pext, BKIC.PROD.RAMT, vend.code, BKAP.VENDNAME, dflt.loc, PACKING.SLIPNUM, BKAP.PO.ENTBY, po.subtot, INVC.NUMBER |
| J7WOLL | WO-L-L Label Printing | sfrom/sthru.oper, from/thru.comp, use.bom.qty, label.qty, scan.wonum, MTWO.WIP.CODE/DESC |

#### J7 Sub-System Highlights

**J7 ACH Export (J7I2SACH):** Exports AP checks to ACH format for bank transmission. Supports Wells Fargo ID field (`wells.id`), configurable effective date format, delimiter, and export filename. Input: check number range + check date range.

**J7 Web Import (J7CIWEBIMPORT):** Imports customer orders from web/FTP into EVO — either EDI module or open SO file. Supports: bank account for payment, kit component expansion, use-imported-SO-number option, and FTP auto-download. Fully unattended mode available.

**J7 Handheld Suite (J7HH*):** Six handheld scanner forms for warehouse operations:
- HHEBINC: Inventory adjustment by serial scan
- HHEBXFER: Inventory transfer by serial scan (from→to location)
- HHLITN: Enter tracking numbers (ship co + freight charge + box ID)
- HHPTSSOE: PTS shipping (item + qty + box + SO# + WO# + lot#)
- HHRTSSOE: RT London shipping (truck# + load# + SO# + customer)
- HHPTSSOELABELS: Print box content labels (RTM + box range + label qty)

**J7 Data Collection (J7DC*):** Mattress/WO manufacturing data collection:
- DCMATLABELS: Print mattress labels by scanning WO + serial + employee
- DCSSOE: Shipping scan (serial + WO → SO)
- DCSSOEVERIFY: Verify shipped SO lines (part, ship qty, order qty, desc)

**J7 WO Sync (J7SYNCWOTOSO):** Full bidirectional WO↔SO synchronization — shows original and edited values side-by-side for: ESD, actual ship date, scheduled start/finish, due date, promise date, WO qty, ship qty, qty complete, issued labor/material.

**J7 Kanban (J7TMCKANBAN):** Creates kanban replenishment orders. Entry per line: item, receive qty, price; reads BKIC.PROD.RAMT for reorder amount. Creates PO-like receipt against vendor with packing slip tracking.

---

### IS.RTM — Report/Program→Printer Assignment Table

Confirmed from J7NMRTMPRINTER.DFM (RTM Printer Setup):

| Field | Description |
|-------|-------------|
| IS.RTM.PROGRAM | Program name that runs the report |
| IS.RTM.RTM | RTM report template filename |
| IS.RTM.PRINTER | Assigned printer for this program/RTM combo |

Purpose: maps each EvoERP program+RTM pair to a specific printer, allowing per-report printer routing without changing Windows defaults.

---

### EVO* Infrastructure Suite

#### EvoCSI — Evo Master Inquiry

Universal cross-module inquiry launcher. Fields: `itemnum`, `custcode`, `sonum`, `invnum`, `Vendcode`, `ponum`, `porecp`, `wonum`, `wsuffix`. One form that can open any major record by code.

#### Evo Notes System (EVOENOTES / EvoNotes / EvoNotesARCH / EvoNotesPrt / EvoNotesRpt / EvoNoteSearch)

**IS.NOTE.* table fields confirmed from DFMs:**

| Field | Description |
|-------|-------------|
| IS.NOTE.CDATE | Creation date |
| IS.NOTE.CTIME | Creation time |
| IS.NOTE.CWHO | Created by (user) |
| IS.NOTE.EWHO | Entered by (may differ from created by) |
| IS.NOTE.TYPE | Note type code |
| IS.NOTE.PRIVATE | Private flag |
| IS.NOTE.CONTACT | Contact name |
| GEN.ID | Generic entity ID (48-char composite: entity type + key) |

Note archive/restore (EvoNotesARCH) filters: date, item, customer, vendor, user (cwho), SO, WO, invoice, PO, CM customer, note type. Supports bulk archive and bulk restore. Reports include/exclude by entity type (customer/vendor/item/WO/SO/PO).

**EvoNoteSearch:** Text search across note bodies — SearchString, matchcase, searchNotes (current/archived/both).

#### Evo Links System (EvoELinks) — IS.LNK.* Table

| Field | Description |
|-------|-------------|
| IS.LNK.DATE | Link creation date |
| IS.LNK.WHO | User who created link |
| IS.LNK.LINK | File path or URL |
| links.alert | Alert flag for this link |
| links.itm.alert | Item-level alert flag |
| is.lnk.private | Private/visible flag |
| is.lnk.sort | Sort number |
| is.lnk.global | Use global path # (1-10) |
| is.lnk.pcb[100] | Print checkboxes (up to 100 print destinations) |
| GlobalPath[1..10] | 10 configurable global base paths for relative links |

Print destinations (link checkboxes): Traveler, Estimate, PO, RFQ, Quote, Acknowledgement, Invoice, Packing Slip, SO line, IN line, and more. Each destination gets an independent enable/disable flag per link.

#### EvoFNO — Features & Options Configurator

Form suite: EvoFNO (main), EvoFNOPO/SO/WO (conversion progress), EvoFNOQty (qty/location entry).

ISFO.HDR.* fields confirmed from DFM: PARENT (item number), DESC, CUST, VEND, RFQ, STATUS, DATE.

Convert action: creates SO (SOCB), WO (WOCB), PO (POCB), New Item (NICB), Sales Quote (SQCB), or RFQ (RQCB) from an F&O configuration. CVTQty/CVTLoc/CVTCV/cvtdate are the conversion parameters.

#### Evo Business Status — Full Detail

EvoBS.DFM confirms the complete ISBSF field set (22 summary fields + detail sub-tables):

**ISBSF Sub-table: WO Detail (EvoBSWO)**

| Field | Description |
|-------|-------------|
| ISBSF.WOS.LAB | WO issues — labor |
| ISBSF.WOS.MAT | WO issues — materials + process |
| ISBSF.WOS.FOH | WO issues — fixed overhead |
| ISBSF.WOS.VOH | WO issues — variable overhead |
| ISBSF.WOS.MEXT | WO issues — misc extra |
| ISBSF.WOS.FP | WO finished production value |
| ISBSF.WOS.WIPV | WO WIP variance |

**ISBSF Sub-table: Cash Detail (EvoBSCash)**

ISBSF.CASH.TOTA (total) + ISBSF.CASH.ACT1 through ACT9 (up to 9 bank accounts).

**EVOBSR** — Business Status Rebuild: regenerates the ISBSF snapshot from live transaction files.

#### EvoScheduler — IS.SCHED.* Table

Full IS.SCHED.* field set confirmed from EvoScheduler.DFM:

| Field | Description |
|-------|-------------|
| IS.SCHED.NAME | Job name (PK) |
| IS.SCHED.DESC | Description |
| IS.SCHED.PROG | Program to execute |
| IS.SCHED.PARAM1..8 | Up to 8 command-line parameters |
| IS.SCHED.LOG | Log file path |
| IS.SCHED.TYPE | Occurrence type (once/weekly/etc.) |
| IS.SCHED.DATE | Next run date |
| IS.SCHED.TIME | Next run time |
| IS.SCHED.RECUR | Recur every N minutes |
| IS.SCHED.LDATE | Last run date |
| IS.SCHED.LTIME | Last run time |
| IS.SCHED.CO | Company code |
| IS.SCHED.EMAIL | Email address for completion notification |
| IS.SCHED.WHO | Operator/owner |

EvoSchedsetup: creates Windows service wrapper. Prompts for server path (g:\path format), SMTP/user/pass/email/name settings, and 32-bit vs 64-bit OS selection.

evoERPsched: simpler scheduler with day-of-week checkboxes (Mon-Sun), run-once vs. weekly mode, and execution time.

#### Evo Reminders — IS.REM.* Table

IS.REM.DATE, IS.REM.TIME, IS.REM.SUBJECT, IS.REM.TYPE, IS.REM.CO, IS.REM.DISP (dismissed).

dayrem.DFM (Day Time Reminders) full fields: TIMES, SUBJECTS, rem.time/sub/item/cust/vend/file, remmin (remind X minutes before), IS.REM.DISP, rem.date/type/contact/phone/femail, REM.EMAIL, other.user, Outlook/Email reminder flags.

#### evoCSR — Calendar Summary Report

Filter fields: month, cust.from/thru, Item.from/thru, ESD (estimated ship date), CDD (customer due date), ENTRY.DATE. Display options: custpo (customer+PO#), qtybo (qty+backorder), socust (SO#+customer).

#### EvoDCmenu — Data Collection Menu

Two variants: EvoDCmenu (9 configurable program buttons, main/settings/about), EvoDCmenu2 (simplified). EvoDCsetup: workstation setup — server path and date format (dd/mm/yy or mm/dd/yy).

#### EVOFILTERS — Compound Filter Form

Multi-entity filter dialog. Supports simultaneous filters across:
- WO: num, finished date, status, start date, machine, work center, scrap code, employee, sequence, actual finish date, due date, class, priority
- JC: job number, labor date, tool, dept, rework code, divide hrs by jobs flag
- SO: SO num, invoice num, order date, est ship date

#### EVOERPUPDW — Archive Work Orders

Bulk WO archive by date (`wa.date`). Archives closed WOs to history.

---

### T6 IN-B — Legacy Inventory Entry (10-Tab Form)

The T6 era "IN-B Enter Inventory" form is split across 10 DFMs, each a tab in a multi-page entry screen:

| Tab DFM | Tab Name | Key Tables/Fields |
|---------|----------|------------------|
| T6EVOINB / T6ISINB | Main | BKIC.PROD.CODE/DESC/NOTE/CLASS/CAT/TYPE, UM variants (BKIC.PROD.UM, MTIC.PROD.SUM/PUM), BKIC.PROD.RLVL/RAMT, MTIC.PROD.LEAD/PCONV/CUBFT/STDPK/FRT%/LOC, reorder, warehouse/lot/serial control, ROHS, UPC, approved vendors |
| T6ISINB2 | Compact main | Subset: code/desc/class/cat/type/status + Sources + Links tabs only |
| T6ISINBECO | ECO | IS.ECO.REVLVL, IS.ECO.DRAW, IS.ECO.ENTDATE, IS.ECO.DATE, IS.ECO.ENTBY, IS.ECO.ECO, IS.ECO.CURRENT |
| T6ISINBLNK | Item Links | I.ORDER, I.LINK, I.OTHER, I.ILOLINK, I.GPATH; IMAGE.TL[1..10] (thumbnails); IMAGE.PCB[1..10] (print checkboxes) |
| T6ISINBMFG | Manufacturer | BKSB.MFG.MPART, BKSB.MFG.MANUF |
| T6ISINBMRP | MRP Settings | MTIC.PROD.MRP, MTIC.PROD.MRPSW, BKIC.PROD.RLVL/RAMT, MTIC.PROD.LEAD/EXPBF/DELBF/WIPDP |
| T6ISINBSPC | Specifications | MTIC.PROD.SPECS[1..12] |
| T6ISINBVND | Vendor Sources | BKSB.VEND.VEND, BKAP.VENDNAME, BKSB.VEND.VPART |
| T6ISSTDCST | Standard Cost | MTIC.PROD.RCOST[1..14], MTIC.PROD.LOTSZ, BKIC.PROD.LSTC/AVGC |
| T6EVOART | Credit Card | BKCM.ACCT.CODE/NAME/ADD1-3/CITY/STATE/ZIP/CCARD/CNUM/CMPNM/PNAME/CEXP |

#### IS.ECO — Engineering Change Order Table

| Field | Description |
|-------|-------------|
| IS.ECO.REVLVL | Revision level (current) |
| IS.ECO.DRAW | Drawing number |
| IS.ECO.ENTDATE | Entry date |
| IS.ECO.DATE | ECO effective date |
| IS.ECO.ENTBY | Entered by |
| IS.ECO.ECO | ECO number |
| IS.ECO.CURRENT | Current revision flag |

#### BKSB Tables — Sub-contractor / Cross-Reference

| Table | Fields | Purpose |
|-------|--------|---------|
| BKSB.MFG | MPART (mfg part#), MANUF (manufacturer) | Approved manufacturer cross-reference per item |
| BKSB.VEND | VEND (vendor code), BKAP.VENDNAME (name), VPART (vendor's part#) | Approved vendor cross-reference per item |

#### Standard Cost Structure — MTIC.PROD.RCOST[1..14]

From T6ISSTDCST.DFM captions, the 14 cost array slots map to:

| Slot(s) | Cost Element | Level |
|---------|-------------|-------|
| [1] | Labor | This level |
| [2] | Variable overhead | This level |
| [3] | Setup | This level |
| [4] | Outside process | This level |
| [5] | Freight | This level |
| [6] | Material | This level |
| [7] | Labor | Rolled-up (all levels) |
| [8] | Material + freight | Rolled-up |
| [9] | Setup | Rolled-up |
| [10] | Labor (duplicate rolled) | Rolled-up |
| [11] | Outside process | Rolled-up |
| [12] | Fixed overhead | Rolled-up |
| [13] | Variable overhead | Rolled-up |
| [14] | Fixed overhead | This level |

Standard Cost = sum of this-level slots; Rolled-up Cost = sum across all BOM levels.

#### MTIC.PROD.SPECS[1..12] — Item Specifications

12-element string array storing up to 12 free-text specification lines per item (from T6ISINBSPC tab).

#### BKCM.ACCT — Credit Card Account Table

From T6EVOART.DFM (part of IN-B):

| Field | Description |
|-------|-------------|
| BKCM.ACCT.CODE | Account code (PK) |
| BKCM.ACCT.NAME | Account name |
| BKCM.ACCT.ADD1..3 | Address lines 1-3 |
| BKCM.ACCT.CITY | City |
| BKCM.ACCT.STATE | State |
| BKCM.ACCT.ZIP | ZIP code |
| BKCM.ACCT.CCARD | Card type |
| BKCM.ACCT.CNUM | Card number |
| BKCM.ACCT.CMPNM | Company name on card |
| BKCM.ACCT.PNAME | Person name on card |
| BKCM.ACCT.CEXP | Card expiration date |

---

### WBK* — Web Interface / Lookup Framework

#### WBKLOOKUP — Evo Lookups (Main List-Picker Widget)

The universal lookup list widget used throughout EvoERP. Full feature set confirmed:

- cbIndexName: sort/index selection
- link.to, Drill.To: drill-down destination
- showgrid / Filter.to: grid display mode + filter
- SSSFD: sub-string search within list
- Built-in tools: Camera (image capture), CalcTot (column total), doc_print, Manager, External Call, Triggers, openclose, Alternate, Memo, arch (archive view)
- Sort options: Vendors Number, Manufacturers, Customers X-Ref
- Tag/untag functions (Tag, Untag, Invert Tag)
- Check mode for multi-select

#### WBKMENUSETUP — Menu Item Setup

Manages EvoERP menu structure. Key tables/fields:

| Field | Description |
|-------|-------------|
| BUTTON_CAPTION | Button caption text |
| BUTTON_IMAGE | Button image file |
| BUTTON_NUM | Button number |
| ACCESS_CODE | Security access code |
| GROUP_CAPTION | Group caption |
| GROUP_NUM | Group number |
| MI_MENU_LVL | Menu level |
| MI_CAPTION | Menu item caption |
| MI_FASTSELECT | Fast-select key |
| MI_PROGRAMNAME | Program to launch |
| MI_IMAGE | Menu item image |
| MI_LABEL | Menu item label |

Operations: Add User, Edit User, Delete User; Add Group, Delete Group, Move to Group; Copy From (copy menu setup); Update to Latest Programs; Clean Up (remove obsolete entries).

#### WBKLPRINT — Order Printing

Three checkboxes: Print Acknowledgements (pbox1), Print Packing Slips (pbox2), Print Invoices (pbox3).

---

### WTAS* — TAS Professional Data Administration Tools

#### WTASDATAM — Maintain Database (Raw Btrieve Browser)

Direct Btrieve file browser. Features: sort by index (cbIndexName), sequential scan (NoKey), record counter (rec_num/curr_rec_num), editing (GoEditing/edit mode), row add, row save, row delete, count/refresh, export visible/all rows. File location override (path_name). Deleted record counter. Displays field-configurable columns.

#### WTASDMGR — TAS Premier 7i Data Dictionary Manager

Full FD (File Descriptor) editor. Fields for each table definition:

| Category | Fields |
|----------|--------|
| Field list | FLD_LIST, FLD_LNAME, FLD_SNAME, FLD_TYPE, FLD_SIZE, FLD_DEC, FLD_ARRAY, FLD_UPCASE, FLD_DESC |
| Host type info | FLD_HTYPE, FLD_HSIZE, FLD_HDEC, FLD_HARRAY, FLD_HOFFSET |
| Key list | AKEY_LIST, AKEY_NAME, SEG_FLD_LIST, SEG_FLD_NAME |
| Key properties | knme (name), kord (order), kmod (modifiable), kdup (allow duplicates), kignore (ignore case), numSeg |
| File info | AFILE_NAME, AFILE_EXT, AFILE_TYPE, AFILE_PATH, AFILE_DESC |

Operations: Save FD, Close FD, Delete FD, Print FD, Create/Initialize File, Reindex Btrieve File, Reindex CodeBase File, Restructure File, Convert Btrieve→CodeBase, Entity Relationships diagram.

#### WTASINIT — Create/Initialize File

New file creation: CF_FLNAME (file name), CF_FLCODE (extension), CF_RTYPE (record type), CF_DESC, CF_PATH, cf_fdname (FD name to use as template).

---

### QC Buyoff Form — autoT7POJC (PO-J-C)

QC inspection/buyoff workflow triggered during PO receipt:

| Field | Description |
|-------|-------------|
| BKQC.QTY.RECVD | Quantity received |
| BKQC.QTY.BUYOFF | Quantity bought off to date |
| BKQC.QTY.REJECT | Quantity rejected to date |
| BUYOFF.REMAIN | Remaining qty to buyoff |
| BKQC.TRN.GQTY | This transaction — accepted qty |
| BKQC.TRN.BQTY | This transaction — rejected qty |
| BKQC.TRN.UQTY | This transaction — use-as-is qty |
| BKQC.TRN.SCRAP | This transaction — scrap qty |
| BKQC.TRN.REWORK | This transaction — rework qty |
| DEFAULT.BING | Default accepted qty bin |
| DEFAULT.BINU | Default use-as-is bin |
| BKQC.PKSLIP.NUM | Packing slip number |
| BKQC.VEND.CODE | Vendor code |
| BKQC.PROD.CODE | Item (product) code |
| BKQC.RECV.DATE | Received date |
| BKQC.PO.NUM | PO number |
| rohs | RoHS compliance flag |

---

### Calendar / Scheduling Infrastructure

**calDDsel** — Calendar Drill Down Type selector: DDTYPE (Est. Receipt Date = opt1, Vendor Promise Date = opt2).

**calrem** — Monthly calendar with drill-down, previous/today nav, Google Calendar export, and closed-WO filter.

**dayrem** — Day Time Reminders entry: TIMES/SUBJECTS list, rem.time/sub/item/cust/vend/file, remmin (minutes before reminder), IS.REM.DISP, rem.date/type/contact/phone/femail, REM.EMAIL, other.user. Can create Outlook reminders and email reminders. Reminder can be assigned to another user.

---

### Utility Forms Confirmed in Pass 91

| Form | Purpose |
|------|---------|
| SSS | Drill Filters (SSSVALUE, SSS1-6) |
| SSSFD | Sub-string search / Evo Notes search (SSSFDVALUE, SSSFD1-7) |
| DDFilters | Drill Down Filters (ANDOR, DBFIELD, OPER, FVALUE, sort_key_name) |
| GetFileName | Enter File dialog (filtname, localfile, serverfile) |
| GetAlphaGen | Generic single-field alpha entry (gagalpha / GAG Caption) |
| udfedit | UDF value editor (editudf) |
| GRIDPLAY | Quick grid inventory viewer (BKIC.PROD.UOH/CODE/DESC/CLASS) |
| ISCCREP | Credit Card Report (fromso/thruso) |
| autoT7POJC | QC Buyoff for PO receipts (see table above) |
| DFMALTS | Developer tool: set ALT keys for DFM forms (DFMName) |
| nzedefs | Email default settings (entAPATH, SubjectField, BCC, subject, body fields) |
| EMAILREL4 | SMTP email relay config (SMTP, Email, Name, Port) |
| ACT7SHKNOTE | WO Sequence Note (data collection: SCAN.WO, scan.oper, woro.note) |
| NUMEMP | # of Employees dialog (xnumemp) |
| dbamenu_LOGIN | Login form (unknown internals) |
| dbamenu_SELCOMP | Select Company form (unknown internals) |

---

### New Tables Summary — Pass 91

| Table | Key Fields | Purpose |
|-------|-----------|---------|
| IS.NOTE | IS_NOTE_ID (48), CDATE, CTIME, CWHO, EWHO, TYPE, PRIVATE, CONTACT | EvoNotes entity — CRM notes linked to any record |
| IS.LNK | DATE, WHO, LINK, SORT, GLOBAL, PCB[100] | Attachments/links per entity |
| IS.SCHED | NAME (PK), DESC, PROG, PARAM1-8, LOG, TYPE, DATE, TIME, RECUR, LDATE, LTIME, CO, EMAIL, WHO | Scheduler jobs |
| IS.REM | DATE, TIME, SUBJECT, TYPE, CO, DISP | User reminders |
| ISFO.HDR | PARENT, DESC, CUST, VEND, RFQ, STATUS, DATE | F&O header |
| IS.ECO | REVLVL, DRAW, ENTDATE, DATE, ENTBY, ECO, CURRENT | Engineering Change Orders |
| BKSB.MFG | MPART, MANUF | Approved manufacturer cross-ref |
| BKSB.VEND | VEND, VPART | Approved vendor cross-ref (per item) |
| BKCM.ACCT | CODE, NAME, ADD1-3, CITY, STATE, ZIP, CCARD, CNUM, CMPNM, PNAME, CEXP | Credit card accounts |
| BKQC | QTY.RECVD, QTY.BUYOFF, QTY.REJECT, TRN.GQTY/BQTY/UQTY/SCRAP/REWORK, PKSLIP.NUM, VEND.CODE, PROD.CODE, RECV.DATE, PO.NUM | QC inspection/buyoff |
| IS.RTM | PROGRAM, RTM, PRINTER | Report→printer routing |
| MTIC.PROD.SPECS[1..12] | (array) | Item specification lines |
| MTIC.PROD.RCOST[1..14] | (array) | Standard cost rollup (14 cost elements) |

'''

with open(path, 'a', encoding='utf-8') as f:
    f.write(block)

print(f'Appended {len(block)} chars to HELP-RESOURCES.md')
