#!/usr/bin/env python3
# file: scripts/template_repo/scaffold_template_repo.py
# version: 1.0.0
# guid: 7f2d3a2e-4b5c-8d9e-0f1a-2b3c4d5e6f70

"""
Scaffold a minimal, public-safe template repository to a target directory.

Design goals:
- No secrets written to disk. No tokens, passwords, or PATs.
- No git submodules or nested repositories are created.
- No network calls. Pure local file system operations.
- Idempotent: safe to re-run; won’t overwrite existing files unless --force is used.

What it creates:
- Core docs: README.md, LICENSE, CODE_OF_CONDUCT.md, CONTRIBUTING.md, SECURITY.md
- .github/ files: workflows (ci), issue templates, PR template, CODEOWNERS
- Basic .gitignore

By default, it does NOT run any git commands. See push_with_gh.py for optional publishing.
"""

from __future__ import annotations

import argparse
import dataclasses
import os
import sys
from pathlib import Path
from typing import Dict, List, Tuple

SUPPORTED_LICENSES: Dict[str, str] = {
    "MIT": """MIT License

Copyright (c) {year} {owner}

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to do so, subject to the
following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
""",
    "Apache-2.0": """Apache License
Version 2.0, January 2004
http://www.apache.org/licenses/

TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

Copyright (c) {year} {owner}

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
""",
}


README_TEMPLATE = """# {name}

{description}

## Status

This repository was created from an automated template scaffold. It intentionally
contains no secrets, tokens, or passwords. See `.github/` for CI and templates.

## License

This project is licensed under the {license} license. See [LICENSE](LICENSE).
"""

CODE_OF_CONDUCT = """# Code of Conduct

This project follows the Contributor Covenant Code of Conduct. Be respectful and
supportive. For issues, contact the maintainers via GitHub issues.
"""

CONTRIBUTING = """# Contributing

We welcome contributions! Please:

- Open an issue describing the change
- Follow conventional commit messages
- Add tests when applicable
- Avoid committing secrets or credentials
"""

SECURITY = """# Security Policy

Please report security issues privately via the repository's security advisory
workflow on GitHub. Do not open public issues for vulnerabilities.
"""

GITIGNORE = """# General
.DS_Store
*.log
logs/
dist/
build/
venv/
.venv/
__pycache__/
*.pyc
node_modules/
coverage*
*.out
"""

WORKFLOW_CI = """name: CI

on:
  push:
    branches: [ main, master ]
  pull_request:
    branches: [ main, master ]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Show repo info
        run: |
          echo "Repository: ${{ github.repository }}"
          echo "Ref: ${{ github.ref }}"
"""

ISSUE_TEMPLATE_BUG = """---
name: Bug report
about: Create a report to help us improve
title: "[BUG]"
labels: bug
assignees: ''
---

Describe the bug and steps to reproduce.
"""

ISSUE_TEMPLATE_FEATURE = """---
name: Feature request
about: Suggest an idea for this project
title: "[FEAT]"
labels: enhancement
assignees: ''
---

Describe the feature and rationale.
"""

PULL_REQUEST_TEMPLATE = """## Summary

Briefly describe the change and motivation.

## Testing

How did you test this change?

## Related Issues

Link to issues if applicable.
"""

CODEOWNERS = """* @OWNER_USERNAME
"""


@dataclasses.dataclass
class Options:
    name: str
    owner: str
    description: str
    license: str
    year: str
    target_dir: Path
    dry_run: bool
    force: bool


def render_license(license_id: str, owner: str, year: str) -> str:
    template = SUPPORTED_LICENSES.get(license_id)
    if not template:
        raise ValueError(
            f"Unsupported license '{license_id}'. Supported: {', '.join(SUPPORTED_LICENSES)}"
        )
    return template.format(owner=owner, year=year)


