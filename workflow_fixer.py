#!/usr/bin/env python3
# file: workflow_fixer.py
# version: 1.0.0
# guid: f1e2d3c4-b5a6-7890-cdef-123456789abc

"""
GitHub Workflow Fixer - Integrated Solution

Single script that discovers failing GitHub Actions workflows, analyzes their logs,
and submits them to GitHub Copilot for automated fixes. Handles large content by
splitting into manageable chunks and creating multiple issue comments.

Features:
- Pulls only failing workflow runs from the repository
- Downloads and analyzes workflow logs
- Generates detailed issue reports with smart content splitting
- Submits to GitHub Copilot for automated fixes
- Creates GitHub issues with multiple comments for large content
- Handles API limits and content size restrictions
"""

import argparse
import json
import os
import re
import subprocess
import time
from typing import Dict, List, Optional, Tuple, Any


class WorkflowFixer:
    """Integrated workflow analysis and fixing tool."""

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
        self.output_dir = "workflow_fixes"
        
        # GitHub issue body limits
        self.max_issue_body_length = 65536  # 64KB limit
        self.max_comment_length = 65536     # 64KB limit for comments
        self.chunk_size = 60000             # Leave some buffer

    def _get_current_repo(self) -> str:
        """Get the current repository from git remote."""
        try:
            result = subprocess.run(
                ["git", "remote", "get-url", "origin"],
                capture_output=True,
                text=True,
                check=True,
            )
            url = result.stdout.strip()

            # Extract owner/repo from various URL formats
            if "github.com" in url:
                if url.startswith("https://"):
                    # https://github.com/owner/repo.git
                    parts = url.replace("https://github.com/", "").replace(".git", "").split("/")
                elif url.startswith("git@"):
                    # git@github.com:owner/repo.git
                    parts = url.replace("git@github.com:", "").replace(".git", "").split("/")
                else:
                    raise ValueError(f"Unrecognized URL format: {url}")

                if len(parts) >= 2:
                    return f"{parts[0]}/{parts[1]}"

            raise ValueError(f"Could not extract repo from URL: {url}")

        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to get repository info: {e}")
            raise ValueError("Could not determine repository. Please specify --repo")

    def _ensure_gh_auth(self) -> bool:
        """Ensure GitHub CLI is authenticated."""
        try:
            result = subprocess.run(
                ["gh", "auth", "status"], capture_output=True, text=True
            )
            if result.returncode == 0:
                return True
        except FileNotFoundError:
            print("❌ GitHub CLI (gh) not found. Please install it first.")
            return False

        print("🔑 GitHub CLI not authenticated. Attempting to get token...")
        try:
            result = subprocess.run(
                ["gh", "auth", "token"], capture_output=True, text=True
            )
            if result.returncode == 0:
                self.gh_token = result.stdout.strip()
                return True
        except Exception:
            pass

        print("❌ GitHub CLI authentication failed. Please run 'gh auth login'")
        return False

    def _run_gh_command(self, args: List[str]) -> Tuple[int, str, str]:
        """Run a GitHub CLI command and return the result."""
        cmd = ["gh"] + args
        print(f"🔧 Running: {' '.join(cmd)}")

        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.returncode, result.stdout, result.stderr

    def get_failing_workflows(self) -> List[Dict]:
        """Get all failing workflow runs from the repository."""
        print(f"🔍 Searching for failing workflows in {self.repo}...")

        # Get ONLY failing workflow runs
        returncode, stdout, stderr = self._run_gh_command([
            "run", "list",
            "--repo", self.repo,
            "--status", "failure",  # Only failed runs
            "--limit", str(self.max_runs),
            "--json", "workflowName,conclusion,createdAt,updatedAt,url,databaseId,headBranch,headSha,workflowDatabaseId"
        ])

        if returncode != 0:
            print(f"❌ Error getting workflow runs: {stderr}")
            return []

        try:
            runs = json.loads(stdout)
            # Double-check that we only have failed runs
            failed_runs = [run for run in runs if run.get('conclusion') == 'failure']
            print(f"📋 Found {len(failed_runs)} failing workflow runs")
            return failed_runs
        except json.JSONDecodeError as e:
            print(f"❌ Error parsing workflow runs JSON: {e}")
            return []

    def get_workflow_logs(self, run_id: str) -> Optional[str]:
        """Download logs for a specific workflow run."""
        print(f"📥 Downloading logs for run {run_id}...")

        returncode, stdout, stderr = self._run_gh_command([
            "run", "view", run_id, "--repo", self.repo, "--log"
        ])

        if returncode != 0:
            print(f"❌ Error downloading logs for run {run_id}: {stderr}")
            return None

        return stdout

    def analyze_workflow_failure(self, run_info: Dict, logs: str) -> Dict:
        """Analyze workflow failure and extract key information."""
        print(f"🔬 Analyzing failure for workflow: {run_info.get('workflowName', 'Unknown')}")

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
            r"Cannot open: (.+)",
            r"/usr/bin/tar: (.+): Cannot open",
        ]

        lines = logs.split("\n")
        errors_found = set()  # Use set to avoid duplicates
        
        for line in lines:
            for pattern in error_patterns:
                matches = re.findall(pattern, line, re.IGNORECASE)
                if matches:
                    for match in matches:
                        if isinstance(match, tuple):
                            match = match[0]
                        error_key = match.strip()[:100]  # Truncate for dedup
                        if error_key not in errors_found:
                            errors_found.add(error_key)
                            analysis["error_summary"].append({
                                "error": match.strip(),
                                "context": line.strip()[:200]  # Limit context length
                            })

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
        if "cannot open" in log_lower and "file exists" in log_lower:
            analysis["potential_issues"].append("File conflict issues")
        if "go: downloading" in log_lower and "cannot open" in log_lower:
            analysis["potential_issues"].append("Go toolchain installation conflicts")

        return analysis

    def split_content_into_chunks(self, content: str, max_length: int) -> List[str]:
        """Split large content into manageable chunks."""
        if len(content) <= max_length:
            return [content]
        
        chunks = []
        current_chunk = ""
        
        # Split by lines to avoid breaking in middle of content
        lines = content.split('\n')
        
        for line in lines:
            # If adding this line would exceed the limit, start a new chunk
            if len(current_chunk) + len(line) + 1 > max_length:
                if current_chunk:
                    chunks.append(current_chunk.strip())
                    current_chunk = line + '\n'
                else:
                    # Single line is too long, split it
                    for i in range(0, len(line), max_length - 100):
                        chunks.append(line[i:i + max_length - 100])
            else:
                current_chunk += line + '\n'
        
        if current_chunk.strip():
            chunks.append(current_chunk.strip())
        
        return chunks

    def create_github_issue(self, analysis: Dict, dry_run: bool = False) -> Optional[str]:
        """Create a GitHub issue for the workflow failure with smart content splitting."""
        run_id = analysis["run_id"]
        
        title = f"🔧 Fix Workflow Failure: {analysis['workflow_name']} (Run #{run_id})"
        
        # Create the main issue body (keep it concise)
        main_body = f"""## Workflow Failure Analysis

**Workflow**: {analysis['workflow_name']}
**Run ID**: {run_id}
**Branch**: {analysis['branch']}
**SHA**: {analysis['sha']}
**Date**: {analysis['created_at']}
**URL**: {analysis['url']}

## Quick Summary
Found {len(analysis['error_summary'])} error(s) in this workflow run.

**Main Issues**:
"""
        
        # Add top 5 errors to main body
        for i, error in enumerate(analysis['error_summary'][:5]):
            main_body += f"- {error['error'][:100]}{'...' if len(error['error']) > 100 else ''}\n"
        
        if len(analysis['error_summary']) > 5:
            main_body += f"- ... and {len(analysis['error_summary']) - 5} more errors (see comments below)\n"
        
        main_body += f"""
**Potential Issue Categories**: {', '.join(analysis['potential_issues'])}

## Fix Request
@github-copilot Please analyze this workflow failure and provide specific fixes for the identified issues.

**Additional Details**: See the detailed analysis in the comments below.
"""

        if dry_run:
            print(f"📝 Would create issue: {title}")
            print(f"Body length: {len(main_body)} characters")
            return None

        # Create the main issue
        returncode, stdout, stderr = self._run_gh_command([
            "issue", "create",
            "--repo", self.repo,
            "--title", title,
            "--body", main_body,
            "--label", "workflow-failure,automation,copilot-help"
        ])

        if returncode != 0:
            print(f"❌ Error creating issue: {stderr}")
            return None

        # Extract issue number from output
        issue_url = stdout.strip()
        issue_number = issue_url.split('/')[-1]
        print(f"✅ Created issue #{issue_number}: {issue_url}")

        # Add detailed analysis as comments (split if needed)
        detailed_analysis = self._create_detailed_analysis(analysis)
        comment_chunks = self.split_content_into_chunks(detailed_analysis, self.chunk_size)
        
        for i, chunk in enumerate(comment_chunks):
            comment_title = f"## Detailed Analysis (Part {i+1}/{len(comment_chunks)})\n\n" if len(comment_chunks) > 1 else "## Detailed Analysis\n\n"
            comment_body = comment_title + chunk
            
            returncode, stdout, stderr = self._run_gh_command([
                "issue", "comment", issue_number,
                "--repo", self.repo,
                "--body", comment_body
            ])
            
            if returncode != 0:
                print(f"❌ Error adding comment {i+1}: {stderr}")
            else:
                print(f"💬 Added detailed analysis comment {i+1}/{len(comment_chunks)}")
            
            # Small delay to avoid rate limiting
            time.sleep(0.5)

        return issue_number

    def _create_detailed_analysis(self, analysis: Dict) -> str:
        """Create detailed analysis content for comments."""
        detailed = f"""### Complete Error Analysis

#### All Errors Found ({len(analysis['error_summary'])} total):
"""
        
        for i, error in enumerate(analysis['error_summary'], 1):
            detailed += f"""
{i}. **Error**: {error['error']}
   **Context**: {error['context']}
"""

        if analysis['file_patterns']:
            detailed += f"""
#### Files That May Need Attention
```
{chr(10).join(analysis['file_patterns'][:20])}
```
"""

        # Add truncated logs (most recent/relevant parts)
        log_lines = analysis['full_logs'].split('\n')
        if len(log_lines) > 50:
            detailed += f"""
#### Recent Log Excerpt (Last 50 lines)
```
{chr(10).join(log_lines[-50:])}
```
"""
        else:
            detailed += f"""
#### Complete Logs
```
{analysis['full_logs']}
```
"""

        detailed += """
#### Recommended Actions
Based on the error patterns, consider:

1. **Check for file conflicts** - Many errors show "Cannot open: File exists"
2. **Review Go toolchain setup** - Conflicts during Go installation
3. **Clean workspace** - Remove conflicting files before setup
4. **Update workflow caching** - Clear/update any cached dependencies
5. **Check for concurrent runs** - Multiple runs might conflict

@github-copilot Please provide specific YAML fixes for the workflow configuration.
"""

        return detailed

    def submit_to_copilot_chat(self, analysis: Dict, issue_number: str = None) -> bool:
        """Submit to GitHub Copilot Chat if available."""
        try:
            # Try Copilot CLI first
            prompt = f"""Fix this GitHub Actions workflow failure:

Workflow: {analysis['workflow_name']}
Errors: {len(analysis['error_summary'])} found

Top 3 errors:
"""
            for error in analysis['error_summary'][:3]:
                prompt += f"- {error['error']}\n"

            prompt += f"""
Potential issues: {', '.join(analysis['potential_issues'])}

Please provide specific YAML workflow fixes.
"""

            returncode, stdout, stderr = self._run_gh_command([
                "copilot", "suggest", "--type", "gh", prompt
            ])

            if returncode == 0:
                print("🤖 Submitted to GitHub Copilot successfully")
                if issue_number:
                    # Add Copilot response to issue
                    self._run_gh_command([
                        "issue", "comment", issue_number,
                        "--repo", self.repo,
                        "--body", f"## GitHub Copilot Response\n\n{stdout}"
                    ])
                return True

        except Exception as e:
            print(f"⚠️ Copilot submission failed: {e}")

        return False

    def process_workflow_failures(self, dry_run: bool = False) -> Dict[str, Any]:
        """Main processing function."""
        if not self._ensure_gh_auth():
            return {"success": False, "error": "Authentication failed"}

        # Ensure output directory exists
        os.makedirs(self.output_dir, exist_ok=True)

        # Get failing workflows
        failing_runs = self.get_failing_workflows()
        if not failing_runs:
            print("✅ No failing workflows found!")
            return {"success": True, "processed": 0}

        results = {
            "success": True,
            "processed": 0,
            "issues_created": [],
            "errors": []
        }

        # Process each failing workflow
        for run in failing_runs:
            try:
                run_id = str(run.get("databaseId", ""))
                
                # Get logs
                logs = self.get_workflow_logs(run_id)
                if not logs:
                    continue

                # Analyze failure
                analysis = self.analyze_workflow_failure(run, logs)
                
                # Create GitHub issue with smart content splitting
                issue_number = self.create_github_issue(analysis, dry_run)
                if issue_number:
                    results["issues_created"].append(issue_number)
                    
                    # Try to submit to Copilot
                    self.submit_to_copilot_chat(analysis, issue_number)

                results["processed"] += 1
                
                # Small delay between runs
                time.sleep(1)
                
            except Exception as e:
                error_msg = f"Error processing run {run.get('databaseId', 'unknown')}: {e}"
                print(f"❌ {error_msg}")
                results["errors"].append(error_msg)

        return results


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="GitHub Workflow Fixer - Integrated Solution",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    %(prog)s                                    # Fix failing workflows in current repo
    %(prog)s --repo owner/repo --max-runs 20   # Fix failures in specific repo
    %(prog)s --dry-run                          # Analyze only, don't create issues
    %(prog)s --max-runs 5                       # Process only top 5 failures
    
