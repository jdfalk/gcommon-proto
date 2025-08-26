#!/usr/bin/env python3
# file: scripts/add_proto_validation.py
# version: 0.1.0
# guid: 4c8c6b9e-5f34-4b9c-9d2f-b0e3d9f7a6c1
"""
Automated validation annotation helper for protobuf files.

Goals:
 1. Systematically (and conservatively) add buf.validate field annotations where
    they are clearly implied by naming conventions (id/email/url/name fields).
 2. Insert missing `import "buf/validate/validate.proto";` statements only when
    at least one annotation will be added (avoid pointless imports).
 3. Preserve existing annotations and options without reformatting unrelated code.
 4. Provide a dry-run report by default so changes can be inspected before apply.

Usage:
  Dry run (report only):
    python3 scripts/add_proto_validation.py

  Apply changes in-place:
    python3 scripts/add_proto_validation.py --apply

Heuristics (intentionally conservative to avoid false positives):
  * UUID pattern applied only to exact field names that frequently represent UUIDs:
      id, user_id, organization_id, created_by, updated_by
  * Email rule when field name contains 'email'
  * URI rule when field name ends with '_url' or contains 'uri'
  * Name fields (ending with _name or exactly name) get min_len=1 and max_len=100 if not present
  * Description fields get max_len=1000 if not already constrained
  * key_hash gets string.min_len=1 (non-empty requirement)
  * Required rule added for primary identifiers (id, user_id, organization_id)

The script avoids modifying lines already containing a `(buf.validate.field)` option.

Limitations / Non-goals:
  * Does not attempt complex semantic inference
  * Does not modify repeated field constraints (could be extended later)
  * Does not add numeric range constraints (needs domain knowledge)

Extensibility:
  Additional heuristic functions can be added to `compute_field_rules`.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import List, Tuple

ROOT = Path(__file__).resolve().parent.parent
PROTO_ROOT = ROOT / "proto" / "gcommon" / "v1"
UUID_PATTERN = (
    "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$"
)

ID_FIELDS = {"id", "user_id", "organization_id", "created_by", "updated_by"}
PRIMARY_ID_FIELDS = {"id", "user_id", "organization_id"}

FIELD_RE = re.compile(
    r"^\s*(?:optional\s+)?(string|bool|bytes|int32|int64|uint32|uint64|google\.protobuf\.Timestamp)\s+(\w+)\s*=\s*(\d+)(.*);\s*$"
)


def compute_field_rules(ftype: str, name: str) -> List[str]:
    rules: List[str] = []
    lname = name.lower()

    if name in ID_FIELDS and ftype == "string":
        rules.append(f'(buf.validate.field).string.pattern = "{UUID_PATTERN}"')
        if name in PRIMARY_ID_FIELDS:
            rules.append("(buf.validate.field).required = true")
    if "email" in lname and ftype == "string":
        rules.append("(buf.validate.field).string.email = true")
    if (lname.endswith("_url") or "uri" in lname) and ftype == "string":
        rules.append("(buf.validate.field).string.uri = true")
    if lname.endswith("_name") or lname == "name":
        if ftype == "string":
            rules.append("(buf.validate.field).string.min_len = 1")
            rules.append("(buf.validate.field).string.max_len = 100")
    if lname == "description" and ftype == "string":
        rules.append("(buf.validate.field).string.max_len = 1000")
    if lname == "key_hash" and ftype == "string":
        rules.append("(buf.validate.field).string.min_len = 1")
    if ftype == "google.protobuf.Timestamp" and lname in {"created_at"}:  # conservative
        rules.append("(buf.validate.field).required = true")
    return rules


def annotate_line(line: str, rules: List[str]) -> str:
    if not rules:
        return line
    # If line already has options, append before closing bracket
    if "[" in line and "]" in line:
        # split before the closing bracket
        prefix, rest = line.rsplit("]", 1)
        # Avoid duplicate insertion if any rule substring already present
        for r in rules:
            if r in prefix:
                continue
            # Insert with preceding comma
            if prefix.strip().endswith("["):
                prefix += f" {r},"
            else:
                if not prefix.strip().endswith(","):
                    prefix += ","
                prefix += f" {r}"
        return prefix + "]" + rest
    # No existing options – create bracketed options
    rule_block = ",\n      ".join(rules)
    if len(rules) == 1:
        return re.sub(r";\s*$", f" [ {rules[0]} ];", line)
    # multi-line block for readability
    return re.sub(r";\s*$", f" [\n      {rule_block}\n    ];", line)


def process_file(path: Path, apply: bool) -> Tuple[int, int, bool]:
    text = path.read_text().splitlines()
    modified = False
    new_lines: List[str] = []
    import_present = any("buf/validate/validate.proto" in l for l in text)
    added_rules = 0
    for line in text:
        m = FIELD_RE.match(line)
        if m and "(buf.validate.field)" not in line:
            ftype, name, number, tail = m.groups()
            rules = compute_field_rules(ftype, name)
            if rules:
                new_line = annotate_line(line, rules)
                new_lines.append(new_line)
                added_rules += len(rules)
                modified = True
                continue
        new_lines.append(line)
    if added_rules and not import_present:
        # Insert import after last existing import line block or after package line
        for i, line in enumerate(new_lines):
            if line.startswith("import "):
                # find last contiguous import line
                j = i
                while j + 1 < len(new_lines) and new_lines[j + 1].startswith("import "):
                    j += 1
                new_lines.insert(j + 1, 'import "buf/validate/validate.proto";')
                modified = True
                break
        else:
            # Fallback: find package line
            for i, line in enumerate(new_lines):
                if line.startswith("package "):
                    new_lines.insert(i + 1, 'import "buf/validate/validate.proto";')
                    modified = True
                    break
    if modified and apply:
        path.write_text("\n".join(new_lines) + "\n")
    return added_rules, 1 if modified else 0, modified


def main():
    apply = "--apply" in sys.argv
    proto_files = list(PROTO_ROOT.rglob("*.proto"))
    total_rules = 0
    modified_files = 0
    for p in proto_files:
        rules_added, file_modified_flag, _ = process_file(p, apply)
        if file_modified_flag:
            modified_files += 1
            total_rules += rules_added
    action = "APPLIED" if apply else "DRY-RUN"
    print(
        f"[{action}] Files considered: {len(proto_files)} | Files modified: {modified_files} | Rules added: {total_rules}"
    )
    if not apply:
        print("Run again with --apply to write changes.")


if __name__ == "__main__":
    main()
