# Handheld (HH) — Mobile Shop Floor Module

Status: partial (program inventory confirmed from rwn_symbols.json; internal logic blocked by RWN encryption).

- **Module code**: `HH` (also accessed via DC module setup)
- **Programs**: 32 T7HH* programs
- **Primary tables**: BKDCLAB, BKICLOC, ISBINLOC, WORKORD, WOBOM, BKARINV, BKAPPO
- **Library**: ISTECH.LIB, ISTECH2.LIB, EVO.LIB, DBA.LIB

HH provides wireless handheld / barcode-scanner access to the same operations available at desktop workstations. Each T7HH* program is the handheld equivalent of a desktop program (T7WO*, T7SO*, T7IN*, T7PO*). HH programs share all database tables with their desktop counterparts — no HH-specific tables exist.

## Programs (32 total) — Pass 269 (2026-06-25)

Source: `samples/rwn_symbols.json` — all T7HH* entries.

### Group 1 — Sales Order / Shipping

| Program | Procs | Lib | Role / key tables |
|---------|------:|-----|-------------------|
| `t7hhssoe.RWN` | 267 | ISTECH2.LIB | **HH-SO Ship Entry** — handheld SO shipment; ISSOBOX+BKARINV+BKARINVL+MTICMSTR+ISSOREVU; **BKIC.LOC 297-var** |
| `T7HHNREL.RWN` | 129 | LISTG60.LIB | **HH-N Release** — item/shipment release; BKARINVL+BKARINV+BKARCUST+BKICMSTR; BKAR.INV 86-var |
| `T7HHN.RWN` | 117 | EVO.LIB | **HH-N** handheld item receipt/release base; MTICMSTR+BKARINVL+BKARINV+BKARCUST; BKAR.INV 86-var |
| `T7HHSSOEVerify.RWN` | 44 | — | HH ship entry verify/confirm; BKARINVL+BKARINV+ISSOBOX; BKAR.INV 86-var |
| `T7HHSOLookup.RWN` | 39 | — | HH SO header lookup; BKARINV |
| `T7HHSODD.RWN` | 80 | — | HH SO drop-ship delivery; BKARINV+BKARCUST+ISSHPVIA+BKARINVL+BKSBMFG |
| `t7hhsoser.RWN` | 56 | — | HH SO serial capture at ship; BKARINVL+BKARTXN+SERIAL |
| `t7hhsobin.RWN` | 55 | — | HH SO bin-confirmed shipment; BKARINVL+BKICLOC+ISBINLOC; ISARTXNB |
| `t7hhsolot.RWN` | 51 | — | HH SO lot-confirmed shipment; BKARINVL+LOT+BKARTXN |
| `T7HHH.RWN` | 65 | — | HH header / shipping (ISSOBOX+ISSHIPCO); ISSOBOX |

### Group 2 — Work Order / Production

| Program | Procs | Lib | Role / key tables |
|---------|------:|-----|-------------------|
| `t7hhwoi.RWN` | 212 | ISTECH.LIB | **HH-WO Issue** — material issue to WO; BKSHORT+WORKORD+BKICLOC+ISBINLOC; BKPR.EMP 105-var |
| `T7HHWOG.RWN` | 201 | EVO.LIB | **HH-WO Good** — WO operation completion; BKSHORT+WOMAT+WORKORD+BKICMSTR; MTWO.WIP 71-var |
| `T7HHWOSCRAP.RWN` | 151 | LISTG60.LIB | **HH-WO Scrap** — scrap reporting; BKSHORT+WOBOM+BKICMSTR+WOMAT; MTWO.WIP 71-var |
| `T7HHWOLabel.RWN` | 150 | DBA.LIB | **HH-WO Label** — WO label print; WORKORD+BKICMSTR+MTICMSTR+WORECV; MTWO.WIP 71-var |
| `T7HHWOP.RWN` | 135 | ISTECH.LIB | **HH-WO Pick** — WO material pick; WORKORD+BKICMSTR+ISBINLOC+WOBOM; MTWO.WIP 71-var |
| `T7HHWOSER.RWN` | 88 | — | HH WO serial capture; MTICMSTR+SERIAL+BKICMSTR+ISSERCNT+SCRAP |
| `T7HHWOLOT.RWN` | 80 | — | HH WO lot at issue; BKICLOC+ISBINLOC+MTICMSTR+LOT+ISBINLOT |
| `t7hhwolookup.RWN` | 39 | — | HH WO header lookup; WORKORD |
| `T7HHWOSCRAP.RWN` | 151 | LISTG60.LIB | HH WO scrap reporting (see above) |

### Group 3 — PO Receipt

