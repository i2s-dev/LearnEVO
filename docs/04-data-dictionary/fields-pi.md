# PI — Physical Inventory: Field Reference

Status: verified-schema

Source: `Evo-DBA_File_Fields 052421.xlsx`, sheet "Fields".
Field descriptions where provided by source; otherwise name-inferred.

---

## BKPIFROZ
**FROZEN PHYSICAL INVENTORY**

Fields: 19

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKPH_INFO_ACCTA | STRING | 10 | — | Asset GL Account Posted |
| 2 | BKPH_INFO_ACCTC | STRING | 10 | — | COGS GL Account Posted |
| 3 | BKPH_INFO_COST | NUMERIC | 8 | 6 | Frozen Unit Cost |
| 4 | BKPH_INFO_DEPTA | STRING | 4 | — | Asset GL Department |
| 5 | BKPH_INFO_DEPTC | STRING | 4 | — | COGS GL Department |
| 6 | BKPH_INFO_FDATE | DATE | 4 | — | Inventory Freeze Date |
| 7 | BKPH_INFO_GLPST | STRING | 1 | — | Posted to GL Y/N |
| 8 | BKPH_INFO_INPST | STRING | 1 | — | Posted to Inventory Y/N |
| 9 | BKPH_INFO_LOC | STRING | 10 | — | Location |
| 10 | BKPH_INFO_LOT | STRING | 1 | — | Lot Controlled Y/N |
| 11 | BKPH_INFO_PADJ | NUMERIC | 8 | 2 | $ Amount Adjusted - Asset +/- |
| 12 | BKPH_INFO_PCOST | NUMERIC | 8 | 6 | Unit Cost Actually Posted |
| 13 | BKPH_INFO_PROD | STRING | 15 | — | Part Number |
| 14 | BKPH_INFO_PUNIT | NUMERIC | 8 | 2 | Unit Change posted by PO-G |
| 15 | BKPH_INFO_QTR | STRING | 2 | — | Inventory Number |
| 16 | BKPH_INFO_SER | STRING | 1 | — | Serial Controlled Y/N |
| 17 | BKPH_INFO_TAGS | INTEGER | 2 | — | Number of Tags Entered |
| 18 | BKPH_INFO_UOH | NUMERIC | 8 | 2 | Units On-Hand |
| 19 | BKPH_INFO_YEAR | STRING | 4 | — | Inventory Year |

## BKPILCNT
**COUNTED LOTS**

Fields: 10

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKPI_LOT_BIN | STRING | 15 | — | — |
| 2 | BKPI_LOT_CODE | STRING | 15 | — | Part Number |
| 3 | BKPI_LOT_LOC | STRING | 10 | — | Location |
| 4 | BKPI_LOT_LOT | STRING | 15 | — | Lot Number |
| 5 | BKPI_LOT_PSTD | STRING | 1 | — | Lot Record Posted Back to Inventory Y/N |
| 6 | BKPI_LOT_QTR | STRING | 2 | — | Inventory Number |
| 7 | BKPI_LOT_QTY | NUMERIC | 8 | 2 | Quantity |
| 8 | BKPI_LOT_SERQTY | NUMERIC | 8 | 2 | Unit On-Hand Total of Serials for This Lot |
| 9 | BKPI_LOT_TAG | NUMERIC | 8 | — | Tag Number |
| 10 | BKPI_LOT_YEAR | STRING | 4 | — | Inventory Year |

## BKPILOT
**FROZEN PI LOTS**

Fields: 10

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKPI_LOT_BIN | STRING | 15 | — | — |
| 2 | BKPI_LOT_CODE | STRING | 15 | — | Part Number |
| 3 | BKPI_LOT_LOC | STRING | 10 | — | Location |
| 4 | BKPI_LOT_LOT | STRING | 15 | — | Lot Number |
| 5 | BKPI_LOT_PSTD | STRING | 1 | — | Lot Record Posted Back to Inventory Y/N |
| 6 | BKPI_LOT_QTR | STRING | 2 | — | Inventory Number |
| 7 | BKPI_LOT_QTY | NUMERIC | 8 | 2 | Quantity |
| 8 | BKPI_LOT_SERQTY | NUMERIC | 8 | 2 | Unit On-Hand Total of Serials for This Lot |
| 9 | BKPI_LOT_TAG | NUMERIC | 8 | — | Tag Number |
| 10 | BKPI_LOT_YEAR | STRING | 4 | — | Inventory Year |

## BKPIMSTR
**PHYSICAL INVENTORY MASTER**

Fields: 3

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKPI_MSTR_DESC | STRING | 30 | — | Description |
| 2 | BKPI_MSTR_QTR | STRING | 2 | — | Inventory Number |
| 3 | BKPI_MSTR_YEAR | STRING | 4 | — | Inventory Year |

## BKPIPHYS
**TAG FILE**

