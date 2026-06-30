# WO — Work Orders: Field Reference

Status: verified-schema

Source: `Evo-DBA_File_Fields 052421.xlsx`, sheet "Fields".
Field descriptions where provided by source; otherwise name-inferred.

---

## BKSHORT
**TEMP FILE FOR SHORTAGE REPROT**

Fields: 9

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BK_SHORT_DATE | DATE | 4 | — | — |
| 2 | BK_SHORT_DESC | STRING | 25 | — | — |
| 3 | BK_SHORT_PCODE | STRING | 15 | — | — |
| 4 | BK_SHORT_PPCODE | STRING | 15 | — | — |
| 5 | BK_SHORT_PPDESC | STRING | 25 | — | — |
| 6 | BK_SHORT_QTYREQ | NUMERIC | 8 | 2 | — |
| 7 | BK_SHORT_SHORT | NUMERIC | 8 | 2 | — |
| 8 | BK_SHORT_WO_SUF | INTEGER | 2 | — | — |
| 9 | BK_SHORT_WONUM | NUMERIC | 8 | — | — |

## ISLSMAP
**PAPERLESS SHOP FLOOR BATCH TRACKER**

Fields: 31

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_MAP_ALPHA_1 | STRING | 25 | — | — |
| 2 | IS_MAP_ALPHA_2 | STRING | 25 | — | — |
| 3 | IS_MAP_ALPHA_3 | STRING | 25 | — | — |
| 4 | IS_MAP_ALPHA_4 | STRING | 25 | — | — |
| 5 | IS_MAP_ALPHA_5 | STRING | 25 | — | — |
| 6 | IS_MAP_BATCH | STRING | 25 | — | — |
| 7 | IS_MAP_CCODE | STRING | 15 | — | — |
| 8 | IS_MAP_CLOT | NUMERIC | 8 | — | — |
| 9 | IS_MAP_CQTY | NUMERIC | 8 | 2 | — |
| 10 | IS_MAP_CQTYPER | NUMERIC | 8 | 8 | — |
| 11 | IS_MAP_CSERIAL | STRING | 25 | — | — |
| 12 | IS_MAP_DATE_1 | DATE | 4 | — | — |
| 13 | IS_MAP_DATE_2 | DATE | 4 | — | — |
| 14 | IS_MAP_DATE_3 | DATE | 4 | — | — |
| 15 | IS_MAP_DATE_4 | DATE | 4 | — | — |
| 16 | IS_MAP_DATE_5 | DATE | 4 | — | — |
| 17 | IS_MAP_EXTRA | STRING | 100 | — | — |
| 18 | IS_MAP_FLAG_1 | STRING | 1 | — | — |
| 19 | IS_MAP_FLAG_2 | STRING | 1 | — | — |
| 20 | IS_MAP_FLAG_3 | STRING | 1 | — | — |
| 21 | IS_MAP_FLAG_4 | STRING | 1 | — | — |
| 22 | IS_MAP_FLAG_5 | STRING | 1 | — | — |
| 23 | IS_MAP_OPER | INTEGER | 2 | — | — |
| 24 | IS_MAP_PCODE | STRING | 15 | — | — |
| 25 | IS_MAP_PLOT | STRING | 15 | — | — |
| 26 | IS_MAP_POSITION | STRING | 10 | — | — |
| 27 | IS_MAP_PQTY | NUMERIC | 8 | 2 | — |
| 28 | IS_MAP_PSERIAL | STRING | 25 | — | — |
| 29 | IS_MAP_TRAYNUM | STRING | 25 | — | — |
| 30 | IS_MAP_WOPRE | NUMERIC | 8 | — | — |
| 31 | IS_MAP_WOSUF | INTEGER | 2 | — | — |

## ISMACS
**MACHINE SCHEDULE**

Fields: 11

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_MACS_EXTRA | STRING | 100 | — | — |
| 2 | IS_MACS_FDATE | DATE | 4 | — | — |
| 3 | IS_MACS_FTIME | TIME | 4 | — | — |
| 4 | IS_MACS_MACNUM | STRING | 4 | — | — |
| 5 | IS_MACS_OPER | INTEGER | 2 | — | — |
| 6 | IS_MACS_SDATE | DATE | 4 | — | — |
| 7 | IS_MACS_STIME | TIME | 4 | — | — |
| 8 | IS_MACS_TREM | NUMERIC | 8 | 2 | — |
| 9 | IS_MACS_WC | STRING | 12 | — | — |
| 10 | IS_MACS_WOPRE | NUMERIC | 8 | — | — |
| 11 | IS_MACS_WOSUF | INTEGER | 2 | — | — |

## ISPREQ
**PARTS REQUEST**

Fields: 23

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_PREQ_CDATE | DATE | 4 | — | — |
| 2 | IS_PREQ_CLOSED | STRING | 1 | — | — |
| 3 | IS_PREQ_EMP | INTEGER | 2 | — | — |
| 4 | IS_PREQ_EXTRA | STRING | 100 | — | — |
| 5 | IS_PREQ_INOTE | STRING | 200 | — | — |
| 6 | IS_PREQ_IQTY | NUMERIC | 8 | 4 | — |
| 7 | IS_PREQ_LCOST | NUMERIC | 8 | 2 | — |
| 8 | IS_PREQ_LOC | STRING | 15 | — | — |
| 9 | IS_PREQ_LOT | STRING | 15 | — | — |
| 10 | IS_PREQ_NOB | STRING | 1 | — | — |
| 11 | IS_PREQ_NOTE | STRING | 200 | — | — |
| 12 | IS_PREQ_NOTE2 | STRING | 200 | — | — |
| 13 | IS_PREQ_OPER | INTEGER | 2 | — | — |
| 14 | IS_PREQ_PART | STRING | 15 | — | — |
| 15 | IS_PREQ_PRINTED | STRING | 1 | — | — |
| 16 | IS_PREQ_QTY | NUMERIC | 8 | 4 | — |
| 17 | IS_PREQ_RDATE | DATE | 4 | — | — |
| 18 | IS_PREQ_REASON | STRING | 30 | — | — |
| 19 | IS_PREQ_SCRAP | STRING | 2 | — | — |
| 20 | IS_PREQ_SERIAL | STRING | 25 | — | — |
| 21 | IS_PREQ_WC | STRING | 12 | — | — |
| 22 | IS_PREQ_WOPRE | NUMERIC | 8 | — | — |
| 23 | IS_PREQ_WOSUF | INTEGER | 2 | — | — |

## ISQCMTHD
**PAPERLESS SHOP FLOOR TEST METHODS**

Fields: 44

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISQC_MTD_DESC | STRING | 60 | — | — |
| 2 | ISQC_MTD_DESC2 | STRING | 60 | — | — |
| 3 | ISQC_MTD_ENTBY | INTEGER | 2 | — | — |
| 4 | ISQC_MTD_ENTDT | DATE | 4 | — | — |
| 5 | ISQC_MTD_EXTRA | STRING | 100 | — | — |
| 6 | ISQC_MTD_METHOD_1 | STRING | 100 | — | — |
| 7 | ISQC_MTD_METHOD_10 | STRING | 100 | — | — |
| 8 | ISQC_MTD_METHOD_11 | STRING | 100 | — | — |
| 9 | ISQC_MTD_METHOD_12 | STRING | 100 | — | — |
| 10 | ISQC_MTD_METHOD_13 | STRING | 100 | — | — |
| 11 | ISQC_MTD_METHOD_14 | STRING | 100 | — | — |
| 12 | ISQC_MTD_METHOD_15 | STRING | 100 | — | — |
| 13 | ISQC_MTD_METHOD_16 | STRING | 100 | — | — |
| 14 | ISQC_MTD_METHOD_17 | STRING | 100 | — | — |
| 15 | ISQC_MTD_METHOD_18 | STRING | 100 | — | — |
| 16 | ISQC_MTD_METHOD_19 | STRING | 100 | — | — |
| 17 | ISQC_MTD_METHOD_2 | STRING | 100 | — | — |
| 18 | ISQC_MTD_METHOD_20 | STRING | 100 | — | — |
| 19 | ISQC_MTD_METHOD_21 | STRING | 100 | — | — |
| 20 | ISQC_MTD_METHOD_22 | STRING | 100 | — | — |
| 21 | ISQC_MTD_METHOD_23 | STRING | 100 | — | — |
| 22 | ISQC_MTD_METHOD_24 | STRING | 100 | — | — |
| 23 | ISQC_MTD_METHOD_25 | STRING | 100 | — | — |
| 24 | ISQC_MTD_METHOD_3 | STRING | 100 | — | — |
| 25 | ISQC_MTD_METHOD_4 | STRING | 100 | — | — |
| 26 | ISQC_MTD_METHOD_5 | STRING | 100 | — | — |
| 27 | ISQC_MTD_METHOD_6 | STRING | 100 | — | — |
| 28 | ISQC_MTD_METHOD_7 | STRING | 100 | — | — |
| 29 | ISQC_MTD_METHOD_8 | STRING | 100 | — | — |
| 30 | ISQC_MTD_METHOD_9 | STRING | 100 | — | — |
| 31 | ISQC_MTD_NOTES_1 | STRING | 60 | — | — |
| 32 | ISQC_MTD_NOTES_10 | STRING | 60 | — | — |
| 33 | ISQC_MTD_NOTES_2 | STRING | 60 | — | — |
| 34 | ISQC_MTD_NOTES_3 | STRING | 60 | — | — |
| 35 | ISQC_MTD_NOTES_4 | STRING | 60 | — | — |
| 36 | ISQC_MTD_NOTES_5 | STRING | 60 | — | — |
| 37 | ISQC_MTD_NOTES_6 | STRING | 60 | — | — |
| 38 | ISQC_MTD_NOTES_7 | STRING | 60 | — | — |
| 39 | ISQC_MTD_NOTES_8 | STRING | 60 | — | — |
| 40 | ISQC_MTD_NOTES_9 | STRING | 60 | — | — |
| 41 | ISQC_MTD_REV | STRING | 5 | — | — |
| 42 | ISQC_MTD_REVBY | INTEGER | 2 | — | — |
| 43 | ISQC_MTD_REVDT | DATE | 4 | — | — |
| 44 | ISQC_MTD_TSTCOD | STRING | 30 | — | — |

## ISQCRSLT
**PAPERLESS SHOP FLOOR TEST RESULTS**

Fields: 57

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISQC_SPC_ACCEPT | STRING | 1 | — | — |
| 2 | ISQC_SPC_ADATE | DATE | 4 | — | — |
| 3 | ISQC_SPC_ALPHA_1 | STRING | 25 | — | — |
| 4 | ISQC_SPC_ALPHA_2 | STRING | 25 | — | — |
| 5 | ISQC_SPC_ALPHA_3 | STRING | 25 | — | — |
| 6 | ISQC_SPC_ALPHA_4 | STRING | 25 | — | — |
| 7 | ISQC_SPC_ALPHA_5 | STRING | 25 | — | — |
| 8 | ISQC_SPC_ANOTES_1 | STRING | 60 | — | — |
| 9 | ISQC_SPC_ANOTES_2 | STRING | 60 | — | — |
| 10 | ISQC_SPC_ANOTES_3 | STRING | 60 | — | — |
| 11 | ISQC_SPC_ANOTES_4 | STRING | 60 | — | — |
| 12 | ISQC_SPC_ANOTES_5 | STRING | 60 | — | — |
| 13 | ISQC_SPC_APPBY | INTEGER | 2 | — | — |
| 14 | ISQC_SPC_BATCH | STRING | 25 | — | — |
| 15 | ISQC_SPC_CNTR | INTEGER | 2 | — | — |
| 16 | ISQC_SPC_CODE | STRING | 15 | — | — |
| 17 | ISQC_SPC_DATE_1 | DATE | 4 | — | — |
| 18 | ISQC_SPC_DATE_2 | DATE | 4 | — | — |
| 19 | ISQC_SPC_DATE_3 | DATE | 4 | — | — |
| 20 | ISQC_SPC_DATE_4 | DATE | 4 | — | — |
| 21 | ISQC_SPC_DATE_5 | DATE | 4 | — | — |
| 22 | ISQC_SPC_EXPMAX | STRING | 2 | — | — |
| 23 | ISQC_SPC_EXPMIN | STRING | 2 | — | — |
| 24 | ISQC_SPC_EXTRA | STRING | 100 | — | — |
| 25 | ISQC_SPC_INVNUM | NUMERIC | 8 | — | — |
| 26 | ISQC_SPC_ITMNO | STRING | 9 | — | — |
| 27 | ISQC_SPC_LOT | STRING | 15 | — | — |
| 28 | ISQC_SPC_LOTQTY | NUMERIC | 8 | 2 | — |
| 29 | ISQC_SPC_LRNUM | NUMERIC | 8 | — | — |
| 30 | ISQC_SPC_MAX | STRING | 15 | — | — |
| 31 | ISQC_SPC_MIN | STRING | 15 | — | — |
| 32 | ISQC_SPC_NUMERC | STRING | 1 | — | — |
| 33 | ISQC_SPC_OPER | INTEGER | 2 | — | — |
| 34 | ISQC_SPC_PASS | STRING | 1 | — | — |
| 35 | ISQC_SPC_PONUM | NUMERIC | 8 | — | — |
| 36 | ISQC_SPC_PSFAIL | STRING | 4 | — | — |
| 37 | ISQC_SPC_RCVNUM | NUMERIC | 8 | — | — |
| 38 | ISQC_SPC_RESULT | STRING | 15 | — | — |
| 39 | ISQC_SPC_SAMPLE | STRING | 25 | — | — |
| 40 | ISQC_SPC_SAMQTY | NUMERIC | 8 | 2 | — |
| 41 | ISQC_SPC_SERIAL | STRING | 25 | — | — |
| 42 | ISQC_SPC_SOLINE | NUMERIC | 8 | — | — |
| 43 | ISQC_SPC_SONUM | NUMERIC | 8 | — | — |
| 44 | ISQC_SPC_TCNTR | INTEGER | 2 | — | — |
| 45 | ISQC_SPC_TDATE | DATE | 4 | — | — |
| 46 | ISQC_SPC_TESTBY | INTEGER | 2 | — | — |
| 47 | ISQC_SPC_TNOTES_1 | STRING | 60 | — | — |
| 48 | ISQC_SPC_TNOTES_2 | STRING | 60 | — | — |
| 49 | ISQC_SPC_TNOTES_3 | STRING | 60 | — | — |
| 50 | ISQC_SPC_TNOTES_4 | STRING | 60 | — | — |
| 51 | ISQC_SPC_TNOTES_5 | STRING | 60 | — | — |
| 52 | ISQC_SPC_TSTCOD | STRING | 30 | — | — |
| 53 | ISQC_SPC_TSTLOT | STRING | 1 | — | — |
| 54 | ISQC_SPC_TSTQTY | NUMERIC | 8 | 2 | — |
| 55 | ISQC_SPC_UNITS | STRING | 15 | — | — |
| 56 | ISQC_SPC_WOPRE | NUMERIC | 8 | — | — |
| 57 | ISQC_SPC_WOSUF | INTEGER | 2 | — | — |

