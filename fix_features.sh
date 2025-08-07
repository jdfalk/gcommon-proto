#!/bin/bash
# file: fix_features.sh
# version: 1.0.0
# guid: f0e1d2c3-b4a5-9687-3021-456789abcdef

set -e

echo "Removing problematic features options from all proto files..."

# Find all proto files and remove the features option
find . -name "*.proto" -type f | while read file; do
    if grep -q "option features\.(pb\.go)\.api_level" "$file"; then
        echo "Fixing $file"
        # Remove the features option line
        sed -i '' '/option features\.(pb\.go)\.api_level/d' "$file"
        # Remove import of go_features if it exists
        sed -i '' '/import "google\/protobuf\/go_features\.proto";/d' "$file"
        sed -i '' '/import "pkg\/common\/proto\/protobuf\/go_features\.proto";/d' "$file"
        # Remove empty lines that might be left behind
        sed -i '' '/^[[:space:]]*$/N;/^\n$/d' "$file"
    fi
done

echo "✅ Fixed all features options"
