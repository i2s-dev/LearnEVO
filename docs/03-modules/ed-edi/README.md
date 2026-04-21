# EDI (ED)

Status: verified (auto-generated from the extracted schema, menu-code dump, and DFM inventory).

- **Module code**: `ED`
- **Tables**: 6 (prefixes `BKED`)
- **UI forms**: 3 (prefixes `T7ED`, `T6ED`)
- **Menu operations**: 6

## Menu operations

| Code | Operation | Legacy module file(s) |
| ---- | --------- | --------------------- |
| `ED-B` | Import EDI Orders | BKEDB;ISEDIB;ISEDIX;NBEDIB;t6edib |
| `ED-C` | Edit EDI Orders | BKEDC |
| `ED-D` | Convert EDI Orders to Sales Orders | BKEDD;ISEDID;t6edid |
| `ED-E` | Export EDI Orders | T6EDIE;t6ediex |
| `ED-G` | Master EDI Set-up | BKEDG |
| `ED-H` | Error report | ISEDIH |

## UI forms (3)

| DFM file | Caption | fields | controls | tabs |
| -------- | ------- | -----: | -------: | ---: |
| `T7EDII.DFM` | ED-I-I | 10 | 37 | 0 |
| `t7ediftp.DFM` | EDI  FTP Program | 7 | 9 | 0 |
| `t7edudf.DFM` | New Screen | 2 | 2 | 0 |

## Database tables (6)

Full field details are in `../../../samples/ddf/schema.md` (see per-table heading).

| Table | File on disk | Fields | Key fields (first 3) |
| ----- | ------------ | -----: | -------------------- |
| **BKEDIDUN** | `BKEDIDUN.B` | 7 | `BKEDI_DUN_CUST`, `BKEDI_DUN_DUNS`, `BKEDI_DUN_EDI` |
| **BKEDIH** | `BKEDIH.B` | 84 | `BKAR_INV_NUM`, `BKAR_INV_SONUM`, `BKAR_INV_INVCD` |
| **BKEDIL** | `BKEDIL.B` | 28 | `BKAR_INVL_INVNM`, `BKAR_INVL_CNTR`, `BKAR_INVL_ESD` |
| **BKEDMSTR** | `BKEDMSTR.B` | 3 | `BKEDI_MST_NEXTN`, `BKEDI_MST_DUNS`, `BKEDI_MST_PATH` |
| **BKEDNOTE** | `BKEDNOTE.B` | 3 | `BKEDI_NOTE_EDI`, `BKEDI_NOTE_SO`, `BKEDI_NOTE_NOTE` |
| **BKEDPOST** | `BKEDPOST.B` | 2 | `BKEDI_POST_INVN`, `BKEDI_POST_CUST` |

## Notes & open questions

- *(populated per-module manually as deeper reading happens.)*
