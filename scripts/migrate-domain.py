#!/usr/bin/env python3
# file: scripts/migrate-domain.py
# version: 1.0.0
# guid: 1e2f3a4b-5c6d-7e8f-9a0b-1c2d3e4f5a6b

"""
Domain-specific migration script for Protocol Buffer reorganization.

This script handles the migration of individual domains with specific
business logic for each domain type.
"""

import os
import re
import sys
import shutil
import argparse
from pathlib import Path
from typing import Dict, List, Optional

class DomainMigrator:
    """Handle domain-specific migration logic."""
    
    def __init__(self, root_dir: str, domain: str, dry_run: bool = False):
        self.root_dir = Path(root_dir)
        self.domain = domain
        self.dry_run = dry_run
        
        # Domain-specific configurations
        self.domain_configs = {
            'common': {
                'subdirs': ['types', 'messages', 'enums', 'services'],
                'file_categories': {
                    'types': ['entity', 'error', 'pagination', 'validation'],
                    'messages': ['audit', 'event', 'notification'],
                    'enums': ['status', 'level', 'type'],
                    'services': ['service']
                }
            },
            'config': {
                'subdirs': ['api', 'v1', 'v2', 'services'],
                'file_categories': {
                    'api': ['api', 'request', 'response'],
                    'v1': ['config', 'setting', 'environment'],
                    'services': ['service']
                }
            },
            'database': {
                'subdirs': ['config', 'services', 'types', 'schema'],
                'file_categories': {
                    'config': ['config', 'connection'],
                    'services': ['service'],
                    'types': ['type'],
                    'schema': ['schema', 'migration']
                }
            },
            'media': {
                'subdirs': ['types', 'metadata', 'services', 'processing'],
                'file_categories': {
                    'types': ['audio', 'video', 'image', 'track'],
                    'metadata': ['metadata', 'info'],
                    'services': ['service'],
                    'processing': ['processing', 'conversion']
                }
            },
            'metrics': {
                'subdirs': ['v1', 'v2', 'services', 'types'],
                'file_categories': {
                    'v1': ['metric', 'health', 'performance'],
                    'v2': ['metric', 'analytics'],
                    'services': ['service'],
                    'types': ['type', 'status']
                }
            },
            'organization': {
                'subdirs': ['api', 'config', 'services', 'types'],
                'file_categories': {
                    'api': ['api', 'request', 'response'],
                    'config': ['config'],
                    'services': ['service'],
                    'types': ['org', 'user', 'role', 'team']
                }
            },
            'queue': {
                'subdirs': ['api', 'config', 'services', 'types'],
                'file_categories': {
                    'api': ['api', 'request', 'response'],
                    'config': ['config', 'subscription'],
                    'services': ['service'],
                    'types': ['message', 'queue', 'topic']
                }
            },
            'web': {
                'subdirs': ['api', 'config', 'events', 'services'],
                'file_categories': {
                    'api': ['api', 'request', 'response'],
                    'config': ['config', 'route'],
                    'events': ['event', 'webhook'],
                    'services': ['service']
                }
            }
        }
    
    def find_source_files(self) -> List[Path]:
        """Find all source proto files for this domain."""
        source_files = []
        
        # Look for domain directories in pkg/
        domain_patterns = self.get_domain_patterns()
        
        for pattern in domain_patterns:
            proto_dir = self.root_dir / 'pkg' / pattern / 'proto'
            if proto_dir.exists():
                source_files.extend(proto_dir.rglob('*.proto'))
        
        return sorted(source_files)
    
    def get_domain_patterns(self) -> List[str]:
        """Get directory patterns for this domain."""
        patterns = [self.domain]
        
        # Add domain-specific patterns
        if self.domain == 'config':
            patterns.extend(['config_1', 'config_2', 'config_api', 'config_config_1', 'config_config_2'])
        elif self.domain == 'database':
            patterns.extend(['database_config', 'database_services', 'db', 'cache'])
        elif self.domain == 'metrics':
            patterns.extend(['metrics_1', 'metrics_2'])
        elif self.domain == 'organization':
            patterns.extend(['org', 'organization_api', 'organization_config'])
        elif self.domain == 'queue':
            patterns.extend(['queue_api', 'queue_config'])
        elif self.domain == 'web':
            patterns.extend(['web_api', 'web_config', 'web_events'])
        elif self.domain == 'common':
            patterns.extend(['auth', 'health', 'log', 'notification'])
        
        return patterns
    
    def categorize_file(self, file_path: Path) -> str:
        """Categorize a file into the appropriate subdirectory."""
        filename = file_path.stem.lower()
        
        if self.domain not in self.domain_configs:
            return 'types'  # Default category
        
        config = self.domain_configs[self.domain]
        
        # Check file categories
        for category, keywords in config['file_categories'].items():
            if any(keyword in filename for keyword in keywords):
                return category
        
        # Default category
        return config['subdirs'][0] if config['subdirs'] else 'types'
    
    def generate_target_path(self, source_file: Path) -> str:
        """Generate target path for a source file."""
        category = self.categorize_file(source_file)
        filename = source_file.name
        
        return f"proto/gcommon/v1/{self.domain}/{category}/{filename}"
    
    def update_file_content(self, content: str, target_path: str) -> str:
        """Update file content with new paths and packages."""
        # Update file header
        content = re.sub(
            r'// file: [^\n]+',
            f'// file: {target_path}',
            content
        )
        
        # Update package declaration
        category = target_path.split('/')[-2]  # Get category from path
        new_package = f"gcommon.v1.{self.domain}.{category}"
        
        content = re.sub(
            r'package\s+[^;]+;',
            f'package {new_package};',
            content
        )
        
        # Update go_package option
        new_go_package = f"github.com/jdfalk/gcommon/pkg/{self.domain}/{category}"
        
        if 'option go_package' in content:
            content = re.sub(
                r'option\s+go_package\s*=\s*"[^"]+";',
                f'option go_package = "{new_go_package}";',
                content
            )
        else:
            # Add go_package option after package declaration
            content = re.sub(
                r'(package\s+[^;]+;)',
                f'\\1\n\noption go_package = "{new_go_package}";',
                content
            )
        
        # Update import paths
        content = self.update_import_paths(content)
        
        return content
    
    def update_import_paths(self, content: str) -> str:
        """Update import paths in the content."""
        # Find all import statements
        imports = re.findall(r'import\s+"([^"]+)";', content)
        
        for old_import in imports:
            if old_import.startswith('pkg/'):
                new_import = self.convert_import_path(old_import)
                content = content.replace(f'import "{old_import}";', f'import "{new_import}";')
        
        return content
    
    def convert_import_path(self, old_import: str) -> str:
        """Convert old import path to new import path."""
        if not old_import.startswith('pkg/'):
            return old_import
        
        # Remove pkg/ prefix
        path_without_pkg = old_import[4:]
        parts = path_without_pkg.split('/')
        
        if len(parts) >= 2:
            domain_part = parts[0]
            filename = parts[-1]
            
            # Map domain to new structure
            domain = self.normalize_domain_name(domain_part)
            
            # Determine category based on filename
            category = self.determine_category_from_filename(filename)
            
            return f"proto/gcommon/v1/{domain}/{category}/{filename}"
        
        return old_import
    
    def normalize_domain_name(self, domain_part: str) -> str:
        """Normalize domain name to standard domain."""
        if domain_part.startswith('config'):
            return 'config'
        elif domain_part.startswith('database') or domain_part.startswith('db'):
            return 'database'
        elif domain_part.startswith('metrics'):
            return 'metrics'
        elif domain_part.startswith('organization') or domain_part.startswith('org'):
            return 'organization'
        elif domain_part.startswith('queue'):
            return 'queue'
        elif domain_part.startswith('web'):
            return 'web'
        elif domain_part in ['auth', 'health', 'log', 'notification']:
            return 'common'
        elif domain_part == 'cache':
            return 'database'
        else:
            return domain_part
    
    def determine_category_from_filename(self, filename: str) -> str:
        """Determine category from filename."""
        filename_lower = filename.lower()
        
        if 'service' in filename_lower:
            return 'services'
        elif any(word in filename_lower for word in ['enum', 'status', 'type']):
            return 'types'
        elif any(word in filename_lower for word in ['config', 'setting']):
            return 'config'
        elif any(word in filename_lower for word in ['api', 'request', 'response']):
            return 'api'
        elif any(word in filename_lower for word in ['event', 'webhook']):
            return 'events'
        else:
            return 'messages'
    
    def migrate_file(self, source_file: Path) -> bool:
        """Migrate a single file."""
        try:
            target_path = self.generate_target_path(source_file)
            target_file = self.root_dir / target_path
            
            # Read source content
            with open(source_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Update content
            updated_content = self.update_file_content(content, target_path)
            
            if self.dry_run:
                print(f"📝 Would migrate: {source_file} -> {target_path}")
                return True
            
            # Create target directory
            target_file.parent.mkdir(parents=True, exist_ok=True)
            
            # Write updated content
            with open(target_file, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            
            print(f"✅ Migrated: {source_file} -> {target_path}")
            return True
            
        except Exception as e:
            print(f"❌ Failed to migrate {source_file}: {str(e)}")
            return False
    
    def run_migration(self) -> int:
        """Run the domain migration."""
        print(f"🚀 Starting {self.domain} domain migration...")
        
        source_files = self.find_source_files()
        
        if not source_files:
            print(f"📁 No proto files found for domain: {self.domain}")
            return 0
        
        print(f"📊 Found {len(source_files)} files to migrate")
        
        migrated = 0
        failed = 0
        
        for source_file in source_files:
            if self.migrate_file(source_file):
                migrated += 1
            else:
                failed += 1
        
        print(f"\n📈 Domain {self.domain} migration summary:")
        print(f"   Migrated: {migrated}")
        print(f"   Failed: {failed}")
        
        return failed

def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description='Domain-specific proto migration')
    parser.add_argument('domain', help='Domain to migrate')
    parser.add_argument('--dry-run', action='store_true',
                       help='Show what would be done without doing it')
    
    args = parser.parse_args()
    
    valid_domains = ['common', 'config', 'database', 'media', 'metrics', 
                    'organization', 'queue', 'web']
    
    if args.domain not in valid_domains:
        print(f"❌ Invalid domain: {args.domain}")
        print(f"Valid domains: {', '.join(valid_domains)}")
        sys.exit(1)
    
    migrator = DomainMigrator('.', args.domain, args.dry_run)
    failed_count = migrator.run_migration()
    
    if failed_count > 0:
        sys.exit(1)
    
    print(f"🎉 Domain {args.domain} migration completed successfully!")

if __name__ == '__main__':
    main()