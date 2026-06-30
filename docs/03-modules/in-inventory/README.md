# Inventory (IN)

Status: verified | Pass 335 (2026-06-26)

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
| `IN-K` | Adjust Physical Levels | BKINK |
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
| `IN-N-D` | Print Inventory Audit (**REMOVED** — redirects to Reconcile Inventory On-Hand) | BKINND |
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
| `MTIT_TYPE` | STRING | 1 | Transaction type code (single char) — see type code table below |
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

**Transaction type codes** (all 14 — fully confirmed Pass 391 2026-06-30):

`MTIT_TYPE` is STRING 1. The first 9 are **SRC-confirmed** from BKLME.SRC L249-257/L605-613.
G and B confirmed from `BKINE.RUN` binary label strings (Pass 391).

| Code | Short label | Full label (binary-confirmed) | Event | Net QTY |
|------|-------------|-------------------------------|-------|---------|
| `A` | `ADJUSTMT` | Adjustments | Manual inventory adjustment | ± |
| `S` | `SHIPMENT` | Shipments | Sales shipment (outbound) | − |
| `P` | `PO RECPT` | Purchase Receipts to Stock | PO receipt into stock | + |
| `J` | `PO JOBRC` | Purchase Receipts to WIP | PO receipt direct to WO/job | + |
| `W` | `WO RECPT` | Work Order Receipts to Stock | Work order finished goods in | + |
| `I` | `WO ISSUE` | Stock Issues to WIP | Work order material issue | − |
| `O` | `OUT PROC` | Outside Processing Receipt | Outside-process receipt | ± |
| `Q` | `QC RECPT` | Receipt to QC | QC inspection receipt | ± |
| `C` | `$ CHANGE` | PO Price Change | Cost change only (no qty change) | 0 |
| `M` | `MKE FROM` | Make From Component Issue | Make-from BOM component issue | − |
| `T` | `TRANSFER` | Transfer | Location-to-location transfer | 0 |
| `R` | `SERV&REP` | Service and Repair | Service/repair transaction | ± |
| `G` | `SCRAP` | Scrap | WO/production scrap recording | − |
| `B` | `BIN TXN` | Bin Transactions | Bin-to-bin transfer within location | 0 |

Note: the binary label "DELETED" (`BKLME.RUN` data channel) is the fallthrough/default
case in BKLME.SRC (L258: unconditional `MEMORY1[1]="DELETED"` after the type chain) — not a
real transaction type code stored in MTIT_TYPE. All 14 codes are confirmed.

**AVGCOST semantics by type (SRC-confirmed BKLME.SRC L272-315):**
- **P/J** (PO receipt): `MTIT.AVGCOST = MTIT.PRICE` on read — stored as PO unit price, NOT weighted avg
- **I/Q/O** (WO issue/QC/outside process): `MTIT.AVGCOST = MTIT.AVGCOST / MTIT.QTY` on read — stored as TOTAL cost (QTY × unit_cost); must divide to get unit cost
- **A/S/W/C**: MTIT.AVGCOST is stored directly as unit cost

**Design notes:**
- INVTXN is the complete audit trail of every inventory movement.
- For FIFO/LIFO costing, BKICVAL maintains cost layers; INVTXN preserves historical record.
- **Lot/serial records are NOT consolidated by LM-E** (BKLME.SRC L236-237: `if mtit.lot<>"" goto find_next` / `if mtit.serial<>"" goto find_next`) — they are preserved individually for traceability.
- LM-E purges individual INVTXN records (`del INVTXN nocnf`) and writes type-summary records with REF="Consolidate Inv Transactions" plus a beginning-balance A record with QTY=BKIC.PROD.UOH.
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

## Programs (53 total, Pass 265 2026-06-25)

Data extracted from rwn_symbols.json (proc counts, lib, db fingerprint, named-var namespaces).

### Core item master editors

