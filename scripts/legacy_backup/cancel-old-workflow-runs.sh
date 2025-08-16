#!/bin/bash
# file: scripts/cancel-old-workflow-runs.sh
# version: 1.0.0
# guid: a1b2c3d4-e5f6-7890-1234-567890abcdef

set -euo pipefail

# Configuration
REPO="jdfalk/gcommon"
WORKFLOW_NAME="Complete Unified Automation"
WORKFLOW_FILE="unified-automation.yml"
MAX_RUNS_TO_KEEP=10  # Keep the most recent N runs
DRY_RUN=false

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --dry-run)
            DRY_RUN=true
            shift
            ;;
        --keep)
            MAX_RUNS_TO_KEEP="$2"
            shift 2
            ;;
        --repo)
            REPO="$2"
            shift 2
            ;;
        --workflow)
            WORKFLOW_FILE="$2"
            shift 2
            ;;
        -h|--help)
            echo "Usage: $0 [OPTIONS]"
            echo ""
            echo "Cancel old GitHub Actions workflow runs to clear backlog."
            echo ""
            echo "Options:"
            echo "  --dry-run          Show what would be canceled without actually doing it"
            echo "  --keep N           Keep the most recent N runs (default: $MAX_RUNS_TO_KEEP)"
            echo "  --repo REPO        Repository in format owner/repo (default: $REPO)"
            echo "  --workflow FILE    Workflow filename (default: $WORKFLOW_FILE)"
            echo "  -h, --help         Show this help message"
            echo ""
            echo "Examples:"
            echo "  $0 --dry-run                           # Preview what would be canceled"
            echo "  $0 --keep 5                           # Keep only 5 most recent runs"
            echo "  $0 --workflow unified-automation.yml  # Cancel specific workflow"
            exit 0
            ;;
        *)
            echo "Unknown option $1"
            exit 1
            ;;
    esac
done

# Check if gh CLI is installed and authenticated
if ! command -v gh &> /dev/null; then
    echo "❌ GitHub CLI (gh) is not installed. Please install it first:"
    echo "   brew install gh"
    exit 1
fi

if ! gh auth status &> /dev/null; then
    echo "❌ GitHub CLI is not authenticated. Please run:"
    echo "   gh auth login"
    exit 1
fi

echo "🔍 Fetching workflow runs for $REPO..."
echo "   Workflow: $WORKFLOW_NAME ($WORKFLOW_FILE)"
echo "   Keeping most recent: $MAX_RUNS_TO_KEEP runs"

if [ "$DRY_RUN" = true ]; then
    echo "   🧪 DRY RUN MODE - No changes will be made"
fi

echo ""

# Get all workflow runs, sorted by creation date (newest first)
echo "📋 Getting list of workflow runs..."

# First get the workflow ID
WORKFLOW_ID=$(gh api repos/$REPO/actions/workflows \
    --jq ".workflows[] | select(.path == \".github/workflows/$WORKFLOW_FILE\") | .id")

if [ -z "$WORKFLOW_ID" ]; then
    echo "❌ Could not find workflow with filename: $WORKFLOW_FILE"
    echo "Available workflows:"
    gh api repos/$REPO/actions/workflows --jq '.workflows[] | "  \(.name) (\(.path))"'
    exit 1
fi

echo "✅ Found workflow ID: $WORKFLOW_ID"

# Get all runs for this workflow
ALL_RUNS=$(gh api repos/$REPO/actions/workflows/$WORKFLOW_ID/runs \
    --paginate \
    --jq '.workflow_runs[] | {id: .id, status: .status, conclusion: .conclusion, created_at: .created_at, run_number: .run_number}')

# Convert to array and sort by run number (descending)
RUNS_ARRAY=$(echo "$ALL_RUNS" | jq -s '. | sort_by(.run_number) | reverse')

TOTAL_RUNS=$(echo "$RUNS_ARRAY" | jq 'length')

# Filter out completed runs - we only want to cancel active ones (queued, in_progress)
ACTIVE_RUNS=$(echo "$RUNS_ARRAY" | jq '[.[] | select(.status != "completed")]')
ACTIVE_COUNT=$(echo "$ACTIVE_RUNS" | jq 'length')

echo "📊 Total workflow runs found: $TOTAL_RUNS"
echo "📊 Active (non-completed) runs found: $ACTIVE_COUNT"

if [ "$ACTIVE_COUNT" -le "$MAX_RUNS_TO_KEEP" ]; then
    echo "✅ No runs need to be canceled (active: $ACTIVE_COUNT, keeping: $MAX_RUNS_TO_KEEP)"
    exit 0
fi

# Get active runs to cancel (skip the first MAX_RUNS_TO_KEEP)
RUNS_TO_CANCEL=$(echo "$ACTIVE_RUNS" | jq ".[$MAX_RUNS_TO_KEEP:]")
CANCEL_COUNT=$(echo "$RUNS_TO_CANCEL" | jq 'length')

echo "🎯 Active runs to cancel: $CANCEL_COUNT"
echo "🔒 Active runs to keep: $MAX_RUNS_TO_KEEP (most recent active runs)"
echo ""

# Show summary by status
echo "📈 Status breakdown of active runs to cancel:"
echo "$RUNS_TO_CANCEL" | jq -r 'group_by(.status) | .[] | "  \(.[0].status): \(length) runs"'
echo ""

if [ "$DRY_RUN" = true ]; then
    echo "🧪 DRY RUN - Would cancel these runs:"
    echo "$RUNS_TO_CANCEL" | jq -r '.[] | "  Run #\(.run_number) (ID: \(.id)) - \(.status) - \(.created_at)"'
    echo ""
    echo "To actually cancel these runs, run without --dry-run flag."
    exit 0
fi

# Confirm before proceeding
echo "⚠️  This will cancel $CANCEL_COUNT workflow runs."
read -p "Are you sure you want to proceed? (y/N): " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "❌ Canceled by user."
    exit 1
fi

echo ""
echo "🚀 Starting cancellation process..."

# Cancel runs in batches
BATCH_SIZE=20
CANCELED=0
FAILED=0

echo "$RUNS_TO_CANCEL" | jq -r '.[] | .id' | while read -r RUN_ID; do
    RUN_INFO=$(echo "$RUNS_TO_CANCEL" | jq -r ".[] | select(.id == $RUN_ID) | \"#\(.run_number) (\(.status))\"")

    if gh api repos/$REPO/actions/runs/$RUN_ID/cancel -X POST &> /dev/null; then
        echo "✅ Canceled run $RUN_INFO"
        ((CANCELED++)) || true
    else
        echo "❌ Failed to cancel run $RUN_INFO"
        ((FAILED++)) || true
    fi

    # Add small delay to avoid rate limiting
    sleep 0.1

    # Show progress every batch
    if (( (CANCELED + FAILED) % BATCH_SIZE == 0 )); then
        echo "📊 Progress: $((CANCELED + FAILED))/$CANCEL_COUNT processed (✅ $CANCELED canceled, ❌ $FAILED failed)"
    fi
done

echo ""
echo "🎉 Cancellation complete!"
echo "   ✅ Successfully canceled: $CANCELED runs"
echo "   ❌ Failed to cancel: $FAILED runs"
echo "   🔒 Kept most recent: $MAX_RUNS_TO_KEEP runs"
echo ""
echo "🔗 View remaining runs: https://github.com/$REPO/actions/workflows/$WORKFLOW_FILE"
