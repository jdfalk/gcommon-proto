#!/usr/bin/env python3
# file: scripts/create_gcommon_repos.py
# version: 1.0.0
# guid: 4f5e6d7c-8b9a-1c2d-3e4f-5a6b7c8d9e0f

"""
Automated script to create gcommon-go and gcommon-py repositories with proper
scaffolding, GitHub Actions workflows, and protocol buffer integration.

This script creates language-specific repositories that sync protocol buffer
definitions from the main gcommon repository and generate language-specific
code with shared utilities and helper functions.
"""

import os
import sys
import subprocess
import tempfile
from pathlib import Path
from typing import Dict
import requests
import time

# Repository configuration
REPOS_CONFIG = {
    'gcommon-go': {
        'description': 'Go SDK for gcommon protocol buffers with shared utilities and helper functions',
        'language': 'go',
        'module_name': 'github.com/jdfalk/gcommon-go',
        'main_package': 'gcommon',
        'buf_plugins': ['protoc-gen-go', 'protoc-gen-go-grpc'],
        'dependencies': [
            'google.golang.org/protobuf@latest',
            'google.golang.org/grpc@latest'
        ]
    },
    'gcommon-py': {
        'description': 'Python SDK for gcommon protocol buffers with shared utilities and helper functions',
        'language': 'python',
        'package_name': 'gcommon',
        'buf_plugins': ['python', 'pyi'],
        'dependencies': [
            'protobuf>=3.20.0',
            'grpcio>=1.50.0',
            'grpcio-tools>=1.50.0'
        ]
    }
}

