# FO — Features & Options: Field Reference

Status: verified-schema + completed field meanings (Pass 574f, 2026-07-06).

Source: `Evo-DBA_File_Fields 052421.xlsx`, sheet "Fields". No Excel descriptions provided;
all field meanings inferred from naming + FO module purpose.

The FO module enables configurable product sales — customers select options from a
product option tree (ISFOLINE), which generates a configuration header (ISFOHEAD),
and converts to SO lines (ISFOORDL). History is tracked in ISFOHIST. ISFOBMRM holds
remarks for individual BOM line options. BKFOCFG is the module configuration singleton.

---

## BKFOCFG
**FEATURES & OPTIONS CONFIGURATION** — module configuration singleton

Fields: 18 | Key: singleton (one record)

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKFO_CFG_EXTRA | STRING | 50 | — | User-defined extra data |
| 2 | BKFO_CFG_MANFET | STRING | 1 | — | Mandatory features flag: `Y`=features must be selected before order confirmation |
| 3 | BKFO_CFG_OPCODE | STRING | 5 | — | Default operation code used when creating new configurations |
| 4 | BKFO_CFG_YN_1 | STRING | 1 | — | FO behavior flag 1 (Y/N — exact meaning requires RWN decryption) |
| 5 | BKFO_CFG_YN_10 | STRING | 1 | — | FO behavior flag 10 |
| 6 | BKFO_CFG_YN_11 | STRING | 1 | — | FO behavior flag 11 |
| 7 | BKFO_CFG_YN_12 | STRING | 1 | — | FO behavior flag 12 |
| 8 | BKFO_CFG_YN_13 | STRING | 1 | — | FO behavior flag 13 |
| 9 | BKFO_CFG_YN_14 | STRING | 1 | — | FO behavior flag 14 |
| 10 | BKFO_CFG_YN_15 | STRING | 1 | — | FO behavior flag 15 |
| 11 | BKFO_CFG_YN_2 | STRING | 1 | — | FO behavior flag 2 |
| 12 | BKFO_CFG_YN_3 | STRING | 1 | — | FO behavior flag 3 |
| 13 | BKFO_CFG_YN_4 | STRING | 1 | — | FO behavior flag 4 |
| 14 | BKFO_CFG_YN_5 | STRING | 1 | — | FO behavior flag 5 |
| 15 | BKFO_CFG_YN_6 | STRING | 1 | — | FO behavior flag 6 |
| 16 | BKFO_CFG_YN_7 | STRING | 1 | — | FO behavior flag 7 |
| 17 | BKFO_CFG_YN_8 | STRING | 1 | — | FO behavior flag 8 |
| 18 | BKFO_CFG_YN_9 | STRING | 1 | — | FO behavior flag 9 |

## ISFOBMRM
**CONFIGURATION LINE REMARKS** — notes/remarks for individual option BOM lines

Fields: 20 | Key: ISFO_BRM_PARENT + ISFO_BRM_COMP + ISFO_BRM_LINE

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISFO_BRM_COMP | STRING | 15 | — | Component item code (the option/part this remark belongs to) |
| 2 | ISFO_BRM_EXTRA | STRING | 100 | — | Extra data |
| 3 | ISFO_BRM_LINE | INTEGER | 2 | — | Remark line number (sequence within this option) |
| 4 | ISFO_BRM_PARENT | STRING | 15 | — | Parent configuration item code |
| 5 | ISFO_BRM_REMARK_1 | STRING | 64 | — | Remark/note line 1 |
| 6 | ISFO_BRM_REMARK_10 | STRING | 64 | — | Remark/note line 10 |
| 7 | ISFO_BRM_REMARK_11 | STRING | 64 | — | Remark/note line 11 |
| 8 | ISFO_BRM_REMARK_12 | STRING | 64 | — | Remark/note line 12 |
| 9 | ISFO_BRM_REMARK_13 | STRING | 64 | — | Remark/note line 13 |
| 10 | ISFO_BRM_REMARK_14 | STRING | 64 | — | Remark/note line 14 |
| 11 | ISFO_BRM_REMARK_15 | STRING | 64 | — | Remark/note line 15 |
| 12 | ISFO_BRM_REMARK_2 | STRING | 64 | — | Remark/note line 2 |
| 13 | ISFO_BRM_REMARK_3 | STRING | 64 | — | Remark/note line 3 |
| 14 | ISFO_BRM_REMARK_4 | STRING | 64 | — | Remark/note line 4 |
| 15 | ISFO_BRM_REMARK_5 | STRING | 64 | — | Remark/note line 5 |
| 16 | ISFO_BRM_REMARK_6 | STRING | 64 | — | Remark/note line 6 |
| 17 | ISFO_BRM_REMARK_7 | STRING | 64 | — | Remark/note line 7 |
| 18 | ISFO_BRM_REMARK_8 | STRING | 64 | — | Remark/note line 8 |
| 19 | ISFO_BRM_REMARK_9 | STRING | 64 | — | Remark/note line 9 |
| 20 | ISFO_BRM_UID | STRING | 40 | — | Unique ID (links this remark to its parent configuration record) |

