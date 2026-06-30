# IN — Inventory: Field Reference

Status: verified-schema

Source: `Evo-DBA_File_Fields 052421.xlsx`, sheet "Fields".
Field descriptions where provided by source; otherwise name-inferred.

---

## BKACTRPT
**IN-L-O REPORT LAYOUT**

Fields: 53

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKAC_FROM_AVGC | NUMERIC | 8 | 4 | Average cost range- from |
| 2 | BKAC_FROM_CAT | STRING | 4 | — | category range - from |
| 3 | BKAC_FROM_CLASS | STRING | 4 | — | product class range - from |
| 4 | BKAC_FROM_CUST | STRING | 10 | — | Customer Code range - from |
| 5 | BKAC_FROM_DATE | DATE | 4 | — | transaction date range - from |
| 6 | BKAC_FROM_DEPT | STRING | 4 | — | Department range - from |
| 7 | BKAC_FROM_DESC | STRING | 30 | — | Description range - from |
| 8 | BKAC_FROM_INV | NUMERIC | 8 | — | Invoice Number range - from |
| 9 | BKAC_FROM_LOC | STRING | 10 | — | location range - from |
| 10 | BKAC_FROM_LOT | STRING | 15 | — | Lot Number range - from |
| 11 | BKAC_FROM_PART | STRING | 15 | — | part number range - from |
| 12 | BKAC_FROM_PLOT | STRING | 15 | — | not used |
| 13 | BKAC_FROM_PO | NUMERIC | 8 | — | PO number range - from |
| 14 | BKAC_FROM_PRICE | NUMERIC | 8 | 4 | Price range - from |
| 15 | BKAC_FROM_QC | STRING | 2 | — | QC Codes range - from |
| 16 | BKAC_FROM_QTY | NUMERIC | 8 | 2 | Quantity range - from |
| 17 | BKAC_FROM_REF | STRING | 30 | — | Reference range - from |
| 18 | BKAC_FROM_SCRAP | STRING | 2 | — | Scrap code range - from |
| 19 | BKAC_FROM_SER | STRING | 25 | — | Serial number range - from |
| 20 | BKAC_FROM_STDC | NUMERIC | 8 | 6 | Standard cost range - from |
| 21 | BKAC_FROM_TYPE | STRING | 1 | — | Transaction type range -from |
| 22 | BKAC_FROM_VEND | STRING | 10 | — | Vendor code range - from |
| 23 | BKAC_FROM_WOPRE | NUMERIC | 8 | — | Work order prefix range - from |
| 24 | BKAC_FROM_WOSUF | INTEGER | 2 | — | Work order suffix range - from |
| 25 | BKAC_ITEM_RANGE | STRING | 8 | — | Part type range -to |
| 26 | BKAC_NAME | STRING | 15 | — | report name |
| 27 | BKAC_RTM | STRING | 15 | — | not used |
| 28 | BKAC_THRU_AVGC | NUMERIC | 8 | 4 | Average cost range- to |
| 29 | BKAC_THRU_CAT | STRING | 4 | — | category range- to |
| 30 | BKAC_THRU_CLASS | STRING | 4 | — | product class range - to |
| 31 | BKAC_THRU_CUST | STRING | 10 | — | Customer Code range - to |
| 32 | BKAC_THRU_DATE | DATE | 4 | — | transaction date range - to |
| 33 | BKAC_THRU_DEPT | STRING | 4 | — | Department range - to |
| 34 | BKAC_THRU_DESC | STRING | 30 | — | Description range - to |
| 35 | BKAC_THRU_INV | NUMERIC | 8 | — | invoice Number range - to |
| 36 | BKAC_THRU_LOC | STRING | 10 | — | location range - to |
| 37 | BKAC_THRU_LOT | STRING | 15 | — | Lot Number range - to |
| 38 | BKAC_THRU_PART | STRING | 15 | — | part number range - to |
| 39 | BKAC_THRU_PLOT | STRING | 15 | — | not used |
| 40 | BKAC_THRU_PO | NUMERIC | 8 | — | PO number range -to |
| 41 | BKAC_THRU_PRICE | NUMERIC | 8 | 4 | Price range - to |
| 42 | BKAC_THRU_QC | STRING | 2 | — | QC Codes range - to |
| 43 | BKAC_THRU_QTY | NUMERIC | 8 | 2 | Quantity range - to |
| 44 | BKAC_THRU_REF | STRING | 30 | — | Reference range - to |
| 45 | BKAC_THRU_SCRAP | STRING | 2 | — | Scrap code range - to |
| 46 | BKAC_THRU_SER | STRING | 25 | — | Serial number range - to |
| 47 | BKAC_THRU_STDC | NUMERIC | 8 | 6 | Standard cost range - to |
| 48 | BKAC_THRU_TYPE | STRING | 1 | — | Transaction type range - to |
| 49 | BKAC_THRU_VEND | STRING | 10 | — | Vendor code range - to |
| 50 | BKAC_THRU_WOPRE | NUMERIC | 8 | — | Work order prefix range - to |
| 51 | BKAC_THRU_WOSUF | INTEGER | 2 | — | Work order suffix range - to |
| 52 | BKAC_TYPE | STRING | 8 | — | report type |
| 53 | BKAC_TYPE_RANGE | STRING | 10 | — | Part type range -from |

## BKICAMTR
**ARCHIVE INVENTORY MASTER**

Fields: 64

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKIC_IS_DCODE | STRING | 3 | — | Duty Code |
| 2 | BKIC_PROD_ADTR | INTEGER | 2 | — | Average Days To Receive |
| 3 | BKIC_PROD_AVFO | NUMERIC | 8 | 4 | MRP Sensitivity Expedite Buffer |
| 4 | BKIC_PROD_AVGC | NUMERIC | 8 | 4 | Average Cost |
| 5 | BKIC_PROD_AVLAB | NUMERIC | 8 | 4 | Average labor cost |
| 6 | BKIC_PROD_AVMAT | NUMERIC | 8 | 4 | Average Material Cost |
| 7 | BKIC_PROD_AVOP | NUMERIC | 8 | 4 | Commissions Y/N |
| 8 | BKIC_PROD_AVSET | NUMERIC | 8 | 4 | Average Setup cost |
| 9 | BKIC_PROD_AVVO | NUMERIC | 8 | 4 | MRP Sensititity Delay Buffer |
| 10 | BKIC_PROD_CAT | STRING | 4 | — | Category (optional) |
| 11 | BKIC_PROD_CLASS | STRING | 4 | — | Product Class (required) |
| 12 | BKIC_PROD_CLYR | NUMERIC | 8 | 2 | Cost od Goods Last Year |
| 13 | BKIC_PROD_CMTD | NUMERIC | 8 | 2 | Cost of Goods Month-To-Date |
| 14 | BKIC_PROD_CODE | STRING | 15 | — | Product Code |
| 15 | BKIC_PROD_CVAR | NUMERIC | 8 | 4 | Cost of Goods Variance |
| 16 | BKIC_PROD_CYTD | NUMERIC | 8 | 2 | Cost of Goods Year-To-Date |
| 17 | BKIC_PROD_DESC | STRING | 30 | — | Description |
| 18 | BKIC_PROD_DPTA | STRING | 4 | — | GL Dept Asset/Expense Account |
| 19 | BKIC_PROD_DPTC | STRING | 4 | — | GL Dept COGS |
| 20 | BKIC_PROD_DPTNT | STRING | 4 | — | GL Dept. Sales Non Tax |
| 21 | BKIC_PROD_DPTS | STRING | 4 | — | GL Dept. Sales |
| 22 | BKIC_PROD_EXTRA | STRING | 100 | — | Extra |
| 23 | BKIC_PROD_GLA | STRING | 10 | — | GL Asset/Expense Account |
| 24 | BKIC_PROD_GLC | STRING | 10 | — | GL COGS Account |
| 25 | BKIC_PROD_GLS | STRING | 10 | — | GL Sales Account |
| 26 | BKIC_PROD_GLSNT | STRING | 10 | — | GL Sales Non-Tax Account |
| 27 | BKIC_PROD_GSLYR | NUMERIC | 8 | 2 | Gross Sales Last Year |
| 28 | BKIC_PROD_GSMTD | NUMERIC | 8 | 2 | Gross Sales Month-To-Date |
| 29 | BKIC_PROD_GSVAR | NUMERIC | 8 | 4 | Gross Sales Variance |
| 30 | BKIC_PROD_GSYTD | NUMERIC | 8 | 2 | Gross Sales Year-To-Date |
| 31 | BKIC_PROD_ISUPC | STRING | 12 | — | UPC Code |
| 32 | BKIC_PROD_LONGP | STRING | 25 | — | — |
| 33 | BKIC_PROD_LORD | DATE | 4 | — | Last Order Date |
| 34 | BKIC_PROD_LRCPT | DATE | 4 | — | Last Receipt Date |
| 35 | BKIC_PROD_LSALE | DATE | 4 | — | Last Sale Date |
| 36 | BKIC_PROD_LSTC | NUMERIC | 8 | 4 | Last Cost |
| 37 | BKIC_PROD_MANUF | STRING | 20 | — | — |
| 38 | BKIC_PROD_NGLYR | NUMERIC | 8 | 4 | — |
| 39 | BKIC_PROD_NGMTD | NUMERIC | 8 | 4 | — |
| 40 | BKIC_PROD_NGVAR | NUMERIC | 8 | 4 | — |
| 41 | BKIC_PROD_NGYTD | NUMERIC | 8 | 4 | — |
| 42 | BKIC_PROD_NOTE | STRING | 30 | — | Description Line 2 |
| 43 | BKIC_PROD_NSLYR | NUMERIC | 8 | 2 | Net Sales Last Year |
| 44 | BKIC_PROD_NSMTD | NUMERIC | 8 | 2 | Net Sales Month-To-Date |
| 45 | BKIC_PROD_NSVAR | NUMERIC | 8 | 4 | Net Sales Variance |
| 46 | BKIC_PROD_NSYTD | NUMERIC | 8 | 2 | Net Sales Year-To-Date |
| 47 | BKIC_PROD_PMAT | INTEGER | 2 | — | — |
| 48 | BKIC_PROD_PRICE | NUMERIC | 8 | 4 | Base Price |
| 49 | BKIC_PROD_RAMT | NUMERIC | 8 | — | Reorder Amount |
| 50 | BKIC_PROD_RLVL | NUMERIC | 8 | — | Reorder Level |
| 51 | BKIC_PROD_TAXIN | STRING | 1 | — | Tax In Y/N |
| 52 | BKIC_PROD_TO | NUMERIC | 8 | 4 | — |
| 53 | BKIC_PROD_TOTVL | NUMERIC | 8 | 2 | Book Value |
| 54 | BKIC_PROD_TXBLE | STRING | 1 | — | Taxable (Y/N) |
| 55 | BKIC_PROD_TYPE | STRING | 1 | — | Type (NRMFABLTKO) |
| 56 | BKIC_PROD_UBO | NUMERIC | 8 | 2 | Units on Back Order |
| 57 | BKIC_PROD_UM | STRING | 3 | — | Stock  J3491Unit of Measure |
| 58 | BKIC_PROD_UOH | NUMERIC | 8 | 2 | Units On-Hand |
| 59 | BKIC_PROD_UOO | NUMERIC | 8 | 2 | Units on Purchase Order |
| 60 | BKIC_PROD_UOSO | NUMERIC | 8 | 2 | Units on Sales Order |
| 61 | BKIC_PROD_USLYR | NUMERIC | 8 | 2 | Units Sold Last Year |
| 62 | BKIC_PROD_USMTD | NUMERIC | 8 | 2 | Units Sold Month-To-Date |
| 63 | BKIC_PROD_USVAR | NUMERIC | 8 | 4 | Units Sold Variance |
| 64 | BKIC_PROD_USYTD | NUMERIC | 8 | 2 | Units Sold Year-To-Date |

