# SO — Sales Orders: Field Reference

Status: verified-schema

Source: `Evo-DBA_File_Fields 052421.xlsx`, sheet "Fields".
Field descriptions where provided by source; otherwise name-inferred.

---

## BKARHINV
**INVOICE HEADER**

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

## BKARHIVL
**INVOICE LINE**

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

## BKARINV
**SALES ORDER HEADER**

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

## BKARINVL
**SALES ORDER LINES**

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

## BKARRDSC
**DBA RECURRING ORDER NOTES**

Fields: 5

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BK_DESC_CODE | STRING | 15 | — | not used |
| 2 | BK_DESC_DESC | STRING | 25 | — | not used |
| 3 | BK_DESC_LINE | INTEGER | 2 | — | Notes line number |
| 4 | BK_DESC_NOTES | STRING | 70 | — | Notes - text |
| 5 | BK_DESC_NUM | NUMERIC | 8 | — | PO Number |

## BKARRINV
**RECURRING ORDER HEADER**

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

## BKARRIVL
**RECURRING ORDER LINE**

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

## BKARTXN
**UNPOSTED LOT ALLOCATION TO ORDER LINES**

Fields: 14

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKAR_TXN_BIN | STRING | 15 | — | — |
| 2 | BKAR_TXN_CODE | STRING | 15 | — | Transaction Code |
| 3 | BKAR_TXN_DATE | DATE | 4 | — | Date |
| 4 | BKAR_TXN_DESC | STRING | 30 | — | Description |
| 5 | BKAR_TXN_EXTRA | STRING | 50 | — | — |
| 6 | BKAR_TXN_LINE | NUMERIC | 8 | — | Line Number |
| 7 | BKAR_TXN_LOC | STRING | 10 | — | — |
| 8 | BKAR_TXN_LOT | STRING | 15 | — | Lot  ID |
| 9 | BKAR_TXN_QTY | NUMERIC | 8 | 2 | Quantity |
| 10 | BKAR_TXN_SERIAL | STRING | 25 | — | Serial ID |
| 11 | BKAR_TXN_SONUM | NUMERIC | 8 | — | SO Number |
| 12 | BKAR_TXN_SRNUM | NUMERIC | 8 | — | — |
| 13 | BKAR_TXN_STOCK | STRING | 15 | — | — |
| 14 | BKAR_TXN_TMPSO | STRING | 40 | — | — |

## BKARTXNS
**UNPOSTED SERIAL ALLOCATION TO ORDER LINES**

Fields: 14

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKAR_TXN_BIN | STRING | 15 | — | — |
| 2 | BKAR_TXN_CODE | STRING | 15 | — | Transaction Code |
| 3 | BKAR_TXN_DATE | DATE | 4 | — | Date |
| 4 | BKAR_TXN_DESC | STRING | 30 | — | Description |
| 5 | BKAR_TXN_EXTRA | STRING | 50 | — | — |
| 6 | BKAR_TXN_LINE | NUMERIC | 8 | — | Line Number |
| 7 | BKAR_TXN_LOC | STRING | 10 | — | — |
| 8 | BKAR_TXN_LOT | STRING | 15 | — | Lot  ID |
| 9 | BKAR_TXN_QTY | NUMERIC | 8 | 2 | Quantity |
| 10 | BKAR_TXN_SERIAL | STRING | 25 | — | Serial ID |
| 11 | BKAR_TXN_SONUM | NUMERIC | 8 | — | SO Number |
| 12 | BKAR_TXN_SRNUM | NUMERIC | 8 | — | — |
| 13 | BKAR_TXN_STOCK | STRING | 15 | — | — |
| 14 | BKAR_TXN_TMPSO | STRING | 40 | — | — |

## BKESTQT
**SALES QUOTATION HEADER**

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

## BKESTQTL
**SALES QUOTATION LINE ITEMS**

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

## BKICAPMA
**ARCHIVE PRICE CODE**

