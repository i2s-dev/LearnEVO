# RM — Routing/Manufacturing: Field Reference

Status: verified-schema

Source: `Evo-DBA_File_Fields 052421.xlsx`, sheet "Fields".
Field descriptions where provided by source; otherwise name-inferred.

---

## ISARMCHG
**CHANGES TO RMA**

Fields: 26

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISAR_CHG_AASD | DATE | 4 | — | — |
| 2 | ISAR_CHG_ACOMPR_1 | NUMERIC | 8 | 4 | — |
| 3 | ISAR_CHG_ACOMPR_2 | NUMERIC | 8 | 4 | — |
| 4 | ISAR_CHG_ADISC | NUMERIC | 8 | 2 | — |
| 5 | ISAR_CHG_AESD | DATE | 4 | — | — |
| 6 | ISAR_CHG_AEXTRA | STRING | 150 | — | — |
| 7 | ISAR_CHG_ALOC | STRING | 10 | — | — |
| 8 | ISAR_CHG_AOOQTY | NUMERIC | 8 | 2 | — |
| 9 | ISAR_CHG_APRICE | NUMERIC | 8 | 4 | — |
| 10 | ISAR_CHG_BASD | DATE | 4 | — | — |
| 11 | ISAR_CHG_BCOMPR_1 | NUMERIC | 8 | 4 | — |
| 12 | ISAR_CHG_BCOMPR_2 | NUMERIC | 8 | 4 | — |
| 13 | ISAR_CHG_BDISC | NUMERIC | 8 | 2 | — |
| 14 | ISAR_CHG_BESD | DATE | 4 | — | — |
| 15 | ISAR_CHG_BEXTRA | STRING | 150 | — | — |
| 16 | ISAR_CHG_BLOC | STRING | 10 | — | — |
| 17 | ISAR_CHG_BOOQTY | NUMERIC | 8 | 2 | — |
| 18 | ISAR_CHG_BPRICE | NUMERIC | 8 | 4 | — |
| 19 | ISAR_CHG_CDATE | DATE | 4 | — | — |
| 20 | ISAR_CHG_INVNUM | NUMERIC | 8 | — | — |
| 21 | ISAR_CHG_LINEID | NUMERIC | 8 | — | — |
| 22 | ISAR_CHG_PCODE | STRING | 15 | — | — |
| 23 | ISAR_CHG_REVLVL | STRING | 10 | — | — |
| 24 | ISAR_CHG_SONUM | NUMERIC | 8 | — | — |
| 25 | ISAR_CHG_UNUM | INTEGER | 4 | — | — |
| 26 | ISAR_CHG_USER | STRING | 15 | — | — |

## ISRMAAI
**ARCHIVE RMA INFO**

Fields: 27

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_RMA_CLOSDATE | DATE | 4 | — | — |
| 2 | IS_RMA_CMDATE | DATE | 4 | — | — |
| 3 | IS_RMA_CMNUM | NUMERIC | 8 | — | — |
| 4 | IS_RMA_DATE | DATE | 4 | — | — |
| 5 | IS_RMA_DISP | STRING | 40 | — | — |
| 6 | IS_RMA_DISPDATE | DATE | 4 | — | — |
| 7 | IS_RMA_DISPSEL | INTEGER | 2 | — | — |
| 8 | IS_RMA_IEXTRA | STRING | 150 | — | — |
| 9 | IS_RMA_INVCD | STRING | 1 | — | — |
| 10 | IS_RMA_INVDATE | DATE | 4 | — | — |
| 11 | IS_RMA_INVNUM | NUMERIC | 8 | — | — |
| 12 | IS_RMA_LINEID | NUMERIC | 8 | — | — |
| 13 | IS_RMA_NUM | NUMERIC | 8 | — | — |
| 14 | IS_RMA_OINVNUM | NUMERIC | 8 | — | — |
| 15 | IS_RMA_OLDRMANO | NUMERIC | 8 | — | — |
| 16 | IS_RMA_OSONUM | NUMERIC | 8 | — | — |
| 17 | IS_RMA_PART | STRING | 15 | — | — |
| 18 | IS_RMA_RCPTDATE | DATE | 4 | — | — |
| 19 | IS_RMA_REASON | STRING | 30 | — | — |
| 20 | IS_RMA_REORDER | STRING | 1 | — | — |
| 21 | IS_RMA_SODATE | DATE | 4 | — | — |
| 22 | IS_RMA_SONUM | NUMERIC | 8 | — | — |
| 23 | IS_RMA_SRNUM | NUMERIC | 8 | — | — |
| 24 | IS_RMA_STATUS | STRING | 30 | — | — |
| 25 | IS_RMA_WARRANTY | STRING | 1 | — | — |
| 26 | IS_RMA_WOPRE | NUMERIC | 8 | — | — |
| 27 | IS_RMA_WOSUF | INTEGER | 2 | — | — |

