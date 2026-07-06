# B-002: h() q-box ordering wrong for b[1] and b[3] in 128-bit key case
**Status:** FIXED
**Date:** 2026-06-12
**Keywords:** Twofish, h(), q-box, q0, q1, MDS, H12, H32, b[1], b[3], 128-bit key, twofish_pure.py, NIST test vector

## Symptom
After fixing the X[3] rotation (B-001), encrypt still produced `de60f86ea019d72f8cc3de9e21f503fb` instead of `9f589f5cf6122c32b6bfec2f2ae8c35a`.

## Root Cause
The q-box sequence for bytes b[1] and b[3] in `_h()` for the k=2 (128-bit) base case was wrong:
- b[1]: had `q0[q1[q1[...]]]` but reference H12 macro says `q0[q0[q1[...]]]`
- b[3]: had `q0[q0[q1[...]]]` but reference H32 macro says `q0[q1[q1[...]]]`

Reference H macros (from twofish-0.3.0/twofish.c):
```c
#define H12( y, L )  MDS_table[1][q0[q1[y]^L[ 9]]^L[1]]
#define H32( y, L )  MDS_table[3][q1[q1[y]^L[11]]^L[3]]
```
MDS_table[1] internally applies q0; MDS_table[3] internally applies q1.

So b[1] inner-to-outer: q1 → q0 (XOR L1) → q0 (XOR L0) → MDS col1
   b[3] inner-to-outer: q1 → q1 (XOR L3) → q1 (XOR L2) → MDS col3 (but that last q1 is inside MDS_table[3])

The correction swapped b[1] and b[3] inner q-box ordering.

## Attempts

| Date | Attempt | Outcome |
|------|---------|---------|
| 2026-06-12 | Wrong q-box order in b[1] and b[3] | FAILED — wrong ciphertext |
| 2026-06-12 | Fixed to match H12/H32 reference macros | PASSES |

## Resolution / Lesson
Always cross-reference the H0x/H1x/H2x/H3x macros from the reference C source rather than guessing the q-box ordering. The inner/outer distinction is subtle.
