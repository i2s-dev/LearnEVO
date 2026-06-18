# Tier 10 — Previously Undocumented Table Families

Status: partial | Source: DDF field-name analysis (Pass 108)

Field meanings are inferred from names unless noted. All field lists extracted from
`samples/ddf/schema.json` (Pervasive PSQL DDF catalog confirmed 2026-06-16).

---

## MK* — Marketing Automation Tables (11 tables)

The MK module implements a **campaign management / drip-marketing system** built on top of
the CRM module (BKCM*). Campaigns are defined as "tracks" — ordered sequences of "events"
(mailings, calls, samples) executed at scheduled intervals.

### MKTRACK — Marketing Track Master

**Purpose:** Defines a named marketing campaign track. One record per track.

| Field | Meaning |
|-------|---------|
| MKTRACK_NUM | Track number (PK) |
| MKTRACK_DESC | Track description / name |
| MKTRACK_CLASS | Track class code (links to MKTCLASS) |
| MKTRACK_ACTIVE | Active flag (Y/N) |

### MKTROUT — Track Routing (Event Sequence)

**Purpose:** Defines the ordered sequence of events within a track. 11 fields.

| Field | Meaning |
|-------|---------|
| MKTROUT_TRACK | Track number (FK → MKTRACK) |
| MKTROUT_SEQ | Sequence number within the track |
| MKTROUT_JUMP | Jump-to sequence on condition |
| MKTROUT_NEXTSEQ | Default next sequence |
| MKTROUT_EVENT | Event code (FK → MKEVENT) |
| MKTROUT_DAYSNXT | Days until next event fires |
| MKTROUT_FIXED | Fixed date flag |
| MKTROUT_SALEBEG | Trigger on sale begin |

### MKEVENT — Event Definition

**Purpose:** Defines a marketing event template (a specific mailing, call, or action). 12 fields.

| Field | Meaning |
|-------|---------|
| MKEVENT_NUM | Event number (PK) |
| MKEVENT_DESC | Event description |
| MKEVENT_CLASS | Event class (FK → MKECLASS) |
| MKEVENT_MEDIA | Media type (mail / email / phone / …) |
| MKEVENT_FORM | Form code (FK → MKFORM) |
| MKEVENT_FUCODE | Follow-up code |
| MKEVENT_REM1 | Reminder 1 text |
| MKEVENT_REM2 | Reminder 2 text |

### MKFORM — Marketing Form / Template

**Purpose:** Letter / email / brochure templates used in events. 6 fields.

| Field | Meaning |
|-------|---------|
| MKFORM_NUM | Form number (PK) |
| MKFORM_DESC | Form description |
| MKFORM_FILE | File path to the template document |
| MKFORM_ATT | Attachment path |
| MKFORM_MEDIA | Media type |
| MKFORM_ACTIVE | Active flag |

### MKASSIGN — Track-to-Account Assignment

**Purpose:** Links a marketing track to a specific CRM account. 6 fields.

| Field | Meaning |
|-------|---------|
| MKASSIGN_ACCT | Account code (FK → BKCMACCN) |
| MKASSIGN_TRACK | Track number (FK → MKTRACK) |
| MKASSIGN_NXTSEQ | Next sequence to execute |
| MKASSIGN_NXTDAT | Date of next event |
| MKASSIGN_SALEND | Sale end/close flag |
| MKASSIGN_PRCODE | Price code applied at sale |

### MKAHIST — Account Marketing History

**Purpose:** Log of all marketing events executed against an account. 9 fields.

| Field | Meaning |
|-------|---------|
| MKAHIST_ACCT | Account code |
| MKAHIST_DATE | Date of contact |
| MKAHIST_TRACK | Track number |
| MKAHIST_SEQ | Sequence within track |
| MKAHIST_EVENT | Event code executed |
| MKAHIST_MEDIA | Media used |
| MKAHIST_FORM | Form used |
| MKAHIST_REM1 | Remark / notes |

### MKDEF — Marketing Module Defaults

**Purpose:** Module-level configuration. 11 fields including REQUIRE (required fields),
CALENDAR (calendar link), TRACK (default track), PRICECD (default price code),
FUCODE (follow-up code), HISTORYCD, TNEXTID (next track ID), TCNEXTID.

### Code tables (3 tables)

| Table | Fields | Purpose |
|-------|--------|---------|
| MKECLASS | 3 | Event class codes (NUM+DESC+ACTIVE) |
| MKTCLASS | 3 | Track class codes (NUM+CLASS+ACTIVE) |
| MKICLASS | 3 | Item class codes — same structure as MKECLASS |

### MKTNOTE — Track Notes

**Purpose:** Free-text notes attached to a track. 3 fields: MKTNOTE_TRACK + MKTNOTE_LINE + MKNOTE_TEXT.

---

## SUM* — Sales Analysis Report Summary Tables (4 tables)

Pre-aggregated monthly summary tables that back the SA (Sales Analysis) module's
top-N and margin reports. These are populated during SA report generation runs
rather than being real-time transactional tables.

