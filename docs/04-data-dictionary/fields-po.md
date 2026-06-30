# PO — Purchase Orders: Field Reference

Status: verified-schema

Source: `Evo-DBA_File_Fields 052421.xlsx`, sheet "Fields".
Field descriptions where provided by source; otherwise name-inferred.

---

## BKAPAPO
**ARCHIVED PO HEADER**

Fields: 58

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKAP_PO_CONFIRM_1 | STRING | 1 | — | — |
| 2 | BKAP_PO_CONFIRM_2 | STRING | 1 | — | — |
| 3 | BKAP_PO_DESC | STRING | 30 | — | PO Description |
| 4 | BKAP_PO_EMPNUM | INTEGER | 2 | — | — |
| 5 | BKAP_PO_ENDLNE | STRING | 1 | — | Ending Lines Y/N |
| 6 | BKAP_PO_ENTBY | STRING | 2 | — | PO Entered By |
| 7 | BKAP_PO_EXTRA | STRING | 150 | — | Extra |
| 8 | BKAP_PO_FOB | STRING | 20 | — | Ship FOB |
| 9 | BKAP_PO_FTERMD | STRING | 10 | — | Freight Terms Description |
| 10 | BKAP_PO_FTERMNM | INTEGER | 2 | — | Freight Terms Number |
| 11 | BKAP_PO_GLDPT | STRING | 4 | — | GL Department |
| 12 | BKAP_PO_INVNUM | STRING | 10 | — | not used |
| 13 | BKAP_PO_ISBROKE | STRING | 10 | — | Broker Code |
| 14 | BKAP_PO_ISCUR | STRING | 3 | — | Currency |
| 15 | BKAP_PO_ISMCDT | DATE | 4 | — | Multi-Currency Date |
| 16 | BKAP_PO_ISREV | STRING | 1 | — | Rev - only called in POB |
| 17 | BKAP_PO_ISRVDT | DATE | 4 | — | Rev Date - only called in POB |
| 18 | BKAP_PO_ISTXGR | STRING | 10 | — | Tax Group |
| 19 | BKAP_PO_ITOTAL | NUMERIC | 8 | 2 | Invoiced Total |
| 20 | BKAP_PO_LOC | STRING | 10 | — | Location |
| 21 | BKAP_PO_LONGPO | STRING | 25 | — | not used |
| 22 | BKAP_PO_NL | INTEGER | 2 | — | Number of Lines |
| 23 | BKAP_PO_NUM | NUMERIC | 8 | — | PO Number |
| 24 | BKAP_PO_OBYCUS | STRING | 15 | — | Job Number |
| 25 | BKAP_PO_ORDDTE | DATE | 4 | — | Order Date |
| 26 | BKAP_PO_PCKSLP | STRING | 15 | — | — |
| 27 | BKAP_PO_PRTD | STRING | 1 | — | Printed   Y/P/R |
| 28 | BKAP_PO_QCTOTAL | NUMERIC | 8 | 2 | QC Total |
| 29 | BKAP_PO_RECNUM | NUMERIC | 8 | — | not used |
| 30 | BKAP_PO_RNI^ | NUMERIC | 8 | 2 | — |
| 31 | BKAP_PO_SHPA1 | STRING | 30 | — | Ship Loc Address Line 1 |
| 32 | BKAP_PO_SHPA2 | STRING | 30 | — | Ship Loc Address Line 2 |
| 33 | BKAP_PO_SHPA3 | STRING | 30 | — | Ship Loc. Address Line 3 |
| 34 | BKAP_PO_SHPATN | STRING | 30 | — | Ship Attention |
| 35 | BKAP_PO_SHPCNT | STRING | 30 | — | Ship Country |
| 36 | BKAP_PO_SHPCOD | STRING | 10 | — | Ship To Loc Code |
| 37 | BKAP_PO_SHPCTY | STRING | 26 | — | Ship Loc City |
| 38 | BKAP_PO_SHPNME | STRING | 30 | — | Ship Loc Name |
| 39 | BKAP_PO_SHPST | STRING | 2 | — | Ship loc State |
| 40 | BKAP_PO_SHPVIA | STRING | 15 | — | Ship VIA |
| 41 | BKAP_PO_SHPZIP | STRING | 10 | — | Ship Loc ZIP Code |
| 42 | BKAP_PO_SUBTOT | NUMERIC | 8 | 2 | Sub Total |
| 43 | BKAP_PO_TAXABLE | STRING | 1 | — | Taxable Y/N |
| 44 | BKAP_PO_TAXAMT | NUMERIC | 8 | 2 | Tax Amount |
| 45 | BKAP_PO_TAXRTE | NUMERIC | 8 | 3 | Tax Rate |
| 46 | BKAP_PO_TERMD | STRING | 10 | — | Terms Description |
| 47 | BKAP_PO_TERMNM | INTEGER | 2 | — | Terms Number |
| 48 | BKAP_PO_TOTAL | NUMERIC | 8 | 2 | Total |
| 49 | BKAP_PO_VNDA1 | STRING | 30 | — | Vendor Address Line 1 |
| 50 | BKAP_PO_VNDA2 | STRING | 30 | — | Vendor Address Line 2 |
| 51 | BKAP_PO_VNDA3 | STRING | 30 | — | Vendor Address 3 |
| 52 | BKAP_PO_VNDATN | STRING | 30 | — | Vendor Attention |
| 53 | BKAP_PO_VNDCNT | STRING | 30 | — | Vvendor Country |
| 54 | BKAP_PO_VNDCOD | STRING | 10 | — | Vendor Code |
| 55 | BKAP_PO_VNDCTY | STRING | 26 | — | Vemdor City |
| 56 | BKAP_PO_VNDNME | STRING | 30 | — | Vendor Name |
| 57 | BKAP_PO_VNDST | STRING | 2 | — | Vendor State |
| 58 | BKAP_PO_VNDZIP | STRING | 10 | — | Vendor ZIP Code |

## BKAPAPOL
**ARCHIVED PO LINES**

Fields: 38

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKAP_POL_ARD | DATE | 4 | — | Actaul Receipt Date |
| 2 | BKAP_POL_BUYOFF | NUMERIC | 8 | 2 | Quantity Buy-Off  From QC |
| 3 | BKAP_POL_CNTR | INTEGER | 2 | — | Line Number |
| 4 | BKAP_POL_ERD | DATE | 4 | — | Estimatred Receipt Date |
| 5 | BKAP_POL_EST | NUMERIC | 8 | — | Estimated Receipt Date |
| 6 | BKAP_POL_EXTRA | STRING | 100 | — | Extra |
| 7 | BKAP_POL_GLA | STRING | 10 | — | GL Account Number |
| 8 | BKAP_POL_GLDPTA | STRING | 4 | — | GL Department |
| 9 | BKAP_POL_INVDTE | DATE | 4 | — | — |
| 10 | BKAP_POL_INVNUM | STRING | 10 | — | not used |
| 11 | BKAP_POL_IQTY | NUMERIC | 8 | 2 | Invoiced Quantity |
| 12 | BKAP_POL_ITM_NO | STRING | 9 | — | Item Number |
| 13 | BKAP_POL_ITYPE | STRING | 1 | — | not used |
| 14 | BKAP_POL_LOC | STRING | 10 | — | Location |
| 15 | BKAP_POL_OO_QTY | NUMERIC | 8 | 2 | Quantity On Order (remaining) |
| 16 | BKAP_POL_OPER | INTEGER | 2 | — | WO Operation number |
| 17 | BKAP_POL_PARENT | STRING | 15 | — | called from POA, POB |
| 18 | BKAP_POL_PCODE | STRING | 15 | — | Part Code |
| 19 | BKAP_POL_PCOGS | NUMERIC | 8 | 2 | COGS |
| 20 | BKAP_POL_PCONV | NUMERIC | 8 | 5 | — |
| 21 | BKAP_POL_PDESC | STRING | 30 | — | Description |
| 22 | BKAP_POL_PDISC | NUMERIC | 8 | 2 | Discount |
| 23 | BKAP_POL_PEXT | NUMERIC | 8 | 2 | Extended  Total |
| 24 | BKAP_POL_PKSQTY | NUMERIC | 8 | 2 | — |
| 25 | BKAP_POL_PONM | NUMERIC | 8 | — | PO Number |
| 26 | BKAP_POL_PPRCE | NUMERIC | 8 | 4 | Price |
| 27 | BKAP_POL_PQTY | NUMERIC | 8 | 2 | Quantity Ordered |
| 28 | BKAP_POL_PRTDIM | STRING | 1 | — | called from POA, POB |
| 29 | BKAP_POL_PSTDTE | DATE | 4 | — | — |
| 30 | BKAP_POL_QC_QTY | NUMERIC | 8 | 2 | QC Quantity |
| 31 | BKAP_POL_RECNUM | NUMERIC | 8 | — | not used |
| 32 | BKAP_POL_RQTY | NUMERIC | 8 | 2 | Recevied Quantity |
| 33 | BKAP_POL_SCRAP | NUMERIC | 8 | 2 | Quantity Scraped |
| 34 | BKAP_POL_TXBLE | STRING | 1 | — | Taxable Y/N |
| 35 | BKAP_POL_WOPRE | NUMERIC | 8 | — | Work Order Prefix |
| 36 | BKAP_POL_WOSUF | INTEGER | 2 | — | Work Order Suffix |
| 37 | NKAP_POL_UM_LIN_1 | STRING | 3 | — | — |
| 38 | NKAP_POL_UM_LIN_2 | STRING | 3 | — | — |

## BKAPHDSC
**PO RECEIVER NOTES**

Fields: 5

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BK_DESC_CODE | STRING | 15 | — | not used |
| 2 | BK_DESC_DESC | STRING | 25 | — | not used |
| 3 | BK_DESC_LINE | INTEGER | 2 | — | Notes line number |
| 4 | BK_DESC_NOTES | STRING | 70 | — | Notes - text |
| 5 | BK_DESC_NUM | NUMERIC | 8 | — | PO Number |

## BKAPHPO
**PO RECEIVER HEADER**

