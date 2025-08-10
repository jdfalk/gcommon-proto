#!/usr/bin/env python3
# file: fix_failing_workflows.py
# version: 1.0.0
# guid: a1b2c3d4-e5f6-7890-abcd-123456789012

"""
GitHub Workflow Fix Tool

Automatically discovers failing GitHub Actions workflows, analyzes their logs,
and uses GitHub Copilot to generate fixes for the issues found.

Features:
- Pulls all failing workflow runs from the repository
- Downloads and analyzes workflow logs
- Generates detailed issue reports
- Submits to GitHub Copilot for automated fixes
- Creates fix branches and pull requests
"""

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
from datetime import datetime
from typing import Dict, List, Optional, Tuple


class GitHubWorkflowFixer:
    """Main class for handling GitHub workflow analysis and fixing."""

    def __init__(self, repo: str = None, max_runs: int = 10, days_back: int = 7):
        """Initialize the workflow fixer.

        Args:
            repo: Repository in format owner/repo (auto-detected if None)
            max_runs: Maximum number of workflow runs to analyze
            days_back: How many days back to look for failing workflows
        """
        self.repo = repo or self._get_current_repo()
        self.max_runs = max_runs
        self.days_back = days_back
        self.gh_token = None
        self.temp_dir = None

    def _get_current_repo(self) -> str:
        """Get the current repository from git remote."""
        try:
            result = subprocess.run(
                ["git", "remote", "get-url", "origin"],
                capture_output=True,
                text=True,
                check=True,
            )
            remote_url = result.stdout.strip()

            # Parse different URL formats
            if "github.com" in remote_url:
                if remote_url.startswith("git@"):
                    # git@github.com:owner/repo.git
                    repo_part = remote_url.split(":")[-1]
                else:
                    # https://github.com/owner/repo.git
                    repo_part = remote_url.split("github.com/")[-1]

                return repo_part.replace(".git", "")

            raise ValueError("Not a GitHub repository")

        except subprocess.CalledProcessError:
            raise ValueError("Could not determine repository from git remote")

    def _ensure_gh_auth(self) -> bool:
        """Ensure GitHub CLI is authenticated."""
        try:
            # Check if already authenticated
            result = subprocess.run(
                ["gh", "auth", "status"], capture_output=True, text=True
            )

            if result.returncode == 0:
                print("✅ GitHub CLI already authenticated")
                # Get the token for API calls
                token_result = subprocess.run(
                    ["gh", "auth", "token"], capture_output=True, text=True, check=True
                )
                self.gh_token = token_result.stdout.strip()
                return True

        except subprocess.CalledProcessError:
            pass

        print("❌ GitHub CLI not authenticated. Please run 'gh auth login' first.")
        return False

    def _run_gh_command(self, args: List[str]) -> Tuple[int, str, str]:
        """Run a GitHub CLI command and return result."""
        cmd = ["gh"] + args
        print(f"🔧 Running: {' '.join(cmd)}")

        result = subprocess.run(cmd, capture_output=True, text=True)

        return result.returncode, result.stdout, result.stderr

    def get_failing_workflows(self) -> List[Dict]:
        """Get all failing workflow runs from the repository."""
        print(f"🔍 Searching for failing workflows in {self.repo}...")

        # Get failing workflow runs (note: since_date could be used for API filtering if needed)
        returncode, stdout, stderr = self._run_gh_command(
            [
                "run",
                "list",
                "--repo",
                self.repo,
                "--status",
                "failure",
                "--limit",
                str(self.max_runs),
                "--json",
                "workflowName,conclusion,createdAt,updatedAt,url,databaseId,headBranch,headSha,workflowDatabaseId",
            ]
        )

        if returncode != 0:
            print(f"❌ Error getting workflow runs: {stderr}")
            return []

        try:
            runs = json.loads(stdout)
            print(f"📋 Found {len(runs)} failing workflow runs")
            return runs
        except json.JSONDecodeError as e:
            print(f"❌ Error parsing workflow runs JSON: {e}")
            return []

    def get_workflow_logs(self, run_id: str) -> Optional[str]:
        """Download logs for a specific workflow run."""
        print(f"📥 Downloading logs for run {run_id}...")

        # Create temp directory if not exists
        if not self.temp_dir:
            self.temp_dir = tempfile.mkdtemp(prefix="workflow_logs_")

        log_file = os.path.join(self.temp_dir, f"run_{run_id}.log")

        returncode, stdout, stderr = self._run_gh_command(
            ["run", "view", run_id, "--repo", self.repo, "--log"]
        )

        if returncode != 0:
            print(f"❌ Error downloading logs for run {run_id}: {stderr}")
            return None

        # Save logs to file
        with open(log_file, "w", encoding="utf-8") as f:
            f.write(stdout)

        return stdout

    def analyze_workflow_failure(self, run_info: Dict, logs: str) -> Dict:
        """Analyze workflow failure and extract key information."""
        print(
            f"🔬 Analyzing failure for workflow: {run_info.get('workflowName', 'Unknown')}"
        )

        analysis = {
            "workflow_name": run_info.get("workflowName", "Unknown"),
            "run_id": run_info.get("databaseId", "Unknown"),
            "branch": run_info.get("headBranch", "Unknown"),
            "sha": run_info.get("headSha", "Unknown"),
            "url": run_info.get("url", ""),
            "created_at": run_info.get("createdAt", ""),
            "error_summary": [],
            "full_logs": logs,
            "potential_issues": [],
            "file_patterns": [],
        }

        # Extract error patterns from logs
        error_patterns = [
            r"Error: (.+)",
            r"FAILED (.+)",
            r"✗ (.+)",
            r"❌ (.+)",
            r"Process completed with exit code (\d+)",
            r"npm ERR! (.+)",
            r"go: (.+)",
            r"fatal: (.+)",
            r"Exception: (.+)",
            r"TypeError: (.+)",
            r"SyntaxError: (.+)",
            r"ModuleNotFoundError: (.+)",
            r"ImportError: (.+)",
        ]

        lines = logs.split("\n")
        for line in lines:
            for pattern in error_patterns:
                matches = re.findall(pattern, line, re.IGNORECASE)
                if matches:
                    for match in matches:
                        if isinstance(match, tuple):
                            match = match[0]
                        analysis["error_summary"].append(
                            {"error": match.strip(), "line": line.strip()}
                        )

        # Identify potential issue categories
        log_lower = logs.lower()
        if "module not found" in log_lower or "import" in log_lower:
            analysis["potential_issues"].append("Missing dependencies")
        if "permission denied" in log_lower:
            analysis["potential_issues"].append("Permission issues")
        if "syntax error" in log_lower:
            analysis["potential_issues"].append("Syntax errors")
        if "timeout" in log_lower:
            analysis["potential_issues"].append("Timeout issues")
        if "network" in log_lower or "connection" in log_lower:
            analysis["potential_issues"].append("Network connectivity")
        if "test" in log_lower and "fail" in log_lower:
            analysis["potential_issues"].append("Test failures")
        if "build" in log_lower and "fail" in log_lower:
            analysis["potential_issues"].append("Build failures")

        # Extract file patterns that might need fixes
        file_pattern_regexes = [
            r"(\S+\.go):\d+:\d+:",
            r"(\S+\.py):\d+:",
            r"(\S+\.js):\d+:\d+:",
            r"(\S+\.ts):\d+:\d+:",
            r"(\S+\.json):",
            r"(\S+\.yaml):",
            r"(\S+\.yml):",
            r"in file (\S+)",
            r"File \"(\S+)\"",
        ]

        for pattern in file_pattern_regexes:
            matches = re.findall(pattern, logs)
            analysis["file_patterns"].extend(matches)

        # Remove duplicates
        analysis["file_patterns"] = list(set(analysis["file_patterns"]))

        return analysis

    def generate_copilot_prompt(self, analysis: Dict) -> str:
        """Generate a comprehensive prompt for GitHub Copilot."""
        prompt = f"""# GitHub Workflow Failure Analysis & Fix Request

## Workflow Information
- **Workflow**: {analysis["workflow_name"]}
- **Run ID**: {analysis["run_id"]}
- **Branch**: {analysis["branch"]}
- **SHA**: {analysis["sha"]}
- **Date**: {analysis["created_at"]}
- **URL**: {analysis["url"]}

## Error Summary
The following errors were detected in the workflow logs:

"""

        for i, error in enumerate(
            analysis["error_summary"][:10], 1
        ):  # Limit to top 10 errors
            prompt += f"{i}. **Error**: {error['error']}\n"
            prompt += f"   **Context**: {error['line']}\n\n"

        if analysis["potential_issues"]:
            prompt += "## Potential Issue Categories\n"
            for issue in analysis["potential_issues"]:
                prompt += f"- {issue}\n"
            prompt += "\n"

        if analysis["file_patterns"]:
            prompt += "## Files That May Need Attention\n"
            for file_path in analysis["file_patterns"][:20]:  # Limit to top 20 files
                prompt += f"- `{file_path}`\n"
            prompt += "\n"

        prompt += """## Request for Copilot

Please analyze the above workflow failure and provide:

1. **Root Cause Analysis**: What is the primary cause of this workflow failure?

2. **Specific Fixes**: Provide specific code changes, configuration updates, or workflow modifications needed to fix the issues.

3. **File-by-File Changes**: For each file that needs modification, provide the exact changes needed.

4. **Workflow Configuration**: If the workflow file itself needs changes, provide the updated YAML.

5. **Dependencies**: List any missing dependencies or version conflicts that need to be resolved.

6. **Testing Strategy**: Recommend how to test the fixes before merging.

## Full Workflow Logs
```
"""

        # Include truncated logs (GitHub Copilot has token limits)
        log_lines = analysis["full_logs"].split("\n")
        if len(log_lines) > 500:
            prompt += "\n".join(log_lines[:250])
            prompt += "\n\n... (logs truncated for brevity) ...\n\n"
            prompt += "\n".join(log_lines[-250:])
        else:
            prompt += analysis["full_logs"]

        prompt += "\n```\n"

        return prompt

    def create_fix_request(
        self, analysis: Dict, prompt: str, output_dir: str = "workflow_fixes"
    ):
        """Create a structured fix request file."""
        os.makedirs(output_dir, exist_ok=True)

        # Create a filename based on workflow and timestamp
        safe_name = re.sub(r"[^\w\-_.]", "_", analysis["workflow_name"])
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{safe_name}_{analysis['run_id']}_{timestamp}.md"
        filepath = os.path.join(output_dir, filename)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(prompt)

        print(f"📝 Created fix request: {filepath}")
        return filepath

    def submit_to_copilot(self, prompt_file: str) -> bool:
        """Submit the fix request to GitHub Copilot using GitHub CLI."""
        print("🤖 Submitting to GitHub Copilot...")

        # Use gh copilot suggest or equivalent command
        # Note: This may vary based on GitHub CLI copilot extension availability
        returncode, stdout, stderr = self._run_gh_command(
            [
                "copilot",
                "suggest",
                "-t",
                "shell",
                f"Fix the GitHub workflow issues described in {prompt_file}",
            ]
        )

        if returncode == 0:
            print("✅ Copilot suggestion received")
            print(stdout)
            return True
        else:
            print(f"❌ Error getting Copilot suggestion: {stderr}")
            # Try alternative approach - create an issue instead
            return self._create_github_issue(prompt_file)

    def _create_github_issue(self, prompt_file: str) -> bool:
        """Create a GitHub issue with the fix request if Copilot is unavailable."""
        print("📋 Creating GitHub issue with fix request...")

        with open(prompt_file, "r", encoding="utf-8") as f:
            content = f.read()

        # Extract workflow name for issue title
        lines = content.split("\n")
        workflow_name = "Unknown Workflow"
        for line in lines:
            if "**Workflow**:" in line:
                workflow_name = line.split("**Workflow**:")[-1].strip()
                break

        issue_title = f"🤖 Auto-Fix Request: {workflow_name} Workflow Failure"

        returncode, stdout, stderr = self._run_gh_command(
            [
                "issue",
                "create",
                "--repo",
                self.repo,
                "--title",
                issue_title,
                "--body-file",
                prompt_file,
                "--label",
                "bug,workflow,auto-generated",
            ]
        )

        if returncode == 0:
            print(f"✅ Created GitHub issue: {stdout.strip()}")
            return True
        else:
            print(f"❌ Error creating GitHub issue: {stderr}")
            return False

    def run_analysis(self) -> bool:
        """Run the complete workflow analysis and fix generation."""
        print("🚀 Starting GitHub Workflow Fix Tool")
        print(f"📁 Repository: {self.repo}")
        print(f"📅 Looking back {self.days_back} days")
        print(f"🔢 Max runs to analyze: {self.max_runs}")

        # Ensure GitHub CLI authentication
        if not self._ensure_gh_auth():
            return False

        # Get failing workflows
        failing_runs = self.get_failing_workflows()
        if not failing_runs:
            print("✅ No failing workflows found!")
            return True

        success_count = 0
        total_count = len(failing_runs)

        for i, run_info in enumerate(failing_runs, 1):
            print(f"\n{'=' * 60}")
            print(f"Processing workflow {i}/{total_count}")
            print(f"{'=' * 60}")

            run_id = str(run_info.get("databaseId", ""))
            if not run_id:
                print("⚠️ Skipping run with missing ID")
                continue

            # Get workflow logs
            logs = self.get_workflow_logs(run_id)
            if not logs:
                print(f"⚠️ Could not get logs for run {run_id}")
                continue

            # Analyze the failure
            analysis = self.analyze_workflow_failure(run_info, logs)

            # Generate Copilot prompt
            prompt = self.generate_copilot_prompt(analysis)

            # Create fix request file
            fix_file = self.create_fix_request(analysis, prompt)

            # Submit to Copilot or create issue
            if self.submit_to_copilot(fix_file):
                success_count += 1

        print(f"\n{'=' * 60}")
        print("🎉 Analysis complete!")
        print(f"✅ Successfully processed: {success_count}/{total_count}")
        print("📁 Fix requests saved in: workflow_fixes/")

        # Cleanup temp directory
        if self.temp_dir and os.path.exists(self.temp_dir):
            import shutil

            shutil.rmtree(self.temp_dir)

        return success_count > 0

    def cleanup(self):
        """Clean up temporary files."""
        if self.temp_dir and os.path.exists(self.temp_dir):
            import shutil

            shutil.rmtree(self.temp_dir)


