#!/bin/bash
# file: create_remaining_missing_types.sh
# version: 1.0.0
# guid: e5f6a7b8-901c-345d-6789-901234567890

set -e

echo "=== Creating remaining missing types ==="

# From the error log, create all remaining missing types

# Metrics missing types
if [ ! -f "pkg/metrics/proto/export_destination_update.proto" ]; then
cat > pkg/metrics/proto/export_destination_update.proto << 'EOF'
// file: pkg/metrics/proto/export_destination_update.proto
// version: 1.0.0
// guid: f6a7b8c9-012d-456e-7890-012345678901

edition = "2023";

package gcommon.v1.metrics;

option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

message ExportDestinationUpdate {
  // Destination ID
  string destination_id = 1;

  // Destination URL
  string url = 2;

  // Authentication token
  string auth_token = 3;

  // Enabled status
  bool enabled = 4;
}
EOF
fi

if [ ! -f "pkg/metrics/proto/export_format.proto" ]; then
cat > pkg/metrics/proto/export_format.proto << 'EOF'
// file: pkg/metrics/proto/export_format.proto
// version: 1.0.0
// guid: a7b8c9d0-123e-567f-8901-123456789012

edition = "2023";

package gcommon.v1.metrics;

option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

enum ExportFormat {
  EXPORT_FORMAT_UNSPECIFIED = 0;
  EXPORT_FORMAT_PROMETHEUS = 1;
  EXPORT_FORMAT_JSON = 2;
  EXPORT_FORMAT_CSV = 3;
  EXPORT_FORMAT_OPENTELEMETRY = 4;
}
EOF
fi

if [ ! -f "pkg/metrics/proto/alerting_rule.proto" ]; then
cat > pkg/metrics/proto/alerting_rule.proto << 'EOF'
// file: pkg/metrics/proto/alerting_rule.proto
// version: 1.0.0
// guid: b8c9d0e1-234f-678a-9012-234567890123

edition = "2023";

package gcommon.v1.metrics;

option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

message AlertingRule {
  // Rule ID
  string id = 1;

  // Rule name
  string name = 2;

  // Query expression
  string query = 3;

  // Alert condition
  string condition = 4;

  // Threshold value
  double threshold = 5;

  // Rule enabled status
  bool enabled = 6;
}
EOF
fi

if [ ! -f "pkg/metrics/proto/time_range.proto" ]; then
cat > pkg/metrics/proto/time_range.proto << 'EOF'
// file: pkg/metrics/proto/time_range.proto
// version: 1.0.0
// guid: c9d0e1f2-345a-789b-0123-345678901234

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/timestamp.proto";

option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

message TimeRange {
  // Start timestamp
  google.protobuf.Timestamp start = 1;

  // End timestamp
  google.protobuf.Timestamp end = 2;

  // Duration in seconds
  int64 duration_seconds = 3;
}
EOF
fi

if [ ! -f "pkg/metrics/proto/timestamp_range.proto" ]; then
cat > pkg/metrics/proto/timestamp_range.proto << 'EOF'
// file: pkg/metrics/proto/timestamp_range.proto
// version: 1.0.0
// guid: d0e1f2a3-456b-890c-1234-456789012345

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/timestamp.proto";

option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

message TimestampRange {
  // Start timestamp
  google.protobuf.Timestamp start = 1;

  // End timestamp
  google.protobuf.Timestamp end = 2;
}
EOF
fi

if [ ! -f "pkg/metrics/proto/query_stats.proto" ]; then
cat > pkg/metrics/proto/query_stats.proto << 'EOF'
// file: pkg/metrics/proto/query_stats.proto
// version: 1.0.0
// guid: e1f2a3b4-567c-901d-2345-567890123456

edition = "2023";

package gcommon.v1.metrics;

option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

message QueryStats {
  // Total queries executed
  int64 total_queries = 1;

  // Average execution time in milliseconds
  double avg_execution_time_ms = 2;

  // Number of failed queries
  int64 failed_queries = 3;

  // Cache hit rate
  double cache_hit_rate = 4;
}
EOF
fi

