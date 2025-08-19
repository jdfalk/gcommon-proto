#!/usr/bin/env python3
# file: fix_sdk_go_package_paths.py
# version: 1.0.0
# guid: 87654321-abcd-1234-5678-987654321098

import re
import glob

def fix_go_package_paths():
    """Fix all go_package options to use SDK paths instead of pkg paths"""
    
    # Find all .proto files
    proto_files = glob.glob("proto/**/*.proto", recursive=True)
    
    fixed_count = 0
    for proto_file in proto_files:
        try:
            with open(proto_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Pattern to match go_package options with pkg paths
            old_pattern = r'option go_package = "github\.com/jdfalk/gcommon/pkg/(.*?)";'
            new_replacement = r'option go_package = "github.com/jdfalk/gcommon/sdks/go/\1";'
            
            # Replace pkg paths with sdks/go paths
            new_content = re.sub(old_pattern, new_replacement, content)
            
            # Check if any changes were made
            if new_content != content:
                with open(proto_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Fixed: {proto_file}")
                fixed_count += 1
        
        except Exception as e:
            print(f"Error processing {proto_file}: {e}")
    
    print(f"\nFixed go_package paths in {fixed_count} files")

if __name__ == "__main__":
    fix_go_package_paths()
