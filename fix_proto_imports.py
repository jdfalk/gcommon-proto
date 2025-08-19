#!/usr/bin/env python3
# file: fix_proto_imports.py
# version: 1.0.0
# guid: 12345678-1234-1234-1234-123456789abc

"""
Script to systematically fix protobuf import issues by analyzing
error messages and adding missing imports.
"""

import glob
import os
import re

# Error patterns we need to fix
error_patterns = ["unknown request type", "unknown response type", "unknown type"]

# Base directory for proto files
PROTO_BASE = "/Users/jdfalk/repos/github.com/jdfalk/gcommon/proto/gcommon/v1"


def find_proto_files():
    """Find all proto files in the workspace."""
    pattern = f"{PROTO_BASE}/**/*.proto"
    return glob.glob(pattern, recursive=True)


def find_message_file(message_name, module_hint=None):
    """Find the proto file that likely contains a message type."""
    # Convert CamelCase to snake_case for filename search
    snake_name = re.sub(r"([A-Z])", r"_\1", message_name).lower().lstrip("_")

    # Common patterns for request/response files
    possible_patterns = [
        f"**/{snake_name}.proto",
        f"**/messages/{snake_name}.proto",
        f"**/messages/**/{snake_name}.proto",
    ]

    for pattern in possible_patterns:
        full_pattern = f"{PROTO_BASE}/{pattern}"
        matches = glob.glob(full_pattern, recursive=True)
        if matches:
            return matches[0]

    return None


def add_import_to_file(file_path, import_path):
    """Add an import statement to a proto file if not already present."""
    with open(file_path, "r") as f:
        content = f.read()

    import_line = f'import "{import_path}";'

    # Check if import already exists
    if import_line in content:
        return False

    # Find the import section and add the new import
    lines = content.split("\n")
    import_idx = -1

    for i, line in enumerate(lines):
        if line.startswith("import "):
            import_idx = i

    if import_idx >= 0:
        # Insert after the last import
        lines.insert(import_idx + 1, import_line)

        with open(file_path, "w") as f:
            f.write("\n".join(lines))
        return True

    return False


def get_relative_import_path(proto_file_path):
    """Convert absolute proto file path to relative import path."""
    # Remove the base path and return relative path from proto root
    rel_path = os.path.relpath(
        proto_file_path, "/Users/jdfalk/repos/github.com/jdfalk/gcommon/proto"
    )
    return rel_path


# Missing imports we know about from the error messages
missing_imports = {
    "/Users/jdfalk/repos/github.com/jdfalk/gcommon/proto/gcommon/v1/config/services/config_admin_service.proto": [
        "restore_config_request.proto",
        "import_config_request.proto",
        "reload_config_request.proto",
        "rollback_config_request.proto",
        "set_config_schema_request.proto",
        "unwatch_config_request.proto",
    ],
    "/Users/jdfalk/repos/github.com/jdfalk/gcommon/proto/gcommon/v1/config/services/config_service.proto": [
        "delete_config_request.proto",
        "watch_config_request.proto",
        "watch_config_response.proto",
    ],
    "/Users/jdfalk/repos/github.com/jdfalk/gcommon/proto/gcommon/v1/database/services/cache_admin_service.proto": [
        "delete_namespace_request.proto"
    ],
    "/Users/jdfalk/repos/github.com/jdfalk/gcommon/proto/gcommon/v1/database/services/database_admin_service.proto": [
        "drop_database_request.proto",
        "drop_schema_request.proto",
    ],
    "/Users/jdfalk/repos/github.com/jdfalk/gcommon/proto/gcommon/v1/database/services/transaction_service.proto": [
        "commit_transaction_request.proto",
        "rollback_transaction_request.proto",
    ],
    "/Users/jdfalk/repos/github.com/jdfalk/gcommon/proto/gcommon/v1/metrics/services/metrics_service.proto": [
        "metrics_stream_metrics_request.proto",
        "metric_data.proto",
    ],
    "/Users/jdfalk/repos/github.com/jdfalk/gcommon/proto/gcommon/v1/queue/services/queue_monitoring_service.proto": [
        "get_cluster_info_request.proto",
        "queue_stream_metrics_request.proto",
        "metrics_event.proto",
    ],
    "/Users/jdfalk/repos/github.com/jdfalk/gcommon/proto/gcommon/v1/queue/services/queue_service.proto": [
        "queue_subscribe_request.proto",
        "subscribe_response.proto",
    ],
}


def main():
    print("🔧 Fixing protobuf imports...")

    fixed_count = 0

    for service_file, missing_files in missing_imports.items():
        if not os.path.exists(service_file):
            print(f"⚠️  Service file not found: {service_file}")
            continue

        print(f"📝 Processing {os.path.basename(service_file)}...")

        for missing_file in missing_files:
            # Find the actual file
            base_name = missing_file.replace(".proto", "")
            proto_file = find_message_file(base_name)

            if proto_file:
                import_path = get_relative_import_path(proto_file)
                if add_import_to_file(service_file, import_path):
                    print(f"  ✅ Added import: {import_path}")
                    fixed_count += 1
                else:
                    print(f"  ℹ️  Import already exists: {import_path}")
            else:
                print(f"  ❌ Could not find: {missing_file}")

    print(f"\n🎉 Fixed {fixed_count} import issues!")


if __name__ == "__main__":
    main()
