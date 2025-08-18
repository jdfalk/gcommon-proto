#!/usr/bin/env python3

# file: fix_import_paths.py
# version: 1.0.0
# guid: 9b3c5d7f-a1e4-6f8b-2c5e-8f9a0b1c2d3e

"""
Fix import paths in protobuf files to correctly reference types.
"""

import os
import re
from pathlib import Path
from typing import Dict, List, Set

class ImportPathFixer:
    def __init__(self, proto_root: str):
        self.proto_root = Path(proto_root)
        
    def build_type_to_file_mapping(self) -> Dict[str, str]:
        """Build a mapping of type names to their defining files."""
        type_mapping = {}
        
        for proto_file in self.proto_root.rglob("*.proto"):
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
    
    def find_types_used_in_file(self, content: str) -> Set[str]:
        """Find all custom types used in a proto file."""
        types_used = set()
        
        # Look for field type declarations
        field_matches = re.findall(r'^\s*(?:repeated\s+)?(\w+)\s+\w+\s*=\s*\d+', content, re.MULTILINE)
        for field_type in field_matches:
            if not field_type.lower() in ['string', 'int32', 'int64', 'uint32', 'uint64', 'bool', 'bytes', 'double', 'float']:
                if not field_type.startswith('google.'):
                    types_used.add(field_type)
        
        # Look for RPC method parameters
        rpc_matches = re.findall(r'rpc\s+\w+\s*\(\s*(\w+)\s*\)\s*returns\s*\(\s*(\w+)\s*\)', content)
        for req_type, resp_type in rpc_matches:
            if not req_type.startswith('google.'):
                types_used.add(req_type)
            if not resp_type.startswith('google.'):
                types_used.add(resp_type)
        
        return types_used
    
    def fix_imports_in_file(self, file_path: Path, type_mapping: Dict[str, str]):
        """Fix imports in a single file."""
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Find types used in this file
        types_used = self.find_types_used_in_file(content)
        
        # Get current imports
        current_imports = set()
        import_matches = re.findall(r'import\s+"([^"]+)";', content)
        for import_path in import_matches:
            current_imports.add(import_path)
        
        # Find required imports
        required_imports = set()
        for type_name in types_used:
            if type_name in type_mapping:
                required_imports.add(type_mapping[type_name])
        
        # Remove incorrect imports and add correct ones
        for import_path in import_matches:
            if import_path.startswith('gcommon/'):
                # Remove the import line
                content = content.replace(f'import "{import_path}";', '')
        
        # Add correct imports
        import_section = []
        import_section.append('import "google/protobuf/go_features.proto";')
        
        for required_import in sorted(required_imports):
            import_section.append(f'import "{required_import}";')
        
        # Replace import section
        # Find the position after package declaration
        package_match = re.search(r'(package\s+[^;]+;\s*\n)', content)
        if package_match:
            # Insert imports after package
            new_imports = '\n' + '\n'.join(import_section) + '\n'
            
            # Remove existing import lines
            content = re.sub(r'\nimport\s+"[^"]+";', '', content)
            
            # Insert new imports
            content = content.replace(package_match.group(1), package_match.group(1) + new_imports)
        
        # Write back if changed
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  ✓ Fixed imports in {file_path}")
            return True
        else:
            return False
    
    def fix_all_imports(self):
        """Fix imports in all protobuf files."""
        print("Building type mapping...")
        type_mapping = self.build_type_to_file_mapping()
        print(f"Found {len(type_mapping)} types")
        
        print("\nFixing imports...")
        files_changed = 0
        
        for proto_file in self.proto_root.rglob("*.proto"):
            if self.fix_imports_in_file(proto_file, type_mapping):
                files_changed += 1
        
        print(f"\nFixed imports in {files_changed} files")

def main():
    fixer = ImportPathFixer("/home/runner/work/gcommon/gcommon/proto")
    fixer.fix_all_imports()

if __name__ == "__main__":
    main()