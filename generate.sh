#!/bin/bash
# file: generate.sh
# Script to generate all protobuf/gRPC code and mocks using buf

set -e

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
cd "${SCRIPT_DIR}"

echo "=== Generating all protobuf/gRPC code and mocks using buf ==="

# ----------------------------------------
# Check Dependencies
# ----------------------------------------
echo ""
echo "=== Checking dependencies ==="

# Check if buf is installed
if ! command -v buf &> /dev/null; then
    echo "Error: buf is not installed or not in PATH."
    echo "Please install buf: https://buf.build/docs/installation"
    exit 1
fi

# Check if mockery is installed
if ! command -v mockery &> /dev/null; then
    echo "Error: mockery is not installed or not in PATH."
    echo "Please install mockery: go install github.com/vektra/mockery/v2@latest"
    exit 1
fi

# ----------------------------------------
# Protobuf/gRPC Code Generation with buf
# ----------------------------------------
echo ""
echo "=== Generating protobuf/gRPC code with buf ==="

# Lint protobuf files (with relaxed rules)
echo "=== Linting protobuf files ==="
buf lint || echo "Warning: Some lint issues found, but continuing..."

# Generate code using buf
echo "=== Generating Go code from protobuf files ==="
buf generate

echo "=== Protobuf/gRPC code generation complete ==="

# ----------------------------------------
# Mock Generation
# ----------------------------------------
echo ""
echo "=== Generating mocks ==="

# Create all required mock directories if they don't exist
mkdir -p \
  "${SCRIPT_DIR}/pkg/auth/mock" \
  "${SCRIPT_DIR}/pkg/cache/mock" \
  "${SCRIPT_DIR}/pkg/common/mock" \
  "${SCRIPT_DIR}/pkg/config/mock" \
  "${SCRIPT_DIR}/pkg/db/mock" \
  "${SCRIPT_DIR}/pkg/health/mock" \
  "${SCRIPT_DIR}/pkg/log/mock" \
  "${SCRIPT_DIR}/pkg/metrics/mock" \
  "${SCRIPT_DIR}/pkg/queue/mock" \
  "${SCRIPT_DIR}/pkg/web/mock"

# Use mockery with the config file to generate mocks directly to their target locations
if [[ -f "${SCRIPT_DIR}/.mockery.yml" ]]; then
    mockery --config="${SCRIPT_DIR}/.mockery.yml"
else
    echo "Warning: .mockery.yml not found, skipping mock generation"
fi

# Clean up any temporary directories that mockery might have created
if [[ -d "${SCRIPT_DIR}/mocks" ]]; then
    echo "Cleaning up temporary mock directories..."
    rm -rf "${SCRIPT_DIR}/mocks"
fi

