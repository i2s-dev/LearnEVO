# LearnEVO Help Browser

A self-contained, browser-based help system covering every aspect of
EvoERP — menu operations, modules, forms, database tables, file formats,
architecture, and step-by-step task walkthroughs.

## Quick start

Double-click **`launch.bat`**, or from a terminal:

```
cd learnevo-help
python -m http.server 8765
```

Then open <http://localhost:8765> in any modern browser.

## What's inside

- **2,607 pages** across 8 kinds:
  - 12 conceptual topics (Welcome, Quick Tour, Architecture, Security, …)
  - 22 module deep-dives (AR, AP, IN, SO, PO, WO, GL, …)
  - 10 how-to recipes (Enter a Customer, Print Checks, Run MRP, …)
  - 759 menu-code pages (every `XX-Y[-Z]` operation)
  - 659 database-table pages (full field schemas)
  - 1,109 UI-form pages (every `.DFM`)
  - 36 glossary entries
- **Full-text search** across everything, with keyword synonyms.
- **Cross-linked**: every page shows outbound and inbound links.
- **Sidebar navigation** grouped by section and module.
- **Keyboard-driven**: Ctrl+K search, `/` focus, `g h` home, etc.

## Search tips

The search bar accepts:

| Query | Example | Behavior |
|-------|---------|----------|
| Plain English | `how to print checks` | Natural-language search |
| Menu code | `AP-H` | Jumps straight to the menu page |
| Module code | `AR` | Jumps to the AR module page |
| Table name | `BKARCUST` | Jumps to the table schema |
| Form name | `T7ARA.DFM` | Jumps to the form inventory entry |
| Field name | `BKAR_CUSTCODE` | Finds tables containing that field |
| Keyword | `customer` | Shows all customer-related pages |

## Keyboard shortcuts

- `Ctrl+K` / `/` — focus search
- `↑` `↓` in search — navigate results
- `Enter` — open highlighted result
- `Esc` — close search
- `g` then `h` — home
- `g` then `r` — recipes
- `g` then `m` — modules
- `g` then `t` — tables

## Rebuilding data

If you update any hand-authored content in `content/`, re-run:

```
python build.py
```

That regenerates `data/*.json` (pages, search index, navigation, keyword map, stats).

## Scope

This browser works entirely off data extracted from the read-only EVO
installation — it does NOT connect to EVO or modify anything. Safe to
leave running; it's just a static site.

## Architecture

- `content/*.py` — hand-authored Markdown source for topics, recipes,
  modules, glossary. Plain Python modules exporting lists of tuples.
- `build.py` — aggregates content + CSVs/JSON from `../samples/` into
  the frontend JSON (`data/`).
- `data/` — generated JSON data. Don't hand-edit.
- `js/` — vanilla JS (no framework):
  - `marked-lite.js` — tiny Markdown → HTML renderer
  - `search.js` — inverted-index search + keyword aliases
  - `renderer.js` — page / sidebar / breadcrumb rendering
  - `app.js` — router, keyboard handling, wiring
- `css/style.css` — styling (dark topbar, light content).
- `index.html` — the single-page shell.

## Extending

### Add a new topic

Edit `content/topics.py`, append a tuple to `TOPICS`:

```python
("my-topic-id", "My Topic Title", "Concepts",
"""
## Heading

Body content in Markdown. Use `[[other-page-id]]` for cross-links.
""",
["keyword1", "keyword2"]),
```

Run `python build.py` and reload.

### Add a new recipe

Edit `content/recipes.py`:

```python
("recipe-my-task", "How to Do My Task", "Module",
["Main Menu", "Module", "XX-Y Something"],  # menu route
"""
## Step-by-step

1. …
""",
["keywords"]),
```

### Add a glossary term

Edit `content/glossary.py`:

```python
("Term", "short def", "long body markdown", ["see-also-page-ids"]),
```
