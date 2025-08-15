#!/usr/bin/env python3
# file: scripts/fix-import-paths.py
# version: 1.0.0
# guid: 2a4d6f18-5c6b-4e9f-9b8a-1c2d3e4f5a6b

import glob
import re
from pathlib import Path

MODULES = [
    "auth",
    "cache",
    "common",
    "config",
    "db",
    "health",
    "log",
    "media",
    "metrics",
    "notification",
    "organization",
    "queue",
    "web",
]

IMPORT_RE = re.compile(
    r'^(\s*)import\s+"(?P<path>(?P<mod>'
    + "|".join(MODULES)
    + ')/proto/[^"]+)"\s*;\s*$',
    re.MULTILINE,
)
PKG_IMPORT_RE = re.compile(
    r'^(\s*)import\s+"pkg/(?P<mod>'
    + "|".join(MODULES)
    + ')/proto/(?P<rest>[^"]+)"\s*;\s*$',
    re.MULTILINE,
)


def normalize_imports(content: str, file_pkg_path: str) -> str:
    # 1) Rewrite non-pkg imports to pkg/
    def _rewrite(m):
        indent = m.group(1)
        path = m.group("path")
        # Avoid double-prefixing if already has pkg/
        if path.startswith("pkg/"):
            return m.group(0)
        return f'{indent}import "pkg/{path}";'

    content = IMPORT_RE.sub(_rewrite, content)

    # 2) De-duplicate imports and drop self-import
    lines = content.splitlines()
    seen = set()
    out_lines = []

    # Determine file's import path for self-import comparison
    # Convert absolute file path to import path like pkg/<module>/proto/<file>
    file_import_path = file_pkg_path

    for line in lines:
        m = re.match(r'^(\s*)import\s+"([^"]+)"\s*;\s*$', line)
        if not m:
            out_lines.append(line)
            continue
        path = m.group(2)
        # Drop self-import
        if path == file_import_path:
            continue
        key = path
        if key in seen:
            continue
        seen.add(key)
        out_lines.append(line)

    return "\n".join(out_lines) + ("\n" if content.endswith("\n") else "")


def main():
    proto_files = glob.glob("pkg/*/proto/**/*.proto", recursive=True)
    fixed = 0
    for fp in proto_files:
        try:
            with open(fp, "r", encoding="utf-8") as f:
                content = f.read()
            # Build import path for this file (pkg/<module>/proto/<...>)
            rel = Path(fp).as_posix()
            # expect path like pkg/<module>/proto/<...>
            if not rel.startswith("pkg/"):
                continue
            file_pkg_path = rel
            newc = normalize_imports(content, file_pkg_path)
            if newc != content:
                with open(fp, "w", encoding="utf-8") as f:
                    f.write(newc)
                fixed += 1
                print(f"Fixed imports: {fp}")
        except Exception as e:
            print(f"Error fixing {fp}: {e}")
    print(f"\nUpdated {fixed} files with corrected import paths and deduped imports.")


if __name__ == "__main__":
    main()
