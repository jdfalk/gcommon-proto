#!/usr/bin/env python3
# file: fix_all_missing_types.py
# version: 1.0.0
# guid: 5f8e9a0b-1c2d-3e4f-5a6b-7c8d9e0f1a2b

"""
Comprehensive script to fix all missing type references in protobuf files.
This handles the remaining unknown types after moving files to common package.
"""

import re
from pathlib import Path


def analyze_unknown_types():
    """Parse buf generate errors and identify missing types."""
    print("Step 1: Analyzing unknown types from buf generate output...")

    # These are the unknown types we need to fix based on the errors
    missing_types = {
        # Types that need to be found and moved/renamed
        "ErrorTypeCount": "metrics",  # Should be in metrics package
        "TimeRestriction": "organization",  # Should be in organization package
        "EmailTemplate": "organization",  # Should be in organization package
        "NotificationFrequency": "organization",  # Should be in organization package
        "ConfigRetrySettings": "common",  # Already moved, need to fix refs
        "MetricsValidationResult": "metrics",  # Should be in metrics package
        "MetricsTimeRange": "metrics",  # Should be in metrics package
        "RetentionPolicyConfig": "common",  # Already moved as MetricsRetentionPolicyConfig
        "MetricsAPIKeyConfig": "metrics",  # Should be in metrics package
        "MetricsConfigChange": "metrics",  # Should be in metrics package
        "OrganizationResourceLimits": "organization",  # Should be in organization package
        "MetricsRetentionInfo": "metrics",  # Should be in metrics package
    }

    return missing_types


def find_type_definitions():
    """Find where each type is actually defined."""
    print("Step 2: Finding type definitions...")

    proto_dir = Path("./proto/gcommon/v1")
    type_locations = {}

    for proto_file in proto_dir.rglob("*.proto"):
        try:
            with open(proto_file, "r", encoding="utf-8") as f:
                content = f.read()

            # Find message definitions
            message_matches = re.findall(r"message\s+(\w+)\s*{", content)
            for msg_name in message_matches:
                type_locations[msg_name] = proto_file

            # Find enum definitions
            enum_matches = re.findall(r"enum\s+(\w+)\s*{", content)
            for enum_name in enum_matches:
                type_locations[enum_name] = proto_file

        except Exception as e:
            print(f"Error reading {proto_file}: {e}")

    return type_locations


def fix_type_references():
    """Fix all type references in protobuf files."""
    print("Step 3: Fixing type references...")

    proto_dir = Path("./proto/gcommon/v1")
    fixes_applied = 0

    # Mapping of incorrect type references to correct ones
    type_fixes = {
        # Types that were moved to common with prefixes
        "gcommon.v1.metrics.RetentionPolicyConfig": "gcommon.v1.common.MetricsRetentionPolicyConfig",
        "gcommon.v1.metrics.MetricsConfigChange": "gcommon.v1.common.MetricsConfigChange",
        "gcommon.v1.config.ConfigRetrySettings": "gcommon.v1.common.ConfigRetrySettings",
        "RetentionPolicyConfig": "gcommon.v1.common.MetricsRetentionPolicyConfig",
        "MetricsConfigChange": "gcommon.v1.common.MetricsConfigChange",
        "ConfigRetrySettings": "gcommon.v1.common.ConfigRetrySettings",
        # Types that need to be referenced with package prefixes
        "ErrorTypeCount": "gcommon.v1.metrics.ErrorTypeCount",
        "TimeRestriction": "gcommon.v1.organization.TimeRestriction",
        "EmailTemplate": "gcommon.v1.organization.EmailTemplate",
        "NotificationFrequency": "gcommon.v1.organization.NotificationFrequency",
        "MetricsValidationResult": "gcommon.v1.metrics.MetricsValidationResult",
        "MetricsTimeRange": "gcommon.v1.metrics.MetricsTimeRange",
        "MetricsAPIKeyConfig": "gcommon.v1.metrics.MetricsAPIKeyConfig",
        "OrganizationResourceLimits": "gcommon.v1.organization.OrganizationResourceLimits",
        "MetricsRetentionInfo": "gcommon.v1.metrics.MetricsRetentionInfo",
    }

    for proto_file in proto_dir.rglob("*.proto"):
        try:
            with open(proto_file, "r", encoding="utf-8") as f:
                content = f.read()

            original_content = content

            # Apply type fixes
            for old_type, new_type in type_fixes.items():
                if old_type in content:
                    content = content.replace(old_type, new_type)

            # Write back if changed
            if content != original_content:
                with open(proto_file, "w", encoding="utf-8") as f:
                    f.write(content)
                fixes_applied += 1
                print(f"Fixed {proto_file}")

        except Exception as e:
            print(f"Error processing {proto_file}: {e}")

    print(f"Applied fixes to {fixes_applied} files")