Fields: 58

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKAP_PO_CONFIRM_1 | STRING | 1 | — | — |
| 2 | BKAP_PO_CONFIRM_2 | STRING | 1 | — | — |
| 3 | BKAP_PO_DESC | STRING | 30 | — | PO Description |
| 4 | BKAP_PO_EMPNUM | INTEGER | 2 | — | — |
| 5 | BKAP_PO_ENDLNE | STRING | 1 | — | Ending Lines Y/N |
| 6 | BKAP_PO_ENTBY | STRING | 2 | — | PO Entered By |
| 7 | BKAP_PO_EXTRA | STRING | 150 | — | Extra |
| 8 | BKAP_PO_FOB | STRING | 20 | — | Ship FOB |
| 9 | BKAP_PO_FTERMD | STRING | 10 | — | Freight Terms Description |
| 10 | BKAP_PO_FTERMNM | INTEGER | 2 | — | Freight Terms Number |
| 11 | BKAP_PO_GLDPT | STRING | 4 | — | GL Department |
| 12 | BKAP_PO_INVNUM | STRING | 10 | — | not used |
| 13 | BKAP_PO_ISBROKE | STRING | 10 | — | Broker Code |
| 14 | BKAP_PO_ISCUR | STRING | 3 | — | Currency |
| 15 | BKAP_PO_ISMCDT | DATE | 4 | — | Multi-Currency Date |
| 16 | BKAP_PO_ISREV | STRING | 1 | — | Rev - only called in POB |
| 17 | BKAP_PO_ISRVDT | DATE | 4 | — | Rev Date - only called in POB |
| 18 | BKAP_PO_ISTXGR | STRING | 10 | — | Tax Group |
| 19 | BKAP_PO_ITOTAL | NUMERIC | 8 | 2 | Invoiced Total |
| 20 | BKAP_PO_LOC | STRING | 10 | — | Location |
| 21 | BKAP_PO_LONGPO | STRING | 25 | — | not used |
| 22 | BKAP_PO_NL | INTEGER | 2 | — | Number of Lines |
| 23 | BKAP_PO_NUM | NUMERIC | 8 | — | PO Number |
| 24 | BKAP_PO_OBYCUS | STRING | 15 | — | Job Number |
| 25 | BKAP_PO_ORDDTE | DATE | 4 | — | Order Date |
| 26 | BKAP_PO_PCKSLP | STRING | 15 | — | — |
| 27 | BKAP_PO_PRTD | STRING | 1 | — | Printed   Y/P/R |
| 28 | BKAP_PO_QCTOTAL | NUMERIC | 8 | 2 | QC Total |
| 29 | BKAP_PO_RECNUM | NUMERIC | 8 | — | not used |
| 30 | BKAP_PO_RNI^ | NUMERIC | 8 | 2 | — |
| 31 | BKAP_PO_SHPA1 | STRING | 30 | — | Ship Loc Address Line 1 |
| 32 | BKAP_PO_SHPA2 | STRING | 30 | — | Ship Loc Address Line 2 |
| 33 | BKAP_PO_SHPA3 | STRING | 30 | — | Ship Loc. Address Line 3 |
| 34 | BKAP_PO_SHPATN | STRING | 30 | — | Ship Attention |
| 35 | BKAP_PO_SHPCNT | STRING | 30 | — | Ship Country |
| 36 | BKAP_PO_SHPCOD | STRING | 10 | — | Ship To Loc Code |
| 37 | BKAP_PO_SHPCTY | STRING | 26 | — | Ship Loc City |
| 38 | BKAP_PO_SHPNME | STRING | 30 | — | Ship Loc Name |
| 39 | BKAP_PO_SHPST | STRING | 2 | — | Ship loc State |
| 40 | BKAP_PO_SHPVIA | STRING | 15 | — | Ship VIA |
| 41 | BKAP_PO_SHPZIP | STRING | 10 | — | Ship Loc ZIP Code |
| 42 | BKAP_PO_SUBTOT | NUMERIC | 8 | 2 | Sub Total |
| 43 | BKAP_PO_TAXABLE | STRING | 1 | — | Taxable Y/N |
| 44 | BKAP_PO_TAXAMT | NUMERIC | 8 | 2 | Tax Amount |
| 45 | BKAP_PO_TAXRTE | NUMERIC | 8 | 3 | Tax Rate |
| 46 | BKAP_PO_TERMD | STRING | 10 | — | Terms Description |
| 47 | BKAP_PO_TERMNM | INTEGER | 2 | — | Terms Number |
| 48 | BKAP_PO_TOTAL | NUMERIC | 8 | 2 | Total |
| 49 | BKAP_PO_VNDA1 | STRING | 30 | — | Vendor Address Line 1 |
| 50 | BKAP_PO_VNDA2 | STRING | 30 | — | Vendor Address Line 2 |
| 51 | BKAP_PO_VNDA3 | STRING | 30 | — | Vendor Address 3 |
| 52 | BKAP_PO_VNDATN | STRING | 30 | — | Vendor Attention |
| 53 | BKAP_PO_VNDCNT | STRING | 30 | — | Vvendor Country |
| 54 | BKAP_PO_VNDCOD | STRING | 10 | — | Vendor Code |
| 55 | BKAP_PO_VNDCTY | STRING | 26 | — | Vemdor City |
| 56 | BKAP_PO_VNDNME | STRING | 30 | — | Vendor Name |
| 57 | BKAP_PO_VNDST | STRING | 2 | — | Vendor State |
| 58 | BKAP_PO_VNDZIP | STRING | 10 | — | Vendor ZIP Code |

## BKAPHPOL
**PO RECEIVER LINES**

Fields: 38

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKAP_POL_ARD | DATE | 4 | — | Actaul Receipt Date |
| 2 | BKAP_POL_BUYOFF | NUMERIC | 8 | 2 | Quantity Buy-Off  From QC |
| 3 | BKAP_POL_CNTR | INTEGER | 2 | — | Line Number |
| 4 | BKAP_POL_ERD | DATE | 4 | — | Estimatred Receipt Date |
| 5 | BKAP_POL_EST | NUMERIC | 8 | — | Estimated Receipt Date |
| 6 | BKAP_POL_EXTRA | STRING | 100 | — | Extra |
| 7 | BKAP_POL_GLA | STRING | 10 | — | GL Account Number |
| 8 | BKAP_POL_GLDPTA | STRING | 4 | — | GL Department |
| 9 | BKAP_POL_INVDTE | DATE | 4 | — | — |
| 10 | BKAP_POL_INVNUM | STRING | 10 | — | not used |
| 11 | BKAP_POL_IQTY | NUMERIC | 8 | 2 | Invoiced Quantity |
| 12 | BKAP_POL_ITM_NO | STRING | 9 | — | Item Number |
| 13 | BKAP_POL_ITYPE | STRING | 1 | — | not used |
| 14 | BKAP_POL_LOC | STRING | 10 | — | Location |
| 15 | BKAP_POL_OO_QTY | NUMERIC | 8 | 2 | Quantity On Order (remaining) |
| 16 | BKAP_POL_OPER | INTEGER | 2 | — | WO Operation number |
| 17 | BKAP_POL_PARENT | STRING | 15 | — | called from POA, POB |
| 18 | BKAP_POL_PCODE | STRING | 15 | — | Part Code |
| 19 | BKAP_POL_PCOGS | NUMERIC | 8 | 2 | COGS |
| 20 | BKAP_POL_PCONV | NUMERIC | 8 | 5 | — |
| 21 | BKAP_POL_PDESC | STRING | 30 | — | Description |
| 22 | BKAP_POL_PDISC | NUMERIC | 8 | 2 | Discount |
| 23 | BKAP_POL_PEXT | NUMERIC | 8 | 2 | Extended  Total |
| 24 | BKAP_POL_PKSQTY | NUMERIC | 8 | 2 | — |
| 25 | BKAP_POL_PONM | NUMERIC | 8 | — | PO Number |
| 26 | BKAP_POL_PPRCE | NUMERIC | 8 | 4 | Price |
| 27 | BKAP_POL_PQTY | NUMERIC | 8 | 2 | Quantity Ordered |
| 28 | BKAP_POL_PRTDIM | STRING | 1 | — | called from POA, POB |
| 29 | BKAP_POL_PSTDTE | DATE | 4 | — | — |
| 30 | BKAP_POL_QC_QTY | NUMERIC | 8 | 2 | QC Quantity |
| 31 | BKAP_POL_RECNUM | NUMERIC | 8 | — | not used |
| 32 | BKAP_POL_RQTY | NUMERIC | 8 | 2 | Recevied Quantity |
| 33 | BKAP_POL_SCRAP | NUMERIC | 8 | 2 | Quantity Scraped |
| 34 | BKAP_POL_TXBLE | STRING | 1 | — | Taxable Y/N |
| 35 | BKAP_POL_WOPRE | NUMERIC | 8 | — | Work Order Prefix |
| 36 | BKAP_POL_WOSUF | INTEGER | 2 | — | Work Order Suffix |
| 37 | NKAP_POL_UM_LIN_1 | STRING | 3 | — | — |
| 38 | NKAP_POL_UM_LIN_2 | STRING | 3 | — | — |

## BKAPPO
**OPEN PO HEADER**

Fields: 58

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKAP_PO_CONFIRM_1 | STRING | 1 | — | — |
| 2 | BKAP_PO_CONFIRM_2 | STRING | 1 | — | — |
| 3 | BKAP_PO_DESC | STRING | 30 | — | PO Description |
| 4 | BKAP_PO_EMPNUM | INTEGER | 2 | — | — |
| 5 | BKAP_PO_ENDLNE | STRING | 1 | — | Ending Lines Y/N |
| 6 | BKAP_PO_ENTBY | STRING | 2 | — | PO Entered By |
| 7 | BKAP_PO_EXTRA | STRING | 150 | — | Extra |
| 8 | BKAP_PO_FOB | STRING | 20 | — | Ship FOB |
| 9 | BKAP_PO_FTERMD | STRING | 10 | — | Freight Terms Description |
| 10 | BKAP_PO_FTERMNM | INTEGER | 2 | — | Freight Terms Number |
| 11 | BKAP_PO_GLDPT | STRING | 4 | — | GL Department |
| 12 | BKAP_PO_INVNUM | STRING | 10 | — | not used |
| 13 | BKAP_PO_ISBROKE | STRING | 10 | — | Broker Code |
| 14 | BKAP_PO_ISCUR | STRING | 3 | — | Currency |
| 15 | BKAP_PO_ISMCDT | DATE | 4 | — | Multi-Currency Date |
| 16 | BKAP_PO_ISREV | STRING | 1 | — | Rev - only called in POB |
| 17 | BKAP_PO_ISRVDT | DATE | 4 | — | Rev Date - only called in POB |
| 18 | BKAP_PO_ISTXGR | STRING | 10 | — | Tax Group |
| 19 | BKAP_PO_ITOTAL | NUMERIC | 8 | 2 | Invoiced Total |
| 20 | BKAP_PO_LOC | STRING | 10 | — | Location |
| 21 | BKAP_PO_LONGPO | STRING | 25 | — | not used |
| 22 | BKAP_PO_NL | INTEGER | 2 | — | Number of Lines |
| 23 | BKAP_PO_NUM | NUMERIC | 8 | — | PO Number |
| 24 | BKAP_PO_OBYCUS | STRING | 15 | — | Job Number |
| 25 | BKAP_PO_ORDDTE | DATE | 4 | — | Order Date |
| 26 | BKAP_PO_PCKSLP | STRING | 15 | — | — |
| 27 | BKAP_PO_PRTD | STRING | 1 | — | Printed   Y/P/R |
| 28 | BKAP_PO_QCTOTAL | NUMERIC | 8 | 2 | QC Total |
| 29 | BKAP_PO_RECNUM | NUMERIC | 8 | — | not used |
| 30 | BKAP_PO_RNI^ | NUMERIC | 8 | 2 | — |
| 31 | BKAP_PO_SHPA1 | STRING | 30 | — | Ship Loc Address Line 1 |
| 32 | BKAP_PO_SHPA2 | STRING | 30 | — | Ship Loc Address Line 2 |
| 33 | BKAP_PO_SHPA3 | STRING | 30 | — | Ship Loc. Address Line 3 |
| 34 | BKAP_PO_SHPATN | STRING | 30 | — | Ship Attention |
| 35 | BKAP_PO_SHPCNT | STRING | 30 | — | Ship Country |
| 36 | BKAP_PO_SHPCOD | STRING | 10 | — | Ship To Loc Code |
| 37 | BKAP_PO_SHPCTY | STRING | 26 | — | Ship Loc City |
| 38 | BKAP_PO_SHPNME | STRING | 30 | — | Ship Loc Name |
| 39 | BKAP_PO_SHPST | STRING | 2 | — | Ship loc State |
| 40 | BKAP_PO_SHPVIA | STRING | 15 | — | Ship VIA |
| 41 | BKAP_PO_SHPZIP | STRING | 10 | — | Ship Loc ZIP Code |
| 42 | BKAP_PO_SUBTOT | NUMERIC | 8 | 2 | Sub Total |
| 43 | BKAP_PO_TAXABLE | STRING | 1 | — | Taxable Y/N |
| 44 | BKAP_PO_TAXAMT | NUMERIC | 8 | 2 | Tax Amount |
| 45 | BKAP_PO_TAXRTE | NUMERIC | 8 | 3 | Tax Rate |
| 46 | BKAP_PO_TERMD | STRING | 10 | — | Terms Description |
| 47 | BKAP_PO_TERMNM | INTEGER | 2 | — | Terms Number |
| 48 | BKAP_PO_TOTAL | NUMERIC | 8 | 2 | Total |
| 49 | BKAP_PO_VNDA1 | STRING | 30 | — | Vendor Address Line 1 |
| 50 | BKAP_PO_VNDA2 | STRING | 30 | — | Vendor Address Line 2 |
| 51 | BKAP_PO_VNDA3 | STRING | 30 | — | Vendor Address 3 |
| 52 | BKAP_PO_VNDATN | STRING | 30 | — | Vendor Attention |
| 53 | BKAP_PO_VNDCNT | STRING | 30 | — | Vvendor Country |
| 54 | BKAP_PO_VNDCOD | STRING | 10 | — | Vendor Code |
| 55 | BKAP_PO_VNDCTY | STRING | 26 | — | Vemdor City |
| 56 | BKAP_PO_VNDNME | STRING | 30 | — | Vendor Name |
| 57 | BKAP_PO_VNDST | STRING | 2 | — | Vendor State |
| 58 | BKAP_PO_VNDZIP | STRING | 10 | — | Vendor ZIP Code |

