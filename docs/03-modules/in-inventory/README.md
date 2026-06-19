# Inventory (IN)

Status: verified (auto-generated from the extracted schema, menu-code dump, and DFM inventory).

- **Module code**: `IN`
- **Tables**: 19 (prefixes `BKIC`, `MTIC`)
- **UI forms**: 67 (prefixes `T7IN`, `T6IN`, `BKIN`)
- **Menu operations**: 40

## Menu operations

| Code | Operation | Legacy module file(s) |
| ---- | --------- | --------------------- |
| `IN-A` | Inventory Inquiry | BKINA;lbkina.run;t6INA;t6INAC |
| `IN-B` | Enter Inventory | BKINB;ISTECH;t6INB;t6INBC |
| `IN-C` | Enter Inventory Adjustments | BKINC |
| `IN-D` | Print Reorder Report | BKIND;T6IND |
| `IN-E` | Print Inventory Transactions | BKINE |
| `IN-F` | Print Inventory Value | BKINF |
| `IN-G` | Print Inventory Labels | BKING;T6ING |
| `IN-H` | Print Inventory Listing | BKINH;t6inh |
| `IN-I` | Print Inventory General Info | BKINI |
| `IN-J` | Print Physical Check | BKINJ |
| `IN-K` | IN-L-E     SM-J- | BKINK;ISSMJS |
| `IN-L-A` | Enter Standard Costs | BKINLA;FIXSTD |
| `IN-L-B` | Enter/Assign Locations | BKINLB |
| `IN-L-C` | Enter Customer Cross-Reference | BKINLC |
| `IN-L-D` | Print Customer Cross-Reference | BKINLD |
| `IN-L-E` | Update Material Standard Costs | BKINLE |
| `IN-L-F` | Enter Material Dimensions | BKINLF |
| `IN-L-G` | Print Material Dimensions | BKINLG |
| `IN-L-H` | Edit FIFO/LIFO Buckets | BKINLH |
| `IN-L-I` | Change Inventory Costing Method | BKINLI |
| `IN-L-J` | Transfer Inventory | BKINLJ;ISINLJ |
| `IN-L-K` | Inventory Exceptions Report | BKINLK |
| `IN-L-L` | BOM report | BKINLL |
| `IN-L-M` | Multi-Transfer Inventory | ISINLM;t6isinlm |
| `IN-L-N` | Copy Item | ISINLN |
| `IN-L-O` | Inventory utilites | BKACT;ISINLO;ISINLOA |
| `IN-L-P` | Multi-Co-Transfer Inventory | ISICT;T6ISICT |
| `IN-L-S` | Rebuild Stock Status | AUTOIND |
| `IN-L-T` | Reset Inventory Cycle Codes | ISINLT |
| `IN-L-U` | Recal UOH From FIFO Layers | ISINLU |
| `IN-L-V` | Archive Obsolete Inventory - | ISINLOA |
| `IN-M-C` | Global Price Change | BKINMC |
| `IN-M-E` | Print Price Code Prices | BKINMI |
| `IN-M-G` | Print Dicount Code Prices | BKINMI |
| `IN-M-I` | Print Contract Prices | BKINMI |
| `IN-N-A` | Print Month End Inventory Costing | BKINNA |
| `IN-N-B` | Print Shipments Costing | BKINNB |
| `IN-N-C` | Print Closed Work Orders Costing | BKINNC |
| `IN-N-D` | Print Inventory Audit | BKINND;ISINND |
| `IN-O` | User Defined Inventory Transactions | BKINO;T6INO |

## UI forms (67)

