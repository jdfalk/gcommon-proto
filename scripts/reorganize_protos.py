#!/usr/bin/env python3
# file: reorganize_protos.py
# version: 1.1.0
# guid: a1b2c3d4-e5f6-7890-abcd-ef1234567890

"""
Reorganize proto files to have a flat structure per module.
Move all proto files from subdirectories to the main proto directory for each module.
Includes proper conflict detection, dry-run mode, and git commits.
"""

import glob
import os
import re
import shutil
import subprocess
import sys
from collections import defaultdict


def check_for_conflicts(modules):
    """Check for potential naming conflicts before reorganizing."""
    print("🔍 Checking for potential naming conflicts...")

    conflicts = defaultdict(list)
    total_files = 0
    files_to_move = 0

    for module in modules:
        module_proto_dir = f"pkg/{module}/proto"
        proto_files = glob.glob(f"{module_proto_dir}/**/*.proto", recursive=True)

        filenames_in_module = defaultdict(list)

        for proto_file in proto_files:
            filename = os.path.basename(proto_file)
            filenames_in_module[filename].append(proto_file)
            total_files += 1

            # Count files that need to be moved (not already in root)
            if os.path.dirname(proto_file) != module_proto_dir:
                files_to_move += 1

        # Check for conflicts within this module
        for filename, file_paths in filenames_in_module.items():
            if len(file_paths) > 1:
                conflicts[module].append({"filename": filename, "paths": file_paths})

    if conflicts:
        print("⚠️  CONFLICTS DETECTED:")
        for module, module_conflicts in conflicts.items():
            print(f"  Module {module}:")
            for conflict in module_conflicts:
                print(f"    {conflict['filename']}:")
                for path in conflict["paths"]:
                    print(f"      - {path}")

        choice = input("\nContinue with automatic conflict resolution? (y/N): ")
        if choice.lower() != "y":
            print("Aborting reorganization.")
            sys.exit(1)
    else:
        if files_to_move == 0:
            print(f"✅ All {total_files} proto files are already in flat structure")
        else:
            print(f"✅ No naming conflicts found across {total_files} proto files")
            print(f"📋 {files_to_move} files need to be moved to flat structure")

    return conflicts, files_to_move


def git_commit_changes(message, files=None):
    """Commit changes to git with conventional commit message."""
    try:
        # Check if there are any changes to commit
        result = subprocess.run(
            ["git", "diff", "--cached", "--quiet"], capture_output=True
        )
        if result.returncode == 0 and not files:
            # No staged changes
            result = subprocess.run(["git", "diff", "--quiet"], capture_output=True)
            if result.returncode == 0:
                print("ℹ️  No changes to commit")
                return True

        if files:
            # Add specific files
            for file in files:
                if os.path.exists(file):
                    subprocess.run(
                        ["git", "add", file], check=True, capture_output=True
                    )
        else:
            # Add all changes
            subprocess.run(["git", "add", "."], check=True, capture_output=True)

        # Check again if there are staged changes
        result = subprocess.run(
            ["git", "diff", "--cached", "--quiet"], capture_output=True
        )
        if result.returncode == 0:
            print("ℹ️  No changes to commit after staging")
            return True

        # Commit with message
        subprocess.run(
            ["git", "commit", "-m", message], check=True, capture_output=True
        )
        print(f"✅ Committed: {message}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Git commit failed: {e}")
        return False


def reorganize_protos(dry_run=False, auto_commit=False):
    """Reorganize proto files with optional dry-run and auto-commit."""
    if dry_run:
        print("🔍 DRY RUN MODE - No files will be moved")
    else:
        print("🔧 Reorganizing proto files to flat structure per module...")

    # Find all modules with proto directories
    modules = []
    for module_dir in glob.glob("pkg/*/proto"):
        module_name = module_dir.split("/")[1]
        modules.append(module_name)

    print(f"Found modules: {modules}")

    # Check for conflicts first
    conflicts, files_to_move = check_for_conflicts(modules)

    if dry_run:
        if files_to_move == 0:
            print("🔍 Dry run completed. Structure is already flat.")
        else:
            print(f"🔍 Dry run completed. Would move {files_to_move} files.")
        return

    if files_to_move == 0:
        print("✅ Proto files are already in flat structure. Checking imports...")
        # Still check and update imports if needed
        updated_files = update_all_imports()
        if auto_commit and updated_files > 0:
            git_commit_changes(
                f"fix(proto): update {updated_files} import statements for flat structure"
            )
        else:
            print("✅ All imports are already up to date.")
        return

    moved_files = 0
    moved_files_by_module = defaultdict(list)

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

            # Handle conflicts (should be rare after our check)
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
            moved_files_by_module[module].append(destination)

            # Update imports in the moved file to reflect new flat structure
            update_imports_in_file(destination, module)

        # Commit changes for this module if auto_commit is enabled
        if auto_commit and moved_files_by_module[module]:
            commit_msg = f"refactor(proto): flatten {module} proto file structure\n\nMoved {len(moved_files_by_module[module])} proto files to flat structure for better Go module compatibility"
            git_commit_changes(commit_msg, moved_files_by_module[module])

    # Remove empty subdirectories
    print("\n🧹 Cleaning up empty subdirectories...")
    removed_dirs = 0
    for module in modules:
        module_proto_dir = f"pkg/{module}/proto"
        for root, dirs, files in os.walk(module_proto_dir, topdown=False):
            for dir_name in dirs:
                dir_path = os.path.join(root, dir_name)
                try:
                    if not os.listdir(dir_path):  # Directory is empty
                        print(f"   Removing empty directory: {dir_path}")
                        os.rmdir(dir_path)
                        removed_dirs += 1
                except OSError:
                    pass  # Directory not empty or other error

    print(f"\n✅ Moved {moved_files} proto files to flat structure")

    if auto_commit and removed_dirs > 0:
        # Commit directory cleanup
        git_commit_changes("chore(proto): remove empty subdirectories after flattening")
    elif removed_dirs == 0:
        print("ℹ️  No empty directories to clean up")

    print("Now updating all import statements...")

    # Update all import statements in all proto files
    updated_files = update_all_imports()

    if auto_commit and updated_files > 0:
        # Commit import updates
        git_commit_changes(
            f"fix(proto): update {updated_files} import statements for flat structure"
        )
    elif updated_files == 0:
        print("ℹ️  All imports are already up to date")


def update_imports_in_file(filepath, module):
    """Update import statements in a proto file to use flat structure."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        original_content = content

        # Update imports that reference subdirectories in the same module
        # e.g., "pkg/auth/proto/messages/file.proto" -> "pkg/auth/proto/file.proto"
        import_pattern = rf'import "pkg/{re.escape(module)}/proto/[^/]+/([^"]+)"'

        def replace_import(match):
            filename = match.group(1)
            return f'import "pkg/{module}/proto/{filename}"'

        content = re.sub(import_pattern, replace_import, content)

        if content != original_content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"   Updated imports in: {filepath}")
            return True
        return False

    except Exception as e:
        print(f"Error updating imports in {filepath}: {e}")
        return False


def update_all_imports():
    """Update all import statements in all proto files."""
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

    if updated_files == 0:
        print("✅ All imports are already up to date")
    else:
        print(f"✅ Updated imports in {updated_files} files")
    return updated_files


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Reorganize proto files to flat structure"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be done without making changes",
    )
    parser.add_argument(
        "--auto-commit",
        action="store_true",
        help="Automatically commit changes with conventional commit messages",
    )

    args = parser.parse_args()

    reorganize_protos(dry_run=args.dry_run, auto_commit=args.auto_commit)
