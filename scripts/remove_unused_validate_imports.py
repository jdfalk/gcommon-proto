#!/usr/bin/env python3
# file: scripts/remove_unused_validate_imports.py
# version: 1.0.0
# guid: 7f5b9c2e-3d4a-4b6c-8f2d-9a1b2c3d4e5f

"""Remove unused `buf/validate/validate.proto` imports from .proto files.

Criteria for removal:
  * File contains a line: import "buf/validate/validate.proto";
  * File does NOT contain the substring "(buf.validate." (indicates no validation options used)

When removing the import, the script will bump the patch component of the
semantic version in the header comment line beginning with `// version:`.

The script is idempotent – running it again will make no further changes.
"""

from __future__ import annotations

import re
from pathlib import Path

RE_VALIDATE_IMPORT = re.compile(
    r'^import\s+"buf/validate/validate\.proto";\s*$', re.MULTILINE
)
RE_VERSION = re.compile(r"^(//\s*version:\s*)(\d+)\.(\d+)\.(\d+)(\s*)$", re.MULTILINE)

PROTO_ROOT = Path("proto")


def bump_patch(version_line: str) -> str:
    match = RE_VERSION.match(version_line)
    if not match:
        return version_line
    prefix, major, minor, patch, suffix = match.groups()
    new_patch = str(int(patch) + 1)
    return f"{prefix}{major}.{minor}.{new_patch}{suffix}"


def process_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")

    # Quick exits
    if "buf/validate/validate.proto" not in text:
        return False
    if "(buf.validate." in text:
        return False  # import is used

    # Remove the import line (handle potential trailing spaces)
    new_text, removed = RE_VALIDATE_IMPORT.subn("", text)
    if not removed:
        return False

    # Collapse any accidental double blank lines created by removal (only local cleanup)
    new_text = re.sub(r"\n{3,}", "\n\n", new_text)

    # Bump version line
    def _bump(m: re.Match) -> str:
        return bump_patch(m.group(0))

    new_text, version_subs = RE_VERSION.subn(_bump, new_text, count=1)

    if new_text != text:
        path.write_text(new_text, encoding="utf-8")
        print(f"Updated: {path} (removed unused validate import, version patch bumped)")
        if version_subs == 0:
            print(f"  NOTE: No version line found to bump in {path}")
        return True
    return False


def main() -> None:
    proto_files = list(PROTO_ROOT.rglob("*.proto"))
    modified = 0
    for f in proto_files:
        try:
            modified |= process_file(f)  # bitwise OR collects if any True
        except Exception as e:  # pragma: no cover (defensive)
            print(f"ERROR processing {f}: {e}")
    if not modified:
        print("No unused validate imports removed.")
    else:
        print("Completed removal of unused validate imports.")


if __name__ == "__main__":
    main()
