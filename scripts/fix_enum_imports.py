#!/usr/bin/env python3
"""
Fix all imports of *_type.proto files from types/ directories to enums/ directories.
The migration moved enum files to enums/ but imports still reference types/.
"""

import re
from pathlib import Path


def fix_enum_imports():
    """Fix all enum import paths in proto files."""
    proto_dir = Path("proto")

    # Pattern to match imports of *_type.proto files from types directories
    import_pattern = re.compile(
        r'import\s+"proto/gcommon/v1/([^/]+)/types/([^"]*_type\.proto)";'
    )

    files_changed = 0
    total_replacements = 0

    # Find all .proto files
    for proto_file in proto_dir.rglob("*.proto"):
        try:
            with open(proto_file, "r", encoding="utf-8") as f:
                content = f.read()

            original_content = content

            # Replace imports from types/*_type.proto to enums/*_type.proto
            def replace_import(match):
                module = match.group(1)  # organization, config, etc.
                filename = match.group(2)  # hierarchy_type.proto, etc.
                return f'import "proto/gcommon/v1/{module}/enums/{filename}";'

            content = import_pattern.sub(replace_import, content)

            # Special case for common types - these should go to common/enums
            common_pattern = re.compile(
                r'import\s+"proto/gcommon/v1/common/types/([^"]*_type\.proto)";'
            )

            def replace_common_import(match):
                filename = match.group(1)
                return f'import "proto/gcommon/v1/common/enums/{filename}";'

            content = common_pattern.sub(replace_common_import, content)

            if content != original_content:
                with open(proto_file, "w", encoding="utf-8") as f:
                    f.write(content)

                # Count replacements
                replacements = len(import_pattern.findall(original_content)) + len(
                    common_pattern.findall(original_content)
                )
                total_replacements += replacements
                files_changed += 1
                print(f"Fixed {replacements} imports in {proto_file}")

        except Exception as e:
            print(f"Error processing {proto_file}: {e}")

    print("\nSummary:")
    print(f"Files changed: {files_changed}")
    print(f"Total import fixes: {total_replacements}")


if __name__ == "__main__":
    fix_enum_imports()
