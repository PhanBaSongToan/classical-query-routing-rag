"""Remove machine-specific absolute paths from generated Markdown reports."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


WINDOWS_PATH = re.compile(r"[A-Za-z]:[\\/](?:Users|home)[^`\s)]*", re.IGNORECASE)
POSIX_PATH = re.compile(r"/(?:home|Users)/[^`\s)]*")


def sanitize(root: Path) -> int:
    changed = 0
    for path in root.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        clean = WINDOWS_PATH.sub("<local-path>", text)
        clean = POSIX_PATH.sub("<local-path>", clean)
        if clean != text:
            path.write_text(clean, encoding="utf-8")
            changed += 1
    return changed


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path, help="Report directory to sanitize")
    args = parser.parse_args()
    print(f"Sanitized {sanitize(args.root)} Markdown report files.")


if __name__ == "__main__":
    main()