| Table | Fields | PK | Purpose |
|-------|--------|----|---------|
| SUMCUST | 5 | CUST+YEAR+MONTH | Monthly sales dollars + COGS per customer |
| SUMINV | 19 | PARTNO+MONTH+YEAR+LOCATION | Inventory movement summary: adj/iss/rcv/beg/end by $ and unit count |
| SUMPNCUS | 6 | CUST+PARTNO+YEAR+MONTH | Monthly sales + COGS by customer + part number combination |
| SUMWC | 7 | WORKCTR+YEAR+MONTH | Work center performance: LABOR+SETUP+UNITS+SCRAP by month |

---

## ISAR* — AR Archive Tables (30 tables)

The ISAR* family stores **archived / historical copies** of the main AR tables after year-end
close or purge operations. The naming pattern is: IS + AR + A (archive) + suffix matching
the original table. Most ISAR tables mirror the exact field structure of their BK counterparts.

Key archive pairs:

| Archive table | Fields | Original | Purpose |
|---------------|--------|----------|---------|
| ISARAHIN | 84 | BKARINV | Archived AR invoice header |
| ISARAIVL | 28 | BKARINVL | Archived AR invoice lines |
| ISARACST | 106 | BKARCUST | Archived customer master snapshot |
| ISARAIVV | 77 | BKARINVV | Archived invoice variance/view |
| ISARAIVI | 16 | BKARINVI | Archived invoice index/image |
| ISARAINV | 84 | BKARINV | Alternate archive (2nd copy / pre-purge) |
| ISARAHTX | 5 | BKARHTAX | Archived invoice tax lines |
| ISARAINT | 23 | BKARINVT | Archived AR transaction |
| ISARACHK | 12 | BKARCHKH | Archived AR check header |
| ISARAT | 12 | BKART | Archived AR transaction record |
| ISARATNT | 3 | BKARTNOT | Archived AR transaction note |
| ISARATXN | 14 | BKARTXN | Archived inventory transaction from AR |
| ISARATXS | 14 | BKARTXNS | Alternate/secondary archive of BKARTXN |
| ISAREMND | 22 | ISREMIND | Archived reminders |
| ISAREX | 51 | ISAREX | Extended AR customer data (RS_EXPDT/UPDT/WHO/FORM fields — credit review dates) |
| ISARFQ | 49 | BKRFQ | Archived RFQ records |

Change log tables (all 26 fields, pattern: ISAR_CHG_SONUM+INVNUM+LINEID+PCODE+CDATE+USER):

| Table | Change context |
|-------|---------------|
| ISARACHG | AR change log (primary) |
| ISARCHG | AR header change log |
| ISARECHG | AR edit change log |
| ISARHCHG | AR history change log |
| ISARICHG | AR invoice change log |
| ISARMCHG | AR month-end change log |
| ISARQCHG | AR quote change log |
| ISARRCHG | AR recurring change log |
| ISARSCGH | AR schedule change log |

Other: ISARADSC/ISARAHDS (5f each — description text lines, BK_DESC_CODE+NUM+LINE+NOTES+DESC pattern),
ISARTXNB (23f — bin-level transaction detail: SONUM+CODE+LINEID+BIN+LOC+QTY).

**Pattern:** The ISAR* archive tables are bulk clones of existing BK*/IS* tables. They allow
the system to purge live tables for performance while keeping historical records accessible.

---

## BKAB* — License / Subscription Tables (2 tables)

The AB module (confirmed: License Manager) stores license keys and renewal dates.

| Table | Fields | Purpose |
|-------|--------|---------|
| BKABCUST | 5 | License dates — BKAB_START (start date), BKAB_EXP (expiry), BKAB_PERIOD (renewal period), BKAB_WARNING (days before expiry to warn), BKAB_STAND_ALNE (standalone flag — unlicensed or standalone mode) |
| BKABVEND | 2 | Registration — BKAB_SERIAL (license serial number), BKAB_REG_NAME (registered name) |

---

## ISAC* — Corrective Action Report (CAR) Tables (3 tables)

The ISAC* tables implement a **Corrective Action / Non-Conformance Report (NCR/CAR)** system.

| Table | Fields | Purpose |
|-------|--------|---------|
| ISACAR | 35 | CAR/NCR record — IS_NCR_NUM (PK), IS_NCR_PART, IS_NCR_COMP, IS_NCR_LOT, IS_NCR_SERIAL, IS_NCR_CDATE (created date), IS_NCR_WHO, IS_NCR_QTY — tracks nonconforming parts by part/lot/serial |
| ISACARFU | 13 | CAR follow-up actions — IS_CARFUP_CAR (FK→ISACAR), IS_CARFUP_DATE, IS_CARFUP_USER, IS_CARFUP_UID, IS_CARFUP_TYPE, IS_CARFUP_EXTRA, IS_CARFUP_CDTE, IS_CARFUP_CWHO |
| ISACTION | 3 | Action type codes — IS_ACTION_TYPE (PK), IS_ACTION_DESC, IS_ACTION_MISC |

---

## ISGL* — Extended GL Tables (6 tables)

These complement the main `BKGL*` tables with IS-module-specific GL data.