| Program | Procs | Lib | DBs | Role / key namespaces |
|---------|------:|-----|----:|----------------------|
| `T7INB.RWN` | 466 | LISTG60 | 69 | **IN-B Enter Inventory** — full item master editor; BKIC.PROD 504-var + BKIC.LOC 297-var + MTIC.PROD 162-var |
| `T7INA.RWN` | 352 | LISTG60 | 53 | **IN-A Inventory Inquiry** — browse/view item master; BKIC.PROD 315-var + BKIC.LOC 324-var + IS.NCR 58-var |
| `T7IND.RWN` | 355 | LISTG60 | 45 | **IN-D Print Reorder Report** — location-level reorder; BKIC.LOC 297-var + ISBUILD |
| `T7INC.RWN` | 247 | LISTG60 | 44 | **IN-C Enter Inventory Adjustments** — manual adj; INVTXN + SCRAP + BKICLOC |
| `T7INS.RWN` | 150 | ISTECH2 | 37 | **IN-S** item status editor; BKICLOCM + BKICLOC + ISIS + MKAHIST |
| `T7INLS.RWN` | 148 | LISTG60 | 36 | **IN-L-S Rebuild Stock Status** — ISIS + ISLOG + BKICLOCM |
| `T7INAC.RWN` | 185 | COSTING.LIB | 29 | **IN-A-C actual costing** sub-form; BKIC.PROD 310-var |
| `T7INAE.RWN` | 185 | COSTING.LIB | 31 | **IN-A-E estimated costing** sub-form; BKIC.PROD 310-var |

### Inventory adjustments / postings

| Program | Procs | Lib | DBs | Role |
|---------|------:|-----|----:|------|
| `T7ING.RWN` | 323 | DBA.LIB | 47 | **IN-G Print Inventory Labels** — BKPR.EMP 107-var + SERIAL + ISLBLMAP + BKAPPOL |
| `T7INO.RWN` | 252 | EVO.LIB | 32 | **IN-O User-Defined Transactions** — INVTXN + BKACTRPT + CLASS |
| `T7INP.RWN` | 184 | LISTG60 | 28 | **IN-P Inventory Posting** — GL-side close; INVTXN + ISGLDATE + BKICLOCM |
| `t7ingImport.RWN` | 78 | EVO.LIB | 20 | **IN-G-A Import & Print Labels** — batch import; LOT + SERIAL + BKARCUST |
| `t7INGA.RWN` | 48 | T7TLL.LIB | 17 | IN-G-A mobile/TLL label variant; LOT + SERIAL |
| `T7INVARCH.RWN` | 52 | EVO.LIB | 64 | **INVTXN archive** — rolls old INVTXN rows to archive; ISGLDATE |
| `T7INVENTORY.RWN` | 54 | EVO.LIB | 14 | Module launcher / dispatcher |

### Location / bin series (T7INL*)

| Program | Procs | Lib | DBs | Role |
|---------|------:|-----|----:|------|
| `T7INLM.RWN` | 243 | T7DBA.LIB | 36 | **IN-L-M Multi-Transfer Inventory** — LOT + ISBINLOC + BKARTXN + SERIAL |
| `T7INLB.RWN` | 224 | LISTG60 | 41 | **IN-L-B Enter/Assign Locations** — BKICLOCM + BKICLOC + ISBINLOC + ISBINLOT + ISBNMSTR |
| `T7INLR.RWN` | 198 | ISTECH | 40 | Location receipt posting sub-program; ISMCF + BKICLOCM + FILELOC |
| `T7INLO.RWN` | 186 | EVO.LIB | 36 | **IN-L-O Inventory Utilities** — INVTXN + BKARINVL |
| `T7INLK.RWN` | 170 | LISTG60 | 22 | **IN-L-K Inventory Exceptions Report** — DBAFIFO + BKICLOC |
| `T7INLJ.RWN` | 155 | ISTECH | 34 | **IN-L-J Transfer Inventory** — SERIAL + LOT + ISBINLOC + INVTXN |
| `T7INLT.RWN` | 152 | LISTG60 | 20 | **IN-L-T Reset Inventory Cycle Codes** — ISCYCLCD |
| `T7INLE.RWN` | 136 | LISTG60 | 22 | **IN-L-E Update Material Standard Costs** — BKAPPOL + BKAPPO |
| `T7INLOA.RWN` | 107 | LISTG60 | 64 | **IN-L-O-A** advanced location history; INVTXN + ROUTING + SERIAL |
| `T7INLA.RWN` | 100 | LISTG60 | 64 | **IN-L-A Enter Standard Costs** — ISICMSTR + IS.NCR |
| `T7INLN.RWN` | 116 | LISTG60 | 27 | **IN-L-N Copy Item** — ISECO + ISNOTES + ISLINKS |
| `T7INLL.RWN` | 133 | LISTG60 | 64 | **IN-L-L BOM Report** — BKBMMSTR |
| `T7INLD.RWN` | 114 | LISTG60 | 64 | **IN-L-D Print Customer Cross-Reference** — BKICREF |
| `T7INLG.RWN` | 118 | LISTG60 | 64 | **IN-L-G Print Material Dimensions** — BKICDIM |
| `T7INLC.RWN` | 88 | LISTG60 | 17 | **IN-L-C Enter Customer Cross-Reference** — BKICREF + BKARCUST + FILELOC |
| `T7INLF.RWN` | 79 | LISTG60 | 64 | **IN-L-F Enter Material Dimensions** — BKICDIM |
| `T7INLV.RWN` | 97 | LISTG60 | 64 | **IN-L-V Archive Obsolete Inventory** — ISICMSTR + CLASS |
| `T7INLQ.RWN` | 96 | EVO.LIB | 64 | IN-LQ item type/qualification; ISITP |
| `T7INLH.RWN` | 93 | LISTG60 | 64 | **IN-L-H Edit FIFO/LIFO Buckets** — DBAFIFO + INVTXN |
| `T7INLI.RWN` | 65 | EVO.LIB | 64 | **IN-L-I Change Inventory Costing Method** — DBAFIFO + BKICLOC |

