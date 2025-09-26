#!/usr/bin/env python3
# file: scripts/rename_directories_to_pb.py
# version: 1.0.0
# guid: b1c2d3e4-f5a6-7b8c-9d0e-1f2a3b4c5d6e

"""
Script to rename all top-level package directories from xxx to xxxpb
to match the pb-suffixed package structure.

This will rename:
- common/ → commonpb/
- metrics/ → metricspb/
- config/ → configpb/
- database/ → databasepb/
- health/ → healthpb/
- media/ → mediapb/
- organization/ → organizationpb/
- queue/ → queuepb/
- web/ → webpb/
"""

import os
import shutil
from pathlib import Path

def rename_directories():
    """Rename all package directories to pb-suffixed names."""
    
    # Directory mappings
    directory_mappings = {
        'common': 'commonpb',
        'metrics': 'metricspb', 
        'config': 'configpb',
        'database': 'databasepb',
        'health': 'healthpb',
        'media': 'mediapb',
        'organization': 'organizationpb',
        'queue': 'queuepb',
        'web': 'webpb'
    }
    
    print("🔄 Renaming package directories to pb-suffixed names...")
    
    for old_name, new_name in directory_mappings.items():
        old_path = Path(old_name)
        new_path = Path(new_name)
        
        if old_path.exists() and old_path.is_dir():
            if new_path.exists():
                print(f"⚠️  Warning: {new_name} already exists, skipping {old_name}")
                continue
                
            print(f"📁 Renaming {old_name}/ → {new_name}/")
            shutil.move(str(old_path), str(new_path))
            print(f"✅ Successfully renamed {old_name} to {new_name}")
        else:
            print(f"❌ Directory {old_name} not found, skipping")
    
    print("\n🎉 Directory renaming complete!")
    print("Next steps:")
    print("1. Commit these changes")
    print("2. Update git tags")
    print("3. Push to BSR with updated tags")

if __name__ == "__main__":
    rename_directories()