"""Extract readable text from a decompiled EvoHELP topic.

Usage: python chm_to_md.py <topic.htm> [<topic.htm> ...]

Prints a markdown-ish rendering of the body text (content of #innerdiv)
with span/style cruft removed and <a> links kept as [text](href).
"""
import html as html_mod
import io
import re
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

CHM_DIR = Path(__file__).resolve().parents[1] / "samples" / "chm" / "extracted"


def extract_body(html: str) -> str:
    m = re.search(r'<div id="innerdiv">(.*?)</div></div>', html, re.S)
    return m.group(1) if m else html


def render(html: str) -> str:
    html = re.sub(r"<!--.*?-->", "", html, flags=re.S)
    html = re.sub(r"<script[^>]*>.*?</script>", "", html, flags=re.S | re.I)
    html = re.sub(r"<style[^>]*>.*?</style>", "", html, flags=re.S | re.I)

    # Links -> markdown
    def link_sub(m: re.Match) -> str:
        href = m.group(1)
        text = re.sub(r"<[^>]+>", "", m.group(2)).strip()
        return f"[{text}]({href})"

    html = re.sub(
        r'<a[^>]*href="([^"]+)"[^>]*>(.*?)</a>', link_sub, html, flags=re.S | re.I
    )

    # Block breaks
    html = re.sub(r"</p\s*>", "\n\n", html, flags=re.I)
    html = re.sub(r"<br\s*/?>", "\n", html, flags=re.I)
    html = re.sub(r"</li\s*>", "\n", html, flags=re.I)
    html = re.sub(r"<li[^>]*>", "- ", html, flags=re.I)
    html = re.sub(r"</tr\s*>", "\n", html, flags=re.I)
    html = re.sub(r"</td\s*>", " | ", html, flags=re.I)

    # Kill remaining tags
    html = re.sub(r"<[^>]+>", "", html)

    # Normalize whitespace (nbsp -> space)
    html = html_mod.unescape(html).replace("\xa0", " ")
    html = re.sub(r"[ \t]+", " ", html)
    html = re.sub(r"\n[ \t]+", "\n", html)
    html = re.sub(r"\n{3,}", "\n\n", html)
    return html.strip()


def process(path: Path) -> str:
    text = path.read_text(encoding="utf-8", errors="replace")
    title_m = re.search(r"<title>(.*?)</title>", text, re.I | re.S)
    title = title_m.group(1).strip() if title_m else path.stem
    body = render(extract_body(text))
    return f"# {title}\n\n*Source: `samples/chm/extracted/{path.name}`*\n\n{body}\n"


def main() -> None:
    args = sys.argv[1:] or []
    if not args:
        print(__doc__)
        sys.exit(1)
    for name in args:
        p = Path(name)
        if not p.is_absolute():
            p = CHM_DIR / name
        print(process(p))
        print("\n---\n")


if __name__ == "__main__":
    main()
