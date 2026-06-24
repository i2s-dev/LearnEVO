# CU — WO Material Cut Sheet

Status: verified | Pass 233

EvoERP module code: **CU**

Programs:
- `T7CUTSHEET2.RWN` — lot-enabled cut sheet (75 procs, src=EVO.LIB, 56 DB tables)
- `T7CUTSHEET2b.RWN` — no-lot variant (60 procs, src=EVO.LIB, 56 DB tables)

CU generates material cut sheets for Work Orders — a printed or screen list of all materials
needed for a WO that have been issued (or are planned to be issued), with lot/serial tracking
and quantity summaries. Used in the shop floor to confirm material picks.

The two variants differ by lot tracking: T7CUTSHEET2 uses ISBINLOT for lot-assigned components;
T7CUTSHEET2b uses ISBINLOC for bin-level (no-lot) components.

---

## Database tables (56 total — EVO.LIB session standard)

Key tables specific to CU function:

| Table | Purpose |
|-------|---------|
| WOMAT | WO material issue records (primary) |
| WORKORD | WO header |
| WOBOM | WO BOM (planned components) |
| LOT | Lot master |
| ISBINLOT | Bin + lot inventory (T7CUTSHEET2 only) |
| BKICMSTR | Production inventory master |
| BKPSUSER | Password-protected user file (T7CUTSHEET2) |
| ISLINKS | Document links |
| BKGLTRAN | GL transactions (cost posting) |
| BKGLX | GL extended |
| ISICMSTR | Estimating inventory master |
| ISDUTY / ISBROKER | Landed cost tables |

---

## WOMAT.* namespace — material issue record (20 vars)

Confirmed from var extraction (T7CUTSHEET2 + T7CUTSHEET2b):

| Var | Field | Meaning |
|-----|-------|---------|
| WOMAT.DATE | DATE | Issue date |
| WOMAT.WOPRE | WOPRE | WO prefix |
| WOMAT.WOSUF | WOSUF | WO suffix |
| WOMAT.QTYISSUED | QTYISSUED | Quantity issued |
| WOMAT.QTYSCRAP | QTYSCRAP | Quantity scrapped |
| WOMAT.SCRAPCD | SCRAPCD | Scrap reason code |
| WOMAT.LOT | LOT | Lot number |
| WOMAT.SERIAL | SERIAL | Serial number |
| MTWO.PRODCODE | PRODCODE | Finished goods item code |
| WOMAT.PRODDESC | PRODDESC | Finished goods description |
| WOMAT.KIT | KIT | Kit flag |
| WOMAT.PCODE | PCODE | Component item code |
| WOMAT.PDESC | PDESC | Component description |
| WOMAT.SCDESC | SCDESC | Scrap code description |
| WOMAT.COST | COST | Issue cost |
| WOMAT.REF | REF | Reference |
| WOMAT.EXTRA | EXTRA | Extra/UDF field |

Note: MTWO.PRODCODE uses MTWO prefix (WO header), not WOMAT prefix.

---

## MTLOT.* namespace — lot tracking (22 vars)

Available in T7CUTSHEET2 (lot-enabled variant only):

| Var | Field | Meaning |
|-----|-------|---------|
| MTLOT.CODE | CODE | Lot code (item) |
| MTLOT.KEY | KEY | Lot key |
| MTLOT.LOT | LOT | Lot number |
| MTLOT.EXPDATE | EXPDATE | Lot expiry date |
| MTLOT.ONHAND | ONHAND | Quantity on hand |
| MTLOT.PO | PO | PO that received this lot |
| MTLOT.RECDOC | RECDOC | Receipt document number |
| MTLOT.VENDOR | VENDOR | Vendor who supplied lot |
| MTLOT.RECDATE | RECDATE | Receipt date |
| MTLOT.RECQTY | RECQTY | Received quantity |
| MTLOT.POCOST | POCOST | PO cost for this lot |
| MTLOT.WO | WO | WO that consumed this lot |
| MTLOT.INRECDATE | INRECDATE | Incoming receipt date |
| MTLOT.WOQTY | WOQTY | WO issue quantity from this lot |
| MTLOT.WOCOST | WOCOST | WO issue cost from this lot |
| MTLOT.NOTES | NOTES | Lot notes |
| MTLOT.LOC | LOC | Lot location |
| MTLOT.WOSUF | WOSUF | WO suffix consuming this lot |
| MTLOT.EXTRA | EXTRA | Extra/UDF |
| MTLOT.BEGIN | BEGIN | Beginning balance |
| MTLOT.OUT | OUT | Quantity issued out |
| MTLOT.MAXOUT | MAXOUT | Maximum quantity that can be issued |

