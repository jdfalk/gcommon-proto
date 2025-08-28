#!/usr/bin/env python3
# file: delete_complex_tags_now.py
# version: 1.0.0
# guid: 11111111-2222-3333-4444-555555555555

"""
Delete complex package-level tags without interaction.
"""

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


def main():
    # Get all tags that match the bad pattern
    output = run_command("git tag -l")
    all_tags = [tag.strip() for tag in output.split("\n") if tag.strip()]

    # Find complex tags (package-level versioning)
    complex_tags = [tag for tag in all_tags if "sdks/go/v1/" in tag and "/v" in tag]

    print(f"🔍 Found {len(complex_tags)} complex package-level tags")
    print(f"Examples: {complex_tags[:3]}...")

    if not complex_tags:
        print("✅ No complex tags found!")
        return

    print(f"\n🗑️ Deleting {len(complex_tags)} local tags...")

    # Delete locally
    deleted_count = 0
    for i, tag in enumerate(complex_tags):
        result = run_command(f"git tag -d '{tag}'")
        if "Deleted tag" in result or "was" in result:
            deleted_count += 1

        if (i + 1) % 50 == 0 or i == len(complex_tags) - 1:
            print(f"  Progress: {i + 1}/{len(complex_tags)} ({deleted_count} deleted)")

    print(f"✅ Deleted {deleted_count} local tags")

    print(f"\n🌐 Deleting from remote (this may take a while)...")

    # Delete from remote in smaller batches
    batch_size = 30
    success_count = 0

    for i in range(0, len(complex_tags), batch_size):
        batch = complex_tags[i : i + batch_size]
        refs_to_delete = [f":refs/tags/{tag}" for tag in batch]

        batch_num = i // batch_size + 1
        total_batches = (len(complex_tags) + batch_size - 1) // batch_size

        print(f"  Batch {batch_num}/{total_batches}: Deleting {len(batch)} tags...")

        cmd = f"git push origin {' '.join(refs_to_delete)}"
        result = run_command(cmd)

        if "deleted" in result.lower() or len(result) == 0:
            success_count += len(batch)
            print(f"    ✅ Success")
        else:
            print(f"    ⚠️ Result: {result[:100]}...")

    print(f"\n🎉 Cleanup complete!")
    print(f"   Local: {deleted_count} tags deleted")
    print(f"   Remote: {success_count} tags deleted")

    # Check remaining tags
    remaining = run_command("git tag -l | grep 'sdks/go/v1/' | wc -l").strip()
    print(f"   Remaining complex tags: {remaining}")


if __name__ == "__main__":
    main()
