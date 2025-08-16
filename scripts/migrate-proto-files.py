#!/usr/bin/env python3
# file: scripts/migrate-proto-files.py
# version: 1.0.0
# guid: 7a8b9c0d-1e2f-3a4b-5c6d-7e8f9a0b1c2d

"""
Comprehensive Protocol Buffer file migration script for GCommon repository.

This script implements the massive reorganization plan by:
1. Analyzing current proto file structure
2. Creating target directory structure
3. Migrating files with updated import paths
4. Updating package names and go_package options
5. Validating migration success

Usage:
    python3 scripts/migrate-proto-files.py [--dry-run] [--domain DOMAIN]
    
Options:
    --dry-run: Show what would be moved without actually moving files
    --domain: Process only specific domain (common, config, database, etc.)
"""

import os
import re
import sys
import json
import shutil
import argparse
from pathlib import Path
from typing import Dict, List, Set, Tuple, Optional
from dataclasses import dataclass, asdict

@dataclass
class ProtoFile:
    """Represents a proto file with its metadata."""
    current_path: str
    target_path: str
    package_name: str
    go_package: str
    imports: List[str]
    messages: List[str]
    services: List[str]
    issues: List[str]

@dataclass
class MigrationStats:
    """Track migration statistics."""
    total_files: int = 0
    migrated_files: int = 0
    failed_files: int = 0
    domains: Dict[str, int] = None
    
    def __post_init__(self):
        if self.domains is None:
            self.domains = {}

