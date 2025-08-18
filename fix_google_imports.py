#!/usr/bin/env python3

# file: fix_google_imports.py
# version: 1.0.0
# guid: 3c5e7a9b-1d4f-6b8c-2e5a-9f1c3e5a7b9d

"""
Fix missing google protobuf imports.
"""

import re
from pathlib import Path
from typing import Set

class GoogleImportFixer:
    def __init__(self, proto_root: str):
        self.proto_root = Path(proto_root)
        
        # Map of google types to their import paths
        self.google_types = {
            'google.protobuf.Timestamp': 'google/protobuf/timestamp.proto',
            'google.protobuf.Duration': 'google/protobuf/duration.proto',
            'google.protobuf.Empty': 'google/protobuf/empty.proto',
            'google.protobuf.Any': 'google/protobuf/any.proto',
            'google.protobuf.FieldMask': 'google/protobuf/field_mask.proto',
            'google.protobuf.Struct': 'google/protobuf/struct.proto',
            'google.protobuf.Value': 'google/protobuf/struct.proto',
            'google.protobuf.ListValue': 'google/protobuf/struct.proto',
            'google.protobuf.NullValue': 'google/protobuf/struct.proto',
        }
    
    def find_google_types_in_content(self, content: str) -> Set[str]:
        """Find all google protobuf types used in content."""
        google_types_used = set()
        
        # Look for field declarations with google types
        google_pattern = r'\b(google\.protobuf\.\w+)\b'
        matches = re.findall(google_pattern, content)
        for match in matches:
            google_types_used.add(match)
        
        return google_types_used
    
    def fix_file(self, file_path: Path) -> bool:
        """Fix google imports in a single file."""
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Find google types used
        google_types_used = self.find_google_types_in_content(content)
        if not google_types_used:
            return False
        
        # Get current imports
        current_imports = set()
        import_matches = re.findall(r'import\s+"([^"]+)";', content)
        for import_path in import_matches:
            current_imports.add(import_path)
        
        # Determine required google imports
        required_google_imports = set()
        for google_type in google_types_used:
            if google_type in self.google_types:
                required_google_imports.add(self.google_types[google_type])
        
        # Add missing google imports
        google_imports_to_add = required_google_imports - current_imports
        
        if google_imports_to_add:
            # Find position to insert imports (after existing google imports)
            google_import_pattern = r'import\s+"google/protobuf/go_features\.proto";'
            match = re.search(google_import_pattern, content)
            
            if match:
                # Insert after go_features import
                insert_pos = match.end()
                new_imports = []
                for import_path in sorted(google_imports_to_add):
                    new_imports.append(f'import "{import_path}";')
                
                if new_imports:
                    content = content[:insert_pos] + '\n' + '\n'.join(new_imports) + content[insert_pos:]
                    
                    # Write back
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    
                    print(f"  ✓ Added google imports to {file_path}")
                    return True
        
        return False
    
    def fix_all_files(self):
        """Fix google imports in all files."""
        print("Fixing google protobuf imports...")
        
        files_changed = 0
        for proto_file in self.proto_root.rglob("*.proto"):
            if self.fix_file(proto_file):
                files_changed += 1
        
        print(f"Fixed google imports in {files_changed} files")

def main():
    fixer = GoogleImportFixer("/home/runner/work/gcommon/gcommon/proto")
    fixer.fix_all_files()

if __name__ == "__main__":
    main()