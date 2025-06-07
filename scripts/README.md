# GitHub Project Manager

A comprehensive Python script for automating GitHub project setup and management. This tool provides idempotent operations for creating and managing GitHub labels, milestones, projects, and issues through JSON configuration files.

## Features

- **Configuration-driven**: Define all GitHub objects in JSON configuration files
- **Idempotent operations**: Safe to run multiple times without duplicates
- **Force updating**: Option to update existing objects
- **Dry-run mode**: Preview changes without making them
- **Comprehensive logging**: Detailed logs of all operations
- **Cross-repository reusable**: Use the same script across different repositories
- **Validation**: JSON schema validation for configuration files
- **Error handling**: Robust error handling with clear messages

## Prerequisites

- Python 3.7+
- GitHub CLI (`gh`) installed and authenticated
- Proper repository permissions for creating issues, projects, etc.

## Installation

1. Copy the script to your repository:
   ```bash
   mkdir -p scripts config
   cp github_project_manager.py scripts/
   ```

2. Install GitHub CLI if not already installed:
   ```bash
   # macOS
   brew install gh

   # Linux
   sudo apt install gh

   # Windows
   winget install GitHub.cli
   ```

3. Authenticate with GitHub:
   ```bash
   gh auth login
   ```

## Configuration

Create a JSON configuration file (e.g., `config/github_setup.json`) with the following structure:

```json
{
  "repository": {
    "owner": "your-username",
    "name": "your-repo",
    "description": "Repository description"
  },
  "labels": [
    {
      "name": "bug",
      "color": "D73A49",
      "description": "Something isn't working"
    }
  ],
  "milestones": [
    {
      "title": "v1.0.0",
      "description": "First release",
      "due_date": "2025-12-31T00:00:00Z"
    }
  ],
  "projects": [
    {
      "title": "Development",
      "body": "Main development project",
      "issue_patterns": ["Module", "Feature"]
    }
  ],
  "issues": [
    {
      "title": "Setup project",
      "body": "Initial project setup tasks",
      "labels": ["enhancement", "priority:high"],
      "milestone": "v1.0.0"
    }
  ]
}
```

### Configuration Schema

The configuration file follows a specific JSON schema. See `config/github_setup_schema.json` for the complete schema definition.

#### Repository Section
- `owner`: GitHub username or organization name
- `name`: Repository name
- `description`: Optional repository description

#### Labels Section
- `name`: Label name (required)
- `color`: 6-digit hex color code without # (required)
- `description`: Label description (optional)

#### Milestones Section
- `title`: Milestone title (required)
- `description`: Milestone description (optional)
- `due_date`: ISO 8601 formatted due date (optional)

#### Projects Section
- `title`: Project title (required)
- `body`: Project description (optional)
- `issue_patterns`: Array of strings to match in issue titles for auto-adding (optional)

#### Issues Section
- `title`: Issue title (required)
- `body`: Issue description in Markdown (optional)
- `labels`: Array of label names to apply (optional)
- `assignees`: Array of GitHub usernames to assign (optional)
- `milestone`: Milestone title to assign (optional)

## Usage

### Basic Usage

```bash
# Run with configuration file
python3 scripts/github_project_manager.py --config config/github_setup.json

# Run in dry-run mode (preview changes)
python3 scripts/github_project_manager.py --config config/github_setup.json --dry-run

# Force update existing objects
python3 scripts/github_project_manager.py --config config/github_setup.json --force-update

# Enable verbose logging
python3 scripts/github_project_manager.py --config config/github_setup.json --verbose
```

### Command Line Options

- `--config, -c`: Path to JSON configuration file (required)
- `--force-update, -f`: Force update existing objects
- `--dry-run, -n`: Run in dry-run mode (no actual changes)
- `--verbose, -v`: Enable verbose logging

### Operation Order

The script performs operations in the following order:

1. **Labels**: Create or update labels
2. **Milestones**: Create milestones
3. **Projects**: Create projects
4. **Issues**: Create or update issues
5. **Project Items**: Add issues to projects based on patterns

This order ensures dependencies are created before dependent objects.

## Examples

### Simple Project Setup

```json
{
  "repository": {
    "owner": "myorg",
    "name": "myproject"
  },
  "labels": [
    {"name": "bug", "color": "D73A49", "description": "Bug reports"},
    {"name": "enhancement", "color": "A2EEEF", "description": "New features"}
  ],
  "issues": [
    {
      "title": "Setup CI/CD pipeline",
      "body": "Configure automated testing and deployment",
      "labels": ["enhancement"]
    }
  ]
}
```

