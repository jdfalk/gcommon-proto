# Contributing to GCommon

Thank you for your interest in contributing to GCommon! This guide will help you understand our development workflow, coding standards, and contribution process.

## 🚀 Quick Start for New Contributors

### Prerequisites

- Go 1.21+ installed
- Git configured with your GitHub account
- Basic understanding of Protocol Buffers and gRPC

### Setting Up Your Development Environment

1. **Fork and clone the repository:**

   ```bash
   git clone https://github.com/YOUR_USERNAME/gcommon.git
   cd gcommon
   ```

2. **Set up the development environment:**

   ```bash
   make setup-dev
   go mod tidy
   ```

3. **Verify your setup:**
   ```bash
   make status
   make validate
   ```

## 📋 Issue Workflow

**CRITICAL:** All development work must include proper GitHub issue tracking using our automated workflow.

### Starting Work on an Issue

1. **Assign yourself and mark the issue as in progress:**

   ```bash
   ./scripts/create-issue-update.sh update ISSUE_NUMBER "" "in-progress"
   # Or manually:
   echo '[{"action": "update", "number": ISSUE_NUMBER, "assignees": ["your-github-username"], "labels": ["in-progress"]}]' > issue_updates.json
   git add issue_updates.json && git commit -m "Start work on issue #ISSUE_NUMBER: [Brief Description]" && git push
   ```

2. **Clean up the update file after each push:**
   ```bash
   rm issue_updates.json
   ```

### During Development

- **Reference Issues:** Always include issue numbers in commit messages (`#ISSUE_NUMBER`)
- **Progress Updates:** Add comments to issues for significant progress using:
  ```bash
  ./scripts/create-issue-update.sh comment ISSUE_NUMBER "Progress update text"
  ```
- **Label Changes:** Update labels if priority or scope changes

### Completing Work

```bash
# Close issue and mark completed
./scripts/create-issue-update.sh close ISSUE_NUMBER "completed"
# Or manually:
echo '[{"action": "update", "number": ISSUE_NUMBER, "state": "closed", "labels": ["completed"]}]' > issue_updates.json
git add issue_updates.json && git commit -m "Complete issue #ISSUE_NUMBER: [What was accomplished]" && git push
```

### Using scripts/create-issue-update.sh

The `scripts/create-issue-update.sh` script is the **required** way to manage GitHub issues programmatically:

```bash
# Create a new issue
./scripts/create-issue-update.sh create "Issue Title" "Issue body" "label1,label2"

# Update an existing issue
./scripts/create-issue-update.sh update 123 "Updated body" "label1,label2"

# Add a comment to an issue
./scripts/create-issue-update.sh comment 123 "Comment text"

# Close an issue
./scripts/create-issue-update.sh close 123 "completed"
```

**Best practices:**

- Use clear, concise titles and bodies
- Use comma-separated labels (no spaces)
- Always check the script output for success and file path
- Do not manually edit or move generated files
- Let the workflow process and archive files as needed

## 💻 Code Style Guidelines

### Go

- Use `gofmt` or `go fmt` to format code
- Tabs for indentation, line length <100 chars
- Package names: short, lowercase, no underscores
- Interface names: -er suffix for actions (e.g., `Reader`, `Writer`)
- Variable/function names: MixedCaps, not underscores
- Exported names: Capitalized; unexported: lowercase
- Acronyms all caps (e.g., `HTTPServer`, `URLPath`)
- Group imports: stdlib, third-party, project
- All exported declarations must have doc comments
- Always check errors, return errors (not panic)
- Early returns to reduce nesting
- Defer file/resource closing
- Use context for cancellation/deadlines
- Keep functions short and focused
- Prefer value receivers unless mutation is needed
- Use channels for concurrency, avoid shared memory

### Protocol Buffers

