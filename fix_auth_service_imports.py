#!/usr/bin/env python3
# file: fix_auth_service_imports.py
# version: 1.0.0
# guid: 9a0b1c2d-3e4f-5a6b-7c8d-9e0f1a2b3c4d

"""
Script to fix missing imports in auth service files.
"""

import os
import re
import subprocess

# Map service method types to their expected proto files
auth_admin_service_types = {
    "CreateUserRequest": "pkg/auth/proto/create_user_request.proto",
    "UpdateUserRequest": "pkg/auth/proto/update_user_request.proto",
    "UpdateUserResponse": "pkg/auth/proto/update_user_response.proto",
    "ListUsersRequest": "pkg/auth/proto/list_users_request.proto",
    "GetUserResponse": "pkg/auth/proto/get_user_response.proto",
    "AssignRoleRequest": "pkg/auth/proto/assign_role_request.proto",
    "CreateRoleRequest": "pkg/auth/proto/create_role_request.proto",
    "UpdateRoleResponse": "pkg/auth/proto/update_role_response.proto",
    "DeleteRoleRequest": "pkg/auth/proto/delete_role_request.proto",
    "InvalidateUserSessionsRequest": "pkg/auth/proto/invalidate_user_sessions_request.proto",
    "GetSystemStatsResponse": "pkg/auth/proto/get_system_stats_response.proto",
}

auth_service_types = {
    "AuthenticateRequest": "pkg/auth/proto/authenticate_request.proto",
    "ValidateTokenRequest": "pkg/auth/proto/validate_token_request.proto",
    "VerifyCredentialsRequest": "pkg/auth/proto/verify_credentials_request.proto",
    "RefreshTokenRequest": "pkg/auth/proto/refresh_token_request.proto",
    "RevokeTokenRequest": "pkg/auth/proto/revoke_token_request.proto",
    "GetUserInfoRequest": "pkg/auth/proto/get_user_info_request.proto",
    "InitiatePasswordResetRequest": "pkg/auth/proto/initiate_password_reset_request.proto",
    "CompletePasswordResetRequest": "pkg/auth/proto/complete_password_reset_request.proto",
    "ChangePasswordRequest": "pkg/auth/proto/change_password_request.proto",
}


def check_file_exists(file_path):
    """Check if a file exists"""
    full_path = f"/Users/jdfalk/repos/github.com/jdfalk/gcommon/{file_path}"
    return os.path.exists(full_path)


def add_missing_imports(service_file, type_mapping):
    """Add missing imports to a service file"""
    full_path = f"/Users/jdfalk/repos/github.com/jdfalk/gcommon/{service_file}"

    with open(full_path, "r") as f:
        content = f.read()

    # Find existing imports
    existing_imports = re.findall(r'import\s+"([^"]+)";', content)

    # Find what types are needed
    needed_imports = []
    for type_name, import_path in type_mapping.items():
        if type_name in content and import_path not in existing_imports:
            if check_file_exists(import_path):
                needed_imports.append(import_path)
                print(f"  Need to add: {import_path}")
            else:
                print(f"  Missing file: {import_path}")

    if needed_imports:
        # Find the last import line
        import_lines = re.findall(r'^import\s+"[^"]+";$', content, re.MULTILINE)
        if import_lines:
            last_import = import_lines[-1]
            # Add new imports after the last existing import
            new_imports = "\n".join(
                f'import "{imp}";' for imp in sorted(needed_imports)
            )
            content = content.replace(last_import, f"{last_import}\n{new_imports}")

            with open(full_path, "w") as f:
                f.write(content)
            print(f"  Added {len(needed_imports)} imports")
            return True

    return False


def main():
    print("Fixing auth service imports...")

    print("\nChecking auth_admin_service.proto...")
    add_missing_imports(
        "pkg/auth/proto/auth_admin_service.proto", auth_admin_service_types
    )

    print("\nChecking auth_service.proto...")
    add_missing_imports("pkg/auth/proto/auth_service.proto", auth_service_types)


if __name__ == "__main__":
    main()
