#!/usr/bin/env python3
# file: fix_remaining_references.py
# version: 1.0.0
# guid: fed12345-6789-cba0-1234-567890abcdef

"""
Fix remaining type references after moving files to common package.
This script will update type names to match the new locations.
"""

import os

# Mapping of old type names to new ones based on the moved files
TYPE_MAPPINGS = {
    # Types that moved from metrics to common with metrics_ prefix
    "MetricsValidationResult": "MetricsValidationResult",
    "MetricsConfigChange": "MetricsConfigChange",
    "RetentionPolicyConfig": "MetricsRetentionPolicyConfig",
    "MetricsTimeRange": "MetricsTimeRange",
    "ErrorTypeCount": "MetricsErrorTypeCount",  # This type is likely in error_stats
    "MetricsAPIKeyConfig": "MetricsAPIKeyConfig",
    "MetricsRetentionInfo": "MetricsRetentionInfo",
    # Types that moved from organization to common with organization_ prefix
    "OrganizationAccessControl": "OrganizationAccessControl",
    "TimeRestriction": "OrganizationTimeRestriction",  # Likely in access_control
    "OrganizationNotificationSettings": "OrganizationNotificationSettings",
    "EmailTemplate": "OrganizationEmailTemplate",  # Likely in notification_settings
    "NotificationFrequency": "OrganizationNotificationFrequency",  # Likely in notification_settings
    "OrganizationResourceLimits": "OrganizationResourceLimits",
    # Types that moved from config to common with config_ prefix
    "ConfigRetrySettings": "ConfigRetrySettings",
}

# Import path updates
IMPORT_UPDATES = {
    "gcommon.v1.metrics.RetentionPolicyConfig": "gcommon.v1.common.MetricsRetentionPolicyConfig",
    "gcommon.v1.metrics.MetricsConfigChange": "gcommon.v1.common.MetricsConfigChange",
    "gcommon.v1.metrics.MetricsAPIKeyConfig": "gcommon.v1.common.MetricsAPIKeyConfig",
    "gcommon.v1.metrics.MetricsTimeRange": "gcommon.v1.common.MetricsTimeRange",
    "gcommon.v1.metrics.MetricsRetentionInfo": "gcommon.v1.common.MetricsRetentionInfo",
    "gcommon.v1.metrics.MetricsValidationResult": "gcommon.v1.common.MetricsValidationResult",
    "gcommon.v1.config.ConfigRetrySettings": "gcommon.v1.common.ConfigRetrySettings",
}


def find_and_update_missing_types():
    """Find files that reference types that may need to be defined or imported."""

    # Types that need to be defined somewhere
    missing_types = {
        "ErrorTypeCount": "metrics_error_stats.proto",
        "TimeRestriction": "organization_access_control.proto",
        "EmailTemplate": "organization_notification_settings.proto",
        "NotificationFrequency": "organization_notification_settings.proto",
    }

    # Check if these types exist in their expected files
    for type_name, expected_file in missing_types.items():
        file_path = f"./proto/gcommon/v1/common/{expected_file}"
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            # Check if the type is defined
            if (
                f"message {type_name}" not in content
                and f"enum {type_name}" not in content
            ):
                print(f"WARNING: Type {type_name} not found in {expected_file}")
                print(
                    "  You may need to manually define this type or check if it was renamed"
                )


def update_fully_qualified_references():
    """Update fully qualified type references throughout the codebase."""
    updated_files = []

    # Find all proto files
    for root, dirs, files in os.walk("./proto"):
        for file in files:
            if file.endswith(".proto"):
                file_path = os.path.join(root, file)
                updated = False

                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()

                    # Update fully qualified type references
                    for old_ref, new_ref in IMPORT_UPDATES.items():
                        if old_ref in content:
                            content = content.replace(old_ref, new_ref)
                            updated = True

                    # Save if updated
                    if updated:
                        with open(file_path, "w", encoding="utf-8") as f:
                            f.write(content)
                        updated_files.append(file_path)

                except Exception as e:
                    print(f"Error updating {file_path}: {e}")

    return updated_files


