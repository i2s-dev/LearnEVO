# Estimating (ES)

Status: verified (auto-generated from the extracted schema, menu-code dump, and DFM inventory).

- **Module code**: `ES`
- **Tables**: 4 (prefixes `BKES`, `ESTSUM`)
- **UI forms**: 7 (prefixes `T7ES`, `T6ES`)
- **Menu operations**: 8

## Menu operations

| Code | Operation | Legacy module file(s) |
| ---- | --------- | --------------------- |
| `ES-A` | Copy RFQs | BKESA;BKPOA;BKPOA1;BKPOF;T6POA |
| `ES-B` | Print Estimates | BKESB |
| `ES-C` | Enter Quote Templates | BKESC |
| `ES-E` | Convert Estimates | BKESE |
| `ES-F` | Copy Estimates | BKESF |
| `ES-G` | Print Estimate Listing | BKESG |
| `ES-H` | Enter Material Costs | BKESH |
| `ES-I` | Print Material Costs | BKESI |

## UI forms (7)

| DFM file | Caption | fields | controls | tabs |
| -------- | ------- | -----: | -------: | ---: |
| `T7ESB.DFM` | ES-B | 16 | 42 | 0 |
| `T7ESC.DFM` | ES-C | 19 | 42 | 0 |
| `T7ESD.DFM` | ES-D  Print Customer Quotes | 14 | 43 | 0 |
| `T7ESE.DFM` |  | 0 | 1 | 0 |
| `T7ESH.DFM` | ES-H Enter Material Costs | 19 | 55 | 0 |
| `T7ESI.DFM` | New Screen | 5 | 24 | 0 |
| `T7EST.DFM` |  | 0 | 1 | 0 |

## Database tables (4)

Full field details are in `../../../samples/ddf/schema.md` (see per-table heading).

| Table | File on disk | Fields | Key fields (first 3) |
| ----- | ------------ | -----: | -------------------- |
| **BKESTCFG** | `BKESTCFG.B` | 13 | `BKEST_CFG_NUM`, `BKEST_CFG_STAT`, `BKEST_CFG_CLASS` |
| **BKESTQT** | `BKESTQT.B` | 84 | `BKAR_INV_NUM`, `BKAR_INV_SONUM`, `BKAR_INV_INVCD` |
| **BKESTQTL** | `BKESTQTL.B` | 28 | `BKAR_INVL_INVNM`, `BKAR_INVL_CNTR`, `BKAR_INVL_ESD` |
| **ESTSUM** | `ESTSUM.B` | 213 | `MTESUM_QUOTE`, `MTESUM_DATE`, `MTESUM_EXPDATE` |

## Notes & open questions

- *(populated per-module manually as deeper reading happens.)*