if [ ! -f "pkg/metrics/proto/histogram_bucket.proto" ]; then
cat > pkg/metrics/proto/histogram_bucket.proto << 'EOF'
// file: pkg/metrics/proto/histogram_bucket.proto
// version: 1.0.0
// guid: f2a3b4c5-678d-012e-3456-678901234567

edition = "2023";

package gcommon.v1.metrics;

option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

message HistogramBucket {
  // Upper bound for the bucket
  double upper_bound = 1;

  // Count of observations in this bucket
  int64 count = 2;

  // Cumulative count
  int64 cumulative_count = 3;
}
EOF
fi

if [ ! -f "pkg/metrics/proto/export_config.proto" ]; then
cat > pkg/metrics/proto/export_config.proto << 'EOF'
// file: pkg/metrics/proto/export_config.proto
// version: 1.0.0
// guid: a3b4c5d6-789e-123f-4567-789012345678

edition = "2023";

package gcommon.v1.metrics;

option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

message ExportConfig {
  // Export enabled status
  bool enabled = 1;

  // Export interval in seconds
  int32 interval_seconds = 2;

  // Export destinations
  repeated string destinations = 3;

  // Export format
  string format = 4;
}
EOF
fi

if [ ! -f "pkg/metrics/proto/health_status.proto" ]; then
cat > pkg/metrics/proto/health_status.proto << 'EOF'
// file: pkg/metrics/proto/health_status.proto
// version: 1.0.0
// guid: b4c5d6e7-890f-234a-5678-890123456789

edition = "2023";

package gcommon.v1.metrics;

option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

enum HealthStatus {
  HEALTH_STATUS_UNSPECIFIED = 0;
  HEALTH_STATUS_HEALTHY = 1;
  HEALTH_STATUS_DEGRADED = 2;
  HEALTH_STATUS_UNHEALTHY = 3;
  HEALTH_STATUS_UNKNOWN = 4;
}
EOF
fi

if [ ! -f "pkg/metrics/proto/provider_settings_update.proto" ]; then
cat > pkg/metrics/proto/provider_settings_update.proto << 'EOF'
// file: pkg/metrics/proto/provider_settings_update.proto
// version: 1.0.0
// guid: c5d6e7f8-901a-345b-6789-901234567890

edition = "2023";

package gcommon.v1.metrics;

option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

message ProviderSettingsUpdate {
  // Provider type
  string provider_type = 1;

  // Settings map
  map<string, string> settings = 2;

  // Enabled status
  bool enabled = 3;
}
EOF
fi

if [ ! -f "pkg/metrics/proto/resource_limits_update.proto" ]; then
cat > pkg/metrics/proto/resource_limits_update.proto << 'EOF'
// file: pkg/metrics/proto/resource_limits_update.proto
// version: 1.0.0
// guid: d6e7f8a9-012b-456c-7890-012345678901

edition = "2023";

package gcommon.v1.metrics;

option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

message ResourceLimitsUpdate {
  // CPU limit
  double cpu_limit = 1;

  // Memory limit in bytes
  int64 memory_limit_bytes = 2;

  // Disk limit in bytes
  int64 disk_limit_bytes = 3;
}
EOF
fi

if [ ! -f "pkg/metrics/proto/security_config_update.proto" ]; then
cat > pkg/metrics/proto/security_config_update.proto << 'EOF'
// file: pkg/metrics/proto/security_config_update.proto
// version: 1.0.0
// guid: e7f8a9b0-123c-567d-8901-123456789012

edition = "2023";

package gcommon.v1.metrics;

option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

message SecurityConfigUpdate {
  // TLS configuration enabled
  bool tls_enabled = 1;

  // Authentication required
  bool auth_required = 2;

  // API key configuration
  map<string, string> api_keys = 3;
}
EOF
fi

if [ ! -f "pkg/metrics/proto/tag_updates.proto" ]; then
cat > pkg/metrics/proto/tag_updates.proto << 'EOF'
// file: pkg/metrics/proto/tag_updates.proto
// version: 1.0.0
// guid: f8a9b0c1-234d-678e-9012-234567890123

edition = "2023";

package gcommon.v1.metrics;

option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

message TagUpdates {
  // Tags to add
  map<string, string> add_tags = 1;

  // Tags to remove
  repeated string remove_tags = 2;

  // Tags to update
  map<string, string> update_tags = 3;
}
EOF
fi

