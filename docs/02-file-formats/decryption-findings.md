# `.RWN` / `.DCY` Decryption — Research Findings

Status: **cipher fully identified; passphrase confirmed; initial IV unknown (one debugger
session away from full decryption)**

Last updated: 2026-06-15

---

## Current state (2026-06-15)

Everything about the cipher is confirmed except the initial 16-byte IV
(`block_buf` at cipher+0x3C inside `tp7runtime.exe`). One debugger session away.

**Confirmed:**
- Cipher: **Twofish**, 128-bit block, **192-bit key**, **CFB mode**
- Passphrase: **`mabufoju`** — hardcoded at file offset `0x75D154`
- Key: `SHA1('mabufoju')[0:20]` + `\x00\x00\x00\x00` = 24 bytes (192-bit)
- Q-box tables (q0 @ file `0x7740A8`, q1 @ `0x7741A8`) verified byte-for-byte vs NIST spec
- `scripts/twofish_pure.py` passes the NIST 192-bit test vector ✓
- Validation: first 8 bytes of every `.RWN`; decrypted pt[0:4] must equal pt[4:8]
- All 20+ scanned `.RWN` files share `ct[0:4]^ct[4:8] = 0x3E0A37C5` ✓
- mode2_handler entry bytes at file 0x34DF50: `55 8b ec 83 c4 f4 53 56 57` ✓
- block_buf is a **16-byte INLINE array** at cipher+0x3C (not a pointer; first 4 bytes
  look like a heap address but are the IV bytes themselves)

**CONFIRMED DEAD END — do not retry:**
- `.DCY` and `.RWN` files use **DIFFERENT IVs**.
  Proof: MDUMMY.DCY has ct[0:4]^ct[4:8] = 0x09553584; all .RWN = 0x3E0A37C5.
  The empirical keystream `0f73767aa296137875eaa22d6fc64b54` from MDUMMY.DCY XOR
  mDummy.DFM is the .DCY keystream Encrypt(IV_dcy) — useless for .RWN decryption.
  See BROKEN.md B-005 for full attempt log.

**Outstanding blocker:**
- `block_buf` is heap garbage, never zeroed; IV ≠ zeros (`0xCE14BE8C` ≠ `0x3E0A37C5`)
- Actual value requires observing block_buf at the FIRST call to mode2_handler
  in a tp7runtime.exe child process that is loading a real .RWN module file

**Current approach — Frida child gating:**
`scripts/get_iv_frida.py` (v3) attaches to evoerp.exe and enables child gating.
When the user closes a module window (e.g. WO-A) and reopens it, Frida pauses the
new tp7runtime.exe child before it runs a single instruction, injects the
mode2_handler hook, then resumes it. IV is captured on the first decrypt call.

See `BROKEN.md` entry B-004/B-005 for the full attempt log.

---

## File structure

```
.RWN file layout:
  [8 bytes — validation block (encrypted; pt[0:4]==pt[4:8] when correct key+IV used)]
  [N bytes — encrypted TAS Pro 7 bytecode body]
```

The 8-byte validation block serves as a passphrase check. After the 8-byte decrypt,
`block_buf` holds the **keystream** (not ciphertext), so subsequent body decryption uses
OFB-like behaviour — the decryptor can continue the keystream without re-seeding.

```
.DCY file layout:
  [same encryption model as .RWN]
  [decrypted content: Delphi VCL form text ("object EditForm...")]
```

---

## Key addresses in tp7runtime.exe

All offsets are raw file offsets. `VA = file_offset + 0x400C00`.

| Symbol | File offset | VA |
|--------|------------|-----|
| validate_func (outer RWN loader) | `0x742654` | `0xB42E54` |
| mode2_handler (CFB decrypt — **breakpoint here**) | `0x34DF50` | `0x74EB50` |
| TDCP_blockcipher constructor | `0x34E230` | `0x74EE30` |
| TDCP_cipher.Init (sets initialized flag; no block_buf) | `0x34D58C` | `0x74E18C` |
| Twofish.Init (key schedule; no block_buf) | `0x34ECA4` | `0x74F8A4` |
| EncryptBlock | `0x34F648` | `0x750248` |
| InitStr_internal (SHA1 key derivation) | `0x34D5F8` | `0x74E1F8` |
| SHA1.Init VMT slot | `0x34CD90` | `0x74D990` |
| passphrase 'mabufoju' string | `0x75D154` | `0xB5DD54` |
| q0 table | `0x7740A8` | `0xB74CA8` |
| q1 table | `0x7741A8` | `0xB74DA8` |

---

## Key derivation (confirmed)

```python
import hashlib
passphrase = b'mabufoju'
key = hashlib.sha1(passphrase).digest() + b'\x00' * 4  # 24 bytes (192-bit)
# key = ecd3549bfed4903bfbf6b50ff92a22fe5b81b0a0 00000000
```

---

## Validation logic (from disassembly of validate_func)

