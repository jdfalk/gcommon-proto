#!/usr/bin/env python3
# file: fix_queue_duplicates.py
# version: 1.0.0
# guid: 8a9b0c1d-2e3f-4a5b-6c7d-8e9f0a1b2c3d

"""
Script to fix duplicate message definitions in queue proto files.
"""

import os
import re
import subprocess


def get_duplicate_files():
    """Get list of files with duplicate symbol definitions."""
    result = subprocess.run(
        ["buf", "generate", "--path", "pkg/queue/proto/"],
        capture_output=True,
        text=True,
        cwd="/Users/jdfalk/repos/github.com/jdfalk/gcommon",
    )

    duplicate_files = set()
    for line in result.stderr.split("\n"):
        if "already defined" in line:
            # Extract file path from error message
            if "pkg/queue/proto/" in line:
                file_path = line.split(":")[0]
                if file_path.startswith("pkg/queue/proto/"):
                    duplicate_files.add(file_path)

    return list(duplicate_files)


def fix_file_duplicates(file_path):
    """Fix duplicates in a specific file by identifying and removing skeleton definitions."""
    full_path = f"/Users/jdfalk/repos/github.com/jdfalk/gcommon/{file_path}"

    if not os.path.exists(full_path):
        print(f"File not found: {full_path}")
        return False

    with open(full_path, "r") as f:
        content = f.read()

    # Find duplicate message patterns
    message_pattern = r"message\s+(\w+)\s*\{"
    messages = re.findall(message_pattern, content)

    # Count occurrences of each message
    message_counts = {}
    for msg in messages:
        message_counts[msg] = message_counts.get(msg, 0) + 1

    duplicates = [msg for msg, count in message_counts.items() if count > 1]

    if not duplicates:
        print(f"No duplicates found in {file_path}")
        return False

    print(f"Found duplicates in {file_path}: {duplicates}")

    # For now, just report the duplicates
    # Manual intervention needed for complex cases
    return True


def main():
    print("Finding files with duplicate symbols...")
    duplicate_files = get_duplicate_files()

    print(f"Found {len(duplicate_files)} files with duplicates:")
    for file_path in sorted(duplicate_files):
        print(f"  - {file_path}")
        fix_file_duplicates(file_path)


if __name__ == "__main__":
    main()
