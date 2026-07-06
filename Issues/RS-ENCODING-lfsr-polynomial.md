# RS-ENCODING: LFSR polynomial reduction
**Status:** FIXED
**Date:** 2026-06-12
**Keywords:** Twofish, RS encoding, LFSR, polynomial reduction, poly 0x14D, MDS, _rs_mds_encode, twofish_pure.py, NIST test vector

## Symptom
RS MDS encoding produced incorrect results, causing key schedule failures.

## Root Cause
The initial implementation used a matrix-multiply approach for RS encoding rather than the correct LFSR polynomial reduction using poly 0x14D.

## Attempts
**Fix (worked):** `_rs_mds_encode` in `scripts/twofish_pure.py` rewritten to use the correct LFSR polynomial reduction (poly 0x14D) via `bx`/`bxx` reduction loop, replacing the earlier matrix-multiply version.

## Resolution / Lesson
Confirmed correct: NIST 192-bit test vector passes with non-zero key `0123456789ABCDEFFEDCBA987654321000112233445566778`. Use LFSR polynomial reduction (poly 0x14D) for RS encoding, not matrix multiplication.