## ISQCSPEC
**PAPERLESS SHOP FLOOR TEST REQUIREMENTS**

Fields: 57

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISQC_SPC_ACCEPT | STRING | 1 | — | — |
| 2 | ISQC_SPC_ADATE | DATE | 4 | — | — |
| 3 | ISQC_SPC_ALPHA_1 | STRING | 25 | — | — |
| 4 | ISQC_SPC_ALPHA_2 | STRING | 25 | — | — |
| 5 | ISQC_SPC_ALPHA_3 | STRING | 25 | — | — |
| 6 | ISQC_SPC_ALPHA_4 | STRING | 25 | — | — |
| 7 | ISQC_SPC_ALPHA_5 | STRING | 25 | — | — |
| 8 | ISQC_SPC_ANOTES_1 | STRING | 60 | — | — |
| 9 | ISQC_SPC_ANOTES_2 | STRING | 60 | — | — |
| 10 | ISQC_SPC_ANOTES_3 | STRING | 60 | — | — |
| 11 | ISQC_SPC_ANOTES_4 | STRING | 60 | — | — |
| 12 | ISQC_SPC_ANOTES_5 | STRING | 60 | — | — |
| 13 | ISQC_SPC_APPBY | INTEGER | 2 | — | — |
| 14 | ISQC_SPC_BATCH | STRING | 25 | — | — |
| 15 | ISQC_SPC_CNTR | INTEGER | 2 | — | — |
| 16 | ISQC_SPC_CODE | STRING | 15 | — | — |
| 17 | ISQC_SPC_DATE_1 | DATE | 4 | — | — |
| 18 | ISQC_SPC_DATE_2 | DATE | 4 | — | — |
| 19 | ISQC_SPC_DATE_3 | DATE | 4 | — | — |
| 20 | ISQC_SPC_DATE_4 | DATE | 4 | — | — |
| 21 | ISQC_SPC_DATE_5 | DATE | 4 | — | — |
| 22 | ISQC_SPC_EXPMAX | STRING | 2 | — | — |
| 23 | ISQC_SPC_EXPMIN | STRING | 2 | — | — |
| 24 | ISQC_SPC_EXTRA | STRING | 100 | — | — |
| 25 | ISQC_SPC_INVNUM | NUMERIC | 8 | — | — |
| 26 | ISQC_SPC_ITMNO | STRING | 9 | — | — |
| 27 | ISQC_SPC_LOT | STRING | 15 | — | — |
| 28 | ISQC_SPC_LOTQTY | NUMERIC | 8 | 2 | — |
| 29 | ISQC_SPC_LRNUM | NUMERIC | 8 | — | — |
| 30 | ISQC_SPC_MAX | STRING | 15 | — | — |
| 31 | ISQC_SPC_MIN | STRING | 15 | — | — |
| 32 | ISQC_SPC_NUMERC | STRING | 1 | — | — |
| 33 | ISQC_SPC_OPER | INTEGER | 2 | — | — |
| 34 | ISQC_SPC_PASS | STRING | 1 | — | — |
| 35 | ISQC_SPC_PONUM | NUMERIC | 8 | — | — |
| 36 | ISQC_SPC_PSFAIL | STRING | 4 | — | — |
| 37 | ISQC_SPC_RCVNUM | NUMERIC | 8 | — | — |
| 38 | ISQC_SPC_RESULT | STRING | 15 | — | — |
| 39 | ISQC_SPC_SAMPLE | STRING | 25 | — | — |
| 40 | ISQC_SPC_SAMQTY | NUMERIC | 8 | 2 | — |
| 41 | ISQC_SPC_SERIAL | STRING | 25 | — | — |
| 42 | ISQC_SPC_SOLINE | NUMERIC | 8 | — | — |
| 43 | ISQC_SPC_SONUM | NUMERIC | 8 | — | — |
| 44 | ISQC_SPC_TCNTR | INTEGER | 2 | — | — |
| 45 | ISQC_SPC_TDATE | DATE | 4 | — | — |
| 46 | ISQC_SPC_TESTBY | INTEGER | 2 | — | — |
| 47 | ISQC_SPC_TNOTES_1 | STRING | 60 | — | — |
| 48 | ISQC_SPC_TNOTES_2 | STRING | 60 | — | — |
| 49 | ISQC_SPC_TNOTES_3 | STRING | 60 | — | — |
| 50 | ISQC_SPC_TNOTES_4 | STRING | 60 | — | — |
| 51 | ISQC_SPC_TNOTES_5 | STRING | 60 | — | — |
| 52 | ISQC_SPC_TSTCOD | STRING | 30 | — | — |
| 53 | ISQC_SPC_TSTLOT | STRING | 1 | — | — |
| 54 | ISQC_SPC_TSTQTY | NUMERIC | 8 | 2 | — |
| 55 | ISQC_SPC_UNITS | STRING | 15 | — | — |
| 56 | ISQC_SPC_WOPRE | NUMERIC | 8 | — | — |
| 57 | ISQC_SPC_WOSUF | INTEGER | 2 | — | — |

## ISSERIAL
**PARENT TO COMPONENT SERIAL MAP**

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

## ISWODESC
**DBA WORK ORDER NOTES**

Fields: 5

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BK_DESC_CODE | STRING | 15 | — | not used |
| 2 | BK_DESC_DESC | STRING | 25 | — | not used |
| 3 | BK_DESC_LINE | INTEGER | 2 | — | Notes line number |
| 4 | BK_DESC_NOTES | STRING | 70 | — | Notes - text |
| 5 | BK_DESC_NUM | NUMERIC | 8 | — | PO Number |

## ISWOEX
**WORK ORDER HEADER 2**

Fields: 39

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_WOEX_ALPHA1 | STRING | 30 | — | — |
| 2 | IS_WOEX_ALPHA2 | STRING | 30 | — | — |
| 3 | IS_WOEX_ALPHA3 | STRING | 1 | — | — |
| 4 | IS_WOEX_ALPHA4 | STRING | 1 | — | — |
| 5 | IS_WOEX_ALPHA5 | STRING | 1 | — | — |
| 6 | IS_WOEX_CAUSE | STRING | 30 | — | — |
| 7 | IS_WOEX_CDATE | DATE | 4 | — | — |
| 8 | IS_WOEX_DATE1 | DATE | 4 | — | — |
| 9 | IS_WOEX_DATE2 | DATE | 4 | — | — |
| 10 | IS_WOEX_DATE3 | DATE | 4 | — | — |
| 11 | IS_WOEX_DATE4 | DATE | 4 | — | — |
| 12 | IS_WOEX_DATE5 | DATE | 4 | — | — |
| 13 | IS_WOEX_DESC1 | STRING | 30 | — | — |
| 14 | IS_WOEX_DESC2 | STRING | 30 | — | — |
| 15 | IS_WOEX_DESC3 | STRING | 30 | — | — |
| 16 | IS_WOEX_DESC4 | STRING | 30 | — | — |
| 17 | IS_WOEX_DESC5 | STRING | 30 | — | — |
| 18 | IS_WOEX_EXTRA | STRING | 100 | — | — |
| 19 | IS_WOEX_GDATE | DATE | 4 | — | — |
| 20 | IS_WOEX_INT1 | INTEGER | 2 | — | — |
| 21 | IS_WOEX_INT2 | INTEGER | 2 | — | — |
| 22 | IS_WOEX_INT3 | INTEGER | 2 | — | — |
| 23 | IS_WOEX_INT4 | INTEGER | 2 | — | — |
| 24 | IS_WOEX_INT5 | INTEGER | 2 | — | — |
| 25 | IS_WOEX_ITP | STRING | 20 | — | — |
| 26 | IS_WOEX_ITPP | STRING | 1 | — | — |
| 27 | IS_WOEX_MCLASS | STRING | 6 | — | — |
| 28 | IS_WOEX_MNUM | NUMERIC | 8 | — | — |
| 29 | IS_WOEX_NOTE_1 | STRING | 100 | — | — |
| 30 | IS_WOEX_NOTE_2 | STRING | 100 | — | — |
| 31 | IS_WOEX_NOTE_3 | STRING | 100 | — | — |
| 32 | IS_WOEX_NOTE_4 | STRING | 100 | — | — |
| 33 | IS_WOEX_NOTE_5 | STRING | 100 | — | — |
| 34 | IS_WOEX_NUM1 | NUMERIC | 8 | 3 | — |
| 35 | IS_WOEX_NUM2 | NUMERIC | 8 | 4 | — |
| 36 | IS_WOEX_RF | STRING | 1 | — | — |
| 37 | IS_WOEX_WC | STRING | 12 | — | — |
| 38 | IS_WOEX_WOPRE | NUMERIC | 8 | — | — |
| 39 | IS_WOEX_WOSUF | INTEGER | 2 | — | — |

## ISWOHDSC
**ARCHIVED DBA WORK ORDER NOTES**

Fields: 5

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BK_DESC_CODE | STRING | 15 | — | not used |
| 2 | BK_DESC_DESC | STRING | 25 | — | not used |
| 3 | BK_DESC_LINE | INTEGER | 2 | — | Notes line number |
| 4 | BK_DESC_NOTES | STRING | 70 | — | Notes - text |
| 5 | BK_DESC_NUM | NUMERIC | 8 | — | PO Number |

## ISWOPRIO
**WORK ORDER PRIORITY MASTER**

Fields: 4

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_WOPRIO_COLOR | NUMERIC | 8 | — | — |
| 2 | IS_WOPRIO_DESC | STRING | 30 | — | — |
| 3 | IS_WOPRIO_EXTRA | STRING | 100 | — | — |
| 4 | IS_WOPRIO_PRIO | STRING | 1 | — | — |

## ISWOROEX
**WORK ORDER ROUTING ADJUNCT FILE**

