#!/usr/bin/env python3
# file: test_issue_scenarios.py  
# version: 1.0.0
# guid: 9e1a2b3c-4d5e-6f7a-8b9c-0d1e2f3a4b5c

"""
Test script to simulate the specific error scenarios mentioned in the problem statement.
"""

import json
import os
import tempfile
import shutil
from pathlib import Path
from improved_issue_manager import ImprovedIssueManager


def create_test_scenario():
    """Create test files that simulate the error scenarios."""
    
    # Create temporary test directory
    test_dir = Path("test_issue_updates")
    test_dir.mkdir(exist_ok=True)
    
    processed_dir = test_dir / "processed"
    processed_dir.mkdir(exist_ok=True)
    
    # 1. Create a comment with null issue number (like the one mentioned)
    comment_with_null = {
        "action": "comment",
        "number": None,
        "body": "Implemented comprehensive error handling framework across modules",
        "guid": "72e0dae2-572f-4485-9329-1b29cb3443c6",
        "legacy_guid": "comment-issue--2025-08-10",
        "created_at": "2025-08-10T12:39:32.000Z",
        "processed_at": None,
        "failed_at": None,
        "sequence": 0,
        "parent_guid": None
    }
    
    # 2. Create a comment with proper issue number pattern  
    comment_with_issue = {
        "action": "comment",
        "number": None,
        "body": "Expand configuration management system",
        "guid": "3365e651-1c02-44a4-aeb7-e28905915e25",
        "legacy_guid": "comment-issue-24-2025-08-10",
        "created_at": "2025-08-10T14:40:36.000Z",
        "processed_at": None,
        "failed_at": None,
        "sequence": 0,
        "parent_guid": None
    }
    
    # 3. Create a duplicate GUID that already exists in processed
    duplicate_issue = {
        "action": "create",
        "title": "Plugin system framework",
        "body": "Implement plugin management skeleton",
        "labels": ["module:plugins", "enhancement"],
        "guid": "81c59d05-0167-40c8-8da2-fa28093f4e35",
        "legacy_guid": "create-plugin-system-framework-2025-08-10",
        "created_at": "2025-08-10T02:55:40.000Z",
        "processed_at": None,
        "failed_at": None,
        "sequence": 0,
        "parent_guid": None
    }
    
    # 4. Create the processed version of the duplicate
    processed_duplicate = {
        "action": "create",
        "title": "Plugin system framework",
        "body": "Implement plugin management skeleton - DIFFERENT CONTENT",
        "labels": ["module:plugins", "enhancement", "priority:high"],
        "guid": "81c59d05-0167-40c8-8da2-fa28093f4e35",
        "legacy_guid": "create-plugin-system-framework-2025-08-10",
        "created_at": "2025-08-10T02:55:40.000Z",
        "processed_at": "2025-08-10T02:56:00.000Z",
        "failed_at": None,
        "sequence": 0,
        "parent_guid": None,
        "number": 994
    }
    
    # Write test files
    with open(test_dir / "72e0dae2-572f-4485-9329-1b29cb3443c6.json", "w") as f:
        json.dump(comment_with_null, f, indent=2)
    
    with open(test_dir / "3365e651-1c02-44a4-aeb7-e28905915e25.json", "w") as f:
        json.dump(comment_with_issue, f, indent=2)
        
    with open(test_dir / "81c59d05-0167-40c8-8da2-fa28093f4e35.json", "w") as f:
        json.dump(duplicate_issue, f, indent=2)
        
    with open(processed_dir / "81c59d05-0167-40c8-8da2-fa28093f4e35.json", "w") as f:
        json.dump(processed_duplicate, f, indent=2)
    
    # 5. Create a file that simulates being deleted mid-process
    missing_file = {
        "action": "create",
        "title": "Test missing file",
        "body": "This file will be missing",
        "guid": "e084deb8-0131-4662-8af2-f7cdeff38022"
    }
    
    with open(test_dir / "e084deb8-0131-4662-8af2-f7cdeff38022.json", "w") as f:
        json.dump(missing_file, f, indent=2)
    
    return test_dir


def simulate_old_behavior():
    """Simulate the old verbose error output."""
    print("🔥 === OLD BEHAVIOR SIMULATION ===")
    print()
    print("📝 Operation Output (stdout)")
    print() 
    print("\\n```\\n")
    print("⚠️ Using legacy flat format. Consider upgrading to grouped format.")
    print("📄 Loaded 4 NEW updates from legacy file: issue_updates.json")
    print("📁 Loaded 95 updates from 95 files in: .github/issue-updates")
    print("🚀 Processing 99 total updates...")
    print()
    print("📋 Update 1/99: create (from issue_updates.json, guid: no-guid)")
    print("🔍 Found duplicate title in issue #212: Queue: implement publish and offset protos")
    print("🚫 Duplicate title detected for issue: Queue: implement publish and offset protos")
    print("❌ Failed to process update 1")
    print()
    print("📋 Update 2/99: create (from issue_updates.json, guid: no-guid)")
    print("🔍 Found duplicate title in issue #213: Implement audit logging protobufs")
    print("🚫 Duplicate title detected for issue: Implement audit logging protobufs")
    print("❌ Failed to process update 2")
    print()
    print("Failed to read file .github/issue-updates/e084deb8-0131-4662-8af2-f7cdeff38022.json: [Errno 2] No such file or directory")
    print("No issue number found for comment: {'action': 'comment', 'number': None, 'body': 'Implemented comprehensive error handling framework across modules', 'guid': '72e0dae2-572f-4485-9329-1b29cb3443c6'}")
    print("Failed to read file .github/issue-updates/3365e651-1c02-44a4-aeb7-e28905915e25.json: [Errno 2] No such file or directory")
    print("Duplicate GUID found: 81c59d05-0167-40c8-8da2-fa28093f4e35 already exists in issue #994")
    print()


def test_improved_behavior():
    """Test the improved behavior."""
    print("✨ === IMPROVED BEHAVIOR ===")
    print()
    
    test_dir = create_test_scenario()
    
    try:
        # First, delete one file to simulate the missing file error
        missing_file = test_dir / "e084deb8-0131-4662-8af2-f7cdeff38022.json"
        if missing_file.exists():
            missing_file.unlink()
        
        # Run the improved manager
        manager = ImprovedIssueManager(str(test_dir), dry_run=True, quiet=False)
        manager.run()
        
    finally:
        # Cleanup
        if test_dir.exists():
            shutil.rmtree(test_dir)


if __name__ == "__main__":
    simulate_old_behavior()
    print("\n" + "="*60 + "\n")
    test_improved_behavior()