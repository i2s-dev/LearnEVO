# Tier 9 — Per-Table Narrative Docs (Java-Confirmed Schemas)

Status: partial | Source: EvoPVT.jar class file constant-pool extraction (Pass 102)

These tables have field schemas confirmed from Java model class files in
`samples/jar/extracted/com/evoerp/sql/tables/`. The field names are exact Pervasive column
names since they are used directly in JDBC PreparedStatement queries.

---

## BKLOGON — Active Login Sessions

**Module:** System (SY) | **PK:** BKLOGON_CODE | **Rows:** one per active EVO session

Stores the currently-logged-in user sessions. Keyed by user code. Used to track who is
active, what program they are running, and what printer is assigned.

| Field | Description |
|-------|-------------|
| BKLOGON_CODE | User login code (PK) |
| BKLOGON_PSWD | Password (encrypted) |
| BKLOGON_SCRTY | Security level code |
| BKLOGON_MENU | Top-level menu number |
| BKLOGON_SUBMENU | Sub-menu position |
| BKLOGON_CMPY | Company code |
| BKLOGON_PRINTER | Default printer name |
| BKLOGON_CURPRT | Current active printer |
| BKLOGON_INUSE | In-use flag (Y/N) |
| BKLOGON_PROG | Current program code (RWN being executed) |

---

## BKSYUSER — System User Master

**Module:** System (SY) | **PK:** BKSY_USER_CODE | **Rows:** one per EVO user

Simple user credentials table. Security level links to BKSLEVEL for menu permissions.

| Field | Description |
|-------|-------------|
| BKSY_USER_CODE | User login code (PK) |
| BKSY_USER_PSWD | Password |
| BKSY_USER_SCTY | Security level (links to BKSLEVEL.BKSL_LEVEL) |
| BKSY_USER_COMP | Default company code |
| BKSY_USER_CHR | Character set / display preference |

---

## BKSLEVEL — Security Level Permission Table

**Module:** System (SY) | **PK:** BKSL_LEVEL | **Rows:** one per security level definition

Controls which menu items each security level can access. 422 fields: 20 menu groups
× 21 fields each (20 item permissions + 1 master YN) + BKSL_LEVEL + BKSL_MENU.

| Field Pattern | Description |
|--------------|-------------|
| BKSL_LEVEL | Security level code (PK) |
| BKSL_MENU | Default menu number for this level |
| BKSL_MENU1_YN | Master enable for menu 1 (Y=access, N=blocked) |
| BKSL_MENU1_1..20 | Per-item permission for each of 20 items on menu 1 |
| BKSL_MENU2_YN..20_YN | Same pattern for menus 2–20 |
| BKSL_MENU2_1..20 | ... |
| *(continues through BKSL_MENU20_20)* | |

Each menu section covers one EvoERP top-level menu. The YN flag gates the entire menu;
the numbered fields (1–20) gate individual menu items within that menu.

---

## BKSYCFG — System Module Configuration

**Module:** System (SY) | **PK:** (single-row config table) | **Rows:** 1

Four flags controlling major module behavior at the company level.

| Field | Description |
|-------|-------------|
| BKSY_CFG_ACCTG | Accounting mode flag |
| BKSY_CFG_ADVWO | Advanced Work Orders mode (Y/N) |
| BKSY_CFG_LITEWO | Lite/simplified Work Orders mode (Y/N) |
| BKSY_CFG_SALES | Sales configuration flag |

---

## BKUPDATE — Version Update Log

**Module:** System (SY) | **PK:** BKUP_COMPANY + BKUP_UPDATE | **Rows:** one per update applied

Records which EvoERP version updates have been applied to each company database.

| Field | Description |
|-------|-------------|
| BKUPDATE_VER | Version string of current update |
| BKUP_COMPANY | Company code this update was applied to |
| BKUP_DATE | Date update was applied |
| BKUP_UPDATE | Update identifier / patch number |

---

## BKSYMSTR — System Master Settings

**Module:** System (SY) | **PK:** (single-row, company-wide) | **Fields:** 286

Company-level default settings for all modules. This is the primary configuration table
for AR, AP, GL, PO, PR, and company identity settings.

