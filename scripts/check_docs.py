#!/usr/bin/env python3
"""Check this documentation repository without reading live DNS or account data."""

import re
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


def main() -> None:
    required = [ROOT / "README.md", ROOT / "AGENTS.md", ROOT / "docs/current-state.md"]
    for path in required:
        if not path.is_file():
            raise SystemExit(f"missing required document: {path.relative_to(ROOT)}")

    for document in ROOT.rglob("*.md"):
        for number, line in enumerate(document.read_text(encoding="utf-8").splitlines(), 1):
            if line.rstrip() != line:
                raise SystemExit(f"trailing whitespace: {document.relative_to(ROOT)}:{number}")
            for match in LINK.finditer(line):
                target = unquote(match.group(1).split("#", 1)[0])
                if not target or "://" in target or target.startswith("mailto:"):
                    continue
                resolved = (document.parent / target).resolve()
                if not resolved.is_relative_to(ROOT) or not resolved.is_file():
                    raise SystemExit(f"broken local link: {document.relative_to(ROOT)}:{number}: {target}")
    print("Documentation links and whitespace: OK")


if __name__ == "__main__":
    main()
