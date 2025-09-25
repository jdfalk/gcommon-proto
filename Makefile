# file: Makefile
# version: 2.0.0
# guid: 6ba7b810-9dad-11d1-80b4-00c04fd430c8

# Variables
BUF := buf
PYTHON := python3

# Directories
PROTO_DIR := proto
SCRIPTS_DIR := scripts

# Main targets
.PHONY: all generate clean help version proto-docs

all: lint

# Validate protobuf definitions (no code generation)
generate:
	@echo "🔄 Running buf generate (validation only)..."
	$(BUF) generate
	@echo "✅ Protobuf validation complete!"

# Generate proto docs
proto-docs:
	@echo "📚 Generating proto docs..."
	$(PYTHON) $(SCRIPTS_DIR)/generate_proto_docs.py --proto-dir proto/gcommon/v1 --out proto-docs --threshold 50
	@echo "✅ Proto docs generated"

# Clean generated files (minimal - just docs)
clean:
	@echo "🧹 Cleaning generated files..."
	rm -rf proto-docs/
	@echo "✅ Clean complete!"

# Lint protobuf files
lint:
	@echo "🔍 Linting protobuf files..."
	$(BUF) lint

# Format protobuf files
format:
	@echo "📝 Formatting protobuf files..."
	$(BUF) format -w

# Create a new version tag
tag:
	@echo "🏷️  Current tags:"
	@git tag --list | sort -V | tail -5
	@echo ""
	@echo "To create a new tag, run: git tag v1.x.x && git push origin v1.x.x"

# Show current version
version:
	@echo "📦 Current version:"
	@git describe --tags --abbrev=0 2>/dev/null || echo "No tags found"

# Development workflow
dev: lint format generate proto-docs

# Help
help:
	@echo "🚀 gcommon Protocol Buffer Definitions"
	@echo ""
	@echo "Available targets:"
	@echo "  all            - Default target, runs lint"
	@echo "  generate       - Validate protobuf definitions (no code generation)"
	@echo "  proto-docs     - Generate protocol buffer documentation"
	@echo "  clean          - Remove generated files"
	@echo "  lint           - Lint protobuf files"
	@echo "  format         - Format protobuf files"
	@echo "  tag            - Show current tags and tag creation instructions"
	@echo "  version        - Show current version"
	@echo "  dev            - Development workflow (lint + format + generate + docs)"
	@echo "  help           - Show this help message"
	@echo ""
	@echo "Note: This repository only contains protocol buffer definitions."
	@echo "Generated code is available in language-specific repositories:"
	@echo "  - Go: https://github.com/jdfalk/gcommon-go"
	@echo "  - Python: https://github.com/jdfalk/gcommon-py"