## BKAPPOL
**OPEN PO LINES**

Fields: 38

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKAP_POL_ARD | DATE | 4 | — | Actaul Receipt Date |
| 2 | BKAP_POL_BUYOFF | NUMERIC | 8 | 2 | Quantity Buy-Off  From QC |
| 3 | BKAP_POL_CNTR | INTEGER | 2 | — | Line Number |
| 4 | BKAP_POL_ERD | DATE | 4 | — | Estimatred Receipt Date |
| 5 | BKAP_POL_EST | NUMERIC | 8 | — | Estimated Receipt Date |
| 6 | BKAP_POL_EXTRA | STRING | 100 | — | Extra |
| 7 | BKAP_POL_GLA | STRING | 10 | — | GL Account Number |
| 8 | BKAP_POL_GLDPTA | STRING | 4 | — | GL Department |
| 9 | BKAP_POL_INVDTE | DATE | 4 | — | — |
| 10 | BKAP_POL_INVNUM | STRING | 10 | — | not used |
| 11 | BKAP_POL_IQTY | NUMERIC | 8 | 2 | Invoiced Quantity |
| 12 | BKAP_POL_ITM_NO | STRING | 9 | — | Item Number |
| 13 | BKAP_POL_ITYPE | STRING | 1 | — | not used |
| 14 | BKAP_POL_LOC | STRING | 10 | — | Location |
| 15 | BKAP_POL_OO_QTY | NUMERIC | 8 | 2 | Quantity On Order (remaining) |
| 16 | BKAP_POL_OPER | INTEGER | 2 | — | WO Operation number |
| 17 | BKAP_POL_PARENT | STRING | 15 | — | called from POA, POB |
| 18 | BKAP_POL_PCODE | STRING | 15 | — | Part Code |
| 19 | BKAP_POL_PCOGS | NUMERIC | 8 | 2 | COGS |
| 20 | BKAP_POL_PCONV | NUMERIC | 8 | 5 | — |
| 21 | BKAP_POL_PDESC | STRING | 30 | — | Description |
| 22 | BKAP_POL_PDISC | NUMERIC | 8 | 2 | Discount |
| 23 | BKAP_POL_PEXT | NUMERIC | 8 | 2 | Extended  Total |
| 24 | BKAP_POL_PKSQTY | NUMERIC | 8 | 2 | — |
| 25 | BKAP_POL_PONM | NUMERIC | 8 | — | PO Number |
| 26 | BKAP_POL_PPRCE | NUMERIC | 8 | 4 | Price |
| 27 | BKAP_POL_PQTY | NUMERIC | 8 | 2 | Quantity Ordered |
| 28 | BKAP_POL_PRTDIM | STRING | 1 | — | called from POA, POB |
| 29 | BKAP_POL_PSTDTE | DATE | 4 | — | — |
| 30 | BKAP_POL_QC_QTY | NUMERIC | 8 | 2 | QC Quantity |
| 31 | BKAP_POL_RECNUM | NUMERIC | 8 | — | not used |
| 32 | BKAP_POL_RQTY | NUMERIC | 8 | 2 | Recevied Quantity |
| 33 | BKAP_POL_SCRAP | NUMERIC | 8 | 2 | Quantity Scraped |
| 34 | BKAP_POL_TXBLE | STRING | 1 | — | Taxable Y/N |
| 35 | BKAP_POL_WOPRE | NUMERIC | 8 | — | Work Order Prefix |
| 36 | BKAP_POL_WOSUF | INTEGER | 2 | — | Work Order Suffix |
| 37 | NKAP_POL_UM_LIN_1 | STRING | 3 | — | — |
| 38 | NKAP_POL_UM_LIN_2 | STRING | 3 | — | — |

## BKAPQUOT
**VENDOR PRICING**

Fields: 49

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKRFQ_ALPHA1 | STRING | 15 | — | — |
| 2 | BKRFQ_COST_1 | NUMERIC | 8 | 4 | — |
| 3 | BKRFQ_COST_10 | NUMERIC | 8 | 4 | — |
| 4 | BKRFQ_COST_2 | NUMERIC | 8 | 4 | — |
| 5 | BKRFQ_COST_3 | NUMERIC | 8 | 4 | — |
| 6 | BKRFQ_COST_4 | NUMERIC | 8 | 4 | — |
| 7 | BKRFQ_COST_5 | NUMERIC | 8 | 4 | — |
| 8 | BKRFQ_COST_6 | NUMERIC | 8 | 4 | — |
| 9 | BKRFQ_COST_7 | NUMERIC | 8 | 4 | — |
| 10 | BKRFQ_COST_8 | NUMERIC | 8 | 4 | — |
| 11 | BKRFQ_COST_9 | NUMERIC | 8 | 4 | — |
| 12 | BKRFQ_CQCHANGE | STRING | 1 | — | — |
| 13 | BKRFQ_CWHO | STRING | 15 | — | — |
| 14 | BKRFQ_EST | NUMERIC | 8 | — | Estimate Number |
| 15 | BKRFQ_EST_LINE | NUMERIC | 8 | — | — |
| 16 | BKRFQ_EXP | DATE | 4 | — | Expiration Date |
| 17 | BKRFQ_EXTRA | STRING | 50 | — | Extra |
| 18 | BKRFQ_FLAG | STRING | 1 | — | — |
| 19 | BKRFQ_GDATE | DATE | 4 | — | — |
| 20 | BKRFQ_ISSUE | DATE | 4 | — | Issue Date |
| 21 | BKRFQ_LCDATE | DATE | 4 | — | — |
| 22 | BKRFQ_LEAD | INTEGER | 2 | — | Lead Time |
| 23 | BKRFQ_MAXDAYS | INTEGER | 2 | — | — |
| 24 | BKRFQ_MIN | NUMERIC | 8 | 2 | Minimum |
| 25 | BKRFQ_MINCST | NUMERIC | 8 | 2 | Minimum Cost |
| 26 | BKRFQ_NUM | NUMERIC | 8 | — | Quote/RFQ Number |
| 27 | BKRFQ_OPER | INTEGER | 2 | — | WO Operation Number |
| 28 | BKRFQ_PARENT | STRING | 15 | — | Parent part Number |
| 29 | BKRFQ_PARNTDESC | STRING | 30 | — | Parent Part Description |
| 30 | BKRFQ_PCONV | NUMERIC | 8 | 4 | — |
| 31 | BKRFQ_PROD | STRING | 15 | — | Part Code |
| 32 | BKRFQ_PRODDESC | STRING | 30 | — | Part Description |
| 33 | BKRFQ_PUM | STRING | 3 | — | Unit of Measure |
| 34 | BKRFQ_QTY_1 | NUMERIC | 8 | 2 | — |
| 35 | BKRFQ_QTY_10 | NUMERIC | 8 | 2 | — |
| 36 | BKRFQ_QTY_2 | NUMERIC | 8 | 2 | — |
| 37 | BKRFQ_QTY_3 | NUMERIC | 8 | 2 | — |
| 38 | BKRFQ_QTY_4 | NUMERIC | 8 | 2 | — |
| 39 | BKRFQ_QTY_5 | NUMERIC | 8 | 2 | — |
| 40 | BKRFQ_QTY_6 | NUMERIC | 8 | 2 | — |
| 41 | BKRFQ_QTY_7 | NUMERIC | 8 | 2 | — |
| 42 | BKRFQ_QTY_8 | NUMERIC | 8 | 2 | — |
| 43 | BKRFQ_QTY_9 | NUMERIC | 8 | 2 | — |
| 44 | BKRFQ_USE | STRING | 1 | — | — |
| 45 | BKRFQ_UWHO | STRING | 15 | — | — |
| 46 | BKRFQ_VEND | STRING | 10 | — | Vendor Code |
| 47 | BKRFQ_VENDNAME | STRING | 25 | — | Vendor Name |
| 48 | BKRFQ_WOPRE | NUMERIC | 8 | — | WO Prefix |
| 49 | BKRFQ_WOSUF | INTEGER | 2 | — | WO Suffix |

## BKAPRFQ
**RFQ HEADER**

Fields: 58

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKAP_PO_CONFIRM_1 | STRING | 1 | — | — |
| 2 | BKAP_PO_CONFIRM_2 | STRING | 1 | — | — |
| 3 | BKAP_PO_DESC | STRING | 30 | — | PO Description |
| 4 | BKAP_PO_EMPNUM | INTEGER | 2 | — | — |
| 5 | BKAP_PO_ENDLNE | STRING | 1 | — | Ending Lines Y/N |
| 6 | BKAP_PO_ENTBY | STRING | 2 | — | PO Entered By |
| 7 | BKAP_PO_EXTRA | STRING | 150 | — | Extra |
| 8 | BKAP_PO_FOB | STRING | 20 | — | Ship FOB |
| 9 | BKAP_PO_FTERMD | STRING | 10 | — | Freight Terms Description |
| 10 | BKAP_PO_FTERMNM | INTEGER | 2 | — | Freight Terms Number |
| 11 | BKAP_PO_GLDPT | STRING | 4 | — | GL Department |
| 12 | BKAP_PO_INVNUM | STRING | 10 | — | not used |
| 13 | BKAP_PO_ISBROKE | STRING | 10 | — | Broker Code |
| 14 | BKAP_PO_ISCUR | STRING | 3 | — | Currency |
| 15 | BKAP_PO_ISMCDT | DATE | 4 | — | Multi-Currency Date |
| 16 | BKAP_PO_ISREV | STRING | 1 | — | Rev - only called in POB |
| 17 | BKAP_PO_ISRVDT | DATE | 4 | — | Rev Date - only called in POB |
| 18 | BKAP_PO_ISTXGR | STRING | 10 | — | Tax Group |
| 19 | BKAP_PO_ITOTAL | NUMERIC | 8 | 2 | Invoiced Total |
| 20 | BKAP_PO_LOC | STRING | 10 | — | Location |
| 21 | BKAP_PO_LONGPO | STRING | 25 | — | not used |
| 22 | BKAP_PO_NL | INTEGER | 2 | — | Number of Lines |
| 23 | BKAP_PO_NUM | NUMERIC | 8 | — | PO Number |
| 24 | BKAP_PO_OBYCUS | STRING | 15 | — | Job Number |
| 25 | BKAP_PO_ORDDTE | DATE | 4 | — | Order Date |
| 26 | BKAP_PO_PCKSLP | STRING | 15 | — | — |
| 27 | BKAP_PO_PRTD | STRING | 1 | — | Printed   Y/P/R |
| 28 | BKAP_PO_QCTOTAL | NUMERIC | 8 | 2 | QC Total |
| 29 | BKAP_PO_RECNUM | NUMERIC | 8 | — | not used |
| 30 | BKAP_PO_RNI^ | NUMERIC | 8 | 2 | — |
| 31 | BKAP_PO_SHPA1 | STRING | 30 | — | Ship Loc Address Line 1 |
| 32 | BKAP_PO_SHPA2 | STRING | 30 | — | Ship Loc Address Line 2 |
| 33 | BKAP_PO_SHPA3 | STRING | 30 | — | Ship Loc. Address Line 3 |
| 34 | BKAP_PO_SHPATN | STRING | 30 | — | Ship Attention |
| 35 | BKAP_PO_SHPCNT | STRING | 30 | — | Ship Country |
| 36 | BKAP_PO_SHPCOD | STRING | 10 | — | Ship To Loc Code |
| 37 | BKAP_PO_SHPCTY | STRING | 26 | — | Ship Loc City |
| 38 | BKAP_PO_SHPNME | STRING | 30 | — | Ship Loc Name |
| 39 | BKAP_PO_SHPST | STRING | 2 | — | Ship loc State |
| 40 | BKAP_PO_SHPVIA | STRING | 15 | — | Ship VIA |
| 41 | BKAP_PO_SHPZIP | STRING | 10 | — | Ship Loc ZIP Code |
| 42 | BKAP_PO_SUBTOT | NUMERIC | 8 | 2 | Sub Total |
| 43 | BKAP_PO_TAXABLE | STRING | 1 | — | Taxable Y/N |
| 44 | BKAP_PO_TAXAMT | NUMERIC | 8 | 2 | Tax Amount |
| 45 | BKAP_PO_TAXRTE | NUMERIC | 8 | 3 | Tax Rate |
| 46 | BKAP_PO_TERMD | STRING | 10 | — | Terms Description |
| 47 | BKAP_PO_TERMNM | INTEGER | 2 | — | Terms Number |
| 48 | BKAP_PO_TOTAL | NUMERIC | 8 | 2 | Total |
| 49 | BKAP_PO_VNDA1 | STRING | 30 | — | Vendor Address Line 1 |
| 50 | BKAP_PO_VNDA2 | STRING | 30 | — | Vendor Address Line 2 |
| 51 | BKAP_PO_VNDA3 | STRING | 30 | — | Vendor Address 3 |
| 52 | BKAP_PO_VNDATN | STRING | 30 | — | Vendor Attention |
| 53 | BKAP_PO_VNDCNT | STRING | 30 | — | Vvendor Country |
| 54 | BKAP_PO_VNDCOD | STRING | 10 | — | Vendor Code |
| 55 | BKAP_PO_VNDCTY | STRING | 26 | — | Vemdor City |
| 56 | BKAP_PO_VNDNME | STRING | 30 | — | Vendor Name |
| 57 | BKAP_PO_VNDST | STRING | 2 | — | Vendor State |
| 58 | BKAP_PO_VNDZIP | STRING | 10 | — | Vendor ZIP Code |

