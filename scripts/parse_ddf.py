"""
Parse Pervasive DDF (Btrieve data-dictionary) files into CSV/JSON.

Pervasive v6+ DDF record layouts (canonical, documented publicly):

  FILE.DDF  — X$File
      Xf$Id        smallint  offset 0   size 2
      Xf$Name      char[20]  offset 2   size 20
      Xf$Loc       char[64]  offset 22  size 64
      Xf$Flags     smallint  offset 86  size 2
      Xf$Reserved  char[10]  offset 88  size 10
      (record length = 98 bytes)

  FIELD.DDF — X$Field
      Xe$Id        smallint  offset 0    size 2   (unique field id across all files)
      Xe$File      smallint  offset 2    size 2   (FK -> X$File.Xf$Id)
      Xe$Name      char[20]  offset 4    size 20
      Xe$DataType  byte      offset 24   size 1
      Xe$Offset    smallint  offset 25   size 2
      Xe$Size      smallint  offset 27   size 2
      Xe$Dec       byte      offset 29   size 1
      Xe$Flags     smallint  offset 30   size 2
      (record length = 32 bytes)

  INDEX.DDF — X$Index
      Xi$File      smallint  offset 0    size 2
      Xi$Field     smallint  offset 2    size 2
      Xi$Number    byte      offset 4    size 1
      Xi$Part      byte      offset 5    size 1
      Xi$Flags     smallint  offset 6    size 2
      (record length = 8 bytes)

The Btrieve file itself has a file-control-section header beginning
'FC' and pages of `page_size` bytes; pages after the header contain
records but also page headers. Instead of reconstructing the B-tree,
we simply scan for records by heuristics: a valid-looking name run of
ASCII letters followed by spaces at the expected offset.

DataType codes (Xe$DataType):
   0 = STRING (char)       1 = INTEGER (signed 2 or 4)
   2 = FLOAT               3 = DATE
   4 = TIME                5 = DECIMAL
   6 = MONEY               7 = LOGICAL
   8 = NUMERIC (N-type)    9 = BFLOAT4
  10 = LSTRING            11 = ZSTRING
  14 = UNSIGNED BINARY    15 = AUTOINCREMENT
  16 = BIT                17 = NUMERICSTS
  18 = NUMERICSA          20 = CURRENCY
  21 = TIMESTAMP          27 = WSTRING (unicode)

Usage:
    python parse_ddf.py file.ddf   -> CSV to stdout
    python parse_ddf.py field.ddf  -> CSV to stdout
    python parse_ddf.py index.ddf  -> CSV to stdout
"""
from __future__ import annotations
import csv
import struct
import sys
from pathlib import Path

DATA_TYPE_NAMES = {
    0: "STRING", 1: "INTEGER", 2: "FLOAT", 3: "DATE", 4: "TIME",
    5: "DECIMAL", 6: "MONEY", 7: "LOGICAL", 8: "NUMERIC",
    9: "BFLOAT4", 10: "LSTRING", 11: "ZSTRING", 14: "UBINARY",
    15: "AUTOINC", 16: "BIT", 17: "NUMSTS", 18: "NUMSA",
    20: "CURRENCY", 21: "TIMESTAMP", 27: "WSTRING",
}


def _clean(b: bytes) -> str:
    return b.split(b"\x00", 1)[0].rstrip().decode("latin-1", errors="replace")


def parse_file_ddf(data: bytes):
    """Scan for 98-byte records that look valid."""
    rec_size = 98
    rows = []
    # Skip the first 4KB which is the header + FCS
    for off in range(0, len(data) - rec_size, 1):
        # heuristic: bytes 2..22 should be mostly printable upper-case letters
        name_bytes = data[off+2:off+22]
        loc_bytes = data[off+22:off+86]
        if not name_bytes[:1].isalpha() or not name_bytes[:1].isupper():
            continue
        # Name must have at least 3 leading alpha bytes
        if not all(b and (chr(b).isalnum() or b == 0x20 or b == ord('$') or b == ord('_')) for b in name_bytes[:8]):
            continue
        name = _clean(name_bytes)
        loc  = _clean(loc_bytes)
        if not name or not loc:
            continue
        # name must look like a table: uppercase, letters+digits, 3-20 chars
        if not (3 <= len(name) <= 20 and name.replace("$", "").replace("_", "").isalnum()):
            continue
        if not (loc.lower().endswith(".ddf") or loc.lower().endswith(".b") or loc.lower().endswith(".btr")
                or loc.upper().endswith(".B") or ".B" in loc.upper()):
            continue
        fid, = struct.unpack_from("<H", data, off)
        flags, = struct.unpack_from("<H", data, off+86)
        rows.append((fid, name, loc, flags))

    # Dedupe by (fid, name)
    seen = set(); out = []
    for r in rows:
        k = (r[0], r[1])
        if k in seen: continue
        seen.add(k); out.append(r)
    out.sort()
    return out