## ISRMAC
**REASONS FOR RETURN**

Fields: 3

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_RMA_CODE | STRING | 30 | — | — |
| 2 | IS_RMA_DESC | STRING | 60 | — | — |
| 3 | IS_RMA_EXTRA | STRING | 100 | — | — |

## ISRMAI
**RMA INFO**

Fields: 27

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_RMA_CLOSDATE | DATE | 4 | — | — |
| 2 | IS_RMA_CMDATE | DATE | 4 | — | — |
| 3 | IS_RMA_CMNUM | NUMERIC | 8 | — | — |
| 4 | IS_RMA_DATE | DATE | 4 | — | — |
| 5 | IS_RMA_DISP | STRING | 40 | — | — |
| 6 | IS_RMA_DISPDATE | DATE | 4 | — | — |
| 7 | IS_RMA_DISPSEL | INTEGER | 2 | — | — |
| 8 | IS_RMA_IEXTRA | STRING | 150 | — | — |
| 9 | IS_RMA_INVCD | STRING | 1 | — | — |
| 10 | IS_RMA_INVDATE | DATE | 4 | — | — |
| 11 | IS_RMA_INVNUM | NUMERIC | 8 | — | — |
| 12 | IS_RMA_LINEID | NUMERIC | 8 | — | — |
| 13 | IS_RMA_NUM | NUMERIC | 8 | — | — |
| 14 | IS_RMA_OINVNUM | NUMERIC | 8 | — | — |
| 15 | IS_RMA_OLDRMANO | NUMERIC | 8 | — | — |
| 16 | IS_RMA_OSONUM | NUMERIC | 8 | — | — |
| 17 | IS_RMA_PART | STRING | 15 | — | — |
| 18 | IS_RMA_RCPTDATE | DATE | 4 | — | — |
| 19 | IS_RMA_REASON | STRING | 30 | — | — |
| 20 | IS_RMA_REORDER | STRING | 1 | — | — |
| 21 | IS_RMA_SODATE | DATE | 4 | — | — |
| 22 | IS_RMA_SONUM | NUMERIC | 8 | — | — |
| 23 | IS_RMA_SRNUM | NUMERIC | 8 | — | — |
| 24 | IS_RMA_STATUS | STRING | 30 | — | — |
| 25 | IS_RMA_WARRANTY | STRING | 1 | — | — |
| 26 | IS_RMA_WOPRE | NUMERIC | 8 | — | — |
| 27 | IS_RMA_WOSUF | INTEGER | 2 | — | — |

## ISSRADSC
**ARCHIVED DBA SERVICE/REPAIR NOTES**

Fields: 5

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BK_DESC_CODE | STRING | 15 | — | not used |
| 2 | BK_DESC_DESC | STRING | 25 | — | not used |
| 3 | BK_DESC_LINE | INTEGER | 2 | — | Notes line number |
| 4 | BK_DESC_NOTES | STRING | 70 | — | Notes - text |
| 5 | BK_DESC_NUM | NUMERIC | 8 | — | PO Number |

## ISSRAINF
**ARCHIVED SERVICE/REPAIR SUPPL INFO**