## BKAPRFQL
**RFQ LINES**

Fields: 38

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKAP_POL_ARD | DATE | 4 | — | Actaul Receipt Date |
| 2 | BKAP_POL_BUYOFF | NUMERIC | 8 | 2 | Quantity Buy-Off  From QC |
| 3 | BKAP_POL_CNTR | INTEGER | 2 | — | Line Number |
| 4 | BKAP_POL_ERD | DATE | 4 | — | Estimatred Receipt Date |
| 5 | BKAP_POL_EST | NUMERIC | 8 | — | Estimated Receipt Date |
| 6 | BKAP_POL_EXTRA | STRING | 100 | — | Extra |
| 7 | BKAP_POL_GLA | STRING | 10 | — | GL Account Number |
| 8 | BKAP_POL_GLDPTA | STRING | 4 | — | GL Department |
| 9 | BKAP_POL_INVDTE | DATE | 4 | — | — |
| 10 | BKAP_POL_INVNUM | STRING | 10 | — | not used |
| 11 | BKAP_POL_IQTY | NUMERIC | 8 | 2 | Invoiced Quantity |
| 12 | BKAP_POL_ITM_NO | STRING | 9 | — | Item Number |
| 13 | BKAP_POL_ITYPE | STRING | 1 | — | not used |
| 14 | BKAP_POL_LOC | STRING | 10 | — | Location |
| 15 | BKAP_POL_OO_QTY | NUMERIC | 8 | 2 | Quantity On Order (remaining) |
| 16 | BKAP_POL_OPER | INTEGER | 2 | — | WO Operation number |
| 17 | BKAP_POL_PARENT | STRING | 15 | — | called from POA, POB |
| 18 | BKAP_POL_PCODE | STRING | 15 | — | Part Code |
| 19 | BKAP_POL_PCOGS | NUMERIC | 8 | 2 | COGS |
| 20 | BKAP_POL_PCONV | NUMERIC | 8 | 5 | — |
| 21 | BKAP_POL_PDESC | STRING | 30 | — | Description |
| 22 | BKAP_POL_PDISC | NUMERIC | 8 | 2 | Discount |
| 23 | BKAP_POL_PEXT | NUMERIC | 8 | 2 | Extended  Total |
| 24 | BKAP_POL_PKSQTY | NUMERIC | 8 | 2 | — |
| 25 | BKAP_POL_PONM | NUMERIC | 8 | — | PO Number |
| 26 | BKAP_POL_PPRCE | NUMERIC | 8 | 4 | Price |
| 27 | BKAP_POL_PQTY | NUMERIC | 8 | 2 | Quantity Ordered |
| 28 | BKAP_POL_PRTDIM | STRING | 1 | — | called from POA, POB |
| 29 | BKAP_POL_PSTDTE | DATE | 4 | — | — |
| 30 | BKAP_POL_QC_QTY | NUMERIC | 8 | 2 | QC Quantity |
| 31 | BKAP_POL_RECNUM | NUMERIC | 8 | — | not used |
| 32 | BKAP_POL_RQTY | NUMERIC | 8 | 2 | Recevied Quantity |
| 33 | BKAP_POL_SCRAP | NUMERIC | 8 | 2 | Quantity Scraped |
| 34 | BKAP_POL_TXBLE | STRING | 1 | — | Taxable Y/N |
| 35 | BKAP_POL_WOPRE | NUMERIC | 8 | — | Work Order Prefix |
| 36 | BKAP_POL_WOSUF | INTEGER | 2 | — | Work Order Suffix |
| 37 | NKAP_POL_UM_LIN_1 | STRING | 3 | — | — |
| 38 | NKAP_POL_UM_LIN_2 | STRING | 3 | — | — |

## BKPOX
**PO DETAIL  - ACCOUNTING DISABLED**

Fields: 19

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKPOX_ARCHDATE | DATE | 4 | — | — |
| 2 | BKPOX_COMPANY | STRING | 2 | — | — |
| 3 | BKPOX_CURRENCY | STRING | 3 | — | — |
| 4 | BKPOX_ENTDATE | DATE | 4 | — | — |
| 5 | BKPOX_FREIGHT | NUMERIC | 8 | 2 | — |
| 6 | BKPOX_INVCDATE | DATE | 4 | — | — |
| 7 | BKPOX_INVCDESC | STRING | 30 | — | — |
| 8 | BKPOX_INVCNUM | STRING | 10 | — | — |
| 9 | BKPOX_PONUM | NUMERIC | 8 | — | — |
| 10 | BKPOX_POSTDATE | DATE | 4 | — | — |
| 11 | BKPOX_SUBTOT | NUMERIC | 8 | 2 | — |
| 12 | BKPOX_TAXAMT | NUMERIC | 8 | 2 | — |
| 13 | BKPOX_TAXCODE | STRING | 10 | — | — |
| 14 | BKPOX_TAXNAME | STRING | 30 | — | — |
| 15 | BKPOX_TERMSCODE | INTEGER | 2 | — | — |
| 16 | BKPOX_TERMSDESC | STRING | 20 | — | — |
| 17 | BKPOX_TOTAL | NUMERIC | 8 | 2 | — |
| 18 | BKPOX_VENDCODE | STRING | 10 | — | — |
| 19 | BKPOX_VENDNAME | STRING | 30 | — | — |

## BKPOXH
**PO DETAIL  - ACCOUNTING DISABLED**

Fields: 19

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKPOX_ARCHDATE | DATE | 4 | — | — |
| 2 | BKPOX_COMPANY | STRING | 2 | — | — |
| 3 | BKPOX_CURRENCY | STRING | 3 | — | — |
| 4 | BKPOX_ENTDATE | DATE | 4 | — | — |
| 5 | BKPOX_FREIGHT | NUMERIC | 8 | 2 | — |
| 6 | BKPOX_INVCDATE | DATE | 4 | — | — |
| 7 | BKPOX_INVCDESC | STRING | 30 | — | — |
| 8 | BKPOX_INVCNUM | STRING | 10 | — | — |
| 9 | BKPOX_PONUM | NUMERIC | 8 | — | — |
| 10 | BKPOX_POSTDATE | DATE | 4 | — | — |
| 11 | BKPOX_SUBTOT | NUMERIC | 8 | 2 | — |
| 12 | BKPOX_TAXAMT | NUMERIC | 8 | 2 | — |
| 13 | BKPOX_TAXCODE | STRING | 10 | — | — |
| 14 | BKPOX_TAXNAME | STRING | 30 | — | — |
| 15 | BKPOX_TERMSCODE | INTEGER | 2 | — | — |
| 16 | BKPOX_TERMSDESC | STRING | 20 | — | — |
| 17 | BKPOX_TOTAL | NUMERIC | 8 | 2 | — |
| 18 | BKPOX_VENDCODE | STRING | 10 | — | — |
| 19 | BKPOX_VENDNAME | STRING | 30 | — | — |

## BKQCMSTR
**QUALITY CONTROL MASTER**

Fields: 14

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKQC_EXTRA | STRING | 25 | — | — |
| 2 | BKQC_OUT_DATE | DATE | 4 | — | — |
| 3 | BKQC_PKSLIP_NUM | STRING | 15 | — | — |
| 4 | BKQC_PKSLIP_QTY | NUMERIC | 8 | 2 | — |
| 5 | BKQC_PO_NUM | NUMERIC | 8 | — | — |
| 6 | BKQC_POL_ITM_NO | STRING | 10 | — | — |
| 7 | BKQC_PROD_CODE | STRING | 15 | — | — |
| 8 | BKQC_QTY_BUYOFF | NUMERIC | 8 | 2 | — |
| 9 | BKQC_QTY_RECVD | NUMERIC | 8 | 2 | — |
| 10 | BKQC_QTY_REJECT | NUMERIC | 8 | 2 | — |
| 11 | BKQC_RECV_DATE | DATE | 4 | — | — |
| 12 | BKQC_RECVR_NUM | NUMERIC | 8 | — | — |
| 13 | BKQC_UNIT_COST | NUMERIC | 8 | 4 | — |
| 14 | BKQC_VEND_CODE | STRING | 10 | — | — |

## BKQCTRAN
**QUALITY CONTROL TRANSACTION**

Fields: 21

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKQC_TRN_ARDTE | DATE | 4 | — | — |
| 2 | BKQC_TRN_BODTE | DATE | 4 | — | — |
| 3 | BKQC_TRN_BQTY | NUMERIC | 8 | 4 | — |
| 4 | BKQC_TRN_BROKEN | STRING | 1 | — | — |
| 5 | BKQC_TRN_CODE | STRING | 15 | — | — |
| 6 | BKQC_TRN_EMPNUM | INTEGER | 2 | — | — |
| 7 | BKQC_TRN_EXTRA | STRING | 100 | — | — |
| 8 | BKQC_TRN_FAULT | STRING | 1 | — | — |
| 9 | BKQC_TRN_FIXQTY | NUMERIC | 8 | 4 | — |
| 10 | BKQC_TRN_FLAG | STRING | 1 | — | — |
| 11 | BKQC_TRN_GQTY | NUMERIC | 8 | 4 | — |
| 12 | BKQC_TRN_INVCD | STRING | 1 | — | — |
| 13 | BKQC_TRN_PO | NUMERIC | 8 | — | — |
| 14 | BKQC_TRN_PODTE | DATE | 4 | — | — |
| 15 | BKQC_TRN_POQTY | NUMERIC | 8 | 4 | — |
| 16 | BKQC_TRN_RECNUM | NUMERIC | 8 | — | — |
| 17 | BKQC_TRN_RECVNM | NUMERIC | 8 | — | — |
| 18 | BKQC_TRN_REWORK | STRING | 2 | — | — |
| 19 | BKQC_TRN_SCRAP | STRING | 2 | — | — |
| 20 | BKQC_TRN_UQTY | NUMERIC | 8 | 4 | — |
| 21 | BKQC_TRN_VEND | STRING | 10 | — | — |

## BKRFQ
**VERBAL FOR QUOTES**