## BKICLOC
**INVENTORY LOCATIONS**

Fields: 32

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKIC_LOC_ALPHA1 | STRING | 30 | — | — |
| 2 | BKIC_LOC_ALPHA2 | STRING | 30 | — | — |
| 3 | BKIC_LOC_BIN | STRING | 15 | — | — |
| 4 | BKIC_LOC_CODE | STRING | 10 | — | Location Code |
| 5 | BKIC_LOC_DATE1 | DATE | 4 | — | — |
| 6 | BKIC_LOC_DPTA | STRING | 4 | — | GL Department |
| 7 | BKIC_LOC_DPTC | STRING | 4 | — | GL COGS Department |
| 8 | BKIC_LOC_DPTS | STRING | 4 | — | GL Sales Department |
| 9 | BKIC_LOC_DPTSNT | STRING | 4 | — | GL Sales Non Tax Department |
| 10 | BKIC_LOC_DPTWIP | STRING | 4 | — | GL WIP Department |
| 11 | BKIC_LOC_EXTRA | STRING | 50 | — | — |
| 12 | BKIC_LOC_FLAG1 | STRING | 1 | — | — |
| 13 | BKIC_LOC_GLA | STRING | 10 | — | GL Account |
| 14 | BKIC_LOC_GLC | STRING | 10 | — | GL COGS Account |
| 15 | BKIC_LOC_GLS | STRING | 10 | — | GL Sales Account |
| 16 | BKIC_LOC_GLSNT | STRING | 10 | — | GL Sales Non-Tax Account |
| 17 | BKIC_LOC_GLWIP | STRING | 10 | — | GL WIP Account |
| 18 | BKIC_LOC_LCDATE | DATE | 4 | — | — |
| 19 | BKIC_LOC_LOT | STRING | 15 | — | — |
| 20 | BKIC_LOC_NUM1 | NUMERIC | 8 | — | — |
| 21 | BKIC_LOC_NUM2 | NUMERIC | 8 | — | — |
| 22 | BKIC_LOC_PROD | STRING | 15 | — | Part Number |
| 23 | BKIC_LOC_SER | STRING | 25 | — | — |
| 24 | BKIC_LOC_UALLOC | NUMERIC | 8 | 2 | Units Allocated |
| 25 | BKIC_LOC_UBO | NUMERIC | 8 | 2 | Units on Back Order |
| 26 | BKIC_LOC_UIQC | NUMERIC | 8 | 2 | Units in QC |
| 27 | BKIC_LOC_UOH | NUMERIC | 8 | 2 | Units on Hand |
| 28 | BKIC_LOC_UOO | NUMERIC | 8 | 2 | Units on PO |
| 29 | BKIC_LOC_UOSO | NUMERIC | 8 | 2 | Units on Sales Order |
| 30 | BKIC_LOC_UOWO | NUMERIC | 8 | 2 | Units on Work Order |
| 31 | BKIC_LOC_UWIP | NUMERIC | 8 | 2 | Units in WIP |
| 32 | BKIC_LOC_WHCTRL | STRING | 1 | — | — |

## BKICLOCM
**INVENTORY LOCATION MASTER**

Fields: 12

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKIC_LOCM_ADDR1 | STRING | 30 | — | Address 1 |
| 2 | BKIC_LOCM_ADDR2 | STRING | 30 | — | Address 2 |
| 3 | BKIC_LOCM_ADDR3 | STRING | 30 | — | Address 3 |
| 4 | BKIC_LOCM_CITY | STRING | 20 | — | City |
| 5 | BKIC_LOCM_CNTCT | STRING | 25 | — | Contact |
| 6 | BKIC_LOCM_CODE | STRING | 10 | — | Location Code |
| 7 | BKIC_LOCM_FAX | STRING | 25 | — | Fax |
| 8 | BKIC_LOCM_NAME | STRING | 30 | — | Name |
| 9 | BKIC_LOCM_PHONE | STRING | 25 | — | Phone |
| 10 | BKIC_LOCM_STATE | STRING | 2 | — | State |
| 11 | BKIC_LOCM_TAX^ | STRING | 20 | — | — |
| 12 | BKIC_LOCM_ZIP | STRING | 10 | — | Zip |

## BKICMSTR
**INVENTORY MASTER**

