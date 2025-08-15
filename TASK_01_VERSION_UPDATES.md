<!-- file: TASK_01_VERSION_UPDATES.md -->
<!-- version: 1.0.0 -->
<!-- guid: a1b2c3d4-e5f6-7a8b-9c0d-1e2f3a4b5c6d -->

# TASK 01: Go and Python Version Requirements Update

## 🎯 OBJECTIVE
Update all Go and Python version requirements across all repositories to use Go 1.23+ and Python 3.13+ as minimum requirements.

## 📋 SCOPE
This task covers updating version requirements in all repositories in the workspace:
- `/Users/jdfalk/repos/github.com/jdfalk/gcommon`
- `/Users/jdfalk/repos/github.com/jdfalk/ghcommon`
- `/Users/jdfalk/repos/github.com/jdfalk/subtitle-manager`
- `/Users/jdfalk/repos/github.com/jdfalk/audiobook-organizer`
- `/Users/jdfalk/repos/github.com/jdfalk/copilot-agent-util-rust`

## 🚨 CRITICAL INSTRUCTIONS

### Documentation Updates
**NEVER edit markdown files directly. ALWAYS use the documentation update system:**

1. **Create documentation updates**:
   ```bash
   ./scripts/create-doc-update.sh [filename] "[content]" [mode] --issue [issue-number]
   ```

2. **Available modes**:
   - `append` - Add content to end of file
   - `prepend` - Add content to beginning of file
   - `replace-section` - Replace specific section
   - `changelog-entry` - Add properly formatted changelog entry

### VS Code Tasks Priority
**MANDATORY: Always use VS Code tasks first before manual commands:**

1. **Use VS Code tasks** via `run_task` tool when available
2. **Check task logs** in `logs/` folder for results
3. **Manual commands** only as last resort

## 📖 CODING INSTRUCTIONS

### Go Instructions (Minimum Go 1.23+)

```markdown
<!-- file: .github/instructions/go.instructions.md -->
<!-- version: 1.3.0 -->
<!-- guid: 4f5a6b7c-8d9e-0f1a-2b3c-4d5e6f7a8b9c -->
<!-- DO NOT EDIT: This file is managed centrally in ghcommon repository -->
<!-- To update: Create an issue/PR in jdfalk/ghcommon -->

---
applyTo: "**/*.go"
description: |
  Go language-specific coding, documentation, and testing rules for Copilot/AI agents and VS Code Copilot customization. These rules extend the general instructions in `general-coding.instructions.md` and merge all unique content from the Google Go Style Guide.
---

# Go Coding Instructions

- Follow the [general coding instructions](general-coding.instructions.md).
- Follow the
  [Google Go Style Guide](https://google.github.io/styleguide/go/index.html) for
  additional best practices.
- All Go files must begin with the required file header (see general
  instructions for details and Go example).

## Version Requirements

- **MANDATORY**: All Go projects must use Go 1.23 or higher
- Update `go.mod` files to specify `go 1.23` minimum
- Update `go.work` files to specify `go 1.23` minimum
- All Go file headers must use version 1.23.0 or higher

## Core Principles

- Clarity over cleverness: Code should be clear and readable
- Simplicity: Prefer simple solutions over complex ones
- Consistency: Follow established patterns within the codebase
- Readability: Code is written for humans to read

## Naming Conventions

- Use short, concise, evocative package names (lowercase, no underscores)
- Use camelCase for unexported names, PascalCase for exported names
- Use short names for short-lived variables, descriptive names for longer-lived
  variables
- Use PascalCase for exported constants, camelCase for unexported constants
- Single-method interfaces should end in "-er" (e.g., Reader, Writer)

## Code Organization

- Use `goimports` to format imports automatically
- Group imports: standard library, third-party, local
- No blank lines within groups, one blank line between groups
- Keep functions short and focused
- Use blank lines to separate logical sections
- Order: receiver, name, parameters, return values

## Formatting

- Use tabs for indentation, spaces for alignment
- Opening brace on same line as declaration, closing brace on its own line
- No strict line length limit, but aim for readability

## Comments

- Every package should have a package comment
- Public functions must have comments starting with the function name
- Comment exported variables, explain purpose and constraints

## Error Handling

- Use lowercase for error messages, no punctuation at end
- Be specific about what failed
- Create custom error types for specific error conditions
- Use `errors.Is` and `errors.As` for error checking

## Best Practices

- Use short variable declarations (`:=`) when possible
- Use `var` for zero values or when type is important
- Use `make()` for slices and maps with known capacity
- Accept interfaces, return concrete types
- Keep interfaces small and focused
- Use channels for communication between goroutines
- Use sync primitives for protecting shared state
- Test file names end with `_test.go`, test function names start with `Test`
- Use table-driven tests for multiple scenarios

## Required File Header

All Go files must begin with a standard header as described in the
[general coding instructions](general-coding.instructions.md). Example for Go:

```go
// file: path/to/file.go
// version: 1.23.0
// guid: 123e4567-e89b-12d3-a456-426614174000
```
```

