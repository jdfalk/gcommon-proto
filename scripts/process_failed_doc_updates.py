#!/usr/bin/env python3
# file: process_failed_doc_updates.py
# version: 1.0.0
# guid: 5a6b7c8d-9e0f-1a2b-3c4d-5e6f7a8b9c0d

"""
Script to process all failed doc-upd            elif mode == 'task-add':
                # Add task to TODO section or end of file
                task_line = f"- [ ] {content}"
                if '## TODO' in current_content or '# TODO' in current_content:
                    # Find TODO section and add task
                    todo_pattern = r'(## TODO.*?(?=## |\Z))'
                    if re.search(todo_pattern, current_content, re.DOTALL):
                        new_content = re.sub(
                            todo_pattern,
                            lambda m: m.group(1).rstrip() + f'\n{task_line}\n\n',
                            current_content,
                            flags=re.DOTALL
                        )
                    else:
                        new_content = current_content.rstrip() + f'\n\n{task_line}\n'
                else:
                    # No TODO section, create one
                    new_content = current_content.rstrip() + f'\n\n## TODO\n\n{task_line}\n'

            elif mode == 'task-complete':
                # Mark a task as complete by changing [ ] to [x]
                task_pattern = rf'- \[ \] {re.escape(content)}'
                completed_task = f'- [x] {content}'
                if re.search(task_pattern, current_content):
                    new_content = re.sub(task_pattern, completed_task, current_content)
                else:
                    # Task not found, add as completed task
                    new_content = current_content.rstrip() + f'\n\n{completed_task}\n'

            elif mode == 'changelog-feature':
                # Add feature to changelog
                changelog_entry = f"- **Feature**: {content}"
                if '## Changelog' in current_content or '# Changelog' in current_content:
                    # Find changelog section and add entry
                    changelog_pattern = r'(## Changelog.*?(?=## |\Z))'
                    if re.search(changelog_pattern, current_content, re.DOTALL):
                        new_content = re.sub(
                            changelog_pattern,
                            lambda m: m.group(1).rstrip() + f'\n{changelog_entry}\n\n',
                            current_content,
                            flags=re.DOTALL
                        )
                    else:
                        new_content = current_content.rstrip() + f'\n\n{changelog_entry}\n'
                else:
                    # No changelog section, create one
                    new_content = current_content.rstrip() + f'\n\n## Changelog\n\n{changelog_entry}\n'

            elif mode in ['insert-after', 'insert-before']:
                # Insert content before or after a specific line/pattern
                after_text = options.get('after', '')
                before_text = options.get('before', '')

                if mode == 'insert-after' and after_text:
                    pattern = re.escape(after_text)
                    replacement = f"{after_text}\n{content}"
                    new_content = re.sub(pattern, replacement, current_content, count=1)
                elif mode == 'insert-before' and before_text:
                    pattern = re.escape(before_text)
                    replacement = f"{content}\n{before_text}"
                    new_content = re.sub(pattern, replacement, current_content, count=1)
                else:
                    # Fallback to append if no specific text provided
                    new_content = current_content.rstrip() + '\n\n' + content + '\n'm successfully.

This script:
1. Finds all failed doc-update files in both repositories
2. Reads and validates each failed update
3. Fixes common issues (missing sections, malformed modes, etc.)
4. Applies the updates to the target files
5. Moves successfully processed files to processed directory
"""

import json
import os
import re
from datetime import datetime
from typing import Any, Dict, List, Optional


