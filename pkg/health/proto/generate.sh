#!/bin/bash
# Script to generate Go code from Protocol Buffer definitions

set -e

# Path to the protobuf file
PROTO_FILE="health.proto"

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

echo "Generating Go code from Protocol Buffers..."
protoc --go_out=. --go_opt=paths=source_relative \
       --go-grpc_out=. --go-grpc_opt=paths=source_relative \
       "${PROTO_FILE}"

echo "Done."