Fields: 51

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_WROEX_ALPHA1 | STRING | 1 | — | — |
| 2 | IS_WROEX_ALPHA2 | STRING | 2 | — | — |
| 3 | IS_WROEX_ALPHA3_1 | STRING | 15 | — | — |
| 4 | IS_WROEX_ALPHA3_10 | STRING | 15 | — | — |
| 5 | IS_WROEX_ALPHA3_2 | STRING | 15 | — | — |
| 6 | IS_WROEX_ALPHA3_3 | STRING | 15 | — | — |
| 7 | IS_WROEX_ALPHA3_4 | STRING | 15 | — | — |
| 8 | IS_WROEX_ALPHA3_5 | STRING | 15 | — | — |
| 9 | IS_WROEX_ALPHA3_6 | STRING | 15 | — | — |
| 10 | IS_WROEX_ALPHA3_7 | STRING | 15 | — | — |
| 11 | IS_WROEX_ALPHA3_8 | STRING | 15 | — | — |
| 12 | IS_WROEX_ALPHA3_9 | STRING | 15 | — | — |
| 13 | IS_WROEX_DATE1 | DATE | 4 | — | — |
| 14 | IS_WROEX_DATE2_1 | DATE | 4 | — | — |
| 15 | IS_WROEX_DATE2_10 | DATE | 4 | — | — |
| 16 | IS_WROEX_DATE2_2 | DATE | 4 | — | — |
| 17 | IS_WROEX_DATE2_3 | DATE | 4 | — | — |
| 18 | IS_WROEX_DATE2_4 | DATE | 4 | — | — |
| 19 | IS_WROEX_DATE2_5 | DATE | 4 | — | — |
| 20 | IS_WROEX_DATE2_6 | DATE | 4 | — | — |
| 21 | IS_WROEX_DATE2_7 | DATE | 4 | — | — |
| 22 | IS_WROEX_DATE2_8 | DATE | 4 | — | — |
| 23 | IS_WROEX_DATE2_9 | DATE | 4 | — | — |
| 24 | IS_WROEX_DESC1 | STRING | 30 | — | — |
| 25 | IS_WROEX_EXTRA | STRING | 100 | — | — |
| 26 | IS_WROEX_FDAY | INTEGER | 2 | — | — |
| 27 | IS_WROEX_FLAG_1 | STRING | 1 | — | — |
| 28 | IS_WROEX_FLAG_2 | STRING | 1 | — | — |
| 29 | IS_WROEX_FLAG_3 | STRING | 1 | — | — |
| 30 | IS_WROEX_FLAG_4 | STRING | 1 | — | — |
| 31 | IS_WROEX_FLAG_5 | STRING | 1 | — | — |
| 32 | IS_WROEX_FOI | STRING | 1 | — | — |
| 33 | IS_WROEX_INT_1 | INTEGER | 2 | — | — |
| 34 | IS_WROEX_INT_2 | INTEGER | 2 | — | — |
| 35 | IS_WROEX_INT_3 | INTEGER | 2 | — | — |
| 36 | IS_WROEX_INT_4 | INTEGER | 2 | — | — |
| 37 | IS_WROEX_INT_5 | INTEGER | 2 | — | — |
| 38 | IS_WROEX_ITP | STRING | 20 | — | — |
| 39 | IS_WROEX_ITPP | STRING | 1 | — | — |
| 40 | IS_WROEX_LQTY | NUMERIC | 8 | 2 | — |
| 41 | IS_WROEX_NUM1 | NUMERIC | 8 | — | — |
| 42 | IS_WROEX_NUM2_1 | NUMERIC | 8 | — | — |
| 43 | IS_WROEX_NUM2_2 | NUMERIC | 8 | — | — |
| 44 | IS_WROEX_NUM2_3 | NUMERIC | 8 | — | — |
| 45 | IS_WROEX_NUM2_4 | NUMERIC | 8 | — | — |
| 46 | IS_WROEX_NUM2_5 | NUMERIC | 8 | — | — |
| 47 | IS_WROEX_OPER | INTEGER | 2 | — | — |
| 48 | IS_WROEX_PRMACH | STRING | 4 | — | — |
| 49 | IS_WROEX_SDAY | INTEGER | 2 | — | — |
| 50 | IS_WROEX_WOPRE | NUMERIC | 8 | — | — |
| 51 | IS_WROEX_WOSUF | INTEGER | 2 | — | — |

## ISWOTRAY
**PAPERLESS BATCH TRACKING**

Fields: 52

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_TRAY_ALPHA_1 | STRING | 25 | — | — |
| 2 | IS_TRAY_ALPHA_10 | STRING | 25 | — | — |
| 3 | IS_TRAY_ALPHA_11 | STRING | 25 | — | — |
| 4 | IS_TRAY_ALPHA_12 | STRING | 25 | — | — |
| 5 | IS_TRAY_ALPHA_13 | STRING | 25 | — | — |
| 6 | IS_TRAY_ALPHA_14 | STRING | 25 | — | — |
| 7 | IS_TRAY_ALPHA_15 | STRING | 25 | — | — |
| 8 | IS_TRAY_ALPHA_16 | STRING | 25 | — | — |
| 9 | IS_TRAY_ALPHA_17 | STRING | 25 | — | — |
| 10 | IS_TRAY_ALPHA_18 | STRING | 25 | — | — |
| 11 | IS_TRAY_ALPHA_19 | STRING | 25 | — | — |
| 12 | IS_TRAY_ALPHA_2 | STRING | 25 | — | — |
| 13 | IS_TRAY_ALPHA_20 | STRING | 25 | — | — |
| 14 | IS_TRAY_ALPHA_3 | STRING | 25 | — | — |
| 15 | IS_TRAY_ALPHA_4 | STRING | 25 | — | — |
| 16 | IS_TRAY_ALPHA_5 | STRING | 25 | — | — |
| 17 | IS_TRAY_ALPHA_6 | STRING | 25 | — | — |
| 18 | IS_TRAY_ALPHA_7 | STRING | 25 | — | — |
| 19 | IS_TRAY_ALPHA_8 | STRING | 25 | — | — |
| 20 | IS_TRAY_ALPHA_9 | STRING | 25 | — | — |
| 21 | IS_TRAY_BIN_1 | STRING | 15 | — | — |
| 22 | IS_TRAY_BIN_2 | STRING | 15 | — | — |
| 23 | IS_TRAY_BIN_3 | STRING | 15 | — | — |
| 24 | IS_TRAY_BIN_4 | STRING | 15 | — | — |
| 25 | IS_TRAY_BIN_5 | STRING | 15 | — | — |
| 26 | IS_TRAY_BINQTY_1 | NUMERIC | 8 | 2 | — |
| 27 | IS_TRAY_BINQTY_2 | NUMERIC | 8 | 2 | — |
| 28 | IS_TRAY_BINQTY_3 | NUMERIC | 8 | 2 | — |
| 29 | IS_TRAY_BINQTY_4 | NUMERIC | 8 | 2 | — |
| 30 | IS_TRAY_BINQTY_5 | NUMERIC | 8 | 2 | — |
| 31 | IS_TRAY_CODE | STRING | 15 | — | — |
| 32 | IS_TRAY_COMQTY | NUMERIC | 8 | 2 | — |
| 33 | IS_TRAY_DATE_1 | DATE | 4 | — | — |
| 34 | IS_TRAY_DATE_2 | DATE | 4 | — | — |
| 35 | IS_TRAY_DATE_3 | DATE | 4 | — | — |
| 36 | IS_TRAY_DATE_4 | DATE | 4 | — | — |
| 37 | IS_TRAY_DATE_5 | DATE | 4 | — | — |
| 38 | IS_TRAY_EXTRA | STRING | 100 | — | — |
| 39 | IS_TRAY_LOC_1 | STRING | 10 | — | — |
| 40 | IS_TRAY_LOC_2 | STRING | 10 | — | — |
| 41 | IS_TRAY_LOC_3 | STRING | 10 | — | — |
| 42 | IS_TRAY_LOC_4 | STRING | 10 | — | — |
| 43 | IS_TRAY_LOC_5 | STRING | 10 | — | — |
| 44 | IS_TRAY_NUM | STRING | 25 | — | — |
| 45 | IS_TRAY_OPDESC | STRING | 30 | — | — |
| 46 | IS_TRAY_OPER | INTEGER | 2 | — | — |
| 47 | IS_TRAY_QCQTY | NUMERIC | 8 | 2 | — |
| 48 | IS_TRAY_QCREQD | STRING | 1 | — | — |
| 49 | IS_TRAY_SCRPQTY | NUMERIC | 8 | 2 | — |
| 50 | IS_TRAY_SQTY | NUMERIC | 8 | 2 | — |
| 51 | IS_TRAY_WOPRE | NUMERIC | 8 | — | — |
| 52 | IS_TRAY_WOSUF | INTEGER | 2 | — | — |

## MTEXCHG
**EXTRA CHARGES**

Fields: 7

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | EXCHG_AMT | NUMERIC | 8 | 6 | — |
| 2 | EXCHG_CODE | STRING | 15 | — | — |
| 3 | EXCHG_COST | NUMERIC | 8 | 6 | — |
| 4 | EXCHG_DESC | STRING | 30 | — | — |
| 5 | EXCHG_EXTRA | STRING | 50 | — | — |
| 6 | EXCHG_LINE | NUMERIC | 8 | — | — |
| 7 | EXCHG_QUOTE | NUMERIC | 8 | — | — |

## OUTHPROC
**OUTSIDE PROCESSING TRANSACTIONS - ARCHIVE**

Fields: 15

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MTPO_ASSY | STRING | 15 | — | Assembly Used |
| 2 | MTPO_ASSYDESC | STRING | 30 | — | Assembly Description |
| 3 | MTPO_COST | NUMERIC | 8 | 4 | Cost |
| 4 | MTPO_DATE | DATE | 4 | — | Date |
| 5 | MTPO_DESC | STRING | 25 | — | Description |
| 6 | MTPO_EXTPR | NUMERIC | 8 | 2 | Extra Process |
| 7 | MTPO_EXTRA | STRING | 50 | — | Extra |
| 8 | MTPO_OPER | INTEGER | 2 | — | WO Operation |
| 9 | MTPO_PO | NUMERIC | 8 | — | PO Inspect/Receive PO Number |
| 10 | MTPO_PROD | STRING | 15 | — | Part Code |
| 11 | MTPO_QTY | NUMERIC | 8 | 2 | Quantity |
| 12 | MTPO_VENDNAME | STRING | 20 | — | PO Inspect/Receive Vendor Name |
| 13 | MTPO_VENDOR | STRING | 10 | — | PO Inspect/Receive Vendor |
| 14 | MTPO_WOPRE | NUMERIC | 8 | — | Work Order Prefix |
| 15 | MTPO_WOSUF | INTEGER | 2 | — | Work Order Suffix |

## OUTPROC
**OUTSIDE PROCESSING TRANSACTIONS**

Fields: 15

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MTPO_ASSY | STRING | 15 | — | Assembly Used |
| 2 | MTPO_ASSYDESC | STRING | 30 | — | Assembly Description |
| 3 | MTPO_COST | NUMERIC | 8 | 4 | Cost |
| 4 | MTPO_DATE | DATE | 4 | — | Date |
| 5 | MTPO_DESC | STRING | 25 | — | Description |
| 6 | MTPO_EXTPR | NUMERIC | 8 | 2 | Extra Process |
| 7 | MTPO_EXTRA | STRING | 50 | — | Extra |
| 8 | MTPO_OPER | INTEGER | 2 | — | WO Operation |
| 9 | MTPO_PO | NUMERIC | 8 | — | PO Inspect/Receive PO Number |
| 10 | MTPO_PROD | STRING | 15 | — | Part Code |
| 11 | MTPO_QTY | NUMERIC | 8 | 2 | Quantity |
| 12 | MTPO_VENDNAME | STRING | 20 | — | PO Inspect/Receive Vendor Name |
| 13 | MTPO_VENDOR | STRING | 10 | — | PO Inspect/Receive Vendor |
| 14 | MTPO_WOPRE | NUMERIC | 8 | — | Work Order Prefix |
| 15 | MTPO_WOSUF | INTEGER | 2 | — | Work Order Suffix |

## QCCODES
**QC CODES**

Fields: 2

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MTQC_CODE | STRING | 2 | — | QC Code |
| 2 | MTQC_DESC | STRING | 30 | — | QC Code Description |

## SCRAP
**SCRAP CODES**

Fields: 21

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MTSCRAP_ALPHA_1 | STRING | 30 | — | — |
| 2 | MTSCRAP_ALPHA_2 | STRING | 30 | — | — |
| 3 | MTSCRAP_ALPHA_3 | STRING | 30 | — | — |
| 4 | MTSCRAP_ALPHA_4 | STRING | 30 | — | — |
| 5 | MTSCRAP_ALPHA_5 | STRING | 30 | — | — |
| 6 | MTSCRAP_CODE | STRING | 2 | — | — |
| 7 | MTSCRAP_DATE_1 | DATE | 4 | — | — |
| 8 | MTSCRAP_DATE_2 | DATE | 4 | — | — |
| 9 | MTSCRAP_DATE_3 | DATE | 4 | — | — |
| 10 | MTSCRAP_DATE_4 | DATE | 4 | — | — |
| 11 | MTSCRAP_DATE_5 | DATE | 4 | — | — |
| 12 | MTSCRAP_DESC | STRING | 30 | — | — |
| 13 | MTSCRAP_EXTRA | STRING | 50 | — | — |
| 14 | MTSCRAP_FLAG_1 | STRING | 1 | — | — |
| 15 | MTSCRAP_FLAG_2 | STRING | 1 | — | — |
| 16 | MTSCRAP_FLAG_3 | STRING | 1 | — | — |
| 17 | MTSCRAP_FLAG_4 | STRING | 1 | — | — |
| 18 | MTSCRAP_FLAG_5 | STRING | 1 | — | — |
| 19 | MTSCRAP_GLACCT | STRING | 10 | — | — |
| 20 | MTSCRAP_GLDPT | STRING | 4 | — | — |
| 21 | MTSCRAP_TYPE | STRING | 1 | — | — |

## WCTRLOAD
**WORK CENTER LOAD %**

