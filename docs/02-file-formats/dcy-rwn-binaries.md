# `.DCY` and `.RWN` — Compiled / Proprietary Binaries

Status: **cipher confirmed; passphrase confirmed; IV is the last blocker.**
See [`decryption-findings.md`](decryption-findings.md) for the full research log.

Last updated: 2026-06-12

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

## Confirmed cipher details (2026-06-12)

- **Cipher:** Twofish, 128-bit block, **192-bit key**, **CFB mode**
- **Passphrase:** `mabufoju` — hardcoded in `tp7runtime.exe` at file offset `0x75D154`
- **Key:** `SHA1('mabufoju')[0:20]` + `\x00\x00\x00\x00` = 24 bytes
- **Key is fixed** — not per-file, not per-license, not per-user. Same key for every `.RWN` and `.DCY` on this installation.
- **Validation:** first 8 bytes of each `.RWN`; decrypted plaintext must have pt[0:4] == pt[4:8]
- **File count:** 1,124 `.RWN` at share root + 3 in `DFM\`; 1,273 `.RUN` (unencrypted)

## Remaining unknown

The only unknown is the **initial IV** (`block_buf` at cipher+0x3C) — uninitialized heap
memory in the Delphi allocator. A debugger session reading `[EAX+0x3C]` at the first
`EncryptBlock` call (`tp7runtime.exe` file offset `0x34DF50`) resolves this completely.

## Things still open

- Full decryption (blocked on IV — see above)
- `.DCY` internal structure after decryption (hypothesis: Delphi VCL form text for forms,
  compiled schema for data dictionary files)
- Does the runtime mmap files or read whole into memory?
