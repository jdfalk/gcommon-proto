#!/usr/bin/env python3
# file: fix_syntax_errors.py
# version: 1.0.0
# guid: 6a9b8c7d-2e3f-4a5b-6c7d-8e9f0a1b2c3d

"""
Fix syntax errors introduced by the previous script.
Message names should not have package prefixes.
"""

import re
from pathlib import Path


def fix_message_names():
    """Fix message names that have incorrect package prefixes."""
    print("Fixing message names with package prefixes...")

    proto_dir = Path("./proto/gcommon/v1")
    fixes_applied = 0

    for proto_file in proto_dir.rglob("*.proto"):
        try:
            with open(proto_file, "r", encoding="utf-8") as f:
                content = f.read()

            original_content = content

            # Fix message declarations that have package prefixes
            # Pattern: message gcommon.v1.package.MessageName { -> message MessageName {
            content = re.sub(
                r"message\s+gcommon\.v1\.\w+\.(\w+)\s*{", r"message \1 {", content
            )

            # Fix enum declarations that have package prefixes
            content = re.sub(
                r"enum\s+gcommon\.v1\.\w+\.(\w+)\s*{", r"enum \1 {", content
            )

            # Fix service declarations that have package prefixes
            content = re.sub(
                r"service\s+gcommon\.v1\.\w+\.(\w+)\s*{", r"service \1 {", content
            )

            if content != original_content:
                with open(proto_file, "w", encoding="utf-8") as f:
                    f.write(content)
                fixes_applied += 1
                print(f"Fixed {proto_file}")

        except Exception as e:
            print(f"Error processing {proto_file}: {e}")

    print(f"Fixed {fixes_applied} files")


def main():
    """Main execution function."""
    print("Fixing syntax errors in protobuf files...")
    print("=" * 50)

    fix_message_names()

    print("=" * 50)
    print("Syntax fixes complete!")
    print("Next: Run buf generate again to check for remaining errors")


if __name__ == "__main__":
    main()
