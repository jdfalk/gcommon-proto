#!/usr/bin/env python3
# file: fix_go_package.py
# version: 1.0.0
# guid: 7b8c9d0e-1f2a-3b4c-5d6e-7f8a9b0c1d2e

import glob
import os
import re


def fix_go_package_option(file_path):
    """Fix the go_package option to use source_relative path."""
    with open(file_path, "r") as f:
        content = f.read()

    # Skip if correct go_package already exists
    if 'option go_package = "github.com/jdfalk/gcommon/pkg/common/proto";' in content:
        return False

    # Replace the go_package option
    old_pattern = (
        r'option go_package = "github\.com/jdfalk/gcommon/pkg/common/proto/commonpb";'
    )
    new_value = 'option go_package = "github.com/jdfalk/gcommon/pkg/common/proto";'

    if re.search(old_pattern, content):
        content = re.sub(old_pattern, new_value, content)

        # Write back to file
        with open(file_path, "w") as f:
            f.write(content)

        print(f"Fixed go_package in {file_path}")
        return True
    else:
        print(f"No matching go_package found in {file_path}")
        return False


def main():
    # Process all proto files in the common module
    common_files = glob.glob(
        "/Users/jdfalk/repos/github.com/jdfalk/gcommon/pkg/common/proto/**/*.proto",
        recursive=True,
    )

    fixed_count = 0
    for file_path in common_files:
        if os.path.isfile(file_path):
            if fix_go_package_option(file_path):
                fixed_count += 1

    print(f"Fixed {fixed_count} files")


if __name__ == "__main__":
    main()