Fields: 14

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKPH_ACTQTY | NUMERIC | 8 | 2 | Quantity Counted |
| 2 | BKPH_BIN | STRING | 10 | — | Bin Location |
| 3 | BKPH_CODE | STRING | 15 | — | Part Number |
| 4 | BKPH_COMMENT | STRING | 30 | — | Comment |
| 5 | BKPH_COUNTDATE | DATE | 4 | — | Count Date |
| 6 | BKPH_EMPNAME | STRING | 15 | — | Employee Name |
| 7 | BKPH_EMPNUM | INTEGER | 2 | — | Employee Number |
| 8 | BKPH_FDATE | DATE | 4 | — | Freeze Date |
| 9 | BKPH_LOC | STRING | 10 | — | Location |
| 10 | BKPH_LOT | STRING | 15 | — | Lot Number |
| 11 | BKPH_QTR | STRING | 2 | — | PI Number |
| 12 | BKPH_SERIAL | STRING | 25 | — | Serial Number |
| 13 | BKPH_TAGNUM | NUMERIC | 8 | — | Tag Number |
| 14 | BKPH_YEAR | STRING | 4 | — | PI Year |

## BKPISCNT
**COUNTED SERIAL NUMBERS**

Fields: 10

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKPI_SER_BIN | STRING | 15 | — | — |
| 2 | BKPI_SER_CODE | STRING | 15 | — | Part Number |
| 3 | BKPI_SER_LOC | STRING | 10 | — | Location for this Serial Number |
| 4 | BKPI_SER_LOTNO | STRING | 15 | — | Lot # for this Serial if both Lot/Serial |
| 5 | BKPI_SER_PSTD | STRING | 1 | — | Serial Record Posted to Inventory Y/N |
| 6 | BKPI_SER_QTR | STRING | 2 | — | Inventory Number |
| 7 | BKPI_SER_QTY | NUMERIC | 8 | 2 | Quantity |
| 8 | BKPI_SER_SERIAL | STRING | 25 | — | Serial Number |
| 9 | BKPI_SER_TAG | NUMERIC | 8 | — | Tag Number |
| 10 | BKPI_SER_YEAR | STRING | 4 | — | Inventory Year |

## BKPISER
**FROZEN SERIAL NUMBERS**

Fields: 10

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKPI_SER_BIN | STRING | 15 | — | — |
| 2 | BKPI_SER_CODE | STRING | 15 | — | Part Number |
| 3 | BKPI_SER_LOC | STRING | 10 | — | Location for this Serial Number |
| 4 | BKPI_SER_LOTNO | STRING | 15 | — | Lot # for this Serial if both Lot/Serial |
| 5 | BKPI_SER_PSTD | STRING | 1 | — | Serial Record Posted to Inventory Y/N |
| 6 | BKPI_SER_QTR | STRING | 2 | — | Inventory Number |
| 7 | BKPI_SER_QTY | NUMERIC | 8 | 2 | Quantity |
| 8 | BKPI_SER_SERIAL | STRING | 25 | — | Serial Number |
| 9 | BKPI_SER_TAG | NUMERIC | 8 | — | Tag Number |
| 10 | BKPI_SER_YEAR | STRING | 4 | — | Inventory Year |

## PIBINLOC
**PI BIN LOCATION**

Fields: 14

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | PIBIN_LOC_BIN | STRING | 15 | — | — |
| 2 | PIBIN_LOC_CDATE | DATE | 4 | — | — |
| 3 | PIBIN_LOC_DFLT | STRING | 1 | — | — |
| 4 | PIBIN_LOC_EXTRA | STRING | 100 | — | — |
| 5 | PIBIN_LOC_FDATE | DATE | 4 | — | — |
| 6 | PIBIN_LOC_ITEM | STRING | 15 | — | — |
| 7 | PIBIN_LOC_LOC | STRING | 10 | — | — |
| 8 | PIBIN_LOC_LOT | STRING | 15 | — | — |
| 9 | PIBIN_LOC_QTR | STRING | 2 | — | — |
| 10 | PIBIN_LOC_RVLVL | STRING | 5 | — | — |
| 11 | PIBIN_LOC_SER | STRING | 25 | — | — |
| 12 | PIBIN_LOC_UOH | NUMERIC | 8 | 2 | — |
| 13 | PIBIN_LOC_VDATE | DATE | 4 | — | — |
| 14 | PIBIN_LOC_YEAR | STRING | 4 | — | — |

## PIBINLOT
**PI LOT BIN LOCATION**

Fields: 14

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | PI_BINLOT_BIN | STRING | 15 | — | — |
| 2 | PI_BINLOT_DATE | DATE | 4 | — | — |
| 3 | PI_BINLOT_EXTRA | STRING | 50 | — | — |
| 4 | PI_BINLOT_FLAG | STRING | 1 | — | — |
| 5 | PI_BINLOT_ITEM | STRING | 15 | — | — |
| 6 | PI_BINLOT_LOC | STRING | 10 | — | — |
| 7 | PI_BINLOT_LOT | STRING | 15 | — | — |
| 8 | PI_BINLOT_NUM | NUMERIC | 8 | — | — |
| 9 | PI_BINLOT_PSTD | STRING | 1 | — | — |
| 10 | PI_BINLOT_QTR | STRING | 2 | — | — |
| 11 | PI_BINLOT_SER | STRING | 25 | — | — |
| 12 | PI_BINLOT_SQTY | NUMERIC | 8 | 2 | — |
| 13 | PI_BINLOT_UOH | NUMERIC | 8 | 2 | — |
| 14 | PI_BINLOT_YR | STRING | 4 | — | — |
