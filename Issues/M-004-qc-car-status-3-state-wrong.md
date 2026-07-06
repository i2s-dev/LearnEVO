# M-004: QC CAR status documented as 3-state; DFM confirms 4-state
**Status:** FIXED
**Date:** 2026-07-01 (Pass 492)
**Keywords:** QC, CAR, status codes, DFM, Items.Strings, T7QCGA, modules.py

## Symptom
modules.py (QC section, CAR workflow) stated CAR status = "3-state: Open / Review / Closed."

## Root Cause
Initial documentation inferred the states from ISCTREVU DFM captions (Pass 471) without reading T7QCGA Items.Strings directly.

## Attempts
**Fix (worked):** Pass 492 DFM scan of T7QCGA.DFM Items.Strings returned:
`['Open', 'Review', 'Failed', 'Closed']` — 4 states.
modules.py corrected: CAR status is 4-state (Open / Review / Failed / Closed).
Also corrected QC-G-D table row and scorecard.

## Resolution / Lesson
Always read Items.Strings from the primary entry form DFM to confirm status codes; don't infer from ancillary forms.
