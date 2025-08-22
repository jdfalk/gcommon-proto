#!/usr/bin/env python3
# file: fix_type_references_aggressive.py
# version: 1.0.0
# guid: 9d0e1f2a-3b4c-5d6e-7f8a-9b0c1d2e3f4a

"""
Aggressive fix for all malformed type references in protobuf files.
This will handle all the complex concatenated prefixes we're seeing.
"""

import re
from pathlib import Path

def aggressive_type_cleanup():
    """Aggressively clean up all malformed type references."""
    print("Starting aggressive type reference cleanup...")
    
    proto_dir = Path('./proto/gcommon/v1')
    fixes_applied = 0
    
    # Define all the types that should be in common with correct paths
    common_types_mapping = {
        'MetricsRetentionPolicyConfig': 'gcommon.v1.common.MetricsRetentionPolicyConfig',
        'MetricsConfigChange': 'gcommon.v1.common.MetricsConfigChange',
        'ConfigRetrySettings': 'gcommon.v1.common.ConfigRetrySettings',
        'MetricsValidationResult': 'gcommon.v1.common.MetricsValidationResult',
        'TimeRangeMetrics': 'gcommon.v1.common.TimeRangeMetrics',
        'MetricsAPIKeyConfig': 'gcommon.v1.common.MetricsAPIKeyConfig',
        'MetricsRetentionInfo': 'gcommon.v1.common.MetricsRetentionInfo',
        'MetricsErrorStats': 'gcommon.v1.common.MetricsErrorStats',
        'OrganizationResourceLimits': 'gcommon.v1.common.OrganizationResourceLimits',
        'MetricsTimeRange': 'gcommon.v1.common.TimeRangeMetrics',  # Alias fix
        'RetentionPolicyConfig': 'gcommon.v1.common.MetricsRetentionPolicyConfig',  # Alias fix
    }
    
    # Define types that should reference their original packages
    original_package_types = {
        'ErrorTypeCount': 'gcommon.v1.metrics.ErrorTypeCount',
        'TimeRestriction': 'gcommon.v1.organization.TimeRestriction',
        'EmailTemplate': 'gcommon.v1.organization.EmailTemplate',
        'NotificationFrequency': 'gcommon.v1.organization.NotificationFrequency',
    }
    
    for proto_file in proto_dir.rglob('*.proto'):
        try:
            with open(proto_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # First, remove all complex concatenated prefixes by finding ANY pattern that looks like:
            # gcommon.v1.X.gcommon.v1.Y.Z or variations
            
            # Remove multiple concatenations like: gcommon.v1.common.gcommon.v1.common.gcommon.v1.common.Type
            content = re.sub(
                r'gcommon\.v1\.\w+\.gcommon\.v1\.\w+\.gcommon\.v1\.\w+\.(\w+)',
                r'\1',
                content
            )
            
            # Remove double concatenations like: gcommon.v1.common.gcommon.v1.common.Type
            content = re.sub(
                r'gcommon\.v1\.\w+\.gcommon\.v1\.\w+\.(\w+)',
                r'\1',
                content
            )
            
            # Remove single duplications like: gcommon.v1.metrics.gcommon.v1.metrics.Type
            content = re.sub(
                r'gcommon\.v1\.(\w+)\.gcommon\.v1\.\1\.(\w+)',
                r'\2',
                content
            )
            
            # Fix malformed concatenations like: Metricsgcommon.v1.common.Type
            content = re.sub(
                r'(\w+)gcommon\.v1\.\w+\.(\w+)',
                r'\2',
                content
            )
            
            # Now apply correct type mappings
            for simple_name, correct_type in common_types_mapping.items():
                # Replace any bare type name with the correct fully qualified type
                content = re.sub(
                    rf'\b{simple_name}\b',
                    correct_type,
                    content
                )
            
            for simple_name, correct_type in original_package_types.items():
                # Replace any bare type name with the correct fully qualified type
                content = re.sub(
                    rf'\b{simple_name}\b',
                    correct_type,
                    content
                )
            
            # Fix any remaining malformed references by normalizing to simple type names first
            # then applying the correct mapping
            
            # Pattern to catch any remaining gcommon.v1.X.Y where Y is in our known types
            all_known_types = {**common_types_mapping, **original_package_types}
            for type_name, correct_type in all_known_types.items():
                content = re.sub(
                    rf'gcommon\.v1\.\w+\.{type_name}',
                    correct_type,
                    content
                )
            
            if content != original_content:
                with open(proto_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                fixes_applied += 1
                print(f"Fixed {proto_file}")
                
        except Exception as e:
            print(f"Error processing {proto_file}: {e}")
    
    print(f"Applied aggressive fixes to {fixes_applied} files")

def fix_import_statements():
    """Add missing import statements for types that need them."""
    print("Adding missing import statements...")
    
    proto_dir = Path('./proto/gcommon/v1')
    fixes_applied = 0
    
    # Map of types to their required imports
    type_imports = {
        'gcommon.v1.metrics.ErrorTypeCount': 'import "gcommon/v1/metrics/error_type_count.proto";',
        'gcommon.v1.organization.TimeRestriction': 'import "gcommon/v1/organization/time_restriction.proto";',
        'gcommon.v1.organization.EmailTemplate': 'import "gcommon/v1/organization/email_template.proto";',
        'gcommon.v1.organization.NotificationFrequency': 'import "gcommon/v1/organization/notification_frequency.proto";',
        'gcommon.v1.common.MetricsRetentionPolicyConfig': 'import "gcommon/v1/common/metrics_retention_policy_config.proto";',
        'gcommon.v1.common.MetricsConfigChange': 'import "gcommon/v1/common/metrics_config_change.proto";',
        'gcommon.v1.common.ConfigRetrySettings': 'import "gcommon/v1/common/config_retry_settings.proto";',
        'gcommon.v1.common.MetricsValidationResult': 'import "gcommon/v1/common/metrics_validation_result.proto";',
        'gcommon.v1.common.TimeRangeMetrics': 'import "gcommon/v1/common/time_range_metrics.proto";',
        'gcommon.v1.common.MetricsAPIKeyConfig': 'import "gcommon/v1/common/metrics_api_key_config.proto";',
        'gcommon.v1.common.MetricsRetentionInfo': 'import "gcommon/v1/common/metrics_retention_info.proto";',
        'gcommon.v1.common.MetricsErrorStats': 'import "gcommon/v1/common/metrics_error_stats.proto";',
        'gcommon.v1.common.OrganizationResourceLimits': 'import "gcommon/v1/common/organization_resource_limits.proto";',
    }
    
    for proto_file in proto_dir.rglob('*.proto'):
        try:
            with open(proto_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            imports_to_add = []
            
            # Check which types are used in this file and need imports
            for type_ref, import_stmt in type_imports.items():
                if type_ref in content and import_stmt not in content:
                    # Don't import from self
                    if proto_file.name not in import_stmt:
                        imports_to_add.append(import_stmt)
            
            if imports_to_add:
                # Find where to insert imports
                lines = content.split('\n')
                insert_pos = 0
                
                for i, line in enumerate(lines):
                    if line.startswith('import '):
                        insert_pos = i + 1
                    elif line.startswith('syntax ') and insert_pos == 0:
                        insert_pos = i + 1
                
                if insert_pos == 0:
                    insert_pos = 1
                
                # Insert all needed imports
                for import_stmt in sorted(imports_to_add):
                    lines.insert(insert_pos, import_stmt)
                    insert_pos += 1
                
                content = '\n'.join(lines)
            
            if content != original_content:
                with open(proto_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                fixes_applied += 1
                print(f"Added imports to {proto_file}")
                
        except Exception as e:
            print(f"Error processing {proto_file}: {e}")
    
    print(f"Added imports to {fixes_applied} files")

def run_aggressive_cleanup():
    """Run the complete aggressive cleanup process."""
    print("Running aggressive protobuf cleanup...")
    print("=" * 60)
    
    aggressive_type_cleanup()
    print()
    
    fix_import_statements()
    print()
    
    print("=" * 60)
    print("Aggressive cleanup complete!")

if __name__ == "__main__":
    run_aggressive_cleanup()
