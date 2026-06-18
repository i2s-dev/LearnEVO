# EvoERP Data Dictionary — Tier 7 Tables (Pass 91–95 Findings)

Status: partial — fields extracted from DFM analysis (Passes 91–95).
Field names confirmed by DFM FieldName= attributes. Types/sizes inferred unless from DDF.

---

## MTWC — Work Center Master

**Purpose:** Defines each work center (machine cell / labor center) used in production
routing. MRP and Shop Scheduling read this to compute available capacity and scheduling
windows.

Primary key: MTWC.CODE (work center code)
Source: T7SHWCMAST.DFM, T7SHWCSREP.DFM

| Field | Type | Meaning |
|-------|------|---------|
| MTWC.CODE | STRING | Work center code (PK) |
| MTWC.DESC | STRING | Work center description |
| MTWC.TYPE | STRING | Type: M=Machine, L=Labor |
| MTWC.DEPT | STRING | Department code |
| MTWC.RATE | FLOAT | Machine/labor rate ($/hr) |
| MTWC.OVHD | FLOAT | Overhead rate ($/hr) |
| MTWC.EFF | FLOAT | Efficiency % (default run rate) |
| MTWC.UTIL | FLOAT | Utilization % (% of available time used) |
| MTWC.QUEUEM | FLOAT | Queue time (hours) before this WC |
| MTWC.MOVET | FLOAT | Move time (hours) after this WC |
| MTWC.CAP | FLOAT | Capacity (hours per shift) |
| MTWC.NSHIFT | INTEGER | Number of shifts per day |
| MTWC.MACH | INTEGER | Number of machines at this WC |
| MTWC.SCHED | STRING | Scheduling method code |
| MTWC.MAXQ | FLOAT | Maximum queue length |
| MTWC.INF | STRING | Infinite capacity flag |

**How it connects:** MTWORO.WC → MTWC.CODE (FK). MTWC drives capacity buckets in the
shop loading report (T7SHWCSREP) and forward/backward scheduling (T7SHSCHED-P).

**Confidence: 72/100** — Field names confirmed from DFMs; field types/sizes inferred.

---

## MTWORO — Work Order Routing Operations

**Purpose:** One row per operation step on a work order. Defines the sequence of
manufacturing steps, work centers, estimated and actual times, and completion status
for in-progress production.

Primary key: WO# + MTWORO.OPER (operation sequence)
Source: T7SHWORO.DFM, T7WORO.DFM, T7SHOPMAINT.DFM

| Field | Type | Meaning |
|-------|------|---------|
| MTWORO.WOPRE | STRING | WO prefix (PK part 1) |
| MTWORO.WOSUF | STRING | WO suffix (PK part 2) |
| MTWORO.OPER | INTEGER | Operation sequence number (PK part 3) |
| MTWORO.WC | STRING | Work center code → MTWC.CODE |
| MTWORO.DESC | STRING | Operation description |
| MTWORO.RUNSTD | FLOAT | Standard run time per unit (hours) |
| MTWORO.SETUPT | FLOAT | Standard setup time (hours) |
| MTWORO.ESTAT | STRING | Operation status (O=open, C=complete) |
| MTWORO.EDATE | DATE | Estimated completion date |
| MTWORO.ADATE | DATE | Actual completion date |
| MTWORO.ARUN | FLOAT | Actual run time accumulated |
| MTWORO.ASETUP | FLOAT | Actual setup time accumulated |
| MTWORO.QCOMP | FLOAT | Quantity completed at this operation |
| MTWORO.QSCRAP | FLOAT | Quantity scrapped at this operation |
| MTWORO.NOTE | STRING | Operation note |
| MTWORO.INSP | STRING | Inspection required flag |
| MTWORO.OUTSRC | STRING | Outsource/subcontract flag |
| MTWORO.OUTSRCVEND | STRING | Outsource vendor code |
| MTWORO.MACHINE | STRING | Specific machine assignment |
| MTWORO.EMP | STRING | Last employee to post labor here |
| MTWORO.CRATIO | FLOAT | Critical ratio (SWO.CRATIO — schedule urgency) |
| MTWORO.RUNDAYS | FLOAT | Scheduled run days remaining (SWO.RUN.DAYS) |

**How it connects:** Reads MTWC for capacity; written by Data Collection (DC) labor posting;
read by Shop Loading (SH) and Shop Dispatch (SH-A); drives critical ratio scheduling.