Key field groups:

| Group | Key Fields |
|-------|-----------|
| **Company** | BKSY_COMP_NAME, BKSY_COMP_ADD1, BKSY_COMP_ADD2, BKSY_COMP_CSZ |
| **AR defaults** | BKSY_ARINV_NUM, BKSY_ARSO_NUM, BKSY_AR_GLACT, BKSY_AR_GLDPT, BKSY_AR_CHKACT, BKSY_AR_FREIGHT, BKSY_AR_FRGTDPT, BKSY_AR_INT_DAY, BKSY_AR_INT_RTE, BKSY_AR_TAXABL, BKSY_AR_SLSP, BKSY_AR_TURNOFF |
| **AP defaults** | BKSY_APINV_NUM, BKSY_APPO_NUM, BKSY_AP_GLACT, BKSY_AP_GLDPT, BKSY_AP_CHKACT, BKSY_AP_DISCGL, BKSY_AP_DISCDPT |
| **GL** | BKSY_GJ_NUM, BKSY_GJ_RECNUM, BKSY_GL_ARINTR, BKSY_GL_CLRING, BKSY_GL_RELYR, BKSY_GL_RETEARN, BKSY_GLDPT_* (clearing/retain/relyr/arin GL depts) |
| **Check accounts** | BKSY_CHK_NAME/NUM/ACT/CUR/DPT_1..9 (9 bank accounts × 5 fields = 45 check fields) |
| **Payment terms** | BKSY_TERMS_1..20 (term names) + BKSY_TRM_AMT/DAY/DISC/EOM/MAX/TYP_1..20 (6 fields × 20 terms = 120 term-detail fields) |
| **PO defaults** | BKSY_PO_FREIGHT, BKSY_PO_FRGTDPT, BKSY_PO_INR, BKSY_PO_INRDPT, BKSY_PO_RNI, BKSY_PO_RNIDPT, BKSY_PO_TAXGL, BKSY_PO_TAXDPT |
| **Payroll** | BKSY_PR_CHKACT, BKSY_PR_ODNAME_1..6 |
| **Misc** | BKSY_FISCAL_YR, BKSY_TAX_RATE, BKSY_TAX_GLACT, BKSY_TAX_GLDPT, BKSY_PLAIN_CHKS, BKSY_PLAIN_INV, BKSY_PLAIN_PO, BKSY_PLAIN_STMT, BKSY_EXTRA |

AR/AP aging buckets: BKSY_AR_AGING_1..5, BKSY_AP_AGING_1..5 (5 aging periods each).
AR/AP end descriptions: BKSY_AR_ENDDESC_1..5, BKSY_AP_ENDDESC_1..5.

---

## AHSYLOG — Security Access Log

**Module:** System (SY/AH) | **PK:** AHSY_USER_CTRL | **Rows:** one per user

Tracks user session access rights. Mirrors BKSLEVEL at runtime for logged-in user.

| Field | Description |
|-------|-------------|
| AHSY_USER_CTRL | Control/session identifier (PK) |
| AHSY_USER_LEVL | Security level code |
| AHSY_USER_MENU | Current menu position |
| AHSY_USER_ACCES_1..20 | 20 access permission flags for current session |

---

## CALENDAR — Shop Calendar

**Module:** System (SY/MT) | **PK:** MTCAL_DATE | **Rows:** one per calendar date

Used by `ShopCalendar.java` to determine working days for scheduling calculations.

| Field | Description |
|-------|-------------|
| MTCAL_DATE | Calendar date (PK) — Java reads as `java.sql.Date` |
| MTCAL_DESC | Description (holiday name, etc.) |
| MTCAL_SAT | Saturday work flag (Y = this Saturday is a work day) |
| MTCAL_SUN | Sunday work flag |
| MTCAL_YEAR | Calendar year |

Java query: `SELECT MTCAL_DATE FROM CALENDAR WHERE MTCAL_DATE IS NOT NULL` — returns all
calendar dates to the `ShopCalendar` set for scheduling logic.

---

## ISSHIPCO — Shipping Carrier Master

