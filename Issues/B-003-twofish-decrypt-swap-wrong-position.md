# B-003: Twofish decrypt test fails (swap in wrong position)
**Status:** FIXED
**Date:** 2026-06-12
**Keywords:** Twofish, decrypt, Feistel, swap, post-loop, pre-loop, twofish_pure.py, NIST test vector

## Symptom
`tf.decrypt(ct) == pt` assertion failed even after encrypt test was passing.

## Root Cause
The "undo last swap" was placed BEFORE the 16-round loop in `decrypt()`, but it must be placed AFTER. Reasoning:

- The encrypt writes ciphertext as `[c16, d16, a16, b16]` (after a final swap before output whitening). After undoing the output whitening, X = `[c16, d16, a16, b16]`.
- This matches the reference's `GET_INPUT` layout (A=c16, B=d16), so T0 and T1 for the first decrypt round (r=15) must be computed from X[0]=c16 and X[1]=d16 — no pre-loop swap needed.
- After all 16 decrypt rounds + in-loop swaps, the state is `[c0, d0, a0, b0]`.
- A single post-loop swap gives `[a0, b0, c0, d0]` = whitened plaintext, which undoes correctly with K[0..3].
- The old code pre-swapped to `[a16, b16, c16, d16]` before the loop, making every round compute T from wrong words.

## Attempts

| Date | Attempt | Outcome |
|------|---------|---------|
| 2026-06-12 | Pre-loop swap (wrong position) | FAILED — T0/T1 computed from wrong words |
| 2026-06-12 | Moved swap to post-loop | PASSES — `assert tf.decrypt(ct) == pt` |

## Resolution / Lesson
In a Feistel with explicit swap-at-end-of-round, the decrypt must start from the raw undo-whitened state and mirror the encrypt's swap structure — including where the final "undo the last swap" lives (after the loop, not before it).
