#!/usr/bin/env python3
# file: push_all_repos.py
# version: 1.0.0
# guid: b2c3d4e5-f6a7-8b9c-0d1e-2f3a4b5c6d7e

"""
Push the committed changes to all repositories
"""

import os
import subprocess

# Define repositories and their paths
repos = [
    "/Users/jdfalk/repos/github.com/jdfalk/gcommon",
    "/Users/jdfalk/repos/github.com/jdfalk/ghcommon",
    "/Users/jdfalk/repos/github.com/jdfalk/subtitle-manager",
    "/Users/jdfalk/repos/github.com/jdfalk/copilot-agent-util-rust",
    "/Users/jdfalk/repos/github.com/jdfalk/apt-cacher-go",
    "/Users/jdfalk/repos/github.com/jdfalk/audiobook-organizer",
    "/Users/jdfalk/repos/github.com/jdfalk/merge-srt-subtitles",
    "/Users/jdfalk/repos/github.com/jdfalk/public-scratch",
]


def push_all_repos():
    """Push changes to all repositories"""

    print("🚀 Pushing changes to all repositories...")

    success_count = 0

    for repo_path in repos:
        try:
            repo_name = os.path.basename(repo_path)

            # Change to the repository directory
            os.chdir(repo_path)

            # Check if there are commits to push
            result = subprocess.run(
                ["git", "status", "--porcelain"], capture_output=True, text=True
            )

            # Check ahead/behind status
            status_result = subprocess.run(
                ["git", "status", "-sb"], capture_output=True, text=True
            )

            if "ahead" not in status_result.stdout:
                print(f"ℹ️ {repo_name}: No commits to push")
                continue

            # Push changes
            subprocess.run(["git", "push"], check=True)

            print(f"✅ {repo_name}: Successfully pushed")
            success_count += 1

        except subprocess.CalledProcessError as e:
            print(f"❌ {repo_name}: Git push failed: {e}")
        except Exception as e:
            print(f"❌ {repo_name}: Error: {e}")

    print(f"\n🎉 Successfully pushed to {success_count} repositories")


if __name__ == "__main__":
    push_all_repos()
