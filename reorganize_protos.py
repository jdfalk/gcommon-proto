#!/usr/bin/env python3
# file: reorganize_protos.py
# version: 1.0.0
# guid: a1b2c3d4-e5f6-7890-abcd-ef1234567890

"""
Reorganize proto files to have a flat structure per module.
Move all proto files from subdirectories to the main proto directory for each module.
"""

import glob
import os
import shutil


def reorganize_protos():
    print("🔧 Reorganizing proto files to flat structure per module...")

    # Find all modules with proto directories
    modules = []
    for module_dir in glob.glob("pkg/*/proto"):
        module_name = module_dir.split("/")[1]
        modules.append(module_name)

    print(f"Found modules: {modules}")

    moved_files = 0

    for module in modules:
        module_proto_dir = f"pkg/{module}/proto"
        print(f"\n📁 Processing module: {module}")

        # Find all proto files in subdirectories
        proto_files = glob.glob(f"{module_proto_dir}/**/*.proto", recursive=True)

        for proto_file in proto_files:
            # Skip files already in the root proto directory
            if os.path.dirname(proto_file) == module_proto_dir:
                continue

            # Get the filename
            filename = os.path.basename(proto_file)
            destination = os.path.join(module_proto_dir, filename)

            # Check for name conflicts
            if os.path.exists(destination):
                print(
                    f"⚠️  Name conflict: {filename} already exists in {module_proto_dir}"
                )
                # Add subdirectory prefix to avoid conflicts
                subdir = os.path.basename(os.path.dirname(proto_file))
                new_filename = f"{subdir}_{filename}"
                destination = os.path.join(module_proto_dir, new_filename)
                print(f"   Renaming to: {new_filename}")

            # Move the file
            print(f"   Moving: {proto_file} -> {destination}")
            shutil.move(proto_file, destination)
            moved_files += 1

            # Update imports in the moved file to reflect new flat structure
            update_imports_in_file(destination, module)

    # Remove empty subdirectories
    print("\n🧹 Cleaning up empty subdirectories...")
    for module in modules:
        module_proto_dir = f"pkg/{module}/proto"
        for root, dirs, files in os.walk(module_proto_dir, topdown=False):
            for dir_name in dirs:
                dir_path = os.path.join(root, dir_name)
                try:
                    if not os.listdir(dir_path):  # Directory is empty
                        print(f"   Removing empty directory: {dir_path}")
                        os.rmdir(dir_path)
                except OSError:
                    pass  # Directory not empty or other error

    print(f"\n✅ Moved {moved_files} proto files to flat structure")
    print("Now updating all import statements...")

    # Update all import statements in all proto files
    update_all_imports()


def update_imports_in_file(filepath, module):
    """Update import statements in a proto file to use flat structure."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        original_content = content

        # Update imports that reference subdirectories in the same module
        # e.g., "pkg/auth/proto/messages/file.proto" -> "pkg/auth/proto/file.proto"
        import_pattern = rf'import "pkg/{module}/proto/[^/]+/([^"]+)"'

        def replace_import(match):
            filename = match.group(1)
            return f'import "pkg/{module}/proto/{filename}"'

        content = re.sub(import_pattern, replace_import, content)

        if content != original_content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"   Updated imports in: {filepath}")

    except Exception as e:
        print(f"Error updating imports in {filepath}: {e}")


def update_all_imports():
    """Update all import statements in all proto files."""
    import re

    all_proto_files = glob.glob("pkg/*/proto/*.proto")
    updated_files = 0

    for proto_file in all_proto_files:
        try:
            with open(proto_file, "r", encoding="utf-8") as f:
                content = f.read()

            original_content = content

            # Update all imports that reference subdirectories
            # Pattern: pkg/MODULE/proto/SUBDIR/file.proto -> pkg/MODULE/proto/file.proto
            import_pattern = r'import "pkg/([^/]+)/proto/[^/]+/([^"]+)"'

            def replace_import(match):
                module = match.group(1)
                filename = match.group(2)
                return f'import "pkg/{module}/proto/{filename}"'

            content = re.sub(import_pattern, replace_import, content)

            if content != original_content:
                with open(proto_file, "w", encoding="utf-8") as f:
                    f.write(content)
                print(f"Updated imports in: {proto_file}")
                updated_files += 1

        except Exception as e:
            print(f"Error updating {proto_file}: {e}")

    print(f"✅ Updated imports in {updated_files} files")


if __name__ == "__main__":
    import re

    reorganize_protos()
