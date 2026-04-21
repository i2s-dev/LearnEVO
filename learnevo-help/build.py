"""
Build the LearnEVO help-browser data files.

Reads:
  - content/topics.py           — hand-authored conceptual pages
  - content/recipes.py          — step-by-step walkthroughs
  - content/modules.py          — module narratives
  - content/glossary.py         — terms
  - ../samples/menu_codes.csv   — 554 menu codes
  - ../samples/chm/menu_help.csv — 636 help-topic titles
  - ../samples/master_index.csv — merged 759-op index
  - ../samples/dfm_parsed/dfm_summary.csv — 1,109 forms
  - ../samples/ddf/schema.json  — 659-table DB schema
  - ../samples/menu_to_form.csv — menu→form xref
  - ../samples/rtm_callers.csv  — RTM→caller xref

Writes:
  - data/pages.json        — every page, keyed by id
  - data/search.json       — prebuilt inverted index
  - data/nav.json          — sidebar tree
  - data/keywords.json     — keyword → page map
"""
import csv
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent
BASE = HERE.parent
sys.path.insert(0, str(HERE / "content"))

from topics import TOPICS
from recipes import RECIPES
from modules import MODULE_NARRATIVES
from glossary import GLOSSARY

SAMPLES = BASE / "samples"

# ---------------------------------------------------------------------- #
# Load raw data
# ---------------------------------------------------------------------- #

def load_csv(path):
    with open(path, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))

menu_rows = load_csv(SAMPLES / "menu_codes.csv")
help_rows = load_csv(SAMPLES / "chm" / "menu_help.csv")
master_rows = load_csv(SAMPLES / "master_index.csv")
dfm_rows = load_csv(SAMPLES / "dfm_parsed" / "dfm_summary.csv")
menu_to_form = {r['code']: r['dfms'] for r in load_csv(SAMPLES / "menu_to_form.csv")}
rtm_callers = {r['rtm']: r for r in load_csv(SAMPLES / "rtm_callers.csv")}

schema = json.loads((SAMPLES / "ddf" / "schema.json").read_text())

# Build a menu→description map from all sources
menu_desc = {}
menu_src = {}
for r in menu_rows:
    menu_desc[r['code']] = r['description']
    menu_src[r['code']] = r.get('sources', '')
for r in help_rows:
    if r['code'] not in menu_desc:
        menu_desc[r['code']] = r['help_title']

# Build module→list-of-codes map
module_menus = {}
for code in menu_desc:
    mod = code.split('-')[0]
    module_menus.setdefault(mod, []).append(code)

# Build module→list-of-forms map
module_forms = {}
form_to_caption = {}
for r in dfm_rows:
    name = r['file'].upper().replace('.DFM', '')
    m = re.match(r'^(T7|T6|BK)([A-Z]{2})', name)
    if m:
        mod = m.group(2)
        module_forms.setdefault(mod, []).append(r['file'])
    form_to_caption[r['file']] = r['caption']

# Module → list-of-tables
module_tables = {}
for tname, info in schema.items():
    m = re.match(r'^(BK|MT)([A-Z]{2})', tname)
    if m:
        mod = m.group(2)
        module_tables.setdefault(mod, []).append(tname)

# ---------------------------------------------------------------------- #
# Normalize wiki-links in markdown
# ---------------------------------------------------------------------- #

WIKI_LINK_RE = re.compile(r'\[\[([^\]|]+)(?:\|([^\]]+))?\]\]')

# All page IDs that will exist — used to auto-rewrite bare table / form
# names like [[BKARCUST]] to [[table-BKARCUST]] if the bare ID isn't a page.
_SCHEMA_TABLES = None
_DFM_NAMES = None
def _all_table_names():
    global _SCHEMA_TABLES
    if _SCHEMA_TABLES is None:
        _SCHEMA_TABLES = set(schema.keys())
    return _SCHEMA_TABLES

