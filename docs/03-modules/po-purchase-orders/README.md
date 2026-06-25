# Purchase Orders (PO)

Status: verified (auto-generated from the extracted schema, menu-code dump, and DFM inventory).

- **Module code**: `PO`
- **Tables**: 8 (prefixes `BKPO`, `BKAPPO`, `BKAPAPO`, `BKAPHPO`)
- **UI forms**: 41 (prefixes `T7PO`, `T6PO`, `BKPO`)
- **Menu operations**: 29

## Narrative / vendor help

**→ [help-content.md](help-content.md)** — consolidated write-up of
all 27 help topics from `EvoHELP.CHM` (overview + PO-A through PO-T,
26 programs). Includes the life-cycle programs, RFQ system (PO-E /
PO-F / PO-G), vendor-data programs (PO-H / PO-L / PO-P), the eight
PO-I-\* reports, the three-step QC inspection flow (PO-J-A / B / C),
and the inquiry / date-maintenance / receiving-slip / e-sign
utilities. Cross-links to WO, JC, AP, IN, MR modules and to the
related System Overview sections.

## Menu operations

| Code | Operation | Legacy module file(s) |
| ---- | --------- | --------------------- |
| `PO-A` | Enable UPC Numbers | BKPOA;BKPOA1;ISTECH;T6POA |
| `PO-B` | Print Purchase Orders | BKPOB;T6POB |
| `PO-C` | P/O Lot Control | BKPOC;BKPOCLOT;BKPOCSER;ISPOC;ISTECH |
| `PO-D` | View PO Receivers | BKPOA;BKPOA1;T6POA |
| `PO-E` | Copy RFQs | BKPOA;BKPOA1;T6POA |
| `PO-E-A` | Request for Quote (Universal) | BKPOEA;T6POEA |
| `PO-F` | Enter Verbal RFQs | BKPOF |
| `PO-G` | Convert RFQs | BKPOG |
| `PO-H` | Enter Vendor Prices | BKPOH;t6poh |
| `PO-I-A` | Print Open Purchase Orders Listing | BKPOENG;T6POENG |
| `PO-I-B` | Print Closed Purchase Orders Listing | BKPOENG;T6POENG |
| `PO-I-C` | Print RFQ Status | BKPOIC |
| `PO-I-D` | Print Vendor Prices | BKPOID |
| `PO-I-E` | Print Receiving Report | BKPOENG;JCPOIE2;PCONRPT;T6POENG |
| `PO-I-F` | Print Received not Invoiced | BKPOENG;T6POENG |
| `PO-I-G` | Print Purchase Order Items by Due Date | BKPOIG |
| `PO-I-H` | Vendor Performance | t6poih |
| `PO-I-I` | Print Purchase Order Changes | ISPOII |
| `PO-I-J` | Print Vendor Purchase History | J6POIJ |
| `PO-J-A` | Print Receipt Travelers | BKPOJA;T6POJA |
| `PO-J-B` | Print Inventory in QC | BKPOJB |
| `PO-J-C` | Enter Inspection Buyoffs | AUTOPOJC;BKPOJC |
| `PO-J-D` | Close PO's | BKPOJD |
| `PO-K` | Close Purchase Orders | BKPOK |
| `PO-M` | Purchase Order Inquiry | BKPOM |
| `PO-P` | View Vendors | BKPOP |
| `PO-Q` | Maintain PO Delivery Dates | BKPOQ |
| `PO-R` | Print Receiving Slip | T6POB |
| `PO-T` | Print PO Stock Item Packing List | T6POB |

## UI forms (41)

