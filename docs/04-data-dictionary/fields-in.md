# IN — Inventory: Field Reference

Status: verified-schema + completed field meanings (Pass 574k-4, 2026-07-06).

Source: `Evo-DBA_File_Fields 052421.xlsx`, sheet "Fields".

Identical-schema notes:
- BKICMSTR and ISICADT are identical 64-field schemas to BKICAMTR (BKIC_PROD_* prefix).
- ISICMSTR is identical 41-field schema to ISICAMTR (IS_PROD_* prefix).
- MTICAMTR and MTICMSTR are identical 109-field schemas to ISMICADT (MTIC_PROD_* prefix).
- INVATXN is identical 24-field schema to INVTXN (MTIT_* prefix).

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

Fields: 64 | Key: BKIC_PROD_CODE

Identical 64-field schema to BKICMSTR and ISICADT (BKIC_PROD_* prefix). Records archived here on inventory master change/delete.

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
| 32 | BKIC_PROD_LONGP | STRING | 25 | — | Long / alternate part number (secondary identifier; extended part code) |
| 33 | BKIC_PROD_LORD | DATE | 4 | — | Last Order Date |
| 34 | BKIC_PROD_LRCPT | DATE | 4 | — | Last Receipt Date |
| 35 | BKIC_PROD_LSALE | DATE | 4 | — | Last Sale Date |
| 36 | BKIC_PROD_LSTC | NUMERIC | 8 | 4 | Last Cost |
| 37 | BKIC_PROD_MANUF | STRING | 20 | — | Manufacturer name |
| 38 | BKIC_PROD_NGLYR | NUMERIC | 8 | 4 | Net Gross Profit last year |
| 39 | BKIC_PROD_NGMTD | NUMERIC | 8 | 4 | Net Gross Profit month-to-date |
| 40 | BKIC_PROD_NGVAR | NUMERIC | 8 | 4 | Net Gross Profit variance (actual vs. budget) |
| 41 | BKIC_PROD_NGYTD | NUMERIC | 8 | 4 | Net Gross Profit year-to-date |
| 42 | BKIC_PROD_NOTE | STRING | 30 | — | Description Line 2 |
| 43 | BKIC_PROD_NSLYR | NUMERIC | 8 | 2 | Net Sales Last Year |
| 44 | BKIC_PROD_NSMTD | NUMERIC | 8 | 2 | Net Sales Month-To-Date |
| 45 | BKIC_PROD_NSVAR | NUMERIC | 8 | 4 | Net Sales Variance |
| 46 | BKIC_PROD_NSYTD | NUMERIC | 8 | 2 | Net Sales Year-To-Date |
| 47 | BKIC_PROD_PMAT | INTEGER | 2 | — | Price matrix code (tiered pricing matrix assignment; links to CLASS table) |
| 48 | BKIC_PROD_PRICE | NUMERIC | 8 | 4 | Base Price |
| 49 | BKIC_PROD_RAMT | NUMERIC | 8 | — | Reorder Amount |
| 50 | BKIC_PROD_RLVL | NUMERIC | 8 | — | Reorder Level |
| 51 | BKIC_PROD_TAXIN | STRING | 1 | — | Tax In Y/N |
| 52 | BKIC_PROD_TO | NUMERIC | 8 | 4 | Inventory turnover ratio (annual units sold / average on-hand) |
| 53 | BKIC_PROD_TOTVL | NUMERIC | 8 | 2 | Book Value |
| 54 | BKIC_PROD_TXBLE | STRING | 1 | — | Taxable (Y/N) |
| 55 | BKIC_PROD_TYPE | STRING | 1 | — | Type (NRMFABLTKO) |
| 56 | BKIC_PROD_UBO | NUMERIC | 8 | 2 | Units on Back Order |
| 57 | BKIC_PROD_UM | STRING | 3 | — | Stock Unit of Measure |
| 58 | BKIC_PROD_UOH | NUMERIC | 8 | 2 | Units On-Hand |
| 59 | BKIC_PROD_UOO | NUMERIC | 8 | 2 | Units on Purchase Order |
| 60 | BKIC_PROD_UOSO | NUMERIC | 8 | 2 | Units on Sales Order |
| 61 | BKIC_PROD_USLYR | NUMERIC | 8 | 2 | Units Sold Last Year |
| 62 | BKIC_PROD_USMTD | NUMERIC | 8 | 2 | Units Sold Month-To-Date |
| 63 | BKIC_PROD_USVAR | NUMERIC | 8 | 4 | Units Sold Variance |
| 64 | BKIC_PROD_USYTD | NUMERIC | 8 | 2 | Units Sold Year-To-Date |

