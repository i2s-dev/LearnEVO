# CS — Customer Service / Commissions: Field Reference

Status: verified-schema + completed field meanings (Pass 574g, 2026-07-06).

Source: `Evo-DBA_File_Fields 052421.xlsx`, sheet "Fields". Excel descriptions partially
present for BKARINVI/ISARAIVI; all other fields name-inferred.

The CS module manages salesperson commissions. BKPRSALE/ISPRSALE are salesperson master
records with 12-month period accumulators. BKPR_COMM_* tables (BKPRACOM/BKPRCOMM/BKPRHCOM)
are the commission pipeline: unposted → posted → archived. BKARINVI/ISARAIVI hold per-invoice
commission data. ISREPLNK/ISREPORD support extended rep assignment + line-item tracking.

---

## BKARINVI
**COMMISSIONS** — per-invoice commission summary (active)

Fields: 16 | Key: BKAR_INVI_INVNM + BKAR_INVI_PCODE

One row per invoice × line item for commission tracking.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKAR_INVI_COMM_1 | NUMERIC | 8 | 4 | Commission amount/rate for salesperson slot 1 |
| 2 | BKAR_INVI_COMM_2 | NUMERIC | 8 | 4 | Commission amount/rate for salesperson slot 2 |
| 3 | BKAR_INVI_COOP | NUMERIC | 8 | 2 | Co-op advertising credit amount |
| 4 | BKAR_INVI_ESD | DATE | 4 | — | Estimated Ship Date |
| 5 | BKAR_INVI_EXTRM | NUMERIC | 8 | 2 | Extra/miscellaneous amount on this invoice line |
| 6 | BKAR_INVI_FRGHT | NUMERIC | 8 | 2 | Freight |
| 7 | BKAR_INVI_INVNM | NUMERIC | 8 | — | Invoice Number (FK → BKARINV) |
| 8 | BKAR_INVI_ITYPE | STRING | 1 | — | Item Type |
| 9 | BKAR_INVI_PCODE | STRING | 15 | — | Part Code (FK → BKICMSTR) |
| 10 | BKAR_INVI_PCOGS | NUMERIC | 8 | 2 | COGS |
| 11 | BKAR_INVI_PDISC | NUMERIC | 8 | 2 | Discount |
| 12 | BKAR_INVI_PEXT | NUMERIC | 8 | 2 | Extended Price |
| 13 | BKAR_INVI_PPRCE | NUMERIC | 8 | 4 | Price |
| 14 | BKAR_INVI_PQTY | NUMERIC | 8 | 2 | Quantity |
| 15 | BKAR_INVI_SONUM | NUMERIC | 8 | — | Sales Order Number |
| 16 | BKAR_INVI_TAX | NUMERIC | 8 | 2 | Tax amount on this invoice line |

## BKPRACOM
**ARCHIVED COMMISSION DETAIL** — commission records after period close

Fields: 12 | Key: BKPR_COMM_ULID

Identical schema to BKPRCOMM — records move here after period archive.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKPR_COMM_AMTPD | NUMERIC | 8 | 2 | Amount paid (commission payment amount issued to salesperson) |
| 2 | BKPR_COMM_CCODE | STRING | 10 | — | Customer code (FK → BKARCUST) |
| 3 | BKPR_COMM_COMM | NUMERIC | 8 | 2 | Commission amount earned on this transaction |
| 4 | BKPR_COMM_EXTRA | STRING | 25 | — | Extra data |
| 5 | BKPR_COMM_INVDT | DATE | 4 | — | Invoice date (when the invoice was posted) |
| 6 | BKPR_COMM_INVNM | NUMERIC | 8 | — | Invoice number (FK → BKARINV) |
| 7 | BKPR_COMM_PAYDT | DATE | 4 | — | Payment date (when commission was paid to salesperson) |
| 8 | BKPR_COMM_PCODE | STRING | 15 | — | Part code (item sold, FK → BKICMSTR) |
| 9 | BKPR_COMM_PD_ON | NUMERIC | 8 | 2 | Paid-on amount (invoice amount commission was calculated from) |
| 10 | BKPR_COMM_SLSP | INTEGER | 2 | — | Salesperson number (FK → BKPRSALE) |
| 11 | BKPR_COMM_TDATE | DATE | 4 | — | Transaction date |
| 12 | BKPR_COMM_ULID | NUMERIC | 8 | 4 | Unique line ID (PK — float-encoded sequence) |

