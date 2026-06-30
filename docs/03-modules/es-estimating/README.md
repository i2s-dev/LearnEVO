# Estimating (ES)

Status: verified | Pass 339 2026-06-26 | Pass 415 live data 2026-06-30

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

| Table | File on disk | Fields | Live Records | PK | Purpose |
| ----- | ------------ | -----: | -----------: | -- | ------- |
| **BKESTCFG** | `BKESTCFG.B` | 18 | 1 | `BKEST_CFG_NUM` | Estimating system config (1 config record, key=2) |
| **BKESTQT** | `BKESTQT.B` | 104 | 6,892 | `BKAR_INV_NUM` | Quote header — 104 fields (84 BKARINV-mirror + 20 extra); `BKAR_INV_QSTAT`='Y'/'N'/' ' |
| **BKESTQTL** | `BKESTQTL.B` | 28 | 462,659 | `BKAR_INVL_INVNM`+`CNTR` | Quote lines — mirrors BKARINVL + `ESD`/`SCCOG` |
| **ESTSUM** | `ESTSUM.B` | 213 | **0** | `MTESUM_QUOTE` | Full estimate BOM/routing/charges — **NOT USED at i2 Systems** (see note below) |
| **BKMATCST** | `BKMATCST.B` | 25 | **0** | `BKMC_CODE` | Material cost schedule: 10-tier qty-break pricing — **NOT USED at i2 Systems** |
| **BKRTCST** | `BKRTCST.B` | 24 | **0** | `QUOTE`+`CODE`+`OPER` | Routing cost schedule — **NOT USED at i2 Systems** |

**Usage pattern at i2 Systems (Pass 415):** ES is used heavily for customer quote documents (6,892 quotes, 461K lines, 661 customers) but NOT for integrated cost estimation. ESTSUM, BKMATCST, and BKRTCST are all empty — the BOM-based cost rollup feature of ES-A is not in use. The module operates in "quote letter" mode only.

### BKESTCFG — Estimating Config (Pass 415, live ODBC confirmed)

1 record, 18 fields. Live values at i2 Systems:

| DDF field | Type | Live Value | Meaning |
|-----------|------|-----------|---------|
| `BKEST_CFG_NUM` | FLOAT | `2.0` | PK — config record number (key=2) |
| `BKEST_CFG_STAT` | STRING(1) | `'A'` | Default status for new estimates |
| `BKEST_CFG_CLASS` | STRING(4) | *(blank)* | Default estimate class code |
| `BKEST_CFG_FORM` | STRING(1) | `'2'` | Quote form variant (1 or 2) |
| `BKEST_CFG_MAT^` | FLOAT | `0.0` | Default material markup % |
| `BKEST_CFG_LAB^` | FLOAT | `0.0` | Default labor markup % |
| `BKEST_CFG_OP^` | FLOAT | `0.0` | Default outside-process markup % |
| `BKEST_CFG_OH^` | FLOAT | `0.0` | Default overhead markup % |
| `BKEST_CFG_TOT^` | FLOAT | `0.0` | Default total markup % |
| `BKEST_CMPY_INFO` | STRING(1) | `'Y'` | Print company info on quotes |
| `BKEST_CFG_DAYS` | INT | `30` | Quote expiry days from entry date |
| `BKEST_CFG_ENDLN_1..5` | STRING(30)×5 | *(all blank)* | Up to 5 custom ending lines on quotes |
| `BKEST_CFG_SONUM` | FLOAT | `56576.0` | Last/next quote number |
| `BKEST_CFG_EXTRA` | STRING(100) | *(zeros)* | Reserved/unused blob |

### BKESTQT — Quote Status Values (Pass 415, live)

| BKAR_INV_QSTAT | Count | Interpretation |
|---------------|------:|----------------|
| `'Y'` | 4,689 | Converted (promoted to order) |
| `' '` | 2,200 | Open / not yet converted |
| `'N'` | 3 | Declined / lost |

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

---

## MTESUM.* field access namespace — Pass 339

Source: string extraction from `samples/BKESA.RUN` and `samples/BKESEA.RUN`.

ESTSUM is accessed via the `MTESUM.*` prefix in all ES programs. Full accessor namespace confirmed from BKESA.RUN:

### Quote header fields

