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


def ensure_go_sdk_structure(repo_root):
    """Ensure the Go SDK structure is properly set up after buf generate."""
    go_sdk_dir = repo_root / "sdks" / "go"
    v1_dir = go_sdk_dir / "v1"

    logger.info(f"Checking Go SDK structure at {go_sdk_dir}")

    # Ensure v1 directory exists (should be created by buf generate)
    if not v1_dir.exists():
        logger.error(
            f"v1 directory not found at {v1_dir} - buf generate may have failed"
        )
        return False

    # Count the number of packages generated
    package_dirs = [d for d in v1_dir.iterdir() if d.is_dir()]
    logger.info(
        f"Found {len(package_dirs)} generated packages: {[d.name for d in package_dirs]}"
    )

    return True


def ensure_go_mod_files(repo_root):
    """Ensure go.mod files are properly configured."""
    go_sdk_dir = repo_root / "sdks" / "go"
    go_mod_path = go_sdk_dir / "go.mod"

    # If go.mod doesn't exist, run setup-go-modules.py to create it
    if not go_mod_path.exists():
        logger.info("go.mod not found, running setup-go-modules.py to create it")
        setup_script = repo_root / "scripts" / "setup-go-modules.py"

        if setup_script.exists():
            result = run_command(
                ["python3", str(setup_script)], cwd=repo_root, check=False
            )
            if result.returncode != 0:
                logger.error("setup-go-modules.py failed")
                return False
        else:
            logger.error(f"setup-go-modules.py not found at {setup_script}")
            return False

    if not go_mod_path.exists():
        logger.error(f"go.mod still not found at {go_mod_path} after running setup")
        return False

    logger.info("Running go mod tidy on main SDK module")
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
        # Ensure Go SDK structure is correct
        if not ensure_go_sdk_structure(repo_root):
            logger.error("Failed to verify Go SDK structure")
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