| DFM file | Caption | fields | controls | tabs |
| -------- | ------- | -----: | -------: | ---: |
| `T7INA.DFM` |  | 0 | 1 | 0 |
| `T7INAACDOC.DFM` |  Accutron Documentation | 4 | 23 | 0 |
| `T7INAALO.DFM` |  | 0 | 7 | 0 |
| `T7INACMP.DFM` | Compliance | 34 | 68 | 0 |
| `T7INAFORECAST.DFM` |  | 4 | 8 | 0 |
| `T7INAPRC.DFM` | Customer Price | 9 | 25 | 0 |
| `T7INASPC.DFM` |  Specifications | 16 | 23 | 0 |
| `T7INAUDF.DFM` |  Specifications | 33 | 73 | 0 |
| `T7INAUSG.DFM` |  | 4 | 8 | 0 |
| `T7INAWIP.DFM` | Item In WIP | 7 | 19 | 0 |
| `T7INB.DFM` |  | 0 | 1 | 0 |
| `T7INB2DB.DFM` |  | 0 | 1 | 0 |
| `T7INBCMP.DFM` | Compliance | 34 | 68 | 0 |
| `T7INBECO.DFM` |  | 0 | 1 | 0 |
| `T7INBLNK.DFM` |  | 0 | 1 | 0 |
| `T7INBMFG.DFM` |  | 0 | 1 | 0 |
| `T7INBMRP.DFM` |  MRP Settings | 15 | 33 | 0 |
| `T7INBSPC.DFM` |  Specifications | 15 | 22 | 0 |
| `T7INBUDF.DFM` |  Specifications | 33 | 73 | 0 |
| `T7INBVND.DFM` |  | 0 | 1 | 0 |
| `T7INC.DFM` | IN-C Enter Inventory Adjustments | 60 | 138 | 0 |
| `T7IND.DFM` | IN-D Print Record Report | 53 | 120 | 2 |
| `T7INDPO.DFM` | IN-D  PO | 1 | 19 | 0 |
| `T7INE.DFM` | IN-E Print Inventory Transactions | 17 | 47 | 0 |
| `T7INF.DFM` | IN-F Print inventory Value | 43 | 87 | 0 |
| `T7ING.DFM` | IN-G  Print Inventory Labels | 85 | 204 | 0 |
| `T7INGimport.DFM` | IN-G-A  Import and Print Inventory Labels | 17 | 49 | 0 |
| `T7INH.DFM` | IN-H  Print Inventory Listning | 20 | 55 | 0 |
| `T7INI.DFM` | IN-I  Print Inventory General Info | 10 | 37 | 0 |
| `T7INJ.DFM` | IN-J  Print Physikal Check | 20 | 51 | 0 |
| `T7INK.DFM` |  | 0 | 1 | 0 |
| `T7INLA.DFM` | IN-L-A | 25 | 77 | 0 |
| `T7INLB.DFM` | IN-L-B | 27 | 71 | 0 |
| `T7INLC.DFM` | IN-L-C | 9 | 33 | 0 |
| `T7INLD.DFM` | IN-L-D  Print Customer Cross-Reference | 10 | 36 | 0 |
| `T7INLE.DFM` | IN-L-E | 12 | 38 | 0 |
| `T7INLF.DFM` |  | 0 | 1 | 0 |
| `T7INLG.DFM` | IN-L-G | 12 | 40 | 0 |
| `T7INLH.DFM` |  | 0 | 1 | 0 |
| `T7INLI.DFM` | IN-L-I | 2 | 25 | 0 |
| `T7INLJ.DFM` | IN-L-J Transfer Inventory | 28 | 81 | 0 |
| `T7INLK.DFM` | IN-L-K | 33 | 69 | 0 |
| `T7INLL.DFM` | IN-L-L | 10 | 36 | 0 |
| `T7INLM.DFM` |  | 0 | 1 | 0 |
| `T7INLN.DFM` |  | 0 | 1 | 0 |
| `T7INLO.DFM` | GL-G | 41 | 77 | 0 |
| `T7INLOA.DFM` | IN-L-O-A | 13 | 42 | 0 |
| `T7INLQ.DFM` |  | 0 | 1 | 0 |
| `T7INLR.DFM` |  | 0 | 1 | 0 |
| `T7INLS.DFM` | New Screen | 3 | 20 | 0 |
| `T7INLT.DFM` | IN-L-T | 40 | 68 | 0 |
| `T7INLV.DFM` | BASE Blank T7 SCREEN | 10 | 36 | 0 |
| `T7INM.DFM` | IN-M  Summary Reorder Report | 21 | 55 | 0 |
| `T7INNA.DFM` | IN-N-A Print Month End Inventory Costing | 18 | 52 | 0 |
| `T7INNB.DFM` | IN-N-B Print Shipments Costing | 13 | 42 | 0 |
| `T7INNC.DFM` | IN-N-C Print Closed Work Orders Costing | 10 | 37 | 0 |
| `T7INND.DFM` | IN-N-D Print Inventory to GL Exceptions Report | 12 | 32 | 0 |
| `T7INO.DFM` | IN-E | 65 | 136 | 2 |
| `T7INP.DFM` | IN-P | 39 | 87 | 0 |
| `T7INS.DFM` |  | 0 | 1 | 0 |
| `T7INVARCH.DFM` | New Screen | 2 | 18 | 0 |
| `T7INVENTORY.DFM` |  | 0 | 1 | 0 |
| `T7INXFERNUM.DFM` |  | 0 | 2 | 0 |
| `t7INBE.DFM` |  | 0 | 1 | 0 |
| `t7inaC.DFM` | T7INA | 53 | 178 | 0 |
| `t7inaE.DFM` |  | 0 | 1 | 0 |
| `t7inbc.DFM` | IN-B  Enter Inventory | 67 | 164 | 0 |

