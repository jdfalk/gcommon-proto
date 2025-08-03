#!/usr/bin/env python3
"""
Fix go_package options in proto files to generate to correct local paths
instead of github.com/jdfalk/gcommon/pkg/ paths.
"""

import os
import re


def fix_go_package(filepath):
    """Fix the go_package option in a proto file."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        # Find current go_package
        go_package_match = re.search(r'option\s+go_package\s*=\s*"([^"]+)"', content)
        if not go_package_match:
            return False

        current_go_package = go_package_match.group(1)

        # Skip if it doesn't have the problematic github.com path
        if not current_go_package.startswith("github.com/jdfalk/gcommon/"):
            return False

        # Extract the package name (part after the semicolon)
        if ";" in current_go_package:
            path_part, package_name = current_go_package.split(";", 1)
            # Remove github.com/jdfalk/gcommon/ prefix
            new_path = path_part.replace("github.com/jdfalk/gcommon/", "")
            new_go_package = f"{new_path};{package_name}"
        else:
            # No package name specified, just fix the path
            new_go_package = current_go_package.replace(
                "github.com/jdfalk/gcommon/", ""
            )

        # Replace in content
        new_content = content.replace(
            f'option go_package = "{current_go_package}"',
            f'option go_package = "{new_go_package}"',
        )

        # Write back if changed
        if new_content != content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Fixed: {filepath}")
            print(f"  Old: {current_go_package}")
            print(f"  New: {new_go_package}")
            return True

        return False

    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False


def main():
    """Fix all proto files."""
    print("🔧 Fixing go_package options in proto files...")

    fixed_count = 0
    total_count = 0

    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".proto"):
                filepath = os.path.join(root, file)
                total_count += 1
                if fix_go_package(filepath):
                    fixed_count += 1

    print(f"\n✅ Fixed {fixed_count} out of {total_count} proto files")
    print("All go_package options now point to local paths instead of github.com URLs")


if __name__ == "__main__":
    main()
