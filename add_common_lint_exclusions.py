#!/usr/bin/env python3
# file: add_common_lint_exclusions.py
# version: 1.0.0
# guid: 12345678-9abc-def0-1234-56789abcdef0

"""
Add lint exclusions to common enum files that are meant to be reusable.
"""

import os
import re


def add_lint_exclusion(file_path):
    """Add ENUM_VALUE_PREFIX exclusion to a proto file."""
    with open(file_path, "r") as f:
        content = f.read()

    # Check if exclusion already exists
    if "buf:lint:ignore ENUM_VALUE_PREFIX" in content:
        print(f"✅ {file_path} already has lint exclusion")
        return False

    # Find the enum declaration line
    enum_pattern = r"^(enum \w+\s*\{)$"
    lines = content.split("\n")

    for i, line in enumerate(lines):
        if re.match(enum_pattern, line.strip()):
            # Insert the exclusion comment before the enum
            lines.insert(i, "// buf:lint:ignore ENUM_VALUE_PREFIX")

            new_content = "\n".join(lines)
            with open(file_path, "w") as f:
                f.write(new_content)
            print(f"✅ Added lint exclusion to {file_path}")
            return True

    print(f"⚠️  Could not find enum declaration in {file_path}")
    return False


def main():
    # Common enum files that should be reusable - expanded list
    common_enum_files = [
        "proto/gcommon/v1/common/enums/permission_level.proto",
        "proto/gcommon/v1/common/enums/provider_type.proto", 
        "proto/gcommon/v1/common/enums/session_state.proto",
        "proto/gcommon/v1/common/enums/subject_type.proto",
        "proto/gcommon/v1/common/enums/two_fa_type.proto",
        "proto/gcommon/v1/common/enums/verification_type.proto",
        "proto/gcommon/v1/common/enums/oauth2_flow_type.proto",
        # Additional common enums that need exclusions
        "proto/gcommon/v1/common/enums/alert_severity.proto",
        "proto/gcommon/v1/common/enums/auth_method.proto", 
        "proto/gcommon/v1/common/enums/compression_type.proto",
        "proto/gcommon/v1/common/enums/export_format.proto",
        "proto/gcommon/v1/common/enums/filter_type.proto",
        "proto/gcommon/v1/common/enums/health_status.proto",
    ]

    for file_path in common_enum_files:
        if os.path.exists(file_path):
            add_lint_exclusion(file_path)
        else:
            print(f"❌ File not found: {file_path}")


if __name__ == "__main__":
    main()
