"""
Join parsed FILE.DDF + FIELD.DDF (+ INDEX.DDF optional) into a
per-table schema Markdown file and JSON.

Reads from samples/ddf/fields.csv (produced by parse_ddf.py) and the
already-parsed file index.

Outputs:
    samples/ddf/schema.json     - full JSON
    samples/ddf/schema.md       - human-readable Markdown
"""
import csv
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).parent
BASE = HERE.parent
SAMPLES = BASE / "samples" / "ddf"


def parse_file_ddf():
    """Run parse_ddf.py on file.ddf and return dict file_id -> (name, loc)."""
    out = subprocess.check_output(
        ["python", str(HERE / "parse_ddf.py"), str(SAMPLES / "file.ddf")],
        text=True,
    )
    files = {}
    for row in csv.DictReader(out.splitlines()):
        files[int(row["file_id"])] = (row["name"], row["location"])
    return files


def load_fields():
    """Read already-parsed fields.csv."""
    rows = []
    with open(SAMPLES / "fields.csv", newline="") as f:
        for r in csv.DictReader(f):
            rows.append(r)
    return rows


def main():
    files = parse_file_ddf()
    fields = load_fields()

    by_file = {}
    for r in fields:
        fid = int(r["file_id"])
        by_file.setdefault(fid, []).append(r)

    # JSON output
    schema = {}
    for fid, (tname, loc) in sorted(files.items()):
        flds = sorted(by_file.get(fid, []), key=lambda r: int(r["offset"]))
        schema[tname] = {
            "file_id": fid,
            "location": loc,
            "fields": [
                {
                    "name": r["name"],
                    "type": r["type"],
                    "offset": int(r["offset"]),
                    "size": int(r["size"]),
                    "dec": int(r["dec"]),
                    "flags": int(r["flags"]),
                }
                for r in flds
            ],
        }

    (SAMPLES / "schema.json").write_text(json.dumps(schema, indent=2))

    # Markdown output — one section per table, sorted
    md = ["# EvoERP Complete Schema (auto-generated)",
          "",
          f"Source: parsed `\\\\I2S109-SOLIDCRM\\DBAMFG$\\Default\\FILE.DDF` + `FIELD.DDF`.",
          f"Tables: {len(files)}  Fields: {sum(len(v['fields']) for v in schema.values())}",
          ""]
    for tname, info in sorted(schema.items()):
        md.append(f"## {tname}  ({info['location']})")
        flds = info["fields"]
        if not flds:
            md.append("_(no fields extracted — table may be large or use nonstandard layout)_")
            md.append("")
            continue
        md.append("")
        md.append("| # | Name | Type | Offset | Size | Dec | Flags |")
        md.append("|---|------|------|--------|------|-----|-------|")
        for i, f in enumerate(flds, 1):
            md.append(
                f"| {i} | `{f['name']}` | {f['type']} | {f['offset']} | {f['size']} | "
                f"{f['dec']} | 0x{f['flags']:04x} |"
            )
        md.append("")
    (SAMPLES / "schema.md").write_text("\n".join(md))
    print(f"Wrote schema.json + schema.md ({len(schema)} tables, "
          f"{sum(len(v['fields']) for v in schema.values())} fields)")


if __name__ == "__main__":
    sys.exit(main())
