#!/bin/bash
# file: pkg/auth/mock/generate.sh
# Script to generate mocks for auth interfaces

set -e

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
ROOT_DIR="$(cd "${SCRIPT_DIR}/../../../" && pwd)"

# Check if SILENT flag is set to true, if not echo output
if [[ "${SILENT}" != "true" ]]; then
    echo "=== Generating auth mocks ==="
fi

# Run mockery using only the configuration file
mockery --config="${ROOT_DIR}/mockery.yaml"

if [[ "${SILENT}" != "true" ]]; then
    echo "=== Auth mock generation complete ==="
fi