Fields: 49

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKRFQ_ALPHA1 | STRING | 15 | — | — |
| 2 | BKRFQ_COST_1 | NUMERIC | 8 | 4 | — |
| 3 | BKRFQ_COST_10 | NUMERIC | 8 | 4 | — |
| 4 | BKRFQ_COST_2 | NUMERIC | 8 | 4 | — |
| 5 | BKRFQ_COST_3 | NUMERIC | 8 | 4 | — |
| 6 | BKRFQ_COST_4 | NUMERIC | 8 | 4 | — |
| 7 | BKRFQ_COST_5 | NUMERIC | 8 | 4 | — |
| 8 | BKRFQ_COST_6 | NUMERIC | 8 | 4 | — |
| 9 | BKRFQ_COST_7 | NUMERIC | 8 | 4 | — |
| 10 | BKRFQ_COST_8 | NUMERIC | 8 | 4 | — |
| 11 | BKRFQ_COST_9 | NUMERIC | 8 | 4 | — |
| 12 | BKRFQ_CQCHANGE | STRING | 1 | — | — |
| 13 | BKRFQ_CWHO | STRING | 15 | — | — |
| 14 | BKRFQ_EST | NUMERIC | 8 | — | Estimate Number |
| 15 | BKRFQ_EST_LINE | NUMERIC | 8 | — | — |
| 16 | BKRFQ_EXP | DATE | 4 | — | Expiration Date |
| 17 | BKRFQ_EXTRA | STRING | 50 | — | Extra |
| 18 | BKRFQ_FLAG | STRING | 1 | — | — |
| 19 | BKRFQ_GDATE | DATE | 4 | — | — |
| 20 | BKRFQ_ISSUE | DATE | 4 | — | Issue Date |
| 21 | BKRFQ_LCDATE | DATE | 4 | — | — |
| 22 | BKRFQ_LEAD | INTEGER | 2 | — | Lead Time |
| 23 | BKRFQ_MAXDAYS | INTEGER | 2 | — | — |
| 24 | BKRFQ_MIN | NUMERIC | 8 | 2 | Minimum |
| 25 | BKRFQ_MINCST | NUMERIC | 8 | 2 | Minimum Cost |
| 26 | BKRFQ_NUM | NUMERIC | 8 | — | Quote/RFQ Number |
| 27 | BKRFQ_OPER | INTEGER | 2 | — | WO Operation Number |
| 28 | BKRFQ_PARENT | STRING | 15 | — | Parent part Number |
| 29 | BKRFQ_PARNTDESC | STRING | 30 | — | Parent Part Description |
| 30 | BKRFQ_PCONV | NUMERIC | 8 | 4 | — |
| 31 | BKRFQ_PROD | STRING | 15 | — | Part Code |
| 32 | BKRFQ_PRODDESC | STRING | 30 | — | Part Description |
| 33 | BKRFQ_PUM | STRING | 3 | — | Unit of Measure |
| 34 | BKRFQ_QTY_1 | NUMERIC | 8 | 2 | — |
| 35 | BKRFQ_QTY_10 | NUMERIC | 8 | 2 | — |
| 36 | BKRFQ_QTY_2 | NUMERIC | 8 | 2 | — |
| 37 | BKRFQ_QTY_3 | NUMERIC | 8 | 2 | — |
| 38 | BKRFQ_QTY_4 | NUMERIC | 8 | 2 | — |
| 39 | BKRFQ_QTY_5 | NUMERIC | 8 | 2 | — |
| 40 | BKRFQ_QTY_6 | NUMERIC | 8 | 2 | — |
| 41 | BKRFQ_QTY_7 | NUMERIC | 8 | 2 | — |
| 42 | BKRFQ_QTY_8 | NUMERIC | 8 | 2 | — |
| 43 | BKRFQ_QTY_9 | NUMERIC | 8 | 2 | — |
| 44 | BKRFQ_USE | STRING | 1 | — | — |
| 45 | BKRFQ_UWHO | STRING | 15 | — | — |
| 46 | BKRFQ_VEND | STRING | 10 | — | Vendor Code |
| 47 | BKRFQ_VENDNAME | STRING | 25 | — | Vendor Name |
| 48 | BKRFQ_WOPRE | NUMERIC | 8 | — | WO Prefix |
| 49 | BKRFQ_WOSUF | INTEGER | 2 | — | WO Suffix |

## BKRFQDES
**RFQ NOTES**

Fields: 5

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BK_DESC_CODE | STRING | 15 | — | not used |
| 2 | BK_DESC_DESC | STRING | 25 | — | not used |
| 3 | BK_DESC_LINE | INTEGER | 2 | — | Notes line number |
| 4 | BK_DESC_NOTES | STRING | 70 | — | Notes - text |
| 5 | BK_DESC_NUM | NUMERIC | 8 | — | PO Number |

## BKSOPO
**TEMP FILE FOR CONVERT SO TO PO**

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

## BKWOPO
**TEMP FILE FOR CONVERT WO TO PO**

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

## ISAPARFL
**ARCHIVED RFQ LINE**

Fields: 38

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKAP_POL_ARD | DATE | 4 | — | Actaul Receipt Date |
| 2 | BKAP_POL_BUYOFF | NUMERIC | 8 | 2 | Quantity Buy-Off  From QC |
| 3 | BKAP_POL_CNTR | INTEGER | 2 | — | Line Number |
| 4 | BKAP_POL_ERD | DATE | 4 | — | Estimatred Receipt Date |
| 5 | BKAP_POL_EST | NUMERIC | 8 | — | Estimated Receipt Date |
| 6 | BKAP_POL_EXTRA | STRING | 100 | — | Extra |
| 7 | BKAP_POL_GLA | STRING | 10 | — | GL Account Number |
| 8 | BKAP_POL_GLDPTA | STRING | 4 | — | GL Department |
| 9 | BKAP_POL_INVDTE | DATE | 4 | — | — |
| 10 | BKAP_POL_INVNUM | STRING | 10 | — | not used |
| 11 | BKAP_POL_IQTY | NUMERIC | 8 | 2 | Invoiced Quantity |
| 12 | BKAP_POL_ITM_NO | STRING | 9 | — | Item Number |
| 13 | BKAP_POL_ITYPE | STRING | 1 | — | not used |
| 14 | BKAP_POL_LOC | STRING | 10 | — | Location |
| 15 | BKAP_POL_OO_QTY | NUMERIC | 8 | 2 | Quantity On Order (remaining) |
| 16 | BKAP_POL_OPER | INTEGER | 2 | — | WO Operation number |
| 17 | BKAP_POL_PARENT | STRING | 15 | — | called from POA, POB |
| 18 | BKAP_POL_PCODE | STRING | 15 | — | Part Code |
| 19 | BKAP_POL_PCOGS | NUMERIC | 8 | 2 | COGS |
| 20 | BKAP_POL_PCONV | NUMERIC | 8 | 5 | — |
| 21 | BKAP_POL_PDESC | STRING | 30 | — | Description |
| 22 | BKAP_POL_PDISC | NUMERIC | 8 | 2 | Discount |
| 23 | BKAP_POL_PEXT | NUMERIC | 8 | 2 | Extended  Total |
| 24 | BKAP_POL_PKSQTY | NUMERIC | 8 | 2 | — |
| 25 | BKAP_POL_PONM | NUMERIC | 8 | — | PO Number |
| 26 | BKAP_POL_PPRCE | NUMERIC | 8 | 4 | Price |
| 27 | BKAP_POL_PQTY | NUMERIC | 8 | 2 | Quantity Ordered |
| 28 | BKAP_POL_PRTDIM | STRING | 1 | — | called from POA, POB |
| 29 | BKAP_POL_PSTDTE | DATE | 4 | — | — |
| 30 | BKAP_POL_QC_QTY | NUMERIC | 8 | 2 | QC Quantity |
| 31 | BKAP_POL_RECNUM | NUMERIC | 8 | — | not used |
| 32 | BKAP_POL_RQTY | NUMERIC | 8 | 2 | Recevied Quantity |
| 33 | BKAP_POL_SCRAP | NUMERIC | 8 | 2 | Quantity Scraped |
| 34 | BKAP_POL_TXBLE | STRING | 1 | — | Taxable Y/N |
| 35 | BKAP_POL_WOPRE | NUMERIC | 8 | — | Work Order Prefix |
| 36 | BKAP_POL_WOSUF | INTEGER | 2 | — | Work Order Suffix |
| 37 | NKAP_POL_UM_LIN_1 | STRING | 3 | — | — |
| 38 | NKAP_POL_UM_LIN_2 | STRING | 3 | — | — |

## ISAPARFQ
**ARCHIVED RFQ HEADER**

Fields: 58

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKAP_PO_CONFIRM_1 | STRING | 1 | — | — |
| 2 | BKAP_PO_CONFIRM_2 | STRING | 1 | — | — |
| 3 | BKAP_PO_DESC | STRING | 30 | — | PO Description |
| 4 | BKAP_PO_EMPNUM | INTEGER | 2 | — | — |
| 5 | BKAP_PO_ENDLNE | STRING | 1 | — | Ending Lines Y/N |
| 6 | BKAP_PO_ENTBY | STRING | 2 | — | PO Entered By |
| 7 | BKAP_PO_EXTRA | STRING | 150 | — | Extra |
| 8 | BKAP_PO_FOB | STRING | 20 | — | Ship FOB |
| 9 | BKAP_PO_FTERMD | STRING | 10 | — | Freight Terms Description |
| 10 | BKAP_PO_FTERMNM | INTEGER | 2 | — | Freight Terms Number |
| 11 | BKAP_PO_GLDPT | STRING | 4 | — | GL Department |
| 12 | BKAP_PO_INVNUM | STRING | 10 | — | not used |
| 13 | BKAP_PO_ISBROKE | STRING | 10 | — | Broker Code |
| 14 | BKAP_PO_ISCUR | STRING | 3 | — | Currency |
| 15 | BKAP_PO_ISMCDT | DATE | 4 | — | Multi-Currency Date |
| 16 | BKAP_PO_ISREV | STRING | 1 | — | Rev - only called in POB |
| 17 | BKAP_PO_ISRVDT | DATE | 4 | — | Rev Date - only called in POB |
| 18 | BKAP_PO_ISTXGR | STRING | 10 | — | Tax Group |
| 19 | BKAP_PO_ITOTAL | NUMERIC | 8 | 2 | Invoiced Total |
| 20 | BKAP_PO_LOC | STRING | 10 | — | Location |
| 21 | BKAP_PO_LONGPO | STRING | 25 | — | not used |
| 22 | BKAP_PO_NL | INTEGER | 2 | — | Number of Lines |
| 23 | BKAP_PO_NUM | NUMERIC | 8 | — | PO Number |
| 24 | BKAP_PO_OBYCUS | STRING | 15 | — | Job Number |
| 25 | BKAP_PO_ORDDTE | DATE | 4 | — | Order Date |
| 26 | BKAP_PO_PCKSLP | STRING | 15 | — | — |
| 27 | BKAP_PO_PRTD | STRING | 1 | — | Printed   Y/P/R |
| 28 | BKAP_PO_QCTOTAL | NUMERIC | 8 | 2 | QC Total |
| 29 | BKAP_PO_RECNUM | NUMERIC | 8 | — | not used |
| 30 | BKAP_PO_RNI^ | NUMERIC | 8 | 2 | — |
| 31 | BKAP_PO_SHPA1 | STRING | 30 | — | Ship Loc Address Line 1 |
| 32 | BKAP_PO_SHPA2 | STRING | 30 | — | Ship Loc Address Line 2 |
| 33 | BKAP_PO_SHPA3 | STRING | 30 | — | Ship Loc. Address Line 3 |
| 34 | BKAP_PO_SHPATN | STRING | 30 | — | Ship Attention |
| 35 | BKAP_PO_SHPCNT | STRING | 30 | — | Ship Country |
| 36 | BKAP_PO_SHPCOD | STRING | 10 | — | Ship To Loc Code |
| 37 | BKAP_PO_SHPCTY | STRING | 26 | — | Ship Loc City |
| 38 | BKAP_PO_SHPNME | STRING | 30 | — | Ship Loc Name |
| 39 | BKAP_PO_SHPST | STRING | 2 | — | Ship loc State |
| 40 | BKAP_PO_SHPVIA | STRING | 15 | — | Ship VIA |
| 41 | BKAP_PO_SHPZIP | STRING | 10 | — | Ship Loc ZIP Code |
| 42 | BKAP_PO_SUBTOT | NUMERIC | 8 | 2 | Sub Total |
| 43 | BKAP_PO_TAXABLE | STRING | 1 | — | Taxable Y/N |
| 44 | BKAP_PO_TAXAMT | NUMERIC | 8 | 2 | Tax Amount |
| 45 | BKAP_PO_TAXRTE | NUMERIC | 8 | 3 | Tax Rate |
| 46 | BKAP_PO_TERMD | STRING | 10 | — | Terms Description |
| 47 | BKAP_PO_TERMNM | INTEGER | 2 | — | Terms Number |
| 48 | BKAP_PO_TOTAL | NUMERIC | 8 | 2 | Total |
| 49 | BKAP_PO_VNDA1 | STRING | 30 | — | Vendor Address Line 1 |
| 50 | BKAP_PO_VNDA2 | STRING | 30 | — | Vendor Address Line 2 |
| 51 | BKAP_PO_VNDA3 | STRING | 30 | — | Vendor Address 3 |
| 52 | BKAP_PO_VNDATN | STRING | 30 | — | Vendor Attention |
| 53 | BKAP_PO_VNDCNT | STRING | 30 | — | Vvendor Country |
| 54 | BKAP_PO_VNDCOD | STRING | 10 | — | Vendor Code |
| 55 | BKAP_PO_VNDCTY | STRING | 26 | — | Vemdor City |
| 56 | BKAP_PO_VNDNME | STRING | 30 | — | Vendor Name |
| 57 | BKAP_PO_VNDST | STRING | 2 | — | Vendor State |
| 58 | BKAP_PO_VNDZIP | STRING | 10 | — | Vendor ZIP Code |

