#!/usr/bin/env python3
# file: fix_common_go_packages.py
# version: 1.0.0
# guid: 123e4567-e89b-12d3-a456-426614174001

import os
import re


def fix_common_go_packages():
    """Fix all go_package options in common proto files to use unified path."""

    # Define the unified go_package for common
    unified_go_package = "github.com/jdfalk/gcommon/sdks/go/common"

    # Pattern to match go_package options with common paths
    pattern = r'option go_package = "github\.com/jdfalk/gcommon/sdks/go/gcommon/v1/common/(?:enums|messages|services)";'
    replacement = f'option go_package = "{unified_go_package}";'

    fixed_count = 0

    # Process all proto files in the common directory
    common_dir = "proto/gcommon/v1/common"

    for root, dirs, files in os.walk(common_dir):
        for file in files:
            if file.endswith(".proto"):
                file_path = os.path.join(root, file)

                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()

                    # Check if this file needs fixing
                    if re.search(pattern, content):
                        # Apply the fix
                        new_content = re.sub(pattern, replacement, content)

                        with open(file_path, "w", encoding="utf-8") as f:
                            f.write(new_content)

                        print(f"Fixed: {file_path}")
                        fixed_count += 1

                except Exception as e:
                    print(f"Error processing {file_path}: {e}")

    print(f"\nFixed go_package paths in {fixed_count} common proto files")


if __name__ == "__main__":
    fix_common_go_packages()
