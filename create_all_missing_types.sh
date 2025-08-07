#!/bin/bash
# file: create_all_missing_types.sh
# version: 1.0.0
# guid: f2a3b4c5-6789-023e-7890-345678901234

set -e

echo "Creating ALL remaining missing types..."

# Metrics missing types
echo "=== Creating Metrics Module Missing Types ==="

# ExportDestinationUpdate
cat > pkg/metrics/proto/export_destination_update.proto << 'EOF'
// file: pkg/metrics/proto/export_destination_update.proto
// version: 1.0.0
// guid: a3b4c5d6-789a-134f-8901-456789012345

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

# ExportFormat
cat > pkg/metrics/proto/export_format.proto << 'EOF'
// file: pkg/metrics/proto/export_format.proto
// version: 1.0.0
// guid: b4c5d6e7-890b-245a-9012-567890123456

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

# AlertingRule
cat > pkg/metrics/proto/alerting_rule.proto << 'EOF'
// file: pkg/metrics/proto/alerting_rule.proto
// version: 1.0.0
// guid: c5d6e7f8-901c-356b-0123-678901234567

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

# TimeRange
cat > pkg/metrics/proto/time_range.proto << 'EOF'
// file: pkg/metrics/proto/time_range.proto
// version: 1.0.0
// guid: d6e7f8a9-012d-467c-1234-789012345678

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

# TimestampRange
cat > pkg/metrics/proto/timestamp_range.proto << 'EOF'
// file: pkg/metrics/proto/timestamp_range.proto
// version: 1.0.0
// guid: e7f8a9b0-123e-578d-2345-890123456789

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

# QueryStats
cat > pkg/metrics/proto/query_stats.proto << 'EOF'
// file: pkg/metrics/proto/query_stats.proto
// version: 1.0.0
// guid: f8a9b0c1-234f-689e-3456-901234567890

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

# HistogramBucket
cat > pkg/metrics/proto/histogram_bucket.proto << 'EOF'
// file: pkg/metrics/proto/histogram_bucket.proto
// version: 1.0.0
// guid: a9b0c1d2-345a-790f-4567-012345678901

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

# ExportConfig
cat > pkg/metrics/proto/export_config.proto << 'EOF'
// file: pkg/metrics/proto/export_config.proto
// version: 1.0.0
// guid: b0c1d2e3-456b-801a-5678-123456789012

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

# HealthStatus for metrics (different from common)
cat > pkg/metrics/proto/health_status.proto << 'EOF'
// file: pkg/metrics/proto/health_status.proto
// version: 1.0.0
// guid: c1d2e3f4-567c-912b-6789-234567890123

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

# ProviderSettingsUpdate and related types
cat > pkg/metrics/proto/provider_settings_update.proto << 'EOF'
// file: pkg/metrics/proto/provider_settings_update.proto
// version: 1.0.0
// guid: d2e3f4a5-678d-023c-7890-345678901234

edition = "2023";

package gcommon.v1.metrics;

option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

message ProviderSettingsUpdate {
  // Prometheus settings update
  PrometheusSettingsUpdate prometheus = 1;

  // OpenTelemetry settings update
  OpenTelemetrySettingsUpdate opentelemetry = 2;

  // StatsD settings update
  StatsDSettingsUpdate statsd = 3;
}

message PrometheusSettingsUpdate {
  // Scrape interval in seconds
  int32 scrape_interval_seconds = 1;

  // Scrape timeout in seconds
  int32 scrape_timeout_seconds = 2;

  // Evaluation interval in seconds
  int32 evaluation_interval_seconds = 3;
}

message OpenTelemetrySettingsUpdate {
  // Endpoint URL
  string endpoint = 1;

  // Sample rate
  double sample_rate = 2;

  // Batch size
  int32 batch_size = 3;
}

message StatsDSettingsUpdate {
  // Host address
  string host = 1;

  // Port number
  int32 port = 2;

  // Buffer size
  int32 buffer_size = 3;
}
EOF

# Continue with more missing types...
echo "Creating more missing types..."

# Provider related types
cat > pkg/metrics/proto/provider_types.proto << 'EOF'
// file: pkg/metrics/proto/provider_types.proto
// version: 1.0.0
// guid: e3f4a5b6-789e-134d-8901-456789012345

edition = "2023";

package gcommon.v1.metrics;

option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

enum ProviderState {
  PROVIDER_STATE_UNSPECIFIED = 0;
  PROVIDER_STATE_ACTIVE = 1;
  PROVIDER_STATE_INACTIVE = 2;
  PROVIDER_STATE_ERROR = 3;
  PROVIDER_STATE_MAINTENANCE = 4;
}

