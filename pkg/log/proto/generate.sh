#!/bin/bash
# file: pkg/log/proto/generate.sh
# Script to generate log service protobuf and gRPC code

set -e

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
cd "${SCRIPT_DIR}"

echo "=== Generating log protobuf and gRPC code ==="

# Check if protoc is installed
if ! command -v protoc &> /dev/null; then
    echo "Error: protoc is not installed" >&2
    exit 1
fi

# Generate the protobuf and gRPC code
protoc \
  -I . \
  -I "$(go list -m -f '{{.Dir}}' google.golang.org/protobuf)/types/known" \
  --go_out=paths=source_relative:. \
  --go-grpc_out=paths=source_relative:. \
  log.proto

echo "=== Log protobuf and gRPC code generation complete ==="
