<!-- file: tasks/REORG/07-rollback-strategy.md -->
<!-- version: 1.0.0 -->
<!-- guid: 0b1c2d3e-4f5a-6b7c-8d9e-0f1a2b3c4d5e -->

# Section 07: Rollback Strategy

## 07.1 Pre-Migration Backups

### 07.1.1 Git-Based Backup Strategy

**Implementation:** Create dedicated backup branches before any migration

```bash
#!/bin/bash
# file: scripts/create-backup.sh
# version: 1.0.0
# guid: 1c2d3e4f-5a6b-7c8d-9e0f-1a2b3c4d5e6f

# Create backup branch with timestamp
BACKUP_BRANCH="proto-reorg-backup-$(date +%Y%m%d_%H%M%S)"

# Create and push backup branch
git checkout -b "$BACKUP_BRANCH"
git push origin "$BACKUP_BRANCH"

# Return to original branch
git checkout -

echo "Backup created: $BACKUP_BRANCH"
```

### 07.1.2 File System Backup

**Implementation:** Create compressed backup of entire repository

```bash
#!/bin/bash
# file: scripts/create-filesystem-backup.sh
# version: 1.0.0
# guid: 2d3e4f5a-6b7c-8d9e-0f1a-2b3c4d5e6f7a

BACKUP_NAME="gcommon-backup-$(date +%Y%m%d_%H%M%S).tar.gz"

# Create comprehensive backup
tar -czf "$BACKUP_NAME" \
    --exclude='.git' \
    --exclude='node_modules' \
    --exclude='target' \
    --exclude='dist' \
    --exclude='*.log' \
    --exclude='logs' \
    .

# Move to backup directory
mkdir -p ~/backups
mv "$BACKUP_NAME" ~/backups/

echo "Filesystem backup created: ~/backups/$BACKUP_NAME"
```

## 07.2 Rollback Procedures

### 07.2.1 Quick Rollback (Configuration Only)

**File:** `scripts/quick-rollback.sh`

```bash
#!/bin/bash
# file: scripts/quick-rollback.sh
# version: 1.0.0
# guid: 3e4f5a6b-7c8d-9e0f-1a2b-3c4d5e6f7a8b

set -euo pipefail

echo "🔄 Executing quick rollback..."

# Restore buf configuration files
if [ -f "buf.yaml.backup" ]; then
    mv buf.yaml.backup buf.yaml
    echo "✅ Restored buf.yaml"
else
    echo "⚠️  buf.yaml.backup not found"
fi

if [ -f "buf.gen.yaml.backup" ]; then
    mv buf.gen.yaml.backup buf.gen.yaml
    echo "✅ Restored buf.gen.yaml"
else
    echo "⚠️  buf.gen.yaml.backup not found"
fi

# Remove proto directory if it exists
if [ -d "proto" ]; then
    rm -rf proto
    echo "✅ Removed proto directory"
fi

# Clean generated files in new locations
if [ -d "pkg" ]; then
    find pkg -name "*.pb.go" -type f -delete 2>/dev/null || true
    find pkg -name "*_grpc.pb.go" -type f -delete 2>/dev/null || true
    echo "✅ Cleaned generated files"
fi

echo "🎉 Quick rollback completed"
```

### 07.2.2 Full Rollback (Git Reset)

**File:** `scripts/full-rollback.sh`

```bash
#!/bin/bash
# file: scripts/full-rollback.sh
# version: 1.0.0
# guid: 4f5a6b7c-8d9e-0f1a-2b3c-4d5e6f7a8b9c

set -euo pipefail

echo "🔄 Executing full rollback..."

# Find the most recent backup branch
BACKUP_BRANCH=$(git branch -r | grep "origin/proto-reorg-backup-" | sort -r | head -1 | sed 's/.*origin\///')

if [ -z "$BACKUP_BRANCH" ]; then
    echo "❌ No backup branch found"
    exit 1
fi

echo "📂 Found backup branch: $BACKUP_BRANCH"

# Confirm with user
read -p "This will reset all changes to $BACKUP_BRANCH. Continue? (y/N): " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "❌ Rollback cancelled"
    exit 1
fi

# Stash any uncommitted changes
git stash push -m "Pre-rollback stash $(date)"

# Reset to backup branch
git fetch origin "$BACKUP_BRANCH"
git reset --hard "origin/$BACKUP_BRANCH"

echo "🎉 Full rollback completed to $BACKUP_BRANCH"
```

### 07.2.3 Selective Rollback

**File:** `scripts/selective-rollback.py`

