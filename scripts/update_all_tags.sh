#!/bin/bash
# file: scripts/update_all_tags.sh
# version: 1.0.0
# guid: update-all-tags-automation

"""
Comprehensive script to update all git tags and BSR labels after directory structure changes.

This script:
1. Force updates all major version tags (v1, v2)
2. Force updates all minor version tags (v1.9, v2.1, etc.)
3. Force pushes all tags to GitHub
4. Force pushes all labels to Buf Schema Registry
"""

set -e  # Exit on any error

echo "🏷️  Starting comprehensive tag update process..."
echo ""

# Define the tags to update
MAJOR_TAGS=("v1" "v2")
MINOR_TAGS=("v1.9" "v2.1" "v1.9.0" "v1.9.1" "v2.0.0" "v2.1.0")
BSR_LABELS=("v1" "v2" "v1.9" "v2.1" "v1.9.0" "v1.9.1" "v2.0.0" "v2.1.0" "main" "latest" "stable" "pb-packages")

echo "📋 Will update the following tags:"
echo "   Major tags: ${MAJOR_TAGS[*]}"
echo "   Minor tags: ${MINOR_TAGS[*]}"
echo "   BSR labels: ${BSR_LABELS[*]}"
echo ""

# 1. Force update all git tags
echo "🔄 Step 1: Force updating git tags..."
for tag in "${MAJOR_TAGS[@]}" "${MINOR_TAGS[@]}"; do
    echo "   Updating tag: $tag"
    git tag -f "$tag" -m "$tag - pb-suffixed directory structure"
done

echo "✅ All git tags updated successfully!"
echo ""

# 2. Force push all tags to GitHub
echo "🚀 Step 2: Force pushing tags to GitHub..."
git push origin --tags --force
echo "✅ All tags pushed to GitHub successfully!"
echo ""

# 3. Push all labels to Buf Schema Registry
echo "🌐 Step 3: Pushing labels to Buf Schema Registry..."
for label in "${BSR_LABELS[@]}"; do
    echo "   Pushing BSR label: $label"
    buf push --label "$label"
done

echo "✅ All BSR labels updated successfully!"
echo ""

echo "🎉 Comprehensive tag update complete!"
echo "   - All git tags updated and pushed to GitHub"
echo "   - All BSR labels updated on buf.build/jdfalk/gcommon"
echo "   - Ready for new pb-suffixed directory structure generation"
