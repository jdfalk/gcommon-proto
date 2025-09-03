#!/bin/bash
# file: setup_github_projects.sh
# version: 1.1.0
# guid: 6a7b8c9d-0e1f-2a3b-4c5d-6e7f8a9b0c1d

# Setup GitHub Projects for automated issue management
# This script creates the projects referenced in the automation workflows

REPO="jdfalk/gcommon"

echo "🚀 Setting up GitHub Projects for automated issue management..."

# Create Protobuf Implementation Epic project
echo "📋 Creating Protobuf Implementation Epic project..."
gh project create --title "Protobuf Implementation Epic" --owner jdfalk

# Create module-specific projects
echo "🔐 Creating Authentication Module project..."
gh project create --title "Authentication Module" --owner jdfalk

echo "🌐 Creating Web Services Module project..."
gh project create --title "Web Services Module" --owner jdfalk

echo "📨 Creating Message Queue Module project..."
gh project create --title "Message Queue Module" --owner jdfalk

echo "⚙️ Creating Configuration Module project..."
gh project create --title "Configuration Module" --owner jdfalk

echo "🔥 Creating High Priority Issues project..."
gh project create --title "High Priority Issues" --owner jdfalk

echo "✅ GitHub Projects setup complete!"
echo "🔧 Next: The auto-assign-projects.yml workflow will automatically assign new issues to appropriate projects based on labels"