**Confidence: 70/100** — Core fields confirmed from multiple DFMs; exact PK structure
(prefix+suffix+oper) inferred from WO patterns across modules.

---

## IS.TRIG — Trigger / Notification Rules

**Purpose:** Defines automatic alert rules that fire when EvoERP detects specified
conditions (item below reorder, WO behind schedule, etc.). One row = one trigger rule.

Primary key: IS.TRIG.CODE
Source: T7ISTRIG.DFM (23 fields confirmed)
File: ISTRIG.B (or IS.TRIG.B depending on company)

| Field | Type | Meaning |
|-------|------|---------|
| IS.TRIG.CODE | STRING | Trigger code (PK) |
| IS.TRIG.CUST | STRING | Customer filter (blank = all) |
| IS.TRIG.VEND | STRING | Vendor filter |
| IS.TRIG.SO | STRING | SO# filter |
| IS.TRIG.PO | STRING | PO# filter |
| IS.TRIG.WOPRE | STRING | WO prefix filter |
| IS.TRIG.WOSUF | STRING | WO suffix filter |
| IS.TRIG.OPER | STRING | WO operation filter |
| IS.TRIG.CLASS | STRING | Item class filter |
| IS.TRIG.CAT | STRING | Item category filter |
| IS.TRIG.PLANNER | STRING | Planner code filter |
| IS.TRIG.BINLOC | STRING | Bin/location filter |
| IS.TRIG.ODEL | STRING | Overdue delivery flag |
| IS.TRIG.TRIGR | STRING | Trigger condition type code |
| IS.TRIG.ONCE | STRING | Fire once flag (suppress repeats) |
| IS.TRIG.LDATE | DATE | Last triggered date |
| IS.TRIG.LTIME | STRING | Last triggered time |
| IS.TRIG.NOTE | STRING | Trigger description / note |
| IS.TRIG.CONTACT | STRING | Contact to notify |
| IS.TRIG.EMAIL | STRING | Email address for notification |
| IS.TRIG.EFLAG | STRING | Email notification enabled flag |
| IS.TRIG.ITYPE | STRING | Item type filter |
| IS.TRIG.DAYS | INTEGER | Days-ahead or threshold value |

**How it connects:** The evoalerts system reads IS.TRIG rows to fire reminders and
emails. IS.TRIG.EMAIL + IS.TRIG.EFLAG drive the auto-email notifications.

**Confidence: 82/100** — All 23 fields confirmed by DFM FieldName= extraction.

---

## BKRFQ — RFQ Price Break Table

**Purpose:** Stores vendor quote price breaks for Request for Quote (RFQ) responses.
One row per vendor/item/quantity break.

Primary key: BKRFQ.EXP + BKRFQ.ISSUE (composite)
Source: T7POARFQ.DFM

| Field | Type | Meaning |
|-------|------|---------|
| BKRFQ.EXP | DATE | RFQ expiration date |
| BKRFQ.ISSUE | DATE | RFQ issue date |
| BKRFQ.QTY | FLOAT | Break quantity threshold |
| BKRFQ.COST | FLOAT | Unit cost at this break |
| BKRFQ.PROD | STRING | Item/product code |
| BKRFQ.LCDATE | DATE | Last change date |

**How it connects:** Written during RFQ response entry (PO-A module); read during PO
line entry to suggest pricing. Links to BKAPVEND (vendor) and BKICMSTR (item) by
context, not FK fields.

**Confidence: 78/100** — All 6 fields confirmed from DFM. PK structure inferred.

---

## BKICPMAT — Pricing Matrix

**Purpose:** Item/customer pricing rules with up to 10 quantity break levels per rule.
Used by SO entry to auto-populate price based on customer, item, quantity, and date.

Primary key: BKIC.PMAT.PCODE + BKIC.PMAT.SDATE (price code + effective date)
Source: T7GFPRICE.DFM (85 fields confirmed across 10 break levels)
File: BKICPMAT.B

| Field | Type | Meaning |
|-------|------|---------|
| BKIC.PMAT.PCODE | STRING | Price code (PK part 1) |
| BKIC.PMAT.SDATE | DATE | Effective start date (PK part 2) |
| BKIC.PMAT.EDATE | DATE | Expiration date |
| BKIC.PMAT.PFLAG | STRING | Price flag / type code |
| BKIC.PMAT.QTY[1-10] | FLOAT | Quantity break thresholds (10 slots) |
| BKIC.PMAT.RATE[1-10] | FLOAT | Price/rate at each break (10 slots) |
| BKIC.PMAT.PDESC[1-10] | STRING | Description label per break (10 slots) |

