# gcommon Repository Ecosystem Automation

<!-- file: scripts/REPOSITORY_AUTOMATION.md -->
<!-- version: 1.0.0 -->
<!-- guid: gcommon-repository-automation-guide -->

This document describes the automated repository ecosystem for the gcommon protocol buffer definitions and language-specific SDKs.

## Architecture Overview

The gcommon ecosystem consists of three synchronized repositories:

- **`gcommon`** - Source repository with protocol buffer definitions
- **`gcommon-go`** - Go SDK with generated Go code and shared utilities
- **`gcommon-py`** - Python SDK with generated Python code and shared utilities

## Automation Scripts

### 1. Repository Creation Script

**File:** `scripts/create_gcommon_repos.py`

Creates the `gcommon-go` and `gcommon-py` repositories with complete scaffolding.

#### Features:
- Creates repositories via GitHub API
- Language-specific directory structures (Go modules, Python packages)
- Automated CI/CD workflows for each language
- Protocol buffer synchronization workflows
- Comprehensive documentation and configuration files

#### Usage

```bash
# Authenticate with GitHub CLI (recommended)
gh auth login

# Create both repositories with full scaffolding
python3 scripts/create_gcommon_repos.py --create-all

# Create only Go repository
python3 scripts/create_gcommon_repos.py --create-go

# Create only Python repository  
python3 scripts/create_gcommon_repos.py --create-py

# Dry run to see what would be created
python3 scripts/create_gcommon_repos.py --create-all --dry-run

# Use specific token if needed
python3 scripts/create_gcommon_repos.py --create-all --token "your_token"
```

#### Generated Structure:

**gcommon-go:**
```
gcommon-go/
├── go.mod                    # Go module definition
├── Makefile                  # Build automation
├── README.md                 # Usage documentation
├── CHANGELOG.md              # Release notes
├── .github/
│   ├── workflows/
│   │   ├── ci.yml           # Go CI pipeline
│   │   ├── release.yml      # Release automation
│   │   └── sync-protos.yml  # Proto synchronization
│   └── dependabot.yml       # Dependency management
├── gcommon/                  # Generated protobuf Go packages
├── shared/                   # Shared Go utilities
│   ├── config/              # Configuration helpers
│   ├── validation/          # Validation utilities
│   └── client/              # gRPC client helpers
└── examples/                 # Usage examples
```

**gcommon-py:**
```
gcommon-py/
├── setup.py                  # Python package setup
├── pyproject.toml           # Modern Python configuration
├── Makefile                 # Build automation
├── README.md                # Usage documentation
├── CHANGELOG.md             # Release notes
├── .github/
│   ├── workflows/
│   │   ├── ci.yml          # Python CI pipeline
│   │   ├── release.yml     # PyPI publishing
│   │   └── sync-protos.yml # Proto synchronization
│   └── dependabot.yml      # Dependency management
├── gcommon/                 # Generated protobuf Python packages
├── shared/                  # Shared Python utilities
│   ├── config/             # Configuration helpers
│   ├── validation/         # Validation utilities
│   └── client/             # gRPC client helpers
└── examples/                # Usage examples
```

### 2. Version Synchronization Manager

**File:** `scripts/version_sync_manager.py`

Manages semantic versioning and synchronization across all repositories.

#### Features:
- Cross-repository version compatibility checking
- Automated version bumping (major, minor, patch)
- Release coordination via GitHub API
- Compatibility matrix generation
- Workflow trigger automation

#### Usage

```bash
# Check current version status across all repositories
python3 scripts/version_sync_manager.py status

# Perform version synchronization (dry run by default)
python3 scripts/version_sync_manager.py sync --bump patch

# Execute actual version synchronization
python3 scripts/version_sync_manager.py sync --bump minor --execute

# Generate compatibility matrix report
python3 scripts/version_sync_manager.py matrix
```