Fields: 85

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKIC_PMAT_ACCRU | NUMERIC | 8 | 2 | — |
| 2 | BKIC_PMAT_BILLB | NUMERIC | 8 | 2 | — |
| 3 | BKIC_PMAT_CLASS | STRING | 4 | — | — |
| 4 | BKIC_PMAT_COMM1_1 | NUMERIC | 8 | 4 | — |
| 5 | BKIC_PMAT_COMM1_10 | NUMERIC | 8 | 4 | — |
| 6 | BKIC_PMAT_COMM1_2 | NUMERIC | 8 | 4 | — |
| 7 | BKIC_PMAT_COMM1_3 | NUMERIC | 8 | 4 | — |
| 8 | BKIC_PMAT_COMM1_4 | NUMERIC | 8 | 4 | — |
| 9 | BKIC_PMAT_COMM1_5 | NUMERIC | 8 | 4 | — |
| 10 | BKIC_PMAT_COMM1_6 | NUMERIC | 8 | 4 | — |
| 11 | BKIC_PMAT_COMM1_7 | NUMERIC | 8 | 4 | — |
| 12 | BKIC_PMAT_COMM1_8 | NUMERIC | 8 | 4 | — |
| 13 | BKIC_PMAT_COMM1_9 | NUMERIC | 8 | 4 | — |
| 14 | BKIC_PMAT_COMM2_1 | NUMERIC | 8 | 4 | — |
| 15 | BKIC_PMAT_COMM2_10 | NUMERIC | 8 | 4 | — |
| 16 | BKIC_PMAT_COMM2_2 | NUMERIC | 8 | 4 | — |
| 17 | BKIC_PMAT_COMM2_3 | NUMERIC | 8 | 4 | — |
| 18 | BKIC_PMAT_COMM2_4 | NUMERIC | 8 | 4 | — |
| 19 | BKIC_PMAT_COMM2_5 | NUMERIC | 8 | 4 | — |
| 20 | BKIC_PMAT_COMM2_6 | NUMERIC | 8 | 4 | — |
| 21 | BKIC_PMAT_COMM2_7 | NUMERIC | 8 | 4 | — |
| 22 | BKIC_PMAT_COMM2_8 | NUMERIC | 8 | 4 | — |
| 23 | BKIC_PMAT_COMM2_9 | NUMERIC | 8 | 4 | — |
| 24 | BKIC_PMAT_CUST | STRING | 10 | — | Customer Code |
| 25 | BKIC_PMAT_DCODE | STRING | 10 | — | — |
| 26 | BKIC_PMAT_EDATE | DATE | 4 | — | — |
| 27 | BKIC_PMAT_EXP | DATE | 4 | — | Expiration Date |
| 28 | BKIC_PMAT_EXTRA | STRING | 50 | — | — |
| 29 | BKIC_PMAT_FRTAL | NUMERIC | 8 | 2 | — |
| 30 | BKIC_PMAT_ISRET_1 | NUMERIC | 8 | 4 | — |
| 31 | BKIC_PMAT_ISRET_10 | NUMERIC | 8 | 4 | — |
| 32 | BKIC_PMAT_ISRET_2 | NUMERIC | 8 | 4 | — |
| 33 | BKIC_PMAT_ISRET_3 | NUMERIC | 8 | 4 | — |
| 34 | BKIC_PMAT_ISRET_4 | NUMERIC | 8 | 4 | — |
| 35 | BKIC_PMAT_ISRET_5 | NUMERIC | 8 | 4 | — |
| 36 | BKIC_PMAT_ISRET_6 | NUMERIC | 8 | 4 | — |
| 37 | BKIC_PMAT_ISRET_7 | NUMERIC | 8 | 4 | — |
| 38 | BKIC_PMAT_ISRET_8 | NUMERIC | 8 | 4 | — |
| 39 | BKIC_PMAT_ISRET_9 | NUMERIC | 8 | 4 | — |
| 40 | BKIC_PMAT_LUMP | NUMERIC | 8 | 2 | — |
| 41 | BKIC_PMAT_METH | STRING | 11 | — | — |
| 42 | BKIC_PMAT_MIN | NUMERIC | 8 | 2 | — |
| 43 | BKIC_PMAT_MINPR | NUMERIC | 8 | 4 | — |
| 44 | BKIC_PMAT_OFFCH | NUMERIC | 8 | 2 | — |
| 45 | BKIC_PMAT_OFFIN | NUMERIC | 8 | 2 | — |
| 46 | BKIC_PMAT_PCODE | STRING | 15 | — | Item Number |
| 47 | BKIC_PMAT_PDESC | STRING | 30 | — | — |
| 48 | BKIC_PMAT_PER_1 | NUMERIC | 8 | 4 | — |
| 49 | BKIC_PMAT_PER_10 | NUMERIC | 8 | 4 | — |
| 50 | BKIC_PMAT_PER_2 | NUMERIC | 8 | 4 | — |
| 51 | BKIC_PMAT_PER_3 | NUMERIC | 8 | 4 | — |
| 52 | BKIC_PMAT_PER_4 | NUMERIC | 8 | 4 | — |
| 53 | BKIC_PMAT_PER_5 | NUMERIC | 8 | 4 | — |
| 54 | BKIC_PMAT_PER_6 | NUMERIC | 8 | 4 | — |
| 55 | BKIC_PMAT_PER_7 | NUMERIC | 8 | 4 | — |
| 56 | BKIC_PMAT_PER_8 | NUMERIC | 8 | 4 | — |
| 57 | BKIC_PMAT_PER_9 | NUMERIC | 8 | 4 | — |
| 58 | BKIC_PMAT_PFLAG | STRING | 1 | — | — |
| 59 | BKIC_PMAT_PNUM | INTEGER | 2 | — | Quantity |
| 60 | BKIC_PMAT_PROMO | NUMERIC | 8 | 2 | — |
| 61 | BKIC_PMAT_QTY_1 | NUMERIC | 8 | 2 | — |
| 62 | BKIC_PMAT_QTY_10 | NUMERIC | 8 | 2 | — |
| 63 | BKIC_PMAT_QTY_2 | NUMERIC | 8 | 2 | — |
| 64 | BKIC_PMAT_QTY_3 | NUMERIC | 8 | 2 | — |
| 65 | BKIC_PMAT_QTY_4 | NUMERIC | 8 | 2 | — |
| 66 | BKIC_PMAT_QTY_5 | NUMERIC | 8 | 2 | — |
| 67 | BKIC_PMAT_QTY_6 | NUMERIC | 8 | 2 | — |
| 68 | BKIC_PMAT_QTY_7 | NUMERIC | 8 | 2 | — |
| 69 | BKIC_PMAT_QTY_8 | NUMERIC | 8 | 2 | — |
| 70 | BKIC_PMAT_QTY_9 | NUMERIC | 8 | 2 | — |
| 71 | BKIC_PMAT_RATE_1 | NUMERIC | 8 | 4 | — |
| 72 | BKIC_PMAT_RATE_10 | NUMERIC | 8 | 4 | — |
| 73 | BKIC_PMAT_RATE_2 | NUMERIC | 8 | 4 | — |
| 74 | BKIC_PMAT_RATE_3 | NUMERIC | 8 | 4 | — |
| 75 | BKIC_PMAT_RATE_4 | NUMERIC | 8 | 4 | — |
| 76 | BKIC_PMAT_RATE_5 | NUMERIC | 8 | 4 | — |
| 77 | BKIC_PMAT_RATE_6 | NUMERIC | 8 | 4 | — |
| 78 | BKIC_PMAT_RATE_7 | NUMERIC | 8 | 4 | — |
| 79 | BKIC_PMAT_RATE_8 | NUMERIC | 8 | 4 | — |
| 80 | BKIC_PMAT_RATE_9 | NUMERIC | 8 | 4 | — |
| 81 | BKIC_PMAT_SCAND | NUMERIC | 8 | 2 | — |
| 82 | BKIC_PMAT_SDATE | DATE | 4 | — | — |
| 83 | BKIC_PMAT_SRTS | NUMERIC | 8 | 2 | — |
| 84 | BKIC_PMAT_SWELL | NUMERIC | 8 | 2 | — |
| 85 | BKIC_PMAT_UID | STRING | 40 | — | — |

## BKICPMAT
**PRICE MATRIX**

