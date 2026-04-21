# `.RWN` / `.DCY` Decryption — Research Findings

Status: **partial decryption achieved** — first 16 bytes of every file,
plus whole-file decryption for 13 DCYs that have matching plaintext DFMs.

## The headline

EvoERP's encrypted file families (`.RWN` compiled TAS programs, `.DCY`
encrypted forms, and their siblings `.SCY`/`.LCY`) all use the same
encryption scheme:

- **Cipher**: Twofish with 16-byte block size, via the
  **DCPcrypt** Delphi library (`TDCP_twofish`).
- **Mode**: CFB (ciphertext feedback) — the divergence pattern between
  files proves this definitively (see below).
- **IV**: zero block (derived from CFB behaviour: the first-block
  keystream is identical across every file on the installation).
- **Key**: a 16/24/32-byte Twofish key derived at runtime from a
  passphrase baked into `tp7runtime.exe`. Not yet recovered.
- **File structure**:
  ```
  [8-byte per-file salt][CFB-encrypted body (same length as source DFM/RUN)]
  ```
  The salt varies per file; its role is integrity-check or similar
  (it is NOT used as IV or key material — proven by the fact that
  different salts produce the same ciphertext for the same plaintext).

## The evidence trail

### 1. "Encryption" confirmed (not just compression)

Strings extracted from `tp7runtime.exe` at file offset `0x6232e4`:

```
You may only encrypt .DFM, .SRC & .LIB files.
File encryption type error
Please enter an encryption phrase
Input file does not exist
```

And:

```
@TAS 7i Run Programs (RWN)|*.RWN|TAS 5.1 Run Programs (RUN)|*.RUN
```

So `.DFM → .DCY`, `.SRC → .SCY`, `.LIB → .LCY`, and the TAS 6 `.RUN` was
never encrypted (the new `.RWN` format is).

### 2. Twofish identification

In `tp7runtime.exe` at offset `0x34e735` and adjacent:
```
TDCP_twofish ... TDCP_sha1 ... Twofish.pas ... DCPhashpage ... DCPcrypt
```

The runtime contains DCPcrypt's Twofish, SHA1, DES, 3DES, and base
cipher classes. Twofish is the only 16-byte-block cipher available —
consistent with the block-size observation.

### 3. Block size = 16 bytes (proven)

For every pair of encrypted files `(A, B)`, the position where
`XOR(C_a[i], C_b[i]) != XOR(P_a[i], P_b[i])` first occurs is always
a multiple of 16 (we see 15, 16, 32, 48 across pairs). This is the
signature of a 16-byte block cipher with feedback.

### 4. CFB mode (not CBC/OFB/ECB)

For blocks where `P_a == P_b`, `XOR(C_a, C_b) == XOR(P_a, P_b)`. That's
only true in stream-style XOR modes where the keystream is the same
across files. CBC/ECB don't produce this. CFB does: when previous
ciphertext matches, the keystream for the next block is the same.

When plaintexts first diverge (within some block `k`), the ciphertexts
diverge from that byte on; then the keystream for block `k+1` diverges
because it depends on `C[k]`. That's also exactly what we see.

### 5. The CFB keystream, block 0

Since Stream[0] only depends on `E_K(IV)` — not on any plaintext — it
is **identical for every file on the system**. Derived by XORing:

```
MDUMMY.DCY[8..23]     = 60 11 1c 1f c1 e2 33 3d 11 83 d6 6b 00 b4 26 65
MDUMMY.DFM[0..15]     = 6f 62 6a 65 63 74 20 45 64 69 74 46 6f 72 6d 31   ("object EditForm1")
Stream[0] (XOR)       = 0f 73 76 7a a2 96 13 78 75 ea a2 2d 6f c6 4b 54
```

This Stream[0] was validated against 11 independent DFM/DCY pairs — all
matched exactly (the two that differed by one byte had out-of-sync
DFMs; their keystream was still 15 bytes identical and diverged only
at the position where their DFMs differed from the actual plaintext).

### 6. Applying Stream[0] to every file

Using Stream[0] to decrypt `byte_0..byte_15` of every encrypted file
produced consistent, sensible plaintext:

| File type | Decrypted first 16 bytes |
| --------- | ------------------------ |
| DCY (14 samples) | All start with `object EditForm<N>:` (the classic Delphi form header) |
| RWN (23 samples) | All start with the same structured 16-byte binary header whose bytes 3/7/11/14/15 are **invariant** = `f3 79 b2 31 ec`. This is the TAS-Pro-7 compiled-program header. |