def _glossary_pid(term):
    """Canonical page id for a glossary term — must match the construction
    used when glossary pages are generated (see section 7 below). Do NOT
    strip trailing dashes — the generator doesn't, and the pid must match
    byte-for-byte."""
    return "glossary-" + re.sub(r'[^a-z0-9]+', '-', term.lower())

# Case-insensitive lookup: normalized term → canonical glossary pid.
_GLOSSARY_TERMS = {term.lower(): _glossary_pid(term) for term, *_ in GLOSSARY}

def _canonicalize(pid):
    """If pid is a bare glossary term, rewrite to its canonical glossary pid.
    Otherwise return pid unchanged."""
    if pid.startswith(('table-', 'menu-', 'module-', 'form-', 'recipe-', 'glossary-')):
        return pid
    low = pid.lower()
    if low in _GLOSSARY_TERMS:
        return _GLOSSARY_TERMS[low]
    return pid

def convert_wiki_links(md):
    """Convert [[page-id]] or [[page-id|label]] to relative links understood by app.
    If `page-id` looks like a bare table name or glossary term, auto-prefix it.
    """
    def repl(m):
        pid = m.group(1)
        label = m.group(2) or pid
        # Auto-prefix bare table names
        if pid in _all_table_names() and not pid.startswith(('table-', 'menu-', 'module-', 'form-', 'recipe-', 'glossary-')):
            return f'[{label}](#table-{pid})'
        # Auto-redirect bare glossary terms to glossary-<slug>
        return f'[{label}](#{_canonicalize(pid)})'
    return WIKI_LINK_RE.sub(repl, md)

# ---------------------------------------------------------------------- #
# Build pages
# ---------------------------------------------------------------------- #

pages = {}

# 1. Topics
for pid, title, section, body, keywords in TOPICS:
    pages[pid] = {
        "id": pid,
        "title": title,
        "section": section,
        "kind": "topic",
        "body": convert_wiki_links(body),
        "keywords": keywords,
    }

# 2. Recipes
for pid, title, module, route, body, keywords in RECIPES:
    pages[pid] = {
        "id": pid,
        "title": title,
        "section": "Recipes",
        "kind": "recipe",
        "module": module,
        "route": route,
        "body": convert_wiki_links(body),
        "keywords": keywords,
    }

# 3. Module pages (combine narrative + auto-generated data)
MODULE_NAMES = {
    "AR": "Accounts Receivable",    "AP": "Accounts Payable",
    "IN": "Inventory",               "SO": "Sales Orders",
    "PO": "Purchase Orders",         "WO": "Work Orders",
    "GL": "General Ledger",          "BM": "Bill of Materials",
    "MR": "MRP",                     "PR": "Payroll",
    "DC": "Data Collection",         "QC": "Quality Control",
    "JC": "Job Costing",             "CS": "Commission System",
    "ES": "Estimating",              "SR": "Service / Repair",
    "PI": "Physical Inventory",      "SH": "Shipping",
    "ED": "EDI",                     "SM": "System Manager",
    "AM": "Archive / Maintenance",   "AD": "Admin Defaults",
    "RF": "Request For Quote",       "RO": "Routings",
    "RM": "RMA",                     "LC": "Lot Control",
    "SC": "Serial Control",          "UT": "Utilities",
    "LW": "Labor/Work Schedule",     "FO": "Form Output",
    "SA": "Sales Analysis",          "SB": "Subcontract",
    "LM": "Label Management",        "SD": "System Defaults",
    "MM": "Multi-Module",            "PL": "Plotting",
    "IS": "Information System",      "DI": "Dispatch",
    "DE": "Delivery/EDI",            "AH": "Audit History",
    "AN": "Analysis",                "AT": "Admin Tools",
    "AV": "Approvals",               "BO": "BOM utilities",
    "CG": "Config",                  "CT": "Counters",
    "CU": "Customer utils",          "DA": "Data utils",
    "DF": "Define",                  "DL": "Download",
    "DO": "Document",                "DP": "Deposit",
    "DR": "Drill down",              "DS": "Disk",
    "DT": "Date tools",              "DX": "DX",
    "EA": "Email A",                 "EB": "Email B",
    "EC": "Email C",                 "ER": "Errors",
    "FR": "Freight",                 "FP": "Freight processing",
    "GF": "Generic forms",           "GI": "GL inquiry",
    "GR": "Grid",                    "HA": "Handheld A",
    "HI": "Handheld I",              "HO": "Hold",
    "HP": "Hold processing",         "HR": "HR",
    "HS": "History",                 "HT": "Handheld T",
    "HH": "Handheld",                "CC": "Cycle Count",
    "PS": "Payroll Setup",           "EI": "EDI (alt)",
    "IC": "Inventory Customization", "CM": "Company Master",
    "PI": "Physical Inventory",      "TA": "TAS config",
    "EV": "Evolution",               "WC": "Work Centers",
}