```python
#!/usr/bin/env python3
# file: scripts/selective-rollback.py
# version: 1.0.0
# guid: 5a6b7c8d-9e0f-1a2b-3c4d-5e6f7a8b9c0d

"""
Selective rollback for specific domains or files.
"""

import os
import sys
import argparse
import subprocess
from pathlib import Path

def rollback_domain(domain):
    """Rollback a specific domain."""
    print(f"🔄 Rolling back {domain} domain...")
    
    # Remove proto files for this domain
    proto_domain_dir = Path(f"proto/gcommon/v1/{domain}")
    if proto_domain_dir.exists():
        shutil.rmtree(proto_domain_dir)
        print(f"✅ Removed {proto_domain_dir}")
    
    # Remove generated files for this domain
    pkg_domain_dir = Path(f"pkg/{domain}")
    if pkg_domain_dir.exists():
        for pb_file in pkg_domain_dir.rglob("*.pb.go"):
            pb_file.unlink()
        for grpc_file in pkg_domain_dir.rglob("*_grpc.pb.go"):
            grpc_file.unlink()
        print(f"✅ Cleaned generated files in {pkg_domain_dir}")
    
    print(f"🎉 {domain} domain rollback completed")

def rollback_file(file_path):
    """Rollback a specific file."""
    print(f"🔄 Rolling back file: {file_path}")
    
    # Check if file exists in proto structure
    proto_file = Path(file_path)
    if proto_file.exists() and proto_file.is_relative_to(Path("proto")):
        proto_file.unlink()
        print(f"✅ Removed {proto_file}")
    
    # Remove corresponding generated files
    if file_path.endswith(".proto"):
        base_name = Path(file_path).stem
        for pb_file in Path("pkg").rglob(f"{base_name}.pb.go"):
            pb_file.unlink()
        for grpc_file in Path("pkg").rglob(f"{base_name}_grpc.pb.go"):
            grpc_file.unlink()
    
    print(f"🎉 File rollback completed: {file_path}")

def main():
    parser = argparse.ArgumentParser(description='Selective rollback tool')
    parser.add_argument('--domain', help='Domain to rollback')
    parser.add_argument('--file', help='Specific file to rollback')
    
    args = parser.parse_args()
    
    if args.domain:
        rollback_domain(args.domain)
    elif args.file:
        rollback_file(args.file)
    else:
        print("❌ Specify either --domain or --file")
        sys.exit(1)

if __name__ == '__main__':
    main()
```

## 07.3 Rollback Validation

### 07.3.1 Post-Rollback Verification

**File:** `scripts/verify-rollback.py`

```python
#!/usr/bin/env python3
# file: scripts/verify-rollback.py
# version: 1.0.0
# guid: 6b7c8d9e-0f1a-2b3c-4d5e-6f7a8b9c0d1e

"""
Verify that rollback was successful.
"""

import os
import sys
from pathlib import Path

def verify_rollback():
    """Verify rollback completed successfully."""
    print("🔍 Verifying rollback...")
    
    issues = []
    
    # Check that proto directory is removed (or empty)
    proto_dir = Path("proto")
    if proto_dir.exists():
        proto_files = list(proto_dir.rglob("*.proto"))
        if proto_files:
            issues.append(f"proto directory still contains {len(proto_files)} files")
    
    # Check that buf configuration is restored
    buf_yaml = Path("buf.yaml")
    if buf_yaml.exists():
        with open(buf_yaml, 'r') as f:
            content = f.read()
            if 'path: proto' in content:
                issues.append("buf.yaml still references proto directory")
    
    # Check that old proto files are still present
    old_proto_files = list(Path("pkg").rglob("*.proto"))
    if not old_proto_files:
        issues.append("Original proto files are missing from pkg/ directory")
    
    # Check for orphaned generated files
    orphaned_files = []
    for pb_file in Path("pkg").rglob("*.pb.go"):
        proto_file = pb_file.with_suffix(".proto")
        if not proto_file.exists():
            orphaned_files.append(str(pb_file))
    
    if orphaned_files:
        issues.append(f"Found {len(orphaned_files)} orphaned generated files")
    
    # Report results
    if issues:
        print("❌ Rollback verification failed:")
        for issue in issues:
            print(f"   • {issue}")
        return False
    else:
        print("✅ Rollback verification passed")
        return True

if __name__ == '__main__':
    if verify_rollback():
        sys.exit(0)
    else:
        sys.exit(1)
```

## 07.4 Emergency Procedures

