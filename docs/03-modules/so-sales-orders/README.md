# Sales Orders (SO)

Status: verified (auto-generated from the extracted schema, menu-code dump, and DFM inventory).

- **Module code**: `SO`
- **Tables**: 7 (prefixes `BKSO`)
- **UI forms**: 69 (prefixes `T7SO`, `T6SO`, `BKSO`)
- **Menu operations**: 48

## Menu operations

| Code | Operation | Legacy module file(s) |
| ---- | --------- | --------------------- |
| `SO-A` | View | BKSOA;BKSOA2;ISSRA;ISTECH;JKSOS1S |
| `SO-B` | Print Acknowledgements | BKSOB;BKSOBB;ISTECH;T6ALSOB;t6sob |
| `SO-C` | Print Pick Ticket | BKSOC;ISTECH;T6ALSOC;t6soc |
| `SO-D` | Print Shipping Labels | BKSOD;T6SOD;t6sodmsg |
| `SO-E` | Release Sales Orders | BKSOE;T6SOE |
| `SO-F` | Print/Reprint Invoices | BKSOF;ISTECH;T6ALSOF;T6SOF |
| `SO-G` | Post Invoices | BKSOG;BKSOGA;BKSOGSAV;ISSRGA |
| `SO-H` | Display Invoice History | BKSOH |
| `SO-I` | Customer Service Inquiry | BKSOI |
| `SO-J` | View Recurring Sales Orders | BKSOJ;BKSOJ2;t6SOJ;t6soj2 |
| `SO-K` | Generate Sales Orders from Recurring SO Templates | BKSOK |
| `SO-L` | Enter/Print Note Templates | BKSOL |
| `SO-M` | Print Template Forms | BKSOM;t6som |
| `SO-N` | Manual Mat Cost/Lab Hours | AUTOSON;BKSON;ISSON |
| `SO-O-A` | Print Open Sales Order Listing | BKSOOA |
| `SO-O-B` | Print Backorder Listing | BKSOOB |
| `SO-O-D` | Print Commissions by Sales Order | BKSOOD |
| `SO-O-E` | Print Shipping Schedule | BKSOOE |
| `SO-O-F` | Print Available to Ship | BKSOOF;t6soof |
| `SO-O-G` | Print Sales Order/Work Order Schedule | BKSOOG |
| `SO-O-H` | Print Invoice Listing | BKSOOH |
| `SO-O-I` | Print Released Sales Orders | BKSOOI |
| `SO-O-J` | Print User-Defined Detail | BKSAM;T6SAM |
| `SO-O-K` | Print User-Defined Summary | BKSAN;T6SAN;j6cfsan |
| `SO-O-M` | Print Sales Order Changes | ISSOOM |
| `SO-O-N` | Print OnTime Shipping Report | ISSOON |
| `SO-O-O` | Sales Order/Work Order Exception Report | ISSOOO;ISSROO |
| `SO-P-A` | Enter Sales Quotations | BKSOA;BKSOA2;BKSOJ;BKSOJ2;ISTECH |
| `SO-P-B` | Print Sales Quotations | BKSOPB;T6ALSOPB;T6SOPB |
| `SO-P-C` | Convert Sales Quotation | BKSOPC |
| `SO-P-D` | Print User-Defined Detail | BKSAM;T6SAM |
| `SO-P-E` | Print User-Defined Summary | BKSAN;T6SAN;j6cfsan |
| `SO-P-F` | Enter Return Authorization | BKSOA;BKSOA2;BKSOJ;BKSOJ2;t6SOJ |
| `SO-P-H` | Enter RMA- Edit Existing RMA | JKSOS1S;JKSOS2S;jksos1.run;jksos2.run |
| `SO-P-I` | Enter Freight & Tracking # | BKSOPI |
| `SO-P-J` | Post Shipped Items | ISSOPJ |
| `SO-P-K` | Close Sales Quotation | ISSOPK |
| `SO-P-L` | Enter Tracking # | BKSOPI |
| `SO-Q` | Customer Service Inquiry | BKSOQ |
| `SO-Q-A` | Enter Base Prices | BKSOQA |
| `SO-Q-B` | Print Base Prices | BKSOQB |
| `SO-Q-C` | Global Price Change | BKSOQC |
| `SO-Q-J` | Generate Base Prices | BKSOQJ |
| `SO-R` | Void Invoice | BKSOGA;BKSOR;ISSRGA |
| `SO-S-B` | Print Return Authorizations | JKSOSB;T6jksosb |
| `SO-T` | View | BKSOA;BKSOA2;BKSOJ;BKSOJ2;t6SOJ |
| `SO-U` | Convert Sales Orders to Purchase Orders | CRSOPO;ISSOPO |
| `SO-X` | Mass Void Invoice | ISMASVOD |