| DFM file | Caption | fields | controls | tabs |
| -------- | ------- | -----: | -------: | ---: |
| `T7POA.DFM` |  | 0 | 1 | 0 |
| `T7POA2.DFM` |  | 0 | 1 | 0 |
| `T7POAC.DFM` | T7POA | 54 | 146 | 0 |
| `T7POACPY.DFM` | New Screen | 3 | 13 | 0 |
| `T7POAE.DFM` |  | 0 | 1 | 0 |
| `T7POAIMPLINES.DFM` | POA Import | 21 | 55 | 0 |
| `T7POAPrBrk.DFM` |  | 1 | 1 | 0 |
| `T7POAVITEM.DFM` |  | 0 | 1 | 0 |
| `T7POB.DFM` | PO-B | 21 | 56 | 0 |
| `T7POEA.DFM` |  PO-E-A | 6 | 26 | 0 |
| `T7POENG.DFM` | PO-ENG | 100 | 228 | 2 |
| `T7POF.DFM` | PO-F | 39 | 98 | 2 |
| `T7POG.DFM` | PO-G | 12 | 35 | 0 |
| `T7POH.DFM` | PO-H | 37 | 111 | 0 |
| `T7POIC.DFM` | PO-I-C | 16 | 55 | 0 |
| `T7POID.DFM` | PO-I-D | 9 | 36 | 0 |
| `T7POIG.DFM` | PO-I-G | 22 | 68 | 0 |
| `T7POIH.DFM` | PO-I-H | 19 | 52 | 0 |
| `T7POII.DFM` | PO-I-I | 12 | 40 | 0 |
| `T7POIL.DFM` | PO-B | 10 | 38 | 0 |
| `T7POJA.DFM` | PO-J-A  Print Receipt Travellers | 15 | 44 | 0 |
| `T7POJB.DFM` | PO-J-B | 26 | 80 | 0 |
| `T7POJC.DFM` | PO-J-C | 33 | 98 | 0 |
| `T7POJD.DFM` | PO-J-D | 10 | 37 | 0 |
| `T7POK.DFM` | PO-K | 9 | 37 | 0 |
| `T7POL.DFM` |  | 0 | 1 | 0 |
| `T7POLA.DFM` | PO-L-A | 9 | 41 | 1 |
| `T7POLINEHIST.DFM` |  | 0 | 1 | 0 |
| `T7POLP.DFM` | PO-L-P | 5 | 27 | 0 |
| `T7POM.DFM` |  | 0 | 1 | 0 |
| `T7POMAST.DFM` | New Screen | 34 | 92 | 0 |
| `T7POP.DFM` |  | 0 | 1 | 0 |
| `T7POPGET.DFM` | POP Caption | 10 | 21 | 0 |
| `T7POS.DFM` |  | 0 | 1 | 0 |
| `T7POSCD.DFM` | Cash Due | 3 | 10 | 0 |
| `T7POSI.DFM` |  | 0 | 1 | 0 |
| `T7POSX.DFM` |  | 0 | 1 | 0 |
| `T7pojcqc.DFM` | Multi Scrap Codes | 4 | 13 | 0 |
| `T7pojcsc.DFM` | Multi Scrap Codes | 4 | 13 | 0 |
| `t7POQ.DFM` |  | 0 | 1 | 0 |
| `t7poc.DFM` |  | 0 | 1 | 0 |

## Database tables (8)

Full field details are in `../../../samples/ddf/schema.md` (see per-table heading).

| Table | File on disk | Fields | Key fields (first 3) |
| ----- | ------------ | -----: | -------------------- |
| **BKAPAPO** | `BKAPAPO.B` | 58 | `BKAP_PO_NUM`, `AHSY_USER_ACCES_5`, `BKAP_PO_PRTD` |
| **BKAPAPOL** | `BKAPAPOL.B` | 38 | `BKAP_POL_PONM`, `BKAP_POL_CNTR`, `BKAP_POL_ERD` |
| **BKAPHPO** | `BKAPHPO.B` | 57 | `BKAP_PO_NUM`, `BKAP_PO_PRTD`, `BKAP_PO_VNDCOD` |
| **BKAPHPOL** | `BKAPHPOL.B` | 38 | `BKAP_POL_PONM`, `BKAP_POL_CNTR`, `BKAP_POL_ERD` |
| **BKAPPO** | `BKAPPO.B` | 57 | `BKAP_PO_NUM`, `BKAP_PO_PRTD`, `BKAP_PO_VNDCOD` |
| **BKAPPOL** | `BKAPPOL.B` | 38 | `BKAP_POL_PONM`, `BKAP_POL_CNTR`, `BKAP_POL_ERD` |
| **BKPOX** | `BKPOX.B` | 19 | `BKPOX_COMPANY`, `BKPOX_INVCNUM`, `BKPOX_INVCDATE` |
| **BKPOXH** | `BKPOXH.B` | 19 | `BKPOX_COMPANY`, `BKPOX_INVCNUM`, `BKPOX_INVCDATE` |

## Programs (38 total) — Pass 267 (2026-06-25)

Source: `samples/rwn_symbols.json` — all T7PO* entries.

### Group 1 — Core PO entry