### 07.4.1 Emergency Stop Script

**File:** `scripts/emergency-stop.sh`

```bash
#!/bin/bash
# file: scripts/emergency-stop.sh
# version: 1.0.0
# guid: 7c8d9e0f-1a2b-3c4d-5e6f-7a8b9c0d1e2f

set -euo pipefail

echo "🚨 EMERGENCY STOP - Halting migration process"

# Kill any running migration processes
pkill -f "migrate-proto-files.py" || true
pkill -f "migrate-domain.py" || true
pkill -f "buf generate" || true

# Create emergency stash
git stash push -m "Emergency stash $(date)"

echo "✅ Migration processes stopped"
echo "💾 Changes stashed for recovery"
echo "🔄 Run rollback script to restore original state"
```

### 07.4.2 Recovery Assistant

**File:** `scripts/recovery-assistant.py`

```python
#!/usr/bin/env python3
# file: scripts/recovery-assistant.py
# version: 1.0.0
# guid: 8d9e0f1a-2b3c-4d5e-6f7a-8b9c0d1e2f3a

"""
Interactive recovery assistant for migration issues.
"""

import os
import sys
import subprocess
from pathlib import Path

class RecoveryAssistant:
    def __init__(self):
        self.issues = []
        
    def diagnose_issues(self):
        """Diagnose current state and identify issues."""
        print("🔍 Diagnosing current state...")
        
        # Check for partial migration
        proto_exists = Path("proto").exists()
        pkg_protos_exist = len(list(Path("pkg").rglob("*.proto"))) > 0
        
        if proto_exists and pkg_protos_exist:
            self.issues.append("Partial migration detected")
        
        # Check for backup files
        if not Path("buf.yaml.backup").exists():
            self.issues.append("Missing buf.yaml backup")
        
        if not Path("buf.gen.yaml.backup").exists():
            self.issues.append("Missing buf.gen.yaml backup")
        
        # Check git status
        result = subprocess.run(['git', 'status', '--porcelain'], 
                              capture_output=True, text=True)
        if result.stdout.strip():
            self.issues.append("Uncommitted changes detected")
        
        # Check for backup branches
        result = subprocess.run(['git', 'branch', '-r'], 
                              capture_output=True, text=True)
        backup_branches = [line for line in result.stdout.split('\n') 
                          if 'proto-reorg-backup-' in line]
        if not backup_branches:
            self.issues.append("No backup branches found")
    
    def suggest_recovery_options(self):
        """Suggest recovery options based on diagnosed issues."""
        print("\n💡 Recovery Options:")
        
        if "Partial migration detected" in self.issues:
            print("   1. Complete the migration with: ./scripts/orchestrate-migration.sh full")
            print("   2. Rollback with: ./scripts/orchestrate-migration.sh rollback")
        
        if "Missing buf.yaml backup" in self.issues:
            print("   3. Restore from git: git checkout HEAD~1 buf.yaml")
        
        if "Uncommitted changes detected" in self.issues:
            print("   4. Stash changes: git stash push -m 'Recovery stash'")
        
        if "No backup branches found" in self.issues:
            print("   5. Create backup now: git checkout -b emergency-backup-$(date +%s)")
    
    def interactive_recovery(self):
        """Run interactive recovery process."""
        self.diagnose_issues()
        
        if not self.issues:
            print("✅ No issues detected")
            return
        
        print(f"\n⚠️  Found {len(self.issues)} issues:")
        for issue in self.issues:
            print(f"   • {issue}")
        
        self.suggest_recovery_options()
        
        print("\n🤔 What would you like to do?")
        print("   1. Attempt automatic recovery")
        print("   2. Get manual recovery steps")
        print("   3. Exit and handle manually")
        
        choice = input("Enter choice (1-3): ").strip()
        
        if choice == "1":
            self.automatic_recovery()
        elif choice == "2":
            self.manual_recovery_steps()
        else:
            print("👋 Exiting - handle recovery manually")
    
    def automatic_recovery(self):
        """Attempt automatic recovery."""
        print("🤖 Attempting automatic recovery...")
        
        # Try rollback first
        result = os.system("./scripts/orchestrate-migration.sh rollback")
        if result == 0:
            print("✅ Automatic rollback successful")
        else:
            print("❌ Automatic rollback failed")
            self.manual_recovery_steps()
    
    def manual_recovery_steps(self):
        """Provide manual recovery steps."""
        print("\n📋 Manual Recovery Steps:")
        print("1. Create emergency backup:")
        print("   git stash push -m 'Emergency backup'")
        print("   git checkout -b emergency-backup-$(date +%s)")
        
        print("\n2. Restore original files:")
        print("   git checkout HEAD~1 buf.yaml buf.gen.yaml")
        print("   rm -rf proto/")
        
        print("\n3. Clean generated files:")
        print("   find pkg -name '*.pb.go' -delete")
        print("   find pkg -name '*_grpc.pb.go' -delete")
        
        print("\n4. Verify state:")
        print("   ./scripts/verify-rollback.py")

if __name__ == '__main__':
    assistant = RecoveryAssistant()
    assistant.interactive_recovery()
```

