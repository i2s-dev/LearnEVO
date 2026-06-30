# LC — Lot Control: Field Reference

Status: verified-schema

Source: `Evo-DBA_File_Fields 052421.xlsx`, sheet "Fields".
Field descriptions where provided by source; otherwise name-inferred.

---

## ISBINLOT
**LOT/BIN DETAIL**

Fields: 11

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_BINLOT_BIN | STRING | 15 | — | — |
| 2 | IS_BINLOT_DATE | DATE | 4 | — | — |
| 3 | IS_BINLOT_DFLT | STRING | 1 | — | — |
| 4 | IS_BINLOT_EXTRA | STRING | 50 | — | — |
| 5 | IS_BINLOT_FLAG | STRING | 1 | — | — |
| 6 | IS_BINLOT_ITEM | STRING | 15 | — | — |
| 7 | IS_BINLOT_LOC | STRING | 10 | — | — |
| 8 | IS_BINLOT_LOT | STRING | 15 | — | — |
| 9 | IS_BINLOT_TMPPO | STRING | 40 | — | — |
| 10 | IS_BINLOT_TMPSO | STRING | 40 | — | — |
| 11 | IS_BINLOT_UOH | NUMERIC | 8 | 2 | — |

## ISHLOTS
**ARCHIVED LOTS**

Fields: 11

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_SER_ADATE | DATE | 4 | — | — |
| 2 | IS_SER_CDESC | STRING | 30 | — | — |
| 3 | IS_SER_COMP | STRING | 15 | — | — |
| 4 | IS_SER_CSERIAL | STRING | 25 | — | — |
| 5 | IS_SER_EXRA | STRING | 100 | — | — |
| 6 | IS_SER_FDATE | DATE | 4 | — | — |
| 7 | IS_SER_PARENT | STRING | 15 | — | — |
| 8 | IS_SER_PDESC | STRING | 30 | — | — |
| 9 | IS_SER_PSERIAL | STRING | 25 | — | — |
| 10 | IS_SER_WOPRE | NUMERIC | 8 | — | — |
| 11 | IS_SER_WOSUF | INTEGER | 2 | — | — |

## LOT
**LOT CONTROL DETAIL**

Fields: 25

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MTLOT_BEGIN | NUMERIC | 8 | 7 | — |
| 2 | MTLOT_CODE | STRING | 15 | — | — |
| 3 | MTLOT_EXPDATE | DATE | 4 | — | — |
| 4 | MTLOT_EXTRA | STRING | 50 | — | — |
| 5 | MTLOT_INRECDATE | DATE | 4 | — | — |
| 6 | MTLOT_LOC | STRING | 10 | — | — |
| 7 | MTLOT_LOT | STRING | 15 | — | — |
| 8 | MTLOT_MAXOUT | NUMERIC | 8 | 7 | — |
| 9 | MTLOT_NOTES_1 | STRING | 45 | — | — |
| 10 | MTLOT_NOTES_2 | STRING | 45 | — | — |
| 11 | MTLOT_NOTES_3 | STRING | 45 | — | — |
| 12 | MTLOT_NOTES_4 | STRING | 45 | — | — |
| 13 | MTLOT_NOTES_5 | STRING | 45 | — | — |
| 14 | MTLOT_ONHAND | NUMERIC | 8 | 2 | — |
| 15 | MTLOT_OUT | NUMERIC | 8 | 7 | — |
| 16 | MTLOT_PO | NUMERIC | 8 | — | — |
| 17 | MTLOT_POCOST | NUMERIC | 8 | 4 | — |
| 18 | MTLOT_RECDATE | DATE | 4 | — | — |
| 19 | MTLOT_RECDOC | NUMERIC | 8 | — | — |
| 20 | MTLOT_RECQTY | NUMERIC | 8 | 2 | — |
| 21 | MTLOT_VENDOR | STRING | 10 | — | — |
| 22 | MTLOT_WO | NUMERIC | 8 | — | — |
| 23 | MTLOT_WOCOST | NUMERIC | 8 | 4 | — |
| 24 | MTLOT_WOQTY | NUMERIC | 8 | 2 | — |
| 25 | MTLOT_WOSUF | INTEGER | 2 | — | — |
