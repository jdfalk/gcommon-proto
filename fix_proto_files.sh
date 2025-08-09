#!/bin/bash
# file: fix_proto_files.sh
# version: 2.0.0
# guid: 123e4567-e89b-12d3-a456-426614174005

# Script to properly add Google protobuf go_features import and API_OPAQUE option to all proto files

echo "Starting proto file fixes..."

find /Users/jdfalk/repos/github.com/jdfalk/gcommon/pkg -name "*.proto" -type f | while read proto_file; do
    echo "Processing: $proto_file"

    # Skip if already has both import and option
    if grep -q 'import "google/protobuf/go_features.proto"' "$proto_file" && grep -q 'option features.(pb.go).api_level = API_OPAQUE' "$proto_file"; then
        echo "  Already has both import and option, skipping"
        continue
    fi

    # Create backup
    cp "$proto_file" "$proto_file.backup"

    # Create a temporary file
    temp_file=$(mktemp)

    # Process line by line
    while IFS= read -r line; do
        echo "$line" >> "$temp_file"

        # After package line, add the import if not already present
        if [[ $line == package* ]]; then
            if ! grep -q 'import "google/protobuf/go_features.proto"' "$proto_file"; then
                echo "" >> "$temp_file"
                echo 'import "google/protobuf/go_features.proto";' >> "$temp_file"
            fi
        fi

        # After go_package option, add the features option if not already present
        if [[ $line == *"option go_package"* ]]; then
            if ! grep -q 'option features.(pb.go).api_level = API_OPAQUE' "$proto_file"; then
                echo 'option features.(pb.go).api_level = API_OPAQUE;' >> "$temp_file"
            fi
        fi

    done < "$proto_file"

    # Replace original file with updated content
    mv "$temp_file" "$proto_file"
    echo "  Updated successfully"

done

echo "All proto files processed!"