### Python Instructions (Minimum Python 3.13+)

```markdown
<!-- file: .github/instructions/python.instructions.md -->
<!-- version: 1.3.0 -->
<!-- guid: 2a5b7c8d-9e1f-4a2b-8c3d-6e9f1a5b7c8d -->
<!-- DO NOT EDIT: This file is managed centrally in ghcommon repository -->
<!-- To update: Create an issue/PR in jdfalk/ghcommon -->

---
applyTo: "**/*.py"
description: |
  Python language-specific coding, documentation, and testing rules for Copilot/AI agents and VS Code Copilot customization. These rules extend the general instructions in `general-coding.instructions.md` and merge all unique content from the Google Python Style Guide.
---

# Python Coding Instructions

- Follow the [general coding instructions](general-coding.instructions.md).
- Follow the
  [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
  for additional best practices.
- All Python files must begin with the required file header (see general
  instructions for details and Python example).

## Version Requirements

- **MANDATORY**: All Python projects must use Python 3.13 or higher
- Update `requirements.txt` files to specify `python>=3.13`
- Update `pyproject.toml` files to specify `requires-python = ">=3.13"`
- Update `setup.py` files to specify `python_requires=">=3.13"`
- All Python file headers must use version 1.23.0 or higher (following Go version alignment)

## Core Principles

- Be consistent: Follow the established patterns in your codebase
- Readability counts: Code is read more often than it is written
- Simple is better than complex: Prefer clarity over cleverness
- Use tools: Leverage formatters like `ruff`, `black`, and `isort` for
  consistency

## Language Rules

- Use `pylint` with Google's pylintrc configuration
- Use absolute imports, never relative
- Avoid mutable global state
- Use nested functions only when closing over a local value
- Use comprehensions for simple cases
- Use default iterators and operators
- Use generators as needed
- Use lambda for one-liners, prefer generator expressions
- Use properties for simple computations
- Use implicit false when possible, `if foo is None:` for None checks
- Do not use mutable objects as default argument values
- Use 4 spaces for indentation, never tabs
- Maximum line length is 80 characters
- Use parentheses for implied line continuation
- Two blank lines between top-level definitions
- One blank line between method definitions
- Use triple-double-quotes for docstrings, Google-style docstring format
- Use f-strings, `%` operator, or `format()` for formatting
- Use `with` statements for resource management

## Required File Header

All Python files must begin with a standard header as described in the
[general coding instructions](general-coding.instructions.md). Example for Python:

```python
#!/usr/bin/env python3
# file: path/to/file.py
# version: 1.23.0
# guid: 123e4567-e89b-12d3-a456-426614174000
```
```

### Rust Utility Instructions