## Database tables (19)

Full field details are in `../../../samples/ddf/schema.md` (see per-table heading).

| Table | File on disk | Fields | Key fields (first 3) |
| ----- | ------------ | -----: | -------------------- |
| **BKICALTD** | `BKICALTD.B` | 16 | `BKIC_ALTD_PCODE`, `BKIC_ALTD_TYPE`, `BKIC_ALTD_DESC` |
| **BKICALTP** | `BKICALTP.B` | 6 | `BKIC_ALTP_TYPE`, `BKIC_ALTP_PCODE`, `BKIC_ALTP_ACODE` |
| **BKICAMTR** | `BKICAMTR.B` | 64 | `BKIC_PROD_CODE`, `BKIC_PROD_DESC`, `BKIC_PROD_TYPE` |
| **BKICAPMA** | `BKICAPMA.B` | 85 | `BKIC_PMAT_CUST`, `BKIC_PMAT_PCODE`, `BKIC_PMAT_PNUM` |
| **BKICDIM** | `BKICDIM.B` | 47 | `BKICDIM_PARTNO`, `BKICDIM_PARENT`, `BKICDIM_FIRST` |
| **BKICELOC** | `BKICELOC.B` | 32 | `BKIC_LOC_PROD`, `BKIC_LOC_CODE`, `BKIC_LOC_UOH` |
| **BKICEMTR** | `BKICEMTR.B` | 64 | `BKIC_PROD_CODE`, `BKIC_PROD_DESC`, `BKIC_PROD_TYPE` |
| **BKICLOC** | `BKICLOC.B` | 32 | `BKIC_LOC_PROD`, `BKIC_LOC_CODE`, `BKIC_LOC_UOH` |
| **BKICLOCM** | `BKICLOCM.B` | 12 | `BKIC_LOCM_CODE`, `BKIC_LOCM_NAME`, `BKIC_LOCM_ADDR1` |
| **BKICMFG** | `BKICMFG.B` | 6 | `BKIC_MFG_PCODE`, `BKIC_MFG_MANUF`, `BKIC_MFG_MCODE` |
| **BKICMSTR** | `BKICMSTR.B` | 64 | `BKIC_PROD_CODE`, `BKIC_PROD_DESC`, `BKIC_PROD_TYPE` |
| **BKICPMAT** | `BKICPMAT.B` | 85 | `BKIC_PMAT_CUST`, `BKIC_PMAT_PCODE`, `BKIC_PMAT_PNUM` |
| **BKICREF** | `BKICREF.B` | 8 | `BKIC_REF_CUST`, `BKIC_REF_CODE`, `BKIC_REF_PDESC` |
| **BKICREQ** | `BKICREQ.B` | 41 | `BKIC_REQ_STATUS`, `BKIC_REQ_BY`, `BKIC_REQ_IDATE` |
| **BKICTAX** | `BKICTAX.B` | 46 | `BKIC_TAX_STATE`, `BKIC_TAX_LOCAL`, `BKIC_TAX_NAME` |
| **BKICVAL** | `BKICVAL.B` | 4 | `BKIC_VAL_CODE`, `BKIC_VAL_DATE`, `BKIC_VAL_TOTVL` |
| **MTICAMTR** | `MTICAMTR.B` | 108 | `MTIC_PROD_CLASS`, `MTIC_PROD_CODE`, `MTIC_PROD_DESC` |
| **MTICEMTR** | `MTICEMTR.B` | 108 | `MTIC_PROD_CLASS`, `MTIC_PROD_CODE`, `MTIC_PROD_DESC` |
| **MTICMSTR** | `MTICMSTR.B` | 108 | `MTIC_PROD_CLASS`, `MTIC_PROD_CODE`, `MTIC_PROD_DESC` |

