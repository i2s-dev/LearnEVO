# `.RWN` / `.DCY` Decryption — Research Findings

Status: **FULLY SOLVED 2026-06-16**

Last updated: 2026-07-07

---

## FINAL CONFIRMED CIPHER PARAMETERS

All confirmed via live Frida capture (`frida_capture_key_and_iv.py`) + Python decryption test.

### Algorithm
- **Cipher**: Twofish, 128-bit block, **192-bit key**, **CFB-128 mode**
- **Key derivation**: `SHA1(runtime_passphrase)[0:20]` + `\x00\x00\x00\x00` = 24 bytes
- **IV parameter to SetKey**: always 0 → P_initial = Encrypt_K(all-zeros)
- **key_bits (ECX at SetKey entry)**: 160 (= SHA1 output length in bits; padded to 192 with 4 zeros)

### Keys (live-captured 2026-06-16; expanded 2026-07-07 Frida session)

Confirmed via Frida CreateFileW hook on evoerp.exe — every SetKey call captured with a
ring buffer of the 30 most recent EVO-extension file opens.

| Key name | SHA-1 (first 20 bytes) | File type confirmed |
|----------|------------------------|---------------------|
| K_A | `d97f05679438037073c30628734764020859f77e` | **WHOAMI.DBA** — identity/license file (K_A fired 5×; WHOAMI.DBA was last in buffer every time) |
| K_B | `a898d21e2fd6ca294026e5d633d9047f91f7ed35` | **.RWN** files (regular TAS Pro 7 modules) |
| K_C | `507d2b20f46ac5f82d47e82a9065d7bc0c2e12bb` | **suwin6.dcy** — ISTech License dialog form |
| K_D | `691e8041ab265b4e6ee052ccc946dba4caac60da` | **.DCY** files (regular Delphi form files) |
| K_E | `d6e9efa8195c45cce839e88e52767768ff8f2463` | **suwin7.dcy** — ISTech subsystem form (fires first at boot; K_E fired once at boot with only suwin7.dcy in buffer) |
| K_F | `fdc2883f6d6537dd667270406d0a4c85969295ac` | **suwin6t.rwn** — ISTech License runtime code companion (K_F fired once with suwin6t.rwn as trigger) |

**NOTE (2026-07-07):** The hash previously recorded for K_C (`fdc2883f...`) was incorrect — that is K_F's hash.
K_C's correct SHA-1 is `507d2b20...` (re-confirmed against suwin6.dcy decryption output).

**suwin6.dcy / K_C confirmed (2026-06-17, re-verified Pass 375 2026-06-29 — prior "binary opcodes" finding was WRONG):**
- Validation block: `4b7650d14b7650d1` — pt[0:4] == pt[4:8] ✅
- **CORRECTION (Pass 375):** Decrypts to a **Delphi VCL text form**, NOT compiled bytecode.
  The earlier "binary opcodes" finding was produced by a stale `suwin6_decrypted.bin` from an
  incorrectly parameterized decryptor (pre-cipher-confirmation code). The correct output is:
  `object EditForm1_1: TEditForm1_1` — the **ISTech License dialog**.