def fix_specific_issues():
    """Fix specific issues found in the buf generate errors."""

    fixes = [
        # Fix retention_policy_info.proto
        {
            "file": "./proto/gcommon/v1/common/retention_policy_info.proto",
            "old": "gcommon.v1.metrics.RetentionPolicyConfig",
            "new": "MetricsRetentionPolicyConfig",
        },
        # Fix config files
        {
            "file": "./proto/gcommon/v1/config/get_config_history_response.proto",
            "old": "gcommon.v1.metrics.MetricsConfigChange",
            "new": "gcommon.v1.common.MetricsConfigChange",
        },
        # Fix validation_settings.proto
        {
            "file": "./proto/gcommon/v1/config/validation_settings.proto",
            "old": "ConfigRetrySettings",
            "new": "gcommon.v1.common.ConfigRetrySettings",
        },
        # Fix organization integration_settings
        {
            "file": "./proto/gcommon/v1/organization/integration_settings.proto",
            "old": "gcommon.v1.metrics.MetricsAPIKeyConfig",
            "new": "gcommon.v1.common.MetricsAPIKeyConfig",
        },
    ]

    fixed_files = []

    for fix in fixes:
        file_path = fix["file"]
        if os.path.exists(file_path):
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()

                if fix["old"] in content:
                    content = content.replace(fix["old"], fix["new"])

                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(content)

                    fixed_files.append(file_path)
                    print(f"Fixed {file_path}: {fix['old']} -> {fix['new']}")

            except Exception as e:
                print(f"Error fixing {file_path}: {e}")

    return fixed_files


def add_missing_imports():
    """Add missing import statements where needed."""

    import_fixes = [
        {
            "file": "./proto/gcommon/v1/config/get_config_history_response.proto",
            "import": 'import "gcommon/v1/common/metrics_config_change.proto";',
        },
        {
            "file": "./proto/gcommon/v1/config/validation_settings.proto",
            "import": 'import "gcommon/v1/common/config_retry_settings.proto";',
        },
        {
            "file": "./proto/gcommon/v1/organization/integration_settings.proto",
            "import": 'import "gcommon/v1/common/metrics_api_key_config.proto";',
        },
        {
            "file": "./proto/gcommon/v1/common/retention_policy_info.proto",
            "import": 'import "gcommon/v1/common/metrics_retention_policy_config.proto";',
        },
    ]

    for fix in import_fixes:
        file_path = fix["file"]
        import_line = fix["import"]

        if os.path.exists(file_path):
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()

                # Check if import already exists
                if import_line not in content:
                    # Find a good place to add the import (after existing imports)
                    lines = content.split("\n")
                    insert_idx = 0

                    # Find last import line
                    for i, line in enumerate(lines):
                        if line.strip().startswith("import "):
                            insert_idx = i + 1

                    # Insert the new import
                    lines.insert(insert_idx, import_line)

                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write("\n".join(lines))

                    print(f"Added import to {file_path}: {import_line}")

            except Exception as e:
                print(f"Error adding import to {file_path}: {e}")


def main():
    """Main function to fix remaining references."""
    print("Fixing remaining type references...")
    print("=" * 50)

    # Step 1: Update fully qualified references
    print("\nStep 1: Updating fully qualified type references...")
    updated_files = update_fully_qualified_references()
    print(f"Updated {len(updated_files)} files")

    # Step 2: Fix specific issues
    print("\nStep 2: Fixing specific reference issues...")
    fixed_files = fix_specific_issues()
    print(f"Fixed {len(fixed_files)} files")

    # Step 3: Add missing imports
    print("\nStep 3: Adding missing import statements...")
    add_missing_imports()

    # Step 4: Check for missing types
    print("\nStep 4: Checking for missing type definitions...")
    find_and_update_missing_types()

    print("\n" + "=" * 50)
    print("Reference fixes complete!")
    print("Next: Run buf generate again to check for remaining errors")


if __name__ == "__main__":
    main()
