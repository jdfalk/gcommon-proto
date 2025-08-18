#!/usr/bin/env python3
# file: fix_duplicate_imports.py
# version: 1.0.0
# guid: 6c5b4a3d-2e1f-9a8b-7c0d-6e5f4a3b2c1d

"""
Fix Duplicate Imports Script

This script removes duplicate import statements from protobuf files.
After fixing import paths, some files may have both the old and new import statements.
"""

import os
import re
from pathlib import Path
from typing import List, Set


class DuplicateImportFixer:
    def __init__(self, base_path: Path):
        self.base_path = base_path
        self.proto_files = self._find_proto_files()
        self.fixes_applied = 0

    def _find_proto_files(self) -> List[Path]:
        """Find all .proto files"""
        proto_files = []
        for root, dirs, files in os.walk(self.base_path):
            for file in files:
                if file.endswith(".proto") and not file.endswith(".original"):
                    proto_files.append(Path(root) / file)
        return proto_files

    def fix_file(self, file_path: Path) -> bool:
        """Fix duplicate imports in a single file"""
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
        except Exception as e:
            print(f"❌ Error reading {file_path}: {e}")
            return False

        original_content = content
        lines = content.split("\n")

        # Track imports we've seen
        seen_imports: Set[str] = set()
        new_lines = []
        removed_duplicates = 0

        for line in lines:
            # Check if this is an import line
            import_match = re.match(r'\s*import\s+"([^"]+)";', line)

            if import_match:
                import_path = import_match.group(1)
                if import_path in seen_imports:
                    # This is a duplicate, skip it
                    removed_duplicates += 1
                    continue
                else:
                    # First time seeing this import
                    seen_imports.add(import_path)
                    new_lines.append(line)
            else:
                # Not an import line, keep it
                new_lines.append(line)

        if removed_duplicates > 0:
            new_content = "\n".join(new_lines)
            try:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(new_content)
                print(
                    f"✅ Removed {removed_duplicates} duplicate imports from {file_path.relative_to(self.base_path)}"
                )
                return True
            except Exception as e:
                print(f"❌ Error writing {file_path}: {e}")
                return False

        return False

    def fix_all_files(self):
        """Fix duplicate imports in all proto files"""
        print("🔧 REMOVING DUPLICATE IMPORTS FROM PROTOBUF FILES")
        print("=" * 60)

        fixed_files = 0

        for file_path in self.proto_files:
            if self.fix_file(file_path):
                fixed_files += 1

        print(f"\n📊 SUMMARY:")
        print(f"Total files checked: {len(self.proto_files)}")
        print(f"Files with duplicate imports fixed: {fixed_files}")

        if fixed_files > 0:
            print(f"\n✅ Duplicate import fixes completed!")
            print(f"You should now run 'buf lint' to check for remaining issues.")
        else:
            print(f"\n🎉 No duplicate imports found!")


def main():
    base_path = Path(".")
    fixer = DuplicateImportFixer(base_path)
    fixer.fix_all_files()


if __name__ == "__main__":
    main()
