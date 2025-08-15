#!/usr/bin/env python3
# file: fix_common_imports.py
# version: 1.0.0
# guid: f1e2d3c4-b5a6-7890-1234-567890abcdef

import glob
import re


def fix_common_imports():
    """Fix all incorrect 'common/proto/' imports to use 'pkg/common/proto/'"""

    # Find all .proto files
    proto_files = glob.glob("pkg/*/proto/*.proto")

    fixed_count = 0
    total_files = len(proto_files)

    print(f"Checking {total_files} proto files for incorrect common imports...")

    for file_path in proto_files:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            # Look for incorrect imports
            old_pattern = r'import "common/proto/([^"]+)"'
            new_pattern = r'import "pkg/common/proto/\1"'

            if re.search(old_pattern, content):
                # Fix the imports
                new_content = re.sub(old_pattern, new_pattern, content)

                # Write back to file
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(new_content)

                fixed_count += 1
                print(f"Fixed: {file_path}")

        except Exception as e:
            print(f"Error processing {file_path}: {e}")

    print(f"\nFixed {fixed_count} out of {total_files} proto files")


if __name__ == "__main__":
    fix_common_imports()
