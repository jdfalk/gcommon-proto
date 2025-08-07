#!/bin/bash
# file: fix_protobuf_issues.sh
# version: 1.0.0
# guid: e4f5a6b7-890e-245f-9012-567890123456

set -e

echo "=== IDEMPOTENT PROTOBUF ISSUE FIXER ==="

# First, check if we need to do anything
echo "Checking current state..."
if buf generate > /tmp/buf_check.log 2>&1; then
    echo "✅ Protobuf compilation already working! No changes needed."
    exit 0
fi

echo "🔧 Issues found, proceeding with fixes..."

# 1. Remove duplicate type definitions by deleting consolidated files that conflict
echo "=== Step 1: Removing duplicate type definitions ==="

# Remove consolidated files that have duplicates with individual files
files_to_remove=(
    "pkg/metrics/proto/metric_types.proto"
    "pkg/metrics/proto/provider_types.proto"
    "pkg/queue/proto/queue_types.proto"
    "pkg/web/proto/web_types.proto"
    "pkg/notification/proto/notification_types.proto"
)

for file in "${files_to_remove[@]}"; do
    if [ -f "$file" ]; then
        echo "Removing duplicate file: $file"
        rm "$file"
    fi
done

# 2. Create only the missing types that don't exist anywhere
echo "=== Step 2: Creating missing types ==="

# Config module missing types
if [ ! -f "pkg/config/proto/access_restriction.proto" ]; then
cat > pkg/config/proto/access_restriction.proto << 'EOF'
// file: pkg/config/proto/access_restriction.proto
// version: 1.0.0
// guid: a1b2c3d4-5678-901e-f234-567890123456

edition = "2023";

package gcommon.v1.config;

option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message AccessRestriction {
  // Restriction type
  string type = 1;

  // Restriction value
  string value = 2;

  // Description
  string description = 3;

  // Enabled status
  bool enabled = 4;
}
EOF
fi

if [ ! -f "pkg/config/proto/rate_limits.proto" ]; then
cat > pkg/config/proto/rate_limits.proto << 'EOF'
// file: pkg/config/proto/rate_limits.proto
// version: 1.0.0
// guid: b2c3d4e5-6789-012f-3456-678901234567

edition = "2023";

package gcommon.v1.config;

option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message RateLimits {
  // Requests per second limit
  int32 requests_per_second = 1;

  // Burst size
  int32 burst_size = 2;

  // Window duration in seconds
  int32 window_duration_seconds = 3;

  // Enabled status
  bool enabled = 4;
}
EOF
fi

if [ ! -f "pkg/config/proto/compliance_audit.proto" ]; then
cat > pkg/config/proto/compliance_audit.proto << 'EOF'
// file: pkg/config/proto/compliance_audit.proto
// version: 1.0.0
// guid: c3d4e5f6-789a-123b-4567-789012345678

edition = "2023";

package gcommon.v1.config;

option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message ComplianceAudit {
  // Audit ID
  string id = 1;

  // Audit type
  string type = 2;

  // Status
  string status = 3;

  // Timestamp
  int64 timestamp = 4;

  // Details
  string details = 5;
}
EOF
fi

if [ ! -f "pkg/config/proto/compliance_reporting.proto" ]; then
cat > pkg/config/proto/compliance_reporting.proto << 'EOF'
// file: pkg/config/proto/compliance_reporting.proto
// version: 1.0.0
// guid: d4e5f6a7-890b-234c-5678-890123456789

edition = "2023";

package gcommon.v1.config;

option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message ComplianceReporting {
  // Enabled status
  bool enabled = 1;

  // Report frequency
  string frequency = 2;

  // Recipients
  repeated string recipients = 3;

  // Report format
  string format = 4;
}
EOF
fi

if [ ! -f "pkg/config/proto/config_change.proto" ]; then
cat > pkg/config/proto/config_change.proto << 'EOF'
// file: pkg/config/proto/config_change.proto
// version: 1.0.0
// guid: e5f6a7b8-901c-345d-6789-901234567890

edition = "2023";

package gcommon.v1.config;

option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message ConfigChange {
  // Change ID
  string id = 1;

  // Key that was changed
  string key = 2;

  // Old value
  string old_value = 3;

  // New value
  string new_value = 4;

  // Timestamp
  int64 timestamp = 5;

  // User who made the change
  string changed_by = 6;
}
EOF
fi

if [ ! -f "pkg/config/proto/config_stats.proto" ]; then
cat > pkg/config/proto/config_stats.proto << 'EOF'
// file: pkg/config/proto/config_stats.proto
// version: 1.0.0
// guid: f6a7b8c9-012d-456e-7890-012345678901

edition = "2023";

package gcommon.v1.config;

option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message ConfigStats {
  // Total config entries
  int64 total_entries = 1;

  // Recently modified count
  int64 recently_modified = 2;

  // Cache hit rate
  double cache_hit_rate = 3;

  // Average lookup time in milliseconds
  double avg_lookup_time_ms = 4;
}
EOF
fi

if [ ! -f "pkg/config/proto/monitoring_alert.proto" ]; then
cat > pkg/config/proto/monitoring_alert.proto << 'EOF'
// file: pkg/config/proto/monitoring_alert.proto
// version: 1.0.0
// guid: a7b8c9d0-123e-567f-8901-123456789012

edition = "2023";

package gcommon.v1.config;

option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message MonitoringAlert {
  // Alert ID
  string id = 1;

  // Alert name
  string name = 2;

  // Alert condition
  string condition = 3;

  // Threshold
  double threshold = 4;

  // Enabled status
  bool enabled = 5;
}
EOF
fi

