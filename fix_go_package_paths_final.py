#!/usr/bin/env python3
# file: fix_go_package_paths_final.py
# version: 1.1.0
# guid: def67890-abcd-1234-5678-90abcdef1234

"""
Fix go_package paths to use proper module paths instead of relative paths.
This fixes the "relative import paths are not supported in module mode" error.
"""

import glob
import re


def fix_go_package_paths():
    print("🔧 Fixing go_package paths to use proper module paths...")

    # Find all .proto files
    proto_files = glob.glob("pkg/**/proto/**/*.proto", recursive=True)

    updated_files = 0

    for proto_file in proto_files:
        try:
            with open(proto_file, "r", encoding="utf-8") as f:
                content = f.read()

            original_content = content

            # Pattern to match go_package options with relative paths
            # Example: option go_package = "../../../../pkg/auth/proto;authpb";
            # Should become: option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto;authpb";
            go_package_pattern = (
                r'option go_package = "(\.\./)*pkg/([^/]+)/proto;([^"]*)"'
            )

            def replace_go_package(match):
                module = match.group(2)  # Extract module name like 'auth', 'web', etc.
                package_suffix = match.group(3)  # Extract package suffix like 'authpb'
                new_path = (
                    f"github.com/jdfalk/gcommon/pkg/{module}/proto;{package_suffix}"
                )
                return f'option go_package = "{new_path}"'

            content = re.sub(go_package_pattern, replace_go_package, content)

            if content != original_content:
                with open(proto_file, "w", encoding="utf-8") as f:
                    f.write(content)
                print(f"Updated go_package in {proto_file}")
                updated_files += 1

        except Exception as e:
            print(f"Error processing {proto_file}: {e}")

    print(f"✅ Updated go_package paths in {updated_files} files")


if __name__ == "__main__":
    fix_go_package_paths()
