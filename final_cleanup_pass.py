#!/usr/bin/env python3
# file: final_cleanup_pass.py
# version: 1.0.0
# guid: b2c3d4e5-f6a7-8b9c-0d1e-2f3a4b5c6d7e

"""
Final cleanup pass to fix the remaining double concatenated prefixes.
"""

import re
from pathlib import Path

def final_type_cleanup():
    """Final cleanup of remaining double concatenated prefixes."""
    print("Starting final cleanup pass...")
    
    proto_dir = Path('./proto/gcommon/v1')
    fixes_applied = 0
    
    for proto_file in proto_dir.rglob('*.proto'):
        try:
            with open(proto_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Fix the remaining double concatenations like:
            # gcommon.v1.common.gcommon.v1.common.MetricsRetentionPolicyConfig
            content = re.sub(
                r'gcommon\.v1\.common\.gcommon\.v1\.common\.(\w+)',
                r'gcommon.v1.common.\1',
                content
            )
            
            # Fix organization double concatenations:
            # gcommon.v1.organization.gcommon.v1.organization.Type
            content = re.sub(
                r'gcommon\.v1\.organization\.gcommon\.v1\.organization\.(\w+)',
                r'gcommon.v1.organization.\1',
                content
            )
            
            # Fix metrics double concatenations:
            # gcommon.v1.metrics.gcommon.v1.metrics.Type
            content = re.sub(
                r'gcommon\.v1\.metrics\.gcommon\.v1\.metrics\.(\w+)',
                r'gcommon.v1.metrics.\1',
                content
            )
            
            # Fix config double concatenations:
            # gcommon.v1.config.gcommon.v1.config.Type
            content = re.sub(
                r'gcommon\.v1\.config\.gcommon\.v1\.config\.(\w+)',
                r'gcommon.v1.config.\1',
                content
            )
            
            # Fix queue double concatenations:
            # gcommon.v1.queue.gcommon.v1.queue.Type
            content = re.sub(
                r'gcommon\.v1\.queue\.gcommon\.v1\.queue\.(\w+)',
                r'gcommon.v1.queue.\1',
                content
            )
            
            # Handle specific cases we saw in the errors
            fixes = {
                'gcommon.v1.common.gcommon.v1.common.MetricsRetentionPolicyConfig': 'gcommon.v1.common.MetricsRetentionPolicyConfig',
                'gcommon.v1.common.gcommon.v1.common.OrganizationResourceLimits': 'gcommon.v1.common.OrganizationResourceLimits',
                'gcommon.v1.common.gcommon.v1.common.TimeRangeMetrics': 'gcommon.v1.common.TimeRangeMetrics',
                'gcommon.v1.organization.OrganizationComplianceSettings': 'gcommon.v1.organization.OrganizationComplianceSettings',
            }
            
            for wrong, correct in fixes.items():
                content = content.replace(wrong, correct)
            
            if content != original_content:
                with open(proto_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                fixes_applied += 1
                print(f"Fixed {proto_file}")
                
        except Exception as e:
            print(f"Error processing {proto_file}: {e}")
    
    print(f"Applied final fixes to {fixes_applied} files")

def add_missing_imports():
    """Add any missing import statements for the final cleanup."""
    print("Adding final missing imports...")
    
    proto_dir = Path('./proto/gcommon/v1')
    fixes_applied = 0
    
    # Check for files that need OrganizationComplianceSettings import
    for proto_file in proto_dir.rglob('*.proto'):
        try:
            with open(proto_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            imports_to_add = []
            
            # Check for OrganizationComplianceSettings usage
            if 'gcommon.v1.organization.OrganizationComplianceSettings' in content:
                import_stmt = 'import "gcommon/v1/organization/organization_compliance_settings.proto";'
                if import_stmt not in content:
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
                
                # Insert imports
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

if __name__ == "__main__":
    print("Running final cleanup pass...")
    print("=" * 50)
    
    final_type_cleanup()
    print()
    
    add_missing_imports()
    print()
    
    print("=" * 50)
    print("Final cleanup complete!")
