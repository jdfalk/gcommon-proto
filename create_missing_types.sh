#!/bin/bash
# file: create_missing_types.sh
# version: 1.0.0
# guid: b1c2d3e4-f5a6-7890-bcde-f12345678901

set -e

echo "Creating missing types for protobuf compilation..."

# Config module missing types
echo "=== Creating Config Module Missing Types ==="

# RateLimits
cat > pkg/config/proto/rate_limits.proto << 'EOF'
// file: pkg/config/proto/rate_limits.proto
// version: 1.0.0
// guid: c2d3e4f5-6a7b-8901-cdef-234567890123

edition = "2023";

package gcommon.v1.config;

option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message RateLimits {
  // Maximum requests per second
  int32 requests_per_second = 1;

  // Maximum burst size
  int32 burst_size = 2;

  // Rate limit window in seconds
  int32 window_seconds = 3;
}
EOF

# ComplianceAudit
cat > pkg/config/proto/compliance_audit.proto << 'EOF'
// file: pkg/config/proto/compliance_audit.proto
// version: 1.0.0
// guid: d3e4f5a6-7b8c-9012-def0-345678901234

edition = "2023";

package gcommon.v1.config;

option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message ComplianceAudit {
  // Audit ID
  string id = 1;

  // Audit name
  string name = 2;

  // Audit type
  string type = 3;

  // Audit enabled status
  bool enabled = 4;
}
EOF

# ComplianceReporting
cat > pkg/config/proto/compliance_reporting.proto << 'EOF'
// file: pkg/config/proto/compliance_reporting.proto
// version: 1.0.0
// guid: e4f5a6b7-8c9d-0123-ef01-456789012345

edition = "2023";

package gcommon.v1.config;

option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message ComplianceReporting {
  // Reporting enabled status
  bool enabled = 1;

  // Report frequency in hours
  int32 frequency_hours = 2;

  // Report recipients
  repeated string recipients = 3;
}
EOF

# ConfigStats
cat > pkg/config/proto/config_stats.proto << 'EOF'
// file: pkg/config/proto/config_stats.proto
// version: 1.0.0
// guid: f5a6b7c8-9d0e-1234-f012-567890123456

edition = "2023";

package gcommon.v1.config;

option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message ConfigStats {
  // Total number of configurations
  int64 total_configs = 1;

  // Number of active configurations
  int64 active_configs = 2;

  // Number of deprecated configurations
  int64 deprecated_configs = 3;

  // Average access frequency
  double avg_access_frequency = 4;
}
EOF

# MonitoringAlert
cat > pkg/config/proto/monitoring_alert.proto << 'EOF'
// file: pkg/config/proto/monitoring_alert.proto
// version: 1.0.0
// guid: a6b7c8d9-0e1f-2345-0123-678901234567

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

  // Alert threshold
  double threshold = 4;

  // Alert enabled status
  bool enabled = 5;
}
EOF

# RotationEvent
cat > pkg/config/proto/rotation_event.proto << 'EOF'
// file: pkg/config/proto/rotation_event.proto
// version: 1.0.0
// guid: b7c8d9e0-1f23-4567-1234-789012345678

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/timestamp.proto";

option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message RotationEvent {
  // Event ID
  string id = 1;

  // Rotation timestamp
  google.protobuf.Timestamp timestamp = 2;

  // Previous value
  string previous_value = 3;

  // New value
  string new_value = 4;

  // Rotation reason
  string reason = 5;
}
EOF

# ParameterConstraints
cat > pkg/config/proto/parameter_constraints.proto << 'EOF'
// file: pkg/config/proto/parameter_constraints.proto
// version: 1.0.0
// guid: c8d9e0f1-2345-6789-2345-890123456789

edition = "2023";

package gcommon.v1.config;

option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message ParameterConstraints {
  // Minimum value
  string min_value = 1;

  // Maximum value
  string max_value = 2;

  // Pattern validation
  string pattern = 3;

  // Required flag
  bool required = 4;

  // Default value
  string default_value = 5;
}
EOF

# UsageTrend
cat > pkg/config/proto/usage_trend.proto << 'EOF'
// file: pkg/config/proto/usage_trend.proto
// version: 1.0.0
// guid: d9e0f1a2-3456-789a-3456-901234567890

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/timestamp.proto";

option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message UsageTrend {
  // Timestamp
  google.protobuf.Timestamp timestamp = 1;

  // Usage count
  int64 usage_count = 2;

  // Trend direction
  string direction = 3;
}
EOF

# ValidationSeverity
cat > pkg/config/proto/validation_severity.proto << 'EOF'
// file: pkg/config/proto/validation_severity.proto
// version: 1.0.0
// guid: e0f1a2b3-4567-890b-4567-012345678901

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

echo "✅ Created Config module missing types"

# Metrics module missing types
echo "=== Creating Metrics Module Missing Types ==="

# AlertSeverity
cat > pkg/metrics/proto/alert_severity.proto << 'EOF'
// file: pkg/metrics/proto/alert_severity.proto
// version: 1.0.0
// guid: f1a2b3c4-5678-901c-5678-123456789012

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

# ComparisonOperator
cat > pkg/metrics/proto/comparison_operator.proto << 'EOF'
// file: pkg/metrics/proto/comparison_operator.proto
// version: 1.0.0
// guid: a2b3c4d5-6789-012d-6789-234567890123

edition = "2023";

package gcommon.v1.metrics;

option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

enum ComparisonOperator {
  COMPARISON_OPERATOR_UNSPECIFIED = 0;
  COMPARISON_OPERATOR_EQUAL = 1;
  COMPARISON_OPERATOR_NOT_EQUAL = 2;
  COMPARISON_OPERATOR_GREATER_THAN = 3;
  COMPARISON_OPERATOR_GREATER_THAN_OR_EQUAL = 4;
  COMPARISON_OPERATOR_LESS_THAN = 5;
  COMPARISON_OPERATOR_LESS_THAN_OR_EQUAL = 6;
}
EOF

# Create a comprehensive script to generate all missing types
echo "=== Creating remaining missing types ==="

# Add imports to files that need common types
echo "Adding missing common type imports..."

# Fix db module Error imports
find pkg/db/proto -name "*.proto" -exec grep -l "gcommon.v1.common.Error" {} \; | while read file; do
    if ! grep -q "import.*pkg/common/proto/error.proto" "$file"; then
        echo "Adding Error import to $file"
        sed -i '' '/^package /a\
\
import "pkg/common/proto/error.proto";' "$file"
    fi
done

echo "✅ Created missing types and imports"
