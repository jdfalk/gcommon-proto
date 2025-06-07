#!/bin/bash

# File: create_github_project.sh
# Purpose: Create GitHub project for gcommon development

set -e

echo "=== Creating GitHub Project ==="

# Create the project and get JSON output
echo "Creating project..."
PROJECT_JSON=$(gh project create --title "gCommon Development" --owner "jdfalk" --format json)

echo "Project JSON response: $PROJECT_JSON"

# Extract project number and URL from JSON
PROJECT_NUMBER=$(echo "$PROJECT_JSON" | jq -r '.number')
PROJECT_URL=$(echo "$PROJECT_JSON" | jq -r '.url')

echo "Project created: $PROJECT_URL"
echo "Project number: $PROJECT_NUMBER"

# Add issues to the project
echo "Adding issues to project..."

for issue_num in {4..41}; do
    echo "Adding issue #$issue_num to project..."
    gh project item-add "$PROJECT_NUMBER" --owner "jdfalk" --url "https://github.com/jdfalk/gcommon/issues/$issue_num"
done

echo "=== Project Setup Complete ==="
echo "Project URL: $PROJECT_URL"
echo "All 38 issues have been added to the project."
echo ""
echo "Next steps:"
echo "1. Visit the project to set up kanban columns"
echo "2. Organize issues by status (Todo, In Progress, Done)"
echo "3. Begin protobuf implementation starting with high-priority modules"
