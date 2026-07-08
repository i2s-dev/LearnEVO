---
name: B-020-frida-false-positive-slots
description: Frida 05c value-match produced false-positive slot assignments for GLCTRL (YN[88]) and WHCTRL (YN[105]); company-differential scans disprove both; APLANG (YN[201]) unverified
metadata:
  type: feedback
---

# B-020 — Frida 05c False-Positive YN Slot Mappings

**Status:** ✅ RESOLVED — false positives identified and removed from KNOWN_SLOTS

**Date:** 2026-07-08

---

## Symptom

Pass 575c (Frida Test 05c) reported three 1:1 YN slot mappings via unique-byte-value matching:

| Slot | Key | Value (05c) |
|------|-----|-------------|
| YN[88] | GLCTRL | 'P' (0x50) |
| YN[105] | WHCTRL | 'Q' (0x51) |
| YN[201] | APLANG | 'E' (0x45) |

These were entered into `KNOWN_SLOTS` in `05d-analyze.py` and added to the count of confirmed slots (88→91).

---

## Root Cause

The 05c matching method ("find the ONE YN slot whose value equals this ISTS.CFG value") only
confirms that no OTHER slot happens to have the same byte at this company. It does NOT confirm
that the ISTS.CFG key actually reads from that slot — only that their values coincide.

When company A and company F were scanned with Test 05d:
- GLCTRL: Company A = 'P' (0x50), Company F = ' ' (0x20) — but YN[88] was 'P' in BOTH scans
- WHCTRL: Company A = 'Q' (0x51), Company F = ' ' (0x20) — but YN[105] was 'Q' in BOTH scans

This is definitive disproof. GLCTRL and WHCTRL change between companies; YN[88] and YN[105]
do not. The 05c matches were coincidental — the value just happened to be unique at company A.

APLANG: Both companies show APLANG='E' (0x45) and YN[201]='E'. No disproof possible from this
data (same value both companies). The mapping remains unverified — could be correct or coincidence.

---

## Additional finding: BKYSMSTR is system-wide

Both company A and company F returned byte-for-byte identical YN arrays (500 hex chars identical).
This confirms the Pass 575f finding (company B99 scan): BKYSMSTR.YN[] is a global system record,
not per-company. The 66 ISTS.CFG keys that differ between companies are stored in a separate
per-company table (likely BKCOMSTR), not BKYSMSTR.YN[].

---

## Attempt log

1. **Pass 575c**: Added GLCTRL/WHCTRL/APLANG to KNOWN_SLOTS based on 05c unique-value match. ← FALSE
2. **Pass 575f**: B99 (company F) differential scan — BKYSMSTR identical between companies.
   Did not check whether GLCTRL/WHCTRL themselves disprove their slot assignments.
3. **Pass 575g (this pass)**: Company A vs company F 05d scans compared key-by-key.
   GLCTRL changed P→' '; WHCTRL changed Q→' '; YN[88] and YN[105] unchanged (both 'P' and 'Q').
   Disproof confirmed. KNOWN_SLOTS corrected; 05d-analyze.py updated.

---

## Resolution

- `KNOWN_SLOTS` in `Frida Tests/tests/05d-analyze.py`:
  - YN[88] GLCTRL — **REMOVED** (disproven)
  - YN[105] WHCTRL — **REMOVED** (disproven)
  - YN[201] APLANG — **retained but marked UNVERIFIED** (same value both companies)
- Confidence rating: YN slot mapping C:88 → C:82
- Effective confirmed count: 101 → ~88 (88 DFM-structural remain valid)

---

## Lesson

**The 05c unique-value method is necessary but not sufficient for slot assignment.**
A match at one company means "this is consistent" not "this is confirmed." The only way to confirm
a 1:1 mapping from live data is via differential (value changes between companies AND the same
byte changes in the matching YN slot). Since BKYSMSTR is system-wide and does NOT vary by
company, the differential approach is permanently closed. The 88 DFM-structural bindings
(direct FieldName='BKYS.YN[N]' in T7MDefNDC.DFM / T7MDEFAULTS.DFM) remain the only
confirmed slot assignments. Never count 05c-style value-matches as confirmed without differential proof.
