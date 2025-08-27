#!/usr/bin/env python3
# file: copy_fixed_ci_workflow.py
# version: 1.0.0
# guid: d4e5f6a7-b8c9-0d1e-2f3a-4b5c6d7e8f9a

"""
Copy fixed CI workflow and linter configuration to all repositories.
Fixes the broken Super Linter configuration and git commit issues.
"""

import shutil
from pathlib import Path


def copy_fixed_ci():
    """Copy the fixed CI workflow and configurations to all repositories."""

    # Source repository (gcommon - where we just fixed the files)
    source_repo = Path("/Users/jdfalk/repos/github.com/jdfalk/gcommon")

    # Target repositories
    target_repos = [
        Path("/Users/jdfalk/repos/github.com/jdfalk/ghcommon"),
        Path("/Users/jdfalk/repos/github.com/jdfalk/subtitle-manager"),
        Path("/Users/jdfalk/repos/github.com/jdfalk/audiobook-organizer"),
        Path("/Users/jdfalk/repos/github.com/jdfalk/copilot-agent-util-rust"),
    ]

    # Files to copy
    files_to_copy = [
        ".github/workflows/ci.yml",
        ".github/linters/super-linter-ci.env",
        ".github/linters/.eslintrc.yml",
    ]

    print("🔧 Copying fixed CI workflow and linter configurations...")

    for target_repo in target_repos:
        if not target_repo.exists():
            print(f"⚠️  Skipping {target_repo.name} - directory doesn't exist")
            continue

        print(f"\n📁 Processing {target_repo.name}...")

        for file_path in files_to_copy:
            source_file = source_repo / file_path
            target_file = target_repo / file_path

            if not source_file.exists():
                print(f"⚠️  Source file not found: {source_file}")
                continue

            # Create target directory if it doesn't exist
            target_file.parent.mkdir(parents=True, exist_ok=True)

            # Copy the file
            try:
                shutil.copy2(source_file, target_file)
                print(f"✅ Copied {file_path}")
            except Exception as e:
                print(f"❌ Failed to copy {file_path}: {e}")

    print("\n🎉 CI workflow and linter configuration copy complete!")
    print("\nKey fixes applied:")
    print("- Fixed .eslintrc.json → .eslintrc.yml configuration")
    print("- Removed inappropriate git commit from validation-only CI")
    print("- Added proper ESLint configuration file")
    print("- Updated CI workflow to version 1.18.0")


if __name__ == "__main__":
    copy_fixed_ci()
