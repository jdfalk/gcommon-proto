#!/bin/bash
# file: workflow_fix_pipeline.sh
# version: 1.0.0
# guid: c3d4e5f6-a7b8-9012-cdef-345678901234

# Workflow Fix Pipeline
#
# Complete automation pipeline for discovering and fixing failing GitHub workflows.
# This script orchestrates both the analysis and fixing phases.

set -e

# Configuration
REPO=""
MAX_RUNS=10
DAYS_BACK=7
DRY_RUN=false
COPILOT_ONLY=false
ISSUES_ONLY=false

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Print colored output
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Function to show usage
show_usage() {
    cat << EOF
GitHub Workflow Fix Pipeline

Usage: $0 [OPTIONS]

OPTIONS:
    --repo REPO          Repository in format owner/repo (auto-detected if not specified)
    --max-runs NUM       Maximum number of workflow runs to analyze (default: 10)
    --days NUM           How many days back to look for failing workflows (default: 7)
    --dry-run            Only analyze and create fix files, don't submit to Copilot
    --copilot-only       Only use Copilot, don't create GitHub issues
    --issues-only        Only create GitHub issues, skip Copilot
    --help               Show this help message

EXAMPLES:
    $0                                    # Analyze current repo with defaults
    $0 --repo owner/repo --max-runs 20   # Analyze specific repo with more runs
    $0 --dry-run                          # Just analyze, don't submit fixes
    $0 --copilot-only                     # Only use Copilot for fixes

WORKFLOW:
    1. Discovers failing GitHub Actions workflows
    2. Downloads and analyzes workflow logs
    3. Generates comprehensive fix requests
    4. Submits to GitHub Copilot for automated fixes
    5. Creates GitHub issues as fallback
    6. Generates PR templates for manual fixes

REQUIREMENTS:
    - GitHub CLI (gh) installed and authenticated
    - Python 3.7+ with required dependencies
    - Access to repository with GitHub Actions
EOF
}

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --repo)
            REPO="$2"
            shift 2
            ;;
        --max-runs)
            MAX_RUNS="$2"
            shift 2
            ;;
        --days)
            DAYS_BACK="$2"
            shift 2
            ;;
        --dry-run)
            DRY_RUN=true
            shift
            ;;
        --copilot-only)
            COPILOT_ONLY=true
            shift
            ;;
        --issues-only)
            ISSUES_ONLY=true
            shift
            ;;
        --help)
            show_usage
            exit 0
            ;;
        *)
            print_error "Unknown option: $1"
            show_usage
            exit 1
            ;;
    esac
done

# Check prerequisites
check_prerequisites() {
    print_status "Checking prerequisites..."

    # Check if gh is installed
    if ! command -v gh &> /dev/null; then
        print_error "GitHub CLI (gh) is not installed. Please install it first."
        print_status "Visit: https://cli.github.com/"
        exit 1
    fi

    # Check if gh is authenticated
    if ! gh auth status &> /dev/null; then
        print_error "GitHub CLI is not authenticated. Please run 'gh auth login' first."
        exit 1
    fi

    # Check if python is available
    if ! command -v python3 &> /dev/null && ! command -v python &> /dev/null; then
        print_error "Python is not installed or not in PATH."
        exit 1
    fi

    # Use python3 if available, otherwise python
    if command -v python3 &> /dev/null; then
        PYTHON_CMD="python3"
    else
        PYTHON_CMD="python"
    fi

    # Check if scripts exist
    if [[ ! -f "fix_failing_workflows.py" ]]; then
        print_error "fix_failing_workflows.py not found in current directory."
        exit 1
    fi

    if [[ ! -f "copilot_workflow_helper.py" ]]; then
        print_error "copilot_workflow_helper.py not found in current directory."
        exit 1
    fi

    print_success "All prerequisites met"
}

# Main pipeline execution
run_pipeline() {
    print_status "Starting GitHub Workflow Fix Pipeline"

    # Build arguments for the analysis script
    ANALYSIS_ARGS=""
    if [[ -n "$REPO" ]]; then
        ANALYSIS_ARGS="$ANALYSIS_ARGS --repo $REPO"
    fi
    ANALYSIS_ARGS="$ANALYSIS_ARGS --max-runs $MAX_RUNS --days $DAYS_BACK"

    if [[ "$DRY_RUN" == true ]]; then
        ANALYSIS_ARGS="$ANALYSIS_ARGS --dry-run"
    fi

    # Step 1: Run workflow analysis
    print_status "Step 1: Analyzing failing workflows..."
    if ! $PYTHON_CMD fix_failing_workflows.py $ANALYSIS_ARGS; then
        print_error "Workflow analysis failed"
        exit 1
    fi

    # Step 2: Process fix requests (only if not dry run)
    if [[ "$DRY_RUN" == false ]]; then
        print_status "Step 2: Processing fix requests with Copilot..."

        if [[ ! -d "workflow_fixes" ]]; then
            print_warning "No workflow_fixes directory found. No fixes to process."
            exit 0
        fi

        # Count fix files
        FIX_COUNT=$(find workflow_fixes -name "*.md" ! -name "*_copilot_response.md" | wc -l)
        if [[ $FIX_COUNT -eq 0 ]]; then
            print_warning "No fix request files found."
            exit 0
        fi

        print_status "Found $FIX_COUNT fix request(s) to process"

        # Build arguments for the helper script
        HELPER_ARGS="workflow_fixes"
        if [[ -n "$REPO" ]]; then
            HELPER_ARGS="$HELPER_ARGS --repo $REPO"
        fi

        if [[ "$ISSUES_ONLY" == true ]]; then
            HELPER_ARGS="$HELPER_ARGS --create-issues-only"
        fi

        # Run the helper script
        if ! $PYTHON_CMD copilot_workflow_helper.py $HELPER_ARGS; then
            print_error "Fix request processing failed"
            exit 1
        fi

        print_success "Fix requests processed successfully"
    else
        print_success "Dry run completed. Check workflow_fixes/ directory for analysis results."
    fi

    # Step 3: Summary
    print_status "Pipeline Summary:"
    if [[ -d "workflow_fixes" ]]; then
        FIX_FILES=$(find workflow_fixes -name "*.md" | wc -l)
        RESPONSE_FILES=$(find workflow_fixes -name "*_copilot_response.md" 2>/dev/null | wc -l)
        print_status "- Fix request files created: $FIX_FILES"
        if [[ $RESPONSE_FILES -gt 0 ]]; then
            print_status "- Copilot responses received: $RESPONSE_FILES"
        fi
    fi

    if [[ -d "pr_templates" ]]; then
        PR_TEMPLATES=$(find pr_templates -name "*.md" | wc -l)
        if [[ $PR_TEMPLATES -gt 0 ]]; then
            print_status "- PR templates created: $PR_TEMPLATES"
        fi
    fi

    print_success "Workflow fix pipeline completed successfully!"

    # Provide next steps
    print_status "Next Steps:"
    print_status "1. Review the generated fix requests in workflow_fixes/"
    print_status "2. Check any Copilot responses for specific fixes"
    print_status "3. Review GitHub issues created for tracking"
    print_status "4. Use PR templates in pr_templates/ for manual fixes"
    print_status "5. Test fixes in feature branches before merging"
}

# Main execution
main() {
    check_prerequisites
    run_pipeline
}

# Run main function
main "$@"