---

## MTWO.WIP.* namespace — WO header status (20 vars in T7CUTSHEET2b)

T7CUTSHEET2b confirms access to the WO production status namespace:

| Var | Field | Meaning |
|-----|-------|---------|
| MTWO.WIP.WOPRE | WOPRE | WO prefix |
| MTWO.WIP.WOSUF | WOSUF | WO suffix |
| MTWO.WIP.BLANK | BLANK | Blank/clear flag |
| MTWO.WIP.MULT | MULT | Multiple WO flag |
| MTWO.WIP.SQTY | SQTY | Scheduled quantity |
| MTWO.WIP.PRTY | PRTY | Priority |
| MTWO.WIP.SSTART | SSTART | Scheduled start date |
| MTWO.WIP.SFIN | SFIN | Scheduled finish date |
| MTWO.WIP.ASTART | ASTART | Actual start date |
| MTWO.WIP.AFIN | AFIN | Actual finish date |
| MTWO.WIP.COMQTY | COMQTY | Completed quantity |
| MTWO.WIP.STATUS | STATUS | WO status code |
| MTWO.WIP.LOCK | LOCK | Concurrent-entry lock |
| MTWO.WIP.ESETUP | ESETUP | Estimated setup cost |
| MTWO.WIP.EMAT | EMAT | Estimated material cost |
| MTWO.WIP.EOUTPR | EOUTPR | Estimated outside-process cost |
| MTWO.WIP.ELABOR | ELABOR | Estimated labor cost |
| MTWO.WIP.ASETUP | ASETUP | Actual setup cost |
| MTWO.WIP.AMAT | AMAT | Actual material cost |
| MTWO.WIP.AOUTPR | AOUTPR | Actual outside-process cost |

See PA module doc for the full 76-var MTWO.WIP.* + MTWORO.* extended namespace.

---

## Control and filter variables

| Var | Meaning |
|-----|---------|
| EJOB | Filter by WO number |
| ELOT | Filter by lot number |
| EQTY | Filter by quantity |
| EPART | Filter by part/item code |
| EUSER / EPASS | Authentication gate (user/password) |
| WHOAMI | Current logged-in user |
| MODE | Display/print mode flag |
| WOTOTQTY | Grand total WO quantity |
| WOQTY | WO quantity (from header) |
| FABQTY | Fabricated/completed quantity |
| ABIQTY | WO remaining quantity (to be issued) |
| LEFTQTY | Quantity left to cut |
| GT.MAT | Grand total material cost |
| GT.ISS | Grand total issued quantity (T7CUTSHEET2b) |
| EDESC | Description filter (T7CUTSHEET2b) |

---

## File handles

| Handle | Table |
|--------|-------|
| WOEMAT.H | WOMAT (material issues) |
| ICMSTR.H | BKICMSTR (inventory master) |
| WORKORD.H | WORKORD (WO header) |
| LOT.H | LOT (lot master) |
| WOBOM.H | WOBOM (planned BOM) |
| LINKS.H | ISLINKS (document links) |
| BKPSUSER_HNDL | BKPSUSER (password auth) |
| BINLOT.H | ISBINLOT (bin+lot — T7CUTSHEET2b) |

---

## Workflow

1. User enters WO number (EJOB) + optional lot/part filters (ELOT/EPART)
2. EUSER/EPASS gate — authentication check via BKPSUSER
3. T7CUTSHEET2 reads WOBOM for planned components, then WOMAT for issued quantities
4. For lot-enabled variant: traverses MTLOT.* for each component to show lot-by-lot breakdown
5. Computes WOQTY/FABQTY/ABIQTY/LEFTQTY for quantity summary
6. GT.MAT = total material cost; GT.ISS = total issued qty
7. Output: printed cut sheet or screen display showing what materials are needed vs. issued

---

## Confidence notes

- WOMAT.* 17-var namespace: confirmed from var extraction (Pass 233)
- MTLOT.* 22-var namespace: confirmed from var extraction (Pass 233)
- MTWO.WIP.* 20-var subset: confirmed from T7CUTSHEET2b extraction (Pass 233)
- Authentication gate (EUSER/EPASS/BKPSUSER_HNDL): confirmed from var extraction
- T7CUTSHEET2b adds BINLOT.H, GT.ISS, EDESC vs T7CUTSHEET2: confirmed from extraction
- Workflow description inferred from var names and table access pattern
