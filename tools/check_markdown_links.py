from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).resolve().parents[1]
IGNORED_DIRS = {".git", ".venv", "__pycache__", ".pytest_cache"}
LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


def markdown_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*.md"):
        if any(part in IGNORED_DIRS for part in path.parts):
            continue
        files.append(path)
    return files


def is_external(target: str) -> bool:
    parsed = urlparse(target)
    return parsed.scheme in {"http", "https", "mailto"}


def strip_fragment(target: str) -> str:
    return target.split("#", 1)[0]


def main() -> int:
    failures: list[str] = []
    for file in markdown_files():
        text = file.read_text(encoding="utf-8")
        for match in LINK_RE.finditer(text):
            target = match.group(1).strip()
            if not target or is_external(target):
                continue
            if target.startswith("#"):
                continue

            clean_target = unquote(strip_fragment(target))
            if not clean_target:
                continue

            linked_path = (file.parent / clean_target).resolve()
            try:
                linked_path.relative_to(ROOT)
            except ValueError:
                failures.append(f"{file.relative_to(ROOT)}: link escapes repo: {target}")
                continue

            if not linked_path.exists():
                failures.append(f"{file.relative_to(ROOT)}: missing link target: {target}")

    if failures:
        print("Markdown link check failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Markdown link check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

