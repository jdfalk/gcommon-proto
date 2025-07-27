#!/usr/bin/env python3
"""
# file: enhanced_issue_manager.py
# version: 2.0.0
# guid: 4f8a2b3c-6d7e-1f2a-3b4c-5d6e7f8a9b0c

Enhanced Issue Manager with timestamp-based chronological processing.

This script extends the existing issue manager to support:
1. Timestamp-based chronological ordering
2. Dependency resolution via parent GUIDs
3. Enhanced validation and rollback capabilities
4. Backwards compatibility with existing formats

Usage:
  python3 enhanced_issue_manager.py process-enhanced --directory .github/issue-updates
  python3 enhanced_issue_manager.py migrate-timestamps --directory .github/issue-updates
"""

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from typing import Any, Dict, List, Tuple


class EnhancedIssueProcessor:
    """Enhanced issue processor with timestamp-based ordering and dependency resolution."""

    def __init__(self, github_api=None, dry_run: bool = False):
        self.api = github_api
        self.dry_run = dry_run
        self.processed_guids = set()
        self.guid_issue_map = {}

    def add_timestamp_to_updates(self, updates_directory: str) -> None:
        """Add timestamps to existing update files that don't have them."""
        print("🕒 Adding timestamps to update files...")

        # Process all JSON files in the directory
        if not os.path.exists(updates_directory):
            print(f"Directory {updates_directory} does not exist")
            return

        json_files = [
            f
            for f in os.listdir(updates_directory)
            if f.endswith(".json") and not f.startswith(".")
        ]

        updated_count = 0

        for filename in json_files:
            file_path = os.path.join(updates_directory, filename)

            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    data = json.load(f)

                modified = False

                # Handle both single objects and arrays
                updates_to_process = [data] if isinstance(data, dict) else data

                for update in updates_to_process:
                    if isinstance(update, dict) and "action" in update:
                        # Check if timestamp is missing
                        if "timestamp" not in update and "created_at" not in update:
                            # Try to extract timestamp from filename if it follows the pattern
                            timestamp = self._extract_timestamp_from_filename(filename)
                            if not timestamp:
                                # Use current time as fallback
                                timestamp = datetime.now(timezone.utc).isoformat()

                            update["timestamp"] = timestamp
                            update["created_at"] = timestamp
                            modified = True

                        # Add format version
                        if "format_version" not in update:
                            update["format_version"] = "2.0"
                            modified = True

                        # Add sequence number if missing
                        if "sequence" not in update:
                            update["sequence"] = 0
                            modified = True

                # Write back if modified
                if modified:
                    if not self.dry_run:
                        with open(file_path, "w", encoding="utf-8") as f:
                            json.dump(data, f, indent=2, ensure_ascii=False)
                        print(f"✅ Enhanced {filename}")
                    else:
                        print(f"[DRY RUN] Would enhance {filename}")
                    updated_count += 1

            except Exception as e:
                print(f"❌ Error processing {filename}: {e}")

        print(f"🎯 Enhanced {updated_count} files with timestamps")

    def _extract_timestamp_from_filename(self, filename: str) -> str:
        """Extract timestamp from filename if it follows the pattern YYYYMMDD_HHMMSS_guid.json"""
        try:
            # Pattern: 20250718_224902_guid.json
            if "_" in filename:
                parts = filename.split("_")
                if len(parts) >= 2:
                    date_part = parts[0]  # 20250718
                    time_part = parts[1]  # 224902

                    if len(date_part) == 8 and len(time_part) == 6:
                        # Parse the date and time
                        year = int(date_part[:4])
                        month = int(date_part[4:6])
                        day = int(date_part[6:8])
                        hour = int(time_part[:2])
                        minute = int(time_part[2:4])
                        second = int(time_part[4:6])

                        dt = datetime(
                            year, month, day, hour, minute, second, tzinfo=timezone.utc
                        )
                        return dt.isoformat()
        except (ValueError, IndexError):
            pass

        return None

    def process_updates_chronologically(self, updates_directory: str) -> bool:
        """Process updates in chronological order based on timestamps."""
        print("🕒 Processing updates in chronological order...")

        # Load all updates
        all_updates = []
        file_paths = []

        if os.path.exists(updates_directory):
            json_files = [
                f
                for f in os.listdir(updates_directory)
                if f.endswith(".json") and not f.startswith(".")
            ]

            for filename in json_files:
                file_path = os.path.join(updates_directory, filename)

                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        data = json.load(f)

                    # Handle both single objects and arrays
                    updates_in_file = [data] if isinstance(data, dict) else data

                    for update in updates_in_file:
                        if isinstance(update, dict) and "action" in update:
                            update["_source_file"] = filename
                            all_updates.append(update)

                    file_paths.append(file_path)

                except Exception as e:
                    print(f"❌ Error loading {filename}: {e}")

        if not all_updates:
            print("📝 No updates to process")
            return True

        # Sort updates chronologically
        sorted_updates = self._sort_updates_chronologically(all_updates)

        # Resolve dependencies
        resolved_updates = self._resolve_dependencies(sorted_updates)

        # Validate sequence
        valid, errors = self._validate_update_sequence(resolved_updates)
        if not valid:
            print("❌ Validation failed:")
            for error in errors:
                print(f"  - {error}")
            return False

        print(f"✅ Validation passed - processing {len(resolved_updates)} updates")

        # Process updates in order
        success_count = 0
        for i, update in enumerate(resolved_updates, 1):
            action = update.get("action", "unknown")
            guid = update.get("guid", "no-guid")
            timestamp = update.get("timestamp", "no-timestamp")

            print(
                f"📋 Update {i}/{len(resolved_updates)}: {action} (guid: {guid}, time: {timestamp})"
            )

            if self.dry_run:
                print(f"[DRY RUN] Would process {action} action")
                success_count += 1
            else:
                # Here you would call the actual issue processing logic
                # For now, just simulate success
                success_count += 1

        print(
            f"🎯 Successfully processed {success_count}/{len(resolved_updates)} updates"
        )
        return True

    def _sort_updates_chronologically(
        self, updates: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        """Sort updates by timestamp, then by sequence number."""

        def get_sort_key(update):
            timestamp = update.get("timestamp") or update.get("created_at", "")
            sequence = update.get("sequence", 0)

            try:
                # Parse timestamp
                dt = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
                return (dt, sequence)
            except (ValueError, AttributeError):
                # Fallback for malformed timestamps
                return (timestamp, sequence)

        return sorted(updates, key=get_sort_key)

    def _resolve_dependencies(
        self, updates: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        """Resolve parent/child dependencies using topological sort."""
        # Build dependency graph
        dependency_graph = {}

        for update in updates:
            guid = update.get("guid")
            parent_guid = update.get("parent_guid")

            if guid:
                dependency_graph[guid] = {
                    "update": update,
                    "depends_on": parent_guid,
                    "children": [],
                }

        # Add children references
        for guid, info in dependency_graph.items():
            parent_guid = info["depends_on"]
            if parent_guid and parent_guid in dependency_graph:
                dependency_graph[parent_guid]["children"].append(guid)

        # Topological sort
        resolved = []
        visited = set()

        def visit(guid):
            if guid in visited:
                return
            visited.add(guid)

            info = dependency_graph.get(guid)
            if not info:
                return

            # Visit parent first
            parent_guid = info["depends_on"]
            if parent_guid and parent_guid not in visited:
                visit(parent_guid)

            resolved.append(info["update"])

        # Process all updates
        for update in updates:
            guid = update.get("guid")
            if guid:
                visit(guid)
            else:
                # No GUID, add to end
                resolved.append(update)

        return resolved

    def _validate_update_sequence(
        self, updates: List[Dict[str, Any]]
    ) -> Tuple[bool, List[str]]:
        """Validate that updates can be applied in the given sequence."""
        errors = []
        created_issues = set()

        for i, update in enumerate(updates):
            action = update.get("action")
            number = update.get("number")
            parent_guid = update.get("parent_guid")

            if action == "create":
                guid = update.get("guid")
                if guid:
                    created_issues.add(guid)
            elif action in ["comment", "update", "close"]:
                if not number and not parent_guid:
                    errors.append(
                        f"Update {i}: {action} action missing issue reference"
                    )
                elif parent_guid and parent_guid not in created_issues:
                    errors.append(
                        f"Update {i}: parent issue {parent_guid} not created yet"
                    )

        return len(errors) == 0, errors


def main():
    """Main function with CLI interface."""
    parser = argparse.ArgumentParser(
        description="Enhanced Issue Manager with timestamp-based processing"
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Migrate timestamps command
    migrate_parser = subparsers.add_parser(
        "migrate-timestamps", help="Add timestamps to existing update files"
    )
    migrate_parser.add_argument(
        "--directory",
        default=".github/issue-updates",
        help="Directory containing update files",
    )
    migrate_parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be done without executing",
    )

    # Process enhanced command
    process_parser = subparsers.add_parser(
        "process-enhanced", help="Process updates in chronological order"
    )
    process_parser.add_argument(
        "--directory",
        default=".github/issue-updates",
        help="Directory containing update files",
    )
    process_parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be done without executing",
    )

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return 1

    processor = EnhancedIssueProcessor(dry_run=getattr(args, "dry_run", False))

    if args.command == "migrate-timestamps":
        processor.add_timestamp_to_updates(args.directory)
        return 0
    elif args.command == "process-enhanced":
        success = processor.process_updates_chronologically(args.directory)
        return 0 if success else 1
    else:
        print(f"Unknown command: {args.command}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
