#!/usr/bin/env python3
# file: scripts/fix-proto-imports.py
# version: 1.0.0
# guid: 2f3a4b5c-6d7e-8f9a-0b1c-2d3e4f5a6b7c

"""
Fix Protocol Buffer Import References

This script updates all import statements in .proto files to reference the correct
locations after the reorganization to the 3-category structure.
"""

import argparse
import json
import re
from pathlib import Path
from typing import Dict, List


class ProtoImportFixer:
    def __init__(self, proto_root: Path, dry_run: bool = False):
        self.proto_root = proto_root
        self.dry_run = dry_run
        self.domains = [
            "common",
            "config",
            "database",
            "media",
            "metrics",
            "organization",
            "queue",
            "web",
        ]

        # Track all moves from the reorganization report
        self.file_moves: Dict[str, str] = {}
        self.fixes_made = 0

    def load_reorganization_moves(self):
        """Load file moves from the reorganization report."""
        report_path = self.proto_root.parent / "reorganization_report.json"
        if not report_path.exists():
            print(f"Warning: No reorganization report found at {report_path}")
            return

        with open(report_path, "r") as f:
            report = json.load(f)

        # Build a mapping of old_path -> new_path for moved files
        for move in report.get("moves", []):
            source = Path(move["source"]).relative_to(self.proto_root.parent)
            target = Path(move["target"]).relative_to(self.proto_root.parent)

            # Convert to import-style paths (remove .proto extension and use forward slashes)
            source_import = str(source).replace(".proto", "").replace("\\", "/")
            target_import = str(target).replace(".proto", "").replace("\\", "/")

            self.file_moves[source_import] = target_import

        print(f"Loaded {len(self.file_moves)} file moves from reorganization report")

    def find_import_statements(self, content: str) -> List[tuple]:
        """Find all import statements in proto file content."""
        # Match both import "path" and import public "path"
        import_pattern = r'^(\s*import\s+(?:public\s+)?")(gcommon/v1/[^"]+)("\s*;.*?)$'
        matches = []

        for line_num, line in enumerate(content.split("\n"), 1):
            match = re.match(import_pattern, line)
            if match:
                prefix = match.group(1)
                import_path = match.group(2)
                suffix = match.group(3)
                matches.append((line_num, line, prefix, import_path, suffix))

        return matches

    def fix_imports_in_file(self, proto_file: Path) -> int:
        """Fix import statements in a single proto file."""
        try:
            content = proto_file.read_text(encoding="utf-8")
        except Exception as e:
            print(f"Error reading {proto_file}: {e}")
            return 0

        import_statements = self.find_import_statements(content)
        if not import_statements:
            return 0

        fixes_in_file = 0
        new_lines = content.split("\n")

        for line_num, original_line, prefix, import_path, suffix in import_statements:
            # Check if this import path needs to be updated
            if import_path in self.file_moves:
                new_import_path = self.file_moves[import_path]
                new_line = f"{prefix}{new_import_path}{suffix}"

                if not self.dry_run:
                    new_lines[line_num - 1] = new_line

                print(f"  {proto_file.relative_to(self.proto_root.parent)}:{line_num}")
                print(f"    - {import_path}")
                print(f"    + {new_import_path}")

                fixes_in_file += 1

        if fixes_in_file > 0 and not self.dry_run:
            try:
                proto_file.write_text("\n".join(new_lines), encoding="utf-8")
            except Exception as e:
                print(f"Error writing {proto_file}: {e}")
                return 0

        return fixes_in_file

    def find_all_proto_files(self) -> List[Path]:
        """Find all .proto files in the repository."""
        proto_files = []

        # Find all .proto files recursively
        for proto_file in self.proto_root.rglob("*.proto"):
            proto_files.append(proto_file)

        return sorted(proto_files)

    def run(self):
        """Run the import fixing process."""
        print("🔧 Starting Protocol Buffer Import Path Fixes")
        print(f"Proto root: {self.proto_root}")
        print(f"Dry run: {self.dry_run}")
        print()

        # Load the reorganization moves
        print("📋 Step 1: Loading reorganization moves...")
        self.load_reorganization_moves()
        print()

        if not self.file_moves:
            print("No file moves found. Nothing to fix.")
            return

        # Find all proto files
        print("🔍 Step 2: Finding all proto files...")
        proto_files = self.find_all_proto_files()
        print(f"Found {len(proto_files)} proto files")
        print()

        # Fix imports in each file
        print("🛠️  Step 3: Fixing import statements...")
        files_with_fixes = 0

        for proto_file in proto_files:
            fixes_in_file = self.fix_imports_in_file(proto_file)
            if fixes_in_file > 0:
                files_with_fixes += 1
                self.fixes_made += fixes_in_file

        print()
        print(f"{'✅ Simulation' if self.dry_run else '✅'} Import fixing complete!")
        print("📊 Summary:")
        print(f"  - Files with fixes: {files_with_fixes}")
        print(f"  - Total import statements fixed: {self.fixes_made}")

        if self.dry_run:
            print("  - Run without --dry-run to apply changes")


def main():
    parser = argparse.ArgumentParser(description="Fix Protocol Buffer import paths")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be changed without making changes",
    )
    parser.add_argument(
        "--proto-root",
        type=Path,
        default=Path(__file__).parent.parent / "proto" / "gcommon" / "v1",
        help="Root directory of proto files",
    )

    args = parser.parse_args()

    if not args.proto_root.exists():
        print(f"Error: Proto root directory does not exist: {args.proto_root}")
        return 1

    fixer = ProtoImportFixer(args.proto_root, args.dry_run)
    fixer.run()

    return 0


if __name__ == "__main__":
    exit(main())