## BKICLOC
**INVENTORY LOCATIONS**

Fields: 32 | Key: BKIC_LOC_CODE + BKIC_LOC_PROD

One record per part per warehouse location. Tracks quantity and lot/serial data at each bin.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKIC_LOC_ALPHA1 | STRING | 30 | — | User-defined alpha field 1 |
| 2 | BKIC_LOC_ALPHA2 | STRING | 30 | — | User-defined alpha field 2 |
| 3 | BKIC_LOC_BIN | STRING | 15 | — | Bin slot within this warehouse location (sub-location code) |
| 4 | BKIC_LOC_CODE | STRING | 10 | — | Location Code |
| 5 | BKIC_LOC_DATE1 | DATE | 4 | — | User-defined date 1 |
| 6 | BKIC_LOC_DPTA | STRING | 4 | — | GL Department |
| 7 | BKIC_LOC_DPTC | STRING | 4 | — | GL COGS Department |
| 8 | BKIC_LOC_DPTS | STRING | 4 | — | GL Sales Department |
| 9 | BKIC_LOC_DPTSNT | STRING | 4 | — | GL Sales Non Tax Department |
| 10 | BKIC_LOC_DPTWIP | STRING | 4 | — | GL WIP Department |
| 11 | BKIC_LOC_EXTRA | STRING | 50 | — | Extra data |
| 12 | BKIC_LOC_FLAG1 | STRING | 1 | — | User-defined flag 1 |
| 13 | BKIC_LOC_GLA | STRING | 10 | — | GL Account |
| 14 | BKIC_LOC_GLC | STRING | 10 | — | GL COGS Account |
| 15 | BKIC_LOC_GLS | STRING | 10 | — | GL Sales Account |
| 16 | BKIC_LOC_GLSNT | STRING | 10 | — | GL Sales Non-Tax Account |
| 17 | BKIC_LOC_GLWIP | STRING | 10 | — | GL WIP Account |
| 18 | BKIC_LOC_LCDATE | DATE | 4 | — | Last cycle count date at this location |
| 19 | BKIC_LOC_LOT | STRING | 15 | — | Lot number (for lot-controlled items at this location) |
| 20 | BKIC_LOC_NUM1 | NUMERIC | 8 | — | User-defined numeric field 1 |
| 21 | BKIC_LOC_NUM2 | NUMERIC | 8 | — | User-defined numeric field 2 |
| 22 | BKIC_LOC_PROD | STRING | 15 | — | Part Number |
| 23 | BKIC_LOC_SER | STRING | 25 | — | Serial number (for serial-controlled items at this location) |
| 24 | BKIC_LOC_UALLOC | NUMERIC | 8 | 2 | Units Allocated |
| 25 | BKIC_LOC_UBO | NUMERIC | 8 | 2 | Units on Back Order |
| 26 | BKIC_LOC_UIQC | NUMERIC | 8 | 2 | Units in QC |
| 27 | BKIC_LOC_UOH | NUMERIC | 8 | 2 | Units on Hand |
| 28 | BKIC_LOC_UOO | NUMERIC | 8 | 2 | Units on PO |
| 29 | BKIC_LOC_UOSO | NUMERIC | 8 | 2 | Units on Sales Order |
| 30 | BKIC_LOC_UOWO | NUMERIC | 8 | 2 | Units on Work Order |
| 31 | BKIC_LOC_UWIP | NUMERIC | 8 | 2 | Units in WIP |
| 32 | BKIC_LOC_WHCTRL | STRING | 1 | — | Warehouse control flag (`Y`=this location is under multi-location warehouse control) |

## BKICLOCM
**INVENTORY LOCATION MASTER**

Fields: 12 | Key: BKIC_LOCM_CODE

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
| 11 | BKIC_LOCM_TAX^ | STRING | 20 | — | Tax jurisdiction code for this warehouse location (computed) |
| 12 | BKIC_LOCM_ZIP | STRING | 10 | — | Zip |

## BKICMSTR
**INVENTORY MASTER**

Fields: 64 | Key: BKIC_PROD_CODE

Identical schema to BKICAMTR above. See that table for all field definitions.

## BKICREF
**INVENTORY CROSS-REFERENCE**

Fields: 8 | Key: BKIC_REF_CODE + BKIC_REF_CUST

Maps internal part numbers to customer item numbers and descriptions.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKIC_REF_CODE | STRING | 15 | — | Item Number |
| 2 | BKIC_REF_CUSCOD | STRING | 25 | — | Customer item Number |
| 3 | BKIC_REF_CUSNME | STRING | 30 | — | Customer Name |
| 4 | BKIC_REF_CUST | STRING | 10 | — | Custmer Code |
| 5 | BKIC_REF_DESC | STRING | 30 | — | Customer Description line 1 |
| 6 | BKIC_REF_DESC2 | STRING | 30 | — | Customer Description line 2 |
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

