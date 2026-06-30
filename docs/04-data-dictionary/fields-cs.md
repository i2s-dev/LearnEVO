# CS — Customer Service: Field Reference

Status: verified-schema

Source: `Evo-DBA_File_Fields 052421.xlsx`, sheet "Fields".
Field descriptions where provided by source; otherwise name-inferred.

---

## BKARINVI
**COMMISSIONS**

Fields: 16

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKAR_INVI_COMM_1 | NUMERIC | 8 | 4 | — |
| 2 | BKAR_INVI_COMM_2 | NUMERIC | 8 | 4 | — |
| 3 | BKAR_INVI_COOP | NUMERIC | 8 | 2 | — |
| 4 | BKAR_INVI_ESD | DATE | 4 | — | Estimated Ship Date |
| 5 | BKAR_INVI_EXTRM | NUMERIC | 8 | 2 | — |
| 6 | BKAR_INVI_FRGHT | NUMERIC | 8 | 2 | Freight |
| 7 | BKAR_INVI_INVNM | NUMERIC | 8 | — | Invoice Number |
| 8 | BKAR_INVI_ITYPE | STRING | 1 | — | Item Type |
| 9 | BKAR_INVI_PCODE | STRING | 15 | — | Part Code |
| 10 | BKAR_INVI_PCOGS | NUMERIC | 8 | 2 | COGS |
| 11 | BKAR_INVI_PDISC | NUMERIC | 8 | 2 | Discount |
| 12 | BKAR_INVI_PEXT | NUMERIC | 8 | 2 | Extended Price |
| 13 | BKAR_INVI_PPRCE | NUMERIC | 8 | 4 | Price |
| 14 | BKAR_INVI_PQTY | NUMERIC | 8 | 2 | Quantity |
| 15 | BKAR_INVI_SONUM | NUMERIC | 8 | — | Sales Order Number |
| 16 | BKAR_INVI_TAX | NUMERIC | 8 | 2 | — |

## BKPRACOM
**ARCHIVED COMMISSION DETAIL**

Fields: 12

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKPR_COMM_AMTPD | NUMERIC | 8 | 2 | — |
| 2 | BKPR_COMM_CCODE | STRING | 10 | — | — |
| 3 | BKPR_COMM_COMM | NUMERIC | 8 | 2 | — |
| 4 | BKPR_COMM_EXTRA | STRING | 25 | — | — |
| 5 | BKPR_COMM_INVDT | DATE | 4 | — | — |
| 6 | BKPR_COMM_INVNM | NUMERIC | 8 | — | — |
| 7 | BKPR_COMM_PAYDT | DATE | 4 | — | — |
| 8 | BKPR_COMM_PCODE | STRING | 15 | — | — |
| 9 | BKPR_COMM_PD_ON | NUMERIC | 8 | 2 | — |
| 10 | BKPR_COMM_SLSP | INTEGER | 2 | — | — |
| 11 | BKPR_COMM_TDATE | DATE | 4 | — | — |
| 12 | BKPR_COMM_ULID | NUMERIC | 8 | 4 | — |

## BKPRAGNT
**AGENTS**

Fields: 4

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKPR_AGNT_CODE | STRING | 10 | — | Vendor Code |
| 2 | BKPR_AGNT_GLACT | STRING | 10 | — | GL Account |
| 3 | BKPR_AGNT_GLDPT | STRING | 4 | — | GL Department |
| 4 | BKPR_AGNT_NUM | INTEGER | 2 | — | Agent number |

## BKPRCOMM
**COMMISSIONS**

Fields: 12

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKPR_COMM_AMTPD | NUMERIC | 8 | 2 | — |
| 2 | BKPR_COMM_CCODE | STRING | 10 | — | — |
| 3 | BKPR_COMM_COMM | NUMERIC | 8 | 2 | — |
| 4 | BKPR_COMM_EXTRA | STRING | 25 | — | — |
| 5 | BKPR_COMM_INVDT | DATE | 4 | — | — |
| 6 | BKPR_COMM_INVNM | NUMERIC | 8 | — | — |
| 7 | BKPR_COMM_PAYDT | DATE | 4 | — | — |
| 8 | BKPR_COMM_PCODE | STRING | 15 | — | — |
| 9 | BKPR_COMM_PD_ON | NUMERIC | 8 | 2 | — |
| 10 | BKPR_COMM_SLSP | INTEGER | 2 | — | — |
| 11 | BKPR_COMM_TDATE | DATE | 4 | — | — |
| 12 | BKPR_COMM_ULID | NUMERIC | 8 | 4 | — |