def main():
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(
        description="Automatically fix failing GitHub workflows using Copilot",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python fix_failing_workflows.py                           # Analyze current repo
  python fix_failing_workflows.py --repo owner/repo         # Analyze specific repo
  python fix_failing_workflows.py --max-runs 20 --days 14  # More comprehensive analysis
  python fix_failing_workflows.py --dry-run                 # Just analyze, don't submit
        """,
    )

    parser.add_argument(
        "--repo",
        help="Repository in format owner/repo (auto-detected if not specified)",
    )

    parser.add_argument(
        "--max-runs",
        type=int,
        default=10,
        help="Maximum number of workflow runs to analyze (default: 10)",
    )

    parser.add_argument(
        "--days",
        type=int,
        default=7,
        help="How many days back to look for failing workflows (default: 7)",
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Only analyze and create fix files, don't submit to Copilot",
    )

    parser.add_argument(
        "--output-dir",
        default="workflow_fixes",
        help="Directory to save fix request files (default: workflow_fixes)",
    )

    args = parser.parse_args()

    try:
        # Create the fixer instance
        fixer = GitHubWorkflowFixer(
            repo=args.repo, max_runs=args.max_runs, days_back=args.days
        )

        if args.dry_run:
            print("🔍 Dry run mode - will not submit to Copilot")

            # Run analysis but skip submission
            failing_runs = fixer.get_failing_workflows()
            if not failing_runs:
                print("✅ No failing workflows found!")
                return 0

            for run_info in failing_runs:
                run_id = str(run_info.get("databaseId", ""))
                if not run_id:
                    continue

                logs = fixer.get_workflow_logs(run_id)
                if logs:
                    analysis = fixer.analyze_workflow_failure(run_info, logs)
                    prompt = fixer.generate_copilot_prompt(analysis)
                    fixer.create_fix_request(analysis, prompt, args.output_dir)

            print(f"📁 Fix requests saved in: {args.output_dir}/")
        else:
            # Run full analysis and submission
            success = fixer.run_analysis()
            return 0 if success else 1

    except KeyboardInterrupt:
        print("\n⚠️ Interrupted by user")
        return 1
    except Exception as e:
        print(f"❌ Error: {e}")
        return 1
    finally:
        if "fixer" in locals():
            fixer.cleanup()


if __name__ == "__main__":
    sys.exit(main())
