#!/bin/bash

echo "=== FIXING ALL MISSING TYPE IMPORTS ==="
echo

# Define the type mappings
declare -A TYPE_MAPPINGS
TYPE_MAPPINGS["gcommon.v1.common.Pagination"]="pkg/common/proto/types/pagination.proto"
TYPE_MAPPINGS["gcommon.v1.common.ResponseMetadata"]="pkg/common/proto/messages/response_metadata.proto"
TYPE_MAPPINGS["gcommon.v1.common.PaginatedResponse"]="pkg/common/proto/messages/paginated_response.proto"
TYPE_MAPPINGS["gcommon.v1.common.HealthStatus"]="pkg/common/proto/enums/health_status.proto"

# Get all files that have missing type references
buf lint 2>&1 | grep "unknown type" | while read -r line; do
    file=$(echo "$line" | cut -d: -f1)
    missing_type=$(echo "$line" | sed 's/.*unknown type //')
    
    echo "Fixing $file for missing type $missing_type"
    
    # Get the import path for this type
    import_path="${TYPE_MAPPINGS[$missing_type]}"
    
    if [ -n "$import_path" ]; then
        # Check if the import already exists
        if ! grep -q "import.*$import_path" "$file"; then
            echo "  Adding import: $import_path"
            
            # Find the line with the last import and add after it
            # Look for the last line that starts with 'import'
            last_import_line=$(grep -n "^import" "$file" | tail -1 | cut -d: -f1)
            
            if [ -n "$last_import_line" ]; then
                # Add the new import after the last import
                sed -i "${last_import_line}a\\import \"$import_path\";" "$file"
            else
                # If no imports exist, add after the package declaration
                package_line=$(grep -n "^package" "$file" | cut -d: -f1)
                if [ -n "$package_line" ]; then
                    sed -i "${package_line}a\\\\nimport \"$import_path\";" "$file"
                fi
            fi
        else
            echo "  Import already exists: $import_path"
        fi
    else
        echo "  WARNING: No mapping found for $missing_type"
    fi
    echo
done

echo "=== IMPORT FIXING COMPLETE ==="