```markdown
<!-- file: .github/instructions/rust-utility.instructions.md -->
<!-- version: 1.2.0 -->
<!-- guid: a1b2c3d4-e5f6-7890-1234-567890abcdef -->

---

applyTo: "\*\*"
description: |
Instructions for using the copilot-agent-util Rust utility as the primary tool for development operations. This utility provides superior performance, memory safety, and comprehensive command coverage compared to manual terminal commands.

---

# Copilot Agent Utility (Rust) - Command Reference

The `copilot-agent-util` (or `copilot-agent-utilr`) is a comprehensive Rust-based development utility that provides superior performance, memory safety, and extensive command coverage. **Always prefer this utility over manual commands when available.**

## 📥 Installation & Download

**Download the copilot-agent-util tool from:**
- **Source Repository**: https://github.com/jdfalk/copilot-agent-util-rust
- **Installation**: Follow the installation instructions in the repository's README
- **Requirements**: The tool is required for proper VS Code task execution and logging

**If the tool is not available in your environment:**
1. Clone the repository: `git clone https://github.com/jdfalk/copilot-agent-util-rust`
2. Build with Cargo: `cargo build --release`
3. Add to PATH or use the binary directly from `target/release/copilot-agent-util`

## 🚨 PRIORITY ORDER FOR OPERATIONS

**MANDATORY: Follow this exact priority when performing ANY operation:**

1. **FIRST**: Use VS Code tasks (via `run_task` tool) when available
2. **SECOND**: Use `copilot-agent-util` / `copilot-agent-utilr` Rust utility
3. **LAST RESORT**: Manual terminal commands only if neither above option exists

[Complete utility documentation continues...]
```

## 🎯 TASK BREAKDOWN

### Phase 1: Update Go Version Requirements (30 minutes)

1. **Find all go.mod files**:
   ```bash
   find /Users/jdfalk/repos/github.com/jdfalk -name "go.mod" -type f
   ```

2. **Update each go.mod file** to specify `go 1.23` or higher

3. **Update go.work files** (if any exist)

4. **Update Go file headers** to use version 1.23.0 or higher

### Phase 2: Update Python Version Requirements (30 minutes)

1. **Find Python requirements files**:
   ```bash
   find /Users/jdfalk/repos/github.com/jdfalk -name "requirements.txt" -o -name "pyproject.toml" -o -name "setup.py" -type f
   ```

2. **Update each requirements file** to specify Python 3.13+ minimum

3. **Update Python file headers** to use version 1.23.0 or higher

### Phase 3: Verify Changes (15 minutes)

1. **Use VS Code tasks** to check for issues

2. **Run go mod tidy** on all Go modules

3. **Verify Python requirements** parse correctly

## 📝 FILES TO UPDATE

### Go Files
- All `go.mod` files throughout workspace
- All `go.work` files (if any)
- All `*.go` file headers to use version 1.23.0+

### Python Files
- All `requirements.txt` files
- All `pyproject.toml` files
- All `setup.py` files
- All `*.py` file headers to use version 1.23.0+

## ✅ SUCCESS CRITERIA

1. **All go.mod files** specify `go 1.23` or higher
2. **All Python requirement files** specify Python 3.13+ minimum
3. **All Go and Python file headers** use version 1.23.0 or higher
4. **No build errors** when running `go mod tidy`
5. **Python requirements** parse without errors

## 🔄 COMMIT STRATEGY

Create a single commit with all version updates:

```
feat(version): update Go to 1.23+ and Python to 3.13+ requirements

Updated all Go and Python version requirements across repositories to use
modern language versions for better performance and security.

Files changed:
- All go.mod files - Updated to require Go 1.23+
- All Python requirement files - Updated to require Python 3.13+
- All Go/Python file headers - Updated to version 1.23.0+
```

## 🚨 IMPORTANT NOTES

- **Follow VS Code tasks priority** - use tasks before manual commands
- **Use documentation update scripts** - never edit docs directly
- **Include complete file paths** in commit messages
- **Test changes** before committing
- **Maintain file header formats** exactly as specified
