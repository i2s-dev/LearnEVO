# KEY-SCHEDULE: Subkey generation from M_e/M_o
**Status:** FIXED
**Date:** 2026-06-12
**Keywords:** Twofish, key schedule, subkeys, M_e, M_o, S_rev, g-function, MDS S-box, rho, _h, twofish_pure.py, NIST test vector

## Symptom
Subkey generation produced incorrect subkeys, causing encrypt/decrypt failures.

## Root Cause
Subkeys were being generated from `S_rev` instead of from `M_e`/`M_o` (raw key byte groups). `S_rev` is used only for the g-function (MDS S-box lookup), not for subkey generation.

## Attempts
**Fix (worked):** Corrected the subkey-generation loop to use `_h(2*i*rho, M_e, k)` and `_h((2*i+1)*rho, M_o, k)`, matching the reference Twofish spec. `S_rev` retained for use in the g-function only.

## Resolution / Lesson
Confirmed correct: NIST test vector confirms correct output. `S_rev` is for g-function (MDS S-box lookup) only. Subkey generation always uses M_e/M_o (raw key byte groups extracted directly from the key material).
