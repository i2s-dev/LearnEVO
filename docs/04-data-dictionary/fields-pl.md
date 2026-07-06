# PL — Checkmark Payroll Integration: Field Reference

Status: verified-schema + inferred meanings (Pass 574, 2026-07-06).

Source: `Evo-DBA_File_Fields 052421.xlsx`, sheet "Fields".

The PL module bridges EvoERP payroll data to **Checkmark Payroll**, a third-party Mac/Windows
payroll application. EvoERP exports check and GL data to Checkmark's flat-file format.

Two tables: BKCPMSTR (configuration — file paths) and BKCPEC (transfer staging records).
Both use the BKCP_* field prefix (BK = legacy gen, CP = CheckMark Payroll).

---

## BKCPEC
**CHECK MARK PAYROLL TRANSFER** — payroll check staging/transfer records

Fields: 10 | Key: BKCP_EC_CHECKNO + BKCP_EC_LINE

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKCP_EC_AMOUNT | NUMERIC | 8 | 2 | Check amount in dollars |
| 2 | BKCP_EC_CHECKNO | NUMERIC | 8 | — | Payroll check number |
| 3 | BKCP_EC_DATE | DATE | 4 | — | Check date |
| 4 | BKCP_EC_DESC | STRING | 25 | — | Description / pay period description |
| 5 | BKCP_EC_ERROR | STRING | 5 | — | Transfer error code (blank = success) |
| 6 | BKCP_EC_GLACCT | STRING | 10 | — | GL account code for this payroll line |
| 7 | BKCP_EC_GLDEPT | STRING | 4 | — | GL department code |
| 8 | BKCP_EC_ISCHK | NUMERIC | 8 | — | Is-check flag / internal reference number |
| 9 | BKCP_EC_LINE | INTEGER | 2 | — | Line number within the check (for multi-distribution GL lines) |
| 10 | BKCP_EC_VEND | STRING | 10 | — | Vendor/employee code (employees treated as vendors for check issuance) |

**Notes:**
- BKCPEC is a staging table — records are written here when exporting to Checkmark,
  then cleared after successful transfer.
- BKCP_EC_GLACCT/GLDEPT link each payroll distribution line to the GL posting account.
- BKCP_EC_ERROR captures transfer errors for review before GL posting.

## BKCPMSTR
**CHECK MARK PAYROLL MASTER** — Checkmark Payroll integration configuration

Fields: 9 | Key: singleton (one configuration record)

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKCP_MST_CFILE | STRING | 20 | — | Check file name (Checkmark output file for check data) |
| 2 | BKCP_MST_CMPATH | STRING | 66 | — | Checkmark application path (directory where Checkmark files reside) |
| 3 | BKCP_MST_COMMEX | STRING | 1 | — | Commission export flag: `Y` = include commission data in export |
| 4 | BKCP_MST_EFILE | STRING | 20 | — | Employee file name (employee master export file) |
| 5 | BKCP_MST_EXPATH | STRING | 66 | — | Export path (destination directory for exported files) |
| 6 | BKCP_MST_HFILE | STRING | 20 | — | History file name (previously-exported payroll archive) |
| 7 | BKCP_MST_IMPATH | STRING | 66 | — | Import path (source directory for importing Checkmark data back) |
| 8 | BKCP_MST_LABEX | STRING | 1 | — | Labor export flag: `Y` = include labor/direct-cost data in export |
| 9 | BKCP_MST_VFILE | STRING | 20 | — | Vendor file name (vendor/payee export for Checkmark accounts payable link) |

**Notes:**
- BKCPMSTR is a singleton config table (one record).
- The three path fields (CMPATH/EXPATH/IMPATH) define the Checkmark ↔ EvoERP file exchange locations.
- File name fields (CFILE/EFILE/HFILE/VFILE) store the flat-file names Checkmark expects.
- COMMEX and LABEX flags control whether optional data streams are included in the export.

**Confidence: 75/100** — table headers confirm "CHECK MARK PAYROLL" identity; field meanings
inferred from names + Checkmark integration context; actual file format and import/export
mechanics require tracing the PL-module RWN bytecode (encrypted).
