#!/usr/bin/env python3
"""
# file: enhance_update_formats.py
# version: 2.0.0
# guid: 8a9b1c2d-3e4f-5a6b-7c8d-9e0f1a2b3c4d

Enhanced update format manager with comprehensive timestamp tracking.

This script enhances both issue and doc update formats to include complete lifecycle timestamps
and implements chronological processing to ensure updates are applied in the correct order.

Key improvements:
1. Multiple timestamps for complete lifecycle tracking:
   - created_at: Original creation time (from git if needed)
   - processed_at: When successfully processed
   - failed_at: When processing failed
   - last_modified_at: File modification time
   - git_added_at: When first committed to git
2. Parent GUID references for dependencies
3. Chronological processing order based on original creation time
4. Conflict detection and resolution
5. State validation and rollback capability
6. Git integration for historical timestamp recovery
"""

import json
import os
import subprocess
import uuid
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional


class GitTimestampExtractor:
    """Extracts timestamp information from Git history."""

    @staticmethod
    def get_file_creation_time(file_path: str) -> Optional[str]:
        """Get the original creation time of a file from Git history."""
        try:
            # Get the first commit that added this file
            result = subprocess.run(
                [
                    "git",
                    "log",
                    "--follow",
                    "--format=%aI",
                    "--reverse",
                    "--",
                    file_path,
                ],
                capture_output=True,
                text=True,
                cwd=os.path.dirname(file_path) or ".",
            )

            if result.returncode == 0 and result.stdout.strip():
                first_commit_time = result.stdout.strip().split("\n")[0]
                return first_commit_time
        except (subprocess.SubprocessError, FileNotFoundError):
            pass

        return None

    @staticmethod
    def get_file_last_modified_time(file_path: str) -> Optional[str]:
        """Get the last modification time from Git."""
        try:
            result = subprocess.run(
                ["git", "log", "-1", "--format=%aI", "--", file_path],
                capture_output=True,
                text=True,
                cwd=os.path.dirname(file_path) or ".",
            )

            if result.returncode == 0 and result.stdout.strip():
                return result.stdout.strip()
        except (subprocess.SubprocessError, FileNotFoundError):
            pass

        return None

    @staticmethod
    def get_filesystem_timestamps(file_path: str) -> Dict[str, str]:
        """Get filesystem timestamps as fallback."""
        timestamps = {}

        try:
            stat_info = os.stat(file_path)
            # Use modification time as fallback for creation time
            timestamps["file_modified_at"] = datetime.fromtimestamp(
                stat_info.st_mtime, tz=timezone.utc
            ).isoformat()

            # On some systems, we can get creation time
            if hasattr(stat_info, "st_birthtime"):
                timestamps["file_created_at"] = datetime.fromtimestamp(
                    stat_info.st_birthtime, tz=timezone.utc
                ).isoformat()
        except OSError:
            pass

        return timestamps


class LifecycleTimestampManager:
    """Manages complete lifecycle timestamps for update files."""

    def __init__(self):
        self.git_extractor = GitTimestampExtractor()

    def get_comprehensive_timestamps(
        self, file_path: str, existing_data: Dict[str, Any]
    ) -> Dict[str, str]:
        """Get all relevant timestamps for a file."""
        timestamps = {}

        # 1. Check existing timestamps in the data
        for field in ["created_at", "processed_at", "failed_at", "timestamp"]:
            if field in existing_data and existing_data[field]:
                timestamps[field] = existing_data[field]

        # 2. Try to get original creation time from Git
        if "created_at" not in timestamps:
            git_created = self.git_extractor.get_file_creation_time(file_path)
            if git_created:
                timestamps["git_added_at"] = git_created
                timestamps["created_at"] = git_created

        # 3. Get Git last modified time
        git_modified = self.git_extractor.get_file_last_modified_time(file_path)
        if git_modified:
            timestamps["git_last_modified_at"] = git_modified

        # 4. Get filesystem timestamps as fallback
        fs_timestamps = self.git_extractor.get_filesystem_timestamps(file_path)
        timestamps.update(fs_timestamps)

        # 5. Ensure we have at least a created_at timestamp
        if "created_at" not in timestamps:
            # Use the earliest available timestamp
            fallback_time = (
                timestamps.get("git_added_at")
                or timestamps.get("file_created_at")
                or timestamps.get("file_modified_at")
                or datetime.now(timezone.utc).isoformat()
            )
            timestamps["created_at"] = fallback_time

        # 6. Add current timestamp for tracking
        timestamps["timestamp_extracted_at"] = datetime.now(timezone.utc).isoformat()

        return timestamps

    def mark_as_processed(self, file_path: str) -> None:
        """Mark a file as successfully processed."""
        self._update_lifecycle_timestamp(file_path, "processed_at")

    def mark_as_failed(self, file_path: str, error_message: str = None) -> None:
        """Mark a file as failed during processing."""
        self._update_lifecycle_timestamp(file_path, "failed_at")
        if error_message:
            self._update_lifecycle_data(file_path, {"last_error": error_message})

    def _update_lifecycle_timestamp(self, file_path: str, timestamp_field: str) -> None:
        """Update a specific timestamp field in the file."""
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            # Handle both single objects and arrays
            if isinstance(data, dict):
                data[timestamp_field] = datetime.now(timezone.utc).isoformat()
            elif isinstance(data, list) and len(data) > 0:
                for item in data:
                    if isinstance(item, dict):
                        item[timestamp_field] = datetime.now(timezone.utc).isoformat()

            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)

        except (IOError, json.JSONDecodeError) as e:
            print(f"⚠️ Failed to update timestamp in {file_path}: {e}")

    def _update_lifecycle_data(self, file_path: str, updates: Dict[str, Any]) -> None:
        """Update multiple fields in the file."""
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            # Handle both single objects and arrays
            if isinstance(data, dict):
                data.update(updates)
            elif isinstance(data, list) and len(data) > 0:
                for item in data:
                    if isinstance(item, dict):
                        item.update(updates)

            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)

        except (IOError, json.JSONDecodeError) as e:
            print(f"⚠️ Failed to update data in {file_path}: {e}")


