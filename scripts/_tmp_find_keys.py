"""Find all module keys in modules.py."""
import re

with open(r'learnevo-help/content/modules.py', encoding='utf-8') as f:
    lines = f.readlines()

targets = {'NE','EM','PA','AL','SE','CH','ML','SE'}
for i, line in enumerate(lines, 1):
    m = re.match(r'^"([A-Z]{2,4})"\s*:', line)
    if m and m.group(1) in targets:
        print(f"Line {i}: {line.rstrip()[:80]}")
        # Also print next 2 lines for context
        if i < len(lines):
            print(f"  +1: {lines[i].rstrip()[:80]}")
        if i+1 < len(lines):
            print(f"  +2: {lines[i+1].rstrip()[:80]}")