def add_missing_imports():
    """Add missing import statements where needed."""
    print("Step 4: Adding missing imports...")

    proto_dir = Path("./proto/gcommon/v1")
    imports_added = 0

    # Files that need specific imports
    import_requirements = {
        "common/retention_policy_info.proto": [
            'import "gcommon/v1/common/metrics_retention_policy_config.proto";'
        ],
        "config/validation_settings.proto": [
            'import "gcommon/v1/common/config_retry_settings.proto";'
        ],
        "config/get_config_history_response.proto": [
            'import "gcommon/v1/common/metrics_config_change.proto";'
        ],
        "metrics/update_result.proto": [
            'import "gcommon/v1/common/metrics_config_change.proto";'
        ],
        "organization/integration_settings.proto": [
            'import "gcommon/v1/metrics/metrics_api_key_config.proto";'
        ],
        "queue/export_queue_request.proto": [
            'import "gcommon/v1/metrics/metrics_time_range.proto";'
        ],
        "queue/get_queue_stats_request.proto": [
            'import "gcommon/v1/metrics/metrics_time_range.proto";'
        ],
        "queue/get_topic_info_response.proto": [
            'import "gcommon/v1/metrics/metrics_retention_info.proto";'
        ],
        "queue/restore_options.proto": [
            'import "gcommon/v1/metrics/metrics_time_range.proto";'
        ],
        "queue/restore_queue_response.proto": [
            'import "gcommon/v1/metrics/metrics_validation_result.proto";'
        ],
        "queue/subscription_config_update.proto": [
            'import "gcommon/v1/common/config_retry_settings.proto";'
        ],
    }

    for file_path, required_imports in import_requirements.items():
        full_path = proto_dir / file_path
        if full_path.exists():
            try:
                with open(full_path, "r", encoding="utf-8") as f:
                    content = f.read()

                # Check if imports are missing and add them
                modified = False
                for import_stmt in required_imports:
                    if import_stmt not in content:
                        # Add import after other imports
                        import_section = re.search(
                            r"(import\s+[^;]+;.*?\n)", content, re.DOTALL
                        )
                        if import_section:
                            last_import_pos = import_section.end()
                            content = (
                                content[:last_import_pos]
                                + import_stmt
                                + "\n"
                                + content[last_import_pos:]
                            )
                        else:
                            # Add after syntax declaration
                            syntax_match = re.search(
                                r'syntax\s+=\s+"proto3";\s*\n', content
                            )
                            if syntax_match:
                                pos = syntax_match.end()
                                content = (
                                    content[:pos]
                                    + "\n"
                                    + import_stmt
                                    + "\n"
                                    + content[pos:]
                                )
                        modified = True

                if modified:
                    with open(full_path, "w", encoding="utf-8") as f:
                        f.write(content)
                    imports_added += 1
                    print(f"Added imports to {file_path}")

            except Exception as e:
                print(f"Error processing {full_path}: {e}")

    print(f"Added imports to {imports_added} files")


def main():
    """Main execution function."""
    print("Fixing all missing types and references...")
    print("=" * 50)

    # Step 1: Analyze what types are missing
    missing_types = analyze_unknown_types()
    print(f"Found {len(missing_types)} missing types")

    # Step 2: Find where types are actually defined
    type_locations = find_type_definitions()
    print(f"Found {len(type_locations)} type definitions")

    # Step 3: Fix type references
    fix_type_references()

    # Step 4: Add missing imports
    add_missing_imports()

    print("=" * 50)
    print("All fixes complete!")
    print("Next: Run buf generate again to check for remaining errors")


if __name__ == "__main__":
    main()
