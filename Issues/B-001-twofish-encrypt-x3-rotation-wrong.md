# B-001: Twofish encrypt test fails: X[3] rotation direction wrong
**Status:** FIXED
**Date:** 2026-06-12
**Keywords:** Twofish, encrypt, Feistel, rotation, ROL, ROR, X[2], X[3], F0, F1, ENCRYPT_RND, twofish_pure.py, NIST test vector

## Symptom
`tf.encrypt(pt)` produced `6ccef8a75c0dc95da0303c045c999c5b` instead of `9f589f5cf6122c32b6bfec2f2ae8c35a`.

## Root Cause
Two rotation errors in the encrypt Feistel round:
1. `X[2]` was written as `_rol32(X[2] ^ F0, 31)` — should be `_ror32(X[2] ^ F0, 1)`.
2. `X[3]` was `_ror32(X[3], 1) ^ F1` — should be `_rol32(X[3], 1) ^ F1`.

Reference macro `ENCRYPT_RND`:
```c
C ^= T0+T1+xkey->K[8+2*(r)]; C = ROR32(C,1);
D = ROL32(D,1); D ^= T0+2*T1+xkey->K[8+2*(r)+1]
```

Note: C is XOR-then-ROR; D is ROL-then-XOR. Order matters.

## Attempts

| Date | Attempt | Outcome |
|------|---------|---------|
| 2026-06-12 | ROR(31) on X[2], ROR on X[3] | FAILED |
| 2026-06-12 | ROR(1) on X[2], ROL(1) on X[3] (then XOR F1) | PASSES |

## Resolution / Lesson
Read the reference macro carefully. C is XOR-then-ROR; D is ROL-then-XOR. Order matters. ROR(31) is NOT the same as ROR(1) — they rotate in the same direction but by different amounts.
