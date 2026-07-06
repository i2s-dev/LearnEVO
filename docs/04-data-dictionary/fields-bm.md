# BM — Bill of Materials: Field Reference

Status: verified-schema + completed field meanings (Pass 574k, 2026-07-06).

Source: `Evo-DBA_File_Fields 052421.xlsx`, sheet "Fields".

BKBMAMTR / BKBMAVAL / BKBMMSTR / BKBMSUMM are all identical 27-field BKBM_* schemas
(same structure as BKBMEMTR in the DI module — see [fields-di.md](fields-di.md)).
BKBMREMK is identical to BKBMERMK from the DI module.

---

## BKBMAMTR
**ARCHIVED BOM** — BOM records moved to archive on change/delete

Fields: 27 | Key: BKBM_PARENT + BKBM_PROD + BKBM_SORT

Identical 27-field schema to BKBMEMTR/BKBMMSTR/BKBMAVAL/BKBMSUMM (BKBM_* prefix).
See [fields-di.md](fields-di.md) BKBMEMTR section for full field list. Unique blanks
resolved below and shared across all four BOM tables.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKBM_C_TYPE | STRING | 1 | — | Component type code (`P`=purchased, `M`=manufactured, `S`=subcontract) |
| 2 | BKBM_COMP | STRING | 20 | — | Component Part Code |
| 3 | BKBM_DATE1 | DATE | 4 | — | Effectivity from date (component valid starting this date) |
| 4 | BKBM_DATE2 | DATE | 4 | — | Effectivity to date (component valid through this date; blank=no expiry) |
| 5 | BKBM_EST_LINE | STRING | 12 | — | Estimate line number / cross-reference key |
| 6 | BKBM_EXTRA | STRING | 20 | — | Extra data |
| 7 | BKBM_NOTES | STRING | 50 | — | BOM Line Notes |
| 8 | BKBM_PARENT | STRING | 20 | — | Parent Part Code (PK) |
| 9 | BKBM_P_TYPE | STRING | 1 | — | Parent item type code (`P`=purchased, `M`=manufactured, `S`=subcontract) |
| 10 | BKBM_PROD | STRING | 20 | — | Product (Component) Part Code |
| 11 | BKBM_PROD_LINE^ | NUMERIC | — | — | BOM line number (computed display sequence) |
| 12 | BKBM_PROD_OPDSC | STRING | 10 | — | Option description code (groups optional components by description) |
| 13 | BKBM_PROD_OPYN_1 | STRING | 1 | — | Option flag 1 — configurable product option Y/N |
| 14 | BKBM_PROD_OPYN_2 | STRING | 1 | — | Option flag 2 — configurable product option Y/N |
| 15 | BKBM_PROD_OPYN_3 | STRING | 1 | — | Option flag 3 — configurable product option Y/N |
| 16 | BKBM_PROD_OPYN_4 | STRING | 1 | — | Option flag 4 — configurable product option Y/N |
| 17 | BKBM_PROD_OPYN_5 | STRING | 1 | — | Option flag 5 — configurable product option Y/N |
| 18 | BKBM_PROD_OPYN_6 | STRING | 1 | — | Option flag 6 — configurable product option Y/N |
| 19 | BKBM_QTY | NUMERIC | — | — | Component Quantity Required per parent |
| 20 | BKBM_QTY2 | NUMERIC | — | — | Component Quantity 2 |
| 21 | BKBM_SCRAP | NUMERIC | — | — | Scrap Factor |
| 22 | BKBM_SORT | NUMERIC | — | — | Sort Sequence |
| 23 | BKBM_STD_COST | NUMERIC | — | — | Standard Cost |
| 24 | BKBM_TYPE | STRING | 1 | — | Component Type |
| 25 | BKBM_UID | NUMERIC | 8 | — | Unique record ID (import batch / last-update identifier) |
| 26 | BKBM_UOM | STRING | 5 | — | Unit of Measure |
| 27 | BKBM_WASTED | NUMERIC | — | — | Waste Factor |

## BKBMAVAL
**BOM AVAILABILITY TEMP** — work table used during availability/shortage calculations

Fields: 27 | Key: BKBM_PARENT + BKBM_PROD + BKBM_SORT

