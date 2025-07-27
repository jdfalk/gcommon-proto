#!/bin/bash
# file: scripts/create-historical-tags.sh
# version: 1.0.0
# guid: c3d4e5f6-a7b8-9c0d-1e2f-3a4b5c6d7e8f

set -e

# Create historical tags for gcommon based on git history
# This creates semantic version tags for major commits/milestones

echo "🏷️  Creating historical tags for gcommon..."

# Get the git log with commit hashes
COMMITS=($(git log --oneline --reverse | head -20 | awk '{print $1}'))

if [ ${#COMMITS[@]} -eq 0 ]; then
    echo "❌ No commits found"
    exit 1
fi

echo "📝 Found ${#COMMITS[@]} commits for tagging"

# Define version progression
VERSIONS=(
    "v0.0.1"  # Initial commit
    "v0.0.2"  # Basic structure
    "v0.0.3"  # Common types
    "v0.0.4"  # Health module
    "v0.0.5"  # Database module
    "v0.0.6"  # Auth module start
    "v0.0.7"  # Cache module
    "v0.0.8"  # Config module
    "v0.0.9"  # Logging module
    "v0.0.10" # Metrics module
    "v0.0.11" # Queue module
    "v0.0.12" # Web module
    "v0.0.13" # Protobuf fixes
    "v0.0.14" # Service definitions
    "v0.0.15" # Import cleanup
    "v0.0.16" # Buf lint fixes
    "v0.0.17" # 1-1-1 structure
    "v0.0.18" # Documentation updates
    "v0.0.19" # CI improvements
    "v0.0.20" # Pre-release candidate
)

# Create tags for historical commits
for i in "${!COMMITS[@]}"; do
    if [ $i -lt ${#VERSIONS[@]} ]; then
        COMMIT="${COMMITS[$i]}"
        VERSION="${VERSIONS[$i]}"

        echo "🏷️  Creating tag $VERSION for commit $COMMIT"

        # Create tag with message
        git tag -a "$VERSION" "$COMMIT" -m "Release $VERSION

Historical release created for commit $COMMIT
This is part of the retroactive versioning for gcommon development.

Features at this point:
- Basic protobuf structure
- Core module definitions
- Service interfaces
"

        # Push the tag
        if git push origin "$VERSION" 2>/dev/null; then
            echo "✅ Successfully created and pushed tag $VERSION"
        else
            echo "⚠️  Tag $VERSION might already exist, skipping push"
        fi
    fi
done

# Create the current release (v0.1.0)
echo "🚀 Creating current release v0.1.0..."
git tag -a "v0.1.0" -m "Release v0.1.0

Major milestone release with:
- Complete protobuf 1-1-1 structure migration
- All buf lint issues resolved
- Service separation and cleanup
- Production-ready health, common, and database modules
- Foundation for subtitle-manager integration

Breaking Changes:
- Migrated from monolithic to 1-1-1 protobuf structure
- Separated service responsibilities (auth, db, etc.)
- Removed duplicate RPC methods

New Features:
- Clean protobuf imports
- Proper service boundaries
- Complete type definitions
- Historical versioning

Modules Status:
- ✅ Health: Production ready
- ✅ Common: Production ready
- ✅ Database: Production ready
- ✅ Log: Complete
- 🔄 Auth: Partial (core functionality working)
- 🔄 Cache: Partial
- 🔄 Config: Partial
- 🔄 Metrics: In progress
- 🔄 Queue: In progress
- 🔄 Web: In progress
"

if git push origin "v0.1.0" 2>/dev/null; then
    echo "✅ Successfully created and pushed release v0.1.0"
else
    echo "⚠️  Tag v0.1.0 might already exist"
fi

echo "🎉 Historical tagging complete!"
echo ""
echo "📋 Summary:"
echo "- Created ${#VERSIONS[@]} historical tags"
echo "- Current release: v0.1.0"
echo "- Next release will be v0.1.1 (patch) or v0.2.0 (minor)"
echo ""
echo "To create a new release, use:"
echo "  gh workflow run release.yml --field release-type=patch"
echo "  gh workflow run release.yml --field release-type=minor"
echo "  gh workflow run release.yml --field release-type=major"