| Table | Fields | Purpose |
|-------|--------|---------|
| ISGLCOA | 67 | IS-enhanced Chart of Accounts — ISGL_ACCT+GLDPT (PK), +TYPE+CR_DR+NON_CASH — adds account type classification and non-cash flag to the base BKGLCOA |
| ISGLBDGT | 67 | Budget version of ISGLCOA — same structure, stores budget amounts instead of actuals |
| ISGLFCOA | 67 | Filtered/forecast COA — same structure, used for forecast scenarios |
| ISGLDATE | 86 | Fiscal calendar — ISGL_CYDATE_1..14 (14 period-end dates) plus historical dates — the 14-period fiscal year definition |
| ISGLHDAT | 86 | Historical ISGLDATE — prior-year fiscal calendar |
| ISGLNBGT | 35 | New/rolling budget — ISGL_BGT_ACCT+GLDPT (PK) + ISGL_BGT_BUDGET_1..14 (budget per period) |

**Key insight:** ISGLDATE (86f) and ISGLHDAT confirm the 14-period fiscal calendar. The 14 date fields define each period's close date, used for GL close validation and period-range reporting.

---

## WO History/Archive Tables (11 tables)

These are archived/historical versions of the main WO transaction tables.
The `WOH*` prefix = "WO History"; `WORO*` / `WORE*` = "WO Routing extended".

| Table | Fields | Mirrors | Purpose |
|-------|--------|---------|---------|
| WOHBOM | 24 | WOBOM | Archived WO bill-of-materials (issued component history) |
| WOHDATE | 13 | WODATE | Archived WO schedule dates (WOPRE+WOSUF+START+FINISH+QTY) |
| WOHEXCHG | 10 | WOEXCHG | Archived WO exchange/change transactions (MTWO_EX_* fields) |
| WOHLABOR | 58 | WOLABOR | Archived WO labor transactions (MTWOLA_* — largest: 58 fields) |
| WOHMAT | 17 | WOMAT | Archived WO material issues (WOMAT_DATE+WOPRE+WOSUF+QTYISSUED+QTYSCRAP+LOT+SERIAL) |
| WOHRECV | 11 | WORECV | Archived WO receipts (MTWOR_WOPRE+WOSUF+DATE+ASSY+DESC+QTY) |
| WOHROUT | 81 | WOROUT | Archived WO routing operations (MTWORO_* — largest: 81 fields) |
| WOROUT | 81 | — | Current WO routing (live); same field set as WOHROUT |
| WOROUTMP | 81 | — | WO routing staging/temp (work area during routing edits) |
| WOROCHG | 24 | — | WO routing change log (WORO_CHG_WOPRE+WOSUF+PART+OPER+CDATE+USER+AOPER+DOPER) |
| WORECV | 11 | — | WO receipt (current live version) |

**Pattern:** WOHROUT/WOROUT/WOROUTMP all have identical 81-field MTWORO_* schemas — the routing table is complex (81 fields) because it stores per-operation setup/run times, labor codes, work center assignments, machine assignments, tool lists, and standard costs.

---

## ISSE* — Service/Serial Equipment Tables (10 tables)

These tables support the SE (Service Equipment) module — managing field service contracts,
equipment serial numbers, and service history for sold equipment.

| Table | Fields | Purpose |
|-------|--------|---------|
| ISSESH | 84 | Service invoice header history — clone of BKARINV (84 BKAR_INV_* fields). Stores historical service invoices. |
| ISSEDH | 84 | Service invoice header draft — same BKAR_INV_* structure, pre-posted. |
| ISSESL | 28 | Service invoice line history — clone of BKARINVL (BKAR_INVL_* fields). |
| ISSEDL | 28 | Service invoice line draft — same BKAR_INVL_* structure. |
| ISSERIAL | 11 | WO serial assembly tracking — IS_SER_WOPRE+WOSUF+PARENT+PDESC+PSERIAL+ADATE+COMP+CDESC — maps assembled serial numbers from sub-assembly WOs to parent WO |
| ISSERR | 14 | WO serial error log — IS_SERR_WOPRE+WOSUF+OPER+TIME+DATE+ERROR+PROCESS+COUNT — serial scan failures and errors during WO scanning |
| ISSERCNT | 9 | Serial count config — IS_SERC_ITEM+CLASS+SPOS+LENG+TOTAL+NUMBER+LAST+EXTRA — controls serial number generation format (start position, length, etc.) |
| ISSEQUIP | 2 | Equipment master — IS_SEQUIP_NAME+IS_SEQUIP_DESC — simple equipment name/description catalog |
| ISSEPROC | 2 | Service process log — IS_SEPROC_PROC+IS_SEPROC_WHO — records which service process ran and who ran it |
| ISSETYPE | 2 | Service error type — IS_SETYPE_ERR+IS_SETYPE_WHO — error type code catalog |

**Key insight:** ISSESH/ISSEDH and ISSESL/ISSEDL mirror BKARINV/BKARINVL exactly — the service module reuses the AR invoice structure for service billing, with history vs. draft variants. ISSERIAL (11f) is the component-serial → parent-serial assembly linkage table used during WO completion scanning.
