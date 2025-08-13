#!/bin/bash
# file: fix_duplicate_service_names.sh
# version: 1.0.0
# guid: 8f7e6d5c-4b3a-2918-7f6e-5d4c3b2a1908

echo "Fixing duplicate _service_service naming..."

# Find all files with duplicate _service_service
find pkg -name "*_service_service.proto" | while read file; do
    # Get the directory and current filename
    dir=$(dirname "$file")
    current_name=$(basename "$file")
    
    # Remove the duplicate _service suffix
    new_name=$(echo "$current_name" | sed 's/_service_service\.proto$/_service.proto/')
    
    if [ "$current_name" != "$new_name" ]; then
        echo "Renaming: $file -> $dir/$new_name"
        mv "$file" "$dir/$new_name"
    fi
done

echo "✅ Fixed duplicate service naming"
