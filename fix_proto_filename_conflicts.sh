#!/bin/bash
# file: fix_proto_filename_conflicts.sh
# version: 1.0.0
# guid: 87654321-4321-8765-cba9-876543210fed

set -e

echo "Fixing proto filename conflicts by adding module prefixes..."

# Function to rename proto files and update imports
rename_proto_file() {
    local file="$1"
    local new_name="$2"
    local dir=$(dirname "$file")
    local new_file="$dir/$new_name"

    if [ "$file" != "$new_file" ] && [ -f "$file" ]; then
        echo "  Renaming: $file -> $new_file"
        mv "$file" "$new_file"

        # Update the file header
        sed -i '' "s|^// file: .*|// file: ${new_file#./}|" "$new_file"

        # Update any imports that reference this file
        local old_import_path="${file#./}"
        local new_import_path="${new_file#./}"

        echo "  Updating imports from $old_import_path to $new_import_path"
        find . -name "*.proto" -exec grep -l "import \"$old_import_path\"" {} \; | while read proto_file; do
            echo "    Updating import in: $proto_file"
            sed -i '' "s|import \"$old_import_path\"|import \"$new_import_path\"|g" "$proto_file"
        done
    fi
}

# Auth vs Web conflicts - prefix web files with "web_"
echo "Processing auth vs web conflicts..."
rename_proto_file "./pkg/web/proto/messages/auth_config.proto" "web_auth_config.proto"
rename_proto_file "./pkg/web/proto/enums/auth_method.proto" "web_auth_method.proto"
rename_proto_file "./pkg/web/proto/requests/authenticate_request.proto" "web_authenticate_request.proto"
rename_proto_file "./pkg/web/proto/responses/authenticate_response.proto" "web_authenticate_response.proto"
rename_proto_file "./pkg/web/proto/requests/authorize_request.proto" "web_authorize_request.proto"
rename_proto_file "./pkg/web/proto/responses/authorize_response.proto" "web_authorize_response.proto"
rename_proto_file "./pkg/web/proto/requests/create_session_request.proto" "web_create_session_request.proto"
rename_proto_file "./pkg/web/proto/responses/create_session_response.proto" "web_create_session_response.proto"
rename_proto_file "./pkg/web/proto/requests/delete_session_request.proto" "web_delete_session_request.proto"
rename_proto_file "./pkg/web/proto/responses/delete_session_response.proto" "web_delete_session_response.proto"
rename_proto_file "./pkg/web/proto/requests/get_session_request.proto" "web_get_session_request.proto"
rename_proto_file "./pkg/web/proto/responses/get_session_response.proto" "web_get_session_response.proto"
rename_proto_file "./pkg/web/proto/requests/list_sessions_request.proto" "web_list_sessions_request.proto"
rename_proto_file "./pkg/web/proto/responses/list_sessions_response.proto" "web_list_sessions_response.proto"
rename_proto_file "./pkg/web/proto/requests/update_session_request.proto" "web_update_session_request.proto"
rename_proto_file "./pkg/web/proto/responses/update_session_response.proto" "web_update_session_response.proto"
rename_proto_file "./pkg/web/proto/messages/session_config.proto" "web_session_config.proto"

# Cache vs Queue conflicts - prefix queue files with "queue_"
echo "Processing cache vs queue conflicts..."
rename_proto_file "./pkg/queue/proto/requests/delete_request.proto" "queue_delete_request.proto"
rename_proto_file "./pkg/queue/proto/responses/delete_response.proto" "queue_delete_response.proto"
rename_proto_file "./pkg/queue/proto/requests/list_subscriptions_request.proto" "queue_list_subscriptions_request.proto"
rename_proto_file "./pkg/queue/proto/requests/publish_request.proto" "queue_publish_request.proto"
rename_proto_file "./pkg/queue/proto/requests/subscribe_request.proto" "queue_subscribe_request.proto"
rename_proto_file "./pkg/queue/proto/requests/unsubscribe_request.proto" "queue_unsubscribe_request.proto"

# Common vs specific package conflicts - prefix specific package files
echo "Processing common vs specific package conflicts..."
rename_proto_file "./pkg/db/proto/messages/batch_operation.proto" "db_batch_operation.proto"
rename_proto_file "./pkg/config/proto/messages/config_value.proto" "config_config_value.proto"
rename_proto_file "./pkg/queue/proto/messages/circuit_breaker_config.proto" "queue_circuit_breaker_config.proto"
rename_proto_file "./pkg/queue/proto/messages/retry_policy.proto" "queue_retry_policy.proto"
rename_proto_file "./pkg/queue/proto/messages/subscription_info.proto" "queue_subscription_info.proto"

# Multi-package conflicts - use package prefixes
echo "Processing multi-package conflicts..."