**Module:** IS (EVO core) | **PK:** IS_SHIP_SHIPVIA | **Rows:** one per carrier code

Defines shipping carriers and their package tracking URL templates. Java reads this
to build parcel tracking links.

| Field | Description |
|-------|-------------|
| IS_SHIP_SHIPVIA | Carrier/Ship-Via code (PK) |
| IS_SHIP_SHPCOD | Short carrier code |
| IS_SHIP_SHPDESC | Carrier description |
| IS_SHIP_SHPNME | Carrier company name |
| IS_SHIP_VNDCOD | Linked AP vendor code |
| IS_SHIP_WEB_1 | URL template 1 (alternate tracking link) |
| IS_SHIP_WEB_2 | URL template 2 — **confirmed used for tracking**: contains `%%TRACK%%` placeholder replaced with tracking number |
| IS_SHIP_WEB_3..5 | Additional URL templates |
| IS_SHIP_NOTES_1..5 | Five note lines |
| IS_SHIP_EXTRA | Extra/overflow |

Java query: `SELECT IS_SHIP_WEB_2 FROM ISSHIPCO WHERE IS_SHIP_SHIPVIA = ?`

---

## ISREMIND — Reminders / Calendar Events

**Module:** IS (EVO core) | **PK:** IS_REM_WHO + IS_REM_DATE | **Rows:** one per reminder

Stores scheduled reminders, appointments, and to-dos for users.

| Field | Description |
|-------|-------------|
| IS_REM_WHO | Assigned-to user code |
| IS_REM_DATE | Reminder date |
| IS_REM_TIME | Reminder time |
| IS_REM_ENDDT | End date (for multi-day events) |
| IS_REM_ENDTM | End time |
| IS_REM_ETIME | Elapsed/duration time |
| IS_REM_SUBJECT | Subject / title |
| IS_REM_TYPE | Reminder type code |
| IS_REM_CO | Company code |
| IS_REM_DISP | Display/disposition flag |
| IS_REM_CUST | Linked customer code |
| IS_REM_VEND | Linked vendor code |
| IS_REM_ITEM | Linked item/product code |
| IS_REM_FILE | Linked file/document |
| IS_REM_MEMO | Memo body text |
| IS_REM_NOTE | Short note field |
| IS_REM_EMAIL | Email address for notification |
| IS_REM_NOTIFY | Notification sent flag |
| IS_REM_SENT | Email sent confirmation flag |
| IS_REM_TRANS | Transaction reference |
| IS_REM_BEFTXT | Before-text / prefix |
| IS_REM_COUNTER | Recurrence counter |
| IS_REM_EDATE | Expiry/end-by date |
| IS_REM_EXTRA | Extra/overflow |

---

## ISBSF — Business Score File

**Module:** IS (EVO core) / EVOBSR | **PK:** ISBSF_STARTDATE | **Rows:** 1 (rebuilt by EVOBSR)

The Business Score File is a pre-computed financial summary rebuilt by the EVOBSR utility.
It aggregates balances from AP, AR, IN, SO, PO, WO, and GL modules into one record.

Key field groups:

| Group | Fields |
|-------|-------|
| **Period** | ISBSF_STARTDATE, ISBSF_ENDDATE |
| **AP** | ISBSF_AP_ATP, ISBSF_AP_BAL, ISBSF_AP_DISC, ISBSF_AP_PAYA, ISBSF_AP_PAYM |
| **AR** | ISBSF_AR_BAL, ISBSF_AR_BILL, ISBSF_AR_COGS, ISBSF_AR_DEPO, ISBSF_AR_DISC, ISBSF_AR_RECP |
| **SO** | ISBSF_SO_BOOK, ISBSF_SO_OPEN, ISBSF_SO_SHIP |
| **PO** | ISBSF_PO_BOOK, ISBSF_PO_OPEN, ISBSF_PO_RECP |
| **IC (Inventory)** | ISBSF_IC_VALUE |
| **WO costs** | ISBSF_WOS_FOH, ISBSF_WOS_FP, ISBSF_WOS_LAB, ISBSF_WOS_MAT, ISBSF_WOS_MEXT, ISBSF_WOS_OUTP, ISBSF_WOS_SETUP, ISBSF_WOS_VOH, ISBSF_WOS_WIPV |
| **WO variances** | ISBSF_WO_FPVAR, ISBSF_WO_ISSU, ISBSF_WO_WIPBAL |
| **Cash accounts** | ISBSF_CASH_ACT1..9 (9 manually-defined cash GL accounts) |
| **Cash GL** | ISBSF_CASH_ACTS_1..100 (up to 100 GL cash account balances) |
| **Cash total** | ISBSF_CASH_TOTA |
| **Extra** | ISBSF_EXTRA |

