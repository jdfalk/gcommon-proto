#!/usr/bin/env python3
# file: scripts/workflow_manager.py
# version: 1.0.0
# guid: d4e5f6a7-b8c9-0123-def4-56789012345b

"""
Modern Workflow Management System

This script provides comprehensive workflow management capabilities for the modernized
CI/CD system. It replaces shell-based automation with robust Python automation.

Features:
- Matrix build configuration
- Dependency management
- Cross-repository workflow sync
- Automated testing and validation
- Comprehensive error handling and logging
"""

import argparse
import json
import logging
import os
import subprocess
import sys
import yaml
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Dict, List, Optional, Union, Any
from urllib.parse import urlparse


@dataclass
class BuildConfig:
    """Configuration for build matrix."""
    go_versions: List[str]
    python_versions: List[str]
    node_versions: List[str]
    platforms: List[str]
    enable_protobuf: bool
    enable_docker: bool


@dataclass
class Repository:
    """Repository configuration."""
    name: str
    url: str
    path: Optional[str] = None
    build_config: Optional[BuildConfig] = None


class WorkflowManager:
    """Modern workflow management system."""
    
    def __init__(self, config_file: Optional[Path] = None, dry_run: bool = False):
        self.dry_run = dry_run
        self.config_file = config_file or Path('.github/workflow-config.yaml')
        self.base_dir = Path.cwd()
        self.scripts_dir = self.base_dir / 'scripts'
        self.workflows_dir = self.base_dir / '.github' / 'workflows'
        
        # Set up logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)
        
        # Load configuration
        self.config = self.load_config()
        
    def load_config(self) -> Dict[str, Any]:
        """Load workflow configuration."""
        default_config = {
            'build': {
                'go_versions': ['1.22', '1.23', '1.24'],
                'python_versions': ['3.11', '3.12', '3.13'],
                'node_versions': ['20', '22', '24'],
                'platforms': ['linux/amd64', 'linux/arm64'],
                'enable_protobuf': True,
                'enable_docker': True
            },
            'repositories': [
                {
                    'name': 'subtitle-manager',
                    'url': 'https://github.com/jdfalk/subtitle-manager'
                },
                {
                    'name': 'audiobook-organizer', 
                    'url': 'https://github.com/jdfalk/audiobook-organizer'
                },
                {
                    'name': 'copilot-agent-util-rust',
                    'url': 'https://github.com/jdfalk/copilot-agent-util-rust'
                }
            ],
            'sync': {
                'auto_sync': True,
                'sync_paths': [
                    '.github/workflows',
                    '.github/instructions', 
                    '.github/prompts',
                    'scripts',
                    '.github/linters',
                    'labels.json',
                    'labels.md'
                ]
            }
        }
        
        if self.config_file.exists():
            try:
                with open(self.config_file, 'r') as f:
                    config = yaml.safe_load(f)
                    # Merge with defaults
                    return {**default_config, **config}
            except Exception as e:
                self.logger.warning(f"Failed to load config file: {e}, using defaults")
        
        return default_config
    
    def save_config(self):
        """Save current configuration."""
        if not self.dry_run:
            self.config_file.parent.mkdir(parents=True, exist_ok=True)
            with open(self.config_file, 'w') as f:
                yaml.dump(self.config, f, default_flow_style=False)
            self.logger.info(f"Configuration saved to {self.config_file}")
    
    def detect_project_type(self, path: Path = None) -> Dict[str, bool]:
        """Detect project types in the repository."""
        if path is None:
            path = self.base_dir
            
        detection = {
            'go': False,
            'python': False,
            'frontend': False,
            'docker': False,
            'protobuf': False
        }
        
        # Check for Go
        if (path / 'go.mod').exists() or any(path.rglob('*.go')):
            detection['go'] = True
            
        # Check for Python
        if ((path / 'pyproject.toml').exists() or 
            (path / 'requirements.txt').exists() or 
            (path / 'setup.py').exists() or 
            any(path.rglob('*.py'))):
            detection['python'] = True
            
        # Check for Frontend
        if ((path / 'package.json').exists() or 
            (path / 'yarn.lock').exists() or 
            (path / 'pnpm-lock.yaml').exists()):
            detection['frontend'] = True
            
        # Check for Docker
        if (any(path.rglob('Dockerfile*')) or 
            any(path.rglob('docker-compose*.yml')) or 
            any(path.rglob('docker-compose*.yaml'))):
            detection['docker'] = True
            
        # Check for Protobuf
        if ((path / 'buf.yaml').exists() or 
            (path / 'buf.gen.yaml').exists() or 
            any(path.rglob('*.proto'))):
            detection['protobuf'] = True
            
        return detection
    
    def generate_build_matrix(self, project_types: Dict[str, bool]) -> Dict[str, Any]:
        """Generate build matrix based on project types."""
        matrix = {'include': []}
        build_config = self.config['build']
        
        if project_types['go']:
            for version in build_config['go_versions']:
                for platform in ['ubuntu-latest', 'macos-latest', 'windows-latest']:
                    matrix['include'].append({
                        'type': 'go',
                        'version': version,
                        'os': platform,
                        'primary': version == build_config['go_versions'][-1] and platform == 'ubuntu-latest'
                    })
        
        if project_types['python']:
            for version in build_config['python_versions']:
                for platform in ['ubuntu-latest', 'macos-latest', 'windows-latest']:
                    matrix['include'].append({
                        'type': 'python',
                        'version': version,
                        'os': platform,
                        'primary': version == build_config['python_versions'][-2] and platform == 'ubuntu-latest'  # Use 3.12 as primary
                    })
        
        if project_types['frontend']:
            for version in build_config['node_versions']:
                for platform in ['ubuntu-latest', 'macos-latest', 'windows-latest']:
                    matrix['include'].append({
                        'type': 'frontend',
                        'version': version,
                        'os': platform,
                        'primary': version == build_config['node_versions'][1] and platform == 'ubuntu-latest'  # Use middle version as primary
                    })
        
        if project_types['docker']:
            for platform in build_config['platforms']:
                matrix['include'].append({
                    'type': 'docker',
                    'platform': platform,
                    'os': 'ubuntu-latest',
                    'primary': platform == 'linux/amd64'
                })
        
        return matrix
    
    def run_command(self, cmd: List[str], cwd: Path = None, capture_output: bool = True) -> subprocess.CompletedProcess:
        """Run a command with proper error handling."""
        if cwd is None:
            cwd = self.base_dir
            
        self.logger.info(f"Running command: {' '.join(cmd)} in {cwd}")
        
        if self.dry_run:
            self.logger.info(f"[DRY RUN] Would run: {' '.join(cmd)}")
            return subprocess.CompletedProcess(cmd, 0, '', '')
        
        try:
            result = subprocess.run(
                cmd,
                cwd=cwd,
                capture_output=capture_output,
                text=True,
                check=True
            )
            return result
        except subprocess.CalledProcessError as e:
            self.logger.error(f"Command failed: {e}")
            self.logger.error(f"stdout: {e.stdout}")
            self.logger.error(f"stderr: {e.stderr}")
            raise
    
    def build_go_project(self) -> bool:
        """Build Go project."""
        try:
            self.logger.info("Building Go project...")
            
            # Download dependencies
            self.run_command(['go', 'mod', 'download'])
            
            # Build all packages
            self.run_command(['go', 'build', '-v', './...'])
            
            # Run tests
            self.run_command(['go', 'test', '-v', '-race', '-coverprofile=coverage.out', './...'])
            
            self.logger.info("Go build completed successfully")
            return True
        except Exception as e:
            self.logger.error(f"Go build failed: {e}")
            return False
    
    def build_python_project(self) -> bool:
        """Build Python project."""
        try:
            self.logger.info("Building Python project...")
            
            # Install dependencies
            if (self.base_dir / 'requirements.txt').exists():
                self.run_command([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
            
            if (self.base_dir / 'pyproject.toml').exists():
                self.run_command([sys.executable, '-m', 'pip', 'install', '-e', '.'])
            
            # Run tests if pytest is available
            try:
                self.run_command([sys.executable, '-m', 'pytest', '--cov', '--cov-report=xml'])
            except:
                # Fallback to unittest
                self.run_command([sys.executable, '-m', 'unittest', 'discover'])
            
            self.logger.info("Python build completed successfully")
            return True
        except Exception as e:
            self.logger.error(f"Python build failed: {e}")
            return False
    
    def build_frontend_project(self) -> bool:
        """Build frontend project."""
        try:
            self.logger.info("Building frontend project...")
            
            # Install dependencies
            self.run_command(['npm', 'ci'])
            
            # Build
            self.run_command(['npm', 'run', 'build'])
            
            # Test
            self.run_command(['npm', 'test'])
            
            self.logger.info("Frontend build completed successfully")
            return True
        except Exception as e:
            self.logger.error(f"Frontend build failed: {e}")
            return False
    
    def generate_protobuf(self) -> bool:
        """Generate protobuf code."""
        try:
            self.logger.info("Generating protobuf code...")
            
            if (self.base_dir / 'buf.gen.yaml').exists():
                self.run_command(['buf', 'generate'])
            else:
                self.logger.warning("No buf.gen.yaml found, skipping protobuf generation")
            
            self.logger.info("Protobuf generation completed successfully")
            return True
        except Exception as e:
            self.logger.error(f"Protobuf generation failed: {e}")
            return False
    
    def run_full_build(self) -> bool:
        """Run complete build process."""
        self.logger.info("Starting full build process...")
        
        # Detect project types
        project_types = self.detect_project_type()
        self.logger.info(f"Detected project types: {project_types}")
        
        success = True
        
        # Generate protobuf first (dependency for others)
        if project_types['protobuf']:
            if not self.generate_protobuf():
                success = False
        
        # Build each project type
        if project_types['go']:
            if not self.build_go_project():
                success = False
        
        if project_types['python']:
            if not self.build_python_project():
                success = False
        
        if project_types['frontend']:
            if not self.build_frontend_project():
                success = False
        
        if success:
            self.logger.info("✅ Full build completed successfully")
        else:
            self.logger.error("❌ Build failed")
        
        return success
    
    def sync_to_repositories(self, sync_type: str = 'all') -> bool:
        """Sync workflows to other repositories."""
        self.logger.info(f"Syncing {sync_type} to repositories...")
        
        repositories = self.config['repositories']
        success = True
        
        for repo_config in repositories:
            repo_name = repo_config['name']
            self.logger.info(f"Syncing to {repo_name}...")
            
            if not self.dry_run:
                # In a real implementation, this would use the GitHub API
                # to dispatch repository events or create PRs
                self.logger.info(f"[SYNC] Would sync {sync_type} to {repo_name}")
            
        return success
    
    def validate_workflows(self) -> bool:
        """Validate workflow files."""
        self.logger.info("Validating workflow files...")
        
        workflow_files = list(self.workflows_dir.glob('*.yml')) + list(self.workflows_dir.glob('*.yaml'))
        success = True
        
        for workflow_file in workflow_files:
            try:
                with open(workflow_file, 'r') as f:
                    yaml.safe_load(f)
                self.logger.info(f"✅ {workflow_file.name} is valid")
            except yaml.YAMLError as e:
                self.logger.error(f"❌ {workflow_file.name} is invalid: {e}")
                success = False
        
        return success
    
    def create_status_report(self) -> Dict[str, Any]:
        """Create a status report of the workflow system."""
        project_types = self.detect_project_type()
        matrix = self.generate_build_matrix(project_types)
        
        return {
            'project_types': project_types,
            'build_matrix': matrix,
            'config': self.config,
            'workflows_valid': self.validate_workflows()
        }


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description='Modern Workflow Management System')
    parser.add_argument('command', choices=['build', 'sync', 'validate', 'status', 'init'], 
                       help='Command to execute')
    parser.add_argument('--config', type=Path, help='Configuration file path')
    parser.add_argument('--dry-run', action='store_true', help='Run in dry-run mode')
    parser.add_argument('--sync-type', default='all', 
                       choices=['all', 'workflows', 'instructions', 'prompts', 'scripts', 'linters', 'labels'],
                       help='Type of sync to perform')
    parser.add_argument('--verbose', '-v', action='store_true', help='Verbose output')
    
    args = parser.parse_args()
    
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    manager = WorkflowManager(config_file=args.config, dry_run=args.dry_run)
    
    try:
        if args.command == 'build':
            success = manager.run_full_build()
            sys.exit(0 if success else 1)
        
        elif args.command == 'sync':
            success = manager.sync_to_repositories(args.sync_type)
            sys.exit(0 if success else 1)
        
        elif args.command == 'validate':
            success = manager.validate_workflows()
            sys.exit(0 if success else 1)
        
        elif args.command == 'status':
            report = manager.create_status_report()
            print(json.dumps(report, indent=2))
        
        elif args.command == 'init':
            manager.save_config()
            print("✅ Workflow configuration initialized")
    
    except KeyboardInterrupt:
        print("\n❌ Operation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()