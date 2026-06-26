# Serial Control (SC)

Status: verified (DDF schema confirmed; workflow from table structure + help content).

- **Module code**: `SC`
- **Tables**: 2 (`SERIAL`, `SERIALH`) — plus cycle-count support via ISSERCNT
- **Primary data tables**: `SERIAL.B` (30 fields), `SERIALH.B` (30 fields, identical schema)

→ See **[help-content.md](help-content.md)** for user-facing serial number procedures.

Serial Control tracks inventory at the individual unit level. Each serialized item has one SERIAL row from receipt through shipment or WO consumption. When the item ships to a customer, the row moves to SERIALH (history), preserving the complete provenance chain.

Serial-tracked items are identified by `BKICMSTR.BKIC_PROD_SERNO = Y`.

## Database tables (2)

| Table | File on disk | Fields | Primary key | Role |
| ----- | ------------ | -----: | ----------- | ---- |
| **SERIAL** | `SERIAL.B` | 30 | `MTSER_CODE` + `MTSER_SERIAL` | Active (in-stock) serial numbers |
| **SERIALH** | `SERIALH.B` | 30 | `MTSER_CODE` + `MTSER_SERIAL` | Shipped / consumed serial history |

## SERIAL / SERIALH — Serial Number Master (30 fields, confirmed from DDF schema.md, Pass 111b 2026-06-19)

Both tables have identical field schemas. SERIAL contains units currently in stock (MTSER_ONHAND > 0); SERIALH contains units that have been shipped to customers or consumed by WOs.

Primary key: `MTSER_CODE` (STRING 15, part code) + `MTSER_SERIAL` (STRING 25, serial number)

| Field | Type | Meaning |
|-------|------|---------|
| `MTSER_CODE` | STRING 15 | Part number (PK 1) |
| `MTSER_SERIAL` | STRING 25 | Serial number (PK 2) |
| `MTSER_LOT` | STRING 15 | Lot number (if item is also lot-tracked) |
| `MTSER_PO` | FLOAT | PO number that received this unit |
| `MTSER_RECDOC` | FLOAT | Receiving document number |
| `MTSER_VENDOR` | STRING 10 | Vendor code who supplied this unit |
| `MTSER_RECDATE` | DATE | Date received from vendor |
| `MTSER_POCOST` | FLOAT | Unit cost from PO |
| `MTSER_SO` | FLOAT | Sales order number that shipped this unit |
| `MTSER_CUSTCODE` | STRING 10 | Customer code the unit shipped to |
| `MTSER_SHIPDATE` | DATE | Date shipped to customer |
| `MTSER_SELLPRICE` | FLOAT | Selling price |
| `MTSER_WO` | FLOAT | Work order prefix that produced this unit |
| `MTSER_ISSDATE` | DATE | Date issued to work order |
| `MTSER_ISSCOST` | FLOAT | Unit cost at WO issue time |
| `MTSER_INRECDATE` | DATE | Date received from work order (WO completion) |
| `MTSER_INRECCOST` | FLOAT | Unit cost at WO completion |
| `MTSER_EXPDATE` | DATE | Expiration date |
| `MTSER_WOCODE` | STRING 15 | Part code produced by the WO |
| `MTSER_NOTES_1..5` | STRING 30 | Notes 1–5 (5 × 30 = 150 chars total) |
| `MTSER_ONHAND` | FLOAT | On-hand quantity (1 = in stock; 0 = shipped/consumed) |
| `MTSER_LOC` | STRING 10 | Warehouse location |
| `MTSER_WOSUF` | UBINARY | WO suffix |
| `MTSER_EXTRA` | STRING 50 | Extra / user-defined |
| `MTSER_BIN` | STRING 15 | Bin location |
| `MTSER_INV` | FLOAT | Invoice number that shipped this unit |

### Field notes

- **Full lifecycle in one row:** A single SERIAL row accumulates data across the unit's entire life. At receipt: MTSER_PO, VENDOR, RECDATE, POCOST. If issued to WO: MTSER_WO, ISSDATE, ISSCOST. After WO completion: MTSER_INRECDATE, INRECCOST. At shipment: MTSER_SO, CUSTCODE, SHIPDATE, SELLPRICE, INV. This makes SERIAL a complete unit biography.
- **SERIAL → SERIALH transition:** When a unit ships (or is consumed by a WO with no return), the row is moved (deleted from SERIAL, inserted into SERIALH). SERIALH is the searchable warranty/history archive.
- **MTSER_ONHAND:** For serialized items, this is always 1 (in stock) or 0 (not in stock). The BKICMSTR.BKIC_PROD_UOH field tracks total serialized on-hand by summing SERIAL rows.
- **Dual origin:** Like LOT, a serial number can originate from a PO purchase OR a WO completion. Purchased units have MTSER_PO; WO-manufactured units have MTSER_WO.

## Serial number workflow

