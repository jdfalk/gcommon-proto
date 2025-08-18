#!/usr/bin/env python3
# file: scripts/fix-all-import-paths.py
# version: 2.0.0
# guid: 6a7b8c9d-0e1f-2a3b-4c5d-6e7f8a9b0c1d

"""
Comprehensive import path fixer for protobuf files.

This script fixes all import statements in protobuf files to use correct paths based on the current structure:
- pkg/{domain}/proto/ (Go packages)
- proto/gcommon/v1/{domain}/{category}/ (proto definitions)

It handles:
1. Import statements in .proto files
2. Go package declarations in .proto files
3. Cross-references between different structures
"""

import logging
import re
import sys
from pathlib import Path
from typing import Dict, Set

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
        self.file_mappings: Dict[str, str] = {}  # old_path -> new_path
        self.import_fixes: Dict[str, str] = {}  # old_import -> new_import
        self.files_processed = 0
        self.imports_fixed = 0

    def scan_existing_structure(self):
        """Scan the current structure to build file mappings."""
        logger.info("Scanning current protobuf structure...")

        # Find all .proto files in new structure
        for domain in DOMAINS:
            domain_path = PKG_DIR / domain
            if not domain_path.exists():
                continue

            for category in CATEGORIES:
                category_path = domain_path / category
                if not category_path.exists():
                    continue

                for proto_file in category_path.glob("*.proto"):
                    relative_path = f"pkg/{domain}/{category}/{proto_file.name}"
                    self.file_mappings[proto_file.name] = relative_path

                    # Create import mapping (without .proto extension)
                    import_name = proto_file.stem
                    self.import_fixes[f"{domain}/{import_name}"] = (
                        f"{domain}/{category}/{import_name}"
                    )

        logger.info(f"Found {len(self.file_mappings)} proto files in new structure")

    def fix_proto_file(self, proto_path: Path) -> bool:
        """Fix import statements and go_package in a single proto file."""
        try:
            with open(proto_path, "r", encoding="utf-8") as f:
                content = f.read()

            original_content = content

            # Fix import statements
            content = self.fix_import_statements(content)

            # Fix go_package option
            content = self.fix_go_package(content, proto_path)

            # Write back if changed
            if content != original_content:
                with open(proto_path, "w", encoding="utf-8") as f:
                    f.write(content)
                logger.info(f"Fixed imports in {proto_path.relative_to(PROJECT_ROOT)}")
                return True

        except Exception as e:
            logger.error(f"Error processing {proto_path}: {e}")

        return False

    def fix_import_statements(self, content: str) -> str:
        """Fix import statements in proto file content."""
        lines = content.split("\n")

        for i, line in enumerate(lines):
            # Match import statements
            import_match = re.match(r'^(\s*import\s+["\'])([^"\']+)(["\'];?\s*)$', line)
            if import_match:
                prefix, import_path, suffix = import_match.groups()

                # Try to fix the import path
                new_import_path = self.fix_single_import_path(import_path)
                if new_import_path != import_path:
                    lines[i] = f"{prefix}{new_import_path}{suffix}"
                    self.imports_fixed += 1

        return "\n".join(lines)

    def fix_single_import_path(self, import_path: str) -> str:
        """Fix a single import path."""
        # Handle different import patterns

        # Pattern 1: pkg/domain/filename.proto -> pkg/domain/category/filename.proto
        match = re.match(r"^pkg/([^/]+)/([^/]+\.proto)$", import_path)
        if match:
            domain, filename = match.groups()
            if domain in DOMAINS and filename in self.file_mappings:
                return self.file_mappings[filename]

        # Pattern 2: domain/filename.proto -> domain/category/filename.proto
        match = re.match(r"^([^/]+)/([^/]+\.proto)$", import_path)
        if match:
            domain, filename = match.groups()
            if domain in DOMAINS and filename in self.file_mappings:
                return self.file_mappings[filename]

        # Pattern 3: filename.proto -> determine domain and category
        if import_path.endswith(".proto") and "/" not in import_path:
            if import_path in self.file_mappings:
                return self.file_mappings[import_path]

        return import_path

    def fix_go_package(self, content: str, proto_path: Path) -> str:
        """Fix go_package option based on file location."""
        # Determine the correct go_package from file path
        try:
            relative_path = proto_path.relative_to(PKG_DIR)
            parts = relative_path.parts

            if len(parts) >= 2:  # domain/category/file.proto
                domain = parts[0]
                category = parts[1] if len(parts) > 2 else "proto"

                new_go_package = f"github.com/jdfalk/gcommon/pkg/{domain}/{category}"

                # Replace go_package option
                go_package_pattern = r'option\s+go_package\s*=\s*["\'][^"\']*["\'];?'
                new_go_package_line = f'option go_package = "{new_go_package}";'

                content = re.sub(go_package_pattern, new_go_package_line, content)

        except Exception as e:
            logger.warning(f"Could not fix go_package for {proto_path}: {e}")

        return content

    def process_all_proto_files(self):
        """Process all proto files in the project."""
        logger.info("Processing all proto files...")

        # Process files in pkg directory
        for proto_file in PKG_DIR.rglob("*.proto"):
            if self.fix_proto_file(proto_file):
                self.files_processed += 1

        # Process files in other directories that might have proto files
        for proto_file in PROJECT_ROOT.rglob("*.proto"):
            if not str(proto_file).startswith(str(PKG_DIR)):
                if self.fix_proto_file(proto_file):
                    self.files_processed += 1

    def fix_documentation_references(self):
        """Fix references in documentation files."""
        logger.info("Fixing documentation references...")

        # Process markdown files
        for md_file in PROJECT_ROOT.rglob("*.md"):
            try:
                with open(md_file, "r", encoding="utf-8") as f:
                    content = f.read()

                original_content = content

                # Fix file path references in documentation
                for old_path, new_path in self.file_mappings.items():
                    # Replace various patterns
                    content = re.sub(
                        rf"\bpkg/([^/]+)/{re.escape(old_path)}\b", new_path, content
                    )

                if content != original_content:
                    with open(md_file, "w", encoding="utf-8") as f:
                        f.write(content)
                    logger.info(
                        f"Fixed references in {md_file.relative_to(PROJECT_ROOT)}"
                    )

            except Exception as e:
                logger.error(f"Error processing {md_file}: {e}")

    def run(self):
        """Run the complete import fixing process."""
        logger.info("Starting comprehensive import path fixing...")

        # Step 1: Scan current structure
        self.scan_existing_structure()

        # Step 2: Fix proto files
        self.process_all_proto_files()

        # Step 3: Fix documentation
        self.fix_documentation_references()

        # Summary
        logger.info("Import fixing complete!")
        logger.info(f"Files processed: {self.files_processed}")
        logger.info(f"Import statements fixed: {self.imports_fixed}")


def main():
    """Main entry point."""
    if not PKG_DIR.exists():
        logger.error(f"Package directory not found: {PKG_DIR}")
        sys.exit(1)

    fixer = ImportPathFixer()
    fixer.run()


if __name__ == "__main__":
    main()