**Field count:** 4 header fields + 10×3 break fields = 34 named; 85 total (remaining
fields are additional break metadata not visible in the pricing popup DFM).

**How it connects:** BKAR.CUST.PCODE → BKICPMAT.PCODE; SO entry calls T7SOAPRC popup
to display breaks; item master may also reference a default PCODE.

**Confidence: 75/100** — Header + 3 break field types confirmed; 51 remaining fields
inferred as additional break slots or date/flag variants.

---

## BKAP.REM — AP Vendor Remittance Address

**Purpose:** Stores the "remit to" mailing address for AP vendors — separate from the
main vendor address on BKAPVEND. Allows payments to be sent to a lockbox or factor.

Primary key: Shares BKAPVEND PK (vendor code)
Source: T7APAENTRY.DFM (REM.* fields on vendor entry form)

| Field | Type | Meaning |
|-------|------|---------|
| BKAP.REM.ADDR1 | STRING | Remittance address line 1 |
| BKAP.REM.ADDR2 | STRING | Remittance address line 2 |
| BKAP.REM.CITY | STRING | Remittance city |
| BKAP.REM.STATE | STRING | Remittance state |
| BKAP.REM.ZIP | STRING | Remittance ZIP |
| BKAP.REM.CNTRY | STRING | Remittance country |

**Confidence: 65/100** — Fields confirmed from DFM labels; exact table name (embedded
in BKAPVEND or separate) not confirmed from DDF.

---

## TMC.Bank — AP Vendor Bank / ACH Fields

**Purpose:** Stores vendor bank account details for ACH/EFT payment processing.
Part of the BKAPVEND record (or a linked extension).

Primary key: Vendor code (shared with BKAPVEND)
Source: T7APAENTRY.DFM TMC.* fields

| Field | Type | Meaning |
|-------|------|---------|
| TMC.Bank | STRING | Bank name |
| TMC.Branch | STRING | Bank branch |
| TMC.AcctBase | STRING | Account number (base) |
| TMC.Suffix | STRING | Account suffix |
| bank.RoutNo | STRING | ABA routing number |

**How it connects:** AP check processing reads these to generate ACH payment files.

**Confidence: 68/100** — All 5 fields confirmed from DFM; whether stored in BKAPVEND
or a linked table (BKAPACK?) not confirmed.

---

## MTWO.WIP — Work Order Cost Accumulator

**Purpose:** Accumulates estimated and actual costs for work orders in progress.
One record per WO. Holds the financial snapshot of what a WO is expected to cost
vs. what has been charged so far.

Primary key: WO# (MTWO.WIP.WOPRE + MTWO.WIP.WOSUF)
Source: T7WOWIPCLC.DFM, T7WOWIP.DFM

**Estimated cost fields (9 confirmed):**

| Field | Meaning |
|-------|---------|
| MTWO.WIP.ESETUP | Estimated setup cost |
| MTWO.WIP.EMAT | Estimated material cost |
| MTWO.WIP.EOUTPR | Estimated outside processing cost |
| MTWO.WIP.ELABOR | Estimated labor cost |
| MTWO.WIP.EFOVHD | Estimated fixed overhead |
| MTWO.WIP.VOVHD | Estimated variable overhead |
| MTWO.WIP.EMISC | Estimated miscellaneous cost |
| MTWO.WIP.EEXTRA | Estimated extra cost |
| MTWO.WIP.ETOT | Estimated total cost |

**Actual cost fields (5 confirmed):**

| Field | Meaning |
|-------|---------|
| MTWO.WIP.ASETUP | Actual setup cost accumulated |
| MTWO.WIP.AMAT | Actual material cost accumulated |
| MTWO.WIP.AOUTPR | Actual outside processing cost |
| MTWO.WIP.ALABOR | Actual labor cost accumulated |
| MTWO.WIP.AFOVHD | Actual fixed overhead accumulated |

**Note:** Actual variable overhead, misc, and extra likely exist but not yet confirmed.

**Confidence: 73/100** — 14 confirmed fields; estimated vs. actual cost split verified.
Total field count for MTWO.WIP not confirmed from DDF.

---

## IS.SPC — Statistical Process Control Data