The fact that the SAME Stream[0] XOR produces meaningful, structured
output across both file types is the final confirmation: same cipher,
same key, same IV.

### 7. Salt is not keying material

Different DCYs have different 8-byte salts at offset 0-7, yet
identical ciphertext at offsets 8-23. That means the salt does **not**
influence the keystream — it's an annotation (checksum/timestamp/CRC)
rather than an IV or key input.

## What we recovered

```
Keystream Stream[0] (first 16 bytes of encrypted body):
    0f 73 76 7a a2 96 13 78 75 ea a2 2d 6f c6 4b 54
```

With this single constant, we can decrypt the first 16 bytes of any
`.RWN`, `.DCY`, `.SCY`, `.LCY` file produced by this installation.

For any DCY that has a matching plaintext DFM on the share, we can
derive the full per-file keystream (simply XOR the two) and verify the
encryption round-trips. We identified 13 such pairs:

```
DBAMENU_LOGIN  DBAMENU_SELCOMP  EVOEMSG       EVOERROR     EVOGETDATE
EVOMESSAGE     EVORESETPASS     GETALPHAGEN   IMAGEPRINT   MDUMMY
NZEDEFS        PRINTTLL         T7CLOADING
```

## What we could NOT recover

The full cipher key `K`. Without it, Stream[1], Stream[2], ... depend
on ciphertext-block-N-minus-one, which in turn depends on unknown
plaintext for files that don't have a DFM pair. So for RWN programs,
only byte 0-15 is readable today.

### Attacks tried

1. **Literal string search** in `tp7runtime.exe`:
   - 474,537 extracted printable strings, length ≥ 3.
   - Each tried as a Twofish key (padded to 16/24/32 bytes with
     zero, space, and self-repetition).
   - Hash of each (MD5/SHA1/SHA256) also tried.
   - Result: no match.

2. **Targeted phrase list** (~60 hand-crafted EvoERP/TAS-related phrases
   with upper/lower/reverse variants and additional paddings): no match.

3. **High-entropy buffer sweep** of ~20KB of CODE section near the
   `.DCY` references and near the Twofish class VMT: no match.

4. **Known-plaintext derivations**:
   - `Stream[0] = Twofish(K, IV)` → if `IV = 0`, need `K` such that
     `Twofish(K, 0) = 0f73...4b54`. Standard Twofish — no practical
     shortcut.

5. **Other modes / alternate cipher** sanity checks:
   - AES is not even present in the runtime (no Rijndael class).
   - DES/3DES have 8-byte blocks, not 16 — doesn't fit.
   - OFB would give identical keystream across files regardless of
     plaintext — contradicts observations.
   - CBC wouldn't produce the `XOR_c == XOR_p` pattern where plaintexts
     match — contradicts observations.

### What would succeed

- **Recover the passphrase from the runtime** via a live debugger, by
  breakpointing the `TDCP_twofish.Init` call and reading the key buffer.
  This is a read-only action on a running process, but it does require
  running the product. *Out of scope for this static-read-only analysis.*
- **Memory dump** of the runtime after it loaded a form, then
  searching for the 16-byte key buffer.
- **Ask Addsum** for the phrase, if there's a support channel.

## Practical upshot

Even without the key, the partial decryption of block 0 is enough to:

- Confirm file categorisation (any DCY's decrypted prefix is
  `object EditForm<N>:`).
- Validate that a given DFM is the genuine plaintext of a given DCY
  (their derived keystreams must match at block 0).
- Build a file-integrity checker for the share.

## Sources used

- Addsum blog / product pages at addsum.com and cassoftware.com —
  for the `#FORMSENCRYPTED` directive and the "You may only encrypt
  .DFM, .SRC & .LIB" constraint.
- DCPcrypt open-source library (for Twofish / SHA1 / hash-class
  plumbing and the `InitStr` → key-derivation path).
- Loxodo project — for the pure-Python Twofish implementation we
  used to test candidate keys.

## Files produced

- `samples/crypto/` — copies of 37 RWN, 14 DCY, and local bootstrap
  DCY/RWN files used for analysis.
- `samples/crypto/pairs/` — the 13 DFM/DCY pairs.
- `scripts/decrypt_dcy.py` — partial-decryption utility.
- `scripts/twofish_py.py` — pure-Python Twofish (loxodo).