- **ISTech License dialog contents:**
  - Caption = `' ISTech License'` (modal, `fsStayOnTop`)
  - Memo1 (company address): `i2 Systems / 355 Bantam Lake Rd / Morris, CT 06763`
  - `lblUserSerialNum` Caption = `'670538'` — hardcoded **serial number**
  - `lblUserNum` Caption = `' 48'` — **48 concurrent users** licensed
  - `lblLicenseType` Caption = `'License Type'`; `lblUserLicType` Caption = `'VPY'` — **VPY license type**
  - `lblFromIgnore` / `lblThruIgnore` — hidden labels, set at runtime to license date range
  - `lblLimitedUse` Caption = `'***'` — placeholder for limited-use status
  - `btnContinue: TGlyphBtn` — dismissal button
  - `Timeout: TRtnTimer` — 3000ms auto-dismiss timer
  - Hint = `'C:\TASPRO7\DBA7\tas6evodba.DFM'` — developer path: ISTech uses `C:\TASPRO7\DBA7\`
  - Copyright: `Evo~ERP 2003-2013 All Rights Reserved` + `MGM Holdings 1985-2003`
- **Purpose of K_C**: protects the license dialog DCY (contains hardcoded serial and user count)
- `samples/suwin6_decrypted.bin` regenerated correctly (Pass 375)
- All DCY files (Type A and B) use the same Delphi VCL text format; K_C and K_D differ only in key bytes

**suwin key summary (corrected Pass 375; K_E/K_F confirmed 2026-07-07):**
| File | Key | Format / Notes |
|------|-----|----------------|
| suwin6.dcy | K_C | Delphi VCL text form (`EditForm1_1` — ISTech License dialog) |
| suwin6.dcy (Default/) | K_C | Same as above (copy for Default company) |
| suwin6t.rwn | K_F | ISTech License runtime code companion (NOT standard K_B — confirmed 2026-07-07) |
| suwin7.dcy | K_E | ISTech subsystem form; fires first at boot (confirmed 2026-07-07 Frida capture) |
| suwin7.rwn | K_B | Standard RWN binary |

**suwin7.dcy — RESOLVED 2026-07-07:**
- Previously: 3,527 bytes, entropy 7.945 — K_A/K_B/K_C/K_D all failed
- Now confirmed: uses K_E (`d6e9efa8195c45cce839e88e52767768ff8f2463`)
- K_E fired once at boot with only suwin7.dcy in the file-open ring buffer

192-bit key = raw key + `\x00\x00\x00\x00`.

**The passphrase "mabufoju" was WRONG.** That was a static string found near the cipher code but is NOT the runtime passphrase. The runtime passphrase is in a BSS global initialized at startup; its plaintext has not been recovered. The raw key bytes above are sufficient for decryption.

### DCY cipher parameters (fully confirmed)

```
K_D_192     = 691e8041ab265b4e6ee052ccc946dba4caac60da00000000
P_initial   = Encrypt(K_D_192, zeros)  = 83fcde64a3f87b20076b10a9a4fc8a7f
K0          = Encrypt(K_D_192, P_init) = ab3c1a7a2fe04f7322f10dfda5ea3636
```

Validation (K0 XOR constant, little-endian le32):
`le32(K0, 0) XOR le32(K0, 4)` = `0x7A1A3CAB XOR 0x734FE02F` = **0x0955DC84** ✓

### RWN cipher parameters (fully confirmed)

```
K_B_192     = a898d21e2fd6ca294026e5d633d9047f91f7ed35 00000000
P_initial   = Encrypt(K_B_192, zeros)  = 0e6fbff653a28a70d102874c6b1825ad  (= IV_rwn)
K0          = Encrypt(K_B_192, P_init) = 8deb949048dc9eae9fdf1779cdc8b551
```

---

## File structure and decryption algorithm

### File layout (same for .RWN and .DCY)

```
Byte 0-7:   Validation header (8 bytes ciphertext)
Byte 8+:    Body (N bytes ciphertext)
```

### Decryption algorithm

```python
from twofish_pure import Twofish

def decrypt_evo_file(raw_bytes, key_raw_20):
    key_192 = key_raw_20 + b'\x00' * 4
    tf = Twofish(key_192)
    P_init = tf.encrypt(bytes(16))       # P_initial
    K0     = tf.encrypt(P_init)          # header keystream

    # Validate header
    header_ct = raw_bytes[0:8]
    header_pt = bytes(a ^ b for a, b in zip(header_ct, K0[:8]))
    assert header_pt[0:4] == header_pt[4:8], "Validation failed"

    # Decrypt body — CRITICAL: P starts at K0, NOT P_initial
    P      = K0
    body   = raw_bytes[8:]
    result = bytearray()
    for i in range(0, len(body), 16):
        blk = body[i:i+16]
        K   = tf.encrypt(P)
        result.extend(a ^ b for a, b in zip(blk, K))
        if len(blk) == 16:
            P = blk          # CFB-128: feedback = ciphertext block
    return bytes(result)

# Decrypt DCY file:
raw = open('SOMEFILE.DCY', 'rb').read()
K_D = bytes.fromhex('691e8041ab265b4e6ee052ccc946dba4caac60da')
plaintext = decrypt_evo_file(raw, K_D)

