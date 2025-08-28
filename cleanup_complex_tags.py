#!/usr/bin/env python3
# file: cleanup_complex_tags.py
# version: 1.0.0
# guid: 87654321-cdef-0123-4567-89abcdef0123

"""
Quick script to clean up complex package-level tags that Go can't use.
"""

import re
import subprocess


def run_command(cmd: str) -> str:
    """Run a command and return output."""
    try:
        result = subprocess.run(
            cmd, shell=True, capture_output=True, text=True, check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return ""


def cleanup_complex_tags():
    """Delete all complex package-level tags."""
    # Get all tags that match the bad pattern
    output = run_command("git tag -l")
    all_tags = [tag.strip() for tag in output.split("\n") if tag.strip()]

    # Find complex tags (package-level versioning)
    complex_tags = [tag for tag in all_tags if "sdks/go/v1/" in tag and "/v" in tag]

    print(f"Found {len(complex_tags)} complex tags to delete")

    if not complex_tags:
        print("No complex tags found!")
        return

    print("Examples:", complex_tags[:5])

    response = (
        input(f"\nDelete {len(complex_tags)} complex tags? (y/N): ").strip().lower()
    )

    if response != "y":
        print("Cancelled.")
        return

    # Delete locally first
    print(f"\n🗑️  Deleting {len(complex_tags)} local tags...")
    deleted_count = 0
    for tag in complex_tags:
        result = run_command(f"git tag -d '{tag}'")
        if "Deleted tag" in result:
            deleted_count += 1
            if deleted_count % 20 == 0:
                print(f"  Deleted {deleted_count}/{len(complex_tags)}...")

    print(f"✅ Deleted {deleted_count} local tags")

    # Delete from remote in batches
    print(f"\n🌐 Deleting from remote...")
    batch_size = 50  # Avoid command line length limits

    for i in range(0, len(complex_tags), batch_size):
        batch = complex_tags[i : i + batch_size]
        # Create refs to delete
        refs_to_delete = [f":refs/tags/{tag}" for tag in batch]

        cmd = f"git push origin {' '.join(refs_to_delete)}"
        print(
            f"  Deleting batch {i // batch_size + 1}/{(len(complex_tags) + batch_size - 1) // batch_size}..."
        )

        result = run_command(cmd)
        if result:
            print(f"    {result}")

    print(f"✅ Done! Deleted {len(complex_tags)} complex tags")


if __name__ == "__main__":
    cleanup_complex_tags()