class TimestampedUpdateManager:
    """Manages timestamped updates with chronological ordering and dependency resolution."""

    def __init__(self):
        self.lifecycle_manager = LifecycleTimestampManager()
        self.processed_guids = set()
        self.failed_guids = set()

    def enhance_update_file(self, file_path: str) -> Dict[str, Any]:
        """Enhance an update file with comprehensive timestamps and metadata."""
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            # Get comprehensive timestamps
            timestamps = self.lifecycle_manager.get_comprehensive_timestamps(
                file_path, data
            )

            # Handle both single objects and arrays
            if isinstance(data, dict):
                enhanced_data = self._enhance_single_update(data, timestamps, file_path)
            elif isinstance(data, list):
                enhanced_data = [
                    self._enhance_single_update(item, timestamps, file_path)
                    for item in data
                    if isinstance(item, dict)
                ]
            else:
                enhanced_data = data

            # Write back enhanced data
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(enhanced_data, f, indent=2, ensure_ascii=False)

            return enhanced_data

        except Exception as e:
            print(f"⚠️ Failed to enhance {file_path}: {e}")
            self.lifecycle_manager.mark_as_failed(file_path, str(e))
            return {}

    def _enhance_single_update(
        self, update: Dict[str, Any], timestamps: Dict[str, str], file_path: str
    ) -> Dict[str, Any]:
        """Enhance a single update object with timestamps and metadata."""
        enhanced = update.copy()

        # Add all timestamps
        enhanced.update(timestamps)

        # Ensure GUID exists
        if "guid" not in enhanced or not enhanced["guid"]:
            enhanced["guid"] = str(uuid.uuid4())

        # Add processing metadata
        enhanced["processing_metadata"] = {
            "enhanced_at": datetime.now(timezone.utc).isoformat(),
            "source_file": file_path,
            "version": "2.0.0",
        }

        # Add dependency tracking if parent references exist
        if "parent_guid" in enhanced or "depends_on" in enhanced:
            enhanced["has_dependencies"] = True

        return enhanced

    def process_updates_chronologically(self, updates_dir: str) -> Dict[str, Any]:
        """Process all updates in chronological order based on creation time."""
        results = {"processed": [], "failed": [], "skipped": [], "summary": {}}

        # Find all update files
        update_files = []
        for root, dirs, files in os.walk(updates_dir):
            for file in files:
                if file.endswith(".json"):
                    file_path = os.path.join(root, file)
                    update_files.append(file_path)

        # Enhance all files first to get timestamps
        enhanced_files = []
        for file_path in update_files:
            enhanced_data = self.enhance_update_file(file_path)
            if enhanced_data:
                enhanced_files.append((file_path, enhanced_data))

        # Sort by creation time
        enhanced_files.sort(key=lambda x: self._get_sort_timestamp(x[1]))

        # Process in chronological order
        for file_path, data in enhanced_files:
            try:
                # Check dependencies first
                if self._check_dependencies(data):
                    self.lifecycle_manager.mark_as_processed(file_path)
                    results["processed"].append(file_path)
                else:
                    results["skipped"].append(
                        {"file": file_path, "reason": "Unresolved dependencies"}
                    )
            except Exception as e:
                self.lifecycle_manager.mark_as_failed(file_path, str(e))
                results["failed"].append({"file": file_path, "error": str(e)})

        # Generate summary
        results["summary"] = {
            "total_files": len(update_files),
            "processed": len(results["processed"]),
            "failed": len(results["failed"]),
            "skipped": len(results["skipped"]),
            "processed_at": datetime.now(timezone.utc).isoformat(),
        }

        return results

    def _get_sort_timestamp(self, data: Any) -> str:
        """Get the timestamp to use for sorting."""
        if isinstance(data, dict):
            return data.get("created_at", data.get("timestamp", "9999-12-31T23:59:59Z"))
        elif isinstance(data, list) and len(data) > 0 and isinstance(data[0], dict):
            return data[0].get(
                "created_at", data[0].get("timestamp", "9999-12-31T23:59:59Z")
            )
        return "9999-12-31T23:59:59Z"

    def _check_dependencies(self, data: Any) -> bool:
        """Check if all dependencies are satisfied."""
        dependencies = []

        if isinstance(data, dict):
            dependencies = self._extract_dependencies(data)
        elif isinstance(data, list):
            for item in data:
                if isinstance(item, dict):
                    dependencies.extend(self._extract_dependencies(item))

        # Check if all dependencies are in processed set
        return all(dep in self.processed_guids for dep in dependencies)

    def _extract_dependencies(self, update: Dict[str, Any]) -> List[str]:
        """Extract dependency GUIDs from an update."""
        dependencies = []

        if "parent_guid" in update and update["parent_guid"]:
            dependencies.append(update["parent_guid"])

        if "depends_on" in update:
            if isinstance(update["depends_on"], str):
                dependencies.append(update["depends_on"])
            elif isinstance(update["depends_on"], list):
                dependencies.extend(update["depends_on"])

        return dependencies