```
+33: CALL stream.Read → reads 8 bytes from .RWN into buf[0..7]
+39: Twofish.Create → create cipher object (EBX = cipher)
+5B: CALL InitStr_internal('mabufoju') → key schedule
+64: MOV BYTE [EBX+0x34], 2   → set mode = 2 (CFB)
+66: PUSH 8                    → size = 8
+68: LEA ECX, [EBP-0x11]      → buf ptr (src)
+6B: LEA EDX, [EBP-0x11]      → buf ptr (dst)
+6E: MOV EAX, EBX             → cipher obj
+74: CALL [VMT+0x50]           → mode2_handler → CFB decrypt 8 bytes
+78: MOV EAX, [EBP-0x11]      → pt[0:4]
+7B: CMP EAX, [EBP-0xD]       → compare pt[4:8]
+7E: JZ → success path         → if equal: proceed to load
+9C: CALL file 0x34D774        → main decrypt-and-load with same cipher
```

After the validation decrypt, the cipher continues in CFB/OFB-like mode for the body.
The 8 validation bytes are the only sentinel; the body is loaded contiguously.

---

## Twofish VMT layout (in tp7runtime.exe)

VMT base at file `0x34E6A8` (VA `0x74F2A8`):

| Slot | File offset | Purpose |
|------|------------|---------|
| VMT[+0x40] | `0x34ECA4` | Twofish.Init |
| VMT[+0x44] | `0x34F614` | Twofish.Done |
| VMT[+0x50] | `0x34DABC` | mode dispatch / Encrypt/Decrypt |
| VMT[+0x58] | `0x34F648` | EncryptBlock |
| VMT[-0x2C] | → `"TDCP_twofish"` | class name (confirmed) |

---

## What was tried and failed

| Attempt | Result |
|---------|--------|
| IV=zeros, SHA1('mabufoju') 192-bit | XOR = 0xCE14BE8C ≠ 0x3E0A37C5 |
| IV=zeros, 128-bit / 256-bit key variants | Wrong |
| IV=file[0:16], all key variants | Wrong |
| SHA1/MD5/SHA256 × 128/192/256-bit × various IVs | All wrong |
| 474k+ embedded strings tried as passphrase (earlier session) | No match |
| ~60 hand-crafted EvoERP phrases (earlier session) | No match |
| Analytical: derive IV from MDUMMY.DCY XOR mDummy.DFM (all OFB/CFB variants) | Dead end — .DCY uses different IV from .RWN |
| Frida spawn tp7runtime.exe with suwin7.rwn | mode2_handler never fires; process exits before RWN load |

See `BROKEN.md` B-004/B-005 for full detail. Do NOT retry: IV=zeros/SHA1-192; analytical DCY derivation.

---

## How to complete decryption (one session)

1. Install x64dbg (free, no install required): https://x64dbg.com/
2. Launch `C:\ISTS\tp7runtime.exe` with a small `.RWN` (e.g. `C:\ISTS\suwin7.rwn`)
3. Set breakpoint at VA `0x74EB50` (file offset `0x34DF50`) — `mode2_handler` entry
4. When breakpoint hits: EAX = cipher object pointer
5. Read bytes `[EAX + 0x3C]` through `[EAX + 0x4B]` (16 bytes) — this is `block_buf` = IV
6. Share those 16 bytes; `scripts/rwn_decrypt.py` can be written immediately

---

## Historical note — earlier analysis

An earlier pass (before the passphrase was found) derived an empirical keystream by
XOR-ing `MDUMMY.DCY[8..23]` against `MDUMMY.DFM[0..15]`, producing a first-block
keystream of `0f 73 76 7a a2 96 13 78 75 ea a2 2d 6f c6 4b 54`. This was validated
against 11 DCY/DFM pairs and produced consistent results. That keystream is now
understood as `Twofish_CFB_Encrypt(K, block_buf)` for the 16-byte block at offset 8 in
`.DCY` files (where the first 8 bytes are the validation block). It can be used to
verify the IV once it is retrieved from the debugger:

```python
# After getting block_buf from debugger:
# Encrypt block_buf with SHA1('mabufoju') 192-bit key using Twofish-ECB
# Result should match 0f 73 76 7a a2 96 13 78 75 ea a2 2d 6f c6 4b 54
# (this cross-checks both the IV value and the key)
```

---

## Scripts

| Script | Status | Purpose |
|--------|--------|---------|
| `scripts/twofish_pure.py` | ✅ Working | Pure Python Twofish; passes NIST 192-bit test vector |
| `scripts/get_iv_frida.py` | ✅ v3 Ready | **Primary IV extractor** — child gating on evoerp.exe; close+reopen module window |
| `scripts/x64dbg_get_iv.txt` | ✅ Ready | Manual fallback — step-by-step x64dbg instructions |
| `scripts/verify_iv.py` | ✅ Ready | Cross-checks iv_bytes.bin against RWN validation constraint |
| `scripts/rwn_decrypt.py` | ✅ Ready | Batch OFB/CFB decryptor — reads iv_bytes.bin, decrypts all .RWN/.DCY |
| `scripts/rwn_validate.py` | 🔄 Passphrase fixed | Validates RWN first 8 bytes; IV still wrong |
| `scripts/rwn_scan.py` | 🔄 Passphrase fixed | Broad-spectrum scan for decrypted content |

### One-time workflow (run in this order after getting Frida)

```
pip install frida-tools
python scripts/get_iv_frida.py          # extracts iv_bytes.bin
python scripts/verify_iv.py             # confirms IV is correct
python scripts/rwn_decrypt.py --validate-only --limit 20   # spot-check 20 files
python scripts/rwn_decrypt.py           # full batch decrypt → samples/rwn_decrypted/
```