| Program | Procs | Lib | Role / key tables |
|---------|------:|-----|-------------------|
| `T7POA.RWN` | 499 | LISTG60.LIB | **PO-A** main PO entry editor; BKAPPO+BKAPVEND+BKAPPOL+MTICMSTR; **BKAP.PO 798-var** (2nd largest namespace in system, after T7SOA) + **BKAP.POL 190-var** |

### Group 2 — Receiving

| Program | Procs | Lib | Role / key tables |
|---------|------:|-----|-------------------|
| `t7poc.RWN` | 377 | LISTG60.LIB | **PO-C** PO receipt (standard); BKAPPOL+BKAPPO+BKAPDESC+MTICMSTR+BKYSMSTR; BKPR.EMP 105-var + BKAR.INV 86-var |
| `T7POIL.RWN` | 110 | LISTG60.LIB | **PO-IL** receiving labor / employee sign-off; BKAPPO+BKPRMSTR+TASCOLOR; BKPR.EMP 103-var |

### Group 3 — QC receiving

| Program | Procs | Lib | Role / key tables |
|---------|------:|-----|-------------------|
| `T7POJC.RWN` | 323 | DBA.LIB | **PO-JC** QC inspection receipt (primary); BKQCMSTR+BKQCTRAN+BKAPPOL+BKAPPO+MTICMSTR; BKPR.EMP 105-var |
| `T7POJA.RWN` | 176 | DBA.LIB | **PO-JA** QC receive alternate form; BKQCMSTR+BKAPPOL+BKICMSTR; BKPR.EMP 105-var + MTWO.WIP 71-var |
| `T7POJB.RWN` | 143 | LISTG60.LIB | **PO-JB** QC browse / inquiry; BKQCMSTR+BKAPPO+BKAPPOL; BKPR.EMP 103-var |
| `T7POIH.RWN` | 103 | LISTG60.LIB | **PO-IH** QC history view; BKQCMSTR+BKAPPOL+BKAPVEND+BKQCTRAN; BKAP.PO 57-var |
| `T7POJD.RWN` | 99 | LISTG60.LIB | **PO-JD** QC detail report; BKQCTRAN+BKAPVEND+BKQCMSTR |

### Group 4 — PO print

| Program | Procs | Lib | Role / key tables |
|---------|------:|-----|-------------------|
| `T7POB.RWN` | 190 | DBA.LIB | **PO-B** print PO (with digital signature support); MTICMSTR+BKAPVEND+BKYSMSTR; BKPR.EMP 105-var |
| `T7POLP.RWN` | 90 | LISTG60.LIB | **PO-LP** PO labels / prep; BKSBVEND+TASCOLOR |
| `T7POL.RWN` | 83 | LISTG60.LIB | **PO-L** PO item labels; BKSBVEND+BKAPVEND+BKICMSTR+ISICMSTR; MTIC.PROD 54-var |
| `T7POLX.RWN` | 60 | LISTG60.LIB | **PO-LX** extended labels; BKSBVEND+BKAPVEND+BKICMSTR |

### Group 5 — PO inquiry / browse

| Program | Procs | Lib | Role / key tables |
|---------|------:|-----|-------------------|
| `T7POM.RWN` | 174 | LISTG60.LIB | **PO-M** PO management / MRP buy; BKAPVEND+BKICMSTR+MTICMSTR+ISNOTES; **BKIC.LOC 264-var** (high location awareness for ordered parts) |
| `T7POIG.RWN` | 171 | LISTG60.LIB | **PO-IG** item/group inquiry; ISNTYPE+ISBUILD+BKAPVEND; BKAR.INV 86-var + MTWO.WIP 71-var |
| `T7POID.RWN` | 127 | DBA.LIB | **PO-ID** PO inquiry detail; BKRFQ+MTICMSTR+BKICMSTR; BKIC.PROD 63-var + MTIC.PROD 54-var |
| `T7POK.RWN` | 141 | LISTG60.LIB | **PO-K** PO type / status browser; MTICMSTR+BKSYMSTR+BKAPPO+BKAPPOL; BKAP.PO 57-var |
| `T7POII.RWN` | 124 | LISTG60.LIB | **PO-II** PO item inquiry; ISAPCHG+MTICMSTR+BKAPPO+BKAPVEND; BKAP.PO 57-var |
| `T7POH.RWN` | 122 | LISTG60.LIB | **PO-H** PO history / vendor price breaks; BKRFQ+BKAPDESC+BKICMSTR+BKAPVEND; BKAP.PO 57-var |
| `T7POQ.RWN` | 106 | LISTG60.LIB | **PO-Q** PO quantity / backlog; BKAPPO+BKAPPOL+BKICLOC; BKAP.PO 57-var |
| `T7POG.RWN` | 124 | LISTG60.LIB | **PO-G** PO grouping / summary; BKRFQ+BKAPPO+BKAPPOL; MTWO.WIP 71-var |

