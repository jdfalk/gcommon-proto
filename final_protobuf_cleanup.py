#!/usr/bin/env python3
# file: final_protobuf_cleanup.py
# version: 1.0.0
# guid: 7b8c9d0e-1f2a-3b4c-5d6e-7f8a9b0c1d2e

"""
Final comprehensive cleanup of all protobuf issues.
This script will fix all the duplicated prefixes and missing imports.
"""

import re
from pathlib import Path


def clean_duplicated_prefixes():
    """Remove duplicated package prefixes from type references."""
    print("Step 1: Cleaning duplicated package prefixes...")

    proto_dir = Path("./proto/gcommon/v1")
    fixes_applied = 0

    for proto_file in proto_dir.rglob("*.proto"):
        try:
            with open(proto_file, "r", encoding="utf-8") as f:
                content = f.read()

            original_content = content

            # Fix duplicated prefixes like gcommon.v1.common.gcommon.v1.common.Type
            content = re.sub(
                r"gcommon\.v1\.(\w+)\.gcommon\.v1\.\1\.(\w+)",
                r"gcommon.v1.\1.\2",
                content,
            )

            # Fix any remaining duplicates
            content = re.sub(
                r"gcommon\.v1\.(\w+)\.gcommon\.v1\.(\w+)\.(\w+)",
                r"gcommon.v1.\2.\3",
                content,
            )

            if content != original_content:
                with open(proto_file, "w", encoding="utf-8") as f:
                    f.write(content)
                fixes_applied += 1
                print(f"Fixed duplicates in {proto_file}")

        except Exception as e:
            print(f"Error processing {proto_file}: {e}")

    print(f"Fixed duplicates in {fixes_applied} files")


def fix_missing_imports():
    """Add all necessary import statements."""
    print("Step 2: Adding missing import statements...")

    proto_dir = Path("./proto/gcommon/v1")

    # Key files that need imports for types that were moved to common
    critical_imports = {
        # Files in common that need imports for types they reference
        "common/metrics_error_stats.proto": [
            'import "gcommon/v1/metrics/error_type_count.proto";'
        ],
        "common/organization_access_control.proto": [
            'import "gcommon/v1/organization/time_restriction.proto";'
        ],
        "common/organization_notification_settings.proto": [
            'import "gcommon/v1/organization/email_template.proto";',
            'import "gcommon/v1/organization/notification_frequency.proto";',
        ],
        "common/retention_policy_info.proto": [
            'import "gcommon/v1/common/metrics_retention_policy_config.proto";'
        ],
        # Files in other packages that need common types
        "config/validation_settings.proto": [
            'import "gcommon/v1/common/config_retry_settings.proto";'
        ],
        "config/get_config_history_response.proto": [
            'import "gcommon/v1/common/metrics_config_change.proto";'
        ],
        "config/config_environment.proto": [
            'import "gcommon/v1/common/organization_access_control.proto";',
            'import "gcommon/v1/common/organization_resource_limits.proto";',
            'import "gcommon/v1/common/organization_notification_settings.proto";',
        ],
        # Files in metrics that need types
        "metrics/create_provider_response.proto": [
            'import "gcommon/v1/common/metrics_validation_result.proto";'
        ],
        "metrics/get_metrics_request.proto": [
            'import "gcommon/v1/common/time_range_metrics.proto";'
        ],
        "metrics/get_metrics_response.proto": [
            'import "gcommon/v1/common/time_range_metrics.proto";'
        ],
        "metrics/get_metrics_summary_request.proto": [
            'import "gcommon/v1/common/time_range_metrics.proto";'
        ],
        "metrics/get_provider_stats_request.proto": [
            'import "gcommon/v1/common/time_range_metrics.proto";'
        ],
        "metrics/metric_query.proto": [
            'import "gcommon/v1/common/time_range_metrics.proto";'
        ],
        "metrics/record_metric_response.proto": [
            'import "gcommon/v1/common/metrics_validation_result.proto";'
        ],
        "metrics/security_config.proto": [
            'import "gcommon/v1/common/metrics_api_key_config.proto";'
        ],
        "metrics/update_provider_response.proto": [
            'import "gcommon/v1/common/metrics_validation_result.proto";'
        ],
        "metrics/update_result.proto": [
            'import "gcommon/v1/common/metrics_config_change.proto";'
        ],
        "metrics/metrics_summary.proto": [
            'import "gcommon/v1/common/metrics_error_stats.proto";',
            'import "gcommon/v1/common/metrics_retention_info.proto";',
        ],
        "metrics/provider_statistics.proto": [
            'import "gcommon/v1/common/metrics_error_stats.proto";'
        ],
        # Files in organization that need types
        "organization/compute_isolation.proto": [
            'import "gcommon/v1/common/organization_resource_limits.proto";'
        ],
        "organization/integration_settings.proto": [
            'import "gcommon/v1/common/metrics_api_key_config.proto";'
        ],
        # Files in queue that need types
        "queue/export_queue_request.proto": [
            'import "gcommon/v1/common/time_range_metrics.proto";'
        ],
        "queue/get_queue_stats_request.proto": [
            'import "gcommon/v1/common/time_range_metrics.proto";'
        ],
        "queue/get_topic_info_response.proto": [
            'import "gcommon/v1/common/metrics_retention_info.proto";'
        ],
        "queue/restore_options.proto": [
            'import "gcommon/v1/common/time_range_metrics.proto";'
        ],
        "queue/restore_queue_response.proto": [
            'import "gcommon/v1/common/metrics_validation_result.proto";'
        ],
        "queue/subscription_config_update.proto": [
            'import "gcommon/v1/common/config_retry_settings.proto";'
        ],
        "queue/get_queue_stats_response.proto": [
            'import "gcommon/v1/common/metrics_error_stats.proto";'
        ],
    }

    imports_added = 0

    for file_path, required_imports in critical_imports.items():
        full_path = proto_dir / file_path
        if full_path.exists():
            try:
                with open(full_path, "r", encoding="utf-8") as f:
                    content = f.read()

                modified = False
                for import_stmt in required_imports:
                    if import_stmt not in content:
                        # Add import after other imports or after syntax
                        lines = content.split("\n")
                        insert_pos = 0

                        # Find the best position to insert
                        for i, line in enumerate(lines):
                            if line.startswith("import "):
                                insert_pos = i + 1
                            elif line.startswith("syntax "):
                                if insert_pos == 0:
                                    insert_pos = i + 1

                        if insert_pos == 0:
                            insert_pos = 1  # After first line

                        lines.insert(insert_pos, import_stmt)
                        content = "\n".join(lines)
                        modified = True

                if modified:
                    with open(full_path, "w", encoding="utf-8") as f:
                        f.write(content)
                    imports_added += 1
                    print(f"Added imports to {file_path}")

            except Exception as e:
                print(f"Error processing {full_path}: {e}")

    print(f"Added imports to {imports_added} files")


