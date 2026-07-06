"""
Hierarchical DFM parser for T7MDefNDC.DFM.
Extracts label captions for all controls with FieldName = 'BKYS.YN[N]'.

Strategy:
- Parse the DFM into a tree of objects (tracking depth via object/end).
- Each object node has: type, name, properties (dict), children (list).
- For each leaf TTabSheet (one that contains controls directly, not sub-sheets):
    * Collect all TLabel/TDBText nodes -> {top: caption}
    * Collect all controls with FieldName='BKYS.YN[N]' -> {top: yn_slot}
    * Match label to control by nearest Top within same container (within 40px)
- Output: sorted YN slot -> (label_caption, container_path, top, allowed_chars)
"""

import re
import sys

DFM_PATH = r"c:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\samples\dfm_parsed\T7MDefNDC.DFM"

# ---------------------------------------------------------------------------
# Tokeniser: yields (indent_level, keyword, rest_of_line)
# keyword is 'object', 'end', or 'prop'
# ---------------------------------------------------------------------------

def tokenise(path):
    with open(path, encoding='utf-8', errors='replace') as f:
        lines = f.readlines()
    i = 0
    while i < len(lines):
        raw = lines[i]
        stripped = raw.rstrip('\n')
        indent = len(stripped) - len(stripped.lstrip())
        content = stripped.strip()
        if content.startswith('object '):
            yield (indent, 'object', content[7:], i+1)
            i += 1
        elif content == 'end':
            yield (indent, 'end', '', i+1)
            i += 1
        else:
            # Multi-line values: accumulate until a line that looks like the start
            # of a new property or 'end' or 'object'
            value = content
            # Handle multi-line blocks (icon data, strings, etc.) by consuming
            # continuation lines (those that don't start a new property/object/end)
            while i + 1 < len(lines):
                next_raw = lines[i+1].rstrip('\n')
                next_stripped = next_raw.strip()
                if (next_stripped.startswith('object ') or
                        next_stripped == 'end' or
                        re.match(r'^[A-Za-z_][A-Za-z0-9_.]*\s*=', next_stripped)):
                    break
                value += '\n' + next_stripped
                i += 1
            yield (indent, 'prop', value, i+1)
            i += 1


# ---------------------------------------------------------------------------
# Tree builder
# ---------------------------------------------------------------------------

class DFMNode:
    __slots__ = ('obj_type', 'obj_name', 'props', 'children', 'lineno')
    def __init__(self, obj_type, obj_name, lineno):
        self.obj_type = obj_type
        self.obj_name = obj_name
        self.props = {}      # prop_name -> raw value string
        self.children = []
        self.lineno = lineno

    def __repr__(self):
        return f'<{self.obj_type} {self.obj_name}>'


def build_tree(tokens):
    """Build tree from token stream. Returns root node."""
    root = DFMNode('__root__', '__root__', 0)
    stack = [root]

    for tok in tokens:
        indent, kind, text, lineno = tok
        if kind == 'object':
            # parse "Name: Type"
            m = re.match(r'(\w+)\s*:\s*(\w+)', text)
            if m:
                name, otype = m.group(1), m.group(2)
            else:
                name, otype = text, 'Unknown'
            node = DFMNode(otype, name, lineno)
            stack[-1].children.append(node)
            stack.append(node)
        elif kind == 'end':
            if len(stack) > 1:
                stack.pop()
        elif kind == 'prop':
            # parse "PropName = value"
            m = re.match(r'([A-Za-z_][A-Za-z0-9_.]*)\s*=\s*(.*)', text, re.DOTALL)
            if m and stack:
                pname = m.group(1)
                pval = m.group(2).strip()
                stack[-1].props[pname] = pval

    return root


# ---------------------------------------------------------------------------
# Extract YN bindings
# ---------------------------------------------------------------------------

YN_RE = re.compile(r"BKYS\.YN\[(\d+)\]", re.IGNORECASE)


def get_int_prop(node, prop, default=None):
    val = node.props.get(prop)
    if val is None:
        return default
    try:
        return int(val)
    except (ValueError, TypeError):
        return default


def get_str_prop(node, prop, default=''):
    val = node.props.get(prop, default)
    # Strip Delphi string delimiters if present
    if val.startswith("'") and val.endswith("'"):
        val = val[1:-1]
    return val


def collect_yn_controls(node, path, results):
    """
    Recursively walk tree. When we reach a container that has YN-bound controls,
    match labels to controls within that container.
    """
    # Collect labels and yn-controls that are DIRECT children of this node
    labels = []    # (top, caption)
    yn_ctrls = []  # (top, yn_slot, obj_type, allowed_chars)

    for child in node.children:
        ctype = child.obj_type
        top = get_int_prop(child, 'Top', -1)
        caption = get_str_prop(child, 'Caption')
        field = get_str_prop(child, 'FieldName')
        allowed = get_str_prop(child, 'AllowedChrs')

        if ctype in ('TLabel', 'TDBText') and caption:
            labels.append((top, caption))

        fn_match = YN_RE.search(field)
        if fn_match:
            slot = int(fn_match.group(1))
            yn_ctrls.append((top, slot, ctype, allowed, child.obj_name))

    # Match yn_ctrls to nearest label within 40px
    if yn_ctrls:
        for (ctrl_top, slot, ctype, allowed, cname) in yn_ctrls:
            best_label = None
            best_dist = 999
            for (lbl_top, lbl_cap) in labels:
                dist = abs(lbl_top - ctrl_top)
                if dist < best_dist:
                    best_dist = dist
                    best_label = lbl_cap
            results.append({
                'slot': slot,
                'label': best_label if best_dist <= 40 else '(no label found)',
                'path': path + '/' + node.obj_name,
                'ctrl_top': ctrl_top,
                'ctrl_type': ctype,
                'allowed': allowed,
                'ctrl_name': cname,
                'label_dist': best_dist,
            })

    # Recurse into children
    child_path = path + '/' + node.obj_name
    for child in node.children:
        collect_yn_controls(child, child_path, results)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print("Parsing DFM...", flush=True)
    tokens = list(tokenise(DFM_PATH))
    print(f"  {len(tokens)} tokens", flush=True)
    root = build_tree(iter(tokens))
    print("  Tree built", flush=True)

    results = []
    collect_yn_controls(root, '', results)

    # Sort by slot number
    results.sort(key=lambda r: r['slot'])

    print(f"\n{'='*80}")
    print(f"YN slot bindings found: {len(results)}")
    print(f"{'='*80}\n")
    print(f"{'Slot':<6} {'Label':<50} {'Allowed':<15} {'Path'}")
    print(f"{'-'*6} {'-'*50} {'-'*15} {'-'*40}")

    seen_slots = set()
    for r in results:
        slot = r['slot']
        dup = '*' if slot in seen_slots else ' '
        seen_slots.add(slot)
        label = (r['label'] or '').replace('\n', ' ')[:50]
        allowed = (r['allowed'] or '')[:15]
        path_short = r['path'].replace('/__root__/', '')[-60:]
        print(f"{slot:<5}{dup} {label:<50} {allowed:<15} {path_short}")

    # Also print any slots where label_dist > 40 (failed matches)
    bad = [r for r in results if r['label_dist'] > 40]
    if bad:
        print(f"\n--- {len(bad)} slots with no label match (dist > 40): ---")
        for r in bad:
            print(f"  YN[{r['slot']}] ctrl_top={r['ctrl_top']} dist={r['label_dist']} path={r['path']}")

    return results


if __name__ == '__main__':
    main()