## BKPRHCOM
**POSTED COMMISSION DETAIL**

Fields: 12

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKPR_COMM_AMTPD | NUMERIC | 8 | 2 | — |
| 2 | BKPR_COMM_CCODE | STRING | 10 | — | — |
| 3 | BKPR_COMM_COMM | NUMERIC | 8 | 2 | — |
| 4 | BKPR_COMM_EXTRA | STRING | 25 | — | — |
| 5 | BKPR_COMM_INVDT | DATE | 4 | — | — |
| 6 | BKPR_COMM_INVNM | NUMERIC | 8 | — | — |
| 7 | BKPR_COMM_PAYDT | DATE | 4 | — | — |
| 8 | BKPR_COMM_PCODE | STRING | 15 | — | — |
| 9 | BKPR_COMM_PD_ON | NUMERIC | 8 | 2 | — |
| 10 | BKPR_COMM_SLSP | INTEGER | 2 | — | — |
| 11 | BKPR_COMM_TDATE | DATE | 4 | — | — |
| 12 | BKPR_COMM_ULID | NUMERIC | 8 | 4 | — |

## BKPRSALE
**SALESPERSON MASTER**

Fields: 86

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKPR_SLS_CLASS_1 | STRING | 2 | — | — |
| 2 | BKPR_SLS_CLASS_2 | STRING | 2 | — | — |
| 3 | BKPR_SLS_COGS_1 | NUMERIC | 8 | 2 | — |
| 4 | BKPR_SLS_COGS_10 | NUMERIC | 8 | 2 | — |
| 5 | BKPR_SLS_COGS_11 | NUMERIC | 8 | 2 | — |
| 6 | BKPR_SLS_COGS_12 | NUMERIC | 8 | 2 | — |
| 7 | BKPR_SLS_COGS_2 | NUMERIC | 8 | 2 | — |
| 8 | BKPR_SLS_COGS_3 | NUMERIC | 8 | 2 | — |
| 9 | BKPR_SLS_COGS_4 | NUMERIC | 8 | 2 | — |
| 10 | BKPR_SLS_COGS_5 | NUMERIC | 8 | 2 | — |
| 11 | BKPR_SLS_COGS_6 | NUMERIC | 8 | 2 | — |
| 12 | BKPR_SLS_COGS_7 | NUMERIC | 8 | 2 | — |
| 13 | BKPR_SLS_COGS_8 | NUMERIC | 8 | 2 | — |
| 14 | BKPR_SLS_COGS_9 | NUMERIC | 8 | 2 | — |
| 15 | BKPR_SLS_COMM_1 | NUMERIC | 8 | 2 | — |
| 16 | BKPR_SLS_COMM_10 | NUMERIC | 8 | 2 | — |
| 17 | BKPR_SLS_COMM_11 | NUMERIC | 8 | 2 | — |
| 18 | BKPR_SLS_COMM_12 | NUMERIC | 8 | 2 | — |
| 19 | BKPR_SLS_COMM_2 | NUMERIC | 8 | 2 | — |
| 20 | BKPR_SLS_COMM_3 | NUMERIC | 8 | 2 | — |
| 21 | BKPR_SLS_COMM_4 | NUMERIC | 8 | 2 | — |
| 22 | BKPR_SLS_COMM_5 | NUMERIC | 8 | 2 | — |
| 23 | BKPR_SLS_COMM_6 | NUMERIC | 8 | 2 | — |
| 24 | BKPR_SLS_COMM_7 | NUMERIC | 8 | 2 | — |
| 25 | BKPR_SLS_COMM_8 | NUMERIC | 8 | 2 | — |
| 26 | BKPR_SLS_COMM_9 | NUMERIC | 8 | 2 | — |
| 27 | BKPR_SLS_EMPNUM | INTEGER | 2 | — | — |
| 28 | BKPR_SLS_EXPACT | STRING | 10 | — | — |
| 29 | BKPR_SLS_EXPDPT | STRING | 4 | — | — |
| 30 | BKPR_SLS_EXTRA | STRING | 100 | — | — |
| 31 | BKPR_SLS_FNMI | STRING | 25 | — | — |
| 32 | BKPR_SLS_GROSS_1 | NUMERIC | 8 | 2 | — |
| 33 | BKPR_SLS_GROSS_10 | NUMERIC | 8 | 2 | — |
| 34 | BKPR_SLS_GROSS_11 | NUMERIC | 8 | 2 | — |
| 35 | BKPR_SLS_GROSS_12 | NUMERIC | 8 | 2 | — |
| 36 | BKPR_SLS_GROSS_2 | NUMERIC | 8 | 2 | — |
| 37 | BKPR_SLS_GROSS_3 | NUMERIC | 8 | 2 | — |
| 38 | BKPR_SLS_GROSS_4 | NUMERIC | 8 | 2 | — |
| 39 | BKPR_SLS_GROSS_5 | NUMERIC | 8 | 2 | — |
| 40 | BKPR_SLS_GROSS_6 | NUMERIC | 8 | 2 | — |
| 41 | BKPR_SLS_GROSS_7 | NUMERIC | 8 | 2 | — |
| 42 | BKPR_SLS_GROSS_8 | NUMERIC | 8 | 2 | — |
| 43 | BKPR_SLS_GROSS_9 | NUMERIC | 8 | 2 | — |
| 44 | BKPR_SLS_HOW_1 | STRING | 1 | — | — |
| 45 | BKPR_SLS_HOW_2 | STRING | 1 | — | — |
| 46 | BKPR_SLS_LNME | STRING | 25 | — | — |
| 47 | BKPR_SLS_PAID_1 | NUMERIC | 8 | 2 | — |
| 48 | BKPR_SLS_PAID_10 | NUMERIC | 8 | 2 | — |
| 49 | BKPR_SLS_PAID_11 | NUMERIC | 8 | 2 | — |
| 50 | BKPR_SLS_PAID_12 | NUMERIC | 8 | 2 | — |
| 51 | BKPR_SLS_PAID_2 | NUMERIC | 8 | 2 | — |
| 52 | BKPR_SLS_PAID_3 | NUMERIC | 8 | 2 | — |
| 53 | BKPR_SLS_PAID_4 | NUMERIC | 8 | 2 | — |
| 54 | BKPR_SLS_PAID_5 | NUMERIC | 8 | 2 | — |
| 55 | BKPR_SLS_PAID_6 | NUMERIC | 8 | 2 | — |
| 56 | BKPR_SLS_PAID_7 | NUMERIC | 8 | 2 | — |
| 57 | BKPR_SLS_PAID_8 | NUMERIC | 8 | 2 | — |
| 58 | BKPR_SLS_PAID_9 | NUMERIC | 8 | 2 | — |
| 59 | BKPR_SLS_QUOTA_1 | NUMERIC | 8 | 2 | — |
| 60 | BKPR_SLS_QUOTA_10 | NUMERIC | 8 | 2 | — |
| 61 | BKPR_SLS_QUOTA_11 | NUMERIC | 8 | 2 | — |
| 62 | BKPR_SLS_QUOTA_12 | NUMERIC | 8 | 2 | — |
| 63 | BKPR_SLS_QUOTA_2 | NUMERIC | 8 | 2 | — |
| 64 | BKPR_SLS_QUOTA_3 | NUMERIC | 8 | 2 | — |
| 65 | BKPR_SLS_QUOTA_4 | NUMERIC | 8 | 2 | — |
| 66 | BKPR_SLS_QUOTA_5 | NUMERIC | 8 | 2 | — |
| 67 | BKPR_SLS_QUOTA_6 | NUMERIC | 8 | 2 | — |
| 68 | BKPR_SLS_QUOTA_7 | NUMERIC | 8 | 2 | — |
| 69 | BKPR_SLS_QUOTA_8 | NUMERIC | 8 | 2 | — |
| 70 | BKPR_SLS_QUOTA_9 | NUMERIC | 8 | 2 | — |
| 71 | BKPR_SLS_RATE_1 | NUMERIC | 8 | 4 | — |
| 72 | BKPR_SLS_RATE_2 | NUMERIC | 8 | 4 | — |
| 73 | BKPR_SLS_RCPTS_1 | NUMERIC | 8 | 2 | — |
| 74 | BKPR_SLS_RCPTS_10 | NUMERIC | 8 | 2 | — |
| 75 | BKPR_SLS_RCPTS_11 | NUMERIC | 8 | 2 | — |
| 76 | BKPR_SLS_RCPTS_12 | NUMERIC | 8 | 2 | — |
| 77 | BKPR_SLS_RCPTS_2 | NUMERIC | 8 | 2 | — |
| 78 | BKPR_SLS_RCPTS_3 | NUMERIC | 8 | 2 | — |
| 79 | BKPR_SLS_RCPTS_4 | NUMERIC | 8 | 2 | — |
| 80 | BKPR_SLS_RCPTS_5 | NUMERIC | 8 | 2 | — |
| 81 | BKPR_SLS_RCPTS_6 | NUMERIC | 8 | 2 | — |
| 82 | BKPR_SLS_RCPTS_7 | NUMERIC | 8 | 2 | — |
| 83 | BKPR_SLS_RCPTS_8 | NUMERIC | 8 | 2 | — |
| 84 | BKPR_SLS_RCPTS_9 | NUMERIC | 8 | 2 | — |
| 85 | BKPR_SLS_WHEN_1 | STRING | 1 | — | — |
| 86 | BKPR_SLS_WHEN_2 | STRING | 1 | — | — |

