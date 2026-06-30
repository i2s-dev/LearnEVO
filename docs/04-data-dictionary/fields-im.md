# IM — Import: Field Reference

Status: verified-schema

Source: `Evo-DBA_File_Fields 052421.xlsx`, sheet "Fields".
Field descriptions where provided by source; otherwise name-inferred.

---

## ISBROKER
**CUSTOMS BROKER FEES**

Fields: 4

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISIS_BRK_CODE | STRING | 10 | — | — |
| 2 | ISIS_BRK_FLAT | NUMERIC | 8 | 2 | — |
| 3 | ISIS_BRK_PERC | NUMERIC | 8 | 6 | — |
| 4 | ISIS_BRK_TYPE | STRING | 1 | — | — |

## ISDUTY
**DUTY CODES**

Fields: 2

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISIS_DUTY_DCODE | STRING | 6 | — | — |
| 2 | ISIS_DUTY_PERC | NUMERIC | 8 | 3 | — |

## ISIS
**INTERNATIONAL DEFAULTS**

Fields: 23

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_AUTO_TAX_CAL | STRING | 1 | — | — |
| 2 | IS_COMM_PRICE | STRING | 1 | — | — |
| 3 | IS_CUR_CVT | STRING | 1 | — | — |
| 4 | IS_DEMO | DATE | 4 | — | — |
| 5 | IS_EZPAY | STRING | 1 | — | — |
| 6 | IS_IMAGING | STRING | 1 | — | — |
| 7 | IS_LANDED_COST | STRING | 1 | — | — |
| 8 | IS_MULTI_CPAY | STRING | 1 | — | — |
| 9 | IS_MULTI_CURR | STRING | 1 | — | — |
| 10 | IS_PIC_PATH | STRING | 20 | — | — |
| 11 | IS_PO_TAX | STRING | 1 | — | — |
| 12 | IS_RETAIL_PRICE | STRING | 1 | — | — |
| 13 | IS_RMA | STRING | 1 | — | — |
| 14 | IS_SPEC_SUP | STRING | 1 | — | — |
| 15 | IS_SPEC_SUPF | INTEGER | 2 | — | — |
| 16 | IS_SPEC_SUPT | INTEGER | 2 | — | — |
| 17 | IS_TAX | STRING | 1 | — | — |
| 18 | IS_TAX_CVT | STRING | 1 | — | — |
| 19 | IS_TAX_FRM | STRING | 1 | — | — |
| 20 | IS_TAX_IN | STRING | 1 | — | — |
| 21 | IS_UPC | STRING | 1 | — | — |
| 22 | IS_UPC_1 | STRING | 6 | — | — |
| 23 | IS_UPC_2 | STRING | 5 | — | — |

## ISLANDF
**LANDED COST DEFAULTS**

Fields: 6

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISIS_LND_GLACF | STRING | 10 | — | — |
| 2 | ISIS_LND_GLADT | STRING | 10 | — | — |
| 3 | ISIS_LND_GLAFR | STRING | 10 | — | — |
| 4 | ISIS_LND_GLDCF | STRING | 4 | — | — |
| 5 | ISIS_LND_GLDDT | STRING | 4 | — | — |
| 6 | ISIS_LND_GLDFR | STRING | 4 | — | — |

## ISMCF
**MULTIPLE CURRENCY MASTER**

