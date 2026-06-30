# SC — Scheduling: Field Reference

Status: verified-schema

Source: `Evo-DBA_File_Fields 052421.xlsx`, sheet "Fields".
Field descriptions where provided by source; otherwise name-inferred.

---

## ISHSERIA
**ARCHIVED SERIAL**

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

## ISSERCNT
**SERIAL NUMBER GENERATION MASTER**

Fields: 9

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_SERC_CLASS | STRING | 4 | — | — |
| 2 | IS_SERC_EXTRA | STRING | 100 | — | — |
| 3 | IS_SERC_ITEM | STRING | 15 | — | — |
| 4 | IS_SERC_L2 | INTEGER | 2 | — | — |
| 5 | IS_SERC_LAST | STRING | 25 | — | — |
| 6 | IS_SERC_LENG | STRING | 2 | — | — |
| 7 | IS_SERC_NUMBER | NUMERIC | 8 | — | — |
| 8 | IS_SERC_SPOS | INTEGER | 2 | — | — |
| 9 | IS_SERC_TOTAL | INTEGER | 2 | — | — |

## SERIAL
**SERIAL NUMBER MASTER**

Fields: 30

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MTSER_BIN | STRING | 15 | — | — |
| 2 | MTSER_CODE | STRING | 15 | — | Item Number |
| 3 | MTSER_CUSTCODE | STRING | 10 | — | Customer Code |
| 4 | MTSER_EXPDATE | DATE | 4 | — | Expiration Date |
| 5 | MTSER_EXTRA | STRING | 50 | — | Extra |
| 6 | MTSER_INRECCOST | NUMERIC | 8 | 4 | — |
| 7 | MTSER_INRECDATE | DATE | 4 | — | — |
| 8 | MTSER_INV | NUMERIC | 8 | — | — |
| 9 | MTSER_ISSCOST | NUMERIC | 8 | 4 | Issue Cost |
| 10 | MTSER_ISSDATE | DATE | 4 | — | Issue Date |
| 11 | MTSER_LOC | STRING | 10 | — | — |
| 12 | MTSER_LOT | STRING | 15 | — | Lot Number |
| 13 | MTSER_NOTES_1 | STRING | 30 | — | — |
| 14 | MTSER_NOTES_2 | STRING | 30 | — | — |
| 15 | MTSER_NOTES_3 | STRING | 30 | — | — |
| 16 | MTSER_NOTES_4 | STRING | 30 | — | — |
| 17 | MTSER_NOTES_5 | STRING | 30 | — | — |
| 18 | MTSER_ONHAND | NUMERIC | 8 | 2 | — |
| 19 | MTSER_PO | NUMERIC | 8 | — | PO Number |
| 20 | MTSER_POCOST | NUMERIC | 8 | 4 | — |
| 21 | MTSER_RECDATE | DATE | 4 | — | — |
| 22 | MTSER_RECDOC | NUMERIC | 8 | — | — |
| 23 | MTSER_SELLPRICE | NUMERIC | 8 | 4 | Sell Price |
| 24 | MTSER_SERIAL | STRING | 25 | — | Serail Number |
| 25 | MTSER_SHIPDATE | DATE | 4 | — | Ship Date |
| 26 | MTSER_SO | NUMERIC | 8 | — | — |
| 27 | MTSER_VENDOR | STRING | 10 | — | Vendor |
| 28 | MTSER_WO | NUMERIC | 8 | — | WO Prefix |
| 29 | MTSER_WOCODE | STRING | 15 | — | — |
| 30 | MTSER_WOSUF | INTEGER | 2 | — | WO Suffix |

## SERIALH
**ARCHIVED SERIAL NUMBERS**

Fields: 30

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MTSER_BIN | STRING | 15 | — | — |
| 2 | MTSER_CODE | STRING | 15 | — | Item Number |
| 3 | MTSER_CUSTCODE | STRING | 10 | — | Customer Code |
| 4 | MTSER_EXPDATE | DATE | 4 | — | Expiration Date |
| 5 | MTSER_EXTRA | STRING | 50 | — | Extra |
| 6 | MTSER_INRECCOST | NUMERIC | 8 | 4 | — |
| 7 | MTSER_INRECDATE | DATE | 4 | — | — |
| 8 | MTSER_INV | NUMERIC | 8 | — | — |
| 9 | MTSER_ISSCOST | NUMERIC | 8 | 4 | Issue Cost |
| 10 | MTSER_ISSDATE | DATE | 4 | — | Issue Date |
| 11 | MTSER_LOC | STRING | 10 | — | — |
| 12 | MTSER_LOT | STRING | 15 | — | Lot Number |
| 13 | MTSER_NOTES_1 | STRING | 30 | — | — |
| 14 | MTSER_NOTES_2 | STRING | 30 | — | — |
| 15 | MTSER_NOTES_3 | STRING | 30 | — | — |
| 16 | MTSER_NOTES_4 | STRING | 30 | — | — |
| 17 | MTSER_NOTES_5 | STRING | 30 | — | — |
| 18 | MTSER_ONHAND | NUMERIC | 8 | 2 | — |
| 19 | MTSER_PO | NUMERIC | 8 | — | PO Number |
| 20 | MTSER_POCOST | NUMERIC | 8 | 4 | — |
| 21 | MTSER_RECDATE | DATE | 4 | — | — |
| 22 | MTSER_RECDOC | NUMERIC | 8 | — | — |
| 23 | MTSER_SELLPRICE | NUMERIC | 8 | 4 | Sell Price |
| 24 | MTSER_SERIAL | STRING | 25 | — | Serail Number |
| 25 | MTSER_SHIPDATE | DATE | 4 | — | Ship Date |
| 26 | MTSER_SO | NUMERIC | 8 | — | — |
| 27 | MTSER_VENDOR | STRING | 10 | — | Vendor |
| 28 | MTSER_WO | NUMERIC | 8 | — | WO Prefix |
| 29 | MTSER_WOCODE | STRING | 15 | — | — |
| 30 | MTSER_WOSUF | INTEGER | 2 | — | WO Suffix |
