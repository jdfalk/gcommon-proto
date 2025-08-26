#!/usr/bin/env python3
# file: copy_fixed_release_workflow.py
# version: 1.0.0
# guid: a1b2c3d4-e5f6-7a8b-9c0d-1e2f3a4b5c6d

"""
Copy the fixed release.yml workflow from gcommon to all other repositories.

This script fixes the CI workflow artifact dependency issue by:
- Removing protobuf dependencies from all build jobs
- Setting protobuf-artifacts to 'false' by default
- Fixing job dependency issues that caused artifact download failures
"""

import os
import shutil
import subprocess

# Define repositories and their paths
repos = [
    "/Users/jdfalk/repos/github.com/jdfalk/ghcommon",
    "/Users/jdfalk/repos/github.com/jdfalk/subtitle-manager",
    "/Users/jdfalk/repos/github.com/jdfalk/copilot-agent-util-rust",
    "/Users/jdfalk/repos/github.com/jdfalk/apt-cacher-go",
    "/Users/jdfalk/repos/github.com/jdfalk/audiobook-organizer",
    "/Users/jdfalk/repos/github.com/jdfalk/public-scratch",
]

source_file = "/Users/jdfalk/repos/github.com/jdfalk/gcommon/.github/workflows/release.yml"


def copy_release_workflow():
    """Copy the fixed release.yml from gcommon to all other repos"""

    print("🔄 Copying fixed release workflow to all repositories...")
    print("🐛 This fixes the CI workflow artifact dependency issues")
    print()

    if not os.path.exists(source_file):
        print("❌ Source release.yml file not found!")
        return False

    success_count = 0
    total_count = len(repos)

    for repo_path in repos:
        repo_name = os.path.basename(repo_path)
        print(f"🔄 Updating {repo_name}...")

        if not os.path.exists(repo_path):
            print(f"   ⚠️ Repository path does not exist: {repo_path}")
            continue

        # Create .github/workflows directory if it doesn't exist
        workflows_dir = os.path.join(repo_path, ".github", "workflows")
        os.makedirs(workflows_dir, exist_ok=True)

        # Copy the workflow file
        target_file = os.path.join(workflows_dir, "release.yml")
        try:
            shutil.copy2(source_file, target_file)
            print(f"   📄 Copied release.yml to {repo_name}")
            success_count += 1
        except Exception as e:
            print(f"   ❌ Failed to copy to {repo_name}: {e}")
            continue

    print()
    print("📊 Summary:")
    print(f"   Successfully updated: {success_count}/{total_count} repositories")

    if success_count == total_count:
        print("✅ All repositories successfully updated!")
    else:
        print("⚠️ Some repositories had issues")

    return success_count == total_count


def commit_changes():
    """Commit the changes to all repositories"""

    print()
    print("📝 Committing changes to all repositories...")

    commit_message = """fix(ci): resolve release workflow artifact dependency issues

Fixed critical CI workflow issues preventing successful builds by removing
problematic protobuf artifact dependencies and simplifying job dependencies.

Issues Addressed:

fix(workflows): remove protobuf artifact dependencies from all build jobs
- Removed generate-protobuf dependency from build-go, build-python, build-frontend, build-docker, build-rust jobs
- Set protobuf-artifacts to 'false' by default to prevent artifact download failures
- Fixed conditional logic that caused jobs to fail when protobuf generation was skipped

fix(workflows): simplify job dependency chain
- Changed from complex conditional protobuf artifact logic to simple language detection
- Removed 'always()' conditions that caused jobs to run even when dependencies failed
- Updated build-status job to only depend on actual build jobs, not protobuf generation

fix(workflows): clean up workflow summary reporting
- Removed reference to generate-protobuf.result in build summary
- Fixed workflow summary table to only show actual build components

Result: CI workflows now run successfully without attempting to download non-existent protobuf artifacts.

Files changed:
- .github/workflows/release.yml - Fixed artifact dependencies and job logic"""

    for repo_path in repos:
        repo_name = os.path.basename(repo_path)
        print(f"📝 Committing to {repo_name}...")

        try:
            # Change to repository directory
            os.chdir(repo_path)

            # Check if there are changes to commit
            result = subprocess.run(
                ["git", "status", "--porcelain"],
                capture_output=True,
                text=True,
                check=True
            )

            if not result.stdout.strip():
                print(f"   ℹ️ {repo_name} - No changes to commit")
                continue

            # Add the workflow file
            subprocess.run(["git", "add", ".github/workflows/release.yml"], check=True)

            # Commit the changes
            subprocess.run(
                ["git", "commit", "-m", commit_message],
                check=True
            )

            print(f"   ✅ {repo_name} - Changes committed")

        except subprocess.CalledProcessError as e:
            print(f"   ❌ {repo_name} - Git operation failed: {e}")
        except Exception as e:
            print(f"   ❌ {repo_name} - Error: {e}")

    print("✅ Commit process completed!")


if __name__ == "__main__":
    if copy_release_workflow():
        commit_changes()
    else:
        print("❌ Copy operation failed, skipping commits")