Fields: 64

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKIC_IS_DCODE | STRING | 3 | — | Duty Code |
| 2 | BKIC_PROD_ADTR | INTEGER | 2 | — | Average Days To Receive |
| 3 | BKIC_PROD_AVFO | NUMERIC | 8 | 4 | MRP Sensitivity Expedite Buffer |
| 4 | BKIC_PROD_AVGC | NUMERIC | 8 | 4 | Average Cost |
| 5 | BKIC_PROD_AVLAB | NUMERIC | 8 | 4 | Average labor cost |
| 6 | BKIC_PROD_AVMAT | NUMERIC | 8 | 4 | Average Material Cost |
| 7 | BKIC_PROD_AVOP | NUMERIC | 8 | 4 | Commissions Y/N |
| 8 | BKIC_PROD_AVSET | NUMERIC | 8 | 4 | Average Setup cost |
| 9 | BKIC_PROD_AVVO | NUMERIC | 8 | 4 | MRP Sensititity Delay Buffer |
| 10 | BKIC_PROD_CAT | STRING | 4 | — | Category (optional) |
| 11 | BKIC_PROD_CLASS | STRING | 4 | — | Product Class (required) |
| 12 | BKIC_PROD_CLYR | NUMERIC | 8 | 2 | Cost od Goods Last Year |
| 13 | BKIC_PROD_CMTD | NUMERIC | 8 | 2 | Cost of Goods Month-To-Date |
| 14 | BKIC_PROD_CODE | STRING | 15 | — | Product Code |
| 15 | BKIC_PROD_CVAR | NUMERIC | 8 | 4 | Cost of Goods Variance |
| 16 | BKIC_PROD_CYTD | NUMERIC | 8 | 2 | Cost of Goods Year-To-Date |
| 17 | BKIC_PROD_DESC | STRING | 30 | — | Description |
| 18 | BKIC_PROD_DPTA | STRING | 4 | — | GL Dept Asset/Expense Account |
| 19 | BKIC_PROD_DPTC | STRING | 4 | — | GL Dept COGS |
| 20 | BKIC_PROD_DPTNT | STRING | 4 | — | GL Dept. Sales Non Tax |
| 21 | BKIC_PROD_DPTS | STRING | 4 | — | GL Dept. Sales |
| 22 | BKIC_PROD_EXTRA | STRING | 100 | — | Extra |
| 23 | BKIC_PROD_GLA | STRING | 10 | — | GL Asset/Expense Account |
| 24 | BKIC_PROD_GLC | STRING | 10 | — | GL COGS Account |
| 25 | BKIC_PROD_GLS | STRING | 10 | — | GL Sales Account |
| 26 | BKIC_PROD_GLSNT | STRING | 10 | — | GL Sales Non-Tax Account |
| 27 | BKIC_PROD_GSLYR | NUMERIC | 8 | 2 | Gross Sales Last Year |
| 28 | BKIC_PROD_GSMTD | NUMERIC | 8 | 2 | Gross Sales Month-To-Date |
| 29 | BKIC_PROD_GSVAR | NUMERIC | 8 | 4 | Gross Sales Variance |
| 30 | BKIC_PROD_GSYTD | NUMERIC | 8 | 2 | Gross Sales Year-To-Date |
| 31 | BKIC_PROD_ISUPC | STRING | 12 | — | UPC Code |
| 32 | BKIC_PROD_LONGP | STRING | 25 | — | — |
| 33 | BKIC_PROD_LORD | DATE | 4 | — | Last Order Date |
| 34 | BKIC_PROD_LRCPT | DATE | 4 | — | Last Receipt Date |
| 35 | BKIC_PROD_LSALE | DATE | 4 | — | Last Sale Date |
| 36 | BKIC_PROD_LSTC | NUMERIC | 8 | 4 | Last Cost |
| 37 | BKIC_PROD_MANUF | STRING | 20 | — | — |
| 38 | BKIC_PROD_NGLYR | NUMERIC | 8 | 4 | — |
| 39 | BKIC_PROD_NGMTD | NUMERIC | 8 | 4 | — |
| 40 | BKIC_PROD_NGVAR | NUMERIC | 8 | 4 | — |
| 41 | BKIC_PROD_NGYTD | NUMERIC | 8 | 4 | — |
| 42 | BKIC_PROD_NOTE | STRING | 30 | — | Description Line 2 |
| 43 | BKIC_PROD_NSLYR | NUMERIC | 8 | 2 | Net Sales Last Year |
| 44 | BKIC_PROD_NSMTD | NUMERIC | 8 | 2 | Net Sales Month-To-Date |
| 45 | BKIC_PROD_NSVAR | NUMERIC | 8 | 4 | Net Sales Variance |
| 46 | BKIC_PROD_NSYTD | NUMERIC | 8 | 2 | Net Sales Year-To-Date |
| 47 | BKIC_PROD_PMAT | INTEGER | 2 | — | — |
| 48 | BKIC_PROD_PRICE | NUMERIC | 8 | 4 | Base Price |
| 49 | BKIC_PROD_RAMT | NUMERIC | 8 | — | Reorder Amount |
| 50 | BKIC_PROD_RLVL | NUMERIC | 8 | — | Reorder Level |
| 51 | BKIC_PROD_TAXIN | STRING | 1 | — | Tax In Y/N |
| 52 | BKIC_PROD_TO | NUMERIC | 8 | 4 | — |
| 53 | BKIC_PROD_TOTVL | NUMERIC | 8 | 2 | Book Value |
| 54 | BKIC_PROD_TXBLE | STRING | 1 | — | Taxable (Y/N) |
| 55 | BKIC_PROD_TYPE | STRING | 1 | — | Type (NRMFABLTKO) |
| 56 | BKIC_PROD_UBO | NUMERIC | 8 | 2 | Units on Back Order |
| 57 | BKIC_PROD_UM | STRING | 3 | — | Stock  J3491Unit of Measure |
| 58 | BKIC_PROD_UOH | NUMERIC | 8 | 2 | Units On-Hand |
| 59 | BKIC_PROD_UOO | NUMERIC | 8 | 2 | Units on Purchase Order |
| 60 | BKIC_PROD_UOSO | NUMERIC | 8 | 2 | Units on Sales Order |
| 61 | BKIC_PROD_USLYR | NUMERIC | 8 | 2 | Units Sold Last Year |
| 62 | BKIC_PROD_USMTD | NUMERIC | 8 | 2 | Units Sold Month-To-Date |
| 63 | BKIC_PROD_USVAR | NUMERIC | 8 | 4 | Units Sold Variance |
| 64 | BKIC_PROD_USYTD | NUMERIC | 8 | 2 | Units Sold Year-To-Date |

## BKICREF
**INVENTORY CROSS-REFERENCE**

Fields: 8

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKIC_REF_CODE | STRING | 15 | — | Item Number |
| 2 | BKIC_REF_CUSCOD | STRING | 25 | — | Customer item Number |
| 3 | BKIC_REF_CUSNME | STRING | 30 | — | Customer Name |
| 4 | BKIC_REF_CUST | STRING | 10 | — | Custmer Code |
| 5 | BKIC_REF_DESC | STRING | 30 | — | Customer Description |
| 6 | BKIC_REF_DESC2 | STRING | 30 | — | — |
| 7 | BKIC_REF_EXTRA | STRING | 50 | — | Extra |
| 8 | BKIC_REF_PDESC | STRING | 30 | — | Item Description |

## BKQTTEMP
**INVENTORY LINKS**

Fields: 5

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BK_DESC_CODE | STRING | 15 | — | not used |
| 2 | BK_DESC_DESC | STRING | 25 | — | not used |
| 3 | BK_DESC_LINE | INTEGER | 2 | — | Notes line number |
| 4 | BK_DESC_NOTES | STRING | 70 | — | Notes - text |
| 5 | BK_DESC_NUM | NUMERIC | 8 | — | PO Number |

## CLASMSTR
**ITEM CLASS MASTER**

Fields: 2

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MTCLASS_M_CLASS | STRING | 4 | — | — |
| 2 | MTCLASS_M_DESC | STRING | 30 | — | — |

## CLASS
**ITEM CLASSES**

Fields: 24

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | CLASS_DPTA | STRING | 4 | — | — |
| 2 | CLASS_DPTC | STRING | 4 | — | — |
| 3 | CLASS_DPTFOH | STRING | 4 | — | — |
| 4 | CLASS_DPTLAB | STRING | 4 | — | — |
| 5 | CLASS_DPTMISC | STRING | 4 | — | — |
| 6 | CLASS_DPTNT | STRING | 4 | — | — |
| 7 | CLASS_DPTS | STRING | 4 | — | — |
| 8 | CLASS_DPTVOH | STRING | 4 | — | — |
| 9 | CLASS_DPTW | STRING | 4 | — | — |
| 10 | CLASS_DPTXTRA | STRING | 4 | — | — |
| 11 | CLASS_EXTRA | STRING | 50 | — | — |
| 12 | CLASS_GLA | STRING | 10 | — | — |
| 13 | CLASS_GLC | STRING | 10 | — | — |
| 14 | CLASS_GLFOH | STRING | 10 | — | — |
| 15 | CLASS_GLLAB | STRING | 10 | — | — |
| 16 | CLASS_GLMISC | STRING | 10 | — | — |
| 17 | CLASS_GLS | STRING | 10 | — | — |
| 18 | CLASS_GLSNT | STRING | 10 | — | — |
| 19 | CLASS_GLVOH | STRING | 10 | — | — |
| 20 | CLASS_GLW | STRING | 10 | — | — |
| 21 | CLASS_GLXTRA | STRING | 10 | — | — |
| 22 | MTCLASS_CLASS | STRING | 4 | — | — |
| 23 | MTCLASS_DESC | STRING | 30 | — | — |
| 24 | MTCLASS_LOC | STRING | 10 | — | — |

## DBAFIFO
**FIFO, LIFO BUCKETS**

Fields: 5

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | FIFO_COST | NUMERIC | 8 | 4 | — |
| 2 | FIFO_PARTNO | STRING | 15 | — | — |
| 3 | FIFO_QTY | NUMERIC | 8 | 2 | — |
| 4 | FIFO_RECVDATE | DATE | 4 | — | — |
| 5 | FIFO_REMAIN | NUMERIC | 8 | 2 | — |

## INVATXN
**ARCHIVE INVENTORY TRANSACTIONS**

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

## INVTXN
**INVENTORY TRANSACTIONS**

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

## ISCATMST
**ITEM CATEGORY MASTER LIST**

Fields: 3

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_CATM_CODE | STRING | 4 | — | — |
| 2 | IS_CATM_DESC | STRING | 60 | — | — |
| 3 | IS_CATM_EXTRA | STRING | 100 | — | — |

## ISCYCLCD
**CYCLE CODE MASTER**

Fields: 7

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_CYCLE_ALPHA | STRING | 15 | — | — |
| 2 | IS_CYCLE_CODE | STRING | 4 | — | — |
| 3 | IS_CYCLE_DATE | DATE | 4 | — | — |
| 4 | IS_CYCLE_DESC | STRING | 30 | — | — |
| 5 | IS_CYCLE_EXTRA | STRING | 50 | — | — |
| 6 | IS_CYCLE_FREQ | INTEGER | 2 | — | — |
| 7 | IS_CYCLE_NUM | NUMERIC | 8 | — | — |

## ISECO
**ITEM ECO LISTING**

Fields: 12

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_ECO_APPBY | STRING | 4 | — | — |
| 2 | IS_ECO_CURRENT | STRING | 1 | — | — |
| 3 | IS_ECO_DATE | DATE | 4 | — | — |
| 4 | IS_ECO_DRAW | STRING | 15 | — | — |
| 5 | IS_ECO_ECO | STRING | 15 | — | — |
| 6 | IS_ECO_ENTBY | STRING | 4 | — | — |
| 7 | IS_ECO_ENTDATE | DATE | 4 | — | — |
| 8 | IS_ECO_EXTRA | STRING | 100 | — | — |
| 9 | IS_ECO_INVDISP | STRING | 2 | — | — |
| 10 | IS_ECO_PART | STRING | 15 | — | — |
| 11 | IS_ECO_REVLVL | STRING | 5 | — | — |
| 12 | IS_ECO_STATUS | STRING | 1 | — | — |