Fields: 54

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISSR_INFO_AL1 | STRING | 25 | — | — |
| 2 | ISSR_INFO_AL10 | STRING | 25 | — | — |
| 3 | ISSR_INFO_AL11 | STRING | 25 | — | — |
| 4 | ISSR_INFO_AL12 | STRING | 25 | — | — |
| 5 | ISSR_INFO_AL13 | STRING | 25 | — | — |
| 6 | ISSR_INFO_AL14 | STRING | 25 | — | — |
| 7 | ISSR_INFO_AL15 | STRING | 25 | — | — |
| 8 | ISSR_INFO_AL16 | STRING | 25 | — | — |
| 9 | ISSR_INFO_AL17 | STRING | 25 | — | — |
| 10 | ISSR_INFO_AL18 | STRING | 25 | — | — |
| 11 | ISSR_INFO_AL19 | STRING | 25 | — | — |
| 12 | ISSR_INFO_AL2 | STRING | 25 | — | — |
| 13 | ISSR_INFO_AL20 | STRING | 25 | — | — |
| 14 | ISSR_INFO_AL3 | STRING | 25 | — | — |
| 15 | ISSR_INFO_AL4 | STRING | 25 | — | — |
| 16 | ISSR_INFO_AL5 | STRING | 25 | — | — |
| 17 | ISSR_INFO_AL6 | STRING | 25 | — | — |
| 18 | ISSR_INFO_AL7 | STRING | 25 | — | — |
| 19 | ISSR_INFO_AL8 | STRING | 25 | — | — |
| 20 | ISSR_INFO_AL9 | STRING | 25 | — | — |
| 21 | ISSR_INFO_ALPHA_1 | STRING | 25 | — | — |
| 22 | ISSR_INFO_ALPHA_10 | STRING | 25 | — | — |
| 23 | ISSR_INFO_ALPHA_11 | STRING | 25 | — | — |
| 24 | ISSR_INFO_ALPHA_12 | STRING | 25 | — | — |
| 25 | ISSR_INFO_ALPHA_13 | STRING | 25 | — | — |
| 26 | ISSR_INFO_ALPHA_14 | STRING | 25 | — | — |
| 27 | ISSR_INFO_ALPHA_15 | STRING | 25 | — | — |
| 28 | ISSR_INFO_ALPHA_16 | STRING | 25 | — | — |
| 29 | ISSR_INFO_ALPHA_17 | STRING | 25 | — | — |
| 30 | ISSR_INFO_ALPHA_18 | STRING | 25 | — | — |
| 31 | ISSR_INFO_ALPHA_19 | STRING | 25 | — | — |
| 32 | ISSR_INFO_ALPHA_2 | STRING | 25 | — | — |
| 33 | ISSR_INFO_ALPHA_20 | STRING | 25 | — | — |
| 34 | ISSR_INFO_ALPHA_3 | STRING | 25 | — | — |
| 35 | ISSR_INFO_ALPHA_4 | STRING | 25 | — | — |
| 36 | ISSR_INFO_ALPHA_5 | STRING | 25 | — | — |
| 37 | ISSR_INFO_ALPHA_6 | STRING | 25 | — | — |
| 38 | ISSR_INFO_ALPHA_7 | STRING | 25 | — | — |
| 39 | ISSR_INFO_ALPHA_8 | STRING | 25 | — | — |
| 40 | ISSR_INFO_ALPHA_9 | STRING | 25 | — | — |
| 41 | ISSR_INFO_CODE | STRING | 15 | — | — |
| 42 | ISSR_INFO_DATE1 | DATE | 4 | — | — |
| 43 | ISSR_INFO_DATE2 | DATE | 4 | — | — |
| 44 | ISSR_INFO_DATE3 | DATE | 4 | — | — |
| 45 | ISSR_INFO_DATE4 | DATE | 4 | — | — |
| 46 | ISSR_INFO_DATE5 | DATE | 4 | — | — |
| 47 | ISSR_INFO_DATE_1 | DATE | 4 | — | — |
| 48 | ISSR_INFO_DATE_2 | DATE | 4 | — | — |
| 49 | ISSR_INFO_DATE_3 | DATE | 4 | — | — |
| 50 | ISSR_INFO_DATE_4 | DATE | 4 | — | — |
| 51 | ISSR_INFO_DATE_5 | DATE | 4 | — | — |
| 52 | ISSR_INFO_EXTRA | STRING | 100 | — | — |
| 53 | ISSR_INFO_SRNUM | NUMERIC | 8 | — | — |
| 54 | ISSR_INFO_UID | NUMERIC | 8 | — | — |

## ISSRAMMS
**ARCHIVED S/R MAKE MODEL SERIAL**

