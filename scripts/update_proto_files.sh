#!/bin/bash
# file: update_proto_files.sh
# version: 1.0.0
# guid: 123e4567-e89b-12d3-a456-426614174004

# Script to add Google protobuf go_features import and API_OPAQUE option to all proto files

find /Users/jdfalk/repos/github.com/jdfalk/gcommon/pkg -name "*.proto" -type f | while read proto_file; do
    echo "Processing: $proto_file"

    # Create a temporary file
    temp_file=$(mktemp)

    # Process the file line by line
    while IFS= read -r line; do
        echo "$line" >> "$temp_file"

        # Add import after edition line
        if [[ $line == edition* ]]; then
            echo "" >> "$temp_file"
            echo 'import "google/protobuf/go_features.proto";' >> "$temp_file"
        fi

        # Add option after package line
        if [[ $line == package* ]]; then
            echo "" >> "$temp_file"
            echo 'option features.(pb.go).api_level = API_OPAQUE;' >> "$temp_file"
        fi

    done < "$proto_file"

    # Replace original file with updated content
    mv "$temp_file" "$proto_file"

done

echo "All proto files updated successfully!"
