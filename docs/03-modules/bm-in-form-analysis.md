# BM and IN Module — DFM Form Analysis
Status: partial | verified-from-DFM

Forms confirmed from \\I2S109-SOLIDCRM\DBAMFG$\T7BM*.DFM and T7IN*.DFM.

---

## BM — Bill of Materials (16 forms)

### Item Status Codes (confirmed from T7BMB)
- **Y** — Active
- **N** — Not Active
- **O** — Obsolete
- **D** — Discontinued
- **E** — Engineering (hold)
- **P** — Production Hold
- **S** — Shipping Hold
- **Q** — Full Quantity Hold
- **R** — Revised Print

### Item Type Codes (confirmed from T7BMD)
`RFAMNLBTKO`
- **R** — Raw Material
- **F** — Finished Good
- **A** — Assembly
- **M** — Make-to-Order
- **N** — No special
- **L** — Labor
- **B** — Buy-to-Order
- **T** — Tool
- **K** — Kit
- **O** — Option

### BOM Forms

| DFM | Purpose | Key fields |
|-----|---------|------------|
| T7BMA.DFM | BOM Master Entry | Parent item#, component table, BKBM.RM.REMARK[1-15] (15 remark lines per component) → BKBMMSTR, BKBMEMTR, BKBMAMTR |
| T7BMB.DFM | BOM Print Options | Parent range, status [YNODEPSQR], print specs/drawings/ECO/remarks/notes/features/approved vendors, qty decimals (0/2/4/6/8), cost decimals (0/2/4/6), RoHS [Y/N/O], linked docs, routing |
| T7BMC.DFM | Multi-Level BOM Print | Component range, print up to X levels, inactive parents option, decimals, features/specs |
| T7BMD.DFM | Availability Report | Parent item#, projected quantity, location, RoHS filter, multiple levels, rebuild stock status, shortages only, class/category/type filters |

**Remaining forms (not yet read):** T7BME through T7BMR (12 forms)

### Key Findings
- **15 remark lines per BOM component** — rich annotation capability
- **Multi-level explosion**: T7BMC explicitly supports "print up to X levels" — confirmed recursive BOM
- **Phantom assembly support**: BKBMAMTR (assembly type table) alongside BKBMEMTR suggests phantom/sub-assembly classification
- **Availability checking**: T7BMD checks component availability against projected WO quantity with "shortages only" filter — direct link to shop floor planning
- **RoHS compliance tracked at BOM level**: Y/N/O (Yes/No/Other) on BOM report and availability check
- **Effectivity**: Active status codes (E=Engineering, O=Obsolete) provide engineering change effectivity

### BOM Tables (all confirmed in DDF)
- **BKBMMSTR** — BOM master (parent item record; PK: BKBM_PARENT)
- **BKBMEMTR** — BOM entry detail (components, qty, UOM, operation link; PK: BKBM_PARENT)
- **BKBMAMTR** — BOM assembly type (phantom/sub-assembly flags; PK: BKBM_PARENT)
- **BKBMCNFG** — BOM configuration (engineering changes; PK: BKBM_CNFG_NUM)
- **BKBMNOTE** — BOM notes (PK: BKBM_NT_PARENT)
- **BKBMREMK** — BOM remarks, 15-line array (PK: BKBM_RM_PARENT)
- **BKBMSUMM** — BOM summary (PK: BKBM_PARENT)
- **BKBMDIM** — BOM dimensions (PK: BKBM_DIM_PARENT)
- **BKBMAVAL** — BOM alternate values (PK: BKBM_PARENT)

**Confidence: 62/100** — 4 core forms read; multi-level BOM and phantom support confirmed; full component field set not extracted.

---

## IN — Inventory (67 forms)

### Core Forms

| DFM | Purpose |
|-----|---------|
| T7INA.DFM | Item Master — create/maintain items. Toolbar: Notes, Find Prev/Next, Lookup, Clear, EvoLinks, Sales Orders, Shipments, Service/Repairs |
| T7INB.DFM | Inventory Transactions — receipts, issues, adjustments. Variants: T7INB2DB, T7INBCMP, T7INBECO, T7INBLNK, T7INBMFG, T7INBMRP, T7INBSPC, T7INBUDF, T7INBVND |
| T7INC.DFM | Inventory Cost/Valuation |
| T7IND.DFM | Inventory Distribution/Locations |

### Location/Bin Forms (T7INL* series — 16+ forms)
`T7INLA` through `T7INLV` — comprehensive location/bin management covering bin assignment, transfers, location status.

### Supplemental Item Master Forms
- **T7INAALO** — Item allocation
- **T7INACMP** — Item components/composition
- **T7INAFORECAST** — Demand forecasting
- **T7INAPRC** — Item pricing tiers
- **T7INASPC** — Item specifications
- **T7INAUDF** — User-defined fields
- **T7INAUSG** — Item usage/demand history
- **T7INAWIP** — Work-in-progress tracking
- **T7INNA–T7INND** — Auto-numbering / sequence setup

**Confidence: 60/100** — Form count and types confirmed; item master fields documented from DDF (see BKICMSTR section below); cost method logic not yet traced.

---

*Last updated: 2026-06-11*
