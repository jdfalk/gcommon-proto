#!/usr/bin/env python3
# file: fix_common_go_packages.py
# version: 2.1.0
# guid: 8c9d0e1f-2a3b-4c5d-6e7f-8a9b0c1d2e3f

"""
Comprehensive fix for all protobuf package and type reference issues.
This script will clean up all duplicated prefixes and ensure proper references.
"""

import re
from pathlib import Path

def clean_all_type_references():
    """Clean up all malformed type references in protobuf files."""
    print("Step 1: Cleaning all malformed type references...")
    
    proto_dir = Path('./proto/gcommon/v1')
    fixes_applied = 0
    
    for proto_file in proto_dir.rglob('*.proto'):
        try:
            with open(proto_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Fix multiple concatenated prefixes like gcommon.v1.common.gcommon.v1.common.Type
            content = re.sub(
                r'gcommon\.v1\.(\w+)\.gcommon\.v1\.\w+\.gcommon\.v1\.(\w+)\.(\w+)',
                r'gcommon.v1.\2.\3',
                content
            )
            
            # Fix double prefixes like gcommon.v1.metrics.gcommon.v1.metrics.Type
            content = re.sub(
                r'gcommon\.v1\.(\w+)\.gcommon\.v1\.\1\.(\w+)',
                r'gcommon.v1.\1.\2',
                content
            )
            
            # Fix cross-package double prefixes like gcommon.v1.metrics.gcommon.v1.common.Type
            content = re.sub(
                r'gcommon\.v1\.(\w+)\.gcommon\.v1\.(\w+)\.(\w+)',
                r'gcommon.v1.\2.\3',
                content
            )
            
            # Fix malformed prefixes like gcommon.v1.common.Metricsgcommon.v1.common.Type
            content = re.sub(
                r'gcommon\.v1\.(\w+)\.(\w+)gcommon\.v1\.(\w+)\.(\w+)',
                r'gcommon.v1.\3.\4',
                content
            )
            
            # Fix quadruple prefixes like gcommon.v1.common.gcommon.v1.common.gcommon.v1.common.Type
            content = re.sub(
                r'gcommon\.v1\.(\w+)\.gcommon\.v1\.\1\.gcommon\.v1\.\1\.(\w+)',
                r'gcommon.v1.\1.\2',
                content
            )
            
            if content != original_content:
                with open(proto_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                fixes_applied += 1
                print(f"Fixed malformed references in {proto_file}")
                
        except Exception as e:
            print(f"Error processing {proto_file}: {e}")
    
    print(f"Fixed malformed references in {fixes_applied} files")

def fix_specific_type_mappings():
    """Fix specific type mappings based on the error messages."""
    print("Step 2: Fixing specific type mappings...")
    
    proto_dir = Path('./proto/gcommon/v1')
    fixes_applied = 0
    
    # Create the correct mapping for each problematic type
    type_mappings = {
        # Types that should reference their original packages with proper imports
        'ErrorTypeCount': {
            'files_to_import': ['common/metrics_error_stats.proto'],
            'import_stmt': 'import "gcommon/v1/metrics/error_type_count.proto";',
            'type_ref': 'gcommon.v1.metrics.ErrorTypeCount'
        },
        'TimeRestriction': {
            'files_to_import': ['common/organization_access_control.proto'],
            'import_stmt': 'import "gcommon/v1/organization/time_restriction.proto";',
            'type_ref': 'gcommon.v1.organization.TimeRestriction'
        },
        'EmailTemplate': {
            'files_to_import': ['common/organization_notification_settings.proto'],
            'import_stmt': 'import "gcommon/v1/organization/email_template.proto";',
            'type_ref': 'gcommon.v1.organization.EmailTemplate'
        },
        'NotificationFrequency': {
            'files_to_import': ['common/organization_notification_settings.proto'],
            'import_stmt': 'import "gcommon/v1/organization/notification_frequency.proto";',
            'type_ref': 'gcommon.v1.organization.NotificationFrequency'
        },
        # Types that were moved to common and need consistent references
        'MetricsRetentionPolicyConfig': {
            'files_to_import': ['common/retention_policy_info.proto', 'metrics/metric_definition.proto'],
            'import_stmt': 'import "gcommon/v1/common/metrics_retention_policy_config.proto";',
            'type_ref': 'gcommon.v1.common.MetricsRetentionPolicyConfig'
        },
        'MetricsConfigChange': {
            'files_to_import': ['config/get_config_history_response.proto', 'metrics/update_result.proto'],
            'import_stmt': 'import "gcommon/v1/common/metrics_config_change.proto";',
            'type_ref': 'gcommon.v1.common.MetricsConfigChange'
        },
        'ConfigRetrySettings': {
            'files_to_import': ['config/validation_settings.proto', 'queue/subscription_config_update.proto'],
            'import_stmt': 'import "gcommon/v1/common/config_retry_settings.proto";',
            'type_ref': 'gcommon.v1.common.ConfigRetrySettings'
        },
        'MetricsValidationResult': {
            'files_to_import': ['metrics/create_provider_response.proto', 'metrics/record_metric_response.proto', 'metrics/update_provider_response.proto', 'queue/restore_queue_response.proto'],
            'import_stmt': 'import "gcommon/v1/common/metrics_validation_result.proto";',
            'type_ref': 'gcommon.v1.common.MetricsValidationResult'
        },
        'TimeRangeMetrics': {
            'files_to_import': ['metrics/get_metrics_request.proto', 'metrics/get_metrics_response.proto', 'metrics/get_metrics_summary_request.proto', 'metrics/get_provider_stats_request.proto', 'metrics/metric_query.proto', 'queue/export_queue_request.proto', 'queue/get_queue_stats_request.proto', 'queue/restore_options.proto'],
            'import_stmt': 'import "gcommon/v1/common/time_range_metrics.proto";',
            'type_ref': 'gcommon.v1.common.TimeRangeMetrics'
        },
        'MetricsAPIKeyConfig': {
            'files_to_import': ['metrics/security_config.proto', 'organization/integration_settings.proto'],
            'import_stmt': 'import "gcommon/v1/common/metrics_api_key_config.proto";',
            'type_ref': 'gcommon.v1.common.MetricsAPIKeyConfig'
        },
        'MetricsRetentionInfo': {
            'files_to_import': ['queue/get_topic_info_response.proto'],
            'import_stmt': 'import "gcommon/v1/common/metrics_retention_info.proto";',
            'type_ref': 'gcommon.v1.common.MetricsRetentionInfo'
        },
        'MetricsErrorStats': {
            'files_to_import': ['metrics/metrics_summary.proto', 'metrics/provider_statistics.proto', 'queue/get_queue_stats_response.proto'],
            'import_stmt': 'import "gcommon/v1/common/metrics_error_stats.proto";',
            'type_ref': 'gcommon.v1.common.MetricsErrorStats'
        },
        'OrganizationResourceLimits': {
            'files_to_import': ['organization/compute_isolation.proto'],
            'import_stmt': 'import "gcommon/v1/common/organization_resource_limits.proto";',
            'type_ref': 'gcommon.v1.common.OrganizationResourceLimits'
        },
    }
    
    # Apply type fixes and add imports
    for type_name, mapping in type_mappings.items():
        for file_rel_path in mapping['files_to_import']:
            file_path = proto_dir / file_rel_path
            if file_path.exists():
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    original_content = content
                    
                    # Replace any reference to this type with the correct one
                    content = re.sub(
                        rf'\b{type_name}\b',
                        mapping['type_ref'],
                        content
                    )
                    
                    # Add import if not present
                    if mapping['import_stmt'] not in content:
                        # Find where to insert the import
                        lines = content.split('\n')
                        insert_pos = 0
                        
                        for i, line in enumerate(lines):
                            if line.startswith('import '):
                                insert_pos = i + 1
                            elif line.startswith('syntax ') and insert_pos == 0:
                                insert_pos = i + 1
                        
                        if insert_pos == 0:
                            insert_pos = 1
                        
                        lines.insert(insert_pos, mapping['import_stmt'])
                        content = '\n'.join(lines)
                    
                    if content != original_content:
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(content)
                        fixes_applied += 1
                        print(f"Fixed {type_name} in {file_rel_path}")
                        
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")
    
    print(f"Applied specific type fixes to {fixes_applied} files")

def fix_remaining_simple_references():
    """Fix simple type references that don't have proper package prefixes."""
    print("Step 3: Fixing simple type references...")
    
    proto_dir = Path('./proto/gcommon/v1')
    fixes_applied = 0
    
    # Map simple names to their correct fully qualified names
    simple_type_fixes = {
        'RetentionPolicyConfig': 'gcommon.v1.common.MetricsRetentionPolicyConfig',
        'MetricsTimeRange': 'gcommon.v1.common.TimeRangeMetrics',
    }
    
    for proto_file in proto_dir.rglob('*.proto'):
        try:
            with open(proto_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Apply simple type fixes
            for old_type, new_type in simple_type_fixes.items():
                content = content.replace(old_type, new_type)
            
            if content != original_content:
                with open(proto_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                fixes_applied += 1
                print(f"Fixed simple references in {proto_file}")
                
        except Exception as e:
            print(f"Error processing {proto_file}: {e}")
    
    print(f"Fixed simple references in {fixes_applied} files")

def run_comprehensive_fixes():
    """Run all the comprehensive fixes in sequence."""
    print("Running comprehensive protobuf reference fixes...")
    print("=" * 60)
    
    clean_all_type_references()
    print()
    
    fix_specific_type_mappings()
    print()
    
    fix_remaining_simple_references()
    print()
    
    print("=" * 60)
    print("Comprehensive fixes complete!")

if __name__ == "__main__":
    run_comprehensive_fixes()
