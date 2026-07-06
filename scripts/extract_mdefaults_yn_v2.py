"""
extract_mdefaults_yn_v2.py
Parse T7MDEFAULTS.DFM with panel-aware positional label matching.

Strategy:
1. Parse the DFM as a tree of (object_name, object_type, properties, children)
2. For each panel/container, collect all TLabel objects and all TTASENTER/TTASComboBox objects
3. Match each BKYS.YN[N] control to the nearest TLabel by Y-coordinate proximity
4. Within same Y row (±4px), prefer the label with highest Left coordinate <= control Left
"""
import re
import os
import sys

DFM_PATH = r'\\i2s109-solidcrm\DBAMFG$\DFM\T7MDEFAULTS.DFM'

def read_file(path):
    for enc in ('utf-8', 'cp1252', 'latin-1'):
        try:
            with open(path, 'r', encoding=enc, errors='replace') as f:
                return f.read()
        except Exception:
            continue
    return ''

# ---- DFM parser ----

class DFMObject:
    def __init__(self, name, typ, line_no):
        self.name = name
        self.typ = typ
        self.line_no = line_no
        self.props = {}   # key -> value (strings)
        self.children = []
        self.parent = None

    def get_int(self, key, default=None):
        v = self.props.get(key)
        if v is None:
            return default
        try:
            return int(v)
        except (ValueError, TypeError):
            return default

    def get_str(self, key, default=''):
        v = self.props.get(key, default)
        if v and v.startswith("'") and v.endswith("'"):
            return v[1:-1]
        return v or default

    def caption(self):
        return self.get_str('Caption')

    def top(self):
        return self.get_int('Top', 0)

    def left(self):
        return self.get_int('Left', 0)

    def field_name(self):
        fn = self.get_str('FieldName').lower()
        return fn

    def yn_slot(self):
        fn = self.field_name()
        m = re.match(r'bkys\.yn\[(\d+)\]', fn, re.IGNORECASE)
        if m:
            return int(m.group(1))
        return None

    def items_strings(self):
        raw = self.props.get('Items.Strings', '')
        if not raw:
            return []
        items = re.findall(r"'([^']+)'", raw)
        return items

def parse_dfm(text):
    lines = text.splitlines()
    root = None
    stack = []
    i = 0
    obj_re = re.compile(r'^\s*object\s+(\w+)\s*:\s*(\w+)', re.IGNORECASE)
    prop_re = re.compile(r'^\s*(\w[\w.]*)\s*=\s*(.*)')
    end_re = re.compile(r'^\s*end\s*$', re.IGNORECASE)
    # Track multi-line values (e.g. Items.Strings)
    in_multiline = None
    ml_key = None
    ml_buf = []

    while i < len(lines):
        line = lines[i]

        # Handle multi-line value accumulation
        if in_multiline:
            ml_buf.append(line.strip())
            if ')' in line:
                if stack:
                    stack[-1].props[ml_key] = ' '.join(ml_buf)
                in_multiline = False
                ml_buf = []
                ml_key = None
            i += 1
            continue

        m = obj_re.match(line)
        if m:
            obj = DFMObject(m.group(1), m.group(2), i + 1)
            if stack:
                obj.parent = stack[-1]
                stack[-1].children.append(obj)
            else:
                root = obj
            stack.append(obj)
            i += 1
            continue

        if end_re.match(line):
            if stack:
                stack.pop()
            i += 1
            continue

        pm = prop_re.match(line)
        if pm and stack:
            key = pm.group(1)
            val = pm.group(2).strip()
            if val.endswith('('):
                in_multiline = True
                ml_key = key
                ml_buf = [val]
            else:
                stack[-1].props[key] = val
        i += 1

    return root

def collect_all(node, result=None):
    if result is None:
        result = []
    result.append(node)
    for child in node.children:
        collect_all(child, result)
    return result

