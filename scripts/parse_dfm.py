"""
Parse a Delphi DFM (text form) file into a structured tree.

DFM grammar (text variant):
    unit     := 'object' ident ':' ident CRLF property* unit* 'end' CRLF
    property := ident '=' value CRLF
    value    := literal | '[' ... ']' | '{' hex '}' | '(' ... ')' | string

We deliberately keep the parser lenient — we only need to walk the
object tree and capture scalar properties. Binary blobs (Icon.Data,
Glyph.Data, etc.) are collected but their contents summarized as a
byte-count.

Usage:
    python parse_dfm.py <file.dfm>            -> pretty tree
    python parse_dfm.py <file.dfm> --json     -> JSON AST
    python parse_dfm.py <dir> --summary       -> per-file field summary
"""
from __future__ import annotations
import json
import re
import sys
from dataclasses import dataclass, field, asdict
from pathlib import Path

IDENT = r"[A-Za-z_][A-Za-z0-9_.]*"
OBJECT_RE = re.compile(rf"^(\s*)(object|inherited)\s+({IDENT})\s*:\s*({IDENT})\s*$")
END_RE = re.compile(r"^(\s*)end\s*$")
PROP_RE = re.compile(rf"^(\s*)({IDENT})\s*=\s*(.*)$")


@dataclass
class Obj:
    name: str
    cls: str
    kind: str = "object"        # 'object' or 'inherited'
    props: dict = field(default_factory=dict)
    children: list = field(default_factory=list)


def parse(text: str) -> Obj:
    lines = text.splitlines()
    stack: list[Obj] = []
    root = None
    i = 0

    def take_multiline_value(start_value: str, i: int) -> tuple[str, int]:
        """Consume the continuation of multi-line values like hex {} or sets []."""
        value = start_value
        openers = "{[("
        closers = "}])"
        depth = sum(value.count(c) for c in openers) - sum(value.count(c) for c in closers)
        # String continuation: lines starting with a quote
        if value.startswith("'") and not (value.rstrip().endswith("'") and len(value) > 1):
            while i < len(lines):
                nxt = lines[i]
                value += " " + nxt.strip()
                i += 1
                if nxt.rstrip().endswith("'"):
                    break
            return value, i
        while depth > 0 and i < len(lines):
            nxt = lines[i]
            value += "\n" + nxt
            depth += sum(nxt.count(c) for c in openers) - sum(nxt.count(c) for c in closers)
            i += 1
        return value, i

    while i < len(lines):
        line = lines[i]
        i += 1
        if not line.strip():
            continue
        m = OBJECT_RE.match(line)
        if m:
            _, kind, name, cls = m.groups()
            obj = Obj(name=name, cls=cls, kind=kind)
            if stack:
                stack[-1].children.append(obj)
            else:
                root = obj
            stack.append(obj)
            continue
        m = END_RE.match(line)
        if m:
            if stack:
                stack.pop()
            continue
        m = PROP_RE.match(line)
        if m and stack:
            _, prop_name, value = m.groups()
            value, i = take_multiline_value(value.strip(), i)
            # Summarize binary blobs
            if value.startswith("{") and "\n" in value:
                raw = value.strip("{}\n ").replace("\n", "").replace(" ", "")
                value = f"<HEX {len(raw)//2} bytes>"
            stack[-1].props[prop_name] = value
    return root


def iter_all(obj: Obj, depth: int = 0):
    yield obj, depth
    for c in obj.children:
        yield from iter_all(c, depth + 1)


def summary(obj: Obj) -> dict:
    """Per-form summary: root caption, class counts, key field/caption text."""
    class_counts: dict[str, int] = {}
    captions: list[str] = []
    field_names: list[str] = []
    for node, _ in iter_all(obj):
        class_counts[node.cls] = class_counts.get(node.cls, 0) + 1
        cap = node.props.get("Caption")
        if cap and cap.startswith("'") and cap.endswith("'"):
            captions.append(cap.strip("'"))
        fn = node.props.get("FieldName")
        if fn:
            field_names.append(fn.strip("'"))
    return {
        "root": obj.name,
        "root_class": obj.cls,
        "caption": obj.props.get("Caption", "").strip("'"),
        "class_counts": class_counts,
        "captions": captions,
        "field_names": field_names,
    }


def pretty(obj: Obj, indent: int = 0) -> str:
    pad = "  " * indent
    out = [f"{pad}{obj.kind} {obj.name}: {obj.cls}"]
    for k, v in obj.props.items():
        val = v if len(v) < 80 else v[:77] + "..."
        out.append(f"{pad}  {k} = {val}")
    for c in obj.children:
        out.append(pretty(c, indent + 1))
    return "\n".join(out)


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    path = Path(argv[1])
    mode = argv[2] if len(argv) > 2 else "--pretty"

    if path.is_dir():
        rows = []
        for p in sorted(path.glob("**/*.dfm")) + sorted(path.glob("**/*.DFM")):
            try:
                tree = parse(p.read_text(encoding="latin-1"))
                s = summary(tree)
                rows.append({"file": str(p.relative_to(path)), **s})
            except Exception as e:  # noqa
                rows.append({"file": str(p.relative_to(path)), "error": str(e)})
        if mode == "--json":
            print(json.dumps(rows, indent=2))
        else:
            for r in rows:
                if "error" in r:
                    print(f"ERR {r['file']}: {r['error']}")
                    continue
                cls_str = ", ".join(f"{k}:{v}" for k, v in sorted(r["class_counts"].items()) if k.startswith("T"))
                print(f"{r['file']:<40} {r['caption'][:50]:<50}  ({len(r['field_names'])} fields)  [{cls_str}]")
        return 0

    text = path.read_text(encoding="latin-1")
    tree = parse(text)
    if mode == "--json":
        def _serialize(o: Obj):
            return {"name": o.name, "cls": o.cls, "kind": o.kind, "props": o.props, "children": [_serialize(c) for c in o.children]}
        print(json.dumps(_serialize(tree), indent=2))
    elif mode == "--summary":
        print(json.dumps(summary(tree), indent=2))
    else:
        print(pretty(tree))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