for code, narrative in MODULE_NARRATIVES.items():
    pid = f"module-{code}"
    name = MODULE_NAMES.get(code, code)
    codes = sorted(module_menus.get(code, []))
    forms = sorted(module_forms.get(code, []))
    tables = sorted(module_tables.get(code, []))
    body_parts = [f"# {code} — {name}\n"]
    body_parts.append(narrative)
    body_parts.append(f"\n## Menu operations ({len(codes)})\n")
    if codes:
        body_parts.append("| Code | Operation |")
        body_parts.append("|---|---|")
        for c in codes:
            body_parts.append(f"| [{c}](#menu-{c}) | {menu_desc.get(c, '')} |")
    body_parts.append(f"\n## Database tables ({len(tables)})\n")
    if tables:
        body_parts.append("| Table | Fields | File |")
        body_parts.append("|---|---:|---|")
        for t in tables:
            info = schema.get(t, {})
            nf = len(info.get("fields", []))
            loc = info.get("location", "?")
            body_parts.append(f"| [{t}](#table-{t}) | {nf} | `{loc}` |")
    body_parts.append(f"\n## UI Forms ({len(forms)})\n")
    if forms:
        body_parts.append("| Form | Caption |")
        body_parts.append("|---|---|")
        for f in forms[:80]:
            cap = form_to_caption.get(f, "") or ""
            body_parts.append(f"| [{f}](#form-{f}) | {cap[:70]} |")
        if len(forms) > 80:
            body_parts.append(f"\n*...and {len(forms)-80} more*")
    pages[pid] = {
        "id": pid,
        "title": f"{code} — {name}",
        "section": "Modules",
        "kind": "module",
        "module": code,
        "body": convert_wiki_links("\n".join(body_parts)),
        "keywords": [code.lower(), name.lower(), code, name] + [c.lower() for c in codes[:10]],
    }

# 4. Menu-code pages (one per code)
for code, desc in menu_desc.items():
    pid = f"menu-{code}"
    mod = code.split('-')[0]
    modname = MODULE_NAMES.get(mod, mod)
    forms_csv = menu_to_form.get(code, '')
    forms = [f for f in forms_csv.split(';') if f] if forms_csv else []
    sources = menu_src.get(code, '')
    body = [
        f"# {code}\n",
        f"**{desc}**\n",
        f"**Module**: [{mod} — {modname}](#module-{mod})  ",
        f"**Menu route**: Main Menu → {modname} → {code}\n",
    ]
    if forms:
        body.append("\n## UI form(s)\n")
        for f in forms:
            cap = form_to_caption.get(f, '')
            body.append(f"- [`{f}`](#form-{f}) — {cap}")
    if sources:
        body.append("\n## Implementing programs\n")
        body.append(", ".join(f"`{s}`" for s in sources.split(';') if s))
    # Related menu codes (same module)
    siblings = sorted([c for c in module_menus.get(mod, []) if c != code])[:15]
    if siblings:
        body.append(f"\n## Sibling operations in {mod}\n")
        for s in siblings[:15]:
            body.append(f"- [{s}](#menu-{s}) {menu_desc.get(s,'')}")
    pages[pid] = {
        "id": pid,
        "title": f"{code} — {desc}",
        "section": "Menu codes",
        "kind": "menu",
        "module": mod,
        "body": "\n".join(body),
        "keywords": [code.lower(), desc.lower()] + desc.lower().split(),
    }