if [ ! -f "pkg/metrics/proto/provider_status.proto" ]; then
cat > pkg/metrics/proto/provider_status.proto << 'EOF'
// file: pkg/metrics/proto/provider_status.proto
// version: 1.0.0
// guid: a9b0c1d2-345e-789f-0123-345678901234

edition = "2023";

package gcommon.v1.metrics;

option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

message ProviderStatus {
  // Current state
  string state = 1;

  // Status message
  string message = 2;

  // Last updated timestamp
  int64 last_updated = 3;

  // Health status
  bool healthy = 4;
}
EOF
fi

if [ ! -f "pkg/metrics/proto/metric_sample.proto" ]; then
cat > pkg/metrics/proto/metric_sample.proto << 'EOF'
// file: pkg/metrics/proto/metric_sample.proto
// version: 1.0.0
// guid: b0c1d2e3-456f-890a-1234-456789012345

edition = "2023";

package gcommon.v1.metrics;

option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

message MetricSample {
  // Sample value
  double value = 1;

  // Sample timestamp
  int64 timestamp = 2;

  // Sample labels
  map<string, string> labels = 3;
}
EOF
fi

if [ ! -f "pkg/metrics/proto/counter_metric.proto" ]; then
cat > pkg/metrics/proto/counter_metric.proto << 'EOF'
// file: pkg/metrics/proto/counter_metric.proto
// version: 1.0.0
// guid: c1d2e3f4-567a-901b-2345-567890123456

edition = "2023";

package gcommon.v1.metrics;

option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

message CounterMetric {
  // Metric name
  string name = 1;

  // Metric value
  double value = 2;

  // Metric labels
  map<string, string> labels = 3;

  // Timestamp
  int64 timestamp = 4;
}
EOF
fi

if [ ! -f "pkg/metrics/proto/summary_metric.proto" ]; then
cat > pkg/metrics/proto/summary_metric.proto << 'EOF'
// file: pkg/metrics/proto/summary_metric.proto
// version: 1.0.0
// guid: d2e3f4a5-678b-012c-3456-678901234567

edition = "2023";

package gcommon.v1.metrics;

option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

message SummaryMetric {
  // Metric name
  string name = 1;

  // Sample count
  int64 sample_count = 2;

  // Sample sum
  double sample_sum = 3;

  // Quantiles
  repeated Quantile quantiles = 4;

  // Metric labels
  map<string, string> labels = 5;

  // Timestamp
  int64 timestamp = 6;
}

message Quantile {
  // Quantile value (0.0 to 1.0)
  double quantile = 1;

  // Value at this quantile
  double value = 2;
}
EOF
fi

if [ ! -f "pkg/metrics/proto/metric_config.proto" ]; then
cat > pkg/metrics/proto/metric_config.proto << 'EOF'
// file: pkg/metrics/proto/metric_config.proto
// version: 1.0.0
// guid: e3f4a5b6-789c-123d-4567-789012345678

edition = "2023";

package gcommon.v1.metrics;

option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

message MetricConfig {
  // Metric name
  string name = 1;

  // Metric type
  string type = 2;

  // Help text
  string help = 3;

  // Labels
  repeated string label_names = 4;

  // Export configuration
  ExportConfig export_config = 5;
}
EOF
fi

# Queue missing types
if [ ! -f "pkg/queue/proto/consumer_stats.proto" ]; then
cat > pkg/queue/proto/consumer_stats.proto << 'EOF'
// file: pkg/queue/proto/consumer_stats.proto
// version: 1.0.0
// guid: f4a5b6c7-890d-234e-5678-890123456789

edition = "2023";

package gcommon.v1.queue;

option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

message ConsumerStats {
  // Consumer ID
  string consumer_id = 1;

  // Messages processed
  int64 messages_processed = 2;

  // Processing rate per second
  double processing_rate = 3;

  // Error count
  int64 error_count = 4;

  // Last active timestamp
  int64 last_active = 5;
}
EOF
fi

if [ ! -f "pkg/queue/proto/queue_info.proto" ]; then
cat > pkg/queue/proto/queue_info.proto << 'EOF'
// file: pkg/queue/proto/queue_info.proto
// version: 1.0.0
// guid: a5b6c7d8-901e-345f-6789-901234567890

