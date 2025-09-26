#!/usr/bin/env python3
# file: scripts/update_go_packages_to_pb.py
# version: 1.0.0
# guid: a1b2c3d4-e5f6-7a8b-9c0d-1e2f3a4b5c6d

"""
Comprehensive script to update all go_package declarations from pkg/xxx to pkg/xxxpb
across all .proto files in the gcommon-proto repository.

This script:
1. Finds all .proto files
2. Updates go_package declarations to use pb-suffixed package names
3. Provides detailed logging of all changes made
4. Creates backup files for safety
"""

import os
import re
import shutil
from pathlib import Path
from typing import List, Tuple

def find_proto_files(root_dir: str) -> List[str]:
    """Find all .proto files in the repository."""
    proto_files = []
    for root, dirs, files in os.walk(root_dir):
        # Skip .git and other hidden directories
        dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['logs', '__pycache__']]

        for file in files:
            if file.endswith('.proto'):
                proto_files.append(os.path.join(root, file))

    return sorted(proto_files)

def create_backup(file_path: str) -> str:
    """Create a backup of the original file."""
    backup_path = f"{file_path}.backup"
    shutil.copy2(file_path, backup_path)
    return backup_path

def update_go_package_line(line: str) -> Tuple[str, bool]:
    """
    Update a go_package line to use pb-suffixed package name.

    Returns:
        Tuple of (updated_line, was_changed)
    """
    # Pattern to match go_package lines
    go_package_pattern = r'option\s+go_package\s*=\s*"([^"]+)";'

    match = re.search(go_package_pattern, line)
    if not match:
        return line, False

    original_package = match.group(1)

    # Map of package transformations
    package_transforms = {
        '/pkg/common': '/pkg/commonpb',
        '/pkg/config': '/pkg/configpb',
        '/pkg/database': '/pkg/databasepb',
        '/pkg/health': '/pkg/healthpb',
        '/pkg/media': '/pkg/mediapb',
        '/pkg/metrics': '/pkg/metricspb',
        '/pkg/organization': '/pkg/organizationpb',
        '/pkg/queue': '/pkg/queuepb',
        '/pkg/web': '/pkg/webpb',
        # Handle versioned packages
        '/pkg/media/v2': '/pkg/mediapb/v2',
        '/pkg/common/v2': '/pkg/commonpb/v2',
        '/pkg/config/v2': '/pkg/configpb/v2',
        '/pkg/database/v2': '/pkg/databasepb/v2',
        '/pkg/health/v2': '/pkg/healthpb/v2',
        '/pkg/metrics/v2': '/pkg/metricspb/v2',
        '/pkg/organization/v2': '/pkg/organizationpb/v2',
        '/pkg/queue/v2': '/pkg/queuepb/v2',
        '/pkg/web/v2': '/pkg/webpb/v2',
    }

    # Apply transformations
    updated_package = original_package
    for old_path, new_path in package_transforms.items():
        if old_path in updated_package:
            updated_package = updated_package.replace(old_path, new_path)
            break

    if updated_package == original_package:
        return line, False

    # Replace the package in the line
    updated_line = re.sub(go_package_pattern, f'option go_package = "{updated_package}";', line)
    return updated_line, True

def update_proto_file(file_path: str) -> Tuple[bool, List[str]]:
    """
    Update go_package declarations in a single .proto file.

    Returns:
        Tuple of (was_updated, list_of_changes)
    """
    changes = []
    was_updated = False

    try:
        # Read the file
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        # Create backup
        backup_path = create_backup(file_path)

        # Process each line
        updated_lines = []
        for line_num, line in enumerate(lines, 1):
            updated_line, changed = update_go_package_line(line)
            updated_lines.append(updated_line)

            if changed:
                was_updated = True
                changes.append(f"Line {line_num}: {line.strip()} -> {updated_line.strip()}")

        # Write updated file if changes were made
        if was_updated:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.writelines(updated_lines)
            print(f"✅ Updated: {file_path}")
            for change in changes:
                print(f"   {change}")
        else:
            # Remove backup if no changes
            os.remove(backup_path)
            print(f"⏸️  No changes: {file_path}")

    except Exception as e:
        print(f"❌ Error processing {file_path}: {e}")
        return False, []

    return was_updated, changes

def main():
    """Main function to orchestrate the go_package updates."""
    print("🚀 Starting go_package update to pb-suffixed packages...")
    print("=" * 60)

    # Find the repository root (current directory for this script)
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(f"Repository root: {repo_root}")

    # Find all .proto files
    proto_files = find_proto_files(repo_root)
    print(f"Found {len(proto_files)} .proto files")
    print()

    # Process each file
    total_updated = 0
    all_changes = []

    for file_path in proto_files:
        relative_path = os.path.relpath(file_path, repo_root)
        print(f"Processing: {relative_path}")

        was_updated, changes = update_proto_file(file_path)
        if was_updated:
            total_updated += 1
            all_changes.extend([f"{relative_path}: {change}" for change in changes])
        print()

    # Summary
    print("=" * 60)
    print("📋 SUMMARY")
    print(f"Total .proto files processed: {len(proto_files)}")
    print(f"Files updated: {total_updated}")
    print(f"Files unchanged: {len(proto_files) - total_updated}")

    if all_changes:
        print(f"\n📝 All changes made:")
        for change in all_changes:
            print(f"   {change}")

    print("\n✨ go_package update complete!")
    print("Next steps:")
    print("1. Update buf.gen.yaml configuration")
    print("2. Update post-processing scripts in gcommon repo")
    print("3. Run buf generate to create new pb-suffixed packages")
    print("4. Clean up old generated code")
    print("5. Update any code importing old packages")

if __name__ == "__main__":
    main()