def fix_type_references():
    """Fix remaining type references to use correct names."""
    print("Step 3: Fixing type references...")

    proto_dir = Path("./proto/gcommon/v1")
    fixes_applied = 0

    # Map of incorrect type references to correct ones
    type_corrections = {
        # Simple name references for types that were moved to common
        "ConfigRetrySettings": "gcommon.v1.common.ConfigRetrySettings",
        "MetricsConfigChange": "gcommon.v1.common.MetricsConfigChange",
        "MetricsRetentionPolicyConfig": "gcommon.v1.common.MetricsRetentionPolicyConfig",
        "MetricsValidationResult": "gcommon.v1.common.MetricsValidationResult",
        "MetricsAPIKeyConfig": "gcommon.v1.common.MetricsAPIKeyConfig",
        "MetricsRetentionInfo": "gcommon.v1.common.MetricsRetentionInfo",
        "MetricsErrorStats": "gcommon.v1.common.MetricsErrorStats",
        "OrganizationResourceLimits": "gcommon.v1.common.OrganizationResourceLimits",
        "OrganizationAccessControl": "gcommon.v1.common.OrganizationAccessControl",
        "OrganizationNotificationSettings": "gcommon.v1.common.OrganizationNotificationSettings",
        "MetricsTimeRange": "gcommon.v1.common.TimeRangeMetrics",  # This was renamed
        # Simple name references for types that stayed in their packages
        "ErrorTypeCount": "gcommon.v1.metrics.ErrorTypeCount",
        "TimeRestriction": "gcommon.v1.organization.TimeRestriction",
        "EmailTemplate": "gcommon.v1.organization.EmailTemplate",
        "NotificationFrequency": "gcommon.v1.organization.NotificationFrequency",
        # Old fully qualified names that need updating
        "gcommon.v1.metrics.RetentionPolicyConfig": "gcommon.v1.common.MetricsRetentionPolicyConfig",
    }

    for proto_file in proto_dir.rglob("*.proto"):
        try:
            with open(proto_file, "r", encoding="utf-8") as f:
                content = f.read()

            original_content = content

            # Apply type corrections
            for old_type, new_type in type_corrections.items():
                content = content.replace(old_type, new_type)

            if content != original_content:
                with open(proto_file, "w", encoding="utf-8") as f:
                    f.write(content)
                fixes_applied += 1
                print(f"Fixed types in {proto_file}")

        except Exception as e:
            print(f"Error processing {proto_file}: {e}")

    print(f"Fixed types in {fixes_applied} files")


def main():
    """Main execution function."""
    print("Final protobuf cleanup...")
    print("=" * 50)

    clean_duplicated_prefixes()
    fix_missing_imports()
    fix_type_references()

    print("=" * 50)
    print("Final cleanup complete!")
    print("Next: Run buf generate to verify all issues are resolved")


if __name__ == "__main__":
    main()
