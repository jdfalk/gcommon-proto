#!/usr/bin/env python3
# file: fix_syntax_errors_final.py
# version: 1.0.0
# guid: a1b2c3d4-e5f6-7a8b-9c0d-1e2f3a4b5c6d

"""
Fix syntax errors in protobuf files where message names got corrupted with package prefixes.
"""

import re
from pathlib import Path

def fix_message_declarations():
    """Fix corrupted message declarations that include package prefixes."""
    print("Fixing corrupted message declarations...")
    
    proto_dir = Path('./proto/gcommon/v1')
    fixes_applied = 0
    
    for proto_file in proto_dir.rglob('*.proto'):
        try:
            with open(proto_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Fix message declarations that start with gcommon.v1.package.MessageName
            # Should be just: message MessageName
            content = re.sub(
                r'message gcommon\.v1\.\w+\.(\w+)',
                r'message \1',
                content
            )
            
            # Fix enum declarations that start with gcommon.v1.package.EnumName
            content = re.sub(
                r'enum gcommon\.v1\.\w+\.(\w+)',
                r'enum \1',
                content
            )
            
            # Fix service declarations that start with gcommon.v1.package.ServiceName
            content = re.sub(
                r'service gcommon\.v1\.\w+\.(\w+)',
                r'service \1',
                content
            )
            
            if content != original_content:
                with open(proto_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                fixes_applied += 1
                print(f"Fixed message declarations in {proto_file}")
                
        except Exception as e:
            print(f"Error processing {proto_file}: {e}")
    
    print(f"Fixed message declarations in {fixes_applied} files")

def add_comprehensive_imports():
    """Add all needed import statements based on file content analysis."""
    print("Adding comprehensive import statements...")
    
    proto_dir = Path('./proto/gcommon/v1')
    fixes_applied = 0
    
    # Complete mapping of types to their required imports
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
        'gcommon.v1.common.OrganizationAccessControl': 'import "gcommon/v1/common/organization_access_control.proto";',
        'gcommon.v1.common.OrganizationNotificationSettings': 'import "gcommon/v1/common/organization_notification_settings.proto";',
    }
    
    for proto_file in proto_dir.rglob('*.proto'):
        try:
            with open(proto_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            imports_to_add = []
            
            # Check which types are referenced and need imports
            for type_ref, import_stmt in type_imports.items():
                if type_ref in content and import_stmt not in content:
                    # Don't import from self
                    import_file = import_stmt.split('"')[1]  # Extract filename from import
                    current_file_path = str(proto_file.relative_to(Path('./proto')))
                    if import_file != current_file_path:
                        imports_to_add.append(import_stmt)
            
            if imports_to_add:
                # Find where to insert imports
                lines = content.split('\n')
                insert_pos = 0
                
                # Look for existing imports or syntax line
                for i, line in enumerate(lines):
                    if line.startswith('import '):
                        insert_pos = i + 1
                    elif line.startswith('syntax ') and insert_pos == 0:
                        insert_pos = i + 1
                    elif line.startswith('option ') and insert_pos == 0:
                        insert_pos = i
                        break
                
                if insert_pos == 0:
                    insert_pos = 1
                
                # Insert all needed imports
                for import_stmt in sorted(imports_to_add):
                    lines.insert(insert_pos, import_stmt)
                    insert_pos += 1
                
                # Add blank line after imports if needed
                if imports_to_add and insert_pos < len(lines) and lines[insert_pos].strip() != '':
                    lines.insert(insert_pos, '')
                
                content = '\n'.join(lines)
            
            if content != original_content:
                with open(proto_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                fixes_applied += 1
                print(f"Added imports to {proto_file}")
                
        except Exception as e:
            print(f"Error processing {proto_file}: {e}")
    
    print(f"Added imports to {fixes_applied} files")

def run_final_fixes():
    """Run the final syntax and import fixes."""
    print("Running final protobuf fixes...")
    print("=" * 60)
    
    fix_message_declarations()
    print()
    
    add_comprehensive_imports()
    print()
    
    print("=" * 60)
    print("Final fixes complete!")

if __name__ == "__main__":
    run_final_fixes()
