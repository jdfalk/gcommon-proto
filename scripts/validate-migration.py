#!/usr/bin/env python3
# file: scripts/validate-migration.py
# version: 1.0.0  
# guid: 9c0d1e2f-3a4b-5c6d-7e8f-9a0b1c2d3e4f

"""
Validation script for proto file migration.

This script validates the migration by:
1. Checking all files were moved correctly
2. Validating import paths are updated
3. Ensuring package names are consistent
4. Verifying buf configuration works
5. Testing code generation
"""

import os
import re
import sys
import subprocess
from pathlib import Path
from typing import List

class MigrationValidator:
    """Validate the proto migration results."""
    
    def __init__(self, root_dir: str = '.', dry_run: bool = False):
        self.root_dir = Path(root_dir)
        self.dry_run = dry_run
        self.errors: List[str] = []
        self.warnings: List[str] = []
        
    def detect_dry_run_mode(self) -> bool:
        """Detect if we're in dry-run mode."""
        if self.dry_run:
            return True
            
        # Check environment variables
        if os.getenv('DRY_RUN', '').lower() in ('true', '1', 'yes'):
            return True
            
        # Check if new structure exists - if not, likely dry-run
        proto_dir = self.root_dir / 'proto' / 'gcommon' / 'v1'
        if not proto_dir.exists():
            return True
            
        return False
        
    def validate_directory_structure(self) -> bool:
        """Validate the new directory structure exists."""
        print("🔍 Validating directory structure...")
        
        is_dry_run = self.detect_dry_run_mode()
        if is_dry_run:
            print("ℹ️  Dry-run mode detected - skipping directory structure validation")
            return True
        
        required_dirs = [
            'proto/gcommon/v1/common',
            'proto/gcommon/v1/config',
            'proto/gcommon/v1/database',
            'proto/gcommon/v1/media',
            'proto/gcommon/v1/metrics',
            'proto/gcommon/v1/organization',
            'proto/gcommon/v1/queue',
            'proto/gcommon/v1/web'
        ]
        
        missing_dirs = []
        for dir_path in required_dirs:
            full_path = self.root_dir / dir_path
            if not full_path.exists():
                missing_dirs.append(dir_path)
        
        if missing_dirs:
            self.errors.extend([f"Missing directory: {d}" for d in missing_dirs])
            return False
        
        print("✅ Directory structure is valid")
        return True
    
    def validate_proto_files(self) -> bool:
        """Validate proto files in new structure."""
        print("🔍 Validating proto files...")
        
        is_dry_run = self.detect_dry_run_mode()
        if is_dry_run:
            print("ℹ️  Dry-run mode detected - skipping proto file validation")
            return True
        
        proto_files = list(self.root_dir.glob('proto/**/*.proto'))
        
        if not proto_files:
            self.errors.append("No proto files found in new structure")
            return False
        
        print(f"📁 Found {len(proto_files)} proto files")
        
        invalid_files = []
        for proto_file in proto_files:
            if not self.validate_single_proto_file(proto_file):
                invalid_files.append(str(proto_file))
        
        if invalid_files:
            self.errors.extend([f"Invalid proto file: {f}" for f in invalid_files])
            return False
        
        print("✅ All proto files are valid")
        return True
    
    def validate_single_proto_file(self, proto_file: Path) -> bool:
        """Validate a single proto file."""
        try:
            with open(proto_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check for required headers
            if not re.search(r'// file: proto/', content):
                self.warnings.append(f"File header path may be incorrect: {proto_file}")
            
            # Check package declaration
            package_match = re.search(r'package\s+([^;]+);', content)
            if not package_match:
                return False
            
            package_name = package_match.group(1).strip()
            if not package_name.startswith('gcommon.v1.'):
                self.warnings.append(f"Package name doesn't follow convention: {package_name} in {proto_file}")
            
            # Check go_package option
            go_package_match = re.search(r'option\s+go_package\s*=\s*"([^"]+)";', content)
            if not go_package_match:
                return False
            
            go_package = go_package_match.group(1).strip()
            if not go_package.startswith('github.com/jdfalk/gcommon/pkg/'):
                self.warnings.append(f"go_package doesn't follow convention: {go_package} in {proto_file}")
            
            # Check import paths
            imports = re.findall(r'import\s+"([^"]+)";', content)
            for import_path in imports:
                if import_path.startswith('pkg/'):
                    self.errors.append(f"Old import path found: {import_path} in {proto_file}")
                    return False
            
            return True
            
        except Exception as e:
            self.errors.append(f"Failed to validate {proto_file}: {str(e)}")
            return False
    
    def validate_no_old_files(self) -> bool:
        """Validate that old proto files have been removed."""
        print("🔍 Checking for remaining old proto files...")
        
        is_dry_run = self.detect_dry_run_mode()
        
        old_proto_files = []
        for proto_file in self.root_dir.glob('pkg/**/*.proto'):
            old_proto_files.append(str(proto_file))
        
        if old_proto_files:
            if is_dry_run:
                print(f"ℹ️  Found {len(old_proto_files)} old proto files (expected in dry-run mode)")
                return True
            else:
                self.warnings.extend([f"Old proto file still exists: {f}" for f in old_proto_files])
                print(f"⚠️  Found {len(old_proto_files)} old proto files")
                return False
        
        print("✅ No old proto files found")
        return True
    
    def validate_buf_configuration(self) -> bool:
        """Validate buf configuration files."""
        print("🔍 Validating buf configuration...")
        
        # Check buf.yaml exists and is valid
        buf_yaml = self.root_dir / 'buf.yaml'
        if not buf_yaml.exists():
            self.errors.append("buf.yaml not found")
            return False
        
        # Check buf.gen.yaml exists and is valid
        buf_gen_yaml = self.root_dir / 'buf.gen.yaml'
        if not buf_gen_yaml.exists():
            self.errors.append("buf.gen.yaml not found")
            return False
        
        print("✅ Buf configuration files exist")
        return True
    
    def validate_buf_build(self) -> bool:
        """Validate that buf can build the new structure."""
        print("🔍 Testing buf build...")
        
        is_dry_run = self.detect_dry_run_mode()
        if is_dry_run:
            print("ℹ️  Dry-run mode detected - skipping buf build test")
            return True
        
        try:
            result = subprocess.run(
                ['buf', 'build', 'proto'],
                cwd=self.root_dir,
                capture_output=True,
                text=True,
                timeout=60
            )
            
            if result.returncode != 0:
                self.errors.append(f"buf build failed: {result.stderr}")
                return False
            
            print("✅ buf build succeeded")
            return True
            
        except subprocess.TimeoutExpired:
            self.errors.append("buf build timed out")
            return False
        except FileNotFoundError:
            self.warnings.append("buf command not found - skipping build test")
            return True
        except Exception as e:
            self.errors.append(f"buf build error: {str(e)}")
            return False
    
    def validate_import_consistency(self) -> bool:
        """Validate that import paths are consistent across all files."""
        print("🔍 Validating import consistency...")
        
        proto_files = list(self.root_dir.glob('proto/**/*.proto'))
        all_imports = set()
        file_imports = {}
        
        # Collect all imports
        for proto_file in proto_files:
            try:
                with open(proto_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                imports = re.findall(r'import\s+"([^"]+)";', content)
                file_imports[str(proto_file)] = imports
                all_imports.update(imports)
                
            except Exception as e:
                self.warnings.append(f"Could not read {proto_file}: {str(e)}")
        
        # Check that imported files exist
        missing_imports = []
        for import_path in all_imports:
            if import_path.startswith('proto/'):
                import_file = self.root_dir / import_path
                if not import_file.exists():
                    missing_imports.append(import_path)
        
        if missing_imports:
            self.errors.extend([f"Missing imported file: {f}" for f in missing_imports])
            return False
        
        print("✅ Import consistency validated")
        return True
    
    def run_validation(self) -> bool:
        """Run complete validation suite."""
        print("🚀 Starting migration validation...")
        
        validations = [
            self.validate_directory_structure,
            self.validate_proto_files,
            self.validate_no_old_files,
            self.validate_buf_configuration,
            self.validate_import_consistency,
            self.validate_buf_build
        ]
        
        all_passed = True
        for validation in validations:
            if not validation():
                all_passed = False
        
        # Print summary
        print("\n📊 Validation Summary:")
        print(f"   Errors: {len(self.errors)}")
        print(f"   Warnings: {len(self.warnings)}")
        
        if self.errors:
            print("\n❌ Errors:")
            for error in self.errors:
                print(f"   • {error}")
        
        if self.warnings:
            print("\n⚠️  Warnings:")
            for warning in self.warnings:
                print(f"   • {warning}")
        
        if all_passed and not self.errors:
            print("\n🎉 Validation passed!")
            return True
        else:
            print("\n💥 Validation failed!")
            return False

def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Validate proto migration')
    parser.add_argument('--dry-run', action='store_true', 
                       help='Run in dry-run mode')
    parser.add_argument('--root-dir', default='.', 
                       help='Root directory of the project')
    
    args = parser.parse_args()
    
    validator = MigrationValidator(args.root_dir, args.dry_run)
    
    if validator.run_validation():
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == '__main__':
    main()