class ProtoMigrator:
    """Main migration class that handles the reorganization."""
    
    def __init__(self, root_dir: str, dry_run: bool = False):
        self.root_dir = Path(root_dir)
        self.dry_run = dry_run
        self.stats = MigrationStats()
        
        # Domain mapping for migration
        self.domain_mapping = {
            'common': {
                'target_base': 'proto/gcommon/v1/common',
                'package_prefix': 'gcommon.v1.common',
                'go_package_prefix': 'github.com/jdfalk/gcommon/pkg/common'
            },
            'config': {
                'target_base': 'proto/gcommon/v1/config',
                'package_prefix': 'gcommon.v1.config',
                'go_package_prefix': 'github.com/jdfalk/gcommon/pkg/config'
            },
            'database': {
                'target_base': 'proto/gcommon/v1/database',
                'package_prefix': 'gcommon.v1.database',
                'go_package_prefix': 'github.com/jdfalk/gcommon/pkg/database'
            },
            'media': {
                'target_base': 'proto/gcommon/v1/media',
                'package_prefix': 'gcommon.v1.media',
                'go_package_prefix': 'github.com/jdfalk/gcommon/pkg/media'
            },
            'metrics': {
                'target_base': 'proto/gcommon/v1/metrics',
                'package_prefix': 'gcommon.v1.metrics',
                'go_package_prefix': 'github.com/jdfalk/gcommon/pkg/metrics'
            },
            'organization': {
                'target_base': 'proto/gcommon/v1/organization',
                'package_prefix': 'gcommon.v1.organization',
                'go_package_prefix': 'github.com/jdfalk/gcommon/pkg/organization'
            },
            'queue': {
                'target_base': 'proto/gcommon/v1/queue',
                'package_prefix': 'gcommon.v1.queue',
                'go_package_prefix': 'github.com/jdfalk/gcommon/pkg/queue'
            },
            'web': {
                'target_base': 'proto/gcommon/v1/web',
                'package_prefix': 'gcommon.v1.web',
                'go_package_prefix': 'github.com/jdfalk/gcommon/pkg/web'
            }
        }
        
    def discover_proto_files(self, domain_filter: Optional[str] = None) -> List[Path]:
        """Discover all proto files in the repository."""
        proto_files = []
        
        for proto_file in self.root_dir.rglob("*.proto"):
            if "pkg/" in str(proto_file) and "/proto/" in str(proto_file):
                # Extract domain from path
                path_parts = str(proto_file).split('/')
                pkg_index = next(i for i, part in enumerate(path_parts) if part == 'pkg')
                if pkg_index + 1 < len(path_parts):
                    domain_part = path_parts[pkg_index + 1]
                    
                    # Map domain variations to standard domains
                    domain = self.normalize_domain_name(domain_part)
                    
                    if domain_filter is None or domain == domain_filter:
                        proto_files.append(proto_file)
                        
        return sorted(proto_files)
    
    def normalize_domain_name(self, domain_part: str) -> str:
        """Normalize domain names to standard domains."""
        # Handle config variations
        if domain_part.startswith('config'):
            return 'config'
        
        # Handle database variations
        if domain_part.startswith('database') or domain_part.startswith('db'):
            return 'database'
            
        # Handle metrics variations
        if domain_part.startswith('metrics'):
            return 'metrics'
            
        # Handle organization variations
        if domain_part.startswith('organization') or domain_part.startswith('org'):
            return 'organization'
            
        # Handle queue variations
        if domain_part.startswith('queue'):
            return 'queue'
            
        # Handle web variations
        if domain_part.startswith('web'):
            return 'web'
            
        # Direct mappings
        domain_map = {
            'auth': 'common',  # Auth becomes part of common
            'health': 'common',  # Health becomes part of common
            'log': 'common',  # Log becomes part of common
            'cache': 'database',  # Cache becomes part of database
            'notification': 'common',  # Notification becomes part of common
        }
        
        return domain_map.get(domain_part, domain_part)
    
    def analyze_proto_file(self, file_path: Path) -> ProtoFile:
        """Analyze a proto file and determine its migration target."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Extract current metadata
            current_path = str(file_path.relative_to(self.root_dir))
            package_match = re.search(r'package\s+([^;]+);', content)
            current_package = package_match.group(1).strip() if package_match else ""
            
            go_package_match = re.search(r'option\s+go_package\s*=\s*"([^"]+)";', content)
            current_go_package = go_package_match.group(1).strip() if go_package_match else ""
            
            # Extract imports
            imports = re.findall(r'import\s+"([^"]+)";', content)
            
            # Extract messages and services
            messages = re.findall(r'message\s+(\w+)\s*{', content)
            services = re.findall(r'service\s+(\w+)\s*{', content)
            
            # Determine target domain and path
            domain = self.extract_domain_from_path(current_path)
            target_path = self.determine_target_path(current_path, domain, content)
            
            # Generate new package name and go_package
            if domain in self.domain_mapping:
                mapping = self.domain_mapping[domain]
                new_package = self.generate_new_package_name(target_path, mapping['package_prefix'])
                new_go_package = self.generate_new_go_package(target_path, mapping['go_package_prefix'])
            else:
                # Fallback for unmapped domains
                new_package = f"gcommon.v1.{domain}"
                new_go_package = f"github.com/jdfalk/gcommon/pkg/{domain}"
            
            issues = []
            
            # Check for issues
            if not package_match:
                issues.append("Missing package declaration")
            if not go_package_match:
                issues.append("Missing go_package option")
                
            return ProtoFile(
                current_path=current_path,
                target_path=target_path,
                package_name=new_package,
                go_package=new_go_package,
                imports=imports,
                messages=messages,
                services=services,
                issues=issues
            )
            
        except Exception as e:
            return ProtoFile(
                current_path=str(file_path.relative_to(self.root_dir)),
                target_path="",
                package_name="",
                go_package="",
                imports=[],
                messages=[],
                services=[],
                issues=[f"Analysis failed: {str(e)}"]
            )
    
    def extract_domain_from_path(self, file_path: str) -> str:
        """Extract domain from the file path."""
        path_parts = file_path.split('/')
        if 'pkg' in path_parts:
            pkg_index = path_parts.index('pkg')
            if pkg_index + 1 < len(path_parts):
                domain_part = path_parts[pkg_index + 1]
                return self.normalize_domain_name(domain_part)
        return 'common'  # Default domain
    
    def determine_target_path(self, current_path: str, domain: str, content: str) -> str:
        """Determine the target path for a proto file."""
        filename = Path(current_path).name
        
        if domain not in self.domain_mapping:
            return f"proto/gcommon/v1/common/types/{filename}"
        
        target_base = self.domain_mapping[domain]['target_base']
        
        # Categorize by file type
        if 'service' in filename.lower() or 'rpc' in content.lower():
            return f"{target_base}/services/{filename}"
        elif any(word in filename.lower() for word in ['enum', 'status', 'type']):
            return f"{target_base}/types/{filename}"
        elif any(word in filename.lower() for word in ['config', 'setting']):
            return f"{target_base}/config/{filename}"
        elif any(word in filename.lower() for word in ['api', 'request', 'response']):
            return f"{target_base}/api/{filename}"
        else:
            # Default to messages directory
            return f"{target_base}/messages/{filename}"
    
    def generate_new_package_name(self, target_path: str, package_prefix: str) -> str:
        """Generate new package name based on target path."""
        path_parts = target_path.split('/')
        
        # Extract subdomain from path
        if len(path_parts) >= 5:  # proto/gcommon/v1/domain/subdomain/file
            subdomain = path_parts[4]
            return f"{package_prefix}.{subdomain}"
        else:
            return package_prefix
    
    def generate_new_go_package(self, target_path: str, go_package_prefix: str) -> str:
        """Generate new go_package based on target path."""
        path_parts = target_path.split('/')
        
        # Extract subdomain from path
        if len(path_parts) >= 5:  # proto/gcommon/v1/domain/subdomain/file
            subdomain = path_parts[4]
            return f"{go_package_prefix}/{subdomain}"
        else:
            return go_package_prefix
    
    def update_proto_content(self, content: str, proto_file: ProtoFile) -> str:
        """Update proto file content with new paths and packages."""
        # Update file header
        content = re.sub(
            r'// file: [^\n]+',
            f'// file: {proto_file.target_path}',
            content
        )
        
        # Update package declaration
        content = re.sub(
            r'package\s+[^;]+;',
            f'package {proto_file.package_name};',
            content
        )
        
        # Update go_package option
        if 'option go_package' in content:
            content = re.sub(
                r'option\s+go_package\s*=\s*"[^"]+";',
                f'option go_package = "{proto_file.go_package}";',
                content
            )
        else:
            # Add go_package option after package declaration
            content = re.sub(
                r'(package\s+[^;]+;)',
                f'\\1\n\noption go_package = "{proto_file.go_package}";',
                content
            )
        
        # Update import paths
        for old_import in proto_file.imports:
            if old_import.startswith('pkg/'):
                # Convert old import to new import path
                new_import = self.convert_import_path(old_import)
                content = content.replace(f'import "{old_import}";', f'import "{new_import}";')
        
        return content
    
    def convert_import_path(self, old_import: str) -> str:
        """Convert old import path to new import path."""
        # Remove pkg/ prefix and convert to new structure
        if old_import.startswith('pkg/'):
            path_without_pkg = old_import[4:]  # Remove 'pkg/'
            parts = path_without_pkg.split('/')
            
            if len(parts) >= 2:
                domain_part = parts[0]
                domain = self.normalize_domain_name(domain_part)
                filename = parts[-1]
                
                if domain in self.domain_mapping:
                    # Try to determine subdomain based on filename or path
                    if 'service' in filename.lower():
                        return f"proto/gcommon/v1/{domain}/services/{filename}"
                    elif any(word in filename.lower() for word in ['enum', 'status', 'type']):
                        return f"proto/gcommon/v1/{domain}/types/{filename}"
                    elif any(word in filename.lower() for word in ['config', 'setting']):
                        return f"proto/gcommon/v1/{domain}/config/{filename}"
                    elif any(word in filename.lower() for word in ['api', 'request', 'response']):
                        return f"proto/gcommon/v1/{domain}/api/{filename}"
                    else:
                        return f"proto/gcommon/v1/{domain}/messages/{filename}"
        
        # Fallback: return original if conversion fails
        return old_import
    
    def migrate_file(self, proto_file: ProtoFile) -> bool:
        """Migrate a single proto file."""
        try:
            source_path = self.root_dir / proto_file.current_path
            target_path = self.root_dir / proto_file.target_path
            
            if not source_path.exists():
                print(f"❌ Source file not found: {source_path}")
                return False
            
            # Read and update content
            with open(source_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            updated_content = self.update_proto_content(content, proto_file)
            
            if self.dry_run:
                print(f"📝 Would migrate: {proto_file.current_path} -> {proto_file.target_path}")
                return True
            
            # Create target directory
            target_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Write updated content to target
            with open(target_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            
            print(f"✅ Migrated: {proto_file.current_path} -> {proto_file.target_path}")
            return True
            
        except Exception as e:
            print(f"❌ Failed to migrate {proto_file.current_path}: {str(e)}")
            return False
    
    def run_migration(self, domain_filter: Optional[str] = None) -> MigrationStats:
        """Run the complete migration process."""
        print("🚀 Starting Protocol Buffer migration...")
        
        # Discover files
        proto_files = self.discover_proto_files(domain_filter)
        self.stats.total_files = len(proto_files)
        
        if domain_filter:
            print(f"📁 Processing domain: {domain_filter}")
        
        print(f"📊 Found {len(proto_files)} proto files to migrate")
        
        # Analyze and migrate files
        for file_path in proto_files:
            proto_file = self.analyze_proto_file(file_path)
            
            if proto_file.issues:
                print(f"⚠️  Issues in {proto_file.current_path}: {', '.join(proto_file.issues)}")
            
            # Track domain stats
            domain = self.extract_domain_from_path(proto_file.current_path)
            self.stats.domains[domain] = self.stats.domains.get(domain, 0) + 1
            
            # Migrate file
            if self.migrate_file(proto_file):
                self.stats.migrated_files += 1
            else:
                self.stats.failed_files += 1
        
        # Print summary
        print(f"\n📈 Migration Summary:")
        print(f"   Total files: {self.stats.total_files}")
        print(f"   Migrated: {self.stats.migrated_files}")
        print(f"   Failed: {self.stats.failed_files}")
        
        print(f"\n📂 Domain breakdown:")
        for domain, count in sorted(self.stats.domains.items()):
            print(f"   {domain}: {count} files")
        
        return self.stats

def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description='Migrate Protocol Buffer files')
    parser.add_argument('--dry-run', action='store_true', 
                       help='Show what would be moved without actually moving files')
    parser.add_argument('--domain', type=str, 
                       help='Process only specific domain (common, config, database, etc.)')
    
    args = parser.parse_args()
    
    # Initialize migrator
    migrator = ProtoMigrator(root_dir='.', dry_run=args.dry_run)
    
    # Run migration
    stats = migrator.run_migration(domain_filter=args.domain)
    
    # Exit with error if any files failed
    if stats.failed_files > 0:
        sys.exit(1)
    
    print("🎉 Migration completed successfully!")

if __name__ == '__main__':
    main()