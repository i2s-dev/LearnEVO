"""
Bulk-parse all DFM files on the EVO network share and produce summary CSV + per-module JSON.

Reads only — never writes to the share.

Usage:
    python bulk_parse_dfm.py
    python bulk_parse_dfm.py --detail <pattern>
"""
import csv
import glob
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent
OUT = HERE.parent / "samples" / "dfm_parsed"
OUT.mkdir(exist_ok=True, parents=True)

sys.path.insert(0, str(HERE))
from parse_dfm import parse, summary  # type: ignore


SHARE_DFMS = [
    r"\\I2S109-SOLIDCRM\DBAMFG$",
    r"C:\ISTS\DFM",
]


def iter_dfms():
    seen = set()
    for root in SHARE_DFMS:
        for ext in ("*.DFM", "*.dfm"):
            for p in glob.glob(str(Path(root) / ext)):
                key = Path(p).name.upper()
                if key in seen:
                    continue
                seen.add(key)
                yield Path(p)


_PFX = re.compile(
    r"^(T7[A-Z]{2}|T6[A-Z]{2}|BK[A-Z]{2}|MT[A-Z]{2}|J7[A-Z]{2}|HT6[A-Z]{2}|"
    r"EvoDC|EvoNote|EvoSched|EvoService|EvoFNO|EvoERP|Evo|IS|AUTO|ACT|"
    r"[A-Z]{2,4})", re.IGNORECASE,
)

def classify(name: str) -> str:
    m = _PFX.match(name)
    return (m.group(1).upper() if m else "?")


def main():
    rows = []
    errors = []
    for i, p in enumerate(iter_dfms()):
        try:
            tree = parse(p.read_text(encoding="latin-1"))
            s = summary(tree)
            rows.append({
                "file": p.name,
                "prefix": classify(p.stem),
                "caption": s["caption"],
                "root_class": s["root_class"],
                "field_count": len(s["field_names"]),
                "enter_count": s["class_counts"].get("TTASENTER", 0),
                "num_count": s["class_counts"].get("TTASNumEnter", 0),
                "date_count": s["class_counts"].get("TTASDateEdit", 0),
                "combo_count": s["class_counts"].get("TTASComboEnter", 0) + s["class_counts"].get("TTASComboBox", 0),
                "check_count": s["class_counts"].get("TTASCheckBox", 0),
                "tab_count": s["class_counts"].get("TTabSheet", 0),
                "grid_count": s["class_counts"].get("TTASDataGrid", 0),
                "total_controls": sum(s["class_counts"].values()),
            })
        except Exception as e:
            errors.append((str(p), str(e)))
        if (i + 1) % 100 == 0:
            print(f"parsed {i+1}", file=sys.stderr)

    rows.sort(key=lambda r: (r["prefix"], r["file"]))
    csv_out = OUT / "dfm_summary.csv"
    with csv_out.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        for r in rows:
            w.writerow(r)

    # Per-prefix counts
    by_prefix = {}
    for r in rows:
        by_prefix.setdefault(r["prefix"], []).append(r)

    with (OUT / "by_prefix.txt").open("w", encoding="utf-8") as f:
        f.write(f"# DFM forms parsed: {len(rows)}  errors: {len(errors)}\n\n")
        for pfx in sorted(by_prefix):
            bucket = by_prefix[pfx]
            f.write(f"## {pfx} ({len(bucket)} forms)\n")
            for r in bucket:
                cap = (r["caption"] or "")[:50]
                f.write(f"  {r['file']:<30} {cap:<52}  fields={r['field_count']:<3} ctrls={r['total_controls']:<4} tabs={r['tab_count']}\n")
            f.write("\n")

    with (OUT / "errors.txt").open("w", encoding="utf-8") as f:
        for p, e in errors:
            f.write(f"{p}\t{e}\n")

    print(f"OK: {len(rows)} forms  err: {len(errors)}  out={OUT}")


if __name__ == "__main__":
    main()