message ProviderStatus {
  // Current state
  ProviderState state = 1;

  // Status message
  string message = 2;

  // Last updated timestamp
  int64 last_updated = 3;
}

message ExportConfigUpdate {
  // Export configuration updates
  repeated ExportDestinationUpdate destinations = 1;

  // Format updates
  string format = 2;

  // Interval updates
  int32 interval_seconds = 3;
}

message ResourceLimitsUpdate {
  // CPU limit
  double cpu_limit = 1;

  // Memory limit in bytes
  int64 memory_limit_bytes = 2;

  // Disk limit in bytes
  int64 disk_limit_bytes = 3;
}

message SecurityConfigUpdate {
  // TLS configuration update
  TLSConfigUpdate tls_config_update = 1;

  // API key configuration update
  APIKeyConfigUpdate api_key_config_update = 2;
}

message TLSConfigUpdate {
  // Certificate path
  string cert_path = 1;

  // Key path
  string key_path = 2;

  // CA path
  string ca_path = 3;

  // Insecure skip verify
  bool insecure_skip_verify = 4;
}

message APIKeyConfigUpdate {
  // API key
  string api_key = 1;

  // Key header name
  string header_name = 2;
}

message TagUpdates {
  // Tags to add
  map<string, string> add_tags = 1;

  // Tags to remove
  repeated string remove_tags = 2;

  // Tags to update
  map<string, string> update_tags = 3;
}
EOF

# Metric related types
cat > pkg/metrics/proto/metric_types.proto << 'EOF'
// file: pkg/metrics/proto/metric_types.proto
// version: 1.0.0
// guid: f4a5b6c7-890f-245e-9012-567890123456

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

message MetricSample {
  // Sample value
  double value = 1;

  // Sample timestamp
  int64 timestamp = 2;

  // Sample labels
  map<string, string> labels = 3;
}

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

# Notification types
echo "Creating Notification module missing types..."

cat > pkg/notification/proto/notification_types.proto << 'EOF'
// file: pkg/notification/proto/notification_types.proto
// version: 1.0.0
// guid: a5b6c7d8-901a-356f-0123-678901234567

edition = "2023";

package gcommon.v1.notification;

option go_package = "github.com/jdfalk/gcommon/pkg/notification/proto";

message SubscriptionPreferences {
  // Email notifications enabled
  bool email_enabled = 1;

  // SMS notifications enabled
  bool sms_enabled = 2;

  // Push notifications enabled
  bool push_enabled = 3;

  // Notification frequency
  string frequency = 4;

  // Quiet hours start
  string quiet_hours_start = 5;

  // Quiet hours end
  string quiet_hours_end = 6;
}

message NotificationMessage {
  // Message ID
  string id = 1;

  // Message title
  string title = 2;

  // Message body
  string body = 3;

  // Message type
  string type = 4;

  // Priority level
  int32 priority = 5;

  // Recipient
  string recipient = 6;

  // Channel type
  string channel = 7;
}
EOF

# Organization types
echo "Creating Organization module missing types..."

cat > pkg/organization/proto/member_role.proto << 'EOF'
// file: pkg/organization/proto/member_role.proto
// version: 1.0.0
// guid: b6c7d8e9-012b-467a-1234-789012345678

edition = "2023";

package gcommon.v1.organization;

option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

enum MemberRole {
  MEMBER_ROLE_UNSPECIFIED = 0;
  MEMBER_ROLE_OWNER = 1;
  MEMBER_ROLE_ADMIN = 2;
  MEMBER_ROLE_MEMBER = 3;
  MEMBER_ROLE_VIEWER = 4;
  MEMBER_ROLE_GUEST = 5;
}
EOF

# Queue types
echo "Creating Queue module missing types..."

cat > pkg/queue/proto/queue_types.proto << 'EOF'
// file: pkg/queue/proto/queue_types.proto
// version: 1.0.0
// guid: c7d8e9f0-123c-578b-2345-890123456789

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

# Web types
echo "Creating Web module missing types..."

cat > pkg/web/proto/web_types.proto << 'EOF'
// file: pkg/web/proto/web_types.proto
// version: 1.0.0
// guid: d8e9f0a1-234d-689c-3456-901234567890

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

enum ServerStatus {
  SERVER_STATUS_UNSPECIFIED = 0;
  SERVER_STATUS_STARTING = 1;
  SERVER_STATUS_RUNNING = 2;
  SERVER_STATUS_STOPPING = 3;
  SERVER_STATUS_STOPPED = 4;
  SERVER_STATUS_ERROR = 5;
}

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

echo "✅ Created ALL missing types"
