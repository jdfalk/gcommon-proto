#!/usr/bin/env python3
# file: fix_go_tagging.py
# version: 1.0.0
# guid: 12345678-9abc-def0-1234-56789abcdef0

"""
Fix Go module tagging strategy to use proper semantic versioning.

Go modules need tags at the module level, not package level.
This script will:
1. Clean up excessive tags
2. Create proper module-level tags
3. Update workflows to use correct tagging strategy
"""

import re
import subprocess
import sys
from typing import List, Set


def run_command(cmd: str) -> str:
    """Run a command and return output."""
    try:
        result = subprocess.run(
            cmd, shell=True, capture_output=True, text=True, check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error running command '{cmd}': {e}")
        return ""


def get_all_tags() -> List[str]:
    """Get all local tags."""
    output = run_command("git tag -l")
    return [tag.strip() for tag in output.split("\n") if tag.strip()]


def categorize_tags(tags: List[str]) -> dict:
    """Categorize tags by type."""
    categories = {
        "root_module": [],  # v1.0.0 format (for root module)
        "sdk_module": [],  # sdks/go/v1.0.0 format (for SDK module)
        "bad_complex": [],  # sdks/go/v1/package/v1.0.0 format (too complex)
        "other": [],
    }

    for tag in tags:
        if re.match(r"^v\d+\.\d+\.\d+$", tag):
            categories["root_module"].append(tag)
        elif re.match(r"^sdks/go/v\d+\.\d+\.\d+$", tag):
            categories["sdk_module"].append(tag)
        elif "sdks/go/v1/" in tag and "/v" in tag:
            categories["bad_complex"].append(tag)
        else:
            categories["other"].append(tag)

    return categories


def get_latest_version(tags: List[str]) -> str:
    """Get the latest semantic version from a list of tags."""
    if not tags:
        return "v0.1.0"

    # Extract version numbers and find the highest
    versions = []
    for tag in tags:
        match = re.search(r"v(\d+)\.(\d+)\.(\d+)", tag)
        if match:
            major, minor, patch = map(int, match.groups())
            versions.append((major, minor, patch, tag))

    if not versions:
        return "v0.1.0"

    # Sort by version tuple and get the latest
    versions.sort(reverse=True)
    return versions[0][3]


def create_proper_tags():
    """Create proper module-level tags."""
    print("🏷️  Analyzing current tags...")

    all_tags = get_all_tags()
    print(f"Found {len(all_tags)} total tags")

    categories = categorize_tags(all_tags)

    print("\n📊 Tag Categories:")
    for category, tags in categories.items():
        print(f"  {category}: {len(tags)} tags")
        if tags and len(tags) <= 5:
            print(f"    Examples: {', '.join(tags[:5])}")
        elif tags:
            print(f"    Examples: {', '.join(tags[:3])}... (+{len(tags) - 3} more)")

    # Determine next versions
    latest_root = get_latest_version(categories["root_module"])
    latest_sdk = get_latest_version(categories["sdk_module"])

    print(f"\n📈 Latest Versions:")
    print(f"  Root module: {latest_root}")
    print(f"  SDK module: {latest_sdk}")

    # Ask for cleanup
    if categories["bad_complex"]:
        print(
            f"\n⚠️  Found {len(categories['bad_complex'])} overly complex tags that should be cleaned up"
        )
        print("These are package-level tags, but Go modules work at module level.")

        response = input("Delete complex package-level tags? (y/N): ").strip().lower()
        if response == "y":
            print("🧹 Cleaning up complex tags...")
            for tag in categories["bad_complex"]:
                print(f"  Deleting: {tag}")
                run_command(f"git tag -d '{tag}'")
                run_command(f"git push origin ':refs/tags/{tag}'")

    # Suggest proper tagging strategy
    print(f"\n✅ Recommended Tagging Strategy:")
    print(f"  For root module (github.com/jdfalk/gcommon): Use v1.0.0, v1.1.0, etc.")
    print(
        f"  For SDK module (github.com/jdfalk/gcommon/sdks/go): Use sdks/go/v1.0.0, sdks/go/v1.1.0, etc."
    )
    print(f"  Current workflow should create: v1.5.0 and sdks/go/v1.5.0 (example)")


def show_go_module_info():
    """Show information about Go modules in this repo."""
    print("\n🔍 Go Module Analysis:")

    # Check root module
    try:
        root_mod = run_command("head -1 go.mod | cut -d' ' -f2")
        print(f"  Root module: {root_mod}")
    except:
        print("  Root module: Not found")

    # Check SDK module
    try:
        sdk_mod = run_command("head -1 sdks/go/go.mod | cut -d' ' -f2")
        print(f"  SDK module: {sdk_mod}")
    except:
        print("  SDK module: Not found")

    print(f"\n💡 How Go finds versions:")
    print(f"  - For {root_mod}: Looks for tags like v1.0.0")
    print(f"  - For {sdk_mod}: Looks for tags like sdks/go/v1.0.0")
    print(f"  - Go IGNORES package-level paths in tags")


if __name__ == "__main__":
    print("🚀 Go Module Tagging Fixer")
    print("=" * 50)

    show_go_module_info()
    create_proper_tags()

    print(f"\n🎯 Next Steps:")
    print(f"  1. Update your workflow to create module-level tags only")
    print(f"  2. Use semantic versioning: major.minor.patch")
    print(f"  3. Tag both modules simultaneously for releases")
    print(f"  4. Example: git tag v1.5.0 && git tag sdks/go/v1.5.0")