### Complex Multi-Module Project

```json
{
  "repository": {
    "owner": "myorg",
    "name": "microservices"
  },
  "labels": [
    {"name": "module:auth", "color": "FF6B6B", "description": "Auth module"},
    {"name": "module:billing", "color": "4ECDC4", "description": "Billing module"},
    {"name": "type:protobuf", "color": "0052CC", "description": "Protocol buffers"},
    {"name": "priority:high", "color": "D73A49", "description": "High priority"}
  ],
  "milestones": [
    {
      "title": "v0.1.0 - Foundation",
      "description": "Basic infrastructure and core modules",
      "due_date": "2025-03-01T00:00:00Z"
    }
  ],
  "projects": [
    {
      "title": "Development Tracking",
      "body": "Track all development work across modules",
      "issue_patterns": ["Module", "Feature", "Bug"]
    }
  ],
  "issues": [
    {
      "title": "Auth Module: Implement protobuf definitions",
      "body": "Define message types for authentication services",
      "labels": ["module:auth", "type:protobuf", "priority:high"],
      "milestone": "v0.1.0 - Foundation"
    },
    {
      "title": "Billing Module: Implement protobuf definitions",
      "body": "Define message types for billing services",
      "labels": ["module:billing", "type:protobuf", "priority:high"],
      "milestone": "v0.1.0 - Foundation"
    }
  ]
}
```

## Features in Detail

### Idempotent Operations

The script is designed to be run multiple times safely:

- **Labels**: Checks for existing labels and skips creation if they exist
- **Milestones**: Checks for existing milestones by title
- **Projects**: Checks for existing projects by title
- **Issues**: Checks for existing issues by title
- **Project Items**: Handles "already exists" errors gracefully

### Force Update Mode

When `--force-update` is specified:

- **Labels**: Updates color and description of existing labels
- **Issues**: Updates body, labels, assignees, and milestone of existing issues
- **Milestones**: Currently skipped (GitHub CLI limitation)
- **Projects**: Not applicable (projects are only created)

### Dry Run Mode

When `--dry-run` is specified:

- All GitHub CLI commands are logged but not executed
- Shows exactly what would be done without making changes
- Useful for validating configuration before running

### Error Handling

The script provides comprehensive error handling:

- **Configuration validation**: Validates JSON structure and required fields
- **GitHub CLI errors**: Captures and reports command failures
- **Dependency validation**: Ensures GitHub CLI is installed
- **Network issues**: Handles API timeouts and connectivity problems

### Logging

Comprehensive logging system:

- **Console output**: Real-time progress and status
- **Log file**: Detailed log saved to `github_project_manager.log`
- **Levels**: Info, warning, error, and debug messages
- **Summary**: Final summary of operations and success rates

## Troubleshooting

### Common Issues

1. **GitHub CLI not found**
   ```
   Error: GitHub CLI (gh) not found. Please install it first.
   ```
   Solution: Install GitHub CLI and ensure it's in your PATH

2. **Authentication required**
   ```
   Error: authentication required
   ```
   Solution: Run `gh auth login` to authenticate

3. **Permission denied**
   ```
   Error: Resource not accessible by integration
   ```
   Solution: Ensure you have appropriate permissions for the repository

4. **Invalid configuration**
   ```
   Error: Required field 'repository' missing from config
   ```
   Solution: Check your JSON configuration against the schema

### Debug Mode

Enable verbose logging for detailed troubleshooting:

```bash
python3 scripts/github_project_manager.py --config config/github_setup.json --verbose
```

### Validation

Validate your configuration before running:

```bash
# Dry run to check configuration
python3 scripts/github_project_manager.py --config config/github_setup.json --dry-run
```

## Best Practices

1. **Start with dry-run**: Always test with `--dry-run` first
2. **Version control configs**: Keep configuration files in version control
3. **Modular configs**: Split large configurations into multiple files
4. **Backup before force-update**: Use force-update carefully
5. **Test incrementally**: Add objects gradually to test integration
6. **Monitor logs**: Check logs for warnings and errors
7. **Schema validation**: Validate JSON against the schema before running

## Contributing

Contributions are welcome! Please:

1. Follow the existing code style
2. Add tests for new features
3. Update documentation
4. Ensure backward compatibility

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Changelog

### v1.0.0
- Initial release
- Support for labels, milestones, projects, and issues
- Idempotent operations
- Force update and dry-run modes
- Comprehensive logging and error handling
- JSON schema validation
- Cross-repository reusability
