# `.DFM` — Delphi Form (UI Layout)

Status: draft.

## Short answer

EVO `.DFM` files are **standard Borland Delphi form resource files** in
their **textual representation** (the kind saved when the IDE's
"Form → Text DFM" option is on). They are plaintext.

Sample: `../../samples/dfm/T7ARA.DFM`:1–15:
```
object EditForm1: TEditForm1
  Left = 460
  Top = 224
  Hint = 'C:\TASPRO7\DBA7\T7ARAE.DFM'
  BorderStyle = bsSingle
  Caption = 'New Screen'
  ClientHeight = 471
  ClientWidth = 666
  Color = clBtnFace
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -13
  Font.Name = 'Arial'
  Font.Style = []
  FormStyle = fsStayOnTop
  Icon.Data = {
    0000010001002020000001000800A80800001600000028000000200000004000
```

## Structure

Top-level:
```
object <InstanceName>: <ClassName>
  <property> = <value>
  ...
  object <Child>: <ChildClass>
    ...
  end
end
```

- Properties are `Name = Value` pairs.
- Nested `object ... end` blocks represent child controls.
- Binary blobs (icons, glyphs, bitmap data) are hex-encoded inside
  `{ ... }` braces, wrapped across lines.
- Strings are single-quoted (`'Arial'`).
- Sets are `[bold, italic]`.
- Enumerations are bare identifiers (`clBtnFace`, `DEFAULT_CHARSET`).

The form class names (`TEditForm1`) and property names come from the
TAS Pro 7 runtime's form-editor DLLs (`qtintf70.dll` / the evoerp
runtime's embedded component palette).

## Why this matters

- All UI layout is **readable**. I can enumerate every field, button,
  grid column, and group box in every form without reverse-engineering.
- The `Hint =` property often retains the **original developer path**
  (e.g. `C:\TASPRO7\DBA7\T7ARAE.DFM` in `T7ARA.DFM`:4) — a useful
  breadcrumb for matching forms back to their original source layout.
- `.DFM` typically pairs 1:1 with an `.RWN` (compiled behavior) of the
  same base name. Example: `T7ARA.DFM` ↔ a related `T7ARA*.RWN`. The
  form holds layout; the RWN holds the TAS Pro logic that drives it.

## Tooling ideas (for later scripts)

- A Python parser can walk the `object … end` tree and emit JSON, so
  we can diff UI between modules or render a field inventory.
- Icon/glyph blobs can be decoded (Windows `.ico`/`.bmp` payloads) to
  recover the icons for documentation.

## Known property families

These are what I've seen so far — catalog will grow:

- Form: `Left`, `Top`, `BorderStyle`, `Caption`, `ClientHeight/Width`,
  `Color`, `Font.*`, `FormStyle`, `Icon.Data`, `OldCreateOrder`.
- Standard VCL controls: `TLabel`, `TEdit`, `TButton`, `TPanel`,
  `TGroupBox`, `TDBGrid`.
- Likely TAS-specific controls (to confirm): `TTASEdit`, `TTASGrid`,
  any `T7*` prefixed components.

## Verifying

- Delphi form format spec: Embarcadero's "About the Form File Format"
  (the text DFM is the Pascal `const ... = (class ... )` serialization
  of VCL's `TComponent.WriteComponent`). This is well-known and stable
  across Delphi 2 – Delphi XE versions. No surprises expected.

## Things still to verify

- Which Delphi/VCL version the runtime embeds (hints at what controls
  are available). The DLL list (`qtintf70.dll` = Qt 3 for Borland's
  CLX) implies **Delphi 6–7** era. Evoerp.exe's embedded form classes
  will confirm this if I peek at the string table later.
