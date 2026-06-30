# ED — EDI: Field Reference

Status: verified-schema

Source: `Evo-DBA_File_Fields 052421.xlsx`, sheet "Fields".
Field descriptions where provided by source; otherwise name-inferred.

---

## BKEDIDUN
**CUSTOMER ID/EDI ENABLEMENT FILE**

Fields: 7

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKEDI_DUN_ADVS | STRING | 1 | — | Advanced Shipping Notice Y/N |
| 2 | BKEDI_DUN_CUST | STRING | 10 | — | Customer Code |
| 3 | BKEDI_DUN_DUNS | STRING | 15 | — | — |
| 4 | BKEDI_DUN_EDI | STRING | 1 | — | EDI Y/N |
| 5 | BKEDI_DUN_EFFDT | DATE | 4 | — | Effective Date |
| 6 | BKEDI_DUN_PRODS | STRING | 1 | — | — |
| 7 | BKEDI_DUN_SHPCD | STRING | 1 | — | USING Ship to Codes Imported Y/N |

## BKEDIH
**TEMPORARY SO HEADERS**

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

## BKEDIL
**TEMPORARY SO LINE ITEMS**

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

## BKEDMSTR
**EDI MASTER SETUP FILE**

Fields: 3

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKEDI_MST_DUNS | STRING | 15 | — | — |
| 2 | BKEDI_MST_NEXTN | NUMERIC | 8 | — | — |
| 3 | BKEDI_MST_PATH | STRING | 66 | — | — |

## BKEDNOTE
**EDI NOTES**

Fields: 3

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKEDI_NOTE_EDI | NUMERIC | 8 | — | — |
| 2 | BKEDI_NOTE_NOTE | STRING | 80 | — | — |
| 3 | BKEDI_NOTE_SO | NUMERIC | 8 | — | — |

## BKEDPOST
**INVOICES SUBJECT TO EDI**

Fields: 2

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKEDI_POST_CUST | STRING | 10 | — | — |
| 2 | BKEDI_POST_INVN | NUMERIC | 8 | — | — |

## ISEDINFO
**EDI SUPPLEMENTAL INFO**

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
