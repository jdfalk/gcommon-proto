#!/usr/bin/env python3
# file: scripts/version_sync_manager.py
# version: 2.0.0
# guid: version-sync-manager-gcommon-system

"""
Version synchronization manager for gcommon repository ecosystem.

This script ensures strict version synchronization between:
- gcommon (protocol buffer source)
- gcommon-go (Go SDK)
- gcommon-py (Python SDK)

Features:
- Semantic versioning enforcement
- Cross-repository version validation
- Automated release coordination
- Version compatibility matrix
"""

import os
import sys
import requests
from pathlib import Path
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from datetime import datetime

@dataclass
class VersionInfo:
    """Version information for a repository."""
    repo_name: str
    current_version: str
    latest_tag: str
    commit_hash: str
    updated_at: str

@dataclass
class VersionSyncConfig:
    """Configuration for version synchronization."""
    source_repo: str = "gcommon-proto"
    target_repos: List[str] = None
    version_strategy: str = "semantic"  # semantic, date, manual
    auto_release: bool = True
    compatibility_matrix: Dict[str, List[str]] = None

    def __post_init__(self):
        if self.target_repos is None:
            self.target_repos = ["gcommon"]
        if self.compatibility_matrix is None:
            self.compatibility_matrix = {
                "gcommon-proto": ["gcommon"],
                "gcommon": ["gcommon-proto"]
            }

