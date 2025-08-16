#!/bin/bash
# file: test_protoc.sh
# Test script to compile protobuf files and identify compilation issues

set -e

cd "$(dirname "$0")"

echo "🧪 GCommon Protobuf Compilation Test"
echo "====================================="
echo ""

failed_files=()
successful_files=()
total_files=0

echo "🔍 Finding all .proto files..."

# Find all proto files in pkg/ directory
while IFS= read -r -d '' proto_file; do
    total_files=$((total_files + 1))
    echo -n "Testing $proto_file ... "

    if protoc --proto_path=. --go_out=. --go_opt=paths=source_relative "$proto_file" 2>/dev/null; then
        echo "✅ SUCCESS"
        successful_files+=("$proto_file")
    else
        echo "❌ FAILED"
        failed_files+=("$proto_file")
    fi
done < <(find pkg -name "*.proto" -type f -print0)

echo ""
echo "📊 COMPILATION SUMMARY"
echo "======================"
echo "Total files tested: $total_files"
echo "✅ Successful: ${#successful_files[@]}"
echo "❌ Failed: ${#failed_files[@]}"

if [ ${#failed_files[@]} -gt 0 ]; then
    echo ""
    echo "🚨 FAILED FILES:"
    for file in "${failed_files[@]}"; do
        echo "   ❌ $file"
    done
    echo ""
    echo "💡 TIP: Run 'protoc --proto_path=. [file]' for detailed error messages"
    exit 1
else
    echo ""
    echo "🎉 All protobuf files compiled successfully!"
fi