#### Version Strategy:
- **Source of Truth:** `gcommon` repository versions drive all synchronization
- **Semantic Versioning:** Strict major.minor.patch versioning
- **Compatibility Rules:** 
  - Major version must match across repositories
  - Minor versions should not differ by more than 1
  - Patch versions can vary independently

#### Synchronization Process:
1. Query current versions from all repositories
2. Check compatibility and identify issues
3. Increment source version based on bump type
4. Create release in source repository
5. Trigger sync workflows in target repositories
6. Monitor and report synchronization status

## Workflow Integration

### Protocol Buffer Synchronization

Each target repository includes a `sync-protos.yml` workflow that:

1. **Triggers:** 
   - Repository dispatch from gcommon version sync
   - Manual workflow dispatch
   - Scheduled sync (daily at 02:00 UTC)

2. **Process:**
   - Downloads protocol buffer files from gcommon at specified version
   - Runs language-specific code generation (buf generate)
   - Updates generated code and shared utilities
   - Commits changes and creates pull request
   - Runs full test suite

3. **Validation:**
   - Syntax and compilation validation
   - Unit test execution
   - Integration test validation
   - Documentation generation

### Release Automation

Both target repositories include automated release workflows:

**Go Repository (`gcommon-go`):**
- Cross-platform binary compilation
- Go module version tagging
- GitHub release creation
- Documentation deployment

**Python Repository (`gcommon-py`):**
- Wheel and source distribution building
- PyPI package publishing
- Version tagging and release notes
- Documentation deployment

## Usage Examples

### Setting Up the Ecosystem

1. **Create repositories:**

   ```bash
   # Authenticate with GitHub CLI (recommended)
   gh auth login
   
   # Create both repositories
   python3 scripts/create_gcommon_repos.py --create-all
   ```

2. **Initial synchronization:**

   ```bash
   python3 scripts/version_sync_manager.py sync --bump minor --execute
   ```

3. **Verify setup:**

   ```bash
   python3 scripts/version_sync_manager.py status
   ```

### Daily Operations

1. **Check version status:**
   ```bash
   python3 scripts/version_sync_manager.py status
   ```

2. **Update protocol buffers and sync:**
   ```bash
   # Make changes to proto files in gcommon
   # Then synchronize with patch version bump
   python3 scripts/version_sync_manager.py sync --bump patch --execute
   ```

3. **Generate compatibility report:**
   ```bash
   python3 scripts/version_sync_manager.py matrix
   ```

### Development Workflow

1. **Protocol Buffer Changes:**
   - Make changes to `.proto` files in gcommon repository
   - Test locally with `buf lint` and `buf generate`
   - Commit and push changes to gcommon
   - Run version sync to propagate to SDK repositories

2. **Shared Utility Updates:**
   - Update utilities in target repositories
   - Test with generated protocol buffer code
   - Version compatibility is automatically checked

3. **Breaking Changes:**
   - Use `--bump major` for breaking protocol changes
   - Update compatibility documentation
   - Coordinate with downstream consumers

## Monitoring and Maintenance

### Health Checks
- Version compatibility monitoring
- Workflow execution status
- Dependency vulnerability scanning
- Documentation freshness

### Troubleshooting
- Check workflow logs in each repository
- Verify GitHub token permissions
- Validate protocol buffer syntax
- Monitor dependency updates

## Security Considerations

- **GitHub Token:** Requires repo, workflow, and admin permissions
- **Secrets Management:** Uses repository secrets for automation
- **Access Control:** Repository access controls SDK generation
- **Dependency Scanning:** Automated vulnerability monitoring

## Migration Guide

If migrating from manual SDK management:

1. Run repository creation script to set up automation
2. Import existing shared utilities to new structure
3. Verify generated code matches existing implementations
4. Update consumer applications to use new repository URLs
5. Set up version synchronization monitoring

---

For questions or issues with the repository automation system, check the workflow logs or create an issue in the gcommon repository.