## ISICADT
**INVENTORY MASTER AUDIT FILE**

Fields: 64

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKIC_IS_DCODE | STRING | 3 | — | Duty Code |
| 2 | BKIC_PROD_ADTR | INTEGER | 2 | — | Average Days To Receive |
| 3 | BKIC_PROD_AVFO | NUMERIC | 8 | 4 | MRP Sensitivity Expedite Buffer |
| 4 | BKIC_PROD_AVGC | NUMERIC | 8 | 4 | Average Cost |
| 5 | BKIC_PROD_AVLAB | NUMERIC | 8 | 4 | Average labor cost |
| 6 | BKIC_PROD_AVMAT | NUMERIC | 8 | 4 | Average Material Cost |
| 7 | BKIC_PROD_AVOP | NUMERIC | 8 | 4 | Commissions Y/N |
| 8 | BKIC_PROD_AVSET | NUMERIC | 8 | 4 | Average Setup cost |
| 9 | BKIC_PROD_AVVO | NUMERIC | 8 | 4 | MRP Sensititity Delay Buffer |
| 10 | BKIC_PROD_CAT | STRING | 4 | — | Category (optional) |
| 11 | BKIC_PROD_CLASS | STRING | 4 | — | Product Class (required) |
| 12 | BKIC_PROD_CLYR | NUMERIC | 8 | 2 | Cost od Goods Last Year |
| 13 | BKIC_PROD_CMTD | NUMERIC | 8 | 2 | Cost of Goods Month-To-Date |
| 14 | BKIC_PROD_CODE | STRING | 15 | — | Product Code |
| 15 | BKIC_PROD_CVAR | NUMERIC | 8 | 4 | Cost of Goods Variance |
| 16 | BKIC_PROD_CYTD | NUMERIC | 8 | 2 | Cost of Goods Year-To-Date |
| 17 | BKIC_PROD_DESC | STRING | 30 | — | Description |
| 18 | BKIC_PROD_DPTA | STRING | 4 | — | GL Dept Asset/Expense Account |
| 19 | BKIC_PROD_DPTC | STRING | 4 | — | GL Dept COGS |
| 20 | BKIC_PROD_DPTNT | STRING | 4 | — | GL Dept. Sales Non Tax |
| 21 | BKIC_PROD_DPTS | STRING | 4 | — | GL Dept. Sales |
| 22 | BKIC_PROD_EXTRA | STRING | 100 | — | Extra |
| 23 | BKIC_PROD_GLA | STRING | 10 | — | GL Asset/Expense Account |
| 24 | BKIC_PROD_GLC | STRING | 10 | — | GL COGS Account |
| 25 | BKIC_PROD_GLS | STRING | 10 | — | GL Sales Account |
| 26 | BKIC_PROD_GLSNT | STRING | 10 | — | GL Sales Non-Tax Account |
| 27 | BKIC_PROD_GSLYR | NUMERIC | 8 | 2 | Gross Sales Last Year |
| 28 | BKIC_PROD_GSMTD | NUMERIC | 8 | 2 | Gross Sales Month-To-Date |
| 29 | BKIC_PROD_GSVAR | NUMERIC | 8 | 4 | Gross Sales Variance |
| 30 | BKIC_PROD_GSYTD | NUMERIC | 8 | 2 | Gross Sales Year-To-Date |
| 31 | BKIC_PROD_ISUPC | STRING | 12 | — | UPC Code |
| 32 | BKIC_PROD_LONGP | STRING | 25 | — | — |
| 33 | BKIC_PROD_LORD | DATE | 4 | — | Last Order Date |
| 34 | BKIC_PROD_LRCPT | DATE | 4 | — | Last Receipt Date |
| 35 | BKIC_PROD_LSALE | DATE | 4 | — | Last Sale Date |
| 36 | BKIC_PROD_LSTC | NUMERIC | 8 | 4 | Last Cost |
| 37 | BKIC_PROD_MANUF | STRING | 20 | — | — |
| 38 | BKIC_PROD_NGLYR | NUMERIC | 8 | 4 | — |
| 39 | BKIC_PROD_NGMTD | NUMERIC | 8 | 4 | — |
| 40 | BKIC_PROD_NGVAR | NUMERIC | 8 | 4 | — |
| 41 | BKIC_PROD_NGYTD | NUMERIC | 8 | 4 | — |
| 42 | BKIC_PROD_NOTE | STRING | 30 | — | Description Line 2 |
| 43 | BKIC_PROD_NSLYR | NUMERIC | 8 | 2 | Net Sales Last Year |
| 44 | BKIC_PROD_NSMTD | NUMERIC | 8 | 2 | Net Sales Month-To-Date |
| 45 | BKIC_PROD_NSVAR | NUMERIC | 8 | 4 | Net Sales Variance |
| 46 | BKIC_PROD_NSYTD | NUMERIC | 8 | 2 | Net Sales Year-To-Date |
| 47 | BKIC_PROD_PMAT | INTEGER | 2 | — | — |
| 48 | BKIC_PROD_PRICE | NUMERIC | 8 | 4 | Base Price |
| 49 | BKIC_PROD_RAMT | NUMERIC | 8 | — | Reorder Amount |
| 50 | BKIC_PROD_RLVL | NUMERIC | 8 | — | Reorder Level |
| 51 | BKIC_PROD_TAXIN | STRING | 1 | — | Tax In Y/N |
| 52 | BKIC_PROD_TO | NUMERIC | 8 | 4 | — |
| 53 | BKIC_PROD_TOTVL | NUMERIC | 8 | 2 | Book Value |
| 54 | BKIC_PROD_TXBLE | STRING | 1 | — | Taxable (Y/N) |
| 55 | BKIC_PROD_TYPE | STRING | 1 | — | Type (NRMFABLTKO) |
| 56 | BKIC_PROD_UBO | NUMERIC | 8 | 2 | Units on Back Order |
| 57 | BKIC_PROD_UM | STRING | 3 | — | Stock  J3491Unit of Measure |
| 58 | BKIC_PROD_UOH | NUMERIC | 8 | 2 | Units On-Hand |
| 59 | BKIC_PROD_UOO | NUMERIC | 8 | 2 | Units on Purchase Order |
| 60 | BKIC_PROD_UOSO | NUMERIC | 8 | 2 | Units on Sales Order |
| 61 | BKIC_PROD_USLYR | NUMERIC | 8 | 2 | Units Sold Last Year |
| 62 | BKIC_PROD_USMTD | NUMERIC | 8 | 2 | Units Sold Month-To-Date |
| 63 | BKIC_PROD_USVAR | NUMERIC | 8 | 4 | Units Sold Variance |
| 64 | BKIC_PROD_USYTD | NUMERIC | 8 | 2 | Units Sold Year-To-Date |

## ISICAMTR
**ARCHIVE INVENTORY MASTER FILE 3**

Fields: 41

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_PROD_ADATE | DATE | 4 | — | — |
| 2 | IS_PROD_ALPHA_1 | STRING | 30 | — | — |
| 3 | IS_PROD_ALPHA_2 | STRING | 30 | — | — |
| 4 | IS_PROD_ALPHA_3 | STRING | 30 | — | — |
| 5 | IS_PROD_ALPHA_4 | STRING | 30 | — | — |
| 6 | IS_PROD_ALPHA_5 | STRING | 30 | — | — |
| 7 | IS_PROD_CDATE | DATE | 4 | — | — |
| 8 | IS_PROD_CODE | STRING | 15 | — | — |
| 9 | IS_PROD_EXTRA | STRING | 150 | — | — |
| 10 | IS_PROD_FLAG_1 | STRING | 1 | — | — |
| 11 | IS_PROD_FLAG_10 | STRING | 1 | — | — |
| 12 | IS_PROD_FLAG_2 | STRING | 1 | — | — |
| 13 | IS_PROD_FLAG_3 | STRING | 1 | — | — |
| 14 | IS_PROD_FLAG_4 | STRING | 1 | — | — |
| 15 | IS_PROD_FLAG_5 | STRING | 1 | — | — |
| 16 | IS_PROD_FLAG_6 | STRING | 1 | — | — |
| 17 | IS_PROD_FLAG_7 | STRING | 1 | — | — |
| 18 | IS_PROD_FLAG_8 | STRING | 1 | — | — |
| 19 | IS_PROD_FLAG_9 | STRING | 1 | — | — |
| 20 | IS_PROD_FOBFULL | NUMERIC | 8 | 2 | — |
| 21 | IS_PROD_FOBPAL | NUMERIC | 8 | 2 | — |
| 22 | IS_PROD_GDATES_1 | DATE | 4 | — | — |
| 23 | IS_PROD_GDATES_2 | DATE | 4 | — | — |
| 24 | IS_PROD_GDATES_3 | DATE | 4 | — | — |
| 25 | IS_PROD_GDATES_4 | DATE | 4 | — | — |
| 26 | IS_PROD_GDATES_5 | DATE | 4 | — | — |
| 27 | IS_PROD_HI | NUMERIC | 8 | — | — |
| 28 | IS_PROD_HT | NUMERIC | 8 | 2 | — |
| 29 | IS_PROD_ITP | STRING | 20 | — | — |
| 30 | IS_PROD_LG | NUMERIC | 8 | 2 | — |
| 31 | IS_PROD_NUM_1 | NUMERIC | 8 | 2 | — |
| 32 | IS_PROD_NUM_2 | NUMERIC | 8 | 2 | — |
| 33 | IS_PROD_NUM_3 | NUMERIC | 8 | 2 | — |
| 34 | IS_PROD_NUM_4 | NUMERIC | 8 | 2 | — |
| 35 | IS_PROD_NUM_5 | NUMERIC | 8 | 2 | — |
| 36 | IS_PROD_RCDATE | DATE | 4 | — | — |
| 37 | IS_PROD_SLEAD | INTEGER | 2 | — | — |
| 38 | IS_PROD_TI | NUMERIC | 8 | — | — |
| 39 | IS_PROD_TOOL | STRING | 15 | — | — |
| 40 | IS_PROD_WD | NUMERIC | 8 | 2 | — |
| 41 | IS_PROD_WT | NUMERIC | 8 | 6 | — |

