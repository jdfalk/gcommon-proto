#!/usr/bin/env python3

# file: fix_protobuf_issues.py
# version: 1.0.0
# guid: 8a2b4f1e-9c3d-4e5f-a7b9-1c2d3e4f5a6b

"""
Comprehensive protobuf fixes for gcommon repository.
This script fixes package names, import paths, and go_package options.
"""

import os
import re
from pathlib import Path
from typing import Dict, List, Set

class ProtobufFixer:
    def __init__(self, proto_root: str):
        self.proto_root = Path(proto_root)
        self.modules = ['common', 'auth', 'config', 'database', 'media', 'metrics', 'organization', 'queue', 'web']
        
    def fix_package_name(self, content: str, file_path: Path) -> str:
        """Fix package declaration to use module-level package names."""
        
        # Extract module from path: proto/gcommon/v1/{module}/...
        path_parts = file_path.parts
        if len(path_parts) >= 4 and path_parts[-4] == 'v1':
            module = path_parts[-3]  # e.g., 'common', 'auth', etc.
            new_package = f"gcommon.v1.{module}"
            
            # Replace package declaration
            content = re.sub(
                r'package\s+gcommon\.v1\.[^;]+;',
                f'package {new_package};',
                content
            )
        
        return content
    
    def fix_go_package(self, content: str, file_path: Path) -> str:
        """Fix go_package option for managed mode compatibility."""
        
        # Extract module from path
        path_parts = file_path.parts
        if len(path_parts) >= 4 and path_parts[-4] == 'v1':
            module = path_parts[-3]
            
            # New go_package should point to pkg directory for managed mode
            new_go_package = f"github.com/jdfalk/gcommon/pkg/{module}"
            
            # Replace go_package option
            content = re.sub(
                r'option go_package = "[^"]*";',
                f'option go_package = "{new_go_package}";',
                content
            )
        
        return content
    
    def get_all_proto_files(self) -> List[Path]:
        """Get all .proto files in the repository."""
        proto_files = []
        for proto_file in self.proto_root.rglob("*.proto"):
            proto_files.append(proto_file)
        return proto_files
    
    def build_type_mapping(self) -> Dict[str, str]:
        """Build a mapping of type names to their correct import paths."""
        type_mapping = {}
        
        for proto_file in self.get_all_proto_files():
            with open(proto_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Find all enum and message definitions
            enum_matches = re.findall(r'enum\s+(\w+)\s*{', content)
            message_matches = re.findall(r'message\s+(\w+)\s*{', content)
            
            # Get relative path from proto root
            rel_path = proto_file.relative_to(self.proto_root)
            
            for enum_name in enum_matches:
                type_mapping[enum_name] = str(rel_path)
            
            for message_name in message_matches:
                type_mapping[message_name] = str(rel_path)
        
        return type_mapping
    
    def fix_imports(self, content: str, type_mapping: Dict[str, str]) -> str:
        """Fix import statements to use correct absolute paths."""
        
        # Find all import statements (excluding google/protobuf imports)
        import_pattern = r'import\s+"(gcommon/[^"]+)";'
        imports = re.findall(import_pattern, content)
        
        for import_path in imports:
            # Convert relative import to absolute path
            # gcommon/v1/common/enums/appender_type.proto -> gcommon/v1/common/enums/appender_type.proto
            new_import = import_path
            content = content.replace(f'import "{import_path}";', f'import "{new_import}";')
        
        # Also check for any missing imports based on types used
        # This is a more complex operation that we'll handle in a separate pass
        
        return content
    
    def fix_single_file(self, file_path: Path):
        """Fix a single protobuf file."""
        print(f"Fixing {file_path}")
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Apply fixes
        content = self.fix_package_name(content, file_path)
        content = self.fix_go_package(content, file_path)
        
        # Only write if changed
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  ✓ Updated {file_path}")
        else:
            print(f"  - No changes needed for {file_path}")
    
    def fix_all_files(self):
        """Fix all protobuf files in the repository."""
        proto_files = self.get_all_proto_files()
        print(f"Found {len(proto_files)} protobuf files")
        
        # First pass: fix package names and go_package options
        print("\n=== Phase 1: Fixing package names and go_package options ===")
        for proto_file in proto_files:
            self.fix_single_file(proto_file)
        
        print("\n=== Phase 2: Building type mapping ===")
        type_mapping = self.build_type_mapping()
        print(f"Found {len(type_mapping)} types")
        
        print("\n=== Phase 3: Fixing import paths ===")
        # Second pass: fix imports
        for proto_file in proto_files:
            with open(proto_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            content = self.fix_imports(content, type_mapping)
            
            if content != original_content:
                with open(proto_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"  ✓ Updated imports in {proto_file}")

def main():
    # Run the fixer
    fixer = ProtobufFixer("/home/runner/work/gcommon/gcommon/proto")
    fixer.fix_all_files()
    
    print("\n=== Fix completed ===")
    print("Run 'buf lint' to check for remaining issues")

if __name__ == "__main__":
    main()