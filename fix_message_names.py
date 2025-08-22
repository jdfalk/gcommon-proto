#!/usr/bin/env python3
# file: fix_message_names.py
# version: 1.0.0
# guid: c3d4e5f6-a7b8-9012-cdef-345678901234

import re
import glob

def fix_message_names():
    """Fix message names that got incorrectly qualified with package paths"""
    
    fixed_files = []
    
    # Process all proto files
    for proto_file in glob.glob("proto/gcommon/v1/**/*.proto", recursive=True):
        try:
            with open(proto_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Fix message declarations that have package qualifiers
            # Pattern: message gcommon.v1.package.MessageName {
            # Should be: message MessageName {
            content = re.sub(
                r'message\s+gcommon\.v1\.[a-z]+\.([A-Z][A-Za-z0-9_]*)\s*\{',
                r'message \1 {',
                content
            )
            
            # Fix enum declarations that have package qualifiers
            content = re.sub(
                r'enum\s+gcommon\.v1\.[a-z]+\.([A-Z][A-Za-z0-9_]*)\s*\{',
                r'enum \1 {',
                content
            )
            
            # Fix service declarations that have package qualifiers
            content = re.sub(
                r'service\s+gcommon\.v1\.[a-z]+\.([A-Z][A-Za-z0-9_]*)\s*\{',
                r'service \1 {',
                content
            )
            
            # Only write if content changed
            if content != original_content:
                with open(proto_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                fixed_files.append(proto_file)
                print(f"Fixed message names in: {proto_file}")
        
        except Exception as e:
            print(f"Error processing {proto_file}: {e}")
    
    return fixed_files

if __name__ == "__main__":
    print("=== Fixing Message Names ===")
    fixed = fix_message_names()
    print(f"\nFixed {len(fixed)} files with incorrect message names")
    for f in fixed:
        print(f"  - {f}")
