#!/usr/bin/env python3
# file: setup_github_projects_automation.py
# version: 1.0.0
# guid: 5f6a7b8c-9d0e-1f2a-3b4c-5d6e7f8a9b0c

"""
Setup automated GitHub Projects workflows for label-based issue assignment.

Creates GitHub Actions workflows to automatically add issues to projects
based on their labels, addressing the missing automation the user identified.
"""

import os
from typing import Dict, List

import yaml


class GitHubProjectsAutomation:
    """Setup automated project assignment workflows."""

    def __init__(self, repo_path: str):
        self.repo_path = repo_path
        self.workflows_dir = os.path.join(repo_path, ".github", "workflows")

        # Project mapping based on labels
        self.project_mappings = {
            "protobuf-implementation": {
                "project_id": "1",  # This would be the actual project ID
                "labels": ["type:protobuf", "epic:protobuf"],
                "description": "Protobuf Implementation Epic",
            },
            "module-auth": {
                "project_id": "2",
                "labels": ["module:auth"],
                "description": "Authentication Module",
            },
            "module-web": {
                "project_id": "3",
                "labels": ["module:web"],
                "description": "Web Services Module",
            },
            "module-queue": {
                "project_id": "4",
                "labels": ["module:queue"],
                "description": "Message Queue Module",
            },
            "module-config": {
                "project_id": "5",
                "labels": ["module:config"],
                "description": "Configuration Module",
            },
            "high-priority": {
                "project_id": "6",
                "labels": ["priority:high", "priority:critical"],
                "description": "High Priority Issues",
            },
        }

    def create_project_assignment_workflow(self) -> str:
        """Create GitHub Actions workflow for automatic project assignment."""

        workflow_content = {
            "name": "Auto-assign Issues to Projects",
            "on": {
                "issues": {"types": ["opened", "labeled", "unlabeled"]},
                "pull_request": {"types": ["opened", "labeled", "unlabeled"]},
            },
            "jobs": {
                "assign-to-projects": {
                    "runs-on": "ubuntu-latest",
                    "steps": [
                        {"name": "Checkout", "uses": "actions/checkout@v4"},
                        {
                            "name": "Auto-assign to Protobuf Project",
                            "if": "contains(github.event.issue.labels.*.name, 'type:protobuf') || contains(github.event.issue.labels.*.name, 'epic:protobuf')",
                            "uses": "alex-page/github-project-automation-plus@v0.9.0",
                            "with": {
                                "project": "Protobuf Implementation Epic",
                                "column": "To Do",
                                "repo-token": "${{ secrets.GITHUB_TOKEN }}",
                            },
                        },
                        {
                            "name": "Auto-assign to Auth Module Project",
                            "if": "contains(github.event.issue.labels.*.name, 'module:auth')",
                            "uses": "alex-page/github-project-automation-plus@v0.9.0",
                            "with": {
                                "project": "Authentication Module",
                                "column": "To Do",
                                "repo-token": "${{ secrets.GITHUB_TOKEN }}",
                            },
                        },
                        {
                            "name": "Auto-assign to Web Module Project",
                            "if": "contains(github.event.issue.labels.*.name, 'module:web')",
                            "uses": "alex-page/github-project-automation-plus@v0.9.0",
                            "with": {
                                "project": "Web Services Module",
                                "column": "To Do",
                                "repo-token": "${{ secrets.GITHUB_TOKEN }}",
                            },
                        },
                        {
                            "name": "Auto-assign to Queue Module Project",
                            "if": "contains(github.event.issue.labels.*.name, 'module:queue')",
                            "uses": "alex-page/github-project-automation-plus@v0.9.0",
                            "with": {
                                "project": "Message Queue Module",
                                "column": "To Do",
                                "repo-token": "${{ secrets.GITHUB_TOKEN }}",
                            },
                        },
                        {
                            "name": "Auto-assign to Config Module Project",
                            "if": "contains(github.event.issue.labels.*.name, 'module:config')",
                            "uses": "alex-page/github-project-automation-plus@v0.9.0",
                            "with": {
                                "project": "Configuration Module",
                                "column": "To Do",
                                "repo-token": "${{ secrets.GITHUB_TOKEN }}",
                            },
                        },
                        {
                            "name": "Auto-assign to High Priority Project",
                            "if": "contains(github.event.issue.labels.*.name, 'priority:high') || contains(github.event.issue.labels.*.name, 'priority:critical')",
                            "uses": "alex-page/github-project-automation-plus@v0.9.0",
                            "with": {
                                "project": "High Priority Issues",
                                "column": "To Do",
                                "repo-token": "${{ secrets.GITHUB_TOKEN }}",
                            },
                        },
                    ],
                }
            },
        }

        # Ensure workflows directory exists
        os.makedirs(self.workflows_dir, exist_ok=True)

        # Write workflow file
        workflow_path = os.path.join(self.workflows_dir, "auto-assign-projects.yml")
        with open(workflow_path, "w") as f:
            yaml.dump(workflow_content, f, default_flow_style=False, sort_keys=False)

        return workflow_path

    def create_project_board_sync_workflow(self) -> str:
        """Create workflow to sync issue status with project boards."""

        workflow_content = {
            "name": "Sync Project Board Status",
            "on": {
                "issues": {"types": ["closed", "reopened"]},
                "pull_request": {"types": ["closed", "reopened"]},
            },
            "jobs": {
                "sync-project-status": {
                    "runs-on": "ubuntu-latest",
                    "steps": [
                        {
                            "name": "Move closed issues to Done",
                            "if": "github.event.action == 'closed'",
                            "uses": "alex-page/github-project-automation-plus@v0.9.0",
                            "with": {
                                "project": "All Projects",
                                "column": "Done",
                                "action": "move",
                                "repo-token": "${{ secrets.GITHUB_TOKEN }}",
                            },
                        },
                        {
                            "name": "Move reopened issues to In Progress",
                            "if": "github.event.action == 'reopened'",
                            "uses": "alex-page/github-project-automation-plus@v0.9.0",
                            "with": {
                                "project": "All Projects",
                                "column": "In Progress",
                                "action": "move",
                                "repo-token": "${{ secrets.GITHUB_TOKEN }}",
                            },
                        },
                    ],
                }
            },
        }

        workflow_path = os.path.join(self.workflows_dir, "sync-project-status.yml")
        with open(workflow_path, "w") as f:
            yaml.dump(workflow_content, f, default_flow_style=False, sort_keys=False)

        return workflow_path

    def create_project_setup_script(self) -> str:
        """Create script to setup GitHub Projects via CLI."""

        script_content = """#!/bin/bash
# file: setup_github_projects.sh
# version: 1.0.0
# guid: 6a7b8c9d-0e1f-2a3b-4c5d-6e7f8a9b0c1d

# Setup GitHub Projects for automated issue management
# This script creates the projects referenced in the automation workflows

REPO="jdfalk/gcommon"

echo "🚀 Setting up GitHub Projects for automated issue management..."

# Create Protobuf Implementation Epic project
echo "📋 Creating Protobuf Implementation Epic project..."
gh project create --title "Protobuf Implementation Epic" --body "Central coordination for all protobuf implementation work across modules" --repo $REPO

# Create module-specific projects
echo "🔐 Creating Authentication Module project..."
gh project create --title "Authentication Module" --body "Authentication and authorization related issues" --repo $REPO

echo "🌐 Creating Web Services Module project..."
gh project create --title "Web Services Module" --body "Web services and HTTP handling issues" --repo $REPO

echo "📨 Creating Message Queue Module project..."
gh project create --title "Message Queue Module" --body "Message queuing and task management issues" --repo $REPO

echo "⚙️ Creating Configuration Module project..."
gh project create --title "Configuration Module" --body "Configuration management related issues" --repo $REPO

echo "🔥 Creating High Priority Issues project..."
gh project create --title "High Priority Issues" --body "Critical and high priority issues requiring immediate attention" --repo $REPO

echo "✅ GitHub Projects setup complete!"
echo "🔧 Next: The auto-assign-projects.yml workflow will automatically assign new issues to appropriate projects based on labels"
"""

        script_path = os.path.join(self.repo_path, "setup_github_projects.sh")
        with open(script_path, "w") as f:
            f.write(script_content)

        # Make executable
        os.chmod(script_path, 0o755)

        return script_path

    def setup_all_automation(self) -> Dict[str, str]:
        """Setup complete GitHub Projects automation."""

        created_files = {}

        # Create workflows
        created_files["project_assignment"] = self.create_project_assignment_workflow()
        created_files["project_sync"] = self.create_project_board_sync_workflow()
        created_files["setup_script"] = self.create_project_setup_script()

        return created_files


def main():
    """Execute GitHub Projects automation setup."""

    repo_path = "/Users/jdfalk/repos/github.com/jdfalk/gcommon"
    automation = GitHubProjectsAutomation(repo_path)

    created_files = automation.setup_all_automation()

    print("✅ GitHub Projects automation setup complete!")
    print("📁 Created files:")
    for purpose, file_path in created_files.items():
        print(f"   - {purpose}: {os.path.basename(file_path)}")

    print("\n🔧 Next steps:")
    print("1. Run ./setup_github_projects.sh to create the actual projects")
    print(
        "2. The workflows will automatically assign issues to projects based on labels"
    )
    print("3. Issues will be moved to 'Done' when closed, 'In Progress' when reopened")

    return created_files


if __name__ == "__main__":
    main()
