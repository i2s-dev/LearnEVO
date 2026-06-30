# EvoERP — Network Topology and Pervasive SQL Configuration

Status: verified | Pass 405 2026-06-30

Sources: ODBC DSN registry (this workstation), `JDBC.INI` from `\\i2s109-solidcrm\DBAMFG$\`,
`taspro7.ini` (both workstation and server-side copies), Pervasive installer packages on share.

---

## Physical network layout

```
┌─────────────────────────────────────────────────────────────────────────┐
│  Workstations (e.g. this machine, tsinclair.I2SYSTEMS)                  │
│                                                                          │
│  C:\ISTS\                                                                │
│    tp7runtime.exe (evoerp.exe)   ← TAS Pro 7 runtime                   │
│    StartEvo.exe                  ← .NET launcher                        │
│    WHOAMI.DBA                    ← per-workstation identity             │
│    taspro7.ini                   ← 3 key paths → \\i2s109-solidcrm\    │
│                                                                          │
│  Pervasive ODBC Client (32-bit)  ← connects via TCP:1583               │
│    DSN=DBA   → i2s109-solidcrm, DB=DBA                                 │
│    DSN="ABI DBA" → i2s109-solidcrm, DB=ABI                             │
│                                                                          │
│  Pervasive Workgroup Engine (local, NOT used in production)             │
│    C:\Program Files (x86)\Pervasive Software\PSQL\bin\w3dbsmgr.exe v11.31
│    C:\Program Files (x86)\Actian\PSQL\bin\w3dbsmgr.exe v12             │
│    (installed but no service running — for local snapshot testing only)  │
└────────────────────┬──────────────────────────────────────────────────┘
                     │ TCP/IP  port 1583
                     │ SMB  \\i2s109-solidcrm\DBAMFG$\
                     │
┌────────────────────▼──────────────────────────────────────────────────┐
│  Server: i2s109-solidcrm                                                │
│                                                                          │
│  Pervasive PSQL Server v11.30 — TCP port 1583                          │
│    Manages Btrieve databases (multiple named DBs, one per company)     │
│                                                                          │
│  Network shares:                                                         │
│    \\i2s109-solidcrm\DBAMFG$\   ← main EVO data + code share          │
│    \\i2s109-solidcrm\ISTS\      ← (legacy; also accessible)           │
│    \\i2s109-solidcrm\EVOReports\← report output share (some companies)│
│    \\i2s109-solidcrm\evo-ERP\   ← legacy EvoERP files                 │
│    \\i2s109-solidcrm\2004.1\    ← DBA Classic 2004.1 legacy           │
└───────────────────────────────────────────────────────────────────────┘
```

---

## Pervasive SQL server mode (confirmed from ODBC DSNs + installer packages)

EvoERP uses Pervasive PSQL in **Client/Server mode** — NOT workgroup mode.

**Evidence:**
- ODBC DSN for "DBA" and "ABI DBA" both use driver `Pervasive ODBC Client Interface`
  with `TransportHint=TCP` and `TCPPort=1583`. The "Client Interface" driver name
  means the ODBC layer connects through the Pervasive MicroKernel Requestor to a remote
  Pervasive Server, not to a local workgroup engine.
- `ServerName=i2s109-SOLIDCRM.1583` — Pervasive convention appends port to server name.
  The `.1583` suffix in the DSN ServerName field is how the Pervasive ODBC Client
  encodes the port (distinct from the `TCPPort` attribute, which is redundant but consistent).
- The Pervasive installer packages stored on the share confirm the server version:
  - `\\i2s109-solidcrm\DBAMFG$\Pervasive\PSQL-Server-11.30.030.000-win.exe` — the v11.30
    server installer, confirming the production server is Pervasive PSQL v11.30.
  - `PSQL-Client-11.30.030.000-win.x86.exe` — corresponding 32-bit client.
  - Patch files: `PSQLv11Patch_Client_x86.msp` and `PSQLv11Patch_Server_x64.msp` — so the
    server is x64, the client is 32-bit (matching TAS Pro 7's 32-bit runtime).

**Pervasive PSQL v11.30 server** runs on i2s109-solidcrm (Windows, x64).
**Pervasive PSQL Client v11.31** is installed on workstations (32-bit, matching TAS Pro 7).

---

## Pervasive databases — one per company (confirmed from JDBC.INI)

The file `\\i2s109-solidcrm\DBAMFG$\JDBC.INI` maps EvoERP company codes to Pervasive
database names and report output paths. This is read by the Java JDBC bridge (EvoPVT.jar /
T7jsql.RWN) for SQL-based features.

| Company (Btrieve suffix) | Pervasive DB name | Report output (Tree Destination) |
|--------------------------|-------------------|----------------------------------|
| BI2 (i2 Systems) | `EVOBI2` | `\\I2S109-SOLIDCRM\DBAMFG$\REPORTS` |
| BAT (AT) | `EVOBAT` | `\\I2S109-SOLIDCRM\DBAMFG$\REPORTS` |
| BAB (AB / ABI) | `abi` | `\\I2S109-SOLIDCRM\EVOREPORTS\` |
| B22 (company 22) | `evob22` | `\\I2S109-SOLIDCRM\EVOREPORTS\` |

All four entries: `Host=i2s109-solidcrm`, `Port=1583`.

**In addition**, from ODBC DSN registration:
- `DBQ=DBA` → Pervasive DB named `DBA` — the main shared EVO code/menus/config database.
- `DBQ=ABI` → Pervasive DB named `ABI` — the legacy American Backplane Inc. database
  (the predecessor company; DSN "ABI DBA").

So the full set of Pervasive databases on i2s109-solidcrm:

| DB name | Contents | Access method |
|---------|----------|---------------|
| `DBA` | Main EVO: DDF schema, programs, menus, config tables | TAS Pro native Btrieve + ODBC DSN=DBA |
| `ABI` | Legacy ABI data | ODBC DSN "ABI DBA" |
| `EVOBI2` | i2 Systems (BI2) company data | JDBC (EvoPVT.jar) |
| `EVOBAT` | Company AT data | JDBC (EvoPVT.jar) |
| `abi` | Company AB / ABI data | JDBC (EvoPVT.jar) |
| `evob22` | Company 22 data | JDBC (EvoPVT.jar) |

---

## Dual data access mechanisms

EvoERP uses two parallel paths to the same Btrieve data:

### Path 1 — TAS Pro native Btrieve (primary, all interactive operations)

```
tp7runtime.exe
  → TAS Pro Btrieve requestor (btrieve.dll / w32mkrde.dll)
  → TCP port 1583
  → Pervasive MicroKernel (Server mode) on i2s109-solidcrm
  → DBA database (DDF files in \\DBAMFG$\)
  → physical .B files in \\DBAMFG$\ (routed by FILELOC per company code)