## ISICMSTR
**INVENTORY MASTER 3**

Fields: 41

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_PROD_ADATE | DATE | 4 | — | — |
| 2 | IS_PROD_ALPHA_1 | STRING | 30 | — | — |
| 3 | IS_PROD_ALPHA_2 | STRING | 30 | — | — |
| 4 | IS_PROD_ALPHA_3 | STRING | 30 | — | — |
| 5 | IS_PROD_ALPHA_4 | STRING | 30 | — | — |
| 6 | IS_PROD_ALPHA_5 | STRING | 30 | — | — |
| 7 | IS_PROD_CDATE | DATE | 4 | — | — |
| 8 | IS_PROD_CODE | STRING | 15 | — | — |
| 9 | IS_PROD_EXTRA | STRING | 150 | — | — |
| 10 | IS_PROD_FLAG_1 | STRING | 1 | — | — |
| 11 | IS_PROD_FLAG_10 | STRING | 1 | — | — |
| 12 | IS_PROD_FLAG_2 | STRING | 1 | — | — |
| 13 | IS_PROD_FLAG_3 | STRING | 1 | — | — |
| 14 | IS_PROD_FLAG_4 | STRING | 1 | — | — |
| 15 | IS_PROD_FLAG_5 | STRING | 1 | — | — |
| 16 | IS_PROD_FLAG_6 | STRING | 1 | — | — |
| 17 | IS_PROD_FLAG_7 | STRING | 1 | — | — |
| 18 | IS_PROD_FLAG_8 | STRING | 1 | — | — |
| 19 | IS_PROD_FLAG_9 | STRING | 1 | — | — |
| 20 | IS_PROD_FOBFULL | NUMERIC | 8 | 2 | — |
| 21 | IS_PROD_FOBPAL | NUMERIC | 8 | 2 | — |
| 22 | IS_PROD_GDATES_1 | DATE | 4 | — | — |
| 23 | IS_PROD_GDATES_2 | DATE | 4 | — | — |
| 24 | IS_PROD_GDATES_3 | DATE | 4 | — | — |
| 25 | IS_PROD_GDATES_4 | DATE | 4 | — | — |
| 26 | IS_PROD_GDATES_5 | DATE | 4 | — | — |
| 27 | IS_PROD_HI | NUMERIC | 8 | — | — |
| 28 | IS_PROD_HT | NUMERIC | 8 | 2 | — |
| 29 | IS_PROD_ITP | STRING | 20 | — | — |
| 30 | IS_PROD_LG | NUMERIC | 8 | 2 | — |
| 31 | IS_PROD_NUM_1 | NUMERIC | 8 | 2 | — |
| 32 | IS_PROD_NUM_2 | NUMERIC | 8 | 2 | — |
| 33 | IS_PROD_NUM_3 | NUMERIC | 8 | 2 | — |
| 34 | IS_PROD_NUM_4 | NUMERIC | 8 | 2 | — |
| 35 | IS_PROD_NUM_5 | NUMERIC | 8 | 2 | — |
| 36 | IS_PROD_RCDATE | DATE | 4 | — | — |
| 37 | IS_PROD_SLEAD | INTEGER | 2 | — | — |
| 38 | IS_PROD_TI | NUMERIC | 8 | — | — |
| 39 | IS_PROD_TOOL | STRING | 15 | — | — |
| 40 | IS_PROD_WD | NUMERIC | 8 | 2 | — |
| 41 | IS_PROD_WT | NUMERIC | 8 | 6 | — |

## ISITMCFG
**AUTO PART GENERATOR**

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

## ISITP
**ITP MASTER LISTING**

Fields: 3

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_ITP_DESC | STRING | 80 | — | — |
| 2 | IS_ITP_EXTRA | STRING | 100 | — | — |
| 3 | IS_ITP_NUM | STRING | 20 | — | — |

## ISLOCCST
**COST BY WAREHOUSE LOCATION (NOT USED)**

Fields: 7

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_LCST_AVGC | NUMERIC | 8 | 4 | — |
| 2 | IS_LCST_BOOKVAL | NUMERIC | 8 | 4 | — |
| 3 | IS_LCST_EXTRA | STRING | 150 | — | — |
| 4 | IS_LCST_LDATE | DATE | 4 | — | — |
| 5 | IS_LCST_LOC | STRING | 10 | — | — |
| 6 | IS_LCST_LTIME | TIME | 4 | — | — |
| 7 | IS_LCST_PART | STRING | 15 | — | — |

## ISMICADT
**INVENTORY MASTER AUDIT FILE 2**

