#!/bin/bash
# file: scripts/dismiss-sdk-alerts.sh
# version: 1.0.0
# guid: b2c3d4e5-f6a7-8901-bcde-f23456789012

# Simple wrapper script for dismissing SDK unused import alerts

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

cd "$REPO_ROOT"

echo "🔧 Dismissing code scanning alerts for unused imports in SDK folder..."
echo ""

# Run the Python script
python3 "$SCRIPT_DIR/dismiss_sdk_unused_import_alerts.py" "$@"

echo ""
echo "✅ Done!"
