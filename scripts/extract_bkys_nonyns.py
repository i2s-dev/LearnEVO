"""
extract_bkys_nonyns.py — Pass 385
Extract BKYSMSTR non-YN field bindings from T7MDefaults.DFM + T7MDefNDC.DFM.
Targets: bkys.num[N], bkys.vnum[N], bkys.date[N], bkys.desc[N]
Also queries live DSN=DBA for NUM/VNUM/DATE/DESC/WONUM/QCNUM/REQNUM/INVNUM/RBNUM values.
"""

import re
import sys

DFM_FILES = [
    r"C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\samples\T7MDefaults.DFM",
    r"C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\samples\dfm\T7MDefNDC.DFM",
]

FIELD_PATTERN = re.compile(r'bkys\.(num|vnum|date|desc)\[(\d+)\]', re.IGNORECASE)


def extract_dfm(path):
    results = []
    try:
        with open(path, 'r', encoding='latin-1', errors='replace') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"# File not found: {path}", file=sys.stderr)
        return results

    # Track current tab and last label
    current_tab = "(root)"
    last_label = "(no label)"
    last_label_line = 0
    current_obj = None
    current_obj_type = None
    current_fn = None
    current_line = 0

    for i, line in enumerate(lines):
        stripped = line.strip()

        # Detect tab sheet caption
        m_tab = re.match(r'object\s+\w+\s*:\s*TTabSheet', stripped)
        if m_tab:
            # Next Caption line sets the tab name
            for j in range(i+1, min(i+5, len(lines))):
                m_cap = re.match(r"Caption\s*=\s*'(.+)'", lines[j].strip())
                if m_cap:
                    current_tab = m_cap.group(1)
                    break

        # Detect labels
        m_lobj = re.match(r'object\s+(\w+)\s*:\s*TLabel', stripped)
        if m_lobj:
            for j in range(i+1, min(i+8, len(lines))):
                m_cap = re.match(r"Caption\s*=\s*'(.+)'", lines[j].strip())
                if m_cap:
                    cap = m_cap.group(1).strip()
                    if len(cap) > 2:
                        last_label = cap
                        last_label_line = i
                    break

        # Detect objects with FieldName matching bkys.num/vnum/date/desc
        m_obj = re.match(r'object\s+(\w+)\s*:\s*(\w+)', stripped)
        if m_obj:
            current_obj = m_obj.group(1)
            current_obj_type = m_obj.group(2)
            current_fn = None
            current_line = i

        if current_obj:
            m_fn = re.match(r"FieldName\s*=\s*'(.+)'", stripped)
            if m_fn:
                fn = m_fn.group(1)
                m_field = FIELD_PATTERN.match(fn)
                if m_field:
                    field_type = m_field.group(1).lower()
                    field_idx = int(m_field.group(2))
                    results.append({
                        'type': field_type,
                        'idx': field_idx,
                        'tab': current_tab,
                        'label': last_label,
                        'obj_type': current_obj_type,
                        'fieldname': fn,
                        'line': current_line + 1,
                        'source': path.split('\\')[-1],
                    })

        if stripped == 'end':
            current_obj = None
            current_obj_type = None

    return results


def query_live():
    try:
        import pyodbc
    except ImportError:
        print("# pyodbc not available — skipping live query", file=sys.stderr)
        return {}

    try:
        conn = pyodbc.connect('DSN=DBA', timeout=5)
        cur = conn.cursor()

        # Build column list for non-YN non-GL fields
        cols = ['BKYS_WONUM', 'BKYS_QCNUM', 'BKYS_REQNUM', 'BKYS_INVNUM', 'BKYS_RBNUM']
        for t in ['NUM', 'VNUM', 'DESC', 'DATE']:
            for n in range(1, 6):
                cols.append(f'BKYS_{t}_{n}')

        sql = f"SELECT {', '.join(cols)} FROM BKYSMSTR"
        cur.execute(sql)
        row = cur.fetchone()
        conn.close()

        if not row:
            return {}

        result = {}
        for i, col in enumerate(cols):
            val = row[i]
            if val is not None:
                result[col] = val
        return result

    except Exception as e:
        print(f"# ODBC error: {e}", file=sys.stderr)
        return {}


def main():
    all_results = []
    for path in DFM_FILES:
        all_results.extend(extract_dfm(path))

    all_results.sort(key=lambda r: (r['type'], r['idx']))

    print("FIELD_TYPE,IDX,TAB,LABEL,OBJ_TYPE,LINE,SOURCE")
    for r in all_results:
        label = r['label'].replace('"', "'")
        print(f"{r['type']},{r['idx']},\"{r['tab']}\",\"{label}\",{r['obj_type']},{r['line']},{r['source']}")

    print(f"\n# Total non-YN bindings found: {len(all_results)}", file=sys.stderr)

    print("\n\n=== LIVE BKYSMSTR VALUES (non-YN non-GL) ===")
    live = query_live()
    if live:
        for col, val in sorted(live.items()):
            print(f"  {col} = {repr(val)}")
    else:
        print("  (no live data)")


if __name__ == '__main__':
    main()