Fields: 109

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MTIC_PROD_ABC | STRING | 1 | — | Vendor Approval ,1,2 |
| 2 | MTIC_PROD_ACTIV | STRING | 1 | — | Active Inventory Y/N |
| 3 | MTIC_PROD_AVAIL | NUMERIC | 8 | 2 | Available |
| 4 | MTIC_PROD_CLASS | STRING | 4 | — | Product Class |
| 5 | MTIC_PROD_CLDES | STRING | 30 | — | Product Class Description |
| 6 | MTIC_PROD_CODE | STRING | 15 | — | Produce Code (Part Number) |
| 7 | MTIC_PROD_COMM | NUMERIC | 8 | 4 | Commission |
| 8 | MTIC_PROD_COST | STRING | 1 | — | Not Used |
| 9 | MTIC_PROD_CUBFT | NUMERIC | 8 | 4 | Cubic Feet |
| 10 | MTIC_PROD_CUM | STRING | 3 | — | Not Used |
| 11 | MTIC_PROD_CUSNM | STRING | 30 | — | Customer Name (not used) |
| 12 | MTIC_PROD_CUST | STRING | 10 | — | Customer Code |
| 13 | MTIC_PROD_CYCLE | STRING | 1 | — | Cycle Count Code |
| 14 | MTIC_PROD_DELBF | INTEGER | 2 | — | MRP Delay Buffer |
| 15 | MTIC_PROD_DESC | STRING | 30 | — | Description - Line 1 |
| 16 | MTIC_PROD_DRAW | STRING | 15 | — | Drawing Number |
| 17 | MTIC_PROD_ESTCD | STRING | 1 | — | Not Used |
| 18 | MTIC_PROD_EXPBF | INTEGER | 2 | — | MRP Expedite Buffer |
| 19 | MTIC_PROD_FRT | NUMERIC | 8 | 6 | Freight Percent |
| 20 | MTIC_PROD_FRT^ | NUMERIC | 8 | 2 | — |
| 21 | MTIC_PROD_GLINV | STRING | 10 | — | Not Used |
| 22 | MTIC_PROD_GLWIP | STRING | 10 | — | GL WIP Account |
| 23 | MTIC_PROD_INVDP | STRING | 4 | — | Not Used |
| 24 | MTIC_PROD_LEAD | INTEGER | 2 | — | Lead Time - Days |
| 25 | MTIC_PROD_LOC | STRING | 10 | — | Inventory Bin Location |
| 26 | MTIC_PROD_LONGP | STRING | 25 | — | Not Used |
| 27 | MTIC_PROD_LOT | STRING | 1 | — | Lot Control Y/N |
| 28 | MTIC_PROD_LOTSZ | NUMERIC | 8 | — | Lot Size |
| 29 | MTIC_PROD_MRP | STRING | 1 | — | MRP Item Y/N |
| 30 | MTIC_PROD_MRPSW | STRING | 1 | — | MRP Round to Whole Number Y/N |
| 31 | MTIC_PROD_OPT | STRING | 1 | — | Has Options Y/N |
| 32 | MTIC_PROD_OPTCD | STRING | 5 | — | Not Used |
| 33 | MTIC_PROD_OPTCS | STRING | 1 | — | Not Used |
| 34 | MTIC_PROD_OPTPR | INTEGER | 2 | — | — |
| 35 | MTIC_PROD_PCONV | NUMERIC | 8 | 5 | PO Conversion Multiplier |
| 36 | MTIC_PROD_PUM | STRING | 3 | — | Purchase Unit Measure |
| 37 | MTIC_PROD_RCOST_1 | NUMERIC | 8 | 6 | — |
| 38 | MTIC_PROD_RCOST_10 | NUMERIC | 8 | 6 | — |
| 39 | MTIC_PROD_RCOST_11 | NUMERIC | 8 | 6 | — |
| 40 | MTIC_PROD_RCOST_12 | NUMERIC | 8 | 6 | — |
| 41 | MTIC_PROD_RCOST_13 | NUMERIC | 8 | 6 | — |
| 42 | MTIC_PROD_RCOST_14 | NUMERIC | 8 | 6 | — |
| 43 | MTIC_PROD_RCOST_15 | NUMERIC | 8 | 6 | — |
| 44 | MTIC_PROD_RCOST_2 | NUMERIC | 8 | 6 | — |
| 45 | MTIC_PROD_RCOST_3 | NUMERIC | 8 | 6 | — |
| 46 | MTIC_PROD_RCOST_4 | NUMERIC | 8 | 6 | — |
| 47 | MTIC_PROD_RCOST_5 | NUMERIC | 8 | 6 | — |
| 48 | MTIC_PROD_RCOST_6 | NUMERIC | 8 | 6 | — |
| 49 | MTIC_PROD_RCOST_7 | NUMERIC | 8 | 6 | — |
| 50 | MTIC_PROD_RCOST_8 | NUMERIC | 8 | 6 | — |
| 51 | MTIC_PROD_RCOST_9 | NUMERIC | 8 | 6 | — |
| 52 | MTIC_PROD_REV | STRING | 5 | — | Revision Level |
| 53 | MTIC_PROD_SER | STRING | 1 | — | Serial Control Y/N |
| 54 | MTIC_PROD_SPECS_1 | STRING | 30 | — | — |
| 55 | MTIC_PROD_SPECS_10 | STRING | 30 | — | — |
| 56 | MTIC_PROD_SPECS_11 | STRING | 30 | — | — |
| 57 | MTIC_PROD_SPECS_12 | STRING | 30 | — | — |
| 58 | MTIC_PROD_SPECS_2 | STRING | 30 | — | — |
| 59 | MTIC_PROD_SPECS_3 | STRING | 30 | — | — |
| 60 | MTIC_PROD_SPECS_4 | STRING | 30 | — | — |
| 61 | MTIC_PROD_SPECS_5 | STRING | 30 | — | — |
| 62 | MTIC_PROD_SPECS_6 | STRING | 30 | — | — |
| 63 | MTIC_PROD_SPECS_7 | STRING | 30 | — | — |
| 64 | MTIC_PROD_SPECS_8 | STRING | 30 | — | — |
| 65 | MTIC_PROD_SPECS_9 | STRING | 30 | — | — |
| 66 | MTIC_PROD_STDC | NUMERIC | 8 | 6 | Not Used |
| 67 | MTIC_PROD_STDPK | NUMERIC | 8 | — | Standard Pack Quantity |
| 68 | MTIC_PROD_SUBST_1 | STRING | 25 | — | — |
| 69 | MTIC_PROD_SUBST_2 | STRING | 25 | — | — |
| 70 | MTIC_PROD_SUBST_3 | STRING | 25 | — | — |
| 71 | MTIC_PROD_SUBST_4 | STRING | 25 | — | — |
| 72 | MTIC_PROD_SUBST_5 | STRING | 25 | — | — |
| 73 | MTIC_PROD_SUM | STRING | 3 | — | Sales Unit Measure |
| 74 | MTIC_PROD_TYPE | STRING | 1 | — | Product TYPE (RFAMKLTBO) |
| 75 | MTIC_PROD_UIQC | NUMERIC | 8 | 2 | Units in QC |
| 76 | MTIC_PROD_UIWIP | NUMERIC | 8 | 2 | Units in WIP |
| 77 | MTIC_PROD_UOA | NUMERIC | 8 | 2 | Units On Allocations |
| 78 | MTIC_PROD_UOWO | NUMERIC | 8 | 2 | Units On Work Order |
| 79 | MTIC_PROD_VEND_1 | STRING | 10 | — | — |
| 80 | MTIC_PROD_VEND_10 | STRING | 10 | — | — |
| 81 | MTIC_PROD_VEND_2 | STRING | 10 | — | — |
| 82 | MTIC_PROD_VEND_3 | STRING | 10 | — | — |
| 83 | MTIC_PROD_VEND_4 | STRING | 10 | — | — |
| 84 | MTIC_PROD_VEND_5 | STRING | 10 | — | — |
| 85 | MTIC_PROD_VEND_6 | STRING | 10 | — | — |
| 86 | MTIC_PROD_VEND_7 | STRING | 10 | — | — |
| 87 | MTIC_PROD_VEND_8 | STRING | 10 | — | — |
| 88 | MTIC_PROD_VEND_9 | STRING | 10 | — | — |
| 89 | MTIC_PROD_VNAM_1 | STRING | 30 | — | — |
| 90 | MTIC_PROD_VNAM_10 | STRING | 30 | — | — |
| 91 | MTIC_PROD_VNAM_2 | STRING | 30 | — | — |
| 92 | MTIC_PROD_VNAM_3 | STRING | 30 | — | — |
| 93 | MTIC_PROD_VNAM_4 | STRING | 30 | — | — |
| 94 | MTIC_PROD_VNAM_5 | STRING | 30 | — | — |
| 95 | MTIC_PROD_VNAM_6 | STRING | 30 | — | — |
| 96 | MTIC_PROD_VNAM_7 | STRING | 30 | — | — |
| 97 | MTIC_PROD_VNAM_8 | STRING | 30 | — | — |
| 98 | MTIC_PROD_VNAM_9 | STRING | 30 | — | — |
| 99 | MTIC_PROD_VPC_1 | STRING | 20 | — | — |
| 100 | MTIC_PROD_VPC_2 | STRING | 20 | — | — |
| 101 | MTIC_PROD_VPC_3 | STRING | 20 | — | — |
| 102 | MTIC_PROD_VPC_4 | STRING | 20 | — | — |
| 103 | MTIC_PROD_VPC_5 | STRING | 20 | — | — |
| 104 | MTIC_PROD_VPC_6 | STRING | 20 | — | — |
| 105 | MTIC_PROD_VPC_7 | STRING | 20 | — | — |
| 106 | MTIC_PROD_VPC_8 | STRING | 20 | — | — |
| 107 | MTIC_PROD_VPC_9 | STRING | 20 | — | — |
| 108 | MTIC_PROD_WIPDP | STRING | 4 | — | GL WIP Department |
| 109 | MTIC_PROD_WT | NUMERIC | 8 | 6 | Weight |

## ISORDECO
**ORDER SPECIFIC ECO**

Fields: 12

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_OECO_DRAW | STRING | 15 | — | — |
| 2 | IS_OECO_ECO | STRING | 15 | — | — |
| 3 | IS_OECO_ENTDATE | DATE | 4 | — | — |
| 4 | IS_OECO_EXTRA | STRING | 100 | — | — |
| 5 | IS_OECO_PART | STRING | 15 | — | — |
| 6 | IS_OECO_PONUM | NUMERIC | 8 | — | — |
| 7 | IS_OECO_REVLVL | STRING | 5 | — | — |
| 8 | IS_OECO_SONUM | NUMERIC | 8 | — | — |
| 9 | IS_OECO_TMPO | STRING | 40 | — | — |
| 10 | IS_OECO_UNUM | NUMERIC | 8 | 4 | — |
| 11 | IS_OECO_WOPRE | NUMERIC | 8 | — | — |
| 12 | IS_OECO_WOSUF | INTEGER | 2 | — | — |

## ISUDFINV
**INVENTORY USER DEFINED DEFINITIONS**

Fields: 8

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_UDF_EXTRA | STRING | 100 | — | — |
| 2 | IS_UDF_FIELD | STRING | 19 | — | — |
| 3 | IS_UDF_LENGTH | INTEGER | 2 | — | — |
| 4 | IS_UDF_NAME | STRING | 15 | — | — |
| 5 | IS_UDF_SCRLBL | STRING | 25 | — | — |
| 6 | IS_UDF_SCRSIZE | INTEGER | 2 | — | — |
| 7 | IS_UDF_SCRVAR | INTEGER | 2 | — | — |
| 8 | IS_UDF_START | INTEGER | 2 | — | — |

## ISUDMSTR
**INVENTORY USER DEFINED MASTER LIST**

Fields: 3

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_UDM_CODE | STRING | 25 | — | — |
| 2 | IS_UDM_DESC | STRING | 60 | — | — |
| 3 | IS_UDM_EXTRA | STRING | 100 | — | — |

## MTICAMTR
**ARCHIVED INVENTORY MASTER 2**