Fields: 8

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | WC_LOAD_CAP | NUMERIC | 8 | 2 | — |
| 2 | WC_LOAD_DATE | DATE | 4 | — | — |
| 3 | WC_LOAD_EXTRA | STRING | 100 | — | — |
| 4 | WC_LOAD_LOAD | NUMERIC | 8 | 2 | — |
| 5 | WC_LOAD_TOTHRS | NUMERIC | 8 | 2 | — |
| 6 | WC_LOAD_UDATE | DATE | 4 | — | — |
| 7 | WC_LOAD_UTIL | NUMERIC | 8 | 2 | — |
| 8 | WC_LOAD_WC | STRING | 12 | — | — |

## WOBOM
**WORK ORDER BILL OF MATERIAL**

Fields: 26

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | WOBOM_^ISSUED | NUMERIC | 8 | 2 | — |
| 2 | WOBOM_AMATCST | NUMERIC | 8 | 2 | — |
| 3 | WOBOM_ASSY | STRING | 15 | — | — |
| 4 | WOBOM_ASSYDESC | STRING | 30 | — | — |
| 5 | WOBOM_ASSYQTY | NUMERIC | 8 | 2 | — |
| 6 | WOBOM_BINLOC | STRING | 10 | — | — |
| 7 | WOBOM_COMPCODE | STRING | 15 | — | — |
| 8 | WOBOM_COMPDESC | STRING | 30 | — | — |
| 9 | WOBOM_EMATCST | NUMERIC | 8 | 2 | — |
| 10 | WOBOM_EXTRA | STRING | 50 | — | — |
| 11 | WOBOM_LINE^ | INTEGER | 2 | — | — |
| 12 | WOBOM_OPER | INTEGER | 2 | — | — |
| 13 | WOBOM_OPTION | STRING | 1 | — | — |
| 14 | WOBOM_QTYISSUED | NUMERIC | 8 | 4 | — |
| 15 | WOBOM_QTYPER | NUMERIC | 8 | 8 | — |
| 16 | WOBOM_REFERENCE | STRING | 20 | — | — |
| 17 | WOBOM_REV | STRING | 5 | — | — |
| 18 | WOBOM_SCRAPQTY | NUMERIC | 8 | 8 | — |
| 19 | WOBOM_SEQ | INTEGER | 2 | — | — |
| 20 | WOBOM_START | DATE | 4 | — | — |
| 21 | WOBOM_TOTQTY | NUMERIC | 8 | 4 | — |
| 22 | WOBOM_UID | STRING | 30 | — | — |
| 23 | WOBOM_UM | STRING | 3 | — | — |
| 24 | WOBOM_VEND | STRING | 10 | — | — |
| 25 | WOBOM_WOPRE | NUMERIC | 8 | — | — |
| 26 | WOBOM_WOSUF | INTEGER | 2 | — | — |

## WOBOMHRM
**WO BILL OF MATERIAL REMARKS - ARCHIVE**

Fields: 7

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | WOBOM_RM_COMP | STRING | 15 | — | — |
| 2 | WOBOM_RM_LINE | INTEGER | 2 | — | — |
| 3 | WOBOM_RM_LINENM | INTEGER | 2 | — | — |
| 4 | WOBOM_RM_PARENT | STRING | 15 | — | — |
| 5 | WOBOM_RM_REMARK | STRING | 30 | — | — |
| 6 | WOBOM_RM_WOPRE | NUMERIC | 8 | — | — |
| 7 | WOBOM_RM_WOSUF | INTEGER | 2 | — | — |

## WOBOMREM
**WO BILL OF MATERIAL REMARKS**

Fields: 7

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | WOBOM_RM_COMP | STRING | 15 | — | — |
| 2 | WOBOM_RM_LINE | INTEGER | 2 | — | — |
| 3 | WOBOM_RM_LINENM | INTEGER | 2 | — | — |
| 4 | WOBOM_RM_PARENT | STRING | 15 | — | — |
| 5 | WOBOM_RM_REMARK | STRING | 30 | — | — |
| 6 | WOBOM_RM_WOPRE | NUMERIC | 8 | — | — |
| 7 | WOBOM_RM_WOSUF | INTEGER | 2 | — | — |

## WODATE
**WORK ORDER DATES**

Fields: 12

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | WODATE_DELPRE | NUMERIC | 8 | — | — |
| 2 | WODATE_DELSUF | INTEGER | 2 | — | — |
| 3 | WODATE_EXTRA | STRING | 100 | — | — |
| 4 | WODATE_FINISH | DATE | 4 | — | — |
| 5 | WODATE_PARPRE | NUMERIC | 8 | — | — |
| 6 | WODATE_PARSUF | INTEGER | 2 | — | — |
| 7 | WODATE_QTY | NUMERIC | 8 | 2 | — |
| 8 | WODATE_START | DATE | 4 | — | — |
| 9 | WODATE_TOPPRE | NUMERIC | 8 | — | — |
| 10 | WODATE_TOPSUF | INTEGER | 2 | — | — |
| 11 | WODATE_WOPRE | NUMERIC | 8 | — | — |
| 12 | WODATE_WOSUF | INTEGER | 2 | — | — |

## WOEXCHG
**WORK ORDER EXTRA CHARGES**

Fields: 10

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MTWO_EX_CHG | NUMERIC | 8 | 6 | — |
| 2 | MTWO_EX_CHGDESC | STRING | 30 | — | — |
| 3 | MTWO_EX_DATE | DATE | 4 | — | — |
| 4 | MTWO_EX_DESC | STRING | 30 | — | — |
| 5 | MTWO_EX_GLACCT | STRING | 10 | — | — |
| 6 | MTWO_EX_GLDPT | STRING | 4 | — | — |
| 7 | MTWO_EX_OP | INTEGER | 2 | — | — |
| 8 | MTWO_EX_PROD | STRING | 15 | — | — |
| 9 | MTWO_EX_WOPRE | NUMERIC | 8 | — | — |
| 10 | MTWO_EX_WOSUF | INTEGER | 2 | — | — |

## WOHBOM
**WORK ORDER BILL OF MATERIAL - ARCHIVE**

Fields: 26

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | WOBOM_^ISSUED | NUMERIC | 8 | 2 | — |
| 2 | WOBOM_AMATCST | NUMERIC | 8 | 2 | — |
| 3 | WOBOM_ASSY | STRING | 15 | — | — |
| 4 | WOBOM_ASSYDESC | STRING | 30 | — | — |
| 5 | WOBOM_ASSYQTY | NUMERIC | 8 | 2 | — |
| 6 | WOBOM_BINLOC | STRING | 10 | — | — |
| 7 | WOBOM_COMPCODE | STRING | 15 | — | — |
| 8 | WOBOM_COMPDESC | STRING | 30 | — | — |
| 9 | WOBOM_EMATCST | NUMERIC | 8 | 2 | — |
| 10 | WOBOM_EXTRA | STRING | 50 | — | — |
| 11 | WOBOM_LINE^ | INTEGER | 2 | — | — |
| 12 | WOBOM_OPER | INTEGER | 2 | — | — |
| 13 | WOBOM_OPTION | STRING | 1 | — | — |
| 14 | WOBOM_QTYISSUED | NUMERIC | 8 | 4 | — |
| 15 | WOBOM_QTYPER | NUMERIC | 8 | 8 | — |
| 16 | WOBOM_REFERENCE | STRING | 20 | — | — |
| 17 | WOBOM_REV | STRING | 5 | — | — |
| 18 | WOBOM_SCRAPQTY | NUMERIC | 8 | 8 | — |
| 19 | WOBOM_SEQ | INTEGER | 2 | — | — |
| 20 | WOBOM_START | DATE | 4 | — | — |
| 21 | WOBOM_TOTQTY | NUMERIC | 8 | 4 | — |
| 22 | WOBOM_UID | STRING | 30 | — | — |
| 23 | WOBOM_UM | STRING | 3 | — | — |
| 24 | WOBOM_VEND | STRING | 10 | — | — |
| 25 | WOBOM_WOPRE | NUMERIC | 8 | — | — |
| 26 | WOBOM_WOSUF | INTEGER | 2 | — | — |

## WOHDATE
**WORK ORDER DATES - ARCHIVE**

Fields: 12

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | WODATE_DELPRE | NUMERIC | 8 | — | — |
| 2 | WODATE_DELSUF | INTEGER | 2 | — | — |
| 3 | WODATE_EXTRA | STRING | 100 | — | — |
| 4 | WODATE_FINISH | DATE | 4 | — | — |
| 5 | WODATE_PARPRE | NUMERIC | 8 | — | — |
| 6 | WODATE_PARSUF | INTEGER | 2 | — | — |
| 7 | WODATE_QTY | NUMERIC | 8 | 2 | — |
| 8 | WODATE_START | DATE | 4 | — | — |
| 9 | WODATE_TOPPRE | NUMERIC | 8 | — | — |
| 10 | WODATE_TOPSUF | INTEGER | 2 | — | — |
| 11 | WODATE_WOPRE | NUMERIC | 8 | — | — |
| 12 | WODATE_WOSUF | INTEGER | 2 | — | — |

## WOHEXCHG
**WORK ORDER EXTRA CHARGES - ARCHIVE**

Fields: 10

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MTWO_EX_CHG | NUMERIC | 8 | 6 | — |
| 2 | MTWO_EX_CHGDESC | STRING | 30 | — | — |
| 3 | MTWO_EX_DATE | DATE | 4 | — | — |
| 4 | MTWO_EX_DESC | STRING | 30 | — | — |
| 5 | MTWO_EX_GLACCT | STRING | 10 | — | — |
| 6 | MTWO_EX_GLDPT | STRING | 4 | — | — |
| 7 | MTWO_EX_OP | INTEGER | 2 | — | — |
| 8 | MTWO_EX_PROD | STRING | 15 | — | — |
| 9 | MTWO_EX_WOPRE | NUMERIC | 8 | — | — |
| 10 | MTWO_EX_WOSUF | INTEGER | 2 | — | — |

## WOHLABOR
**LABOR TRANSACTIONS - ARCHIVE**

Fields: 45

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MTWOLA_ASSY | STRING | 15 | — | — |
| 2 | MTWOLA_ASSYDESC | STRING | 30 | — | — |
| 3 | MTWOLA_AUDIT | STRING | 35 | — | — |
| 4 | MTWOLA_COMPLETE | STRING | 1 | — | — |
| 5 | MTWOLA_DATE | DATE | 4 | — | — |
| 6 | MTWOLA_DATE2 | DATE | 4 | — | — |
| 7 | MTWOLA_DEDUCT | TIME | 4 | — | — |
| 8 | MTWOLA_EMP | INTEGER | 2 | — | — |
| 9 | MTWOLA_EMP2 | INTEGER | 2 | — | — |
| 10 | MTWOLA_EXTRA | STRING | 50 | — | — |
| 11 | MTWOLA_FOHCOST | NUMERIC | 8 | 2 | — |
| 12 | MTWOLA_LABCOST | NUMERIC | 8 | 2 | — |
| 13 | MTWOLA_LABRATE | NUMERIC | 8 | 4 | — |
| 14 | MTWOLA_MACH | STRING | 4 | — | — |
| 15 | MTWOLA_MACHCOST | NUMERIC | 8 | 2 | — |
| 16 | MTWOLA_MACHDATE | DATE | 4 | — | — |
| 17 | MTWOLA_MISC | NUMERIC | 8 | 6 | — |
| 18 | MTWOLA_MISCDESC | STRING | 30 | — | — |
| 19 | MTWOLA_NOJOBS | INTEGER | 2 | — | — |
| 20 | MTWOLA_OPER | INTEGER | 2 | — | — |
| 21 | MTWOLA_OTEAM | INTEGER | 2 | — | — |
| 22 | MTWOLA_PARTS | NUMERIC | 8 | 2 | — |
| 23 | MTWOLA_POSTED | STRING | 1 | — | — |
| 24 | MTWOLA_QCCODE | STRING | 2 | — | — |
| 25 | MTWOLA_QCDESC | STRING | 30 | — | — |
| 26 | MTWOLA_REGOVER | STRING | 1 | — | — |
| 27 | MTWOLA_REWORK | STRING | 1 | — | — |
| 28 | MTWOLA_RUNHRS | NUMERIC | 8 | 2 | — |
| 29 | MTWOLA_SCDESC | STRING | 30 | — | — |
| 30 | MTWOLA_SCRAPCD | STRING | 2 | — | — |
| 31 | MTWOLA_SCRAPPED | NUMERIC | 8 | 2 | — |
| 32 | MTWOLA_SETCOST | NUMERIC | 8 | 2 | — |
| 33 | MTWOLA_SETUPHRS | NUMERIC | 8 | 2 | — |
| 34 | MTWOLA_SHIFT | INTEGER | 2 | — | — |
| 35 | MTWOLA_START | TIME | 4 | — | — |
| 36 | MTWOLA_STOP | TIME | 4 | — | — |
| 37 | MTWOLA_TEAM | INTEGER | 2 | — | — |
| 38 | MTWOLA_TOOL | STRING | 15 | — | — |
| 39 | MTWOLA_TOOLDATE | DATE | 4 | — | — |
| 40 | MTWOLA_TRXN | INTEGER | 2 | — | — |
| 41 | MTWOLA_VOHCOST | NUMERIC | 8 | 2 | — |
| 42 | MTWOLA_WC | STRING | 12 | — | — |
| 43 | MTWOLA_WCDATE | DATE | 4 | — | — |
| 44 | MTWOLA_WOPRE | NUMERIC | 8 | — | — |
| 45 | MTWOLA_WOSUF | INTEGER | 2 | — | — |

