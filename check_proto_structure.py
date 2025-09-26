#!/usr/bin/env python3
# file: check_proto_structure.py
# version: 1.0.0
# guid: f1e2d3c4-b5a6-9876-5432-1098fedcba21

"""
Check the current structure of proto files in the gcommon repository.
Shows directory structure, file counts, and validates BSR compatibility.
"""

import os
import glob
from pathlib import Path

def check_proto_structure():
    """Check the current proto structure."""
    print("=== GCOMMON PROTO STRUCTURE CHECK ===\n")
    
    # Get all module directories at root level
    root_modules = []
    for item in os.listdir('.'):
        if os.path.isdir(item) and not item.startswith('.') and not item.startswith('_'):
            v1_path = os.path.join(item, 'v1')
            if os.path.exists(v1_path):
                root_modules.append(item)
    
    root_modules.sort()
    print(f"Found {len(root_modules)} modules at root level:")
    for module in root_modules:
        print(f"  - {module}/")
    
    print("\n=== MODULE DETAILS ===")
    
    total_files = 0
    for module in root_modules:
        v1_path = os.path.join(module, 'v1')
        proto_files = glob.glob(f"{v1_path}/*.proto")
        subdirs = [d for d in os.listdir(v1_path) 
                  if os.path.isdir(os.path.join(v1_path, d))]
        
        print(f"\n{module}/v1/:")
        print(f"  Proto files: {len(proto_files)}")
        
        if subdirs:
            print(f"  ⚠️  Subdirectories found (should be flattened): {subdirs}")
            for subdir in subdirs:
                subdir_path = os.path.join(v1_path, subdir)
                subdir_protos = glob.glob(f"{subdir_path}/*.proto")
                print(f"    {subdir}/: {len(subdir_protos)} proto files")
        
        total_files += len(proto_files)
        
        # Show first few proto files as examples
        if proto_files:
            print(f"  Example files:")
            for proto in sorted(proto_files)[:3]:
                filename = os.path.basename(proto)
                print(f"    - {filename}")
            if len(proto_files) > 3:
                print(f"    ... and {len(proto_files) - 3} more")
    
    print(f"\n=== SUMMARY ===")
    print(f"Total modules: {len(root_modules)}")
    print(f"Total proto files: {total_files}")
    
    # Check for old proto directory
    if os.path.exists('proto'):
        print("⚠️  Old 'proto/' directory still exists")
    else:
        print("✅ Old 'proto/' directory removed")
    
    # Check buf.yaml
    print(f"\n=== BUF CONFIGURATION ===")
    if os.path.exists('buf.yaml'):
        with open('buf.yaml', 'r') as f:
            content = f.read()
            if 'path: .' in content and 'buf.build/jdfalk/gcommon' in content:
                print("✅ buf.yaml configured for BSR")
            else:
                print("⚠️  buf.yaml needs BSR configuration")
    else:
        print("❌ buf.yaml not found")

def check_sample_imports():
    """Check import statements in a few sample proto files."""
    print(f"\n=== SAMPLE IMPORT CHECK ===")
    
    # Find a few sample proto files
    sample_files = []
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.proto') and 'v1' in root:
                sample_files.append(os.path.join(root, file))
                if len(sample_files) >= 3:
                    break
        if len(sample_files) >= 3:
            break
    
    for proto_file in sample_files:
        print(f"\nChecking {proto_file}:")
        try:
            with open(proto_file, 'r') as f:
                lines = f.readlines()
                imports = [line.strip() for line in lines if line.strip().startswith('import ')]
                if imports:
                    for imp in imports[:3]:  # Show first 3 imports
                        print(f"  {imp}")
                    if len(imports) > 3:
                        print(f"  ... and {len(imports) - 3} more imports")
                else:
                    print("  No imports found")
        except Exception as e:
            print(f"  Error reading file: {e}")

if __name__ == "__main__":
    os.chdir('/Users/jdfalk/repos/github.com/jdfalk/gcommon')
    check_proto_structure()
    check_sample_imports()