#!/usr/bin/env python3
# file: scripts/version_sync_manager.py
# version: 3.0.1
# guid: b1b9c1e2-d3e4-5f6a-7b8c-9d0e1f2a3b4c

"""
Enhanced version synchronization manager for gcommon repository ecosystem.

This script ensures strict version synchronization between:
- gcommon-proto (protocol buffer source)
- gcommon (Go consumer)
- Other consuming repositories

Features:
- Semantic versioning enforcement with intelligent commit analysis
- GitHub Copilot CLI integration for intelligent version bump determination
- Buf Schema Registry integration with consolidated multi-label push
- Cross-repository version validation
- Automated GitHub release creation
- Version co            # Step 5: Repository Updates
            print(f"\n🔄 Step 5: Repository Updates")
            print("-" * 30)

            related_repos = ['gcommon']  # Only gcommon repository now

            if dry_run:
                print(f"   Would update {len(related_repos)} related repository:")
                for repo in related_repos:
                    print(f"     - {repo}")
            else:
                print(f"   Updating {len(related_repos)} related repository...")
                for repo in related_repos:
                    success = self.trigger_sync_workflow(repo, new_version)
                    if success:
                        print(f"     ✅ {repo}")
                    else:
                        print(f"     ❌ {repo} (failed)")
- Simple 'generate' command for complete automation
- Automatic floating tag management (preserves patch releases)
"""

import os
import sys
import subprocess
import re
import requests
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any
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

