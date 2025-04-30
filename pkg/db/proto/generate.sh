#!/bin/bash
# file: pkg/db/proto/generate.sh

set -e

# Directory where this script is located
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# Change to the directory where this script is located
cd "${DIR}"

# Run protoc to generate Go code from proto files
protoc --go_out=. --go_opt=paths=source_relative \
    --go-grpc_out=. --go-grpc_opt=paths=source_relative \
    database.proto

echo "Database protocol buffer code generation completed successfully"
