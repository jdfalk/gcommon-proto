#!/usr/bin/env python3
"""
Update go_package options to work with paths=source_relative.
This ensures generated Go files end up in the correct package structure.
"""

import os
import re


def update_go_package_for_source_relative(filepath):
    """Update the go_package option for source_relative generation."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        # Find current go_package
        go_package_match = re.search(r'option\s+go_package\s*=\s*"([^"]+)"', content)
        if not go_package_match:
            return False

        current_go_package = go_package_match.group(1)

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

        # For source_relative, we want the Go files to be generated in a
        # structure that makes sense for Go imports
        # We'll generate files in pkg/module/pb/ with relative paths from proto files

        # Calculate the relative path from the proto file to the pb directory
        # Example: pkg/media/proto/enums/quality_score.proto -> ../../../pb
        proto_depth = len(
            [p for p in path_parts[2:] if p]
        )  # Count subdirs under proto/
        relative_path = "../" * (proto_depth + 1) + "pb"

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
            print(f"Updated: {filepath}")
            print(f"  Old: {current_go_package}")
            print(f"  New: {new_go_package}")
            return True

        return False

    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False


def main():
    """Update all proto files for source_relative generation."""
    print("🔧 Updating go_package options for paths=source_relative...")
    print("This will set up proper Go package structure for generated files.")

    fixed_count = 0
    total_count = 0

    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".proto"):
                filepath = os.path.join(root, file)
                total_count += 1
                if update_go_package_for_source_relative(filepath):
                    fixed_count += 1

    print(f"\n✅ Updated {fixed_count} out of {total_count} proto files")
    print(
        "\nNow you can update buf.gen.yaml to use paths=source_relative for both plugins:"
    )
    print("  - protocolbuffers/go: paths=source_relative")
    print("  - grpc/go: paths=source_relative")
    print("\nThe generated files will be placed in pkg/{module}/pb/ directories.")


if __name__ == "__main__":
    main()