class GCommonRepoCreator:
    def __init__(self, github_token: str, org: str = "jdfalk"):
        """Initialize the repository creator with GitHub credentials."""
        self.github_token = github_token
        self.org = org
        self.headers = {
            'Authorization': f'token {github_token}',
            'Accept': 'application/vnd.github.v3+json',
            'Content-Type': 'application/json'
        }
        self.base_url = 'https://api.github.com'
        
    def create_repository(self, repo_name: str, config: Dict) -> bool:
        """Create a new GitHub repository with the specified configuration."""
        print(f"Creating repository: {repo_name}")
        
        repo_data = {
            'name': repo_name,
            'description': config['description'],
            'private': False,
            'has_issues': True,
            'has_projects': False,
            'has_wiki': False,
            'has_downloads': True,
            'auto_init': False,
            'allow_squash_merge': True,
            'allow_merge_commit': False,
            'allow_rebase_merge': True,
            'delete_branch_on_merge': True
        }
        
        response = requests.post(
            f"{self.base_url}/user/repos",
            headers=self.headers,
            json=repo_data
        )
        
        if response.status_code == 201:
            print(f"✅ Repository {repo_name} created successfully")
            return True
        elif response.status_code == 422 and 'already exists' in response.text:
            print(f"⚠️  Repository {repo_name} already exists, continuing...")
            return True
        else:
            print(f"❌ Failed to create repository {repo_name}: {response.text}")
            return False
    
    def clone_and_setup_repo(self, repo_name: str, config: Dict) -> bool:
        """Clone the repository and set up the initial structure."""
        print(f"Setting up repository structure for {repo_name}")
        
        # Create temporary directory for repo setup
        with tempfile.TemporaryDirectory() as temp_dir:
            repo_path = Path(temp_dir) / repo_name
            
            # Clone the repository using HTTPS with token authentication
            clone_url = f"https://{self.github_token}@github.com/{self.org}/{repo_name}.git"
            result = subprocess.run(['git', 'clone', clone_url, str(repo_path)], 
                                  capture_output=True, text=True)
            
            if result.returncode != 0:
                print(f"❌ Failed to clone repository: {result.stderr}")
                return False
                
            # Change to repo directory
            os.chdir(repo_path)
            
            # Create base structure
            self._create_base_structure(repo_path, repo_name, config)
            
            # Create language-specific structure
            if config['language'] == 'go':
                self._create_go_structure(repo_path, config)
            elif config['language'] == 'python':
                self._create_python_structure(repo_path, config)
                
            # Create GitHub Actions workflows
            self._create_workflows(repo_path, repo_name, config)
            
            # Commit and push initial structure
            subprocess.run(['git', 'add', '.'], check=True)
            subprocess.run(['git', 'commit', '-m', f'feat: initial {repo_name} repository structure\n\nCreated comprehensive repository structure with:\n- Protocol buffer integration from gcommon repo\n- Language-specific build configuration\n- GitHub Actions workflows for CI/CD\n- Automated version synchronization\n- Proper module/package structure'], check=True)
            subprocess.run(['git', 'push', 'origin', 'main'], check=True)
            
            print(f"✅ Repository {repo_name} setup completed successfully")
            return True
    
    def _create_base_structure(self, repo_path: Path, repo_name: str, config: Dict):
        """Create the base repository structure common to both languages."""
        
        # Create directories
        dirs = [
            '.github/workflows',
            '.github/instructions', 
            '.vscode',
            'scripts',
            'docs',
            'tests',
            'examples'
        ]
        
        for dir_path in dirs:
            (repo_path / dir_path).mkdir(parents=True, exist_ok=True)
            
        # Create README.md
        readme_content = f"""# {repo_name}

{config['description']}

## Overview

This repository provides {config['language'].upper()} bindings and utilities for the gcommon protocol buffer definitions. It automatically synchronizes with the main [gcommon](https://github.com/jdfalk/gcommon) repository to ensure protocol buffer definitions are always up to date.

## Features

- **Automated Protocol Buffer Sync**: Automatically pulls latest proto definitions from gcommon
- **Strict Version Synchronization**: Ensures version compatibility across all gcommon repositories
- **Shared Utilities**: Common helper functions and business logic implementations
- **CI/CD Integration**: Automated building, testing, and releasing
- **Documentation**: Comprehensive API documentation and examples

## Installation

### Using the Generated Code

```{"bash" if config['language'] == 'go' else 'bash'}
{"go get github.com/jdfalk/gcommon-go" if config['language'] == 'go' else 'pip install gcommon'}
```

### Development Setup

```bash
git clone https://github.com/jdfalk/{repo_name}.git
cd {repo_name}
{"make setup" if config['language'] == 'go' else 'pip install -e .[dev]'}
```

## Usage

See the [examples](examples/) directory for comprehensive usage examples.

## Version Synchronization

This repository maintains strict version synchronization with:
- [gcommon](https://github.com/jdfalk/gcommon) - Protocol buffer definitions
- [gcommon-go](https://github.com/jdfalk/gcommon-go) - Go SDK
- [gcommon-py](https://github.com/jdfalk/gcommon-py) - Python SDK

Version updates are automatically triggered when the gcommon repository releases new versions.

## Contributing

Please see [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
"""
        
        with open(repo_path / 'README.md', 'w') as f:
            f.write(readme_content)
            
        # Create basic files from template structure
        self._create_license(repo_path)
        self._create_contributing(repo_path)
        self._create_code_of_conduct(repo_path)
        self._create_security(repo_path)
        self._create_agents_md(repo_path)
        self._create_gitignore(repo_path, config['language'])
        self._create_buf_config(repo_path, repo_name, config)
        
    def _create_go_structure(self, repo_path: Path, config: Dict):
        """Create Go-specific repository structure."""
        
        # Create go.mod
        go_mod_content = f"""module {config['module_name']}

go 1.21

require (
    google.golang.org/protobuf v1.31.0
    google.golang.org/grpc v1.57.0
)
"""
        
        with open(repo_path / 'go.mod', 'w') as f:
            f.write(go_mod_content)
            
        # Create Makefile
        makefile_content = """# file: Makefile
# version: 1.0.0
# guid: makefile-gcommon-go-automation

.PHONY: help setup build test clean generate sync-protos install-tools

help: ## Show this help message
	@echo "Available targets:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \\033[36m%-15s\\033[0m %s\\n", $$1, $$2}'

setup: install-tools ## Set up development environment
	go mod download
	go mod tidy

install-tools: ## Install required tools
	go install google.golang.org/protobuf/cmd/protoc-gen-go@latest
	go install google.golang.org/grpc/cmd/protoc-gen-go-grpc@latest
	go install github.com/bufbuild/buf/cmd/buf@latest

generate: sync-protos ## Generate Go code from protocol buffers
	buf generate

sync-protos: ## Sync protocol buffer definitions from gcommon repo
	./scripts/sync-protos.sh

build: generate ## Build the Go module
	go build ./...

test: generate ## Run tests
	go test -v ./...

clean: ## Clean generated files
	find . -name "*.pb.go" -type f -delete
	find . -name "*_grpc.pb.go" -type f -delete
	rm -rf proto/

lint: ## Run linters
	golangci-lint run

doc: ## Generate documentation
	godoc -http=:6060

.DEFAULT_GOAL := help
"""
        
        with open(repo_path / 'Makefile', 'w') as f:
            f.write(makefile_content)
            
        # Create example Go file
        (repo_path / 'examples').mkdir(exist_ok=True)
        example_go = """// file: examples/basic_usage.go
// version: 1.0.0
// guid: example-go-basic-usage

package main

import (
	"fmt"
	"log"

	// Import the generated protobuf packages
	// Note: These will be available after running 'make generate'
)

func main() {
	fmt.Println("gcommon-go basic usage example")
	
	// TODO: Add examples once protobuf code is generated
	log.Println("Run 'make generate' to generate protocol buffer code")
}
"""
        
        with open(repo_path / 'examples/basic_usage.go', 'w') as f:
            f.write(example_go)
            
    def _create_python_structure(self, repo_path: Path, config: Dict):
        """Create Python-specific repository structure."""
        
        # Create pyproject.toml
        pyproject_content = f"""[build-system]
requires = ["setuptools>=45", "wheel", "setuptools-scm[toml]>=6.2"]
build-backend = "setuptools.build_meta"

[project]
name = "{config['package_name']}"
description = "{config['description']}"
readme = "README.md"
requires-python = ">=3.8"
license = {{text = "MIT"}}
authors = [
    {{name = "jdfalk", email = "jdfalk@users.noreply.github.com"}},
]
classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9", 
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: System :: Networking",
]
dependencies = [
    "protobuf>=3.20.0",
    "grpcio>=1.50.0",
    "grpcio-tools>=1.50.0",
]
dynamic = ["version"]

[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",
    "pytest-cov>=4.0.0",
    "black>=22.0.0",
    "isort>=5.0.0",
    "mypy>=1.0.0",
    "grpcio-testing>=1.50.0",
]

[project.urls]
Homepage = "https://github.com/jdfalk/{repo_path.name}"
Repository = "https://github.com/jdfalk/{repo_path.name}"
Issues = "https://github.com/jdfalk/{repo_path.name}/issues"

[tool.setuptools]
packages = ["gcommon"]

[tool.setuptools_scm]

[tool.black]
line-length = 100
target-version = ['py38']

[tool.isort]
profile = "black"
line_length = 100

[tool.mypy]
python_version = "3.8"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
"""
        
        with open(repo_path / 'pyproject.toml', 'w') as f:
            f.write(pyproject_content)
            
        # Create package structure
        package_dir = repo_path / config['package_name']
        package_dir.mkdir(exist_ok=True)
        
        # Create __init__.py
        init_content = f'''"""
{config['description']}

This package provides Python bindings for the gcommon protocol buffers.
"""

# file: {config['package_name']}/__init__.py
# version: 1.0.0  
# guid: gcommon-py-package-init

__version__ = "0.1.0"
__author__ = "jdfalk"
__email__ = "jdfalk@users.noreply.github.com"

# Import common utilities when they're available
try:
    from .utils import *
except ImportError:
    # Utils not yet generated
    pass

# Version info
__all__ = ["__version__", "__author__", "__email__"]
'''
        
        with open(package_dir / '__init__.py', 'w') as f:
            f.write(init_content)
            
        # Create Makefile for Python
        makefile_content = """# file: Makefile
# version: 1.0.0
# guid: makefile-gcommon-py-automation

.PHONY: help setup build test clean generate sync-protos install-tools

help: ## Show this help message
	@echo "Available targets:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \\033[36m%-15s\\033[0m %s\\n", $$1, $$2}'

setup: install-tools ## Set up development environment
	pip install -e .[dev]

install-tools: ## Install required tools
	pip install buf grpcio-tools

generate: sync-protos ## Generate Python code from protocol buffers
	buf generate

sync-protos: ## Sync protocol buffer definitions from gcommon repo
	./scripts/sync-protos.sh

build: generate ## Build the Python package
	python -m build

test: generate ## Run tests
	pytest tests/ -v --cov=gcommon

clean: ## Clean generated files
	find . -name "*_pb2.py" -type f -delete
	find . -name "*_pb2_grpc.py" -type f -delete
	find . -name "*_pb2.pyi" -type f -delete
	rm -rf build/ dist/ *.egg-info/
	rm -rf proto/

lint: ## Run linters
	black .
	isort .
	mypy gcommon/

format: ## Format code
	black .
	isort .

install: build ## Install the package
	pip install dist/*.whl

.DEFAULT_GOAL := help
"""
        
        with open(repo_path / 'Makefile', 'w') as f:
            f.write(makefile_content)
            
        # Create example Python file
        example_py = '''"""
Basic usage example for gcommon-py

This example demonstrates how to use the generated protocol buffer code.
"""

# file: examples/basic_usage.py
# version: 1.0.0
# guid: example-py-basic-usage

import logging
import sys

# Import the generated protobuf packages
# Note: These will be available after running 'make generate'

def main():
    """Main example function."""
    print("gcommon-py basic usage example")
    
    # TODO: Add examples once protobuf code is generated
    logging.info("Run 'make generate' to generate protocol buffer code")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
'''
        
        with open(repo_path / 'examples/basic_usage.py', 'w') as f:
            f.write(example_py)

    def _create_buf_config(self, repo_path: Path, repo_name: str, config: Dict):
        """Create buf configuration files for protocol buffer generation."""
        
        # Create buf.yaml for external proto dependency
        buf_yaml_content = f"""# file: buf.yaml
# version: 1.0.0
# guid: buf-config-{repo_name}

version: v1
lint:
  use:
    - DEFAULT
breaking:
  use:
    - FILE
deps:
  - buf.build/protocolbuffers/protobuf
  - buf.build/grpc-ecosystem/grpc-gateway
"""
        
        with open(repo_path / 'buf.yaml', 'w') as f:
            f.write(buf_yaml_content)
            
        # Create buf.gen.yaml for code generation
        if config['language'] == 'go':
            buf_gen_content = f"""# file: buf.gen.yaml
# version: 1.0.0
# guid: buf-gen-config-{repo_name}

version: v1
plugins:
  - plugin: buf.build/protocolbuffers/go
    out: .
    opt:
      - paths=source_relative
      - module={config['module_name']}
  - plugin: buf.build/grpc/go
    out: .
    opt:
      - paths=source_relative
      - module={config['module_name']}
"""
        else:  # Python
            buf_gen_content = f"""# file: buf.gen.yaml
# version: 1.0.0
# guid: buf-gen-config-{repo_name}

version: v1
plugins:
  - plugin: buf.build/protocolbuffers/python
    out: .
  - plugin: buf.build/protocolbuffers/pyi
    out: .
"""
        
        with open(repo_path / 'buf.gen.yaml', 'w') as f:
            f.write(buf_gen_content)
            
    def _create_workflows(self, repo_path: Path, repo_name: str, config: Dict):
        """Create GitHub Actions workflows."""
        
        # Create CI workflow
        ci_workflow = f"""# file: .github/workflows/ci.yml
# version: 1.0.0
# guid: ci-workflow-{repo_name}

name: CI

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v4
    
    - name: Set up {"Go" if config['language'] == 'go' else "Python"}
      uses: {"actions/setup-go@v4" if config['language'] == 'go' else "actions/setup-python@v4"}
      with:
        {"go-version: '1.21'" if config['language'] == 'go' else "python-version: '3.11'"}
        
    - name: Install buf
      run: |
        BUF_VERSION="1.26.1"
        curl -sSL "https://github.com/bufbuild/buf/releases/download/v${{BUF_VERSION}}/buf-$(uname -s)-$(uname -m)" -o "/usr/local/bin/buf"
        chmod +x "/usr/local/bin/buf"
        
    - name: Setup dependencies
      run: make setup
      
    - name: Generate protocol buffers
      run: make generate
      
    - name: Run tests
      run: make test
      
    - name: Run linting
      run: make lint
"""
        
        with open(repo_path / '.github/workflows/ci.yml', 'w') as f:
            f.write(ci_workflow)
            
        # Create proto sync workflow
        sync_workflow = f"""# file: .github/workflows/sync-protos.yml
# version: 1.0.0
# guid: sync-protos-workflow-{repo_name}

name: Sync Protocol Buffers

on:
  schedule:
    - cron: '0 6 * * *'  # Daily at 6 AM UTC
  workflow_dispatch:
  repository_dispatch:
    types: [proto-updated]

jobs:
  sync-protos:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v4
      with:
        token: ${{{{ secrets.GITHUB_TOKEN }}}}
        
    - name: Set up {"Go" if config['language'] == 'go' else "Python"}
      uses: {"actions/setup-go@v4" if config['language'] == 'go' else "actions/setup-python@v4"}
      with:
        {"go-version: '1.21'" if config['language'] == 'go' else "python-version: '3.11'"}
        
    - name: Install buf
      run: |
        BUF_VERSION="1.26.1"
        curl -sSL "https://github.com/bufbuild/buf/releases/download/v${{BUF_VERSION}}/buf-$(uname -s)-$(uname -m)" -o "/usr/local/bin/buf"
        chmod +x "/usr/local/bin/buf"
        
    - name: Setup dependencies
      run: make setup
      
    - name: Sync protocol buffers from gcommon
      run: make sync-protos
      
    - name: Generate code
      run: make generate
      
    - name: Check for changes
      id: changes
      run: |
        if git diff --quiet; then
          echo "changed=false" >> $GITHUB_OUTPUT
        else
          echo "changed=true" >> $GITHUB_OUTPUT
        fi
        
    - name: Commit changes
      if: steps.changes.outputs.changed == 'true'
      run: |
        git config --local user.email "action@github.com"
        git config --local user.name "GitHub Action"
        git add .
        git commit -m "feat(proto): sync protocol buffers from gcommon

        Automated sync of protocol buffer definitions and regeneration of language-specific code.
        
        Generated by: GitHub Actions workflow"
        git push
"""
        
        with open(repo_path / '.github/workflows/sync-protos.yml', 'w') as f:
            f.write(sync_workflow)
    
    def _create_license(self, repo_path: Path):
        """Create MIT license file."""
        license_content = """MIT License

Copyright (c) 2025 jdfalk

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
"""
        
        with open(repo_path / 'LICENSE', 'w') as f:
            f.write(license_content)
    
    def _create_contributing(self, repo_path: Path):
        """Create contributing guidelines."""
        contributing_content = """# Contributing

We welcome contributions! Please:

- Open an issue describing the change
- Follow conventional commit messages
- Add tests when applicable
- Avoid committing secrets or credentials
- Update documentation as needed

## Development Process

1. Fork the repository
2. Create a feature branch
3. Make changes with tests
4. Run the full test suite
5. Submit a pull request

## Code Style

- Follow language-specific style guides
- Use meaningful variable and function names
- Add comments for complex logic
- Keep functions focused and small

## Testing

All changes should include appropriate tests. Run the test suite with:

```bash
make test
```

## Questions

Feel free to open an issue for questions or discussion.
"""
        
        with open(repo_path / 'CONTRIBUTING.md', 'w') as f:
            f.write(contributing_content)
    
    def _create_code_of_conduct(self, repo_path: Path):
        """Create code of conduct."""
        coc_content = """# Code of Conduct

This project follows the Contributor Covenant Code of Conduct. Be respectful and
supportive. For issues, contact the maintainers via GitHub issues.
"""
        
        with open(repo_path / 'CODE_OF_CONDUCT.md', 'w') as f:
            f.write(coc_content)
    
    def _create_security(self, repo_path: Path):
        """Create security policy."""
        security_content = """# Security Policy

Please report security issues privately via the repository's security advisory
workflow on GitHub. Do not open public issues for vulnerabilities.
"""
        
        with open(repo_path / 'SECURITY.md', 'w') as f:
            f.write(security_content)
    
    def _create_agents_md(self, repo_path: Path):
        """Create AGENTS.md pointer file."""
        agents_content = """<!-- file: AGENTS.md -->
<!-- version: 1.0.0 -->
<!-- guid: 2e7c1a4b-5d3f-4b8c-9e1f-7a6b2c3d4e5f -->

# AGENTS.md

> NOTE: This is a pointer. All detailed Copilot, agent, and workflow instructions are in the `.github/` directory.

## Canonical Source for Agent Instructions

- General rules: `.github/instructions/`
- System documentation: `.github/copilot-instructions.md`

> For any agent, Copilot, or workflow task, **always refer to the above files.**
"""
        
        with open(repo_path / 'AGENTS.md', 'w') as f:
            f.write(agents_content)
    
    def _create_gitignore(self, repo_path: Path, language: str):
        """Create language-specific .gitignore file."""
        if language == 'go':
            gitignore_content = """# Binaries for programs and plugins
*.exe
*.exe~
*.dll
*.so
*.dylib

# Test binary, built with `go test -c`
*.test

# Output of the go coverage tool, specifically when used with LiteIDE
*.out

# Dependency directories (remove the comment below to include it)
# vendor/

# Go workspace file
go.work

# IDE
.vscode/
.idea/

# Generated protocol buffer files
*.pb.go
*_grpc.pb.go

# Temporary proto directory
proto/

# Logs
logs/
*.log

# OS
.DS_Store
Thumbs.db
"""
        else:  # Python
            gitignore_content = """# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
.hypothesis/
.pytest_cache/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
.python-version

# celery beat schedule file
celerybeat-schedule

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Generated protocol buffer files
*_pb2.py
*_pb2_grpc.py
*_pb2.pyi

# Temporary proto directory
proto/

# IDE
.vscode/
.idea/
*.swp
*.swo

# Logs
logs/
*.log

# OS
.DS_Store
Thumbs.db
"""
        
        with open(repo_path / '.gitignore', 'w') as f:
            f.write(gitignore_content)
    
    def create_sync_script(self, repo_path: Path, repo_name: str):
        """Create the proto synchronization script."""
        script_path = repo_path / 'scripts/sync-protos.sh'
        script_content = f"""#!/bin/bash
# file: scripts/sync-protos.sh
# version: 1.0.0
# guid: sync-protos-script-{repo_name}

set -euo pipefail

# Configuration
GCOMMON_REPO="https://github.com/jdfalk/gcommon.git"
PROTO_DIR="proto"
TEMP_DIR=$(mktemp -d)

echo "🔄 Syncing protocol buffers from gcommon repository..."

# Clean up on exit
cleanup() {{
    rm -rf "$TEMP_DIR"
}}
trap cleanup EXIT

# Clone gcommon repository to temporary directory
echo "📥 Cloning gcommon repository..."
git clone --depth 1 "$GCOMMON_REPO" "$TEMP_DIR/gcommon"

# Remove existing proto directory
if [ -d "$PROTO_DIR" ]; then
    echo "🗑️  Removing existing proto directory..."
    rm -rf "$PROTO_DIR"
fi

# Copy proto files from gcommon
echo "📋 Copying protocol buffer files..."
cp -r "$TEMP_DIR/gcommon/proto" "$PROTO_DIR"

# Copy buf configuration if it doesn't exist or is outdated
if [ ! -f "buf.yaml" ] || [ "$TEMP_DIR/gcommon/buf.yaml" -nt "buf.yaml" ]; then
    echo "⚙️  Updating buf.yaml configuration..."
    cp "$TEMP_DIR/gcommon/buf.yaml" "buf.yaml"
fi

# Update buf.lock
echo "🔒 Updating buf.lock..."
buf mod update

echo "✅ Protocol buffer sync completed successfully!"
echo "🏗️  Run 'make generate' to regenerate language-specific code."
"""
        
        script_path.parent.mkdir(parents=True, exist_ok=True)
        with open(script_path, 'w') as f:
            f.write(script_content)
        
        # Make script executable
        os.chmod(script_path, 0o755)
    
    def create_all_repositories(self, dry_run=False) -> bool:
        """Create all gcommon repositories with proper configuration."""
        success = True
        
        if dry_run:
            print("🔍 DRY RUN MODE: Would create all repositories")
            for repo_name, config in REPOS_CONFIG.items():
                print(f"  - Would create {repo_name} repository with {config['language']} configuration")
            return True
        
        for repo_name, config in REPOS_CONFIG.items():
            print(f"\n{'='*60}")
            print(f"Creating {repo_name} repository")
            print(f"{'='*60}")
            
            # Create repository
            if not self.create_repository(repo_name, config):
                success = False
                continue
                
            # Wait a moment for GitHub to propagate
            time.sleep(2)
            
            # Clone and setup repository
            if not self.clone_and_setup_repo(repo_name, config):
                success = False
                continue
        
        if success:
            print(f"\n{'='*60}")
            print("🎉 All repositories created successfully!")
            print(f"{'='*60}")
            print("\nNext steps:")
            print("1. Review the created repositories on GitHub")
            print("2. Clone them locally for development")
            print("3. Run 'make sync-protos' to get protocol buffer definitions")
            print("4. Run 'make generate' to generate language-specific code")
            print("5. Set up any additional secrets or configuration needed")
        else:
            print("\n❌ Some repositories failed to create. Check the output above.")
            
        return success
    
    def create_specific_repository(self, repo_name: str, dry_run=False) -> bool:
        """Create a specific repository (gcommon-go or gcommon-py)"""
        if repo_name not in REPOS_CONFIG:
            print(f"❌ Error: Repository {repo_name} not found in configuration")
            return False
        
        config = REPOS_CONFIG[repo_name]
        
        if dry_run:
            print(f"🔍 DRY RUN MODE: Would create {repo_name} repository with {config['language']} configuration")
            return True
        
        print(f"\n{'='*60}")
        print(f"Creating {repo_name} repository")
        print(f"{'='*60}")
        
        # Create repository
        if not self.create_repository(repo_name, config):
            return False
            
        # Wait a moment for GitHub to propagate
        time.sleep(2)
        
        # Clone and setup repository
        if not self.clone_and_setup_repo(repo_name, config):
            return False
        
        print(f"\n✅ {repo_name} repository created successfully!")
        return True

