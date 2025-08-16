#!/bin/bash
# file: scripts/generate-microservice.sh
# version: 1.0.0
# guid: 5ba61827-676a-4e67-a489-09f585cd3c44

set -euo pipefail

# generate-microservice.sh
#
# Scaffold a new microservice project from predefined templates.
#
# Usage:
#   ./scripts/generate-microservice.sh TEMPLATE TARGET_DIR
#
# Arguments:
#   TEMPLATE    Name of the template to use (e.g., basic-api-service)
#   TARGET_DIR  Directory where the new service should be created

usage() {
    echo "Usage: $0 TEMPLATE TARGET_DIR" >&2
    echo "Available templates:" >&2
    ls templates >&2
}

if [[ $# -ne 2 ]]; then
    usage
    exit 1
fi

template="$1"
target="$2"
source_dir="templates/$template"

if [[ ! -d "$source_dir" ]]; then
    echo "unknown template: $template" >&2
    exit 1
fi

mkdir -p "$target"
cp -a "$source_dir/". "$target/"

echo "Created $target from $template template"
