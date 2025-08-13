#!/usr/bin/env python3
# file: issue_system_repair.py
# version: 1.0.0
# guid: f4e7d6c5-b8a9-4152-8fc3-2e4b7f8a9c3d

"""
Comprehensive Issue System Repair Tool

This script fixes the major issues in the GitHub issue management system:
1. Removes duplicate GUID files by moving them to processed/
2. Fixes malformed JSON files
3. Handles missing file references
4. Cleans up invalid issue number references
5. Automatically commits changes

Usage:
    python3 issue_system_repair.py --directory .github/issue-updates --auto-commit
    python3 issue_system_repair.py --dry-run  # Preview changes only
"""

import argparse
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Set


class IssueSystemRepair:
    """Comprehensive repair tool for the issue management system."""

    def __init__(
        self, directory: str, dry_run: bool = False, auto_commit: bool = False
    ):
        self.directory = Path(directory)
        self.processed_dir = self.directory / "processed"
        self.dry_run = dry_run
        self.auto_commit = auto_commit
        self.processed_guids: Set[str] = set()
        self.guid_to_file: Dict[str, str] = {}
        self.guid_to_issue: Dict[str, int] = {}
        self.errors: List[str] = []
        self.fixes: List[str] = []

        # Ensure processed directory exists
        if not self.dry_run:
            self.processed_dir.mkdir(exist_ok=True)

    def load_processed_guids(self) -> None:
        """Load all GUIDs from processed files to track what's already been handled."""
        print("📁 Loading processed GUIDs...")

        if not self.processed_dir.exists():
            return

        for file_path in self.processed_dir.glob("*.json"):
            try:
                with open(file_path, "r") as f:
                    data = json.load(f)

                guid = data.get("guid")
                legacy_guid = data.get("legacy_guid")

                if guid:
                    self.processed_guids.add(guid)
                if legacy_guid:
                    self.processed_guids.add(legacy_guid)

                # Track issue numbers if available
                issue_number = data.get("number")
                if issue_number and guid:
                    self.guid_to_issue[guid] = issue_number

            except (json.JSONDecodeError, IOError) as e:
                print(f"⚠️  Warning: Could not read processed file {file_path}: {e}")

    def scan_unprocessed_files(self) -> Dict[str, List[str]]:
        """Scan unprocessed files and categorize issues."""
        print("🔍 Scanning unprocessed files...")

        issues = {
            "duplicates": [],
            "malformed": [],
            "missing_refs": [],
            "invalid_numbers": [],
            "valid": [],
        }

        for file_path in self.directory.glob("*.json"):
            if file_path.name == "processed":
                continue

            try:
                with open(file_path, "r") as f:
                    content = f.read().strip()

                # Check for malformed JSON
                try:
                    data = json.loads(content)
                except json.JSONDecodeError as e:
                    issues["malformed"].append(str(file_path))
                    self.errors.append(f"Malformed JSON in {file_path}: {e}")
                    continue

                guid = data.get("guid")
                legacy_guid = data.get("legacy_guid")
                action = data.get("action")
                issue_number = data.get("number")

                # Check for duplicate GUIDs
                is_duplicate = False
                if guid and guid in self.processed_guids:
                    issues["duplicates"].append(str(file_path))
                    is_duplicate = True
                elif legacy_guid and legacy_guid in self.processed_guids:
                    issues["duplicates"].append(str(file_path))
                    is_duplicate = True
                elif guid and guid in self.guid_to_file:
                    # Duplicate in unprocessed files
                    issues["duplicates"].append(str(file_path))
                    is_duplicate = True

                if not is_duplicate:
                    # Track this GUID
                    if guid:
                        self.guid_to_file[guid] = str(file_path)
                    if legacy_guid:
                        self.guid_to_file[legacy_guid] = str(file_path)

                # Check for invalid issue numbers
                if action in ["comment", "update", "close"] and (
                    not issue_number or issue_number <= 0
                ):
                    issues["invalid_numbers"].append(str(file_path))

                if not is_duplicate:
                    issues["valid"].append(str(file_path))

            except IOError as e:
                issues["missing_refs"].append(str(file_path))
                self.errors.append(f"Could not read file {file_path}: {e}")

        return issues

    def fix_malformed_json(self, file_path: str) -> bool:
        """Attempt to fix malformed JSON files."""
        print(f"🔧 Fixing malformed JSON: {file_path}")

        try:
            with open(file_path, "r") as f:
                content = f.read().strip()

            # Common fixes
            # 1. Remove trailing comma before closing brace
            content = content.replace(",\n}", "\n}")
            content = content.replace(", }", " }")

            # 2. Fix missing quotes around values
            # This is a basic fix - may need more sophisticated parsing
            lines = content.split("\n")
            fixed_lines = []

            for line in lines:
                # Fix lines like: "parent_issue": dependencies,security
                if (
                    '": ' in line
                    and not line.strip().endswith(",")
                    and not line.strip().endswith("}")
                ):
                    if not (
                        line.strip().endswith('"')
                        or line.strip().endswith("null")
                        or line.strip().endswith("true")
                        or line.strip().endswith("false")
                        or line.strip().endswith("]")
                        or line.strip().isdigit()
                    ):
                        # Add quotes around the value
                        key_part, value_part = line.split('": ', 1)
                        line = f'{key_part}": "{value_part.strip()}"'

                fixed_lines.append(line)

            content = "\n".join(fixed_lines)

            # Test if it's valid JSON now
            try:
                json.loads(content)

                if not self.dry_run:
                    with open(file_path, "w") as f:
                        f.write(content)

                self.fixes.append(f"Fixed malformed JSON: {file_path}")
                return True

            except json.JSONDecodeError:
                # If still invalid, create a backup and mark for manual review
                if not self.dry_run:
                    backup_path = f"{file_path}.backup"
                    shutil.copy(file_path, backup_path)

                self.errors.append(
                    f"Could not auto-fix JSON: {file_path} (backup created)"
                )
                return False

        except Exception as e:
            self.errors.append(f"Error fixing JSON {file_path}: {e}")
            return False

    def move_duplicate_to_processed(self, file_path: str) -> bool:
        """Move a duplicate file to the processed directory."""
        file_name = Path(file_path).name
        dest_path = self.processed_dir / file_name

        print(f"📦 Moving duplicate to processed: {file_name}")

        try:
            if not self.dry_run:
                # If destination exists, create a unique name
                if dest_path.exists():
                    base_name = dest_path.stem
                    suffix = dest_path.suffix
                    counter = 1
                    while dest_path.exists():
                        dest_path = (
                            self.processed_dir / f"{base_name}_dup{counter}{suffix}"
                        )
                        counter += 1

                shutil.move(file_path, dest_path)

            self.fixes.append(f"Moved duplicate to processed: {file_name}")
            return True

        except Exception as e:
            self.errors.append(f"Error moving duplicate {file_path}: {e}")
            return False

    def fix_invalid_issue_numbers(self, file_path: str) -> bool:
        """Fix files with invalid issue numbers."""
        print(f"🔧 Fixing invalid issue number: {file_path}")

        try:
            with open(file_path, "r") as f:
                data = json.load(f)

            action = data.get("action")

            if action in ["comment", "update", "close"]:
                # For these actions, if no valid issue number, we need to either:
                # 1. Move to processed as invalid
                # 2. Try to infer the issue number from the GUID mapping

                guid = data.get("guid")
                legacy_guid = data.get("legacy_guid")

                # Try to find the issue number from our mapping
                issue_number = None
                if guid and guid in self.guid_to_issue:
                    issue_number = self.guid_to_issue[guid]
                elif legacy_guid and legacy_guid in self.guid_to_issue:
                    issue_number = self.guid_to_issue[legacy_guid]

                if issue_number:
                    data["number"] = issue_number

                    if not self.dry_run:
                        with open(file_path, "w") as f:
                            json.dump(data, f, indent=2)

                    self.fixes.append(
                        f"Fixed issue number for {file_path}: #{issue_number}"
                    )
                    return True
                else:
                    # Move to processed as invalid
                    return self.move_duplicate_to_processed(file_path)

            return True

        except Exception as e:
            self.errors.append(f"Error fixing issue number {file_path}: {e}")
            return False

    def run_repair(self) -> None:
        """Run the complete repair process."""
        print("🔧 Starting Issue System Repair...")
        print(f"📂 Working directory: {self.directory}")
        print(f"🧪 Dry run mode: {self.dry_run}")

        # Step 1: Load processed GUIDs
        self.load_processed_guids()
        print(f"📊 Found {len(self.processed_guids)} processed GUIDs")

        # Step 2: Scan unprocessed files
        issues = self.scan_unprocessed_files()

        print("\n📈 Scan Results:")
        print(f"  ✅ Valid files: {len(issues['valid'])}")
        print(f"  🔄 Duplicate files: {len(issues['duplicates'])}")
        print(f"  🚨 Malformed JSON: {len(issues['malformed'])}")
        print(f"  ❌ Invalid issue numbers: {len(issues['invalid_numbers'])}")
        print(f"  📁 Missing references: {len(issues['missing_refs'])}")

        # Step 3: Fix malformed JSON files
        if issues["malformed"]:
            print(f"\n🔧 Fixing {len(issues['malformed'])} malformed JSON files...")
            for file_path in issues["malformed"]:
                self.fix_malformed_json(file_path)

        # Step 4: Move duplicates to processed
        if issues["duplicates"]:
            print(
                f"\n📦 Moving {len(issues['duplicates'])} duplicate files to processed..."
            )
            for file_path in issues["duplicates"]:
                self.move_duplicate_to_processed(file_path)

        # Step 5: Fix invalid issue numbers
        if issues["invalid_numbers"]:
            print(
                f"\n🔧 Fixing {len(issues['invalid_numbers'])} files with invalid issue numbers..."
            )
            for file_path in issues["invalid_numbers"]:
                self.fix_invalid_issue_numbers(file_path)

        # Step 6: Report results
        print("\n📊 Repair Summary:")
        print(f"  ✅ Fixes applied: {len(self.fixes)}")
        print(f"  ❌ Errors encountered: {len(self.errors)}")

        if self.fixes:
            print("\n🎯 Fixes Applied:")
            for fix in self.fixes:
                print(f"  • {fix}")

        if self.errors:
            print("\n⚠️  Errors:")
            for error in self.errors:
                print(f"  • {error}")

        # Step 7: Auto-commit if requested
        if self.auto_commit and not self.dry_run and self.fixes:
            self.auto_commit_changes()

    def auto_commit_changes(self) -> None:
        """Automatically commit the repair changes."""
        print("\n🔄 Auto-committing changes...")

        try:
            # Change to the repository root
            repo_root = self.directory.parent.parent
            os.chdir(repo_root)

            # Add changes
            subprocess.run(["git", "add", ".github/issue-updates/"], check=True)

            # Check if there are changes to commit
            result = subprocess.run(
                ["git", "diff", "--cached", "--quiet"], capture_output=True
            )
            if result.returncode == 0:
                print("  ℹ️  No changes to commit")
                return

            # Commit changes
            commit_message = (
                f"fix: repair issue system - {len(self.fixes)} fixes applied\n\n"
            )
            commit_message += "Automated repair includes:\n"
            for fix in self.fixes[:10]:  # Limit to first 10 fixes in commit message
                commit_message += f"- {fix}\n"
            if len(self.fixes) > 10:
                commit_message += f"- ... and {len(self.fixes) - 10} more fixes\n"

            subprocess.run(["git", "commit", "-m", commit_message], check=True)
            print(f"  ✅ Committed {len(self.fixes)} fixes")

            # Optionally push
            push_result = subprocess.run(
                ["git", "push"], capture_output=True, text=True
            )
            if push_result.returncode == 0:
                print("  🚀 Pushed changes to remote")
            else:
                print(f"  ⚠️  Could not push: {push_result.stderr}")

        except subprocess.CalledProcessError as e:
            print(f"  ❌ Git operation failed: {e}")
        except Exception as e:
            print(f"  ❌ Auto-commit failed: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="Repair the GitHub issue management system"
    )
    parser.add_argument(
        "--directory",
        default=".github/issue-updates",
        help="Directory containing issue update files",
    )
    parser.add_argument(
        "--dry-run", action="store_true", help="Preview changes without applying them"
    )
    parser.add_argument(
        "--auto-commit",
        action="store_true",
        help="Automatically commit fixes using git",
    )

    args = parser.parse_args()

    if not os.path.exists(args.directory):
        print(f"❌ Directory not found: {args.directory}")
        sys.exit(1)

    repair_tool = IssueSystemRepair(
        directory=args.directory, dry_run=args.dry_run, auto_commit=args.auto_commit
    )

    repair_tool.run_repair()

    if repair_tool.errors:
        sys.exit(1)


if __name__ == "__main__":
    main()