Fields: 2 | Key: MTCLASS_M_CLASS

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MTCLASS_M_CLASS | STRING | 4 | — | Class code (PK) |
| 2 | MTCLASS_M_DESC | STRING | 30 | — | Class description |

## CLASS
**ITEM CLASSES**

Fields: 24 | Key: MTCLASS_CLASS

Defines GL account and department defaults for each product class. Used by
BKICMSTR to route transactions to the correct GL accounts by item class.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | CLASS_DPTA | STRING | 4 | — | GL department for Asset/Expense account |
| 2 | CLASS_DPTC | STRING | 4 | — | GL department for COGS account |
| 3 | CLASS_DPTFOH | STRING | 4 | — | GL department for Factory Overhead account |
| 4 | CLASS_DPTLAB | STRING | 4 | — | GL department for Labor account |
| 5 | CLASS_DPTMISC | STRING | 4 | — | GL department for Miscellaneous account |
| 6 | CLASS_DPTNT | STRING | 4 | — | GL department for Sales Non-Tax account |
| 7 | CLASS_DPTS | STRING | 4 | — | GL department for Sales account |
| 8 | CLASS_DPTVOH | STRING | 4 | — | GL department for Variable Overhead account |
| 9 | CLASS_DPTW | STRING | 4 | — | GL department for WIP (Work In Process) account |
| 10 | CLASS_DPTXTRA | STRING | 4 | — | GL department for Extra/Other account |
| 11 | CLASS_EXTRA | STRING | 50 | — | Extra data |
| 12 | CLASS_GLA | STRING | 10 | — | GL account for Asset/Expense (inventory asset) |
| 13 | CLASS_GLC | STRING | 10 | — | GL account for COGS |
| 14 | CLASS_GLFOH | STRING | 10 | — | GL account for Factory Overhead |
| 15 | CLASS_GLLAB | STRING | 10 | — | GL account for Labor |
| 16 | CLASS_GLMISC | STRING | 10 | — | GL account for Miscellaneous |
| 17 | CLASS_GLS | STRING | 10 | — | GL account for Sales |
| 18 | CLASS_GLSNT | STRING | 10 | — | GL account for Sales Non-Tax |
| 19 | CLASS_GLVOH | STRING | 10 | — | GL account for Variable Overhead |
| 20 | CLASS_GLW | STRING | 10 | — | GL account for WIP (Work In Process) |
| 21 | CLASS_GLXTRA | STRING | 10 | — | GL account for Extra/Other |
| 22 | MTCLASS_CLASS | STRING | 4 | — | Class code (PK; FK → CLASMSTR) |
| 23 | MTCLASS_DESC | STRING | 30 | — | Class description |
| 24 | MTCLASS_LOC | STRING | 10 | — | Default warehouse location for this class |

## DBAFIFO
**FIFO, LIFO BUCKETS**

Fields: 5 | Key: FIFO_PARTNO + FIFO_RECVDATE

One record per cost lot (receipt event) for FIFO/LIFO valuation. Quantities decrement as items are issued.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | FIFO_COST | NUMERIC | 8 | 4 | Unit cost of this FIFO/LIFO cost lot |
| 2 | FIFO_PARTNO | STRING | 15 | — | Part number (FK → BKICMSTR) |
| 3 | FIFO_QTY | NUMERIC | 8 | 2 | Original quantity received into this cost lot |
| 4 | FIFO_RECVDATE | DATE | 4 | — | Date this cost lot was received |
| 5 | FIFO_REMAIN | NUMERIC | 8 | 2 | Remaining quantity in this cost lot (decrements as items are issued) |

## INVATXN
**ARCHIVE INVENTORY TRANSACTIONS**

Fields: 24 | Key: MTIT_CODE + MTIT_DATE

Identical 24-field schema to INVTXN (MTIT_* prefix). Records archived here from INVTXN on period close.
See INVTXN below for all field definitions.

## INVTXN
**INVENTORY TRANSACTIONS**

Fields: 24 | Key: MTIT_CODE + MTIT_DATE

