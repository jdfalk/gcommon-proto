#!/usr/bin/env python3
# file: fix_all_imports.py
# version: 1.0.0
# guid: b2c3d4e5-f6a7-8901-bcde-f23456789012

import re
import glob

def fix_all_imports():
    """Fix all problematic imports systematically"""
    
    # Define import mappings - old import -> new import
    import_fixes = {
        # Files that should be in common
        'gcommon/v1/metrics/metrics_time_range.proto': 'gcommon/v1/common/time_range_metrics.proto',
        'gcommon/v1/metrics/metrics_api_key_config.proto': 'gcommon/v1/common/metrics_api_key_config.proto',
        'gcommon/v1/metrics/metrics_validation_result.proto': 'gcommon/v1/common/metrics_validation_result.proto',
        'gcommon/v1/metrics/metrics_config_change.proto': 'gcommon/v1/common/metrics_config_change.proto',
        'gcommon/v1/metrics/metrics_error_stats.proto': 'gcommon/v1/common/metrics_error_stats.proto',
        'gcommon/v1/metrics/metrics_retention_info.proto': 'gcommon/v1/common/metrics_retention_info.proto',
        'gcommon/v1/metrics/metrics_retention_policy_config.proto': 'gcommon/v1/common/metrics_retention_policy_config.proto',
        'gcommon/v1/organization/organization_compliance_settings.proto': 'gcommon/v1/common/organization_compliance_settings.proto',
        'gcommon/v1/organization/organization_access_control.proto': 'gcommon/v1/common/organization_access_control.proto',
        'gcommon/v1/organization/organization_notification_settings.proto': 'gcommon/v1/common/organization_notification_settings.proto',
        'gcommon/v1/organization/organization_resource_limits.proto': 'gcommon/v1/common/organization_resource_limits.proto',
        'gcommon/v1/config/config_retry_settings.proto': 'gcommon/v1/common/config_retry_settings.proto',
    }
    
    # Define type reference fixes - old type -> new type
    type_fixes = {
        # Fix type references to match the new imports
        'gcommon.v1.metrics.MetricsTimeRange': 'gcommon.v1.common.TimeRangeMetrics',
        'gcommon.v1.metrics.MetricsAPIKeyConfig': 'gcommon.v1.common.MetricsAPIKeyConfig',
        'gcommon.v1.metrics.MetricsValidationResult': 'gcommon.v1.common.MetricsValidationResult',
        'gcommon.v1.metrics.MetricsConfigChange': 'gcommon.v1.common.MetricsConfigChange',
        'gcommon.v1.metrics.MetricsErrorStats': 'gcommon.v1.common.MetricsErrorStats',
        'gcommon.v1.metrics.MetricsRetentionInfo': 'gcommon.v1.common.MetricsRetentionInfo',
        'gcommon.v1.metrics.MetricsRetentionPolicyConfig': 'gcommon.v1.common.MetricsRetentionPolicyConfig',
        'gcommon.v1.organization.OrganizationComplianceSettings': 'gcommon.v1.common.OrganizationComplianceSettings',
        'gcommon.v1.organization.OrganizationAccessControl': 'gcommon.v1.common.OrganizationAccessControl',
        'gcommon.v1.organization.OrganizationNotificationSettings': 'gcommon.v1.common.OrganizationNotificationSettings',
        'gcommon.v1.organization.OrganizationResourceLimits': 'gcommon.v1.common.OrganizationResourceLimits',
        'gcommon.v1.config.ConfigRetrySettings': 'gcommon.v1.common.ConfigRetrySettings',
        
        # Also fix unqualified types where they should be fully qualified
        'MetricsTimeRange': 'gcommon.v1.common.TimeRangeMetrics',
        'MetricsAPIKeyConfig': 'gcommon.v1.common.MetricsAPIKeyConfig',
        'MetricsValidationResult': 'gcommon.v1.common.MetricsValidationResult',
        'MetricsConfigChange': 'gcommon.v1.common.MetricsConfigChange',
        'MetricsErrorStats': 'gcommon.v1.common.MetricsErrorStats',
        'MetricsRetentionInfo': 'gcommon.v1.common.MetricsRetentionInfo',
        'MetricsRetentionPolicyConfig': 'gcommon.v1.common.MetricsRetentionPolicyConfig',
        'OrganizationComplianceSettings': 'gcommon.v1.common.OrganizationComplianceSettings',
        'OrganizationAccessControl': 'gcommon.v1.common.OrganizationAccessControl',
        'OrganizationNotificationSettings': 'gcommon.v1.common.OrganizationNotificationSettings',
        'OrganizationResourceLimits': 'gcommon.v1.common.OrganizationResourceLimits',
        'ConfigRetrySettings': 'gcommon.v1.common.ConfigRetrySettings',
    }
    
    fixed_files = []
    
    # Process all proto files
    for proto_file in glob.glob("proto/gcommon/v1/**/*.proto", recursive=True):
        try:
            with open(proto_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Fix imports
            for old_import, new_import in import_fixes.items():
                old_pattern = f'import "{old_import}";'
                new_pattern = f'import "{new_import}";'
                content = content.replace(old_pattern, new_pattern)
            
            # Remove duplicate imports by processing line by line
            lines = content.split('\n')
            seen_imports = set()
            filtered_lines = []
            
            for line in lines:
                if line.strip().startswith('import "'):
                    if line not in seen_imports:
                        seen_imports.add(line)
                        filtered_lines.append(line)
                    # Skip duplicate imports
                else:
                    filtered_lines.append(line)
            
            content = '\n'.join(filtered_lines)
            
            # Fix type references
            for old_type, new_type in type_fixes.items():
                # Use word boundaries to avoid partial matches
                pattern = r'\b' + re.escape(old_type) + r'\b'
                content = re.sub(pattern, new_type, content)
            
            # Fix duplicated package references like "gcommon.v1.common.gcommon.v1.common."
            content = re.sub(r'gcommon\.v1\.common\.gcommon\.v1\.common\.', 'gcommon.v1.common.', content)
            content = re.sub(r'gcommon\.v1\.metrics\.gcommon\.v1\.metrics\.', 'gcommon.v1.metrics.', content)
            content = re.sub(r'gcommon\.v1\.organization\.gcommon\.v1\.organization\.', 'gcommon.v1.organization.', content)
            content = re.sub(r'gcommon\.v1\.config\.gcommon\.v1\.config\.', 'gcommon.v1.config.', content)
            
            # Only write if content changed
            if content != original_content:
                with open(proto_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                fixed_files.append(proto_file)
                print(f"Fixed imports/types in: {proto_file}")
        
        except Exception as e:
            print(f"Error processing {proto_file}: {e}")
    
    return fixed_files

if __name__ == "__main__":
    print("=== Fixing All Import and Type Reference Issues ===")
    fixed = fix_all_imports()
    print(f"\nFixed {len(fixed)} files")
    for f in fixed:
        print(f"  - {f}")