Fields: 12

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISSR_MMS_EXTRA | STRING | 150 | — | — |
| 2 | ISSR_MMS_INDATE | DATE | 4 | — | — |
| 3 | ISSR_MMS_INVNUM | NUMERIC | 8 | — | — |
| 4 | ISSR_MMS_LINEID | INTEGER | 2 | — | — |
| 5 | ISSR_MMS_MAKE | STRING | 50 | — | — |
| 6 | ISSR_MMS_MODLE | STRING | 50 | — | — |
| 7 | ISSR_MMS_OUTDTE | DATE | 4 | — | — |
| 8 | ISSR_MMS_PART | STRING | 15 | — | — |
| 9 | ISSR_MMS_SERIAL | STRING | 50 | — | — |
| 10 | ISSR_MMS_SRVNUM | NUMERIC | 8 | — | — |
| 11 | ISSR_MMS_WOPRE | NUMERIC | 8 | — | — |
| 12 | ISSR_MMS_WOSUF | INTEGER | 2 | — | — |

## ISSRDESC
**SERVICE/REPAIR DBA NOTES**

Fields: 5

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BK_DESC_CODE | STRING | 15 | — | not used |
| 2 | BK_DESC_DESC | STRING | 25 | — | not used |
| 3 | BK_DESC_LINE | INTEGER | 2 | — | Notes line number |
| 4 | BK_DESC_NOTES | STRING | 70 | — | Notes - text |
| 5 | BK_DESC_NUM | NUMERIC | 8 | — | PO Number |

## ISSRINFO
**SERVICE/REPAIR SUPPL INFO**

Fields: 54

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISSR_INFO_AL1 | STRING | 25 | — | — |
| 2 | ISSR_INFO_AL10 | STRING | 25 | — | — |
| 3 | ISSR_INFO_AL11 | STRING | 25 | — | — |
| 4 | ISSR_INFO_AL12 | STRING | 25 | — | — |
| 5 | ISSR_INFO_AL13 | STRING | 25 | — | — |
| 6 | ISSR_INFO_AL14 | STRING | 25 | — | — |
| 7 | ISSR_INFO_AL15 | STRING | 25 | — | — |
| 8 | ISSR_INFO_AL16 | STRING | 25 | — | — |
| 9 | ISSR_INFO_AL17 | STRING | 25 | — | — |
| 10 | ISSR_INFO_AL18 | STRING | 25 | — | — |
| 11 | ISSR_INFO_AL19 | STRING | 25 | — | — |
| 12 | ISSR_INFO_AL2 | STRING | 25 | — | — |
| 13 | ISSR_INFO_AL20 | STRING | 25 | — | — |
| 14 | ISSR_INFO_AL3 | STRING | 25 | — | — |
| 15 | ISSR_INFO_AL4 | STRING | 25 | — | — |
| 16 | ISSR_INFO_AL5 | STRING | 25 | — | — |
| 17 | ISSR_INFO_AL6 | STRING | 25 | — | — |
| 18 | ISSR_INFO_AL7 | STRING | 25 | — | — |
| 19 | ISSR_INFO_AL8 | STRING | 25 | — | — |
| 20 | ISSR_INFO_AL9 | STRING | 25 | — | — |
| 21 | ISSR_INFO_ALPHA_1 | STRING | 25 | — | — |
| 22 | ISSR_INFO_ALPHA_10 | STRING | 25 | — | — |
| 23 | ISSR_INFO_ALPHA_11 | STRING | 25 | — | — |
| 24 | ISSR_INFO_ALPHA_12 | STRING | 25 | — | — |
| 25 | ISSR_INFO_ALPHA_13 | STRING | 25 | — | — |
| 26 | ISSR_INFO_ALPHA_14 | STRING | 25 | — | — |
| 27 | ISSR_INFO_ALPHA_15 | STRING | 25 | — | — |
| 28 | ISSR_INFO_ALPHA_16 | STRING | 25 | — | — |
| 29 | ISSR_INFO_ALPHA_17 | STRING | 25 | — | — |
| 30 | ISSR_INFO_ALPHA_18 | STRING | 25 | — | — |
| 31 | ISSR_INFO_ALPHA_19 | STRING | 25 | — | — |
| 32 | ISSR_INFO_ALPHA_2 | STRING | 25 | — | — |
| 33 | ISSR_INFO_ALPHA_20 | STRING | 25 | — | — |
| 34 | ISSR_INFO_ALPHA_3 | STRING | 25 | — | — |
| 35 | ISSR_INFO_ALPHA_4 | STRING | 25 | — | — |
| 36 | ISSR_INFO_ALPHA_5 | STRING | 25 | — | — |
| 37 | ISSR_INFO_ALPHA_6 | STRING | 25 | — | — |
| 38 | ISSR_INFO_ALPHA_7 | STRING | 25 | — | — |
| 39 | ISSR_INFO_ALPHA_8 | STRING | 25 | — | — |
| 40 | ISSR_INFO_ALPHA_9 | STRING | 25 | — | — |
| 41 | ISSR_INFO_CODE | STRING | 15 | — | — |
| 42 | ISSR_INFO_DATE1 | DATE | 4 | — | — |
| 43 | ISSR_INFO_DATE2 | DATE | 4 | — | — |
| 44 | ISSR_INFO_DATE3 | DATE | 4 | — | — |
| 45 | ISSR_INFO_DATE4 | DATE | 4 | — | — |
| 46 | ISSR_INFO_DATE5 | DATE | 4 | — | — |
| 47 | ISSR_INFO_DATE_1 | DATE | 4 | — | — |
| 48 | ISSR_INFO_DATE_2 | DATE | 4 | — | — |
| 49 | ISSR_INFO_DATE_3 | DATE | 4 | — | — |
| 50 | ISSR_INFO_DATE_4 | DATE | 4 | — | — |
| 51 | ISSR_INFO_DATE_5 | DATE | 4 | — | — |
| 52 | ISSR_INFO_EXTRA | STRING | 100 | — | — |
| 53 | ISSR_INFO_SRNUM | NUMERIC | 8 | — | — |
| 54 | ISSR_INFO_UID | NUMERIC | 8 | — | — |

