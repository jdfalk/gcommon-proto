#!/usr/bin/env python3
# file: copy_super_linter_env.py
# version: 1.0.0
# guid: a9b8c7d6-e5f4-3a2b-1c9d-8e7f6a5b4c3d

"""
Copy Super Linter environment configuration and updated CI workflow to all repositories.
Moves VALIDATE_ and FIX_ variables to .env file for easier management.
"""

import os
import shutil
import subprocess
from pathlib import Path


def get_repo_paths():
    """Get all repository paths in the workspace."""
    return [
        "/Users/jdfalk/repos/github.com/jdfalk/gcommon",
        "/Users/jdfalk/repos/github.com/jdfalk/ghcommon",
        "/Users/jdfalk/repos/github.com/jdfalk/subtitle-manager",
        "/Users/jdfalk/repos/github.com/jdfalk/copilot-agent-util-rust",
        "/Users/jdfalk/repos/github.com/jdfalk/apt-cacher-go",
        "/Users/jdfalk/repos/github.com/jdfalk/audiobook-organizer",
        "/Users/jdfalk/repos/github.com/jdfalk/public-scratch",
    ]


def copy_super_linter_env():
    """Copy Super Linter environment configuration to all repositories."""
    source_repo = "/Users/jdfalk/repos/github.com/jdfalk/gcommon"
    source_env_file = os.path.join(source_repo, ".github/linters/super-linter.env")
    source_ci_file = os.path.join(source_repo, ".github/workflows/ci.yml")

    target_repos = [repo for repo in get_repo_paths() if repo != source_repo]

    success_count = 0
    error_count = 0

    print(
        "🚀 Copying Super Linter environment configuration and updated CI workflow..."
    )
    print(f"📁 Source: {source_repo}")
    print(f"📋 Target repositories: {len(target_repos)}")
    print()

    for target_repo in target_repos:
        repo_name = os.path.basename(target_repo)
        print(f"📂 Processing {repo_name}...")

        try:
            # Create .github/linters directory if it doesn't exist
            target_linters_dir = os.path.join(target_repo, ".github/linters")
            os.makedirs(target_linters_dir, exist_ok=True)

            # Copy super-linter.env file
            target_env_file = os.path.join(target_linters_dir, "super-linter.env")
            shutil.copy2(source_env_file, target_env_file)
            print(f"  ✅ Copied super-linter.env")

            # Copy updated ci.yml file
            target_workflows_dir = os.path.join(target_repo, ".github/workflows")
            os.makedirs(target_workflows_dir, exist_ok=True)
            target_ci_file = os.path.join(target_workflows_dir, "ci.yml")
            shutil.copy2(source_ci_file, target_ci_file)
            print(f"  ✅ Copied ci.yml")

            # Git add the new files
            os.chdir(target_repo)
            subprocess.run(
                ["git", "add", ".github/linters/super-linter.env"], check=True
            )
            subprocess.run(["git", "add", ".github/workflows/ci.yml"], check=True)
            print(f"  ✅ Added files to git")

            # Commit the changes
            commit_message = """feat(ci): move Super Linter configuration to environment file

Moved all VALIDATE_ and FIX_ variables from CI workflow to dedicated environment file for easier management and customization.

Files changed:
- .github/linters/super-linter.env - Complete Super Linter configuration with all VALIDATE_ and FIX_ variables
- .github/workflows/ci.yml - Updated to load configuration from environment file"""

            subprocess.run(["git", "commit", "-m", commit_message], check=True)
            print(f"  ✅ Committed changes")

            success_count += 1
            print(f"  🎉 {repo_name}: SUCCESS")

        except Exception as e:
            error_count += 1
            print(f"  ❌ {repo_name}: ERROR - {str(e)}")

        print()

    print("📊 Summary:")
    print(f"  ✅ Successful: {success_count}")
    print(f"  ❌ Errors: {error_count}")
    print(f"  📋 Total: {len(target_repos)}")

    if success_count == len(target_repos):
        print("\n🎉 All repositories updated successfully!")
        print(
            "🔧 You can now easily customize Super Linter settings by editing .github/linters/super-linter.env in each repository"
        )
    else:
        print(
            f"\n⚠️  {error_count} repositories had errors. Please check the output above."
        )


if __name__ == "__main__":
    copy_super_linter_env()
