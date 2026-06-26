# Estimating (ES)

Status: verified | Pass 315 2026-06-25

Sources: DDF schema (tier2-tables.md), DFM field analysis (T7ESB/C/D/E/H/I.DFM), CHM help content.

- **Module code**: `ES`
- **Tables**: 5 core (BKESTCFG, BKESTQT, BKESTQTL, ESTSUM + BKMATCST for ES-H)
- **UI forms**: 7 (T7ESB/C/D/E/H/I/T)
- **Menu operations**: 8

---

## Menu operations

| Code | Operation | Programs | Confidence |
| ---- | --------- | -------- | ---------- |
| `ES-A` | Enter Estimates (main + sub-programs) | BKESA;BKESAA;BKESAB;BKESAC;BKESH | 92 (binary confirmed) |
| `ES-B` | Print Estimates | BKESB (T7ESB.DFM) | 85 (DFM confirmed) |
| `ES-C` | Enter Quote Templates | BKESC;BKESCA (T7ESC.DFM) | 90 (binary + DFM confirmed) |
| `ES-D` | Print Customer Quotes | BKESD (T7ESD.DFM) | 85 (DFM confirmed) |
| `ES-E` | Convert Estimates to WO/SO | BKESE (T7ESE.DFM) | 85 (DFM confirmed) |
| `ES-F` | Copy Estimates | BKESF | 75 (table structure) |
| `ES-G` | Print Estimate Listing | BKESG | 75 (table structure) |
| `ES-H` | Enter Material Costs | BKESH (T7ESH.DFM) | 90 (DFM + BKMATCST schema confirmed) |
| `ES-I` | Print Material Costs | BKESI (T7ESI.DFM) | 85 (DFM confirmed) |

---

## UI forms — DFM field analysis (Pass 315)

### T7ESB — ES-B Print Estimates

| FieldName | Meaning |
|-----------|---------|
| `ETBcomboval` | Printer/destination selector grid |
| `PLDTYPE` | Print layout type |
| `from.cust` / `thru.cust` | Customer range filter |
| `from.cclass` / `thru.cclass` | Customer class range filter |
| `sFROM.SONUM` / `sTHRU.SONUM` | Sales order number range filter |
| `from.job` / `thru.job` | Job number range filter |
| `PRT.ext` | Include extended details flag |
| `ISPRT.NOTES` | Include notes flag |
| `ISPRT.HID.NOTES` | Include hidden notes flag |
| `ISPRT.KIT` | Include kit components flag |
| `ISPRT.ECO` | Include ECO reference flag |
| `prt.xref` | Print cross-reference flag |

### T7ESC — ES-C Configure Quote Print Templates

Selects which sections to include in the printed estimate/quote. The 10 `PRINT.REPORT[N]` flags
are Y/N toggles controlling each printable section of the quote template.

| FieldName | Meaning |
|-----------|---------|
| `ETBcomboval` | Template selector grid |
| `SELECT_FROM1` / `SELECT_THRU1` | Template range |
| `PRINT.REPORT[1..10]` | Ten section-inclusion flags (Y/N each) |
| `ISPRINT.REPT11` | Additional report section 11 flag |
| `ISPRT.2ND.DESC` | Print second description line flag |
| `ISPRT.BOMMULT` | Include BOM multiplier in print |
| `ISPRT.BOMDET` | Include BOM detail lines |
| `ISPRT.ROUTDET` | Include routing operations detail |
| `ISPRT.EXTRAS` | Include surcharges/extras |

### T7ESD — ES-D Print Customer Quotes

| FieldName | Meaning |
|-----------|---------|
| `ETBcomboval` | Printer selector |
| `sFROM.QTNUM` / `sTHRU.QTNUM` | Quote number range |
| `from.cust` / `thru.cust` | Customer range |
| `from.cclass` / `thru.cclass` | Customer class range |
| `from.expdate` / `thru.expdate` | Quote expiration date range |
| `qt.status` | Quote status filter (e.g. Open, Accepted, Lost) |
| `consolidated` | Print consolidated version flag |
| `prt.ext` | Include extended detail |
| `ais.dec` | AIS decimal format flag |
| `PLDTYPE` | Print layout type |

