#!/usr/bin/env python3
# file: fix_imports.py
# version: 1.0.0
# guid: 87654321-4321-8765-dcba-876543210987

"""
Script to fix incorrect import paths in proto files.
Changes common/api/request_metadata.proto -> common/types/request_metadata.proto
"""

from pathlib import Path


def fix_imports_in_file(file_path):
    """Fix import paths in a single proto file."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Fix the specific import path
        old_import = 'import "proto/gcommon/v1/common/api/request_metadata.proto";'
        new_import = 'import "proto/gcommon/v1/common/types/request_metadata.proto";'

        new_content = content.replace(old_import, new_import)

        if new_content != content:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            return True
        return False

    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False


def main():
    """Fix all proto files with incorrect imports."""
    proto_dir = Path("proto")
    if not proto_dir.exists():
        print("Error: proto directory not found")
        return

    fixed_count = 0
    total_count = 0

    for proto_file in proto_dir.rglob("*.proto"):
        total_count += 1
        if fix_imports_in_file(proto_file):
            fixed_count += 1
            print(f"Fixed: {proto_file}")

    print(f"\nSummary: Fixed {fixed_count} out of {total_count} proto files")


if __name__ == "__main__":
    main()