## UI forms (69)

| DFM file | Caption | fields | controls | tabs |
| -------- | ------- | -----: | -------: | ---: |
| `T7SOABKD.DFM` | Enter Booking Date | 1 | 5 | 0 |
| `T7SOAC.DFM` | T7SOA | 71 | 167 | 0 |
| `T7SOACITEM.DFM` |  | 0 | 1 | 0 |
| `T7SOACPY.DFM` | New Screen | 2 | 11 | 0 |
| `T7SOAE.DFM` |  | 0 | 1 | 0 |
| `T7SOAFRT.DFM` | Enter Freight | 1 | 5 | 0 |
| `T7SOAIMPLINES.DFM` |  | 0 | 1 | 0 |
| `T7SOAPRC.DFM` | Item Pricing | 4 | 11 | 0 |
| `T7SOAXCOM.DFM` |  | 0 | 1 | 0 |
| `T7SOB.DFM` | SO-B | 23 | 52 | 0 |
| `T7SOBIN.DFM` |  | 0 | 1 | 0 |
| `T7SOC.DFM` | SO-C | 59 | 118 | 0 |
| `T7SOD.DFM` |  | 0 | 1 | 0 |
| `T7SODDesc.DFM` | New Screen | 2 | 9 | 0 |
| `T7SODPallet.DFM` | New Screen | 2 | 4 | 0 |
| `T7SOE.DFM` |  | 0 | 1 | 0 |
| `T7SOF.DFM` | SO-F | 82 | 154 | 0 |
| `T7SOFDEP.DFM` | New Screen | 7 | 30 | 0 |
| `T7SOG.DFM` | SOG COGS Report | 12 | 38 | 0 |
| `T7SOGA.DFM` | SO-G-A Order Posting | 2 | 7 | 0 |
| `T7SOGACHK.DFM` | Cash Terms | 5 | 13 | 0 |
| `T7SOGCogs.DFM` | SOG COGS Report | 10 | 35 | 0 |
| `T7SOGComm.DFM` | SOG Commission Report | 10 | 35 | 0 |
| `T7SOHINFO.DFM` | Sales Header Misc. Infromation | 26 | 61 | 0 |
| `T7SOINFO.DFM` | Sales Misc. Infromation | 26 | 61 | 0 |
| `T7SOJINFO.DFM` | Recurring Order Information | 4 | 12 | 0 |
| `T7SOK.DFM` |  | 0 | 4 | 0 |
| `T7SOLINEHIST.DFM` |  | 0 | 1 | 0 |
| `T7SOLINFO.DFM` | Sales Line Misc. Infromation | 26 | 60 | 0 |
| `T7SOLOT.DFM` |  | 0 | 1 | 0 |
| `T7SON.DFM` | SO-N | 32 | 69 | 0 |
| `T7SONQTY.DFM` | T7SONQTY | 24 | 42 | 0 |
| `T7SOOA.DFM` | SO-OA | 39 | 81 | 0 |
| `T7SOOB.DFM` | SO-OB | 11 | 37 | 0 |
| `T7SOOD.DFM` | SO-OA | 10 | 35 | 0 |
| `T7SOOE.DFM` | SO-O-E | 47 | 107 | 0 |
| `T7SOOF.DFM` | SO-OF | 29 | 73 | 0 |
| `T7SOOG.DFM` | SO-O-G | 27 | 67 | 0 |
| `T7SOOH.DFM` | SO-Oh | 18 | 49 | 0 |
| `T7SOOI.DFM` | SO-OI | 30 | 69 | 0 |
| `T7SOOM.DFM` | SO-O-M | 20 | 47 | 0 |
| `T7SOON.DFM` | SO-O-N | 30 | 70 | 0 |
| `T7SOPB.DFM` | SO-P-B | 17 | 40 | 0 |
| `T7SOPC.DFM` | SO-PC | 30 | 72 | 0 |
| `T7SOPF.DFM` |  | 0 | 1 | 0 |
| `T7SOPI.DFM` | New Screen | 11 | 41 | 0 |
| `T7SOPJ.DFM` | New Screen | 2 | 10 | 0 |
| `T7SOPK.DFM` |  | 0 | 1 | 0 |
| `T7SOPM.DFM` | SO-P-M | 7 | 28 | 0 |
| `T7SOPO.DFM` | SO-PO | 24 | 58 | 0 |
| `T7SOPOR.DFM` | SO-PO Review | 9 | 22 | 0 |
| `T7SOPP.DFM` | SO-P-P | 8 | 29 | 0 |
| `T7SOQA.DFM` | SO-QA | 8 | 27 | 0 |
| `T7SOQB.DFM` | SO-QB | 9 | 33 | 0 |
| `T7SOQC.DFM` | SO-QC | 22 | 51 | 0 |
| `T7SOQH.DFM` | SO-QH | 99 | 145 | 0 |
| `T7SOQI.DFM` | T7SOQI | 39 | 91 | 0 |
| `T7SOQJ.DFM` | SO-QJ | 17 | 45 | 0 |
| `T7SOQK.DFM` | SO-Q-K  Print Catalog | 20 | 54 | 0 |
| `T7SOQL.DFM` | SO-Q-L | 9 | 35 | 0 |
| `T7SOR.DFM` | SO-R | 26 | 61 | 0 |
| `T7SORevu.DFM` |  | 0 | 1 | 0 |
| `T7SORevuPSWD.dfm` | Enter Contract Review ID and password | 3 | 12 | 0 |
| `T7SOS.DFM` | SO-S | 12 | 36 | 0 |
| `T7SOSER.DFM` |  | 0 | 1 | 0 |
| `T7SOV.DFM` |  | 0 | 1 | 0 |
| `t7SOA.DFM` |  | 0 | 1 | 0 |
| `t7Soa2.DFM` |  | 0 | 1 | 0 |
| `t7sondte.DFM` | t7sondte | 1 | 5 | 0 |