### T7ESE — ES-E Convert Estimates

Converts a quote/estimate to a Sales Order and/or Work Order. Key fields:

| FieldName | Meaning |
|-----------|---------|
| `sFROM.QUOTE` | Source quote number to convert |
| `ISTO.WO` | Convert to Work Order flag |
| `ISTO.SO` | Convert to Sales Order flag |
| `ISTO.PROD` | Convert to production/template item flag |
| `SO.NUM` | Existing SO to add lines to (if not creating new) |
| `sWO.NUM` | WO number (if converting to WO) |
| `incl.est.no` | Include estimate reference number on order |
| `is.est.cust` | Use estimated customer (not a confirmed customer) |
| `CUST.PO` | Customer PO number |
| `LOCATION` | Warehouse location |
| `START.DATE` / `FINISH.DATE` | WO scheduled start and finish |
| `ESD.DATE` | Estimated ship date |
| `SELL.PRICE` | Override selling price |
| `ORD.QTY` | Order quantity |
| `ISUPD.CONTRACT` | Update contract pricing flag |
| `APART` / `AQTY` / `APRICE` | Additional line: part, qty, price |
| `AESD` / `AWSD` / `AWFD` | Additional line: ship date, WO start, WO finish |
| `UCP` | Unit cost price |

### T7ESH — ES-H Enter Material Costs (BKMATCST editor)

ES-H edits the `BKMATCST` table — a 10-tier quantity-break pricing schedule for materials
used in estimating. The DFM shows tiers 1–5; the DDF schema confirms 10 tiers exist in the table.

| FieldName | Maps to BKMATCST field | Meaning |
|-----------|----------------------|---------|
| `BKMC.CODE` | `BKMC_CODE` (PK) | Material part number |
| `BKIC.PROD.DESC` | (BKICMSTR display) | Item description — read-only display |
| `BKMC.DATE` | `BKMC_DATE` | Effective date of this price schedule |
| `BKMC.COST[1..5]` | `BKMC_COST_1..5` | Unit cost for quantity tier 1–5 |
| `BKMC.QTY[1..5]` | `BKMC_QTY_1..5` | Quantity breakpoint for tier 1–5 |
| `MTIC.PROD.VEND[1]` | (MTICMSTR display) | Primary vendor — read-only |
| `MTIC.PROD.LEAD` | (MTICMSTR display) | Lead time — read-only |
| `MTIC.PROD.STDPK` | (MTICMSTR display) | Standard pack qty — read-only |
| `MTIC.PROD.SPECS[1..2]` | (MTICMSTR display) | Spec fields 1–2 — read-only |

### T7ESI — ES-I Print Material Costs

| FieldName | Meaning |
|-----------|---------|
| `from.item` / `thru.item` | Item number range |
| `from.date` / `thru.date` | Effective date range |
| `ETBcomboval` | Printer selector |

---

## Database tables

| Table | File on disk | Fields | PK | Purpose |
| ----- | ------------ | -----: | -- | ------- |
| **BKESTCFG** | `BKESTCFG.B` | 13 | `BKEST_CFG_NUM` | Estimating system configuration per estimate number |
| **BKESTQT** | `BKESTQT.B` | 84 | `BKAR_INV_NUM` | Quote header — clones BKARINV structure + `QSTAT`/`MDATE`/`MISC` |
| **BKESTQTL** | `BKESTQTL.B` | 28 | `BKAR_INVL_INVNM`+`CNTR` | Quote lines — clones BKARINVL structure + `ESD`/`SCCOG` |
| **ESTSUM** | `ESTSUM.B` | 213 | `MTESUM_QUOTE` | Full estimate summary: materials + routing + charges; `BOM_FLAG`/`RT_FLAG`/`EX_FLAG` mark WO-transfer status |
| **BKMATCST** | `BKMATCST.B` | 25 | `BKMC_CODE` | Material cost schedule: 10-tier qty-break pricing per item; edited by ES-H |