Fields: 85

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKIC_PMAT_ACCRU | NUMERIC | 8 | 2 | — |
| 2 | BKIC_PMAT_BILLB | NUMERIC | 8 | 2 | — |
| 3 | BKIC_PMAT_CLASS | STRING | 4 | — | — |
| 4 | BKIC_PMAT_COMM1_1 | NUMERIC | 8 | 4 | — |
| 5 | BKIC_PMAT_COMM1_10 | NUMERIC | 8 | 4 | — |
| 6 | BKIC_PMAT_COMM1_2 | NUMERIC | 8 | 4 | — |
| 7 | BKIC_PMAT_COMM1_3 | NUMERIC | 8 | 4 | — |
| 8 | BKIC_PMAT_COMM1_4 | NUMERIC | 8 | 4 | — |
| 9 | BKIC_PMAT_COMM1_5 | NUMERIC | 8 | 4 | — |
| 10 | BKIC_PMAT_COMM1_6 | NUMERIC | 8 | 4 | — |
| 11 | BKIC_PMAT_COMM1_7 | NUMERIC | 8 | 4 | — |
| 12 | BKIC_PMAT_COMM1_8 | NUMERIC | 8 | 4 | — |
| 13 | BKIC_PMAT_COMM1_9 | NUMERIC | 8 | 4 | — |
| 14 | BKIC_PMAT_COMM2_1 | NUMERIC | 8 | 4 | — |
| 15 | BKIC_PMAT_COMM2_10 | NUMERIC | 8 | 4 | — |
| 16 | BKIC_PMAT_COMM2_2 | NUMERIC | 8 | 4 | — |
| 17 | BKIC_PMAT_COMM2_3 | NUMERIC | 8 | 4 | — |
| 18 | BKIC_PMAT_COMM2_4 | NUMERIC | 8 | 4 | — |
| 19 | BKIC_PMAT_COMM2_5 | NUMERIC | 8 | 4 | — |
| 20 | BKIC_PMAT_COMM2_6 | NUMERIC | 8 | 4 | — |
| 21 | BKIC_PMAT_COMM2_7 | NUMERIC | 8 | 4 | — |
| 22 | BKIC_PMAT_COMM2_8 | NUMERIC | 8 | 4 | — |
| 23 | BKIC_PMAT_COMM2_9 | NUMERIC | 8 | 4 | — |
| 24 | BKIC_PMAT_CUST | STRING | 10 | — | Customer Code |
| 25 | BKIC_PMAT_DCODE | STRING | 10 | — | — |
| 26 | BKIC_PMAT_EDATE | DATE | 4 | — | — |
| 27 | BKIC_PMAT_EXP | DATE | 4 | — | Expiration Date |
| 28 | BKIC_PMAT_EXTRA | STRING | 50 | — | — |
| 29 | BKIC_PMAT_FRTAL | NUMERIC | 8 | 2 | — |
| 30 | BKIC_PMAT_ISRET_1 | NUMERIC | 8 | 4 | — |
| 31 | BKIC_PMAT_ISRET_10 | NUMERIC | 8 | 4 | — |
| 32 | BKIC_PMAT_ISRET_2 | NUMERIC | 8 | 4 | — |
| 33 | BKIC_PMAT_ISRET_3 | NUMERIC | 8 | 4 | — |
| 34 | BKIC_PMAT_ISRET_4 | NUMERIC | 8 | 4 | — |
| 35 | BKIC_PMAT_ISRET_5 | NUMERIC | 8 | 4 | — |
| 36 | BKIC_PMAT_ISRET_6 | NUMERIC | 8 | 4 | — |
| 37 | BKIC_PMAT_ISRET_7 | NUMERIC | 8 | 4 | — |
| 38 | BKIC_PMAT_ISRET_8 | NUMERIC | 8 | 4 | — |
| 39 | BKIC_PMAT_ISRET_9 | NUMERIC | 8 | 4 | — |
| 40 | BKIC_PMAT_LUMP | NUMERIC | 8 | 2 | — |
| 41 | BKIC_PMAT_METH | STRING | 11 | — | — |
| 42 | BKIC_PMAT_MIN | NUMERIC | 8 | 2 | — |
| 43 | BKIC_PMAT_MINPR | NUMERIC | 8 | 4 | — |
| 44 | BKIC_PMAT_OFFCH | NUMERIC | 8 | 2 | — |
| 45 | BKIC_PMAT_OFFIN | NUMERIC | 8 | 2 | — |
| 46 | BKIC_PMAT_PCODE | STRING | 15 | — | Item Number |
| 47 | BKIC_PMAT_PDESC | STRING | 30 | — | — |
| 48 | BKIC_PMAT_PER_1 | NUMERIC | 8 | 4 | — |
| 49 | BKIC_PMAT_PER_10 | NUMERIC | 8 | 4 | — |
| 50 | BKIC_PMAT_PER_2 | NUMERIC | 8 | 4 | — |
| 51 | BKIC_PMAT_PER_3 | NUMERIC | 8 | 4 | — |
| 52 | BKIC_PMAT_PER_4 | NUMERIC | 8 | 4 | — |
| 53 | BKIC_PMAT_PER_5 | NUMERIC | 8 | 4 | — |
| 54 | BKIC_PMAT_PER_6 | NUMERIC | 8 | 4 | — |
| 55 | BKIC_PMAT_PER_7 | NUMERIC | 8 | 4 | — |
| 56 | BKIC_PMAT_PER_8 | NUMERIC | 8 | 4 | — |
| 57 | BKIC_PMAT_PER_9 | NUMERIC | 8 | 4 | — |
| 58 | BKIC_PMAT_PFLAG | STRING | 1 | — | — |
| 59 | BKIC_PMAT_PNUM | INTEGER | 2 | — | Quantity |
| 60 | BKIC_PMAT_PROMO | NUMERIC | 8 | 2 | — |
| 61 | BKIC_PMAT_QTY_1 | NUMERIC | 8 | 2 | — |
| 62 | BKIC_PMAT_QTY_10 | NUMERIC | 8 | 2 | — |
| 63 | BKIC_PMAT_QTY_2 | NUMERIC | 8 | 2 | — |
| 64 | BKIC_PMAT_QTY_3 | NUMERIC | 8 | 2 | — |
| 65 | BKIC_PMAT_QTY_4 | NUMERIC | 8 | 2 | — |
| 66 | BKIC_PMAT_QTY_5 | NUMERIC | 8 | 2 | — |
| 67 | BKIC_PMAT_QTY_6 | NUMERIC | 8 | 2 | — |
| 68 | BKIC_PMAT_QTY_7 | NUMERIC | 8 | 2 | — |
| 69 | BKIC_PMAT_QTY_8 | NUMERIC | 8 | 2 | — |
| 70 | BKIC_PMAT_QTY_9 | NUMERIC | 8 | 2 | — |
| 71 | BKIC_PMAT_RATE_1 | NUMERIC | 8 | 4 | — |
| 72 | BKIC_PMAT_RATE_10 | NUMERIC | 8 | 4 | — |
| 73 | BKIC_PMAT_RATE_2 | NUMERIC | 8 | 4 | — |
| 74 | BKIC_PMAT_RATE_3 | NUMERIC | 8 | 4 | — |
| 75 | BKIC_PMAT_RATE_4 | NUMERIC | 8 | 4 | — |
| 76 | BKIC_PMAT_RATE_5 | NUMERIC | 8 | 4 | — |
| 77 | BKIC_PMAT_RATE_6 | NUMERIC | 8 | 4 | — |
| 78 | BKIC_PMAT_RATE_7 | NUMERIC | 8 | 4 | — |
| 79 | BKIC_PMAT_RATE_8 | NUMERIC | 8 | 4 | — |
| 80 | BKIC_PMAT_RATE_9 | NUMERIC | 8 | 4 | — |
| 81 | BKIC_PMAT_SCAND | NUMERIC | 8 | 2 | — |
| 82 | BKIC_PMAT_SDATE | DATE | 4 | — | — |
| 83 | BKIC_PMAT_SRTS | NUMERIC | 8 | 2 | — |
| 84 | BKIC_PMAT_SWELL | NUMERIC | 8 | 2 | — |
| 85 | BKIC_PMAT_UID | STRING | 40 | — | — |

## BKQTNOTE
**DBA QUOTE NOTES**

Fields: 5

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BK_DESC_CODE | STRING | 15 | — | not used |
| 2 | BK_DESC_DESC | STRING | 25 | — | not used |
| 3 | BK_DESC_LINE | INTEGER | 2 | — | Notes line number |
| 4 | BK_DESC_NOTES | STRING | 70 | — | Notes - text |
| 5 | BK_DESC_NUM | NUMERIC | 8 | — | PO Number |

## BKSAREPT
**REPORT NAMES FOR SA-M & SA-N**

Fields: 57

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKSA_BASE | STRING | 1 | — | — |
| 2 | BKSA_FROM1 | NUMERIC | 8 | — | — |
| 3 | BKSA_FROM10 | STRING | 10 | — | — |
| 4 | BKSA_FROM11 | STRING | 30 | — | — |
| 5 | BKSA_FROM12 | STRING | 30 | — | — |
| 6 | BKSA_FROM13 | STRING | 4 | — | — |
| 7 | BKSA_FROM14 | STRING | 4 | — | — |
| 8 | BKSA_FROM15 | INTEGER | 2 | — | — |
| 9 | BKSA_FROM16 | INTEGER | 2 | — | — |
| 10 | BKSA_FROM17 | STRING | 10 | — | — |
| 11 | BKSA_FROM18 | STRING | 15 | — | — |
| 12 | BKSA_FROM19 | STRING | 25 | — | — |
| 13 | BKSA_FROM2 | DATE | 4 | — | — |
| 14 | BKSA_FROM20 | NUMERIC | 8 | 2 | — |
| 15 | BKSA_FROM21 | STRING | 15 | — | — |
| 16 | BKSA_FROM22 | STRING | 4 | — | — |
| 17 | BKSA_FROM23 | DATE | 4 | — | — |
| 18 | BKSA_FROM24 | NUMERIC | 8 | 2 | — |
| 19 | BKSA_FROM25 | NUMERIC | 8 | 2 | — |
| 20 | BKSA_FROM26 | STRING | 3 | — | — |
| 21 | BKSA_FROM3 | DATE | 4 | — | — |
| 22 | BKSA_FROM4 | NUMERIC | 8 | — | — |
| 23 | BKSA_FROM5 | STRING | 10 | — | — |
| 24 | BKSA_FROM6 | STRING | 10 | — | — |
| 25 | BKSA_FROM7 | STRING | 2 | — | — |
| 26 | BKSA_FROM8 | STRING | 2 | — | — |
| 27 | BKSA_FROM9 | STRING | 10 | — | — |
| 28 | BKSA_NAME | STRING | 15 | — | — |
| 29 | BKSA_RTM | STRING | 15 | — | — |
| 30 | BKSA_THRU1 | NUMERIC | 8 | — | — |
| 31 | BKSA_THRU10 | STRING | 10 | — | — |
| 32 | BKSA_THRU11 | STRING | 30 | — | — |
| 33 | BKSA_THRU12 | STRING | 30 | — | — |
| 34 | BKSA_THRU13 | STRING | 4 | — | — |
| 35 | BKSA_THRU14 | STRING | 4 | — | — |
| 36 | BKSA_THRU15 | INTEGER | 2 | — | — |
| 37 | BKSA_THRU16 | INTEGER | 2 | — | — |
| 38 | BKSA_THRU17 | STRING | 10 | — | — |
| 39 | BKSA_THRU18 | STRING | 15 | — | — |
| 40 | BKSA_THRU19 | STRING | 25 | — | — |
| 41 | BKSA_THRU2 | DATE | 4 | — | — |
| 42 | BKSA_THRU20 | NUMERIC | 8 | 2 | — |
| 43 | BKSA_THRU21 | STRING | 15 | — | — |
| 44 | BKSA_THRU22 | STRING | 4 | — | — |
| 45 | BKSA_THRU23 | DATE | 4 | — | — |
| 46 | BKSA_THRU24 | NUMERIC | 8 | 2 | — |
| 47 | BKSA_THRU25 | NUMERIC | 8 | 2 | — |
| 48 | BKSA_THRU26 | STRING | 3 | — | — |
| 49 | BKSA_THRU3 | DATE | 4 | — | — |
| 50 | BKSA_THRU4 | NUMERIC | 8 | — | — |
| 51 | BKSA_THRU5 | STRING | 10 | — | — |
| 52 | BKSA_THRU6 | STRING | 10 | — | — |
| 53 | BKSA_THRU7 | STRING | 2 | — | — |
| 54 | BKSA_THRU8 | STRING | 2 | — | — |
| 55 | BKSA_THRU9 | STRING | 10 | — | — |
| 56 | BKSA_TITLE | STRING | 40 | — | — |
| 57 | BKSA_TYPE | STRING | 8 | — | — |

