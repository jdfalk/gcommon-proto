#!/bin/bash
# file: scripts/validate-protos.sh
# version: 1.0.0
# guid: b56b0b7e-9c4c-4d1f-942f-3a77c3c8f6ab

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR/.."

source .github/scripts/ci-status.sh || true

print_status "Running protobuf compilation test"

# Compile all proto files with protoc to verify they compile
proto_failures=()
PROTO_INCLUDE="$(go env GOPATH)/pkg/mod/google.golang.org/protobuf@*/src"
for proto in $(find pkg -name "*.proto" -type f); do
    if ! protoc --proto_path=. --proto_path="$PROTO_INCLUDE" --go_out=/tmp --go-grpc_out=/tmp "$proto" 2> /dev/null; then
        proto_failures+=("$proto")
    fi
done

if [ ${#proto_failures[@]} -ne 0 ]; then
    print_error "Compilation failed for ${#proto_failures[@]} files"
    for file in "${proto_failures[@]}"; do
        echo " - $file"
    done
    exit 1
fi

print_success "All protobuf files compiled successfully"

print_status "Running buf lint"
buf lint

print_success "Protobuf validation complete"