# 5. Table pages
for tname, info in schema.items():
    pid = f"table-{tname}"
    fields = info.get("fields", [])
    mod_prefix = tname[2:4] if tname.startswith(("BK", "MT")) else ""
    modname = MODULE_NAMES.get(mod_prefix, mod_prefix) if mod_prefix else ""
    body = [
        f"# `{tname}` — Database Table",
        f"**Location**: `{info.get('location', '?')}` *(per-company extension)*  ",
        f"**Fields**: {len(fields)}  ",
        f"**Module prefix**: `{mod_prefix}` — [{modname}](#module-{mod_prefix})" if mod_prefix else "",
        "",
        "## Schema",
        "",
        "| # | Field | Type | Offset | Size | Dec |",
        "|---|---|---|--:|--:|--:|",
    ]
    for i, f in enumerate(fields, 1):
        body.append(f"| {i} | `{f['name']}` | {f['type']} | {f['offset']} | {f['size']} | {f['dec']} |")
    pages[pid] = {
        "id": pid,
        "title": f"Table: {tname}",
        "section": "Tables",
        "kind": "table",
        "module": mod_prefix,
        "body": "\n".join(body),
        "keywords": [tname.lower(), tname] + [f['name'].lower() for f in fields[:50]],
    }

# 6. Form pages
for r in dfm_rows:
    form_name = r['file']
    pid = f"form-{form_name}"
    cap = r.get("caption", "")
    mod = ""
    m = re.match(r'^(T7|T6|BK)([A-Z]{2})', form_name.upper())
    if m:
        mod = m.group(2)
    # Try to guess the menu code: T7XXY.DFM → XX-Y
    menu_guess = None
    mm = re.match(r'^(T7|T6|BK)([A-Z]{2})([A-Z])([A-Z]?)', form_name.upper().replace('.DFM', ''))
    if mm:
        menu_guess = f"{mm.group(2)}-{mm.group(3)}" + (f"-{mm.group(4)}" if mm.group(4) else "")
    body = [
        f"# Form: `{form_name}`",
        f"**Caption**: {cap}  ",
        f"**Root class**: `{r.get('root_class','')}`  ",
        f"**Total controls**: {r.get('total_controls','')}  ",
        f"**Field (bound) count**: {r.get('field_count','')}  ",
        f"**Tab sheets**: {r.get('tab_count','')}  ",
        "",
        "## Control counts",
        "",
        f"| TTASEnter | TTASNumEnter | TTASDateEdit | TTASComboEnter/Box | TTASCheckBox | TTASDataGrid |",
        f"|---:|---:|---:|---:|---:|---:|",
        f"| {r.get('enter_count',0)} | {r.get('num_count',0)} | {r.get('date_count',0)} | {r.get('combo_count',0)} | {r.get('check_count',0)} | {r.get('grid_count',0)} |",
    ]
    if menu_guess and menu_guess in menu_desc:
        body.append(f"\n## Menu operation\n\n[`{menu_guess}`](#menu-{menu_guess}) — {menu_desc[menu_guess]}")
    pages[pid] = {
        "id": pid,
        "title": f"Form: {form_name}",
        "section": "Forms",
        "kind": "form",
        "module": mod,
        "body": "\n".join(body),
        "keywords": [form_name.lower(), cap.lower() if cap else ""] + (cap.lower().split() if cap else []),
    }

# 7. Glossary entries
def _resolve_ref(ref):
    """Resolve a see-also reference to its canonical page id."""
    if ref in _all_table_names():
        return 'table-' + ref
    # Menu-code pattern
    if re.match(r'^[A-Z]{2}-[A-Z](?:-[A-Z])?$', ref):
        return 'menu-' + ref
    # Bare glossary term → canonical glossary pid
    return _canonicalize(ref)

