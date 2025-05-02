#!/bin/bash
# file: pkg/log/mock/generate.sh
# Script to generate mocks for logging interfaces

set -e

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
ROOT_DIR="$(cd "${SCRIPT_DIR}/../../../" && pwd)"

# Check if SILENT flag is set to true, if not echo output
if [[ "${SILENT}" != "true" ]]; then
    echo "=== Generating log mocks ==="
fi

# Run mockery using only the configuration file
mockery --config="${ROOT_DIR}/mockery.yaml"

if [[ "${SILENT}" != "true" ]]; then
    echo "=== Log mock generation complete ==="
fi
