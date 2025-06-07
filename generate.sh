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

# Generate common proto first (since other protos may import it)
if [[ -f "pkg/common/proto/common.proto" ]]; then
    echo "=== Generating monolithic common protobuf code ==="
    protoc --proto_path=. --go_out=. --go_opt=paths=source_relative \
           --go-grpc_out=. --go-grpc_opt=paths=source_relative \
           pkg/common/proto/common.proto
    echo "=== Monolithic common protobuf code generation complete ==="
fi

# Check migration status and generate protobuf code accordingly
echo "=== Analyzing protobuf migration status ==="

# Function to check if a module has sufficient 1-1-1 migration
check_migration_status() {
    local module=$1
    local monolithic_file="pkg/${module}/proto/${module}.proto"
    local onetoone_count=0
    
    # Special case for database module (monolithic file is database.proto not db.proto)
    if [[ "$module" == "db" ]]; then
        monolithic_file="pkg/db/proto/database.proto"
    fi
    
    # Count 1-1-1 structure files (excluding monolithic file)
    if [[ -d "pkg/${module}/proto" ]]; then
        onetoone_count=$(find "pkg/${module}/proto" -name "*.proto" ! -name "$(basename "$monolithic_file")" 2>/dev/null | wc -l | tr -d ' ')
    fi
    
    # Migration thresholds: use 1-1-1 if we have >5 files OR >50% migration
    if [[ $onetoone_count -gt 5 ]]; then
        echo "1-1-1"
    elif [[ -f "$monolithic_file" ]]; then
        echo "monolithic"
    else
        echo "none"
    fi
}

# Generate protobuf code based on migration status
modules=("auth" "cache" "config" "db" "health" "log" "metrics" "queue" "web")

for module in "${modules[@]}"; do
    status=$(check_migration_status "$module")
    
    case $status in
        "1-1-1")
            echo "=== Generating $module module (1-1-1 structure) ==="
            find "pkg/${module}/proto" -name "*.proto" -type f | while read -r proto_file; do
                proto_name=$(basename "$proto_file")
                echo "=== Generating $module/$proto_name ==="
                protoc --proto_path=. --go_out=. --go_opt=paths=source_relative \
                       --go-grpc_out=. --go-grpc_opt=paths=source_relative \
                       "$proto_file"
            done
            echo "=== $module module (1-1-1) generation complete ==="
            ;;
        "monolithic")
            echo "=== Generating $module module (monolithic structure) ==="
            if [[ "$module" == "db" ]]; then
                monolithic_file="pkg/db/proto/database.proto"
            else
                monolithic_file="pkg/${module}/proto/${module}.proto"
            fi
            
            if [[ -f "$monolithic_file" ]]; then
                protoc --proto_path=. --go_out=. --go_opt=paths=source_relative \
                       --go-grpc_out=. --go-grpc_opt=paths=source_relative \
                       "$monolithic_file"
                echo "=== $module module (monolithic) generation complete ==="
            fi
            ;;
        "none")
            echo "=== Skipping $module module (no proto files found) ==="
            ;;
    esac
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
  "${SCRIPT_DIR}/pkg/common/mock" \
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