```

Used for: **all interactive TAS Pro programs** — data entry, lookups, reports, menus.
Lock mode controlled by TAS Pro `open TABLE lock N/R/F` keyword.

### Path 2 — JDBC / Java SQL (MRP, exports, scheduled tasks)

```
TAS Pro program → SQLCALL / MYSQL_QUERY keyword
  → T7jsql.RWN (Java bridge) → EvoPVT.jar
  → JDBC → Pervasive PSQL SQL engine on i2s109-solidcrm:1583
  → Named database (EVOBI2, EVOBAT, etc. from JDBC.INI)
  → same physical .B files (accessed through PSQL SQL layer)
```

Used for: **SQL-based features** — MRP tree queries, catalog export (T7DEU),
scheduled reporting. EvoPVT.jar is the Java runtime bridge loaded by T7jsql.RWN.
Connection parameters come from JDBC.INI (Host/Port/Name per company).

---

## StartEvo.exe EVOADMIN DSN (from StartEvo.exe string analysis)

`StartEvo.exe` (the .NET launcher) references a DSN named `EVOADMIN` in its embedded
strings: `Server DSN=EVOADMIN;Host=<server>;Port=<port>`. This DSN is **not registered**
on this workstation (not found in ODBC registry). It is likely created at install time
or only on the server itself — used by StartEvo.exe for pre-launch license validation:

```sql
SELECT count(*) FROM tas_menus WHERE menu_name = ? AND program_name = ?
```

`tas_menus` is the Pervasive SQL name for the BKMENUSU menu configuration table.
The EVOADMIN DSN validates that a user/company combination is permitted to run a module
before `tp7runtime.exe` is even started.

---

## taspro7.ini path routing (the three key lines)

Every workstation's `C:\ISTS\taspro7.ini` controls where the TAS Pro runtime looks for
everything:

```ini
[Setup]
DataDictPath=\\I2S109-SOLIDCRM\DBAMFG$\   ← DDF schema location (+ data root)
DfltRunPrg=\\I2S109-SOLIDCRM\DBAMFG$\EvoERPmenu.rwn  ← entry-point program
DefaultPath=\\I2S109-SOLIDCRM\DBAMFG$\    ← base for all bare-name program chains
```

The server-side copy at `\\i2s109-solidcrm\DBAMFG$\taspro7.ini` has these blank
(`DataDictPath=` / `DefaultPath=`) — so TAS Pro resolves paths relative to current
directory when run directly on the server (used for server-side automated tasks).

---

## ARCHIVE.INI — per-company module archive dates

`\\i2s109-solidcrm\DBAMFG$\ARCHIVE.INI` stores the last archive date per module per
company. Section names use Btrieve file suffixes:

| Section | Module | Company |
|---------|--------|---------|
| `[SALES BI2]` | Sales Orders | I2 Systems |
| `[WORK ORDER BI2]` | Work Orders | I2 Systems |
| `[SALES BAB]` | Sales Orders | AB |
| `[WORK ORDER BAB]` | Work Orders | AB |
| `[WORK ORDER B99]` | Work Orders | 99 |
| `[WORK ORDER BAT]` | Work Orders | AT |
| `[SALES B22]`, `[WORK ORDER B22]` | Sales/WO | Company 22 |
| `[SALES BUU]`, `[WORK ORDER BUU]` | Sales/WO | Company UU |

Company 22 and UU are additional company codes not previously documented.
The `[Misc]` section (`ReUser`, `ReCo`, `ReMenu`) stores the last-used login state.

---

**Confidence: 88/100** — Pervasive server/client mode confirmed from ODBC DSN driver names
and installer packages; TCP port 1583 confirmed from two independent sources (DSN + JDBC.INI);
per-company Pervasive DB names confirmed from JDBC.INI; EVOADMIN DSN existence confirmed from
StartEvo.exe strings but not from ODBC registry (may be server-only); DDF relative path
assumption (for local snapshot) is inferred, not directly verified.