## ISAPCHG
**CHANGES TO PURCHASE ORDERS**

Fields: 32

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISAP_CHG_AARD | DATE | 4 | — | — |
| 2 | ISAP_CHG_ACONV | NUMERIC | 8 | 5 | — |
| 3 | ISAP_CHG_ADISC | NUMERIC | 8 | 2 | — |
| 4 | ISAP_CHG_AERD | DATE | 4 | — | — |
| 5 | ISAP_CHG_AEXTRA | STRING | 150 | — | — |
| 6 | ISAP_CHG_AGLA | STRING | 10 | — | — |
| 7 | ISAP_CHG_AGLD | STRING | 4 | — | — |
| 8 | ISAP_CHG_ALOC | STRING | 10 | — | — |
| 9 | ISAP_CHG_AOOQTY | NUMERIC | 8 | 2 | — |
| 10 | ISAP_CHG_AOPER | INTEGER | 2 | — | — |
| 11 | ISAP_CHG_APRICE | NUMERIC | 8 | 4 | — |
| 12 | ISAP_CHG_AWOP | NUMERIC | 8 | — | — |
| 13 | ISAP_CHG_AWOS | INTEGER | 2 | — | — |
| 14 | ISAP_CHG_BARD | DATE | 4 | — | — |
| 15 | ISAP_CHG_BCONV | NUMERIC | 8 | 5 | — |
| 16 | ISAP_CHG_BDISC | NUMERIC | 8 | 2 | — |
| 17 | ISAP_CHG_BERD | DATE | 4 | — | — |
| 18 | ISAP_CHG_BEXTRA | STRING | 150 | — | — |
| 19 | ISAP_CHG_BGLA | STRING | 10 | — | — |
| 20 | ISAP_CHG_BGLD | STRING | 4 | — | — |
| 21 | ISAP_CHG_BLOC | STRING | 10 | — | — |
| 22 | ISAP_CHG_BOOQTY | NUMERIC | 8 | 2 | — |
| 23 | ISAP_CHG_BOPER | INTEGER | 2 | — | — |
| 24 | ISAP_CHG_BPRICE | NUMERIC | 8 | 4 | — |
| 25 | ISAP_CHG_BWOP | NUMERIC | 8 | — | — |
| 26 | ISAP_CHG_BWOS | INTEGER | 2 | — | — |
| 27 | ISAP_CHG_CDATE | DATE | 4 | — | — |
| 28 | ISAP_CHG_LINEID | INTEGER | 2 | — | — |
| 29 | ISAP_CHG_PCODE | STRING | 15 | — | — |
| 30 | ISAP_CHG_PONUM | NUMERIC | 8 | — | — |
| 31 | ISAP_CHG_REVLVL | STRING | 10 | — | — |
| 32 | ISAP_CHG_USER | STRING | 15 | — | — |

## ISAPHQT
**ARCHIVE VENDOR PRICING**

Fields: 49

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKRFQ_ALPHA1 | STRING | 15 | — | — |
| 2 | BKRFQ_COST_1 | NUMERIC | 8 | 4 | — |
| 3 | BKRFQ_COST_10 | NUMERIC | 8 | 4 | — |
| 4 | BKRFQ_COST_2 | NUMERIC | 8 | 4 | — |
| 5 | BKRFQ_COST_3 | NUMERIC | 8 | 4 | — |
| 6 | BKRFQ_COST_4 | NUMERIC | 8 | 4 | — |
| 7 | BKRFQ_COST_5 | NUMERIC | 8 | 4 | — |
| 8 | BKRFQ_COST_6 | NUMERIC | 8 | 4 | — |
| 9 | BKRFQ_COST_7 | NUMERIC | 8 | 4 | — |
| 10 | BKRFQ_COST_8 | NUMERIC | 8 | 4 | — |
| 11 | BKRFQ_COST_9 | NUMERIC | 8 | 4 | — |
| 12 | BKRFQ_CQCHANGE | STRING | 1 | — | — |
| 13 | BKRFQ_CWHO | STRING | 15 | — | — |
| 14 | BKRFQ_EST | NUMERIC | 8 | — | Estimate Number |
| 15 | BKRFQ_EST_LINE | NUMERIC | 8 | — | — |
| 16 | BKRFQ_EXP | DATE | 4 | — | Expiration Date |
| 17 | BKRFQ_EXTRA | STRING | 50 | — | Extra |
| 18 | BKRFQ_FLAG | STRING | 1 | — | — |
| 19 | BKRFQ_GDATE | DATE | 4 | — | — |
| 20 | BKRFQ_ISSUE | DATE | 4 | — | Issue Date |
| 21 | BKRFQ_LCDATE | DATE | 4 | — | — |
| 22 | BKRFQ_LEAD | INTEGER | 2 | — | Lead Time |
| 23 | BKRFQ_MAXDAYS | INTEGER | 2 | — | — |
| 24 | BKRFQ_MIN | NUMERIC | 8 | 2 | Minimum |
| 25 | BKRFQ_MINCST | NUMERIC | 8 | 2 | Minimum Cost |
| 26 | BKRFQ_NUM | NUMERIC | 8 | — | Quote/RFQ Number |
| 27 | BKRFQ_OPER | INTEGER | 2 | — | WO Operation Number |
| 28 | BKRFQ_PARENT | STRING | 15 | — | Parent part Number |
| 29 | BKRFQ_PARNTDESC | STRING | 30 | — | Parent Part Description |
| 30 | BKRFQ_PCONV | NUMERIC | 8 | 4 | — |
| 31 | BKRFQ_PROD | STRING | 15 | — | Part Code |
| 32 | BKRFQ_PRODDESC | STRING | 30 | — | Part Description |
| 33 | BKRFQ_PUM | STRING | 3 | — | Unit of Measure |
| 34 | BKRFQ_QTY_1 | NUMERIC | 8 | 2 | — |
| 35 | BKRFQ_QTY_10 | NUMERIC | 8 | 2 | — |
| 36 | BKRFQ_QTY_2 | NUMERIC | 8 | 2 | — |
| 37 | BKRFQ_QTY_3 | NUMERIC | 8 | 2 | — |
| 38 | BKRFQ_QTY_4 | NUMERIC | 8 | 2 | — |
| 39 | BKRFQ_QTY_5 | NUMERIC | 8 | 2 | — |
| 40 | BKRFQ_QTY_6 | NUMERIC | 8 | 2 | — |
| 41 | BKRFQ_QTY_7 | NUMERIC | 8 | 2 | — |
| 42 | BKRFQ_QTY_8 | NUMERIC | 8 | 2 | — |
| 43 | BKRFQ_QTY_9 | NUMERIC | 8 | 2 | — |
| 44 | BKRFQ_USE | STRING | 1 | — | — |
| 45 | BKRFQ_UWHO | STRING | 15 | — | — |
| 46 | BKRFQ_VEND | STRING | 10 | — | Vendor Code |
| 47 | BKRFQ_VENDNAME | STRING | 25 | — | Vendor Name |
| 48 | BKRFQ_WOPRE | NUMERIC | 8 | — | WO Prefix |
| 49 | BKRFQ_WOSUF | INTEGER | 2 | — | WO Suffix |

## ISAPOPO
**ARCHIVED OPEN PO**

Fields: 58

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKAP_PO_CONFIRM_1 | STRING | 1 | — | — |
| 2 | BKAP_PO_CONFIRM_2 | STRING | 1 | — | — |
| 3 | BKAP_PO_DESC | STRING | 30 | — | PO Description |
| 4 | BKAP_PO_EMPNUM | INTEGER | 2 | — | — |
| 5 | BKAP_PO_ENDLNE | STRING | 1 | — | Ending Lines Y/N |
| 6 | BKAP_PO_ENTBY | STRING | 2 | — | PO Entered By |
| 7 | BKAP_PO_EXTRA | STRING | 150 | — | Extra |
| 8 | BKAP_PO_FOB | STRING | 20 | — | Ship FOB |
| 9 | BKAP_PO_FTERMD | STRING | 10 | — | Freight Terms Description |
| 10 | BKAP_PO_FTERMNM | INTEGER | 2 | — | Freight Terms Number |
| 11 | BKAP_PO_GLDPT | STRING | 4 | — | GL Department |
| 12 | BKAP_PO_INVNUM | STRING | 10 | — | not used |
| 13 | BKAP_PO_ISBROKE | STRING | 10 | — | Broker Code |
| 14 | BKAP_PO_ISCUR | STRING | 3 | — | Currency |
| 15 | BKAP_PO_ISMCDT | DATE | 4 | — | Multi-Currency Date |
| 16 | BKAP_PO_ISREV | STRING | 1 | — | Rev - only called in POB |
| 17 | BKAP_PO_ISRVDT | DATE | 4 | — | Rev Date - only called in POB |
| 18 | BKAP_PO_ISTXGR | STRING | 10 | — | Tax Group |
| 19 | BKAP_PO_ITOTAL | NUMERIC | 8 | 2 | Invoiced Total |
| 20 | BKAP_PO_LOC | STRING | 10 | — | Location |
| 21 | BKAP_PO_LONGPO | STRING | 25 | — | not used |
| 22 | BKAP_PO_NL | INTEGER | 2 | — | Number of Lines |
| 23 | BKAP_PO_NUM | NUMERIC | 8 | — | PO Number |
| 24 | BKAP_PO_OBYCUS | STRING | 15 | — | Job Number |
| 25 | BKAP_PO_ORDDTE | DATE | 4 | — | Order Date |
| 26 | BKAP_PO_PCKSLP | STRING | 15 | — | — |
| 27 | BKAP_PO_PRTD | STRING | 1 | — | Printed   Y/P/R |
| 28 | BKAP_PO_QCTOTAL | NUMERIC | 8 | 2 | QC Total |
| 29 | BKAP_PO_RECNUM | NUMERIC | 8 | — | not used |
| 30 | BKAP_PO_RNI^ | NUMERIC | 8 | 2 | — |
| 31 | BKAP_PO_SHPA1 | STRING | 30 | — | Ship Loc Address Line 1 |
| 32 | BKAP_PO_SHPA2 | STRING | 30 | — | Ship Loc Address Line 2 |
| 33 | BKAP_PO_SHPA3 | STRING | 30 | — | Ship Loc. Address Line 3 |
| 34 | BKAP_PO_SHPATN | STRING | 30 | — | Ship Attention |
| 35 | BKAP_PO_SHPCNT | STRING | 30 | — | Ship Country |
| 36 | BKAP_PO_SHPCOD | STRING | 10 | — | Ship To Loc Code |
| 37 | BKAP_PO_SHPCTY | STRING | 26 | — | Ship Loc City |
| 38 | BKAP_PO_SHPNME | STRING | 30 | — | Ship Loc Name |
| 39 | BKAP_PO_SHPST | STRING | 2 | — | Ship loc State |
| 40 | BKAP_PO_SHPVIA | STRING | 15 | — | Ship VIA |
| 41 | BKAP_PO_SHPZIP | STRING | 10 | — | Ship Loc ZIP Code |
| 42 | BKAP_PO_SUBTOT | NUMERIC | 8 | 2 | Sub Total |
| 43 | BKAP_PO_TAXABLE | STRING | 1 | — | Taxable Y/N |
| 44 | BKAP_PO_TAXAMT | NUMERIC | 8 | 2 | Tax Amount |
| 45 | BKAP_PO_TAXRTE | NUMERIC | 8 | 3 | Tax Rate |
| 46 | BKAP_PO_TERMD | STRING | 10 | — | Terms Description |
| 47 | BKAP_PO_TERMNM | INTEGER | 2 | — | Terms Number |
| 48 | BKAP_PO_TOTAL | NUMERIC | 8 | 2 | Total |
| 49 | BKAP_PO_VNDA1 | STRING | 30 | — | Vendor Address Line 1 |
| 50 | BKAP_PO_VNDA2 | STRING | 30 | — | Vendor Address Line 2 |
| 51 | BKAP_PO_VNDA3 | STRING | 30 | — | Vendor Address 3 |
| 52 | BKAP_PO_VNDATN | STRING | 30 | — | Vendor Attention |
| 53 | BKAP_PO_VNDCNT | STRING | 30 | — | Vvendor Country |
| 54 | BKAP_PO_VNDCOD | STRING | 10 | — | Vendor Code |
| 55 | BKAP_PO_VNDCTY | STRING | 26 | — | Vemdor City |
| 56 | BKAP_PO_VNDNME | STRING | 30 | — | Vendor Name |
| 57 | BKAP_PO_VNDST | STRING | 2 | — | Vendor State |
| 58 | BKAP_PO_VNDZIP | STRING | 10 | — | Vendor ZIP Code |

