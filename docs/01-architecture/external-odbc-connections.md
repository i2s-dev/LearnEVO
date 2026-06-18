# Connecting External Software to the EVO Database

Status: verified — confirmed working on a live workstation (2026-04-22)
against the `i2s109-solidcrm` Pervasive/Actian server. Read-only scope
only (per [../../CLAUDE.md](../../CLAUDE.md) — no writes to the share or
the database).

## TL;DR

- EVO's database is Pervasive/Actian PSQL (Btrieve + SQL via ODBC).
- The **only** connection path that works consistently across user
  machines is a pre-configured **ODBC DSN**, not a DSN-less driver
  string. Use `DSN=DBA` in code.
- **Bitness matters even with a DSN.** A 32-bit process sees only
  32-bit DSNs; a 64-bit process sees only 64-bit DSNs. They live in
  separate registry namespaces and are configured in separate admin
  UIs. Ship both builds of any tool, or pick the bitness that matches
  where the DSN was created.

## Machine prerequisites (what EVO users already have)

Every workstation where an employee runs EVO has:

1. A Pervasive/Actian client runtime installed (EVO requires it).
2. An ODBC DSN — typically called **`DBA`** — pointing at the
   `@DBA` database on `i2s109-solidcrm`. Often a second DSN named
   `ABI` points at the historical/archive database. These are created
   once during EVO install/setup.

If EVO itself launches and logs in successfully on a machine, the
Pervasive client and the DSN are present and working. That fact alone
is enough to know external ODBC code *can* connect from that machine —
you just have to speak to it correctly.

## Preferred connection string

```csharp
const string ConnectionString = "DSN=DBA;";
```

No driver name, no server, no database. The DSN carries all of that.

### Why not a DSN-less connection string?

The "obvious" form `Driver={Pervasive ODBC Interface};ServerName=i2s109-solidcrm;dbq=@DBA;`
**works on some machines and fails with `IM002` on others**, because
the exact registered driver name varies between Pervasive/Actian
releases. Depending on which components were installed, a machine may
have any combination of:

- `Pervasive ODBC Client Interface` (remote-server client — the one
  clients usually have)
