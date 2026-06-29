"""
extract_yn_all.py — Pass 382
Extract ALL BKYS.YN[N] mappings from T7MDefaults.DFM using sequential pairing.

Strategy: for each YN control, take the label that PRECEDES it in the DFM file
(nearest earlier label in file order, within the same tab sheet).
Also record whether the control is a TTASComboBox (has Items.Strings = option list)
or TTASENTER (Y/N flag).

Output: sorted CSV to stdout.
"""

import re
import sys

DFM = r"C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\samples\T7MDefaults.DFM"

def main():
    with open(DFM, 'r', encoding='latin-1', errors='replace') as f:
        lines = f.readlines()

    results = []  # (yn_index, tab, label, items, obj_type, line_num)

    current_tab = "(root)"
    current_obj = None
    current_obj_type = None
    current_props = {}
    # Last seen label in this tab
    last_label_in_tab = {}  # tab_name -> last caption
    # All labels seen in order (tab, top, caption)
    labels_by_tab = {}  # tab -> list of (line_num, caption)
    # Objects collected
    all_objects = []  # (tab, type, name, props_dict)

    for i, line in enumerate(lines):
        # Detect tab sheet
        m_tab = re.match(r'\s+object\s+(\w+)\s*:\s*TTabSheet', line)
        if m_tab:
            # Will pick up Caption in next few lines
            current_tab_pending = True

        # Detect any object
        m_obj = re.match(r'\s+object\s+(\w+)\s*:\s*(\w+)', line)
        if m_obj:
            # Save previous object
            if current_obj and current_props:
                all_objects.append((current_tab, current_obj_type, current_obj, dict(current_props)))
            current_obj = m_obj.group(1)
            current_obj_type = m_obj.group(2)
            current_props = {'_line': i + 1}
            if current_obj_type == 'TTabSheet':
                current_tab = "(pending)"
            continue

        if current_obj:
            for prop in ['Caption', 'FieldName', 'Left', 'Top', 'Width']:
                m = re.match(r'\s+' + prop + r'\s*=\s*(.+)', line)
                if m:
                    val = m.group(1).strip().strip("'")
                    current_props[prop] = val
                    if prop == 'Caption' and current_obj_type == 'TTabSheet':
                        current_tab = val
                    break

            # Capture Items.Strings
            if 'Items.Strings' in line:
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
            all_objects.append((current_tab, current_obj_type, current_obj, dict(current_props)))
            current_obj = None
            current_obj_type = None
            current_props = {}

    # Build per-tab ordered label list and YN control list
    from collections import defaultdict
    tab_labels = defaultdict(list)    # tab -> [(line_num, caption)]
    tab_yn = defaultdict(list)        # tab -> [(line_num, yn_index, obj_type, items)]

    for tab, obj_type, obj_name, props in all_objects:
        line_num = props.get('_line', 0)
        if obj_type == 'TLabel':
            cap = props.get('Caption', '').strip()
            if cap and not cap.startswith('{') and len(cap) > 2:
                tab_labels[tab].append((line_num, cap))
        else:
            fn = props.get('FieldName', '')
            m = re.match(r'bkys\.yn\[(\d+)\]', fn, re.IGNORECASE)
            if m:
                yn_idx = int(m.group(1))
                items = props.get('_items', [])
                tab_yn[tab].append((line_num, yn_idx, obj_type, items))

    # Pair: for each YN control, find the last label BEFORE it (in line_num order) within same tab
    yn_results = []
    for tab, yn_list in tab_yn.items():
        labels = sorted(tab_labels[tab], key=lambda x: x[0])
        for yn_line, yn_idx, obj_type, items in yn_list:
            # Find last label before this line
            best_label = "(no label)"
            for lline, lcap in labels:
                if lline < yn_line:
                    best_label = lcap
                # Past the control — stop
                elif lline > yn_line + 5:
                    break
            yn_results.append((yn_idx, tab, best_label, obj_type, items, yn_line))

    yn_results.sort(key=lambda x: x[0])

    print("YN_INDEX,TAB,LABEL,OBJ_TYPE,OPTIONS,LINE")
    for yn_idx, tab, label, obj_type, items, line_num in yn_results:
        label_clean = label.replace('"', "'").replace('\n', ' ')
        opts = "; ".join(items[:6])
        opts_clean = opts.replace('"', "'")
        print(f'{yn_idx},"{tab}","{label_clean}","{obj_type}","{opts_clean}",{line_num}')

    print(f"# Total YN mappings: {len(yn_results)}", file=sys.stderr)
    print(f"# Unique YN indices: {len(set(r[0] for r in yn_results))}", file=sys.stderr)

if __name__ == '__main__':
    main()