## WOHMAT
**MATERIAL TRANSACTIONS - ARCHIVE**

Fields: 17

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MTWO_PRODCODE | STRING | 15 | — | — |
| 2 | WOMAT_COST | NUMERIC | 8 | 2 | — |
| 3 | WOMAT_DATE | DATE | 4 | — | — |
| 4 | WOMAT_EXTRA | STRING | 50 | — | — |
| 5 | WOMAT_KIT | STRING | 1 | — | — |
| 6 | WOMAT_LOT | STRING | 15 | — | — |
| 7 | WOMAT_PCODE | STRING | 15 | — | — |
| 8 | WOMAT_PDESC | STRING | 30 | — | — |
| 9 | WOMAT_PRODDESC | STRING | 30 | — | — |
| 10 | WOMAT_QTYISSUED | NUMERIC | 8 | 4 | — |
| 11 | WOMAT_QTYSCRAP | NUMERIC | 8 | 2 | — |
| 12 | WOMAT_REF | STRING | 15 | — | — |
| 13 | WOMAT_SCDESC | STRING | 30 | — | — |
| 14 | WOMAT_SCRAPCD | STRING | 2 | — | — |
| 15 | WOMAT_SERIAL | STRING | 25 | — | — |
| 16 | WOMAT_WOPRE | NUMERIC | 8 | — | — |
| 17 | WOMAT_WOSUF | INTEGER | 2 | — | — |

## WOHRECV
**WORK ORDER RECEIPTS - ARCHIVE**

Fields: 11

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MTWOR_ASSY | STRING | 15 | — | — |
| 2 | MTWOR_AVGC | NUMERIC | 8 | 4 | — |
| 3 | MTWOR_DATE | DATE | 4 | — | — |
| 4 | MTWOR_DESC | STRING | 30 | — | — |
| 5 | MTWOR_LOT | STRING | 15 | — | — |
| 6 | MTWOR_QTY | NUMERIC | 8 | 2 | — |
| 7 | MTWOR_REF | STRING | 15 | — | — |
| 8 | MTWOR_SERIAL | STRING | 25 | — | — |
| 9 | MTWOR_USESTD | STRING | 1 | — | — |
| 10 | MTWOR_WOPRE | NUMERIC | 8 | — | — |
| 11 | MTWOR_WOSUF | INTEGER | 2 | — | — |

## WOHROUT
**WORK ORDER ROUTING - ARCHIVE**

Fields: 83

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MTWORO_^COMP | INTEGER | 2 | — | — |
| 2 | MTWORO_ACTHRS | NUMERIC | 8 | 4 | — |
| 3 | MTWORO_AFOHCST | NUMERIC | 8 | 4 | — |
| 4 | MTWORO_ALABCST | NUMERIC | 8 | 4 | — |
| 5 | MTWORO_AMCHCST | NUMERIC | 8 | 4 | — |
| 6 | MTWORO_AOUTCST | NUMERIC | 8 | 4 | — |
| 7 | MTWORO_ASETCST | NUMERIC | 8 | 4 | — |
| 8 | MTWORO_ASETHRS | NUMERIC | 8 | 4 | — |
| 9 | MTWORO_AVOHCST | NUMERIC | 8 | 4 | — |
| 10 | MTWORO_CODE | STRING | 15 | — | — |
| 11 | MTWORO_CONTNTN | NUMERIC | 8 | — | — |
| 12 | MTWORO_DEPT | STRING | 3 | — | — |
| 13 | MTWORO_DESC | STRING | 30 | — | — |
| 14 | MTWORO_EFOHCST | NUMERIC | 8 | 4 | — |
| 15 | MTWORO_ELABCST | NUMERIC | 8 | 4 | — |
| 16 | MTWORO_EMCHCST | NUMERIC | 8 | 4 | — |
| 17 | MTWORO_EOUTCST | NUMERIC | 8 | 4 | — |
| 18 | MTWORO_ESETCST | NUMERIC | 8 | 4 | — |
| 19 | MTWORO_ESETHRS | NUMERIC | 8 | 4 | — |
| 20 | MTWORO_ESSTHRS | TIME | 4 | — | — |
| 21 | MTWORO_ESTHRS | NUMERIC | 8 | 4 | — |
| 22 | MTWORO_EVOHCST | NUMERIC | 8 | 4 | — |
| 23 | MTWORO_EXTRA | STRING | 150 | — | — |
| 24 | MTWORO_FINISH | DATE | 4 | — | — |
| 25 | MTWORO_FINISH2 | DATE | 4 | — | — |
| 26 | MTWORO_FINISHED | DATE | 4 | — | — |
| 27 | MTWORO_INSTR_1 | STRING | 60 | — | — |
| 28 | MTWORO_INSTR_10 | STRING | 60 | — | — |
| 29 | MTWORO_INSTR_11 | STRING | 60 | — | — |
| 30 | MTWORO_INSTR_12 | STRING | 60 | — | — |
| 31 | MTWORO_INSTR_13 | STRING | 60 | — | — |
| 32 | MTWORO_INSTR_14 | STRING | 60 | — | — |
| 33 | MTWORO_INSTR_15 | STRING | 60 | — | — |
| 34 | MTWORO_INSTR_2 | STRING | 60 | — | — |
| 35 | MTWORO_INSTR_3 | STRING | 60 | — | — |
| 36 | MTWORO_INSTR_4 | STRING | 60 | — | — |
| 37 | MTWORO_INSTR_5 | STRING | 60 | — | — |
| 38 | MTWORO_INSTR_6 | STRING | 60 | — | — |
| 39 | MTWORO_INSTR_7 | STRING | 60 | — | — |
| 40 | MTWORO_INSTR_8 | STRING | 60 | — | — |
| 41 | MTWORO_INSTR_9 | STRING | 60 | — | — |
| 42 | MTWORO_LEAD | INTEGER | 2 | — | — |
| 43 | MTWORO_LONGTIME | NUMERIC | 8 | 7 | — |
| 44 | MTWORO_MACHNO | STRING | 4 | — | — |
| 45 | MTWORO_MD_PR_HR | STRING | 1 | — | — |
| 46 | MTWORO_MIN_CHG | NUMERIC | 8 | 2 | — |
| 47 | MTWORO_MISCACST | NUMERIC | 8 | 2 | — |
| 48 | MTWORO_MISCCOST | NUMERIC | 8 | 2 | — |
| 49 | MTWORO_MISCDESC | STRING | 30 | — | — |
| 50 | MTWORO_NEGOVLP | NUMERIC | 8 | 2 | — |
| 51 | MTWORO_NUM | INTEGER | 2 | — | — |
| 52 | MTWORO_NUM_PERS | NUMERIC | 8 | 2 | — |
| 53 | MTWORO_NUM_PROC | INTEGER | 2 | — | — |
| 54 | MTWORO_OP_TEMP^ | INTEGER | 2 | — | — |
| 55 | MTWORO_OPER | INTEGER | 2 | — | — |
| 56 | MTWORO_OPER2 | INTEGER | 2 | — | — |
| 57 | MTWORO_OPERDESC | STRING | 30 | — | — |
| 58 | MTWORO_OVERLAP | INTEGER | 2 | — | — |
| 59 | MTWORO_PARTSHR | NUMERIC | 8 | 2 | — |
| 60 | MTWORO_PIECE_RT | NUMERIC | 8 | 2 | — |
| 61 | MTWORO_PO | NUMERIC | 8 | — | — |
| 62 | MTWORO_PR_PERHR | NUMERIC | 8 | 2 | — |
| 63 | MTWORO_PRINT | STRING | 1 | — | — |
| 64 | MTWORO_PRIORITY | STRING | 1 | — | — |
| 65 | MTWORO_PROJ | NUMERIC | 8 | — | — |
| 66 | MTWORO_QTYCOM | NUMERIC | 8 | 2 | — |
| 67 | MTWORO_SCHED_WC | STRING | 12 | — | — |
| 68 | MTWORO_SCRAPPED | NUMERIC | 8 | 2 | — |
| 69 | MTWORO_SQTY | NUMERIC | 8 | 2 | — |
| 70 | MTWORO_START | DATE | 4 | — | — |
| 71 | MTWORO_STARTED | DATE | 4 | — | — |
| 72 | MTWORO_STD_TIME | STRING | 1 | — | — |
| 73 | MTWORO_STQTY | NUMERIC | 8 | 2 | — |
| 74 | MTWORO_TIME_PPR | TIME | 4 | — | — |
| 75 | MTWORO_TIMEPART | TIME | 4 | — | — |
| 76 | MTWORO_TOOL | STRING | 15 | — | — |
| 77 | MTWORO_TYPE | STRING | 1 | — | — |
| 78 | MTWORO_VEND | STRING | 10 | — | — |
| 79 | MTWORO_VENDNAME | STRING | 30 | — | — |
| 80 | MTWORO_WC | STRING | 12 | — | — |
| 81 | MTWORO_WCDESC | STRING | 30 | — | — |
| 82 | MTWORO_WOPRE | NUMERIC | 8 | — | WO Prefix |
| 83 | MTWORO_WOSUF | INTEGER | 2 | — | WO Suffix |

## WOLABOR
**LABOR TRANSACTIONS**

Fields: 45

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MTWOLA_ASSY | STRING | 15 | — | — |
| 2 | MTWOLA_ASSYDESC | STRING | 30 | — | — |
| 3 | MTWOLA_AUDIT | STRING | 35 | — | — |
| 4 | MTWOLA_COMPLETE | STRING | 1 | — | — |
| 5 | MTWOLA_DATE | DATE | 4 | — | — |
| 6 | MTWOLA_DATE2 | DATE | 4 | — | — |
| 7 | MTWOLA_DEDUCT | TIME | 4 | — | — |
| 8 | MTWOLA_EMP | INTEGER | 2 | — | — |
| 9 | MTWOLA_EMP2 | INTEGER | 2 | — | — |
| 10 | MTWOLA_EXTRA | STRING | 50 | — | — |
| 11 | MTWOLA_FOHCOST | NUMERIC | 8 | 2 | — |
| 12 | MTWOLA_LABCOST | NUMERIC | 8 | 2 | — |
| 13 | MTWOLA_LABRATE | NUMERIC | 8 | 4 | — |
| 14 | MTWOLA_MACH | STRING | 4 | — | — |
| 15 | MTWOLA_MACHCOST | NUMERIC | 8 | 2 | — |
| 16 | MTWOLA_MACHDATE | DATE | 4 | — | — |
| 17 | MTWOLA_MISC | NUMERIC | 8 | 6 | — |
| 18 | MTWOLA_MISCDESC | STRING | 30 | — | — |
| 19 | MTWOLA_NOJOBS | INTEGER | 2 | — | — |
| 20 | MTWOLA_OPER | INTEGER | 2 | — | — |
| 21 | MTWOLA_OTEAM | INTEGER | 2 | — | — |
| 22 | MTWOLA_PARTS | NUMERIC | 8 | 2 | — |
| 23 | MTWOLA_POSTED | STRING | 1 | — | — |
| 24 | MTWOLA_QCCODE | STRING | 2 | — | — |
| 25 | MTWOLA_QCDESC | STRING | 30 | — | — |
| 26 | MTWOLA_REGOVER | STRING | 1 | — | — |
| 27 | MTWOLA_REWORK | STRING | 1 | — | — |
| 28 | MTWOLA_RUNHRS | NUMERIC | 8 | 2 | — |
| 29 | MTWOLA_SCDESC | STRING | 30 | — | — |
| 30 | MTWOLA_SCRAPCD | STRING | 2 | — | — |
| 31 | MTWOLA_SCRAPPED | NUMERIC | 8 | 2 | — |
| 32 | MTWOLA_SETCOST | NUMERIC | 8 | 2 | — |
| 33 | MTWOLA_SETUPHRS | NUMERIC | 8 | 2 | — |
| 34 | MTWOLA_SHIFT | INTEGER | 2 | — | — |
| 35 | MTWOLA_START | TIME | 4 | — | — |
| 36 | MTWOLA_STOP | TIME | 4 | — | — |
| 37 | MTWOLA_TEAM | INTEGER | 2 | — | — |
| 38 | MTWOLA_TOOL | STRING | 15 | — | — |
| 39 | MTWOLA_TOOLDATE | DATE | 4 | — | — |
| 40 | MTWOLA_TRXN | INTEGER | 2 | — | — |
| 41 | MTWOLA_VOHCOST | NUMERIC | 8 | 2 | — |
| 42 | MTWOLA_WC | STRING | 12 | — | — |
| 43 | MTWOLA_WCDATE | DATE | 4 | — | — |
| 44 | MTWOLA_WOPRE | NUMERIC | 8 | — | — |
| 45 | MTWOLA_WOSUF | INTEGER | 2 | — | — |

