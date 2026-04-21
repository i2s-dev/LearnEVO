# `.DCY` and `.RWN` — Compiled / Proprietary Binaries

Status: open-questions. Both formats appear to be **encrypted or
compressed with no recognizable magic number**.

## `.DCY` — Data Dictionary

Observed samples (in `../../samples/dcy/`):

| File                | Size      |
| ------------------- | --------- |
| `EVOERPMENU.DCY`    | 1,466,302 |
| `EVODC.DCY`         | 745,884   |
| `EVOUSERS.DCY`      | 27,027    |
| `ISABOUT.DCY`       | 136,471   |
| `WBKLOOKUP.DCY`     | 23,708    |
| `suwin6.dcy` (local)| 32,876    |

Hex dumps show no recognizable header. First 16 bytes of `EVOUSERS.DCY`:
`88 EB B4 87 0C 37 E1 8E 60 11 1C 1F C1 E2 33 3D` — high entropy,
non-printable, different each file. Not PKZIP (`PK\x03\x04`), not
Btrieve, not LZH, not standard Delphi form binary.

Consistent with: TAS Pro 7's own compression+obfuscation wrapper. The
runtime knows how to load them at boot.

## `.RWN` — Compiled TAS Pro 7 Program

Similar profile: the first bytes of `EvoERPmenu.RWN` are
`AA 37 A9 0F 6F 00 A3 31 85 52 47 89 2A FC 0F 01` — again high-entropy
with no obvious header.

Pairing: the runtime appears to load a `.RWN` alongside its companion
`.DCY`. Evidence: `EVOERPMENU.DCY` exists beside `EvoERPmenu.RWN`, and
`DBAMENU_FLEX.DCY` beside `DBAMENU_FLEX.RUN`. The `.DCY` likely holds
the **data/schema dictionary** the program uses; the `.RWN` holds the
**executable byte code**.

## Why I think they're encrypted, not just compressed

- Two files with the same nominal content but different names/sizes
  show **completely different byte distributions** from offset 0 onward
  — a pure compression format would still have a consistent header
  (LZ/Deflate/LZMA/etc.).
- No readable strings at any offset in the first 4 KB of either file,
  even though the programs clearly reference column names and messages
  (strings should appear as literals somewhere).
- TAS Pro historically ships with a license-bound decoder in the runtime
  — this matches behavior where files can only be opened by the
  authorized `tp7runtime.exe`.

## Plan to make progress (without modifying anything)

1. Inspect `tp7runtime.exe` / `evoerp.exe` strings for magic numbers and
   mention of ".DCY" / ".RWN" loader functions. Read-only.
2. Look for a pairing: some modules have **both** `.RWN` and
   `.SRC`/`.DFM`. Comparing compiled vs. source byte patterns may reveal
   a fixed header or XOR key if the encryption is simple.
3. Check available TAS Pro documentation (online reference, Computer
   Keyes legacy docs) — external research task.
4. Check whether a paired **old** `.RUN` exists that might be a simpler
   (pre-encryption) format.
5. See if `EvoPVT.jar` contains Java-side parsers for either format —
   unzipping a JAR is safe, and it might literally ship a decoder.

## Things still open

- Is `.DCY` the same format as TAS Pro 6's old `.DCT`? Or a new one?
- Are the per-file keys derived from the file name? From the license?
  From the user seat (`WHOAMI.DBA`)?
- Does the runtime mmap the files (constant random access) or read them
  whole into memory once?
