#!/bin/bash
# file: scripts/release.sh
# version: 1.0.0
# guid: d4e5f6a7-b8c9-0d1e-2f3a-4b5c6d7e8f9a

set -e

# Quick release script for gcommon
# Usage: ./scripts/release.sh [patch|minor|major|prerelease]

RELEASE_TYPE="${1:-patch}"
DRY_RUN="${2:-false}"

echo "🚀 Creating gcommon release..."
echo "📦 Release type: $RELEASE_TYPE"
echo "🧪 Dry run: $DRY_RUN"

# Ensure we're on main branch
CURRENT_BRANCH=$(git branch --show-current)
if [ "$CURRENT_BRANCH" != "main" ]; then
    echo "❌ Please switch to main branch first"
    echo "Current branch: $CURRENT_BRANCH"
    exit 1
fi

# Ensure working directory is clean
if [ -n "$(git status --porcelain)" ]; then
    echo "❌ Working directory is not clean. Please commit your changes first."
    git status --short
    exit 1
fi

# Pull latest changes
echo "📥 Pulling latest changes..."
git pull origin main

# Get current version
LATEST_TAG=$(git tag -l --sort=-version:refname | head -n1)
if [ -z "$LATEST_TAG" ]; then
    LATEST_TAG="v0.0.0"
fi

echo "📋 Current version: $LATEST_TAG"

# Calculate next version
VERSION=${LATEST_TAG#v}
IFS='.' read -ra ADDR <<< "$VERSION"
MAJOR=${ADDR[0]:-0}
MINOR=${ADDR[1]:-0}
PATCH=${ADDR[2]:-0}

case "$RELEASE_TYPE" in
    "major")
        MAJOR=$((MAJOR + 1))
        MINOR=0
        PATCH=0
        ;;
    "minor")
        MINOR=$((MINOR + 1))
        PATCH=0
        ;;
    "patch")
        PATCH=$((PATCH + 1))
        ;;
    "prerelease")
        COMMIT_COUNT=$(git rev-list --count HEAD)
        NEW_VERSION="v${MAJOR}.${MINOR}.${PATCH}-alpha.${COMMIT_COUNT}"
        ;;
    *)
        echo "❌ Invalid release type: $RELEASE_TYPE"
        echo "Valid options: patch, minor, major, prerelease"
        exit 1
        ;;
esac

if [ "$RELEASE_TYPE" != "prerelease" ]; then
    NEW_VERSION="v${MAJOR}.${MINOR}.${PATCH}"
fi

echo "🏷️  New version: $NEW_VERSION"

if [ "$DRY_RUN" = "true" ]; then
    echo "🧪 DRY RUN - Would create tag: $NEW_VERSION"
    echo "🧪 DRY RUN - Would push tag to origin"
    exit 0
fi

# Create and push tag
echo "📝 Creating tag $NEW_VERSION..."
git tag -a "$NEW_VERSION" -m "Release $NEW_VERSION

Automated release created on $(date)
Release type: $RELEASE_TYPE
Previous version: $LATEST_TAG

Changes in this release:
- See CHANGELOG.md for detailed changes
- Run 'git log $LATEST_TAG..$NEW_VERSION --oneline' for commit history
"

echo "📤 Pushing tag to origin..."
git push origin "$NEW_VERSION"

echo "✅ Release $NEW_VERSION created successfully!"
echo ""
echo "📋 Next steps:"
echo "1. Check GitHub releases page for automatic release creation"
echo "2. Update go.mod in dependent projects to use new version"
echo "3. Update CHANGELOG.md with release notes"
echo ""
echo "🔗 GitHub release: https://github.com/jdfalk/gcommon/releases/tag/$NEW_VERSION"
