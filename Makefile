# file: Makefile
# version: 1.1.0
# guid: 6ba7b810-9dad-11d1-80b4-00c04fd430c8

# Variables
BUF := buf
PYTHON := python3
GO := go

# Directories
PROTO_DIR := proto
SDK_GO_DIR := sdks/go
SDK_PYTHON_DIR := sdks/python
SCRIPTS_DIR := scripts

# Main targets
.PHONY: all generate clean help version python-install

all: generate

# Generate protobuf code and run post-processing
generate:
	@echo "🔄 Running buf generate..."
	$(BUF) generate
	@echo "🔄 Setting up Go SDK..."
	$(PYTHON) $(SCRIPTS_DIR)/setup-go-modules.py
	@echo "🔄 Setting up Python SDK..."
	$(PYTHON) $(SCRIPTS_DIR)/setup-python-sdk.py
	@echo "📚 Generating proto docs..."
	$(PYTHON) $(SCRIPTS_DIR)/generate_proto_docs.py --proto-dir proto/gcommon/v1 --out proto-docs --threshold 50
	@echo "✅ Generation complete!"

# Generate proto docs only
.PHONY: proto-docs
proto-docs:
	@echo "📚 Generating proto docs (standalone)..."
	$(PYTHON) $(SCRIPTS_DIR)/generate_proto_docs.py --proto-dir proto/gcommon/v1 --out proto-docs --threshold 50 --verbose
	@echo "✅ Proto docs generated"

# Clean generated files
clean:
	@echo "🧹 Cleaning generated files..."
	rm -rf $(SDK_GO_DIR)/gcommon/
	rm -rf $(SDK_PYTHON_DIR)/gcommon/
	@echo "✅ Clean complete!"

# Lint protobuf files
lint:
	@echo "🔍 Linting protobuf files..."
	$(BUF) lint

# Format protobuf files
format:
	@echo "📝 Formatting protobuf files..."
	$(BUF) format -w

# Run go mod tidy in SDK directory
tidy:
	@echo "🧹 Running go mod tidy..."
	cd $(SDK_GO_DIR) && $(GO) mod tidy

# Install Python SDK in development mode
python-install:
	@echo "📦 Installing Python SDK in development mode..."
	cd $(SDK_PYTHON_DIR) && pip install -e .

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

# Full rebuild (clean + generate)
rebuild: clean generate

# Development workflow
dev: lint format generate

# Help
help:
	@echo "🚀 gcommon Protocol Buffer Management"
	@echo ""
	@echo "Available targets:"
	@echo "  all            - Default target, runs generate"
	@echo "  generate       - Generate protobuf code and run post-processing"
	@echo "  clean          - Remove generated files"
	@echo "  lint           - Lint protobuf files"
	@echo "  format         - Format protobuf files"
	@echo "  tidy           - Run go mod tidy in SDK directory"
	@echo "  python-install - Install Python SDK in development mode"
	@echo "  tag            - Show current tags and tag creation instructions"
	@echo "  version        - Show current version"
	@echo "  rebuild        - Clean and regenerate everything"
	@echo "  dev            - Development workflow (lint + format + generate)"
	@echo "  help           - Show this help message"
	@echo ""
	@echo "Examples:"
	@echo "  make generate       # Generate code"
	@echo "  make dev            # Development workflow"
	@echo "  make rebuild        # Full rebuild"
	@echo "  make python-install # Install Python SDK for development"
