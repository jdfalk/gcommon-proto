#!/usr/bin/env python3
# file: workflow_health_monitor.py
# version: 1.0.0
# guid: d4e5f6a7-b8c9-0123-def4-56789012345a

"""
GitHub Workflow Health Monitor

Continuous monitoring script for GitHub Actions workflows with automated
alerting and fix suggestion capabilities.
"""

import argparse
import json
import logging
import subprocess
import sys
import time
from datetime import datetime
from typing import Dict, List, Optional, Set, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('workflow_monitor.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)


class WorkflowHealthMonitor:
    """Monitor GitHub Actions workflows and detect health issues."""
    
    def __init__(self, repo: Optional[str] = None, check_interval: int = 300):
        """
        Initialize the workflow health monitor.
        
        Args:
            repo: Repository in format 'owner/repo' (auto-detected if None)
            check_interval: Time between health checks in seconds (default: 5 minutes)
        """
        self.repo = repo or self._get_current_repo()
        self.check_interval = check_interval
        self.known_failures: Set[str] = set()
        self.failure_counts: Dict[str, int] = {}
        self.last_check = datetime.now()
        
        # Health thresholds
        self.failure_threshold = 3  # Alert after 3 consecutive failures
        self.success_rate_threshold = 0.7  # Alert if success rate drops below 70%
        
        logger.info(f"Initialized workflow monitor for {self.repo}")
        logger.info(f"Check interval: {check_interval} seconds")
    
    def _get_current_repo(self) -> str:
        """Get the current repository from git remote."""
        try:
            result = subprocess.run(
                ['git', 'remote', 'get-url', 'origin'],
                capture_output=True,
                text=True,
                check=True
            )
            url = result.stdout.strip()
            
            # Extract owner/repo from various URL formats
            if 'github.com' in url:
                if url.startswith('https://'):
                    # https://github.com/owner/repo.git
                    parts = url.replace('https://github.com/', '').replace('.git', '').split('/')
                elif url.startswith('git@'):
                    # git@github.com:owner/repo.git
                    parts = url.replace('git@github.com:', '').replace('.git', '').split('/')
                else:
                    raise ValueError(f"Unrecognized URL format: {url}")
                
                if len(parts) >= 2:
                    return f"{parts[0]}/{parts[1]}"
            
            raise ValueError(f"Could not extract repo from URL: {url}")
            
        except subprocess.CalledProcessError as e:
            logger.error(f"Failed to get repository info: {e}")
            raise ValueError("Could not determine repository. Please specify --repo")
    
    def _run_gh_command(self, args: List[str]) -> Tuple[bool, str]:
        """
        Run a GitHub CLI command and return success status and output.
        
        Args:
            args: Command arguments for gh
            
        Returns:
            Tuple of (success, output)
        """
        try:
            result = subprocess.run(
                ['gh'] + args,
                capture_output=True,
                text=True,
                check=True
            )
            return True, result.stdout
        except subprocess.CalledProcessError as e:
            logger.error(f"GitHub CLI command failed: {' '.join(args)}")
            logger.error(f"Error: {e.stderr}")
            return False, e.stderr
    
    def get_workflow_runs(self, limit: int = 50) -> List[Dict]:
        """
        Get recent workflow runs for the repository.
        
        Args:
            limit: Maximum number of runs to retrieve
            
        Returns:
            List of workflow run dictionaries
        """
        success, output = self._run_gh_command([
            'run', 'list',
            '--repo', self.repo,
            '--limit', str(limit),
            '--json', 'id,status,conclusion,workflowName,createdAt,headBranch'
        ])
        
        if not success:
            logger.error("Failed to get workflow runs")
            return []
        
        try:
            runs = json.loads(output)
            return runs
        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse workflow runs JSON: {e}")
            return []
    
    def analyze_workflow_health(self, runs: List[Dict]) -> Dict[str, Dict]:
        """
        Analyze workflow health metrics.
        
        Args:
            runs: List of workflow run dictionaries
            
        Returns:
            Dictionary of workflow health metrics
        """
        health_metrics = {}
        
        # Group runs by workflow name
        workflows = {}
        for run in runs:
            workflow_name = run.get('workflowName', 'Unknown')
            if workflow_name not in workflows:
                workflows[workflow_name] = []
            workflows[workflow_name].append(run)
        
        # Analyze each workflow
        for workflow_name, workflow_runs in workflows.items():
            total_runs = len(workflow_runs)
            successful_runs = sum(1 for run in workflow_runs if run.get('conclusion') == 'success')
            failed_runs = sum(1 for run in workflow_runs if run.get('conclusion') == 'failure')
            
            success_rate = successful_runs / total_runs if total_runs > 0 else 0
            
            # Check for consecutive failures
            consecutive_failures = 0
            for run in sorted(workflow_runs, key=lambda x: x.get('createdAt', ''), reverse=True):
                if run.get('conclusion') == 'failure':
                    consecutive_failures += 1
                else:
                    break
            
            # Determine health status
            if consecutive_failures >= self.failure_threshold:
                health_status = 'critical'
            elif success_rate < self.success_rate_threshold:
                health_status = 'warning'
            elif failed_runs > 0:
                health_status = 'degraded'
            else:
                health_status = 'healthy'
            
            health_metrics[workflow_name] = {
                'status': health_status,
                'total_runs': total_runs,
                'successful_runs': successful_runs,
                'failed_runs': failed_runs,
                'success_rate': success_rate,
                'consecutive_failures': consecutive_failures,
                'last_run_status': workflow_runs[0].get('conclusion') if workflow_runs else 'unknown'
            }
        
        return health_metrics
    
    def detect_new_failures(self, health_metrics: Dict[str, Dict]) -> List[str]:
        """
        Detect new workflow failures that need attention.
        
        Args:
            health_metrics: Current health metrics
            
        Returns:
            List of workflow names with new critical issues
        """
        new_failures = []
        
        for workflow_name, metrics in health_metrics.items():
            if metrics['status'] == 'critical':
                # Check if this is a new critical failure
                if workflow_name not in self.known_failures:
                    new_failures.append(workflow_name)
                    self.known_failures.add(workflow_name)
                    self.failure_counts[workflow_name] = self.failure_counts.get(workflow_name, 0) + 1
                    logger.warning(f"New critical failure detected: {workflow_name}")
            else:
                # Remove from known failures if it's recovered
                if workflow_name in self.known_failures:
                    self.known_failures.remove(workflow_name)
                    logger.info(f"Workflow recovered: {workflow_name}")
        
        return new_failures
    
    def generate_health_report(self, health_metrics: Dict[str, Dict]) -> str:
        """
        Generate a comprehensive health report.
        
        Args:
            health_metrics: Current health metrics
            
        Returns:
            Formatted health report
        """
        report_lines = [
            f"# Workflow Health Report - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            f"Repository: {self.repo}",
            "",
            "## Summary",
            ""
        ]
        
        # Count workflows by status
        status_counts = {}
        for metrics in health_metrics.values():
            status = metrics['status']
            status_counts[status] = status_counts.get(status, 0) + 1
        
        for status in ['healthy', 'degraded', 'warning', 'critical']:
            count = status_counts.get(status, 0)
            if count > 0:
                emoji = {
                    'healthy': '✅',
                    'degraded': '⚠️',
                    'warning': '🟡',
                    'critical': '🔴'
                }.get(status, '❓')
                report_lines.append(f"- {emoji} {status.title()}: {count} workflows")
        
        report_lines.extend([
            "",
            "## Workflow Details",
            ""
        ])
        
        # Sort workflows by severity
        severity_order = {'critical': 0, 'warning': 1, 'degraded': 2, 'healthy': 3}
        sorted_workflows = sorted(
            health_metrics.items(),
            key=lambda x: (severity_order.get(x[1]['status'], 4), x[0])
        )
        
        for workflow_name, metrics in sorted_workflows:
            status_emoji = {
                'healthy': '✅',
                'degraded': '⚠️',
                'warning': '🟡',
                'critical': '🔴'
            }.get(metrics['status'], '❓')
            
            report_lines.extend([
                f"### {status_emoji} {workflow_name}",
                f"- **Status**: {metrics['status'].title()}",
                f"- **Success Rate**: {metrics['success_rate']:.1%} ({metrics['successful_runs']}/{metrics['total_runs']})",
                f"- **Consecutive Failures**: {metrics['consecutive_failures']}",
                f"- **Last Run**: {metrics['last_run_status']}",
                ""
            ])
        
        return "\n".join(report_lines)
    
    def send_alert(self, workflow_name: str, metrics: Dict) -> bool:
        """
        Send alert for critical workflow failure.
        
        Args:
            workflow_name: Name of the failing workflow
            metrics: Health metrics for the workflow
            
        Returns:
            True if alert was sent successfully
        """
        alert_message = f"""
🚨 Workflow Alert: {workflow_name}

Repository: {self.repo}
Status: CRITICAL
Consecutive Failures: {metrics['consecutive_failures']}
Success Rate: {metrics['success_rate']:.1%}
Last Run: {metrics['last_run_status']}

This workflow has failed {metrics['consecutive_failures']} times in a row.
Please investigate and fix the issue.

Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        """.strip()
        
        logger.critical(f"ALERT: {workflow_name} - {metrics['consecutive_failures']} consecutive failures")
        
        # Here you could integrate with notification systems like:
        # - Slack webhooks
        # - Email notifications
        # - PagerDuty
        # - GitHub issues
        # - Discord webhooks
        
        # For now, just log the alert
        print("\n" + "="*50)
        print("WORKFLOW ALERT")
        print("="*50)
        print(alert_message)
        print("="*50 + "\n")
        
        return True
    
    def run_health_check(self) -> Dict[str, Dict]:
        """
        Run a single health check cycle.
        
        Returns:
            Current health metrics
        """
        logger.info("Running workflow health check...")
        
        # Get recent workflow runs
        runs = self.get_workflow_runs()
        if not runs:
            logger.warning("No workflow runs found")
            return {}
        
        # Analyze health metrics
        health_metrics = self.analyze_workflow_health(runs)
        
        # Detect new failures
        new_failures = self.detect_new_failures(health_metrics)
        
        # Send alerts for new critical failures
        for workflow_name in new_failures:
            metrics = health_metrics[workflow_name]
            if metrics['status'] == 'critical':
                self.send_alert(workflow_name, metrics)
        
        # Generate and save health report
        report = self.generate_health_report(health_metrics)
        
        # Save report to file
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        report_file = f"workflow_health_report_{timestamp}.md"
        
        try:
            with open(report_file, 'w') as f:
                f.write(report)
            logger.info(f"Health report saved to {report_file}")
        except Exception as e:
            logger.error(f"Failed to save health report: {e}")
        
        # Log summary
        total_workflows = len(health_metrics)
        critical_count = sum(1 for m in health_metrics.values() if m['status'] == 'critical')
        warning_count = sum(1 for m in health_metrics.values() if m['status'] == 'warning')
        
        logger.info(f"Health check complete: {total_workflows} workflows, {critical_count} critical, {warning_count} warnings")
        
        self.last_check = datetime.now()
        return health_metrics
    
    def start_monitoring(self) -> None:
        """Start continuous monitoring loop."""
        logger.info("Starting continuous workflow monitoring...")
        logger.info(f"Check interval: {self.check_interval} seconds")
        logger.info("Press Ctrl+C to stop monitoring")
        
        try:
            while True:
                try:
                    self.run_health_check()
                    logger.info(f"Next check in {self.check_interval} seconds...")
                    time.sleep(self.check_interval)
                except KeyboardInterrupt:
                    logger.info("Monitoring stopped by user")
                    break
                except Exception as e:
                    logger.error(f"Error during health check: {e}")
                    logger.info("Continuing monitoring after error...")
                    time.sleep(60)  # Wait 1 minute before retrying
        except KeyboardInterrupt:
            logger.info("Monitoring stopped")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="GitHub Workflow Health Monitor",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    %(prog)s                                    # Monitor current repo every 5 minutes
    %(prog)s --repo owner/repo                  # Monitor specific repo
    %(prog)s --interval 60 --once              # Single check with 1-minute data
    %(prog)s --continuous --interval 300       # Continuous monitoring every 5 minutes
    
The monitor will:
    1. Check workflow health every interval
    2. Detect new critical failures (3+ consecutive failures)
    3. Alert when success rate drops below 70%%
    4. Generate health reports
    5. Log all activity to workflow_monitor.log
        """
    )
    
    parser.add_argument(
        '--repo',
        help='Repository in format owner/repo (auto-detected if not specified)'
    )
    
    parser.add_argument(
        '--interval',
        type=int,
        default=300,
        help='Check interval in seconds (default: 300 = 5 minutes)'
    )
    
    parser.add_argument(
        '--once',
        action='store_true',
        help='Run a single health check and exit'
    )
    
    parser.add_argument(
        '--continuous',
        action='store_true',
        help='Run continuous monitoring (default behavior)'
    )
    
    parser.add_argument(
        '--failure-threshold',
        type=int,
        default=3,
        help='Number of consecutive failures before alerting (default: 3)'
    )
    
    parser.add_argument(
        '--success-threshold',
        type=float,
        default=0.7,
        help='Minimum success rate before alerting (default: 0.7 = 70%%)'
    )
    
    args = parser.parse_args()
    
    # Create monitor
    monitor = WorkflowHealthMonitor(
        repo=args.repo,
        check_interval=args.interval
    )
    
    # Set custom thresholds
    monitor.failure_threshold = args.failure_threshold
    monitor.success_rate_threshold = args.success_threshold
    
    # Run monitoring
    if args.once:
        monitor.run_health_check()
    else:
        monitor.start_monitoring()


if __name__ == '__main__':
    main()
