#!/bin/bash

# Script to add basic header and package information to empty proto files

echo "🔧 ADDING BASIC HEADERS TO EMPTY PROTO FILES..."
echo "==============================================="

# Function to add basic proto content
add_basic_proto_content() {
    local proto_file="$1"
    local module_name=$(echo "$proto_file" | sed 's|pkg/\([^/]*\)/.*|\1|')
    local file_name=$(basename "$proto_file" .proto)
    local file_type=""
    local package_name="gcommon.v1.${module_name}"

    # Determine file type based on directory
    if [[ "$proto_file" == *"/services/"* ]]; then
        file_type="Service"
    elif [[ "$proto_file" == *"/requests/"* ]]; then
        file_type="Request"
    elif [[ "$proto_file" == *"/responses/"* ]]; then
        file_type="Response"
    elif [[ "$proto_file" == *"/messages/"* ]]; then
        file_type="Message"
    elif [[ "$proto_file" == *"/enums/"* ]]; then
        file_type="Enum"
    elif [[ "$proto_file" == *"/types/"* ]]; then
        file_type="Type"
    else
        file_type="Definition"
    fi

    # Convert file_type to lowercase using tr
    local file_type_lower=$(echo "$file_type" | tr '[:upper:]' '[:lower:]')

    # Only add content if file is empty or very small
    if [[ ! -s "$proto_file" ]] || [[ $(wc -c < "$proto_file") -lt 50 ]]; then
        cat > "$proto_file" << EOF
// filepath: $proto_file
// file: ${proto_file#pkg/}
//
// ${file_type} definitions for ${module_name} module
// TODO: Implement actual protobuf definitions
//
edition = "2023";

package ${package_name};

import "google/protobuf/go_features.proto";

option go_package = "github.com/jdfalk/gcommon/pkg/${module_name}/proto;${module_name}pb";
option features.(pb.go).api_level = API_HYBRID;

// TODO: Add ${file_type_lower} definitions here
// This is a placeholder file created during 1-1-1 migration
// Implement the actual protobuf definitions according to the ${module_name} module requirements
EOF
        echo "✅ Added basic content to: $proto_file"
    else
        echo "⏭️  Skipped (not empty): $proto_file"
    fi
}

# Counter for processed files
processed_count=0
skipped_count=0

# Process all empty proto files
while IFS= read -r proto_file; do
    if [[ -f "$proto_file" ]]; then
        add_basic_proto_content "$proto_file"
        ((processed_count++))
    else
        echo "⚠️  File not found: $proto_file"
        ((skipped_count++))
    fi
done < empty_protos.txt

echo ""
echo "📊 SUMMARY:"
echo "==========="
echo "Processed files: $processed_count"
echo "Skipped files: $skipped_count"
echo ""
echo "✅ All empty proto files now have basic headers and package information!"
echo "🚀 Ready for protobuf implementation!"