## Database tables (7)

Full field details are in `../../../samples/ddf/schema.md` (see per-table heading).

| Table | File on disk | Fields | Key fields (first 3) |
| ----- | ------------ | -----: | -------------------- |
| **BKSOHLOT** | `BKSOHLOT.B` | 14 | `BKAR_TXN_SONUM`, `BKAR_TXN_CODE`, `BKAR_TXN_DESC` |
| **BKSOHSER** | `BKSOHSER.B` | 14 | `BKAR_TXN_SONUM`, `BKAR_TXN_CODE`, `BKAR_TXN_DESC` |
| **BKSOLOCK** | `BKSOLOCK.B` | 5 | `BKSO_LOCK_REC`, `BKSO_LOCK_ITEM`, `BKSO_LOCK_DATE` |
| **BKSONOTE** | `BKSONOTE.B` | 5 | `BK_DESC_CODE`, `BK_DESC_NUM`, `BK_DESC_LINE` |
| **BKSOPO** | `BKSOPO.B` | 16 | `BKMRP_PO_UID`, `BKMRP_PO_VEND`, `BKMRP_PO_DATE` |
| **BKSOX** | `BKSOX.B` | 25 | `BKSOX_COMPANY`, `BKSOX_INVCNUM`, `BKSOX_INVCDATE` |
| **BKSOXH** | `BKSOXH.B` | 25 | `BKSOX_COMPANY`, `BKSOX_INVCNUM`, `BKSOX_INVCDATE` |

## BKSO\* Table Documentation (Pass 110e 2026-06-19)

**Note:** The primary SO/Invoice data lives in BKARINV (header) and BKARINVL (lines), documented in the AR module. The BKSO\* tables are supplementary.

### BKSOHLOT — SO Shipment Lot Tracking (14f)
Tracks lot assignments for SO shipments. One record per lot number assigned to a shipped SO line.