edition = "2023";

package gcommon.v1.queue;

option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

message QueueInfo {
  // Queue name
  string name = 1;

  // Queue type
  string type = 2;

  // Message count
  int64 message_count = 3;

  // Consumer count
  int32 consumer_count = 4;

  // Queue status
  string status = 5;
}
EOF
fi

if [ ! -f "pkg/queue/proto/subscription_info.proto" ]; then
cat > pkg/queue/proto/subscription_info.proto << 'EOF'
// file: pkg/queue/proto/subscription_info.proto
// version: 1.0.0
// guid: b6c7d8e9-012f-456a-7890-012345678901

edition = "2023";

package gcommon.v1.queue;

option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

message SubscriptionInfo {
  // Subscription ID
  string id = 1;

  // Topic name
  string topic = 2;

  // Consumer group
  string consumer_group = 3;

  // Subscription status
  string status = 4;

  // Message backlog
  int64 backlog = 5;
}
EOF
fi

if [ ! -f "pkg/queue/proto/received_message.proto" ]; then
cat > pkg/queue/proto/received_message.proto << 'EOF'
// file: pkg/queue/proto/received_message.proto
// version: 1.0.0
// guid: c7d8e9f0-123a-567b-8901-123456789012

edition = "2023";

package gcommon.v1.queue;

option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

message ReceivedMessage {
  // Message ID
  string id = 1;

  // Message data
  bytes data = 2;

  // Message attributes
  map<string, string> attributes = 3;

  // Receive timestamp
  int64 receive_timestamp = 4;

  // Acknowledgment ID
  string ack_id = 5;
}
EOF
fi

# Web missing types
if [ ! -f "pkg/web/proto/cache_strategy.proto" ]; then
cat > pkg/web/proto/cache_strategy.proto << 'EOF'
// file: pkg/web/proto/cache_strategy.proto
// version: 1.0.0
// guid: d8e9f0a1-234b-678c-9012-234567890123

edition = "2023";

package gcommon.v1.web;

option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

enum CacheStrategy {
  CACHE_STRATEGY_UNSPECIFIED = 0;
  CACHE_STRATEGY_NO_CACHE = 1;
  CACHE_STRATEGY_MEMORY = 2;
  CACHE_STRATEGY_REDIS = 3;
  CACHE_STRATEGY_HYBRID = 4;
}
EOF
fi

if [ ! -f "pkg/web/proto/server_status.proto" ]; then
cat > pkg/web/proto/server_status.proto << 'EOF'
// file: pkg/web/proto/server_status.proto
// version: 1.0.0
// guid: e9f0a1b2-345c-789d-0123-345678901234

edition = "2023";

package gcommon.v1.web;

option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

enum ServerStatus {
  SERVER_STATUS_UNSPECIFIED = 0;
  SERVER_STATUS_STARTING = 1;
  SERVER_STATUS_RUNNING = 2;
  SERVER_STATUS_STOPPING = 3;
  SERVER_STATUS_STOPPED = 4;
  SERVER_STATUS_ERROR = 5;
}
EOF
fi

if [ ! -f "pkg/web/proto/middleware_config.proto" ]; then
cat > pkg/web/proto/middleware_config.proto << 'EOF'
// file: pkg/web/proto/middleware_config.proto
// version: 1.0.0
// guid: f0a1b2c3-456d-890e-1234-456789012345

edition = "2023";

package gcommon.v1.web;

option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

message MiddlewareConfig {
  // Middleware name
  string name = 1;

  // Middleware type
  string type = 2;

  // Configuration parameters
  map<string, string> config = 3;

  // Enabled status
  bool enabled = 4;

  // Priority order
  int32 priority = 5;
}
EOF
fi

echo "✅ Created all remaining missing types"
echo "Now testing buf generate..."

if buf generate > /tmp/buf_test_result.log 2>&1; then
    echo "🎉 SUCCESS! All protobuf compilation issues are now fixed!"
    rm -f /tmp/buf_test_result.log
else
    echo "⚠️  Still some issues remain:"
    head -10 /tmp/buf_test_result.log
fi
