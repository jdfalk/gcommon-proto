#!/usr/bin/env python3
# file: cleanup_bad_tags.py
# version: 1.0.0
# guid: def12345-6789-abcd-ef01-234567890abc

"""
Clean up malformed and redundant git tags.

This script removes:
1. Old SDK tags that don't follow the module-specific pattern
2. Malformed tags like sdks/go/v1/v1.2.0
"""

import subprocess
import sys


def delete_tag(tag_name):
    """Delete a git tag locally."""
    try:
        subprocess.run(
            ["git", "tag", "-d", tag_name],
            capture_output=True,
            text=True,
            check=True,
        )
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error deleting tag {tag_name}: {e.stderr}")
        return False


def delete_remote_tag(tag_name):
    """Delete a git tag from remote."""
    try:
        subprocess.run(
            ["git", "push", "origin", f":refs/tags/{tag_name}"],
            capture_output=True,
            text=True,
            check=True,
        )
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error deleting remote tag {tag_name}: {e.stderr}")
        return False


def main():
    # Tags to delete (from the git-tags file analysis)
    old_sdk_tags = [
        "sdks/go/v0.0.1",
        "sdks/go/v0.0.10",
        "sdks/go/v0.0.11",
        "sdks/go/v0.0.12",
        "sdks/go/v0.0.13",
        "sdks/go/v0.0.14",
        "sdks/go/v0.0.15",
        "sdks/go/v0.0.16",
        "sdks/go/v0.0.17",
        "sdks/go/v0.0.18",
        "sdks/go/v0.0.19",
        "sdks/go/v0.0.2",
        "sdks/go/v0.0.20",
        "sdks/go/v0.0.3",
        "sdks/go/v0.0.4",
        "sdks/go/v0.0.5",
        "sdks/go/v0.0.6",
        "sdks/go/v0.0.7",
        "sdks/go/v0.0.8",
        "sdks/go/v0.0.9",
        "sdks/go/v0.1.0",
        "sdks/go/v0.1.1",
        "sdks/go/v1.0.0",
        "sdks/go/v1.1.0",
        "sdks/go/v1.2.0",
        "sdks/go/v1.3.0",
    ]

    # Malformed tags
    malformed_tags = ["sdks/go/v1/v1.2.0", "sdks/go/v1/v1.3.0"]

    all_bad_tags = old_sdk_tags + malformed_tags

    print(f"Deleting {len(all_bad_tags)} bad tags...")

    local_deleted = 0
    remote_deleted = 0

    for tag in all_bad_tags:
        print(f"Deleting tag: {tag}")

        # Delete locally
        if delete_tag(tag):
            local_deleted += 1
            print("  ✅ Deleted locally")
        else:
            print("  ⚠️  Failed to delete locally (may not exist)")

        # Delete from remote
        if delete_remote_tag(tag):
            remote_deleted += 1
            print("  ✅ Deleted from remote")
        else:
            print("  ⚠️  Failed to delete from remote (may not exist)")

    print("\n📊 Summary:")
    print(f"   Total bad tags: {len(all_bad_tags)}")
    print(f"   Deleted locally: {local_deleted}")
    print(f"   Deleted from remote: {remote_deleted}")

    print("\n✅ Cleanup complete!")
    print(f"   Old SDK tags removed: {len(old_sdk_tags)}")
    print(f"   Malformed tags removed: {len(malformed_tags)}")
    print("   Remaining tags should be clean module-specific tags")

    return 0


if __name__ == "__main__":
    sys.exit(main())