### Inquiry / reports

| Program | Procs | Lib | DBs | Role |
|---------|------:|-----|----:|------|
| `T7INF.RWN` | 194 | LISTG60 | 29 | **IN-F Print Inventory Value** — BKICLOC + BKAP.POL 38-var |
| `T7INM.RWN` | 147 | LISTG60 | 25 | **IN-M Summary Reorder Report** — WORKORD + BKAPPOL + WOBOM + BKMRPFC |
| `T7INE.RWN` | 158 | LISTG60 | 27 | **IN-E Print Inventory Transactions** — MKAHIST + INVTXN |
| `T7INH.RWN` | 134 | LISTG60 | 64 | **IN-H Print Inventory Listing** — BKICREF + BKSBVEND + INVTXN |
| `T7INI.RWN` | 121 | LISTG60 | 64 | **IN-I Print Inventory General Info** — BKARCUST + BKAPVEND + BKSBMFG |
| `T7INJ.RWN` | 143 | LISTG60 | 64 | **IN-J Print Physical Check** — ISBUILD + ISBINLOC + ISCYCLCD |
| `T7INK.RWN` | 142 | ISTECH | 35 | IN-K bin inventory kit; ISBINLOC + INVTXN |
| `T7INDPO.RWN` | 134 | EVO.LIB | 30 | IN-D-PO demand/PO drill-down; BKMRPPO + BKAPPO |
| `T7INNC.RWN` | 135 | LISTG60 | 18 | **IN-N-C Print Closed WO Costing** — WORKORD |
| `T7INND.RWN` | 129 | LISTG60 | 22 | **IN-N-D Print Inventory to GL Exceptions** — BKGLTRAN + BKGLCOA |
| `T7INNB.RWN` | 119 | LISTG60 | 64 | **IN-N-B Print Shipments Costing** — INVTXN |
| `T7INNA.RWN` | 98 | EVO.LIB | 64 | **IN-N-A Print Month End Inventory Costing** — INVTXN |

### New Entity / NZL license checks (NZLICE.LIB stubs)

| Program | Procs | Lib | Role |
|---------|------:|-----|------|
| `T7INAS.RWN` | 17 | NZLICE | New Zealand license check for IN-A |
| `T7INBLIM.RWN` | 15 | NZLICE | NZ limit check for IN-B |
| `T7INBNC.RWN` | 15 | NZLICE | NZ NCR license check |
| `T7INLIMA.RWN` | 15 | NZLICE | NZ LIMA license check |
| `T7INLIMACCESS.RWN` | 15 | NZLICE | NZ license access check |

---

## Supplemental item master panels (Pass 265 2026-06-25)

The IN-A (inquiry) and IN-B (edit) item master programs display sub-forms via wmount/load_form.
These DFMs appear as pop-up tabs on the item record.

### IN-A sub-panels (T7INA*.DFM)

