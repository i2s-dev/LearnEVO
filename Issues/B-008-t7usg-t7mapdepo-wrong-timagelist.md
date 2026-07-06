# B-008: T7USG.DFM and T7MAPDEPO.DFM incorrectly described as TImageList
**Status:** FIXED (Pass 82, 2026-06-18)
**Date:** 2026-06-18
**Keywords:** T7USG.DFM, T7MAPDEPO.DFM, TImageList, DFM, TEditForm1, ISTRIGRS, BKARDEP, ISARDEPL, samples/dfm

## Symptom
Prior session summary stated "T7USG.DFM is TImageList (no form content)" and "T7MAPDEPO.DFM is TImageList (no form content)". Both were flagged as unusable for analysis.

## Root Cause
These DFMs were NOT analyzed during the prior session — the claim was carried forward from an even earlier session or was a speculation, not a result of actually reading the files. The files existed on the network share and were never copied to samples/dfm/ until Pass 82.

## Attempts
**Fix (Pass 82, 2026-06-18):** Copied both DFMs to samples/dfm/ and ran analysis. Both are TEditForm1 with full content:
- T7USG.DFM: 36 captions, 37 field bindings — complete trigger entry form confirming all 25 ISTRIGRS fields
- T7MAPDEPO.DFM: 26 captions, 20 field bindings — complete deposit application form with BKARDEP + ISARDEPL bindings

## Resolution / Lesson
Never mark a DFM as "TImageList / no content" without actually reading the file. Always copy to samples/dfm/ and run the caption/field extraction script before concluding a DFM has no useful content.
