"""Find all module keys in modules.py - comprehensive search."""
import re

with open(r'learnevo-help/content/modules.py', encoding='utf-8') as f:
    content = f.read()

# Find all top-level dict keys (patterns like: "XX": """ at start of line)
keys_with_lines = []
for m in re.finditer(r'^"([^"]+)"\s*:', content, re.MULTILINE):
    line_num = content[:m.start()].count('\n') + 1
    keys_with_lines.append((line_num, m.group(1)))

print(f"Total keys: {len(keys_with_lines)}")
print("\nAll keys (line, key):")
for line, key in keys_with_lines:
    print(f"  {line:5d}: {key}")
