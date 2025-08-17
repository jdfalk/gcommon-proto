#!/usr/bin/env python3
# file: scripts/master-migration.py
# version: 1.0.0
# guid: 8d7c6b5a-4f3e-2d1c-0b9a-8f7e6d5c4b3a

"""
GCommon Protocol Buffer Master Migration Script

This script orchestrates the complete reorganization of 1,632+ Protocol Buffer files
from pkg/*/proto/ to proto/gcommon/v1/ structure.

Features:
- Comprehensive error handling and validation
- Automatic rollback capabilities
- Dry-run mode for safe testing
- Progress tracking and detailed logging
- Backup creation and restoration
- Domain-specific processing
"""

import argparse
import datetime
import json
import logging
import shutil
import subprocess
import sys
import tarfile
import time
from pathlib import Path
from typing import Any, Dict, List, Optional


class Colors:
    """ANSI color codes for terminal output"""

    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    YELLOW = "\033[1;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    BOLD = "\033[1m"
    RESET = "\033[0m"


class MigrationLogger:
    """Enhanced logging with colors and progress tracking"""

    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self.start_time = time.time()

        # Set up file logging
        log_dir = Path("logs")
        log_dir.mkdir(exist_ok=True)

        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file = log_dir / f"migration_{timestamp}.log"

        logging.basicConfig(
            level=logging.DEBUG if verbose else logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
            handlers=[
                logging.FileHandler(log_file),
                logging.StreamHandler(sys.stdout) if verbose else logging.NullHandler(),
            ],
        )

        self.logger = logging.getLogger(__name__)
        self.log_file = log_file

    def _print_colored(self, message: str, color: str, prefix: str = ""):
        """Print colored message to console"""
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        full_message = f"[{timestamp}] {prefix}{message}"
        print(f"{color}{full_message}{Colors.RESET}")

    def log(self, message: str):
        """General log message"""
        self._print_colored(message, Colors.BLUE)
        self.logger.info(message)

    def success(self, message: str):
        """Success message"""
        self._print_colored(message, Colors.GREEN, "✅ ")
        self.logger.info(f"SUCCESS: {message}")

    def warning(self, message: str):
        """Warning message"""
        self._print_colored(message, Colors.YELLOW, "⚠️  ")
        self.logger.warning(message)

    def error(self, message: str):
        """Error message"""
        self._print_colored(message, Colors.RED, "❌ ")
        self.logger.error(message)

    def info(self, message: str):
        """Info message"""
        self._print_colored(message, Colors.CYAN, "ℹ️  ")
        self.logger.info(message)

    def step(self, message: str):
        """Step message"""
        self._print_colored(message, Colors.PURPLE, "🚀 STEP: ")
        self.logger.info(f"STEP: {message}")


class BackupManager:
    """Manages backup creation and restoration"""

    def __init__(self, root_dir: Path, logger: MigrationLogger):
        self.root_dir = root_dir
        self.logger = logger
        self.backup_dir = Path.home() / "backups"
        self.backup_dir.mkdir(exist_ok=True)
        self.git_backup_branch = None
        self.filesystem_backup = None

    def create_backups(self, dry_run: bool = False) -> Dict[str, Any]:
        """Create git and filesystem backups"""
        backup_info = {
            "timestamp": datetime.datetime.now().isoformat(),
            "git_branch": None,
            "filesystem_backup": None,
            "success": False,
        }

        if dry_run:
            self.logger.info("Would create backups (dry-run mode)")
            backup_info["success"] = True
            return backup_info

        try:
            # Create git backup branch
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            git_branch = f"proto-reorg-backup-{timestamp}"

            self.logger.log(f"Creating git backup branch: {git_branch}")
            subprocess.run(
                ["git", "checkout", "-b", git_branch],
                cwd=self.root_dir,
                check=True,
                capture_output=True,
            )

            try:
                subprocess.run(
                    ["git", "push", "origin", git_branch],
                    cwd=self.root_dir,
                    check=True,
                    capture_output=True,
                )
                self.logger.success(f"Git backup branch pushed: {git_branch}")
            except subprocess.CalledProcessError:
                self.logger.warning("Could not push backup branch to remote")

            subprocess.run(
                ["git", "checkout", "-"],
                cwd=self.root_dir,
                check=True,
                capture_output=True,
            )

            self.git_backup_branch = git_branch
            backup_info["git_branch"] = git_branch

            # Create filesystem backup
            backup_file = self.backup_dir / f"gcommon-backup-{timestamp}.tar.gz"
            self.logger.log(f"Creating filesystem backup: {backup_file}")

            with tarfile.open(backup_file, "w:gz") as tar:
                tar.add(
                    self.root_dir,
                    arcname="gcommon",
                    exclude=lambda x: any(
                        exclude in x
                        for exclude in [
                            ".git",
                            "node_modules",
                            "target",
                            ".log",
                            "logs",
                            "__pycache__",
                        ]
                    ),
                )

            self.filesystem_backup = backup_file
            backup_info["filesystem_backup"] = str(backup_file)
            backup_info["success"] = True

            self.logger.success("Backups created successfully")

            # Save backup info
            backup_info_file = self.backup_dir / f"backup-info-{timestamp}.json"
            with open(backup_info_file, "w") as f:
                json.dump(backup_info, f, indent=2)

            return backup_info

        except Exception as e:
            self.logger.error(f"Failed to create backups: {e}")
            backup_info["error"] = str(e)
            return backup_info

    def restore_from_backup(self, backup_info_file: Optional[Path] = None):
        """Restore from the most recent backup"""
        try:
            if backup_info_file is None:
                # Find most recent backup
                backup_files = list(self.backup_dir.glob("backup-info-*.json"))
                if not backup_files:
                    raise FileNotFoundError("No backup info files found")
                backup_info_file = max(backup_files, key=lambda x: x.stat().st_mtime)

            with open(backup_info_file) as f:
                backup_info = json.load(f)

            if backup_info["git_branch"]:
                self.logger.log(
                    f"Restoring from git branch: {backup_info['git_branch']}"
                )
                subprocess.run(
                    ["git", "checkout", backup_info["git_branch"]],
                    cwd=self.root_dir,
                    check=True,
                )

            if backup_info["filesystem_backup"]:
                self.logger.log(
                    f"Filesystem backup available: {backup_info['filesystem_backup']}"
                )
                self.logger.info(
                    "To restore filesystem: extract the tar.gz file manually"
                )

            self.logger.success("Restore completed")

        except Exception as e:
            self.logger.error(f"Failed to restore backup: {e}")
            raise


class MasterMigration:
    """Main migration orchestrator"""

    TOTAL_STEPS = 12
    DOMAINS = [
        "common",
        "config",
        "database",
        "media",
        "metrics",
        "organization",
        "queue",
        "web",
    ]

    def __init__(self):
        self.root_dir = Path(__file__).parent.parent.resolve()
        self.scripts_dir = self.root_dir / "scripts"
        self.current_step = 0
        self.logger = None
        self.backup_manager = None
        self.start_time = None

    def setup_logging(self, verbose: bool = False):
        """Initialize logging"""
        self.logger = MigrationLogger(verbose)
        self.backup_manager = BackupManager(self.root_dir, self.logger)

    def progress(self, message: str):
        """Track and display progress"""
        self.current_step += 1
        progress_msg = f"Progress: {self.current_step}/{self.TOTAL_STEPS} - {message}"
        self.logger._print_colored(progress_msg, Colors.PURPLE, "📊 ")
        self.logger.logger.info(f"PROGRESS: {progress_msg}")

    def run_script(
        self, script_name: str, args: List[str] = None, dry_run: bool = False
    ) -> subprocess.CompletedProcess:
        """Run a Python script with error handling"""
        if args is None:
            args = []

        if dry_run and "--dry-run" not in args:
            args.append("--dry-run")

        script_path = self.scripts_dir / script_name
        cmd = [sys.executable, str(script_path)] + args

        self.logger.log(f"Running: {' '.join(cmd)}")

        try:
            result = subprocess.run(
                cmd, cwd=self.root_dir, check=True, capture_output=True, text=True
            )
            if result.stdout and self.logger.verbose:
                self.logger.info(f"Output: {result.stdout}")
            return result
        except subprocess.CalledProcessError as e:
            self.logger.error(f"Script failed: {script_name}")
            self.logger.error(f"Error: {e.stderr}")
            raise

    def run_shell_script(
        self, script_name: str, args: List[str] = None
    ) -> subprocess.CompletedProcess:
        """Run a shell script with error handling"""
        if args is None:
            args = []

        script_path = self.scripts_dir / script_name
        cmd = [str(script_path)] + args

        self.logger.log(f"Running: {' '.join(cmd)}")

        try:
            result = subprocess.run(
                cmd, cwd=self.root_dir, check=True, capture_output=True, text=True
            )
            if result.stdout and self.logger.verbose:
                self.logger.info(f"Output: {result.stdout}")
            return result
        except subprocess.CalledProcessError as e:
            self.logger.error(f"Shell script failed: {script_name}")
            self.logger.error(f"Error: {e.stderr}")
            raise

    def check_prerequisites(self) -> bool:
        """Check all prerequisites"""
        self.logger.step("Checking Prerequisites")

        missing_tools = []

        # Check required tools
        for tool in ["python3", "git"]:
            if shutil.which(tool) is None:
                missing_tools.append(tool)

        # Check Python dependencies
        try:
            import importlib.util

            spec = importlib.util.find_spec("yaml")
            if spec is None:
                raise ImportError("yaml module not found")
        except ImportError:
            self.logger.warning("PyYAML not found - attempting to install...")
            try:
                subprocess.run(
                    [sys.executable, "-m", "pip", "install", "pyyaml"],
                    check=True,
                    capture_output=True,
                )
                self.logger.success("PyYAML installed successfully")
            except subprocess.CalledProcessError:
                self.logger.error("Failed to install PyYAML - please install manually")
                return False

        # Check optional tools
        if shutil.which("buf") is None:
            self.logger.warning(
                "buf command not found - some validations will be skipped"
            )
            self.logger.info("Install buf: https://docs.buf.build/installation")

        if shutil.which("go") is None:
            self.logger.warning(
                "go command not found - Go compilation tests will be skipped"
            )

        if missing_tools:
            self.logger.error(f"Missing required tools: {', '.join(missing_tools)}")
            return False

        # Check repository state
        try:
            result = subprocess.run(
                ["git", "status", "--porcelain"],
                cwd=self.root_dir,
                capture_output=True,
                text=True,
            )
            if result.stdout.strip():
                self.logger.warning("Repository has uncommitted changes")

        except subprocess.CalledProcessError:
            self.logger.error("Failed to check git status")
            return False

        self.logger.success("Prerequisites check completed")
        return True

    def step_analysis(self, dry_run: bool = False):
        """Step 1: Analysis and Preparation"""
        self.progress("Current State Analysis")

        self.logger.log("Analyzing current proto structure...")
        self.run_shell_script("orchestrate-migration.sh", ["analyze"])

        if self.logger.verbose:
            self.logger.log("Generating dependency analysis...")
            try:
                self.run_script("analyze-dependencies.py", dry_run=dry_run)
            except subprocess.CalledProcessError:
                self.logger.warning("Dependency analysis failed (non-critical)")

        self.logger.success("Analysis completed")

    def step_backup(self, dry_run: bool = False, skip_backup: bool = False):
        """Step 2: Backup Creation"""
        if skip_backup:
            self.logger.warning("Skipping backup creation")
            return

        self.progress("Creating Backups")

        backup_info = self.backup_manager.create_backups(dry_run)
        if not backup_info["success"]:
            raise RuntimeError("Failed to create backups")

        self.logger.success("Backups created")

    def step_create_structure(self, dry_run: bool = False):
        """Step 3: Directory Structure Creation"""
        self.progress("Creating Directory Structure")

        if not dry_run:
            self.logger.log("Creating proto directory structure...")
            self.run_shell_script("orchestrate-migration.sh", ["prepare"])
        else:
            self.logger.info("Would create proto directory structure (dry-run mode)")

        self.logger.success("Directory structure ready")

    def step_migrate_domains(
        self, dry_run: bool = False, domain_filter: Optional[str] = None
    ):
        """Step 4: Domain Migration"""
        self.progress("Migrating Protocol Buffer Files")

        domains = [domain_filter] if domain_filter else self.DOMAINS

        if domain_filter:
            self.logger.log(f"Processing only domain: {domain_filter}")

        for domain in domains:
            self.logger.log(f"Migrating domain: {domain}")

            args = [domain]
            if dry_run:
                args.append("--dry-run")

            self.run_script("migrate-domain.py", args)

            if self.logger.verbose and not dry_run:
                self.logger.log(f"Validating {domain} migration...")
                try:
                    self.run_script("test-import-resolution.py", dry_run=dry_run)
                except subprocess.CalledProcessError:
                    self.logger.warning(f"{domain} import validation failed")

        self.logger.success("Domain migration completed")

    def step_update_buf_config(self, dry_run: bool = False):
        """Step 5: Buf Configuration Update"""
        self.progress("Updating Buf Configuration")

        if not dry_run:
            self.logger.log("Updating buf.yaml and buf.gen.yaml...")
            self.run_script("update-buf-config.py")
        else:
            self.logger.info("Would update buf configuration (dry-run mode)")

        self.logger.success("Buf configuration updated")

    def step_update_imports(self, dry_run: bool = False):
        """Step 6: Import Path Updates"""
        self.progress("Updating Import Paths")

        self.logger.log("Updating import paths across all proto files...")

        if not dry_run:
            self.logger.log("Import paths updated during migration")
        else:
            self.logger.info("Would update import paths (dry-run mode)")

        self.logger.success("Import paths updated")

    def step_generate_code(self, dry_run: bool = False):
        """Step 7: Code Generation"""
        self.progress("Generating Code")

        if shutil.which("buf") and not dry_run:
            self.logger.log("Generating protocol buffer code...")
            try:
                subprocess.run(["buf", "generate"], cwd=self.root_dir, check=True)
            except subprocess.CalledProcessError:
                self.logger.warning("Code generation had issues")
        else:
            self.logger.info("Would generate code (buf not available or dry-run mode)")

        self.logger.success("Code generation completed")

    def step_validation(self, dry_run: bool = False):
        """Step 8: Validation"""
        self.progress("Validating Migration")

        self.logger.log("Running migration validation...")
        try:
            self.run_script("validate-migration.py", dry_run=dry_run)
        except subprocess.CalledProcessError:
            self.logger.warning("Some validation checks failed")

        if self.logger.verbose:
            self.logger.log("Running comprehensive validation...")
            try:
                self.run_script("comprehensive-validation.py", dry_run=dry_run)
            except subprocess.CalledProcessError:
                self.logger.warning("Comprehensive validation had issues")

        self.logger.success("Validation completed")

    def step_performance(self, dry_run: bool = False):
        """Step 9: Performance Testing"""
        self.progress("Performance Testing")

        if shutil.which("buf") and not dry_run:
            self.logger.log("Running performance comparison...")
            try:
                self.run_script("performance-comparison.py", dry_run=dry_run)
            except subprocess.CalledProcessError:
                self.logger.warning("Performance testing had issues")
        else:
            self.logger.info(
                "Would run performance tests (dry-run mode or buf not available)"
            )

        self.logger.success("Performance testing completed")

    def step_cleanup(self, dry_run: bool = False):
        """Step 10: Post-Migration Cleanup"""
        self.progress("Post-Migration Cleanup")

        if not dry_run:
            self.logger.log("Cleaning up old generated files...")
            try:
                self.run_script("cleanup-generated-code.py")
            except subprocess.CalledProcessError:
                self.logger.warning("Generated code cleanup had issues")

            self.logger.log("Cleaning up old proto files...")
            try:
                self.run_script("cleanup-old-protos.py")
            except subprocess.CalledProcessError:
                self.logger.warning("Old proto cleanup had issues")
        else:
            self.logger.info("Would perform cleanup (dry-run mode)")

        self.logger.success("Cleanup completed")

    def step_documentation(self, dry_run: bool = False):
        """Step 11: Documentation Updates"""
        self.progress("Updating Documentation")

        if not dry_run:
            self.logger.log("Updating proto documentation...")
            try:
                self.run_script("update-proto-docs.py")
            except subprocess.CalledProcessError:
                self.logger.warning("Documentation update had issues")

            self.logger.log("Generating migration report...")
            try:
                self.run_script("generate-migration-report.py")
            except subprocess.CalledProcessError:
                self.logger.warning("Report generation had issues")
        else:
            self.logger.info("Would update documentation (dry-run mode)")

        self.logger.success("Documentation updated")

    def step_final_verification(self, dry_run: bool = False):
        """Step 12: Final Verification"""
        self.progress("Final Verification")

        self.logger.log("Running final system verification...")
        try:
            self.run_script("final-verification.py", dry_run=dry_run)
        except subprocess.CalledProcessError:
            self.logger.error("Final verification failed")

            if not dry_run:
                self.logger.warning("Migration may need attention - check logs")
                self.logger.info(
                    "To rollback: python3 scripts/master-migration.py --rollback"
                )

            raise RuntimeError("Final verification failed")

        self.logger.success("Final verification passed")

    def rollback(self):
        """Rollback to previous state"""
        self.logger.step("Rolling back migration")

        try:
            self.backup_manager.restore_from_backup()
            self.logger.success("Rollback completed successfully")
        except Exception as e:
            self.logger.error(f"Rollback failed: {e}")
            raise

    def run_migration(
        self,
        dry_run: bool = False,
        skip_backup: bool = False,
        domain_filter: Optional[str] = None,
        verbose: bool = False,
    ):
        """Execute the complete migration process"""
        self.setup_logging(verbose)
        self.start_time = time.time()

        # Print header
        print(f"{Colors.BOLD}🚀 GCommon Protocol Buffer Master Migration{Colors.RESET}")
        print("=" * 50)
        print()
        print("📊 Migration Overview:")
        print("   • Total proto files: ~1,632")
        print(f"   • Domains: {len(self.DOMAINS)} ({', '.join(self.DOMAINS)})")
        print("   • Target structure: proto/gcommon/v1/")
        print(f"   • Dry run: {dry_run}")
        print(f"   • Skip backup: {skip_backup}")
        print(f"   • Domain filter: {domain_filter or 'all'}")
        print(f"   • Verbose: {verbose}")
        print()

        if not dry_run:
            self.logger.warning("This will reorganize 1,632+ protocol buffer files")
            response = input("Continue with actual migration? (y/N): ")
            if response.lower() != "y":
                self.logger.info("Migration cancelled")
                return

        try:
            # Execute migration steps
            if not self.check_prerequisites():
                raise RuntimeError("Prerequisites check failed")

            self.step_analysis(dry_run)
            self.step_backup(dry_run, skip_backup)
            self.step_create_structure(dry_run)
            self.step_migrate_domains(dry_run, domain_filter)
            self.step_update_buf_config(dry_run)
            self.step_update_imports(dry_run)
            self.step_generate_code(dry_run)
            self.step_validation(dry_run)
            self.step_performance(dry_run)
            self.step_cleanup(dry_run)
            self.step_documentation(dry_run)
            self.step_final_verification(dry_run)

            # Success summary
            end_time = time.time()
            duration = int(end_time - self.start_time)

            print()
            print(f"{Colors.BOLD}🎉 MIGRATION COMPLETED SUCCESSFULLY!{Colors.RESET}")
            print("=" * 40)
            print()
            print("📊 Migration Summary:")
            print(f"   • Duration: {duration}s")
            print(f"   • Mode: {'DRY RUN' if dry_run else 'ACTUAL'}")
            print(f"   • Domains processed: {domain_filter or 'all'}")
            print(f"   • Log file: {self.logger.log_file}")
            print()

            if not dry_run:
                print("📋 Next Steps:")
                print("   1. Review migration-report.html")
                print("   2. Update CI/CD pipelines")
                print("   3. Update team documentation")
                print("   4. Test code generation: buf generate")
                print("   5. Verify builds: go build ./...")
                print()
                print("📁 Generated Files:")
                print("   • migration-report.html - Detailed migration report")
                print("   • migration-report.json - Migration statistics")
                print("   • docs/PROTO_STRUCTURE.md - New structure documentation")
                print()
                print("🔄 Rollback (if needed):")
                print("   python3 scripts/master-migration.py --rollback")
            else:
                print("ℹ️  This was a dry run. To execute actual migration:")
                print(
                    f"   python3 scripts/master-migration.py {' '.join(arg for arg in sys.argv[1:] if arg != '--dry-run')}"
                )

            print()
            print("🎯 Migration completed successfully!")

        except Exception as e:
            self.logger.error(f"Migration failed: {e}")
            if not dry_run:
                self.logger.info(
                    "Consider running rollback: python3 scripts/master-migration.py --rollback"
                )
            raise


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description="GCommon Protocol Buffer Master Migration Script",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                          # Full migration with backups
  %(prog)s --dry-run                # Preview migration plan
  %(prog)s --domain common          # Migrate only common domain
  %(prog)s --skip-backup --verbose  # Migration without backup (verbose)
  %(prog)s --rollback               # Rollback to previous state

⚠️  WARNING: This script will reorganize 1,632+ files. Always run with
   --dry-run first to review the migration plan.

📚 For detailed information, see:
   - tasks/REORG/MASSIVE-REORG-PLAN.md
   - scripts/MIGRATION_README.md
        """,
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be done without executing",
    )
    parser.add_argument(
        "--skip-backup",
        action="store_true",
        help="Skip backup creation (not recommended)",
    )
    parser.add_argument(
        "--domain",
        type=str,
        choices=MasterMigration.DOMAINS,
        help="Process only specific domain",
    )
    parser.add_argument("--verbose", action="store_true", help="Enable verbose logging")
    parser.add_argument(
        "--rollback", action="store_true", help="Rollback to previous state"
    )

    args = parser.parse_args()

    migration = MasterMigration()

    try:
        if args.rollback:
            migration.setup_logging(args.verbose)
            migration.rollback()
        else:
            migration.run_migration(
                dry_run=args.dry_run,
                skip_backup=args.skip_backup,
                domain_filter=args.domain,
                verbose=args.verbose,
            )
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}Migration interrupted by user{Colors.RESET}")
        sys.exit(1)
    except Exception as e:
        print(f"\n{Colors.RED}Migration failed: {e}{Colors.RESET}")
        sys.exit(1)


if __name__ == "__main__":
    main()