**Purpose:** Stores SPC measurement data collected during production. Each row is
one measurement event with up to 3 estimated values.

Primary key: Inferred composite (item + date/time + lot)
Source: T7ISMSPC.DFM

| Field | Type | Meaning |
|-------|------|---------|
| IS.SPC.CODE | STRING | Item/product code |
| IS.SPC.DATE | DATE | Measurement date |
| IS.SPC.TIME | STRING | Measurement time |
| IS.SPC.LOT | STRING | Lot number |
| IS.SPC.OPER | STRING | Operation or inspection point |
| IS.SPC.WHO | STRING | Employee who measured |
| IS.SPC.ESTE[1-3] | FLOAT | Estimated measurement values (3 slots) |
| IS.SPC.MEAS[1-n] | FLOAT | Actual measurement values (array) |
| IS.SPC.NOTE | STRING | Measurement note |

**Confidence: 62/100** — Core fields confirmed; IS.SPC.ESTE[3] confirmed as 3-slot
estimated array; full field count not extracted.

---

## IS.SERR — Serial Error / Non-Conformance

**Purpose:** Records serial-number-level non-conformances, defects, or scrap events
during production or QC inspection.

Primary key: Serial number + date (inferred)
Source: T7ISSERR.DFM

| Field | Type | Meaning |
|-------|------|---------|
| IS.SERR.SERN | STRING | Serial number |
| IS.SERR.CODE | STRING | Item/product code |
| IS.SERR.DATE | DATE | Error date |
| IS.SERR.OPER | STRING | Operation where error occurred |
| IS.SERR.TYPE | STRING | Error type code |
| IS.SERR.DESC | STRING | Error description |
| IS.SERR.DISP | STRING | Disposition code (rework/scrap/accept) |
| IS.SERR.WHO | STRING | Employee |
| IS.SERR.NOTE | STRING | Notes |

**Confidence: 60/100** — Field names inferred from DFM labels; exact field list not
fully extracted from DDF.

---

## IS.STRACK — Serial Number Genealogy / Tracking

**Purpose:** Tracks the genealogy and movement history of serialized items —
which serial numbers were built from which components, and where they went.

Primary key: Serial number
Source: T7ISSTRACK.DFM

| Field | Type | Meaning |
|-------|------|---------|
| IS.STRACK.SERN | STRING | Serial number (PK) |
| IS.STRACK.CODE | STRING | Item/product code |
| IS.STRACK.LOT | STRING | Lot number |
| IS.STRACK.WO | STRING | WO# that produced this serial |
| IS.STRACK.DATE | DATE | Build/receive date |
| IS.STRACK.CUST | STRING | Customer it shipped to |
| IS.STRACK.SO | STRING | SO# it shipped on |
| IS.STRACK.SHIP | DATE | Ship date |
| IS.STRACK.LOC | STRING | Current bin location |
| IS.STRACK.STAT | STRING | Status (in-stock / shipped / returned) |
| IS.STRACK.PARENT | STRING | Parent serial number (for sub-assemblies) |

**Confidence: 60/100** — Structure inferred from genealogy pattern; individual fields
confirmed from DFM labels but DDF extraction not done.

---

## DRILLM — Drill-Down Menu Configuration

**Purpose:** Configures the drill-down relationships between EvoERP records — e.g.,
from a WO you can drill to the SO that spawned it, or from an item to its usage history.
One row defines one parent→child navigation link.

Primary key: DRILLM.PARENT + DRILLM.CHILD (composite)
Source: EvoERPDrillM.DFM (10 confirmed fields)
File: DRILLM.B

| Field | Type | Meaning |
|-------|------|---------|
| DRILLM.PARENT | STRING | Parent record type / module code |
| DRILLM.CHILD | STRING | Child record type / module code |
| DRILLM.MENU | STRING | Menu option to invoke |
| DRILLM.PFILE | STRING | Parent file/table name |
| DRILLM.FILE | STRING | Child file/table name |
| DRILLM.TFIELD[1-5] | STRING | Target field names (5 slots — what to pass) |
| DRILLM.SFIELD[1-5] | STRING | Source field names (5 slots — where to get it) |

**How it connects:** At runtime, selecting a drill-down option passes SFIELD values
from the current record into the TFIELD positions of the child lookup. Enables
cross-module navigation without hard-coded links.

**Confidence: 80/100** — All 10+ fields confirmed from DFM FieldName= extraction;
exact record count in DRILLM.B not measured.