for term, short, body, see_also in GLOSSARY:
    pid = f"glossary-{re.sub(r'[^a-z0-9]+', '-', term.lower())}"
    full_body = [f"# {term}", f"*{short}*", "", body]
    if see_also:
        full_body.append("\n## See also")
        for s in see_also:
            resolved = _resolve_ref(s)
            full_body.append(f"- [{s}](#{resolved})")
    pages[pid] = {
        "id": pid,
        "title": term,
        "section": "Glossary",
        "kind": "glossary",
        "body": convert_wiki_links("\n".join(full_body)),
        "keywords": [term.lower(), term] + short.lower().split(),
    }

# 8. Auto-generate stub pages for any referenced-but-missing page IDs
#    so broken links degrade to "coming soon" rather than 404.
missing = set()
for p in list(pages.values()):
    body = p.get("body", "")
    for m in re.finditer(r'\(#([a-zA-Z0-9\-_.]+)\)', body):
        ref = m.group(1)
        if ref not in pages:
            missing.add(ref)

def _humanize(pid):
    return pid.replace("-", " ").replace("_", " ").title()

for mid in sorted(missing):
    title = _humanize(mid)
    # Categorize
    if mid.startswith("recipe-"):
        kind, section = "recipe", "Recipes"
        title = title.replace("Recipe ", "Recipe: ")
    elif mid.startswith("format-"):
        kind, section = "topic", "Reference"
    elif mid.startswith("subsystem-"):
        kind, section = "topic", "Architecture"
    else:
        kind, section = "topic", "Reference"
    body = (
        f"# {title}\n\n"
        f"*This topic is referenced but not yet fully written. "
        f"Related pages:*\n\n"
    )
    # Add a few related pages using search
    related_ids = []
    for tok in re.split(r'[\-_]+', mid):
        if tok.lower() in ('recipe','format','subsystem','index'): continue
        for pid in pages:
            if tok.lower() in pid.lower() and pid not in related_ids:
                related_ids.append(pid)
        if len(related_ids) >= 6: break
    for pid in related_ids[:6]:
        body += f"- [{pages[pid]['title']}](#{pid})\n"
    body += (
        f"\nYou can also search the help system for \"{title}\" — "
        f"press `Ctrl+K` and type it.\n"
    )
    pages[mid] = {
        "id": mid,
        "title": title,
        "section": section,
        "kind": kind,
        "body": body,
        "keywords": [w.lower() for w in re.split(r'[-_\s]+', mid) if len(w) > 1],
    }

print(f"Auto-generated {len(missing)} stub pages for referenced-but-missing IDs")

# ---------------------------------------------------------------------- #
# Build navigation tree
# ---------------------------------------------------------------------- #

nav = {
    "Getting Started": [],
    "Concepts": [],
    "Architecture": [],
    "Modules": [],
    "Recipes": [],
    "Menu codes": {},
    "Tables": {},
    "Forms": {},
    "Data": [],
    "Reference": [],
    "Integration": [],
    "Glossary": [],
}

# Topics, recipes, and glossary straight in
for pid, p in pages.items():
    sec = p["section"]
    entry = {"id": pid, "title": p["title"]}
    if sec in nav and isinstance(nav[sec], list):
        nav[sec].append(entry)

# Group menu codes by module
for pid, p in pages.items():
    if p["kind"] == "menu":
        mod = p["module"]
        nav["Menu codes"].setdefault(mod, []).append({"id": pid, "title": p["title"]})
for mod in nav["Menu codes"]:
    nav["Menu codes"][mod].sort(key=lambda x: x["id"])

# Group tables by prefix
for pid, p in pages.items():
    if p["kind"] == "table":
        mod = p["module"] or "other"
        nav["Tables"].setdefault(mod, []).append({"id": pid, "title": p["title"]})
for mod in nav["Tables"]:
    nav["Tables"][mod].sort(key=lambda x: x["id"])

# Group forms by module
for pid, p in pages.items():
    if p["kind"] == "form":
        mod = p["module"] or "other"
        nav["Forms"].setdefault(mod, []).append({"id": pid, "title": p["title"]})
for mod in nav["Forms"]:
    nav["Forms"][mod].sort(key=lambda x: x["id"])

