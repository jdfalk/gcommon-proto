#!/usr/bin/env python3
# file: create_proper_tags.py
# version: 1.0.0
# guid: aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee

"""
Create proper Go module tags for both root and SDK modules.
This is the CORRECT way to tag Go modules.
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


def get_latest_version(tags):
    """Get the latest semantic version."""
    versions = []
    for tag in tags:
        match = re.search(r"v(\d+)\.(\d+)\.(\d+)", tag)
        if match:
            major, minor, patch = map(int, match.groups())
            versions.append((major, minor, patch, tag))

    if not versions:
        return None

    versions.sort(reverse=True)
    return versions[0][3]


def main():
    print("🏷️ Go Module Tagging Guide")
    print("=" * 50)

    # Get current tags
    all_tags = run_command("git tag -l").split("\n")
    root_tags = [tag for tag in all_tags if re.match(r"^v\d+\.\d+\.\d+$", tag)]
    sdk_tags = [tag for tag in all_tags if tag.startswith("sdks/go/v")]

    latest_root = get_latest_version(root_tags)
    latest_sdk = get_latest_version(sdk_tags)

    print(f"📊 Current Status:")
    print(f"  Root module tags: {len(root_tags)} (latest: {latest_root})")
    print(f"  SDK module tags: {len(sdk_tags)} (latest: {latest_sdk})")

    print(f"\n✅ CORRECT Go Module Tagging:")
    print(f"  🎯 Root module (github.com/jdfalk/gcommon):")
    print(f"     Uses simple tags: v1.0.0, v1.1.0, v1.2.0, etc.")
    print(f"     Command: git tag v1.5.0 && git push origin v1.5.0")

    print(f"\n  🎯 SDK module (github.com/jdfalk/gcommon/sdks/go):")
    print(f"     Uses prefixed tags: sdks/go/v1.0.0, sdks/go/v1.1.0, etc.")
    print(f"     Command: git tag sdks/go/v1.5.0 && git push origin sdks/go/v1.5.0")

    print(f"\n📝 How Go Resolves Versions:")
    print(f"  When someone imports: github.com/jdfalk/gcommon/sdks/go@v1.4.0")
    print(f"  Go looks for tag: sdks/go/v1.4.0 ✅ (FOUND!)")
    print(
        f"  Go IGNORES: sdks/go/v1/common/v1.4.0 ❌ (package-level, not module-level)"
    )

    print(f"\n🚀 Workflow Integration:")
    print(f"  Your GitHub workflow should create BOTH tags simultaneously:")
    print(f"  1. Calculate next version (e.g., v1.5.0)")
    print(f"  2. Create root tag: git tag v1.5.0")
    print(f"  3. Create SDK tag: git tag sdks/go/v1.5.0")
    print(f"  4. Push both: git push origin v1.5.0 sdks/go/v1.5.0")

    print(f"\n🔧 go.mod Files:")
    print(f"  Root: module github.com/jdfalk/gcommon")
    print(f"  SDK:  module github.com/jdfalk/gcommon/sdks/go")
    print(f"  This creates TWO separate Go modules in one repo")

    if latest_root and latest_sdk:
        if latest_root != latest_sdk.replace("sdks/go/", ""):
            next_version = latest_root.replace("v", "").split(".")
            next_version[2] = str(int(next_version[2]) + 1)
            next_ver = f"v{'.'.join(next_version)}"

            print(f"\n💡 Suggestion:")
            print(f"  Create matching SDK tag for current version:")
            print(
                f"  git tag sdks/go/{latest_root} && git push origin sdks/go/{latest_root}"
            )


if __name__ == "__main__":
    main()