## WOMAT
**MATERIAL TRANSACTIONS**

Fields: 17

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MTWO_PRODCODE | STRING | 15 | — | — |
| 2 | WOMAT_COST | NUMERIC | 8 | 2 | — |
| 3 | WOMAT_DATE | DATE | 4 | — | — |
| 4 | WOMAT_EXTRA | STRING | 50 | — | — |
| 5 | WOMAT_KIT | STRING | 1 | — | — |
| 6 | WOMAT_LOT | STRING | 15 | — | — |
| 7 | WOMAT_PCODE | STRING | 15 | — | — |
| 8 | WOMAT_PDESC | STRING | 30 | — | — |
| 9 | WOMAT_PRODDESC | STRING | 30 | — | — |
| 10 | WOMAT_QTYISSUED | NUMERIC | 8 | 4 | — |
| 11 | WOMAT_QTYSCRAP | NUMERIC | 8 | 2 | — |
| 12 | WOMAT_REF | STRING | 15 | — | — |
| 13 | WOMAT_SCDESC | STRING | 30 | — | — |
| 14 | WOMAT_SCRAPCD | STRING | 2 | — | — |
| 15 | WOMAT_SERIAL | STRING | 25 | — | — |
| 16 | WOMAT_WOPRE | NUMERIC | 8 | — | — |
| 17 | WOMAT_WOSUF | INTEGER | 2 | — | — |

## WORECV
**WORK ORDER RECEIPTS**

Fields: 11

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MTWOR_ASSY | STRING | 15 | — | — |
| 2 | MTWOR_AVGC | NUMERIC | 8 | 4 | — |
| 3 | MTWOR_DATE | DATE | 4 | — | — |
| 4 | MTWOR_DESC | STRING | 30 | — | — |
| 5 | MTWOR_LOT | STRING | 15 | — | — |
| 6 | MTWOR_QTY | NUMERIC | 8 | 2 | — |
| 7 | MTWOR_REF | STRING | 15 | — | — |
| 8 | MTWOR_SERIAL | STRING | 25 | — | — |
| 9 | MTWOR_USESTD | STRING | 1 | — | — |
| 10 | MTWOR_WOPRE | NUMERIC | 8 | — | — |
| 11 | MTWOR_WOSUF | INTEGER | 2 | — | — |

## WORKACHG
**ARCHIVED WO CHANGES**

Fields: 25

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | WO_CHG_AASD | DATE | 4 | — | — |
| 2 | WO_CHG_ACLASS | STRING | 1 | — | — |
| 3 | WO_CHG_ADDATE | DATE | 4 | — | — |
| 4 | WO_CHG_ADESC | STRING | 30 | — | — |
| 5 | WO_CHG_AEXTRA | STRING | 150 | — | — |
| 6 | WO_CHG_AFDATE | DATE | 4 | — | — |
| 7 | WO_CHG_APRIO | STRING | 1 | — | — |
| 8 | WO_CHG_AQTY | NUMERIC | 8 | 2 | — |
| 9 | WO_CHG_ASDATE | DATE | 4 | — | — |
| 10 | WO_CHG_ASTATUS | STRING | 1 | — | — |
| 11 | WO_CHG_BASD | DATE | 4 | — | — |
| 12 | WO_CHG_BCLASS | STRING | 1 | — | — |
| 13 | WO_CHG_BDDATE | DATE | 4 | — | — |
| 14 | WO_CHG_BDESC | STRING | 30 | — | — |
| 15 | WO_CHG_BEXTRA | STRING | 150 | — | — |
| 16 | WO_CHG_BFDATE | DATE | 4 | — | — |
| 17 | WO_CHG_BPRIO | STRING | 1 | — | — |
| 18 | WO_CHG_BQTY | NUMERIC | 8 | 2 | — |
| 19 | WO_CHG_BSDATE | DATE | 4 | — | — |
| 20 | WO_CHG_BSTATUS | STRING | 1 | — | — |
| 21 | WO_CHG_CDATE | DATE | 4 | — | — |
| 22 | WO_CHG_CODE | STRING | 15 | — | — |
| 23 | WO_CHG_USER | STRING | 15 | — | — |
| 24 | WO_CHG_WOPRE | NUMERIC | 8 | — | — |
| 25 | WO_CHG_WOSUF | INTEGER | 2 | — | — |

## WORKCHG
**WO CHANGES**

Fields: 25

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | WO_CHG_AASD | DATE | 4 | — | — |
| 2 | WO_CHG_ACLASS | STRING | 1 | — | — |
| 3 | WO_CHG_ADDATE | DATE | 4 | — | — |
| 4 | WO_CHG_ADESC | STRING | 30 | — | — |
| 5 | WO_CHG_AEXTRA | STRING | 150 | — | — |
| 6 | WO_CHG_AFDATE | DATE | 4 | — | — |
| 7 | WO_CHG_APRIO | STRING | 1 | — | — |
| 8 | WO_CHG_AQTY | NUMERIC | 8 | 2 | — |
| 9 | WO_CHG_ASDATE | DATE | 4 | — | — |
| 10 | WO_CHG_ASTATUS | STRING | 1 | — | — |
| 11 | WO_CHG_BASD | DATE | 4 | — | — |
| 12 | WO_CHG_BCLASS | STRING | 1 | — | — |
| 13 | WO_CHG_BDDATE | DATE | 4 | — | — |
| 14 | WO_CHG_BDESC | STRING | 30 | — | — |
| 15 | WO_CHG_BEXTRA | STRING | 150 | — | — |
| 16 | WO_CHG_BFDATE | DATE | 4 | — | — |
| 17 | WO_CHG_BPRIO | STRING | 1 | — | — |
| 18 | WO_CHG_BQTY | NUMERIC | 8 | 2 | — |
| 19 | WO_CHG_BSDATE | DATE | 4 | — | — |
| 20 | WO_CHG_BSTATUS | STRING | 1 | — | — |
| 21 | WO_CHG_CDATE | DATE | 4 | — | — |
| 22 | WO_CHG_CODE | STRING | 15 | — | — |
| 23 | WO_CHG_USER | STRING | 15 | — | — |
| 24 | WO_CHG_WOPRE | NUMERIC | 8 | — | — |
| 25 | WO_CHG_WOSUF | INTEGER | 2 | — | — |

## WORKCTR
**WORK CENTERS**

Fields: 25

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MTWC_^UTIL | NUMERIC | 8 | 2 | — |
| 2 | MTWC_AVGQTIME | INTEGER | 2 | — | — |
| 3 | MTWC_COST_LB | NUMERIC | 8 | 6 | — |
| 4 | MTWC_DEPT | STRING | 4 | — | — |
| 5 | MTWC_DEPTDESC | STRING | 30 | — | — |
| 6 | MTWC_EST_VOVHD | NUMERIC | 8 | 4 | — |
| 7 | MTWC_EXTRA | STRING | 100 | — | — |
| 8 | MTWC_FOVHD | NUMERIC | 8 | 4 | — |
| 9 | MTWC_HRS_SHIFT | INTEGER | 2 | — | — |
| 10 | MTWC_HRSWEEK | INTEGER | 2 | — | — |
| 11 | MTWC_LABOR | NUMERIC | 8 | 4 | — |
| 12 | MTWC_LEAD | INTEGER | 2 | — | — |
| 13 | MTWC_LEVEL_YN | STRING | 1 | — | — |
| 14 | MTWC_MACHINE | NUMERIC | 8 | 4 | — |
| 15 | MTWC_MIN_CHG | NUMERIC | 8 | 2 | — |
| 16 | MTWC_OUTPROC | STRING | 1 | — | — |
| 17 | MTWC_PARENT_WC | STRING | 12 | — | — |
| 18 | MTWC_PARENT_YN | STRING | 1 | — | — |
| 19 | MTWC_QPR1 | INTEGER | 2 | — | — |
| 20 | MTWC_QPR2 | INTEGER | 2 | — | — |
| 21 | MTWC_QPR3 | INTEGER | 2 | — | — |
| 22 | MTWC_SETUP | NUMERIC | 8 | 4 | — |
| 23 | MTWC_VOVHD | NUMERIC | 8 | 4 | — |
| 24 | MTWC_WC | STRING | 12 | — | — |
| 25 | MTWC_WCDESC | STRING | 30 | — | — |

## WORKHORD
**WORK ORDER HEADER - ARCHIVE**

Fields: 82

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MTWO_CUSTCODE | STRING | 10 | — | Customer Code |
| 2 | MTWO_CUSTNAME | STRING | 25 | — | Customer Name |
| 3 | MTWO_WIP_AEXTRA | NUMERIC | 8 | 2 | — |
| 4 | MTWO_WIP_AFIN | DATE | 4 | — | Actual Finish Date |
| 5 | MTWO_WIP_AFOVHD | NUMERIC | 8 | 2 | — |
| 6 | MTWO_WIP_ALABOR | NUMERIC | 8 | 2 | Actual Labor Cost |
| 7 | MTWO_WIP_AMAT | NUMERIC | 8 | 2 | Actual Material Cost |
| 8 | MTWO_WIP_AMISC | NUMERIC | 8 | 2 | — |
| 9 | MTWO_WIP_AOTH | NUMERIC | 8 | 2 | — |
| 10 | MTWO_WIP_AOUTPR | NUMERIC | 8 | 2 | Actual Outside Process Cost |
| 11 | MTWO_WIP_ASETUP | NUMERIC | 8 | 2 | Actual Setup Cost |
| 12 | MTWO_WIP_ASTART | DATE | 4 | — | Acual Start Date |
| 13 | MTWO_WIP_ATOTAL | NUMERIC | 8 | 2 | Actaul Total Cost |
| 14 | MTWO_WIP_AVOVHD | NUMERIC | 8 | 2 | — |
| 15 | MTWO_WIP_BLANK | STRING | 1 | — | — |
| 16 | MTWO_WIP_CHGORD | INTEGER | 2 | — | — |
| 17 | MTWO_WIP_CODE | STRING | 15 | — | — |
| 18 | MTWO_WIP_COMQTY | NUMERIC | 8 | 2 | — |
| 19 | MTWO_WIP_CONTAT | STRING | 25 | — | — |
| 20 | MTWO_WIP_CUSORD | STRING | 25 | — | — |
| 21 | MTWO_WIP_DDATE | DATE | 4 | — | — |
| 22 | MTWO_WIP_DESC | STRING | 30 | — | — |
| 23 | MTWO_WIP_EEXTRA | NUMERIC | 8 | 2 | — |
| 24 | MTWO_WIP_EFOVHD | NUMERIC | 8 | 2 | — |
| 25 | MTWO_WIP_ELABOR | NUMERIC | 8 | 2 | Est. Labor Cost |
| 26 | MTWO_WIP_EMAT | NUMERIC | 8 | 2 | Est. Material Cost |
| 27 | MTWO_WIP_EMISC | NUMERIC | 8 | 2 | — |
| 28 | MTWO_WIP_EOTH | NUMERIC | 8 | 2 | — |
| 29 | MTWO_WIP_EOUTPR | NUMERIC | 8 | 2 | Est. Outside Process Cost |
| 30 | MTWO_WIP_ESETUP | NUMERIC | 8 | 2 | Est. Setup Cost |
| 31 | MTWO_WIP_EST | NUMERIC | 8 | — | — |
| 32 | MTWO_WIP_ETOT | NUMERIC | 8 | 2 | Est. Toatal Cost |
| 33 | MTWO_WIP_EXTRA^ | NUMERIC | 8 | 2 | — |
| 34 | MTWO_WIP_EXTRAV | NUMERIC | 8 | 2 | — |
| 35 | MTWO_WIP_FOVHD^ | NUMERIC | 8 | 2 | — |
| 36 | MTWO_WIP_FOVHDV | NUMERIC | 8 | 2 | — |
| 37 | MTWO_WIP_INSTR_1 | STRING | 60 | — | — |
| 38 | MTWO_WIP_INSTR_10 | STRING | 60 | — | — |
| 39 | MTWO_WIP_INSTR_2 | STRING | 60 | — | — |
| 40 | MTWO_WIP_INSTR_3 | STRING | 60 | — | — |
| 41 | MTWO_WIP_INSTR_4 | STRING | 60 | — | — |
| 42 | MTWO_WIP_INSTR_5 | STRING | 60 | — | — |
| 43 | MTWO_WIP_INSTR_6 | STRING | 60 | — | — |
| 44 | MTWO_WIP_INSTR_7 | STRING | 60 | — | — |
| 45 | MTWO_WIP_INSTR_8 | STRING | 60 | — | — |
| 46 | MTWO_WIP_INSTR_9 | STRING | 60 | — | — |
| 47 | MTWO_WIP_LABOR^ | NUMERIC | 8 | 2 | — |
| 48 | MTWO_WIP_LABORV | NUMERIC | 8 | 2 | — |
| 49 | MTWO_WIP_LOC | STRING | 10 | — | — |
| 50 | MTWO_WIP_LOCK | STRING | 1 | — | — |
| 51 | MTWO_WIP_MAT^ | NUMERIC | 8 | 2 | — |
| 52 | MTWO_WIP_MATV | NUMERIC | 8 | 2 | — |
| 53 | MTWO_WIP_MISC^ | NUMERIC | 8 | 2 | — |
| 54 | MTWO_WIP_MISCV | NUMERIC | 8 | 2 | — |
| 55 | MTWO_WIP_MULT | STRING | 1 | — | — |
| 56 | MTWO_WIP_OTHPER | NUMERIC | 8 | 2 | — |
| 57 | MTWO_WIP_OTHV | NUMERIC | 8 | 2 | — |
| 58 | MTWO_WIP_OUTPR^ | NUMERIC | 8 | 2 | — |
| 59 | MTWO_WIP_OUTPRV | NUMERIC | 8 | 2 | — |
| 60 | MTWO_WIP_PPRCE | NUMERIC | 8 | 4 | — |
| 61 | MTWO_WIP_PROJ | STRING | 15 | — | — |
| 62 | MTWO_WIP_PRTY | STRING | 1 | — | Priority |
| 63 | MTWO_WIP_QCONV | STRING | 1 | — | — |
| 64 | MTWO_WIP_SCHED_1 | STRING | 1 | — | — |
| 65 | MTWO_WIP_SCHED_2 | STRING | 1 | — | — |
| 66 | MTWO_WIP_SCONV | STRING | 1 | — | — |
| 67 | MTWO_WIP_SETUP^ | NUMERIC | 8 | 2 | — |
| 68 | MTWO_WIP_SETUPV | NUMERIC | 8 | 2 | — |
| 69 | MTWO_WIP_SFIN | DATE | 4 | — | Scheduled Finish Date |
| 70 | MTWO_WIP_SOLINE | NUMERIC | 8 | — | — |
| 71 | MTWO_WIP_SONUM | NUMERIC | 8 | — | SO Number |
| 72 | MTWO_WIP_SQTY | NUMERIC | 8 | 2 | Start Quantity |
| 73 | MTWO_WIP_SSTART | DATE | 4 | — | Scheduled Start Date |
| 74 | MTWO_WIP_STATUS | STRING | 1 | — | Status |
| 75 | MTWO_WIP_TOT^ | NUMERIC | 8 | 2 | — |
| 76 | MTWO_WIP_TOTV | NUMERIC | 8 | 2 | — |
| 77 | MTWO_WIP_USERCD | STRING | 1 | — | — |
| 78 | MTWO_WIP_VOVHD | NUMERIC | 8 | 2 | — |
| 79 | MTWO_WIP_VOVHD^ | NUMERIC | 8 | 2 | — |
| 80 | MTWO_WIP_VOVHDV | NUMERIC | 8 | 2 | — |
| 81 | MTWO_WIP_WOPRE | NUMERIC | 8 | — | WO Prefix |
| 82 | MTWO_WIP_WOSUF | INTEGER | 2 | — | WO Suffix |

