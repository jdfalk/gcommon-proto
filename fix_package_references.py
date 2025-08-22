#!/usr/bin/env python3
# file: fix_package_references.py
# version: 1.0.0
# guid: e1f2a3b4-5c6d-7e8f-9a0b-1c2d3e4f5a6b

"""
Fix incorrect package references in protobuf files.
This script only fixes package references, NOT imports.
"""

import os
import re


def main():
    """Fix package references in proto files."""
    print("=== Fixing Package References ===")

    # First run buf lint to get the errors
    os.system("buf lint > /tmp/buf_errors.txt 2>&1")

    try:
        with open("/tmp/buf_errors.txt", "r") as f:
            errors = f.read()
    except Exception:
        errors = ""

    if not errors:
        print("No buf lint errors found")
        return

    # Parse errors and extract files with unknown type issues
    fixes_made = 0
    lines = errors.split("\n")

    for line in lines:
        if "unknown type" in line:
            # Parse the error line
            parts = line.split(":")
            if len(parts) >= 4:
                file_path = parts[0]
                if "unknown type gcommon.v1.common." in line:
                    # Extract the type name
                    type_match = re.search(
                        r"unknown type gcommon\.v1\.common\.(\w+)", line
                    )
                    if type_match:
                        type_name = type_match.group(1)

                        # Try to fix by changing common to config
                        if fix_package_reference(
                            file_path, type_name, "common", "config"
                        ):
                            fixes_made += 1
                            print(f"Fixed {file_path}: {type_name} common -> config")

    print(f"\nMade {fixes_made} package reference fixes")


def fix_package_reference(file_path, type_name, old_package, new_package):
    """Fix a specific package reference in a file."""
    if not os.path.exists(file_path):
        return False

    try:
        with open(file_path, "r") as f:
            content = f.read()

        # Look for the problematic reference
        old_ref = f"gcommon.v1.{old_package}.{type_name}"
        new_ref = f"gcommon.v1.{new_package}.{type_name}"

        if old_ref in content:
            # Make sure we're not changing import lines or package lines
            lines = content.split("\n")
            modified = False

            for i, line in enumerate(lines):
                # Skip import lines and package lines
                if line.strip().startswith("import ") or line.strip().startswith(
                    "package "
                ):
                    continue

                if old_ref in line:
                    lines[i] = line.replace(old_ref, new_ref)
                    modified = True

            if modified:
                with open(file_path, "w") as f:
                    f.write("\n".join(lines))
                return True

    except Exception as e:
        print(f"Error processing {file_path}: {e}")

    return False


if __name__ == "__main__":
    main()
