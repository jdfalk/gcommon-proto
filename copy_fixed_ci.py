#!/usr/bin/env python3
# file: copy_fixed_ci.py
# version: 1.0.0
# guid: a1b2c3d4-e5f6-7a8b-9c0d-1e2f3a4b5c6d

"""
Copy the fixed ci.yml from gcommon to all other repositories
"""

import os
import shutil
import subprocess
from pathlib import Path

# Define repositories and their paths
repos = [
    "/Users/jdfalk/repos/github.com/jdfalk/ghcommon",
    "/Users/jdfalk/repos/github.com/jdfalk/subtitle-manager",
    "/Users/jdfalk/repos/github.com/jdfalk/copilot-agent-util-rust",
    "/Users/jdfalk/repos/github.com/jdfalk/apt-cacher-go",
    "/Users/jdfalk/repos/github.com/jdfalk/audiobook-organizer",
    "/Users/jdfalk/repos/github.com/jdfalk/public-scratch",
]

source_file = "/Users/jdfalk/repos/github.com/jdfalk/gcommon/.github/workflows/ci.yml"


def copy_ci_workflow():
    """Copy the fixed ci.yml from gcommon to all other repos"""

    if not os.path.exists(source_file):
        print(f"❌ Source file not found: {source_file}")
        return False

    print(f"📂 Source: {source_file}")
    print(f"🎯 Copying to {len(repos)} repositories...")

    success_count = 0

    for repo_path in repos:
        try:
            # Ensure the .github/workflows directory exists
            workflows_dir = os.path.join(repo_path, ".github", "workflows")
            os.makedirs(workflows_dir, exist_ok=True)

            # Copy the file
            dest_file = os.path.join(workflows_dir, "ci.yml")
            shutil.copy2(source_file, dest_file)

            repo_name = os.path.basename(repo_path)
            print(f"✅ Copied to {repo_name}")
            success_count += 1

        except Exception as e:
            repo_name = os.path.basename(repo_path)
            print(f"❌ Failed to copy to {repo_name}: {e}")

    print(f"\n🎉 Successfully copied to {success_count}/{len(repos)} repositories")
    return success_count == len(repos)


def commit_changes():
    """Commit the changes in each repository"""

    commit_message = """fix(ci): replace matrix-build with release workflow and preserve comprehensive VALIDATE settings

Fixed workflow reference issues by replacing non-existent matrix-build.yml with local release.yml file reference and maintained all comprehensive VALIDATE_* settings for Super Linter.

Files changed:
- .github/workflows/ci.yml - Updated matrix-build references to use release workflow, preserved comprehensive VALIDATE settings"""

    print(f"\n📝 Committing changes to all repositories...")

    for repo_path in repos:
        try:
            repo_name = os.path.basename(repo_path)

            # Change to the repository directory
            os.chdir(repo_path)

            # Check if there are changes
            result = subprocess.run(
                ["git", "status", "--porcelain"], capture_output=True, text=True
            )

            if not result.stdout.strip():
                print(f"ℹ️ {repo_name}: No changes to commit")
                continue

            # Add and commit changes
            subprocess.run(["git", "add", ".github/workflows/ci.yml"], check=True)
            subprocess.run(["git", "commit", "-m", commit_message], check=True)

            print(f"✅ {repo_name}: Changes committed")

        except subprocess.CalledProcessError as e:
            print(f"❌ {repo_name}: Git operation failed: {e}")
        except Exception as e:
            print(f"❌ {repo_name}: Error: {e}")


if __name__ == "__main__":
    print("🚀 Starting CI workflow fix across all repositories...")

    if copy_ci_workflow():
        commit_changes()
        print(
            "\n🎯 All done! Fixed ci.yml workflow has been deployed to all repositories."
        )
    else:
        print("\n❌ Some copies failed. Please check the errors above.")