Total: 143 fields. The CASH_ACTS_1..100 array stores per-account cash balances for the
CashFlow dashboard (CASHFLOW.DFM uses this table).

---

## MACHINE — Machine Master

**Module:** WO / DC | **PK:** TMACH_MACHINE | **Rows:** one per machine

Defines physical machines assigned to work centers. Related to WORKCTR via TMACH_WC.

| Field | Description |
|-------|-------------|
| TMACH_MACHINE | Machine code (PK) |
| TMACH_WC | Work center code (FK → WORKCTR) |
| TMACH_WCDESC | Work center description (denormalized) |
| TMACH_DESC | Machine description |
| TMACH_DATE | Date field (last service/install date) |
| TMACH_HRSUSED | Hours used (running total) |
| TMACH_HRSMAINT | Hours between maintenance |
| TMACH_EXTRA | Extra/overflow |
| TMACH_NOTES_1..8 | Eight note lines |

---

## WORKCTR — Work Center Master

**Module:** WO / SH (Shop Loading) | **PK:** MTWC_WC | **Rows:** one per work center

Defines manufacturing work centers: labor rates, overhead rates, capacity, and scheduling
parameters. Used by routing, work orders, and shop loading.

| Field | Description |
|-------|-------------|
| MTWC_WC | Work center code (PK) |
| MTWC_WCDESC | Work center description |
| MTWC_DEPT | Department code |
| MTWC_DEPTDESC | Department description (denormalized) |
| MTWC_LABOR | Labor cost rate ($/hr) |
| MTWC_SETUP | Setup cost rate ($/hr) |
| MTWC_FOVHD | Fixed overhead rate ($/hr) |
| MTWC_VOVHD | Variable overhead rate ($/hr) |
| MTWC_EST_VOVHD | Estimated variable overhead |
| MTWC_LEAD | Lead time (days) |
| MTWC_HRSWEEK | Hours per week capacity |
| MTWC_HRS_SHIFT | Hours per shift |
| MTWC_AVGQTIME | Average queue time |
| MTWC_COST_LB | Labor burden factor |
| MTWC_MACHINE | Default machine code |
| MTWC_MIN_CHG | Minimum charge amount |
| MTWC_OUTPROC | Outside process flag (Y = subcontracted) |
| MTWC_PARENT_WC | Parent work center (for hierarchical WCs) |
| MTWC_PARENT_YN | Is this a parent work center? (Y/N) |
| MTWC_LEVEL_YN | Level-loading flag |
| MTWC_QPR1..3 | Queue priority rates 1–3 |
| MTWC_EXTRA | Extra/overflow |

---

## ROUTING — Routing Operation Master

**Module:** WO | **PK:** MTRO_CODE + MTRO_NUM | **Rows:** one per routing operation step

Defines the manufacturing routing for each item: sequence of work center operations,
time standards, costs, and instructions. 62 confirmed fields.