## BKSOHLOT
**INVOICE LOT CONTROL**

Fields: 14

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKAR_TXN_BIN | STRING | 15 | — | — |
| 2 | BKAR_TXN_CODE | STRING | 15 | — | Transaction Code |
| 3 | BKAR_TXN_DATE | DATE | 4 | — | Date |
| 4 | BKAR_TXN_DESC | STRING | 30 | — | Description |
| 5 | BKAR_TXN_EXTRA | STRING | 50 | — | — |
| 6 | BKAR_TXN_LINE | NUMERIC | 8 | — | Line Number |
| 7 | BKAR_TXN_LOC | STRING | 10 | — | — |
| 8 | BKAR_TXN_LOT | STRING | 15 | — | Lot  ID |
| 9 | BKAR_TXN_QTY | NUMERIC | 8 | 2 | Quantity |
| 10 | BKAR_TXN_SERIAL | STRING | 25 | — | Serial ID |
| 11 | BKAR_TXN_SONUM | NUMERIC | 8 | — | SO Number |
| 12 | BKAR_TXN_SRNUM | NUMERIC | 8 | — | — |
| 13 | BKAR_TXN_STOCK | STRING | 15 | — | — |
| 14 | BKAR_TXN_TMPSO | STRING | 40 | — | — |

## BKSOHSER
**INVOICE SERIAL CONTROL**

Fields: 14

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKAR_TXN_BIN | STRING | 15 | — | — |
| 2 | BKAR_TXN_CODE | STRING | 15 | — | Transaction Code |
| 3 | BKAR_TXN_DATE | DATE | 4 | — | Date |
| 4 | BKAR_TXN_DESC | STRING | 30 | — | Description |
| 5 | BKAR_TXN_EXTRA | STRING | 50 | — | — |
| 6 | BKAR_TXN_LINE | NUMERIC | 8 | — | Line Number |
| 7 | BKAR_TXN_LOC | STRING | 10 | — | — |
| 8 | BKAR_TXN_LOT | STRING | 15 | — | Lot  ID |
| 9 | BKAR_TXN_QTY | NUMERIC | 8 | 2 | Quantity |
| 10 | BKAR_TXN_SERIAL | STRING | 25 | — | Serial ID |
| 11 | BKAR_TXN_SONUM | NUMERIC | 8 | — | SO Number |
| 12 | BKAR_TXN_SRNUM | NUMERIC | 8 | — | — |
| 13 | BKAR_TXN_STOCK | STRING | 15 | — | — |
| 14 | BKAR_TXN_TMPSO | STRING | 40 | — | — |

## BKSOLOCK
**LOCK FILE FOR SO INVOICE POSTING**

Fields: 5

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKSO_LOCK_DATE | DATE | 4 | — | — |
| 2 | BKSO_LOCK_ITEM | STRING | 25 | — | — |
| 3 | BKSO_LOCK_REC | STRING | 10 | — | — |
| 4 | BKSO_LOCK_TIME | TIME | 4 | — | — |
| 5 | BKSO_LOCK_WHO | STRING | 25 | — | — |

## BKSONOTE
**SALES ORDER ASSIGNED TEMPLATES**

Fields: 5

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BK_DESC_CODE | STRING | 15 | — | not used |
| 2 | BK_DESC_DESC | STRING | 25 | — | not used |
| 3 | BK_DESC_LINE | INTEGER | 2 | — | Notes line number |
| 4 | BK_DESC_NOTES | STRING | 70 | — | Notes - text |
| 5 | BK_DESC_NUM | NUMERIC | 8 | — | PO Number |

## BKSOX
**SO DETAIL  - ACCOUNTING DISABLED**

Fields: 25

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKSOX_ARCHDATE | DATE | 4 | — | — |
| 2 | BKSOX_COMPANY | STRING | 2 | — | — |
| 3 | BKSOX_CURRENCY | STRING | 3 | — | — |
| 4 | BKSOX_CUSTCODE | STRING | 10 | — | — |
| 5 | BKSOX_CUSTNAME | STRING | 30 | — | — |
| 6 | BKSOX_CUSTPO | STRING | 25 | — | — |
| 7 | BKSOX_DEPOSIT | NUMERIC | 8 | 2 | — |
| 8 | BKSOX_ENTDATE | DATE | 4 | — | — |
| 9 | BKSOX_FREIGHT | NUMERIC | 8 | 2 | — |
| 10 | BKSOX_INVCDATE | DATE | 4 | — | — |
| 11 | BKSOX_INVCDESC | STRING | 30 | — | — |
| 12 | BKSOX_INVCNUM | NUMERIC | 8 | — | — |
| 13 | BKSOX_JOBNUM | STRING | 15 | — | — |
| 14 | BKSOX_POSTDATE | DATE | 4 | — | — |
| 15 | BKSOX_RETEN | NUMERIC | 8 | 2 | — |
| 16 | BKSOX_SHIPDATE | DATE | 4 | — | — |
| 17 | BKSOX_SHIPPER | NUMERIC | 8 | — | — |
| 18 | BKSOX_SONUM | NUMERIC | 8 | — | — |
| 19 | BKSOX_SUBTOT | NUMERIC | 8 | 2 | — |
| 20 | BKSOX_TAXAMT | NUMERIC | 8 | 2 | — |
| 21 | BKSOX_TAXCODE | STRING | 10 | — | — |
| 22 | BKSOX_TAXNAME | STRING | 30 | — | — |
| 23 | BKSOX_TERMSCODE | INTEGER | 2 | — | — |
| 24 | BKSOX_TERMSDESC | STRING | 20 | — | — |
| 25 | BKSOX_TOTAL | NUMERIC | 8 | 2 | — |

## BKSOXH
**SO DETAIL  - ACCOUNTING DISABLED**

