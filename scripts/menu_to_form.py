"""Cross-reference menu codes to DFM forms."""
import csv
import re
from collections import defaultdict

BASE = r"c:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\samples"

menu = {}
for r in csv.DictReader(open(BASE + r"\menu_codes.csv")):
    menu[r["code"]] = r["description"]

dfms = list(csv.DictReader(open(BASE + r"\dfm_parsed\dfm_summary.csv")))

dfm_by_code = defaultdict(list)
for r in dfms:
    name = r["file"].upper()
    # Strip extension and trailing qualifiers
    stem = name.replace(".DFM", "")
    # Match T7XX Y [Z?][rest?] - T7INA, T7INA2, T7INAE, etc.
    m = re.match(r"^(T7|T6|BK)([A-Z]{2})([A-Z])([A-Z]?)", stem)
    if m:
        mod = m.group(2)
        l1 = m.group(3)
        l2 = m.group(4)
        # Only treat l2 as a sub-operation letter if there's nothing else after it
        # Actually let's produce both codes: XX-Y and XX-Y-Z (when Z is alpha)
        code = f"{mod}-{l1}"
        dfm_by_code[code].append(r["file"])
        if l2:
            code2 = f"{mod}-{l1}-{l2}"
            dfm_by_code[code2].append(r["file"])

with open(BASE + r"\menu_to_form.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["code", "description", "dfms"])
    for code in sorted(menu):
        w.writerow([code, menu[code], ";".join(dfm_by_code.get(code, []))])

matched = sum(1 for c in menu if dfm_by_code.get(c))
print(f"Menu codes: {len(menu)}, with at least 1 matching DFM: {matched}")

# Write Markdown table
with open(BASE + r"\menu_to_form.md", "w", encoding="utf-8") as f:
    f.write("# Menu Code → DFM Form Cross-Reference\n\n")
    f.write(f"Total menu codes: **{len(menu)}**. With at least 1 matching DFM form: **{matched}** ({matched*100//len(menu)}%).\n\n")
    f.write("| Code | Description | DFM(s) |\n|---|---|---|\n")
    for code in sorted(menu):
        desc = menu[code].replace("|", "\\|")
        dfms_list = dfm_by_code.get(code, [])
        dfs = ", ".join(f"`{d}`" for d in dfms_list[:5])
        f.write(f"| `{code}` | {desc} | {dfs} |\n")

print("Wrote menu_to_form.csv and menu_to_form.md")