```
Receive from PO (PO-L/PO-M → serial entry screen)
  → Create SERIAL row (MTSER_PO, VENDOR, RECDATE, POCOST)
  → MTSER_ONHAND = 1
  → BKICMSTR.UOH += 1
  → Log INVTXN (TYPE = receipt, MTIT_SERIAL = serial#)

Issue to Work Order (WO-C Issue → T7DCBSERIAL)
  → Update SERIAL: MTSER_WO, MTSER_ISSDATE, MTSER_ISSCOST
  → MTSER_ONHAND = 0 (now inside WO)

WO Completion (WO-E Receive → serial assignment)
  → Create NEW SERIAL row for manufactured serial#
  → MTSER_WO, MTSER_INRECDATE, MTSER_INRECCOST
  → MTSER_ONHAND = 1

Ship to Customer (SO-C / SH → serial assignment)
  → Update SERIAL: MTSER_SO, CUSTCODE, SHIPDATE, SELLPRICE, INV
  → MTSER_ONHAND = 0
  → Move row: SERIAL → SERIALH

Physical Inventory (PI-C → T7DCBSERIAL)
  → BKPISER = frozen serial snapshot; BKPISCNT = counted entry
  → PI-G detects missing/extra serials and posts INVTXN adjustments
```

## Related tables

| Table | Module | Relationship |
|-------|--------|-------------|
| `SERIALH` | SC | History archive — identical schema; rows moved here after shipment |
| `INVTXN` | IN | Full transaction audit log — all serial movements recorded here |
| `BKICMSTR` | IN | Item master — `BKIC_PROD_SERNO` flag enables serial tracking |
| `BKPISER` / `BKPISCNT` | PI | Physical inventory serial snapshot / count |
| `BKSOHLOT` / `BKSOHSER` | SO | Serial numbers recorded on shipped SO lines |
| `BKAR_TXN_SERIAL` | AR | Serial number on AR shipment transaction |
| `ISSERCNT` | SC | Serial counter / sequence number management (cycle count support) |
| `ISSCOMP` | SC | Compound serial tracking (T7SCOMP) |

---

## Programs (9 total, Pass 265 2026-06-25)

Data extracted from rwn_symbols.json.

| Program | Procs | Lib | DBs | Role / key tables |
|---------|------:|-----|----:|-------------------|
| `T7SCF.RWN` | 131 | LISTG60 | 32 | **SC-F** serial format setup / full serial editor; SERIAL + BKICMSTR |
| `T7SCC.RWN` | 121 | LISTG60 | 32 | **SC-C** serial inquiry/browse; SERIAL + BKICMSTR |
| `T7SCH.RWN` | 113 | EVO.LIB | 32 | **SC-H** serial history browser; MTICMSTR + SERIAL; BKAR.INV 86-var + MTWO.WIP 71-var |
| `T7SCG.RWN` | 92 | LISTG60 | 18 | **SC-G** serial format/counter setup; ISSERCNT + MTICMSTR + CLASMSTR |
| `T7SCE.RWN` | 88 | LISTG60 | 32 | **SC-E** serial edit; BKICMSTR + SERIAL |
| `T7SCA.RWN` | 78 | LISTG60 | 25 | **SC-A** serial master editor; SERIAL + MTICMSTR + BKYSMSTR; BKAR.INV 86-var |
| `T7SCB.RWN` | 59 | LISTG60 | 32 | **SC-B** assign serial control on items; BKICMSTR + MTICMSTR (sets BKIC_PROD_SERNO flag) |
| `T7SCOMP.RWN` | 54 | EVO.LIB | 32 | **SC-COMP** compound serial management; ISSCOMP table (serial assemblies) |
| `T7SCD.RWN` | 5 | stub | 32 | Stub — serial duplicate check (no business logic) |

**T7SCH** is the largest program by proc count after the two main editors. Its access to BKAR.INV 86-var and MTWO.WIP 71-var confirms serial history crosses into AR shipment and WO data — SC-H shows the complete chain: WO receipt → stock → shipment.

**T7SCG** is the serial counter/format program — it manages ISSERCNT which controls auto-generation of serial numbers (total length, start position, last number assigned). This is the "serial number format" setup that feeds the auto-assign logic in PO receipt and WO completion.

**T7SCOMP** manages ISSCOMP (compound serial assemblies) — this is for items where a serial number represents an assembly of multiple serialized components. Each compound serial record tracks which sub-serials are bound together.

---

## TAS6-era programs (BKSC*.RUN) — binary inventory (Pass 324)

Sources: string extraction from `samples/BKSC*.RUN`.