Fields: 25

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKSOX_ARCHDATE | DATE | 4 | — | — |
| 2 | BKSOX_COMPANY | STRING | 2 | — | — |
| 3 | BKSOX_CURRENCY | STRING | 3 | — | — |
| 4 | BKSOX_CUSTCODE | STRING | 10 | — | — |
| 5 | BKSOX_CUSTNAME | STRING | 30 | — | — |
| 6 | BKSOX_CUSTPO | STRING | 25 | — | — |
| 7 | BKSOX_DEPOSIT | NUMERIC | 8 | 2 | — |
| 8 | BKSOX_ENTDATE | DATE | 4 | — | — |
| 9 | BKSOX_FREIGHT | NUMERIC | 8 | 2 | — |
| 10 | BKSOX_INVCDATE | DATE | 4 | — | — |
| 11 | BKSOX_INVCDESC | STRING | 30 | — | — |
| 12 | BKSOX_INVCNUM | NUMERIC | 8 | — | — |
| 13 | BKSOX_JOBNUM | STRING | 15 | — | — |
| 14 | BKSOX_POSTDATE | DATE | 4 | — | — |
| 15 | BKSOX_RETEN | NUMERIC | 8 | 2 | — |
| 16 | BKSOX_SHIPDATE | DATE | 4 | — | — |
| 17 | BKSOX_SHIPPER | NUMERIC | 8 | — | — |
| 18 | BKSOX_SONUM | NUMERIC | 8 | — | — |
| 19 | BKSOX_SUBTOT | NUMERIC | 8 | 2 | — |
| 20 | BKSOX_TAXAMT | NUMERIC | 8 | 2 | — |
| 21 | BKSOX_TAXCODE | STRING | 10 | — | — |
| 22 | BKSOX_TAXNAME | STRING | 30 | — | — |
| 23 | BKSOX_TERMSCODE | INTEGER | 2 | — | — |
| 24 | BKSOX_TERMSDESC | STRING | 20 | — | — |
| 25 | BKSOX_TOTAL | NUMERIC | 8 | 2 | — |

## DISCOUNT
**DISCOUNT TABLE MASTER**

Fields: 85

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKIC_PMAT_ACCRU | NUMERIC | 8 | 2 | — |
| 2 | BKIC_PMAT_BILLB | NUMERIC | 8 | 2 | — |
| 3 | BKIC_PMAT_CLASS | STRING | 4 | — | — |
| 4 | BKIC_PMAT_COMM1_1 | NUMERIC | 8 | 4 | — |
| 5 | BKIC_PMAT_COMM1_10 | NUMERIC | 8 | 4 | — |
| 6 | BKIC_PMAT_COMM1_2 | NUMERIC | 8 | 4 | — |
| 7 | BKIC_PMAT_COMM1_3 | NUMERIC | 8 | 4 | — |
| 8 | BKIC_PMAT_COMM1_4 | NUMERIC | 8 | 4 | — |
| 9 | BKIC_PMAT_COMM1_5 | NUMERIC | 8 | 4 | — |
| 10 | BKIC_PMAT_COMM1_6 | NUMERIC | 8 | 4 | — |
| 11 | BKIC_PMAT_COMM1_7 | NUMERIC | 8 | 4 | — |
| 12 | BKIC_PMAT_COMM1_8 | NUMERIC | 8 | 4 | — |
| 13 | BKIC_PMAT_COMM1_9 | NUMERIC | 8 | 4 | — |
| 14 | BKIC_PMAT_COMM2_1 | NUMERIC | 8 | 4 | — |
| 15 | BKIC_PMAT_COMM2_10 | NUMERIC | 8 | 4 | — |
| 16 | BKIC_PMAT_COMM2_2 | NUMERIC | 8 | 4 | — |
| 17 | BKIC_PMAT_COMM2_3 | NUMERIC | 8 | 4 | — |
| 18 | BKIC_PMAT_COMM2_4 | NUMERIC | 8 | 4 | — |
| 19 | BKIC_PMAT_COMM2_5 | NUMERIC | 8 | 4 | — |
| 20 | BKIC_PMAT_COMM2_6 | NUMERIC | 8 | 4 | — |
| 21 | BKIC_PMAT_COMM2_7 | NUMERIC | 8 | 4 | — |
| 22 | BKIC_PMAT_COMM2_8 | NUMERIC | 8 | 4 | — |
| 23 | BKIC_PMAT_COMM2_9 | NUMERIC | 8 | 4 | — |
| 24 | BKIC_PMAT_CUST | STRING | 10 | — | Customer Code |
| 25 | BKIC_PMAT_DCODE | STRING | 10 | — | — |
| 26 | BKIC_PMAT_EDATE | DATE | 4 | — | — |
| 27 | BKIC_PMAT_EXP | DATE | 4 | — | Expiration Date |
| 28 | BKIC_PMAT_EXTRA | STRING | 50 | — | — |
| 29 | BKIC_PMAT_FRTAL | NUMERIC | 8 | 2 | — |
| 30 | BKIC_PMAT_ISRET_1 | NUMERIC | 8 | 4 | — |
| 31 | BKIC_PMAT_ISRET_10 | NUMERIC | 8 | 4 | — |
| 32 | BKIC_PMAT_ISRET_2 | NUMERIC | 8 | 4 | — |
| 33 | BKIC_PMAT_ISRET_3 | NUMERIC | 8 | 4 | — |
| 34 | BKIC_PMAT_ISRET_4 | NUMERIC | 8 | 4 | — |
| 35 | BKIC_PMAT_ISRET_5 | NUMERIC | 8 | 4 | — |
| 36 | BKIC_PMAT_ISRET_6 | NUMERIC | 8 | 4 | — |
| 37 | BKIC_PMAT_ISRET_7 | NUMERIC | 8 | 4 | — |
| 38 | BKIC_PMAT_ISRET_8 | NUMERIC | 8 | 4 | — |
| 39 | BKIC_PMAT_ISRET_9 | NUMERIC | 8 | 4 | — |
| 40 | BKIC_PMAT_LUMP | NUMERIC | 8 | 2 | — |
| 41 | BKIC_PMAT_METH | STRING | 11 | — | — |
| 42 | BKIC_PMAT_MIN | NUMERIC | 8 | 2 | — |
| 43 | BKIC_PMAT_MINPR | NUMERIC | 8 | 4 | — |
| 44 | BKIC_PMAT_OFFCH | NUMERIC | 8 | 2 | — |
| 45 | BKIC_PMAT_OFFIN | NUMERIC | 8 | 2 | — |
| 46 | BKIC_PMAT_PCODE | STRING | 15 | — | Item Number |
| 47 | BKIC_PMAT_PDESC | STRING | 30 | — | — |
| 48 | BKIC_PMAT_PER_1 | NUMERIC | 8 | 4 | — |
| 49 | BKIC_PMAT_PER_10 | NUMERIC | 8 | 4 | — |
| 50 | BKIC_PMAT_PER_2 | NUMERIC | 8 | 4 | — |
| 51 | BKIC_PMAT_PER_3 | NUMERIC | 8 | 4 | — |
| 52 | BKIC_PMAT_PER_4 | NUMERIC | 8 | 4 | — |
| 53 | BKIC_PMAT_PER_5 | NUMERIC | 8 | 4 | — |
| 54 | BKIC_PMAT_PER_6 | NUMERIC | 8 | 4 | — |
| 55 | BKIC_PMAT_PER_7 | NUMERIC | 8 | 4 | — |
| 56 | BKIC_PMAT_PER_8 | NUMERIC | 8 | 4 | — |
| 57 | BKIC_PMAT_PER_9 | NUMERIC | 8 | 4 | — |
| 58 | BKIC_PMAT_PFLAG | STRING | 1 | — | — |
| 59 | BKIC_PMAT_PNUM | INTEGER | 2 | — | Quantity |
| 60 | BKIC_PMAT_PROMO | NUMERIC | 8 | 2 | — |
| 61 | BKIC_PMAT_QTY_1 | NUMERIC | 8 | 2 | — |
| 62 | BKIC_PMAT_QTY_10 | NUMERIC | 8 | 2 | — |
| 63 | BKIC_PMAT_QTY_2 | NUMERIC | 8 | 2 | — |
| 64 | BKIC_PMAT_QTY_3 | NUMERIC | 8 | 2 | — |
| 65 | BKIC_PMAT_QTY_4 | NUMERIC | 8 | 2 | — |
| 66 | BKIC_PMAT_QTY_5 | NUMERIC | 8 | 2 | — |
| 67 | BKIC_PMAT_QTY_6 | NUMERIC | 8 | 2 | — |
| 68 | BKIC_PMAT_QTY_7 | NUMERIC | 8 | 2 | — |
| 69 | BKIC_PMAT_QTY_8 | NUMERIC | 8 | 2 | — |
| 70 | BKIC_PMAT_QTY_9 | NUMERIC | 8 | 2 | — |
| 71 | BKIC_PMAT_RATE_1 | NUMERIC | 8 | 4 | — |
| 72 | BKIC_PMAT_RATE_10 | NUMERIC | 8 | 4 | — |
| 73 | BKIC_PMAT_RATE_2 | NUMERIC | 8 | 4 | — |
| 74 | BKIC_PMAT_RATE_3 | NUMERIC | 8 | 4 | — |
| 75 | BKIC_PMAT_RATE_4 | NUMERIC | 8 | 4 | — |
| 76 | BKIC_PMAT_RATE_5 | NUMERIC | 8 | 4 | — |
| 77 | BKIC_PMAT_RATE_6 | NUMERIC | 8 | 4 | — |
| 78 | BKIC_PMAT_RATE_7 | NUMERIC | 8 | 4 | — |
| 79 | BKIC_PMAT_RATE_8 | NUMERIC | 8 | 4 | — |
| 80 | BKIC_PMAT_RATE_9 | NUMERIC | 8 | 4 | — |
| 81 | BKIC_PMAT_SCAND | NUMERIC | 8 | 2 | — |
| 82 | BKIC_PMAT_SDATE | DATE | 4 | — | — |
| 83 | BKIC_PMAT_SRTS | NUMERIC | 8 | 2 | — |
| 84 | BKIC_PMAT_SWELL | NUMERIC | 8 | 2 | — |
| 85 | BKIC_PMAT_UID | STRING | 40 | — | — |