| Field | Description |
|-------|-------------|
| MTRO_NUM | Routing step number (sequence within the routing) |
| MTRO_CODE | Product/item code (FK → BKICMSTR) |
| MTRO_OPER | Operation code |
| MTRO_OPERDESC | Operation description |
| MTRO_DESC | Long description |
| MTRO_WC | Work center code (FK → WORKCTR) |
| MTRO_WCDESC | Work center description (denormalized) |
| MTRO_TYPE | Routing type |
| MTRO_R_TYPE | Run type |
| MTRO_CLASS | Class code |
| MTRO_LABOR | Labor cost rate |
| MTRO_SETUP | Setup rate |
| MTRO_SETUPHRS | Standard setup hours |
| MTRO_STD_TIME | Standard run time (hrs/piece) |
| MTRO_DEF_TIME | Default time |
| MTRO_LEAD | Lead time (days) |
| MTRO_LONGTIME | Long-run time adjustment |
| MTRO_LOTSIZE | Standard lot size for this operation |
| MTRO_OVERLAP | Overlap percentage (parallel processing) |
| MTRO_NEGOVLP | Negative overlap |
| MTRO_PRINT | Print this operation on traveler (Y/N) |
| MTRO_PARTSHR | Shared part flag |
| MTRO_MACHINE | Machine code |
| MTRO_TMACHINE | Template machine |
| MTRO_TMACHDESC | Template machine description |
| MTRO_TOOL | Tool code |
| MTRO_TOOLDESC | Tool description |
| MTRO_MIN_CHG | Minimum charge |
| MTRO_PIECE_RATE | Piece rate |
| MTRO_NUM_PERSON | Number of persons required |
| MTRO_NUM_PROCES | Number of simultaneous processes |
| MTRO_MD_PROC_HR | Machine-down processing/hr rate |
| MTRO_PROC_PERHR | Processes per hour |
| MTRO_TIME_PERPR | Time per process |
| MTRO_TIMEPART | Time part factor |
| MTRO_FOVHD | Fixed overhead rate |
| MTRO_VOVHD | Variable overhead rate |
| MTRO_EST_LINE | Estimate line link |
| MTRO_EST_TAG | Estimate tag |
| MTRO_MISC_ACOST | Miscellaneous actual cost |
| MTRO_OP_TEMP_NO | Operation template number |
| MTRO_VENDCODE | Vendor code (for outside process) |
| MTRO_VENDCOST | Vendor cost (for outside process) |
| MTRO_VENDNAME | Vendor name (denormalized) |
| MTRO_INSTR_1..15 | 15 instruction / work instruction lines |
| MTRO_EXTRA | Extra/overflow |
| MTWO_MISC_COST | WO misc cost (stored in routing record) |
| MTWO_MISC_DESC | WO misc cost description |

---

## BKBMMSTR — Bill of Materials Component

**Module:** BM (Bill of Materials) | **PK:** BKBM_UID | **Rows:** one per BOM component relationship

Each row represents one parent-component relationship in a BOM. 26 fields confirmed.

| Field | Description |
|-------|-------------|
| BKBM_UID | Unique identifier (PK) |
| BKBM_PARENT | Parent item code |
| BKBM_COMPONENT | Child/component item code |
| BKBM_P_TYPE | Parent type indicator |
| BKBM_C_TYPE | Component type indicator |
| BKBM_QTY_REQD | Quantity required per parent unit |
| BKBM_REFERENCE | Reference designator (PCB location, etc.) |
| BKBM_REV | Revision level |
| BKBM_EXTRA | Extra/overflow |
| BKBM_DATE1 | Date field 1 |
| BKBM_DATE2 | Date field 2 |
| BKBM_EST_LINE | Estimate line number link |
| BKBM_PROD_OP | Production operation code |
| BKBM_PROD_OPDSC | Production operation description |
| BKBM_PROD_DUPOP | Duplicate operation flag |
| BKBM_PROD_TYPE | Production type |
| BKBM_PROD_SCRAP | Scrap factor |
| BKBM_PROD_PRICE | Production price override |
| BKBM_PROD_VEND | Production vendor code |
| BKBM_PROD_RTNUM | Production routing step number |
| BKBM_PROD_OPYN_1..6 | Six operation Y/N flags |

---

## ISFOHEAD — Features & Options Header

**Module:** IS / FO (Features & Options) | **PK:** ISFO_HDR_UID | **Rows:** one per F&O definition

Master record for a Features & Options (F&O) product configuration. Links a parent item
to optional sub-components that can be selected at order time.