Fields: 49

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISIS_MCF_AMTAD | NUMERIC | 8 | 2 | — |
| 2 | ISIS_MCF_AMTAP | NUMERIC | 8 | 2 | — |
| 3 | ISIS_MCF_AMTAPD | NUMERIC | 8 | 2 | — |
| 4 | ISIS_MCF_AMTAR | NUMERIC | 8 | 2 | — |
| 5 | ISIS_MCF_AMTBNK | NUMERIC | 8 | 2 | — |
| 6 | ISIS_MCF_AMTCS | NUMERIC | 8 | 2 | — |
| 7 | ISIS_MCF_AMTFE | NUMERIC | 8 | 2 | — |
| 8 | ISIS_MCF_AMTPOR | NUMERIC | 8 | 2 | — |
| 9 | ISIS_MCF_BASE | STRING | 1 | — | Y |
| 10 | ISIS_MCF_CODE | STRING | 3 | — | Y |
| 11 | ISIS_MCF_DEC | INTEGER | 2 | — | — |
| 12 | ISIS_MCF_DESC | STRING | 25 | — | Y |
| 13 | ISIS_MCF_GLAADX | STRING | 10 | — | — |
| 14 | ISIS_MCF_GLAAP | STRING | 10 | — | Y |
| 15 | ISIS_MCF_GLAAPD | STRING | 10 | — | — |
| 16 | ISIS_MCF_GLAAPX | STRING | 10 | — | Y |
| 17 | ISIS_MCF_GLAAR | STRING | 10 | — | Y |
| 18 | ISIS_MCF_GLAARD | STRING | 10 | — | Y |
| 19 | ISIS_MCF_GLAARX | STRING | 10 | — | Y |
| 20 | ISIS_MCF_GLABK | STRING | 10 | — | Y |
| 21 | ISIS_MCF_GLABKX | STRING | 10 | — | Y |
| 22 | ISIS_MCF_GLABS | STRING | 10 | — | Y |
| 23 | ISIS_MCF_GLACS | STRING | 10 | — | — |
| 24 | ISIS_MCF_GLACSX | STRING | 10 | — | — |
| 25 | ISIS_MCF_GLAIS | STRING | 10 | — | Y |
| 26 | ISIS_MCF_GLAPDX | STRING | 10 | — | — |
| 27 | ISIS_MCF_GLAPO | STRING | 10 | — | Y |
| 28 | ISIS_MCF_GLAPOX | STRING | 10 | — | Y |
| 29 | ISIS_MCF_GLDADX | STRING | 4 | — | — |
| 30 | ISIS_MCF_GLDAP | STRING | 4 | — | Y |
| 31 | ISIS_MCF_GLDAPD | STRING | 4 | — | — |
| 32 | ISIS_MCF_GLDAPX | STRING | 4 | — | Y |
| 33 | ISIS_MCF_GLDAR | STRING | 4 | — | Y |
| 34 | ISIS_MCF_GLDARD | STRING | 4 | — | Y |
| 35 | ISIS_MCF_GLDARX | STRING | 4 | — | Y |
| 36 | ISIS_MCF_GLDBK | STRING | 4 | — | Y |
| 37 | ISIS_MCF_GLDBKX | STRING | 4 | — | Y |
| 38 | ISIS_MCF_GLDBS | STRING | 4 | — | Y |
| 39 | ISIS_MCF_GLDCS | STRING | 4 | — | — |
| 40 | ISIS_MCF_GLDCSX | STRING | 4 | — | — |
| 41 | ISIS_MCF_GLDIS | STRING | 4 | — | Y |
| 42 | ISIS_MCF_GLDPDX | STRING | 4 | — | — |
| 43 | ISIS_MCF_GLDPO | STRING | 4 | — | Y |
| 44 | ISIS_MCF_GLDPOX | STRING | 4 | — | Y |
| 45 | ISIS_MCF_INTDAY | NUMERIC | 8 | — | — |
| 46 | ISIS_MCF_INTRES | NUMERIC | 8 | 3 | — |
| 47 | ISIS_MCF_SYMBOL | STRING | 1 | — | Y |
| 48 | ISIS_MCF_SYMDSC | STRING | 10 | — | N |
| 49 | ISIS_MCF_SYMPOS | STRING | 1 | — | Y |

## ISMCR
**MULTI-CURRENCY EXCHANGE RATE**

Fields: 22

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISIS_MCR_BASE | STRING | 3 | — | — |
| 2 | ISIS_MCR_DATE | DATE | 4 | — | — |
| 3 | ISIS_MCR_RATE_1 | NUMERIC | 8 | 6 | — |
| 4 | ISIS_MCR_RATE_10 | NUMERIC | 8 | 6 | — |
| 5 | ISIS_MCR_RATE_2 | NUMERIC | 8 | 6 | — |
| 6 | ISIS_MCR_RATE_3 | NUMERIC | 8 | 6 | — |
| 7 | ISIS_MCR_RATE_4 | NUMERIC | 8 | 6 | — |
| 8 | ISIS_MCR_RATE_5 | NUMERIC | 8 | 6 | — |
| 9 | ISIS_MCR_RATE_6 | NUMERIC | 8 | 6 | — |
| 10 | ISIS_MCR_RATE_7 | NUMERIC | 8 | 6 | — |
| 11 | ISIS_MCR_RATE_8 | NUMERIC | 8 | 6 | — |
| 12 | ISIS_MCR_RATE_9 | NUMERIC | 8 | 6 | — |
| 13 | ISIS_MCR_SOURCE_1 | STRING | 3 | — | — |
| 14 | ISIS_MCR_SOURCE_10 | STRING | 3 | — | — |
| 15 | ISIS_MCR_SOURCE_2 | STRING | 3 | — | — |
| 16 | ISIS_MCR_SOURCE_3 | STRING | 3 | — | — |
| 17 | ISIS_MCR_SOURCE_4 | STRING | 3 | — | — |
| 18 | ISIS_MCR_SOURCE_5 | STRING | 3 | — | — |
| 19 | ISIS_MCR_SOURCE_6 | STRING | 3 | — | — |
| 20 | ISIS_MCR_SOURCE_7 | STRING | 3 | — | — |
| 21 | ISIS_MCR_SOURCE_8 | STRING | 3 | — | — |
| 22 | ISIS_MCR_SOURCE_9 | STRING | 3 | — | — |
