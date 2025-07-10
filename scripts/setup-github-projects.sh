#!/bin/bash
# file: scripts/setup-github-projects.sh
# version: 2.0.0
# guid: 9255d459-ae8e-428e-943b-7529ac0e8196

set -euo pipefail

ORG="${ORG:-jdfalk}"
REPO="${REPO:-gcommon}"

PROJECTS=("Metrics" "Queue" "Web" "Auth" "Cache" "Config")

#------------------------------
# Authentication Helpers
#------------------------------
setup_auth() {
    echo "Checking GitHub CLI authentication..."
    if ! gh auth token >/dev/null 2>&1; then
        echo "❌ GitHub CLI is not authenticated. Please run: gh auth login" >&2
        exit 1
    fi

    if ! gh project list --owner "$ORG" >/dev/null 2>&1; then
        echo "⚠️  Missing project scopes, attempting refresh..." >&2
        if ! gh auth refresh -s project,read:project >/dev/null 2>&1; then
            echo "❌ Failed to refresh authentication" >&2
            exit 1
        fi
    fi

    export GH_TOKEN=$(gh auth token)
    echo "✅ Authentication configured"
}

#------------------------------
# Project Helpers
#------------------------------
create_project() {
    local title="$1"
    local description="$2"
    local data
    echo "Creating project: $title"
    data=$(gh project create --owner "$ORG" --title "$title" --format json)
    local number
    number=$(echo "$data" | jq -r '.number')
    if [[ -n "$number" && "$number" != "null" ]]; then
        gh project edit "$number" --owner "$ORG" --description "$description"
        echo "$number"
    fi
}

get_project_number() {
    local title="$1"
    gh project list --owner "$ORG" --format json | jq -r --arg t "$title" '.projects[] | select(.title==$t) | .number'
}

link_repository() {
    local number="$1"
    gh project link --owner "$ORG" --repo "$REPO" "$number" >/dev/null 2>&1 || true
}

link_issues() {
    local number="$1"
    local label="$2"
    gh issue list --repo "$ORG/$REPO" --label "$label" --state open --json number \
        | jq -r '.[].number' | while read -r num; do
            gh project item-add "$number" --owner "$ORG" --url "https://github.com/$ORG/$REPO/issues/$num" >/dev/null 2>&1 || true
        done
}

#------------------------------
# Main
#------------------------------
main() {
    setup_auth

    for module in "${PROJECTS[@]}"; do
        local title="$module Module"
        local description="Development tasks for the $module module"
        local number
        number=$(get_project_number "$title")
        if [[ -z "$number" || "$number" == "null" ]]; then
            number=$(create_project "$title" "$description")
        fi
        if [[ -n "$number" && "$number" != "null" ]]; then
            link_repository "$number"
            link_issues "$number" "module:${module,,}"
            echo "✅ Project $title ready (#$number)"
        else
            echo "❌ Failed to create or locate project for $module" >&2
        fi
    done

    echo "🎉 Project setup completed"
}

main "$@"