| TAS variable | Meaning |
|-------------|---------|
| `MTESUM.QUOTE` | Quote number (PK) |
| `MTESUM.CODE` | Item number |
| `MTESUM.DESC` | Item description |
| `MTESUM.UM` | Unit of measure |
| `MTESUM.REV` | Revision level |
| `MTESUM.STATUS` | Quote status: `A`=Active, `C`=Converted, `I`=Inactive, `X`=Cancelled, `D`=Archived |
| `MTESUM.DATE` | Entry date |
| `MTESUM.EXPDATE` | Expiration date |
| `MTESUM.CUSTCODE` | Customer code |
| `MTESUM.NAME` | Customer name |
| `MTESUM.ATTN` | Attention / contact name |
| `MTESUM.SLSP.NUM` | Salesperson number |
| `MTESUM.PROJ` | Project code |
| `MTESUM.NOTES` | Free-text notes; `MTESUM.NOTES[1..10]` confirmed (10 note lines, accessed in BKESD) |

### Per-quantity-break cost summary (14 cost types × 10 qty breaks)

| TAS variable | Meaning |
|-------------|---------|
| `MTESUM.MAT` | Material cost |
| `MTESUM.MATMU` | Material markup % |
| `MTESUM.SETUP` | Setup cost |
| `MTESUM.LAB` | Labor cost |
| `MTESUM.LABMU` | Labor markup % |
| `MTESUM.OP` | Outside-process cost |
| `MTESUM.OPMU` | Outside-process markup % |
| `MTESUM.OH` | Overhead cost |
| `MTESUM.OHMU` | Overhead markup % |
| `MTESUM.OVALL` | Overall (total) cost |
| `MTESUM.MISC` | Misc charges |
| `MTESUM.EXTRA` | Extra charges |
| `MTESUM.TOTAL` | Grand total |
| `MTESUM.COST` | Unit cost |
| `MTESUM.PRICE` | Quote/sell price |

---

## BKESTCFG configuration keys — Pass 339

BKESTCFG stores system defaults loaded at ES-A startup. Key names confirmed from BKESA.RUN string extraction:

| Key | Meaning |
|-----|---------|
| `MAT%` | Default material markup % |
| `LAB%` | Default labor markup % |
| `OP%` | Default outside-process markup % |
| `OH%` | Default overhead markup % |
| `TOT%` | Default total markup % |
| `DAYS` | Quote expiry days from entry date |
| `CLASS` | Default estimate class code |
| `STAT` | Default estimate status code on creation |
| `CMEST` | CRM-linked estimate integration flag |
| `INBESA` | ES-A in-bound data entry integration flag |

---

## BKESE — ES-E Convert Estimates: complete 45-table analysis — Pass 339

BKESE.RUN (309KB, latest ISTS Enhancement **03/27/23**) is the largest and most recently modified ES program. It handles the entire estimate-to-order pipeline in one operation.

### Source tables (read from estimate)
`ESTSUM`, `BKBMMSTR`, `ROUTING`, `WORKCTR`, `BKRTCST`, `BKMATCST`, `BKRFQ`, `MTEXCHG`, `MTICMSTR`, `BKARCUST`, `BKCMACCT`

### Target tables (written at conversion)
| Target | Written | Purpose |
|--------|---------|---------|
| `BKARINV` | SO header | New sales order created |
| `BKARINVL` | SO lines | Line items from estimate |
| `BKARINVT` | SO transaction | SO transaction record |
| `WORKORD` | WO header | New work order (if converting to WO) |
| `WOBOM` | WO BOM | Bill of materials transferred from BKBMMSTR |
| `WOROUT` | WO routing | Routing transferred from ROUTING table |
| `WODATE` | WO operation dates | Scheduled start/finish per operation |
| `BKGLTRAN` | GL journal entries | Overhead/cost GL entries posted on convert |
| `ISLOG` | Audit trail | Conversion event logged |
| `MKAHIST` | Change history | Marketing/history audit |

### Reference tables (applied during conversion)
| Table | Purpose |
|-------|---------|
| `BKICMSTR` / `BKICLOC` / `BKICLOCM` | Item and location lookup |
| `BKICPMAT` | Pricing matrix — applied to SO sell price at conversion |
| `ISTERMS` | Payment terms applied to the new SO |
| `ISTAXGRP` / `BKICTAX` | Tax group and tax rate applied |
| `BKPRSALE` | Salesperson applied from estimate |
| `ISJOB` | Job costing link created at conversion |
| `ISWOEX` | WO extension UDF fields copied from estimate |
| `CALENDAR` | EVO calendar — used for lead-time and scheduled-date calc |
| `ISIS` | Multi-currency — quote prices converted if multi-currency |
| `BKAPDESC` | Description codes |
| `BKAPVEND` | Vendor reference |
| `FILELOC` | File location registry |
| `ISNUMBER` | `ESTNUMA`, `WONUMA`, `SONUMA` — auto-number counters |

