#!/bin/bash
# file: add_missing_imports.sh
# version: 1.0.0
# guid: a1b2c3d4-5678-901e-f234-567890123456

set -e

echo "=== Adding missing imports to proto files ==="

# Function to add import if not present
add_import_if_missing() {
    local file="$1"
    local import_line="$2"

    if [ -f "$file" ] && ! grep -q "$import_line" "$file"; then
        # Find the line after the package declaration
        local package_line=$(grep -n "^package " "$file" | head -1 | cut -d: -f1)
        if [ -n "$package_line" ]; then
            # Insert import after package line
            sed -i "" "${package_line}a\\
$import_line\\
" "$file"
            echo "Added import to $file: $import_line"
        fi
    fi
}

# Add imports for config module
add_import_if_missing "pkg/config/proto/access_control.proto" 'import "pkg/config/proto/access_restriction.proto";'
add_import_if_missing "pkg/config/proto/access_control.proto" 'import "pkg/config/proto/rate_limits.proto";'

add_import_if_missing "pkg/config/proto/compliance_settings.proto" 'import "pkg/config/proto/compliance_audit.proto";'
add_import_if_missing "pkg/config/proto/compliance_settings.proto" 'import "pkg/config/proto/compliance_reporting.proto";'

add_import_if_missing "pkg/config/proto/get_config_history_response.proto" 'import "pkg/config/proto/config_change.proto";'

add_import_if_missing "pkg/config/proto/get_config_stats_response.proto" 'import "pkg/config/proto/config_stats.proto";'

add_import_if_missing "pkg/config/proto/monitoring_settings.proto" 'import "pkg/config/proto/monitoring_alert.proto";'

add_import_if_missing "pkg/config/proto/rotation_settings.proto" 'import "pkg/config/proto/rotation_event.proto";'

add_import_if_missing "pkg/config/proto/template_parameter.proto" 'import "pkg/config/proto/parameter_constraints.proto";'

add_import_if_missing "pkg/config/proto/usage_statistics.proto" 'import "pkg/config/proto/usage_trend.proto";'

add_import_if_missing "pkg/config/proto/validation_rule.proto" 'import "pkg/config/proto/validation_severity.proto";'

# Add imports for metrics module
add_import_if_missing "pkg/metrics/proto/alert_notification.proto" 'import "pkg/metrics/proto/alert_severity.proto";'

add_import_if_missing "pkg/metrics/proto/alerting_condition.proto" 'import "pkg/metrics/proto/comparison_operator.proto";'

add_import_if_missing "pkg/metrics/proto/export_config_update.proto" 'import "pkg/metrics/proto/export_destination_update.proto";'

add_import_if_missing "pkg/metrics/proto/export_metrics_request.proto" 'import "pkg/metrics/proto/export_format.proto";'

add_import_if_missing "pkg/metrics/proto/get_alerting_rules_response.proto" 'import "pkg/metrics/proto/alerting_rule.proto";'

add_import_if_missing "pkg/metrics/proto/get_provider_stats_request.proto" 'import "pkg/metrics/proto/time_range.proto";'

add_import_if_missing "pkg/metrics/proto/get_stats_request.proto" 'import "pkg/metrics/proto/timestamp_range.proto";'

add_import_if_missing "pkg/metrics/proto/get_stats_response.proto" 'import "pkg/metrics/proto/query_stats.proto";'

add_import_if_missing "pkg/metrics/proto/histogram_metric.proto" 'import "pkg/metrics/proto/histogram_bucket.proto";'

add_import_if_missing "pkg/metrics/proto/metric_config.proto" 'import "pkg/metrics/proto/export_config.proto";'

add_import_if_missing "pkg/metrics/proto/metric_health.proto" 'import "pkg/metrics/proto/health_status.proto";'

add_import_if_missing "pkg/metrics/proto/provider_config_update.proto" 'import "pkg/metrics/proto/provider_settings_update.proto";'
add_import_if_missing "pkg/metrics/proto/provider_config_update.proto" 'import "pkg/metrics/proto/export_config_update.proto";'
add_import_if_missing "pkg/metrics/proto/provider_config_update.proto" 'import "pkg/metrics/proto/resource_limits_update.proto";'
add_import_if_missing "pkg/metrics/proto/provider_config_update.proto" 'import "pkg/metrics/proto/security_config_update.proto";'
add_import_if_missing "pkg/metrics/proto/provider_config_update.proto" 'import "pkg/metrics/proto/tag_updates.proto";'

add_import_if_missing "pkg/metrics/proto/provider_info.proto" 'import "pkg/metrics/proto/provider_status.proto";'

add_import_if_missing "pkg/metrics/proto/provider_summary.proto" 'import "pkg/metrics/proto/provider_status.proto";'

add_import_if_missing "pkg/metrics/proto/record_counter_response.proto" 'import "pkg/metrics/proto/counter_metric.proto";'

add_import_if_missing "pkg/metrics/proto/record_summary_request.proto" 'import "pkg/metrics/proto/summary_metric.proto";'

add_import_if_missing "pkg/metrics/proto/set_alerting_rules_request.proto" 'import "pkg/metrics/proto/alerting_rule.proto";'

add_import_if_missing "pkg/metrics/proto/set_metric_config_request.proto" 'import "pkg/metrics/proto/metric_config.proto";'

add_import_if_missing "pkg/metrics/proto/time_series.proto" 'import "pkg/metrics/proto/metric_sample.proto";'

# Add imports for notification module
add_import_if_missing "pkg/notification/proto/get_preferences_response.proto" 'import "pkg/notification/proto/subscription_preferences.proto";'

add_import_if_missing "pkg/notification/proto/send_notification_request.proto" 'import "pkg/notification/proto/notification_message.proto";'

add_import_if_missing "pkg/notification/proto/update_preferences_request.proto" 'import "pkg/notification/proto/subscription_preferences.proto";'

# Add imports for organization module
add_import_if_missing "pkg/organization/proto/organization_member.proto" 'import "pkg/organization/proto/member_role.proto";'

# Add imports for queue module
add_import_if_missing "pkg/queue/proto/get_queue_stats_response.proto" 'import "pkg/queue/proto/consumer_stats.proto";'

add_import_if_missing "pkg/queue/proto/list_queues_response.proto" 'import "pkg/queue/proto/queue_info.proto";'

add_import_if_missing "pkg/queue/proto/list_subscriptions_response.proto" 'import "pkg/queue/proto/subscription_info.proto";'

add_import_if_missing "pkg/queue/proto/pull_response.proto" 'import "pkg/queue/proto/received_message.proto";'

# Add imports for web module
add_import_if_missing "pkg/web/proto/cache_config.proto" 'import "pkg/web/proto/cache_strategy.proto";'

add_import_if_missing "pkg/web/proto/start_server_response.proto" 'import "pkg/web/proto/server_status.proto";'

add_import_if_missing "pkg/web/proto/update_middleware_config_request.proto" 'import "pkg/web/proto/middleware_config.proto";'

echo "✅ All imports added"
echo "Testing buf generate..."

if buf generate > /tmp/buf_final_test.log 2>&1; then
    echo "🎉 SUCCESS! All protobuf compilation issues are now COMPLETELY fixed!"
    rm -f /tmp/buf_final_test.log
else
    echo "⚠️  Still some issues remain:"
    head -20 /tmp/buf_final_test.log
fi