## BKPRAGNT
**AGENTS** — sales agent to GL account mapping

Fields: 4 | Key: BKPR_AGNT_NUM

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKPR_AGNT_CODE | STRING | 10 | — | Vendor Code |
| 2 | BKPR_AGNT_GLACT | STRING | 10 | — | GL Account |
| 3 | BKPR_AGNT_GLDPT | STRING | 4 | — | GL Department |
| 4 | BKPR_AGNT_NUM | INTEGER | 2 | — | Agent number |

## BKPRCOMM
**COMMISSIONS** — active/unposted commission detail

Fields: 12 | Key: BKPR_COMM_ULID

Identical schema to BKPRACOM. See BKPRACOM above for field definitions.

## BKPRHCOM
**POSTED COMMISSION DETAIL** — commission records after posting

Fields: 12 | Key: BKPR_COMM_ULID

Identical schema to BKPRACOM. See BKPRACOM above for field definitions.

## BKPRSALE
**SALESPERSON MASTER** — salesperson record with 12-period performance accumulators

Fields: 86 | Key: BKPR_SLS_EMPNUM

One row per salesperson. Each of COGS/COMM/GROSS/PAID/QUOTA/RCPTS has 12 monthly slots.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKPR_SLS_CLASS_1 | STRING | 2 | — | Sales class code 1 (item class this rep specializes in) |
| 2 | BKPR_SLS_CLASS_2 | STRING | 2 | — | Sales class code 2 |
| 3 | BKPR_SLS_COGS_1 | NUMERIC | 8 | 2 | Cost of goods sold — month 1 (Jan) |
| 4 | BKPR_SLS_COGS_10 | NUMERIC | 8 | 2 | COGS — month 10 (Oct) |
| 5 | BKPR_SLS_COGS_11 | NUMERIC | 8 | 2 | COGS — month 11 (Nov) |
| 6 | BKPR_SLS_COGS_12 | NUMERIC | 8 | 2 | COGS — month 12 (Dec) |
| 7 | BKPR_SLS_COGS_2 | NUMERIC | 8 | 2 | COGS — month 2 (Feb) |
| 8 | BKPR_SLS_COGS_3 | NUMERIC | 8 | 2 | COGS — month 3 (Mar) |
| 9 | BKPR_SLS_COGS_4 | NUMERIC | 8 | 2 | COGS — month 4 (Apr) |
| 10 | BKPR_SLS_COGS_5 | NUMERIC | 8 | 2 | COGS — month 5 (May) |
| 11 | BKPR_SLS_COGS_6 | NUMERIC | 8 | 2 | COGS — month 6 (Jun) |
| 12 | BKPR_SLS_COGS_7 | NUMERIC | 8 | 2 | COGS — month 7 (Jul) |
| 13 | BKPR_SLS_COGS_8 | NUMERIC | 8 | 2 | COGS — month 8 (Aug) |
| 14 | BKPR_SLS_COGS_9 | NUMERIC | 8 | 2 | COGS — month 9 (Sep) |
| 15 | BKPR_SLS_COMM_1 | NUMERIC | 8 | 2 | Commission earned — month 1 |
| 16 | BKPR_SLS_COMM_10 | NUMERIC | 8 | 2 | Commission earned — month 10 |
| 17 | BKPR_SLS_COMM_11 | NUMERIC | 8 | 2 | Commission earned — month 11 |
| 18 | BKPR_SLS_COMM_12 | NUMERIC | 8 | 2 | Commission earned — month 12 |
| 19 | BKPR_SLS_COMM_2 | NUMERIC | 8 | 2 | Commission earned — month 2 |
| 20 | BKPR_SLS_COMM_3 | NUMERIC | 8 | 2 | Commission earned — month 3 |
| 21 | BKPR_SLS_COMM_4 | NUMERIC | 8 | 2 | Commission earned — month 4 |
| 22 | BKPR_SLS_COMM_5 | NUMERIC | 8 | 2 | Commission earned — month 5 |
| 23 | BKPR_SLS_COMM_6 | NUMERIC | 8 | 2 | Commission earned — month 6 |
| 24 | BKPR_SLS_COMM_7 | NUMERIC | 8 | 2 | Commission earned — month 7 |
| 25 | BKPR_SLS_COMM_8 | NUMERIC | 8 | 2 | Commission earned — month 8 |
| 26 | BKPR_SLS_COMM_9 | NUMERIC | 8 | 2 | Commission earned — month 9 |
| 27 | BKPR_SLS_EMPNUM | INTEGER | 2 | — | Employee/salesperson number (PK) |
| 28 | BKPR_SLS_EXPACT | STRING | 10 | — | Expense GL account (for rep-related expense postings) |
| 29 | BKPR_SLS_EXPDPT | STRING | 4 | — | Expense GL department |
| 30 | BKPR_SLS_EXTRA | STRING | 100 | — | Extra data |
| 31 | BKPR_SLS_FNMI | STRING | 25 | — | First name and middle initial |
| 32 | BKPR_SLS_GROSS_1 | NUMERIC | 8 | 2 | Gross sales — month 1 |
| 33 | BKPR_SLS_GROSS_10 | NUMERIC | 8 | 2 | Gross sales — month 10 |
| 34 | BKPR_SLS_GROSS_11 | NUMERIC | 8 | 2 | Gross sales — month 11 |
| 35 | BKPR_SLS_GROSS_12 | NUMERIC | 8 | 2 | Gross sales — month 12 |
| 36 | BKPR_SLS_GROSS_2 | NUMERIC | 8 | 2 | Gross sales — month 2 |
| 37 | BKPR_SLS_GROSS_3 | NUMERIC | 8 | 2 | Gross sales — month 3 |
| 38 | BKPR_SLS_GROSS_4 | NUMERIC | 8 | 2 | Gross sales — month 4 |
| 39 | BKPR_SLS_GROSS_5 | NUMERIC | 8 | 2 | Gross sales — month 5 |
| 40 | BKPR_SLS_GROSS_6 | NUMERIC | 8 | 2 | Gross sales — month 6 |
| 41 | BKPR_SLS_GROSS_7 | NUMERIC | 8 | 2 | Gross sales — month 7 |
| 42 | BKPR_SLS_GROSS_8 | NUMERIC | 8 | 2 | Gross sales — month 8 |
| 43 | BKPR_SLS_GROSS_9 | NUMERIC | 8 | 2 | Gross sales — month 9 |
| 44 | BKPR_SLS_HOW_1 | STRING | 1 | — | Commission calculation method slot 1: `P`=on payment, `I`=on invoice |
| 45 | BKPR_SLS_HOW_2 | STRING | 1 | — | Commission calculation method slot 2 |
| 46 | BKPR_SLS_LNME | STRING | 25 | — | Last name |
| 47 | BKPR_SLS_PAID_1 | NUMERIC | 8 | 2 | Commission paid to rep — month 1 |
| 48 | BKPR_SLS_PAID_10 | NUMERIC | 8 | 2 | Commission paid — month 10 |
| 49 | BKPR_SLS_PAID_11 | NUMERIC | 8 | 2 | Commission paid — month 11 |
| 50 | BKPR_SLS_PAID_12 | NUMERIC | 8 | 2 | Commission paid — month 12 |
| 51 | BKPR_SLS_PAID_2 | NUMERIC | 8 | 2 | Commission paid — month 2 |
| 52 | BKPR_SLS_PAID_3 | NUMERIC | 8 | 2 | Commission paid — month 3 |
| 53 | BKPR_SLS_PAID_4 | NUMERIC | 8 | 2 | Commission paid — month 4 |
| 54 | BKPR_SLS_PAID_5 | NUMERIC | 8 | 2 | Commission paid — month 5 |
| 55 | BKPR_SLS_PAID_6 | NUMERIC | 8 | 2 | Commission paid — month 6 |
| 56 | BKPR_SLS_PAID_7 | NUMERIC | 8 | 2 | Commission paid — month 7 |
| 57 | BKPR_SLS_PAID_8 | NUMERIC | 8 | 2 | Commission paid — month 8 |
| 58 | BKPR_SLS_PAID_9 | NUMERIC | 8 | 2 | Commission paid — month 9 |
| 59 | BKPR_SLS_QUOTA_1 | NUMERIC | 8 | 2 | Sales quota — month 1 |
| 60 | BKPR_SLS_QUOTA_10 | NUMERIC | 8 | 2 | Sales quota — month 10 |
| 61 | BKPR_SLS_QUOTA_11 | NUMERIC | 8 | 2 | Sales quota — month 11 |
| 62 | BKPR_SLS_QUOTA_12 | NUMERIC | 8 | 2 | Sales quota — month 12 |
| 63 | BKPR_SLS_QUOTA_2 | NUMERIC | 8 | 2 | Sales quota — month 2 |
| 64 | BKPR_SLS_QUOTA_3 | NUMERIC | 8 | 2 | Sales quota — month 3 |
| 65 | BKPR_SLS_QUOTA_4 | NUMERIC | 8 | 2 | Sales quota — month 4 |
| 66 | BKPR_SLS_QUOTA_5 | NUMERIC | 8 | 2 | Sales quota — month 5 |
| 67 | BKPR_SLS_QUOTA_6 | NUMERIC | 8 | 2 | Sales quota — month 6 |
| 68 | BKPR_SLS_QUOTA_7 | NUMERIC | 8 | 2 | Sales quota — month 7 |
| 69 | BKPR_SLS_QUOTA_8 | NUMERIC | 8 | 2 | Sales quota — month 8 |
| 70 | BKPR_SLS_QUOTA_9 | NUMERIC | 8 | 2 | Sales quota — month 9 |
| 71 | BKPR_SLS_RATE_1 | NUMERIC | 8 | 4 | Commission rate — tier 1 (%) |
| 72 | BKPR_SLS_RATE_2 | NUMERIC | 8 | 4 | Commission rate — tier 2 (%) |
| 73 | BKPR_SLS_RCPTS_1 | NUMERIC | 8 | 2 | Cash receipts collected — month 1 |
| 74 | BKPR_SLS_RCPTS_10 | NUMERIC | 8 | 2 | Cash receipts — month 10 |
| 75 | BKPR_SLS_RCPTS_11 | NUMERIC | 8 | 2 | Cash receipts — month 11 |
| 76 | BKPR_SLS_RCPTS_12 | NUMERIC | 8 | 2 | Cash receipts — month 12 |
| 77 | BKPR_SLS_RCPTS_2 | NUMERIC | 8 | 2 | Cash receipts — month 2 |
| 78 | BKPR_SLS_RCPTS_3 | NUMERIC | 8 | 2 | Cash receipts — month 3 |
| 79 | BKPR_SLS_RCPTS_4 | NUMERIC | 8 | 2 | Cash receipts — month 4 |
| 80 | BKPR_SLS_RCPTS_5 | NUMERIC | 8 | 2 | Cash receipts — month 5 |
| 81 | BKPR_SLS_RCPTS_6 | NUMERIC | 8 | 2 | Cash receipts — month 6 |
| 82 | BKPR_SLS_RCPTS_7 | NUMERIC | 8 | 2 | Cash receipts — month 7 |
| 83 | BKPR_SLS_RCPTS_8 | NUMERIC | 8 | 2 | Cash receipts — month 8 |
| 84 | BKPR_SLS_RCPTS_9 | NUMERIC | 8 | 2 | Cash receipts — month 9 |
| 85 | BKPR_SLS_WHEN_1 | STRING | 1 | — | When commission triggers for tier 1: `P`=on payment, `I`=on invoice |
| 86 | BKPR_SLS_WHEN_2 | STRING | 1 | — | When commission triggers for tier 2 |

