#!/usr/bin/env python3

# Script to systematically fix protobuf unknown type errors
# This will parse the buf_lint_errors.txt file and fix them systematically

import re
import os
from pathlib import Path

def parse_lint_errors(error_file):
    """Parse the buf lint errors file and extract error information."""
    errors = []
    with open(error_file, 'r') as f:
        for line in f:
            if 'unknown type' in line:
                # Parse lines like:
                # gcommon/v1/common/messages/auth_provider.proto:27:3:field gcommon.v1.common.messages.auth_provider.AuthProvider.type: unknown type AuthProviderType
                match = re.match(r'(.+\.proto):(\d+):(\d+):field .+: unknown type (.+)', line.strip())
                if match:
                    proto_file, line_num, col, unknown_type = match.groups()
                    errors.append({
                        'file': proto_file,
                        'line': int(line_num),
                        'unknown_type': unknown_type
                    })
    return errors

def find_enum_or_message_file(base_dir, type_name):
    """Find where a type is defined by searching enum and message files."""
    # Convert CamelCase to snake_case for file names
    file_name = re.sub(r'(?<!^)(?=[A-Z])', '_', type_name).lower()
    
    # Search in all modules
    for module in ['common', 'config', 'database', 'media', 'metrics', 'organization', 'queue', 'web']:
        enum_path = Path(base_dir) / f"proto/gcommon/v1/{module}/enums/{file_name}.proto"
        message_path = Path(base_dir) / f"proto/gcommon/v1/{module}/messages/{file_name}.proto"
        
        if enum_path.exists():
            return f"proto/gcommon/v1/{module}/enums/{file_name}.proto", f"gcommon.v1.{module}"
        if message_path.exists():
            return f"proto/gcommon/v1/{module}/messages/{file_name}.proto", f"gcommon.v1.{module}"
    
    return None, None

def fix_proto_file(proto_file, unknown_type, package_name):
    """Fix a proto file by adding import and using fully qualified type name."""
    with open(proto_file, 'r') as f:
        content = f.read()
    
    # Add import if not already present
    type_file, type_package = find_enum_or_message_file('/home/runner/work/gcommon/gcommon', unknown_type)
    if type_file and type_package:
        import_line = f'import "{type_file}";'
        if import_line not in content:
            # Add import after existing imports
            lines = content.split('\n')
            import_index = -1
            for i, line in enumerate(lines):
                if line.strip().startswith('import '):
                    import_index = i
            
            if import_index >= 0:
                lines.insert(import_index + 1, import_line)
                content = '\n'.join(lines)
        
        # Replace unqualified type with fully qualified type
        # Look for pattern: TypeName followed by field name
        qualified_type = f"{type_package}.{unknown_type}"
        
        # Replace patterns like "TypeName field_name = N;" with "package.TypeName field_name = N;"
        content = re.sub(
            rf'\b{unknown_type}\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*=',
            rf'{qualified_type} \1 =',
            content
        )
        
        # Replace patterns like "repeated TypeName" with "repeated package.TypeName"
        content = re.sub(
            rf'\brepeated\s+{unknown_type}\b',
            f'repeated {qualified_type}',
            content
        )
        
        with open(proto_file, 'w') as f:
            f.write(content)
        
        print(f"Fixed {proto_file}: {unknown_type} -> {qualified_type}")
        return True
    
    print(f"Could not find definition for {unknown_type}")
    return False

def main():
    base_dir = '/home/runner/work/gcommon/gcommon'
    errors = parse_lint_errors(f'{base_dir}/buf_lint_errors.txt')
    
    print(f"Found {len(errors)} unknown type errors")
    
    for error in errors:
        proto_file = f"{base_dir}/{error['file']}"
        if os.path.exists(proto_file):
            fix_proto_file(proto_file, error['unknown_type'], 'gcommon.v1.common')
        else:
            print(f"File not found: {proto_file}")

if __name__ == '__main__':
    main()