## ISAPOPOL
**ARCHIVED OPEN PO LINES**

Fields: 38

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKAP_POL_ARD | DATE | 4 | — | Actaul Receipt Date |
| 2 | BKAP_POL_BUYOFF | NUMERIC | 8 | 2 | Quantity Buy-Off  From QC |
| 3 | BKAP_POL_CNTR | INTEGER | 2 | — | Line Number |
| 4 | BKAP_POL_ERD | DATE | 4 | — | Estimatred Receipt Date |
| 5 | BKAP_POL_EST | NUMERIC | 8 | — | Estimated Receipt Date |
| 6 | BKAP_POL_EXTRA | STRING | 100 | — | Extra |
| 7 | BKAP_POL_GLA | STRING | 10 | — | GL Account Number |
| 8 | BKAP_POL_GLDPTA | STRING | 4 | — | GL Department |
| 9 | BKAP_POL_INVDTE | DATE | 4 | — | — |
| 10 | BKAP_POL_INVNUM | STRING | 10 | — | not used |
| 11 | BKAP_POL_IQTY | NUMERIC | 8 | 2 | Invoiced Quantity |
| 12 | BKAP_POL_ITM_NO | STRING | 9 | — | Item Number |
| 13 | BKAP_POL_ITYPE | STRING | 1 | — | not used |
| 14 | BKAP_POL_LOC | STRING | 10 | — | Location |
| 15 | BKAP_POL_OO_QTY | NUMERIC | 8 | 2 | Quantity On Order (remaining) |
| 16 | BKAP_POL_OPER | INTEGER | 2 | — | WO Operation number |
| 17 | BKAP_POL_PARENT | STRING | 15 | — | called from POA, POB |
| 18 | BKAP_POL_PCODE | STRING | 15 | — | Part Code |
| 19 | BKAP_POL_PCOGS | NUMERIC | 8 | 2 | COGS |
| 20 | BKAP_POL_PCONV | NUMERIC | 8 | 5 | — |
| 21 | BKAP_POL_PDESC | STRING | 30 | — | Description |
| 22 | BKAP_POL_PDISC | NUMERIC | 8 | 2 | Discount |
| 23 | BKAP_POL_PEXT | NUMERIC | 8 | 2 | Extended  Total |
| 24 | BKAP_POL_PKSQTY | NUMERIC | 8 | 2 | — |
| 25 | BKAP_POL_PONM | NUMERIC | 8 | — | PO Number |
| 26 | BKAP_POL_PPRCE | NUMERIC | 8 | 4 | Price |
| 27 | BKAP_POL_PQTY | NUMERIC | 8 | 2 | Quantity Ordered |
| 28 | BKAP_POL_PRTDIM | STRING | 1 | — | called from POA, POB |
| 29 | BKAP_POL_PSTDTE | DATE | 4 | — | — |
| 30 | BKAP_POL_QC_QTY | NUMERIC | 8 | 2 | QC Quantity |
| 31 | BKAP_POL_RECNUM | NUMERIC | 8 | — | not used |
| 32 | BKAP_POL_RQTY | NUMERIC | 8 | 2 | Recevied Quantity |
| 33 | BKAP_POL_SCRAP | NUMERIC | 8 | 2 | Quantity Scraped |
| 34 | BKAP_POL_TXBLE | STRING | 1 | — | Taxable Y/N |
| 35 | BKAP_POL_WOPRE | NUMERIC | 8 | — | Work Order Prefix |
| 36 | BKAP_POL_WOSUF | INTEGER | 2 | — | Work Order Suffix |
| 37 | NKAP_POL_UM_LIN_1 | STRING | 3 | — | — |
| 38 | NKAP_POL_UM_LIN_2 | STRING | 3 | — | — |

## ISAPQTQT
**ARCHIVED VENDOR PRICING**

Fields: 49

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKRFQ_ALPHA1 | STRING | 15 | — | — |
| 2 | BKRFQ_COST_1 | NUMERIC | 8 | 4 | — |
| 3 | BKRFQ_COST_10 | NUMERIC | 8 | 4 | — |
| 4 | BKRFQ_COST_2 | NUMERIC | 8 | 4 | — |
| 5 | BKRFQ_COST_3 | NUMERIC | 8 | 4 | — |
| 6 | BKRFQ_COST_4 | NUMERIC | 8 | 4 | — |
| 7 | BKRFQ_COST_5 | NUMERIC | 8 | 4 | — |
| 8 | BKRFQ_COST_6 | NUMERIC | 8 | 4 | — |
| 9 | BKRFQ_COST_7 | NUMERIC | 8 | 4 | — |
| 10 | BKRFQ_COST_8 | NUMERIC | 8 | 4 | — |
| 11 | BKRFQ_COST_9 | NUMERIC | 8 | 4 | — |
| 12 | BKRFQ_CQCHANGE | STRING | 1 | — | — |
| 13 | BKRFQ_CWHO | STRING | 15 | — | — |
| 14 | BKRFQ_EST | NUMERIC | 8 | — | Estimate Number |
| 15 | BKRFQ_EST_LINE | NUMERIC | 8 | — | — |
| 16 | BKRFQ_EXP | DATE | 4 | — | Expiration Date |
| 17 | BKRFQ_EXTRA | STRING | 50 | — | Extra |
| 18 | BKRFQ_FLAG | STRING | 1 | — | — |
| 19 | BKRFQ_GDATE | DATE | 4 | — | — |
| 20 | BKRFQ_ISSUE | DATE | 4 | — | Issue Date |
| 21 | BKRFQ_LCDATE | DATE | 4 | — | — |
| 22 | BKRFQ_LEAD | INTEGER | 2 | — | Lead Time |
| 23 | BKRFQ_MAXDAYS | INTEGER | 2 | — | — |
| 24 | BKRFQ_MIN | NUMERIC | 8 | 2 | Minimum |
| 25 | BKRFQ_MINCST | NUMERIC | 8 | 2 | Minimum Cost |
| 26 | BKRFQ_NUM | NUMERIC | 8 | — | Quote/RFQ Number |
| 27 | BKRFQ_OPER | INTEGER | 2 | — | WO Operation Number |
| 28 | BKRFQ_PARENT | STRING | 15 | — | Parent part Number |
| 29 | BKRFQ_PARNTDESC | STRING | 30 | — | Parent Part Description |
| 30 | BKRFQ_PCONV | NUMERIC | 8 | 4 | — |
| 31 | BKRFQ_PROD | STRING | 15 | — | Part Code |
| 32 | BKRFQ_PRODDESC | STRING | 30 | — | Part Description |
| 33 | BKRFQ_PUM | STRING | 3 | — | Unit of Measure |
| 34 | BKRFQ_QTY_1 | NUMERIC | 8 | 2 | — |
| 35 | BKRFQ_QTY_10 | NUMERIC | 8 | 2 | — |
| 36 | BKRFQ_QTY_2 | NUMERIC | 8 | 2 | — |
| 37 | BKRFQ_QTY_3 | NUMERIC | 8 | 2 | — |
| 38 | BKRFQ_QTY_4 | NUMERIC | 8 | 2 | — |
| 39 | BKRFQ_QTY_5 | NUMERIC | 8 | 2 | — |
| 40 | BKRFQ_QTY_6 | NUMERIC | 8 | 2 | — |
| 41 | BKRFQ_QTY_7 | NUMERIC | 8 | 2 | — |
| 42 | BKRFQ_QTY_8 | NUMERIC | 8 | 2 | — |
| 43 | BKRFQ_QTY_9 | NUMERIC | 8 | 2 | — |
| 44 | BKRFQ_USE | STRING | 1 | — | — |
| 45 | BKRFQ_UWHO | STRING | 15 | — | — |
| 46 | BKRFQ_VEND | STRING | 10 | — | Vendor Code |
| 47 | BKRFQ_VENDNAME | STRING | 25 | — | Vendor Name |
| 48 | BKRFQ_WOPRE | NUMERIC | 8 | — | WO Prefix |
| 49 | BKRFQ_WOSUF | INTEGER | 2 | — | WO Suffix |

## ISARFQ
**ARCHIVE RFQ**

Fields: 49

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKRFQ_ALPHA1 | STRING | 15 | — | — |
| 2 | BKRFQ_COST_1 | NUMERIC | 8 | 4 | — |
| 3 | BKRFQ_COST_10 | NUMERIC | 8 | 4 | — |
| 4 | BKRFQ_COST_2 | NUMERIC | 8 | 4 | — |
| 5 | BKRFQ_COST_3 | NUMERIC | 8 | 4 | — |
| 6 | BKRFQ_COST_4 | NUMERIC | 8 | 4 | — |
| 7 | BKRFQ_COST_5 | NUMERIC | 8 | 4 | — |
| 8 | BKRFQ_COST_6 | NUMERIC | 8 | 4 | — |
| 9 | BKRFQ_COST_7 | NUMERIC | 8 | 4 | — |
| 10 | BKRFQ_COST_8 | NUMERIC | 8 | 4 | — |
| 11 | BKRFQ_COST_9 | NUMERIC | 8 | 4 | — |
| 12 | BKRFQ_CQCHANGE | STRING | 1 | — | — |
| 13 | BKRFQ_CWHO | STRING | 15 | — | — |
| 14 | BKRFQ_EST | NUMERIC | 8 | — | Estimate Number |
| 15 | BKRFQ_EST_LINE | NUMERIC | 8 | — | — |
| 16 | BKRFQ_EXP | DATE | 4 | — | Expiration Date |
| 17 | BKRFQ_EXTRA | STRING | 50 | — | Extra |
| 18 | BKRFQ_FLAG | STRING | 1 | — | — |
| 19 | BKRFQ_GDATE | DATE | 4 | — | — |
| 20 | BKRFQ_ISSUE | DATE | 4 | — | Issue Date |
| 21 | BKRFQ_LCDATE | DATE | 4 | — | — |
| 22 | BKRFQ_LEAD | INTEGER | 2 | — | Lead Time |
| 23 | BKRFQ_MAXDAYS | INTEGER | 2 | — | — |
| 24 | BKRFQ_MIN | NUMERIC | 8 | 2 | Minimum |
| 25 | BKRFQ_MINCST | NUMERIC | 8 | 2 | Minimum Cost |
| 26 | BKRFQ_NUM | NUMERIC | 8 | — | Quote/RFQ Number |
| 27 | BKRFQ_OPER | INTEGER | 2 | — | WO Operation Number |
| 28 | BKRFQ_PARENT | STRING | 15 | — | Parent part Number |
| 29 | BKRFQ_PARNTDESC | STRING | 30 | — | Parent Part Description |
| 30 | BKRFQ_PCONV | NUMERIC | 8 | 4 | — |
| 31 | BKRFQ_PROD | STRING | 15 | — | Part Code |
| 32 | BKRFQ_PRODDESC | STRING | 30 | — | Part Description |
| 33 | BKRFQ_PUM | STRING | 3 | — | Unit of Measure |
| 34 | BKRFQ_QTY_1 | NUMERIC | 8 | 2 | — |
| 35 | BKRFQ_QTY_10 | NUMERIC | 8 | 2 | — |
| 36 | BKRFQ_QTY_2 | NUMERIC | 8 | 2 | — |
| 37 | BKRFQ_QTY_3 | NUMERIC | 8 | 2 | — |
| 38 | BKRFQ_QTY_4 | NUMERIC | 8 | 2 | — |
| 39 | BKRFQ_QTY_5 | NUMERIC | 8 | 2 | — |
| 40 | BKRFQ_QTY_6 | NUMERIC | 8 | 2 | — |
| 41 | BKRFQ_QTY_7 | NUMERIC | 8 | 2 | — |
| 42 | BKRFQ_QTY_8 | NUMERIC | 8 | 2 | — |
| 43 | BKRFQ_QTY_9 | NUMERIC | 8 | 2 | — |
| 44 | BKRFQ_USE | STRING | 1 | — | — |
| 45 | BKRFQ_UWHO | STRING | 15 | — | — |
| 46 | BKRFQ_VEND | STRING | 10 | — | Vendor Code |
| 47 | BKRFQ_VENDNAME | STRING | 25 | — | Vendor Name |
| 48 | BKRFQ_WOPRE | NUMERIC | 8 | — | WO Prefix |
| 49 | BKRFQ_WOSUF | INTEGER | 2 | — | WO Suffix |

