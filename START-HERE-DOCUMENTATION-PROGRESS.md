# START-HERE-DOCUMENTATION-PROGRESS.md

> **Read this first.** This document tells any new agent (or returning agent) exactly where
> the decompilation project stands, what work is available right now, and what is blocked.
> It is the authoritative session-start checklist. Keep it current.

Last updated: 2026-06-12

---

## 1. Project in one paragraph

We are reverse-engineering **EvoERP**, a manufacturing ERP built on TAS Professional 7
(`tp7runtime.exe`). The vendor has granted explicit permission to decompile. EvoERP has
two compiled-program formats: `.RUN` (TAS Pro 6, unencrypted) and `.RWN` (TAS Pro 7,
encrypted). We have confirmed the `.RWN` cipher is **Twofish** (DCPcrypt `TDCP_twofish`),
identified a candidate passphrase, and fully mapped the decrypt function addresses in
`tp7runtime.exe`. We cannot yet validate the passphrase because the Python environment
lacks a working Twofish library. All `.SRC`, `.RUN`, `.DCY`, `.DFM`, `.RTM`, and `.B`
work is fully unblocked and should proceed autonomously.

---

## 2. What we CAN do right now

These tasks are fully unblocked. Proceed autonomously:

| Task | Where to start |
|------|---------------|
| Read and document `.SRC` files (TAS Pro 7 source — plain text) | `\\i2s109-solidcrm\DBAMFG$\` (read-only) or copies in `samples/` |
| Read, hex-dump, and analyze `.RUN` files (TAS Pro 6 compiled — unencrypted) | `samples/rosetta/*.RUN` |
| **Rosetta Stone opcode mapping** — correlate `.SRC` source constructs with `.RUN` binary patterns to build an opcode table | `samples/rosetta/` — 7 complete SRC+RUN pairs |
| Read and document `.DCY` data dictionary files (schema definitions) | Network share, read-only |
| Read and document `.DFM` form files (UI layout) | Network share, read-only |
| Read and document `.RTM` ReportBuilder report templates | Network share, read-only |
| Study `.B` Btrieve data files via `.DDF` schema files | Network share, read-only |
| Study `tp7runtime.exe` in read-only mode (hex dump, string search, Capstone disassembly) | `C:\ISTS\tp7runtime.exe` (read-only) |
| Update `docs/`, `PROJECT-STRUCTURE.md`, `HELP-RESOURCES.md`, `EVO-DECOMPILE-TODO.md` | This workspace (read-write) |
| Write the `.RUN` disassembler (`scripts/run_disasm.py`) once enough opcodes are mapped | `scripts/` |

---

## 3. What we CANNOT do yet (blocked)

Do NOT attempt these until the blocker in §4 is resolved:

| Blocked task | Why |
|-------------|-----|
| Decrypt any `.RWN` file | Twofish passphrase not yet validated |
| Disassemble `.RWN` bytecode | Blocked on decryption |
| Write `rwn_decrypt.py` or `batch_decompile.ps1` | Blocked on key confirmation |
| Write stub / placeholder code for the `.RWN` path | Forbidden — creates false progress |

---

## 4. The current blocker — and how to resolve it

**Blocker:** Python `pycryptodome` does not include Twofish. The candidate passphrase
cannot be tested without a working Twofish implementation.

**What we know:**
- Cipher: **TDCP_twofish** (Twofish block cipher from DCPcrypt)
- Candidate passphrase: `"An error has occurred during conversion of this field from alpha to the appropriate binary form."`
- Key derivation: `SHA1(passphrase)[0:20]` + zero padding (NOT cycling)
- Validation target: decrypt `samples/rosetta/T7INA.RWN` offset 0x10 onward; bytes at
  decrypted offset 0xC5–0xC9 must equal `TAS32` (`54 41 53 33 32`)

**Two paths to resolve the blocker (pick whichever is available):**

### Path A — Get a working Twofish Python library
```powershell
# Try these in order until one works:
pip install twofish                        # pure Python; needs MSVC build tools
pip install twofish --no-build-isolation   # alternate
# If both fail, install Visual C++ Build Tools and retry
```
Once installed, run `scripts/rwn_validate.py` (template already in `DECOMPILE-INSTRUCTIONS.md`).

### Path B — x64dbg runtime memory dump (no library needed)
1. Download x64dbg: https://x64dbg.com/
2. Launch `tp7runtime.exe` and open a small `.RWN` (e.g. `suwin7.rwn`, 8.6 KB)
3. Set a breakpoint at VA `0x742654` (the RWN header decrypt/validate function)
4. When the breakpoint hits, step past the `InitStr` call (VA `0x74E1F8`)
5. The TDCP_twofish cipher object is in register EBX; read 16–32 bytes from
   `[EBX + key_offset]` — this is the derived key
6. Copy those bytes into `rwn_validate.py` and test directly (no library needed for
   a raw-key test via pycryptodome's DES3 substitute — or implement one block manually)

---

## 5. Research state snapshot

| Area | Status | Confidence | Notes |
|------|--------|-----------|-------|
| `.RWN` cipher identified | ✅ Done | 92/100 | Twofish (TDCP_twofish), VMT confirmed |
| Passphrase candidate | ✅ Found | 55/100 | "An error has occurred..." — untested |
| Key derivation method | ✅ Confirmed | 88/100 | SHA1 + zero pad, confirmed from code |
| TAS32 plaintext check location | ✅ Confirmed | 96/100 | Decrypted offset 0xC5, 5 bytes |
| Passphrase validated against T7INA.RWN | ❌ Blocked | 0/100 | Needs Twofish library or x64dbg |
| `.RWN` decryptor script | ❌ Blocked | — | Blocked on validation |
| `.RUN` header structure | 🔄 Partial | 92/100 | Magic + file table confirmed; bytecode start TBD |
| `.RUN` opcode table | ❌ Not started | 0/100 | 7 Rosetta Stone pairs ready; work unblocked |
| `.SRC` source language | ✅ Documented | 90/100 | Full syntax reference in DECOMPILE-INSTRUCTIONS.md |
| `.DCY` data dictionary | 🔄 Partial | 50/100 | Some tables documented in docs/ |
| `.DFM` forms | 🔄 Partial | 40/100 | Format known; content coverage low |
| `.RTM` report templates | 🔄 Partial | 40/100 | Format known; content coverage low |
| `PROJECT-STRUCTURE.md` | 🔄 In progress | — | Updated each session |
| `HELP-RESOURCES.md` | 🔄 In progress | — | Updated each session |

---

## 6. Key documents — read these before working

| Document | Purpose |
|----------|---------|
| `DECOMPILE-INSTRUCTIONS.md` | Full `.RWN` decryption research: cipher, addresses, key derivation, Python code templates |
| `EVO-DECOMPILE-TODO.md` | Master checklist with confidence ratings for every analysis area |
| `docs/README.md` | Index of all documentation completed so far |
| `PROJECT-STRUCTURE.md` | Catalog of every EvoERP file and its purpose |
| `HELP-RESOURCES.md` | User-facing knowledge base: tables, fields, how-to recipes |
| `research/OPEN_QUESTIONS.md` | Unresolved questions — pick from here for next work |
| `CLAUDE.md` | Scope rules, autonomy protocol, confidence ratings, all standing instructions |

---

## 7. Highest-value next tasks (in priority order)

1. **Resolve the Twofish blocker** (Path A or B above) — unlocks everything
2. **`.RUN` opcode mapping** — 7 Rosetta Stone pairs in `samples/rosetta/`; start with
   `BKAWLB.SRC` + `BKAWLB.RUN` (smallest pair at 139 KB compiled); map `proc`/`return`
   first, then `open`/`close`, then `if`/`endif`
3. **`.DCY` data dictionary coverage** — read all `.DCY` files from the network share;
   document table names, field names, key fields; feed into `HELP-RESOURCES.md`
4. **`.SRC` module coverage** — read T7* source files and document each module's purpose,
   the tables it touches, and its menu entry