| Field | Description |
|-------|-------------|
| ISFO_HDR_UID | Unique identifier (PK) |
| ISFO_HDR_PARENT | Parent item code |
| ISFO_HDR_DESC | Description |
| ISFO_HDR_STATUS | Status code |
| ISFO_HDR_DATE | Creation/last-modified date |
| ISFO_HDR_CUST | Customer code (if customer-specific F&O) |
| ISFO_HDR_VEND | Vendor code (if vendor-specific) |
| ISFO_HDR_RFQ | RFQ reference |
| ISFO_HDR_REV | Revision level |
| ISFO_HDR_PERM | Permanent flag |
| ISFO_HDR_MDATES_1..5 | Five milestone dates |
| ISFO_HDR_EXTRA | Extra/overflow |

Conversion flags from ISFOHEAD DFM (confirmed Pass 99):
SOCB (SO), WOCB (WO), POCB (PO), NICB (NI — item), SQCB (SQ — service quote), RQCB (RQ — RFQ)

---

## ISFOLINE — Features & Options Line

**Module:** IS / FO (Features & Options) | **PK:** ISFO_LIN_UID | **Rows:** one per F&O component

Component line within a Features & Options definition. 78 fields. Very similar to
BKBMMSTR but with 50 operation flags and conversion support.

Key fields: ISFO_LIN_UID, ISFO_LIN_PARENT, ISFO_LIN_COMP, ISFO_LIN_TYPE, ISFO_LIN_LEVEL,
ISFO_LIN_LINEN (line number), ISFO_LIN_OP, ISFO_LIN_OPDSC, ISFO_LIN_DUPOP, ISFO_LIN_RTNUM,
ISFO_LIN_QTYREQ, ISFO_LIN_PRICE, ISFO_LIN_SCRAP, ISFO_LIN_REV, ISFO_LIN_REF, ISFO_LIN_VEND,
ISFO_LIN_DATE1, ISFO_LIN_DATE2, ISFO_LIN_CBRANC (child branch), ISFO_LIN_PBRANC (parent branch),
ISFO_LIN_BEXTRA, ISFO_LIN_EXTRA,
ISFO_LIN_OPFLAG_1..50 (50 operation flag fields),
ISFO_LIN_OPYN_1..6 (6 operation Y/N flags)

---

## BKICLOC — Inventory Location Record

**Module:** IC (Inventory) | **PK:** BKIC_LOC_CODE + BKIC_LOC_BIN | **Rows:** one per item-location-bin

Per-location inventory quantities and GL account assignments. 32 fields.

| Field | Description |
|-------|-------------|
| BKIC_LOC_CODE | Item/product code |
| BKIC_LOC_BIN | Bin/location identifier |
| BKIC_LOC_UOH | Units on hand at this location |
| BKIC_LOC_UOO | Units on order (PO) |
| BKIC_LOC_UOSO | Units on SO (customer backorder) |
| BKIC_LOC_UOWO | Units on WO |
| BKIC_LOC_UWIP | Units in WIP |
| BKIC_LOC_UALLOC | Units allocated |
| BKIC_LOC_UBO | Units back-ordered |
| BKIC_LOC_UIQC | Units in QC inspection |
| BKIC_LOC_GLA | GL account — additions (receipt) |
| BKIC_LOC_GLC | GL account — COGS |
| BKIC_LOC_GLS | GL account — sales |
| BKIC_LOC_GLSNT | GL account — sales non-taxable |
| BKIC_LOC_GLWIP | GL account — WIP |
| BKIC_LOC_DPTA | GL dept — additions |
| BKIC_LOC_DPTC | GL dept — COGS |
| BKIC_LOC_DPTS | GL dept — sales |
| BKIC_LOC_DPTSNT | GL dept — sales non-taxable |
| BKIC_LOC_DPTWIP | GL dept — WIP |
| BKIC_LOC_LOT | Lot control flag (Y/N) |
| BKIC_LOC_SER | Serial control flag (Y/N) |
| BKIC_LOC_PROD | Production location flag |
| BKIC_LOC_WHCTRL | Warehouse control flag |
| BKIC_LOC_ALPHA1 | Alpha field 1 |
| BKIC_LOC_ALPHA2 | Alpha field 2 |
| BKIC_LOC_NUM1 | Numeric field 1 |
| BKIC_LOC_NUM2 | Numeric field 2 |
| BKIC_LOC_DATE1 | Date field 1 |
| BKIC_LOC_LCDATE | Last count date (physical inventory) |
| BKIC_LOC_FLAG1 | Additional flag field |
| BKIC_LOC_EXTRA | Extra/overflow |

