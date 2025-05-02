#!/bin/bash
# file: pkg/auth/proto/generate.sh
# Script to generate auth service protobuf and gRPC code

set -e

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
cd "${SCRIPT_DIR}"

echo "=== Generating auth protobuf and gRPC code ==="

# Check if protoc is installed
if ! command -v protoc &> /dev/null; then
    echo "Error: protoc is not installed" >&2
    exit 1
fi

# Generate the protobuf and gRPC code
protoc \
  -I . \
  --go_out=paths=source_relative:. \
  --go-grpc_out=paths=source_relative:. \
  auth.proto

echo "=== Auth protobuf and gRPC code generation complete ==="
