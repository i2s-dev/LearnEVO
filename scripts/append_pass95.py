import sys
sys.stdout.reconfigure(encoding='utf-8')

path = r'C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\HELP-RESOURCES.md'

block = r'''

---

## Pass 95 — SOA/EVO-infra/WTAS/WBK/SM-IJ/CAL DFM sweep (2026-06-18)

### SO — Additional Header and Line Fields (T7SOA / t7Soa2)

**BKAR.INV additional fields confirmed from T7SOA:**

| Field | Description |
|-------|-------------|
| BKAR.INV.FRGHT | Freight amount on SO/invoice |
| BKAR.INV.SUBTOT | Sub-total (before tax + freight) |
| BKAR.INV.TAXAMT | Tax amount |
| BKAR.INV.TOTAL | Grand total |
| BKAR.INV.NL | Note line flag |
| sobookdate | Booking date for the SO |

**SO Line arrays (t7Soa2 line.prod.* — display buffer index up to 5001):**

| Field | Description |
|-------|-------------|
| line.prod.NUM[n] | Line number |
| line.prod.CODE[n] | Item code |
| line.prod.DESC[n] | Item description |
| line.prod.QTY[n] | Ordered quantity |
| line.prod.UBO[n] | Unit backorder quantity |
| line.prod.PRCE[n] | Price |
| line.prod.UM[n] | Unit of measure |
| line.prod.DISC[n] | Discount percentage |
| line.prod.ESD[n] | Estimated ship date |
| line.prod.ASD[n] | Actual ship date |
| line.prod.TAX[n] | Line taxable flag |
| line.prod.RTS[n] | Return to stock flag |
| line.prod.STAT[n] | Line status |
| line.prod.LONGP[n] | Long product description flag |
| line.prod.HIDE[n] | Hidden line flag |
| line.prod.IPEXT[n] | In-progress extension |
| line.prod.OQTY[n] | Original quantity |
| line.prod.FATD[n] | Fill at time of dispatch flag |
| line.prod.UPCHG[n] | Upgrade charge |
| line.wt | Single line weight |
| tot.line.wt | Total order weight |

**T7SOABKD — Booking Date:** sobookdate — popup to enter/change the SO booking date.

**T7SOAFRT — Freight Entry:** bkar.inv.frght — popup to enter freight amount on SO.

**T7SOAIMPLINES — Import SO Lines (7-column mapping):**
FIELD.NUMBER[1-7] = item code / description / quantity / price / ESD / comment / location.
Also: company.code/path (source ERP company for inter-company imports), sponum (source PO),
vend.code/name, incl.kit (include kit components), skip.zero.qty, incl.2nd.desc,
incl.specs, imp.comments, date.format (MM/DD/YY or DD/MM/YY).

**T7SOAPRC — SO Pricing Popup:**
BKIC.PMAT.QTY + BKIC.PMAT.RATE + BKIC.PMAT.PDESC — shows tiered pricing from the
pricing matrix (BKICPMAT) when entering SO lines.

**T7SOAXCOM — Extra SO Commission Override:**
Per-SO commission overrides beyond the customer default:
seREP (rep code), Empname (employee name), ecommp (commission %), eoveramt (overage amount),
eoverp (overage %). Arrays: LABEL, REP, VCOMMP, OVERAMT, OVERP — one row per extra commission.

**T7SOINFO / T7SOHINFO — Sales UDF (ISSR.INFO):**
Both the line-level (SOINFO) and header-level (SOHINFO) UDF forms use the SAME
ISSR.INFO table: ISSR.INFO.DATE1-5 (5 date UDFs) + ISSR.INFO.AL1-20 (20 alpha UDFs).
The ISSR.INFO.SRNUM PK links to the SO or SR number.

**T7SOJINFO — Recurring SO Info:**
mem.group (recurring group code), bkar.inv.invdte (invoice date), mem.freq (frequency),
mem.max (maximum invoices). Controls the recurring SO scheduling (group + frequency + limit).

---

### SM-I Suite — CRM Code Tables (T7SMIA through T7SMIF)

**All SM-I forms manage BKCM.* code tables:**

| Form | Table | PK Field | Fields |
|------|-------|----------|--------|
| T7SMIA | Lead Sources | BKCM.LEAD.SCODE | + DESC |
| T7SMIB | Territory Codes | BKCM.TERR.TCODE | + DESC + EMAIL |
| T7SMIC | Activity/History Codes | BKCM.ACFC.FCODE | + DESC + REP (rep flag) + dashboard toggle |
| T7SMID | Account/Category Codes | BKCM.ACCC.CCODE | + DESC (same as T7BRANDS) |
| T7SMIE | Document Type Codes | BKCM.DTCD.DCODE | + DESC |
| T7SMIF | Item Category Master | IS.CATM.CODE | + DESC |

**Key distinction:** IS.CATM is the item category master (under SM, affects inventory and CRM).
BKCM.ACFC is the CRM activity/history follow-up code with a CRM Dashboard inclusion flag.
BKCM.TERR includes an email address for territory routing.

---

### SM-J Suite — Archive and Purge Programs (T7SMJA through T7SMJH)

**Complete SM-J archive/purge program inventory:**

| Form | Purpose | Key Range Fields |
|------|---------|-----------------|
| T7SMJA | Inventory Reconciliation (report-only mode) | RPT.ONLY flag |
| T7SMJB | WO Archive/Restore/Purge | WO#, act.fin.date, job, cust, item; ARCH.CLOSE/CANCEL; orphan.woex |
| T7SMJC | Inventory Reconciliation | MASTER/TRANSACT levels, RSS (stock status report), METHOD, item/class, transdate |
| T7SMJD | Inventory Transaction Archive | Type [ASPJWIQOCMTRG], date range, consolidation date |
| T7SMJE | WO Purge (closed/cancelled) | PURGE.CLOSE/PURGE.CANCEL, WO range, act.fin.date range |
| T7SMJF | PO Archive | PO range, vendor range, date range |
| T7SMJG | QC Receiver Archive | arch.or.purge flag, date range, QC receiver# range, vendor range |
| T7SMJH | DC Data Collection Purge | CUT.DATE — purges all DC records before this date |

**T7SMJD Transaction Type codes [ASPJWIQOCMTRG]:**
A=AR, S=SO, P=PO, J=JC labor, W=WO, I=Inventory, Q=QC, O=overhead, C=cost adjustment,
M=MRP, T=transfer, R=return, G=GL.

---

### IS.REM — Reminder Table Additional Fields

evoreminders.DFM and dayrem.DFM confirm:

| Field | Description |
|-------|-------------|
| IS.REM.DATE | Reminder date |
| IS.REM.TIME | Reminder time |
| IS.REM.SUBJECT | Subject line |
| IS.REM.TYPE | Reminder type code |
| IS.REM.CO | Company code |
| IS.REM.DISP | Dismissed flag |

**dayrem additional fields:** rem.item (item#), rem.cust (customer), rem.vend (vendor),
rem.file (file/URL link), rem.contact/phone/femail (contact info), REM.EMAIL (email reminder flag),
other.user (create reminder for a different user — cross-user reminders).

---

### EvoFilters — Global Filter Form (EVOFILTERS.DFM)

The global filter form confirms the full range of JC/WO/SO filter fields used across
EvoERP reports and analysis screens:

**WO filters:** from/thru WO#, WO finished date, WO status, WO start date, machine, WC,
scrap code, employee, sequence range, WO act.fin.date, due date, WO class, WO priority [1-9].

**JC filters:** job range, labor date range, tool range, dept range, rework code range,
div.hrs (divide hours by number of jobs).

**SO/Invoice filters:** SO range, invoice range, order date range, ESD range, invoice date range,
cust order (customer PO) range, salesperson 1 + 2 ranges, job number range.

---

### EvoService / EvoScheduler Setup

**EVOSERVICESETUP.DFM** confirms EvoService installer settings:
email.cfg.SMTP/user/pass/Email/Name/sec (security), smtpport, esettings (email settings toggle),
thirtytwo/sixtyfour (OS bitness), file_name (server path).

**evoERPsched.DFM** confirms the ERP batch scheduler:
stime (schedule time), mon/tue/wed/thur/Fri/sat/sun (day toggles), runonce/weekly (frequency),
rtime (run-at time). Batch jobs can be scheduled on specific days of the week.

---

### WBK Menu System — Additional Fields Confirmed

**WBKLUGRID.DFM — Grid Lookup Editor:**
FD_COLHEADER (column header), FD_FIELDNAME (field name), FD_TOT (total flag), FD_FUNC (function),
FD_TYPE (field type), FD_SIZE (field size), LUGRID_END (start at end flag), SEC.LEVEL (security),
KD_COLHEADER/KEYNAME/FIELDNAME (key definition columns).

**WBKMENUBUTT.DFM — Button Setup:**
MI_BUTT_CAP (button caption), MI_BUTT_OPT (button option), MI_BUTT_NUMB (button number).

**WBKMENUSUEU.DFM — Menu Item Setup:**
GROUP_CAPTION/NUM, BUTTON_CAPTION/IMAGE/NUM, access_code, MI_MENU_LVL (menu level),
MI_CAPTION (caption), MI_FASTSELECT (quick key), MI_OLD_OPT/CAP/PRGNME (old menu values for migration).

**WBKMENUSUCPRG.DFM:** Change program name — FROM_PRG_NAME / TO_PRG_NAME (migration tool).
**WBKMENUSUNEWAC.DFM:** New access code — NewAC, ACCopyFrm (copy from existing code).

**WBKLPRINT.DFM:** Order printing options — pbox1 (Acknowledgements), pbox2 (Packing Slips),
pbox3 (Invoices). Three separate print jobs selectable per session.

---

### WTAS Additional Forms

**WTASFLOC / WTASINIT — File Location Table (CFFLOC):**

| Field | Description |
|-------|-------------|
| CF_FLNAME | File/table name |
| CF_FLCODE | File code |
| CF_RTYPE | Record type |
| CF_DESC | Description |
| CF_PATH | File path |
| cf_fdname | Field definition name |

WTASFLOC maintains this table; WTASINIT creates new entries (initializes new data files).
This is the EvoERP file registry — every data table in the system is registered here.

**WTASDMS2-5 — Auxiliary browser dialogs:**
- DMS2: Enter array elements (ARRAYCNTR)
- DMS3: Edit memo field
- DMS4: Enter filter expression (FilterExpr)
- DMS5: Enter find-next expression (FindFilterExpr)

---

### EvoERP Infrastructure — Other Findings

**EvoERPbackup.DFM — Backup System:**
zipfiles (file list), zipName (archive name), fullsystem/compdata/custom (backup scope toggles),
COMP.TAG/EXT/NAME (component list), CSTFILELIST (custom file list).
Three backup scopes: Full System, Company Data, or Customized file list.

**EVOERPUPDW.DFM — Archive Work Orders:**
wa.date — archives closed WOs to the WO history file as of this date.

**nzemailtll.DFM — Email Composer:**
entTO/CC/entICC (To/CC/BCC arrays), EMAILLIST/EMAILLBL (recipient list), CONTNAME,
bccself, TEMPATT (attachment), Email.cfg.subj (subject). Auto-email infrastructure
for sending invoices, reports, and notifications directly from EvoERP.

**printtll.DFM — Print Dialog:**
print_opt[1-4] = Printer / Preview / Email / File modes.
autoemail (auto-send to contact), contname/contnum/contprimcode (contact for email routing).
Confirms the four output modes available from any EvoERP print dialog.

**autoT7POJC.DFM — Auto QC Buyoff (PO-J-C):**
Confirms BKQC.RECV.DATE (receive date), BKAP.POL.WOSUF (WO suffix on PO line), rohs (RoHS
compliance flag on receipt). Automated version of the QC buyoff form for receiving.

**imageinfo.DFM — Image GPS Metadata:**
File.Name, Create.date/time, LatTXT/LONGTXT — reads GPS geolocation from image EXIF data.
Used in EvoLinks when attaching geotagged photos to records.

**SSS.DFM — Drill Filters:** SSSVALUE + SSS1-6 — 6-slot quick filter for drill-down queries.
**SSSFD.DFM — Sub-String Search:** SSSFDVALUE + SSSFD1-7 — 7-slot substring search across EvoNotes.

**ACT7SHKNOTE.DFM — Shackleton WO Note:**
SCAN.WO, scan.oper, woro.note — shop-floor WO operation note entry (third-party integration).

**NascoPAYex.DFM — Nasco Payroll Export:**
pdate — payroll export for a specific customer integration (Nasco brand).

**GetAlphaGen.DFM / GetFileName.DFM:**
Generic input dialogs used internally: alpha value prompt (gagalpha),
file name prompt with local/server toggle.

'''

with open(path, 'a', encoding='utf-8') as f:
    f.write(block)

print(f'Appended {len(block)} chars to HELP-RESOURCES.md')
