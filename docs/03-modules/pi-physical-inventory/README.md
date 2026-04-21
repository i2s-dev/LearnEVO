# Physical Inventory (PI)

Status: verified (auto-generated from the extracted schema, menu-code dump, and DFM inventory).

- **Module code**: `PI`
- **Tables**: 7 (prefixes `BKPI`)
- **UI forms**: 10 (prefixes `T7PI`, `T6PI`)
- **Menu operations**: 9

## Menu operations

| Code | Operation | Legacy module file(s) |
| ---- | --------- | --------------------- |
| `PI-A` | Frozen Inventory Report | BKPIA;BKPIB |
| `PI-B` | Frozen Inventory Report | BKPIB |
| `PI-C` | Enter Tag Counts | BKPIC |
| `PI-C-A` | Physical Inventory Exception Report | BKPICA;T6PICA |
| `PI-D` | Missing Tags Report | BKPID |
| `PI-E` | Edit Frozen Inventory Costs | BKPIE |
| `PI-F` | Physical Inventory Report | BKPIF;T6PIF |
| `PI-G` | Update Actual Inventory | BKPIF;BKPIG;T6PIF |
| `PI-H` | Purge Physical Inventory | BKPIF;BKPIH;T6PIF |

## UI forms (10)

| DFM file | Caption | fields | controls | tabs |
| -------- | ------- | -----: | -------: | ---: |
| `T7PIA.DFM` | PI-A Capture Frozen Inventory | 31 | 65 | 0 |
| `T7PIB.DFM` | PI-B Frozen Inventory Report | 10 | 34 | 0 |
| `T7PIC.DFM` |  | 0 | 1 | 0 |
| `T7PICA.DFM` | PI-C-A  Physical Inventory Exception Report | 6 | 26 | 0 |
| `T7PID.DFM` | PI-D  Missing Tags Report | 4 | 28 | 0 |
| `T7PIE.DFM` |  | 0 | 1 | 0 |
| `T7PIF.DFM` | PI-F Phisical Inventory Report | 13 | 44 | 0 |
| `T7PIG.DFM` | PI-G Update Actual Inventory | 11 | 40 | 0 |
| `T7PIH.DFM` | PI-H Purge Physical Inventory | 3 | 21 | 0 |
| `T7PILOC.DFM` |  | 0 | 3 | 0 |

## Database tables (7)

Full field details are in `../../../samples/ddf/schema.md` (see per-table heading).

| Table | File on disk | Fields | Key fields (first 3) |
| ----- | ------------ | -----: | -------------------- |
| **BKPIFROZ** | `BKPIFROZ.B` | 19 | `BKPH_INFO_UOH`, `BKPH_INFO_YEAR`, `BKPH_INFO_QTR` |
| **BKPILCNT** | `BKPILCNT.B` | 10 | `BKPI_LOT_YEAR`, `BKPI_LOT_QTR`, `BKPI_LOT_CODE` |
| **BKPILOT** | `BKPILOT.B` | 10 | `BKPI_LOT_YEAR`, `BKPI_LOT_QTR`, `BKPI_LOT_CODE` |
| **BKPIMSTR** | `BKPIMSTR.B` | 3 | `BKPI_MSTR_YEAR`, `BKPI_MSTR_QTR`, `BKPI_MSTR_DESC` |
| **BKPIPHYS** | `BKPIPHYS.B` | 14 | `BKPH_TAGNUM`, `BKPH_ACTQTY`, `BKPH_EMPNUM` |
| **BKPISCNT** | `BKPISCNT.B` | 10 | `BKPI_SER_YEAR`, `BKPI_SER_QTR`, `BKPI_SER_CODE` |
| **BKPISER** | `BKPISER.B` | 10 | `BKPI_SER_YEAR`, `BKPI_SER_QTR`, `BKPI_SER_CODE` |

## Notes & open questions

- *(populated per-module manually as deeper reading happens.)*
