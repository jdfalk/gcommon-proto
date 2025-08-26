#!/usr/bin/env python3
# file: setup_dependabot_all_repos.py
# version: 1.0.0
# guid: f8e7d6c5-4b3a-2918-7654-3210fedcba98

"""
Setup comprehensive dependabot.yml files for all repositories.
Detects project languages and creates appropriate configurations.
"""

import uuid
from pathlib import Path
from typing import Dict, Set

import yaml


def detect_project_languages(repo_path: Path) -> Set[str]:
    """Detect programming languages and package managers used in a repository."""
    languages = set()

    # Check for various language indicators
    files_to_check = {
        "go.mod": "go",
        "Cargo.toml": "rust",
        "package.json": "npm",
        "requirements.txt": "python",
        "pyproject.toml": "python",
        "setup.py": "python",
        "Dockerfile": "docker",
        "docker-compose.yml": "docker",
        "docker-compose.yaml": "docker",
    }

    for file_name, language in files_to_check.items():
        if (repo_path / file_name).exists():
            languages.add(language)

    # Check for GitHub Actions
    github_workflows = repo_path / ".github" / "workflows"
    if github_workflows.exists() and any(github_workflows.glob("*.yml")):
        languages.add("github-actions")

    # Check for webui directory with package.json
    webui_package = repo_path / "webui" / "package.json"
    if webui_package.exists():
        languages.add("npm-webui")

    # Check for scripts directory with Python files
    scripts_dir = repo_path / "scripts"
    if scripts_dir.exists() and any(scripts_dir.glob("*.py")):
        languages.add("python-scripts")

    return languages


def generate_dependabot_config(languages: Set[str], repo_name: str) -> Dict:
    """Generate dependabot configuration based on detected languages."""

    config = {"version": 2, "updates": []}

    # Base configuration templates
    templates = {
        "go": {
            "package-ecosystem": "gomod",
            "directory": "/",
            "schedule": {
                "interval": "weekly",
                "day": "monday",
                "time": "09:00",
                "timezone": "America/New_York",
            },
            "open-pull-requests-limit": 5,
            "commit-message": {"prefix": "go", "include": "scope"},
            "labels": ["dependencies", "tech:go"],
            "allow": [{"dependency-type": "direct"}],
            "ignore": [
                {
                    "dependency-name": "*",
                    "update-types": ["version-update:semver-major"],
                }
            ],
        },
        "rust": {
            "package-ecosystem": "cargo",
            "directory": "/",
            "schedule": {
                "interval": "weekly",
                "day": "monday",
                "time": "10:00",
                "timezone": "America/New_York",
            },
            "open-pull-requests-limit": 5,
            "commit-message": {"prefix": "rust", "include": "scope"},
            "labels": ["dependencies", "tech:rust"],
            "allow": [{"dependency-type": "direct"}],
            "ignore": [
                {
                    "dependency-name": "*",
                    "update-types": ["version-update:semver-major"],
                }
            ],
        },
        "npm": {
            "package-ecosystem": "npm",
            "directory": "/",
            "schedule": {
                "interval": "weekly",
                "day": "tuesday",
                "time": "09:00",
                "timezone": "America/New_York",
            },
            "open-pull-requests-limit": 8,
            "commit-message": {"prefix": "npm", "include": "scope"},
            "labels": ["dependencies", "tech:nodejs"],
            "allow": [{"dependency-type": "direct"}, {"dependency-type": "indirect"}],
            "ignore": [
                {
                    "dependency-name": "*",
                    "update-types": ["version-update:semver-major"],
                }
            ],
            "groups": {
                "dev-dependencies": {
                    "patterns": ["*eslint*", "*prettier*", "*commitlint*", "@types/*"],
                    "update-types": ["minor", "patch"],
                }
            },
        },
        "npm-webui": {
            "package-ecosystem": "npm",
            "directory": "/webui",
            "schedule": {
                "interval": "weekly",
                "day": "tuesday",
                "time": "10:00",
                "timezone": "America/New_York",
            },
            "open-pull-requests-limit": 8,
            "commit-message": {"prefix": "npm", "include": "scope"},
            "labels": ["dependencies", "tech:typescript", "ui"],
            "allow": [{"dependency-type": "direct"}, {"dependency-type": "indirect"}],
            "ignore": [
                {
                    "dependency-name": "*",
                    "update-types": ["version-update:semver-major"],
                }
            ],
            "groups": {
                "dev-dependencies": {
                    "patterns": ["*eslint*", "*prettier*", "*commitlint*", "@types/*"],
                    "update-types": ["minor", "patch"],
                }
            },
        },
        "python": {
            "package-ecosystem": "pip",
            "directory": "/",
            "schedule": {
                "interval": "weekly",
                "day": "tuesday",
                "time": "11:00",
                "timezone": "America/New_York",
            },
            "open-pull-requests-limit": 3,
            "commit-message": {"prefix": "python", "include": "scope"},
            "labels": ["dependencies", "tech:python"],
            "allow": [{"dependency-type": "direct"}],
            "ignore": [
                {
                    "dependency-name": "*",
                    "update-types": ["version-update:semver-major"],
                }
            ],
        },
        "python-scripts": {
            "package-ecosystem": "pip",
            "directory": "/scripts",
            "schedule": {
                "interval": "weekly",
                "day": "tuesday",
                "time": "12:00",
                "timezone": "America/New_York",
            },
            "open-pull-requests-limit": 3,
            "commit-message": {"prefix": "python", "include": "scope"},
            "labels": ["dependencies", "tech:python"],
            "allow": [{"dependency-type": "direct"}],
            "ignore": [
                {
                    "dependency-name": "*",
                    "update-types": ["version-update:semver-major"],
                }
            ],
        },
        "docker": {
            "package-ecosystem": "docker",
            "directory": "/",
            "schedule": {
                "interval": "weekly",
                "day": "wednesday",
                "time": "09:00",
                "timezone": "America/New_York",
            },
            "open-pull-requests-limit": 3,
            "commit-message": {"prefix": "docker", "include": "scope"},
            "labels": ["dependencies", "tech:docker"],
        },
        "github-actions": {
            "package-ecosystem": "github-actions",
            "directory": "/",
            "schedule": {
                "interval": "weekly",
                "day": "wednesday",
                "time": "10:00",
                "timezone": "America/New_York",
            },
            "open-pull-requests-limit": 5,
            "commit-message": {"prefix": "ci", "include": "scope"},
            "labels": ["dependencies", "github-actions", "ci-cd"],
            "groups": {
                "ci-dependencies": {
                    "patterns": ["actions/*", "github/*"],
                    "update-types": ["minor", "patch"],
                },
                "external-actions": {
                    "patterns": ["*"],
                    "exclude-patterns": ["actions/*", "github/*"],
                    "update-types": ["minor", "patch"],
                },
            },
        },
    }

    # Add configurations for detected languages
    for language in sorted(languages):
        if language in templates:
            config["updates"].append(templates[language])

    return config