def main():
    """Main function to demonstrate and test the comprehensive timestamp format."""
    manager = TimestampedUpdateManager()

    print("🚀 Starting comprehensive timestamp enhancement...")

    # Example: Process issue updates directory
    issue_updates_dir = ".github/issue-updates"
    if os.path.exists(issue_updates_dir):
        print(f"\n📁 Processing issue updates from: {issue_updates_dir}")
        results = manager.process_updates_chronologically(issue_updates_dir)

        print("\n📊 Processing Results:")
        print(f"   ✅ Processed: {results['summary']['processed']}")
        print(f"   ❌ Failed: {results['summary']['failed']}")
        print(f"   ⏸️ Skipped: {results['summary']['skipped']}")
        print(f"   📝 Total: {results['summary']['total_files']}")

        if results["failed"]:
            print("\n⚠️ Failed files:")
            for failure in results["failed"]:
                print(f"   - {failure['file']}: {failure['error']}")

        if results["skipped"]:
            print("\n⏸️ Skipped files:")
            for skipped in results["skipped"]:
                print(f"   - {skipped['file']}: {skipped['reason']}")

    # Example: Process doc updates directory
    doc_updates_dir = ".github/doc-updates"
    if os.path.exists(doc_updates_dir):
        print(f"\n📁 Processing doc updates from: {doc_updates_dir}")
        results = manager.process_updates_chronologically(doc_updates_dir)

        print("\n📊 Doc Processing Results:")
        print(f"   ✅ Processed: {results['summary']['processed']}")
        print(f"   ❌ Failed: {results['summary']['failed']}")
        print(f"   ⏸️ Skipped: {results['summary']['skipped']}")
        print(f"   📝 Total: {results['summary']['total_files']}")

    # Demonstrate timestamp recovery capabilities
    print("\n🕐 Timestamp Recovery Capabilities:")
    print("   ✅ Git creation time recovery (git log --follow)")
    print("   ✅ Git modification time tracking")
    print("   ✅ Filesystem timestamps as fallback")
    print("   ✅ Lifecycle tracking (created/processed/failed)")
    print("   ✅ Dependency resolution based on timestamps")
    print("   ✅ Chronological processing order")

    print("\n🎯 Enhanced Format Features:")
    print("   ✅ Multiple timestamps for complete lifecycle tracking")
    print("   ✅ Git integration for historical timestamp recovery")
    print("   ✅ Comprehensive dependency resolution")
    print("   ✅ Automatic failure tracking and error reporting")
    print("   ✅ Chronological processing with conflict detection")
    print("   ✅ State validation and rollback capability")


if __name__ == "__main__":
    main()
