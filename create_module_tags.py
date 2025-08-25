#!/usr/bin/env python3
# file: create_module_tags.py
# version: 1.0.0
# guid: abc12345-6789-abcd-ef01-234567890abc

"""
Create all missing module-specific tags for gcommon SDK modules.

This script creates tags like:
- sdks/go/v1/common/v1.1.0
- sdks/go/v1/config/v1.1.0
etc. for each module and each version.
"""

import subprocess
import sys


def get_all_version_tags():
    """Get all version tags from git."""
    try:
        result = subprocess.run(
            ["git", "tag", "-l", "v*"],
            capture_output=True,
            text=True,
            check=True,
        )
        return [tag.strip() for tag in result.stdout.split("\n") if tag.strip()]
    except subprocess.CalledProcessError as e:
        print(f"Error getting tags: {e}")
        return []


def get_existing_module_tags():
    """Get all existing module tags."""
    try:
        result = subprocess.run(
            ["git", "tag", "-l", "sdks/go/v1/*/v*"],
            capture_output=True,
            text=True,
            check=True,
        )
        return [tag.strip() for tag in result.stdout.split("\n") if tag.strip()]
    except subprocess.CalledProcessError:
        return []


def create_tag(tag_name, commit_ref):
    """Create a git tag."""
    try:
        subprocess.run(
            ["git", "tag", tag_name, commit_ref],
            capture_output=True,
            text=True,
            check=True,
        )
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error creating tag {tag_name}: {e.stderr}")
        return False


def main():
    # Define all SDK modules
    modules = [
        "common",
        "config",
        "database",
        "media",
        "metrics",
        "organization",
        "queue",
        "web",
    ]

    # Get all version tags (like v1.0.0, v1.1.0, etc.)
    version_tags = get_all_version_tags()
    print(f"Found {len(version_tags)} version tags")

    # Filter to only get clean version tags (not module-specific ones)
    clean_version_tags = [tag for tag in version_tags if not tag.startswith("sdks/")]
    clean_version_tags.sort()

    print(f"Clean version tags: {clean_version_tags}")

    # Get existing module tags to avoid duplicates
    existing_module_tags = get_existing_module_tags()
    print(f"Found {len(existing_module_tags)} existing module tags")

    tags_created = 0
    tags_skipped = 0

    for version in clean_version_tags:
        for module in modules:
            module_tag = f"sdks/go/v1/{module}/{version}"

            if module_tag in existing_module_tags:
                print(f"✓ Tag already exists: {module_tag}")
                tags_skipped += 1
                continue

            print(f"Creating tag: {module_tag} -> {version}")
            if create_tag(module_tag, version):
                tags_created += 1
                print(f"✅ Created: {module_tag}")
            else:
                print(f"❌ Failed: {module_tag}")

    print("\n📊 Summary:")
    print(f"   Tags created: {tags_created}")
    print(f"   Tags skipped (already exist): {tags_skipped}")
    print(f"   Total modules: {len(modules)}")
    print(f"   Total versions: {len(clean_version_tags)}")
    print(f"   Expected total tags: {len(modules) * len(clean_version_tags)}")

    if tags_created > 0:
        print("\n🚀 To push all tags to remote:")
        print("   git push origin --tags")

    return 0


if __name__ == "__main__":
    sys.exit(main())