- Follow [Google's Protocol Buffer Style Guide](https://developers.google.com/protocol-buffers/docs/style)
- Use snake_case for field names
- Use PascalCase for message and service names
- Include comprehensive documentation for all messages and services
- Validate protobuf compilation with `make validate`

### Markdown

- Use consistent heading hierarchy
- Fenced code blocks with language specification
- Line length: 80-100 characters
- Use meaningful link text
- Use `-` for bullet points
- Blank lines around code blocks and headers

## 📝 Commit Message Standards

We use [Conventional Commits](https://www.conventionalcommits.org/) format:

### Format

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

### Types

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code changes that neither fix bugs nor add features
- `perf`: Performance improvements
- `test`: Adding or updating tests
- `build`: Changes to build system or dependencies
- `ci`: Changes to CI configuration
- `chore`: Other changes that don't modify src or test files
- `revert`: Reverting a previous commit

### Required Elements

**REQUIRED:** Always include a "Files changed:" section in the commit body:

```markdown
Files changed:

- Added feature: [src/feature.go](src/feature.go)
- Updated tests: [test/feature_test.go](test/feature_test.go)
```

### Examples

```bash
feat(metrics): add Prometheus counter implementation

Add Prometheus-based counter implementation for metrics collection.
Includes support for labels and proper error handling.

Files changed:

- Added implementation: [pkg/metrics/prometheus/counter.go](pkg/metrics/prometheus/counter.go)
- Added tests: [pkg/metrics/prometheus/counter_test.go](pkg/metrics/prometheus/counter_test.go)

Fixes #68
```

### Guidelines

- Use imperative present tense ("add" not "added")
- No period at end of description, keep under 50 characters
- Include motivation and contrast with previous behavior in body
- Reference real issues only: `Fixes #123` or `Closes #456`
- No commit should be submitted without file change documentation

## 🔄 Pull Request Process

### Before Creating a PR

1. **Ensure your branch is up to date:**

   ```bash
   git checkout main
   git pull origin main
   git checkout your-feature-branch
   git rebase main
   ```

2. **Run tests and validation:**

   ```bash
   make validate
   make test
   ```

3. **Check code formatting:**
   ```bash
   go fmt ./...
   ```

### PR Description Template

Use this template for your pull request description:

```markdown
## Description

[Concise overview of the changes]

## Motivation

[Why these changes were necessary]

## Changes

[Detailed list of changes made]

## Testing

[How the changes were tested]

## Screenshots

[If applicable]

## Related Issues

[Links to related tickets/issues]
```

### Guidelines

- Be concise, focus on what/why
- Use bullet points for changes
- Describe how changes were tested
- Link to all relevant issues/tickets
- For breaking changes, include a "Breaking Changes" section

## 🧪 Testing

### Running Tests

```bash
# Run all tests
make test

# Run tests for specific module
go test ./pkg/metrics/... -v

# Run tests with coverage
go test ./... -coverprofile=coverage.out
go tool cover -html=coverage.out
```

### Writing Tests

- Write comprehensive tests for new functionality
- Follow existing test naming conventions in the codebase
- Include edge cases and error handling in tests
- Document tests with clear descriptions of what's being tested
- Maintain test coverage when modifying existing code
- Use table-driven tests for multiple test cases

### Test Guidelines

```go
func TestFeatureName(t *testing.T) {
    tests := []struct {
        name     string
        input    InputType
        expected ExpectedType
        wantErr  bool
    }{
        {
            name:     "valid input case",
            input:    validInput,
            expected: expectedOutput,
            wantErr:  false,
        },
        // More test cases...
    }

    for _, tt := range tests {
        t.Run(tt.name, func(t *testing.T) {
            result, err := YourFunction(tt.input)
            if (err != nil) != tt.wantErr {
                t.Errorf("YourFunction() error = %v, wantErr %v", err, tt.wantErr)
                return
            }
            if !reflect.DeepEqual(result, tt.expected) {
                t.Errorf("YourFunction() = %v, expected %v", result, tt.expected)
            }
        })
    }
}
```

## 🏗️ Development Workflow

### Project Structure

```
gcommon/
├── pkg/                    # Core library packages
│   ├── metrics/           # Metrics collection
│   ├── db/               # Database operations
│   ├── health/           # Health checking
│   └── ...
├── examples/             # Example applications
├── docs/                # Documentation
├── scripts/             # Development scripts
└── proto/              # Protocol buffer definitions
```

### Priority Areas for Contribution

Current development priorities:

1. **Completing Metrics Module** (75% → 100%)
2. **Finishing Logging Module** (50% → 100%)
3. **Documentation improvements**
4. **Example applications**

See [TODO.md](TODO.md) for detailed implementation status and [CHANGELOG.md](CHANGELOG.md) for technical architecture details.

### High-Impact Quick Wins

```bash
# Get current status
make status

# Check specific modules
make health-status
make config-status
make metrics-status
```

## 🔧 Development Tools

### Makefile Targets

- `make help` - Show all available commands
- `make status` - Get current implementation status
- `make validate` - Validate protobuf compilation
- `make compile` - Compile all protobuf files
- `make test` - Run all tests
- `make clean` - Clean generated files
- `make setup-dev` - Set up development environment

### Protobuf Development

```bash
# Validate protobuf files
make validate

# Compile protobuf files
make compile

# Check coverage
./validate_protobuf_coverage.py
```

## 🚨 Security & Best Practices

### Security Guidelines

- Avoid hardcoding sensitive information
- Use proper error handling and input validation
- Follow secure coding practices for Go
- Review dependencies for security vulnerabilities
- Use context for cancellation and timeouts

### Code Quality

- Write clear, self-documenting code
- Use meaningful variable and function names
- Keep functions small and focused
- Add comprehensive documentation for public APIs
- Follow established patterns in the codebase

## 📚 Additional Resources

### Documentation

- **[Getting Started Guide](docs/user/getting-started.md)** - Complete setup and first steps
- **[Project Roadmap](TODO.md)** - Implementation status and plans
- **[Technical Architecture](CHANGELOG.md)** - Detailed technical documentation
- **[Issue Management Workflow](ISSUE_MANAGEMENT.md)** - Detailed issue management process

### Module-Specific Guides

- [Metrics Collection](docs/user/metrics.md)
- [Logging](docs/user/logging.md)
- [Database Operations](docs/user/database.md)
- [Health Monitoring](docs/user/health-kubernetes.md)

### Getting Help

- **📖 Documentation**: [docs/](docs/) directory
- **💡 Examples**: [examples/](examples/) directory
- **🐛 Issues**: [GitHub Issues](https://github.com/jdfalk/gcommon/issues)
- **💬 Discussions**: [GitHub Discussions](https://github.com/jdfalk/gcommon/discussions)

## 📄 License

By contributing to GCommon, you agree that your contributions will be licensed under the [MIT License](LICENSE).

---

**Thank you for contributing to GCommon!** 🎉

For detailed agent and development guidelines, see [AGENTS.md](AGENTS.md).
