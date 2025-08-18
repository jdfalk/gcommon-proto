#!/usr/bin/env python3
# file: fix_go_package.py
# version: 1.0.0
# guid: 12345678-1234-5678-9abc-123456789012

"""
Script to fix malformed go_package options in proto files.
Changes: option go_package value; -> option go_package = "value";
"""

import re
import sys
from pathlib import Path


def fix_go_package_in_file(file_path):
    """Fix go_package option format in a single proto file."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Pattern to match: option go_package some.package.name;
        # Replace with: option go_package = "some.package.name";
        pattern = r"option\s+go_package\s+([^=\s;]+);"
        replacement = r'option go_package = "\1";'

        new_content = re.sub(pattern, replacement, content)

        if new_content != content:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            return True
        return False

    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False


def main():
    """Fix all proto files in the proto directory."""
    proto_dir = Path("proto")
    if not proto_dir.exists():
        print("Error: proto directory not found")
        sys.exit(1)

    fixed_count = 0
    total_count = 0

    for proto_file in proto_dir.rglob("*.proto"):
        total_count += 1
        if fix_go_package_in_file(proto_file):
            fixed_count += 1
            print(f"Fixed: {proto_file}")

    print(f"\nSummary: Fixed {fixed_count} out of {total_count} proto files")


if __name__ == "__main__":
    main()