Fields: 109

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MTIC_PROD_ABC | STRING | 1 | — | Vendor Approval ,1,2 |
| 2 | MTIC_PROD_ACTIV | STRING | 1 | — | Active Inventory Y/N |
| 3 | MTIC_PROD_AVAIL | NUMERIC | 8 | 2 | Available |
| 4 | MTIC_PROD_CLASS | STRING | 4 | — | Product Class |
| 5 | MTIC_PROD_CLDES | STRING | 30 | — | Product Class Description |
| 6 | MTIC_PROD_CODE | STRING | 15 | — | Produce Code (Part Number) |
| 7 | MTIC_PROD_COMM | NUMERIC | 8 | 4 | Commission |
| 8 | MTIC_PROD_COST | STRING | 1 | — | Not Used |
| 9 | MTIC_PROD_CUBFT | NUMERIC | 8 | 4 | Cubic Feet |
| 10 | MTIC_PROD_CUM | STRING | 3 | — | Not Used |
| 11 | MTIC_PROD_CUSNM | STRING | 30 | — | Customer Name (not used) |
| 12 | MTIC_PROD_CUST | STRING | 10 | — | Customer Code |
| 13 | MTIC_PROD_CYCLE | STRING | 1 | — | Cycle Count Code |
| 14 | MTIC_PROD_DELBF | INTEGER | 2 | — | MRP Delay Buffer |
| 15 | MTIC_PROD_DESC | STRING | 30 | — | Description - Line 1 |
| 16 | MTIC_PROD_DRAW | STRING | 15 | — | Drawing Number |
| 17 | MTIC_PROD_ESTCD | STRING | 1 | — | Not Used |
| 18 | MTIC_PROD_EXPBF | INTEGER | 2 | — | MRP Expedite Buffer |
| 19 | MTIC_PROD_FRT | NUMERIC | 8 | 6 | Freight Percent |
| 20 | MTIC_PROD_FRT^ | NUMERIC | 8 | 2 | — |
| 21 | MTIC_PROD_GLINV | STRING | 10 | — | Not Used |
| 22 | MTIC_PROD_GLWIP | STRING | 10 | — | GL WIP Account |
| 23 | MTIC_PROD_INVDP | STRING | 4 | — | Not Used |
| 24 | MTIC_PROD_LEAD | INTEGER | 2 | — | Lead Time - Days |
| 25 | MTIC_PROD_LOC | STRING | 10 | — | Inventory Bin Location |
| 26 | MTIC_PROD_LONGP | STRING | 25 | — | Not Used |
| 27 | MTIC_PROD_LOT | STRING | 1 | — | Lot Control Y/N |
| 28 | MTIC_PROD_LOTSZ | NUMERIC | 8 | — | Lot Size |
| 29 | MTIC_PROD_MRP | STRING | 1 | — | MRP Item Y/N |
| 30 | MTIC_PROD_MRPSW | STRING | 1 | — | MRP Round to Whole Number Y/N |
| 31 | MTIC_PROD_OPT | STRING | 1 | — | Has Options Y/N |
| 32 | MTIC_PROD_OPTCD | STRING | 5 | — | Not Used |
| 33 | MTIC_PROD_OPTCS | STRING | 1 | — | Not Used |
| 34 | MTIC_PROD_OPTPR | INTEGER | 2 | — | — |
| 35 | MTIC_PROD_PCONV | NUMERIC | 8 | 5 | PO Conversion Multiplier |
| 36 | MTIC_PROD_PUM | STRING | 3 | — | Purchase Unit Measure |
| 37 | MTIC_PROD_RCOST_1 | NUMERIC | 8 | 6 | — |
| 38 | MTIC_PROD_RCOST_10 | NUMERIC | 8 | 6 | — |
| 39 | MTIC_PROD_RCOST_11 | NUMERIC | 8 | 6 | — |
| 40 | MTIC_PROD_RCOST_12 | NUMERIC | 8 | 6 | — |
| 41 | MTIC_PROD_RCOST_13 | NUMERIC | 8 | 6 | — |
| 42 | MTIC_PROD_RCOST_14 | NUMERIC | 8 | 6 | — |
| 43 | MTIC_PROD_RCOST_15 | NUMERIC | 8 | 6 | — |
| 44 | MTIC_PROD_RCOST_2 | NUMERIC | 8 | 6 | — |
| 45 | MTIC_PROD_RCOST_3 | NUMERIC | 8 | 6 | — |
| 46 | MTIC_PROD_RCOST_4 | NUMERIC | 8 | 6 | — |
| 47 | MTIC_PROD_RCOST_5 | NUMERIC | 8 | 6 | — |
| 48 | MTIC_PROD_RCOST_6 | NUMERIC | 8 | 6 | — |
| 49 | MTIC_PROD_RCOST_7 | NUMERIC | 8 | 6 | — |
| 50 | MTIC_PROD_RCOST_8 | NUMERIC | 8 | 6 | — |
| 51 | MTIC_PROD_RCOST_9 | NUMERIC | 8 | 6 | — |
| 52 | MTIC_PROD_REV | STRING | 5 | — | Revision Level |
| 53 | MTIC_PROD_SER | STRING | 1 | — | Serial Control Y/N |
| 54 | MTIC_PROD_SPECS_1 | STRING | 30 | — | — |
| 55 | MTIC_PROD_SPECS_10 | STRING | 30 | — | — |
| 56 | MTIC_PROD_SPECS_11 | STRING | 30 | — | — |
| 57 | MTIC_PROD_SPECS_12 | STRING | 30 | — | — |
| 58 | MTIC_PROD_SPECS_2 | STRING | 30 | — | — |
| 59 | MTIC_PROD_SPECS_3 | STRING | 30 | — | — |
| 60 | MTIC_PROD_SPECS_4 | STRING | 30 | — | — |
| 61 | MTIC_PROD_SPECS_5 | STRING | 30 | — | — |
| 62 | MTIC_PROD_SPECS_6 | STRING | 30 | — | — |
| 63 | MTIC_PROD_SPECS_7 | STRING | 30 | — | — |
| 64 | MTIC_PROD_SPECS_8 | STRING | 30 | — | — |
| 65 | MTIC_PROD_SPECS_9 | STRING | 30 | — | — |
| 66 | MTIC_PROD_STDC | NUMERIC | 8 | 6 | Not Used |
| 67 | MTIC_PROD_STDPK | NUMERIC | 8 | — | Standard Pack Quantity |
| 68 | MTIC_PROD_SUBST_1 | STRING | 25 | — | — |
| 69 | MTIC_PROD_SUBST_2 | STRING | 25 | — | — |
| 70 | MTIC_PROD_SUBST_3 | STRING | 25 | — | — |
| 71 | MTIC_PROD_SUBST_4 | STRING | 25 | — | — |
| 72 | MTIC_PROD_SUBST_5 | STRING | 25 | — | — |
| 73 | MTIC_PROD_SUM | STRING | 3 | — | Sales Unit Measure |
| 74 | MTIC_PROD_TYPE | STRING | 1 | — | Product TYPE (RFAMKLTBO) |
| 75 | MTIC_PROD_UIQC | NUMERIC | 8 | 2 | Units in QC |
| 76 | MTIC_PROD_UIWIP | NUMERIC | 8 | 2 | Units in WIP |
| 77 | MTIC_PROD_UOA | NUMERIC | 8 | 2 | Units On Allocations |
| 78 | MTIC_PROD_UOWO | NUMERIC | 8 | 2 | Units On Work Order |
| 79 | MTIC_PROD_VEND_1 | STRING | 10 | — | — |
| 80 | MTIC_PROD_VEND_10 | STRING | 10 | — | — |
| 81 | MTIC_PROD_VEND_2 | STRING | 10 | — | — |
| 82 | MTIC_PROD_VEND_3 | STRING | 10 | — | — |
| 83 | MTIC_PROD_VEND_4 | STRING | 10 | — | — |
| 84 | MTIC_PROD_VEND_5 | STRING | 10 | — | — |
| 85 | MTIC_PROD_VEND_6 | STRING | 10 | — | — |
| 86 | MTIC_PROD_VEND_7 | STRING | 10 | — | — |
| 87 | MTIC_PROD_VEND_8 | STRING | 10 | — | — |
| 88 | MTIC_PROD_VEND_9 | STRING | 10 | — | — |
| 89 | MTIC_PROD_VNAM_1 | STRING | 30 | — | — |
| 90 | MTIC_PROD_VNAM_10 | STRING | 30 | — | — |
| 91 | MTIC_PROD_VNAM_2 | STRING | 30 | — | — |
| 92 | MTIC_PROD_VNAM_3 | STRING | 30 | — | — |
| 93 | MTIC_PROD_VNAM_4 | STRING | 30 | — | — |
| 94 | MTIC_PROD_VNAM_5 | STRING | 30 | — | — |
| 95 | MTIC_PROD_VNAM_6 | STRING | 30 | — | — |
| 96 | MTIC_PROD_VNAM_7 | STRING | 30 | — | — |
| 97 | MTIC_PROD_VNAM_8 | STRING | 30 | — | — |
| 98 | MTIC_PROD_VNAM_9 | STRING | 30 | — | — |
| 99 | MTIC_PROD_VPC_1 | STRING | 20 | — | — |
| 100 | MTIC_PROD_VPC_2 | STRING | 20 | — | — |
| 101 | MTIC_PROD_VPC_3 | STRING | 20 | — | — |
| 102 | MTIC_PROD_VPC_4 | STRING | 20 | — | — |
| 103 | MTIC_PROD_VPC_5 | STRING | 20 | — | — |
| 104 | MTIC_PROD_VPC_6 | STRING | 20 | — | — |
| 105 | MTIC_PROD_VPC_7 | STRING | 20 | — | — |
| 106 | MTIC_PROD_VPC_8 | STRING | 20 | — | — |
| 107 | MTIC_PROD_VPC_9 | STRING | 20 | — | — |
| 108 | MTIC_PROD_WIPDP | STRING | 4 | — | GL WIP Department |
| 109 | MTIC_PROD_WT | NUMERIC | 8 | 6 | Weight |

## MTICMSTR
**INVENTORY MASTER 2**

