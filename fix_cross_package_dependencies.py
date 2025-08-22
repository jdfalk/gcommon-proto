#!/usr/bin/env python3
# file: fix_cross_package_dependencies.py
# version: 1.0.0
# guid: def12345-6789-abc0-1234-567890fedcba

"""
Fix cross-package dependencies by moving problematic files to common package.
This script will move files and update their package declarations and import paths.
"""

import os
import re
import shutil

# Files that need to be moved to common (from our analysis)
FILES_TO_MOVE = {
    "metrics": [
        "validation_result.proto",
        "config_change.proto",
        "retention_policy_config.proto",
        "time_range.proto",
        "error_stats.proto",
        "api_key_config.proto",
        "retention_info.proto",
    ],
    "organization": [
        "access_control.proto",
        "notification_settings.proto",
        "compliance_settings.proto",
        "resource_limits.proto",
    ],
    "config": ["retry_settings.proto"],
}


def update_package_declaration(file_path, new_package="gcommon.v1.common"):
    """Update the package declaration in a proto file."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Update package declaration
        content = re.sub(
            r"^package\s+gcommon\.v1\.[^;]+;",
            f"package {new_package};",
            content,
            flags=re.MULTILINE,
        )

        # Update go_package option
        content = re.sub(
            r'option go_package = "[^"]*";',
            'option go_package = "github.com/jdfalk/gcommon/sdk/go";',
            content,
        )

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

        return True
    except Exception as e:
        print(f"Error updating {file_path}: {e}")
        return False


def update_import_references(old_import_path, new_import_path):
    """Update all references to the old import path throughout the codebase."""
    updated_files = []

    # Find all proto files
    for root, dirs, files in os.walk("./proto"):
        for file in files:
            if file.endswith(".proto"):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()

                    # Check if this file imports the old path
                    if old_import_path in content:
                        # Update the import
                        new_content = content.replace(old_import_path, new_import_path)

                        with open(file_path, "w", encoding="utf-8") as f:
                            f.write(new_content)

                        updated_files.append(file_path)

                except Exception as e:
                    print(f"Error updating imports in {file_path}: {e}")

    return updated_files


def move_files_to_common():
    """Move files from their current packages to common."""
    moved_files = []

    for source_package, files in FILES_TO_MOVE.items():
        source_dir = f"./proto/gcommon/v1/{source_package}"
        target_dir = "./proto/gcommon/v1/common"

        # Ensure target directory exists
        os.makedirs(target_dir, exist_ok=True)

        for filename in files:
            source_path = os.path.join(source_dir, filename)
            target_path = os.path.join(target_dir, filename)

            if os.path.exists(source_path):
                print(f"Moving {source_path} -> {target_path}")

                # Check if target already exists
                if os.path.exists(target_path):
                    # Create a backup name
                    base, ext = os.path.splitext(filename)
                    backup_name = f"{base}_{source_package}{ext}"
                    target_path = os.path.join(target_dir, backup_name)
                    print(f"  Target exists, using backup name: {backup_name}")

                # Move the file
                shutil.move(source_path, target_path)

                # Update package declaration in the moved file
                if update_package_declaration(target_path):
                    print(f"  Updated package declaration in {target_path}")

                # Update all import references
                old_import = f"gcommon/v1/{source_package}/{filename}"
                new_import = f"gcommon/v1/common/{os.path.basename(target_path)}"

                updated_files = update_import_references(old_import, new_import)
                print(f"  Updated imports in {len(updated_files)} files")

                moved_files.append(
                    {
                        "source": source_path,
                        "target": target_path,
                        "old_import": old_import,
                        "new_import": new_import,
                        "updated_files": updated_files,
                    }
                )
            else:
                print(f"WARNING: Source file not found: {source_path}")

    return moved_files


def rename_for_uniqueness():
    """Rename files to avoid conflicts and make them more descriptive."""
    renames = {
        # Make names more specific to avoid conflicts
        "validation_result.proto": "metrics_validation_result.proto",
        "config_change.proto": "metrics_config_change.proto",
        "retention_policy_config.proto": "metrics_retention_policy_config.proto",
        "time_range.proto": "metrics_time_range.proto",
        "error_stats.proto": "metrics_error_stats.proto",
        "api_key_config.proto": "metrics_api_key_config.proto",
        "retention_info.proto": "metrics_retention_info.proto",
        "access_control.proto": "organization_access_control.proto",
        "notification_settings.proto": "organization_notification_settings.proto",
        "compliance_settings.proto": "organization_compliance_settings.proto",
        "resource_limits.proto": "organization_resource_limits.proto",
        "retry_settings.proto": "config_retry_settings.proto",
    }

    common_dir = "./proto/gcommon/v1/common"
    renamed_files = []

    for old_name, new_name in renames.items():
        old_path = os.path.join(common_dir, old_name)
        new_path = os.path.join(common_dir, new_name)

        if os.path.exists(old_path):
            print(f"Renaming {old_name} -> {new_name}")
            shutil.move(old_path, new_path)

            # Update all import references
            old_import = f"gcommon/v1/common/{old_name}"
            new_import = f"gcommon/v1/common/{new_name}"

            updated_files = update_import_references(old_import, new_import)
            print(f"  Updated imports in {len(updated_files)} files")

            renamed_files.append(
                {
                    "old_name": old_name,
                    "new_name": new_name,
                    "updated_files": updated_files,
                }
            )

    return renamed_files


def main():
    """Main function to fix cross-package dependencies."""
    print("Fixing cross-package dependencies...")
    print("=" * 50)

    if not os.path.exists("./proto"):
        print(
            "Error: proto directory not found. Run this script from the repository root."
        )
        return

    # Step 1: Move files to common
    print("\nStep 1: Moving files to common package...")
    moved_files = move_files_to_common()

    # Step 2: Rename for uniqueness
    print("\nStep 2: Renaming files for uniqueness...")
    renamed_files = rename_for_uniqueness()

    # Summary
    print("\n" + "=" * 50)
    print("SUMMARY")
    print("=" * 50)
    print(f"Files moved: {len(moved_files)}")
    print(f"Files renamed: {len(renamed_files)}")

    print("\nMoved files:")
    for item in moved_files:
        print(f"  {item['source']} -> {item['target']}")

    print("\nRenamed files:")
    for item in renamed_files:
        print(f"  {item['old_name']} -> {item['new_name']}")

    print("\nNext steps:")
    print("1. Run buf generate to regenerate Go code")
    print("2. Run the dependency analysis again to verify fixes")
    print("3. Test that everything compiles correctly")


if __name__ == "__main__":
    main()
