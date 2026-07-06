"""
extract_mdefaults_yn.py
Parse T7MDEFAULTS.DFM and extract all BKYS.YN[N] control bindings
with their associated labels and combo items.

Strategy:
- Scan each line for FieldName = 'bkys.yn[N]' (case-insensitive)
- For each match, search backwards in the same component block for a Caption
  or look at Items.Strings if it's a TTASComboBox
- Also capture the object type and name
"""
import re
import os

DFM_PATH = r'\\i2s109-solidcrm\DBAMFG$\DFM\T7MDEFAULTS.DFM'

def read_file(path):
    for enc in ('utf-8', 'cp1252', 'latin-1'):
        try:
            with open(path, 'r', encoding=enc, errors='replace') as f:
                return f.readlines()
        except Exception:
            continue
    return []

def extract_yn_bindings(lines):
    yn_re = re.compile(r"FieldName\s*=\s*'bkys\.yn\[(\d+)\]'", re.IGNORECASE)
    obj_re = re.compile(r'^\s*object\s+(\w+)\s*:\s*(\w+)', re.IGNORECASE)
    caption_re = re.compile(r"Caption\s*=\s*'([^']*)'", re.IGNORECASE)
    items_re = re.compile(r"'([^']+)'")

    results = []

    for i, line in enumerate(lines):
        m = yn_re.search(line)
        if not m:
            continue
        slot = int(m.group(1))

        # Walk back to find the object declaration for this control
        obj_name = ''
        obj_type = ''
        items_strings = []
        for j in range(i, max(i - 60, 0), -1):
            om = obj_re.match(lines[j])
            if om:
                obj_name = om.group(1)
                obj_type = om.group(2)
                break

        # If it's a TTASComboBox, scan forward to find Items.Strings
        if 'combo' in obj_type.lower():
            in_items = False
            for j in range(max(i - 40, 0), i + 5):
                if 'Items.Strings' in lines[j]:
                    in_items = True
                if in_items:
                    ms = items_re.findall(lines[j])
                    for s in ms:
                        s = s.strip()
                        if s and 'Items.Strings' not in s:
                            items_strings.append(s)
                if in_items and ')' in lines[j] and 'Items.Strings' not in lines[j]:
                    break

        # Walk back from the object start to find the nearest TLabel Caption
        # (labels typically appear before the object they describe)
        caption = ''
        if obj_name:
            # Find object start line
            obj_start = i
            for j in range(i, max(i - 60, 0), -1):
                om = obj_re.match(lines[j])
                if om and om.group(1) == obj_name:
                    obj_start = j
                    break
            # Look back up to 80 lines before the object for a TLabel
            for j in range(obj_start - 1, max(obj_start - 100, 0), -1):
                cm = caption_re.search(lines[j])
                if cm:
                    cap = cm.group(1).strip()
                    if cap:
                        caption = cap
                        break
                # Stop if we hit another 'object' declaration that isn't a TLabel
                om2 = obj_re.match(lines[j])
                if om2 and 'label' not in om2.group(2).lower() and 'panel' not in om2.group(2).lower():
                    # only stop if we've hit a non-label, non-panel object
                    pass

        results.append({
            'slot': slot,
            'line': i + 1,
            'obj_name': obj_name,
            'obj_type': obj_type,
            'caption': caption,
            'items': items_strings[:4],  # first 4 items
        })

    return results

def main():
    print(f"Reading {DFM_PATH} ...")
    lines = read_file(DFM_PATH)
    print(f"  {len(lines)} lines")

    results = extract_yn_bindings(lines)

    # Sort by slot number
    results.sort(key=lambda r: r['slot'])

    # Deduplicate (same slot may appear in multiple tabs/pages of the form)
    seen = {}
    for r in results:
        slot = r['slot']
        if slot not in seen:
            seen[slot] = r
        else:
            # Keep the one with more info
            existing = seen[slot]
            if (not existing['caption'] and r['caption']) or \
               (not existing['items'] and r['items']):
                seen[slot] = r

    print(f"\n{'Slot':>5}  {'Object':<20}  {'Type':<22}  {'Caption / Items'}")
    print('-' * 100)
    for slot in sorted(seen.keys()):
        r = seen[slot]
        if r['items']:
            label = ' | '.join(r['items'][:3])
        else:
            label = r['caption']
        print(f"  {slot:>3}  {r['obj_name']:<20}  {r['obj_type']:<22}  {label}")

    print(f"\nTotal unique YN slots in T7MDEFAULTS.DFM: {len(seen)}")

    # Save as TSV
    out_path = os.path.join(os.path.dirname(__file__), '_tmp_mdefaults_yn.tsv')
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write('slot\tobj_name\tobj_type\tcaption\titems\tline\n')
        for slot in sorted(seen.keys()):
            r = seen[slot]
            items_str = ' | '.join(r['items'])
            f.write(f"{slot}\t{r['obj_name']}\t{r['obj_type']}\t{r['caption']}\t{items_str}\t{r['line']}\n")
    print(f"\nSaved TSV: {out_path}")

if __name__ == '__main__':
    main()
