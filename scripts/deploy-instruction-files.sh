#!/bin/bash
# file: scripts/deploy-instruction-files.sh
# version: 1.0.0
# guid: d1e2f3a4-b5c6-7890-1234-567890abcdef

set -euo pipefail

# Script to deploy instruction files and copilot-util-args across all repositories
# This ensures all repositories have the latest standardized configurations

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Logging functions
log_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

log_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

log_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Get the directory containing this script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

# Repository paths (adjust these paths as needed)
REPOS=(
    "/Users/jdfalk/repos/github.com/jdfalk/gcommon"
    "/Users/jdfalk/repos/github.com/jdfalk/ghcommon"
    "/Users/jdfalk/repos/github.com/jdfalk/subtitle-manager"
    "/Users/jdfalk/repos/github.com/jdfalk/copilot-agent-util-rust"
    "/Users/jdfalk/repos/scratch"
)

# Files to copy (source path relative to gcommon repo)
INSTRUCTION_FILES=(
    ".github/instructions/rust.instructions.md"
    ".github/instructions/rust-utility.instructions.md"
    ".github/instructions/general-coding.instructions.md"
)

UTIL_FILES=(
    "copilot-util-args"
)

VSCODE_TASK_FILES=(
    ".vscode/tasks.json"
)

# Function to check if repository exists
check_repo() {
    local repo_path="$1"
    if [[ ! -d "$repo_path" ]]; then
        log_error "Repository not found: $repo_path"
        return 1
    fi
    return 0
}

# Function to create directory if it doesn't exist
ensure_directory() {
    local dir_path="$1"
    if [[ ! -d "$dir_path" ]]; then
        log_info "Creating directory: $dir_path"
        mkdir -p "$dir_path"
    fi
}

# Function to copy file with backup
copy_with_backup() {
    local source="$1"
    local dest="$2"
    local repo_name="$3"

    if [[ ! -f "$source" ]]; then
        log_error "Source file not found: $source"
        return 1
    fi

    # Create backup if destination exists
    if [[ -f "$dest" ]]; then
        local backup="${dest}.backup.$(date +%Y%m%d_%H%M%S)"
        log_info "Backing up existing file: $(basename "$dest") -> $(basename "$backup")"
        cp "$dest" "$backup"
    fi

    # Ensure destination directory exists
    ensure_directory "$(dirname "$dest")"

    # Copy file
    cp "$source" "$dest"
    log_success "Copied $(basename "$source") to $repo_name"
}

# Function to update VS Code tasks with args file support
update_tasks_json() {
    local repo_path="$1"
    local repo_name="$(basename "$repo_path")"
    local tasks_file="$repo_path/.vscode/tasks.json"

    # Skip if repository doesn't have tasks.json or if it's the source repo
    if [[ ! -f "$tasks_file" || "$repo_path" == "$REPO_ROOT" ]]; then
        return 0
    fi

    log_info "Updating VS Code tasks for $repo_name"

    # Copy the updated tasks.json from gcommon
    copy_with_backup "$REPO_ROOT/.vscode/tasks.json" "$tasks_file" "$repo_name"
}

# Main deployment function
deploy_to_repo() {
    local repo_path="$1"
    local repo_name="$(basename "$repo_path")"

    log_info "Deploying to repository: $repo_name"

    if ! check_repo "$repo_path"; then
        return 1
    fi

    # Copy instruction files
    for file in "${INSTRUCTION_FILES[@]}"; do
        local source="$REPO_ROOT/$file"
        local dest="$repo_path/$file"
        copy_with_backup "$source" "$dest" "$repo_name"
    done

    # Copy utility configuration files
    for file in "${UTIL_FILES[@]}"; do
        local source="$REPO_ROOT/$file"
        local dest="$repo_path/$file"
        copy_with_backup "$source" "$dest" "$repo_name"
    done

    # Update VS Code tasks
    update_tasks_json "$repo_path"

    log_success "Completed deployment to $repo_name"
    echo
}

# Function to show usage
show_usage() {
    echo "Usage: $0 [OPTIONS]"
    echo
    echo "Options:"
    echo "  --dry-run    Show what would be copied without actually copying"
    echo "  --repo PATH  Deploy to specific repository path only"
    echo "  --help       Show this help message"
    echo
    echo "Examples:"
    echo "  $0                                    Deploy to all repositories"
    echo "  $0 --dry-run                         Show what would be deployed"
    echo "  $0 --repo /path/to/specific/repo     Deploy to specific repository"
}

# Parse command line arguments
DRY_RUN=false
SPECIFIC_REPO=""

while [[ $# -gt 0 ]]; do
    case $1 in
        --dry-run)
            DRY_RUN=true
            shift
            ;;
        --repo)
            SPECIFIC_REPO="$2"
            shift 2
            ;;
        --help)
            show_usage
            exit 0
            ;;
        *)
            log_error "Unknown option: $1"
            show_usage
            exit 1
            ;;
    esac
done

# Main execution
main() {
    log_info "Starting deployment of instruction files and configurations"
    log_info "Source repository: $(basename "$REPO_ROOT")"
    echo

    if [[ "$DRY_RUN" == "true" ]]; then
        log_warning "DRY RUN MODE - No files will be modified"
        echo
    fi

    local target_repos=()
    if [[ -n "$SPECIFIC_REPO" ]]; then
        target_repos=("$SPECIFIC_REPO")
    else
        target_repos=("${REPOS[@]}")
    fi

    local success_count=0
    local total_count=${#target_repos[@]}

    for repo in "${target_repos[@]}"; do
        if [[ "$DRY_RUN" == "true" ]]; then
            log_info "Would deploy to: $(basename "$repo")"
            ((success_count++))
        else
            if deploy_to_repo "$repo"; then
                ((success_count++))
            fi
        fi
    done

    echo
    log_info "Deployment Summary:"
    log_info "Successfully processed: $success_count/$total_count repositories"

    if [[ "$success_count" -eq "$total_count" ]]; then
        log_success "All deployments completed successfully!"
    else
        log_warning "Some deployments failed. Check the output above for details."
        exit 1
    fi
}

# Run main function
main "$@"
