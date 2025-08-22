#!/usr/bin/env python3
# file: fix_syntax_errors_immediate.py
# version: 1.0.0
# guid: a1b2c3d4-e5f6-7890-abcd-ef1234567890

import re
import glob

def fix_syntax_errors():
    """Fix immediate syntax errors in protobuf files"""
    
    proto_dir = "proto/gcommon/v1"
    
    # Find all .proto files with syntax errors
    error_patterns = [
        (r'package\s+([^;]+)\.\s*$', r'package \1;'),  # Fix package line with trailing dot
        (r'package\s+([^;{]+)\s*\{', r'package \1;\n\n{'),  # Fix package line with { instead of ;
        (r'gcommon\.v1\.common\.gcommon\.v1\.common\.', 'gcommon.v1.common.'),  # Fix double references
        (r'gcommon\.v1\.metrics\.gcommon\.v1\.metrics\.', 'gcommon.v1.metrics.'),
        (r'gcommon\.v1\.organization\.gcommon\.v1\.organization\.', 'gcommon.v1.organization.'),
        (r'gcommon\.v1\.config\.gcommon\.v1\.config\.', 'gcommon.v1.config.'),
    ]
    
    fixed_files = []
    
    for proto_file in glob.glob(f"{proto_dir}/**/*.proto", recursive=True):
        try:
            with open(proto_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Apply all syntax fixes
            for pattern, replacement in error_patterns:
                content = re.sub(pattern, replacement, content, flags=re.MULTILINE)
            
            # Special case: fix package lines that end with . instead of ;
            lines = content.split('\n')
            for i, line in enumerate(lines):
                if line.strip().startswith('package ') and line.strip().endswith('.'):
                    lines[i] = line.rstrip('.') + ';'
                # Fix lines where package declaration has a { at the end
                elif re.match(r'package\s+[^;]+\s*\{', line.strip()):
                    lines[i] = re.sub(r'(package\s+[^;{]+)\s*\{.*', r'\1;', line)
            
            content = '\n'.join(lines)
            
            # Only write if content changed
            if content != original_content:
                with open(proto_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                fixed_files.append(proto_file)
                print(f"Fixed syntax in: {proto_file}")
            
        except Exception as e:
            print(f"Error processing {proto_file}: {e}")
    
    return fixed_files

if __name__ == "__main__":
    print("=== Fixing Immediate Syntax Errors ===")
    fixed = fix_syntax_errors()
    print(f"\nFixed {len(fixed)} files with syntax errors")
    for f in fixed:
        print(f"  - {f}")
