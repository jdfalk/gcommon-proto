#!/usr/bin/env python3
# file: fix_go_package_paths_correct.py
# version: 1.0.0
# guid: 9d0e1f2a-3b4c-5d6e-7f8a-9b0c1d2e3f4a

import glob
import os
import re


def fix_go_package_path(file_path):
    """Fix the go_package option based on the actual file path."""
    with open(file_path, "r") as f:
        content = f.read()

    # Skip if no go_package option exists
    if "option go_package" not in content:
        return False

    # Determine the correct Go package path based on file path
    if "/pkg/common/proto/" in file_path:
        correct_go_package = "github.com/jdfalk/gcommon/pkg/common/proto"
    elif "/pkg/auth/proto/" in file_path:
        correct_go_package = "github.com/jdfalk/gcommon/pkg/auth/proto"
    elif "/pkg/cache/proto/" in file_path:
        correct_go_package = "github.com/jdfalk/gcommon/pkg/cache/proto"
    elif "/pkg/config/proto/" in file_path:
        correct_go_package = "github.com/jdfalk/gcommon/pkg/config/proto"
    elif "/pkg/db/proto/" in file_path:
        correct_go_package = "github.com/jdfalk/gcommon/pkg/db/proto"
    elif "/pkg/health/proto/" in file_path:
        correct_go_package = "github.com/jdfalk/gcommon/pkg/health/proto"
    elif "/pkg/log/proto/" in file_path:
        correct_go_package = "github.com/jdfalk/gcommon/pkg/log/proto"
    elif "/pkg/media/proto/" in file_path:
        correct_go_package = "github.com/jdfalk/gcommon/pkg/media/proto"
    elif "/pkg/metrics/proto/" in file_path:
        correct_go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto"
    elif "/pkg/notification/proto/" in file_path:
        correct_go_package = "github.com/jdfalk/gcommon/pkg/notification/proto"
    elif "/pkg/organization/proto/" in file_path:
        correct_go_package = "github.com/jdfalk/gcommon/pkg/organization/proto"
    elif "/pkg/queue/proto/" in file_path:
        correct_go_package = "github.com/jdfalk/gcommon/pkg/queue/proto"
    elif "/pkg/web/proto/" in file_path:
        correct_go_package = "github.com/jdfalk/gcommon/pkg/web/proto"
    else:
        print(f"Warning: Could not determine package for {file_path}")
        return False

    # Check if it already has the correct go_package
    if f'option go_package = "{correct_go_package}";' in content:
        return False  # Already correct

    # Replace any existing go_package option with the correct one
    go_package_pattern = r'option go_package = "[^"]+";'
    new_go_package = f'option go_package = "{correct_go_package}";'

    if re.search(go_package_pattern, content):
        content = re.sub(go_package_pattern, new_go_package, content)

        # Write back to file
        with open(file_path, "w") as f:
            f.write(content)

        print(f"Fixed go_package in {file_path} -> {correct_go_package}")
        return True
    else:
        print(f"Warning: No go_package option found in {file_path}")
        return False


def main():
    # Process all proto files in all modules
    all_proto_files = glob.glob(
        "/Users/jdfalk/repos/github.com/jdfalk/gcommon/pkg/**/proto/**/*.proto",
        recursive=True,
    )

    fixed_count = 0
    correct_count = 0

    for file_path in all_proto_files:
        if os.path.isfile(file_path):
            result = fix_go_package_path(file_path)
            if result:
                fixed_count += 1
            else:
                correct_count += 1

    print("\nSummary:")
    print(f"Fixed go_package in {fixed_count} files")
    print(f"{correct_count} files already had correct go_package")


if __name__ == "__main__":
    main()