| Field | Type | Size | Meaning |
|-------|------|------|---------|
| `BKAR_TXN_SONUM` | FLOAT | 8 | SO / invoice number (PK part 1) |
| `BKAR_TXN_CODE` | STRING | 15 | Item code (PK part 2) |
| `BKAR_TXN_DESC` | STRING | 30 | Item description |
| `BKAR_TXN_QTY` | FLOAT | 8 | Quantity shipped from this lot |
| `BKAR_TXN_LOT` | STRING | 15 | Lot number |
| `BKAR_TXN_SERIAL` | STRING | 25 | Serial number (if dual lot+serial) |
| `BKAR_TXN_DATE` | DATE | 4 | Ship date |
| `BKAR_TXN_STOCK` | STRING | 15 | Stock location |
| `BKAR_TXN_LINE` | FLOAT | 8 | SO line number |
| `BKAR_TXN_LOC` | STRING | 10 | Bin/location code |
| `BKAR_TXN_TMPSO` | STRING | 40 | Temp SO reference string |
| `BKAR_TXN_SRNUM` | FLOAT | 8 | Ship receipt number |
| `BKAR_TXN_EXTRA` | STRING | 50 | Extra field |
| `BKAR_TXN_BIN` | STRING | 15 | Bin code |

### BKSOHSER — SO Shipment Serial Tracking (14f)
Identical structure to BKSOHLOT. Tracks serial number assignments for SO shipments. Uses `BKAR_TXN_SERIAL` as the serial number field.

### BKSOLOCK — SO Line Edit Lock (5f)
Prevents concurrent edits on the same SO line.

| Field | Type | Size | Meaning |
|-------|------|------|---------|
| `BKSO_LOCK_REC` | STRING | 10 | Record key (SO number or item code) |
| `BKSO_LOCK_ITEM` | STRING | 25 | Item / line being locked |
| `BKSO_LOCK_DATE` | DATE | 4 | Lock date |
| `BKSO_LOCK_TIME` | TIME | 4 | Lock time |
| `BKSO_LOCK_WHO` | STRING | 25 | User holding the lock |

### BKSONOTE — SO Note Lines (5f)
Standard EVO description-line table. Same BK_DESC_* layout used in AP/AR notes.
PK: `BK_DESC_CODE`(15) + `BK_DESC_NUM`(float) + `BK_DESC_LINE`(uint). Fields: NOTES(70), DESC(25).

### BKSOPO — MRP Planned Purchase Orders (16f)
Shared with MRP module (BKMRP prefix). MRP writes planned POs here; SO module reads them for SO-to-PO cross-reference.

| Field | Type | Size | Meaning |
|-------|------|------|---------|
| `BKMRP_PO_UID` | STRING | 20 | Unique planned order ID (PK) |
| `BKMRP_PO_VEND` | STRING | 10 | Planned vendor code |
| `BKMRP_PO_DATE` | DATE | 4 | Order date |
| `BKMRP_PO_ERD` | DATE | 4 | Expected receipt date |
| `BKMRP_PO_PART` | STRING | 15 | Part number to purchase |
| `BKMRP_PO_QTY` | FLOAT | 8 | Planned quantity |
| `BKMRP_PO_PRICE` | FLOAT | 8 | Planned unit price |
| `BKMRP_PO_WOPRE/SUF` | FLOAT+UINT | 10 | Linked WO prefix + suffix |
| `BKMRP_PO_PLANR` | STRING | 4 | Planner code |
| `BKMRP_PO_CONF` | STRING | 1 | Confirmed flag (Y = firmed PO) |
| `BKMRP_PO_DONE` | STRING | 10 | Done / received marker |
| `BKMRP_PO_MTREC` | UBINARY | 4 | Master record pointer |
| `BKMRP_PO_EXTRA` | STRING | 50 | Extra field |
| `BKMRP_PO_EST` | STRING | 10 | Estimate number reference |
| `BKMRP_PO_ESTLNE` | FLOAT | 8 | Estimate line number |

### BKSOX — SO Invoice Supplemental Record (25f)
Per-invoice summary/metadata used for cross-module reporting and multi-company scenarios.
PK: `BKSOX_COMPANY`(2) + `BKSOX_INVCNUM`(float) + `BKSOX_INVCDATE`(date).
Key fields: CUSTCODE/NAME, SUBTOT/TAXAMT/FREIGHT/DEPOSIT/RETEN/TOTAL ($ totals), CURRENCY(3), SONUM, CUSTPO(25), TERMSCODE+DESC, INVCDESC(30), SHIPDATE, SHIPPER, JOBNUM(15), TAXCODE+TAXNAME, POSTDATE, ARCHDATE, ENTDATE.