class FailedDocUpdateProcessor:
    """Processes failed doc-update files and applies them successfully."""

    def __init__(self):
        self.processed_count = 0
        self.failed_count = 0
        self.results = []

    def find_failed_updates(self, repo_path: str) -> List[str]:
        """Find all failed doc-update JSON files in a repository."""
        failed_dir = os.path.join(repo_path, ".github", "doc-updates", "failed")
        failed_files = []

        if os.path.exists(failed_dir):
            for file in os.listdir(failed_dir):
                if file.endswith(".json"):
                    failed_files.append(os.path.join(failed_dir, file))

        return sorted(failed_files)

    def read_update_file(self, file_path: str) -> Optional[Dict[str, Any]]:
        """Read and parse a doc-update file."""
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"❌ Failed to read {file_path}: {e}")
            return None

    def read_error_file(self, update_file_path: str) -> Optional[str]:
        """Read the corresponding error file if it exists."""
        error_file_path = update_file_path.replace(".json", "_error.txt")
        if os.path.exists(error_file_path):
            try:
                with open(error_file_path, "r", encoding="utf-8") as f:
                    return f.read().strip()
            except Exception:
                pass
        return None

    def fix_update_data(
        self, update_data: Dict[str, Any], error_msg: Optional[str] = None
    ) -> Dict[str, Any]:
        """Fix common issues in update data."""
        fixed_data = update_data.copy()

        # Fix mode issues
        if "mode" in fixed_data:
            mode = fixed_data["mode"]

            # Fix "after" mode to "append"
            if mode == "after":
                fixed_data["mode"] = "append"
                print(f"   🔧 Fixed mode: 'after' → 'append'")

            # Fix replace-section without section
            elif mode == "replace-section":
                if not fixed_data.get("options", {}).get("section"):
                    # Try to detect section from content
                    content = fixed_data.get("content", "")
                    if "Progress" in content or "progress" in content:
                        fixed_data["options"]["section"] = "Progress"
                        print(f"   🔧 Added missing section: 'Progress'")
                    elif "TODO" in content or "Task" in content:
                        fixed_data["options"]["section"] = "TODO"
                        print(f"   🔧 Added missing section: 'TODO'")
                    elif "Implementation" in content:
                        fixed_data["options"]["section"] = "Implementation Status"
                        print(f"   🔧 Added missing section: 'Implementation Status'")
                    else:
                        # Fall back to append mode
                        fixed_data["mode"] = "append"
                        print(
                            f"   🔧 Changed mode: 'replace-section' → 'append' (no section found)"
                        )

        # Ensure options exists
        if "options" not in fixed_data:
            fixed_data["options"] = {}

        # Fix null options fields
        for field in [
            "section",
            "after",
            "before",
            "task_id",
            "badge_name",
            "priority",
            "category",
        ]:
            if field not in fixed_data["options"]:
                fixed_data["options"][field] = None

        return fixed_data

    def apply_doc_update(self, repo_path: str, update_data: Dict[str, Any]) -> bool:
        """Apply a doc-update to the target file."""
        try:
            target_file = os.path.join(repo_path, update_data["file"])

            if not os.path.exists(target_file):
                print(f"   ⚠️ Target file does not exist: {update_data['file']}")
                return False

            # Read current content
            with open(target_file, "r", encoding="utf-8") as f:
                current_content = f.read()

            mode = update_data["mode"]
            content = update_data["content"]
            options = update_data.get("options", {})

            # Apply the update based on mode
            if mode == "append":
                new_content = current_content.rstrip() + "\n\n" + content + "\n"

            elif mode == "prepend":
                new_content = content + "\n\n" + current_content

            elif mode == "replace-section":
                section = options.get("section")
                if section:
                    # Find and replace the section
                    section_pattern = rf"## {re.escape(section)}.*?(?=## |\Z)"
                    if re.search(section_pattern, current_content, re.DOTALL):
                        new_content = re.sub(
                            section_pattern,
                            f"## {section}\n\n{content}\n\n",
                            current_content,
                            flags=re.DOTALL,
                        )
                    else:
                        # Section not found, append instead
                        new_content = (
                            current_content.rstrip()
                            + f"\n\n## {section}\n\n{content}\n"
                        )
                else:
                    # No section specified, append
                    new_content = current_content.rstrip() + "\n\n" + content + "\n"

            elif mode == "task-add":
                # Add task to TODO section or end of file
                task_line = f"- [ ] {content}"
                if "## TODO" in current_content or "# TODO" in current_content:
                    # Find TODO section and add task
                    todo_pattern = r"(## TODO.*?(?=## |\Z))"
                    if re.search(todo_pattern, current_content, re.DOTALL):
                        new_content = re.sub(
                            todo_pattern,
                            lambda m: m.group(1).rstrip() + f"\n{task_line}\n\n",
                            current_content,
                            flags=re.DOTALL,
                        )
                    else:
                        new_content = current_content.rstrip() + f"\n\n{task_line}\n"
                else:
                    # No TODO section, create one
                    new_content = (
                        current_content.rstrip() + f"\n\n## TODO\n\n{task_line}\n"
                    )

            elif mode == "task-complete":
                # Mark a task as complete by changing [ ] to [x]
                task_pattern = rf"- \[ \] {re.escape(content)}"
                completed_task = f"- [x] {content}"
                if re.search(task_pattern, current_content):
                    new_content = re.sub(task_pattern, completed_task, current_content)
                else:
                    # Task not found, add as completed task
                    new_content = current_content.rstrip() + f"\n\n{completed_task}\n"

            elif mode == "changelog-feature":
                # Add feature to changelog
                changelog_entry = f"- **Feature**: {content}"
                if (
                    "## Changelog" in current_content
                    or "# Changelog" in current_content
                ):
                    # Find changelog section and add entry
                    changelog_pattern = r"(## Changelog.*?(?=## |\Z))"
                    if re.search(changelog_pattern, current_content, re.DOTALL):
                        new_content = re.sub(
                            changelog_pattern,
                            lambda m: m.group(1).rstrip() + f"\n{changelog_entry}\n\n",
                            current_content,
                            flags=re.DOTALL,
                        )
                    else:
                        new_content = (
                            current_content.rstrip() + f"\n\n{changelog_entry}\n"
                        )
                else:
                    # No changelog section, create one
                    new_content = (
                        current_content.rstrip()
                        + f"\n\n## Changelog\n\n{changelog_entry}\n"
                    )

            elif mode in ["insert-after", "insert-before"]:
                # Insert content before or after a specific line/pattern
                after_text = options.get("after", "")
                before_text = options.get("before", "")

                if mode == "insert-after" and after_text:
                    pattern = re.escape(after_text)
                    replacement = f"{after_text}\n{content}"
                    new_content = re.sub(pattern, replacement, current_content, count=1)
                elif mode == "insert-before" and before_text:
                    pattern = re.escape(before_text)
                    replacement = f"{content}\n{before_text}"
                    new_content = re.sub(pattern, replacement, current_content, count=1)
                else:
                    # Fallback to append if no specific text provided
                    new_content = current_content.rstrip() + "\n\n" + content + "\n"

            else:
                print(f"   ⚠️ Unknown mode: {mode}")
                return False

            # Write the updated content
            with open(target_file, "w", encoding="utf-8") as f:
                f.write(new_content)

            print(f"   ✅ Applied {mode} update to {update_data['file']}")
            return True

        except Exception as e:
            print(f"   ❌ Failed to apply update: {e}")
            return False

    def move_to_processed(self, failed_file_path: str, repo_path: str) -> None:
        """Move successfully processed file to processed directory."""
        try:
            processed_dir = os.path.join(
                repo_path, ".github", "doc-updates", "processed"
            )
            os.makedirs(processed_dir, exist_ok=True)

            filename = os.path.basename(failed_file_path)
            processed_path = os.path.join(processed_dir, filename)

            # Move the JSON file
            os.rename(failed_file_path, processed_path)

            # Move the error file if it exists
            error_file = failed_file_path.replace(".json", "_error.txt")
            if os.path.exists(error_file):
                error_processed_path = os.path.join(
                    processed_dir, filename.replace(".json", "_error.txt")
                )
                os.rename(error_file, error_processed_path)

            print(f"   📁 Moved to processed: {filename}")

        except Exception as e:
            print(f"   ⚠️ Failed to move file: {e}")

    def process_failed_file(self, file_path: str, repo_path: str) -> bool:
        """Process a single failed doc-update file."""
        print(f"\n📄 Processing: {os.path.basename(file_path)}")

        # Read the update data
        update_data = self.read_update_file(file_path)
        if not update_data:
            return False

        # Read error message for context
        error_msg = self.read_error_file(file_path)
        if error_msg:
            print(f"   📋 Original error: {error_msg[:100]}...")

        # Fix common issues
        fixed_data = self.fix_update_data(update_data, error_msg)

        # Apply the update
        success = self.apply_doc_update(repo_path, fixed_data)

        if success:
            # Move to processed
            self.move_to_processed(file_path, repo_path)
            self.processed_count += 1

            # Record result
            self.results.append(
                {
                    "file": os.path.basename(file_path),
                    "status": "success",
                    "target": fixed_data["file"],
                    "mode": fixed_data["mode"],
                    "repo": os.path.basename(repo_path),
                }
            )

            return True
        else:
            self.failed_count += 1
            self.results.append(
                {
                    "file": os.path.basename(file_path),
                    "status": "failed",
                    "target": fixed_data.get("file", "unknown"),
                    "mode": fixed_data.get("mode", "unknown"),
                    "repo": os.path.basename(repo_path),
                }
            )
            return False

    def process_all_repos(self, repo_paths: List[str]) -> None:
        """Process failed doc-updates in all specified repositories."""
        print("🚀 Processing All Failed Doc-Updates")
        print("=" * 50)

        for repo_path in repo_paths:
            repo_name = os.path.basename(repo_path)
            print(f"\n📁 Repository: {repo_name}")

            failed_files = self.find_failed_updates(repo_path)
            if not failed_files:
                print(f"   ✅ No failed files found")
                continue

            print(f"   📊 Found {len(failed_files)} failed files")

            for file_path in failed_files:
                self.process_failed_file(file_path, repo_path)

        # Print summary
        self.print_summary()

    def print_summary(self) -> None:
        """Print processing summary."""
        print(f"\n" + "=" * 50)
        print(f"📊 PROCESSING SUMMARY")
        print(f"=" * 50)
        print(f"✅ Successfully processed: {self.processed_count}")
        print(f"❌ Failed to process: {self.failed_count}")
        print(f"📝 Total files: {self.processed_count + self.failed_count}")

        if self.results:
            print(f"\n📋 Results by Repository:")

            repos = {}
            for result in self.results:
                repo = result["repo"]
                if repo not in repos:
                    repos[repo] = {"success": 0, "failed": 0}
                repos[repo][result["status"]] += 1

            for repo, counts in repos.items():
                total = counts["success"] + counts["failed"]
                success_rate = (counts["success"] / total * 100) if total > 0 else 0
                print(
                    f"   {repo}: {counts['success']}/{total} ({success_rate:.1f}% success)"
                )


def main():
    """Main function to process all failed doc-updates."""
    processor = FailedDocUpdateProcessor()

    # Define repository paths
    repo_paths = [
        "/Users/jdfalk/repos/github.com/jdfalk/gcommon",
        "/Users/jdfalk/repos/github.com/jdfalk/subtitle-manager",
    ]

    # Process all repositories
    processor.process_all_repos(repo_paths)

    print(f"\n🎉 Processing complete!")
    print(f"All failed doc-updates have been processed and applied.")


if __name__ == "__main__":
    main()