## INVETXN
**TEMP FILE FOR UNPOSTED INVENTORY TRANSACTIONS**

Fields: 24

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MTIT_AVGCOST | NUMERIC | 8 | 4 | — |
| 2 | MTIT_CLASS | STRING | 4 | — | — |
| 3 | MTIT_CODE | STRING | 15 | — | — |
| 4 | MTIT_CUST | STRING | 10 | — | — |
| 5 | MTIT_DATE | DATE | 4 | — | — |
| 6 | MTIT_DEPT | STRING | 4 | — | — |
| 7 | MTIT_DESC | STRING | 30 | — | — |
| 8 | MTIT_EXTRA | STRING | 50 | — | — |
| 9 | MTIT_INVOICE | NUMERIC | 8 | — | — |
| 10 | MTIT_LOC | STRING | 10 | — | — |
| 11 | MTIT_LOT | STRING | 15 | — | — |
| 12 | MTIT_PO | NUMERIC | 8 | — | — |
| 13 | MTIT_PRICE | NUMERIC | 8 | 4 | — |
| 14 | MTIT_PRODLOT | STRING | 15 | — | — |
| 15 | MTIT_QC | STRING | 2 | — | — |
| 16 | MTIT_QTY | NUMERIC | 8 | 2 | — |
| 17 | MTIT_REF | STRING | 30 | — | — |
| 18 | MTIT_SCRAP | STRING | 2 | — | — |
| 19 | MTIT_SERIAL | STRING | 25 | — | — |
| 20 | MTIT_STDCST | NUMERIC | 8 | 6 | — |
| 21 | MTIT_TYPE | STRING | 1 | — | — |
| 22 | MTIT_VENDOR | STRING | 10 | — | — |
| 23 | MTIT_WOPRE | NUMERIC | 8 | — | — |
| 24 | MTIT_WOSUF | INTEGER | 2 | — | — |

## ISARADSC
**ARCHIVED CLOSED SALES ORDER NOTES**

Fields: 5

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BK_DESC_CODE | STRING | 15 | — | not used |
| 2 | BK_DESC_DESC | STRING | 25 | — | not used |
| 3 | BK_DESC_LINE | INTEGER | 2 | — | Notes line number |
| 4 | BK_DESC_NOTES | STRING | 70 | — | Notes - text |
| 5 | BK_DESC_NUM | NUMERIC | 8 | — | PO Number |

## ISARAHDS
**ARCHIVED INVOICE NOTES**

Fields: 5

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BK_DESC_CODE | STRING | 15 | — | not used |
| 2 | BK_DESC_DESC | STRING | 25 | — | not used |
| 3 | BK_DESC_LINE | INTEGER | 2 | — | Notes line number |
| 4 | BK_DESC_NOTES | STRING | 70 | — | Notes - text |
| 5 | BK_DESC_NUM | NUMERIC | 8 | — | PO Number |

## ISARAHIL
**ARCHIVED INVOICE LINES**

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

## ISARAHIN
**ARCHIVED INVOICE HEADERS**

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

## ISARAINV
**ARCHIVED CLOSED SALES ORDER HEADERS**

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

## ISARAIVL
**ARCHIVED CLOSED SALES ORDER LINES**

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

## ISARATXN
**ARCHIVED LOT LINK TO INVOICE LINE**

Fields: 14

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKAR_TXN_BIN | STRING | 15 | — | — |
| 2 | BKAR_TXN_CODE | STRING | 15 | — | Transaction Code |
| 3 | BKAR_TXN_DATE | DATE | 4 | — | Date |
| 4 | BKAR_TXN_DESC | STRING | 30 | — | Description |
| 5 | BKAR_TXN_EXTRA | STRING | 50 | — | — |
| 6 | BKAR_TXN_LINE | NUMERIC | 8 | — | Line Number |
| 7 | BKAR_TXN_LOC | STRING | 10 | — | — |
| 8 | BKAR_TXN_LOT | STRING | 15 | — | Lot  ID |
| 9 | BKAR_TXN_QTY | NUMERIC | 8 | 2 | Quantity |
| 10 | BKAR_TXN_SERIAL | STRING | 25 | — | Serial ID |
| 11 | BKAR_TXN_SONUM | NUMERIC | 8 | — | SO Number |
| 12 | BKAR_TXN_SRNUM | NUMERIC | 8 | — | — |
| 13 | BKAR_TXN_STOCK | STRING | 15 | — | — |
| 14 | BKAR_TXN_TMPSO | STRING | 40 | — | — |

## ISARATXS
**ARCHIVED SERIAL LINK TO INVOICE LINE**

Fields: 14

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKAR_TXN_BIN | STRING | 15 | — | — |
| 2 | BKAR_TXN_CODE | STRING | 15 | — | Transaction Code |
| 3 | BKAR_TXN_DATE | DATE | 4 | — | Date |
| 4 | BKAR_TXN_DESC | STRING | 30 | — | Description |
| 5 | BKAR_TXN_EXTRA | STRING | 50 | — | — |
| 6 | BKAR_TXN_LINE | NUMERIC | 8 | — | Line Number |
| 7 | BKAR_TXN_LOC | STRING | 10 | — | — |
| 8 | BKAR_TXN_LOT | STRING | 15 | — | Lot  ID |
| 9 | BKAR_TXN_QTY | NUMERIC | 8 | 2 | Quantity |
| 10 | BKAR_TXN_SERIAL | STRING | 25 | — | Serial ID |
| 11 | BKAR_TXN_SONUM | NUMERIC | 8 | — | SO Number |
| 12 | BKAR_TXN_SRNUM | NUMERIC | 8 | — | — |
| 13 | BKAR_TXN_STOCK | STRING | 15 | — | — |
| 14 | BKAR_TXN_TMPSO | STRING | 40 | — | — |

## ISARCHG
**CHANGES TO SALES ORDERS**

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

## ISARHCHG
**ON TIME DELIVERY**

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

## ISARQCHG
**CHANGES TO QUOTES**

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

## ISARRCHG
**CHANGES TO RECURRING SO**

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

## ISARTXNB
**BIN ALLOCATION TO SO LINE**

