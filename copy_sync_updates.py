#!/usr/bin/env python3
# file: copy_sync_updates.py
# version: 1.0.0
# guid: 8f9a1b2c-3d4e-5f6a-7b8c-9d0e1f2a3b4c

"""
Copy updated sync system to all repositories.

Updates the sync system across all repositories to use the new configuration-driven approach.
"""

import shutil
import sys
from pathlib import Path


def main():
    """Copy sync updates to all repositories."""
    # Get the workspace root
    workspace_root = Path.cwd().parent
    target_repos = [
        "ghcommon",
        "subtitle-manager",
        "audiobook-organizer",
        "copilot-agent-util-rust",
    ]

    source_repo = workspace_root / "ghcommon"
    if not source_repo.exists():
        print(f"❌ Source repository {source_repo} not found")
        return 1

    # Files to copy
    files_to_copy = [
        ".github/scripts/sync-receiver-sync-files.py",
        ".github/workflows/sync-receiver.yml",
        ".github/workflow-config.yaml",
    ]

    print("🚀 Copying sync system updates to all repositories...")

    for repo_name in target_repos:
        repo_path = workspace_root / repo_name
        if not repo_path.exists():
            print(f"⚠️  Repository {repo_name} not found at {repo_path}")
            continue

        print(f"\n📁 Updating {repo_name}...")

        for file_path in files_to_copy:
            source_file = source_repo / file_path
            target_file = repo_path / file_path

            if not source_file.exists():
                print(f"  ⚠️  Source file {source_file} not found")
                continue

            # Create target directory if needed
            target_file.parent.mkdir(parents=True, exist_ok=True)

            # Copy file
            try:
                shutil.copy2(source_file, target_file)
                print(f"  ✅ Copied {file_path}")
            except Exception as e:
                print(f"  ❌ Failed to copy {file_path}: {e}")

    print("\n🎉 Sync system updates complete!")
    print("\nNext steps:")
    print("1. Review workflow-config.yaml in each repository")
    print("2. Commit changes in each repository")
    print("3. Test sync functionality")

    return 0


if __name__ == "__main__":
    sys.exit(main())