### BKSOXH — SO Invoice Supplemental History (25f)
Identical structure to BKSOX. Stores archived/closed invoice supplemental records.

## Programs (70 total) — Pass 266 (2026-06-25)

Source: `samples/rwn_symbols.json` — all T7SO* entries. Top 25 by proc count shown; 45 smaller programs follow the same naming conventions.

### Group 1 — Core order entry editors

| Program | Procs | Lib | Role / key tables |
|---------|------:|-----|-------------------|
| `T7SOA.RWN` | 606 | T7DBA.LIB | **SO-A** main order entry; BKARINV+ISTAXGRP+ISSHPVIA+ISORDECO; **BKAR.INV 1376-var** (largest namespace in system) |
| `T7SOB.RWN` | 221 | DBA.LIB | **SO-B** order acknowledgment print; MTICMSTR+BKARCUST+BKYSMSTR; BKPR.EMP 105-var |
| `T7SOB75.RWN` | 184 | DBA.LIB | **SO-B** v7.5 variant acknowledgment; same table set as T7SOB |
| `T7SOPB.RWN` | 194 | DBA.LIB | **SO-PB** print SO (alternative format); MTICMSTR+BKARCUST; BKPR.EMP 105-var |
| `T7SOOE.RWN` | 244 | DBA.LIB | **SO-OE** order entry alternate; ISBUILD+BKARINV+BKARINVL; BKAR.INV 86-var + MTWO.WIP 71-var |

### Group 2 — Shipping and packing

| Program | Procs | Lib | Role / key tables |
|---------|------:|-----|-------------------|
| `T7SOC.RWN` | 323 | DBA.LIB | **SO-C** ship / certificate of conformance; MTICMSTR+BKARCUST+BKYSMSTR+BKARINV+ISSRINFO; BKPR.EMP 107-var |
| `T7SOE.RWN` | 244 | ISTECH2.LIB | **SO-E** packing slip / serial receipt; BKARINV+BKARINVL+BKICMSTR+ISSRINFO; **BKAR.INV 344-var** |
| `T7SOPK.RWN` | 135 | LISTG60.LIB | **SO-PK** packing list; BKARINV+BKARCUST+ISSHPVIA+ISTAXGRP; **BKAR.INV 774-var** (2nd highest in system) |

### Group 3 — Invoicing

| Program | Procs | Lib | Role / key tables |
|---------|------:|-----|-------------------|
| `T7SOF.RWN` | 307 | ISTECH.LIB | **SO-F** invoice print / create; MTICMSTR+BKARCUST+BKSYMSTR+BKYSMSTR; BKPR.EMP 105-var + BKAR.INV 86-var |
| `T7SOGA.RWN` | 174 | LISTG60.LIB | **SO-GA** GL analysis report; BKARINV+BKYSMSTR+BKSYMSTR+BKARCUST; BKAR.INV 86-var + BKAR.INVL 84-var |
| `T7SOGCogs.RWN` | 140 | LISTG60.LIB | **SO-GCOGS** COGS (cost of goods sold) report; BKSYMSTR+BKARINV+BKARINVL; BKIC.PROD 63-var |
| `T7SOGComm.RWN` | 135 | LISTG60.LIB | **SO-GCOMM** sales commissions report; BKSYMSTR+BKARINV+BKARINVL; MTWO.WIP 71-var |

### Group 4 — Scheduling (SO → WO)

| Program | Procs | Lib | Role / key tables |
|---------|------:|-----|-------------------|
| `T7SON.RWN` | 361 | LISTG60.LIB | **SO-N** production scheduling from SO; WORKORD+CALENDAR+BKYSMSTR+BKARINV; **BKIC.LOC 297-var** — highest cross-module namespace for location data |

### Group 5 — Order inquiry / browse