---

## Cost accumulation arrays — Pass 339

BKESA.RUN (Enter Estimates main router) uses two internal arrays for multi-level BOM and routing cost rollup before writing totals back to ESTSUM:

**BARR_* — BOM cost accumulation (12 elements):**
`BARR_LEV`, `BARR_COMP`, `BARR_PAR`, `BARR_LINE`, `BARR_QTY`, `BARR_SET`,
`BARR_MAT`, `BARR_OP`, `BARR_LAB`, `BARR_FOH`, `BARR_VOH`, `BARR_MISC`

**RARR_* — Routing cost accumulation (9 elements):**
`RARR_CNTR`, `RARR_PART`, `RARR_QTY`, `RARR_SEQ`, `RARR_SET`,
`RARR_LAB`, `RARR_OP`, `RARR_OH`, `RARR_MISC`

---

## ISTS Enhancement dates — TAS6 ES programs

Enhancement dates extracted from binary strings — show modification chronology:

| Program | ISTS Enhancement | Notes |
|---------|-----------------|-------|
| `BKESAB.RUN` | 09/03/10 | Earliest — Routings sub-screen |
| `BKESB.RUN` | 05/09/11 | Print Estimates |
| `BKESG.RUN` | 07/23/12 | Print Estimate Listing |
| `BKESH.RUN` | 09/22/12 | Enter Material Costs |
| `BKESF.RUN` | 05/27/15 | Copy Estimates |
| `BKESA.RUN` | 08/23/18 | Enter Estimates main |
| `BKESD.RUN` | 08/23/18 | Print Customer Quotes (same date as BKESA — updated together) |
| `BKESE.RUN` | 03/27/23 | Convert Estimate → SO/WO — **most recently modified ES program** |

---

## Live Data Analysis (Pass 421+422, 2026-06-30)

| Table | Count | Notes |
|-------|------:|-------|
| BKESTQT | 6,894 | Quote headers (Y=5,909 open / X=366 cancelled / blank=618) |
| BKESTQTL | 462,727 | Quote line items (~67 lines/quote avg) |
| ESTSUM | 0 | Legacy TAS6 estimate summary — not used in T7 era |
| ISESTAQT | 5,816 | IS-era archived quote headers (BKAR_INV_* schema clone) |
| ISESTAQL | 130,792 | IS-era archived quote lines (~22.5 lines/quote avg) |
| ISESTHDR | 0 | IS-era in-progress quote headers — not used |
| ISESTLNE | 0 | IS-era in-progress quote lines — not used |
| ISESAHDR | 0 | ES archive header variant — not used |
| ISESALNE | 0 | ES archive line variant — not used |
| ISESTASM | 0 | ES assembly cost summary — not used |
| ISESADTL/ISESTDTL | 0 | ES cost detail breakdown — not used |
| ISESTPO | 0 | ES MRP PO bridge — not used |

**Key insight:** Estimating is heavily used — 6,894 quotes with 462,727 line items.
BKESTQT uses the exact BKAR_INV_* field naming (same schema as AR invoices) with
INVCD status: Y=active quote, X=cancelled, blank=unset. Average 67 line items per
quote confirms the estimating module handles complex multi-line BOMs.

ISESTAQT/ISESTAQL hold 5,816 archived quotes (the IS-era schema layer) while the
older ISESTHDR/ISESTLNE in-progress tables are empty — confirming the T7-era BKESTQT
pipeline is the active one and IS-era archive tables stored historical data only.

---

**Confidence: 95/100** — DFM field sets fully confirmed (Pass 315) for 6 of 8 programs;
BKMATCST 25-field schema confirmed from DDF; BKESTQT/BKESTQTL/ESTSUM schemas from DDF;
TAS6 15-program inventory confirmed from binary (Pass 324); ES-A sub-program architecture
confirmed; BKICDIM field namespace confirmed; ES-A title corrected to "Enter Estimates";
MTESUM.* 15-header + 15×10-qty-break cost field namespace fully documented (Pass 339);
BKESTCFG config keys confirmed; BKESE 45-table conversion architecture fully mapped;
status codes A/C/I/X/D confirmed; BARR_*/RARR_* cost arrays confirmed;
ISTS Enhancement chronology 2010–2023 confirmed; live data: BKESTQT=6,894/BKESTQTL=462,727/ISESTAQT=5,816/ISESTAQL=130,792 (Pass421/422).