# Sort sections
for sec in ("Getting Started", "Concepts", "Architecture", "Modules",
            "Recipes", "Data", "Reference", "Integration", "Glossary"):
    nav[sec].sort(key=lambda x: x["title"])


# ---------------------------------------------------------------------- #
# Build search index (inverted)
# ---------------------------------------------------------------------- #

STOP = set("the a an and or of to in on at for is are was were be been being have has had do does did will would could should may might can shall this that these those i you he she it we they me him her us them my your his their our which what when where why how".split())

def tokenize(text):
    text = text.lower()
    tokens = re.findall(r"[a-z0-9_\-]+", text)
    return [t for t in tokens if t not in STOP and len(t) > 1]

# title_tokens, body_tokens per page, then invert
index = {}  # token -> list of (page_id, score, context)
page_sum = {}  # page_id -> {title, section, kind, snippet}

for pid, p in pages.items():
    title_tokens = tokenize(p["title"])
    body_tokens = tokenize(p["body"][:8000])  # limit body size
    keyword_tokens = tokenize(" ".join(p.get("keywords", [])))
    # Collect snippet: first 180 chars of body stripped of markup
    snippet = re.sub(r'[#*`\[\]]+', '', p["body"])
    snippet = re.sub(r'\n+', ' ', snippet)[:180].strip()
    page_sum[pid] = {
        "id": pid,
        "title": p["title"],
        "section": p["section"],
        "kind": p["kind"],
        "snippet": snippet,
        "module": p.get("module", ""),
    }
    # Weighted postings
    for tok in set(title_tokens):
        index.setdefault(tok, []).append((pid, 10))
    for tok in set(keyword_tokens):
        index.setdefault(tok, []).append((pid, 5))
    for tok in set(body_tokens):
        index.setdefault(tok, []).append((pid, 1))

# Merge postings per (page, token) by summing scores
for tok in index:
    merged = {}
    for pid, score in index[tok]:
        merged[pid] = merged.get(pid, 0) + score
    index[tok] = sorted(merged.items(), key=lambda x: -x[1])

# ---------------------------------------------------------------------- #
# Keyword map (synonyms / aliases → page ids)
# ---------------------------------------------------------------------- #

