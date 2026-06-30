# MR — Material Requirements: Field Reference

Status: verified-schema

Source: `Evo-DBA_File_Fields 052421.xlsx`, sheet "Fields".
Field descriptions where provided by source; otherwise name-inferred.

---

## BKMRPFC
**FORECASTS**

Fields: 9

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKMRP_FC_CQTY | NUMERIC | 8 | 2 | — |
| 2 | BKMRP_FC_DATE | DATE | 4 | — | — |
| 3 | BKMRP_FC_DATE1 | DATE | 4 | — | — |
| 4 | BKMRP_FC_EXTRA | STRING | 25 | — | — |
| 5 | BKMRP_FC_FLAG | STRING | 1 | — | — |
| 6 | BKMRP_FC_NUM | NUMERIC | 8 | — | — |
| 7 | BKMRP_FC_OQTY | NUMERIC | 8 | 2 | — |
| 8 | BKMRP_FC_PART | STRING | 15 | — | — |
| 9 | BKMRP_FC_QTY | NUMERIC | 8 | 2 | — |

## BKMRPPO
**MRP TO PO CONVERSION FILE (Temporary)**

Fields: 16

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKMRP_PO_CONF | STRING | 1 | — | — |
| 2 | BKMRP_PO_DATE | DATE | 4 | — | — |
| 3 | BKMRP_PO_DONE | STRING | 10 | — | — |
| 4 | BKMRP_PO_ERD | DATE | 4 | — | — |
| 5 | BKMRP_PO_EST | STRING | 10 | — | — |
| 6 | BKMRP_PO_ESTLNE | NUMERIC | 8 | — | — |
| 7 | BKMRP_PO_EXTRA | STRING | 50 | — | — |
| 8 | BKMRP_PO_MTREC | INTEGER | 4 | — | — |
| 9 | BKMRP_PO_PART | STRING | 15 | — | — |
| 10 | BKMRP_PO_PLANR | STRING | 4 | — | — |
| 11 | BKMRP_PO_PRICE | NUMERIC | 8 | 4 | — |
| 12 | BKMRP_PO_QTY | NUMERIC | 8 | 2 | — |
| 13 | BKMRP_PO_UID | STRING | 20 | — | — |
| 14 | BKMRP_PO_VEND | STRING | 10 | — | — |
| 15 | BKMRP_PO_WOPRE | NUMERIC | 8 | — | — |
| 16 | BKMRP_PO_WOSUF | INTEGER | 2 | — | — |

## BKMRPSW
**TEMP FILE USED BY MRP**

Fields: 2

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKMRP_SW_PART | STRING | 15 | — | — |
| 2 | BKMRP_SW_SW | STRING | 1 | — | — |

## ISMRPFC
**MRP FORECAST**

Fields: 9

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKMRP_FC_CQTY | NUMERIC | 8 | 2 | — |
| 2 | BKMRP_FC_DATE | DATE | 4 | — | — |
| 3 | BKMRP_FC_DATE1 | DATE | 4 | — | — |
| 4 | BKMRP_FC_EXTRA | STRING | 25 | — | — |
| 5 | BKMRP_FC_FLAG | STRING | 1 | — | — |
| 6 | BKMRP_FC_NUM | NUMERIC | 8 | — | — |
| 7 | BKMRP_FC_OQTY | NUMERIC | 8 | 2 | — |
| 8 | BKMRP_FC_PART | STRING | 15 | — | — |
| 9 | BKMRP_FC_QTY | NUMERIC | 8 | 2 | — |

## ISSLSFC
**FORECAST**

Fields: 9

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKMRP_FC_CQTY | NUMERIC | 8 | 2 | — |
| 2 | BKMRP_FC_DATE | DATE | 4 | — | — |
| 3 | BKMRP_FC_DATE1 | DATE | 4 | — | — |
| 4 | BKMRP_FC_EXTRA | STRING | 25 | — | — |
| 5 | BKMRP_FC_FLAG | STRING | 1 | — | — |
| 6 | BKMRP_FC_NUM | NUMERIC | 8 | — | — |
| 7 | BKMRP_FC_OQTY | NUMERIC | 8 | 2 | — |
| 8 | BKMRP_FC_PART | STRING | 15 | — | — |
| 9 | BKMRP_FC_QTY | NUMERIC | 8 | 2 | — |

## MTMRP
**MATERIAL REQUIREMENTS (MRP) MASTER**

Fields: 12

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MTMRP_ACTION | STRING | 10 | — | Action |
| 2 | MTMRP_DATE | DATE | 4 | — | MRP Date |
| 3 | MTMRP_EXTRA | STRING | 50 | — | Extra |
| 4 | MTMRP_ONHAND | NUMERIC | 8 | 2 | MRP Quantity On-Hand |
| 5 | MTMRP_ORDER | STRING | 10 | — | Order Ref. |
| 6 | MTMRP_PARTNO | STRING | 15 | — | Part Number |
| 7 | MTMRP_PEGTO | STRING | 10 | — | Pegged To |
| 8 | MTMRP_PG_FDATE | DATE | 4 | — | Finish Date |
| 9 | MTMRP_PG_QTY | NUMERIC | 8 | 2 | Pegged Quantity |
| 10 | MTMRP_PG_SDATE | DATE | 4 | — | Start Date |
| 11 | MTMRP_QTY | NUMERIC | 8 | 2 | MRP Quantity |
| 12 | MTMRP_STARTDT | DATE | 4 | — | Start Date |

## SUMPNCUS
**MRP TEMP FILE**

Fields: 6

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | SUMPNCUS_COGS | NUMERIC | 8 | 2 | — |
| 2 | SUMPNCUS_CUST | STRING | 10 | — | — |
| 3 | SUMPNCUS_MONTH | INTEGER | 2 | — | — |
| 4 | SUMPNCUS_PARTNO | STRING | 15 | — | — |
| 5 | SUMPNCUS_SALES | NUMERIC | 8 | 4 | — |
| 6 | SUMPNCUS_YEAR | INTEGER | 2 | — | — |
