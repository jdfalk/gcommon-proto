#!/usr/bin/env python3
# file: scripts/dismiss_sdk_unused_import_alerts.py
# version: 1.2.0
# guid: a1b2c3d4-e5f6-7890-abcd-ef1234567890

"""
Script to dismiss code scanning alerts for unused imports and global variables in the SDK folder.

This script uses the GitHub CLI to:
1. List all open code scanning alerts for Python unused imports and global variables in the sdks/ folder
2. Dismiss them with an appropriate reason
3. Provide a summary of dismissed alerts

Usage:
    python3 scripts/dismiss_sdk_unused_import_alerts.py [--dry-run] [--reason REASON]

Options:
    --dry-run       Show what would be dismissed without actually dismissing
    --reason        Dismiss reason (default: "false positive")
    --help          Show this help message
"""

import argparse
import json
import subprocess
import sys
from typing import Any, Dict, List


def run_gh_command(args: List[str]) -> List[Dict[str, Any]]:
    """Run a GitHub CLI command and return parsed JSON result."""
    try:
        cmd = ["gh"] + args
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        if not result.stdout.strip():
            return []

        # Handle NDJSON format (multiple JSON objects separated by newlines)
        lines = result.stdout.strip().split("\n")
        results = []
        for line in lines:
            if line.strip():
                try:
                    results.append(json.loads(line))
                except json.JSONDecodeError:
                    # Skip malformed lines
                    continue
        return results

    except subprocess.CalledProcessError as e:
        print(f"Error running GitHub CLI command: {e}")
        print(f"Command: {' '.join(cmd)}")
        print(f"Error output: {e.stderr}")
        sys.exit(1)


def get_unused_import_alerts() -> List[Dict[str, Any]]:
    """Get all open code scanning alerts for Python unused imports and global variables in sdks/ folder."""
    # Get all open alerts
    alerts = run_gh_command(
        [
            "api",
            "repos/jdfalk/gcommon/code-scanning/alerts",
            "--paginate",
            "--jq",
            '.[] | select(.state == "open" and (.most_recent_instance.location.path | startswith("sdks/")) and (.rule.id == "py/unused-import" or .rule.id == "py/unused-global-variable")) | {number, state, rule: .rule.id, message: .message.text, path: .most_recent_instance.location.path, url}',
        ]
    )

    return alerts


def dismiss_alert(alert_number: int, reason: str, comment: str) -> bool:
    """Dismiss a specific alert."""
    try:
        run_gh_command(
            [
                "api",
                f"repos/jdfalk/gcommon/code-scanning/alerts/{alert_number}",
                "--method",
                "PATCH",
                "--field",
                "state=dismissed",
                "--field",
                f"dismissed_reason={reason}",
                "--field",
                f"dismissed_comment={comment}",
            ]
        )
        return True
    except Exception as e:
        print(f"Failed to dismiss alert {alert_number}: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description="Dismiss code scanning alerts for Python unused imports and global variables in SDK folder"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be dismissed without actually dismissing",
    )
    parser.add_argument(
        "--reason",
        default="false positive",
        choices=["false positive", "won't fix", "used in tests"],
        help="Dismiss reason (default: false positive)",
    )

    args = parser.parse_args()

    print(
        "🔍 Fetching code scanning alerts for Python unused imports and global variables in sdks/ folder..."
    )
    alerts = get_unused_import_alerts()

    if not alerts:
        print("✅ No Python unused import/global variable alerts found in sdks/ folder")
        return

    print(
        f"📋 Found {len(alerts)} Python unused import/global variable alert(s) in sdks/ folder:"
    )
    print()

    dismissed_count = 0
    failed_count = 0

    for alert in alerts:
        alert_number = alert["number"]
        rule_id = alert["rule"]
        path = alert["path"]

        print(f"  Alert #{alert_number}: {rule_id}")
        print(f"    File: {path}")

        if args.dry_run:
            print(f"    Would dismiss with reason: {args.reason}")
        else:
            comment = "Auto-dismissed: SDK generated files often have unused imports/variables that are part of the protobuf generation process"
            success = dismiss_alert(alert_number, args.reason, comment)

            if success:
                print("    ✅ Dismissed")
                dismissed_count += 1
            else:
                print("    ❌ Failed to dismiss")
                failed_count += 1

        print()

    if args.dry_run:
        print(f"🔍 Dry run complete. Would dismiss {len(alerts)} alert(s)")
    else:
        print("📊 Summary:")
        print(f"  ✅ Successfully dismissed: {dismissed_count}")
        if failed_count > 0:
            print(f"  ❌ Failed to dismiss: {failed_count}")
        print(f"  📋 Total processed: {len(alerts)}")


if __name__ == "__main__":
    main()