Identical schema to BKBMAMTR above. See that table for all field definitions.

## BKBMMSTR
**BOM MASTER — ACTIVE BOM** — production bill of materials

Fields: 27 | Key: BKBM_PARENT + BKBM_PROD + BKBM_SORT

Identical schema to BKBMAMTR above. See that table for all field definitions.

## BKBMSUMM
**SUMMARIZED BOM TEMP** — work table used during single-level/multi-level BOM explosion

Fields: 27 | Key: BKBM_PARENT + BKBM_PROD + BKBM_SORT

Identical schema to BKBMAMTR above. See that table for all field definitions.

## BKBMNOTE
**BOM HEADER NOTES** — 15-line free-text notes for a parent item's BOM

Fields: 16 | Key: BKBM_NT_PARENT

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKBM_NT_NOTE_1 | STRING | 64 | — | BOM header note line 1 |
| 2 | BKBM_NT_NOTE_2 | STRING | 64 | — | BOM header note line 2 |
| 3 | BKBM_NT_NOTE_3 | STRING | 64 | — | BOM header note line 3 |
| 4 | BKBM_NT_NOTE_4 | STRING | 64 | — | BOM header note line 4 |
| 5 | BKBM_NT_NOTE_5 | STRING | 64 | — | BOM header note line 5 |
| 6 | BKBM_NT_NOTE_6 | STRING | 64 | — | BOM header note line 6 |
| 7 | BKBM_NT_NOTE_7 | STRING | 64 | — | BOM header note line 7 |
| 8 | BKBM_NT_NOTE_8 | STRING | 64 | — | BOM header note line 8 |
| 9 | BKBM_NT_NOTE_9 | STRING | 64 | — | BOM header note line 9 |
| 10 | BKBM_NT_NOTE_10 | STRING | 64 | — | BOM header note line 10 |
| 11 | BKBM_NT_NOTE_11 | STRING | 64 | — | BOM header note line 11 |
| 12 | BKBM_NT_NOTE_12 | STRING | 64 | — | BOM header note line 12 |
| 13 | BKBM_NT_NOTE_13 | STRING | 64 | — | BOM header note line 13 |
| 14 | BKBM_NT_NOTE_14 | STRING | 64 | — | BOM header note line 14 |
| 15 | BKBM_NT_NOTE_15 | STRING | 64 | — | BOM header note line 15 |
| 16 | BKBM_NT_PARENT | STRING | 20 | — | Parent Part Code (PK — one note set per parent item) |

## BKBMREMK
**BOM COMPONENT REMARKS** — 15-line per-component remarks (live BOM equivalent of BKBMERMK)

Fields: 20 | Key: BKBM_RM_PARENT + BKBM_RM_PROD

Identical schema to BKBMERMK (DI module). See [fields-di.md](fields-di.md) BKBMERMK
section for the BKBM_RM_REMARK_1..15, BKBM_RM_EXTRA, BKBM_RM_UID fields.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKBM_RM_EXTRA | STRING | 20 | — | Extra data |
| 2 | BKBM_RM_PARENT | STRING | 20 | — | Parent Part Code (PK) |
| 3 | BKBM_RM_PROD | STRING | 20 | — | Component Part Code (PK) |
| 4 | BKBM_RM_REMARK_1 | STRING | 64 | — | Component remark line 1 |
| 5 | BKBM_RM_REMARK_2 | STRING | 64 | — | Component remark line 2 |
| 6 | BKBM_RM_REMARK_3 | STRING | 64 | — | Component remark line 3 |
| 7 | BKBM_RM_REMARK_4 | STRING | 64 | — | Component remark line 4 |
| 8 | BKBM_RM_REMARK_5 | STRING | 64 | — | Component remark line 5 |
| 9 | BKBM_RM_REMARK_6 | STRING | 64 | — | Component remark line 6 |
| 10 | BKBM_RM_REMARK_7 | STRING | 64 | — | Component remark line 7 |
| 11 | BKBM_RM_REMARK_8 | STRING | 64 | — | Component remark line 8 |
| 12 | BKBM_RM_REMARK_9 | STRING | 64 | — | Component remark line 9 |
| 13 | BKBM_RM_REMARK_10 | STRING | 64 | — | Component remark line 10 |
| 14 | BKBM_RM_REMARK_11 | STRING | 64 | — | Component remark line 11 |
| 15 | BKBM_RM_REMARK_12 | STRING | 64 | — | Component remark line 12 |
| 16 | BKBM_RM_REMARK_13 | STRING | 64 | — | Component remark line 13 |
| 17 | BKBM_RM_REMARK_14 | STRING | 64 | — | Component remark line 14 |
| 18 | BKBM_RM_REMARK_15 | STRING | 64 | — | Component remark line 15 |
| 19 | BKBM_RM_SORT | NUMERIC | — | — | Sort Sequence |
| 20 | BKBM_RM_UID | NUMERIC | 8 | — | Unique record ID (import batch / last-update identifier) |

