#!/bin/bash

# File: add_remaining_issues_to_project.sh
# Purpose: Add remaining issues to the existing GitHub project

set -e

PROJECT_NUMBER="2"
echo "=== Adding Remaining Issues to Project #$PROJECT_NUMBER ==="

# Start from issue 20 (since we got to around issue 19 before interruption)
for issue_num in {20..41}; do
    echo "Adding issue #$issue_num to project..."
    gh project item-add "$PROJECT_NUMBER" --owner "@me" --url "https://github.com/jdfalk/gcommon/issues/$issue_num"
done

echo "=== Finished Adding Issues ==="
echo "Project URL: https://github.com/users/jdfalk/projects/2"
echo ""
echo "All issues should now be in the project."
echo ""
echo "Next steps:"
echo "1. Visit https://github.com/users/jdfalk/projects/2"
echo "2. Set up kanban columns (Todo, In Progress, Done)"
echo "3. Organize issues by priority and module"
echo "4. Begin protobuf implementation starting with high-priority modules"