## ISARAIVI
**ARCHIVED COMMISSION DETAIL**

Fields: 16

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKAR_INVI_COMM_1 | NUMERIC | 8 | 4 | — |
| 2 | BKAR_INVI_COMM_2 | NUMERIC | 8 | 4 | — |
| 3 | BKAR_INVI_COOP | NUMERIC | 8 | 2 | — |
| 4 | BKAR_INVI_ESD | DATE | 4 | — | Estimated Ship Date |
| 5 | BKAR_INVI_EXTRM | NUMERIC | 8 | 2 | — |
| 6 | BKAR_INVI_FRGHT | NUMERIC | 8 | 2 | Freight |
| 7 | BKAR_INVI_INVNM | NUMERIC | 8 | — | Invoice Number |
| 8 | BKAR_INVI_ITYPE | STRING | 1 | — | Item Type |
| 9 | BKAR_INVI_PCODE | STRING | 15 | — | Part Code |
| 10 | BKAR_INVI_PCOGS | NUMERIC | 8 | 2 | COGS |
| 11 | BKAR_INVI_PDISC | NUMERIC | 8 | 2 | Discount |
| 12 | BKAR_INVI_PEXT | NUMERIC | 8 | 2 | Extended Price |
| 13 | BKAR_INVI_PPRCE | NUMERIC | 8 | 4 | Price |
| 14 | BKAR_INVI_PQTY | NUMERIC | 8 | 2 | Quantity |
| 15 | BKAR_INVI_SONUM | NUMERIC | 8 | — | Sales Order Number |
| 16 | BKAR_INVI_TAX | NUMERIC | 8 | 2 | — |