### BKMATCST — Material Cost Schedule (Pass 315, DFM + DDF confirmed)

The `BKMATCST` table stores up to 10 quantity-break price tiers per material item.
ES-H edits tiers 1–5 through the DFM; all 10 tiers exist in the DDF schema.

| Field prefix | DDF field | Meaning |
|-------------|-----------|---------|
| `BKMC.CODE` | `BKMC_CODE` | Part number (PK), STRING 15 |
| `BKMC.DATE` | `BKMC_DATE` | Effective date |
| `BKMC.QTY[1..10]` | `BKMC_QTY_1..10` | Quantity breakpoints (10 tiers) |
| `BKMC.COST[1..10]` | `BKMC_COST_1..10` | Unit cost at each tier (10 tiers) |
| (extra fields) | `MIN` / `MINCST` / `EXTRA` | Min order qty, min cost charge, misc |

---

## Architecture notes

- **BKESTQT mirrors BKARINV**: The estimating quote header reuses the AR Invoice field structure
  (same `BKAR_INV_*` prefix), adding `QSTAT` (quote status), `MDATE`, and `MISC`. This means
  ES-E Convert Estimates can directly promote a quote to an AR Invoice line-for-line.
- **BKESTQTL mirrors BKARINVL**: Same pattern on the lines table; adds `BKAR_INVL_ESD` (estimated
  ship date) and `BKAR_INVL_SCCOG`.
- **ESTSUM is the detailed estimate**: Separate from the BKESTQT quote header, ESTSUM holds the
  full BOM + routing + surcharge estimate. `MTESUM_BOM_FLAG` / `RT_FLAG` / `EX_FLAG` track
  whether each section has been transferred to a WO.
- **ES-A copies from RFQ**: ES-A imports RFQs from the PO module (uses BKPOA/BKPOF programs),
  converting vendor RFQ responses into estimates.
- **ES-E conversion**: Converts estimate → SO (BKESTQT lines → BKARINVL) and/or WO (ESTSUM BOM → WOBOM)
  in one operation. Supports adding lines to an existing order.

---

## TAS6-era programs (BKES*.RUN) — binary inventory (Pass 324)

Sources: string extraction from `samples/BKES*.RUN`.

| File | Size | Menu Code | Title (from binary) | Key Tables |
|------|-----:|-----------|---------------------|------------|
| `BKESA.RUN` | 310KB | ES-A | Enter Estimates (main router) | BKESTCFG, ESTSUM, BKARCUST, BKICMSTR, BKRTCST, BKRFQ, BKBMMSTR, BKMATCST, ROUTING, WORKCTR, WORKORD |
| `BKESAA.RUN` | 147KB | ES-A | Enter Estimates [Bill of Materials] | BKFOCFG, BKBMMSTR, BKBMREMK, BKBMNOTE, BKBMDIM, MACHINE, BKICDIM, BKMATRIM |
| `BKESAB.RUN` | 249KB | ES-A | Enter Estimates [Routings] | ROUTING, ESTSUM, WORKCTR, BKRTCST, BKRTSPEC, BKRTTEMP, BKICMSTR |
| `BKESAC.RUN` | 107KB | ES-A | Enter Estimates [Material Dimensions] | BKICDIM, BKICMSTR, BKBMMSTR (BKICDIM field accessors below) |
| `BKESAV.RUN` | 7KB | stub | help dispatch → BKESAA | BKSYMSTR, BKSYHELP |
| `BKESB.RUN` | 199KB | ES-B | Print Estimates | BKESTCFG, ESTSUM, BKARCUST, BKICMSTR, BKRFQ, BKBMMSTR, BKBMNOTE, BKBMREMK, ROUTING, BKRTCST, BKMATCST; dispatches → BKESA, BKESE |
| `BKESC.RUN` | 61KB | ES-C | Enter Quote Templates | ESTSUM (MTESUM.*), BKQTTEMP, BKQTNOTE; dispatches → BKESCA |
| `BKESCA.RUN` | 37KB | ES-C | Enter Quote Templates [Print] | BKQTTEMP |
| `BKESD.RUN` | 213KB | ES-D | Print Customer Quotes [Letterhead] / [Universal] | BKESTCFG, ESTSUM (MTESUM.* 20+ fields), BKARCUST; reads all MTESUM.NOTES[1..10] |
| `BKESE.RUN` | 302KB | ES-E | Convert Estimates → SO/WO | ESTSUM, BKARINV, BKARINVL, WORKORD, WOBOM, BKBMMSTR, BKRFQ, WODATE, BKGLTRAN, BKICLOCM |
| `BKESEA.RUN` | 77KB | ES-E | Convert sub-program (WO match/assign) | ESTSUM, MTICMSTR, WORKORD, ROUTING, WOBOM, BKMATCST; MTWO.WIP.* and MTESUM.* namespace access |
| `BKESF.RUN` | 196KB | ES-F | Copy Estimates | BKESTCFG, ESTSUM, BKICMSTR, BKBMMSTR, BKBMREMK, ROUTING, BKRTSPEC, BKMATCST, BKQTNOTE |
| `BKESG.RUN` | 224KB | ES-G | Print Estimate Listing | ESTSUM, BKARCUST, BKCMACCT, BKICMSTR |
| `BKESH.RUN` | 183KB | ES-A / ES-H | Enter Estimates [Material Costs] / Enter Material Costs | BKMATCST, BKICMSTR |
| `BKESI.RUN` | 95KB | ES-I | Print Material Costs | BKMATCST, BKICMSTR; field accessors: BKMC.CODE/DATE/QTY/COST, BKIC.PROD.CODE/DESC |

