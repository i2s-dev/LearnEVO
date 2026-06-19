# Lot Control (LC)

Status: verified (DDF schema confirmed; workflow from DFM + help content).

- **Module code**: `LC`
- **Tables**: 1 (`LOT`)
- **Primary data table**: `LOT.B` (25 fields)

→ See **[help-content.md](help-content.md)** for user-facing lot control procedures.

Lot Control tracks inventory by lot number — each receipt of lot-tracked items creates or updates a LOT row. Lots carry provenance information (vendor, PO, receipt date, cost) and enable FIFO/LIFO costing, expiration date management, and full traceability from receipt through shipment or WO consumption.

Lot-tracked items are identified by `BKICMSTR.BKIC_PROD_LOTNO = Y`.

## Database tables (1)

| Table | File on disk | Fields | Primary key |
| ----- | ------------ | -----: | ----------- |
| **LOT** | `LOT.B` | 25 | `MTLOT_CODE` + `MTLOT_LOT` |

## LOT — Lot Master (25 fields, confirmed from DDF schema.md, Pass 111b 2026-06-19)

Primary key: `MTLOT_CODE` (STRING 15, part code) + `MTLOT_LOT` (STRING 15, lot number)

One row per lot per part. When the same lot number is received across multiple POs, the row is updated (on-hand qty increases) rather than a new row being created.

| Field | Type | Meaning |
|-------|------|---------|
| `MTLOT_CODE` | STRING 15 | Part number (PK 1) |
| `MTLOT_LOT` | STRING 15 | Lot number (PK 2) |
| `MTLOT_EXPDATE` | DATE | Expiration date (empty = no expiry) |
| `MTLOT_ONHAND` | FLOAT | Current on-hand quantity for this lot |
| `MTLOT_PO` | FLOAT | Purchase order number that received this lot |
| `MTLOT_RECDOC` | FLOAT | Receiving document number (PO receipt record) |
| `MTLOT_VENDOR` | STRING 10 | Vendor code who supplied this lot |
| `MTLOT_RECDATE` | DATE | Date lot was received from vendor |
| `MTLOT_RECQTY` | FLOAT | Original received quantity |
| `MTLOT_POCOST` | FLOAT | Unit cost from PO (vendor purchase cost) |
| `MTLOT_WO` | FLOAT | Work order prefix that produced this lot (if WO-manufactured) |
| `MTLOT_INRECDATE` | DATE | Internal receipt date (WO completion / internal movement) |
| `MTLOT_WOQTY` | FLOAT | WO completion quantity |
| `MTLOT_WOCOST` | FLOAT | WO completion unit cost |
| `MTLOT_NOTES_1..5` | STRING 45 | Notes lines 1–5 (5 × 45 = 225 chars total) |
| `MTLOT_LOC` | STRING 10 | Warehouse location |
| `MTLOT_WOSUF` | UBINARY | WO suffix (for WO-manufactured lots) |
| `MTLOT_EXTRA` | STRING 50 | Extra / user-defined |
| `MTLOT_BEGIN` | FLOAT (7 dec) | Beginning balance (weight/measure for certified lots) |
| `MTLOT_OUT` | FLOAT (7 dec) | Out quantity (issued/shipped) |
| `MTLOT_MAXOUT` | FLOAT (7 dec) | Maximum allowable out quantity |

### Field notes

- **Dual origin:** A lot can originate from a PO purchase (MTLOT_PO + MTLOT_VENDOR + MTLOT_POCOST) OR from a WO completion (MTLOT_WO + MTLOT_WOSUF + MTLOT_WOCOST). Purchased and manufactured lots are tracked in the same table.
- **MTLOT_BEGIN / MTLOT_OUT / MTLOT_MAXOUT:** The 7-decimal precision suggests these are used for lots measured by weight, length, or volume rather than integer count — e.g. coil stock, raw material, chemical lots. They may track a "certificate of conformance" quantity separate from the standard on-hand count.
- **Location tracking:** MTLOT_LOC places the lot in a specific warehouse location. When a lot spans multiple locations (split storage), multiple rows would exist with the same MTLOT_CODE + MTLOT_LOT but different LOC values — though the DDF shows a single PK, so splits would require different lot numbers per location.
- **INVTXN link:** All lot movements (issues, receipts, returns) are logged in INVTXN (inventory transaction log) with MTIT_LOT = the lot number, providing a full audit trail separate from the LOT on-hand balance.

## Lot control workflow

```
Receive PO (PO-L/PO-M)
  → Create or update LOT row (MTLOT_PO, VENDOR, RECDATE, RECQTY, POCOST)
  → BKICMSTR.BKIC_PROD_UOH += MTLOT_RECQTY
  → Log INVTXN (TYPE = receipt, MTIT_LOT = lot#)

Issue to Work Order (WO-C Issue)
  → Reduce MTLOT_ONHAND by issued qty
  → Log INVTXN (TYPE = WO issue, MTIT_LOT = lot#, MTIT_WOPRE/WOSUF = WO)

WO Completion (WO-E Receive)
  → Create LOT row for manufactured lot (MTLOT_WO, WOSUF, INRECDATE, WOCOST)
  → Log INVTXN (TYPE = WO receipt)

Ship to Customer (SO-C / SH)
  → Reduce MTLOT_ONHAND by shipped qty
  → Log INVTXN (TYPE = shipment, MTIT_LOT = lot#, MTIT_CUST = customer)

Physical Inventory (PI-C)
  → BKPILOT = frozen lot snapshot; BKPILCNT = counted lot entry
  → PI-G adjusts MTLOT_ONHAND and posts INVTXN adjustment
```

## Related tables

| Table | Module | Relationship |
|-------|--------|-------------|
| `INVTXN` | IN | Full transaction audit log — all lot movements recorded here |
| `BKICMSTR` | IN | Item master — `BKIC_PROD_LOTNO` flag enables lot tracking |
| `BKPILOT` / `BKPILCNT` | PI | Physical inventory lot snapshot / count |
| `BKSOHLOT` | SO | Lot number recorded on shipped sales order line |
| `BKAR_TXN_LOT` | AR | Lot number on AR shipment transaction |
| `BKAPPOL_LOT` | PO | Lot number on received PO line (field in BKAPPOL) |
