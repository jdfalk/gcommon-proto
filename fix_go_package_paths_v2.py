#!/usr/bin/env python3
# file: fix_go_package_paths_v2.py
# version: 1.0.0
# guid: def67890-abcd-1234-5678-90abcdef1234

"""
Fix go_package paths in proto files to point to proto directories instead of pb directories.
"""

import os


def fix_go_package_paths():
    """Fix all go_package options to use proto instead of pb."""
    fixed_count = 0

    # Walk through all proto files
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".proto"):
                file_path = os.path.join(root, file)

                try:
                    with open(file_path, "r") as f:
                        content = f.read()

                    # Extract module name from path
                    # e.g., pkg/auth/proto/messages/file.proto -> auth
                    path_parts = file_path.split("/")
                    if (
                        len(path_parts) >= 4
                        and path_parts[0] == "."
                        and path_parts[1] == "pkg"
                    ):
                        module = path_parts[2]

                        # Pattern to match go_package lines with pb references
                        old_pattern = rf'option go_package = "../../../../pkg/{module}/pb;{module}pb";'
                        new_pattern = f'option go_package = "../../../../pkg/{module}/proto;{module}pb";'

                        if old_pattern in content:
                            new_content = content.replace(old_pattern, new_pattern)

                            with open(file_path, "w") as f:
                                f.write(new_content)

                            print(f"Fixed go_package in {file_path}")
                            fixed_count += 1

                except Exception as e:
                    print(f"Error processing {file_path}: {e}")

    print(f"\n✅ Fixed {fixed_count} go_package paths")


if __name__ == "__main__":
    print("🔧 Fixing go_package paths...")
    fix_go_package_paths()
