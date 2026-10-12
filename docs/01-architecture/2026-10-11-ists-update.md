# 2026-10-11 ISTS update — what changed

Status: partial — only the files touched during the KI-003 investigation are listed; full changed-file scan pending.

Context: EVO moved to `i2s-evo` (192.168.0.237) on 2026-10-09; the old server `i2s109-solidcrm` is retired
(**do not use**). On Sunday 2026-10-11 program and drill files on `\\i2s-evo\EVOERP\` were replaced. These dates are
from file listings [DATA] and can be cited.

## Timeline (file modification times, Eastern)

| When | What |
|------|------|
| 10/09 | Server swap to i2s-evo |
| 10/10 17:03 | `Testdata\ISDRILL.B99` modified (already 3456-byte records) |
| 10/11 09:43–09:47 | `Bak Up\` subfolders and `UPDATE\` folder touched (`UPDATE\` is empty now) |
| 10/11 10:23 | `T7WOA.RWN` (1,031,261 B) and `WBKLOOKUP.RWN` (718,359 B) replaced |
| 10/11 10:27–11:06 | Per-company WORKORD/WOMAT for AB, AT, CA, Default modified |
| 10/11 11:37 | `I2\WOBOM.BI2` modified (743 MB) |
| 10/11 11:58–12:01 | `ISDRILL.B*` in AB, AT, CA, Default modified (3456-byte records) |
| 10/11 16:42 | `Drill\ISDRILLM.B`, `Drill\BKLUGRID.DBF/.dbt/.mdx` replaced |
| 10/12 morning | Users report WO-A Material Issues → "Empty File" ([KI-003](../../Issues/KI-003-wo-a-material-issues-empty-file.md)) |

## Version strings

| Program | Version | Source |
|---------|---------|--------|
| T7WOA.RWN | ISTS Enhancement 09/16/26 | WO-A title bar [OBS] |
| WBKLOOKUP.RWN | ISTS Enhancement 05/05/26 (was 05/30/24) | decrypted strings [DEC] |

## Notable content changes [DEC — internal only]

- **WBKLOOKUP**: +226 / −38 strings. New program-filter system (`ISDRILL LOOKUP.PFILTER`, `LOOKUP.PWHILE`,
  "This is a Program Filter and cannot be removed."), grid-filter debug logging, `EvoGridSettings.ini`, EVO Service
  settings, PDF preview, many new ISTS.CFG flags (ITAR, SO/PO signatures, WOIEMP/WOIEST…), ISEXUSER user extension.
- **T7WOA**: +336 strings. Quality holds ("Full Stop", "Production Hold", "Shipping Hold", "First Article",
  "Routing Review Required"), self-update check ("Newer Files Copied, Please restart WO-A", pre-copy hash values),
  generic buttons btnGen1–4, rework WO checkbox, Evo personal user settings, EVO Service logging.
- ISDRILL layout: both new programs agree (PFILTER @3416, PWHILE @3436, 20 B each).

## Backups available

- None on the server for the previous WBKLOOKUP/T7WOA (`UPDATE\` empty, `Bak Up\` has none).
- `Drill\BKLUGRID.xBF/.xbt/.xdx` (2025-05-31) = previous grid definitions.
- Root `ISDRILLM.B` (2026-05-30) = an older drill master.
- Local research copies: `samples/crypto/rwn/T7WOA.RWN` (2025-03-28 build); old WBKLOOKUP only as decrypted
  `samples/rwn_decrypted/WBKLOOKUP.RWN.dec` (June 2026).
- **User rule: never roll back anything without asking.**

## Local copies made 2026-10-12

`samples/t7woa-20261011/` (T7WOA + WBKLOOKUP .RWN/.DFM + `dec/`), `samples/drill-20261012/` (ISDRILLM, BKLUGRID
new + old, every company's ISDRILL), `samples/i2-20261012/` (WORKORD.BI2, WOBOM.BI2, ISDRILL.BI2 — .BI2 git-ignored).