Transaction log for all inventory movements. One record per inventory transaction event.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | MTIT_AVGCOST | NUMERIC | 8 | 4 | Average cost at time of transaction |
| 2 | MTIT_CLASS | STRING | 4 | — | Product class code |
| 3 | MTIT_CODE | STRING | 15 | — | Part number (FK → BKICMSTR) |
| 4 | MTIT_CUST | STRING | 10 | — | Customer code (FK → BKARCUST; if SO-related) |
| 5 | MTIT_DATE | DATE | 4 | — | Transaction date |
| 6 | MTIT_DEPT | STRING | 4 | — | GL department |
| 7 | MTIT_DESC | STRING | 30 | — | Description / reference note |
| 8 | MTIT_EXTRA | STRING | 50 | — | Extra data |
| 9 | MTIT_INVOICE | NUMERIC | 8 | — | Invoice or SO number (if sales-related) |
| 10 | MTIT_LOC | STRING | 10 | — | Warehouse location code (FK → BKICLOCM) |
| 11 | MTIT_LOT | STRING | 15 | — | Lot number (for lot-controlled items) |
| 12 | MTIT_PO | NUMERIC | 8 | — | PO number (if receipt-related) |
| 13 | MTIT_PRICE | NUMERIC | 8 | 4 | Unit price at time of transaction |
| 14 | MTIT_PRODLOT | STRING | 15 | — | Production lot number (for manufactured items) |
| 15 | MTIT_QC | STRING | 2 | — | QC disposition code |
| 16 | MTIT_QTY | NUMERIC | 8 | 2 | Transaction quantity (positive=receipt/addition, negative=issue/deduction) |
| 17 | MTIT_REF | STRING | 30 | — | Reference / document number |
| 18 | MTIT_SCRAP | STRING | 2 | — | Scrap reason code |
| 19 | MTIT_SERIAL | STRING | 25 | — | Serial number (for serial-controlled items) |
| 20 | MTIT_STDCST | NUMERIC | 8 | 6 | Standard cost at time of transaction |
| 21 | MTIT_TYPE | STRING | 1 | — | Transaction type code (I=issue, R=receipt, A=adjustment, etc.) |
| 22 | MTIT_VENDOR | STRING | 10 | — | Vendor code (FK → BKAPVEND; if PO receipt) |
| 23 | MTIT_WOPRE | NUMERIC | 8 | — | Work order prefix (if WO-related) |
| 24 | MTIT_WOSUF | INTEGER | 2 | — | Work order suffix (if WO-related) |

## ISCATMST
**ITEM CATEGORY MASTER LIST**

Fields: 3 | Key: IS_CATM_CODE

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_CATM_CODE | STRING | 4 | — | Category code (PK) |
| 2 | IS_CATM_DESC | STRING | 60 | — | Category description |
| 3 | IS_CATM_EXTRA | STRING | 100 | — | Extra data |

## ISCYCLCD
**CYCLE CODE MASTER**

Fields: 7 | Key: IS_CYCLE_CODE

Controls cycle count frequency for groups of inventory items.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_CYCLE_ALPHA | STRING | 15 | — | User-defined alpha field |
| 2 | IS_CYCLE_CODE | STRING | 4 | — | Cycle count code (PK) |
| 3 | IS_CYCLE_DATE | DATE | 4 | — | Last count date for items on this cycle code |
| 4 | IS_CYCLE_DESC | STRING | 30 | — | Cycle count description |
| 5 | IS_CYCLE_EXTRA | STRING | 50 | — | Extra data |
| 6 | IS_CYCLE_FREQ | INTEGER | 2 | — | Count frequency in days (how often items on this cycle are counted) |
| 7 | IS_CYCLE_NUM | NUMERIC | 8 | — | Number of items assigned to this cycle code |

## ISECO
**ITEM ECO LISTING**

Fields: 12 | Key: IS_ECO_ECO

Engineering Change Orders (ECOs) — tracks authorized changes to part specifications or revision levels.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_ECO_APPBY | STRING | 4 | — | Approved by (user code who authorized this ECO) |
| 2 | IS_ECO_CURRENT | STRING | 1 | — | Current / active ECO flag (`Y`=this ECO is in effect) |
| 3 | IS_ECO_DATE | DATE | 4 | — | ECO effective date |
| 4 | IS_ECO_DRAW | STRING | 15 | — | Drawing number this ECO applies to |
| 5 | IS_ECO_ECO | STRING | 15 | — | ECO number (PK — Engineering Change Order identifier) |
| 6 | IS_ECO_ENTBY | STRING | 4 | — | Entered by (user code who created this record) |
| 7 | IS_ECO_ENTDATE | DATE | 4 | — | Entry date (date this ECO record was created) |
| 8 | IS_ECO_EXTRA | STRING | 100 | — | Extra data |
| 9 | IS_ECO_INVDISP | STRING | 2 | — | Inventory disposition code (how to handle on-hand stock at revision change) |
| 10 | IS_ECO_PART | STRING | 15 | — | Part number this ECO applies to (FK → BKICMSTR) |
| 11 | IS_ECO_REVLVL | STRING | 5 | — | New revision level established by this ECO |
| 12 | IS_ECO_STATUS | STRING | 1 | — | ECO status code (`P`=pending, `A`=approved, `I`=implemented) |