| DFM | Caption | Fields | Purpose |
|-----|---------|-------:|---------|
| `T7INAACDOC.DFM` | Accutron Documentation | 4 | Customer-specific documentation panel |
| `T7INAALO.DFM` | (blank) | 0 | Allocation lookup (7 controls = grid only) |
| `T7INACMP.DFM` | Compliance | 34 | RoHS / environmental compliance flags |
| `T7INAFORECAST.DFM` | (blank) | 4 | Demand forecast entry |
| `T7INAPRC.DFM` | Customer Price | 9 | Per-customer price code entry |
| `T7INASPC.DFM` | Specifications | 16 | Item specifications |
| `T7INAUDF.DFM` | Specifications (UDF) | 33 | User-defined fields |
| `T7INAUSG.DFM` | (blank) | 4 | Usage statistics |
| `T7INAWIP.DFM` | Item In WIP | 7 | WIP inventory drill-down |
| `t7inaC.DFM` | T7INA | 53 | Primary item inquiry form (53 visible fields) |
| `t7inaE.DFM` | (blank) | 0 | Estimated cost sub-panel |

### IN-B sub-panels (T7INB*.DFM)

| DFM | Caption | Fields | Purpose |
|-----|---------|-------:|---------|
| `T7INBCMP.DFM` | Compliance | 34 | RoHS compliance (mirrors T7INACMP) |
| `T7INBECO.DFM` | (blank) | 0 | ECO (Engineering Change Order) link |
| `T7INBMFG.DFM` | (blank) | 0 | Manufacturing data panel |
| `T7INBMRP.DFM` | MRP Settings | 15 | MRP parameters (lot size, lead time, etc.) |
| `T7INBSPC.DFM` | Specifications | 15 | Item specifications (edit mode) |
| `T7INBUDF.DFM` | Specifications (UDF) | 33 | User-defined fields (edit mode) |
| `T7INBVND.DFM` | (blank) | 0 | Vendor info panel |
| `t7inbc.DFM` | IN-B Enter Inventory | 67 | Primary item editor form (67 visible fields) |

**Design note:** The IN-B MRP Settings panel (T7INBMRP, 15 fields) is the per-item configuration point for the MR (MRP) module — lead time, lot size, safety stock, order policy, and similar parameters are stored in BKICMSTR and read by MRP planning programs.

---

## IS-prefix auxiliary tables (Pass 265 2026-06-25)

Discovered from DB fingerprints in T7IN* programs; not all are in standard DDF.

| Table | First seen in | Purpose (inferred from program context) |
|-------|--------------|----------------------------------------|
| `ISICMSTR` | T7INA, T7INLA, T7INLR, T7INLV | IS item master — extended per-item data outside BKICMSTR; appears alongside IS.NCR namespace |
| `ISITP` | T7INA, T7INLQ | Item type profile — classifies items by type/category for reporting |
| `ISBINLOC` | T7INLB, T7INLJ, T7INJ, T7INK | Bin location assignment record — maps item+lot to a specific bin within a warehouse location |
| `ISBINLOT` | T7INLB | Bin lot record — lot-level bin assignment data |
| `ISBNMSTR` | T7INLB | Bin master — defines physical bin locations within a warehouse |
| `ISCYCLCD` | T7INLT, T7INJ | Cycle count code table — assigns cycle count frequency codes to items |
| `ISICUL` | T7ING | Item category / UL listing data — possibly certification (UL = Underwriters Laboratories) |
| `ISMCF` | T7INLR | Manufacturing constraint factor — used in location receipt logic |
| `FILELOC` | T7INLB, T7INLC, T7INLR | File-level location master — top-level location definitions |
| `ISECO` | T7INLN | Engineering Change Order header |
| `DBAFIFO` | T7INLH, T7INLI, T7INLK | FIFO cost layer work table — parallel to BKICVAL, used by costing engine |
| `ISGLDATE` | T7INP, T7IND | GL date control — current posting period date lock |
| `MKAHIST` | T7INE, T7INF, T7INH, T7INI | Market/sales history — appears across inquiry programs; may be a shared demand-history table |
| `ISIS` | T7INS, T7INLS, T7INB, many | IS Information Systems inquiry base — appears universally alongside MKAHIST+ISLOG+ISDRILL |

---

## Pass 335 — TAS6 binary analysis of 32 BKIN*.RUN programs (2026-06-26)

