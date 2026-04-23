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

## Related

- [../04-data-dictionary/overview.md](../04-data-dictionary/overview.md)
  — the 649 tables you can `SELECT` from once connected.
- [./security-and-login.md](./security-and-login.md) — EVO's own login
  path (separate from raw ODBC; uses `AHSYLOG`).