## ISICADT
**INVENTORY MASTER AUDIT FILE**

Fields: 64 | Key: BKIC_PROD_CODE

Identical schema to BKICAMTR above. See that table for all field definitions.

## ISICAMTR
**ARCHIVE INVENTORY MASTER FILE 3**

Fields: 41 | Key: IS_PROD_CODE

Identical 41-field schema to ISICMSTR (IS_PROD_* prefix). Extended part attributes archived on change.
See ISICMSTR below for all field definitions.

## ISICMSTR
**INVENTORY MASTER 3**

Fields: 41 | Key: IS_PROD_CODE

Extended inventory master — supplemental attributes per part (dimensional data, UDFs, dates, flags, ITP).
Joined to BKICMSTR on IS_PROD_CODE = BKIC_PROD_CODE.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_PROD_ADATE | DATE | 4 | — | Audit date (last record modification date) |
| 2 | IS_PROD_ALPHA_1 | STRING | 30 | — | User-defined alpha field 1 |
| 3 | IS_PROD_ALPHA_2 | STRING | 30 | — | User-defined alpha field 2 |
| 4 | IS_PROD_ALPHA_3 | STRING | 30 | — | User-defined alpha field 3 |
| 5 | IS_PROD_ALPHA_4 | STRING | 30 | — | User-defined alpha field 4 |
| 6 | IS_PROD_ALPHA_5 | STRING | 30 | — | User-defined alpha field 5 |
| 7 | IS_PROD_CDATE | DATE | 4 | — | Creation date (record creation date) |
| 8 | IS_PROD_CODE | STRING | 15 | — | Part number (PK; FK → BKICMSTR) |
| 9 | IS_PROD_EXTRA | STRING | 150 | — | Extra data |
| 10 | IS_PROD_FLAG_1 | STRING | 1 | — | User-defined flag 1 |
| 11 | IS_PROD_FLAG_10 | STRING | 1 | — | User-defined flag 10 |
| 12 | IS_PROD_FLAG_2 | STRING | 1 | — | User-defined flag 2 |
| 13 | IS_PROD_FLAG_3 | STRING | 1 | — | User-defined flag 3 |
| 14 | IS_PROD_FLAG_4 | STRING | 1 | — | User-defined flag 4 |
| 15 | IS_PROD_FLAG_5 | STRING | 1 | — | User-defined flag 5 |
| 16 | IS_PROD_FLAG_6 | STRING | 1 | — | User-defined flag 6 |
| 17 | IS_PROD_FLAG_7 | STRING | 1 | — | User-defined flag 7 |
| 18 | IS_PROD_FLAG_8 | STRING | 1 | — | User-defined flag 8 |
| 19 | IS_PROD_FLAG_9 | STRING | 1 | — | User-defined flag 9 |
| 20 | IS_PROD_FOBFULL | NUMERIC | 8 | 2 | Full truckload/container quantity (units per full load; used for freight calculation) |
| 21 | IS_PROD_FOBPAL | NUMERIC | 8 | 2 | Pallet quantity (units per pallet; used for freight calculation) |
| 22 | IS_PROD_GDATES_1 | DATE | 4 | — | User-defined date 1 |
| 23 | IS_PROD_GDATES_2 | DATE | 4 | — | User-defined date 2 |
| 24 | IS_PROD_GDATES_3 | DATE | 4 | — | User-defined date 3 |
| 25 | IS_PROD_GDATES_4 | DATE | 4 | — | User-defined date 4 |
| 26 | IS_PROD_GDATES_5 | DATE | 4 | — | User-defined date 5 |
| 27 | IS_PROD_HI | NUMERIC | 8 | — | Pallet high: number of tiers per pallet (with TI defines pallet configuration) |
| 28 | IS_PROD_HT | NUMERIC | 8 | 2 | Item height (in configured unit of measure) |
| 29 | IS_PROD_ITP | STRING | 20 | — | ITP code (Inspection and Test Plan code; FK → ISITP) |
| 30 | IS_PROD_LG | NUMERIC | 8 | 2 | Item length (in configured unit of measure) |
| 31 | IS_PROD_NUM_1 | NUMERIC | 8 | 2 | User-defined numeric field 1 |
| 32 | IS_PROD_NUM_2 | NUMERIC | 8 | 2 | User-defined numeric field 2 |
| 33 | IS_PROD_NUM_3 | NUMERIC | 8 | 2 | User-defined numeric field 3 |
| 34 | IS_PROD_NUM_4 | NUMERIC | 8 | 2 | User-defined numeric field 4 |
| 35 | IS_PROD_NUM_5 | NUMERIC | 8 | 2 | User-defined numeric field 5 |
| 36 | IS_PROD_RCDATE | DATE | 4 | — | Record creation / revision date |
| 37 | IS_PROD_SLEAD | INTEGER | 2 | — | Supplier lead time in days |
| 38 | IS_PROD_TI | NUMERIC | 8 | — | Pallet tie: number of items per pallet tier (with HI defines pallet configuration) |
| 39 | IS_PROD_TOOL | STRING | 15 | — | Tooling number / tooling code reference |
| 40 | IS_PROD_WD | NUMERIC | 8 | 2 | Item width (in configured unit of measure) |
| 41 | IS_PROD_WT | NUMERIC | 8 | 6 | Item weight |