## WORKORD
**WORK ORDER HEADER**

Fields: 82

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MTWO_CUSTCODE | STRING | 10 | — | Customer Code |
| 2 | MTWO_CUSTNAME | STRING | 25 | — | Customer Name |
| 3 | MTWO_WIP_AEXTRA | NUMERIC | 8 | 2 | — |
| 4 | MTWO_WIP_AFIN | DATE | 4 | — | Actual Finish Date |
| 5 | MTWO_WIP_AFOVHD | NUMERIC | 8 | 2 | — |
| 6 | MTWO_WIP_ALABOR | NUMERIC | 8 | 2 | Actual Labor Cost |
| 7 | MTWO_WIP_AMAT | NUMERIC | 8 | 2 | Actual Material Cost |
| 8 | MTWO_WIP_AMISC | NUMERIC | 8 | 2 | — |
| 9 | MTWO_WIP_AOTH | NUMERIC | 8 | 2 | — |
| 10 | MTWO_WIP_AOUTPR | NUMERIC | 8 | 2 | Actual Outside Process Cost |
| 11 | MTWO_WIP_ASETUP | NUMERIC | 8 | 2 | Actual Setup Cost |
| 12 | MTWO_WIP_ASTART | DATE | 4 | — | Acual Start Date |
| 13 | MTWO_WIP_ATOTAL | NUMERIC | 8 | 2 | Actaul Total Cost |
| 14 | MTWO_WIP_AVOVHD | NUMERIC | 8 | 2 | — |
| 15 | MTWO_WIP_BLANK | STRING | 1 | — | — |
| 16 | MTWO_WIP_CHGORD | INTEGER | 2 | — | — |
| 17 | MTWO_WIP_CODE | STRING | 15 | — | — |
| 18 | MTWO_WIP_COMQTY | NUMERIC | 8 | 2 | — |
| 19 | MTWO_WIP_CONTAT | STRING | 25 | — | — |
| 20 | MTWO_WIP_CUSORD | STRING | 25 | — | — |
| 21 | MTWO_WIP_DDATE | DATE | 4 | — | — |
| 22 | MTWO_WIP_DESC | STRING | 30 | — | — |
| 23 | MTWO_WIP_EEXTRA | NUMERIC | 8 | 2 | — |
| 24 | MTWO_WIP_EFOVHD | NUMERIC | 8 | 2 | — |
| 25 | MTWO_WIP_ELABOR | NUMERIC | 8 | 2 | Est. Labor Cost |
| 26 | MTWO_WIP_EMAT | NUMERIC | 8 | 2 | Est. Material Cost |
| 27 | MTWO_WIP_EMISC | NUMERIC | 8 | 2 | — |
| 28 | MTWO_WIP_EOTH | NUMERIC | 8 | 2 | — |
| 29 | MTWO_WIP_EOUTPR | NUMERIC | 8 | 2 | Est. Outside Process Cost |
| 30 | MTWO_WIP_ESETUP | NUMERIC | 8 | 2 | Est. Setup Cost |
| 31 | MTWO_WIP_EST | NUMERIC | 8 | — | — |
| 32 | MTWO_WIP_ETOT | NUMERIC | 8 | 2 | Est. Toatal Cost |
| 33 | MTWO_WIP_EXTRA^ | NUMERIC | 8 | 2 | — |
| 34 | MTWO_WIP_EXTRAV | NUMERIC | 8 | 2 | — |
| 35 | MTWO_WIP_FOVHD^ | NUMERIC | 8 | 2 | — |
| 36 | MTWO_WIP_FOVHDV | NUMERIC | 8 | 2 | — |
| 37 | MTWO_WIP_INSTR_1 | STRING | 60 | — | — |
| 38 | MTWO_WIP_INSTR_10 | STRING | 60 | — | — |
| 39 | MTWO_WIP_INSTR_2 | STRING | 60 | — | — |
| 40 | MTWO_WIP_INSTR_3 | STRING | 60 | — | — |
| 41 | MTWO_WIP_INSTR_4 | STRING | 60 | — | — |
| 42 | MTWO_WIP_INSTR_5 | STRING | 60 | — | — |
| 43 | MTWO_WIP_INSTR_6 | STRING | 60 | — | — |
| 44 | MTWO_WIP_INSTR_7 | STRING | 60 | — | — |
| 45 | MTWO_WIP_INSTR_8 | STRING | 60 | — | — |
| 46 | MTWO_WIP_INSTR_9 | STRING | 60 | — | — |
| 47 | MTWO_WIP_LABOR^ | NUMERIC | 8 | 2 | — |
| 48 | MTWO_WIP_LABORV | NUMERIC | 8 | 2 | — |
| 49 | MTWO_WIP_LOC | STRING | 10 | — | — |
| 50 | MTWO_WIP_LOCK | STRING | 1 | — | — |
| 51 | MTWO_WIP_MAT^ | NUMERIC | 8 | 2 | — |
| 52 | MTWO_WIP_MATV | NUMERIC | 8 | 2 | — |
| 53 | MTWO_WIP_MISC^ | NUMERIC | 8 | 2 | — |
| 54 | MTWO_WIP_MISCV | NUMERIC | 8 | 2 | — |
| 55 | MTWO_WIP_MULT | STRING | 1 | — | — |
| 56 | MTWO_WIP_OTHPER | NUMERIC | 8 | 2 | — |
| 57 | MTWO_WIP_OTHV | NUMERIC | 8 | 2 | — |
| 58 | MTWO_WIP_OUTPR^ | NUMERIC | 8 | 2 | — |
| 59 | MTWO_WIP_OUTPRV | NUMERIC | 8 | 2 | — |
| 60 | MTWO_WIP_PPRCE | NUMERIC | 8 | 4 | — |
| 61 | MTWO_WIP_PROJ | STRING | 15 | — | — |
| 62 | MTWO_WIP_PRTY | STRING | 1 | — | Priority |
| 63 | MTWO_WIP_QCONV | STRING | 1 | — | — |
| 64 | MTWO_WIP_SCHED_1 | STRING | 1 | — | — |
| 65 | MTWO_WIP_SCHED_2 | STRING | 1 | — | — |
| 66 | MTWO_WIP_SCONV | STRING | 1 | — | — |
| 67 | MTWO_WIP_SETUP^ | NUMERIC | 8 | 2 | — |
| 68 | MTWO_WIP_SETUPV | NUMERIC | 8 | 2 | — |
| 69 | MTWO_WIP_SFIN | DATE | 4 | — | Scheduled Finish Date |
| 70 | MTWO_WIP_SOLINE | NUMERIC | 8 | — | — |
| 71 | MTWO_WIP_SONUM | NUMERIC | 8 | — | SO Number |
| 72 | MTWO_WIP_SQTY | NUMERIC | 8 | 2 | Start Quantity |
| 73 | MTWO_WIP_SSTART | DATE | 4 | — | Scheduled Start Date |
| 74 | MTWO_WIP_STATUS | STRING | 1 | — | Status |
| 75 | MTWO_WIP_TOT^ | NUMERIC | 8 | 2 | — |
| 76 | MTWO_WIP_TOTV | NUMERIC | 8 | 2 | — |
| 77 | MTWO_WIP_USERCD | STRING | 1 | — | — |
| 78 | MTWO_WIP_VOVHD | NUMERIC | 8 | 2 | — |
| 79 | MTWO_WIP_VOVHD^ | NUMERIC | 8 | 2 | — |
| 80 | MTWO_WIP_VOVHDV | NUMERIC | 8 | 2 | — |
| 81 | MTWO_WIP_WOPRE | NUMERIC | 8 | — | WO Prefix |
| 82 | MTWO_WIP_WOSUF | INTEGER | 2 | — | WO Suffix |

## WOROCHG
**WO ROUTING CHANGES**

Fields: 24

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | WORO_CHG_AEXTRA | STRING | 100 | — | — |
| 2 | WORO_CHG_ALONG | NUMERIC | 8 | 7 | — |
| 3 | WORO_CHG_AMACH | STRING | 4 | — | — |
| 4 | WORO_CHG_ANUMP | NUMERIC | 8 | 2 | — |
| 5 | WORO_CHG_AOPER | STRING | 1 | — | — |
| 6 | WORO_CHG_ASETUP | TIME | 4 | — | — |
| 7 | WORO_CHG_ASTDT | STRING | 1 | — | — |
| 8 | WORO_CHG_ATOOL | STRING | 15 | — | — |
| 9 | WORO_CHG_AWC | STRING | 12 | — | — |
| 10 | WORO_CHG_BEXTRA | STRING | 100 | — | — |
| 11 | WORO_CHG_BLONG | NUMERIC | 8 | 7 | — |
| 12 | WORO_CHG_BMATCH | STRING | 4 | — | — |
| 13 | WORO_CHG_BNUMP | NUMERIC | 8 | 2 | — |
| 14 | WORO_CHG_BSETUP | TIME | 4 | — | — |
| 15 | WORO_CHG_BSTDT | STRING | 1 | — | — |
| 16 | WORO_CHG_BTOOL | STRING | 15 | — | — |
| 17 | WORO_CHG_BWC | STRING | 12 | — | — |
| 18 | WORO_CHG_CDATE | DATE | 4 | — | — |
| 19 | WORO_CHG_DOPER | STRING | 1 | — | — |
| 20 | WORO_CHG_OPER | INTEGER | 2 | — | — |
| 21 | WORO_CHG_PART | STRING | 15 | — | — |
| 22 | WORO_CHG_USER | STRING | 15 | — | — |
| 23 | WORO_CHG_WOPRE | NUMERIC | 8 | — | — |
| 24 | WORO_CHG_WOSUF | INTEGER | 2 | — | — |

## WOROUT
**WORK ORDER ROUTING**