## ISFOHEAD
**CONFIGURATION HEADER** — one record per product configuration session

Fields: 16 | Key: ISFO_HDR_UID

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISFO_HDR_CUST | STRING | 10 | — | Customer code (FK → BKARCUST) |
| 2 | ISFO_HDR_DATE | DATE | 4 | — | Configuration created date |
| 3 | ISFO_HDR_DESC | STRING | 30 | — | Configuration description |
| 4 | ISFO_HDR_EXTRA | STRING | 150 | — | Extra data |
| 5 | ISFO_HDR_MDATES_1 | DATE | 4 | — | Milestone date 1 (delivery schedule slot 1) |
| 6 | ISFO_HDR_MDATES_2 | DATE | 4 | — | Milestone date 2 |
| 7 | ISFO_HDR_MDATES_3 | DATE | 4 | — | Milestone date 3 |
| 8 | ISFO_HDR_MDATES_4 | DATE | 4 | — | Milestone date 4 |
| 9 | ISFO_HDR_MDATES_5 | DATE | 4 | — | Milestone date 5 |
| 10 | ISFO_HDR_PARENT | STRING | 15 | — | Root parent item code being configured (FK → BKICMSTR) |
| 11 | ISFO_HDR_PERM | STRING | 1 | — | Permanent flag: `Y`=save configuration record, `N`=temporary/working |
| 12 | ISFO_HDR_REV | STRING | 5 | — | Configuration revision number |
| 13 | ISFO_HDR_RFQ | STRING | 20 | — | RFQ/quote reference number |
| 14 | ISFO_HDR_STATUS | STRING | 15 | — | Configuration status (e.g., Quoted, Confirmed, Shipped) |
| 15 | ISFO_HDR_UID | STRING | 40 | — | Unique configuration ID (PK) |
| 16 | ISFO_HDR_VEND | STRING | 10 | — | Vendor code (if vendor-supplied configuration) |

## ISFOHIST
**CONFIGURATION HISTORY** — conversion and status change log for configurations

Fields: 15 | Key: ISFO_HIST_UID + ISFO_HIST_DATE

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISFO_HIST_CITEM | STRING | 15 | — | Configuration item code (item that was configured) |
| 2 | ISFO_HIST_CV | STRING | 10 | — | Configuration version at this history point |
| 3 | ISFO_HIST_CVTNO | NUMERIC | 8 | — | Conversion document number (SO/PO/WO created from this config) |
| 4 | ISFO_HIST_CVTTO | STRING | 4 | — | Conversion type code (SO=Sales Order, WO=Work Order, PO=Purchase Order) |
| 5 | ISFO_HIST_DATE | DATE | 4 | — | History record date |
| 6 | ISFO_HIST_DDATE | DATE | 4 | — | Delivery date at this history point |
| 7 | ISFO_HIST_EXTRA | STRING | 100 | — | Extra data |
| 8 | ISFO_HIST_LOC | STRING | 10 | — | Warehouse location |
| 9 | ISFO_HIST_PART | STRING | 15 | — | Parent item code |
| 10 | ISFO_HIST_PRICE | NUMERIC | 8 | 2 | Configuration price at this history point |
| 11 | ISFO_HIST_QTY | NUMERIC | 8 | 4 | Quantity |
| 12 | ISFO_HIST_STATU | STRING | 40 | — | Status description (free-text status at this history point) |
| 13 | ISFO_HIST_TIME | TIME | 4 | — | Time of event |
| 14 | ISFO_HIST_UID | STRING | 40 | — | Configuration unique ID (FK → ISFOHEAD.ISFO_HDR_UID) |
| 15 | ISFO_HIST_WHO | STRING | 20 | — | User who created/modified this history record |