def match_yn_to_labels(root):
    all_objects = collect_all(root)

    # Group objects by their parent container
    container_groups = {}  # parent_id -> list of DFMObject
    for obj in all_objects:
        pid = id(obj.parent) if obj.parent else 0
        container_groups.setdefault(pid, []).append(obj)

    # For each TTASENTER/TTASComboBox with YN slot, find its label
    results = []
    for obj in all_objects:
        slot = obj.yn_slot()
        if slot is None:
            continue

        # Get items strings for combo boxes
        items = obj.items_strings()

        # Find sibling labels in the same container
        pid = id(obj.parent)
        siblings = container_groups.get(pid, [])

        labels_in_container = [
            s for s in siblings
            if 'label' in s.typ.lower() and s.caption()
        ]

        # Also look at grandparent level for cases where labels are in a parent panel
        gp_labels = []
        if obj.parent and obj.parent.parent:
            gpid = id(obj.parent.parent)
            gp_siblings = container_groups.get(gpid, [])
            gp_labels = [
                s for s in gp_siblings
                if 'label' in s.typ.lower() and s.caption()
            ]

        obj_top = obj.top()
        obj_left = obj.left()

        def score_label(lbl):
            """Lower score = better match."""
            dy = abs(lbl.top() - obj_top)
            dx = obj_left - lbl.left()
            # Prefer labels on the same row (dy < 5) to the left
            if dy <= 5:
                if 0 <= dx <= 500:
                    return (0, dy, dx)  # same row, to the left
                else:
                    return (1, dy, abs(dx))
            # Next prefer labels just above (within 30px)
            elif -5 < lbl.top() - obj_top <= 30:
                return (2, dy, abs(lbl.left() - obj_left))
            else:
                return (3, dy, abs(lbl.left() - obj_left))

        best_label = ''
        if labels_in_container:
            best = min(labels_in_container, key=score_label)
            s = score_label(best)
            if s[0] <= 2 and s[1] <= 30:
                best_label = best.caption()

        if not best_label and gp_labels:
            best = min(gp_labels, key=score_label)
            s = score_label(best)
            if s[0] <= 2 and s[1] <= 30:
                best_label = best.caption()

        results.append({
            'slot': slot,
            'line': obj.line_no,
            'obj_name': obj.name,
            'obj_type': obj.typ,
            'caption': best_label,
            'items': items[:4],
        })

    return results

def main():
    print(f"Reading {DFM_PATH} ...")
    text = read_file(DFM_PATH)
    print(f"  {len(text):,} chars, {text.count(chr(10)):,} lines")

    print("Parsing DFM tree ...")
    root = parse_dfm(text)
    if root is None:
        print("ERROR: parse failed — no root found")
        sys.exit(1)

    print("Matching YN controls to labels ...")
    results = match_yn_to_labels(root)

    # Sort by slot, deduplicate keeping best info
    results.sort(key=lambda r: r['slot'])
    seen = {}
    for r in results:
        slot = r['slot']
        if slot not in seen:
            seen[slot] = r
        else:
            existing = seen[slot]
            if (not existing['caption'] and r['caption']) or \
               (not existing['items'] and r['items']):
                seen[slot] = r

    print(f"\n{'Slot':>5}  {'Object':<22}  {'Type':<22}  {'Caption / Items'}")
    print('-' * 110)
    for slot in sorted(seen.keys()):
        r = seen[slot]
        if r['items']:
            label = ' | '.join(r['items'][:3])
        else:
            label = r['caption']
        print(f"  {slot:>3}  {r['obj_name']:<22}  {r['obj_type']:<22}  {label}")

    print(f"\nTotal unique YN slots: {len(seen)}")

    out_path = os.path.join(os.path.dirname(__file__), '_tmp_mdefaults_yn_v2.tsv')
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write('slot\tobj_name\tobj_type\tcaption\titems\tline\n')
        for slot in sorted(seen.keys()):
            r = seen[slot]
            items_str = ' | '.join(r['items'])
            f.write(f"{slot}\t{r['obj_name']}\t{r['obj_type']}\t{r['caption']}\t{items_str}\t{r['line']}\n")
    print(f"Saved: {out_path}")

if __name__ == '__main__':
    main()
