#!/usr/bin/env python3  
# file: unified_issue_automation.py
# version: 1.0.0
# guid: 7a8b9c0d-1e2f-3456-a789-b012c3d4e5f6

"""
Unified Issue Automation Script

This script replaces the problematic workflow calls and provides local automation
for issue management with proper error handling and clean output.

Usage:
    python3 unified_issue_automation.py [--operation OPERATION] [--dry-run] [--quiet]
"""

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Dict, List, Optional
from improved_issue_manager import ImprovedIssueManager


class UnifiedIssueAutomation:
    """Unified automation for issue management operations."""
    
    def __init__(self, dry_run: bool = False, quiet: bool = False):
        self.dry_run = dry_run
        self.quiet = quiet
        self.base_dir = Path.cwd()
        self.issue_updates_dir = self.base_dir / ".github" / "issue-updates"
        self.config_file = self.base_dir / ".github" / "unified-automation-config.json"
        self.config = self.load_config()
        
    def log(self, message: str, level: str = "info") -> None:
        """Clean logging with minimal formatting."""
        if self.quiet and level == "info":
            return
            
        icons = {
            "info": "•",
            "success": "✓", 
            "warning": "!",
            "error": "✗",
            "processing": "→"
        }
        
        icon = icons.get(level, "•")
        print(f"{icon} {message}")

    def load_config(self) -> Dict:
        """Load automation configuration."""
        default_config = {
            "issue_management": {
                "enabled": True,
                "operations": "auto",
                "cleanup_issue_updates": True,
                "force_update": False
            },
            "output": {
                "quiet": False,
                "clean_format": True,
                "max_errors_shown": 5
            }
        }
        
        if self.config_file.exists():
            try:
                with open(self.config_file, 'r') as f:
                    user_config = json.load(f)
                default_config.update(user_config)
            except Exception as e:
                self.log(f"Warning: Could not load config file: {e}", "warning")
        
        return default_config

    def run_issue_management(self) -> bool:
        """Run issue management operations."""
        if not self.config.get("issue_management", {}).get("enabled", True):
            self.log("Issue management disabled in config")
            return True
            
        self.log("Running issue management automation", "processing")
        
        manager = ImprovedIssueManager(
            directory=str(self.issue_updates_dir),
            dry_run=self.dry_run,
            quiet=self.quiet
        )
        
        return manager.run()

    def run_legacy_format_migration(self) -> bool:
        """Handle legacy issue_updates.json file."""
        legacy_file = self.base_dir / "issue_updates.json"
        
        if not legacy_file.exists():
            return True
            
        self.log("Processing legacy issue_updates.json", "processing")
        
        try:
            with open(legacy_file, 'r') as f:
                legacy_updates = json.load(f)
            
            if not isinstance(legacy_updates, list):
                self.log("Legacy file is not a list format", "error")
                return False
            
            # Convert legacy updates to individual files
            migrated_count = 0
            for i, update in enumerate(legacy_updates):
                if not isinstance(update, dict) or 'action' not in update:
                    continue
                    
                # Generate a GUID if missing
                if 'guid' not in update:
                    import uuid
                    update['guid'] = str(uuid.uuid4())
                
                # Create individual file
                filename = f"legacy_{i:03d}_{update['guid']}.json"
                file_path = self.issue_updates_dir / filename
                
                if not self.dry_run:
                    self.issue_updates_dir.mkdir(parents=True, exist_ok=True)
                    with open(file_path, 'w') as f:
                        json.dump(update, f, indent=2, ensure_ascii=False)
                
                migrated_count += 1
            
            self.log(f"Migrated {migrated_count} updates from legacy file", "success")
            
            # Move legacy file to backup
            if not self.dry_run and migrated_count > 0:
                backup_file = self.base_dir / "issue_updates.json.backup"
                legacy_file.rename(backup_file)
                self.log(f"Legacy file backed up to {backup_file.name}")
            
            return True
            
        except Exception as e:
            self.log(f"Error processing legacy file: {e}", "error")
            return False

    def cleanup_empty_directories(self) -> None:
        """Clean up empty directories after processing."""
        if self.dry_run:
            return
            
        for subdir in ["processed", "duplicates"]:
            dir_path = self.issue_updates_dir / subdir
            if dir_path.exists() and not any(dir_path.iterdir()):
                try:
                    dir_path.rmdir()
                    self.log(f"Removed empty directory: {subdir}")
                except OSError:
                    pass

    def generate_status_report(self) -> Dict:
        """Generate a status report of the automation run."""
        report = {
            "timestamp": "2025-08-13T00:44:00Z",
            "dry_run": self.dry_run,
            "directories": {
                "issue_updates": str(self.issue_updates_dir),
                "processed": str(self.issue_updates_dir / "processed"),
                "duplicates": str(self.issue_updates_dir / "duplicates")
            },
            "file_counts": {}
        }
        
        # Count files in each directory
        for name, path_str in report["directories"].items():
            path = Path(path_str)
            if path.exists():
                json_files = list(path.glob("*.json"))
                report["file_counts"][name] = len(json_files)
            else:
                report["file_counts"][name] = 0
        
        return report

    def run(self, operation: str = "all") -> bool:
        """Main execution method."""
        try:
            if self.dry_run:
                self.log("=== DRY RUN MODE - No changes will be made ===", "warning")
            
            self.log(f"Starting unified automation (operation: {operation})", "processing")
            
            success = True
            
            # Handle legacy format migration
            if operation in ["all", "migrate", "issues"]:
                if not self.run_legacy_format_migration():
                    success = False
            
            # Run issue management
            if operation in ["all", "issues"]:
                if not self.run_issue_management():
                    success = False
            
            # Cleanup
            if success and self.config.get("issue_management", {}).get("cleanup_issue_updates", True):
                self.cleanup_empty_directories()
            
            # Generate status report
            if not self.quiet:
                report = self.generate_status_report()
                self.log("", "info")
                self.log("=== AUTOMATION COMPLETE ===", "success" if success else "error")
                self.log(f"Processed files: {report['file_counts'].get('processed', 0)}", "info")
                self.log(f"Duplicate files: {report['file_counts'].get('duplicates', 0)}", "info")
                self.log(f"Remaining files: {report['file_counts'].get('issue_updates', 0)}", "info")
            
            return success
            
        except KeyboardInterrupt:
            self.log("Automation cancelled by user", "warning")
            return False
        except Exception as e:
            self.log(f"Automation failed: {e}", "error")
            return False


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Unified Issue Automation"
    )
    parser.add_argument(
        "--operation",
        choices=["all", "issues", "migrate"],
        default="all",
        help="Operation to perform"
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
    
    automation = UnifiedIssueAutomation(
        dry_run=args.dry_run,
        quiet=args.quiet
    )
    
    success = automation.run(args.operation)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()