## ISFOLINE
**CONFIGURATION LINES** — option BOM lines with 50+6 option flag bits

Fields: 78 | Key: ISFO_LIN_UID + ISFO_LIN_LINEN

One row per configurable BOM component. The 50 OPFLAG bits represent which product
options have been selected for this line item. The 6 OPYN slots are additional Y/N flags.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISFO_LIN_BEXTRA | STRING | 50 | — | Branch extra data |
| 2 | ISFO_LIN_CBRANC | INTEGER | 2 | — | Child branch number (position in option tree branching) |
| 3 | ISFO_LIN_COMP | STRING | 15 | — | Component item code for this option line |
| 4 | ISFO_LIN_DATE1 | DATE | 4 | — | Effective-from date (when this option became available) |
| 5 | ISFO_LIN_DATE2 | DATE | 4 | — | Expiry date (when this option was discontinued) |
| 6 | ISFO_LIN_DUPOP | STRING | 1 | — | Duplicate option flag: `Y`=allow same option selected multiple times |
| 7 | ISFO_LIN_EXTRA | STRING | 150 | — | Extra data |
| 8 | ISFO_LIN_LEVEL | INTEGER | 2 | — | BOM tree level number (1=top, higher=deeper) |
| 9 | ISFO_LIN_LINEN | INTEGER | 2 | — | Line number within this configuration level |
| 10 | ISFO_LIN_OP | STRING | 3 | — | Option code (3-char: identifies which product option this represents) |
| 11 | ISFO_LIN_OPDSC | STRING | 5 | — | Option description code (5-char label) |
| 12 | ISFO_LIN_OPFLAG_1 | STRING | 1 | — | Option flag slot 1: `Y`=this option selected for this configuration line |
| 13 | ISFO_LIN_OPFLAG_10 | STRING | 1 | — | Option flag slot 10 |
| 14 | ISFO_LIN_OPFLAG_11 | STRING | 1 | — | Option flag slot 11 |
| 15 | ISFO_LIN_OPFLAG_12 | STRING | 1 | — | Option flag slot 12 |
| 16 | ISFO_LIN_OPFLAG_13 | STRING | 1 | — | Option flag slot 13 |
| 17 | ISFO_LIN_OPFLAG_14 | STRING | 1 | — | Option flag slot 14 |
| 18 | ISFO_LIN_OPFLAG_15 | STRING | 1 | — | Option flag slot 15 |
| 19 | ISFO_LIN_OPFLAG_16 | STRING | 1 | — | Option flag slot 16 |
| 20 | ISFO_LIN_OPFLAG_17 | STRING | 1 | — | Option flag slot 17 |
| 21 | ISFO_LIN_OPFLAG_18 | STRING | 1 | — | Option flag slot 18 |
| 22 | ISFO_LIN_OPFLAG_19 | STRING | 1 | — | Option flag slot 19 |
| 23 | ISFO_LIN_OPFLAG_2 | STRING | 1 | — | Option flag slot 2 |
| 24 | ISFO_LIN_OPFLAG_20 | STRING | 1 | — | Option flag slot 20 |
| 25 | ISFO_LIN_OPFLAG_21 | STRING | 1 | — | Option flag slot 21 |
| 26 | ISFO_LIN_OPFLAG_22 | STRING | 1 | — | Option flag slot 22 |
| 27 | ISFO_LIN_OPFLAG_23 | STRING | 1 | — | Option flag slot 23 |
| 28 | ISFO_LIN_OPFLAG_24 | STRING | 1 | — | Option flag slot 24 |
| 29 | ISFO_LIN_OPFLAG_25 | STRING | 1 | — | Option flag slot 25 |
| 30 | ISFO_LIN_OPFLAG_26 | STRING | 1 | — | Option flag slot 26 |
| 31 | ISFO_LIN_OPFLAG_27 | STRING | 1 | — | Option flag slot 27 |
| 32 | ISFO_LIN_OPFLAG_28 | STRING | 1 | — | Option flag slot 28 |
| 33 | ISFO_LIN_OPFLAG_29 | STRING | 1 | — | Option flag slot 29 |
| 34 | ISFO_LIN_OPFLAG_3 | STRING | 1 | — | Option flag slot 3 |
| 35 | ISFO_LIN_OPFLAG_30 | STRING | 1 | — | Option flag slot 30 |
| 36 | ISFO_LIN_OPFLAG_31 | STRING | 1 | — | Option flag slot 31 |
| 37 | ISFO_LIN_OPFLAG_32 | STRING | 1 | — | Option flag slot 32 |
| 38 | ISFO_LIN_OPFLAG_33 | STRING | 1 | — | Option flag slot 33 |
| 39 | ISFO_LIN_OPFLAG_34 | STRING | 1 | — | Option flag slot 34 |
| 40 | ISFO_LIN_OPFLAG_35 | STRING | 1 | — | Option flag slot 35 |
| 41 | ISFO_LIN_OPFLAG_36 | STRING | 1 | — | Option flag slot 36 |
| 42 | ISFO_LIN_OPFLAG_37 | STRING | 1 | — | Option flag slot 37 |
| 43 | ISFO_LIN_OPFLAG_38 | STRING | 1 | — | Option flag slot 38 |
| 44 | ISFO_LIN_OPFLAG_39 | STRING | 1 | — | Option flag slot 39 |
| 45 | ISFO_LIN_OPFLAG_4 | STRING | 1 | — | Option flag slot 4 |
| 46 | ISFO_LIN_OPFLAG_40 | STRING | 1 | — | Option flag slot 40 |
| 47 | ISFO_LIN_OPFLAG_41 | STRING | 1 | — | Option flag slot 41 |
| 48 | ISFO_LIN_OPFLAG_42 | STRING | 1 | — | Option flag slot 42 |
| 49 | ISFO_LIN_OPFLAG_43 | STRING | 1 | — | Option flag slot 43 |
| 50 | ISFO_LIN_OPFLAG_44 | STRING | 1 | — | Option flag slot 44 |
| 51 | ISFO_LIN_OPFLAG_45 | STRING | 1 | — | Option flag slot 45 |
| 52 | ISFO_LIN_OPFLAG_46 | STRING | 1 | — | Option flag slot 46 |
| 53 | ISFO_LIN_OPFLAG_47 | STRING | 1 | — | Option flag slot 47 |
| 54 | ISFO_LIN_OPFLAG_48 | STRING | 1 | — | Option flag slot 48 |
| 55 | ISFO_LIN_OPFLAG_49 | STRING | 1 | — | Option flag slot 49 |
| 56 | ISFO_LIN_OPFLAG_5 | STRING | 1 | — | Option flag slot 5 |
| 57 | ISFO_LIN_OPFLAG_50 | STRING | 1 | — | Option flag slot 50 |
| 58 | ISFO_LIN_OPFLAG_6 | STRING | 1 | — | Option flag slot 6 |
| 59 | ISFO_LIN_OPFLAG_7 | STRING | 1 | — | Option flag slot 7 |
| 60 | ISFO_LIN_OPFLAG_8 | STRING | 1 | — | Option flag slot 8 |
| 61 | ISFO_LIN_OPFLAG_9 | STRING | 1 | — | Option flag slot 9 |
| 62 | ISFO_LIN_OPYN_1 | STRING | 1 | — | Additional Y/N option flag 1 |
| 63 | ISFO_LIN_OPYN_2 | STRING | 1 | — | Additional Y/N option flag 2 |
| 64 | ISFO_LIN_OPYN_3 | STRING | 1 | — | Additional Y/N option flag 3 |
| 65 | ISFO_LIN_OPYN_4 | STRING | 1 | — | Additional Y/N option flag 4 |
| 66 | ISFO_LIN_OPYN_5 | STRING | 1 | — | Additional Y/N option flag 5 |
| 67 | ISFO_LIN_OPYN_6 | STRING | 1 | — | Additional Y/N option flag 6 |
| 68 | ISFO_LIN_PARENT | STRING | 15 | — | Parent configuration item code |
| 69 | ISFO_LIN_PBRANC | INTEGER | 2 | — | Parent branch number (position in tree under parent) |
| 70 | ISFO_LIN_PRICE | NUMERIC | 8 | 4 | Unit price for this option component |
| 71 | ISFO_LIN_QTYREQ | NUMERIC | 8 | 8 | Quantity required per parent unit |
| 72 | ISFO_LIN_REF | STRING | 20 | — | Reference number (drawing or spec reference) |
| 73 | ISFO_LIN_REV | STRING | 5 | — | Revision number |
| 74 | ISFO_LIN_RTNUM | INTEGER | 2 | — | Routing operation number for this component |
| 75 | ISFO_LIN_SCRAP | NUMERIC | 8 | 2 | Scrap allowance percentage |
| 76 | ISFO_LIN_TYPE | STRING | 1 | — | Component type: `M`=make, `B`=buy, `P`=phantom, `R`=reference |
| 77 | ISFO_LIN_UID | STRING | 40 | — | Unique configuration line ID |
| 78 | ISFO_LIN_VEND | STRING | 10 | — | Vendor code for buy components (FK → BKAPVEND) |