@dataclass
class CommitAnalysis:
    """Analysis of commits since last version."""
    breaking_changes: List[str]
    features: List[str]
    fixes: List[str]
    suggested_bump: str  # major, minor, patch

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

    def run_command(self, cmd: List[str], capture_output: bool = True, input: Optional[str] = None) -> subprocess.CompletedProcess:
        """Run a command and return the result."""
        try:
            return subprocess.run(cmd, capture_output=capture_output, text=True, check=True, input=input)
        except subprocess.CalledProcessError as e:
            print(f"❌ Command failed: {' '.join(cmd)}")
            print(f"   Error: {e.stderr if e.stderr else str(e)}")
            raise

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

    def bump_version(self, version: str, bump_type: str) -> str:
        """Bump a semantic version string by the specified type."""
        # Ensure version starts with 'v'
        if not version.startswith('v'):
            clean_version = version
        else:
            clean_version = version[1:]  # Remove 'v' prefix

        # Use existing increment_version method
        new_version = self.increment_version(clean_version, bump_type)

        # Return with 'v' prefix
        return f"v{new_version}"

    def get_next_available_version(self, attempted_version: str) -> str:
        """Get the next available version if the attempted version already exists."""
        # Parse the attempted version
        clean_version = attempted_version.lstrip('v')
        major, minor, patch = self.parse_semantic_version(clean_version)

        # Keep incrementing patch version until we find one that doesn't exist
        while True:
            candidate = f"v{major}.{minor}.{patch}"
            try:
                result = self.run_command(['git', 'tag', '--list', candidate])
                if not result.stdout.strip():
                    # Tag doesn't exist, use this version
                    return candidate
            except subprocess.CalledProcessError:
                # Tag doesn't exist, use this version
                return candidate

            # Increment patch and try again
            patch += 1
            if patch > 50:  # Safety valve to prevent infinite loops
                raise Exception(f"Could not find available version after {candidate}")

    def get_git_tags(self) -> Tuple[List[str], List[str], List[str]]:
        """Get all git tags categorized by type."""
        try:
            result = self.run_command(['git', 'tag', '--list'])
            all_tags = [tag for tag in result.stdout.strip().split('\n') if tag and re.match(r'^v\d+(\.\d+)*$', tag)]
            all_tags.sort(key=lambda x: [int(part) for part in x.lstrip('v').split('.')])

            major_tags = [tag for tag in all_tags if re.match(r'^v\d+$', tag)]
            minor_tags = [tag for tag in all_tags if re.match(r'^v\d+\.\d+$', tag)]
            patch_tags = [tag for tag in all_tags if re.match(r'^v\d+\.\d+\.\d+$', tag)]

            return major_tags, minor_tags, patch_tags
        except subprocess.CalledProcessError:
            return [], [], []

    def analyze_commits_since_tag(self, tag: str) -> CommitAnalysis:
        """Analyze commits since the last tag to determine version bump type."""
        try:
            # Get commits since the tag
            result = self.run_command(['git', 'log', f'{tag}..HEAD', '--oneline'])
            commits = result.stdout.strip().split('\n') if result.stdout.strip() else []

            breaking_changes = []
            features = []
            fixes = []

            for commit in commits:
                if not commit:
                    continue

                # Look for conventional commit patterns
                if re.search(r'^[a-f0-9]+\s+.*!:', commit) or 'BREAKING CHANGE' in commit:
                    breaking_changes.append(commit)
                elif re.search(r'^[a-f0-9]+\s+feat(\([^)]*\))?:', commit):
                    features.append(commit)
                elif re.search(r'^[a-f0-9]+\s+fix(\([^)]*\))?:', commit):
                    fixes.append(commit)
                else:
                    # Default to fix for non-conventional commits
                    fixes.append(commit)

            # Determine suggested bump
            if breaking_changes:
                suggested_bump = "major"
            elif features:
                suggested_bump = "minor"
            else:
                suggested_bump = "patch"

            return CommitAnalysis(
                breaking_changes=breaking_changes,
                features=features,
                fixes=fixes,
                suggested_bump=suggested_bump
            )

        except subprocess.CalledProcessError:
            return CommitAnalysis([], [], [], "patch")

    def analyze_commits_with_copilot(self, tag: str) -> str:
        """Use GitHub Copilot CLI to analyze commits and suggest version bump."""
        try:
            # Get commit messages since tag
            result = self.run_command(['git', 'log', f'{tag}..HEAD', '--pretty=format:%s'])
            commit_messages = result.stdout.strip()

            if not commit_messages:
                return "patch"

            # Try to use GitHub Copilot CLI
            prompt = f"""
Based on these commit messages, determine if this should be a major, minor, or patch version bump:

{commit_messages}

Consider:
- Breaking changes = major
- New features = minor
- Bug fixes = patch

Respond with just one word: major, minor, or patch
"""

            try:
                # Try gh copilot suggest first (but handle crashes gracefully)
                print("   Trying GitHub Copilot CLI for intelligent analysis...")
                copilot_result = self.run_command(['gh', 'copilot', 'suggest', '-t', 'shell'], input=prompt)
                response = copilot_result.stdout.lower()

                if 'major' in response:
                    print("   ✅ Copilot suggests: major")
                    return 'major'
                elif 'minor' in response:
                    print("   ✅ Copilot suggests: minor")
                    return 'minor'
                else:
                    print("   ✅ Copilot suggests: patch")
                    return 'patch'

            except (subprocess.CalledProcessError, Exception) as e:
                print(f"   ⚠️  GitHub Copilot CLI failed (error: {str(e)[:100]}...)")
                print("   📋 Falling back to conventional commit analysis...")
                # Fall back to conventional commit analysis
                analysis = self.analyze_commits_since_tag(tag)
                print(f"   ✅ Conventional analysis suggests: {analysis.suggested_bump}")
                return analysis.suggested_bump

        except subprocess.CalledProcessError:
            return "patch"

    def update_floating_tags(self, new_version: str) -> bool:
        """Update floating tags (major/minor) to point to current commit."""
        try:
            major, minor, patch = self.parse_semantic_version(new_version)
            major_tag = f"v{major}"
            minor_tag = f"v{major}.{minor}"

            # Update major tag
            print(f"   Updating floating tag: {major_tag}")
            self.run_command(['git', 'tag', '-f', major_tag, '-m', f'{major_tag} - floating tag update'])

            # Update minor tag
            print(f"   Updating floating tag: {minor_tag}")
            self.run_command(['git', 'tag', '-f', minor_tag, '-m', f'{minor_tag} - floating tag update'])

            return True
        except subprocess.CalledProcessError:
            print("❌ Failed to update floating tags")
            return False

    def push_to_buf_registry(self, new_version: str = None, dry_run: bool = False) -> bool:
        """Push to Buf Schema Registry with consolidated multi-label command - only new version + floating labels."""
        try:
            # Build label list - only floating tags and new version
            labels = []

            # Add new version label if provided
            if new_version:
                labels.append(new_version)
                print(f"   📌 Adding NEW version label: {new_version}")

            # Add floating/special labels that should always be updated
            floating_labels = ['main', 'latest', 'stable', 'pb-packages']

            # Add major/minor floating tags if we have a new version
            if new_version:
                try:
                    major, minor, patch = self.parse_semantic_version(new_version.lstrip('v'))
                    floating_labels.extend([f"v{major}", f"v{major}.{minor}"])
                    print(f"   🔄 Adding floating tags: v{major}, v{major}.{minor}")
                except:
                    pass

            labels.extend(floating_labels)

            if not labels:
                print("⚠️  No labels found for buf push")
                return True

            # Build consolidated buf push command
            cmd = ['buf', 'push']
            for label in labels:
                if label:
                    cmd.extend(['--label', label])

            print(f"🌐 Pushing to Buf Schema Registry with {len(labels)} labels...")
            print(f"   Labels: {', '.join(labels)}")
            print("   ✅ SAFE MODE: Only pushing new version + floating labels (preserving old versions)")

            if dry_run:
                print(f"   DRY RUN: Would execute: {' '.join(cmd)}")
                return True

            self.run_command(cmd)
            print("✅ Successfully pushed to Buf Schema Registry")
            return True

        except subprocess.CalledProcessError:
            print("❌ Failed to push to Buf Schema Registry")
            return False

    def get_latest_release(self) -> Optional[Dict[str, Any]]:
        """Get the latest release from GitHub, or fallback to latest git tag."""
        try:
            # First try GitHub releases
            response = requests.get(
                f"{self.base_url}/repos/{self.org}/gcommon-proto/releases/latest",
                headers=self.headers
            )
            if response.status_code == 200:
                return response.json()

            # Fallback to git tags if no GitHub release exists
            print("   No GitHub releases found, checking git tags...")
            try:
                # Get all tags and find the latest semantic version tag
                result = self.run_command(['git', 'tag', '--list', '--sort=-version:refname'])
                tags = [tag for tag in result.stdout.strip().split('\n') if tag and re.match(r'^v\d+(\.\d+)*$', tag)]

                if tags:
                    latest_tag = tags[0]  # Already sorted, take the first (latest)
                    print(f"   Using latest git tag: {latest_tag}")
                    return {'tag_name': latest_tag}

            except subprocess.CalledProcessError:
                pass

            return None
        except Exception as e:
            print(f"   Warning: Could not get latest release: {e}")
            return None

    def create_github_release(self, tag_name: str, name: str, body: str, prerelease: bool = False) -> Optional[Dict[str, Any]]:
        """Create a GitHub release."""
        try:
            release_data = {
                'tag_name': tag_name,
                'target_commitish': 'main',
                'name': name,
                'body': body,
                'draft': False,
                'prerelease': prerelease
            }

            response = requests.post(
                f"{self.base_url}/repos/{self.org}/gcommon-proto/releases",
                headers=self.headers,
                json=release_data
            )

            if response.status_code == 201:
                return response.json()
            else:
                print(f"❌ Failed to create GitHub release: {response.text}")
                return None

        except Exception as e:
            print(f"❌ Error creating GitHub release: {e}")
            return None

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

    def generate_everything(self, bump_type: Optional[str] = None, dry_run: bool = False) -> bool:
        """
        Comprehensive 'generate' command that handles everything automatically.

        Args:
            bump_type: Optional version bump type ('major', 'minor', 'patch', 'auto')
            dry_run: If True, show what would be done without executing

        Returns:
            bool: True if successful, False otherwise
        """
        print("🚀 Starting comprehensive version management and release generation...")
        print("=" * 70)

        try:
            # Step 1: Get latest release and determine version bump
            print("\n📋 Step 1: Version Analysis")
            print("-" * 30)

            latest_release = self.get_latest_release()
            current_version = latest_release['tag_name'] if latest_release else "v0.0.0"
            print(f"   Current version: {current_version}")

            # Determine bump type
            if not bump_type or bump_type == 'auto':
                print("   Analyzing commits for automatic version bump...")
                suggested_bump = self.analyze_commits_with_copilot(current_version)
                print(f"   Suggested bump type: {suggested_bump}")
                bump_type = suggested_bump

            new_version = self.bump_version(current_version, bump_type)
            print(f"   New version: {new_version}")

            if dry_run:
                print("\n🔍 DRY RUN MODE - No changes will be made")
                print("-" * 40)

            # Step 2: Create and push git tag
            print(f"\n🏷️  Step 2: Git Tag Management")
            print("-" * 30)

            if dry_run:
                print(f"   Would create tag: {new_version}")
                print(f"   Would update floating tags")
                print(f"   Would push tags to origin")
            else:
                # Check if tag already exists
                try:
                    self.run_command(['git', 'tag', '--list', new_version])
                    existing_tags = self.run_command(['git', 'tag', '--list', new_version]).stdout.strip()
                    if existing_tags:
                        print(f"   ⚠️  Tag {new_version} already exists, skipping tag creation...")
                        print("   📋 Checking if we need to increment to next version...")

                        # Get next available version
                        next_version = self.get_next_available_version(new_version)
                        print(f"   ✅ Using next available version: {next_version}")
                        new_version = next_version

                except subprocess.CalledProcessError:
                    # Tag doesn't exist, proceed normally
                    pass

                print(f"   Creating tag: {new_version}")
                result = self.run_command(['git', 'tag', new_version, '-m', f'Release {new_version}'])

                # Update floating tags
                if not self.update_floating_tags(new_version):
                    print("⚠️  Warning: Failed to update floating tags (continuing...)")

                # Push all tags
                print("   Pushing tags to origin...")
                self.run_command(['git', 'push', 'origin', '--tags', '--force'])
                print("✅ Tags created and pushed successfully")

            # Step 3: Create GitHub release
            print(f"\n📦 Step 3: GitHub Release Creation")
            print("-" * 30)

            if dry_run:
                print(f"   Would create GitHub release: {new_version}")
            else:
                commit_analysis = self.analyze_commits_since_tag(current_version)
                changelog = self.generate_changelog(commit_analysis)

                release = self.create_github_release(
                    tag_name=new_version,
                    name=f"Release {new_version}",
                    body=changelog,
                    prerelease=False
                )

                if release:
                    print(f"✅ GitHub release created: {release['html_url']}")
                else:
                    print("⚠️  Warning: Failed to create GitHub release (continuing...)")

            # Step 4: Push to Buf Schema Registry
            print(f"\n🌐 Step 4: Buf Schema Registry")
            print("-" * 30)

            if not self.push_to_buf_registry(new_version=new_version, dry_run=dry_run):
                print("⚠️  Warning: Failed to push to Buf Schema Registry")

            # Step 5: Update related repositories
            print(f"\n🔄 Step 5: Repository Updates")
            print("-" * 30)

            related_repos = ['gcommon']  # Only gcommon repository now

            if dry_run:
                print(f"   Would update {len(related_repos)} related repository:")
                for repo in related_repos:
                    print(f"     - {repo}")
            else:
                print(f"   Updating {len(related_repos)} related repository...")
                for repo in related_repos:
                    success = self.trigger_sync_workflow(repo, new_version)
                    if success:
                        print(f"     ✅ {repo}")
                    else:
                        print(f"     ❌ {repo} (failed)")

            # Summary
            print(f"\n🎉 Summary")
            print("=" * 70)
            print(f"   Version: {current_version} → {new_version}")
            print(f"   Bump type: {bump_type}")
            if dry_run:
                print(f"   Mode: DRY RUN (no changes made)")
            else:
                print(f"   Changes applied successfully!")
            print(f"   Related repos: {len(related_repos)} repository")

            return True

        except Exception as e:
            print(f"\n❌ Generation failed: {e}")
            return False

    def generate_changelog(self, commit_analysis: CommitAnalysis) -> str:
        """Generate a changelog from commit analysis."""
        changelog = []

        if commit_analysis.breaking_changes:
            changelog.append("## Breaking Changes")
            for commit in commit_analysis.breaking_changes:
                changelog.append(f"- {commit}")
            changelog.append("")

        if commit_analysis.features:
            changelog.append("## Features")
            for commit in commit_analysis.features:
                changelog.append(f"- {commit}")
            changelog.append("")

        if commit_analysis.fixes:
            changelog.append("## Bug Fixes")
            for commit in commit_analysis.fixes:
                changelog.append(f"- {commit}")
            changelog.append("")

        return "\n".join(changelog)

def main():
    """Main entry point for version sync manager."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Comprehensive version management and release automation for gcommon ecosystem",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s generate                    # Auto-detect version bump and handle everything
  %(prog)s generate --bump minor      # Force minor version bump
  %(prog)s generate --dry-run         # Show what would be done
  %(prog)s release --version v1.2.3   # Create specific version release
  %(prog)s update-repos --version v1.2.3  # Update related repositories
        """
    )
    parser.add_argument('--token', help="GitHub token (or use GITHUB_TOKEN env var)")
    parser.add_argument('--org', default="jdfalk", help="GitHub organization")
    parser.add_argument('command', choices=['generate', 'status', 'sync', 'matrix'], help="Command to execute")
    parser.add_argument('--bump', choices=['major', 'minor', 'patch', 'auto'], default='auto',
                       help="Version bump type (auto will analyze commits)")
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
        if args.command == 'generate':
            success = manager.generate_everything(
                bump_type=args.bump if args.bump != 'auto' else None,
                dry_run=args.dry_run
            )
            sys.exit(0 if success else 1)

        elif args.command == 'status':
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
