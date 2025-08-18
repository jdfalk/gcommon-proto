#!/usr/bin/env python3

# file: fix_internal_imports.py
# version: 1.0.0
# guid: 5d7f9b1e-3c5a-6f8d-2e4b-8a1c3d5f7b9e

"""
Fix internal type imports within and across modules.
"""

import re
from pathlib import Path
from typing import Dict, List, Set, Tuple

class InternalImportFixer:
    def __init__(self, proto_root: str):
        self.proto_root = Path(proto_root)
        
    def build_comprehensive_type_mapping(self) -> Dict[str, Tuple[str, str]]:
        """Build mapping of type names to (file_path, package)."""
        type_mapping = {}
        
        for proto_file in self.proto_root.rglob("*.proto"):
            with open(proto_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract package name
            package_match = re.search(r'package\s+([^;]+);', content)
            package = package_match.group(1) if package_match else ""
            
            # Find all enum and message definitions
            enum_matches = re.findall(r'enum\s+(\w+)\s*{', content)
            message_matches = re.findall(r'message\s+(\w+)\s*{', content)
            
            # Get relative path from proto root
            rel_path = proto_file.relative_to(self.proto_root)
            
            for enum_name in enum_matches:
                if enum_name not in type_mapping:
                    type_mapping[enum_name] = (str(rel_path), package)
            
            for message_name in message_matches:
                if message_name not in type_mapping:
                    type_mapping[message_name] = (str(rel_path), package)
        
        return type_mapping
    
    def find_used_types_in_content(self, content: str) -> Set[str]:
        """Find all custom types referenced in the content."""
        types_used = set()
        
        # Look for field type declarations
        field_matches = re.findall(r'^\s*(?:repeated\s+|optional\s+)?(\w+)\s+\w+\s*=\s*\d+', content, re.MULTILINE)
        for field_type in field_matches:
            if not field_type.lower() in ['string', 'int32', 'int64', 'uint32', 'uint64', 'bool', 'bytes', 'double', 'float']:
                if not field_type.startswith('google.'):
                    types_used.add(field_type)
        
        # Look for map value types
        map_matches = re.findall(r'map<[^,]+,\s*(\w+)>', content)
        for map_type in map_matches:
            if not map_type.lower() in ['string', 'int32', 'int64', 'uint32', 'uint64', 'bool', 'bytes', 'double', 'float']:
                if not map_type.startswith('google.'):
                    types_used.add(map_type)
        
        # Look for RPC method parameters
        rpc_matches = re.findall(r'rpc\s+\w+\s*\(\s*(\w+)\s*\)\s*returns\s*\(\s*(\w+)\s*\)', content)
        for req_type, resp_type in rpc_matches:
            if not req_type.startswith('google.'):
                types_used.add(req_type)
            if not resp_type.startswith('google.'):
                types_used.add(resp_type)
        
        # Look for fully qualified types like gcommon.v1.common.Error
        qualified_matches = re.findall(r'gcommon\.v1\.\w+\.(\w+)', content)
        for qualified_type in qualified_matches:
            types_used.add(qualified_type)
        
        return types_used
    
    def get_current_package(self, content: str) -> str:
        """Extract the current package from file content."""
        package_match = re.search(r'package\s+([^;]+);', content)
        return package_match.group(1) if package_match else ""
    
    def fix_file_imports(self, file_path: Path, type_mapping: Dict[str, Tuple[str, str]]) -> bool:
        """Fix imports in a single file."""
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Get current package
        current_package = self.get_current_package(content)
        
        # Find types used in this file
        types_used = self.find_used_types_in_content(content)
        
        if not types_used:
            return False
        
        # Get current imports
        current_imports = set()
        import_matches = re.findall(r'import\s+"([^"]+)";', content)
        for import_path in import_matches:
            current_imports.add(import_path)
        
        # Determine required imports
        required_imports = set()
        
        for type_name in types_used:
            if type_name in type_mapping:
                file_path_str, package = type_mapping[type_name]
                
                # Only add import if the type is from a different file
                # and not from the same package (unless it's a cross-package reference)
                file_rel_path = Path(file_path).relative_to(self.proto_root)
                
                if file_path_str != str(file_rel_path):
                    required_imports.add(file_path_str)
        
        # Filter out already imported files
        new_imports = required_imports - current_imports
        
        if new_imports:
            # Find where to insert imports (after google imports)
            google_import_lines = []
            other_import_lines = []
            
            for import_path in sorted(current_imports):
                if import_path.startswith('google/'):
                    google_import_lines.append(f'import "{import_path}";')
                else:
                    other_import_lines.append(f'import "{import_path}";')
            
            for import_path in sorted(new_imports):
                if not import_path.startswith('google/'):
                    other_import_lines.append(f'import "{import_path}";')
            
            # Remove duplicate and existing imports
            all_import_lines = google_import_lines + other_import_lines
            unique_imports = list(dict.fromkeys(all_import_lines))  # preserve order, remove dupes
            
            # Replace import section
            # Find package line
            package_match = re.search(r'(package\s+[^;]+;\s*\n)', content)
            if package_match:
                # Remove all existing import lines
                content = re.sub(r'\nimport\s+"[^"]+";', '', content)
                
                # Insert new import section
                new_import_section = '\n' + '\n'.join(unique_imports) + '\n'
                content = content.replace(package_match.group(1), package_match.group(1) + new_import_section)
                
                # Write back if changed
                if content != original_content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"  ✓ Fixed internal imports in {file_path}")
                    return True
        
        return False
    
    def fix_all_internal_imports(self):
        """Fix internal imports in all files."""
        print("Building comprehensive type mapping...")
        type_mapping = self.build_comprehensive_type_mapping()
        print(f"Found {len(type_mapping)} types across all modules")
        
        print("\nFixing internal imports...")
        files_changed = 0
        
        for proto_file in self.proto_root.rglob("*.proto"):
            if self.fix_file_imports(proto_file, type_mapping):
                files_changed += 1
        
        print(f"Fixed internal imports in {files_changed} files")

def main():
    fixer = InternalImportFixer("/home/runner/work/gcommon/gcommon/proto")
    fixer.fix_all_internal_imports()

if __name__ == "__main__":
    main()