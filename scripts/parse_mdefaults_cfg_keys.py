"""
parse_mdefaults_cfg_keys.py — Pass 380
Extract ISTS.CFG.* field → label caption mappings from T7MDefaults.DFM
using Top-position pairing within each tab page.

Covers all non-YN ISTS.CFG.* and BKEST.CFG.* fields (495 expected).
"""

import re
from collections import defaultdict

DFM_FILE = r"c:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\samples\T7MDefaults.DFM"

def main():
    with open(DFM_FILE, 'r', encoding='latin-1', errors='replace') as f:
        content = f.read()
        lines = content.split('\n')

    current_tab = "Root"
    current_obj = None
    current_obj_type = None
    current_props = {}

    all_objects = []  # (tab_name, obj_type, obj_name, props_dict)

    for i, line in enumerate(lines):
        m = re.match(r'\s+object\s+(\w+)\s*:\s*(\w+)', line)
        if m:
            if current_obj and current_props:
                all_objects.append((current_tab, current_obj_type, current_obj, current_props))
            current_obj = m.group(1)
            current_obj_type = m.group(2)
            current_props = {'_line': i + 1}
            if current_obj_type == 'TTabSheet':
                current_tab = "(pending)"
            continue

        if current_obj is not None:
            for prop in ['Caption', 'FieldName', 'Left', 'Top', 'Width', 'Height', 'AllowedChrs', 'Hint']:
                m = re.match(r'\s+' + prop + r'\s*=\s*(.+)', line)
                if m:
                    val = m.group(1).strip().strip("'")
                    current_props[prop] = val
                    if prop == 'Caption' and current_obj_type == 'TTabSheet':
                        current_tab = val
                    break

        if current_obj is not None and 'Items.Strings' in line:
            items = []
            j = i + 1
            while j < len(lines) and j < i + 30:
                item_line = lines[j].strip()
                if item_line == ')':
                    break
                item_line = item_line.strip("'()")
                if item_line:
                    items.append(item_line)
                j += 1
            current_props['_items'] = items

        if line.strip() == 'end' and current_obj:
            if current_props:
                all_objects.append((current_tab, current_obj_type, current_obj, current_props.copy()))
            current_obj = None
            current_obj_type = None
            current_props = {}

    by_tab = defaultdict(list)
    for tab, obj_type, obj_name, props in all_objects:
        by_tab[tab].append((obj_type, obj_name, props))

    print("=== ISTS.CFG.* / BKEST.CFG.* key -> Label Caption mapping from T7MDefaults.DFM ===")
    print()

    all_mappings = []  # (key, tab, label, allowed, items, hint, line_num)

    cfg_pattern = re.compile(r'((?:ists|bkest|bkys)\.cfg\.[a-z0-9#$%]+)', re.IGNORECASE)
    # Also match bkys.* non-YN fields like BKYS.WONUM
    bkys_pattern = re.compile(r'(bkys\.[a-z0-9#$%]+(?:\[[0-9]+\])?)', re.IGNORECASE)

    for tab_name, objects in sorted(by_tab.items()):
        labels = {}
        for obj_type, obj_name, props in objects:
            if obj_type == 'TLabel':
                top = int(props.get('Top', -1))
                cap = props.get('Caption', '').strip()
                if cap and not cap.startswith('{') and len(cap) > 3:
                    labels[top] = cap

        for obj_type, obj_name, props in objects:
            field = props.get('FieldName', '')
            if not field:
                continue

            # Match ISTS.CFG.* or BKEST.CFG.* (exclude YN[N] — already documented)
            m_cfg = cfg_pattern.match(field)
            m_bkys = bkys_pattern.match(field) if not m_cfg else None

            key = None
            if m_cfg:
                key = m_cfg.group(1).upper()
            elif m_bkys:
                # only non-YN bkys fields
                raw = m_bkys.group(1)
                if not re.search(r'yn\[', raw, re.IGNORECASE):
                    key = raw.upper()

            if not key:
                continue

            ctrl_top = int(props.get('Top', -1))
            allowed = props.get('AllowedChrs', '')
            hint = props.get('Hint', '')
            items = props.get('_items', [])
            line_num = props.get('_line', 0)

            if ctrl_top < 0 or not labels:
                best_label = "(no label found)"
            else:
                best_top = min(labels.keys(), key=lambda t: abs(t - ctrl_top))
                dist = abs(best_top - ctrl_top)
                best_label = labels[best_top] if dist < 40 else f"(nearest label dist={dist}: {labels[best_top]!r})"

            all_mappings.append((key, tab_name, best_label, allowed, items, hint, line_num))

    all_mappings.sort(key=lambda x: (x[0], x[1]))

    prev_key = None
    for key, tab, label, allowed, items, hint, line_num in all_mappings:
        marker = " [DUP]" if key == prev_key else ""
        print(f"{key}  [{tab}]  {label!r}{marker}")
        if allowed:
            print(f"   AllowedChrs: {allowed!r}")
        if hint:
            print(f"   Hint: {hint!r}")
        if items:
            print(f"   Items: {items[:5]}")
        prev_key = key

    print()
    print(f"Total ISTS.CFG/BKEST.CFG/BKYS non-YN mappings: {len(all_mappings)}")

    # CSV output
    print()
    print("=== CSV ===")
    print("KEY,TAB,DESCRIPTION,ALLOWED_CHARS,HINT")
    for key, tab, label, allowed, items, hint, line_num in all_mappings:
        if items:
            label_full = label + ' | Options: ' + '; '.join(items[:5])
        else:
            label_full = label
        label_full = label_full.replace('"', "'")
        hint_clean = hint.replace('"', "'")
        print(f'"{key}","{tab}","{label_full}","{allowed}","{hint_clean}"')

if __name__ == '__main__':
    main()
