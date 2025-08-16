#!/bin/bash
# file: analyze_proto_files.sh
# version: 1.0.0
# guid: a0b1c2d3-4e5f-6a7b-8c9d-0e1f2a3b4c5d

echo "Analyzing remaining proto files that need splitting..."
echo "================================================================"

# Files that contain both enums and messages
files_to_check=(
    "./pkg/config/proto/config_audit_log.proto"
    "./pkg/config/proto/config_metadata.proto"
    "./pkg/config/proto/config_restore_point.proto"
    "./pkg/config/proto/config_secret.proto"
    "./pkg/config/proto/config_template.proto"
    "./pkg/config/proto/config_value.proto"
    "./pkg/config/proto/config_version.proto"
    "./pkg/metrics/proto/delete_provider_request.proto"
    "./pkg/metrics/proto/record_metrics_request.proto"
    "./pkg/metrics/proto/update_provider_request.proto"
    "./pkg/metrics/proto/update_provider_response.proto"
    "./pkg/queue/proto/cluster_info.proto"
    "./pkg/queue/proto/get_queue_stats_request.proto"
    "./pkg/queue/proto/load_balancing_config.proto"
    "./pkg/queue/proto/replication_config.proto"
    "./pkg/queue/proto/routing_config.proto"
    "./pkg/queue/proto/schema_config.proto"
    "./pkg/queue/proto/serialization_config.proto"
)

for file in "${files_to_check[@]}"; do
    if [[ -f "$file" ]]; then
        echo ""
        echo "File: $file"
        echo "  Enums:"
        grep -n "^enum " "$file" | sed 's/^/    /'
        echo "  Messages:"
        grep -n "^message " "$file" | sed 's/^/    /'

        enum_count=$(grep -c "^enum " "$file")
        message_count=$(grep -c "^message " "$file")
        total_count=$((enum_count + message_count))

        echo "  Summary: $enum_count enums, $message_count messages, $total_count total definitions"

        if [[ $total_count -gt 1 ]]; then
            echo "  Status: NEEDS SPLITTING"
        else
            echo "  Status: OK (follows 1-1-1 pattern)"
        fi
    else
        echo "File not found: $file"
    fi
done

echo ""
echo "================================================================"
echo "Summary: Files that need splitting are marked as 'NEEDS SPLITTING'"