## ISARAIVI
**ARCHIVED COMMISSION DETAIL** — per-invoice commission data after period archive

Fields: 16 | Key: BKAR_INVI_INVNM + BKAR_INVI_PCODE

Identical schema to BKARINVI — archived copy after period close.
See BKARINVI above for all field definitions.

## ISPRSALE
**SALESPERSON LIST EXTENDED COMMISSION** — IS-module salesperson master

Fields: 86 | Key: BKPR_SLS_EMPNUM

Identical schema to BKPRSALE (same BKPR_SLS_* prefix). IS-era extended salesperson
master. See BKPRSALE above for all field definitions.

## ISREPLNK
**EXTENDED COMMISSION REP ASSIGNMENT** — maps reps to specific customer/item combinations

Fields: 10 | Key: ISREP_LNK_REPNM + ISREP_LNK_CUST + ISREP_LNK_ITEM

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISREP_LNK_CLASS | STRING | 4 | — | Item class code for this rep assignment |
| 2 | ISREP_LNK_COMM^ | NUMERIC | 8 | 4 | Commission rate (%) for this rep/customer/item combination |
| 3 | ISREP_LNK_CUST | STRING | 10 | — | Customer code (FK → BKARCUST) |
| 4 | ISREP_LNK_DATE | DATE | 4 | — | Assignment creation date |
| 5 | ISREP_LNK_EDATE | DATE | 4 | — | Assignment expiry date |
| 6 | ISREP_LNK_EXTRA | STRING | 100 | — | Extra data |
| 7 | ISREP_LNK_ITEM | STRING | 15 | — | Item code for this rep assignment (FK → BKICMSTR; blank=all items) |
| 8 | ISREP_LNK_LABEL | STRING | 5 | — | Assignment label/category code |
| 9 | ISREP_LNK_REPNM | INTEGER | 2 | — | Rep number (FK → BKPRSALE.BKPR_SLS_EMPNUM) |
| 10 | ISREP_LNK_SDATE | DATE | 4 | — | Assignment effective start date |