KEYWORD_ALIASES = {
    "customer": ["module-AR", "table-BKARCUST", "menu-AR-A", "recipe-enter-customer"],
    "customers": ["module-AR", "table-BKARCUST", "menu-AR-A", "recipe-enter-customer"],
    "vendor": ["module-AP", "table-BKAPVEND", "menu-AP-A", "recipe-enter-vendor"],
    "vendors": ["module-AP", "table-BKAPVEND", "menu-AP-A", "recipe-enter-vendor"],
    "supplier": ["module-AP", "table-BKAPVEND", "menu-AP-A"],
    "item": ["module-IN", "table-BKICMSTR", "menu-IN-A", "recipe-enter-item"],
    "inventory": ["module-IN", "table-BKICMSTR", "menu-IN-A"],
    "stock": ["module-IN", "table-BKICMSTR", "menu-IN-A"],
    "part": ["module-IN", "table-BKICMSTR"],
    "invoice": ["recipe-enter-voucher", "recipe-print-invoice", "menu-AR-B", "menu-SO-F"],
    "bill": ["recipe-enter-voucher", "menu-AP-B"],
    "payment": ["recipe-record-payment", "menu-AR-C"],
    "check": ["recipe-print-checks", "menu-AP-H"],
    "pay": ["recipe-print-checks", "menu-AP-H", "recipe-pick-invoices"],
    "aging": ["menu-AR-F", "menu-AP-I", "recipe-ar-aging"],
    "so": ["module-SO", "menu-SO-A"],
    "sales order": ["module-SO", "menu-SO-A", "recipe-enter-so"],
    "po": ["module-PO", "menu-PO-A", "recipe-enter-po"],
    "purchase order": ["module-PO", "menu-PO-A", "recipe-enter-po"],
    "wo": ["module-WO", "menu-WO-A", "recipe-work-order"],
    "work order": ["module-WO", "menu-WO-A", "recipe-work-order"],
    "bom": ["module-BM", "table-BKBMMSTR", "recipe-enter-bom"],
    "bill of materials": ["module-BM"],
    "routing": ["module-RO", "recipe-enter-routing"],
    "mrp": ["module-MR", "recipe-run-mrp"],
    "gl": ["module-GL"],
    "general ledger": ["module-GL"],
    "accounting": ["module-GL", "module-AM"],
    "close": ["recipe-month-end-close", "module-AM"],
    "month end": ["recipe-month-end-close"],
    "year end": ["recipe-year-end-close"],
    "fiscal": ["module-AM", "recipe-month-end-close"],
    "payroll": ["module-PR"],
    "employee": ["module-PR"],
    "commission": ["module-CS"],
    "report": ["overview", "reporting-pipeline"],
    "print": ["recipe-print-checks", "recipe-print-invoice"],
    "login": ["security-model", "recipe-login"],
    "password": ["security-model"],
    "user": ["security-model", "recipe-add-user", "table-AHSYLOG"],
    "company": ["multi-company", "recipe-add-company"],
    "physical": ["module-PI", "recipe-physical-inventory"],
    "count": ["recipe-physical-inventory"],
    "backup": ["recipe-backup"],
    "rma": ["recipe-rma"],
    "quote": ["menu-SO-P-A", "menu-PO-E"],
    "rfq": ["recipe-rfq"],
    "tax": ["menu-AR-K", "menu-AP-S"],
    "1099": ["menu-AP-S", "recipe-1099"],
    "w2": ["module-PR", "menu-PR-H"],
    "help": ["welcome"],
    "encryption": ["dcy-rwn-decryption"],
    "decrypt": ["dcy-rwn-decryption"],
    "rwn": ["format-rwn", "dcy-rwn-decryption"],
    "dcy": ["format-dfm", "dcy-rwn-decryption"],
    "dfm": ["format-dfm"],
    "src": ["format-src"],
    "rtm": ["format-rtm"],
    "twofish": ["dcy-rwn-decryption"],
    "cfb": ["dcy-rwn-decryption"],
    "odbc": ["odbc-access"],
    "pervasive": ["odbc-access", "architecture-overview"],
    "sql": ["odbc-access"],
    "tas": ["architecture-overview", "format-src"],
    "delphi": ["architecture-overview"],
    "keyboard": ["menu-navigation"],
    "f1": ["menu-navigation"],
    "f2": ["menu-navigation"],
    "lookup": ["menu-navigation"],
    "shortcut": ["menu-navigation"],
    "workflow": ["core-workflows"],
    "multi-company": ["multi-company"],
    "companies": ["multi-company"],
}

# ---------------------------------------------------------------------- #
# Write outputs
# ---------------------------------------------------------------------- #

out = HERE / "data"
out.mkdir(exist_ok=True)

(out / "pages.json").write_text(json.dumps(pages, separators=(',', ':')))
(out / "nav.json").write_text(json.dumps(nav, separators=(',', ':')))
(out / "search.json").write_text(json.dumps({"index": index, "summaries": page_sum}, separators=(',', ':')))
(out / "keywords.json").write_text(json.dumps(KEYWORD_ALIASES, separators=(',', ':')))

# Also write stats
stats = {
    "pages": len(pages),
    "by_kind": {},
    "tokens_in_index": len(index),
    "nav_sections": list(nav.keys()),
}
for p in pages.values():
    stats["by_kind"][p["kind"]] = stats["by_kind"].get(p["kind"], 0) + 1
(out / "stats.json").write_text(json.dumps(stats, indent=2))

print("Build complete:")
for k, v in stats["by_kind"].items():
    print(f"  {k}: {v}")
print(f"  total pages: {stats['pages']}")
print(f"  search tokens: {stats['tokens_in_index']}")

# Print approximate file sizes
for f in (out / "pages.json", out / "search.json", out / "nav.json", out / "keywords.json"):
    print(f"  {f.name}: {f.stat().st_size:,} bytes")