### ES-A sub-program architecture

ES-A in TAS6 is a multi-tab form delivered via the main router (BKESA) plus four sub-programs, each handling a distinct tab of the estimate:

| Sub-program | Tab |
|-------------|-----|
| BKESA | Main header + summary |
| BKESAA | Bill of Materials |
| BKESAB | Routings |
| BKESAC | Material Dimensions |
| BKESH | Material Costs (also ES-H standalone) |

**Correction (Pass 324):** ES-A is "Enter Estimates" — not "Copy RFQs to Estimates" as prior menu_codes.csv analysis inferred. The BKESA.RUN binary title string `"ES-A  Enter Estimates"` is definitive. RFQ import is handled as a sub-workflow within BKESA (opens BKRFQ), not the primary purpose.

### BKICDIM field accessors (confirmed from BKESAC.RUN)

Material dimensions screen accesses these BKICDIM fields:

| TAS variable | Meaning |
|-------------|---------|
| `BKICDIM.PARENT` | Parent part number |
| `BKICDIM.PARTNO` | Component/dimension part number |
| `BKICDIM.FIRST` | First dimension (width) |
| `BKICDIM.F.TOL` | First dimension tolerance |
| `BKICDIM.SECOND` | Second dimension (length/height) |
| `BKICDIM.S.TOL` | Second dimension tolerance |
| `BKICDIM.THICK` | Material thickness |
| `BKICDIM.T.TOL` | Thickness tolerance |
| `BKICDIM.SETUP` | Setup code |
| `BKICDIM.DENSITY` | Material density |

### Cross-module links from ES binary

- BKESE opens `BKGLTRAN` — ES-E posts GL entries during estimate→order conversion (overhead/cost transfer)
- BKESEA accesses `MTWO.WIP.*` namespace (WO master) for WO assignment during convert
- BKESF reads `BKQTNOTE` — Copy Estimates also duplicates quote note content
- BKESD reads `MTESUM.NOTES[1..10]` — 10 free-text note lines on estimates

**Confidence: 93/100** — DFM field sets fully confirmed (Pass 315) for 6 of 8 programs;
BKMATCST 25-field schema confirmed from DDF; BKESTQT/BKESTQTL/ESTSUM schemas from DDF;
TAS6 15-program inventory confirmed from binary (Pass 324); ES-A sub-program architecture
confirmed; BKICDIM field namespace confirmed; ES-A title corrected to "Enter Estimates".
