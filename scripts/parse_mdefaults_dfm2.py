"""
parse_mdefaults_dfm2.py — Pass 379
Extract BKYS.YN[N] → label Caption mappings from T7MDefaults.DFM
by matching Top positions of TLabel and input controls within each tab page.

In TAS Pro 7 DFMs:
- TLabel at (Left=X1, Top=Y) with Caption = 'Description'
- TTASENTER or TTASComboBox at (Left=X2, Top=Y+/-2) with FieldName = 'bkys.yn[N]'
- Same/nearby Top = same row = same setting

Strategy:
1. Parse DFM into a list of (object_type, properties_dict) per tab page
2. For each tab page, pair labels and input controls by closest Top value
3. For BKYS.YN[N] controls, find the closest label Caption
"""

import re
import sys
from collections import defaultdict

DFM_FILE = r"c:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\samples\T7MDefaults.DFM"

def main():
    with open(DFM_FILE, 'r', encoding='latin-1', errors='replace') as f:
        content = f.read()
        lines = content.split('\n')

    # Extract all object blocks with their properties
    # Using simple line-by-line approach

    current_tab = "Root"
    current_obj = None
    current_props = {}
    depth = 0

    # Store: list of (tab_name, obj_type, obj_name, props_dict)
    all_objects = []

    for i, line in enumerate(lines):
        stripped = line.strip()

        # Detect tab page
        if 'TTabSheet' in line and 'object' in line:
            # Will capture Caption in subsequent lines
            pass

        # Object start
        m = re.match(r'\s+object\s+(\w+)\s*:\s*(\w+)', line)
        if m:
            if current_obj and current_props:
                all_objects.append((current_tab, current_obj_type, current_obj, current_props))
            current_obj = m.group(1)
            current_obj_type = m.group(2)
            current_props = {'_line': i + 1}
            depth += 1
            if current_obj_type == 'TTabSheet':
                current_tab = "(pending)"
            continue

        # Property
        if current_obj is not None:
            for prop in ['Caption', 'FieldName', 'Left', 'Top', 'Width', 'Height']:
                m = re.match(r'\s+' + prop + r'\s*=\s*(.+)', line)
                if m:
                    val = m.group(1).strip().strip("'")
                    current_props[prop] = val
                    if prop == 'Caption' and current_obj_type == 'TTabSheet':
                        current_tab = val
                    break

        # Items.Strings (for combos)
        if current_obj is not None and 'Items.Strings' in line:
            # Collect items
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

        # Object end
        if stripped == 'end' and current_obj:
            if current_props:
                all_objects.append((current_tab, current_obj_type, current_obj, current_props.copy()))
            current_obj = None
            current_obj_type = None
            current_props = {}
            depth -= 1

    # Group by tab
    by_tab = defaultdict(list)
    for tab, obj_type, obj_name, props in all_objects:
        by_tab[tab].append((obj_type, obj_name, props))

    # For each tab, find all labels and YN controls, pair by Top position
    print("=== BKYS.YN[N] <-> Label Caption mapping from T7MDefaults.DFM ===")
    print()

    yn_mappings = []  # (yn_index, description, items, tab, allowed_chrs)

    for tab_name, objects in sorted(by_tab.items()):
        # Get labels (TLabel) in this tab
        labels = {}  # top -> caption
        for obj_type, obj_name, props in objects:
            if obj_type == 'TLabel':
                top = int(props.get('Top', -1))
                cap = props.get('Caption', '').strip()
                if cap and not cap.startswith('{'):
                    labels[top] = cap

        # Get YN input controls
        yn_controls = []
        for obj_type, obj_name, props in objects:
            field = props.get('FieldName', '')
            if not field:
                continue
            m = re.match(r'bkys\.yn\[(\d+)\]', field, re.IGNORECASE)
            if not m:
                continue
            yn_num = int(m.group(1))
            top = int(props.get('Top', -1))
            allowed = props.get('AllowedChrs', '')
            items = props.get('_items', [])
            yn_controls.append((yn_num, obj_name, top, allowed, items))

        if not yn_controls:
            continue

        # For each YN control, find nearest label by Top position
        for yn_num, obj_name, ctrl_top, allowed, items in sorted(yn_controls):
            if ctrl_top < 0 or not labels:
                best_label = "(no label found)"
            else:
                # Find label with nearest Top
                best_top = min(labels.keys(), key=lambda t: abs(t - ctrl_top))
                best_label = labels[best_top] if abs(best_top - ctrl_top) < 30 else "(no close label)"

            yn_mappings.append((yn_num, tab_name, best_label, allowed, items))

    # Sort by YN number and print
    yn_mappings.sort(key=lambda x: x[0])
    for yn_num, tab, label, allowed, items in yn_mappings:
        print(f"YN[{yn_num:3d}]  [{tab}]  {label!r}")
        if allowed:
            print(f"         AllowedChrs: {allowed!r}")
        if items:
            print(f"         Items: {items[:4]}")

    print()
    print(f"Total YN mappings found: {len(yn_mappings)}")

    # Also generate a compact CSV
    print()
    print("=== CSV output ===")
    print("YN_INDEX,TAB,DESCRIPTION,ALLOWED_CHARS")
    for yn_num, tab, label, allowed, items in yn_mappings:
        # For combo boxes, encode the items
        if items:
            label_full = label + ' | Options: ' + '; '.join(items[:4])
        else:
            label_full = label
        label_full = label_full.replace('"', "'")
        print(f'{yn_num},"{tab}","{label_full}","{allowed}"')

if __name__ == '__main__':
    main()
