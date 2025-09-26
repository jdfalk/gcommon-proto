#!/usr/bin/env python3
# file: scripts/fix_imports_after_directory_rename.py
# version: 1.0.0
# guid: fix-imports-after-rename-script

"""
Fix all import statements after renaming directories to pb-suffixed names.

This script:
1. Finds all .proto files
2. Updates import statements from old directory names to pb-suffixed names
3. Handles all package imports (common -> commonpb, metrics -> metricspb, etc.)
"""

import os
import re
from pathlib import Path
from typing import List, Dict

def get_directory_mappings() -> Dict[str, str]:
    """Get mapping of old directory names to new pb-suffixed names."""
    return {
        'common/': 'commonpb/',
        'metrics/': 'metricspb/',
        'config/': 'configpb/',
        'database/': 'databasepb/',
        'health/': 'healthpb/',
        'media/': 'mediapb/',
        'organization/': 'organizationpb/',
        'queue/': 'queuepb/',
        'web/': 'webpb/',
    }

def find_proto_files(root_dir: str) -> List[str]:
    """Find all .proto files in the repository."""
    proto_files = []
    for root, dirs, files in os.walk(root_dir):
        # Skip .git and other hidden directories
        dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['logs', '__pycache__', 'scripts']]

        for file in files:
            if file.endswith('.proto'):
                proto_files.append(os.path.join(root, file))

    return sorted(proto_files)

def fix_imports_in_file(file_path: str, mappings: Dict[str, str]) -> int:
    """
    Fix import statements in a single proto file.
    
    Returns number of imports fixed.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        fixes_made = 0
        
        # Find and replace import statements
        for old_dir, new_dir in mappings.items():
            # Pattern to match import statements like: import "common/v1/something.proto"
            pattern = rf'import\s+"({re.escape(old_dir)}[^"]+)"'
            
            def replace_import(match):
                old_import = match.group(1)
                new_import = old_import.replace(old_dir, new_dir)
                return f'import "{new_import}"'
            
            new_content, count = re.subn(pattern, replace_import, content)
            if count > 0:
                content = new_content
                fixes_made += count
                print(f"    Fixed {count} imports from {old_dir} to {new_dir}")
        
        # Write back if changes were made
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
                
        return fixes_made
        
    except Exception as e:
        print(f"    ❌ Error processing {file_path}: {e}")
        return 0

def main():
    """Main function to fix all imports."""
    print("🔧 Fixing import statements after directory rename...")
    print()
    
    mappings = get_directory_mappings()
    print("📋 Directory mappings:")
    for old_dir, new_dir in mappings.items():
        print(f"   {old_dir} → {new_dir}")
    print()
    
    # Find all proto files
    proto_files = find_proto_files('.')
    print(f"📁 Found {len(proto_files)} proto files to process")
    print()
    
    total_fixes = 0
    files_with_fixes = 0
    
    # Process each file
    for file_path in proto_files:
        relative_path = os.path.relpath(file_path)
        print(f"🔍 Processing: {relative_path}")
        
        fixes = fix_imports_in_file(file_path, mappings)
        if fixes > 0:
            files_with_fixes += 1
            total_fixes += fixes
            print(f"    ✅ Fixed {fixes} import statements")
        else:
            print(f"    ✓ No imports to fix")
    
    print()
    print("📊 Summary:")
    print(f"   Files processed: {len(proto_files)}")
    print(f"   Files with fixes: {files_with_fixes}")
    print(f"   Total import statements fixed: {total_fixes}")
    print()
    
    if total_fixes > 0:
        print("✅ Import fixing complete! All proto files should now have correct pb-suffixed imports.")
    else:
        print("ℹ️  No import statements needed fixing.")

if __name__ == "__main__":
    main()