| Program | Procs | Lib | Role / key tables |
|---------|------:|-----|-------------------|
| `t7hhpoc.RWN` | 262 | ISTECH.LIB | **HH-PO Receipt** — PO receive; BKSBMFG+BKAPPO+MTICMSTR+ISDIGSIG+BKAPPOL; BKAR.INV 86-var + MTWO.WIP 71-var |
| `T7HHPOCBIN.RWN` | 202 | ISTECH.LIB | **HH-PO Receipt Bin** — PO receive to bin location; BKAPPO+BKYSMSTR+MTICMSTR+BKAPPOL; BKAR.INV 86-var |
| `t7hhinga.RWN` | 150 | DBA.LIB | **HH-IN Good Arrival** — IN goods receipt; BKAPPO+BKYSMSTR+BKAPPOL+BKICMSTR; BKAP.PO 57-var |
| `T7HHINbins.RWN` | 48 | — | HH IN receipt to bin; ISBINLOC+MTICMSTR+BKICMSTR |
| `T7HHPOCLS.RWN` | 5 | — | HH PO receipt stub; BKAPPO+MTICMSTR+BKAPPOL |

### Group 4 — DC Labor (Handheld scan-in)

| Program | Procs | Lib | Role / key tables |
|---------|------:|-----|-------------------|
| `T7HHDCA.RWN` | 167 | ISTECH.LIB | **HH-DC-A** handheld labor scan; BKDCLAB+BKDCSHFT+BKYSMSTR+BKPRMSTR+WORKORD; BKPR.EMP 105-var |
| `T7HHDCA1.RWN` | 82 | — | HH-DC-A variant 1; BKDCSHFT+BKYSMSTR+BKPRMSTR+BKDCLAB+WORKORD |
| `t7hhdcb.RWN` | 5 | — | HH-DC-B stub; BKDCLAB+BKDCSHFT+BKPRMSTR+WORKORD |
| `t7hhdcc.RWN` | 5 | — | HH-DC-C stub; BKDCLAB+BKDCSHFT+BKPRMSTR+WORKORD |

### Group 5 — Location / Bin Management

| Program | Procs | Lib | Role / key tables |
|---------|------:|-----|-------------------|
| `T7HHINLJ.RWN` | 114 | — | HH IN location journal; BKICLOCM+BKYSMSTR+BKICMSTR+SERIAL; BKIC.LOC 297-var |
| `T7HHO.RWN` | 79 | EVO.LIB | HH order bin / location display; BKICMSTR+ISBNMSTR+ISBINLOC+BKICLOC |

### Group 6 — Physical Inventory

| Program | Procs | Lib | Role / key tables |
|---------|------:|-----|-------------------|
| `T7HHPIC.RWN` | 105 | — | **HH-PI Count** — physical inventory scan; BKYSMSTR+BKPIMSTR+BKPRMSTR+BKICMSTR+SERIAL |

## Key design patterns

| Namespace | Typical count | Meaning |
|-----------|:------------:|---------|
| `ISTS.CFG` | 495–542 | System configuration — universal in all HH programs |
| `BKIC.LOC` | 297 | IC location fields — HH is the primary location-access path |
| `BKPR.EMP` | 105 | Employee master — all labor/production scans need full employee record |
| `BKAR.INV` | 86 | AR invoice header — shipment/delivery HH programs read full SO header |
| `MTWO.WIP` | 71 | WIP fields — WO-related HH programs access full WIP namespace |

## New tables confirmed in HH programs

| Table | Appears In | Role |
|-------|-----------|------|
| `ISSOBOX` | t7hhssoe, T7HHH | SO shipping box/container assignments (box number + contents) |
| `ISSOREVU` | t7hhssoe | SO review / verification queue before ship confirm |
| `ISBINLOC` | t7hhwoi, T7HHPOCBIN | Bin location master — physical bin addresses in warehouse |
| `ISBINLOT` | T7HHWOLOT | Bin + lot cross-reference (lot-tracked material per bin) |
| `ISARTXNB` | t7hhsobin | AR transaction + bin (ship-from bin reference on AR transaction) |
| `ISSERCNT` | T7HHWOSER | Serial count — WO serial number assignment tracking |
| `SCRAP` | T7HHWOSER | Scrap table — WO scrap transactions |
| `WORECV` | T7HHWOLabel | WO receive — finished goods receipt from WO |
| `WOMAT` | T7HHWOG, T7HHWOSCRAP | WO material — WO component issue transactions |
| `ISSHPVIA` | T7HHSODD | Ship via master (carrier codes + configuration) |
| `BKPIMSTR` | T7HHPIC | Physical inventory master — PI count records |
| `BKSBMFG` | t7hhpoc | SB manufacturer / approved vendor manufacturer code |

## Relationship to DC module

The HH module extends the DC (Data Collection) module concept to wireless scanners:
- **Desktop DC**: T7DCA / T7DCPSF / T7DCG — workstation-mounted terminals
- **Handheld DC**: T7HHDCA / T7HHDCA1 — wireless handheld scanners
- Both write to BKDCLAB (same table, same schema)
- Non-labor HH functions (WO/PO/SO) have no desktop T7DC* equivalent — they bypass the DC labor flow entirely and write directly to their respective module tables
