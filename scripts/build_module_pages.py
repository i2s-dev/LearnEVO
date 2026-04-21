"""
For each major EVO module, auto-build a docs page that joins:
- menu codes (samples/menu_codes.csv)
- DB tables       (samples/ddf/schema.json, filtered by table prefix)
- UI forms        (samples/dfm_parsed/dfm_summary.csv, filtered by file prefix)
- known source    (samples/src/*.src if matching)

Outputs one .md per module under docs/03-modules/<slug>/README.md
"""
import csv
import json
import re
from pathlib import Path

BASE = Path(__file__).parent.parent
DOCS = BASE / "docs" / "03-modules"
SCHEMA = json.loads((BASE / "samples" / "ddf" / "schema.json").read_text())
MENU_ROWS = list(csv.DictReader((BASE / "samples" / "menu_codes.csv").open()))
DFM_ROWS = list(csv.DictReader((BASE / "samples" / "dfm_parsed" / "dfm_summary.csv").open()))

MODULES = [
    # (module_code, slug, title, table_prefixes, form_prefixes)
    ("AR", "ar-accounts-receivable", "Accounts Receivable", ["BKAR", "BKAB", "BKART"], ["T7AR", "T6AR", "BKAR"]),
    ("AP", "ap-accounts-payable",    "Accounts Payable",    ["BKAP", "BKAB"],          ["T7AP", "T6AP", "BKAP"]),
    ("IN", "in-inventory",           "Inventory",           ["BKIC", "MTIC"],          ["T7IN", "T6IN", "BKIN"]),
    ("SO", "so-sales-orders",        "Sales Orders",        ["BKSO"],                  ["T7SO", "T6SO", "BKSO"]),
    ("PO", "po-purchase-orders",     "Purchase Orders",     ["BKPO", "BKAPPO", "BKAPAPO", "BKAPHPO"], ["T7PO", "T6PO", "BKPO"]),
    ("WO", "wo-work-orders",         "Work Orders",         ["WO", "WORK"],            ["T7WO", "T6WO", "BKWO"]),
    ("GL", "gl-general-ledger",      "General Ledger",      ["BKGL"],                  ["T7GL", "T6GL", "BKGL"]),
    ("BM", "bm-bill-of-materials",   "Bill of Materials",   ["BKBM"],                  ["T7BM", "T6BM", "BKBM"]),
    ("MR", "mr-mrp",                 "MRP (Material Requirements Planning)", ["BKMR", "MTMR"],   ["T7MR", "T6MR", "BKMR"]),
    ("PR", "pr-payroll",             "Payroll",             ["BKPR"],                  ["T7PR", "T6PR", "BKPR"]),
    ("DC", "dc-data-collection",     "Data Collection (Shop Floor)", ["BKDC"],         ["T7DC", "T6DC", "EVODC"]),
    ("QC", "qc-quality-control",     "Quality Control",     ["BKQC"],                  ["T7QC", "T6QC"]),
    ("JC", "jc-job-costing",         "Job Costing",         ["WOHLABOR", "BKJC", "WOLABOR"], ["T7JC", "T6JC"]),
    ("CS", "cs-commission-system",   "Commission System",   ["BKCS", "BKPR"],          ["T7CS", "T6CS"]),
    ("ES", "es-estimating",          "Estimating",          ["BKES", "ESTSUM"],        ["T7ES", "T6ES"]),
    ("SR", "sr-service-repair",      "Service / Repair",    ["BKSR", "BKRM"],          ["T7SR", "T6SR"]),
    ("PI", "pi-physical-inventory",  "Physical Inventory",  ["BKPI"],                  ["T7PI", "T6PI"]),
    ("SH", "sh-shipping",            "Shipping",            ["BKSH"],                  ["T7SH", "T6SH"]),
    ("ED", "ed-edi",                 "EDI",                 ["BKED"],                  ["T7ED", "T6ED"]),
    ("SM", "sm-system-manager",      "System Manager / Setup", ["BKSY", "BKYS", "AHSY"], ["T7SM", "T6SM", "EVO"]),
]


def tables_for(prefixes):
    out = []
    for t, info in sorted(SCHEMA.items()):
        for p in prefixes:
            if t.startswith(p):
                out.append((t, info))
                break
    return out


def forms_for(prefixes):
    out = []
    for r in DFM_ROWS:
        for p in prefixes:
            if r["file"].upper().startswith(p):
                out.append(r)
                break
    return sorted(out, key=lambda r: r["file"])


def menu_for(mod):
    return [r for r in MENU_ROWS if r["module"] == mod]


def write_module(mod, slug, title, table_prefixes, form_prefixes):
    tables = tables_for(table_prefixes)
    forms = forms_for(form_prefixes)
    menu = menu_for(mod)

    out = DOCS / slug / "README.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        f"# {title} ({mod})",
        "",
        "Status: verified (auto-generated from the extracted schema, menu-code dump, and DFM inventory).",
        "",
        f"- **Module code**: `{mod}`",
        f"- **Tables**: {len(tables)} (prefixes {', '.join('`'+p+'`' for p in table_prefixes)})",
        f"- **UI forms**: {len(forms)} (prefixes {', '.join('`'+p+'`' for p in form_prefixes)})",
        f"- **Menu operations**: {len(menu)}",
        "",
    ]

    if menu:
        lines += [
            "## Menu operations",
            "",
            "| Code | Operation | Legacy module file(s) |",
            "| ---- | --------- | --------------------- |",
        ]
        for m in sorted(menu, key=lambda r: r["code"]):
            lines.append(f"| `{m['code']}` | {m['description']} | {m['sources']} |")
        lines.append("")

    if forms:
        lines += [
            f"## UI forms ({len(forms)})",
            "",
            "| DFM file | Caption | fields | controls | tabs |",
            "| -------- | ------- | -----: | -------: | ---: |",
        ]
        for r in forms:
            cap = (r["caption"] or "").replace("|", "\\|")[:70]
            lines.append(f"| `{r['file']}` | {cap} | {r['field_count']} | {r['total_controls']} | {r['tab_count']} |")
        lines.append("")

    if tables:
        lines += [
            f"## Database tables ({len(tables)})",
            "",
            "Full field details are in `../../../samples/ddf/schema.md` (see per-table heading).",
            "",
            "| Table | File on disk | Fields | Key fields (first 3) |",
            "| ----- | ------------ | -----: | -------------------- |",
        ]
        for t, info in tables:
            f3 = ", ".join(f"`{f['name']}`" for f in info["fields"][:3])
            lines.append(f"| **{t}** | `{info['location']}` | {len(info['fields'])} | {f3} |")
        lines.append("")

    lines += [
        "## Notes & open questions",
        "",
        "- *(populated per-module manually as deeper reading happens.)*",
        "",
    ]
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {out}  (menu={len(menu)}, forms={len(forms)}, tables={len(tables)})")


def main():
    for args in MODULES:
        write_module(*args)


if __name__ == "__main__":
    main()
