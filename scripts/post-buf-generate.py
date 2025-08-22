#!/usr/bin/env python3
# file: scripts/post-buf-generate.py
# version: 1.0.0
# guid: 550e8400-e29b-41d4-a716-446655440026

"""
Post-generation script for buf generate.
This script:
1. Creates/updates the v1 symlink in sdks/go
2. Ensures go.mod files are properly set up
3. Runs go mod tidy to clean up dependencies
"""

import logging
import subprocess
import sys
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def run_command(cmd, cwd=None, check=True):
    """Run a shell command and return the result."""
    try:
        logger.info(f"Running: {' '.join(cmd)} {f'(in {cwd})' if cwd else ''}")
        result = subprocess.run(
            cmd, cwd=cwd, check=check, capture_output=True, text=True
        )
        if result.stdout:
            logger.info(f"Output: {result.stdout.strip()}")
        return result
    except subprocess.CalledProcessError as e:
        logger.error(f"Command failed: {e}")
        logger.error(f"Stderr: {e.stderr}")
        if check:
            raise
        return e


def create_v1_symlink(repo_root):
    """Create/update the v1 symlink in sdks/go."""
    go_sdk_dir = repo_root / "sdks" / "go"
    v1_symlink = go_sdk_dir / "v1"

    # Target for the symlink (relative path)
    target = "github.com/jdfalk/gcommon/sdks/go/v1"

    logger.info(f"Managing v1 symlink at {v1_symlink}")

    # Remove existing symlink if it exists
    if v1_symlink.is_symlink():
        logger.info("Removing existing v1 symlink")
        v1_symlink.unlink()
    elif v1_symlink.exists():
        logger.warning(f"v1 exists but is not a symlink: {v1_symlink}")
        return False

    # Create the symlink
    logger.info(f"Creating symlink: {v1_symlink} -> {target}")
    v1_symlink.symlink_to(target)

    return True


def ensure_go_mod_files(repo_root):
    """Ensure go.mod files are properly configured."""
    go_sdk_dir = repo_root / "sdks" / "go"
    go_mod_path = go_sdk_dir / "go.mod"

    if not go_mod_path.exists():
        logger.error(f"go.mod not found at {go_mod_path}")
        return False

    logger.info("Running go mod tidy")
    result = run_command(["go", "mod", "tidy"], cwd=go_sdk_dir, check=False)

    if result.returncode != 0:
        logger.warning("go mod tidy failed, but continuing")

    return True


def get_current_version(repo_root):
    """Get the latest git tag for versioning."""
    try:
        result = run_command(
            ["git", "describe", "--tags", "--abbrev=0"], cwd=repo_root, check=False
        )
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            logger.warning("No git tags found, using v1.0.0")
            return "v1.0.0"
    except Exception as e:
        logger.warning(f"Error getting git version: {e}")
        return "v1.0.0"


def main():
    """Main function."""
    # Get repository root
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent

    logger.info(f"Repository root: {repo_root}")
    logger.info("Starting post-buf-generate processing")

    try:
        # Create v1 symlink
        if not create_v1_symlink(repo_root):
            logger.error("Failed to create v1 symlink")
            return 1

        # Ensure go.mod files
        if not ensure_go_mod_files(repo_root):
            logger.error("Failed to process go.mod files")
            return 1

        # Get current version
        current_version = get_current_version(repo_root)
        logger.info(f"Current version: {current_version}")

        logger.info("Post-buf-generate processing completed successfully")
        return 0

    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