## ISDIGSIG
**PO DIGITAL SIGNATURE**

Fields: 89

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_DSIG_ACTIVE_1 | STRING | 1 | — | — |
| 2 | IS_DSIG_ACTIVE_10 | STRING | 1 | — | — |
| 3 | IS_DSIG_ACTIVE_2 | STRING | 1 | — | — |
| 4 | IS_DSIG_ACTIVE_3 | STRING | 1 | — | — |
| 5 | IS_DSIG_ACTIVE_4 | STRING | 1 | — | — |
| 6 | IS_DSIG_ACTIVE_5 | STRING | 1 | — | — |
| 7 | IS_DSIG_ACTIVE_6 | STRING | 1 | — | — |
| 8 | IS_DSIG_ACTIVE_7 | STRING | 1 | — | — |
| 9 | IS_DSIG_ACTIVE_8 | STRING | 1 | — | — |
| 10 | IS_DSIG_ACTIVE_9 | STRING | 1 | — | — |
| 11 | IS_DSIG_ADATE | DATE | 4 | — | — |
| 12 | IS_DSIG_AMT_1 | NUMERIC | 8 | 2 | — |
| 13 | IS_DSIG_AMT_10 | NUMERIC | 8 | 2 | — |
| 14 | IS_DSIG_AMT_2 | NUMERIC | 8 | 2 | — |
| 15 | IS_DSIG_AMT_3 | NUMERIC | 8 | 2 | — |
| 16 | IS_DSIG_AMT_4 | NUMERIC | 8 | 2 | — |
| 17 | IS_DSIG_AMT_5 | NUMERIC | 8 | 2 | — |
| 18 | IS_DSIG_AMT_6 | NUMERIC | 8 | 2 | — |
| 19 | IS_DSIG_AMT_7 | NUMERIC | 8 | 2 | — |
| 20 | IS_DSIG_AMT_8 | NUMERIC | 8 | 2 | — |
| 21 | IS_DSIG_AMT_9 | NUMERIC | 8 | 2 | — |
| 22 | IS_DSIG_ATIME | TIME | 4 | — | — |
| 23 | IS_DSIG_DATE_1 | DATE | 4 | — | — |
| 24 | IS_DSIG_DATE_10 | DATE | 4 | — | — |
| 25 | IS_DSIG_DATE_2 | DATE | 4 | — | — |
| 26 | IS_DSIG_DATE_3 | DATE | 4 | — | — |
| 27 | IS_DSIG_DATE_4 | DATE | 4 | — | — |
| 28 | IS_DSIG_DATE_5 | DATE | 4 | — | — |
| 29 | IS_DSIG_DATE_6 | DATE | 4 | — | — |
| 30 | IS_DSIG_DATE_7 | DATE | 4 | — | — |
| 31 | IS_DSIG_DATE_8 | DATE | 4 | — | — |
| 32 | IS_DSIG_DATE_9 | DATE | 4 | — | — |
| 33 | IS_DSIG_EMP | INTEGER | 2 | — | — |
| 34 | IS_DSIG_EXTRA | STRING | 100 | — | — |
| 35 | IS_DSIG_FDATE_1 | DATE | 4 | — | — |
| 36 | IS_DSIG_FDATE_10 | DATE | 4 | — | — |
| 37 | IS_DSIG_FDATE_2 | DATE | 4 | — | — |
| 38 | IS_DSIG_FDATE_3 | DATE | 4 | — | — |
| 39 | IS_DSIG_FDATE_4 | DATE | 4 | — | — |
| 40 | IS_DSIG_FDATE_5 | DATE | 4 | — | — |
| 41 | IS_DSIG_FDATE_6 | DATE | 4 | — | — |
| 42 | IS_DSIG_FDATE_7 | DATE | 4 | — | — |
| 43 | IS_DSIG_FDATE_8 | DATE | 4 | — | — |
| 44 | IS_DSIG_FDATE_9 | DATE | 4 | — | — |
| 45 | IS_DSIG_FILE | STRING | 256 | — | — |
| 46 | IS_DSIG_FLAG_1 | STRING | 1 | — | — |
| 47 | IS_DSIG_FLAG_10 | STRING | 1 | — | — |
| 48 | IS_DSIG_FLAG_2 | STRING | 1 | — | — |
| 49 | IS_DSIG_FLAG_3 | STRING | 1 | — | — |
| 50 | IS_DSIG_FLAG_4 | STRING | 1 | — | — |
| 51 | IS_DSIG_FLAG_5 | STRING | 1 | — | — |
| 52 | IS_DSIG_FLAG_6 | STRING | 1 | — | — |
| 53 | IS_DSIG_FLAG_7 | STRING | 1 | — | — |
| 54 | IS_DSIG_FLAG_8 | STRING | 1 | — | — |
| 55 | IS_DSIG_FLAG_9 | STRING | 1 | — | — |
| 56 | IS_DSIG_MOTCACH | STRING | 16 | — | — |
| 57 | IS_DSIG_POAMT | NUMERIC | 8 | 2 | — |
| 58 | IS_DSIG_POENTBY | STRING | 2 | — | — |
| 59 | IS_DSIG_SDATE_1 | DATE | 4 | — | — |
| 60 | IS_DSIG_SDATE_10 | DATE | 4 | — | — |
| 61 | IS_DSIG_SDATE_2 | DATE | 4 | — | — |
| 62 | IS_DSIG_SDATE_3 | DATE | 4 | — | — |
| 63 | IS_DSIG_SDATE_4 | DATE | 4 | — | — |
| 64 | IS_DSIG_SDATE_5 | DATE | 4 | — | — |
| 65 | IS_DSIG_SDATE_6 | DATE | 4 | — | — |
| 66 | IS_DSIG_SDATE_7 | DATE | 4 | — | — |
| 67 | IS_DSIG_SDATE_8 | DATE | 4 | — | — |
| 68 | IS_DSIG_SDATE_9 | DATE | 4 | — | — |
| 69 | IS_DSIG_SOENTBY | STRING | 5 | — | — |
| 70 | IS_DSIG_TDATE_1 | DATE | 4 | — | — |
| 71 | IS_DSIG_TDATE_10 | DATE | 4 | — | — |
| 72 | IS_DSIG_TDATE_2 | DATE | 4 | — | — |
| 73 | IS_DSIG_TDATE_3 | DATE | 4 | — | — |
| 74 | IS_DSIG_TDATE_4 | DATE | 4 | — | — |
| 75 | IS_DSIG_TDATE_5 | DATE | 4 | — | — |
| 76 | IS_DSIG_TDATE_6 | DATE | 4 | — | — |
| 77 | IS_DSIG_TDATE_7 | DATE | 4 | — | — |
| 78 | IS_DSIG_TDATE_8 | DATE | 4 | — | — |
| 79 | IS_DSIG_TDATE_9 | DATE | 4 | — | — |
| 80 | IS_DSIG_TYPE_1 | STRING | 10 | — | — |
| 81 | IS_DSIG_TYPE_10 | STRING | 10 | — | — |
| 82 | IS_DSIG_TYPE_2 | STRING | 10 | — | — |
| 83 | IS_DSIG_TYPE_3 | STRING | 10 | — | — |
| 84 | IS_DSIG_TYPE_4 | STRING | 10 | — | — |
| 85 | IS_DSIG_TYPE_5 | STRING | 10 | — | — |
| 86 | IS_DSIG_TYPE_6 | STRING | 10 | — | — |
| 87 | IS_DSIG_TYPE_7 | STRING | 10 | — | — |
| 88 | IS_DSIG_TYPE_8 | STRING | 10 | — | — |
| 89 | IS_DSIG_TYPE_9 | STRING | 10 | — | — |

## ISPODESC
**PURCHASE ORDER DESCRIPTION LIST**

Fields: 1

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IORD_DESC_CODE | STRING | 30 | — | — |

## ISQCAMST
**ARCHIVED QC RECEIPTS**

Fields: 14

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKQC_EXTRA | STRING | 25 | — | — |
| 2 | BKQC_OUT_DATE | DATE | 4 | — | — |
| 3 | BKQC_PKSLIP_NUM | STRING | 15 | — | — |
| 4 | BKQC_PKSLIP_QTY | NUMERIC | 8 | 2 | — |
| 5 | BKQC_PO_NUM | NUMERIC | 8 | — | — |
| 6 | BKQC_POL_ITM_NO | STRING | 10 | — | — |
| 7 | BKQC_PROD_CODE | STRING | 15 | — | — |
| 8 | BKQC_QTY_BUYOFF | NUMERIC | 8 | 2 | — |
| 9 | BKQC_QTY_RECVD | NUMERIC | 8 | 2 | — |
| 10 | BKQC_QTY_REJECT | NUMERIC | 8 | 2 | — |
| 11 | BKQC_RECV_DATE | DATE | 4 | — | — |
| 12 | BKQC_RECVR_NUM | NUMERIC | 8 | — | — |
| 13 | BKQC_UNIT_COST | NUMERIC | 8 | 4 | — |
| 14 | BKQC_VEND_CODE | STRING | 10 | — | — |

## ISQCATRN
**ARCHIVED QC BUYOFF**

Fields: 21

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKQC_TRN_ARDTE | DATE | 4 | — | — |
| 2 | BKQC_TRN_BODTE | DATE | 4 | — | — |
| 3 | BKQC_TRN_BQTY | NUMERIC | 8 | 4 | — |
| 4 | BKQC_TRN_BROKEN | STRING | 1 | — | — |
| 5 | BKQC_TRN_CODE | STRING | 15 | — | — |
| 6 | BKQC_TRN_EMPNUM | INTEGER | 2 | — | — |
| 7 | BKQC_TRN_EXTRA | STRING | 100 | — | — |
| 8 | BKQC_TRN_FAULT | STRING | 1 | — | — |
| 9 | BKQC_TRN_FIXQTY | NUMERIC | 8 | 4 | — |
| 10 | BKQC_TRN_FLAG | STRING | 1 | — | — |
| 11 | BKQC_TRN_GQTY | NUMERIC | 8 | 4 | — |
| 12 | BKQC_TRN_INVCD | STRING | 1 | — | — |
| 13 | BKQC_TRN_PO | NUMERIC | 8 | — | — |
| 14 | BKQC_TRN_PODTE | DATE | 4 | — | — |
| 15 | BKQC_TRN_POQTY | NUMERIC | 8 | 4 | — |
| 16 | BKQC_TRN_RECNUM | NUMERIC | 8 | — | — |
| 17 | BKQC_TRN_RECVNM | NUMERIC | 8 | — | — |
| 18 | BKQC_TRN_REWORK | STRING | 2 | — | — |
| 19 | BKQC_TRN_SCRAP | STRING | 2 | — | — |
| 20 | BKQC_TRN_UQTY | NUMERIC | 8 | 4 | — |
| 21 | BKQC_TRN_VEND | STRING | 10 | — | — |

## ISRFQADS
**ARCHIVE RFQ NOTES**

Fields: 5

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BK_DESC_CODE | STRING | 15 | — | not used |
| 2 | BK_DESC_DESC | STRING | 25 | — | not used |
| 3 | BK_DESC_LINE | INTEGER | 2 | — | Notes line number |
| 4 | BK_DESC_NOTES | STRING | 70 | — | Notes - text |
| 5 | BK_DESC_NUM | NUMERIC | 8 | — | PO Number |