Source: string extraction from `samples/BKIN*.RUN` (copied from `\\i2s109-solidcrm\DBAMFG$\`).

### 32-program TAS6 inventory

| File | Size | Confirmed role | Key binary evidence |
|------|-----:|----------------|---------------------|
| `BKINA.RUN` | 342 KB | IN-A Inventory Inquiry | "IN-A Inventory Inquiry"; extensive stock status: SOs/POs/WOs/allocs/WIP/transactions; BOM drill-down; where-used; customer X-ref; lot/serial; "Click to see Imaging"; ISTS.CFG 200+ keys |
| `BKINB.RUN` | 426 KB | IN-B Enter Inventory / DE-J-A Edit Imported Inventory | "IN-B Enter Inventory" AND "DE-J-A Edit Imported Inventory" — dual dispatch; types R/M/F/B/T/K; service/repair; multi-yield; track M/M/S |
| `BKINC.RUN` | 375 KB | IN-C Enter Inventory Adjustments | "IN-C Enter Inventory Adjustments"; types N/L/T/K/B/O excluded; "You cannot take the Inventory Negative"; scrap/purchase receipt modes |
| `BKIND.RUN` | 367 KB | IN-D Print Reorder Report | "IN-D Print Reorder Report"; SO/PO/WO detail filter options; stock status rebuild option; sort by item/vendor |
| `BKINE.RUN` | 222 KB | IN-E Print Inventory Transactions | "IN-E Print Inventory Transactions"; type filter string "ASPJWIOQCMTRGB"; bin transactions variant |
| `BKINF.RUN` | 305 KB | IN-F Print Inventory Value | "IN-F Print Inventory Value"; avg cost × units; class/type/vendor/customer/GL asset filters; "Include Onhand with $0 costs" option |
| `BKING.RUN` | 240 KB | IN-G Print Inventory Labels | "IN-G Print Inventory Labels"; 1/2/3 column; barcode; bin location S/D/N; standard pack quantity; PO receiving labels |
| `BKINH.RUN` | 216 KB | IN-H Print Inventory Listing | "IN-H Print Inventory Listing"; "ROHS COMPLIANT INVENTORY LISTING" variant |
| `BKINI.RUN` | 203 KB | IN-I Print Inventory General Info | "IN-I Print Inventory General Info"; columns: stock UM/price UM/cost method/lot ctrl/serial ctrl/lead time/weight/cubic feet/primary vendor/mfgr item no/rev level/specs |
| `BKINIT.RUN` | 6 KB | System message stub | Only MESSAGE/ERR strings — internal error-message utility, not user-facing |
| `BKINJ.RUN` | 253 KB | IN-J Print Physical Check | "IN-J Print Physical Check"; cycle code filter; "Consolidate Locations?"; active status filter |
| `BKINK.RUN` | 290 KB | IN-K Adjust Physical Levels | "IN-K Adjust Physical Levels"; lot/serial hold warning; FIFO/LIFO note; "You cannot take the Inventory Negative" |
| `BKINLA.RUN` | 236 KB | IN-L-A Enter Standard Costs | "IN-L-A Enter Standard Costs"; LOT/SERIAL control; ESTD COST/BASE PRICE/EPO PRICE/RMA RECPT columns |
| `BKINLB.RUN` | 280 KB | IN-L-B Enter/Assign Locations | "IN-L-B Enter/Assign Locations"; FACTORY/WAREHOUSE LOCATION; GENERATE/DELETE LOCATION RECORDS; BKIC.LOCM.* namespace |
| `BKINLC.RUN` | 203 KB | IN-L-C Enter Customer Cross-Reference | "IN-L-C Enter Customer Cross-Reference"; BKIC.REF.* namespace |
| `BKINLD.RUN` | 201 KB | IN-L-D Print Customer Cross-Reference | "IN-L-D Print Customer Cross-Reference"; CUSTOMER CROSS REFERENCES header |
| `BKINLE.RUN` | 192 KB | IN-L-E Update Material Standard Costs | "IN-L-E Update Material Standard Costs"; bulk update from avg/last cost |
| `BKINLF.RUN` | 204 KB | IN-L-F Enter Material Dimensions | "IN-L-F Enter Material Dimensions"; BKICDIM.* namespace confirmed |
| `BKINLG.RUN` | 190 KB | IN-L-G Print Material Dimensions | "IN-L-G Print Material Dimensions"; MATERIAL DIMENSIONS report header |
| `BKINLH.RUN` | 240 KB | IN-L-H Edit FIFO/LIFO Buckets | "IN-L-H Edit FIFO/LIFO Buckets"; GL posting to clearing account on cost change |
| `BKINLI.RUN` | 124 KB | IN-L-I Change Inventory Costing Method | "IN-L-I Change Inventory Costing Method"; "AVERAGE COST" / "STANDARD COST" current method strings; GL clearance codes |
| `BKINLJ.RUN` | 315 KB | IN-L-J Transfer Inventory | "IN-L-J Transfer Inventory"; ISBINLOT/ISBINLOTA; LOT/SERIAL error handling |
| `BKINLK.RUN` | 259 KB | IN-L-K Inventory Exceptions Report | "IN-L-K Inventory Exceptions Report"; exception types multi-select; by-location reporting |
| `BKINLL.RUN` | 203 KB | IN-L-L BOM Report | "IN-L-L BOM report"; BKBM.COMPONENT/BKBM.PARENT namespace |
| `BKINMC.RUN` | 98 KB | IN-M-C Global Price Change | "IN-M-C Global Price Change"; multi-module string "IN-PO-BM-LW-LC-SC-FO-PI"; BKIC.PMAT.* namespace |
| `BKINMI.RUN` | 128 KB | IN-M-I / IN-M-E / IN-M-G (price reports) | "IN-M-I Print Contract Prices" + "IN-M-E Print Price Code Prices" + "IN-M-G Print Dicount Code Prices" — single TAS6 program handles all three; BKIC.PMAT.* namespace |
| `BKINNA.RUN` | 132 KB | IN-N-A Print Month End Inventory Costing | "IN-N-A Print Month End Inventory Costing"; 9 transaction categories in report |
| `BKINNB.RUN` | 218 KB | IN-N-B Print Shipments Costing | "IN-N-B Print Shipments Costing"; "MONTHLY SHIPMENTS AT STANDARD COST" |
| `BKINNC.RUN` | 159 KB | IN-N-C Print Closed Work Orders Costing | "IN-N-C Print Closed Work Orders Costing"; STANDARD/STANDARD.MAT vars |
| `BKINND.RUN` | 8 KB | IN-N-D — REMOVED | "IN-N-D, Print Inventory Audit, has been removed from the system. Please use Reconcile Inventory On-Hand instead." — stub only |
| `BKINO.RUN` | 349 KB | IN-O User Defined Inventory Transactions | "IN-O User Defined Inventory Transactions"; LOT HIST/SER HIST/INV TXN table references; custom transaction types |
| `BKINTCUR.RUN` | 66 KB | Multi-currency conversion utility | Touches BKAP.PO.ISCUR/IS.MCCODE, BKAR.INV.ISCUR/IS.MCCODE, BKAR.INVT.MCCOD/MCRAT, BKAR.INVV.ISCUR, BKAP.INVL.ISCUR, BKAP.CHK.ISCUR, BKIS.TAX.ISCUR — confirms IS-currency fields across all modules |

### Menu code corrections confirmed by binary

| Code | Prior description | Corrected description | Source |
|------|-----------------|-----------------------|--------|
| `IN-K` | "IN-L-E SM-J-" (garbled parse) | Adjust Physical Levels | BKINK.RUN: "IN-K Adjust Physical Levels" literal string |
| `IN-N-D` | Print Inventory Audit | **REMOVED** — displays removal message, redirects to Reconcile Inventory On-Hand | BKINND.RUN: 8 KB stub with explicit removal message |

### IN-B dual dispatch — DE-J-A confirmed

`BKINB.RUN` contains both `"IN-B  Enter Inventory"` and `"DE-J-A  Edit Imported Inventory"` as program title strings, and both appear in add-new and edit-existing variants:
- `"DE-J-A  Edit Imported Inventory - Add New Item Number"`
- `"IN-B  Enter Inventory - Add New"`
- `"DE-J-A  Edit Imported Inventory - Edit Existing Item Number"`
- `"IN-B  Enter Inventory - Edit Existing"`

BKINB is the TAS6 backing for both `IN-B` (standard inventory entry) and `DE-J-A` (imported item editing). DE-J-A is the Data Entry module code for importing item records from an external source and editing them within EVO.

### BKINE transaction type string — all 14 type codes confirmed

`BKINE.RUN` and `BKINMC.RUN` both contain the literal string `ASPJWIOQCMTRGB` — this is the full enumeration of all 14 valid INVTXN transaction type codes used as a menu filter. Extending the 9 previously SRC-confirmed codes:

| Code | Previously known | Extended meaning (inferred from BKINNA report sections) |
|------|------------------|---------------------------------------------------------|
| `A` | ✅ SRC: ADJUSTMT | Manual adjustment |
| `S` | ✅ SRC: SHIPMENT | Sales shipment |
| `P` | ✅ SRC: PO RECPT | PO receipt to stock |
| `J` | ✅ SRC: PO JOBRC | PO receipt to WIP/job |
| `W` | ✅ SRC: WO RECPT | Work order receipt |
| `I` | ✅ SRC: WO ISSUE | WO material issue |
| `O` | ✅ SRC: OUT PROC | Outside-process receipt |
| `Q` | ✅ SRC: QC RECPT | QC inspection receipt |
| `C` | ✅ SRC: $ CHANGE | PO price change (cost change, no qty) |
| `M` | new | Make-From component issue (BKINNA: "MAKE FROM COMPONENT ISSUE") |
| `T` | new | Inventory transfer (BKINNA: "TRANSFERS") |
| `R` | new | Service/repair transaction (BKINNA: "SERVICE AND REPAIR") |
| `G` | new | **Scrap** — WO/production scrap recording (BKINE.RUN label: "G - Scrap"; short: "SCRAP") |
| `B` | new | **Bin Transactions** — bin-to-bin transfer within location (BKINE.RUN label: "B - Bin Transactions"; short: "BIN TXN") |

### BKINNA month-end report categories — all transaction types mapped

`BKINNA.RUN` (IN-N-A Print Month End Inventory Costing) has 9 section headers, each corresponding to a transaction type:

| Section header | Type code |
|---------------|-----------|
| PURCHASE RECEIPTS TO STOCK | P |
| PURCHASE RECEIPTS TO WIP | J |
| STOCK ISSUES TO WIP | I |
| WORK ORDER RECEIPTS TO STOCK | W |
| ADJUSTMENTS | A |
| OUTSIDE PROCESSING RECEIPTS | O |
| PO PRICE CHANGE | C |
| MAKE FROM COMPONENT ISSUE | M (new) |
| TRANSFERS | T (new) |
| SERVICE AND REPAIR | R (new) — note: S=SHIPMENT is not in month-end costing (it's in BKINNB separately) |

### BKINTCUR — multi-currency field confirmations across modules

`BKINTCUR.RUN` is a cross-module multi-currency conversion utility that touches the multi-currency flag and rate fields in every major module simultaneously:

| Namespace | Module | Field meaning |
|-----------|--------|---------------|
| `BKAP.PO.ISCUR` | AP | PO multi-currency flag |
| `BKAP.IS.MCCODE` | AP | AP multi-currency code |
| `BKAR.INV.ISCUR` | AR | AR invoice multi-currency flag |
| `BKAR.IS.MCCODE` | AR | AR multi-currency code |
| `BKAR.INVV.ISCUR` | AR | AR vouchered invoice multi-currency flag |
| `BKAR.INVT.MCCOD` | AR | AR open-item ledger currency code |
| `BKAR.INVT.MCRAT` | AR | AR open-item ledger exchange rate |
| `BKAP.INVL.ISCUR` | AP | AP invoice line multi-currency flag |
| `BKAP.INVT.MCCOD` | AP | AP open-item currency code |
| `BKAP.INVT.MCRAT` | AP | AP open-item exchange rate |
| `BKAP.CHK.ISCUR` | AP | AP check multi-currency flag |
| `BKIS.TAX.ISCUR` | IS | IS tax record multi-currency flag |
| `BKIS.TAX.PONO` | IS | IS tax PO number |
| `BKIS.TAX.VEND` | IS | IS tax vendor code |
| `BKIS.TAX.CUST` | IS | IS tax customer code |

`BKIS.TAX.*` namespace is new — confirms the IS module has its own tax records table that tracks both vendor (PO) and customer (SO) tax amounts with a multi-currency flag.

### New accessor namespaces confirmed (Pass 335)

| Namespace | Found in | Meaning |
|-----------|----------|---------|
| `BKIC.LOCM.CODE` | BKINLB, BKINLK | Location master code |
| `BKIC.LOCM.CITY` | BKINLB | Location city |
| `BKIC.LOCM.STATE` | BKINLB | Location state |
| `BKIC.LOCM.ZIP` | BKINLB | Location ZIP |
| `BKIC.LOCM.TAX#` | BKINLB | Location tax number |
| `BKIC.LOCM.CNTCT` | BKINLB | Location contact name |
| `BKIC.LOCM.PHONE` | BKINLB | Location phone |
| `BKIC.LOCM.ADDR3` | BKINLK | Location address line 3 |
| `BKICDIM.PARTNO` | BKINLF, BKINLG | Material dimensions part number |
| `BKICDIM.PARENT` | BKINLF, BKINLG | Parent assembly of material part |
| `BKICDIM.GENERIC` | BKINLF, BKINLG | Phantom part for grouping alternates |
| `BKICDIM.FIRST/.F.TOL` | BKINLF | First dimension + tolerance |
| `BKICDIM.SECOND/.S.TOL` | BKINLF | Second dimension + tolerance |
| `BKICDIM.THICK/.T.TOL` | BKINLF | Thickness + tolerance |
| `BKICDIM.SETUP` | BKINLF | Material setup code |
| `BKICDIM.DENSITY` | BKINLF | Material density |
| `BKICDIM.ALLOY` | BKINLF | Alloy specification |
| `BKICDIM.TEMPER` | BKINLF | Temper specification |
| `BKICDIM.FINISH` | BKINLF | Surface finish |
| `BKICDIM.HARDNES` | BKINLF | Hardness |
| `BKIC.PMAT.PCODE` | BKINMC, BKINMI | Price matrix product code |
| `BKIC.PMAT.CUST` | BKINMC, BKINMI | Price matrix customer code |
| `BKIC.PMAT.RATE` | BKINMC, BKINMI | Price/discount rate |
| `BKIC.PMAT.PER` | BKINMC, BKINMI | Per-unit basis |
| `BKIC.PMAT.DCODE` | BKINMI | Discount code |
| `BKIC.PMAT.PNUM` | BKINMI | Price number |
| `BKIC.PMAT.CLASS` | BKINMI | Product class filter |
| `BKIC.PMAT.EXP` | BKINMI | Contract expiry date |
| `BKIC.PMAT.QTY` | BKINMI | Quantity break |
| `BKIC.PMAT.COMM1/.COMM2` | BKINMI | Commission codes 1 + 2 |
| `BKIS.TAX.ISCUR` | BKINTCUR | IS tax record multi-currency flag |
| `BKIS.TAX.PONO` | BKINTCUR | IS tax PO number |
| `BKIS.TAX.VEND` | BKINTCUR | IS tax vendor |
| `BKIS.TAX.CUST` | BKINTCUR | IS tax customer |

---

## Notes & open questions

- BKICMSTR (64f) vs MTICMSTR (108f): The 44-field difference includes fields like `MTIC_PROD_CLASS` PK, 10 vendor slots (VEND_1..10, VNAM_1..10, VPC_1..9), 15 replacement costs (RCOST_1..15), lot size (LOTSZ), optional features (OPT/OPTCS/OPTCD), cumulative scheduling (CUM), and long part# (LONGP).
- MTINVDEF (108f identical schema to MTICMSTR) acts as the "factory default" template — when a user creates a new item, the system copies default values from MTINVDEF to pre-populate fields.
- Relationship between BKIC* and MTIC* items: unclear whether every BKIC item has a corresponding MTIC record, or if they are independent catalogs. Without RWN source code, the sync/copy logic cannot be confirmed.
- **INVTXN type codes G and B: ✅ RESOLVED (Pass 391 2026-06-30):** G=Scrap (binary label "G - Scrap", short "SCRAP") and B=Bin Transactions (binary label "B - Bin Transactions", short "BIN TXN") — confirmed from BKINE.RUN type selector screen string list. BKINNA lacks these sections because scrap and bin moves are handled by BKINE (transaction entry) rather than month-end costing reports.
- **BKINIT.RUN purpose (Pass 335):** The 6 KB BKINIT.RUN contains only MESSAGE/ERR strings. It is likely a shared message/error lookup utility called by other BKIN programs — not a standalone user-facing program.
