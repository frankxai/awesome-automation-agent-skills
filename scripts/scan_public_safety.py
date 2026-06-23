#!/usr/bin/env python3
"""Scan docs for common private automation leakage markers."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


PATTERNS = {
    "local_windows_path": re.compile(r"[A-Za-z]:\\\\Users\\\\", re.IGNORECASE),
    "local_unix_path": re.compile(r"/Users/[^\\s]+|/home/[^\\s]+"),
    "secret_label": re.compile(r"(?i)(api[_-]?key|secret|token|password)\\s*[:=]\\s*['\\\"]?[^\\s'\\\"]{8,}"),
    "bearer_token": re.compile(r"(?i)bearer\\s+[a-z0-9._\\-]{16,}"),
    "webhook_url": re.compile(r"https://[^\\s)\\]\"]*(webhook|hook)[^\\s)\\]\"]*", re.IGNORECASE),
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="?", default=".")
    args = parser.parse_args()
    root = Path(args.path).resolve()
    findings: list[str] = []
    for path in root.rglob("*"):
        if path.is_dir() or ".git" in path.parts:
            continue
        if path.name == "scan_public_safety.py":
            continue
        if path.suffix.lower() not in {".md", ".json", ".yml", ".yaml", ".py"}:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for name, pattern in PATTERNS.items():
            for match in pattern.finditer(text):
                rel = path.relative_to(root)
                line = text.count("\n", 0, match.start()) + 1
                findings.append(f"{rel}:{line}: {name}")
    if findings:
        print("Sensitive markers found:")
        for finding in findings:
            print(f"- {finding}")
        return 1
    print("No obvious sensitive markers found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