| File | Size | Menu Code | Title (from binary) | Key Tables |
|------|-----:|-----------|---------------------|------------|
| `BKSCA.RUN` | 209KB | SC-A | Edit Serial Numbers (active / archived) | SERIAL, SERIALH, MTICMSTR, BKARINV, BKICLOC, ISBINLOC, BKICLOCM, BKICMSTR |
| `BKSCB.RUN` | 181KB | SC-B | Assign Serial Control | MTICMSTR, BKICMSTR |
| `BKSCC.RUN` | 223KB | SC-C | Print Serial Availability | BKICMSTR, SERIAL, BKICLOCM, MTICMSTR, BKARTXN |
| `BKSCD.RUN` | 3KB | stub | dispatches → BKINOA | BKSYMSTR, BKINOA |
| `BKSCE.RUN` | 107KB | SC-E | Reconcile Inventory | BKICMSTR, SERIAL, MTICMSTR, BKICLOC |
| `BKSCF.RUN` | 53KB | SC-F | **Purchase Order Serial Control** | BKAPPO, BKAPPOL, MTICMSTR, INVTXN, SERIAL |
| `BKSCG.RUN` | 56KB | SC-G | **Sales Order Serial Control** | BKARINV, BKARINVL, MTICMSTR, INVTXN, SERIAL |
| `BKSCHKYS.RUN` | 5KB | stub | Key selection | TASCOLOR, FILEKNUM |

### T6 vs T7 menu assignment shift

In TAS6, SC-F = "Purchase Order Serial Control" and SC-G = "Sales Order Serial Control". In TAS7, those functions moved and T7SCF became the "Serial Format / Full Serial Editor" while T7SCG became "Serial Format/Counter Setup". The TAS6 SC-F/G covered the PO→serial and SO→serial assignment operations; in T7 these are handled by PO-L/PO-M and SO-C entry screens directly.

### SC-B part type restriction (confirmed from binary)

BKSCB.RUN contains: `"Serial numbering is not allowed for part types N, L, T, K, B, or O."`

This constrains which item types can be serial-tracked:

| Type | Meaning | Serializable? |
|------|---------|:---:|
| N | Non-stocked / misc charge | No |
| L | Labor | No |
| T | Text / description line | No |
| K | Kit header | No |
| B | Bulk material | No |
| O | Outside process | No |
| M / F / P / etc. | Standard manufactured/purchased | Yes |

### MTIT.* namespace — INVTXN field prefix (confirmed from BKSCF/BKSCG)

BKSCF and BKSCG use `MTIT.*` to access INVTXN fields during serial assignment:

| TAS variable | Meaning |
|-------------|---------|
| `MTIT.TYPE` | Transaction type |
| `MTIT.CLASS` | Item class |
| `MTIT.DATE` | Transaction date |
| `MTIT.CODE` | Part number |
| `MTIT.QTY` | Quantity |
| `MTIT.SERIAL` | Serial number on transaction |
| `MTIT.INVOICE` | Invoice number |
| `MTIT.LOT` | Lot number |
| `MTIT.LOC` | Warehouse location |
| `MTIT.PRICE` | Unit price |
| `MTIT.DESC` | Description |

This confirms `MTIT` = `INVTXN` (prefix `MTIT_` maps to `INVTXN` Btrieve file). Previously only `MTIT_SERIAL` was known as an INVTXN field; this establishes the full field-access namespace used by SC programs.

### SC-F / SC-G field accessors (confirmed, Pass 324)

BKSCF — BKAP.PO.* and BKAP.POL.* fields accessed for PO serial linkage:
`BKAP.PO.NUM`, `BKAP.PO.VNDCOD`, `BKAP.PO.VNDNME`, `BKAP.PO.ORDDTE`, `BKAP.PO.TOTAL`, `BKAP.POL.PONM`, `BKAP.POL.PCODE`, `BKAP.POL.RQTY`, `BKAP.POL.IQTY`, `BKAP.POL.WOPRE`, `BKAP.POL.ARD`

BKSCG — BKAR.INV.* and BKAR.INVL.* fields accessed for SO serial linkage:
`BKAR.INV.SONUM`, `BKAR.INV.NUM`, `BKAR.INV.CUSCOD`, `BKAR.INV.CUSNME`, `BKAR.INV.CUSORD`, `BKAR.INV.SHPCOD`, `BKAR.INV.SHPNME`, `BKAR.INV.TOTAL`, `BKAR.INV.DESC`, `BKAR.INV.JOBNUM`, `BKAR.INV.INVCD`, `BKAR.INVL.INVNM`, `BKAR.INVL.PCODE`, `BKAR.INVL.USTD`, `BKAR.INVL.ASD`

Both programs also use `MTSER.*` (SERIAL table fields) and `CHECK_OPEN_ONLY` filter.

**Confidence: 92/100** — All 9 T7 programs confirmed from rwn_symbols.json; SERIAL/SERIALH schemas confirmed from DDF; ISSERCNT and ISSCOMP confirmed from program DB lists; TAS6 8-program binary inventory confirmed (Pass 324); SC-B part type restriction string confirmed; MTIT.* namespace (INVTXN fields) confirmed from BKSCF/BKSCG; T6→T7 menu assignment shift documented; BKINOA stub target identified.