# Compression type - keep log version as base, prefix others
rename_proto_file "./pkg/metrics/proto/enums/compression_type.proto" "metrics_compression_type.proto"
rename_proto_file "./pkg/queue/proto/enums/compression_type.proto" "queue_compression_type.proto"
rename_proto_file "./pkg/web/proto/enums/compression_type.proto" "web_compression_type.proto"

# Health status - keep common version as base, prefix others
rename_proto_file "./pkg/metrics/proto/enums/health_status.proto" "metrics_health_status.proto"
rename_proto_file "./pkg/queue/proto/enums/health_status.proto" "queue_health_status.proto"
rename_proto_file "./pkg/web/proto/enums/health_status.proto" "web_health_status.proto"

# Health check files - keep health package as base, prefix others
rename_proto_file "./pkg/auth/proto/requests/health_check_request.proto" "auth_health_check_request.proto"
rename_proto_file "./pkg/cache/proto/requests/health_check_request.proto" "cache_health_check_request.proto"
rename_proto_file "./pkg/config/proto/requests/health_check_request.proto" "config_health_check_request.proto"
rename_proto_file "./pkg/db/proto/requests/health_check_request.proto" "db_health_check_request.proto"
rename_proto_file "./pkg/metrics/proto/requests/health_check_request.proto" "metrics_health_check_request.proto"
rename_proto_file "./pkg/queue/proto/requests/health_check_request.proto" "queue_health_check_request.proto"
rename_proto_file "./pkg/web/proto/requests/health_check_request.proto" "web_health_check_request.proto"

rename_proto_file "./pkg/auth/proto/responses/health_check_response.proto" "auth_health_check_response.proto"
rename_proto_file "./pkg/config/proto/responses/health_check_response.proto" "config_health_check_response.proto"
rename_proto_file "./pkg/db/proto/responses/health_check_response.proto" "db_health_check_response.proto"
rename_proto_file "./pkg/metrics/proto/responses/health_check_response.proto" "metrics_health_check_response.proto"
rename_proto_file "./pkg/queue/proto/responses/health_check_response.proto" "queue_health_check_response.proto"
rename_proto_file "./pkg/web/proto/responses/health_check_response.proto" "web_health_check_response.proto"

# Metrics vs web conflicts
rename_proto_file "./pkg/web/proto/requests/get_metrics_request.proto" "web_get_metrics_request.proto"
rename_proto_file "./pkg/web/proto/responses/get_metrics_response.proto" "web_get_metrics_response.proto"
rename_proto_file "./pkg/web/proto/messages/performance_stats.proto" "web_performance_stats.proto"

# Stats conflicts
rename_proto_file "./pkg/metrics/proto/responses/get_stats_response.proto" "metrics_get_stats_response.proto"

# Misc conflicts
rename_proto_file "./pkg/web/proto/messages/cache_config.proto" "web_cache_config.proto"
rename_proto_file "./pkg/web/proto/messages/compression_config.proto" "web_compression_config.proto"
rename_proto_file "./pkg/queue/proto/enums/consistency_level.proto" "queue_consistency_level.proto"
rename_proto_file "./pkg/organization/proto/enums/isolation_level.proto" "org_isolation_level.proto"
rename_proto_file "./pkg/metrics/proto/types/time_range.proto" "metrics_time_range.proto"
rename_proto_file "./pkg/web/proto/messages/timeout_config.proto" "web_timeout_config.proto"
rename_proto_file "./pkg/queue/proto/types/timestamp_range.proto" "queue_timestamp_range.proto"
rename_proto_file "./pkg/health/proto/requests/watch_request.proto" "health_watch_request.proto"

# HTTP conflicts within web package
rename_proto_file "./pkg/web/proto/requests/http_request.proto" "web_http_request_type.proto"
rename_proto_file "./pkg/web/proto/responses/http_response.proto" "web_http_response_type.proto"

# Rate limit conflicts
rename_proto_file "./pkg/queue/proto/messages/rate_limit_config.proto" "queue_rate_limit_config.proto"
rename_proto_file "./pkg/web/proto/messages/rate_limit_config.proto" "web_rate_limit_config.proto"

# Retention policy conflicts within metrics
rename_proto_file "./pkg/metrics/proto/messages/retention_policy.proto" "metrics_retention_policy_config.proto"
rename_proto_file "./pkg/metrics/proto/types/retention_policy.proto" "metrics_retention_policy_type.proto"
rename_proto_file "./pkg/queue/proto/messages/retention_policy.proto" "queue_retention_policy.proto"

# Query stats conflicts
rename_proto_file "./pkg/metrics/proto/types/query_stats.proto" "metrics_query_stats.proto"

# Common audit log - keep common version, prefix auth version
rename_proto_file "./pkg/auth/proto/messages/audit_log.proto" "auth_audit_log.proto"

echo "Done! All filename conflicts should now be resolved."
echo "You may need to manually check and update any remaining import statements."
