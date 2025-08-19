#!/usr/bin/env python3
# file: fix_common_package_paths.py
# version: 1.0.0
# guid: 123e4567-e89b-12d3-a456-426614174001

"""
Fix go_package paths for common package to ensure all files in the same package
have the same go_package value. The common package needs to consolidate all
enums, messages, and services into a single package path.
"""

import os
import re


def fix_common_package_paths():
    """Fix go_package paths for the common package."""

    # All common package files should use this go_package
    target_go_package = "github.com/jdfalk/gcommon/sdks/go/gcommon/v1/common"

    # Find all proto files in the common package
    common_proto_files = []
    for root, dirs, files in os.walk("proto/gcommon/v1/common"):
        for file in files:
            if file.endswith(".proto"):
                common_proto_files.append(os.path.join(root, file))

    print(f"Found {len(common_proto_files)} files in common package")

    fixed_count = 0

    for file_path in common_proto_files:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            # Pattern to match any go_package option
            go_package_pattern = r'option\s+go_package\s*=\s*"[^"]+";'

            if re.search(go_package_pattern, content):
                # Replace with the target go_package
                new_content = re.sub(
                    go_package_pattern,
                    f'option go_package = "{target_go_package}";',
                    content,
                )

                if new_content != content:
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    print(f"Fixed: {file_path}")
                    fixed_count += 1

        except Exception as e:
            print(f"Error processing {file_path}: {e}")

    print(f"\nFixed go_package in {fixed_count} common package files")


def fix_routing_pattern_enum():
    """Fix the routing pattern enum to have _UNSPECIFIED suffix."""
    file_path = "proto/gcommon/v1/queue/enums/routing_pattern.proto"

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Replace ROUTING_PATTERN_EXACT with ROUTING_PATTERN_UNSPECIFIED
        new_content = content.replace(
            "ROUTING_PATTERN_EXACT = 0;", "ROUTING_PATTERN_UNSPECIFIED = 0;"
        )

        if new_content != content:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Fixed enum zero value in: {file_path}")

    except Exception as e:
        print(f"Error fixing routing pattern enum: {e}")


def remove_unused_import():
    """Remove unused import from revoke_permission_request.proto."""
    file_path = "proto/gcommon/v1/common/messages/revoke_permission_request.proto"

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        # Remove the unused import line
        new_lines = []
        for line in lines:
            if (
                'import "gcommon/v1/common/messages/list_permissions_request.proto";'
                not in line
            ):
                new_lines.append(line)
            else:
                print(f"Removed unused import from: {file_path}")

        if len(new_lines) != len(lines):
            with open(file_path, "w", encoding="utf-8") as f:
                f.writelines(new_lines)

    except Exception as e:
        print(f"Error removing unused import: {e}")


if __name__ == "__main__":
    print("Fixing common package go_package paths...")
    fix_common_package_paths()

    print("\nFixing routing pattern enum...")
    fix_routing_pattern_enum()

    print("\nRemoving unused imports...")
    remove_unused_import()

    print("\nDone!")
