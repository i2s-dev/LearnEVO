"""
parse_mdefaults_dfm.py — Pass 379
Extract field-name to label/caption mappings from T7MDefaults.DFM.

Strategy: DFM is text with object/end blocks. For each object with a
FieldName = 'BKYS.YN[N]' or similar, find:
  1. The nearest preceding TLabel Caption within the same tab page
  2. The Items.Strings (for combo boxes)
  3. The current tab page name (Caption)

This gives us the meaning of each BKYS.YN[N] setting.
"""

import re
import sys

DFM_FILE = r"c:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\samples\T7MDefaults.DFM"

def main():
    with open(DFM_FILE, 'r', encoding='latin-1', errors='replace') as f:
        lines = f.readlines()

    # Build an index: for each line, track the current tab page context (TTabSheet Caption)
    # and collect all FieldName references with nearby context

    # Strategy: scan for FieldName = 'BKYS.*' or 'ISTS.CFG.*'
    # Then backtrack to find the nearest Label Caption

    # Pass 1: collect all FieldName positions
    field_refs = []  # (line_num, field_name)
    for i, line in enumerate(lines):
        m = re.search(r"FieldName\s*=\s*'([^']+)'", line)
        if m:
            field_refs.append((i, m.group(1)))

    print(f"Total FieldName references: {len(field_refs)}")

    # Pass 2: for each BKYS.YN[N] reference, find context
    yn_refs = [(ln, fn) for ln, fn in field_refs if re.match(r'BKYS\.YN\[', fn, re.IGNORECASE)]
    bkys_refs = [(ln, fn) for ln, fn in field_refs if re.match(r'BKYS\.|ISTS\.CFG\.|BKEST\.CFG\.', fn, re.IGNORECASE)]

    print(f"BKYS.YN[N] references: {len(yn_refs)}")
    print(f"All BKYS/ISTS.CFG/BKEST.CFG references: {len(bkys_refs)}")
    print()

    # For YN references, print context
    print("=== BKYS.YN[N] field mappings ===")
    for line_num, field_name in yn_refs:
        # Find the object name (go back until we find 'object XXXX: TTASComboBox' or similar)
        obj_name = "(unknown)"
        obj_type = "(unknown)"
        for j in range(line_num, max(0, line_num - 60), -1):
            m = re.match(r'\s+object\s+(\w+):\s+(\w+)', lines[j])
            if m:
                obj_name = m.group(1)
                obj_type = m.group(2)
                break

        # Find Items.Strings (for combo boxes) — look forward
        items = []
        in_items = False
        for j in range(line_num, min(len(lines), line_num + 50)):
            if 'Items.Strings' in lines[j]:
                in_items = True
            elif in_items:
                if lines[j].strip().startswith("'"):
                    item_text = lines[j].strip().strip("'")
                    items.append(item_text)
                elif lines[j].strip() == ')':
                    break

        # Find nearest TLabel Caption before this line (within 200 lines)
        labels_before = []
        for j in range(line_num - 1, max(0, line_num - 200), -1):
            m = re.search(r"Caption\s*=\s*'([^']*)'", lines[j])
            if m and m.group(1).strip():
                labels_before.append((line_num - j, m.group(1).strip()))
                if len(labels_before) >= 4:
                    break

        # Find the tab page this control is on (search backward for TTabSheet)
        tab_caption = "(unknown tab)"
        for j in range(line_num, max(0, line_num - 500), -1):
            if 'object' in lines[j] and 'TTabSheet' in lines[j]:
                # Find its Caption
                for k in range(j, min(len(lines), j + 20)):
                    m = re.search(r"Caption\s*=\s*'([^']*)'", lines[k])
                    if m:
                        tab_caption = m.group(1).strip()
                        break
                break

        print(f"Line {line_num+1:5d}: {field_name}")
        print(f"   Control: {obj_name} ({obj_type})")
        print(f"   Tab: {tab_caption}")
        if items:
            print(f"   Items: {items[:4]}")
        if labels_before:
            print(f"   Nearby labels (dist, caption):")
            for dist, cap in labels_before[:3]:
                print(f"      -{dist}: {cap!r}")
        print()

    # Also show a summary of what BKYS.YN values appear vs ISTS.CFG vs others
    print()
    print("=== Summary of all BKYS.*/ISTS.CFG.*/BKEST.CFG.* fields ===")
    from collections import Counter
    prefix_count = Counter()
    for _, fn in bkys_refs:
        # Extract prefix
        m = re.match(r'([A-Za-z]+\.[A-Za-z]+)\.', fn)
        if m:
            prefix_count[m.group(0)] += 1
        else:
            prefix_count[fn.split('.')[0]] += 1
    for prefix, count in sorted(prefix_count.items(), key=lambda x: -x[1])[:30]:
        print(f"  {count:4d}  {prefix}")

if __name__ == '__main__':
    main()