## ISREPORD
**EXTENDED COMMISSION LINE ITEM COMMISSIONS** — line-level commission tracking

Fields: 15 | Key: ISREP_ORD_ULID

One row per invoice line × rep assignment. Tracks commission earned and paid at the
individual invoice line level.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISREP_ORD_AMT | NUMERIC | 8 | 2 | Invoice line amount (basis for commission calculation) |
| 2 | ISREP_ORD_AMTRM | NUMERIC | 8 | 2 | Amount after returns/adjustments |
| 3 | ISREP_ORD_CBK | STRING | 1 | — | Chargeback flag: `Y`=this commission has an associated chargeback |
| 4 | ISREP_ORD_CMAMT | NUMERIC | 8 | 2 | Commission amount earned on this line |
| 5 | ISREP_ORD_COMPR | NUMERIC | 8 | 4 | Commission percentage rate applied |
| 6 | ISREP_ORD_CUST | STRING | 10 | — | Customer code (FK → BKARCUST) |
| 7 | ISREP_ORD_EXTRA | STRING | 100 | — | Extra data |
| 8 | ISREP_ORD_INVDT | DATE | 4 | — | Invoice date |
| 9 | ISREP_ORD_INVNM | NUMERIC | 8 | — | Invoice number (FK → BKARINV) |
| 10 | ISREP_ORD_PAYDT | DATE | 4 | — | Payment date (when commission was paid) |
| 11 | ISREP_ORD_PCODE | STRING | 15 | — | Part code (FK → BKICMSTR) |
| 12 | ISREP_ORD_REPNM | INTEGER | 2 | — | Rep number (FK → BKPRSALE.BKPR_SLS_EMPNUM) |
| 13 | ISREP_ORD_REPWH | STRING | 1 | — | Rep share code: `W`=whole commission to this rep, `H`=half, `S`=split |
| 14 | ISREP_ORD_SONUM | NUMERIC | 8 | — | Sales order number |
| 15 | ISREP_ORD_ULID | NUMERIC | 8 | 4 | Unique line ID (PK — float-encoded) |

**Confidence: 80/100** — BKARINVI/ISARAIVI partial descriptions from Excel confirmed;
BKPR_COMM_* and BKPR_SLS_* field semantics clear from commission accounting context;
BKPR_SLS_HOW_*/WHEN_* exact values (P/I/etc.) and CLASS_*/RATE tier behavior require
RWN decryption; ISREPLNK/ISREPORD meanings clear from extended commission feature context.