## ISPRSALE
**SALESPERSON LIST EXTENDED COMMISSION**

Fields: 86

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKPR_SLS_CLASS_1 | STRING | 2 | — | — |
| 2 | BKPR_SLS_CLASS_2 | STRING | 2 | — | — |
| 3 | BKPR_SLS_COGS_1 | NUMERIC | 8 | 2 | — |
| 4 | BKPR_SLS_COGS_10 | NUMERIC | 8 | 2 | — |
| 5 | BKPR_SLS_COGS_11 | NUMERIC | 8 | 2 | — |
| 6 | BKPR_SLS_COGS_12 | NUMERIC | 8 | 2 | — |
| 7 | BKPR_SLS_COGS_2 | NUMERIC | 8 | 2 | — |
| 8 | BKPR_SLS_COGS_3 | NUMERIC | 8 | 2 | — |
| 9 | BKPR_SLS_COGS_4 | NUMERIC | 8 | 2 | — |
| 10 | BKPR_SLS_COGS_5 | NUMERIC | 8 | 2 | — |
| 11 | BKPR_SLS_COGS_6 | NUMERIC | 8 | 2 | — |
| 12 | BKPR_SLS_COGS_7 | NUMERIC | 8 | 2 | — |
| 13 | BKPR_SLS_COGS_8 | NUMERIC | 8 | 2 | — |
| 14 | BKPR_SLS_COGS_9 | NUMERIC | 8 | 2 | — |
| 15 | BKPR_SLS_COMM_1 | NUMERIC | 8 | 2 | — |
| 16 | BKPR_SLS_COMM_10 | NUMERIC | 8 | 2 | — |
| 17 | BKPR_SLS_COMM_11 | NUMERIC | 8 | 2 | — |
| 18 | BKPR_SLS_COMM_12 | NUMERIC | 8 | 2 | — |
| 19 | BKPR_SLS_COMM_2 | NUMERIC | 8 | 2 | — |
| 20 | BKPR_SLS_COMM_3 | NUMERIC | 8 | 2 | — |
| 21 | BKPR_SLS_COMM_4 | NUMERIC | 8 | 2 | — |
| 22 | BKPR_SLS_COMM_5 | NUMERIC | 8 | 2 | — |
| 23 | BKPR_SLS_COMM_6 | NUMERIC | 8 | 2 | — |
| 24 | BKPR_SLS_COMM_7 | NUMERIC | 8 | 2 | — |
| 25 | BKPR_SLS_COMM_8 | NUMERIC | 8 | 2 | — |
| 26 | BKPR_SLS_COMM_9 | NUMERIC | 8 | 2 | — |
| 27 | BKPR_SLS_EMPNUM | INTEGER | 2 | — | — |
| 28 | BKPR_SLS_EXPACT | STRING | 10 | — | — |
| 29 | BKPR_SLS_EXPDPT | STRING | 4 | — | — |
| 30 | BKPR_SLS_EXTRA | STRING | 100 | — | — |
| 31 | BKPR_SLS_FNMI | STRING | 25 | — | — |
| 32 | BKPR_SLS_GROSS_1 | NUMERIC | 8 | 2 | — |
| 33 | BKPR_SLS_GROSS_10 | NUMERIC | 8 | 2 | — |
| 34 | BKPR_SLS_GROSS_11 | NUMERIC | 8 | 2 | — |
| 35 | BKPR_SLS_GROSS_12 | NUMERIC | 8 | 2 | — |
| 36 | BKPR_SLS_GROSS_2 | NUMERIC | 8 | 2 | — |
| 37 | BKPR_SLS_GROSS_3 | NUMERIC | 8 | 2 | — |
| 38 | BKPR_SLS_GROSS_4 | NUMERIC | 8 | 2 | — |
| 39 | BKPR_SLS_GROSS_5 | NUMERIC | 8 | 2 | — |
| 40 | BKPR_SLS_GROSS_6 | NUMERIC | 8 | 2 | — |
| 41 | BKPR_SLS_GROSS_7 | NUMERIC | 8 | 2 | — |
| 42 | BKPR_SLS_GROSS_8 | NUMERIC | 8 | 2 | — |
| 43 | BKPR_SLS_GROSS_9 | NUMERIC | 8 | 2 | — |
| 44 | BKPR_SLS_HOW_1 | STRING | 1 | — | — |
| 45 | BKPR_SLS_HOW_2 | STRING | 1 | — | — |
| 46 | BKPR_SLS_LNME | STRING | 25 | — | — |
| 47 | BKPR_SLS_PAID_1 | NUMERIC | 8 | 2 | — |
| 48 | BKPR_SLS_PAID_10 | NUMERIC | 8 | 2 | — |
| 49 | BKPR_SLS_PAID_11 | NUMERIC | 8 | 2 | — |
| 50 | BKPR_SLS_PAID_12 | NUMERIC | 8 | 2 | — |
| 51 | BKPR_SLS_PAID_2 | NUMERIC | 8 | 2 | — |
| 52 | BKPR_SLS_PAID_3 | NUMERIC | 8 | 2 | — |
| 53 | BKPR_SLS_PAID_4 | NUMERIC | 8 | 2 | — |
| 54 | BKPR_SLS_PAID_5 | NUMERIC | 8 | 2 | — |
| 55 | BKPR_SLS_PAID_6 | NUMERIC | 8 | 2 | — |
| 56 | BKPR_SLS_PAID_7 | NUMERIC | 8 | 2 | — |
| 57 | BKPR_SLS_PAID_8 | NUMERIC | 8 | 2 | — |
| 58 | BKPR_SLS_PAID_9 | NUMERIC | 8 | 2 | — |
| 59 | BKPR_SLS_QUOTA_1 | NUMERIC | 8 | 2 | — |
| 60 | BKPR_SLS_QUOTA_10 | NUMERIC | 8 | 2 | — |
| 61 | BKPR_SLS_QUOTA_11 | NUMERIC | 8 | 2 | — |
| 62 | BKPR_SLS_QUOTA_12 | NUMERIC | 8 | 2 | — |
| 63 | BKPR_SLS_QUOTA_2 | NUMERIC | 8 | 2 | — |
| 64 | BKPR_SLS_QUOTA_3 | NUMERIC | 8 | 2 | — |
| 65 | BKPR_SLS_QUOTA_4 | NUMERIC | 8 | 2 | — |
| 66 | BKPR_SLS_QUOTA_5 | NUMERIC | 8 | 2 | — |
| 67 | BKPR_SLS_QUOTA_6 | NUMERIC | 8 | 2 | — |
| 68 | BKPR_SLS_QUOTA_7 | NUMERIC | 8 | 2 | — |
| 69 | BKPR_SLS_QUOTA_8 | NUMERIC | 8 | 2 | — |
| 70 | BKPR_SLS_QUOTA_9 | NUMERIC | 8 | 2 | — |
| 71 | BKPR_SLS_RATE_1 | NUMERIC | 8 | 4 | — |
| 72 | BKPR_SLS_RATE_2 | NUMERIC | 8 | 4 | — |
| 73 | BKPR_SLS_RCPTS_1 | NUMERIC | 8 | 2 | — |
| 74 | BKPR_SLS_RCPTS_10 | NUMERIC | 8 | 2 | — |
| 75 | BKPR_SLS_RCPTS_11 | NUMERIC | 8 | 2 | — |
| 76 | BKPR_SLS_RCPTS_12 | NUMERIC | 8 | 2 | — |
| 77 | BKPR_SLS_RCPTS_2 | NUMERIC | 8 | 2 | — |
| 78 | BKPR_SLS_RCPTS_3 | NUMERIC | 8 | 2 | — |
| 79 | BKPR_SLS_RCPTS_4 | NUMERIC | 8 | 2 | — |
| 80 | BKPR_SLS_RCPTS_5 | NUMERIC | 8 | 2 | — |
| 81 | BKPR_SLS_RCPTS_6 | NUMERIC | 8 | 2 | — |
| 82 | BKPR_SLS_RCPTS_7 | NUMERIC | 8 | 2 | — |
| 83 | BKPR_SLS_RCPTS_8 | NUMERIC | 8 | 2 | — |
| 84 | BKPR_SLS_RCPTS_9 | NUMERIC | 8 | 2 | — |
| 85 | BKPR_SLS_WHEN_1 | STRING | 1 | — | — |
| 86 | BKPR_SLS_WHEN_2 | STRING | 1 | — | — |