## BKICVAL — FIFO/LIFO Cost Layer Table (4 fields, confirmed from DDF schema.md line 6393, Pass 110h 2026-06-19)

Primary key: `BKIC_VAL_CODE` (STRING 15) + `BKIC_VAL_DATE` (DATE)

| Field | Type | Meaning |
|-------|------|---------|
| `BKIC_VAL_CODE` | STRING 15 | Part code (PK part 1) |
| `BKIC_VAL_DATE` | DATE | Receipt date for this cost layer (PK part 2) |
| `BKIC_VAL_TOTVL` | FLOAT (2 dec) | Total dollar value remaining in this layer |
| `BKIC_VAL_UOH` | FLOAT (2 dec) | Units on hand remaining in this layer |

**FIFO/LIFO costing mechanics:**
- Each inventory receipt creates a new BKICVAL row with CODE + receipt DATE + total value + qty
- Effective cost per unit for a layer = TOTVL / UOH
- **FIFO:** consume the row with the **oldest** DATE first; decrement UOH; if UOH reaches 0, delete row and move to next oldest
- **LIFO:** consume the row with the **newest** DATE first
- **Average cost:** does not use BKICVAL layers for costing; computes running weighted average from INVTXN.AVGCOST instead
- The user selects FIFO, LIFO, or average via IN-L-I (Change Inventory Costing Method); BKICVAL is populated for FIFO/LIFO items
- IN-L-U (Recalculate UOH From FIFO Layers) reconciles BKICVAL against actual transactions

---

## INVTXN — Inventory Transaction Log (24 fields, confirmed from DDF schema.md line 11702, Pass 110h 2026-06-19)

Primary key: `MTIT_TYPE` + `MTIT_CLASS` + `MTIT_DATE` + `MTIT_CODE`

Uses `MTIT_*` field prefix (same MT* pattern as MTICMSTR — multi-class transaction).

