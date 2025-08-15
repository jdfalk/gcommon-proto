#!/usr/bin/env python3
# file: fix_import_paths.py
# version: 1.0.0
# guid: 7c6b5a4d-3e2f-1a9b-8c0d-7e6f5a4b3c2d

"""
Fix Import Paths Script

This script systematically fixes incorrect import paths in protobuf files.
Specifically, it changes imports from "web/proto/..." to "pkg/web/proto/..."
and similar patterns for other modules.
"""

import os
import re
from pathlib import Path
from typing import Dict, List


class ImportPathFixer:
    def __init__(self, base_path: Path):
        self.base_path = base_path
        self.proto_files = self._find_proto_files()
        self.fixes_applied = 0

        # Define the path corrections needed
        self.path_fixes = {
            r'"web/proto/': r'"pkg/web/proto/',
            r'"auth/proto/': r'"pkg/auth/proto/',
            r'"cache/proto/': r'"pkg/cache/proto/',
            r'"common/proto/': r'"pkg/common/proto/',
            r'"config/proto/': r'"pkg/config/proto/',
            r'"db/proto/': r'"pkg/db/proto/',
            r'"health/proto/': r'"pkg/health/proto/',
            r'"log/proto/': r'"pkg/log/proto/',
            r'"metrics/proto/': r'"pkg/metrics/proto/',
            r'"organization/proto/': r'"pkg/organization/proto/',
            r'"queue/proto/': r'"pkg/queue/proto/',
        }

    def _find_proto_files(self) -> List[Path]:
        """Find all .proto files"""
        proto_files = []
        for root, dirs, files in os.walk(self.base_path):
            for file in files:
                if file.endswith(".proto") and not file.endswith(".original"):
                    proto_files.append(Path(root) / file)
        return proto_files

    def fix_file(self, file_path: Path) -> bool:
        """Fix import paths in a single file"""
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
        except Exception as e:
            print(f"❌ Error reading {file_path}: {e}")
            return False

        original_content = content

        # Apply all path fixes
        for old_pattern, new_pattern in self.path_fixes.items():
            content = re.sub(old_pattern, new_pattern, content)

        # Check if any changes were made
        if content != original_content:
            try:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(content)

                # Count changes
                changes = sum(
                    len(re.findall(old_pattern, original_content))
                    for old_pattern in self.path_fixes.keys()
                )

                print(
                    f"✅ Fixed {changes} import paths in {file_path.relative_to(self.base_path)}"
                )
                return True
            except Exception as e:
                print(f"❌ Error writing {file_path}: {e}")
                return False

        return False

    def fix_all_files(self):
        """Fix import paths in all proto files"""
        print("🔧 FIXING IMPORT PATHS IN PROTOBUF FILES")
        print("=" * 60)

        fixed_files = 0

        for file_path in self.proto_files:
            if self.fix_file(file_path):
                fixed_files += 1

        print(f"\n📊 SUMMARY:")
        print(f"Total files checked: {len(self.proto_files)}")
        print(f"Files with fixes applied: {fixed_files}")

        if fixed_files > 0:
            print(f"\n✅ Import path fixes completed!")
            print(f"You should now run 'buf lint' to check for remaining issues.")
        else:
            print(f"\n🎉 No import path issues found!")

    def preview_changes(self):
        """Preview what changes would be made without applying them"""
        print("🔍 PREVIEW OF IMPORT PATH CHANGES")
        print("=" * 60)

        total_changes = 0

        for file_path in self.proto_files:
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
            except Exception as e:
                print(f"❌ Error reading {file_path}: {e}")
                continue

            file_changes = []

            for old_pattern, new_pattern in self.path_fixes.items():
                matches = re.findall(old_pattern + r'[^"]*"', content)
                for match in matches:
                    old_import = match
                    new_import = re.sub(old_pattern, new_pattern, match)
                    file_changes.append((old_import, new_import))

            if file_changes:
                print(f"\n📁 {file_path.relative_to(self.base_path)}:")
                for old_import, new_import in file_changes:
                    print(f"  - {old_import}")
                    print(f"  + {new_import}")
                total_changes += len(file_changes)

        print(f"\n📊 PREVIEW SUMMARY:")
        print(f"Total import changes needed: {total_changes}")


def main():
    import sys

    base_path = Path(".")
    fixer = ImportPathFixer(base_path)

    if len(sys.argv) > 1 and sys.argv[1] == "--preview":
        fixer.preview_changes()
    else:
        fixer.fix_all_files()


if __name__ == "__main__":
    main()
