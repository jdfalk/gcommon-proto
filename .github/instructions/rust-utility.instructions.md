<!-- file: .github/instructions/rust-utility.instructions.md -->
<!-- version: 1.0.0 -->
<!-- guid: a1b2c3d4-e5f6-7890-1234-567890abcdef -->

---
applyTo: "**"
description: |
  Instructions for using the copilot-agent-util Rust utility as the primary tool for development operations. This utility provides superior performance, memory safety, and comprehensive command coverage compared to manual terminal commands.
---

# Copilot Agent Utility (Rust) - Command Reference

The `copilot-agent-util` (or `copilot-agent-utilr`) is a comprehensive Rust-based development utility that provides superior performance, memory safety, and extensive command coverage. **Always prefer this utility over manual commands when available.**

## 🚨 PRIORITY ORDER FOR OPERATIONS

**MANDATORY: Follow this exact priority when performing ANY operation:**

1. **FIRST**: Use VS Code tasks (via `run_task` tool) when available
2. **SECOND**: Use `copilot-agent-util` / `copilot-agent-utilr` Rust utility
3. **LAST RESORT**: Manual terminal commands only if neither above option exists

## Available Commands

### 🔧 Git Operations (Comprehensive)

The utility provides **complete git functionality** with 18+ subcommands:

```bash
# Git command structure
copilot-agent-utilr git <subcommand> [options] [args]

# Available git subcommands:
copilot-agent-utilr git add [files...]           # Add files to staging
copilot-agent-utilr git commit -m "message"      # Commit changes
copilot-agent-utilr git push                     # Push to remote
copilot-agent-utilr git pull                     # Pull from remote
copilot-agent-utilr git status                   # Show working tree status
copilot-agent-utilr git branch [name]            # List/create branches
copilot-agent-utilr git checkout <branch>        # Switch branches
copilot-agent-utilr git merge <branch>           # Merge branches
copilot-agent-utilr git rebase <branch>          # Rebase commits
copilot-agent-utilr git reset [options]          # Reset state
copilot-agent-utilr git log [options]            # Show commit history
copilot-agent-utilr git diff [options]           # Show differences
copilot-agent-utilr git stash [command]          # Stash changes
copilot-agent-utilr git remote [command]         # Manage remotes
copilot-agent-utilr git tag [options]            # Manage tags
copilot-agent-utilr git clone <url>              # Clone repository
copilot-agent-utilr git fetch                    # Fetch from remote
copilot-agent-utilr git init                     # Initialize repository
```

**Git Command Examples:**
```bash
# Status and basic operations
copilot-agent-utilr git status
copilot-agent-utilr git add .
copilot-agent-utilr git commit -m "feat: add new feature"
copilot-agent-utilr git push

# Branch operations
copilot-agent-utilr git branch feature-branch
copilot-agent-utilr git checkout feature-branch
copilot-agent-utilr git merge main

# Advanced operations
copilot-agent-utilr git log --oneline -10
copilot-agent-utilr git diff HEAD~1
copilot-agent-utilr git stash push -m "WIP changes"
```

### 📝 Text Processing

#### Sed Stream Editor
Superior Rust implementation of sed with full regex support:

```bash
# Sed command structure
copilot-agent-utilr sed [options] [files...]

# Common sed operations:
echo "text" | copilot-agent-utilr sed -e 's/old/new/g'        # Substitute
copilot-agent-utilr sed -i -e 's/old/new/g' file.txt         # In-place edit
copilot-agent-utilr sed -e '/pattern/d' file.txt             # Delete lines
copilot-agent-utilr sed -e '3,5p' -n file.txt                # Print specific lines
```

**Sed Options:**
- `-e, --expression <expression>`: Sed expression/script
- `-i, --in-place`: Edit files in place
- `--backup <SUFFIX>`: Backup suffix for in-place editing
- `-n, --quiet`: Suppress automatic printing
- `-r, --extended-regexp`: Use extended regular expressions

#### AWK Pattern Processing
Complete AWK interpreter with pattern matching and field processing:

```bash
# AWK command structure
copilot-agent-utilr awk 'program' [files...]

# Common AWK operations:
echo "one two three" | copilot-agent-utilr awk '{print $2}'  # Print second field
copilot-agent-utilr awk '/pattern/ {print $0}' file.txt      # Pattern matching
copilot-agent-utilr awk 'BEGIN{sum=0} {sum+=$1} END{print sum}' numbers.txt
```

**AWK Features:**
- Field processing (`$1`, `$2`, `$NF`, etc.)
- Pattern matching with regex
- Variables and arithmetic operations
- BEGIN and END blocks
- Built-in functions and operators

### ✏️ Custom Editor

Superior Rust-powered terminal editor with advanced features:

```bash
# Editor command structure
copilot-agent-utilr editor <file> [options]

# Editor options:
-l, --line <NUMBER>      # Start at specific line
-c, --column <NUMBER>    # Start at specific column
-r, --readonly           # Open in read-only mode
-s, --syntax <LANG>      # Syntax highlighting (rust, python, javascript, go)
```

**Editor Features:**
- **Vi-like keybindings** with multiple modes (normal, insert, command, search, visual)
- **Syntax highlighting** for Rust, Python, JavaScript, Go
- **File operations**: save, save-as, quit, force-quit
- **Search and replace** with regex support
- **Superior performance** with crossterm terminal integration

## 🔄 Integration with VS Code Tasks

Many repositories have VS Code tasks that use the Rust utility. **Always check for tasks first:**

```bash
# Example task usage (preferred method):
run_task("Git Status", "/path/to/workspace")           # Uses copilot-agent-utilr
run_task("Git Add All", "/path/to/workspace")          # Uses copilot-agent-utilr
run_task("Git Commit", "/path/to/workspace")           # Uses copilot-agent-utilr
run_task("Buf Generate with Output", "/path/to/workspace")  # Uses copilot-agent-utilr
```

## 📋 Usage Priority Examples

### Git Operations
```bash
# ✅ BEST: Use VS Code task (if available)
run_task("Git Status", "/path/to/workspace")

# ✅ GOOD: Use Rust utility directly
copilot-agent-utilr git status

# ❌ AVOID: Manual git command
git status
```

### Text Processing
```bash
# ✅ BEST: Use Rust utility
echo "data" | copilot-agent-utilr sed -e 's/old/new/'
echo "fields" | copilot-agent-utilr awk '{print $2}'

# ❌ AVOID: Manual commands
echo "data" | sed 's/old/new/'
echo "fields" | awk '{print $2}'
```

### File Editing
```bash
# ✅ BEST: Use Rust editor
copilot-agent-utilr editor myfile.rs --syntax rust

# ❌ AVOID: Manual editors
nano myfile.rs
vim myfile.rs
```

## 💡 Benefits of the Rust Utility

1. **Memory Safety**: Rust's borrow checker prevents memory errors
2. **Performance**: Native compiled binary with zero-cost abstractions
3. **Reliability**: Comprehensive error handling and type safety
4. **Consistency**: Unified interface across all development operations
5. **Logging**: Integrated logging for debugging and audit trails
6. **Cross-platform**: Works consistently across all operating systems

## 🚀 Advanced Usage

### Chaining Operations
```bash
# Complex git workflow
copilot-agent-utilr git add .
copilot-agent-utilr git commit -m "feat: implement new feature"
copilot-agent-utilr git push

# Text processing pipeline
copilot-agent-utilr sed -e 's/old/new/g' input.txt | \
copilot-agent-utilr awk '{print $1, $3}' > output.txt
```

### Error Handling
The Rust utility provides superior error messages and handling:
- Clear error descriptions with context
- Proper exit codes for automation
- Detailed logging for debugging
- Safe failure modes without data corruption

## 📚 Command Reference Summary

| Category | Command | Purpose |
|----------|---------|---------|
| Git | `copilot-agent-utilr git <subcommand>` | Complete git operations (18+ subcommands) |
| Text Processing | `copilot-agent-utilr sed <options>` | Stream editing with regex support |
| Text Processing | `copilot-agent-utilr awk '<program>'` | Pattern processing and field extraction |
| Editing | `copilot-agent-utilr editor <file>` | Superior terminal editor with syntax highlighting |

**Remember: Always use VS Code tasks first, then the Rust utility, and manual commands only as a last resort.**