def create_dependabot_file(repo_path: Path, repo_name: str) -> bool:
    """Create or update dependabot.yml file for a repository."""
    try:
        # Detect languages
        languages = detect_project_languages(repo_path)

        if not languages:
            print(f"  No supported languages detected in {repo_name}")
            return False

        print(f"  Detected languages: {', '.join(sorted(languages))}")

        # Generate configuration
        config = generate_dependabot_config(languages, repo_name)

        # Create .github directory if it doesn't exist
        github_dir = repo_path / ".github"
        github_dir.mkdir(exist_ok=True)

        # Write dependabot.yml
        dependabot_file = github_dir / "dependabot.yml"

        # Create file header
        header_lines = [
            "# file: .github/dependabot.yml",
            "# version: 1.0.0",
            f"# guid: {str(uuid.uuid4())}",
            "",
            f"# Smart Dependabot configuration for {repo_name}",
            f"# Supports: {', '.join(sorted(languages))}",
            "",
        ]

        with open(dependabot_file, "w") as f:
            # Write header
            for line in header_lines:
                f.write(line + "\n")

            # Write YAML configuration
            yaml.dump(config, f, default_flow_style=False, sort_keys=False)

        print(
            f"  ✅ Created dependabot.yml with {len(config['updates'])} configurations"
        )
        return True

    except Exception as e:
        print(f"  ❌ Error creating dependabot.yml: {e}")
        return False


def main():
    """Main function to setup dependabot for all repositories."""
    print("🔧 Setting up comprehensive dependabot.yml files for all repositories")

    # Define repository paths
    base_path = Path.home() / "repos" / "github.com" / "jdfalk"

    repos = [
        "gcommon",
        "ghcommon",
        "subtitle-manager",
        "copilot-agent-util-rust",
        "apt-cacher-go",
        "audiobook-organizer",
        "public-scratch",
    ]

    success_count = 0
    total_count = len(repos)

    for repo_name in repos:
        repo_path = base_path / repo_name

        if not repo_path.exists():
            print(f"⚠️  Repository {repo_name} not found at {repo_path}")
            continue

        print(f"\n📁 Processing {repo_name}...")

        if create_dependabot_file(repo_path, repo_name):
            success_count += 1

    print(
        f"\n🎉 Setup complete! Successfully configured {success_count}/{total_count} repositories"
    )

    if success_count < total_count:
        print(
            "⚠️  Some repositories could not be processed. Check the output above for details."
        )


if __name__ == "__main__":
    main()
