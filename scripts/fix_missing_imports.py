#!/usr/bin/env python3
# file: fix_missing_imports.py
# version: 1.0.0
# guid: 8a9b7c6d-5e4f-3a2b-1c0d-8e7f6a5b4c3d

"""
Proto Missing Imports Fixer

This script automatically fixes missing imports in proto files by:
1. Reading the missing imports analysis output
2. Adding import statements for types that exist
3. Processing files in batches for efficiency
"""

import re
from pathlib import Path
from typing import Dict, List


class ProtoImportFixer:
    def __init__(self, base_path: Path, analysis_file: Path):
        self.base_path = base_path
        self.analysis_file = analysis_file
        self.fixes_applied = 0
        self.files_modified = 0

    def _parse_analysis_file(self) -> Dict[str, List[str]]:
        """Parse the missing imports analysis to get file -> [imports] mapping"""
        file_imports = {}

        with open(self.analysis_file, "r") as f:
            content = f.read()

        # Extract import sections
        import_sections = re.findall(
            r"📦 IMPORT: ([^\n]+)\n.*?Needed by \d+ files:\n(.*?)(?=📦 IMPORT:|$)",
            content,
            re.DOTALL,
        )

        for import_proto, files_section in import_sections:
            import_proto = import_proto.strip()

            # Extract file mappings from the section
            file_mappings = re.findall(r"• ([^→]+) → (\w+)", files_section)

            for file_path, type_name in file_mappings:
                file_path = file_path.strip()
                full_file_path = self.base_path / file_path

                if full_file_path not in file_imports:
                    file_imports[full_file_path] = []

                file_imports[full_file_path].append(import_proto)

        return file_imports

    def _add_import_to_file(self, file_path: Path, import_path: str) -> bool:
        """Add an import to a proto file if it doesn't already exist"""
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
        except Exception as e:
            print(f"❌ Error reading {file_path}: {e}")
            return False

        # Check if import already exists
        import_pattern = f'import "{import_path}";'
        if import_pattern in content:
            return False  # Already imported

        # Find where to insert the import (after other imports or after syntax/package)
        lines = content.split("\n")
        insert_index = 0

        # Find the best place to insert
        for i, line in enumerate(lines):
            stripped = line.strip()
            if stripped.startswith("import "):
                insert_index = i + 1
            elif (
                stripped.startswith("syntax ")
                or stripped.startswith("package ")
                or stripped.startswith("edition ")
            ):
                if insert_index == 0:  # No imports found yet
                    insert_index = i + 1
            elif stripped and not stripped.startswith("//"):
                # Found first non-comment, non-metadata line
                break

        # Insert the import
        lines.insert(insert_index, f'import "{import_path}";')

        # Add blank line after imports if not present
        if insert_index < len(lines) - 1 and lines[insert_index + 1].strip() != "":
            lines.insert(insert_index + 1, "")

        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write("\n".join(lines))
            return True
        except Exception as e:
            print(f"❌ Error writing {file_path}: {e}")
            return False

    def _verify_import_exists(self, import_path: str) -> bool:
        """Verify that the import path actually exists"""
        full_path = self.base_path / import_path
        return full_path.exists()

    def fix_imports(self, max_files: int = 50) -> None:
        """Fix missing imports for up to max_files"""
        print("🔧 PROTO IMPORT FIXER")
        print("=" * 60)

        file_imports = self._parse_analysis_file()
        print(f"📊 Found {len(file_imports)} files needing imports")

        files_processed = 0
        for file_path, imports in file_imports.items():
            if files_processed >= max_files:
                print(f"\n⏱️  Reached maximum files limit ({max_files})")
                break

            if not file_path.exists():
                print(f"⚠️  File not found: {file_path}")
                continue

            print(f"\n📁 Processing: {file_path.relative_to(self.base_path)}")

            file_modified = False
            for import_path in set(imports):  # Remove duplicates
                if not self._verify_import_exists(import_path):
                    print(f"   ⚠️  Import not found: {import_path}")
                    continue

                if self._add_import_to_file(file_path, import_path):
                    print(f'   ✅ Added: import "{import_path}";')
                    self.fixes_applied += 1
                    file_modified = True
                else:
                    print(f"   ⏭️  Skipped: {import_path} (already exists)")

            if file_modified:
                self.files_modified += 1

            files_processed += 1

        print("\n📊 SUMMARY")
        print("-" * 30)
        print(f"Files processed: {files_processed}")
        print(f"Files modified: {self.files_modified}")
        print(f"Imports added: {self.fixes_applied}")


def main():
    base_path = Path("pkg")
    analysis_file = Path("missing-protos-clean")

    if not analysis_file.exists():
        print(f"❌ Analysis file not found: {analysis_file}")
        print("Run analyze_missing_imports.py first")
        return

    fixer = ProtoImportFixer(base_path, analysis_file)
    fixer.fix_imports(max_files=5000)  # Process remaining files


if __name__ == "__main__":
    main()
