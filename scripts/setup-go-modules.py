#!/usr/bin/env python3
# file: scripts/setup-go-modules.py
# version: 2.7.0
# guid: f1e2d3c4-b5a6-789c-def0-123456789abc

"""
Post-generation script to enforce a single Go module for the gcommon SDK.

Changes in v2.7.0:
 - Removed per-package module generation logic
 - Removed per-package go mod tidy / fmt invocations
 - Added cleanup of legacy per-package go.mod files
 - Retain only main SDK module (sdks/go) management
 - Run a single go mod tidy
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


def ensure_go_mod_exists(module_path, module_name, file_path_comment="sdks/go/go.mod"):
    """Ensure single SDK go.mod file exists with core dependencies only."""
    go_mod_path = module_path / "go.mod"

    requires_section = "\n".join(
        [
            "\tgoogle.golang.org/protobuf v1.36.8",
            "\tgoogle.golang.org/grpc v1.75.0",
            "\tbuf.build/go/protovalidate v0.14.0",
        ]
    )

    go_mod_content = f"""// file: {file_path_comment}
// version: 1.3.1
// guid: abcdef01-2345-6789-abcd-ef0123456789

module {module_name}

go 1.23

require (
{requires_section}
)

// Indirect dependencies intentionally omitted; maintained via `go mod tidy`.
"""

    with open(go_mod_path, "w") as f:
        f.write(go_mod_content)
    print(f"Created/updated go.mod: {go_mod_path}")


def run_go_mod_tidy(module_path):
    """Run go mod tidy in the module directory."""
    try:
        subprocess.run(
            ["go", "mod", "tidy"],
            cwd=module_path,
            capture_output=True,
            text=True,
            check=True,
        )
        print(f"✅ go mod tidy successful: {module_path}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ go mod tidy failed in {module_path}:")
        print(f"   stdout: {e.stdout}")
        print(f"   stderr: {e.stderr}")
        return False


def run_go_fmt(module_path):
    """Run go fmt in the module directory."""
    try:
        result = subprocess.run(
            ["go", "fmt", "./..."],
            cwd=module_path,
            capture_output=True,
            text=True,
            check=True,
        )
        if result.stdout.strip():
            print(f"✅ go fmt formatted files: {module_path}")
            print(f"   formatted: {result.stdout.strip()}")
        else:
            print(f"✅ go fmt: no formatting needed: {module_path}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ go fmt failed in {module_path}:")
        print(f"   stdout: {e.stdout}")
        print(f"   stderr: {e.stderr}")
        return False


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
    old_replace = "replace github.com/jdfalk/gcommon/proto => ./sdks/go/gcommon/v1"
    new_replace = "replace github.com/jdfalk/gcommon/proto => ./sdks/go/v1"

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

    print("Setting up single Go SDK module")
    print(f"Working in: {go_sdk_dir}")

    # Ensure the go sdk directory exists
    go_sdk_dir.mkdir(parents=True, exist_ok=True)

    # Ensure main SDK go.mod exists with correct module name
    module_name = "github.com/jdfalk/gcommon/sdks/go"
    ensure_go_mod_exists(go_sdk_dir, module_name)

    # Update root go.mod with correct replace directive
    update_root_go_mod(project_root)

    # Remove any legacy per-package go.mod files
    generated_path = go_sdk_dir / "v1"
    removed = []
    if generated_path.exists():
        for path in generated_path.rglob("go.mod"):
            try:
                path.unlink()
                removed.append(path)
            except OSError as e:
                print(f"⚠️  Could not remove {path}: {e}")
    if removed:
        print(f"🧹 Removed {len(removed)} legacy per-package go.mod files")
    else:
        print("✅ No legacy per-package go.mod files present")

    # Run go mod tidy and go fmt on the main SDK module
    print("\n🔧 Running go mod tidy and go fmt on single SDK module...")
    if run_go_mod_tidy(go_sdk_dir):
        print("✅ Main SDK module go mod tidy successful")
        run_go_fmt(go_sdk_dir)
    else:
        print("❌ Main SDK module go mod tidy failed")

    # Inform about generated protobuf packages (for visibility only)
    if generated_path.exists():
        pkgs = [d.name for d in generated_path.iterdir() if d.is_dir()]
        if pkgs:
            print(f"✅ Generated protobuf packages detected: {', '.join(sorted(pkgs))}")
        else:
            print("ℹ️ No generated protobuf packages detected (run buf generate?)")
    else:
        print("ℹ️ Generated path missing (run buf generate before usage)")

    print("\n✅ Go SDK single-module setup complete!")
    print(f"   - SDK Module: {module_name}")
    print("   - Legacy per-package modules: removed if present")
    print("   - go mod tidy: executed once")

    return 0


if __name__ == "__main__":
    sys.exit(main())