Fields: 83

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MTWORO_^COMP | INTEGER | 2 | — | — |
| 2 | MTWORO_ACTHRS | NUMERIC | 8 | 4 | — |
| 3 | MTWORO_AFOHCST | NUMERIC | 8 | 4 | — |
| 4 | MTWORO_ALABCST | NUMERIC | 8 | 4 | — |
| 5 | MTWORO_AMCHCST | NUMERIC | 8 | 4 | — |
| 6 | MTWORO_AOUTCST | NUMERIC | 8 | 4 | — |
| 7 | MTWORO_ASETCST | NUMERIC | 8 | 4 | — |
| 8 | MTWORO_ASETHRS | NUMERIC | 8 | 4 | — |
| 9 | MTWORO_AVOHCST | NUMERIC | 8 | 4 | — |
| 10 | MTWORO_CODE | STRING | 15 | — | — |
| 11 | MTWORO_CONTNTN | NUMERIC | 8 | — | — |
| 12 | MTWORO_DEPT | STRING | 3 | — | — |
| 13 | MTWORO_DESC | STRING | 30 | — | — |
| 14 | MTWORO_EFOHCST | NUMERIC | 8 | 4 | — |
| 15 | MTWORO_ELABCST | NUMERIC | 8 | 4 | — |
| 16 | MTWORO_EMCHCST | NUMERIC | 8 | 4 | — |
| 17 | MTWORO_EOUTCST | NUMERIC | 8 | 4 | — |
| 18 | MTWORO_ESETCST | NUMERIC | 8 | 4 | — |
| 19 | MTWORO_ESETHRS | NUMERIC | 8 | 4 | — |
| 20 | MTWORO_ESSTHRS | TIME | 4 | — | — |
| 21 | MTWORO_ESTHRS | NUMERIC | 8 | 4 | — |
| 22 | MTWORO_EVOHCST | NUMERIC | 8 | 4 | — |
| 23 | MTWORO_EXTRA | STRING | 150 | — | — |
| 24 | MTWORO_FINISH | DATE | 4 | — | — |
| 25 | MTWORO_FINISH2 | DATE | 4 | — | — |
| 26 | MTWORO_FINISHED | DATE | 4 | — | — |
| 27 | MTWORO_INSTR_1 | STRING | 60 | — | — |
| 28 | MTWORO_INSTR_10 | STRING | 60 | — | — |
| 29 | MTWORO_INSTR_11 | STRING | 60 | — | — |
| 30 | MTWORO_INSTR_12 | STRING | 60 | — | — |
| 31 | MTWORO_INSTR_13 | STRING | 60 | — | — |
| 32 | MTWORO_INSTR_14 | STRING | 60 | — | — |
| 33 | MTWORO_INSTR_15 | STRING | 60 | — | — |
| 34 | MTWORO_INSTR_2 | STRING | 60 | — | — |
| 35 | MTWORO_INSTR_3 | STRING | 60 | — | — |
| 36 | MTWORO_INSTR_4 | STRING | 60 | — | — |
| 37 | MTWORO_INSTR_5 | STRING | 60 | — | — |
| 38 | MTWORO_INSTR_6 | STRING | 60 | — | — |
| 39 | MTWORO_INSTR_7 | STRING | 60 | — | — |
| 40 | MTWORO_INSTR_8 | STRING | 60 | — | — |
| 41 | MTWORO_INSTR_9 | STRING | 60 | — | — |
| 42 | MTWORO_LEAD | INTEGER | 2 | — | — |
| 43 | MTWORO_LONGTIME | NUMERIC | 8 | 7 | — |
| 44 | MTWORO_MACHNO | STRING | 4 | — | — |
| 45 | MTWORO_MD_PR_HR | STRING | 1 | — | — |
| 46 | MTWORO_MIN_CHG | NUMERIC | 8 | 2 | — |
| 47 | MTWORO_MISCACST | NUMERIC | 8 | 2 | — |
| 48 | MTWORO_MISCCOST | NUMERIC | 8 | 2 | — |
| 49 | MTWORO_MISCDESC | STRING | 30 | — | — |
| 50 | MTWORO_NEGOVLP | NUMERIC | 8 | 2 | — |
| 51 | MTWORO_NUM | INTEGER | 2 | — | — |
| 52 | MTWORO_NUM_PERS | NUMERIC | 8 | 2 | — |
| 53 | MTWORO_NUM_PROC | INTEGER | 2 | — | — |
| 54 | MTWORO_OP_TEMP^ | INTEGER | 2 | — | — |
| 55 | MTWORO_OPER | INTEGER | 2 | — | — |
| 56 | MTWORO_OPER2 | INTEGER | 2 | — | — |
| 57 | MTWORO_OPERDESC | STRING | 30 | — | — |
| 58 | MTWORO_OVERLAP | INTEGER | 2 | — | — |
| 59 | MTWORO_PARTSHR | NUMERIC | 8 | 2 | — |
| 60 | MTWORO_PIECE_RT | NUMERIC | 8 | 2 | — |
| 61 | MTWORO_PO | NUMERIC | 8 | — | — |
| 62 | MTWORO_PR_PERHR | NUMERIC | 8 | 2 | — |
| 63 | MTWORO_PRINT | STRING | 1 | — | — |
| 64 | MTWORO_PRIORITY | STRING | 1 | — | — |
| 65 | MTWORO_PROJ | NUMERIC | 8 | — | — |
| 66 | MTWORO_QTYCOM | NUMERIC | 8 | 2 | — |
| 67 | MTWORO_SCHED_WC | STRING | 12 | — | — |
| 68 | MTWORO_SCRAPPED | NUMERIC | 8 | 2 | — |
| 69 | MTWORO_SQTY | NUMERIC | 8 | 2 | — |
| 70 | MTWORO_START | DATE | 4 | — | — |
| 71 | MTWORO_STARTED | DATE | 4 | — | — |
| 72 | MTWORO_STD_TIME | STRING | 1 | — | — |
| 73 | MTWORO_STQTY | NUMERIC | 8 | 2 | — |
| 74 | MTWORO_TIME_PPR | TIME | 4 | — | — |
| 75 | MTWORO_TIMEPART | TIME | 4 | — | — |
| 76 | MTWORO_TOOL | STRING | 15 | — | — |
| 77 | MTWORO_TYPE | STRING | 1 | — | — |
| 78 | MTWORO_VEND | STRING | 10 | — | — |
| 79 | MTWORO_VENDNAME | STRING | 30 | — | — |
| 80 | MTWORO_WC | STRING | 12 | — | — |
| 81 | MTWORO_WCDESC | STRING | 30 | — | — |
| 82 | MTWORO_WOPRE | NUMERIC | 8 | — | WO Prefix |
| 83 | MTWORO_WOSUF | INTEGER | 2 | — | WO Suffix |

## WOROUTMP
**AGGREGATE WO ROUTINGS (Temporary)**

Fields: 83

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MTWORO_^COMP | INTEGER | 2 | — | — |
| 2 | MTWORO_ACTHRS | NUMERIC | 8 | 4 | — |
| 3 | MTWORO_AFOHCST | NUMERIC | 8 | 4 | — |
| 4 | MTWORO_ALABCST | NUMERIC | 8 | 4 | — |
| 5 | MTWORO_AMCHCST | NUMERIC | 8 | 4 | — |
| 6 | MTWORO_AOUTCST | NUMERIC | 8 | 4 | — |
| 7 | MTWORO_ASETCST | NUMERIC | 8 | 4 | — |
| 8 | MTWORO_ASETHRS | NUMERIC | 8 | 4 | — |
| 9 | MTWORO_AVOHCST | NUMERIC | 8 | 4 | — |
| 10 | MTWORO_CODE | STRING | 15 | — | — |
| 11 | MTWORO_CONTNTN | NUMERIC | 8 | — | — |
| 12 | MTWORO_DEPT | STRING | 3 | — | — |
| 13 | MTWORO_DESC | STRING | 30 | — | — |
| 14 | MTWORO_EFOHCST | NUMERIC | 8 | 4 | — |
| 15 | MTWORO_ELABCST | NUMERIC | 8 | 4 | — |
| 16 | MTWORO_EMCHCST | NUMERIC | 8 | 4 | — |
| 17 | MTWORO_EOUTCST | NUMERIC | 8 | 4 | — |
| 18 | MTWORO_ESETCST | NUMERIC | 8 | 4 | — |
| 19 | MTWORO_ESETHRS | NUMERIC | 8 | 4 | — |
| 20 | MTWORO_ESSTHRS | TIME | 4 | — | — |
| 21 | MTWORO_ESTHRS | NUMERIC | 8 | 4 | — |
| 22 | MTWORO_EVOHCST | NUMERIC | 8 | 4 | — |
| 23 | MTWORO_EXTRA | STRING | 150 | — | — |
| 24 | MTWORO_FINISH | DATE | 4 | — | — |
| 25 | MTWORO_FINISH2 | DATE | 4 | — | — |
| 26 | MTWORO_FINISHED | DATE | 4 | — | — |
| 27 | MTWORO_INSTR_1 | STRING | 60 | — | — |
| 28 | MTWORO_INSTR_10 | STRING | 60 | — | — |
| 29 | MTWORO_INSTR_11 | STRING | 60 | — | — |
| 30 | MTWORO_INSTR_12 | STRING | 60 | — | — |
| 31 | MTWORO_INSTR_13 | STRING | 60 | — | — |
| 32 | MTWORO_INSTR_14 | STRING | 60 | — | — |
| 33 | MTWORO_INSTR_15 | STRING | 60 | — | — |
| 34 | MTWORO_INSTR_2 | STRING | 60 | — | — |
| 35 | MTWORO_INSTR_3 | STRING | 60 | — | — |
| 36 | MTWORO_INSTR_4 | STRING | 60 | — | — |
| 37 | MTWORO_INSTR_5 | STRING | 60 | — | — |
| 38 | MTWORO_INSTR_6 | STRING | 60 | — | — |
| 39 | MTWORO_INSTR_7 | STRING | 60 | — | — |
| 40 | MTWORO_INSTR_8 | STRING | 60 | — | — |
| 41 | MTWORO_INSTR_9 | STRING | 60 | — | — |
| 42 | MTWORO_LEAD | INTEGER | 2 | — | — |
| 43 | MTWORO_LONGTIME | NUMERIC | 8 | 7 | — |
| 44 | MTWORO_MACHNO | STRING | 4 | — | — |
| 45 | MTWORO_MD_PR_HR | STRING | 1 | — | — |
| 46 | MTWORO_MIN_CHG | NUMERIC | 8 | 2 | — |
| 47 | MTWORO_MISCACST | NUMERIC | 8 | 2 | — |
| 48 | MTWORO_MISCCOST | NUMERIC | 8 | 2 | — |
| 49 | MTWORO_MISCDESC | STRING | 30 | — | — |
| 50 | MTWORO_NEGOVLP | NUMERIC | 8 | 2 | — |
| 51 | MTWORO_NUM | INTEGER | 2 | — | — |
| 52 | MTWORO_NUM_PERS | NUMERIC | 8 | 2 | — |
| 53 | MTWORO_NUM_PROC | INTEGER | 2 | — | — |
| 54 | MTWORO_OP_TEMP^ | INTEGER | 2 | — | — |
| 55 | MTWORO_OPER | INTEGER | 2 | — | — |
| 56 | MTWORO_OPER2 | INTEGER | 2 | — | — |
| 57 | MTWORO_OPERDESC | STRING | 30 | — | — |
| 58 | MTWORO_OVERLAP | INTEGER | 2 | — | — |
| 59 | MTWORO_PARTSHR | NUMERIC | 8 | 2 | — |
| 60 | MTWORO_PIECE_RT | NUMERIC | 8 | 2 | — |
| 61 | MTWORO_PO | NUMERIC | 8 | — | — |
| 62 | MTWORO_PR_PERHR | NUMERIC | 8 | 2 | — |
| 63 | MTWORO_PRINT | STRING | 1 | — | — |
| 64 | MTWORO_PRIORITY | STRING | 1 | — | — |
| 65 | MTWORO_PROJ | NUMERIC | 8 | — | — |
| 66 | MTWORO_QTYCOM | NUMERIC | 8 | 2 | — |
| 67 | MTWORO_SCHED_WC | STRING | 12 | — | — |
| 68 | MTWORO_SCRAPPED | NUMERIC | 8 | 2 | — |
| 69 | MTWORO_SQTY | NUMERIC | 8 | 2 | — |
| 70 | MTWORO_START | DATE | 4 | — | — |
| 71 | MTWORO_STARTED | DATE | 4 | — | — |
| 72 | MTWORO_STD_TIME | STRING | 1 | — | — |
| 73 | MTWORO_STQTY | NUMERIC | 8 | 2 | — |
| 74 | MTWORO_TIME_PPR | TIME | 4 | — | — |
| 75 | MTWORO_TIMEPART | TIME | 4 | — | — |
| 76 | MTWORO_TOOL | STRING | 15 | — | — |
| 77 | MTWORO_TYPE | STRING | 1 | — | — |
| 78 | MTWORO_VEND | STRING | 10 | — | — |
| 79 | MTWORO_VENDNAME | STRING | 30 | — | — |
| 80 | MTWORO_WC | STRING | 12 | — | — |
| 81 | MTWORO_WCDESC | STRING | 30 | — | — |
| 82 | MTWORO_WOPRE | NUMERIC | 8 | — | WO Prefix |
| 83 | MTWORO_WOSUF | INTEGER | 2 | — | WO Suffix |
