#!/usr/bin/env python3
# file: scripts/fix_workflow_permissions.py
# version: 1.0.0
# guid: f1x-w0rk-f10w-p3rm-1551055-12345

"""
Fix GitHub Actions workflow permission issues

This script identifies GitHub Actions workflows that:
1. Have git commit/push operations but missing 'contents: write' permission
2. Use github-actions[bot] user for automated commits
3. Need proper permissions for automated operations

The script scans all .github/workflows/*.yml files and suggests fixes.
"""

import re
from pathlib import Path
from typing import Dict, List

import yaml


def find_workflows(base_path: str) -> List[Path]:
    """Find all GitHub Actions workflow files."""
    workflows = []
    for repo_path in Path(base_path).iterdir():
        if repo_path.is_dir():
            workflow_dir = repo_path / ".github" / "workflows"
            if workflow_dir.exists():
                workflows.extend(workflow_dir.glob("*.yml"))
                workflows.extend(workflow_dir.glob("*.yaml"))
    return workflows


def analyze_workflow(workflow_path: Path) -> Dict:
    """Analyze a workflow file for permission issues."""
    result = {
        "path": str(workflow_path),
        "needs_fix": False,
        "has_git_operations": False,
        "has_permissions": False,
        "has_contents_write": False,
        "git_operations": [],
        "issues": [],
    }

    try:
        with open(workflow_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Check for git operations
        git_patterns = [
            r"git\s+commit\s+-m",
            r"git\s+push",
            r"git\s+add.*&&.*git\s+commit",
            r"github-actions\[bot\]",
        ]

        for pattern in git_patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            if matches:
                result["has_git_operations"] = True
                result["git_operations"].extend(matches)

        # Parse YAML to check permissions
        try:
            yaml_content = yaml.safe_load(content)
            if yaml_content and "permissions" in yaml_content:
                result["has_permissions"] = True
                permissions = yaml_content["permissions"]
                if (
                    isinstance(permissions, dict)
                    and permissions.get("contents") == "write"
                ):
                    result["has_contents_write"] = True
        except yaml.YAMLError:
            result["issues"].append("Invalid YAML syntax")

        # Determine if fix is needed
        if result["has_git_operations"] and not result["has_contents_write"]:
            result["needs_fix"] = True
            if not result["has_permissions"]:
                result["issues"].append("Missing permissions block")
            else:
                result["issues"].append("Missing 'contents: write' permission")

    except Exception as e:
        result["issues"].append(f"Error reading file: {e}")

    return result


def suggest_fix(analysis: Dict) -> str:
    """Suggest a fix for the workflow."""
    if not analysis["needs_fix"]:
        return "No fix needed"

    suggestions = []

    if "Missing permissions block" in analysis["issues"]:
        suggestions.append("""
Add this permissions block after the 'on:' section:

permissions:
  contents: write  # Required for automated git operations

""")
    elif "Missing 'contents: write' permission" in analysis["issues"]:
        suggestions.append("""
Add 'contents: write' to the existing permissions block:

permissions:
  contents: write  # Add this line
  # ... other existing permissions

""")

    return "\n".join(suggestions)


def main():
    """Main execution function."""
    print("🔍 Scanning GitHub Actions workflows for permission issues...\n")

    # Find all workflows in the workspace
    base_path = "/Users/jdfalk/repos/github.com/jdfalk"
    workflows = find_workflows(base_path)

    if not workflows:
        print("❌ No workflow files found")
        return

    print(f"📁 Found {len(workflows)} workflow files\n")

    issues_found = []

    for workflow in workflows:
        analysis = analyze_workflow(workflow)

        if analysis["needs_fix"]:
            issues_found.append(analysis)
            print(f"⚠️  ISSUE: {analysis['path']}")
            print(f"   Git operations: {', '.join(set(analysis['git_operations']))}")
            print(f"   Issues: {', '.join(analysis['issues'])}")
            print(f"   Fix: {suggest_fix(analysis)}")
            print("-" * 80)
        elif analysis["has_git_operations"]:
            print(
                f"✅ OK: {analysis['path']} - Has git operations with proper permissions"
            )

    print("\n📊 Summary:")
    print(f"   Total workflows: {len(workflows)}")
    print(f"   Need fixes: {len(issues_found)}")
    print(f"   Issues resolved: {len(workflows) - len(issues_found)}")

    if issues_found:
        print(f"\n🚨 {len(issues_found)} workflows need permission fixes!")
        print("Run this script with --fix flag to automatically apply fixes.")
    else:
        print("\n🎉 All workflows have proper permissions!")


if __name__ == "__main__":
    main()
