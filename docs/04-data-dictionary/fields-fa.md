# FA — Fixed Assets: Field Reference

Status: verified-schema

Source: `Evo-DBA_File_Fields 052421.xlsx`, sheet "Fields".
Field descriptions where provided by source; otherwise name-inferred.

---

## ISFXASST
**FIXED ASSET MASTER**

Fields: 23

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_FXA_ACCUMDEP | NUMERIC | 8 | 2 | — |
| 2 | IS_FXA_ACDEPA | STRING | 10 | — | — |
| 3 | IS_FXA_ACDEPD | STRING | 4 | — | — |
| 4 | IS_FXA_CSTBAS | NUMERIC | 8 | 2 | — |
| 5 | IS_FXA_DEPEXPA | STRING | 10 | — | — |
| 6 | IS_FXA_DEPEXPD | STRING | 4 | — | — |
| 7 | IS_FXA_DESC | STRING | 30 | — | — |
| 8 | IS_FXA_DESC2 | STRING | 30 | — | — |
| 9 | IS_FXA_EDATE | DATE | 4 | — | — |
| 10 | IS_FXA_EXTRA | STRING | 100 | — | — |
| 11 | IS_FXA_GLA | STRING | 10 | — | — |
| 12 | IS_FXA_GLD | STRING | 4 | — | — |
| 13 | IS_FXA_LDEPAMT | NUMERIC | 8 | 2 | — |
| 14 | IS_FXA_LDEPDATE | DATE | 4 | — | — |
| 15 | IS_FXA_LDEPPERC | NUMERIC | 8 | 8 | — |
| 16 | IS_FXA_LIFE | NUMERIC | 8 | — | — |
| 17 | IS_FXA_METH | STRING | 30 | — | — |
| 18 | IS_FXA_NUMBER | NUMERIC | 8 | — | — |
| 19 | IS_FXA_RESVAL | NUMERIC | 8 | 2 | — |
| 20 | IS_FXA_SDATE | DATE | 4 | — | — |
| 21 | IS_FXA_SERIAL | STRING | 30 | — | — |
| 22 | IS_FXA_SOLD | NUMERIC | 8 | 2 | — |
| 23 | IS_FXA_TYPE | STRING | 30 | — | — |

## ISFXATRN
**FIXED ASSET TRANSACTIONS**

Fields: 12

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_FXT_ACDEPA | STRING | 10 | — | — |
| 2 | IS_FXT_ACDEPD | STRING | 4 | — | — |
| 3 | IS_FXT_AMOUNT | NUMERIC | 8 | 2 | — |
| 4 | IS_FXT_AUDIT | STRING | 25 | — | — |
| 5 | IS_FXT_DATE | DATE | 4 | — | — |
| 6 | IS_FXT_DEPEXPA | STRING | 10 | — | — |
| 7 | IS_FXT_DEPEXPD | STRING | 4 | — | — |
| 8 | IS_FXT_EXTRA | STRING | 100 | — | — |
| 9 | IS_FXT_NETAVAL | NUMERIC | 8 | 2 | — |
| 10 | IS_FXT_NUMBER | NUMERIC | 8 | — | — |
| 11 | IS_FXT_PERC | NUMERIC | 8 | 8 | — |
| 12 | IS_FXT_POSTED | STRING | 1 | — | — |
