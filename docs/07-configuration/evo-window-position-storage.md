# EVO Window Position & Size Storage

Status: verified

---

## Summary

EvoERP stores the position and size of every form/dialog window in the Windows registry
under the current user's hive. When a form is closed, TAS Pro 7 writes the window
geometry. When the same form is opened again, TAS Pro 7 reads those values and restores
the window to the same position and size.

---

## Registry Location

```
HKEY_CURRENT_USER\Software\Addsum\TAS Pro 7\Form Loc Size Storage
```

- One **subkey per form**, named `<PROGRAM>-<FORMNAME>`.
  - `PROGRAM` = the RWN filename without extension (e.g. `T7WOD`, `T7INA`)
  - `FORMNAME` = the Delphi form class name (e.g. `T7WOD`, `T7RTMVALID`)
  - Example: `T7WOD-T7WOD`, `T7WOD-T7RTMVALID`, `T7INA-T7INA`
- As of 2026-08-18, there are **55 subkeys** on the test machine.
- Each subkey contains four DWORD values: `Top`, `Left`, `Width`, `Height`.
- A fifth value (`WindowState` or similar) may also be present.

---

## Value Format

All four values are stored as **DWORD (unsigned 32-bit integer)**.

Windows virtual screen coordinates can be **negative** on multi-monitor setups where a
secondary monitor sits to the left of or above the primary monitor. When EVO stores a
negative coordinate, it wraps around 2³² and appears as a large positive number (e.g.
`4294966555` = `−741` signed). This is normal Windows behavior, not corruption.

**Reading a stored coordinate:**
```powershell
$raw   = (Get-ItemProperty $regPath).Top   # arrives as uint/int64 in PS
$bytes = [BitConverter]::GetBytes([uint32]($raw -band 0xFFFFFFFF))
$signed = [BitConverter]::ToInt32($bytes, 0)   # gives the true signed coordinate
```

**Writing a coordinate back:**
```powershell
$bytes    = [BitConverter]::GetBytes([int32]$signed)
$unsigned = [BitConverter]::ToUInt32($bytes, 0)
Set-ItemProperty -Path $regPath -Name "Top" -Value $unsigned -Type DWord
```

---

## Confirmed Behavior

| Observation | How verified |
|-------------|-------------|
| Registry key confirmed present | Read directly 2026-08-18 |
| 55 subkeys present | Get-ChildItem count |
| Top/Left/Width/Height values confirmed | Read and compared to live window |
| Stored coordinates match live window coordinates exactly | T7INA-T7INA: stored Top=−741 Left=−125 = live Top=−741 Left=−125 |
| Negative coords stored as unsigned DWORD wrapping | Bit-level comparison |
| EVO reads this key on form open | Inferred from position restoration behavior |
| EVO writes this key on form close | Inferred; registry values match form positions |

---

## Additional Storage Locations

### Per-User INI file

```
C:\ISTS\EvoSettings.INI   (or a user-named copy, e.g. MARKZ.INI)
```

Stores user preferences such as default printer, toolbar state, module settings, and
email configuration. Does **not** store window geometry.

### PrintSettings

```
HKEY_CURRENT_USER\Software\Addsum\TAS Pro 7\PrintSettings
```

Stores `ZoomSetting` and `ZoomPercent` for the print preview. Separate from form geometry.

---

## The Off-Screen Dialog Problem

**Symptom:** EVO appears to freeze after clicking Print. No dialog visible. Print queue empty.

**Cause:** The "Save Print Output As" shell file-picker dialog is spawned relative to
its parent EVO form. If the parent form has a stored position on a monitor that no
longer exists (or has different resolution/arrangement), the child dialog opens in
virtual coordinate space that maps to no physical display.

**Immediate fix (live session):**
1. Enumerate all windows owned by the `evoerp` process using `EnumWindows`.
2. Find the dialog by title (`Save Print Output As`).
3. Confirm it is truly off-screen (e.g. `Top < 0` and `Top < monitor.Top`).
4. Use `SetWindowPos` to move it to visible coordinates.

**Permanent fix:**
Update the parent form's stored `Top`/`Left` in the registry to a position that is
within the bounds of currently connected monitors. The child dialog will then open
in a valid location on the next print.

**Tool:** See `programs/evo-window-manager/EvoWindowManager.ps1`.

---

## Key Naming Pattern

| Window title prefix | Registry key prefix |
|---------------------|---------------------|
| `IN-A` | `T7INA-*` |
| `IN-B` | `T7INB-*` |
| `WO-A` | `T7WOA-*` |
| `WO-D` | `T7WOD-*` |
| `WO-G` | `T7WOG-*` |
| `SO-A` | `T7SOA-*` |
| `AP-A` | `T7APA-*` |
| `AR-A` | `T7ARA-*` |
| `GL-C` | `T7GLC-*` |
| `WC-A` | `T7WCA-*` |
| `Evo ~ ERP` (main menu) | `EVOERPMENU-*` |
| ReportBuilder print dialog | `*-T7RTMVALID` |
| TAS Pro 7 print dialog | `T7PRINT-PRINTTLL` |

A single program (e.g. `T7WOD`) may have multiple subkeys — one for its main form
and one for each child form it spawns (report validator, sub-dialogs, etc.).