## ISITMCFG
**AUTO PART GENERATOR**

Fields: 9 | Key: IS_SERC_CLASS

Configuration table for auto-generating part numbers by class using a numeric sequence.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_SERC_CLASS | STRING | 4 | — | Part class code for this auto-generation configuration (PK) |
| 2 | IS_SERC_EXTRA | STRING | 100 | — | Extra data |
| 3 | IS_SERC_ITEM | STRING | 15 | — | Base/template part number prefix |
| 4 | IS_SERC_L2 | INTEGER | 2 | — | Length of segment 2 (character count of the second number block) |
| 5 | IS_SERC_LAST | STRING | 25 | — | Last generated part number (auto-increment tracking) |
| 6 | IS_SERC_LENG | STRING | 2 | — | Total length of the generated part number string |
| 7 | IS_SERC_NUMBER | NUMERIC | 8 | — | Next number in the auto-generation sequence |
| 8 | IS_SERC_SPOS | INTEGER | 2 | — | Start position of the numeric segment within the part number |
| 9 | IS_SERC_TOTAL | INTEGER | 2 | — | Total length of the numeric portion |

## ISITP
**ITP MASTER LISTING**

Fields: 3 | Key: IS_ITP_NUM

Master list of Inspection and Test Plans referenced from ISICMSTR.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_ITP_DESC | STRING | 80 | — | ITP description |
| 2 | IS_ITP_EXTRA | STRING | 100 | — | Extra data |
| 3 | IS_ITP_NUM | STRING | 20 | — | ITP number / code (PK) |

## ISLOCCST
**COST BY WAREHOUSE LOCATION (NOT USED)**

Fields: 7 | Key: IS_LCST_PART + IS_LCST_LOC

Not used in production. Intended to track per-location average cost and book value.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | IS_LCST_AVGC | NUMERIC | 8 | 4 | Average cost at this location |
| 2 | IS_LCST_BOOKVAL | NUMERIC | 8 | 4 | Book value (on-hand qty × average cost) at this location |
| 3 | IS_LCST_EXTRA | STRING | 150 | — | Extra data |
| 4 | IS_LCST_LDATE | DATE | 4 | — | Last transaction date at this location |
| 5 | IS_LCST_LOC | STRING | 10 | — | Warehouse location code (FK → BKICLOCM) |
| 6 | IS_LCST_LTIME | TIME | 4 | — | Last transaction time at this location |
| 7 | IS_LCST_PART | STRING | 15 | — | Part number (FK → BKICMSTR) |

## ISMICADT
**INVENTORY MASTER AUDIT FILE 2**

Fields: 109 | Key: MTIC_PROD_CODE

