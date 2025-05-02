#!/bin/bash
# file: pkg/cache/proto/generate.sh
# Script to generate cache service protobuf and gRPC code

set -e

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
cd "${SCRIPT_DIR}"

echo "=== Generating cache protobuf and gRPC code ==="

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
  cache.proto

echo "=== Cache protobuf and gRPC code generation complete ==="
