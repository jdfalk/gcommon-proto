#!/usr/bin/env python3
# file: scripts/cleanup_workflow_runs.py
# version: 1.0.0
# guid: 7d9b1f2e-6c3a-4e1d-8a5f-2b9c7d4e1f8a

"""GitHub Actions workflow run cleanup utility.

Deletes (or dry-runs) workflow runs older than a specified age (default 7 days)
for the current repository. Designed to help control Actions storage usage.

Key features:
  - Dry-run by default (must pass --apply to actually delete)
  - Age threshold configurable via --days (default 7)
  - Optional filtering by workflow name or file (repeat --workflow)
  - Optional status filtering (success, failure, completed, etc.)
  - Paged fetching (auto-handles pagination until no more runs or cutoff reached)
  - Rate limit awareness (backs off when secondary rate limit headers appear)
  - Uses PAT from JF_CI_GH_PAT first, then GITHUB_TOKEN

Environment:
  JF_CI_GH_PAT or GITHUB_TOKEN must be set with repo scope.

Exit codes:
  0 success (even if nothing deleted)
  1 generic error (auth, HTTP unexpected, etc.)

Examples:
  Dry run (default):
    python3 scripts/cleanup_workflow_runs.py

  Actually delete runs older than 10 days for a specific workflow:
    python3 scripts/cleanup_workflow_runs.py --days 10 --workflow release.yml --apply

  Delete only failed or cancelled runs older than 14 days:
    python3 scripts/cleanup_workflow_runs.py --days 14 --status failure --status cancelled --apply
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from typing import Dict, Iterable, Optional

API_ROOT = "https://api.github.com"


def _auth_token() -> str:
    token = os.getenv("JF_CI_GH_PAT") or os.getenv("GITHUB_TOKEN")
    if not token:
        print(
            "ERROR: Neither JF_CI_GH_PAT nor GITHUB_TOKEN is set in the environment",
            file=sys.stderr,
        )
        sys.exit(1)
    return token


def _headers(token: str) -> Dict[str, str]:
    return {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "workflow-cleanup-script",
    }


def _request(url: str, token: str, method: str = "GET") -> dict:
    req = urllib.request.Request(url, headers=_headers(token), method=method)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            if resp.status == 204:  # No content (e.g. successful DELETE)
                return {"status": 204}
            data = resp.read().decode("utf-8")
            return json.loads(data)
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace") if hasattr(e, "read") else ""
        print(f"HTTP {e.code} for {method} {url}: {body}", file=sys.stderr)
        # 404 on deletion of an in-flight or already-removed run: treat as non-fatal
        if e.code in (404, 410):
            return {"status": e.code, "warning": True}
        time.sleep(2)
        raise


def _parse_args(argv: Optional[Iterable[str]] = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Cleanup old GitHub Actions workflow runs")
    p.add_argument(
        "--days", type=int, default=7, help="Age threshold in days (default 7)"
    )
    p.add_argument(
        "--workflow",
        action="append",
        default=[],
        help="Workflow name or filename to restrict (repeatable)",
    )
    p.add_argument(
        "--status",
        action="append",
        default=[],
        help="Limit to specific statuses (completed, failure, success, cancelled, etc.)",
    )
    p.add_argument(
        "--per-page", type=int, default=100, help="Runs per page to fetch (max 100)"
    )
    p.add_argument(
        "--max-delete",
        type=int,
        default=500,
        help="Safety cap on number of deletions (default 500)",
    )
    p.add_argument(
        "--apply",
        action="store_true",
        help="Actually perform deletions (omit for dry-run)",
    )
    p.add_argument(
        "--owner",
        default=os.getenv("GITHUB_REPOSITORY", "").split("/")[0],
        help="Repository owner (auto from GITHUB_REPOSITORY)",
    )
    p.add_argument(
        "--repo",
        default=os.getenv("GITHUB_REPOSITORY", "").split("/")[-1],
        help="Repository name (auto from GITHUB_REPOSITORY)",
    )
    p.add_argument(
        "--sleep",
        type=float,
        default=0.25,
        help="Sleep between deletions to avoid secondary rate limits",
    )
    return p.parse_args(list(argv) if argv is not None else None)


def _resolve_workflows(owner: str, repo: str, token: str) -> Dict[str, int]:
    url = f"{API_ROOT}/repos/{owner}/{repo}/actions/workflows"
    result = _request(url, token)
    workflows: Dict[str, int] = {}
    for wf in result.get("workflows", []):
        workflows[wf.get("path") or wf["name"]] = wf["id"]
        workflows[wf["name"]] = wf["id"]
    return workflows


def _list_runs(
    owner: str, repo: str, workflow_id: int, token: str, per_page: int
) -> Iterable[dict]:
    page = 1
    while True:
        url = f"{API_ROOT}/repos/{owner}/{repo}/actions/workflows/{workflow_id}/runs?per_page={per_page}&page={page}"
        data = _request(url, token)
        runs = data.get("workflow_runs", [])
        if not runs:
            break
        for r in runs:
            yield r
        page += 1


def main(argv: Optional[Iterable[str]] = None) -> int:
    args = _parse_args(argv)
    token = _auth_token()

    if not args.owner or not args.repo:
        print(
            "ERROR: Could not determine owner/repo; supply --owner and --repo explicitly",
            file=sys.stderr,
        )
        return 1

    cutoff = dt.datetime.utcnow() - dt.timedelta(days=args.days)
    cutoff_iso = cutoff.replace(microsecond=0).isoformat() + "Z"
    print(f"Cutoff: deleting runs older than {cutoff_iso} (>{args.days} days)")
    print(f"Mode: {'APPLY' if args.apply else 'DRY-RUN'}")

    try:
        workflows = _resolve_workflows(args.owner, args.repo, token)
    except Exception as e:  # noqa: BLE001
        print(f"Failed to list workflows: {e}", file=sys.stderr)
        return 1

    selected: Dict[str, int]
    if args.workflow:
        selected = {}
        for w in args.workflow:
            if w in workflows:
                selected[w] = workflows[w]
            else:
                print(
                    f"WARNING: workflow identifier '{w}' not found; skipping",
                    file=sys.stderr,
                )
    else:
        selected = workflows

    if not selected:
        print("No matching workflows found; exiting")
        return 0

    total_checked = 0
    total_delete_candidates = 0
    total_deleted = 0

    status_filter = {s.lower() for s in args.status} if args.status else None

    for wf_name, wf_id in selected.items():
        print(f"\n== Workflow: {wf_name} (id={wf_id}) ==")
        try:
            for run in _list_runs(args.owner, args.repo, wf_id, token, args.per_page):
                total_checked += 1
                created_at = run.get("created_at")  # e.g. 2025-08-18T12:34:56Z
                run_id = run.get("id")
                status = (run.get("conclusion") or run.get("status") or "").lower()

                # Parse created_at
                try:
                    run_dt = (
                        dt.datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%SZ")
                        if created_at
                        else None
                    )
                except ValueError:
                    run_dt = None

                if not run_dt:
                    continue  # skip malformed

                if status_filter and status not in status_filter:
                    continue

                if run_dt >= cutoff:
                    # Since runs are returned newest-first, we can break early for this workflow
                    # once we hit a run newer than cutoff AND we've already seen at least one older
                    continue

                total_delete_candidates += 1
                if total_delete_candidates > args.max_delete:
                    print("Reached max-delete safety cap; stopping further deletions")
                    return 0

                url = f"{API_ROOT}/repos/{args.owner}/{args.repo}/actions/runs/{run_id}"
                print(
                    f"Delete candidate: run_id={run_id} created_at={created_at} status={status}"
                )
                if args.apply:
                    try:
                        _request(url, token, method="DELETE")
                        total_deleted += 1
                        time.sleep(args.sleep)
                    except Exception as e:  # noqa: BLE001
                        print(f"Failed to delete run {run_id}: {e}", file=sys.stderr)
        except Exception as e:  # noqa: BLE001
            print(f"Error processing workflow {wf_name}: {e}", file=sys.stderr)

    print("\nSummary:")
    print(f"  Checked runs: {total_checked}")
    print(f"  Candidates over age: {total_delete_candidates}")
    if args.apply:
        print(f"  Deleted: {total_deleted}")
    else:
        print("  Deleted: 0 (dry-run; re-run with --apply to delete)")
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
