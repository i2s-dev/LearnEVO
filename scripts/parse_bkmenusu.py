"""
Parse BKMENUSU.TXT — EvoERP complete menu structure.

File format (CSV-style):
  GROUPS section:   "GROUPS","<category>","<module_code>"
  BUTTONS section:  "BUTTONS","<full_name>","<module_code>",<icon_id>
  Menu items:       "<CODE>","<menu_text>","<program_file>"
    where CODE = 2-char module + 1-char operation letter (e.g. "ADA" = AD + A)

Outputs:
  samples/menu_catalog.csv  — full menu item table
  samples/module_names.csv  — module code → name → group
"""
import csv
import re
from pathlib import Path
from collections import defaultdict

SAMPLES = Path(r"C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\samples")


def parse_bkmenusu():
    groups = {}     # module_code -> category_name
    buttons = {}    # module_code -> full_module_name, icon_id
    menu_items = [] # list of {code, module, op, text, program}

    raw_lines = (SAMPLES / 'BKMENUSU.TXT').read_text(encoding='utf-8-sig', errors='replace')
    # Parse as CSV
    reader = csv.reader(raw_lines.splitlines())
    for row in reader:
        if not row or len(row) < 2:
            continue
        tag = row[0].strip()
        if tag == 'GROUPS':
            if len(row) >= 3:
                category = row[1].strip()
                mod = row[2].strip()
                groups[mod] = category
        elif tag == 'BUTTONS':
            if len(row) >= 3:
                full_name = row[1].strip()
                mod = row[2].strip()
                icon_id = row[3].strip() if len(row) >= 4 else ''
                buttons[mod] = (full_name, icon_id)
        else:
            # Menu item line: code, text, program
            code = row[0].strip()
            if len(code) >= 3 and len(row) >= 3:
                text = row[1].strip()
                program = row[2].strip() if len(row) >= 3 else ''
                # Extract module (first 2 chars) and operation (rest)
                mod = code[:2]
                op = code[2:]
                menu_items.append({
                    'code': code,
                    'module': mod,
                    'operation': op,
                    'text': text,
                    'program': program,
                })

    print(f"Groups: {len(groups)}")
    print(f"Buttons: {len(buttons)}")
    print(f"Menu items: {len(menu_items)}")

    # Write module names CSV
    with open(SAMPLES / 'module_names.csv', 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['module_code', 'full_name', 'group', 'icon_id', 'item_count'])
        for mod in sorted(groups.keys() | buttons.keys()):
            category = groups.get(mod, '(no group)')
            full_name, icon_id = buttons.get(mod, ('(no name)', ''))
            count = sum(1 for m in menu_items if m['module'] == mod)
            w.writerow([mod, full_name, category, icon_id, count])

    print(f"\nModule reference (from BKMENUSU.TXT):")
    print(f"{'Code':<6} {'Group':<12} {'Full Name':<40} {'Items':>5}")
    print("-" * 65)
    for mod in sorted(groups.keys() | buttons.keys()):
        category = groups.get(mod, '?')
        full_name, icon_id = buttons.get(mod, ('?', ''))
        count = sum(1 for m in menu_items if m['module'] == mod)
        print(f"{mod:<6} {category:<12} {full_name:<40} {count:>5}")

    # Write full menu catalog
    with open(SAMPLES / 'menu_catalog.csv', 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['code', 'module', 'operation', 'group', 'module_name', 'menu_text', 'program'])
        for item in menu_items:
            mod = item['module']
            category = groups.get(mod, '?')
            full_name, _ = buttons.get(mod, ('?', ''))
            w.writerow([item['code'], mod, item['operation'], category, full_name,
                        item['text'], item['program']])

    print(f"\nMenu items by module (top 20):")
    by_mod = defaultdict(list)
    for item in menu_items:
        by_mod[item['module']].append(item)
    for mod, items in sorted(by_mod.items(), key=lambda x: -len(x[1]))[:20]:
        full_name, _ = buttons.get(mod, ('?', ''))
        cat = groups.get(mod, '?')
        print(f"  {mod} ({cat:12} {full_name:35}): {len(items)} items")

    # Show sample items for a few modules
    for mod in ['WO', 'AP', 'CM', 'DE', 'SM']:
        items = by_mod.get(mod, [])
        if items:
            print(f"\n  {mod} sample operations:")
            for item in items[:5]:
                print(f"    {item['code']}: {item['text']!r} -> {item['program']}")

    # Check T6 vs T7 programs
    t6_count = sum(1 for m in menu_items if m['program'].upper().startswith('T6'))
    t7_count = sum(1 for m in menu_items if m['program'].upper().startswith('T7'))
    bk_count = sum(1 for m in menu_items if m['program'].upper().startswith('BK'))
    other_count = len(menu_items) - t6_count - t7_count - bk_count
    print(f"\nProgram file generations:")
    print(f"  T6 (TAS Pro 6 .RUN): {t6_count}")
    print(f"  T7 (TAS Pro 7 .RWN): {t7_count}")
    print(f"  BK* (Btrieve data?): {bk_count}")
    print(f"  Other: {other_count}")

    return groups, buttons, menu_items


if __name__ == '__main__':
    parse_bkmenusu()
