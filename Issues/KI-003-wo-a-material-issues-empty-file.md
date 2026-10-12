# KI-003 — WO-A Material Issues button shows "Empty File" (all WOs, since ~10/11/26)

Status: ACTIVE — cause isolated to 10/11 program update; report to ISTS pending
Docs: [wo-a-material-issues.md](../docs/03-modules/wo-work-orders/wo-a-material-issues.md) ·
[lookup-drill-engine.md](../docs/01-architecture/lookup-drill-engine.md) ·
[2026-10-11-ists-update.md](../docs/01-architecture/2026-10-11-ists-update.md)
Date: 2026-10-12   Module: WO-A (T7WOA.RWN) / lookup engine (WBKLOOKUP.RWN)   Company: I2

## Symptom
WO-A, enter WO 55968-1 -> header shows "* New / Being Created on 10/12/26", blank Part #, Status F,
Start = today. Clicking Material Issues (button `Mat`, handler MAT.CLICK) -> dialog "Information: Empty File".

## Verified facts (2026-10-12)
- "Empty File" text exists only in WBKLOOKUP.RWN (3 lookup routines) — shown when the lookup returns no records.
- 55968-1 EXISTS in I2\WORKORD.BI2 (raw decode): status **C**, part 222042 "4' SHELF LIGHT", qty 3000/3000,
  act start 10/08/26, act finish 10/09/26, AMAT $38,095.48, 3 key hits (data + index entries), record not corrupt.
- WOMAT.BI2 has 106 rows for 55968-1 (9/22–10/9/26, one part, net 25,800 issued).
- Lookup def (Drill\ISDRILLM.B, WORKORDERS -> WOMATL "Materials"): WOMAT filtered by
  WOMAT.WOPRE/WOSUF = **MTWO.WIP.WOPRE/WOSUF of the WO record loaded in WO-A**. Unchanged by update.
  => "Empty File" is a consequence of WO-A not having loaded the WO record ("* New").
- ISTS update deployed **2026-10-11**: T7WOA.RWN (10:23, "ISTS Enhancement 09/16/26"), WBKLOOKUP.RWN (10:23,
  "ISTS Enhancement 05/05/26", new program-filter system ISDRILL LOOKUP.PFILTER/PWHILE), Drill\ISDRILLM.B and
  Drill\BKLUGRID.DBF/.dbt/.mdx (16:42). Old copies: Drill\BKLUGRID.xBF/.xbt (2025-05-31), root ISDRILLM.B (2026-05-30).
- Other WOs for comparison: 56273-22 (F, 2 WOMAT rows), 56268-8 (F, 1), 55553-1 (R, 23).
  Other closed-10/09 WOs: 55686-1, 55977-1, 56039-1, 56179-1, 56304-1.

## Side findings
- I2 ODBC DDF (X$Field) for WORKORD and ISNUMBER includes 1-byte null indicators per field that the TAS
  records don't have -> ODBC returns garbage for these tables. WOMAT DDF is fine. Decoder: offset - (field_index+1).

## Update 2026-10-12 (user tests + deeper analysis)
User tests in WO-A: 56273-22 (F) loads OK -> Material Issues = Empty File; 55553-1 (R) loads OK -> Empty File;
55977-1 (C) shows "* New" -> Empty File. User TYPED 55968-1 (normal 2-year habit), not New(+).
=> Lookup broken for ALL WOs, not a WO-record problem. (Closed WOs opening as "* New" = separate question.)

- Material Issues does NOT look up WOMAT directly. I2\ISDRILL.BI2 scratch record written by WO-A (ID T7WOA073325A20261012):
  GRID=WOBOMMI  FILE=WOBOM  KEY=0  COMM="WOBOMMI Work Order Materials 2"
  WHILE=`WOBOM.WOPRE = VAL( 55977 ) .A. WOBOM.WOSUF = INT(VAL( 1 ))`  PFILTER/PWHILE blank.
  WOMAT is a drill-down from WOBOMMI (ISDRILLM WOBOMMI->WOMATL).
- WOBOM.BI2 (743 MB, mtime 10/11 11:37) HAS BOM lines for all test WOs (raw scan, corrected offsets).
- WOBOM indexes (X$Index): k0 OPER+WOPRE+WOSUF, k1 WOPRE+WOSUF+ASSY+LINE+COMP, k2 WOPRE, k3 WOPRE+WOSUF ...
  — same as documented earlier (primary-keys.md), so file structure unchanged.
