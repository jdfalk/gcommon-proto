#!/usr/bin/env python3
# file: fix_malformed_tags.py
# version: 1.0.0
# guid: d4e5f6a7-b8c9-0123-def4-56789012345e

"""
Specifically target and delete the malformed ^{} tags and other problematic remote tags.
"""

import os
import subprocess
import sys


def run_command(cmd, check=True):
    """Run a command and return the result"""
    print(f"Running: {cmd}")
    try:
        result = subprocess.run(
            cmd, shell=True, capture_output=True, text=True, check=check
        )
        if result.stdout:
            print(f"Output: {result.stdout.strip()}")
        return result
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e}")
        print(f"stderr: {e.stderr}")
        return None


def get_malformed_remote_tags():
    """Get all malformed remote tags that need to be deleted"""
    print("Fetching current remote tags...")
    result = run_command("git ls-remote --tags origin", check=False)

    if not result or not result.stdout:
        print("Failed to fetch remote tags")
        return []

    malformed_tags = []
    lines = result.stdout.strip().split("\n")

    for line in lines:
        if "\t" in line:
            hash_part, ref_part = line.split("\t", 1)
            ref_part = ref_part.strip()

            if ref_part.startswith("refs/tags/"):
                tag_name = ref_part.replace("refs/tags/", "")

                # Rule 1: Tags ending with ^{} are malformed
                if tag_name.endswith("^{}"):
                    malformed_tags.append(tag_name)

    return malformed_tags


def delete_malformed_remote_tags(malformed_tags):
    """Delete malformed tags from remote in batches"""
    if not malformed_tags:
        print("No malformed remote tags found")
        return

    print(f"Found {len(malformed_tags)} malformed remote tags to delete")

    # Show examples
    print("Examples of malformed tags:")
    for i, tag in enumerate(malformed_tags[:5]):
        print(f"  - {tag}")
    if len(malformed_tags) > 5:
        print(f"  ... and {len(malformed_tags) - 5} more")

    # Confirm
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "--force":
        response = "y"
        print(f"\nForce mode: Deleting {len(malformed_tags)} malformed remote tags...")
    else:
        response = input(
            f"\nDelete {len(malformed_tags)} malformed remote tags? (y/N): "
        )

    if response.lower() != "y":
        print("Aborted")
        return

    # Delete in batches to avoid command line length limits
    batch_size = 20  # Conservative for complex tag names
    successful_deletes = 0

    for i in range(0, len(malformed_tags), batch_size):
        batch = malformed_tags[i : i + batch_size]

        print(
            f"\nDeleting batch {i // batch_size + 1}/{(len(malformed_tags) + batch_size - 1) // batch_size} ({len(batch)} tags)"
        )

        # For tags with special characters like ^{}, we need to properly quote them
        for tag in batch:
            # Delete each tag individually to handle special characters
            # Use shlex.quote to properly escape special characters for shell execution
            import shlex

            quoted_tag = shlex.quote(tag)
            cmd = f"git push origin :refs/tags/{quoted_tag}"
            result = run_command(cmd, check=False)

            if result and result.returncode == 0:
                successful_deletes += 1
                print(f"✅ Deleted: {tag}")
            else:
                print(f"❌ Failed to delete: {tag}")

    print(
        f"\n📊 Deletion summary: {successful_deletes}/{len(malformed_tags)} malformed tags deleted"
    )


def main():
    print("🔧 MALFORMED TAG FIXER 🔧")
    print("=" * 40)
    print("This will delete remote tags with ^{} suffixes and other malformed patterns")

    # Get malformed remote tags
    malformed_tags = get_malformed_remote_tags()

    if not malformed_tags:
        print("✅ No malformed remote tags found!")
        return 0

    # Delete malformed remote tags
    delete_malformed_remote_tags(malformed_tags)

    print("\n🎉 Malformed tag cleanup complete!")

    return 0


if __name__ == "__main__":
    sys.exit(main())
