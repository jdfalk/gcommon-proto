#!/bin/bash
# file: quick_status_check.sh
# Quick status check and next steps for GCommon protobuf implementation

echo "🚀 GCommon Protobuf Implementation Status"
echo "=========================================="
echo ""

# Check if we have the required files
if [[ ! -f "issues.json" ]]; then
    echo "❌ issues.json not found - run merge_protobuf_issues.py first"
    exit 1
fi

if [[ ! -f "empty_protos.txt" ]]; then
    echo "❌ empty_protos.txt not found - run protobuf analysis first"
    exit 1
fi

# Count issues and files
TOTAL_ISSUES=$(jq length issues.json)
PROTOBUF_ISSUES=$(jq '[.[] | select(.title | contains("Protobuf"))] | length' issues.json)
EMPTY_FILES=$(wc -l < empty_protos.txt | xargs)
NON_EMPTY_FILES=$(wc -l < non_empty_protos.txt | xargs)
TOTAL_FILES=$((EMPTY_FILES + NON_EMPTY_FILES))

echo "📊 Current Numbers:"
echo "   Total protobuf files: $TOTAL_FILES"
echo "   Implemented files: $NON_EMPTY_FILES"
echo "   Empty files: $EMPTY_FILES"
echo "   Total GitHub issues: $TOTAL_ISSUES"
echo "   Protobuf-specific issues: $PROTOBUF_ISSUES"
echo ""

# Calculate completion percentage
COMPLETION_PERCENT=$(echo "scale=1; $NON_EMPTY_FILES * 100 / $TOTAL_FILES" | bc)
echo "🎯 Overall Completion: $COMPLETION_PERCENT%"
echo ""

# Show module priorities
echo "📋 Module Implementation Priority Order:"
echo "   1. 🔴 Metrics (95 files) - Start here!"
echo "   2. 🔴 Queue (175 files)"
echo "   3. 🔴 Web (176 files)"
echo "   4. 🟠 Auth (109 files)"
echo "   5. 🟠 Cache (36 files)"
echo "   6. 🟡 Config (20 files)"
echo "   7. 🟡 Health (14 files)"
echo ""

# Check GitHub project setup
echo "🔗 Important Links:"
echo "   GitHub Project Board: https://github.com/users/jdfalk/projects/3"
echo "   Issues: https://github.com/jdfalk/gcommon/issues"
echo ""

# Next steps
echo "⚡ Immediate Next Steps:"
echo "   1. Visit GitHub Project Board and set up Kanban columns"
echo "   2. Start with Issue #67: Protobuf Validation Pipeline"
echo "   3. Then tackle Issue #68: Metrics Messages (highest priority)"
echo "   4. Follow the implementation workflow in PROTOBUF_IMPLEMENTATION_PLAN.md"
echo ""

# Check if protoc is available
if command -v protoc &> /dev/null; then
    PROTOC_VERSION=$(protoc --version)
    echo "✅ protoc available: $PROTOC_VERSION"
else
    echo "❌ protoc not found - install with: brew install protobuf"
fi

# Check if buf is available
if command -v buf &> /dev/null; then
    BUF_VERSION=$(buf --version)
    echo "✅ buf available: $BUF_VERSION"
else
    echo "❌ buf not found - install with: brew install bufbuild/buf/buf"
fi

echo ""
echo "🎉 Ready to start implementing! All planning work is complete."
echo "   See PROTOBUF_IMPLEMENTATION_PLAN.md for detailed workflow."