Fields: 109

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MTIC_PROD_ABC | STRING | 1 | — | Vendor Approval ,1,2 |
| 2 | MTIC_PROD_ACTIV | STRING | 1 | — | Active Inventory Y/N |
| 3 | MTIC_PROD_AVAIL | NUMERIC | 8 | 2 | Available |
| 4 | MTIC_PROD_CLASS | STRING | 4 | — | Product Class |
| 5 | MTIC_PROD_CLDES | STRING | 30 | — | Product Class Description |
| 6 | MTIC_PROD_CODE | STRING | 15 | — | Produce Code (Part Number) |
| 7 | MTIC_PROD_COMM | NUMERIC | 8 | 4 | Commission |
| 8 | MTIC_PROD_COST | STRING | 1 | — | Not Used |
| 9 | MTIC_PROD_CUBFT | NUMERIC | 8 | 4 | Cubic Feet |
| 10 | MTIC_PROD_CUM | STRING | 3 | — | Not Used |
| 11 | MTIC_PROD_CUSNM | STRING | 30 | — | Customer Name (not used) |
| 12 | MTIC_PROD_CUST | STRING | 10 | — | Customer Code |
| 13 | MTIC_PROD_CYCLE | STRING | 1 | — | Cycle Count Code |
| 14 | MTIC_PROD_DELBF | INTEGER | 2 | — | MRP Delay Buffer |
| 15 | MTIC_PROD_DESC | STRING | 30 | — | Description - Line 1 |
| 16 | MTIC_PROD_DRAW | STRING | 15 | — | Drawing Number |
| 17 | MTIC_PROD_ESTCD | STRING | 1 | — | Not Used |
| 18 | MTIC_PROD_EXPBF | INTEGER | 2 | — | MRP Expedite Buffer |
| 19 | MTIC_PROD_FRT | NUMERIC | 8 | 6 | Freight Percent |
| 20 | MTIC_PROD_FRT^ | NUMERIC | 8 | 2 | — |
| 21 | MTIC_PROD_GLINV | STRING | 10 | — | Not Used |
| 22 | MTIC_PROD_GLWIP | STRING | 10 | — | GL WIP Account |
| 23 | MTIC_PROD_INVDP | STRING | 4 | — | Not Used |
| 24 | MTIC_PROD_LEAD | INTEGER | 2 | — | Lead Time - Days |
| 25 | MTIC_PROD_LOC | STRING | 10 | — | Inventory Bin Location |
| 26 | MTIC_PROD_LONGP | STRING | 25 | — | Not Used |
| 27 | MTIC_PROD_LOT | STRING | 1 | — | Lot Control Y/N |
| 28 | MTIC_PROD_LOTSZ | NUMERIC | 8 | — | Lot Size |
| 29 | MTIC_PROD_MRP | STRING | 1 | — | MRP Item Y/N |
| 30 | MTIC_PROD_MRPSW | STRING | 1 | — | MRP Round to Whole Number Y/N |
| 31 | MTIC_PROD_OPT | STRING | 1 | — | Has Options Y/N |
| 32 | MTIC_PROD_OPTCD | STRING | 5 | — | Not Used |
| 33 | MTIC_PROD_OPTCS | STRING | 1 | — | Not Used |
| 34 | MTIC_PROD_OPTPR | INTEGER | 2 | — | — |
| 35 | MTIC_PROD_PCONV | NUMERIC | 8 | 5 | PO Conversion Multiplier |
| 36 | MTIC_PROD_PUM | STRING | 3 | — | Purchase Unit Measure |
| 37 | MTIC_PROD_RCOST_1 | NUMERIC | 8 | 6 | — |
| 38 | MTIC_PROD_RCOST_10 | NUMERIC | 8 | 6 | — |
| 39 | MTIC_PROD_RCOST_11 | NUMERIC | 8 | 6 | — |
| 40 | MTIC_PROD_RCOST_12 | NUMERIC | 8 | 6 | — |
| 41 | MTIC_PROD_RCOST_13 | NUMERIC | 8 | 6 | — |
| 42 | MTIC_PROD_RCOST_14 | NUMERIC | 8 | 6 | — |
| 43 | MTIC_PROD_RCOST_15 | NUMERIC | 8 | 6 | — |
| 44 | MTIC_PROD_RCOST_2 | NUMERIC | 8 | 6 | — |
| 45 | MTIC_PROD_RCOST_3 | NUMERIC | 8 | 6 | — |
| 46 | MTIC_PROD_RCOST_4 | NUMERIC | 8 | 6 | — |
| 47 | MTIC_PROD_RCOST_5 | NUMERIC | 8 | 6 | — |
| 48 | MTIC_PROD_RCOST_6 | NUMERIC | 8 | 6 | — |
| 49 | MTIC_PROD_RCOST_7 | NUMERIC | 8 | 6 | — |
| 50 | MTIC_PROD_RCOST_8 | NUMERIC | 8 | 6 | — |
| 51 | MTIC_PROD_RCOST_9 | NUMERIC | 8 | 6 | — |
| 52 | MTIC_PROD_REV | STRING | 5 | — | Revision Level |
| 53 | MTIC_PROD_SER | STRING | 1 | — | Serial Control Y/N |
| 54 | MTIC_PROD_SPECS_1 | STRING | 30 | — | — |
| 55 | MTIC_PROD_SPECS_10 | STRING | 30 | — | — |
| 56 | MTIC_PROD_SPECS_11 | STRING | 30 | — | — |
| 57 | MTIC_PROD_SPECS_12 | STRING | 30 | — | — |
| 58 | MTIC_PROD_SPECS_2 | STRING | 30 | — | — |
| 59 | MTIC_PROD_SPECS_3 | STRING | 30 | — | — |
| 60 | MTIC_PROD_SPECS_4 | STRING | 30 | — | — |
| 61 | MTIC_PROD_SPECS_5 | STRING | 30 | — | — |
| 62 | MTIC_PROD_SPECS_6 | STRING | 30 | — | — |
| 63 | MTIC_PROD_SPECS_7 | STRING | 30 | — | — |
| 64 | MTIC_PROD_SPECS_8 | STRING | 30 | — | — |
| 65 | MTIC_PROD_SPECS_9 | STRING | 30 | — | — |
| 66 | MTIC_PROD_STDC | NUMERIC | 8 | 6 | Not Used |
| 67 | MTIC_PROD_STDPK | NUMERIC | 8 | — | Standard Pack Quantity |
| 68 | MTIC_PROD_SUBST_1 | STRING | 25 | — | — |
| 69 | MTIC_PROD_SUBST_2 | STRING | 25 | — | — |
| 70 | MTIC_PROD_SUBST_3 | STRING | 25 | — | — |
| 71 | MTIC_PROD_SUBST_4 | STRING | 25 | — | — |
| 72 | MTIC_PROD_SUBST_5 | STRING | 25 | — | — |
| 73 | MTIC_PROD_SUM | STRING | 3 | — | Sales Unit Measure |
| 74 | MTIC_PROD_TYPE | STRING | 1 | — | Product TYPE (RFAMKLTBO) |
| 75 | MTIC_PROD_UIQC | NUMERIC | 8 | 2 | Units in QC |
| 76 | MTIC_PROD_UIWIP | NUMERIC | 8 | 2 | Units in WIP |
| 77 | MTIC_PROD_UOA | NUMERIC | 8 | 2 | Units On Allocations |
| 78 | MTIC_PROD_UOWO | NUMERIC | 8 | 2 | Units On Work Order |
| 79 | MTIC_PROD_VEND_1 | STRING | 10 | — | — |
| 80 | MTIC_PROD_VEND_10 | STRING | 10 | — | — |
| 81 | MTIC_PROD_VEND_2 | STRING | 10 | — | — |
| 82 | MTIC_PROD_VEND_3 | STRING | 10 | — | — |
| 83 | MTIC_PROD_VEND_4 | STRING | 10 | — | — |
| 84 | MTIC_PROD_VEND_5 | STRING | 10 | — | — |
| 85 | MTIC_PROD_VEND_6 | STRING | 10 | — | — |
| 86 | MTIC_PROD_VEND_7 | STRING | 10 | — | — |
| 87 | MTIC_PROD_VEND_8 | STRING | 10 | — | — |
| 88 | MTIC_PROD_VEND_9 | STRING | 10 | — | — |
| 89 | MTIC_PROD_VNAM_1 | STRING | 30 | — | — |
| 90 | MTIC_PROD_VNAM_10 | STRING | 30 | — | — |
| 91 | MTIC_PROD_VNAM_2 | STRING | 30 | — | — |
| 92 | MTIC_PROD_VNAM_3 | STRING | 30 | — | — |
| 93 | MTIC_PROD_VNAM_4 | STRING | 30 | — | — |
| 94 | MTIC_PROD_VNAM_5 | STRING | 30 | — | — |
| 95 | MTIC_PROD_VNAM_6 | STRING | 30 | — | — |
| 96 | MTIC_PROD_VNAM_7 | STRING | 30 | — | — |
| 97 | MTIC_PROD_VNAM_8 | STRING | 30 | — | — |
| 98 | MTIC_PROD_VNAM_9 | STRING | 30 | — | — |
| 99 | MTIC_PROD_VPC_1 | STRING | 20 | — | — |
| 100 | MTIC_PROD_VPC_2 | STRING | 20 | — | — |
| 101 | MTIC_PROD_VPC_3 | STRING | 20 | — | — |
| 102 | MTIC_PROD_VPC_4 | STRING | 20 | — | — |
| 103 | MTIC_PROD_VPC_5 | STRING | 20 | — | — |
| 104 | MTIC_PROD_VPC_6 | STRING | 20 | — | — |
| 105 | MTIC_PROD_VPC_7 | STRING | 20 | — | — |
| 106 | MTIC_PROD_VPC_8 | STRING | 20 | — | — |
| 107 | MTIC_PROD_VPC_9 | STRING | 20 | — | — |
| 108 | MTIC_PROD_WIPDP | STRING | 4 | — | GL WIP Department |
| 109 | MTIC_PROD_WT | NUMERIC | 8 | 6 | Weight |