Fields: 23

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISAR_TXN_ALPHA_1 | STRING | 25 | — | — |
| 2 | ISAR_TXN_ALPHA_2 | STRING | 25 | — | — |
| 3 | ISAR_TXN_ALPHA_3 | STRING | 25 | — | — |
| 4 | ISAR_TXN_ALPHA_4 | STRING | 25 | — | — |
| 5 | ISAR_TXN_ALPHA_5 | STRING | 25 | — | — |
| 6 | ISAR_TXN_BIN | STRING | 15 | — | — |
| 7 | ISAR_TXN_BOX | INTEGER | 2 | — | — |
| 8 | ISAR_TXN_CODE | STRING | 15 | — | — |
| 9 | ISAR_TXN_DATE | DATE | 4 | — | — |
| 10 | ISAR_TXN_EXTRA | STRING | 100 | — | — |
| 11 | ISAR_TXN_FLAG_1 | STRING | 1 | — | — |
| 12 | ISAR_TXN_FLAG_2 | STRING | 1 | — | — |
| 13 | ISAR_TXN_FLAG_3 | STRING | 1 | — | — |
| 14 | ISAR_TXN_FLAG_4 | STRING | 1 | — | — |
| 15 | ISAR_TXN_FLAG_5 | STRING | 1 | — | — |
| 16 | ISAR_TXN_LINEID | NUMERIC | 8 | — | — |
| 17 | ISAR_TXN_LOC | STRING | 10 | — | — |
| 18 | ISAR_TXN_LOT | STRING | 15 | — | — |
| 19 | ISAR_TXN_QTY | NUMERIC | 8 | 2 | — |
| 20 | ISAR_TXN_RLEASD | STRING | 1 | — | — |
| 21 | ISAR_TXN_SERIAL | STRING | 25 | — | — |
| 22 | ISAR_TXN_SONUM | NUMERIC | 8 | — | — |
| 23 | ISAR_TXN_TMPSO | STRING | 40 | — | — |

## ISBOLMS
**BILL OF LADING**

Fields: 22

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISSO_BOX_BOX | INTEGER | 2 | — | — |
| 2 | ISSO_BOX_CODE | STRING | 15 | — | — |
| 3 | ISSO_BOX_DATE | DATE | 4 | — | — |
| 4 | ISSO_BOX_EXTRA | STRING | 150 | — | — |
| 5 | ISSO_BOX_HT | NUMERIC | 8 | 2 | — |
| 6 | ISSO_BOX_INVNUM | NUMERIC | 8 | — | — |
| 7 | ISSO_BOX_LG | NUMERIC | 8 | 2 | — |
| 8 | ISSO_BOX_LINE | NUMERIC | 8 | — | — |
| 9 | ISSO_BOX_LOT | STRING | 15 | — | — |
| 10 | ISSO_BOX_QTY | NUMERIC | 8 | 2 | — |
| 11 | ISSO_BOX_SERIAL | STRING | 25 | — | — |
| 12 | ISSO_BOX_SHIPPR | NUMERIC | 8 | — | — |
| 13 | ISSO_BOX_SHPCOD | STRING | 10 | — | — |
| 14 | ISSO_BOX_SKID | INTEGER | 2 | — | — |
| 15 | ISSO_BOX_SONUM | NUMERIC | 8 | — | — |
| 16 | ISSO_BOX_TEMP | STRING | 1 | — | — |
| 17 | ISSO_BOX_TRACK | STRING | 40 | — | — |
| 18 | ISSO_BOX_UCC | STRING | 30 | — | — |
| 19 | ISSO_BOX_WD | NUMERIC | 8 | 2 | — |
| 20 | ISSO_BOX_WEIGHT | NUMERIC | 8 | 2 | — |
| 21 | ISSO_BOX_WOPRE | NUMERIC | 8 | — | — |
| 22 | ISSO_BOX_WOSUF | INTEGER | 2 | — | — |

## ISESTAQL
**ARCHIVE QUOTE LINES**

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

## ISESTAQT
**ARCHIVE QUOTE HEADER**

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

## ISORDDSC
**SALES ORDER DESCRIPTION LIST**

Fields: 1

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IORD_DESC_CODE | STRING | 30 | — | — |

## ISQSOA
**TEMP FILE FOR QUICK SO ENTRY**

Fields: 12

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_QSOA_CUST | STRING | 10 | — | — |
| 2 | IS_QSOA_DESC | STRING | 30 | — | — |
| 3 | IS_QSOA_DISC | NUMERIC | 8 | 2 | — |
| 4 | IS_QSOA_EXTRA | STRING | 50 | — | — |
| 5 | IS_QSOA_ITEM | STRING | 15 | — | — |
| 6 | IS_QSOA_MDATE1 | DATE | 4 | — | — |
| 7 | IS_QSOA_MDATE2 | DATE | 4 | — | — |
| 8 | IS_QSOA_PRICE | NUMERIC | 8 | 4 | — |
| 9 | IS_QSOA_QTY | NUMERIC | 8 | 2 | — |
| 10 | IS_QSOA_SHPDTE | DATE | 4 | — | — |
| 11 | IS_QSOA_SHPTO | STRING | 10 | — | — |
| 12 | IS_QSOA_UID | STRING | 40 | — | — |

## ISQTINFO
**SUPPLEMENTAL QUOTE INFO**

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

## ISSOABOX
**ARCHIVED SHIPPING DETAIL**

Fields: 22

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISSO_BOX_BOX | INTEGER | 2 | — | — |
| 2 | ISSO_BOX_CODE | STRING | 15 | — | — |
| 3 | ISSO_BOX_DATE | DATE | 4 | — | — |
| 4 | ISSO_BOX_EXTRA | STRING | 150 | — | — |
| 5 | ISSO_BOX_HT | NUMERIC | 8 | 2 | — |
| 6 | ISSO_BOX_INVNUM | NUMERIC | 8 | — | — |
| 7 | ISSO_BOX_LG | NUMERIC | 8 | 2 | — |
| 8 | ISSO_BOX_LINE | NUMERIC | 8 | — | — |
| 9 | ISSO_BOX_LOT | STRING | 15 | — | — |
| 10 | ISSO_BOX_QTY | NUMERIC | 8 | 2 | — |
| 11 | ISSO_BOX_SERIAL | STRING | 25 | — | — |
| 12 | ISSO_BOX_SHIPPR | NUMERIC | 8 | — | — |
| 13 | ISSO_BOX_SHPCOD | STRING | 10 | — | — |
| 14 | ISSO_BOX_SKID | INTEGER | 2 | — | — |
| 15 | ISSO_BOX_SONUM | NUMERIC | 8 | — | — |
| 16 | ISSO_BOX_TEMP | STRING | 1 | — | — |
| 17 | ISSO_BOX_TRACK | STRING | 40 | — | — |
| 18 | ISSO_BOX_UCC | STRING | 30 | — | — |
| 19 | ISSO_BOX_WD | NUMERIC | 8 | 2 | — |
| 20 | ISSO_BOX_WEIGHT | NUMERIC | 8 | 2 | — |
| 21 | ISSO_BOX_WOPRE | NUMERIC | 8 | — | — |
| 22 | ISSO_BOX_WOSUF | INTEGER | 2 | — | — |

## ISSOAHBX
**ARCHIVED INVOICE BOX ALLOCATION**

Fields: 22

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISSO_BOX_BOX | INTEGER | 2 | — | — |
| 2 | ISSO_BOX_CODE | STRING | 15 | — | — |
| 3 | ISSO_BOX_DATE | DATE | 4 | — | — |
| 4 | ISSO_BOX_EXTRA | STRING | 150 | — | — |
| 5 | ISSO_BOX_HT | NUMERIC | 8 | 2 | — |
| 6 | ISSO_BOX_INVNUM | NUMERIC | 8 | — | — |
| 7 | ISSO_BOX_LG | NUMERIC | 8 | 2 | — |
| 8 | ISSO_BOX_LINE | NUMERIC | 8 | — | — |
| 9 | ISSO_BOX_LOT | STRING | 15 | — | — |
| 10 | ISSO_BOX_QTY | NUMERIC | 8 | 2 | — |
| 11 | ISSO_BOX_SERIAL | STRING | 25 | — | — |
| 12 | ISSO_BOX_SHIPPR | NUMERIC | 8 | — | — |
| 13 | ISSO_BOX_SHPCOD | STRING | 10 | — | — |
| 14 | ISSO_BOX_SKID | INTEGER | 2 | — | — |
| 15 | ISSO_BOX_SONUM | NUMERIC | 8 | — | — |
| 16 | ISSO_BOX_TEMP | STRING | 1 | — | — |
| 17 | ISSO_BOX_TRACK | STRING | 40 | — | — |
| 18 | ISSO_BOX_UCC | STRING | 30 | — | — |
| 19 | ISSO_BOX_WD | NUMERIC | 8 | 2 | — |
| 20 | ISSO_BOX_WEIGHT | NUMERIC | 8 | 2 | — |
| 21 | ISSO_BOX_WOPRE | NUMERIC | 8 | — | — |
| 22 | ISSO_BOX_WOSUF | INTEGER | 2 | — | — |