if [ ! -f "pkg/config/proto/rotation_event.proto" ]; then
cat > pkg/config/proto/rotation_event.proto << 'EOF'
// file: pkg/config/proto/rotation_event.proto
// version: 1.0.0
// guid: b8c9d0e1-234f-678a-9012-234567890123

edition = "2023";

package gcommon.v1.config;

option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message RotationEvent {
  // Event ID
  string id = 1;

  // Event type
  string type = 2;

  // Timestamp
  int64 timestamp = 3;

  // Previous value
  string previous_value = 4;

  // New value
  string new_value = 5;

  // Status
  string status = 6;
}
EOF
fi

if [ ! -f "pkg/config/proto/parameter_constraints.proto" ]; then
cat > pkg/config/proto/parameter_constraints.proto << 'EOF'
// file: pkg/config/proto/parameter_constraints.proto
// version: 1.0.0
// guid: c9d0e1f2-345a-789b-0123-345678901234

edition = "2023";

package gcommon.v1.config;

option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message ParameterConstraints {
  // Minimum value
  string min_value = 1;

  // Maximum value
  string max_value = 2;

  // Pattern regex
  string pattern = 3;

  // Required status
  bool required = 4;

  // Allowed values
  repeated string allowed_values = 5;
}
EOF
fi

if [ ! -f "pkg/config/proto/usage_trend.proto" ]; then
cat > pkg/config/proto/usage_trend.proto << 'EOF'
// file: pkg/config/proto/usage_trend.proto
// version: 1.0.0
// guid: d0e1f2a3-456b-890c-1234-456789012345

edition = "2023";

package gcommon.v1.config;

option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message UsageTrend {
  // Time period
  string period = 1;

  // Access count
  int64 access_count = 2;

  // Modification count
  int64 modification_count = 3;

  // Growth rate
  double growth_rate = 4;
}
EOF
fi

if [ ! -f "pkg/config/proto/validation_severity.proto" ]; then
cat > pkg/config/proto/validation_severity.proto << 'EOF'
// file: pkg/config/proto/validation_severity.proto
// version: 1.0.0
// guid: e1f2a3b4-567c-901d-2345-567890123456

edition = "2023";

package gcommon.v1.config;

option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

enum ValidationSeverity {
  VALIDATION_SEVERITY_UNSPECIFIED = 0;
  VALIDATION_SEVERITY_INFO = 1;
  VALIDATION_SEVERITY_WARNING = 2;
  VALIDATION_SEVERITY_ERROR = 3;
  VALIDATION_SEVERITY_CRITICAL = 4;
}
EOF
fi

# Metrics module missing types
if [ ! -f "pkg/metrics/proto/alert_severity.proto" ]; then
cat > pkg/metrics/proto/alert_severity.proto << 'EOF'
// file: pkg/metrics/proto/alert_severity.proto
// version: 1.0.0
// guid: f2a3b4c5-678d-012e-3456-678901234567

edition = "2023";

package gcommon.v1.metrics;

option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

enum AlertSeverity {
  ALERT_SEVERITY_UNSPECIFIED = 0;
  ALERT_SEVERITY_LOW = 1;
  ALERT_SEVERITY_MEDIUM = 2;
  ALERT_SEVERITY_HIGH = 3;
  ALERT_SEVERITY_CRITICAL = 4;
}
EOF
fi

if [ ! -f "pkg/metrics/proto/comparison_operator.proto" ]; then
cat > pkg/metrics/proto/comparison_operator.proto << 'EOF'
// file: pkg/metrics/proto/comparison_operator.proto
// version: 1.0.0
// guid: a3b4c5d6-789e-123f-4567-789012345678

edition = "2023";

package gcommon.v1.metrics;

option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

enum ComparisonOperator {
  COMPARISON_OPERATOR_UNSPECIFIED = 0;
  COMPARISON_OPERATOR_EQUAL = 1;
  COMPARISON_OPERATOR_NOT_EQUAL = 2;
  COMPARISON_OPERATOR_GREATER = 3;
  COMPARISON_OPERATOR_GREATER_EQUAL = 4;
  COMPARISON_OPERATOR_LESS = 5;
  COMPARISON_OPERATOR_LESS_EQUAL = 6;
}
EOF
fi

# Organization module missing types
if [ ! -f "pkg/organization/proto/member_role.proto" ]; then
cat > pkg/organization/proto/member_role.proto << 'EOF'
// file: pkg/organization/proto/member_role.proto
// version: 1.0.0
// guid: b4c5d6e7-890f-234a-5678-890123456789

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
fi

# Notification module missing types
if [ ! -f "pkg/notification/proto/subscription_preferences.proto" ]; then
cat > pkg/notification/proto/subscription_preferences.proto << 'EOF'
// file: pkg/notification/proto/subscription_preferences.proto
// version: 1.0.0
// guid: c5d6e7f8-901a-345b-6789-901234567890

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
EOF
fi

if [ ! -f "pkg/notification/proto/notification_message.proto" ]; then
cat > pkg/notification/proto/notification_message.proto << 'EOF'
// file: pkg/notification/proto/notification_message.proto
// version: 1.0.0
// guid: d6e7f8a9-012b-456c-7890-012345678901

edition = "2023";

package gcommon.v1.notification;

option go_package = "github.com/jdfalk/gcommon/pkg/notification/proto";

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
fi

# Individual missing types that already exist should be left alone

echo "=== Step 3: Testing compilation ==="
if buf generate > /tmp/buf_final_check.log 2>&1; then
    echo "✅ SUCCESS: All protobuf issues fixed!"
    rm -f /tmp/buf_check.log /tmp/buf_final_check.log
else
    echo "❌ Some issues remain. Check /tmp/buf_final_check.log for details:"
    head -20 /tmp/buf_final_check.log
fi

echo "=== Fix script completed ==="