def main():
    """Main entry point for the repository creation script."""
    import argparse
    import subprocess
    
    parser = argparse.ArgumentParser(description="Create gcommon SDK repositories with full scaffolding")
    parser.add_argument('--token', help="GitHub token (or use gh auth token)")
    parser.add_argument('--create-go', action='store_true', help="Create gcommon-go repository only")
    parser.add_argument('--create-py', action='store_true', help="Create gcommon-py repository only")
    parser.add_argument('--create-all', action='store_true', help="Create both repositories")
    parser.add_argument('--dry-run', action='store_true', help="Show what would be created without executing")
    
    args = parser.parse_args()
    
    # Default to create all if no specific repo specified
    if not any([args.create_go, args.create_py, args.create_all]):
        args.create_all = True
        print("ℹ️  No specific repository specified, creating all repositories")
    
    # Get GitHub token
    github_token = args.token
    if not github_token:
        # Try to get token from gh CLI
        try:
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
    
    if args.dry_run:
        print("� DRY RUN MODE - No repositories will be created")
        print("Remove --dry-run to actually create repositories")
    
    print("🚀 Starting gcommon repository creation...")
    
    # Create repository creator
    creator = GCommonRepoCreator(github_token)
    
    # Create repositories based on arguments
    success = True
    if args.create_all:
        print("Creating both gcommon-go and gcommon-py repositories...")
        success = creator.create_all_repositories(dry_run=args.dry_run)
    else:
        if args.create_go:
            print("Creating gcommon-go repository...")
            success = creator.create_specific_repository("gcommon-go", dry_run=args.dry_run)
        if args.create_py:
            print("Creating gcommon-py repository...")
            success = creator.create_specific_repository("gcommon-py", dry_run=args.dry_run) and success
    
    sys.exit(0 if success else 1)

if __name__ == '__main__':
    main()