## ISSRINV
**SERVICE/REPAIR & RMA HEADER**

Fields: 82

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKAR_INV_BILA1 | STRING | 30 | — | Billing Address 1 |
| 2 | BKAR_INV_BILA2 | STRING | 30 | — | Billing Address 2 |
| 3 | BKAR_INV_BILA3 | STRING | 30 | — | Billing Address 3 |
| 4 | BKAR_INV_BILATN | STRING | 30 | — | Billing Attention |
| 5 | BKAR_INV_BILCNT | STRING | 30 | — | Billing Country |
| 6 | BKAR_INV_BILCOD | STRING | 10 | — | Bill To Code |
| 7 | BKAR_INV_BILCTY | STRING | 30 | — | Billing City |
| 8 | BKAR_INV_BILNME | STRING | 30 | — | Bill To Name |
| 9 | BKAR_INV_BILST | STRING | 2 | — | Billing State |
| 10 | BKAR_INV_BILZIP | STRING | 10 | — | Billing ZIP |
| 11 | BKAR_INV_CCOAMT | NUMERIC | 8 | 2 | — |
| 12 | BKAR_INV_CHKNUM | NUMERIC | 8 | — | Check Number |
| 13 | BKAR_INV_COGS | NUMERIC | 8 | 2 | COGS |
| 14 | BKAR_INV_COMAMT | NUMERIC | 8 | 2 | — |
| 15 | BKAR_INV_COMMPR_1 | NUMERIC | 8 | 4 | — |
| 16 | BKAR_INV_COMMPR_2 | NUMERIC | 8 | 4 | — |
| 17 | BKAR_INV_CUSA1 | STRING | 30 | — | Customer Address 1 |
| 18 | BKAR_INV_CUSA2_1 | STRING | 30 | — | — |
| 19 | BKAR_INV_CUSA2_2 | STRING | 30 | — | — |
| 20 | BKAR_INV_CUSATT | STRING | 30 | — | Attention: |
| 21 | BKAR_INV_CUSCNT | STRING | 30 | — | Country |
| 22 | BKAR_INV_CUSCOD | STRING | 10 | — | Customer Code |
| 23 | BKAR_INV_CUSCTY | STRING | 26 | — | City |
| 24 | BKAR_INV_CUSNME | STRING | 30 | — | Customer Name |
| 25 | BKAR_INV_CUSORD | STRING | 25 | — | Customer Order |
| 26 | BKAR_INV_CUSST | STRING | 2 | — | State |
| 27 | BKAR_INV_CUSZIP | STRING | 10 | — | ZIP Code |
| 28 | BKAR_INV_DCODE | STRING | 10 | — | Discount Code |
| 29 | BKAR_INV_DEPAMT | NUMERIC | 8 | 2 | — |
| 30 | BKAR_INV_DESC | STRING | 30 | — | Orser Description |
| 31 | BKAR_INV_ENDLNE | STRING | 1 | — | Ending lines Y/N |
| 32 | BKAR_INV_ENTBY | STRING | 5 | — | Entered By |
| 33 | BKAR_INV_EXTRA | STRING | 150 | — | Extra |
| 34 | BKAR_INV_FOB | STRING | 15 | — | FOB |
| 35 | BKAR_INV_FRGHT | NUMERIC | 8 | 2 | Freight Amount |
| 36 | BKAR_INV_GLDPT | STRING | 4 | — | GL Department |
| 37 | BKAR_INV_INDATE | DATE | 4 | — | — |
| 38 | BKAR_INV_INVCD | STRING | 1 | — | INVCD X/P/Y |
| 39 | BKAR_INV_INVDTE | DATE | 4 | — | Invoice Date |
| 40 | BKAR_INV_ISCUR | STRING | 3 | — | — |
| 41 | BKAR_INV_ISMCDT | DATE | 4 | — | — |
| 42 | BKAR_INV_ISREV | STRING | 1 | — | — |
| 43 | BKAR_INV_ISRVDT | DATE | 4 | — | — |
| 44 | BKAR_INV_ISTXKY | STRING | 10 | — | — |
| 45 | BKAR_INV_ITMZTX_1 | STRING | 1 | — | — |
| 46 | BKAR_INV_ITMZTX_2 | STRING | 1 | — | — |
| 47 | BKAR_INV_JOBNUM | STRING | 15 | — | Job Number 1 |
| 48 | BKAR_INV_LINV^P | NUMERIC | 8 | — | — |
| 49 | BKAR_INV_LOC | STRING | 10 | — | Location |
| 50 | BKAR_INV_NL | INTEGER | 2 | — | Number Lines |
| 51 | BKAR_INV_NUM | NUMERIC | 8 | — | Invoice Number |
| 52 | BKAR_INV_ORDDTE | DATE | 4 | — | Order Date |
| 53 | BKAR_INV_PCODE | INTEGER | 2 | — | Price Code |
| 54 | BKAR_INV_RELNUM | NUMERIC | 8 | — | — |
| 55 | BKAR_INV_RETEN | NUMERIC | 8 | 2 | — |
| 56 | BKAR_INV_RTS | STRING | 1 | — | Ready To Ship Y/N |
| 57 | BKAR_INV_SCCOGS | NUMERIC | 8 | 2 | — |
| 58 | BKAR_INV_SHIPDT | DATE | 4 | — | Ship Date |
| 59 | BKAR_INV_SHIPPR | NUMERIC | 8 | — | Shipper Number |
| 60 | BKAR_INV_SHPA1 | STRING | 30 | — | Shi[ Address 1 |
| 61 | BKAR_INV_SHPA2_1 | STRING | 30 | — | — |
| 62 | BKAR_INV_SHPA2_2 | STRING | 30 | — | — |
| 63 | BKAR_INV_SHPATN | STRING | 30 | — | Ship Attention |
| 64 | BKAR_INV_SHPCNT | STRING | 30 | — | Ship Country |
| 65 | BKAR_INV_SHPCOD | STRING | 10 | — | Ship To Code |
| 66 | BKAR_INV_SHPCTY | STRING | 26 | — | Ship City |
| 67 | BKAR_INV_SHPNME | STRING | 30 | — | Ship Name |
| 68 | BKAR_INV_SHPST | STRING | 2 | — | Shop State |
| 69 | BKAR_INV_SHPVIA | STRING | 15 | — | Ship Via |
| 70 | BKAR_INV_SHPZIP | STRING | 10 | — | Ship ZIP Code |
| 71 | BKAR_INV_SLSP | INTEGER | 2 | — | Salesperson 1 |
| 72 | BKAR_INV_SLSP2 | INTEGER | 2 | — | Sales Person 2 |
| 73 | BKAR_INV_SONUM | NUMERIC | 8 | — | Sales Order   Number |
| 74 | BKAR_INV_SUBTOT | NUMERIC | 8 | 2 | Sub Total |
| 75 | BKAR_INV_TAXABL | STRING | 1 | — | Taxable Y/N |
| 76 | BKAR_INV_TAXAMT | NUMERIC | 8 | 2 | Tax Amount |
| 77 | BKAR_INV_TAXKEY | STRING | 4 | — | — |
| 78 | BKAR_INV_TAXRTE | NUMERIC | 8 | 4 | Tax Rate |
| 79 | BKAR_INV_TERMD | STRING | 10 | — | Terms Description |
| 80 | BKAR_INV_TERMNM | INTEGER | 2 | — | Terms Number |
| 81 | BKAR_INV_TOTAL | NUMERIC | 8 | 2 | Total |
| 82 | BKAR_INV_TRACK | STRING | 40 | — | — |

## ISSRINVL
**SERVICE/REPAIR & RMA LINE**

Fields: 29

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKAR_INVL_ABQTY | NUMERIC | 8 | 2 | options Quantity |
| 2 | BKAR_INVL_ASD | DATE | 4 | — | Actual Ship Date |
| 3 | BKAR_INVL_CNTR | INTEGER | 2 | — | Line Counter |
| 4 | BKAR_INVL_COMPR_1 | NUMERIC | 8 | 4 | — |
| 5 | BKAR_INVL_COMPR_2 | NUMERIC | 8 | 4 | — |
| 6 | BKAR_INVL_COOP | NUMERIC | 8 | 2 | — |
| 7 | BKAR_INVL_ESD | DATE | 4 | — | Estimated Ship Date |
| 8 | BKAR_INVL_EXTRA | STRING | 100 | — | Extra |
| 9 | BKAR_INVL_FRGHT | NUMERIC | 8 | 2 | Freight |
| 10 | BKAR_INVL_INVNM | NUMERIC | 8 | — | Sales Order Number |
| 11 | BKAR_INVL_ITYPE | STRING | 1 | — | Part Type |
| 12 | BKAR_INVL_JOB^ | STRING | 10 | — | — |
| 13 | BKAR_INVL_LOC | STRING | 10 | — | Location |
| 14 | BKAR_INVL_OOQTY | NUMERIC | 8 | 2 | Original Order Quantity |
| 15 | BKAR_INVL_PCODE | STRING | 15 | — | Part Code |
| 16 | BKAR_INVL_PCOGS | NUMERIC | 8 | 4 | COGS |
| 17 | BKAR_INVL_PDESC | STRING | 30 | — | Part Description |
| 18 | BKAR_INVL_PDISC | NUMERIC | 8 | 2 | Discount |
| 19 | BKAR_INVL_PEXT | NUMERIC | 8 | 2 | Extended Price |
| 20 | BKAR_INVL_PPRCE | NUMERIC | 8 | 4 | Price |
| 21 | BKAR_INVL_PQTY | NUMERIC | 8 | 2 | Quantity |
| 22 | BKAR_INVL_RTS | STRING | 1 | — | Ready to Ship |
| 23 | BKAR_INVL_SCCOG | NUMERIC | 8 | 4 | — |
| 24 | BKAR_INVL_TXAMT | NUMERIC | 8 | 2 | Tax Amount |
| 25 | BKAR_INVL_TXBLE | STRING | 1 | — | Taxable Y/N |
| 26 | BKAR_INVL_UBO | NUMERIC | 8 | 2 | Units on Back Order |
| 27 | BKAR_INVL_UM_LN_1 | STRING | 3 | — | — |
| 28 | BKAR_INVL_UM_LN_2 | STRING | 3 | — | — |
| 29 | BKAR_INVL_USTD | NUMERIC | 8 | 2 | Units Shipped To Date |

## ISSRMMS
**S/R MAKE MODEL SERIAL**

Fields: 12

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISSR_MMS_EXTRA | STRING | 150 | — | — |
| 2 | ISSR_MMS_INDATE | DATE | 4 | — | — |
| 3 | ISSR_MMS_INVNUM | NUMERIC | 8 | — | — |
| 4 | ISSR_MMS_LINEID | INTEGER | 2 | — | — |
| 5 | ISSR_MMS_MAKE | STRING | 50 | — | — |
| 6 | ISSR_MMS_MODLE | STRING | 50 | — | — |
| 7 | ISSR_MMS_OUTDTE | DATE | 4 | — | — |
| 8 | ISSR_MMS_PART | STRING | 15 | — | — |
| 9 | ISSR_MMS_SERIAL | STRING | 50 | — | — |
| 10 | ISSR_MMS_SRVNUM | NUMERIC | 8 | — | — |
| 11 | ISSR_MMS_WOPRE | NUMERIC | 8 | — | — |
| 12 | ISSR_MMS_WOSUF | INTEGER | 2 | — | — |
