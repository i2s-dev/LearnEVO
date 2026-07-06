"""
Extract BKYS.YN[N] and ISTS.CFG.* references from all 7 SRC files.
Goal: find confirmed YN slot -> meaning mappings from readable TAS Pro source.
Also look for comments that explain what each BKYS.YN[N] controls.
"""
import re, os, sys, io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

SRC_DIR = r'samples\src'
SRC_FILES = ['BKAPH.SRC', 'BKAPHA.SRC', 'BKAWLB.SRC', 'BKDCA.SRC', 'BKLME.SRC', 'BKMRF.SRC', 'BKROA.SRC']

# Pattern to find BKYS.YN[N] with context
yn_pat = re.compile(r'BKYS\.YN\[(\d+)\]')
# Also case-insensitive versions
yn_pat_ci = re.compile(r'(?i)BKYS\.YN\[(\d+)\]')
cfg_pat = re.compile(r'(?i)ISTS\.CFG\.([A-Z0-9.]+)')
# Look for comments near YN references
comment_pat = re.compile(r'\*.*$', re.MULTILINE)

all_yn_refs = {}  # slot -> [(file, lineno, line, context_lines)]
all_cfg_refs = {}  # key -> [(file, lineno, line)]
cfg_yn_pairs = []  # (file, lineno, yn_slot, cfg_key, line)

for fname in SRC_FILES:
    fpath = os.path.join(SRC_DIR, fname)
    if not os.path.exists(fpath):
        print(f"NOT FOUND: {fpath}")
        continue

    # Try reading with different encodings
    for enc in ['cp1252', 'latin-1', 'utf-8']:
        try:
            with open(fpath, encoding=enc) as f:
                lines = f.readlines()
            break
        except:
            continue

    module = fname.replace('.SRC', '')
    print(f"\n{'='*60}")
    print(f"FILE: {fname} ({len(lines)} lines)")
    print(f"{'='*60}")

    for lineno, line in enumerate(lines, 1):
        line_stripped = line.rstrip()

        # Find BKYS.YN[N] references
        for m in yn_pat_ci.finditer(line):
            slot = int(m.group(1))
            # Get context: current line + up to 3 surrounding lines
            ctx_start = max(0, lineno - 3)
            ctx_lines = lines[ctx_start:lineno + 2]
            ctx_text = ''.join(ctx_lines).strip()

            if slot not in all_yn_refs:
                all_yn_refs[slot] = []
            all_yn_refs[slot].append((module, lineno, line_stripped, ctx_text))

        # Find ISTS.CFG.* references
        for m in cfg_pat.finditer(line):
            key = 'ISTS.CFG.' + m.group(1).upper()
            if key not in all_cfg_refs:
                all_cfg_refs[key] = []
            all_cfg_refs[key].append((module, lineno, line_stripped))

# Print YN slot summary
print(f"\n\n{'='*60}")
print(f"BKYS.YN SLOT REFERENCES ACROSS ALL SRC FILES")
print(f"{'='*60}")
for slot in sorted(all_yn_refs.keys()):
    refs = all_yn_refs[slot]
    print(f"\nYN[{slot}] — {len(refs)} reference(s):")
    for module, lineno, line, ctx in refs:
        print(f"  {module}:{lineno}: {line.strip()}")
        # Show any comment lines in context
        for ctx_line in ctx.split('\n'):
            if ctx_line.strip().startswith('*') or 'YN[' in ctx_line or 'ISTS.CFG' in ctx_line.upper():
                if ctx_line.strip() != line.strip():
                    print(f"    > {ctx_line.strip()}")

# Print CFG key summary
print(f"\n\n{'='*60}")
print(f"ISTS.CFG.* REFERENCES ACROSS ALL SRC FILES")
print(f"{'='*60}")
for key in sorted(all_cfg_refs.keys()):
    refs = all_cfg_refs[key]
    print(f"\n{key} — {len(refs)} reference(s):")
    for module, lineno, line in refs:
        print(f"  {module}:{lineno}: {line.strip()}")
