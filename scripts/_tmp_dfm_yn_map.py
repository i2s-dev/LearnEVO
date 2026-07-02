"""
Parse T7MDefNDC.DFM: match TLabel captions to TTASENTER FieldName bindings
by positional order within each container (TabSheet/TPanel/TGroupBox).

DFM layout: all labels defined first within a container, then all input controls.
Label[i] → Control[i] within the same container.
"""

import re
import sys

DFM_PATH = r"C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\samples\dfm_parsed\T7MDefNDC.DFM"

def parse_dfm_yn_map(path):
    with open(path, 'r', encoding='utf-8', errors='replace') as f:
        lines = f.readlines()

    # Stack-based container tracking
    # Each entry: {'name': str, 'type': str, 'caption': str, 'labels': [], 'controls': []}
    # labels = [(order, caption_text)]
    # controls = [(order, fieldname)]

    container_stack = []
    current_obj_type = None
    current_obj_name = None
    current_fieldname = None
    current_caption = None
    obj_order = [0]  # global object order counter (mutable via list)

    # Containers we care about for matching
    CONTAINER_TYPES = {'TTabSheet', 'TPanel', 'TGroupBox', 'TScrollBox'}
    LABEL_TYPES = {'TLabel', 'TStaticText'}
    CONTROL_TYPES = {'TTASENTER', 'TTASNumEnter', 'TTASMemo', 'TCheckBox', 'TEdit',
                     'TComboBox', 'TTASCheckBox', 'TTASComboBox'}

    # Results: list of (container_path, label_caption, fieldname) tuples
    results = []

    # Per-container state
    # For each container on stack, track labels and controls seen so far
    container_data = []  # parallel to container_stack: [{'labels': [(order,cap)], 'controls': [(order,fn)]}]

    depth = 0
    i = 0
    n = len(lines)

    while i < n:
        line = lines[i].rstrip()
        stripped = line.strip()

        # Detect 'object Name: Type'
        obj_match = re.match(r'\s*object\s+(\w+)\s*:\s*(\w+)', line)
        if obj_match:
            obj_order[0] += 1
            oname = obj_match.group(1)
            otype = obj_match.group(2)
            depth += 1

            if otype in CONTAINER_TYPES:
                container_stack.append({'name': oname, 'type': otype, 'caption': ''})
                container_data.append({'labels': [], 'controls': []})
            elif otype in LABEL_TYPES:
                # Scan ahead to find Caption for this label
                cap = ''
                j = i + 1
                while j < n and not re.match(r'\s*end\b', lines[j]) and not re.match(r'\s*object\s+', lines[j]):
                    cm = re.match(r"\s*Caption\s*=\s*'(.*)'", lines[j])
                    if cm:
                        cap = cm.group(1)
                        # Handle concatenated strings like 'foo'#39's' → "foo's"
                        cap = re.sub(r"#(\d+)", lambda m: chr(int(m.group(1))), cap)
                        break
                    j += 1
                if container_data:
                    container_data[-1]['labels'].append((obj_order[0], cap))
            elif otype in CONTROL_TYPES:
                # Scan ahead to find FieldName for this control
                fn = ''
                j = i + 1
                while j < n and not re.match(r'\s*end\b', lines[j]) and not re.match(r'\s*object\s+', lines[j]):
                    fm = re.match(r"\s*FieldName\s*=\s*'([^']*)'", lines[j])
                    if fm:
                        fn = fm.group(1)
                        break
                    j += 1
                if container_data and fn:
                    container_data[-1]['controls'].append((obj_order[0], fn))

        # Detect 'end'
        elif re.match(r'\s*end\b', stripped):
            if container_stack and depth == len(container_stack):
                # Closing a container
                cinfo = container_stack.pop()
                cdata = container_data.pop()

                # Build path
                path_parts = [c['name'] for c in container_stack] + [cinfo['name']]
                cpath = ' > '.join(path_parts[-3:])  # last 3 levels for readability

                labels = cdata['labels']
                controls = cdata['controls']

                # Match by position
                for idx in range(min(len(labels), len(controls))):
                    lorder, lcap = labels[idx]
                    corder, cfn = controls[idx]
                    results.append((cpath, lcap, cfn))

                # Pass up unmatched labels/controls to parent (if present)
                # (some containers have nested containers that already consumed their labels)
                # Don't pass up — this approach is per-container only

            depth -= 1

        i += 1

    return results

results = parse_dfm_yn_map(DFM_PATH)

# Filter for bkys.yn[N] FieldNames
yn_results = [(path, cap, fn) for (path, cap, fn) in results if re.match(r'bkys\.yn\[\d+\]', fn)]

# Sort by N
def yn_key(r):
    m = re.search(r'\[(\d+)\]', r[2])
    return int(m.group(1)) if m else 999

yn_results.sort(key=yn_key)

print(f"Total matched pairs: {len(results)}")
print(f"YN slot matches: {len(yn_results)}")
print()
print(f"{'Slot':<12} {'Caption':<60} {'Container'}")
print('-' * 120)
for path, cap, fn in yn_results:
    slot = re.search(r'\[(\d+)\]', fn).group(1)
    print(f"YN[{slot:<8}] {cap:<60} {path}")

# Also show all ists.cfg.* mappings
print()
print("=== ISTS.CFG KEY MAPPINGS ===")
cfg_results = [(path, cap, fn) for (path, cap, fn) in results if fn.startswith('ists.cfg.')]
cfg_results.sort(key=lambda r: r[2])
for path, cap, fn in cfg_results:
    print(f"{fn:<30} {cap:<60} {path}")