## 07.5 Backup Management

### 07.5.1 Backup Cleanup Script

**File:** `scripts/cleanup-backups.sh`

```bash
#!/bin/bash
# file: scripts/cleanup-backups.sh
# version: 1.0.0
# guid: 9e0f1a2b-3c4d-5e6f-7a8b-9c0d1e2f3a4b

set -euo pipefail

echo "🧹 Cleaning up old backups..."

# Clean old backup branches (keep last 5)
echo "Cleaning backup branches..."
git branch -r | grep "origin/proto-reorg-backup-" | sort -r | tail -n +6 | while read branch; do
    branch_name=$(echo "$branch" | sed 's/.*origin\///')
    echo "Deleting old backup branch: $branch_name"
    git push origin --delete "$branch_name" 2>/dev/null || true
done

# Clean old filesystem backups (keep last 10)
BACKUP_DIR="$HOME/backups"
if [ -d "$BACKUP_DIR" ]; then
    echo "Cleaning filesystem backups..."
    find "$BACKUP_DIR" -name "gcommon-backup-*.tar.gz" -type f | sort -r | tail -n +11 | while read backup; do
        echo "Deleting old backup: $(basename "$backup")"
        rm "$backup"
    done
fi

echo "✅ Backup cleanup completed"
```

### 07.5.2 Backup Verification

**File:** `scripts/verify-backups.py`

```python
#!/usr/bin/env python3
# file: scripts/verify-backups.py
# version: 1.0.0
# guid: 0f1a2b3c-4d5e-6f7a-8b9c-0d1e2f3a4b5c

"""
Verify that backups are valid and restorable.
"""

import os
import sys
import tempfile
import subprocess
from pathlib import Path

def verify_git_backups():
    """Verify git backup branches."""
    print("🔍 Verifying git backups...")
    
    result = subprocess.run(['git', 'branch', '-r'], 
                          capture_output=True, text=True)
    
    backup_branches = [line.strip() for line in result.stdout.split('\n') 
                      if 'proto-reorg-backup-' in line]
    
    if not backup_branches:
        print("❌ No git backup branches found")
        return False
    
    print(f"✅ Found {len(backup_branches)} git backup branches")
    
    # Test that we can checkout the latest backup
    latest_backup = sorted(backup_branches)[-1].split('/')[-1]
    
    try:
        subprocess.run(['git', 'fetch', 'origin', latest_backup], 
                      check=True, capture_output=True)
        print(f"✅ Latest backup {latest_backup} is accessible")
        return True
    except subprocess.CalledProcessError:
        print(f"❌ Cannot access latest backup {latest_backup}")
        return False

def verify_filesystem_backups():
    """Verify filesystem backups."""
    print("🔍 Verifying filesystem backups...")
    
    backup_dir = Path.home() / "backups"
    if not backup_dir.exists():
        print("❌ Backup directory not found")
        return False
    
    backup_files = list(backup_dir.glob("gcommon-backup-*.tar.gz"))
    
    if not backup_files:
        print("❌ No filesystem backups found")
        return False
    
    print(f"✅ Found {len(backup_files)} filesystem backups")
    
    # Test that latest backup can be extracted
    latest_backup = sorted(backup_files)[-1]
    
    with tempfile.TemporaryDirectory() as temp_dir:
        try:
            subprocess.run(['tar', '-tzf', str(latest_backup)], 
                          check=True, capture_output=True, cwd=temp_dir)
            print(f"✅ Latest backup {latest_backup.name} is valid")
            return True
        except subprocess.CalledProcessError:
            print(f"❌ Latest backup {latest_backup.name} is corrupted")
            return False

if __name__ == '__main__':
    git_ok = verify_git_backups()
    fs_ok = verify_filesystem_backups()
    
    if git_ok and fs_ok:
        print("🎉 All backups verified successfully")
        sys.exit(0)
    else:
        print("💥 Backup verification failed")
        sys.exit(1)
```