## ISREPLNK
**EXTENDED COMMISSION REP ASSIGNMENT**

Fields: 10

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISREP_LNK_CLASS | STRING | 4 | — | — |
| 2 | ISREP_LNK_COMM^ | NUMERIC | 8 | 4 | — |
| 3 | ISREP_LNK_CUST | STRING | 10 | — | — |
| 4 | ISREP_LNK_DATE | DATE | 4 | — | — |
| 5 | ISREP_LNK_EDATE | DATE | 4 | — | — |
| 6 | ISREP_LNK_EXTRA | STRING | 100 | — | — |
| 7 | ISREP_LNK_ITEM | STRING | 15 | — | — |
| 8 | ISREP_LNK_LABEL | STRING | 5 | — | — |
| 9 | ISREP_LNK_REPNM | INTEGER | 2 | — | — |
| 10 | ISREP_LNK_SDATE | DATE | 4 | — | — |

## ISREPORD
**EXTENDED COMMISSION LINE ITEM COMMISIONS**

Fields: 15

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISREP_ORD_AMT | NUMERIC | 8 | 2 | — |
| 2 | ISREP_ORD_AMTRM | NUMERIC | 8 | 2 | — |
| 3 | ISREP_ORD_CBK | STRING | 1 | — | — |
| 4 | ISREP_ORD_CMAMT | NUMERIC | 8 | 2 | — |
| 5 | ISREP_ORD_COMPR | NUMERIC | 8 | 4 | — |
| 6 | ISREP_ORD_CUST | STRING | 10 | — | — |
| 7 | ISREP_ORD_EXTRA | STRING | 100 | — | — |
| 8 | ISREP_ORD_INVDT | DATE | 4 | — | — |
| 9 | ISREP_ORD_INVNM | NUMERIC | 8 | — | — |
| 10 | ISREP_ORD_PAYDT | DATE | 4 | — | — |
| 11 | ISREP_ORD_PCODE | STRING | 15 | — | — |
| 12 | ISREP_ORD_REPNM | INTEGER | 2 | — | — |
| 13 | ISREP_ORD_REPWH | STRING | 1 | — | — |
| 14 | ISREP_ORD_SONUM | NUMERIC | 8 | — | — |
| 15 | ISREP_ORD_ULID | NUMERIC | 8 | 4 | — |
