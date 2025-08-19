#!/usr/bin/env python3
# file: fix_inline_enums.py
# version: 1.0.0
# guid: abcd1234-5678-90ef-abcd-1234567890ef

"""
Fix inline enum definitions by removing them and using the proper common enum imports.
"""

import os
import re


def fix_inline_enums():
    """Fix files with inline enum definitions that should use common enums."""

    # Files with inline enums that need fixing
    inline_enum_fixes = [
        {
            "file": "proto/gcommon/v1/common/messages/list_permissions_request.proto",
            "remove_enum": r"enum AuthSubjectType \{[^}]+\}",
            "ensure_import": "gcommon/v1/common/enums/subject_type.proto",
        },
        {
            "file": "proto/gcommon/v1/common/messages/revoke_permission_request.proto",
            "remove_enum": r"enum AuthSubjectType \{[^}]+\}",
            "ensure_import": "gcommon/v1/common/enums/subject_type.proto",
        },
        {
            "file": "proto/gcommon/v1/common/messages/permission_metadata.proto",
            "remove_enum": r"enum AuthPermissionLevel \{[^}]+\}",
            "ensure_import": "gcommon/v1/common/enums/permission_level.proto",
        },
        {
            "file": "proto/gcommon/v1/common/messages/resend_verification_request.proto",
            "remove_enum": r"enum AuthVerificationType \{[^}]+\}",
            "ensure_import": "gcommon/v1/common/enums/verification_type.proto",
        },
        {
            "file": "proto/gcommon/v1/common/messages/session_metadata.proto",
            "remove_enum": r"enum AuthSessionState \{[^}]+\}",
            "ensure_import": "gcommon/v1/common/enums/session_state.proto",
        },
        {
            "file": "proto/gcommon/v1/common/messages/verify2_fa_request.proto",
            "remove_enum": r"enum AuthTwoFaType \{[^}]+\}",
            "ensure_import": "gcommon/v1/common/enums/two_fa_type.proto",
        },
    ]

    for fix in inline_enum_fixes:
        file_path = fix["file"]
        if not os.path.exists(file_path):
            print(f"❌ File not found: {file_path}")
            continue

        with open(file_path, "r") as f:
            content = f.read()

        # Remove inline enum definition
        original_content = content
        content = re.sub(
            fix["remove_enum"], "", content, flags=re.MULTILINE | re.DOTALL
        )

        # Clean up extra whitespace
        content = re.sub(r"\n\s*\n\s*\n", "\n\n", content)

        # Ensure import exists
        import_line = f'import "{fix["ensure_import"]}";'
        if import_line not in content:
            # Find the import section and add the import
            import_pattern = r'(import "[^"]+";)'
            match = re.search(import_pattern, content)
            if match:
                # Add after the last import
                imports = re.findall(import_pattern, content)
                last_import = imports[-1]
                content = content.replace(last_import, f"{last_import}\n{import_line}")
            else:
                # Add after package declaration
                content = re.sub(r"(package [^;]+;)", f"\\1\n\n{import_line}", content)

        if content != original_content:
            with open(file_path, "w") as f:
                f.write(content)
            print(f"✅ Fixed inline enums in {file_path}")
        else:
            print(f"ℹ️  No changes needed in {file_path}")


if __name__ == "__main__":
    fix_inline_enums()
