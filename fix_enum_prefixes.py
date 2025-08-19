#!/usr/bin/env python3
# file: fix_enum_prefixes.py
# version: 1.0.0
# guid: c1d2e3f4-5a6b-7c8d-9e0f-1a2b3c4d5e6f

"""
Fix broken enum prefixes in protobuf files.
The automated script created terrible nested prefixes - this fixes them.
"""

import re
import subprocess
from typing import Dict, List, Tuple


def get_lint_issues() -> List[str]:
    """Get all enum prefix issues from buf lint."""
    try:
        result = subprocess.run(
            ["buf", "lint"], capture_output=True, text=True, cwd="."
        )
        return [
            line
            for line in result.stdout.split("\n")
            if "should be prefixed with" in line
        ]
    except Exception as e:
        print(f"Error running buf lint: {e}")
        return []


def parse_enum_issue(line: str) -> Tuple[str, str, str, str]:
    """Parse a buf lint enum issue line."""
    # Example: proto/path/file.proto:17:3:Enum value name "BAD_NAME" should be prefixed with "GOOD_PREFIX_".
    parts = line.split(":")
    if len(parts) < 4:
        return None, None, None, None

    file_path = parts[0]

    # Extract the bad name and expected prefix
    match = re.search(
        r'Enum value name "([^"]+)" should be prefixed with "([^"]+)"', line
    )
    if not match:
        return None, None, None, None

    bad_name = match.group(1)
    expected_prefix = match.group(2)

    return file_path, bad_name, expected_prefix, line


def fix_enum_name(bad_name: str, expected_prefix: str) -> str:
    """Fix a bad enum name by using the expected prefix."""

    # Remove common bad prefixes and extract the meaningful part
    bad_prefixes = [
        "COMMON_ACKMODE_",
        "COMMON_AUDITACTION_",
        "COMMON_AUDITRESULT_",
        "LOG_APPENDER_TYPE_",
        "LOG_FORMATTER_TYPE_",
        "WEB_SERVERSTATUS_",
        "WEB_SSLPROTOCOL_",
        "AUTH_SESSION_STATE_",
        "TEMPLATE_CHANGE_TYPE_",
        "CONFIG_CHANGE_TYPE_",
    ]

    # Find the meaningful part after removing bad prefixes
    meaningful_part = bad_name
    for bad_prefix in bad_prefixes:
        if meaningful_part.startswith(bad_prefix):
            meaningful_part = meaningful_part[len(bad_prefix) :]
            break

    # Remove redundant parts that match the expected prefix
    # E.g., if expected_prefix is "ACK_MODE_" and we have "ACK_MODE_MANUAL", just use "MANUAL"
    expected_base = expected_prefix.rstrip("_")
    if meaningful_part.startswith(expected_base + "_"):
        meaningful_part = meaningful_part[len(expected_base + "_") :]

    # Handle UNSPECIFIED specially
    if meaningful_part == "UNSPECIFIED":
        return expected_prefix + "UNSPECIFIED"

    # Construct the good name
    return expected_prefix + meaningful_part


def fix_file_enums(file_path: str, fixes: List[Tuple[str, str]]) -> bool:
    """Fix enum names in a file."""
    try:
        with open(file_path, "r") as f:
            content = f.read()

        original_content = content

        # Apply fixes
        for bad_name, good_name in fixes:
            # Replace the enum value definition
            pattern = rf"\b{re.escape(bad_name)}\s*="
            replacement = f"{good_name} ="
            content = re.sub(pattern, replacement, content)

            print(f"  {bad_name} -> {good_name}")

        if content != original_content:
            with open(file_path, "w") as f:
                f.write(content)
            return True
        return False

    except Exception as e:
        print(f"Error fixing file {file_path}: {e}")
        return False


def main():
    """Main function to fix all enum prefix issues."""
    print("🔍 Getting enum prefix issues from buf lint...")

    issues = get_lint_issues()
    if not issues:
        print("✅ No enum prefix issues found!")
        return

    print(f"📋 Found {len(issues)} enum prefix issues")

    # Group issues by file
    file_fixes: Dict[str, List[Tuple[str, str]]] = {}

    for issue_line in issues:
        file_path, bad_name, expected_prefix, full_line = parse_enum_issue(issue_line)

        if not file_path or not bad_name or not expected_prefix:
            print(f"⚠️  Could not parse: {issue_line}")
            continue

        good_name = fix_enum_name(bad_name, expected_prefix)

        if file_path not in file_fixes:
            file_fixes[file_path] = []

        file_fixes[file_path].append((bad_name, good_name))

    # Apply fixes file by file
    print(f"\n🔧 Fixing {len(file_fixes)} files...")

    for file_path, fixes in file_fixes.items():
        print(f"\n📝 Fixing {file_path}:")
        success = fix_file_enums(file_path, fixes)
        if success:
            print(f"  ✅ Fixed {len(fixes)} enum values")
        else:
            print("  ❌ Failed to fix file")

    print("\n🎯 Complete! Run 'buf lint' to check remaining issues.")


if __name__ == "__main__":
    main()
