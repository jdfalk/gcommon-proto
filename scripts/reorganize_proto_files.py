#!/usr/bin/env python3
# file: reorganize_proto_files.py
# version: 1.0.0
# guid: 8f7e6d5c-4b3a-2198-7f6e-5d4c3b2a1908

"""
Proto File Reorganizer

This script moves all the 1-1-1 proto files back to their module root directories
so that Go code generation works correctly (all files in same package).
"""

import shutil
from pathlib import Path


def reorganize_proto_module(module_path: Path):
    """Reorganize a single module's proto files"""
    print(f"Reorganizing {module_path}")

    # Find all subdirectories with proto files
    subdirs = ["requests", "responses", "messages", "services", "enums", "types"]

    files_moved = 0
    for subdir in subdirs:
        subdir_path = module_path / subdir
        if subdir_path.exists() and subdir_path.is_dir():
            # Move all .proto files from subdirectory to module root
            for proto_file in subdir_path.glob("*.proto"):
                target_path = module_path / proto_file.name

                # Handle name conflicts by checking if target exists
                if target_path.exists():
                    print(f"  ⚠️  Conflict: {target_path.name} already exists, skipping")
                    continue

                shutil.move(str(proto_file), str(target_path))
                print(f"  ✓ Moved {proto_file.name}")
                files_moved += 1

            # Remove empty subdirectory
            if not any(subdir_path.iterdir()):
                shutil.rmtree(subdir_path)
                print(f"  🗂️  Removed empty directory {subdir}")

    return files_moved


def find_proto_modules(base_path: Path):
    """Find all proto module directories"""
    modules = []

    for item in base_path.iterdir():
        if item.is_dir():
            proto_dir = item / "proto"
            if proto_dir.exists():
                modules.append(proto_dir)

    return modules


def main():
    """Main reorganization function"""
    base_path = Path("pkg")

    if not base_path.exists():
        print(f"Error: {base_path} directory not found")
        return

    print("🔄 REORGANIZING PROTO FILES")
    print("=" * 50)

    modules = find_proto_modules(base_path)
    print(f"Found {len(modules)} proto modules")

    total_moved = 0
    for module in modules:
        moved = reorganize_proto_module(module)
        total_moved += moved

    print("\n✅ COMPLETED:")
    print(f"Reorganized {len(modules)} modules")
    print(f"Moved {total_moved} proto files to module roots")
    print(
        "\nNow all proto files are in their module directories for correct Go package generation!"
    )


if __name__ == "__main__":
    main()