## BKSBMFG
**APPROVED MANUFACTURER LIST (AML)** — approved manufacturers per component, optionally per customer

Fields: 6 | Key: BKSB_MFG_PARNT + BKSB_MFG_PROD + BKSB_MFG_MANUF

One record per approved manufacturer entry. Customer code may be blank for a global approval.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKSB_MFG_CUST | STRING | 10 | — | Customer code requiring this approved manufacturer (blank = all customers) |
| 2 | BKSB_MFG_EXTRA | STRING | 20 | — | Extra data |
| 3 | BKSB_MFG_MANUF | STRING | 30 | — | Approved manufacturer name |
| 4 | BKSB_MFG_MPART | STRING | 30 | — | Manufacturer's part number / catalog number |
| 5 | BKSB_MFG_PARNT | STRING | 20 | — | Parent assembly part code (FK → BKICMSTR — the item that uses this component) |
| 6 | BKSB_MFG_PROD | STRING | 20 | — | Component part code for which this manufacturer is approved (FK → BKICMSTR) |

## BKSBPART
**APPROVED SUBSTITUTE PARTS** — approved substitutes per component, optionally per customer

Fields: 5 | Key: BKSB_PART_PARNT + BKSB_PART_PROD + BKSB_PART_SUBST

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKSB_PART_CUST | STRING | 10 | — | Customer code (blank=all customers; or specific customer requiring this substitution) |
| 2 | BKSB_PART_EXTRA | STRING | 20 | — | Extra data |
| 3 | BKSB_PART_PARNT | STRING | 20 | — | Parent assembly part code (FK → BKICMSTR) |
| 4 | BKSB_PART_PROD | STRING | 20 | — | Original component part code (the part being substituted) |
| 5 | BKSB_PART_SUBST | STRING | 20 | — | Substitute part code (FK → BKICMSTR — use this when PROD is unavailable) |

## BKSBVEND
**APPROVED VENDOR LIST (AVL)** — approved vendors per component, optionally per customer

Fields: 6 | Key: BKSB_VEND_PARNT + BKSB_VEND_PROD + BKSB_VEND_VEND

One record per approved vendor entry. Customer code may be blank for a global approval.

| # | Field | Type | Size | Dec | Description |
|---|-------|------|------|-----|-------------|
| 1 | BKSB_VEND_CUST | STRING | 10 | — | Customer code (blank=all; or specific customer requiring this vendor) |
| 2 | BKSB_VEND_EXTRA | STRING | 20 | — | Extra data |
| 3 | BKSB_VEND_PARNT | STRING | 20 | — | Parent assembly part code (FK → BKICMSTR — the item that uses this purchased component) |
| 4 | BKSB_VEND_PROD | STRING | 20 | — | Component part code for which this vendor is approved (FK → BKICMSTR) |
| 5 | BKSB_VEND_VEND | STRING | 10 | — | Approved vendor code (FK → BKAPVEND) |
| 6 | BKSB_VEND_VPART | STRING | 30 | — | Vendor's part number / catalog number for this component |

**Confidence: 78/100** — BOM core fields (PARENT, COMP, QTY, SCRAP, UOM, SORT) confirmed from
standard BOM practice and DI module cross-reference; C_TYPE/P_TYPE flag codes, PROD_OPDSC/OPYN
option mechanism, EST_LINE key, and approved-source table FK relationships inferred from field
names and manufacturing context; exact OPYN_1..6 option codes and configurable product logic
require RWN decryption to verify.
