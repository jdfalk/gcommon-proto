#!/usr/bin/env python3
# file: scripts/setup-go-modules.py
# version: 1.0.0
# guid: f1e2d3c4-b5a6-789c-def0-123456789abc

"""
Post-generation script to set up Go modules and symlinks for gcommon SDK.

This script:
1. Creates the v1 symlink pointing to the generated Go code
2. Creates go.mod files in all module subfolders
3. Sets up proper module paths for versioned imports
"""

import os
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


def create_symlink(target, link_path):
    """Create a symlink, removing existing one if present."""
    if link_path.exists() or link_path.is_symlink():
        if link_path.is_symlink():
            link_path.unlink()
        elif link_path.is_dir():
            link_path.rmdir()
        elif link_path.is_file():
            link_path.unlink()

    # Create relative symlink
    relative_target = os.path.relpath(target, link_path.parent)
    link_path.symlink_to(relative_target)
    print(f"Created symlink: {link_path} -> {relative_target}")


def create_go_mod(module_path, module_name, version):
    """Create a go.mod file in the specified directory."""
    go_mod_content = f"""module {module_name}

go 1.22
"""

    go_mod_path = module_path / "go.mod"
    with open(go_mod_path, "w") as f:
        f.write(go_mod_content)
    print(f"Created go.mod: {go_mod_path}")


def main():
    # Get script directory and project root
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    go_sdk_dir = project_root / "sdks" / "go"

    # Get version
    version = get_latest_version_tag()
    major_version = version.split(".")[0]  # e.g., "v1" from "v1.2.3"

    print(f"Setting up Go modules for version {version}")
    print(f"Working in: {go_sdk_dir}")

    # Ensure the go sdk directory exists
    go_sdk_dir.mkdir(parents=True, exist_ok=True)

    # Path to the actual generated code (what buf creates)
    actual_generated_path = go_sdk_dir / "gcommon" / major_version

    # Create the github.com import path structure
    github_path = (
        go_sdk_dir / "github.com" / "jdfalk" / "gcommon" / "sdks" / "go" / major_version
    )
    github_path.mkdir(parents=True, exist_ok=True)

    # Create v1 symlink in the root go directory pointing to the github.com path
    v1_symlink = go_sdk_dir / major_version
    if github_path.exists():
        create_symlink(github_path, v1_symlink)
    else:
        print(f"Warning: GitHub import path not found: {github_path}")
        print(
            "This is normal after buf clean. The symlink will be created on next buf generate."
        )

    # Create root go.mod for the entire SDK
    create_go_mod(go_sdk_dir, "github.com/jdfalk/gcommon/proto", version)

    # If the actual generated code exists, create symlinks in the github.com path
    # but create only ONE go.mod for the entire github.com path, not per module
    if actual_generated_path.exists():
        for module_dir in actual_generated_path.iterdir():
            if module_dir.is_dir() and not module_dir.name.startswith("."):
                # Create symlink from github.com path to actual generated code
                target_dir = github_path / module_dir.name
                create_symlink(module_dir, target_dir)

        # Create a single go.mod for the entire v1 module (in the github.com path)
        module_name = "github.com/jdfalk/gcommon/proto"
        create_go_mod(github_path, module_name, version)
    else:
        print(f"Warning: Generated code path not found: {actual_generated_path}")
        print(
            "This is normal after buf clean. The modules will be created on next buf generate."
        )

    print("✅ Go module setup complete!")
    print(f"   - Version: {version}")
    print(f"   - Symlink: {v1_symlink}")
    print(
        "   - Modules available for import as: github.com/jdfalk/gcommon/proto/<module>"
    )

    return 0


if __name__ == "__main__":
    sys.exit(main())