# Decrypt RWN file:
K_B = bytes.fromhex('a898d21e2fd6ca294026e5d633d9047f91f7ed35')
plaintext = decrypt_evo_file(raw_rwn, K_B)
```

### Critical detail — body P_start = K0 (assembly-confirmed 2026-06-16)

**Mechanism (from `mode2_handler` disassembly, file 0x34DF50):**

DCPcrypt's CFB mode has two separate code paths depending on block completeness:

- **Full 16-byte block** (body): after XOR, executes `Move(CT[0:16] → block_buf)` — CFB feedback update.
- **Partial block** (8-byte validation header): `EncryptBlock(P_initial → K0)` runs, then XOR, but **no** `Move(CT → block_buf)` is executed.

Relevant assembly (partial-block path, `0x74EBF6`–`0x74EC27`):
```
0x74EBF6  mov eax, [ebx+0x3c]  ; block_buf ptr (P_initial on first call)
0x74EC01  call [esi+0x58]       ; EncryptBlock(P in-place) → block_buf = K0
0x74EC13  call 0x403544         ; Move(CT[0:8] → output[0:8])
0x74EC27  call 0x74f18c         ; XorBuf(output[0:8] ^= K0[0:8], 8)
                                 ; <- NO Move(CT → block_buf) here
```

Full-block path (body loop, `0x74EBD1`):
```
0x74EBD1  call 0x403544         ; Move(CT[0:16] → block_buf) <- feedback update ONLY for full blocks
```

**Result:** After the 8-byte partial validation block, `block_buf = K0`. No code resets or re-arms it.
When `body_load` (0x74E374) calls `mode2_handler` for the body chunks, the same cipher object
is used with `block_buf` still = K0. So body block 1 keystream = `Encrypt(K0)`.

This is standard DCPcrypt partial-block CFB behavior, not a special re-arming. Confidence: **100/100**.

---

## Validation constants

The 8-byte validation header serves as an integrity/key check. Plaintext passes when:
- `header_pt[0:4] == header_pt[4:8]`  (first word equals second word)

The EncryptBlock XOR filter used in Frida capture scripts:
- `.RWN` files: `le32(K0, 0) XOR le32(K0, 4) = 0x3E0A37C5`  
- `.DCY` files: `le32(K0, 0) XOR le32(K0, 4) = 0x0955DC84`

These constants are derived from K0 (which is fixed for a given key), not from the file content.

---

## Verification results (2026-06-16)

| Test | Result |
|------|--------|
| K_D decrypts MDUMMY.DCY validation | `d484de56 d484de56` (equal) ✓ |
| K_D decrypts MDUMMY.DCY body | `object EditForm1: TEditForm1\r\nLeft=0\r\nHint='C:\taspro7\DBA7\mDummy.DFM'...` ✓ |
| K_B `Encrypt(zeros)` = IV_rwn | `0e6fbff653a28a70d102874c6b1825ad` ✓ |
| key_bits (live capture) | 160 for all SetKey calls ✓ |
| IV param (live capture) | 0x00000000 for all SetKey calls ✓ |

---

## DCY file content structure (Pass 109 — 2026-06-18)

After decryption, every DCY file has the following layout:

```
Offset  Size  Field
0       4     File ID (4-byte value, purpose unknown — possibly a CRC or timestamp)
4       4     File ID repeated (identical to bytes 0-3)
8       var   DFM content — one of two forms:
```

**Form A — Text DFM (37 of 41 files):**
```
Offset 8+: Standard Delphi text DFM starting with "object <ClassName>: T<ClassName>"
```
Content is 100% plain Delphi text DFM format — readable directly as ASCII/Latin-1.

**Form B — Binary DFM (4 files: DBAMENU_LOGIN, DBAMENU_RUNPRG, DBAMENU_SELCOMP, DBAMENU_FLEX):**
```
Offset 8:     0xFF 0x0A 0x00       (binary-DFM format marker)
Offset 11:    <classname>\0        (null-terminated uppercase class name, e.g. "TEDITFORM4")
Offset 11+N:  0x30 0x10            (constant — possibly Delphi component version flag)
Offset 13+N:  uint16-LE            (DFM content size in bytes = file_size - 28)
Offset 15+N:  0x00 0x00            (padding)
Offset 28:    TPF0<binary DFM>     (standard Delphi binary DFM format, see Object Pascal docs)
```

The DFM content size stored at offset 13+N exactly equals `file_size - 28` in all 4 confirmed cases.

**DCY files are Delphi UI forms, NOT data dictionary files.** The name "DCY" appears to
stand for something other than "data dictionary" — all 41 decrypted files are Delphi form
definitions (`TEditForm1` through `TEditForm17`). They define the top-level program windows
for the EvoERP launcher and utility programs (not for the TAS Pro 7 RWN-based modules, which
use DFM files on the network share instead).

**Notable DCY forms (Pass 109):**

| DCY file | Caption | Purpose |
|----------|---------|---------|
| EVOERPMENU.DCY | " Evo - ERP" | Main EvoERP menu — 1.4MB, 20,868 lines; 30 toolbar slots tb1..tb30; full menu: File/Module/Tools/Size/Support/Help; TTASStrList for button/group/menu data |
| EVOUSERS.DCY | " Evo Users" | Active-user management grid — shows ISLOG table fields (WHO/COMPANY/WHAT/DOING/STARTT/STARTD/KILL); buttons: Logout Users / Enable Logins / Disable Logins / Clear User / Message |
| WBKLOOKUP.DCY | "Lookup: " | Core universal lookup dialog — TTASDataGrid + cbKeys (index selector); Select/Edit/AddNew/Delete buttons |
| WBKLUGRID.DCY | "Maintain Grid Lookup Data" | Configures column layouts for BKLUGRID lookup grids; FD_* field config (header/fieldname/type/size/func/edit) + KD_* sort key config |
| EVOERPBACKUP.DCY | (backup form) | EvoERP backup configuration form |
| EVOERPSCHED.DCY | (scheduler form) | EvoERP task scheduler form |
| MDUMMY.DCY | (dummy base) | Base EditForm1 template with embedded icon data |
| DUMMY.DCY | (dummy base) | Same as MDUMMY — alternate template |

**EVOUSERS confirmation:** The EvoUsers form is the admin screen for managing logged-in users.
It displays ISLOG table fields in a grid, confirming that `IS_LOG_KILL = '.T.'` is set via
this screen's "Logout Users" button to force a graceful session termination.

## What is NOT yet known

- The plaintext passphrase(s) behind K_A through K_F — not needed for decryption; raw bytes sufficient
- Whether additional keys beyond K_F exist (other encrypted file types not yet observed)
- Whether different file types (.RUN, old-gen) use the same cipher
- The meaning of the 4-byte repeated File ID in the DCY header (CRC? Timestamp? Random?)
- The decrypted content and form structure of suwin7.dcy (key K_E now confirmed; decryption not yet run)

**Resolved 2026-07-07 (no longer unknown):**
- ~~What K_A is used for~~ → **WHOAMI.DBA** (identity/license file)
- ~~What K_E and K_F are~~ → **K_E = suwin7.dcy**, **K_F = suwin6t.rwn**

### File-open trace observations (2026-07-07 Frida session)

The following previously undocumented files were observed in the CreateFileW ring buffer
during the live capture session:

| File | Key used | Notes |
|------|----------|-------|
| evomenu_Login.DCY | K_D | Login dialog form |
| issplash.DCY | K_D | Splash screen form (shown at startup) |
| EVO.UPD | — | Update definition file (observed opened; encryption status unknown) |
| START_UP.RUN | — | TAS Pro 6 startup routine — **unencrypted** (pre-TAS7 era) |
| suwin7.rwn | K_B | Companion runtime to suwin7.dcy; uses standard RWN key (not K_E) |

---

## How B-007 was solved (2026-06-16)

Prior analysis used sha1("mabufoju") which was WRONG. Fixed by:
1. Running `frida_capture_key_and_iv.py` (dynamic address resolution via `mod.base.add(RVA)`)
2. Observing key_bits=160, live key bytes ≠ sha1("mabufoju")
3. Testing all 4 live-captured keys against MDUMMY.DCY → K_D validates ✓
4. Discovering body P_start = K0 by computing `Decrypt_KD(emp_ks0) = K0`

See BROKEN.md B-007 for full attempt history.

---

## Dead ends (do not retry)

- sha1("mabufoju") as passphrase — WRONG key, confirmed 2026-06-16
- IV_dcy = `cd47af18...` — was derived with wrong key, invalid
- P_initial as body P_start — wrong; body starts at P = K0
- CFB-64 / CFB-8 / OFB variants — wrong mode; standard CFB-128 confirmed
- All attempts in BROKEN.md B-007 table (11 failed attempts, 2026-06-15)
