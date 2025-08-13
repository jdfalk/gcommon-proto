#!/bin/bash
# file: scripts/quick-cancel-runs.sh
# version: 1.0.0
# guid: b2c3d4e5-f6a7-8901-2345-678901bcdef0

# Quick script to cancel old unified automation runs
# Usage: ./scripts/quick-cancel-runs.sh [dry-run]

set -euo pipefail

REPO="jdfalk/gcommon"
KEEP=5  # Keep only the 5 most recent runs

if [[ "${1:-}" == "dry-run" ]]; then
    echo "🧪 DRY RUN MODE - Previewing what would be canceled..."
    ./scripts/cancel-old-workflow-runs.sh --dry-run --keep $KEEP --repo $REPO
else
    echo "🚀 Canceling old workflow runs (keeping $KEEP most recent)..."
    ./scripts/cancel-old-workflow-runs.sh --keep $KEEP --repo $REPO
fi
