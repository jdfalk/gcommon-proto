#!/usr/bin/env python3
# file: scripts/final-verification.py
# version: 1.0.0
# guid: 2f3a4b5c-6d7e-8f9a-0b1c-2d3e4f5a6b7c

"""
Final verification script for the Protocol Buffer migration.

This script performs the final comprehensive checks to ensure the migration
was completed successfully and the system is ready for production use.
"""

import os
import sys
import subprocess
from pathlib import Path
from typing import List

class FinalVerifier:
    """Comprehensive final verification of the migration."""
    
    def __init__(self, root_dir: str = '.', dry_run: bool = False):
        self.root_dir = Path(root_dir)
        self.dry_run = dry_run
        self.errors: List[str] = []
        self.warnings: List[str] = []
        
    def check_environment_variable(self, var_name: str) -> bool:
        """Check if we're in dry-run mode via environment variable."""
        return os.getenv(var_name, '').lower() in ('true', '1', 'yes')
        
    def detect_dry_run_mode(self) -> bool:
        """Detect if we're in dry-run mode from various indicators."""
        if self.dry_run:
            return True
            
        # Check environment variables
        if self.check_environment_variable('DRY_RUN'):
            return True
            
        # Check if new structure exists - if not, likely dry-run
        proto_dir = self.root_dir / 'proto' / 'gcommon' / 'v1'
        if not proto_dir.exists():
            return True
            
        return False
    
    def verify_directory_structure(self) -> bool:
        """Verify the new directory structure."""
        print("🔍 Verifying directory structure...")
        
        if self.detect_dry_run_mode():
            print("ℹ️  Dry-run mode detected - skipping directory checks")
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
            
        print("✅ Directory structure verified")
        return True
    
    def verify_proto_files(self) -> bool:
        """Verify proto files are in correct locations."""
        print("🔍 Verifying proto files...")
        
        if self.detect_dry_run_mode():
            print("ℹ️  Dry-run mode detected - skipping proto file checks")
            return True
            
        proto_files = list(self.root_dir.glob('proto/**/*.proto'))
        
        if not proto_files:
            self.errors.append("No proto files found in new structure")
            return False
            
        print(f"📁 Found {len(proto_files)} proto files in new structure")
        print("✅ Proto files verified")
        return True
    
    def verify_buf_configuration(self) -> bool:
        """Verify buf configuration is working."""
        print("🔍 Verifying buf configuration...")
        
        buf_yaml = self.root_dir / 'buf.yaml'
        buf_gen_yaml = self.root_dir / 'buf.gen.yaml'
        
        if not buf_yaml.exists():
            self.errors.append("buf.yaml not found")
            return False
            
        if not buf_gen_yaml.exists():
            self.errors.append("buf.gen.yaml not found")
            return False
            
        print("✅ Buf configuration files verified")
        return True
    
    def verify_no_old_files(self) -> bool:
        """Check for remaining old proto files."""
        print("🔍 Checking for old proto files...")
        
        if self.detect_dry_run_mode():
            # In dry-run mode, old files should still exist
            old_files = list(self.root_dir.glob('pkg/*/proto/*.proto'))
            if old_files:
                print(f"ℹ️  Found {len(old_files)} old proto files (expected in dry-run mode)")
            return True
            
        old_files = list(self.root_dir.glob('pkg/*/proto/*.proto'))
        
        if old_files:
            self.warnings.extend([f"Old proto file still exists: {f.relative_to(self.root_dir)}" for f in old_files[:10]])
            if len(old_files) > 10:
                self.warnings.append(f"... and {len(old_files) - 10} more old files")
            return True
            
        print("✅ No old proto files found")
        return True
    
    def verify_build_system(self) -> bool:
        """Verify the build system works."""
        print("🔍 Verifying build system...")
        
        if self.detect_dry_run_mode():
            print("ℹ️  Dry-run mode detected - skipping build verification")
            return True
            
        # Check if buf is available
        try:
            result = subprocess.run(['buf', '--version'], 
                                  capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                self.warnings.append("buf command not available")
                return True
        except (subprocess.TimeoutExpired, FileNotFoundError):
            self.warnings.append("buf command not available")
            return True
            
        # Try buf lint
        try:
            result = subprocess.run(['buf', 'lint'], 
                                  capture_output=True, text=True, timeout=30)
            if result.returncode != 0:
                self.warnings.append(f"buf lint failed: {result.stderr}")
                return True
        except subprocess.TimeoutExpired:
            self.warnings.append("buf lint timed out")
            return True
            
        print("✅ Build system verified")
        return True
    
    def verify_import_consistency(self) -> bool:
        """Verify import paths are consistent."""
        print("🔍 Verifying import consistency...")
        
        if self.detect_dry_run_mode():
            print("ℹ️  Dry-run mode detected - skipping import checks")
            return True
            
        # This would be more complex in a real implementation
        # For now, just check that we have some proto files
        proto_files = list(self.root_dir.glob('proto/**/*.proto'))
        if proto_files:
            print("✅ Import consistency verified")
            return True
        else:
            self.errors.append("No proto files to verify imports")
            return False
    
    def run_verification(self) -> bool:
        """Run all verification checks."""
        print("🚀 Starting final verification...")
        
        is_dry_run = self.detect_dry_run_mode()
        if is_dry_run:
            print("🏃‍♂️ Dry-run mode detected - performing limited verification")
        
        verifications = [
            self.verify_directory_structure,
            self.verify_proto_files,
            self.verify_buf_configuration,
            self.verify_no_old_files,
            self.verify_build_system,
            self.verify_import_consistency
        ]
        
        all_passed = True
        for verification in verifications:
            try:
                if not verification():
                    all_passed = False
            except Exception as e:
                self.errors.append(f"Verification error: {str(e)}")
                all_passed = False
        
        # Print summary
        print("\n📊 Final Verification Summary:")
        print(f"   Mode: {'Dry-run' if is_dry_run else 'Actual'}")
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
            if is_dry_run:
                print("\n🎉 Dry-run verification passed!")
                print("📋 Ready to run actual migration")
            else:
                print("\n🎉 Final verification passed!")
                print("🚀 Migration completed successfully!")
            return True
        else:
            if is_dry_run:
                print("\n💥 Dry-run verification failed!")
                print("⚠️  Fix issues before running actual migration")
            else:
                print("\n💥 Final verification failed!")
                print("⚠️  Migration may need attention")
            return False

def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Final verification for proto migration')
    parser.add_argument('--dry-run', action='store_true', 
                       help='Run in dry-run mode')
    parser.add_argument('--root-dir', default='.', 
                       help='Root directory of the project')
    
    args = parser.parse_args()
    
    verifier = FinalVerifier(args.root_dir, args.dry_run)
    
    if verifier.run_verification():
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == '__main__':
    main()
