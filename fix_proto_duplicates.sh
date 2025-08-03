#!/bin/bash
# file: fix_proto_duplicates.sh
# version: 1.0.0
# guid: 12345678-1234-5678-9abc-123456789abc

set -e

# Get all duplicate proto file basenames
duplicates=(
    "audit_log.proto"
    "auth_config.proto"
    "auth_method.proto"
    "authenticate_request.proto"
    "authenticate_response.proto"
    "authorize_request.proto"
    "authorize_response.proto"
    "batch_operation.proto"
    "cache_config.proto"
    "circuit_breaker_config.proto"
    "compression_config.proto"
    "compression_type.proto"
    "config_value.proto"
    "consistency_level.proto"
    "create_session_request.proto"
    "create_session_response.proto"
    "delete_request.proto"
    "delete_response.proto"
    "delete_session_request.proto"
    "delete_session_response.proto"
    "export_config.proto"
    "get_metrics_request.proto"
    "get_metrics_response.proto"
    "get_session_request.proto"
    "get_session_response.proto"
    "get_stats_response.proto"
    "health_check_request.proto"
    "health_check_response.proto"
    "health_status.proto"
    "http_request.proto"
    "http_response.proto"
    "isolation_level.proto"
    "list_sessions_request.proto"
    "list_sessions_response.proto"
    "list_subscriptions_request.proto"
    "metric_aggregation.proto"
    "performance_stats.proto"
    "publish_request.proto"
    "query_stats.proto"
    "rate_limit_config.proto"
    "retention_policy.proto"
    "retry_policy.proto"
    "session_config.proto"
    "subscribe_request.proto"
    "subscription_info.proto"
    "time_range.proto"
    "timeout_config.proto"
    "timestamp_range.proto"
    "unsubscribe_request.proto"
    "update_session_request.proto"
    "update_session_response.proto"
    "watch_request.proto"
)

echo "Processing duplicate proto files..."

for proto in "${duplicates[@]}"; do
    echo "Processing $proto..."

    # Find all instances of this filename
    files=($(find . -name "$proto" | sort))

    if [ ${#files[@]} -eq 0 ]; then
        echo "  No files found for $proto"
        continue
    fi

    if [ ${#files[@]} -eq 1 ]; then
        echo "  Only one file found: ${files[0]}"
        continue
    fi

    echo "  Found ${#files[@]} files:"
    for file in "${files[@]}"; do
        echo "    $file"
    done

    # Check each file for CONFLICT_DISABLED content
    active_files=()
    disabled_files=()

    for file in "${files[@]}"; do
        if grep -q "CONFLICT_DISABLED" "$file"; then
            disabled_files+=("$file")
            echo "    $file - DISABLED (will be removed)"
        else
            active_files+=("$file")
            echo "    $file - ACTIVE (will be kept)"
        fi
    done

    # Remove disabled files
    for file in "${disabled_files[@]}"; do
        echo "  Removing disabled file: $file"
        rm "$file"
    done

    # If we still have duplicates after removing disabled files, we need manual intervention
    if [ ${#active_files[@]} -gt 1 ]; then
        echo "  WARNING: Multiple active files remain for $proto:"
        for file in "${active_files[@]}"; do
            echo "    $file"
        done
        echo "  Manual resolution required!"
    fi

    echo ""
done

echo "Done processing duplicates!"
echo ""
echo "Remaining duplicates that need manual resolution:"
for proto in "${duplicates[@]}"; do
    files=($(find . -name "$proto" | sort))
    if [ ${#files[@]} -gt 1 ]; then
        echo "$proto:"
        for file in "${files[@]}"; do
            echo "  $file"
        done
    fi
done
