#!/usr/bin/env python3
"""
Fix go_package options to use module-specific paths for source_relative generation.
This prevents package name conflicts by ensuring each module generates to its own directory.
"""

import os
import re


def fix_go_package_paths(filepath):
    """Fix the go_package option to use module-specific paths."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        # Find current go_package
        go_package_match = re.search(r'option\s+go_package\s*=\s*"([^"]+)"', content)
        if not go_package_match:
            return False

        current_go_package = go_package_match.group(1)

        # Skip if it doesn't use relative paths (we want to fix all relative paths)
        if not ("../" in current_go_package):
            return False

        # Parse the file path to determine the package structure
        # Example: pkg/media/proto/enums/quality_score.proto
        rel_path = filepath.replace("./", "")
        path_parts = rel_path.split("/")

        if len(path_parts) < 3 or path_parts[0] != "pkg":
            return False

        module_name = path_parts[1]  # e.g., "media", "auth", "queue"

        # Extract package name if it exists
        package_name = f"{module_name}pb"
        if ";" in current_go_package:
            _, existing_package = current_go_package.split(";", 1)
            package_name = existing_package

        # Calculate the relative path from the proto file to the module-specific pb directory
        # Example: pkg/media/proto/enums/quality_score.proto -> ../../pkg/media/pb
        proto_depth = len(
            [p for p in path_parts[2:] if p]
        )  # Count subdirs under proto/
        relative_path = "../" * proto_depth + f"../pkg/{module_name}/pb"

        new_go_package = f"{relative_path};{package_name}"

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
    """Fix all proto files to use module-specific paths."""
    print("🔧 Fixing go_package options to use module-specific paths...")
    print("This prevents package name conflicts in source_relative mode.")

    fixed_count = 0
    total_count = 0

    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".proto"):
                filepath = os.path.join(root, file)
                total_count += 1
                if fix_go_package_paths(filepath):
                    fixed_count += 1

    print(f"\n✅ Fixed {fixed_count} out of {total_count} proto files")
    print("Each module now generates to its own pkg/{module}/pb/ directory.")


if __name__ == "__main__":
    main()