## ISFOORDL
**CONFIGURATION ORDER LINE CONVERSION** — converts configuration selections to SO lines

Fields: 18 | Key: ISFO_ORDL_UID + ISFO_ORDL_LINE

Generated when a configuration is converted to a Sales Order. Each row becomes one
SO line item.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | ISFO_ORDL_DRAW | STRING | 15 | — | Drawing/part number |
| 2 | ISFO_ORDL_ESD | DATE | 4 | — | Estimated ship date for this line |
| 3 | ISFO_ORDL_EXTRA | STRING | 100 | — | Extra data |
| 4 | ISFO_ORDL_LINE | INTEGER | 2 | — | SO line number this order line maps to |
| 5 | ISFO_ORDL_LN | STRING | 3 | — | Line type code (3-char) |
| 6 | ISFO_ORDL_LOC | STRING | 10 | — | Warehouse location for fulfillment |
| 7 | ISFO_ORDL_OUID | NUMERIC | 8 | 4 | Order unique ID (links to parent configuration header) |
| 8 | ISFO_ORDL_PCODE | STRING | 15 | — | Product/item code (part number on the SO line) |
| 9 | ISFO_ORDL_PDESC | STRING | 30 | — | Product description |
| 10 | ISFO_ORDL_PDISC | NUMERIC | 8 | 2 | Price discount percentage |
| 11 | ISFO_ORDL_PEXT | NUMERIC | 8 | 2 | Extended price (quantity × unit price) |
| 12 | ISFO_ORDL_PPRCE | NUMERIC | 8 | 4 | Unit price |
| 13 | ISFO_ORDL_PQTY | NUMERIC | 8 | 2 | Quantity ordered |
| 14 | ISFO_ORDL_REV | STRING | 5 | — | Revision number |
| 15 | ISFO_ORDL_TXBLE | STRING | 1 | — | Taxable flag: `Y`=this line is taxable |
| 16 | ISFO_ORDL_TYPE | STRING | 6 | — | Line type (STOCK, NSTOCK, SERVICE, etc.) |
| 17 | ISFO_ORDL_UID | STRING | 40 | — | Unique ID (FK → ISFOHEAD.ISFO_HDR_UID) |
| 18 | ISFO_ORDL_UM | STRING | 3 | — | Unit of measure |

**Confidence: 72/100** — FO module table structures clear from naming + ERP context;
ISFO_LIN_OPFLAG_1..50 exact meanings (which flags map to which product options) require RWN
decryption of the FO configuration engine; BKFO_CFG_YN_1..15 exact semantics unknown;
module used for configurable product sales at i2 Systems (FO ERP module present but usage unknown).