---

## IS.FIB — Field Information Base

**Purpose:** Associates EvoERP fields with metadata — which program class, group,
contract, user, and program own each configurable field. Used by the customization
and security framework to control field visibility and editability.

Primary key: IS.FIB.CLASS + IS.FIB.GROUP (composite inferred)
Source: T7FSFIB.DFM (5 confirmed fields)

| Field | Type | Meaning |
|-------|------|---------|
| IS.FIB.CLASS | STRING | Object class code |
| IS.FIB.GROUP | STRING | Field group code |
| IS.FIB.CONTRACT | STRING | Contract / module owner |
| IS.FIB.WHO | STRING | User who last changed |
| IS.FIB.PROGRAM | STRING | Program that owns this field definition |

**Confidence: 70/100** — All 5 fields confirmed; table size and full usage pattern
not yet traced.

---

## CFFLOC — EvoERP File Location Registry

**Purpose:** Maintains the registry of every data file (Btrieve .B table) used in
EvoERP — name, code, record type, description, and path. The authoritative list of
what tables exist in the system.

Primary key: CF_FLNAME (file/table name)
Source: WTASFLOC.DFM / WTASINIT.DFM (6 confirmed fields)
File: CFFLOC.B

| Field | Type | Meaning |
|-------|------|---------|
| CF_FLNAME | STRING | File / table name (PK) |
| CF_FLCODE | STRING | Short file code |
| CF_RTYPE | STRING | Record type identifier |
| CF_DESC | STRING | Human description |
| CF_PATH | STRING | File path on disk |
| cf_fdname | STRING | Field definition name (links to field dictionary) |

**Confidence: 75/100** — All 6 fields confirmed from DFM. This table is the internal
"file registry" — WTASINIT adds rows here when initializing a new data table.

---

## IS.CATM — Item Category Master

**Purpose:** Defines item category codes used to classify inventory items for
filtering, reporting, and CRM activity grouping.

Primary key: IS.CATM.CODE
Source: T7SMIF.DFM (2 fields confirmed)

| Field | Type | Meaning |
|-------|------|---------|
| IS.CATM.CODE | STRING | Category code (PK) |
| IS.CATM.DESC | STRING | Category description |

**Note:** Maintained under SM-I (T7SMIF). Affects both inventory classification and
CRM item categorization (referenced from BKCM activity records).

**Confidence: 72/100** — Both fields confirmed; additional metadata fields possible
but not confirmed.

---

## BKCM Code Tables — CRM Reference Data

Five small code tables maintained via the SM-I suite. All have the same 2-field
(code + description) pattern with minor extensions.

### BKCM.LEAD — Lead Source Codes (T7SMIA)

| Field | Meaning |
|-------|---------|
| BKCM.LEAD.SCODE | Lead source code (PK) |
| BKCM.LEAD.DESC | Description |

### BKCM.TERR — Territory Codes (T7SMIB)

| Field | Meaning |
|-------|---------|
| BKCM.TERR.TCODE | Territory code (PK) |
| BKCM.TERR.DESC | Description |
| BKCM.TERR.EMAIL | Routing email address for territory |

### BKCM.ACFC — Activity / Follow-Up Codes (T7SMIC)

| Field | Meaning |
|-------|---------|
| BKCM.ACFC.FCODE | Activity code (PK) |
| BKCM.ACFC.DESC | Description |
| BKCM.ACFC.REP | Rep assignment flag |
| BKCM.ACFC.DASH | CRM Dashboard inclusion flag |

### BKCM.DTCD — Document Type Codes (T7SMIE)

| Field | Meaning |
|-------|---------|
| BKCM.DTCD.DCODE | Document type code (PK) |
| BKCM.DTCD.DESC | Description |

### BKCM.ACCC — Account / Brand Codes (T7SMID / T7BRANDS)

| Field | Meaning |
|-------|---------|
| BKCM.ACCC.CCODE | Account/brand code (PK) |
| BKCM.ACCC.DESC | Description |

**Confidence: 82/100** — All fields confirmed from SM-I DFMs. BKCM.ACCC also appears
as T7BRANDS (brand code table under a separate menu path).

---

## ISSR.INFO — Sales / Service Request UDF Fields

**Purpose:** User-defined field extension table for both SO header records (via
T7SOHINFO) and SO line records (via T7SOINFO). The same table / schema is used for
both header-level and line-level UDFs on sales orders.