def parse_field_ddf(data: bytes):
    """Scan for 32-byte field records."""
    rec_size = 32
    rows = []
    for off in range(0, len(data) - rec_size, 1):
        name_bytes = data[off+4:off+24]
        if not name_bytes[:1].isalpha() or not name_bytes[:1].isupper():
            continue
        if not all(chr(b).isprintable() for b in name_bytes if b != 0):
            continue
        name = _clean(name_bytes)
        if not (2 <= len(name) <= 20):
            continue
        if not name.replace("_", "").replace("$", "").replace(".", "").replace("-", "").replace("#", "").isalnum():
            continue
        field_id, file_id = struct.unpack_from("<HH", data, off)
        data_type = data[off+24]
        offset_ = struct.unpack_from("<H", data, off+25)[0]
        size    = struct.unpack_from("<H", data, off+27)[0]
        dec     = data[off+29]
        flags   = struct.unpack_from("<H", data, off+30)[0]
        # Filter nonsense
        if data_type > 30 or size > 4000 or size == 0:
            continue
        if offset_ > 8000:
            continue
        if file_id == 0 or file_id > 700:
            continue
        if field_id == 0 or field_id > 65000:
            continue
        if dec > 20:
            continue
        # Field name must not contain junk chars that aren't typical
        if not all(c.isalnum() or c in "_$.#-" for c in name):
            continue
        rows.append((file_id, field_id, name, data_type, offset_, size, dec, flags))
    # Dedupe by (file_id, name) — field_id is less reliable
    seen = set(); out = []
    for r in rows:
        k = (r[0], r[2])
        if k in seen: continue
        seen.add(k); out.append(r)
    out.sort()
    return out


def main():
    if len(sys.argv) < 2:
        print(__doc__); return 2
    path = Path(sys.argv[1])
    data = path.read_bytes()
    name = path.name.lower()
    w = csv.writer(sys.stdout)
    if name.startswith("file."):
        rows = parse_file_ddf(data)
        w.writerow(["file_id", "name", "location", "flags"])
        for r in rows:
            w.writerow(r)
        print(f"# {len(rows)} tables", file=sys.stderr)
    elif name.startswith("field."):
        rows = parse_field_ddf(data)
        w.writerow(["file_id", "field_id", "name", "type_code", "type", "offset", "size", "dec", "flags"])
        for r in rows:
            w.writerow([r[0], r[1], r[2], r[3], DATA_TYPE_NAMES.get(r[3], '?'), r[4], r[5], r[6], r[7]])
        print(f"# {len(rows)} fields", file=sys.stderr)
    elif name.startswith("index."):
        # INDEX.DDF records: 8 bytes each
        #   Xi$File      smallint  offset 0
        #   Xi$Field     smallint  offset 2
        #   Xi$Number    smallint  offset 4
        #   Xi$Part      smallint  offset 6
        #   Xi$Flags     smallint  offset 8   (some versions 9 bytes total)
        rec_size = 8
        rows = []
        for off in range(0, len(data) - rec_size, 1):
            file_id, field_id, num, part = struct.unpack_from("<HHHH", data, off)
            if file_id == 0 or file_id > 700: continue
            if field_id == 0 or field_id > 65000: continue
            if num > 50 or part > 50: continue
            rows.append((file_id, field_id, num, part))
        seen = set(); out = []
        for r in rows:
            k = r[:4]
            if k in seen: continue
            seen.add(k); out.append(r)
        out.sort()
        w.writerow(["file_id", "field_id", "index_num", "part_num"])
        for r in out: w.writerow(r)
        print(f"# {len(out)} index parts", file=sys.stderr)
    else:
        print(f"Unsupported DDF: {name}")
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
