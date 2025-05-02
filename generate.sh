#!/bin/bash
# file: generate.sh
# Script to generate all mocks and protobuf/gRPC code

set -e

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
cd "${SCRIPT_DIR}"

echo "=== Generating all mocks and protobuf/gRPC code ==="

# Generate all protobuf/gRPC code first
echo ""
echo "=== Generating protobuf/gRPC code ==="

# Function to run a generate script in its own directory
run_generate_script() {
    local script_path="$1"
    local script_dir=$(dirname "$script_path")
    local script_name=$(basename "$script_path")
    local pkg_name=$(basename "$script_dir")

    # Save current directory
    local original_dir=$(pwd)

    # Change to the script's directory
    cd "$script_dir"

    # Run the script but suppress its output
    if [[ -x "./$script_name" ]]; then
        # Only show main script output
        echo "=== Generating $pkg_name protobuf and gRPC code ==="
        # Run the script but don't print its echo statements
        SILENT=true ./"$script_name" > /dev/null
        echo "=== $pkg_name protobuf and gRPC code generation complete ==="
    else
        echo "Warning: $script_name is not executable"
        chmod +x "./$script_name"
        echo "=== Generating $pkg_name protobuf and gRPC code ==="
        SILENT=true ./"$script_name" > /dev/null
        echo "=== $pkg_name protobuf and gRPC code generation complete ==="
    fi

    # Return to original directory
    cd "$original_dir"
}

# Run all protobuf generation scripts from their respective directories
run_generate_script "${SCRIPT_DIR}/pkg/auth/proto/generate.sh"
run_generate_script "${SCRIPT_DIR}/pkg/cache/proto/generate.sh"
run_generate_script "${SCRIPT_DIR}/pkg/config/proto/generate.sh"
run_generate_script "${SCRIPT_DIR}/pkg/db/proto/generate.sh"
run_generate_script "${SCRIPT_DIR}/pkg/health/proto/generate.sh"
run_generate_script "${SCRIPT_DIR}/pkg/log/proto/generate.sh"
run_generate_script "${SCRIPT_DIR}/pkg/metrics/proto/generate.sh"
run_generate_script "${SCRIPT_DIR}/pkg/queue/proto/generate.sh"
run_generate_script "${SCRIPT_DIR}/pkg/web/proto/generate.sh"

echo ""
echo "=== Generating mocks ==="

# Generate mocks using the mockery.yaml config
mockery --config="${SCRIPT_DIR}/mockery.yaml"

# Function to run a mock generate script in its own directory
run_mock_script() {
    local script_path="$1"
    local script_dir=$(dirname "$script_path")
    local pkg_name=$(basename "$(dirname "$script_dir")")

    # Only run if the script exists and is executable
    if [[ -f "$script_path" && -x "$script_path" ]]; then
        # Save current directory
        local original_dir=$(pwd)

        # Change to the script's directory
        cd "$script_dir"

        echo "=== Generating $pkg_name mocks ==="
        SILENT=true ./$(basename "$script_path") > /dev/null
        echo "=== $pkg_name mocks generation complete ==="

        # Return to original directory
        cd "$original_dir"
    fi
}

# Run all mock generation scripts
run_mock_script "${SCRIPT_DIR}/pkg/auth/mock/generate.sh"
run_mock_script "${SCRIPT_DIR}/pkg/cache/mock/generate.sh"
run_mock_script "${SCRIPT_DIR}/pkg/config/mock/generate.sh"
run_mock_script "${SCRIPT_DIR}/pkg/db/mock/generate.sh"
run_mock_script "${SCRIPT_DIR}/pkg/health/mock/generate.sh"
run_mock_script "${SCRIPT_DIR}/pkg/log/mock/generate.sh"
run_mock_script "${SCRIPT_DIR}/pkg/metrics/mock/generate.sh"
run_mock_script "${SCRIPT_DIR}/pkg/web/mock/generate.sh"

echo ""
echo "=== Code generation complete ==="
