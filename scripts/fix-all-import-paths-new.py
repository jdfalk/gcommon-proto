#!/usr/bin/env python3
# file: scripts/fix-all-import-paths-new.py
# version: 2.0.0
# guid: 6a7b8c9d-0e1f-2a3b-4c5d-6e7f8a9b0c1d

"""
Comprehensive import path fixer for protobuf files.

This script fixes import statements in protobuf files based on the actual current structure:
- pkg/{domain}/proto/ (Go packages)
- proto/gcommon/v1/{domain}/{category}/ (proto definitions)

It scans the actual file locations and fixes import paths accordingly.
"""

import logging
import re
import sys
from pathlib import Path
from typing import Dict

# Set up logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Project root directory
PROJECT_ROOT = Path(__file__).parent.parent
PKG_DIR = PROJECT_ROOT / "pkg"
PROTO_DIR = PROJECT_ROOT / "proto"


class ImportPathFixer:
    def __init__(self):
        self.proto_file_map: Dict[str, str] = {}  # filename -> full_path
        self.files_processed = 0
        self.imports_fixed = 0

    def scan_proto_files(self):
        """Scan all protobuf files and build a mapping."""
        logger.info("Scanning protobuf files...")

        # Scan pkg directory
        if PKG_DIR.exists():
            for proto_file in PKG_DIR.rglob("*.proto"):
                self.proto_file_map[proto_file.name] = str(
                    proto_file.relative_to(PROJECT_ROOT)
                )

        # Scan proto directory
        if PROTO_DIR.exists():
            for proto_file in PROTO_DIR.rglob("*.proto"):
                self.proto_file_map[proto_file.name] = str(
                    proto_file.relative_to(PROJECT_ROOT)
                )

        logger.info(f"Found {len(self.proto_file_map)} proto files")

    def fix_import_path(self, import_path: str) -> str:
        """Fix a single import path."""
        # Extract filename from import path
        if "/" in import_path:
            filename = import_path.split("/")[-1]
        else:
            filename = import_path

        # If we have this file in our mapping, use the correct path
        if filename in self.proto_file_map:
            return self.proto_file_map[filename]

        return import_path

    def fix_proto_file(self, proto_path: Path) -> bool:
        """Fix import statements in a single proto file."""
        try:
            with open(proto_path, "r", encoding="utf-8") as f:
                content = f.read()

            original_content = content
            lines = content.split("\n")

            for i, line in enumerate(lines):
                # Match import statements
                import_match = re.match(
                    r'^(\s*import\s+["\'])([^"\']+)(["\'];?\s*)$', line
                )
                if import_match:
                    prefix, import_path, suffix = import_match.groups()

                    # Fix the import path
                    new_import_path = self.fix_import_path(import_path)
                    if new_import_path != import_path:
                        lines[i] = f"{prefix}{new_import_path}{suffix}"
                        self.imports_fixed += 1
                        logger.info(f"Fixed import: {import_path} -> {new_import_path}")

            # Fix go_package if needed
            content = "\n".join(lines)
            content = self.fix_go_package(content, proto_path)

            # Write back if changed
            if content != original_content:
                with open(proto_path, "w", encoding="utf-8") as f:
                    f.write(content)
                return True

        except Exception as e:
            logger.error(f"Error processing {proto_path}: {e}")

        return False

    def fix_go_package(self, content: str, proto_path: Path) -> str:
        """Fix go_package option based on file location."""
        try:
            # Determine the correct go_package from file path
            relative_path = proto_path.relative_to(PROJECT_ROOT)
            path_parts = str(relative_path).split("/")

            # For files in pkg/{domain}/proto/
            if (
                len(path_parts) >= 3
                and path_parts[0] == "pkg"
                and path_parts[2] == "proto"
            ):
                domain = path_parts[1]
                new_go_package = f"github.com/jdfalk/gcommon/pkg/{domain}/proto"

                # Replace go_package option
                go_package_pattern = r'option\s+go_package\s*=\s*["\'][^"\']*["\'];?'
                new_go_package_line = f'option go_package = "{new_go_package}";'

                content = re.sub(go_package_pattern, new_go_package_line, content)

            # For files in proto/gcommon/v1/{domain}/{category}/
            elif (
                len(path_parts) >= 5
                and path_parts[0] == "proto"
                and path_parts[1] == "gcommon"
            ):
                domain = path_parts[3]
                category = path_parts[4]
                new_go_package = (
                    f"github.com/jdfalk/gcommon/proto/gcommon/v1/{domain}/{category}"
                )

                # Replace go_package option
                go_package_pattern = r'option\s+go_package\s*=\s*["\'][^"\']*["\'];?'
                new_go_package_line = f'option go_package = "{new_go_package}";'

                content = re.sub(go_package_pattern, new_go_package_line, content)

        except Exception as e:
            logger.warning(f"Could not fix go_package for {proto_path}: {e}")

        return content

    def process_all_files(self):
        """Process all proto files."""
        logger.info("Processing all proto files...")

        all_proto_files = []

        # Collect all proto files
        if PKG_DIR.exists():
            all_proto_files.extend(PKG_DIR.rglob("*.proto"))
        if PROTO_DIR.exists():
            all_proto_files.extend(PROTO_DIR.rglob("*.proto"))

        for proto_file in all_proto_files:
            if self.fix_proto_file(proto_file):
                self.files_processed += 1

    def run(self):
        """Run the complete import fixing process."""
        logger.info("Starting import path fixing...")

        # Step 1: Scan all proto files
        self.scan_proto_files()

        # Step 2: Fix all files
        self.process_all_files()

        # Summary
        logger.info("Import fixing complete!")
        logger.info(f"Files processed: {self.files_processed}")
        logger.info(f"Import statements fixed: {self.imports_fixed}")


def main():
    """Main entry point."""
    if not PKG_DIR.exists() and not PROTO_DIR.exists():
        logger.error("No proto directories found")
        sys.exit(1)

    fixer = ImportPathFixer()
    fixer.run()


if __name__ == "__main__":
    main()
