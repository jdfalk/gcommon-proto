#!/bin/bash
# file: test_protoc.sh
# Test script to compile all 1-1-1 proto files and identify issues

cd /Users/jdfalk/repos/github.com/jdfalk/gcommon

echo "Testing protobuf compilation for 1-1-1 files..."
echo "================================================"

failed_files=()
successful_files=()

# Find all 1-1-1 proto files
find pkg -name "*.proto" -type f | grep -v -E "(common\.proto|auth\.proto|cache\.proto|database\.proto|config\.proto|health\.proto|log\.proto|metrics\.proto|queue\.proto|web\.proto)" | while read -r proto_file; do
    echo -n "Testing $proto_file ... "

    if protoc --proto_path=. --go_out=. --go_opt=paths=source_relative "$proto_file" 2>/dev/null; then
        echo "✅ SUCCESS"
        echo "$proto_file" >> /tmp/successful_files.txt
    else
        echo "❌ FAILED"
        echo "$proto_file" >> /tmp/failed_files.txt
        # Show the error
        echo "   Error: $(protoc --proto_path=. --go_out=. --go_opt=paths=source_relative "$proto_file" 2>&1)"
    fi
done

echo
echo "==============================================="
echo "Summary:"
if [[ -f /tmp/successful_files.txt ]]; then
    success_count=$(wc -l < /tmp/successful_files.txt)
    echo "✅ Successful compilations: $success_count"
else
    echo "✅ Successful compilations: 0"
fi

if [[ -f /tmp/failed_files.txt ]]; then
    fail_count=$(wc -l < /tmp/failed_files.txt)
    echo "❌ Failed compilations: $fail_count"
    echo
    echo "Failed files:"
    cat /tmp/failed_files.txt
else
    echo "❌ Failed compilations: 0"
    echo "🎉 All files compiled successfully!"
fi

# Cleanup
rm -f /tmp/successful_files.txt /tmp/failed_files.txt