- BKLUGRID WOBOMMI grid record + memo (columns, keys "WOBOM.KEY"/"WOBOM.KEY5") IDENTICAL new vs 2025-05-31 backup (.xBF/.xbt).
- ISDRILL record layout: new T7WOA and new WBKLOOKUP agree (PFILTER@3416, PWHILE@3436, 20B each);
  I2\ISDRILL.BI2 reclen 3456 (widened); 22\ and root/Drill ISDRILL.B still 3416 (unused).
- Drill-style calls store KEY=0 + key no. in COMM (same for working-looking BINS calls), so KEY=0 alone is not proof.
- No pre-update copies on server (UPDATE\ empty, Bak Up\ has none). Local: samples/crypto/rwn/T7WOA.RWN (2025-03-28 build);
  old WBKLOOKUP only as decrypted .dec (samples/rwn_decrypted, June 2026).

Conclusion so far: data + lookup config unchanged and valid; failure introduced by the 10/11 program update
(T7WOA.RWN 09/16/26 build and/or WBKLOOKUP.RWN 05/05/26 build). Exact faulty logic needs RWN bytecode decompile.
USER RULE: do NOT roll back anything without asking.

## Evidence split — what may be cited to ISTS (user rule 2026-10-12)

Anything learned from decrypted/decompiled code must NOT be used to report the issue.

**Reportable (observed in EVO, customer data, file metadata):**
- WO-A → Material Issues shows "Information – Empty File" for 56273-22 (F), 55553-1 (R), 55977-1 (C), 55968-1 (C).
- 56273-22 and 55553-1 load normally (part, dates) yet still show "Empty File".
- Closed WOs 55968-1 / 55977-1 open as "* New – Being Created" instead of loading.
- WO-A title bar: "ISTS Enhancement 09/16/26".
- Via Zen ODBC / own data files: WOMAT has 2 / 23 / 106 rows for 56273-22 / 55553-1 / 55968-1; WOBOM has BOM lines
  for all of them; WORKORD has 55968-1 status C, finished 10/09/26.
- File dates: T7WOA.RWN + WBKLOOKUP.RWN 10/11/26 10:23; Drill\ISDRILLM.B + Drill\BKLUGRID.* 10/11/26 16:42;
  server moved to i2s-evo 10/09/26. Worked for ~2 years before (user experience; pin down last-known-good date).
- Side issue: ODBC DDF for WORKORD/WOBOM/ISNUMBER is misaligned (1-byte null indicators) — readable via Zen tools.

**Grey (readable unencrypted vendor config/scratch files — reveals internals; user decides):**
- ISDRILL scratch record: lookup WOBOMMI "Work Order Materials" on WOBOM, WHILE `WOBOM.WOPRE = VAL(55977) .A. ...`.
- WOBOMMI grid definition identical to the 2025-05-31 backup (Drill\BKLUGRID.xBF).

**Internal only (decrypted code — never cite):**
- "Empty File" originates in WBKLOOKUP.RWN; MAT.CLICK handler; PFILTER/PWHILE fields; WBKLOOKUP build "05/05/26";
  ISDRILL field offsets; closed-WO strings in T7WOA.

**Draft report text:**
> Since on or about 10/11/26, WO-A → Material Issues shows "Empty File" for every work order we try (e.g. 56273-22,
> 55553-1), including open WOs that load normally and have material issued (confirmed via ODBC: WOMAT and WOBOM contain
> records for these WOs). Closed WOs (e.g. 55968-1) now open as "* New". This worked until recently. Our server moved
> to i2s-evo on 10/09, and T7WOA.RWN / WBKLOOKUP.RWN show modified dates of 10/11. Can you advise?

## Open questions / next step
- ~~Did user type 55968-1 or use New (+)?~~ Typed (answered 2026-10-12).
- ~~Do F/R WOs show materials?~~ No — Empty File for all (answered 2026-10-12).
- Scope: do other drill buttons (IN-A Bins, other WO-A drills) also return Empty File?
- Last date Material Issues is known to have worked (before 10/09 migration or before 10/11 update?).
- Closed WOs opening as "* New": intended in 09/16/26 build or a second bug?
- Awaiting ISTS response.

## Attempts
1. 2026-10-12 — Theory "WOMAT empty for this WO" — WRONG (106 rows exist).
2. 2026-10-12 — Theory "WO header missing" — WRONG (record exists, status C).
3. 2026-10-12 — Theory "lookup config / data file changed" — WRONG (grid, memo, indexes unchanged; WOBOM has data).