### Group 6 — Special flows

| Program | Procs | Lib | Role / key tables |
|---------|------:|-----|-------------------|
| `T7POENG.RWN` | 274 | LISTG60.LIB | **PO-ENG** engineering / kit PO entry; ISBUILD+BKAPPOL+BKAPPO+MTICMSTR; MTWO.WIP 71-var |
| `T7POEA.RWN` | 184 | ISTECH.LIB | **PO-EA** EDI / AP electronic PO; BKYSMSTR+BKAPPO+BKAPPOL+BKICMSTR+BKAPDESC; BKPR.EMP 105-var |
| `T7POS.RWN` | 104 | LISTG60.LIB | **PO-S** PO→SO direct shipment conversion; BKARCUST+ISTERMS+ISQSOA+BKARINV+BKARINVL; BKAR.INV 86-var — drop-ship PO creates SO invoice |
| `T7POAIMPLINES.RWN` | 132 | LISTG60.LIB | **PO-AIMPLINES** PO line import; BKAPPO+BKICMSTR+BKAPPOL+BKICLOC; BKAP.PO 57-var |

### Group 7 — RFQ / Estimating bridge

| Program | Procs | Lib | Role / key tables |
|---------|------:|-----|-------------------|
| `T7POF.RWN` | 85 | LISTG60.LIB | **PO-F** forecast / RFQ; BKRFQ+BKARINVL+ISESTDTL+BKESTCFG; MTWO.WIP 71-var — RFQ bridges PO and Estimating modules |

### Group 8 — CRM / utilities

| Program | Procs | Lib | Role / key tables |
|---------|------:|-----|-------------------|
| `T7POP.RWN` | 53 | EVO.LIB | **PO-P** CRM vendor integration; BKAPVND2+BKCMVNDF+BKCMVNFC+BKCMVNDH — links PO vendor to CRM contact records |
| `T7POSI.RWN` | 53 | EVO.LIB | **PO-SI** CRM/system index; BKCMACCC |
| `T7POLA.RWN` | 47 | EVO.LIB | **PO-LA** PO label auto-print |
| `t7poo.RWN` | 17 | NZLICE.LIB | NZL license stub — no business logic |

### Notable namespace findings

| Namespace | Count | Program | Meaning |
|-----------|------:|---------|---------|
| `BKAP.PO` | 798 | T7POA | PO header field accessor — 2nd largest namespace in system |
| `BKAP.POL` | 190 | T7POA | PO line field accessor — confirms T7POA accesses every PO line field |
| `BKIC.LOC` | 264 | T7POM | Location awareness for MRP buy recommendations |
| `BKPR.EMP` | 105 | t7poc, T7POB, T7POJC | Receiving and printing require employee record (signer) |
| `BKAR.INV` | 86 | t7poc, T7POJC, T7POS | PO receiving and drop-ship flow bridge to AR invoice |
| `MTWO.WIP` | 71 | T7POIG, T7POJA, T7POF | WIP-aware PO processing (outside-process, kit assembly) |

### New tables discovered in PO programs

| Table | Appears In | Inferred Role |
|-------|-----------|---------------|
| `BKRFQ` | T7POID, T7POG, T7POH, T7POF, T7POIC | Request for Quote header (bridges Estimating→PO) |
| `ISNTYPE` | T7POIG, T7WOLB | Note type codes — categories for notes attached to records |
| `ISQSOA` | T7POS | Quick SO address — destination address for drop-ship POs |
| `ISTERMS` | T7POS (+ T7AR*, T7AP*) | Payment terms master (discount days, net days, terms description) |
| `ISAPCHG` | T7POII | AP change tracking — records changes to PO/invoice data |
| `BKSBVEND` | T7POLP, T7POL, T7POLX | Sub-vendor / distributor master (supply chain tier 2) |
| `BKCMVNDF` / `BKCMVNFC` / `BKCMVNDH` | T7POP | CRM vendor files — link PO vendor to CRM contact/call records |

---

## Notes & open questions

- *(populated per-module manually as deeper reading happens.)*
