#!/usr/bin/env python3
# file: scripts/issue_health_check.py
# version: 1.0.0
# guid: a8b9c1d2-e3f4-5678-9abc-def123456789

"""
Issue System Health Check

A lightweight monitoring script that can be run regularly to detect and
prevent issue system problems before they accumulate.

Usage:
    python3 scripts/issue_health_check.py
    python3 scripts/issue_health_check.py --auto-fix
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Dict, Set


def check_issue_system_health(directory: str = ".github/issue-updates") -> Dict[str, any]:
    """Check the health of the issue system and return a status report."""
    results = {
        "status": "healthy",
        "warnings": [],
        "errors": [],
        "stats": {
            "total_files": 0,
            "processed_files": 0,
            "pending_files": 0,
            "malformed_files": 0,
            "duplicate_guids": 0
        }
    }
    
    directory = Path(directory)
    processed_dir = directory / "processed"
    
    if not directory.exists():
        results["errors"].append(f"Issue updates directory does not exist: {directory}")
        results["status"] = "error"
        return results
    
    # Track GUIDs for duplicate detection
    seen_guids: Set[str] = set()
    guid_files: Dict[str, str] = {}
    
    # Check processed files
    if processed_dir.exists():
        for file_path in processed_dir.glob("*.json"):
            results["stats"]["processed_files"] += 1
            try:
                with open(file_path, 'r') as f:
                    data = json.load(f)
                    guid = data.get('guid')
                    if guid:
                        if guid in seen_guids:
                            results["warnings"].append(f"Duplicate GUID in processed: {guid}")
                            results["stats"]["duplicate_guids"] += 1
                        else:
                            seen_guids.add(guid)
                            guid_files[guid] = str(file_path)
            except (json.JSONDecodeError, IOError):
                results["stats"]["malformed_files"] += 1
    
    # Check pending files
    for file_path in directory.glob("*.json"):
        if file_path.name == "processed":
            continue
            
        results["stats"]["pending_files"] += 1
        
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                
                guid = data.get('guid')
                if guid:
                    if guid in seen_guids:
                        results["errors"].append(f"Duplicate GUID found: {guid} in {file_path.name}")
                        results["stats"]["duplicate_guids"] += 1
                        if results["status"] != "error":
                            results["status"] = "warning"
                    else:
                        seen_guids.add(guid)
                        guid_files[guid] = str(file_path)
                
                # Check for invalid issue numbers
                action = data.get('action')
                issue_number = data.get('number')
                if action in ['comment', 'update', 'close'] and (not issue_number or issue_number <= 0):
                    results["warnings"].append(f"Invalid issue number in {file_path.name}: {issue_number}")
                    if results["status"] == "healthy":
                        results["status"] = "warning"
                        
        except json.JSONDecodeError:
            results["errors"].append(f"Malformed JSON: {file_path.name}")
            results["stats"]["malformed_files"] += 1
            results["status"] = "error"
        except IOError as e:
            results["errors"].append(f"Cannot read file {file_path.name}: {e}")
            results["status"] = "error"
    
    results["stats"]["total_files"] = results["stats"]["processed_files"] + results["stats"]["pending_files"]
    
    return results


def print_health_report(results: Dict[str, any]) -> None:
    """Print a formatted health report."""
    status_emoji = {
        "healthy": "✅",
        "warning": "⚠️",
        "error": "❌"
    }
    
    print("\n🏥 Issue System Health Check")
    print(f"Status: {status_emoji.get(results['status'], '❓')} {results['status'].upper()}")
    
    print("\n📊 Statistics:")
    stats = results["stats"]
    print(f"  • Total files: {stats['total_files']}")
    print(f"  • Processed files: {stats['processed_files']}")
    print(f"  • Pending files: {stats['pending_files']}")
    print(f"  • Malformed files: {stats['malformed_files']}")
    print(f"  • Duplicate GUIDs: {stats['duplicate_guids']}")
    
    if results["warnings"]:
        print(f"\n⚠️  Warnings ({len(results['warnings'])}):")
        for warning in results["warnings"]:
            print(f"  • {warning}")
    
    if results["errors"]:
        print(f"\n❌ Errors ({len(results['errors'])}):")
        for error in results["errors"]:
            print(f"  • {error}")
    
    if results["status"] == "healthy":
        print("\n🎉 System is healthy!")
    elif results["status"] == "warning":
        print("\n💡 System has warnings - consider running repair tool")
    else:
        print("\n🚨 System has errors - run repair tool immediately")


def main():
    parser = argparse.ArgumentParser(description='Check issue system health')
    parser.add_argument('--directory', default='.github/issue-updates',
                        help='Directory containing issue update files')
    parser.add_argument('--auto-fix', action='store_true',
                        help='Automatically run repair tool if issues found')
    
    args = parser.parse_args()
    
    results = check_issue_system_health(args.directory)
    print_health_report(results)
    
    # Auto-fix if requested and issues found
    if args.auto_fix and results["status"] != "healthy":
        print("\n🔧 Auto-fix requested - running repair tool...")
        
        import subprocess
        try:
            repair_script = Path(__file__).parent.parent / "issue_system_repair.py"
            if repair_script.exists():
                subprocess.run([sys.executable, str(repair_script), "--auto-commit"], check=True)
                print("✅ Repair completed")
            else:
                print("❌ Repair script not found")
        except subprocess.CalledProcessError as e:
            print(f"❌ Repair failed: {e}")
    
    # Exit with appropriate code
    if results["status"] == "error":
        sys.exit(1)
    elif results["status"] == "warning":
        sys.exit(2)
    else:
        sys.exit(0)


if __name__ == '__main__':
    main()
