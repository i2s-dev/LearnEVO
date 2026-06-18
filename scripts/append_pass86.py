import sys
sys.stdout.reconfigure(encoding='utf-8')

path = r'C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\HELP-RESOURCES.md'

content = r"""


---

## Pass 86 DFM Analysis (2026-06-18) -- DE/EDI full suite, EVO system tools, reminders, IM, RM, GF

### DE/EDI Module -- Full Import/Export Suite

The DE module handles ALL external data exchange. Much broader than "EDI" alone -- it covers file imports, web sync, and data utilities across all modules.

**T7DEER.DFM:** Error Report -- validates items against Estimating OR Production, prints only error records. PRT.BAD, zero.qtyreqd, est.prod flag.

**T7DEFECT.DFM:** Defect code master. Table `IS.DEF.*`: IS.DEF.CODE + IS.DEF.DESC.

**T7DEHD.DFM:** "PI-C Import Tags" -- imports physical inventory count tags FROM a file. YEAR+QTR (PI run ID), count.date, FIELD.NUMBER[1..9] positional mapping, comma.fixed, replace [S/R], x.by.stdpk (multiply qty by standard pack).

**T7DEJH.DFM:** "DE-J-H" -- WO materials issue import from file. WOMAT.WOPRE/WOSUF/PCODE/PDESC/QTYISSUED/DATE/LOT/REF. Imports WO issue transactions from scanners or external files.

**T7DEK.DFM:** "Replace all Values" -- global field find-and-replace in a Btrieve file. which.file, which.field, replace.all, search.for, replace.with. Data correction utility.

**T7DEL.DFM:** "Erase Files" -- bulk erase Inventory/BOM/Customer/Routings/Vendor/COA/Labor files. Data initialization utility.

**T7DEM.DFM:** BOM component import to Estimating OR Production. PRT.BAD, zero.qtyreqd, est.prod flag.

**T7DEP860.DFM:** "Import EDI 860" -- EDI 860 = Purchase Order Change. BKAR.INV.CUSCOD/CUSNME, RELEASE_NUM, CUSORD, SONUM.

**T7DEPB.DFM:** "Import EDI Orders" -- main EDI SO import (EDI 850). EDI Number, Customer, Release Number, Customer Order, Line Number. EDI pricing flag, reindex, PSV/Fixed format.

**T7DEPD.DFM:** "DE-P-D" -- create SOs from EDI orders. NEW.SO, ORDER.DATE, EST.DATE, LOC, CUST.PO. Quote fields (sFQUOTE.NUM, sTQUOTE.NUM) -- EDI quotes convert to SOs.

**T7DEPE.DFM:** "DE-P-E" -- EDI invoice export (EDI 810). BKAR.INV.NUM, BOL (Bill of Lading), DISTRIB (Distribution Center flag), ONE.FILE.PER.CUST. from/thru invoice#/customer range.

**T7DEPF.DFM:** Invoice export (PSV or fixed). FROM/THRU invoice#, include header, SO vs INV output type.

**T7DEPH.DFM:** "DE-P-H" -- SO data export (EDI 856 ASN). SO#, STDPCK (standard pack), CUSTPO, PRCE.

**T7DEQ.DFM:** AR invoice import from file. Invoice#, Customer, Date, Amount, Exchange Rate, Currency Code, Description, Terms#.

**T7DER.DFM:** AP invoice import from file. Same as DEQ + Taxes + Freight fields.

**T7DET.DFM:** "Web Import" -- FTP download to EDI or Open SO. auto.mode, bank account, add kit components, error check, skip.SO, send.reminder, rename.file, imp.price.

**T7DETB.DFM:** "DE-T-B" -- web import with extended options. EDI vs Open SO, drop shipment fee/default [YNG], include 2nd desc, include specs, import comments. FIELD.NUMBER[1..44] flexible positional mapping.

**T7DEU.DFM:** "Web Item Export" -- CSV/FTP export. item type [RFAMNLBTKO], class/active filters, FTP settings, adjust qty for SO within X days, web-items-only, all locations, include BO qty.

**T7DEV.DFM:** "POA Import" -- PO receipt import from file. Table `ISAP.QPO.*`: PONUM + PCODE + PQTY (queued PO receipt lines). Receipt date, packing slip#, employee#, rename.file.

**T7DEX.DFM:** Data dictionary field selector. MEM.SELECT.FLD/NUM, MEM.DICT_NAME/TYPE/SIZE/DEC/ARRAY. Reused by DE import screens to allow flexible user-defined positional field mapping.

DE module structure:

| Series | Purpose |
|---|---|
| P-series | EDI transactions (850/860/856/810) |
| D/H-series | Handheld/file data import (PI tags, WO materials) |
| J-series | WO materials/issue import |
| Q-series | AR invoice import |
| R-series | AP invoice import |
| T-series | Web order import (FTP) |
| U-series | Web item export (FTP/CSV) |
| V-series | POA (PO receipt) import |
| DEK/DEL | Data utilities (global replace, file erase) |

New tables: `IS.DEF.*` (defect codes: CODE+DESC), `ISAP.QPO.*` (queued PO receipt lines: PONUM+PCODE+PQTY). Confidence DE: 78->86.

---

### EVO System Infrastructure Tools

**EVOENOTES.DFM:** "Entering Notes" -- Evo Notes system. Table `IS.NOTE.*`: CDATE, CTIME, CWHO (created by), EWHO (assigned to), TYPE, PRIVATE, CONTACT. Notes linked to any EVO record type (item, customer, vendor, SO, WO, PO, invoice).

**EvoELinks.DFM:** "Entering Links" -- Evo Links/documents system. Table `IS.LNK.*`: DATE, WHO, LINK (path/URL), ALERT, PRIVATE, SORT, GLOBAL (use global path #), PCB[100] (print control bits per doc type). GlobalPath[1..10] = 10 configurable server base paths for document links. imageinfo.DFM shows GPS/EXIF data (lat/lon/date/time) is read from geo-tagged image attachments.

**EvoEMsg.DFM:** Broadcast message to another user (entMSG + sendwho). Inter-user messaging within EVO.

**EVOFILTERS.DFM:** Reusable WO/JC global filter panel. WO# range, WO finished/start/actual-fin/due dates, WO status, machine, work center, scrap code, employee, sequence#, JC job#/labor date, tool, department, WO class, WO priority [1-9].

**EvoCSI.DFM:** "Evo Master Inquiry" -- central cross-reference lookup. Enter any of: Customer Code, Item#, SO#, Invoice#, Vendor Code, PO Receipts, PO#, WO# to jump to that record.

**evoCSR.DFM:** "Calendar Summary Report" -- by month, customer/item range. ESD vs CDD view. Custom field display: Customer+PO# / Qty+BO / SO#+Customer.

**EvoERPDrillM.DFM:** "Drill Down Menus" editor. Table `DRILLM.*`: PARENT (parent grid field), CHILD, MENU (menu text), PFILE (parent file), FILE (child file), TField[1..5]/SField[1..5] (source/target field mappings). Configures custom drill-down navigation between any two data grids.

**EvoFNO.DFM:** Features & Options main form. Table `ISFO.HDR.*` confirmed: PARENT (item code), DESC, CUST, VEND, RFQ, STATUS, DATE. Converts to: SO, WO, PO, New Item, Sales Quote, RFQ via SOCB/WOCB/POCB/NICB/SQCB/RQCB conversion type flags.

**EvoNotesARCH/EvoNoteSearch/EvoNotesPrt/EvoNotesRpt:** Evo Notes management suite. Archive/restore notes by entity range. Search by string (matchcase, current/archived/both). Print by up to 6 note types. Report by date/entity range.

**EvoSchedsetup.DFM:** Installs Evo Scheduler as a Windows service. SMTP email config (SMTP/user/pass/email/name/port), 32/64-bit OS option.

**EvoMobilesetup.DFM:** Installs EvoMobile reminder service (same SMTP config).

**EVOSERVICESETUP.DFM:** Installs EvoService for the server (main background processing Windows service). SMTP email, 32/64-bit OS, security setting (email.cfg.sec + smtpport + esettings).

**EVOFUP.DFM:** Support tool -- uploads files to a technician (FUTECH picker, fu.name, fu.REmail, FU.ATTACH). Used for submitting bugs/logs to support.

**Evocnvtb.DFM:** "Synchronize Data Dictionary with Btrieve" -- syncs the TAS data dictionary with the actual Btrieve file structure.

**printtll.DFM:** Universal print dialog. Options: Printer/Preview/Email/File. Auto-email with contact name/number/primary code. dflt.printer, prt.file.type, fpath.

**Chart dialogs (chartBarModal/chartLineModal/ChartPieModal):** EVO has built-in charting. Bar (3 series with colors), line (2 series, 6 data points), pie (up to 10 slices). Used in Business Status and dashboard screens.

**EvoDCmenu.DFM:** Data Collection Menu -- touch-friendly DC menu with 9 configurable program buttons (Prog1-9).

**evoERPsched.DFM:** "Evo ERP Scheduler" -- schedule recurring tasks. Run once or weekly on specific days. stime + mon/tue/wed/thu/fri/sat/sun flags.

**EvoERPbackup.DFM:** "Evo Backups" -- creates ZIP archives. Full System / Company Data / Custom modes. zipfiles list, zipName, COMP.TAG/EXT/NAME.

New tables: `IS.NOTE.*` (Evo Notes), `IS.LNK.*` (Evo Links), `DRILLM.*` (drill-down menu config), `ISFO.HDR.*` (F&O header).

---

### Calendar / Reminders (RE module update)

**dayrem.DFM:** "Day Time Reminders" -- Evo Reminder entry/view. Table `IS.REM.*`:

| Field | Meaning |
|---|---|
| IS.REM.DISP | Dismissed/displayed flag |
| IS.REM.EMAIL | Email reminder flag |
| rem.date / rem.time | Reminder date and time |
| rem.type | Reminder type |
| rem.sub | Subject |
| rem.item / rem.cust / rem.vend | Linked entity |
| rem.file | File or URL attachment |
| rem.contact / rem.phone / rem.femail | Contact details |
| remmin | Minutes before event to alert |
| other.user | Assign reminder to another user |

Outlook calendar integration. Google Calendar export via CALREMGC (by date range, open/dismissed/all).

**T7RemindRpt.DFM:** "CM-B-D" -- Reminders report. By date/item/customer/type/user/vendor/company. Open/dismissed/both. Reminders vs Follow-Ups filter toggle.

**evorereminders.DFM:** Reschedule/snooze popup. remdate + remmin + remtime.

CALDRILL/caldrillbt/CALGRIDDRILL/calrem = calendar view screens (no data fields -- rendered from calendar data).

New table: `IS.REM.*`. Confidence RE: 75->83.

---

### IM/Multi-Currency Module (CORRECTION: not just Landed Cost)

**CORRECTION**: IM module is the full Multi-Currency module. ISIS prefix = currency system. Landed cost (duties/freight/customs) is one sub-component.

**T7IMB.DFM:** "IM-B" -- Currency master. Table `ISIS.MCF.*` (Multi-Currency Factor):

| Field | Meaning |
|---|---|
| ISIS.MCF.CODE | Currency code |
| ISIS.MCF.BASE | Is base currency flag |
| ISIS.MCF.SYMBOL / SYMPOS / DEC | Currency formatting |
| ISIS.MCF.GLAAP / GLDAP | AP control GL accounts (debit/credit) |
| ISIS.MCF.GLAAPX / GLDAPX | AP conversion gain/loss |
| ISIS.MCF.GLAAR / GLDAR | AR control GL accounts |
| ISIS.MCF.GLAARX / GLDARX | AR conversion gain/loss |
| ISIS.MCF.GLAPO / GLDPO | PO control GL accounts |
| ISIS.MCF.GLAPOX / GLDPOX | PO conversion gain/loss |
| ISIS.MCF.GLACS | Commission account |
| ISIS.MCF.INTRES / INTDAY | Interest rate + days |

**T7IMC.DFM:** Exchange rates. `ISIS.MCR.*`: DATE + BASE (PK), SOURCE[1..10] (currency codes), RATE[1..10] (exchange rates). Up to 10 currencies per date record.

**T7IMD.DFM:** Landed cost GL accounts. `ISIS.LND.*`: GLADT/GLDDT (duty debit/credit), GLAFR/GLDFR (freight), GLACF/GLDCF (customs fees).

**T7IME.DFM:** Duty codes. `ISIS.DUTY.*`: DCODE + PERC (percentage rate).

**T7IMF.DFM:** Broker codes. `ISIS.BRK.*`: CODE + FLAT (flat fee) + PERC (percentage) + TYPE.

New tables: ISIS.MCF.* (currency master with 20+ GL accounts), ISIS.MCR.* (exchange rates: up to 10 currencies per date), ISIS.LND.* (landed cost GL), ISIS.DUTY.* (duty codes), ISIS.BRK.* (broker codes). Confidence IM: 78->88.

---

### RM/RMA Module (update)

**T7RMAWHY.DFM:** RMA Why -- SRMA.OINVNUM (original invoice#), SRMA.OSONUM (original SO#), IS.RMA.STATUS, reason/description/warranty/promise date. Warranty codes: N=None, L=Limited, P=Parts, B=Both.

**T7RMD.DFM:** "RM-D" -- Full RMA disposition. Receive qty/date/location. Disposition options:
- Issue Credit Memo: Create New CM or Add to Original SO
- Issue Replacement SO: New SO / Original SO / Add Both to Same New SO (and CM together)
- Issue Service and Repair Order: Add new line to original SR
- Return to: Stock, Rework, Repair, or Scrap (in-house or ship to customer)

**T7RMDASK.DFM:** Location/SO dialog. Pass RMA# to Desc/Job/None [D/J/N]. restock.charge. SO#, ESD, original/RMA/SO price comparison.

**T7RME.DFM:** "RM-E" -- RMA reason code master. Table `IS.RMA.*`: IS.RMA.CODE + IS.RMA.DESC.

**T7RMG.DFM:** "RM-G" -- RMA report. By customer/item/reason code/date/RMA#. Sort options, class/category range, incl.open.rmas flag.

New tables: `SRMA.*` (OINVNUM+OSONUM = original invoice/SO references for RMA), `IS.RMA.*` (reason code master: CODE+DESC). Confidence RM: 78->85.

---

### GF/AR Charges Module (update)

**t7GFdept / t7GFdiv:** Department and division code masters. Tables `IS.GF.DEPT` (DEPT+DESC) and `IS.GF.DIV` (DIV+DESC).

**T7GFV / T7GFVS:** AR charge entry/view. today, SO, ORDDATE, ESD, SHIPTO, SORTJ (sort by job), SORTG (sort by group), JOB. Charges linked to SO + job + dept/div.

New tables: IS.GF.DEPT, IS.GF.DIV. Confidence GF: 75->82.

---

### Additional Discoveries

**autoT7POJC.DFM:** PO QC buyoff at receiving. Extended BKQC.* fields confirmed: QTY.RECVD/BUYOFF/REJECT, TRN.GQTY/BQTY/UQTY/SCRAP/REWORK, PKSLIP.NUM. DEFAULT.BING/BINU = default bins for good/use-as-is disposition. rohs = RoHS compliance flag at PO receipt level. Confidence QC: 88->90.

**ht6* (T6 handheld programs):** ht6inc (PO receiving: item+qty), ht6so (create SO: PO#+item+desc+qty), ht6wo (monitor WO by up to 8 work centers: WCT/desc/sqty/eqty per station), ht6close (WO close confirmation).

**NascoPAYex.DFM:** "Export Payroll Data" -- exports to Nasco payroll format. pdate input. Nasco = third-party payroll processing vendor integration.

**nzedefs / nzemailtll:** Evo Email system. nzedefs = email defaults (SMTP path, attachment, signature, body text, BCC self, subject template, field substitution). nzemailtll = full email compose: To/CC/BCC/ICC (internal CC), subject, form, attachment, EMAILLIST/CONTNAME/ICCLIST.

**SSS.DFM:** "Drill Filters" quick popup -- SSSVALUE + SSS1-6 (6 quick filter slots used by drill-down grids).

**SSSFD.DFM:** "Sub String Search" -- 7-slot substring search for Evo Notes (SSSFD1-7).

**ACT7SHKNOTE.DFM:** Add note to WO sequence operation (SCAN.WO, scan.oper, woro.note). Confirms per-operation note attachment on WO routing.

---

### New Table Summary -- Pass 86

| Table | Purpose | Source |
|---|---|---|
| `IS.NOTE.*` | Evo Notes (CDATE+CTIME+CWHO+EWHO+TYPE+PRIVATE+CONTACT) | EVOENOTES |
| `IS.LNK.*` | Evo Links/documents (DATE+WHO+LINK+ALERT+PCB[100]+GlobalPath[10]) | EvoELinks |
| `IS.REM.*` | Evo Reminders (DATE+TIME+SUB+TYPE+ENTITY+FILE+DISP+EMAIL) | dayrem |
| `DRILLM.*` | Drill-down menu config (PARENT+CHILD+MENU+PFILE+FILE) | EvoERPDrillM |
| `ISFO.HDR.*` | Features & Options header (PARENT+DESC+CUST+VEND+RFQ+STATUS+DATE) | EvoFNO |
| `ISIS.MCF.*` | Multi-currency master (CODE+BASE+SYMBOL+20+ GL accounts) | T7IMB |
| `ISIS.MCR.*` | Exchange rates (DATE+BASE+SOURCE[10]+RATE[10]) | T7IMC |
| `ISIS.LND.*` | Landed cost GL accounts (duty/freight/customs) | T7IMD |
| `ISIS.DUTY.*` | Duty code master (DCODE+PERC) | T7IME |
| `ISIS.BRK.*` | Customs broker master (CODE+FLAT+PERC+TYPE) | T7IMF |
| `IS.GF.DEPT` | GF department code (DEPT+DESC) | t7GFdept |
| `IS.GF.DIV` | GF division code (DIV+DESC) | t7GFdiv |
| `IS.DEF.*` | Defect code master (CODE+DESC) | T7DEFECT |
| `ISAP.QPO.*` | Queued PO receipt lines (PONUM+PCODE+PQTY) | T7DEV |
| `SRMA.*` | RMA original invoice/SO reference (OINVNUM+OSONUM) | T7RMAWHY |
| `IS.RMA.*` | RMA reason codes (CODE+DESC) | T7RME |

---

*Pass 86 complete (2026-06-18). 100 DFMs: T7DE* EDI full suite (20 programs), EVO system infrastructure (45), calendar/reminders (10), T7RM/RMA (5), T7IM/Multi-Currency (5), T7GF/AR Charges (5), ht6 T6 handheld (4), misc (10). Key correction: IM = Multi-Currency (ISIS.MCF/MCR/LND/DUTY/BRK), not just landed cost. Key new tables: IS.NOTE/LNK/REM (notes/links/reminders), DRILLM (drill-down config), ISFO.HDR (F&O header), full ISIS.* multi-currency system, IS.GF.DEPT/DIV, IS.DEF, ISAP.QPO, SRMA/IS.RMA. Confidence updates: DE 78->86, IM 78->88, RM 78->85, GF 75->82, FO 83->87, RE 75->83, Notes 72->82, QC 88->90, DC 87->89.*
"""

with open(path, 'a', encoding='utf-8') as f:
    f.write(content)
print('Pass 86 appended.')