The tool will:
    1. Find ONLY failing GitHub Actions workflows
    2. Download and analyze their logs
    3. Create GitHub issues with smart content splitting
    4. Submit to GitHub Copilot for automated fixes
    5. Handle large content by splitting into multiple comments
        """
    )

    parser.add_argument(
        "--repo",
        help="Repository in format owner/repo (auto-detected if not specified)"
    )

    parser.add_argument(
        "--max-runs",
        type=int,
        default=10,
        help="Maximum number of failing runs to analyze (default: 10)"
    )

    parser.add_argument(
        "--days",
        type=int,
        default=7,
        help="How many days back to look for failures (default: 7)"
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Analyze failures but don't create issues or submit to Copilot"
    )

    args = parser.parse_args()

    print("🚀 GitHub Workflow Fixer - Integrated Solution")
    print("=" * 50)

    if args.dry_run:
        print("🔍 Dry run mode - will not create issues or submit to Copilot")

    # Create and run the fixer
    fixer = WorkflowFixer(
        repo=args.repo,
        max_runs=args.max_runs,
        days_back=args.days
    )

    results = fixer.process_workflow_failures(dry_run=args.dry_run)

    # Print summary
    print("\n" + "=" * 50)
    print("📊 SUMMARY")
    print("=" * 50)

    if results["success"]:
        print(f"✅ Processed {results['processed']} failing workflows")
        if results["issues_created"]:
            print(f"🎫 Created {len(results['issues_created'])} GitHub issues:")
            for issue in results["issues_created"]:
                print(f"   - Issue #{issue}: https://github.com/{fixer.repo}/issues/{issue}")
        
        if results["errors"]:
            print(f"⚠️ {len(results['errors'])} errors encountered:")
            for error in results["errors"]:
                print(f"   - {error}")
    else:
        print(f"❌ Failed: {results.get('error', 'Unknown error')}")

    print("\n🎯 Next Steps:")
    print("1. Review the created GitHub issues")
    print("2. Check Copilot responses for specific fixes")
    print("3. Test proposed fixes in feature branches")
    print("4. Apply fixes and monitor workflow success")


if __name__ == "__main__":
    main()
