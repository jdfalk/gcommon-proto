#!/usr/bin/env python3
# file: scripts/setup-go-modules.py
# version: 2.0.0
# guid: f1e2d3c4-b5a6-789c-def0-123456789abc

"""
Post-generation script to ensure Go module exists for gcommon SDK.

This script:
1. Ensures the Go SDK directory has a proper go.mod file
2. Validates that generated protobuf code is in the correct location
3. No symlinks needed - buf generates directly to sdks/go/gcommon/v1/
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

    if go_mod_path.exists():
        print(f"✅ Go module already exists: {go_mod_path}")
        return

    go_mod_content = f"""// file: sdks/go/go.mod
// version: 1.0.0
// guid: abcdef01-2345-6789-abcd-ef0123456789

module {module_name}

go 1.21

require (
\tgoogle.golang.org/protobuf v1.34.2
)
"""

    with open(go_mod_path, "w") as f:
        f.write(go_mod_content)
    print(f"Created go.mod: {go_mod_path}")


def main():
    # Get script directory and project root
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    go_sdk_dir = project_root / "sdks" / "go"

    print("Setting up Go SDK module")
    print(f"Working in: {go_sdk_dir}")

    # Ensure the go sdk directory exists
    go_sdk_dir.mkdir(parents=True, exist_ok=True)

    # Ensure go.mod exists with correct module name
    module_name = "github.com/jdfalk/gcommon/sdks/go"
    ensure_go_mod_exists(go_sdk_dir, module_name)

    # Check if generated code exists
    generated_path = go_sdk_dir / "gcommon" / "v1"
    if generated_path.exists():
        package_count = len([d for d in generated_path.iterdir() if d.is_dir()])
        print(f"✅ Generated code found: {package_count} packages in {generated_path}")
    else:
        print(f"⚠️  Generated code not found: {generated_path}")
        print("   This is normal if buf generate hasn't run yet.")

    print("✅ Go module setup complete!")
    print(f"   - Module: {module_name}")
    print("   - Import path: github.com/jdfalk/gcommon/sdks/go/gcommon/v1/<package>")

    return 0


if __name__ == "__main__":
    sys.exit(main())
