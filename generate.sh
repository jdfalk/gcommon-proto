#!/bin/bash
# file: generate.sh
# Script to generate all protobuf/gRPC code and mocks

set -e

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
cd "${SCRIPT_DIR}"

echo "=== Generating all protobuf/gRPC code and mocks ==="

# ----------------------------------------
# Check Dependencies
# ----------------------------------------
echo ""
echo "=== Checking dependencies ==="

# Check if protoc is installed
if ! command -v protoc &> /dev/null; then
    echo "Error: protoc is not installed or not in PATH."
    echo "Please install Protocol Buffers compiler: https://grpc.io/docs/protoc-installation/"
    exit 1
fi

# Check if required Go plugins are installed
if ! command -v protoc-gen-go &> /dev/null || ! command -v protoc-gen-go-grpc &> /dev/null; then
    echo "Installing required protoc plugins for Go..."
    go install google.golang.org/protobuf/cmd/protoc-gen-go@latest
    go install google.golang.org/grpc/cmd/protoc-gen-go-grpc@latest
fi

# Check if mockery is installed
if ! command -v mockery &> /dev/null; then
    echo "Error: mockery is not installed or not in PATH."
    echo "Please install mockery: go install github.com/vektra/mockery/v2@latest"
    exit 1
fi

# ----------------------------------------
# Protobuf/gRPC Code Generation
# ----------------------------------------
echo ""
echo "=== Generating protobuf/gRPC code ==="

# Find all .proto files and generate Go code
find pkg -name "*.proto" -type f | while read -r proto_file; do
    # Get the directory containing the proto file
    proto_dir=$(dirname "$proto_file")
    proto_name=$(basename "$proto_file")
    pkg_name=$(basename "$(dirname "$proto_dir")")

    echo "=== Generating $pkg_name protobuf and gRPC code ==="

    # Change to the proto directory
    cd "${SCRIPT_DIR}/${proto_dir}"

    # Generate Go code from proto file
    protoc --go_out=. --go_opt=paths=source_relative \
           --go-grpc_out=. --go-grpc_opt=paths=source_relative \
           "$proto_name"

    echo "=== $pkg_name protobuf and gRPC code generation complete ==="

    # Return to script directory
    cd "${SCRIPT_DIR}"
done

# ----------------------------------------
# Mock Generation
# ----------------------------------------
echo ""
echo "=== Generating mocks ==="

# Create all required mock directories if they don't exist
mkdir -p \
  "${SCRIPT_DIR}/pkg/auth/mock" \
  "${SCRIPT_DIR}/pkg/cache/mock" \
  "${SCRIPT_DIR}/pkg/config/mock" \
  "${SCRIPT_DIR}/pkg/db/mock" \
  "${SCRIPT_DIR}/pkg/health/mock" \
  "${SCRIPT_DIR}/pkg/log/mock" \
  "${SCRIPT_DIR}/pkg/metrics/mock" \
  "${SCRIPT_DIR}/pkg/queue/mock" \
  "${SCRIPT_DIR}/pkg/web/mock"

# Use mockery with the config file to generate mocks directly to their target locations
mockery --config="${SCRIPT_DIR}/.mockery.yml"

# Clean up any temporary directories that mockery might have created
if [[ -d "${SCRIPT_DIR}/mocks" ]]; then
    echo "Cleaning up temporary mock directories..."
    rm -rf "${SCRIPT_DIR}/mocks"
fi

echo ""
echo "=== Code generation complete ==="