Primary key: ISSR.INFO.SRNUM (SO or SR number)
Source: T7SOHINFO.DFM (header) + T7SOINFO.DFM (line)

| Field | Type | Meaning |
|-------|------|---------|
| ISSR.INFO.SRNUM | STRING | SO or SR number (PK) |
| ISSR.INFO.DATE1 | DATE | User date field 1 |
| ISSR.INFO.DATE2 | DATE | User date field 2 |
| ISSR.INFO.DATE3 | DATE | User date field 3 |
| ISSR.INFO.DATE4 | DATE | User date field 4 |
| ISSR.INFO.DATE5 | DATE | User date field 5 |
| ISSR.INFO.AL1 | STRING | User alpha field 1 |
| … | … | … |
| ISSR.INFO.AL20 | STRING | User alpha field 20 |

**Total confirmed:** 26 fields (1 PK + 5 dates + 20 alpha).

**Key finding:** This same table is accessed at BOTH the SO header level (one row per
SO) and the SO line level (one row per line), distinguished by SRNUM format. There is
no separate "header UDF table" vs. "line UDF table" — the same ISSR.INFO schema serves
both roles.

**Confidence: 78/100** — Field names confirmed from both SOHINFO and SOINFO DFMs.
Exact mechanism for distinguishing header vs. line rows (SRNUM format) inferred.

---

## IS.REM — Reminder / Alert Records

**Purpose:** Stores user reminders that appear in the EvoERP calendar and alert system.
Reminders can be personal or cross-user, and can link to customers, vendors, items, and
other entities.

Primary key: Inferred (user + date + subject)
Source: evoreminders.DFM, dayrem.DFM

| Field | Type | Meaning |
|-------|------|---------|
| IS.REM.DATE | DATE | Reminder date |
| IS.REM.TIME | STRING | Reminder time |
| IS.REM.SUBJECT | STRING | Subject line |
| IS.REM.TYPE | STRING | Reminder type code |
| IS.REM.CO | STRING | Company code |
| IS.REM.DISP | STRING | Dismissed flag (Y = user dismissed) |
| rem.item | STRING | Linked item/product code |
| rem.cust | STRING | Linked customer code |
| rem.vend | STRING | Linked vendor code |
| rem.file | STRING | Linked file / URL |
| rem.contact | STRING | Contact name |
| rem.phone | STRING | Contact phone |
| rem.femail | STRING | Contact email |
| REM.EMAIL | STRING | Send email notification flag |
| other.user | STRING | Create reminder for a different user |

**Confidence: 70/100** — Fields confirmed from DFMs; IS.REM.* prefix names verified;
rem.* field prefix suggests a different namespace (possibly same table, aliased).

---

## BKAR.INV — AR Invoice / SO Summary Financial Fields

**Purpose:** The AR invoice header includes key financial summary fields that are
populated when an SO is invoiced or posted. These fields represent the top-level
financials on each invoice/SO.

Primary key: BKAR.INV.INVNUM
Source: T7SOA.DFM (confirmed Pass 95)

**Summary financial fields confirmed:**

| Field | Meaning |
|-------|---------|
| BKAR.INV.FRGHT | Freight amount |
| BKAR.INV.SUBTOT | Sub-total (pre-tax, pre-freight) |
| BKAR.INV.TAXAMT | Tax amount |
| BKAR.INV.TOTAL | Grand total |
| BKAR.INV.NL | Note line flag |

**Additional SO header fields confirmed:**

| Field | Meaning |
|-------|---------|
| sobookdate | Booking date for the SO |
| mem.group | Recurring SO group code |
| mem.freq | Recurring SO frequency |
| mem.max | Recurring SO max invoices |

**Confidence: 85/100** — All fields confirmed from T7SOA/T7SOJINFO DFMs. These
extend the BKARINV schema documented in tier1-tables.md.

---

## BKQC — QC Receiver Fields (Pass 95 additions)

**Purpose:** Extends the QC receive record documented in tier1-tables.md with
fields confirmed from autoT7POJC.DFM.

Additional confirmed fields:

| Field | Meaning |
|-------|---------|
| BKQC.RECV.DATE | QC receive date |
| BKAP.POL.WOSUF | WO suffix on PO line (links QC receipt to WO) |
| rohs | RoHS compliance flag (set on receipt) |

**Confidence: 78/100** — All 3 fields confirmed from autoT7POJC DFM.
