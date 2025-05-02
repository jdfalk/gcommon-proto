#!/bin/bash
# file: pkg/metrics/proto/generate.sh
# Script to generate metrics service protobuf and gRPC code

set -e

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
cd "${SCRIPT_DIR}"

echo "=== Generating metrics protobuf and gRPC code ==="

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
  metrics.proto

echo "=== Metrics protobuf and gRPC code generation complete ==="