---

## BKQCMSTR — QC Receiving Record

**Module:** QC (Quality Control) | **PK:** BKQC_RECVR_NUM | **Rows:** one per QC receiving record

Tracks quality control inspection for incoming purchase order receipts. 14 fields.

| Field | Description |
|-------|-------------|
| BKQC_RECVR_NUM | Receiver/inspection number (PK) |
| BKQC_RECV_DATE | Inspection date (also tracked as BKQC.RECV.DATE in DFMs) |
| BKQC_PO_NUM | Purchase order number |
| BKQC_POL_ITM_NO | PO line item number |
| BKQC_PROD_CODE | Product/item code received |
| BKQC_VEND_CODE | Vendor code |
| BKQC_PKSLIP_NUM | Packing slip number |
| BKQC_PKSLIP_QTY | Packing slip quantity |
| BKQC_QTY_RECVD | Quantity received |
| BKQC_QTY_REJECT | Quantity rejected |
| BKQC_QTY_BUYOFF | Quantity accepted / bought off |
| BKQC_UNIT_COST | Unit cost |
| BKQC_OUT_DATE | Date sent out for inspection |
| BKQC_EXTRA | Extra/overflow |

RoHS extension (confirmed from DFM analysis, Pass 95): BKQC.RECV.DATE is also
set in autoT7POJC (automated PO job close) when configuring the quality checkpoint.

---

## INVTXN — Inventory Transaction Log

**Module:** Cross-module (IN/SO/WO/PO/PI) | **PK:** (date+code+type — append-only) | **Fields:** 24

Every inventory movement in EvoERP writes a row to INVTXN. This is the core audit trail for
on-hand quantities, costs, and lot/serial tracking. Called by SO posting, WO receipts, PO
receiving, PI adjustments, and manual IC adjustments.