class VersionSyncManager:
    def __init__(self, github_token: str, org: str = "jdfalk"):
        """Initialize the version sync manager."""
        self.github_token = github_token
        self.org = org
        self.headers = {
            'Authorization': f'token {github_token}',
            'Accept': 'application/vnd.github.v3+json',
            'Content-Type': 'application/json'
        }
        self.base_url = 'https://api.github.com'
        self.config = VersionSyncConfig()

    def get_repository_version(self, repo_name: str) -> Optional[VersionInfo]:
        """Get current version information for a repository."""
        try:
            # Get latest release
            response = requests.get(
                f"{self.base_url}/repos/{self.org}/{repo_name}/releases/latest",
                headers=self.headers
            )

            if response.status_code == 200:
                release_data = response.json()
                latest_tag = release_data.get('tag_name', 'v0.0.0')
            else:
                # No releases yet, check tags
                tags_response = requests.get(
                    f"{self.base_url}/repos/{self.org}/{repo_name}/tags",
                    headers=self.headers
                )
                if tags_response.status_code == 200 and tags_response.json():
                    latest_tag = tags_response.json()[0]['name']
                else:
                    latest_tag = 'v0.0.0'

            # Get latest commit
            commits_response = requests.get(
                f"{self.base_url}/repos/{self.org}/{repo_name}/commits/main",
                headers=self.headers
            )

            if commits_response.status_code == 200:
                commit_data = commits_response.json()
                commit_hash = commit_data['sha'][:8]
                updated_at = commit_data['commit']['author']['date']
            else:
                commit_hash = 'unknown'
                updated_at = datetime.now().isoformat()

            return VersionInfo(
                repo_name=repo_name,
                current_version=latest_tag.lstrip('v'),
                latest_tag=latest_tag,
                commit_hash=commit_hash,
                updated_at=updated_at
            )

        except Exception as e:
            print(f"❌ Error getting version for {repo_name}: {e}")
            return None

    def get_all_versions(self) -> Dict[str, VersionInfo]:
        """Get version information for all repositories in the ecosystem."""
        repos = [self.config.source_repo] + self.config.target_repos
        versions = {}

        for repo in repos:
            version_info = self.get_repository_version(repo)
            if version_info:
                versions[repo] = version_info

        return versions

    def parse_semantic_version(self, version: str) -> Tuple[int, int, int]:
        """Parse semantic version string into major.minor.patch tuple."""
        version = version.lstrip('v')
        parts = version.split('.')

        try:
            major = int(parts[0]) if len(parts) > 0 else 0
            minor = int(parts[1]) if len(parts) > 1 else 0
            patch = int(parts[2]) if len(parts) > 2 else 0
            return (major, minor, patch)
        except ValueError:
            return (0, 0, 0)

    def increment_version(self, current_version: str, bump_type: str = "patch") -> str:
        """Increment version based on bump type (major, minor, patch)."""
        major, minor, patch = self.parse_semantic_version(current_version)

        if bump_type == "major":
            return f"{major + 1}.0.0"
        elif bump_type == "minor":
            return f"{major}.{minor + 1}.0"
        else:  # patch
            return f"{major}.{minor}.{patch + 1}"

    def check_version_compatibility(self, versions: Dict[str, VersionInfo]) -> Dict[str, List[str]]:
        """Check version compatibility across repositories."""
        compatibility_issues = {}

        for repo, dependencies in self.config.compatibility_matrix.items():
            if repo not in versions:
                continue

            repo_version = self.parse_semantic_version(versions[repo].current_version)
            issues = []

            for dep in dependencies:
                if dep not in versions:
                    issues.append(f"Dependency {dep} not found")
                    continue

                dep_version = self.parse_semantic_version(versions[dep].current_version)

                # Check if major versions are compatible
                if repo_version[0] != dep_version[0] and max(repo_version[0], dep_version[0]) > 0:
                    issues.append(f"Major version mismatch with {dep}: {repo_version[0]} vs {dep_version[0]}")

                # Warn about minor version differences
                if abs(repo_version[1] - dep_version[1]) > 1:
                    issues.append(f"Minor version gap with {dep}: {repo_version[1]} vs {dep_version[1]}")

            if issues:
                compatibility_issues[repo] = issues

        return compatibility_issues

    def create_release(self, repo_name: str, version: str, changelog: str = "") -> bool:
        """Create a new release for a repository."""
        tag_name = f"v{version}"

        release_data = {
            'tag_name': tag_name,
            'target_commitish': 'main',
            'name': f"Release {tag_name}",
            'body': changelog or f"Release {tag_name}\n\nAutomated release created by version sync manager.",
            'draft': False,
            'prerelease': False
        }

        response = requests.post(
            f"{self.base_url}/repos/{self.org}/{repo_name}/releases",
            headers=self.headers,
            json=release_data
        )

        if response.status_code == 201:
            print(f"✅ Created release {tag_name} for {repo_name}")
            return True
        else:
            print(f"❌ Failed to create release for {repo_name}: {response.text}")
            return False

    def trigger_sync_workflow(self, repo_name: str, source_version: str) -> bool:
        """Trigger the proto sync workflow in a target repository."""
        workflow_data = {
            'ref': 'main',
            'inputs': {
                'source_version': source_version,
                'force_sync': 'true'
            }
        }

        response = requests.post(
            f"{self.base_url}/repos/{self.org}/{repo_name}/actions/workflows/sync-protos.yml/dispatches",
            headers=self.headers,
            json=workflow_data
        )

        if response.status_code == 204:
            print(f"✅ Triggered sync workflow for {repo_name}")
            return True
        else:
            print(f"⚠️  Could not trigger sync workflow for {repo_name}: {response.status_code}")
            return False

    def sync_versions(self, bump_type: str = "patch", dry_run: bool = False) -> bool:
        """Synchronize versions across all repositories."""
        print("🔄 Starting version synchronization process...")

        # Get current versions
        versions = self.get_all_versions()
        if not versions:
            print("❌ Could not retrieve version information")
            return False

        print("\n📊 Current Version Status:")
        print("-" * 60)
        for repo, version_info in versions.items():
            print(f"{repo:15} | {version_info.current_version:10} | {version_info.commit_hash}")

        # Check compatibility
        compatibility_issues = self.check_version_compatibility(versions)
        if compatibility_issues:
            print("\n⚠️  Version Compatibility Issues:")
            for repo, issues in compatibility_issues.items():
                for issue in issues:
                    print(f"  {repo}: {issue}")

        # Determine new version based on source repo
        source_repo = self.config.source_repo
        if source_repo not in versions:
            print(f"❌ Source repository {source_repo} not found")
            return False

        current_source_version = versions[source_repo].current_version
        new_version = self.increment_version(current_source_version, bump_type)

        print("\n🎯 Planned Version Update:")
        print(f"  Source ({source_repo}): {current_source_version} → {new_version}")

        if dry_run:
            print("\n🔍 DRY RUN MODE - No changes will be made")
            print("  Use --execute to perform actual version sync")
            return True

        # Create releases and trigger syncs
        success = True

        # First, create release for source repository
        if self.config.auto_release:
            if not self.create_release(source_repo, new_version, f"Protocol buffer definitions update to v{new_version}"):
                success = False

        # Then trigger sync workflows for target repositories
        for target_repo in self.config.target_repos:
            if not self.trigger_sync_workflow(target_repo, new_version):
                success = False

        if success:
            print("\n✅ Version synchronization completed successfully!")
            print(f"   All repositories should now be synced to version {new_version}")
        else:
            print("\n❌ Version synchronization encountered errors")
            print("   Check the output above for details")

        return success

    def generate_compatibility_matrix(self) -> str:
        """Generate a compatibility matrix report."""
        versions = self.get_all_versions()
        if not versions:
            return "❌ Could not retrieve version information"

        report = "# gcommon Ecosystem Version Compatibility Matrix\n\n"
        report += f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}\n\n"

        report += "## Current Versions\n\n"
        report += "| Repository | Version | Commit | Last Updated |\n"
        report += "|------------|---------|--------|-------------|\n"

        for repo, version_info in versions.items():
            report += f"| {repo} | {version_info.current_version} | {version_info.commit_hash} | {version_info.updated_at[:10]} |\n"

        compatibility_issues = self.check_version_compatibility(versions)

        if compatibility_issues:
            report += "\n## Compatibility Issues\n\n"
            for repo, issues in compatibility_issues.items():
                report += f"### {repo}\n"
                for issue in issues:
                    report += f"- ⚠️ {issue}\n"
                report += "\n"
        else:
            report += "\n## ✅ All repositories are compatible\n\n"

        report += "## Synchronization Strategy\n\n"
        report += f"- Source Repository: {self.config.source_repo}\n"
        report += f"- Target Repositories: {', '.join(self.config.target_repos)}\n"
        report += f"- Version Strategy: {self.config.version_strategy}\n"
        report += f"- Auto Release: {self.config.auto_release}\n"

        return report

