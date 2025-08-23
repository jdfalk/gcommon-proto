#!/usr/bin/env python3
# file: scripts/setup-go-modules.py
# version: 2.1.0
# guid: f1e2d3c4-b5a6-789c-def0-123456789abc

"""
Post-generation script to ensure Go modules exist for gcommon SDK.

This script:
1. Ensures the Go SDK directory has a proper go.mod file
2. Updates the root go.mod file with correct replace directive
3. Validates that generated protobuf code is in the correct location
4. Ensures all paths match the actual generated structure
"""

import subprocess
import sys
from pathlib import Path


def get_latest_version_tag():
    """Get the latest version tag from git."""
    try:
        result = subprocess.run(
            ["git", "describe", "--tags", "--abbrev=0", "--match=v*"],
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return "v1.0.0"  # Default if no tags exist


def ensure_go_mod_exists(module_path, module_name):
    """Ensure go.mod file exists and has correct content."""
    go_mod_path = module_path / "go.mod"

    go_mod_content = f"""// file: sdks/go/go.mod
// version: 1.1.0
// guid: abcdef01-2345-6789-abcd-ef0123456789

module {module_name}

go 1.23

require (
\tgoogle.golang.org/protobuf v1.34.2
\tgoogle.golang.org/grpc v1.65.0
)

require (
\tgolang.org/x/net v0.28.0 // indirect
\tgolang.org/x/sys v0.24.0 // indirect
\tgolang.org/x/text v0.17.0 // indirect
\tgoogle.golang.org/genproto/googleapis/rpc v0.0.0-20240730163845-b1a4ccb954bf // indirect
)
"""

    with open(go_mod_path, "w") as f:
        f.write(go_mod_content)
    print(f"Created/updated go.mod: {go_mod_path}")


def update_root_go_mod(project_root):
    """Update the root go.mod file with correct replace directive."""
    root_go_mod = project_root / "go.mod"

    if not root_go_mod.exists():
        print(f"⚠️  Root go.mod not found: {root_go_mod}")
        return

    # Read the current content
    with open(root_go_mod, "r") as f:
        content = f.read()

    # Check if it has the old incorrect replace directive
    old_replace = "replace github.com/jdfalk/gcommon/proto => ./sdks/go/v1"
    new_replace = "replace github.com/jdfalk/gcommon/proto => ./sdks/go/gcommon/v1"

    if old_replace in content:
        content = content.replace(old_replace, new_replace)
        with open(root_go_mod, "w") as f:
            f.write(content)
        print(f"✅ Updated root go.mod replace directive: {new_replace}")
    elif new_replace in content:
        print("✅ Root go.mod already has correct replace directive")
    else:
        print("⚠️  Root go.mod needs manual update for replace directive")


def main():
    # Get script directory and project root
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    go_sdk_dir = project_root / "sdks" / "go"

    print("Setting up Go SDK modules")
    print(f"Working in: {go_sdk_dir}")

    # Ensure the go sdk directory exists
    go_sdk_dir.mkdir(parents=True, exist_ok=True)

    # Ensure go.mod exists with correct module name
    module_name = "github.com/jdfalk/gcommon/sdks/go"
    ensure_go_mod_exists(go_sdk_dir, module_name)

    # Update root go.mod with correct replace directive
    update_root_go_mod(project_root)

    # Check if generated code exists
    generated_path = go_sdk_dir / "gcommon" / "v1"
    if generated_path.exists():
        package_count = len([d for d in generated_path.iterdir() if d.is_dir()])
        print(f"✅ Generated code found: {package_count} packages in {generated_path}")

        # List the packages for verification
        packages = [d.name for d in generated_path.iterdir() if d.is_dir()]
        print(f"   Packages: {', '.join(sorted(packages))}")
    else:
        print(f"⚠️  Generated code not found: {generated_path}")
        print("   This is normal if buf generate hasn't run yet.")

    print("✅ Go module setup complete!")
    print(f"   - SDK Module: {module_name}")
    print("   - Import path: github.com/jdfalk/gcommon/sdks/go/gcommon/v1/<package>")
    print("   - Replace directive: ./sdks/go/gcommon/v1")

    return 0


if __name__ == "__main__":
    sys.exit(main())