| Field | Type | Size | Meaning |
|-------|------|------|---------|
| MTIT_TYPE | STRING | 1 | Transaction type: `R`=receive (PO), `I`=issue (to WO), `A`=adjustment, `S`=ship (SO), `P`=PI/physical, `X`=scrap |
| MTIT_CLASS | STRING | 4 | Item class code |
| MTIT_DATE | DATE | 4 | Transaction date |
| MTIT_CODE | STRING | 15 | Part number / item code |
| MTIT_QTY | FLOAT | 8 | Quantity (positive = in, negative = out) |
| MTIT_AVGCOST | FLOAT | 8 | Average cost per unit at time of transaction |
| MTIT_STDCST | FLOAT | 8 | Standard cost per unit at time of transaction |
| MTIT_LOC | STRING | 10 | Location / warehouse code |
| MTIT_REF | STRING | 30 | Reference number — the source document (SO#, PO#, WO#, etc.) |
| MTIT_CUST | STRING | 10 | Customer code (for SO/AR transactions) |
| MTIT_INVOICE | FLOAT | 8 | Invoice number (for SO transactions) |
| MTIT_PRICE | FLOAT | 8 | Selling price (for SO transactions) |
| MTIT_PO | FLOAT | 8 | PO number (for PO/AP transactions) |
| MTIT_WOPRE | FLOAT | 8 | WO prefix (for WO-related transactions) |
| MTIT_WOSUF | UBINARY | 2 | WO suffix |
| MTIT_LOT | STRING | 15 | Lot number (if lot-tracked) |
| MTIT_SERIAL | STRING | 25 | Serial number (if serial-tracked) |
| MTIT_VENDOR | STRING | 10 | Vendor code (for PO/AP transactions) |
| MTIT_SCRAP | STRING | 2 | Scrap reason code |
| MTIT_QC | STRING | 2 | QC code |
| MTIT_DEPT | STRING | 4 | Department code |
| MTIT_DESC | STRING | 30 | Transaction description |
| MTIT_PRODLOT | STRING | 15 | Production lot (for WO receipts — the lot assigned to finished goods) |
| MTIT_EXTRA | STRING | 50 | Extra / overflow field |

**Usage pattern:** When SO-G posts a shipment, it writes one INVTXN row per line item
(TYPE=`S`, CODE=part, QTY=-shipped_qty, REF=SO#, CUST=customer). When WO receipts post,
they write TYPE=`R`/`I` rows. BKICLOC on-hand is decremented/incremented, then INVTXN
gets the corresponding audit row.

---

## WOLABOR — WO Labor Transaction (58 fields)

**Module:** WO / DC | **PK:** (WOPRE+WOSUF+OPER+TRXN) | **Fields:** 58

Each clock-in / clock-out event on a work order writes one WOLABOR row. This is the
primary table for job-cost labor actuals. Referenced by JC module for cost analysis
and by DC module as the source of truth for labor entry.

Key fields by category:

**Identity:**
| Field | Type | Meaning |
|-------|------|---------|
| MTWOLA_DATE | DATE | Labor date |
| MTWOLA_EMP | UBINARY | Employee number |
| MTWOLA_WOPRE | FLOAT | WO prefix |
| MTWOLA_WOSUF | UBINARY | WO suffix |
| MTWOLA_OPER | UBINARY | Operation number |
| MTWOLA_TRXN | UBINARY | Transaction sequence |
| MTWOLA_POSTED | STRING(1) | Posted flag |
| MTWOLA_REGOVER | STRING(1) | Regular (`R`) or overtime (`O`) |

**Hours and quantities:**
| Field | Meaning |
|-------|---------|
| MTWOLA_RUNHRS | Run hours |
| MTWOLA_SETUPHRS | Setup hours |
| MTWOLA_NOJOBS | Number of jobs / pieces |
| MTWOLA_PARTS | Parts count |
| MTWOLA_SCRAPPED | Scrapped quantity |
| MTWOLA_COMPLETE | Complete flag (Y/N) |
| MTWOLA_REWORK | Rework flag |

**Costs (computed and stored at posting time):**
| Field | Meaning |
|-------|---------|
| MTWOLA_LABRATE | Labor rate ($/hr) |
| MTWOLA_LABCOST | Labor cost |
| MTWOLA_SETCOST | Setup cost |
| MTWOLA_MACHCOST | Machine cost |
| MTWOLA_FOHCOST | Fixed overhead cost |
| MTWOLA_VOHCOST | Variable overhead cost |
| MTWOLA_MISC | Miscellaneous cost |

**Quality:**
| Field | Meaning |
|-------|---------|
| MTWOLA_QCCODE | QC reject code |
| MTWOLA_QCDESC | QC reject description |
| MTWOLA_SCRAPCD | Scrap code |
| MTWOLA_SCDESC | Scrap description |

**Resources assigned:**
| Field | Meaning |
|-------|---------|
| MTWOLA_WC | Work center code |
| MTWOLA_MACH | Machine code |
| MTWOLA_TOOL | Tool code |
| MTWOLA_SHIFT | Shift number |
| MTWOLA_TEAM | Team ID |

**Time stamps (DC time-clock integration):**
| Field | Meaning |
|-------|---------|
| MTWOLA_START | Clock-in time |
| MTWOLA_STOP | Clock-out time |
| MTWOLA_DEDUCT | Deduction (break time) |

**Cycle count tracking (per-cycle production metrics):**
| Field | Meaning |
|-------|---------|
| MTWOLA_CYCHR/MIN/SEC | Cycle time (hours/minutes/seconds) |
| MTWOLA_CYCPARTS | Parts produced per cycle |
| MTWOLA_CYCNOTE | Cycle note (255 chars) |

**Custom flags:** MTWOLA_FLAG_1..5 (5 × STRING 1) and MTWOLA_ALPHA_1..3 (3 × STRING 30)
for customer-specific extensions.

---

*Tier 9 per-table narrative docs — Java-confirmed field schemas from EvoPVT.jar class files;
DDF-confirmed schemas from Pass 108. Generated Pass 103, updated Pass 108, 2026-06-18.*