| Field | Type | Size | Meaning |
|-------|------|------|---------|
| `MTIT_TYPE` | STRING | 1 | Transaction type: R=receipt, S=shipment, A=adjustment, W=WO issue, etc. |
| `MTIT_CLASS` | STRING | 4 | Product class (aligns with MTIC_PROD_CLASS) |
| `MTIT_DATE` | DATE | 4 | Transaction date |
| `MTIT_CODE` | STRING | 15 | Part code |
| `MTIT_QTY` | FLOAT | 8 | Quantity moved (positive=in, negative=out) |
| `MTIT_AVGCOST` | FLOAT | 8 | Weighted average cost at time of transaction |
| `MTIT_STDCST` | FLOAT | 8 | Standard cost at time of transaction |
| `MTIT_LOC` | STRING | 10 | Warehouse location |
| `MTIT_REF` | STRING | 30 | Reference number (SO#, PO#, WO#, or free text) |
| `MTIT_CUST` | STRING | 10 | Customer (for sales shipments) |
| `MTIT_INVOICE` | FLOAT | 8 | Invoice number |
| `MTIT_PRICE` | FLOAT | 8 | Selling price (for SO shipments) |
| `MTIT_PO` | FLOAT | 8 | PO number (for receipts) |
| `MTIT_WOPRE` | FLOAT | 8 | Work order prefix (for WO issues/receipts) |
| `MTIT_WOSUF` | UBINARY | 2 | Work order suffix |
| `MTIT_LOT` | STRING | 15 | Lot number (for lot-tracked items) |
| `MTIT_SERIAL` | STRING | 25 | Serial number (for serial-tracked items) |
| `MTIT_VENDOR` | STRING | 10 | Vendor (for PO receipts) |
| `MTIT_SCRAP` | STRING | 2 | Scrap reason code |
| `MTIT_QC` | STRING | 2 | Quality control code |
| `MTIT_DEPT` | STRING | 4 | Department |
| `MTIT_DESC` | STRING | 30 | Description |
| `MTIT_PRODLOT` | STRING | 15 | Production lot |
| `MTIT_EXTRA` | STRING | 50 | Extra / user-defined |

**Design notes:**
- INVTXN is the complete audit trail of every inventory movement — receipts, shipments, adjustments, WO issues, and WO completions all write here.
- For FIFO/LIFO costing, BKICVAL maintains the actual cost layers; INVTXN preserves the historical record of what was consumed and at what cost.
- `MTIT_AVGCOST` is updated by the system each time inventory is received, recalculating the running weighted average (total value on hand ÷ total units on hand).
- The lot and serial fields link to lot tracking (BKICLOC LOT field) and serial tracking systems.
- INVTXN is printed by IN-E (Print Inventory Transactions) and IN-N-D (Print Inventory Audit).

---

## MT* vs BK* scope — confirmed from DDF field analysis (Pass 110g 2026-06-19)

There are two parallel item master families in the IN module:

| Prefix | Tables | Fields | PK structure | Purpose |
|--------|--------|--------|--------------|---------|
| **BKIC*** | BKICMSTR, BKICAMTR, BKICEMTR | 64 each | `BKIC_PROD_CODE` only | Single-company item master — keyed by flat part number, 64 operational fields |
| **MTIC*** | MTICMSTR, MTICAMTR, MTICEMTR, MTINVDEF | 108 each | `MTIC_PROD_CLASS` + `MTIC_PROD_CODE` | Multi-class/multi-company item catalog — adds product CLASS as first key, 108 fields including all BKIC fields plus vendor list (10 slots), cost rollup snapshots, and lot size |

**Interpretation:** The MTIC* tables support a broader multi-division or multi-company product catalog where the same part code can exist in multiple product classes. They are wider (108 vs 64 fields) and include additional data for cost accounting snapshots and vendor management.

**MTIC* table roles:**

| Table | Purpose |
|-------|---------|
| **MTICMSTR** | Multi-class item master — the active catalog record (108f) |
| **MTICAMTR** | Point-in-time snapshot of MTICMSTR when actual costs were rolled up (108f, identical schema) |
| **MTICEMTR** | Point-in-time snapshot of MTICMSTR when estimated costs were rolled up (108f, identical schema) |
| **MTINVDEF** | Inventory creation defaults — template used when entering a new item (108f, identical schema) |

**BKIC* table roles:**

| Table | Purpose |
|-------|---------|
| **BKICMSTR** | Company-specific item master (64f) — operational data, on-hand quantities via BKICLOC |
| **BKICAMTR** | Actual cost snapshot of BKICMSTR (64f, identical schema) |
| **BKICEMTR** | Estimated cost snapshot of BKICMSTR (64f, identical schema) |

**Design note:** The snapshot pattern (AMTR = actual, EMTR = estimated) allows variance analysis: compare BKICMSTR vs BKICAMTR (current vs. last actual rollup) or BKICEMTR (current vs. last estimated rollup). The MTIC* snapshots serve the same purpose for the multi-class catalog. These snapshots are populated by IN-L-A (Enter Standard Costs) and IN-L-E (Update Material Standard Costs).

**MTEXCHG** (7f, `EXCHG_QUOTE`/`EXCHG_AMT`/`EXCHG_DESC`/`EXCHG_COST`/`EXCHG_EXTRA`/`EXCHG_CODE`/`EXCHG_LINE`) — Multi-currency exchange rate table. Likely used by the MU (multi-currency) module. `EXCHG_CODE` (15 chars) is the currency code; `EXCHG_AMT` (6 dec places) is the exchange rate.

**MTMRP** (13f) — MRP calculation work table. Used by the MR (MRP) module. Fields: `MTMRP_PARTNO`, `MTMRP_DATE`, `MTMRP_QTY`, `MTMRP_ONHAND`, `MTMRP_PEGTO` (pegged-to demand order), `MTMRP_ORDER` (supply order), `MTMRP_STARTDT`, `MTMRP_ACTION`, `MTMRP_PG_SDATE/FDATE/QTY` (pegging start/finish dates and qty), `MTMRP_EXTRA`, `MTMRP_LOC`. This stores the MRP explosion results and demand-supply pegging before the planned orders are released.

## Notes & open questions

- BKICMSTR (64f) vs MTICMSTR (108f): The 44-field difference includes fields like `MTIC_PROD_CLASS` PK, 10 vendor slots (VEND_1..10, VNAM_1..10, VPC_1..9), 15 replacement costs (RCOST_1..15), lot size (LOTSZ), optional features (OPT/OPTCS/OPTCD), cumulative scheduling (CUM), and long part# (LONGP).
- MTINVDEF (108f identical schema to MTICMSTR) acts as the "factory default" template — when a user creates a new item, the system copies default values from MTINVDEF to pre-populate fields.
- Relationship between BKIC* and MTIC* items: unclear whether every BKIC item has a corresponding MTIC record, or if they are independent catalogs. Without RWN source code, the sync/copy logic cannot be confirmed.
