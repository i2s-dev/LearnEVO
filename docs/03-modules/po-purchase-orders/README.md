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

## Notes & open questions

- *(populated per-module manually as deeper reading happens.)*