| Program | Procs | Lib | Role / key tables |
|---------|------:|-----|-------------------|
| `T7SOD.RWN` | 218 | LISTG60.LIB | **SO-D** JIT delivery plan; ISARJDLP+BKARINV+BKARINVL+BKARCUST; BKAR.INV 86-var + MTWO.WIP 71-var |
| `T7SOOA.RWN` | 197 | LISTG60.LIB | **SO-OA** order activity browse; BKSYMSTR+BKARINV+BKARINVL+WORKORD; MTWO.WIP 71-var |
| `T7SOOI.RWN` | 188 | LISTG60.LIB | **SO-OI** order inquiry; BKSYMSTR+BKARINV+BKARINVL+BKICMSTR; BKIC.PROD 63-var |
| `T7SOPO.RWN` | 190 | LISTG60.LIB | **SO-PO** print open orders; MTICMSTR+BKYSMSTR+BKARINV+BKARINVL; MTWO.WIP 71-var |
| `T7SOOF.RWN` | 173 | LISTG60.LIB | **SO-OF** fulfillment / ship-from-loc report; BKSYMSTR+BKARINVL+BKICMSTR+BKICLOC; BKIC.PROD 63-var |
| `T7SOPC.RWN` | 157 | LISTG60.LIB | **SO-PC** print customer orders; BKYSMSTR+BKARINV+BKARINVL+ISICMSTR; BKAR.INV 86-var |
| `T7SOOG.RWN` | 150 | LISTG60.LIB | **SO-OG** order grouping/summary; BKSYMSTR+BKARINV+BKARINVL+BKICMSTR; MTWO.WIP 71-var |
| `T7SOAIMPLINES.RWN` | 156 | LISTG60.LIB | **SO-AIMPLINES** SO import / line import; BKARINV+BKARINVL+BKICREF+MTICMSTR; BKAR.INV 86-var |

### Group 6 — Quick quote / pricing

| Program | Procs | Lib | Role / key tables |
|---------|------:|-----|-------------------|
| `T7SOQH.RWN` | 200 | LISTG60.LIB | **SO-QH** quick order / header; BKICPMAT+BKARCUST+BKICMSTR+BKYSMSTR; BKIC.PROD 126-var + MTIC.PROD 54-var |
| `T7SOQI.RWN` | 167 | LISTG60.LIB | **SO-QI** quick order inquiry; BKSYMSTR+BKICMSTR+BKICPMAT+MTICMSTR; BKIC.PROD 63-var |
| `T7SOQK.RWN` | 160 | LISTG60.LIB | **SO-QK** quick kit order; BKICMSTR+MTICMSTR+BKSYMSTR+ISBUILD; BKAR.INV 86-var |

### Group 7 — Order utilities / surcharges

| Program | Procs | Lib | Role / key tables |
|---------|------:|-----|-------------------|
| `T7SOON.RWN` | 166 | LISTG60.LIB | **SO-ON** order surcharges/notes; BKSYMSTR+ISBUILD+ISARCHG+BKARINV; BKAR.INV 86-var |
| `T7SOPB` *(see Group 1)* | — | — | — |

### Notable namespace findings

| Namespace | Count | Program | Meaning |
|-----------|------:|---------|---------|
| `BKAR.INV` | 1376 | T7SOA | SO entry full invoice accessor — largest in system |
| `BKAR.INV` | 774 | T7SOPK | Packing list — 2nd highest; reads every invoice field for pack |
| `BKAR.INV` | 344 | T7SOE | Packing slip — serial receipt link |
| `BKIC.LOC` | 297 | T7SON | Scheduling from SO — full location/bin awareness |
| `ISTS.CFG` | 542 | T7SOA, T7SON | System config namespace (appears in nearly all programs) |
| `BKPR.EMP` | 107 | T7SOC | Shipping uses employee table (Certificate of Conformance signer) |

### New tables discovered in SO programs

| Table | Appears In | Inferred Role |
|-------|-----------|---------------|
| `ISORDECO` | T7SOA | Order engineering change — ECO cross-reference on open orders |
| `ISSHPVIA` | T7SOA, T7SOPK | Shipping method/carrier master (FedEx, UPS, truck, etc.) |
| `ISSRINFO` | T7SOE, T7SOC | Serial information on SO lines — serial→order linkage |
| `ISARJDLP` | T7SOD | AR JIT delivery plan — scheduled release quantities by date |
| `ISARCHG` | T7SOON | AR charge/surcharge codes (freight, handling, misc charges) |
| `ISBUILD` | T7SOOE, T7SOOI, T7SOON, T7SOQK | Kit/build assembly definition (shared with BM/WO modules) |
| `BKICPMAT` | T7SOQH, T7SOQI | Customer-specific pricing matrix (customer + part → price) |
| `BKICREF` | T7SOAIMPLINES | Item cross-reference (customer part# → internal part#) |

---

## Notes & open questions

- *(populated per-module manually as deeper reading happens.)*