def plan_files(opts: Options) -> List[Tuple[Path, str]]:
    root = opts.target_dir
    files: List[Tuple[Path, str]] = []

    files.append(
        (
            root / "README.md",
            README_TEMPLATE.format(
                name=opts.name, description=opts.description, license=opts.license
            ),
        )
    )
    files.append(
        (root / "LICENSE", render_license(opts.license, opts.owner, opts.year))
    )
    files.append((root / "CODE_OF_CONDUCT.md", CODE_OF_CONDUCT))
    files.append((root / "CONTRIBUTING.md", CONTRIBUTING))
    files.append((root / "SECURITY.md", SECURITY))
    files.append((root / ".gitignore", GITIGNORE))

    # .github structure
    files.append(
        (
            root / ".github" / "CODEOWNERS",
            CODEOWNERS.replace("OWNER_USERNAME", opts.owner),
        )
    )
    files.append((root / ".github" / "pull_request_template.md", PULL_REQUEST_TEMPLATE))
    files.append(
        (root / ".github" / "ISSUE_TEMPLATE" / "bug_report.md", ISSUE_TEMPLATE_BUG)
    )
    files.append(
        (
            root / ".github" / "ISSUE_TEMPLATE" / "feature_request.md",
            ISSUE_TEMPLATE_FEATURE,
        )
    )
    files.append((root / ".github" / "workflows" / "ci.yml", WORKFLOW_CI))

    return files


def ensure_parents(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def write_file(path: Path, content: str, force: bool) -> None:
    if path.exists() and not force:
        return
    ensure_parents(path)
    path.write_text(content, encoding="utf-8")


def print_plan(files: List[Tuple[Path, str]]) -> None:
    for p, _ in files:
        print(p)


def normalize_path(p: str) -> Path:
    return Path(os.path.expanduser(os.path.expandvars(p))).resolve()


def parse_args(argv: List[str]) -> Options:
    parser = argparse.ArgumentParser(
        description="Scaffold a public-safe template repository (no secrets, no submodules)."
    )
    parser.add_argument(
        "--name", required=True, help="Repository name (e.g., my-template-repo)"
    )
    parser.add_argument(
        "--owner",
        required=True,
        help="GitHub owner/org (used for CODEOWNERS and copyright)",
    )
    parser.add_argument(
        "--description", default="A minimal public-safe template repository."
    )
    parser.add_argument(
        "--license", choices=list(SUPPORTED_LICENSES.keys()), default="MIT"
    )
    parser.add_argument("--year", default="2025")
    parser.add_argument(
        "--target", required=True, help="Target directory to create the repository in"
    )
    parser.add_argument(
        "--dry-run", action="store_true", help="Only print files that would be created"
    )
    parser.add_argument(
        "--force", action="store_true", help="Overwrite existing files when present"
    )

    args = parser.parse_args(argv)
    target_dir = normalize_path(args.target)

    return Options(
        name=args.name,
        owner=args.owner,
        description=args.description,
        license=args.license,
        year=args.year,
        target_dir=target_dir,
        dry_run=args.dry_run,
        force=args.force,
    )


def assert_no_nested_repo(target_dir: Path) -> None:
    # Ensure we don't accidentally create a git repo inside another repo as a submodule-like structure
    # by checking for .git presence in ancestors (informational) and in target (prevent creation here).
    if (target_dir / ".git").exists():
        # Do not delete or modify; just warn and continue (we won't run git here anyway).
        print(
            "Warning: target directory contains a .git folder. This script does not run git commands.",
            file=sys.stderr,
        )


def main(argv: List[str]) -> int:
    opts = parse_args(argv)
    assert_no_nested_repo(opts.target_dir)
    files = plan_files(opts)

    if opts.dry_run:
        print_plan(files)
        return 0

    for path, content in files:
        write_file(path, content, force=opts.force)

    print(f"Scaffold complete at: {opts.target_dir}")
    print(
        "Note: No git commands were executed. Use push_with_gh.py if you want to publish."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