## ISSOAINF
**ARCHIVED SOA INFO**

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

## ISSOALOT
**ARCHIVED INVOICE LOT CONTROL**

Fields: 14

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKAR_TXN_BIN | STRING | 15 | — | — |
| 2 | BKAR_TXN_CODE | STRING | 15 | — | Transaction Code |
| 3 | BKAR_TXN_DATE | DATE | 4 | — | Date |
| 4 | BKAR_TXN_DESC | STRING | 30 | — | Description |
| 5 | BKAR_TXN_EXTRA | STRING | 50 | — | — |
| 6 | BKAR_TXN_LINE | NUMERIC | 8 | — | Line Number |
| 7 | BKAR_TXN_LOC | STRING | 10 | — | — |
| 8 | BKAR_TXN_LOT | STRING | 15 | — | Lot  ID |
| 9 | BKAR_TXN_QTY | NUMERIC | 8 | 2 | Quantity |
| 10 | BKAR_TXN_SERIAL | STRING | 25 | — | Serial ID |
| 11 | BKAR_TXN_SONUM | NUMERIC | 8 | — | SO Number |
| 12 | BKAR_TXN_SRNUM | NUMERIC | 8 | — | — |
| 13 | BKAR_TXN_STOCK | STRING | 15 | — | — |
| 14 | BKAR_TXN_TMPSO | STRING | 40 | — | — |

## ISSOASER
**ARCHIVED INVOICE SERIAL CONTROL**

Fields: 14

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKAR_TXN_BIN | STRING | 15 | — | — |
| 2 | BKAR_TXN_CODE | STRING | 15 | — | Transaction Code |
| 3 | BKAR_TXN_DATE | DATE | 4 | — | Date |
| 4 | BKAR_TXN_DESC | STRING | 30 | — | Description |
| 5 | BKAR_TXN_EXTRA | STRING | 50 | — | — |
| 6 | BKAR_TXN_LINE | NUMERIC | 8 | — | Line Number |
| 7 | BKAR_TXN_LOC | STRING | 10 | — | — |
| 8 | BKAR_TXN_LOT | STRING | 15 | — | Lot  ID |
| 9 | BKAR_TXN_QTY | NUMERIC | 8 | 2 | Quantity |
| 10 | BKAR_TXN_SERIAL | STRING | 25 | — | Serial ID |
| 11 | BKAR_TXN_SONUM | NUMERIC | 8 | — | SO Number |
| 12 | BKAR_TXN_SRNUM | NUMERIC | 8 | — | — |
| 13 | BKAR_TXN_STOCK | STRING | 15 | — | — |
| 14 | BKAR_TXN_TMPSO | STRING | 40 | — | — |

## ISSOBOX
**SHIPPING DETAIL**

Fields: 22

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISSO_BOX_BOX | INTEGER | 2 | — | — |
| 2 | ISSO_BOX_CODE | STRING | 15 | — | — |
| 3 | ISSO_BOX_DATE | DATE | 4 | — | — |
| 4 | ISSO_BOX_EXTRA | STRING | 150 | — | — |
| 5 | ISSO_BOX_HT | NUMERIC | 8 | 2 | — |
| 6 | ISSO_BOX_INVNUM | NUMERIC | 8 | — | — |
| 7 | ISSO_BOX_LG | NUMERIC | 8 | 2 | — |
| 8 | ISSO_BOX_LINE | NUMERIC | 8 | — | — |
| 9 | ISSO_BOX_LOT | STRING | 15 | — | — |
| 10 | ISSO_BOX_QTY | NUMERIC | 8 | 2 | — |
| 11 | ISSO_BOX_SERIAL | STRING | 25 | — | — |
| 12 | ISSO_BOX_SHIPPR | NUMERIC | 8 | — | — |
| 13 | ISSO_BOX_SHPCOD | STRING | 10 | — | — |
| 14 | ISSO_BOX_SKID | INTEGER | 2 | — | — |
| 15 | ISSO_BOX_SONUM | NUMERIC | 8 | — | — |
| 16 | ISSO_BOX_TEMP | STRING | 1 | — | — |
| 17 | ISSO_BOX_TRACK | STRING | 40 | — | — |
| 18 | ISSO_BOX_UCC | STRING | 30 | — | — |
| 19 | ISSO_BOX_WD | NUMERIC | 8 | 2 | — |
| 20 | ISSO_BOX_WEIGHT | NUMERIC | 8 | 2 | — |
| 21 | ISSO_BOX_WOPRE | NUMERIC | 8 | — | — |
| 22 | ISSO_BOX_WOSUF | INTEGER | 2 | — | — |

## ISSOHBOX
**SHIPPED BOX ID**

Fields: 22

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISSO_BOX_BOX | INTEGER | 2 | — | — |
| 2 | ISSO_BOX_CODE | STRING | 15 | — | — |
| 3 | ISSO_BOX_DATE | DATE | 4 | — | — |
| 4 | ISSO_BOX_EXTRA | STRING | 150 | — | — |
| 5 | ISSO_BOX_HT | NUMERIC | 8 | 2 | — |
| 6 | ISSO_BOX_INVNUM | NUMERIC | 8 | — | — |
| 7 | ISSO_BOX_LG | NUMERIC | 8 | 2 | — |
| 8 | ISSO_BOX_LINE | NUMERIC | 8 | — | — |
| 9 | ISSO_BOX_LOT | STRING | 15 | — | — |
| 10 | ISSO_BOX_QTY | NUMERIC | 8 | 2 | — |
| 11 | ISSO_BOX_SERIAL | STRING | 25 | — | — |
| 12 | ISSO_BOX_SHIPPR | NUMERIC | 8 | — | — |
| 13 | ISSO_BOX_SHPCOD | STRING | 10 | — | — |
| 14 | ISSO_BOX_SKID | INTEGER | 2 | — | — |
| 15 | ISSO_BOX_SONUM | NUMERIC | 8 | — | — |
| 16 | ISSO_BOX_TEMP | STRING | 1 | — | — |
| 17 | ISSO_BOX_TRACK | STRING | 40 | — | — |
| 18 | ISSO_BOX_UCC | STRING | 30 | — | — |
| 19 | ISSO_BOX_WD | NUMERIC | 8 | 2 | — |
| 20 | ISSO_BOX_WEIGHT | NUMERIC | 8 | 2 | — |
| 21 | ISSO_BOX_WOPRE | NUMERIC | 8 | — | — |
| 22 | ISSO_BOX_WOSUF | INTEGER | 2 | — | — |

## ISSOHNFO
**INVOICE SUPPLEMENTAL INFO**

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

## ISSOINFO
**SALES ORDER SUPPLEMENTAL INFO**

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

## ISSRAINV
**ARCHIVED SALES ORDER HEADER**

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

## ISSRAIVL
**ARCHIVED SALES ORDER LINE**

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

## NOTETEMP
**SALES ORDER NOTE TEMPLATES**

Fields: 5

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BK_DESC_CODE | STRING | 15 | — | not used |
| 2 | BK_DESC_DESC | STRING | 25 | — | not used |
| 3 | BK_DESC_LINE | INTEGER | 2 | — | Notes line number |
| 4 | BK_DESC_NOTES | STRING | 70 | — | Notes - text |
| 5 | BK_DESC_NUM | NUMERIC | 8 | — | PO Number |
