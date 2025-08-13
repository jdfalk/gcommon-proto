#!/usr/bin/env python3
# file: improved_issue_manager.py
# version: 1.0.0
# guid: 8f2a3b4c-5d6e-7f8a-9b0c-1d2e3f4a5b6c

"""
Improved Issue Manager with Enhanced Error Handling and Output Formatting

This script addresses the major issues in the current issue management system:
1. Proper duplicate handling with update merging
2. File reading error prevention
3. Clean, formatted output without excessive newlines
4. Comment validation and issue number resolution
5. Comprehensive error handling and recovery

Usage:
    python3 improved_issue_manager.py --directory .github/issue-updates [--dry-run] [--quiet]
"""

import argparse
import json
import os
import sys
import shutil
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Set, Optional, Tuple, Any
import re


class ImprovedIssueManager:
    """Enhanced issue manager with comprehensive error handling and clean output."""

    def __init__(self, directory: str, dry_run: bool = False, quiet: bool = False):
        self.directory = Path(directory)
        self.processed_dir = self.directory / "processed"
        self.duplicates_dir = self.directory / "duplicates"
        self.dry_run = dry_run
        self.quiet = quiet
        
        # Tracking collections
        self.processed_guids: Dict[str, Dict] = {}
        self.unprocessed_files: List[Path] = []
        self.failed_files: List[str] = []
        self.duplicate_files: List[str] = []
        self.updates_created: List[str] = []
        
        # Statistics
        self.stats = {
            'processed': 0,
            'duplicates_moved': 0,
            'updates_created': 0,
            'errors': 0,
            'comments_fixed': 0
        }
        
        # Ensure directories exist
        if not self.dry_run:
            self.processed_dir.mkdir(exist_ok=True)
            self.duplicates_dir.mkdir(exist_ok=True)

    def log(self, message: str, level: str = "info") -> None:
        """Clean logging with proper formatting."""
        if self.quiet and level == "info":
            return
            
        icons = {
            "info": "ℹ️",
            "success": "✅", 
            "warning": "⚠️",
            "error": "❌",
            "processing": "🔄"
        }
        
        icon = icons.get(level, "•")
        print(f"{icon} {message}")

    def load_processed_issues(self) -> None:
        """Load processed issues and map GUIDs to issue numbers."""
        self.log("Loading processed issues...", "processing")
        
        if not self.processed_dir.exists():
            return
            
        processed_count = 0
        for file_path in self.processed_dir.glob("*.json"):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                
                guid = data.get('guid')
                issue_number = data.get('number')
                
                if guid:
                    self.processed_guids[guid] = {
                        'file': str(file_path),
                        'issue_number': issue_number,
                        'data': data
                    }
                    processed_count += 1
                    
            except Exception as e:
                self.log(f"Warning: Could not read processed file {file_path.name}: {e}", "warning")
        
        self.log(f"Loaded {processed_count} processed issues")

    def discover_unprocessed_files(self) -> None:
        """Find all unprocessed JSON files."""
        self.log("Discovering unprocessed files...", "processing")
        
        if not self.directory.exists():
            self.log(f"Directory {self.directory} does not exist", "error")
            return
            
        # Find all JSON files that aren't in subdirectories
        for file_path in self.directory.glob("*.json"):
            if file_path.is_file():
                self.unprocessed_files.append(file_path)
        
        self.log(f"Found {len(self.unprocessed_files)} unprocessed files")

    def validate_and_fix_comment(self, data: Dict) -> Tuple[bool, Optional[int]]:
        """Validate and attempt to fix comment actions with missing issue numbers."""
        if data.get('action') != 'comment':
            return True, data.get('number')
            
        issue_number = data.get('number')
        
        # If number is None or invalid, try to resolve it
        if not issue_number or issue_number <= 0:
            # Try to find issue number from legacy_guid pattern
            legacy_guid = data.get('legacy_guid', '')
            if 'comment-issue-' in legacy_guid:
                # Extract issue number from pattern like "comment-issue-24-2025-08-10"
                match = re.search(r'comment-issue-(\d+)-', legacy_guid)
                if match:
                    resolved_number = int(match.group(1))
                    if resolved_number > 0:
                        data['number'] = resolved_number
                        self.stats['comments_fixed'] += 1
                        self.log(f"Fixed comment issue number: {resolved_number} for GUID {data.get('guid', 'unknown')}")
                        return True, resolved_number
            
            # Handle the case where legacy_guid is "comment-issue--2025-08-10" (double dash)
            if 'comment-issue--' in legacy_guid:
                # This indicates a comment without a specific issue number
                # We can either skip this or mark it for manual review
                self.log(f"Comment without specific issue number (GUID: {data.get('guid', 'unknown')})", "warning")
                # For now, skip this comment as it lacks a target issue
                return False, None
            
            # Cannot resolve issue number
            self.log(f"Cannot resolve issue number for comment GUID {data.get('guid', 'unknown')}", "warning")
            return False, None
            
        return True, issue_number

    def handle_duplicate_guid(self, file_path: Path, data: Dict) -> bool:
        """Handle duplicate GUID by merging data or moving to duplicates folder."""
        guid = data.get('guid')
        existing = self.processed_guids.get(guid)
        
        if not existing:
            return False
            
        self.log(f"Duplicate GUID detected: {guid} (file: {file_path.name})")
        
        # Compare data to see if there are meaningful differences
        existing_data = existing['data']
        
        # Check if the data is essentially the same
        keys_to_compare = ['action', 'title', 'body', 'labels', 'number']
        has_differences = False
        
        for key in keys_to_compare:
            if data.get(key) != existing_data.get(key):
                has_differences = True
                break
        
        if has_differences:
            # Create an update file for the differences
            update_data = {
                'action': 'update',
                'guid': f"{guid}-update-{datetime.now(timezone.utc).strftime('%Y%m%d%H%M%S')}",
                'parent_guid': guid,
                'original_issue_number': existing.get('issue_number'),
                'updates': {},
                'created_at': datetime.now(timezone.utc).isoformat(),
                'reason': 'Duplicate GUID with different content'
            }
            
            # Add differing fields to updates
            for key in keys_to_compare:
                if data.get(key) != existing_data.get(key):
                    update_data['updates'][key] = data.get(key)
            
            # Save update file
            update_filename = f"{update_data['guid']}.json"
            update_path = self.directory / update_filename
            
            if not self.dry_run:
                with open(update_path, 'w', encoding='utf-8') as f:
                    json.dump(update_data, f, indent=2, ensure_ascii=False)
            
            self.updates_created.append(update_filename)
            self.stats['updates_created'] += 1
            self.log(f"Created update file: {update_filename}")
        
        # Move original duplicate to duplicates folder
        dest_path = self.duplicates_dir / file_path.name
        
        # Handle name conflicts
        counter = 1
        while dest_path.exists():
            stem = file_path.stem
            suffix = file_path.suffix
            dest_path = self.duplicates_dir / f"{stem}_dup{counter}{suffix}"
            counter += 1
        
        if not self.dry_run:
            shutil.move(str(file_path), str(dest_path))
        
        self.duplicate_files.append(file_path.name)
        self.stats['duplicates_moved'] += 1
        self.log(f"Moved duplicate to: duplicates/{dest_path.name}")
        
        return True

    def process_file(self, file_path: Path) -> bool:
        """Process a single issue update file."""
        try:
            # Check if file still exists (might have been moved by previous processing)
            if not file_path.exists():
                self.log(f"File no longer exists (already processed): {file_path.name}", "warning")
                return True
                
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
        except FileNotFoundError:
            self.log(f"File not found (likely moved): {file_path.name}", "warning")
            return True
        except json.JSONDecodeError as e:
            self.log(f"Invalid JSON in {file_path.name}: {e}", "error")
            self.failed_files.append(str(file_path))
            self.stats['errors'] += 1
            return False
        except Exception as e:
            self.log(f"Error reading {file_path.name}: {e}", "error")
            self.failed_files.append(str(file_path))
            self.stats['errors'] += 1
            return False
        
        guid = data.get('guid')
        
        # Check for duplicate GUID
        if guid and guid in self.processed_guids:
            return self.handle_duplicate_guid(file_path, data)
        
        # Validate and fix comment actions
        if data.get('action') == 'comment':
            valid, issue_number = self.validate_and_fix_comment(data)
            if not valid:
                self.log(f"Invalid comment action in {file_path.name}", "error")
                self.failed_files.append(str(file_path))
                self.stats['errors'] += 1
                return False
        
        # Move to processed folder
        dest_path = self.processed_dir / file_path.name
        
        # Handle name conflicts
        counter = 1
        while dest_path.exists():
            stem = file_path.stem
            suffix = file_path.suffix
            dest_path = self.processed_dir / f"{stem}_proc{counter}{suffix}"
            counter += 1
        
        if not self.dry_run:
            # Update data if we made changes
            if data.get('action') == 'comment' and self.stats['comments_fixed'] > 0:
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
            
            shutil.move(str(file_path), str(dest_path))
        
        # Track in processed GUIDs
        if guid:
            self.processed_guids[guid] = {
                'file': str(dest_path),
                'issue_number': data.get('number'),
                'data': data
            }
        
        self.stats['processed'] += 1
        return True

    def process_all_files(self) -> bool:
        """Process all unprocessed files."""
        if not self.unprocessed_files:
            self.log("No files to process")
            return True
            
        self.log(f"Processing {len(self.unprocessed_files)} files...", "processing")
        
        success_count = 0
        for file_path in self.unprocessed_files:
            if self.process_file(file_path):
                success_count += 1
        
        self.log(f"Successfully processed {success_count}/{len(self.unprocessed_files)} files", "success")
        return success_count == len(self.unprocessed_files)

    def print_summary(self) -> None:
        """Print a clean summary of operations."""
        self.log("", "info")  # Empty line
        self.log("=== PROCESSING SUMMARY ===", "info")
        self.log(f"Files processed: {self.stats['processed']}", "success")
        self.log(f"Duplicates moved: {self.stats['duplicates_moved']}", "info")
        self.log(f"Update files created: {self.stats['updates_created']}", "info") 
        self.log(f"Comments fixed: {self.stats['comments_fixed']}", "info")
        self.log(f"Errors encountered: {self.stats['errors']}", "error" if self.stats['errors'] > 0 else "info")
        
        if self.duplicate_files:
            self.log("", "info")
            self.log("Duplicate files moved:", "info")
            for filename in self.duplicate_files:
                self.log(f"  • {filename}", "info")
        
        if self.updates_created:
            self.log("", "info")
            self.log("Update files created:", "info")
            for filename in self.updates_created:
                self.log(f"  • {filename}", "info")
        
        if self.failed_files:
            self.log("", "info")
            self.log("Failed files:", "error")
            for filename in self.failed_files:
                self.log(f"  • {filename}", "error")

    def run(self) -> bool:
        """Main execution method."""
        try:
            if self.dry_run:
                self.log("=== DRY RUN MODE ===", "warning")
            
            self.load_processed_issues()
            self.discover_unprocessed_files()
            success = self.process_all_files()
            self.print_summary()
            
            return success
            
        except KeyboardInterrupt:
            self.log("Operation cancelled by user", "warning")
            return False
        except Exception as e:
            self.log(f"Unexpected error: {e}", "error")
            return False


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Improved Issue Manager with Enhanced Error Handling"
    )
    parser.add_argument(
        "--directory",
        default=".github/issue-updates",
        help="Directory containing issue update files"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview operations without making changes"
    )
    parser.add_argument(
        "--quiet",
        action="store_true", 
        help="Reduce output verbosity"
    )
    
    args = parser.parse_args()
    
    manager = ImprovedIssueManager(
        directory=args.directory,
        dry_run=args.dry_run,
        quiet=args.quiet
    )
    
    success = manager.run()
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()