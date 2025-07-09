<!-- file: .github/copilot-instructions.md -->
<!-- version: 1.0.0 -->
<!-- guid: 2b3c4d5e-6f7a-8b9c-0d1e-2f3a4b5c6d7e -->

# GCommon - Copilot/AI Agent Coding Instructions System

This repository uses a centralized, modular system for Copilot/AI agent coding, documentation, and workflow instructions, following the latest VS Code Copilot customization best practices.

## System Overview

- **General rules**: `.github/instructions/general-coding.instructions.md` (applies to all files)
- **Language/task-specific rules**: `.github/instructions/*.instructions.md` (with `applyTo` frontmatter)
- **Prompt files**: `.github/prompts/` (for Copilot/AI prompt customization)
- **Agent-specific docs**: `.github/AGENTS.md`, `.github/CLAUDE.md`, etc. (pointers to this system)
- **VS Code integration**: `.vscode/copilot/` contains symlinks to canonical `.github/instructions/` files for VS Code Copilot features

## How It Works

- **General instructions** are always included for all files and languages.
- **Language/task-specific instructions** extend the general rules and use the `applyTo` field to target file globs (e.g., `**/*.go`, `**/*.proto`).
- **All code style, documentation, and workflow rules are now found exclusively in `.github/instructions/*.instructions.md` files.**
- **Prompt files** are stored in `.github/prompts/` and can reference instructions as needed.
- **Agent docs** (e.g., AGENTS.md) point to `.github/` as the canonical source for all rules.
- **VS Code** uses symlinks in `.vscode/copilot/` to include these instructions for Copilot customization.

## Project-Specific Context

This is the **GCommon** repository, focused on common Go libraries and Protocol Buffer definitions for distributed systems.

**Primary Languages**: Go, Protocol Buffers
**Key Features**: gRPC services, common data structures, shared utilities

## For Contributors

- **Edit or add rules** in `.github/instructions/` only. Do not use or reference any `code-style-*.md` files; these are obsolete.
- **Add new prompts** in `.github/prompts/`.
- **Update agent docs** to reference this system.
- **Do not duplicate rules**; always reference the general instructions from specific ones.
- **See `.github/README.md`** for a human-friendly summary and contributor guide.

For full details, see the [general coding instructions](instructions/general-coding.instructions.md) and language-specific files in `.github/instructions/`.
- Prefer explicit type annotations where applicable
- Keep functions small and focused on a single responsibility
- Use meaningful variable names that indicate purpose
- Refer to language-specific style guidelines in `.github/code-style-*.md` files which override these general guidelines when conflicts occur

## Testing

- Write comprehensive tests for new functionality
- When updating tests, update the documentation to maintain consistency
- Follow test naming conventions used in the codebase
- Include edge cases and error handling in tests
- Maintain test coverage when modifying existing code
- Follow additional testing guidelines specified in `.github/testing-*.md` files which override these general guidelines when conflicts occur

## Security & Best Practices

- Avoid hardcoding sensitive information
- Follow secure coding practices
- Use proper error handling
- Validate inputs appropriately
- Consider performance implications of code changes

## Version Control

- Write clear commit messages that explain the purpose of changes
- Keep pull requests focused on a single feature or fix
- Reference issue numbers in commits and PRs when applicable
- Follow commit message guidelines specified in `.github/commit-messages-*.md` files which override these general guidelines when conflicts occur

## Project-Specific

- Import from project modules rather than duplicating functionality
- Respect the established architecture patterns
- Before suggesting one-off commands, first check if there's a defined task in tasks.json that can accomplish the same goal
