#!/usr/bin/env python3
"""
Fix buf lint issues by removing unused imports and addressing RPC message reuse.
"""

import re


def remove_unused_import(filepath, import_line):
    """Remove an unused import from a proto file."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        # Find and remove the import line
        import_pattern = re.escape(import_line).replace(r"\"", r'"')
        pattern = rf'^import\s+"{import_pattern}";\s*$'

        new_content = re.sub(pattern, "", content, flags=re.MULTILINE)

        # Also try without the full path match in case of variations
        simple_pattern = rf'^import\s+"{re.escape(import_line)}";\s*$'
        new_content = re.sub(simple_pattern, "", new_content, flags=re.MULTILINE)

        # Write back if changed
        if new_content != content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Removed unused import from {filepath}: {import_line}")
            return True

        return False

    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False


def main():
    """Fix all buf lint issues."""
    print("🔧 Fixing buf lint issues...")

    # List of unused imports to remove (filepath, import_path)
    unused_imports = [
        (
            "pkg/auth/proto/requests/list_user_sessions_request.proto",
            "pkg/common/proto/messages/error.proto",
        ),
        (
            "pkg/auth/proto/requests/logout_request.proto",
            "pkg/common/proto/messages/error.proto",
        ),
        (
            "pkg/auth/proto/requests/terminate_session_request.proto",
            "pkg/common/proto/messages/error.proto",
        ),
        (
            "pkg/auth/proto/responses/create_session_response.proto",
            "pkg/common/proto/messages/request_metadata.proto",
        ),
        (
            "pkg/auth/proto/responses/create_session_response.proto",
            "pkg/common/proto/messages/error.proto",
        ),
        (
            "pkg/auth/proto/responses/logout_response.proto",
            "pkg/common/proto/messages/request_metadata.proto",
        ),
        (
            "pkg/cache/proto/requests/mget_request.proto",
            "pkg/common/proto/messages/error.proto",
        ),
        (
            "pkg/config/proto/messages/config_audit_log.proto",
            "pkg/common/proto/messages/request_metadata.proto",
        ),
        (
            "pkg/config/proto/messages/config_metadata.proto",
            "pkg/common/proto/messages/request_metadata.proto",
        ),
        (
            "pkg/config/proto/messages/config_restore_point.proto",
            "pkg/common/proto/messages/request_metadata.proto",
        ),
        (
            "pkg/config/proto/messages/config_secret.proto",
            "pkg/common/proto/messages/request_metadata.proto",
        ),
        (
            "pkg/config/proto/messages/config_value.proto",
            "pkg/common/proto/messages/request_metadata.proto",
        ),
        (
            "pkg/health/proto/messages/check_result.proto",
            "pkg/common/proto/messages/request_metadata.proto",
        ),
        (
            "pkg/health/proto/requests/configure_alerting_request.proto",
            "pkg/common/proto/messages/error.proto",
        ),
        (
            "pkg/health/proto/requests/disable_check_request.proto",
            "pkg/common/proto/messages/error.proto",
        ),
        (
            "pkg/health/proto/requests/enable_check_request.proto",
            "pkg/common/proto/messages/error.proto",
        ),
        (
            "pkg/health/proto/requests/get_check_status_request.proto",
            "pkg/common/proto/messages/error.proto",
        ),
        (
            "pkg/health/proto/requests/get_health_history_request.proto",
            "pkg/common/proto/messages/error.proto",
        ),
        (
            "pkg/health/proto/requests/get_health_metrics_request.proto",
            "pkg/common/proto/messages/error.proto",
        ),
        (
            "pkg/health/proto/requests/get_health_request.proto",
            "pkg/common/proto/messages/error.proto",
        ),
        (
            "pkg/health/proto/requests/get_service_health_request.proto",
            "pkg/common/proto/messages/error.proto",
        ),
        (
            "pkg/health/proto/requests/health_check_request.proto",
            "pkg/common/proto/messages/error.proto",
        ),
        (
            "pkg/health/proto/requests/list_checks_request.proto",
            "pkg/common/proto/messages/error.proto",
        ),
        (
            "pkg/health/proto/requests/list_services_request.proto",
            "pkg/common/proto/messages/error.proto",
        ),
        (
            "pkg/health/proto/requests/register_check_request.proto",
            "pkg/common/proto/messages/error.proto",
        ),
        (
            "pkg/health/proto/requests/reset_health_stats_request.proto",
            "pkg/common/proto/messages/error.proto",
        ),
        (
            "pkg/health/proto/requests/run_check_request.proto",
            "pkg/common/proto/messages/error.proto",
        ),
        (
            "pkg/health/proto/requests/set_health_request.proto",
            "pkg/common/proto/messages/error.proto",
        ),
        (
            "pkg/health/proto/requests/unregister_check_request.proto",
            "pkg/common/proto/messages/error.proto",
        ),
        (
            "pkg/health/proto/requests/watch_request.proto",
            "pkg/common/proto/messages/error.proto",
        ),
        (
            "pkg/health/proto/responses/configure_alerting_response.proto",
            "pkg/common/proto/messages/request_metadata.proto",
        ),
        (
            "pkg/health/proto/responses/disable_check_response.proto",
            "pkg/common/proto/messages/request_metadata.proto",
        ),
        (
            "pkg/health/proto/responses/enable_check_response.proto",
            "pkg/common/proto/messages/request_metadata.proto",
        ),
        (
            "pkg/health/proto/responses/get_health_metrics_response.proto",
            "pkg/common/proto/messages/error.proto",
        ),
        (
            "pkg/health/proto/responses/get_service_health_response.proto",
            "pkg/common/proto/messages/request_metadata.proto",
        ),
        (
            "pkg/health/proto/responses/health_check_response.proto",
            "pkg/common/proto/messages/request_metadata.proto",
        ),
        (
            "pkg/health/proto/responses/list_services_response.proto",
            "pkg/common/proto/messages/error.proto",
        ),
        (
            "pkg/health/proto/responses/register_check_response.proto",
            "pkg/common/proto/messages/request_metadata.proto",
        ),
        (
            "pkg/health/proto/responses/reset_health_stats_response.proto",
            "pkg/common/proto/messages/request_metadata.proto",
        ),
        (
            "pkg/health/proto/responses/run_check_response.proto",
            "pkg/common/proto/messages/request_metadata.proto",
        ),
        (
            "pkg/health/proto/responses/set_health_response.proto",
            "pkg/common/proto/messages/request_metadata.proto",
        ),
        (
            "pkg/health/proto/responses/unregister_check_response.proto",
            "pkg/common/proto/messages/request_metadata.proto",
        ),
        (
            "pkg/health/proto/responses/watch_response.proto",
            "pkg/common/proto/messages/request_metadata.proto",
        ),
        (
            "pkg/metrics/proto/messages/export_config_options.proto",
            "pkg/metrics/proto/enums/compression_type.proto",
        ),
        (
            "pkg/metrics/proto/messages/export_config_options.proto",
            "pkg/metrics/proto/enums/export_format.proto",
        ),
        (
            "pkg/metrics/proto/messages/metric_aggregation_result.proto",
            "pkg/metrics/proto/enums/aggregation_type.proto",
        ),
        (
            "pkg/metrics/proto/messages/metric_family.proto",
            "pkg/metrics/proto/enums/metric_type.proto",
        ),
        (
            "pkg/metrics/proto/messages/metric_family.proto",
            "pkg/metrics/proto/messages/metric_data.proto",
        ),
        (
            "pkg/metrics/proto/messages/summary_metric.proto",
            "pkg/common/proto/messages/error.proto",
        ),
        (
            "pkg/metrics/proto/requests/record_counter_request.proto",
            "pkg/common/proto/messages/error.proto",
        ),
        (
            "pkg/queue/proto/requests/acknowledge_request.proto",
            "pkg/common/proto/messages/error.proto",
        ),
        (
            "pkg/queue/proto/requests/commit_offset_request.proto",
            "pkg/common/proto/messages/error.proto",
        ),
        (
            "pkg/queue/proto/requests/enqueue_request.proto",
            "pkg/common/proto/messages/error.proto",
        ),
        (
            "pkg/queue/proto/requests/get_queue_stats_request.proto",
            "pkg/common/proto/messages/error.proto",
        ),
        (
            "pkg/queue/proto/requests/list_queues_request.proto",
            "pkg/common/proto/messages/error.proto",
        ),
        (
            "pkg/queue/proto/requests/list_subscriptions_request.proto",
            "pkg/common/proto/messages/error.proto",
        ),
        (
            "pkg/queue/proto/requests/peek_request.proto",
            "pkg/common/proto/messages/error.proto",
        ),
        (
            "pkg/queue/proto/requests/publish_request.proto",
            "pkg/common/proto/messages/error.proto",
        ),
        (
            "pkg/queue/proto/requests/pull_request.proto",
            "pkg/common/proto/messages/error.proto",
        ),
        (
            "pkg/queue/proto/requests/send_message_request.proto",
            "pkg/common/proto/messages/error.proto",
        ),
        (
            "pkg/queue/proto/responses/ack_response.proto",
            "pkg/common/proto/messages/request_metadata.proto",
        ),
        (
            "pkg/queue/proto/responses/get_offset_response.proto",
            "pkg/common/proto/messages/error.proto",
        ),
        (
            "pkg/queue/proto/responses/get_queue_stats_response.proto",
            "pkg/common/proto/messages/request_metadata.proto",
        ),
        (
            "pkg/queue/proto/responses/get_queue_stats_response.proto",
            "pkg/common/proto/messages/error.proto",
        ),
        (
            "pkg/queue/proto/responses/list_queues_response.proto",
            "pkg/common/proto/messages/request_metadata.proto",
        ),
        (
            "pkg/queue/proto/responses/list_queues_response.proto",
            "pkg/common/proto/messages/error.proto",
        ),
        (
            "pkg/queue/proto/responses/list_subscriptions_response.proto",
            "pkg/common/proto/messages/request_metadata.proto",
        ),
        (
            "pkg/queue/proto/responses/list_subscriptions_response.proto",
            "pkg/common/proto/messages/error.proto",
        ),
        (
            "pkg/queue/proto/responses/pull_response.proto",
            "pkg/common/proto/messages/request_metadata.proto",
        ),
        (
            "pkg/queue/proto/responses/pull_response.proto",
            "pkg/common/proto/messages/error.proto",
        ),
        (
            "pkg/queue/proto/responses/send_message_response.proto",
            "pkg/common/proto/messages/request_metadata.proto",
        ),
        (
            "pkg/web/proto/messages/server_event.proto",
            "pkg/common/proto/messages/error.proto",
        ),
        (
            "pkg/web/proto/requests/add_middleware_request.proto",
            "pkg/common/proto/messages/error.proto",
        ),
        (
            "pkg/web/proto/requests/configure_global_request.proto",
            "pkg/common/proto/messages/error.proto",
        ),
        (
            "pkg/web/proto/requests/create_server_request.proto",
            "pkg/common/proto/messages/error.proto",
        ),
        (
            "pkg/web/proto/requests/export_server_config_request.proto",
            "pkg/common/proto/messages/error.proto",
        ),
        (
            "pkg/web/proto/requests/get_access_logs_request.proto",
            "pkg/common/proto/messages/error.proto",
        ),
        (
            "pkg/web/proto/requests/get_route_metrics_request.proto",
            "pkg/common/proto/messages/error.proto",
        ),
        (
            "pkg/web/proto/requests/get_server_health_request.proto",
            "pkg/common/proto/messages/error.proto",
        ),
        (
            "pkg/web/proto/requests/get_server_logs_request.proto",
            "pkg/common/proto/messages/error.proto",
        ),
        (
            "pkg/web/proto/requests/get_server_metrics_request.proto",
            "pkg/common/proto/messages/error.proto",
        ),
        (
            "pkg/web/proto/requests/get_ssl_certificate_info_request.proto",
            "pkg/common/proto/messages/error.proto",
        ),
        (
            "pkg/web/proto/requests/handle_request_request.proto",
            "pkg/common/proto/messages/error.proto",
        ),
        (
            "pkg/web/proto/requests/http_request_per.proto",
            "pkg/common/proto/messages/error.proto",
        ),
        (
            "pkg/web/proto/requests/import_server_config_request.proto",
            "pkg/common/proto/messages/error.proto",
        ),
        (
            "pkg/web/proto/requests/list_servers_request.proto",
            "pkg/common/proto/messages/error.proto",
        ),
        (
            "pkg/web/proto/requests/reload_server_config_request.proto",
            "pkg/common/proto/messages/error.proto",
        ),
        (
            "pkg/web/proto/requests/remove_middleware_request.proto",
            "pkg/common/proto/messages/error.proto",
        ),
        (
            "pkg/web/proto/requests/start_server_request.proto",
            "pkg/common/proto/messages/error.proto",
        ),
        (
            "pkg/web/proto/requests/stream_server_events_request.proto",
            "pkg/common/proto/messages/error.proto",
        ),
        (
            "pkg/web/proto/requests/update_ssl_certificate_request.proto",
            "pkg/common/proto/messages/error.proto",
        ),
        (
            "pkg/web/proto/responses/start_server_response.proto",
            "pkg/common/proto/messages/request_metadata.proto",
        ),
    ]

    fixed_count = 0
    for filepath, import_path in unused_imports:
        if remove_unused_import(filepath, import_path):
            fixed_count += 1

    print(f"\n✅ Fixed {fixed_count} unused import issues")

    # Note about RPC message reuse issues
    print(
        "\n⚠️  Note: There are also RPC message reuse issues that need manual attention:"
    )
    print(
        "  - pkg/cache/proto/services/cache_service.proto: FlushRequest/FlushResponse used multiple times"
    )
    print(
        "  - pkg/web/proto/services/web_admin_service.proto: CacheConfig and FlushRequest/FlushResponse used multiple times"
    )
    print(
        "  These require creating specific request/response types for each RPC method."
    )


if __name__ == "__main__":
    main()