def main():
    """Main entry point for version sync manager."""
    import argparse

    parser = argparse.ArgumentParser(description="gcommon version synchronization manager")
    parser.add_argument('--token', help="GitHub token (or use GITHUB_TOKEN env var)")
    parser.add_argument('--org', default="jdfalk", help="GitHub organization")
    parser.add_argument('command', choices=['status', 'sync', 'matrix'], help="Command to execute")
    parser.add_argument('--bump', choices=['major', 'minor', 'patch'], default='patch',
                       help="Version bump type for sync command")
    parser.add_argument('--dry-run', action='store_true', help="Show what would be done without executing")
    parser.add_argument('--execute', action='store_true', help="Actually perform the sync (default is dry run)")

    args = parser.parse_args()

    # Get GitHub token
    github_token = args.token
    if not github_token:
        # Try to get token from gh CLI
        try:
            import subprocess
            result = subprocess.run(['gh', 'auth', 'token'], capture_output=True, text=True, check=True)
            github_token = result.stdout.strip()
            print("✅ Using GitHub token from gh CLI")
        except (subprocess.CalledProcessError, FileNotFoundError):
            # Fall back to environment variables
            github_token = os.environ.get('GITHUB_TOKEN') or os.environ.get('GH_TOKEN')
            if github_token:
                print("✅ Using GitHub token from environment variable")

    if not github_token:
        print("❌ Error: GitHub token is required")
        print("Options:")
        print("  1. Use --token argument")
        print("  2. Run 'gh auth login' to authenticate with gh CLI")
        print("  3. Set GITHUB_TOKEN environment variable")
        sys.exit(1)

    # Create version sync manager
    manager = VersionSyncManager(github_token, args.org)

    try:
        if args.command == 'status':
            versions = manager.get_all_versions()
            if versions:
                print("\n📊 gcommon Ecosystem Version Status")
                print("=" * 50)
                for repo, version_info in versions.items():
                    print(f"{repo:15} | v{version_info.current_version:10} | {version_info.commit_hash} | {version_info.updated_at[:10]}")

                compatibility_issues = manager.check_version_compatibility(versions)
                if compatibility_issues:
                    print("\n⚠️  Compatibility Issues Found:")
                    for repo, issues in compatibility_issues.items():
                        for issue in issues:
                            print(f"  {repo}: {issue}")
                else:
                    print("\n✅ All repositories are version-compatible")
            else:
                print("❌ Could not retrieve version information")
                sys.exit(1)

        elif args.command == 'sync':
            # Default to dry run unless --execute is specified
            dry_run = not args.execute
            success = manager.sync_versions(args.bump, dry_run)
            sys.exit(0 if success else 1)

        elif args.command == 'matrix':
            report = manager.generate_compatibility_matrix()
            print(report)

            # Optionally save to file
            output_file = Path("compatibility-matrix.md")
            with open(output_file, 'w') as f:
                f.write(report)
            print(f"\n📄 Report saved to {output_file}")

    except KeyboardInterrupt:
        print("\n⚠️  Operation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
