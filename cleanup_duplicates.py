import os
import re

def clean_file(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()
    
    # Track seen imports and keep only first occurrence
    seen_imports = set()
    cleaned_lines = []
    
    for line in lines:
        # Check if this is an import line
        if line.strip().startswith('import "'):
            import_match = re.search(r'import "([^"]+)"', line)
            if import_match:
                import_path = import_match.group(1)
                if import_path not in seen_imports:
                    seen_imports.add(import_path)
                    cleaned_lines.append(line)
                # Skip duplicate imports
            else:
                cleaned_lines.append(line)
        else:
            cleaned_lines.append(line)
    
    # Write back the cleaned file
    with open(filepath, 'w') as f:
        f.writelines(cleaned_lines)

# Process all proto files
for root, dirs, files in os.walk('pkg'):
    for file in files:
        if file.endswith('.proto'):
            filepath = os.path.join(root, file)
            clean_file(filepath)
            print(f"Cleaned {filepath}")