Identical 109-field schema to MTICAMTR and MTICMSTR (MTIC_PROD_* prefix). Extended
inventory master 2 records archived here on change/delete.

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
| 20 | MTIC_PROD_FRT^ | NUMERIC | 8 | 2 | Freight dollar amount (computed: FRT% × unit cost) |
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
| 34 | MTIC_PROD_OPTPR | INTEGER | 2 | — | Option pricing type code |
| 35 | MTIC_PROD_PCONV | NUMERIC | 8 | 5 | PO Conversion Multiplier |
| 36 | MTIC_PROD_PUM | STRING | 3 | — | Purchase Unit Measure |
| 37 | MTIC_PROD_RCOST_1 | NUMERIC | 8 | 6 | Replacement/retail cost tier 1 |
| 38 | MTIC_PROD_RCOST_10 | NUMERIC | 8 | 6 | Replacement/retail cost tier 10 |
| 39 | MTIC_PROD_RCOST_11 | NUMERIC | 8 | 6 | Replacement/retail cost tier 11 |
| 40 | MTIC_PROD_RCOST_12 | NUMERIC | 8 | 6 | Replacement/retail cost tier 12 |
| 41 | MTIC_PROD_RCOST_13 | NUMERIC | 8 | 6 | Replacement/retail cost tier 13 |
| 42 | MTIC_PROD_RCOST_14 | NUMERIC | 8 | 6 | Replacement/retail cost tier 14 |
| 43 | MTIC_PROD_RCOST_15 | NUMERIC | 8 | 6 | Replacement/retail cost tier 15 |
| 44 | MTIC_PROD_RCOST_2 | NUMERIC | 8 | 6 | Replacement/retail cost tier 2 |
| 45 | MTIC_PROD_RCOST_3 | NUMERIC | 8 | 6 | Replacement/retail cost tier 3 |
| 46 | MTIC_PROD_RCOST_4 | NUMERIC | 8 | 6 | Replacement/retail cost tier 4 |
| 47 | MTIC_PROD_RCOST_5 | NUMERIC | 8 | 6 | Replacement/retail cost tier 5 |
| 48 | MTIC_PROD_RCOST_6 | NUMERIC | 8 | 6 | Replacement/retail cost tier 6 |
| 49 | MTIC_PROD_RCOST_7 | NUMERIC | 8 | 6 | Replacement/retail cost tier 7 |
| 50 | MTIC_PROD_RCOST_8 | NUMERIC | 8 | 6 | Replacement/retail cost tier 8 |
| 51 | MTIC_PROD_RCOST_9 | NUMERIC | 8 | 6 | Replacement/retail cost tier 9 |
| 52 | MTIC_PROD_REV | STRING | 5 | — | Revision Level |
| 53 | MTIC_PROD_SER | STRING | 1 | — | Serial Control Y/N |
| 54 | MTIC_PROD_SPECS_1 | STRING | 30 | — | Product specification line 1 |
| 55 | MTIC_PROD_SPECS_10 | STRING | 30 | — | Product specification line 10 |
| 56 | MTIC_PROD_SPECS_11 | STRING | 30 | — | Product specification line 11 |
| 57 | MTIC_PROD_SPECS_12 | STRING | 30 | — | Product specification line 12 |
| 58 | MTIC_PROD_SPECS_2 | STRING | 30 | — | Product specification line 2 |
| 59 | MTIC_PROD_SPECS_3 | STRING | 30 | — | Product specification line 3 |
| 60 | MTIC_PROD_SPECS_4 | STRING | 30 | — | Product specification line 4 |
| 61 | MTIC_PROD_SPECS_5 | STRING | 30 | — | Product specification line 5 |
| 62 | MTIC_PROD_SPECS_6 | STRING | 30 | — | Product specification line 6 |
| 63 | MTIC_PROD_SPECS_7 | STRING | 30 | — | Product specification line 7 |
| 64 | MTIC_PROD_SPECS_8 | STRING | 30 | — | Product specification line 8 |
| 65 | MTIC_PROD_SPECS_9 | STRING | 30 | — | Product specification line 9 |
| 66 | MTIC_PROD_STDC | NUMERIC | 8 | 6 | Not Used |
| 67 | MTIC_PROD_STDPK | NUMERIC | 8 | — | Standard Pack Quantity |
| 68 | MTIC_PROD_SUBST_1 | STRING | 25 | — | Substitute part number 1 (alternate part code for substitution) |
| 69 | MTIC_PROD_SUBST_2 | STRING | 25 | — | Substitute part number 2 |
| 70 | MTIC_PROD_SUBST_3 | STRING | 25 | — | Substitute part number 3 |
| 71 | MTIC_PROD_SUBST_4 | STRING | 25 | — | Substitute part number 4 |
| 72 | MTIC_PROD_SUBST_5 | STRING | 25 | — | Substitute part number 5 |
| 73 | MTIC_PROD_SUM | STRING | 3 | — | Sales Unit Measure |
| 74 | MTIC_PROD_TYPE | STRING | 1 | — | Product TYPE (RFAMKLTBO) |
| 75 | MTIC_PROD_UIQC | NUMERIC | 8 | 2 | Units in QC |
| 76 | MTIC_PROD_UIWIP | NUMERIC | 8 | 2 | Units in WIP |
| 77 | MTIC_PROD_UOA | NUMERIC | 8 | 2 | Units On Allocations |
| 78 | MTIC_PROD_UOWO | NUMERIC | 8 | 2 | Units On Work Order |
| 79 | MTIC_PROD_VEND_1 | STRING | 10 | — | Approved vendor code 1 (FK → BKAPVEND) |
| 80 | MTIC_PROD_VEND_10 | STRING | 10 | — | Approved vendor code 10 |
| 81 | MTIC_PROD_VEND_2 | STRING | 10 | — | Approved vendor code 2 |
| 82 | MTIC_PROD_VEND_3 | STRING | 10 | — | Approved vendor code 3 |
| 83 | MTIC_PROD_VEND_4 | STRING | 10 | — | Approved vendor code 4 |
| 84 | MTIC_PROD_VEND_5 | STRING | 10 | — | Approved vendor code 5 |
| 85 | MTIC_PROD_VEND_6 | STRING | 10 | — | Approved vendor code 6 |
| 86 | MTIC_PROD_VEND_7 | STRING | 10 | — | Approved vendor code 7 |
| 87 | MTIC_PROD_VEND_8 | STRING | 10 | — | Approved vendor code 8 |
| 88 | MTIC_PROD_VEND_9 | STRING | 10 | — | Approved vendor code 9 |
| 89 | MTIC_PROD_VNAM_1 | STRING | 30 | — | Vendor name 1 (display name for VEND_1) |
| 90 | MTIC_PROD_VNAM_10 | STRING | 30 | — | Vendor name 10 |
| 91 | MTIC_PROD_VNAM_2 | STRING | 30 | — | Vendor name 2 |
| 92 | MTIC_PROD_VNAM_3 | STRING | 30 | — | Vendor name 3 |
| 93 | MTIC_PROD_VNAM_4 | STRING | 30 | — | Vendor name 4 |
| 94 | MTIC_PROD_VNAM_5 | STRING | 30 | — | Vendor name 5 |
| 95 | MTIC_PROD_VNAM_6 | STRING | 30 | — | Vendor name 6 |
| 96 | MTIC_PROD_VNAM_7 | STRING | 30 | — | Vendor name 7 |
| 97 | MTIC_PROD_VNAM_8 | STRING | 30 | — | Vendor name 8 |
| 98 | MTIC_PROD_VNAM_9 | STRING | 30 | — | Vendor name 9 |
| 99 | MTIC_PROD_VPC_1 | STRING | 20 | — | Vendor part code 1 (vendor's catalog number for VEND_1) |
| 100 | MTIC_PROD_VPC_2 | STRING | 20 | — | Vendor part code 2 |
| 101 | MTIC_PROD_VPC_3 | STRING | 20 | — | Vendor part code 3 |
| 102 | MTIC_PROD_VPC_4 | STRING | 20 | — | Vendor part code 4 |
| 103 | MTIC_PROD_VPC_5 | STRING | 20 | — | Vendor part code 5 |
| 104 | MTIC_PROD_VPC_6 | STRING | 20 | — | Vendor part code 6 |
| 105 | MTIC_PROD_VPC_7 | STRING | 20 | — | Vendor part code 7 |
| 106 | MTIC_PROD_VPC_8 | STRING | 20 | — | Vendor part code 8 |
| 107 | MTIC_PROD_VPC_9 | STRING | 20 | — | Vendor part code 9 |
| 108 | MTIC_PROD_WIPDP | STRING | 4 | — | GL WIP Department |
| 109 | MTIC_PROD_WT | NUMERIC | 8 | 6 | Weight |

## MTICAMTR
**INVENTORY ARCHIVE MASTER 2**

Fields: 109 | Key: MTIC_PROD_CODE

Identical schema to ISMICADT above. See that table for all field definitions.

## MTICMSTR
**INVENTORY MASTER 2**

Fields: 109 | Key: MTIC_PROD_CODE

Identical schema to ISMICADT above. See that table for all field definitions.

**Confidence: 78/100** — BKICMSTR/BKICLOC/BKICLOCM core fields confirmed from standard inventory
master context; BKIC_PROD_NGLYR/MTD/VAR/YTD inferred as Net Gross Profit metrics matching
LYR/MTD/VAR/YTD naming pattern of surrounding GSLYR/NSLYR/CLYR fields; BKIC_PROD_PMAT as price
matrix code inferred from INTEGER type and CLASS table FK pattern; IS_PROD_HI/TI as pallet-config
tie/high from retail/EDI standards context; INVTXN transaction type codes, ISECO status codes,
MTIC_PROD_RCOST tier usage, and BKIC_PROD_TO turnover ratio confirmed from field-name semantics;
exact option pricing codes (OPTPR) and flag semantics require RWN decryption to verify.