- `Pervasive ODBC Engine Interface` (local engine)
- `Pervasive ODBC Interface` (a combined/compatibility alias — **not
  present on every install**, even though it's what most docs cite)

ODBC's `Driver={...}` clause is a literal registry lookup. If the
exact string isn't registered on that machine, you get `IM002: Data
source name not found and no default driver specified` even though a
fully functional Pervasive ODBC stack is right there. Using a DSN
bypasses this — you just ride on whatever driver the DSN was bound to
at setup time (which, by definition, is one that exists on the box).

## Bitness: the non-obvious trap

A .NET process built for `win-x64` is 64-bit and can only:
- load 64-bit ODBC drivers, and
- see DSNs stored in the **64-bit** ODBC registry hive.

A `win-x86` build is 32-bit and can only see the **32-bit** hive.
These are separate namespaces. A DSN named `DBA` in the 32-bit admin
is **invisible** to a 64-bit process and vice versa.

The admin UIs are also two separate executables despite confusing
names:

| Bitness  | ODBC admin path                          |
|----------|------------------------------------------|
| 64-bit   | `C:\Windows\System32\odbcad32.exe`       |
| 32-bit   | `C:\Windows\SysWOW64\odbcad32.exe`       |

(Yes — the one in `System32` is 64-bit and the one in `SysWOW64` is
32-bit. Microsoft legacy.)

**EVO itself is a 32-bit application** (TAS Pro 7 runtime is 32-bit —
see [../07-runtime-boot/boot-sequence.md](../07-runtime-boot/boot-sequence.md)),
so on most workstations the `DBA` DSN was created on the 32-bit side.
That means a 64-bit build of your external tool will hit `IM002` even
though EVO works fine on the same machine. The fix is to run the
32-bit build.

### Recommendation for external tools

Publish **both** bitnesses and distribute them side by side:

```
YourTool.exe        ← 64-bit, for machines with a 64-bit DBA DSN
YourTool-x86.exe    ← 32-bit, for machines matching EVO's native setup
```

A single MSBuild project can emit both via `dotnet publish -r win-x64`
and `dotnet publish -r win-x86`. See the `WhoClosedEVOWO` project's
`Build.bat` for a working two-output example.

### How to detect which one to run

At runtime in .NET: `Environment.Is64BitProcess` tells you the current
process's bitness. A helpful error catch:

```csharp
catch (OdbcException ex) when (ex.Message.Contains("IM002"))
{
    var bitness = Environment.Is64BitProcess ? "64-bit" : "32-bit";
    // Tell the user to check the matching ODBC admin, or switch to
    // the other bitness build if that DSN is configured there instead.
}
```

## Minimal working example (.NET 8, C#)

```csharp
using System.Data.Odbc;

const string ConnectionString = "DSN=DBA;";

using var conn = new OdbcConnection(ConnectionString);
conn.Open();
using var cmd = conn.CreateCommand();
cmd.CommandText = "SELECT WO_CHG_USER, WO_CHG_CDATE FROM WORKCHG " +
                  "WHERE WO_CHG_WOPRE = ? AND WO_CHG_WOSUF = ? " +
                  "ORDER BY WO_CHG_CDATE ASC";
cmd.Parameters.Add(new OdbcParameter { Value = "74314" });
cmd.Parameters.Add(new OdbcParameter { Value = "1" });

using var reader = cmd.ExecuteReader();
while (reader.Read())
{
    // ...
}
```

Project file must target a specific RID so that bitness is fixed at
publish time. `AnyCPU` is not sufficient — you need `win-x64` *or*
`win-x86` explicitly passed to `dotnet publish -r`.

## Common failures and what they mean

| Symptom                                              | Most likely cause                                                          |
|------------------------------------------------------|-----------------------------------------------------------------------------|
| `IM002` with DSN-less `Driver={Pervasive ODBC Interface}` | That exact driver name isn't registered on this machine (version-dependent). Switch to `DSN=DBA`. |
| `IM002` with `DSN=DBA` in a 64-bit build             | DSN was created on the 32-bit side only. Run the 32-bit build of your tool. |
| `IM002` with `DSN=DBA` in a 32-bit build             | The 32-bit DSN hasn't been set up on this machine yet. Open `SysWOW64\odbcad32.exe` and add a System DSN `DBA` pointing at `i2s109-solidcrm` / `@DBA`. |
| Connection opens but `SELECT` returns nothing       | Probably hitting the wrong database (`@DBA` vs. `@ABI`) — check which DSN name you used. |

## Known DSN names on this installation (Pass 105, 2026-06-18)

| DSN name | Used by | Purpose |
|----------|---------|---------|
| `DBA` | External tools, Crystal Reports, Excel | Standard Pervasive ODBC access to all 659 `.B` tables via SQL. Read-write. |
| `ABI` | Historical reporting tools | Points at the archive database (`@ABI`). |
| `EVOADMIN` | `StartEvo.exe` (.NET launcher) | Elevated Pervasive Server DSN used for license validation. StartEvo queries: `SELECT count(*) FROM tas_menus WHERE menu_name = ? AND program_name = ?` before allowing launch. Not for external tools — connection credentials unknown. |

The `EVOADMIN` DSN is set up as a **Server DSN** (format: `Server DSN=EVOADMIN;Host=<server>;Port=<port>`)
rather than a standard ODBC DSN. It is distinct from `DBA` and requires server-side configuration
on `i2s109-solidcrm`. Its purpose is licensing: `tas_menus` is the PSQL SQL-engine view of
`BKMENUSU.DBF` (the xBase menu database). If a program is not in `tas_menus`, StartEvo.exe
refuses to launch it regardless of what EVO's own security system (`AHSYLOG`) allows.

## Transactional vs. Relational API

Pervasive PSQL exposes two distinct access paths:

| API | Description | Who uses it |
|-----|-------------|-------------|
| **Btrieve (Transactional)** | Record-manager API: open/find/get/insert/update/delete by key. The native `.B` file format. | `tp7runtime.exe` (TAS Pro 4GL) — all EVO internal operations |
| **ODBC/SQL (Relational)** | SQL `SELECT`/`INSERT`/`UPDATE`/`DELETE` via ODBC driver over the same `.B` files. The DDF schema (`file.ddf`, `field.ddf`, `index.ddf`) provides the metadata. | `StartEvo.exe` (PSQL .NET driver), external reporting tools (Crystal Reports, BIRT, Excel) |

Both access the same physical `.B` files. The Btrieve API is faster and handles record locking
natively; the ODBC/SQL API is read-friendly for reporting. For write operations from external
tools, Btrieve semantics (including the DDF-defined indexes) are enforced at the engine level —
SQL `UPDATE` modifies the same B-tree as TAS Pro `write`.

## DSN setup parameters (what goes inside a Pervasive ODBC DSN)

When creating the `DBA` DSN in `SysWOW64\odbcad32.exe` (32-bit admin), the Pervasive ODBC
Client Interface driver prompts for:

| Parameter | Value for this installation |
|-----------|---------------------------|
| Data Source Name | `DBA` (or `ABI` for the archive database) |
| Server Name (Host) | `i2s109-solidcrm` |
| Database Name | `@DBA` (the `@` prefix is Pervasive shorthand for a server-registered database — distinct from a disk path) |
| Port | `1583` (default Pervasive TCP port; rarely changed) |
| Driver | `Pervasive ODBC Client Interface` (for remote connections from workstations) |

The connection string in code stays `DSN=DBA;` — all of the above is baked into the DSN by whoever
ran `odbcad32.exe` at workstation setup. No parameters need to be repeated in code.

`EVOADMIN` uses the **Server DSN** flavor (format: `Server DSN=EVOADMIN;Host=i2s109-solidcrm;Port=1583`)
and is configured server-side only — not visible in the workstation ODBC admin.

## Read/write capability via ODBC (Relational engine)

The Pervasive Relational engine (ODBC/SQL path) supports full SQL DML:

- **SELECT** — always works; primary use case for external reporting tools.
- **INSERT / UPDATE / DELETE** — work at the engine level. SQL writes go through the same
  Btrieve B-tree that TAS Pro uses, so indexes defined in the DDF are maintained automatically.
  EvoERP has **no database-side constraints** (no FK, triggers, or stored procedures in Pervasive) —
  all referential integrity is enforced in TAS Pro application code. An external SQL write
  bypasses those application-layer rules entirely.

Practical implication: external ODBC code *can* corrupt EVO data if it writes rows that
TAS Pro would consider invalid (wrong status codes, missing cross-references, etc.). Use
ODBC writes from external tools only for non-critical housekeeping (e.g., setting flags in
a custom table). Never write to core transactional tables (BKARINV, BKICMSTR, etc.) from outside EVO.

## Table locking behavior when EVO has records open

Pervasive PSQL's Relational engine uses **read-committed isolation** for ODBC connections.
Key behaviors:

- **ODBC reads (SELECT)** see the last committed version of a record and are **never blocked**
  by a Btrieve lock held by EVO — even if TAS Pro has the record open in an edit session.
  Dirty reads are not possible; you see committed data only.

- **ODBC writes (INSERT/UPDATE/DELETE)** can conflict with Btrieve locks. If TAS Pro holds
  an explicit record lock (`B_SINGLE_NO_WAIT_LOCK` or similar), an ODBC UPDATE on the same
  record returns SQLSTATE `40001` (serialization failure) or a timeout. In practice EVO holds
  locks only for the duration of a single screen save (milliseconds), so conflicts are transient.

- **File-level locks** (`B_FILE_LOCK`) are used by EVO during month-end close and some posting
  operations. During these periods, ODBC reads may block until the file lock is released.

Summary: for reporting (SELECT), ODBC reads are safe at any time. For writes, coordinate to
avoid the narrow windows when EVO holds explicit locks.

## Related

- [../04-data-dictionary/overview.md](../04-data-dictionary/overview.md)
  — the 659 tables you can `SELECT` from once connected.
- [./security-and-login.md](./security-and-login.md) — EVO's own login
  path (separate from raw ODBC; uses `AHSYLOG`).
