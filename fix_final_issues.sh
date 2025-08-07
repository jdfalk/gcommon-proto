#!/bin/bash
# file: fix_final_issues.sh
# version: 1.0.0
# guid: b1c2d3e4-5678-901f-2345-678901234567

set -e

echo "=== Fixing final protobuf issues ==="

# 1. Fix duplicate ConsumerStats in consumer_group.proto
if grep -q "message ConsumerStats" pkg/queue/proto/consumer_group.proto; then
    echo "Removing duplicate ConsumerStats from consumer_group.proto"
    # Remove the duplicate ConsumerStats message and keep only the import
    sed -i '' '/^message ConsumerStats {/,/^}/d' pkg/queue/proto/consumer_group.proto
    # Add import if not present
    if ! grep -q 'import "pkg/queue/proto/consumer_stats.proto"' pkg/queue/proto/consumer_group.proto; then
        # Find package line and add import after it
        package_line=$(grep -n "^package " pkg/queue/proto/consumer_group.proto | head -1 | cut -d: -f1)
        if [ -n "$package_line" ]; then
            sed -i '' "${package_line}a\\
import \"pkg/queue/proto/consumer_stats.proto\";\\
" pkg/queue/proto/consumer_group.proto
        fi
    fi
fi

# 2. Fix duplicate StatsDSettingsUpdate
if [ -f "pkg/metrics/proto/provider_settings_update.proto" ] && [ -f "pkg/metrics/proto/stats_dsettings_update.proto" ]; then
    echo "Removing duplicate StatsDSettingsUpdate from provider_settings_update.proto"
    # Remove the duplicate StatsDSettingsUpdate message
    sed -i '' '/^message StatsDSettingsUpdate {/,/^}/d' pkg/metrics/proto/provider_settings_update.proto
    # Add import
    if ! grep -q 'import "pkg/metrics/proto/stats_dsettings_update.proto"' pkg/metrics/proto/provider_settings_update.proto; then
        package_line=$(grep -n "^package " pkg/metrics/proto/provider_settings_update.proto | head -1 | cut -d: -f1)
        if [ -n "$package_line" ]; then
            sed -i '' "${package_line}a\\
import \"pkg/metrics/proto/stats_dsettings_update.proto\";\\
" pkg/metrics/proto/provider_settings_update.proto
        fi
    fi
fi

# 3. Create missing ProviderState enum
if [ ! -f "pkg/metrics/proto/provider_state.proto" ]; then
cat > pkg/metrics/proto/provider_state.proto << 'EOF'
// file: pkg/metrics/proto/provider_state.proto
// version: 1.0.0
// guid: c2d3e4f5-6789-012a-3456-789012345678

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
EOF
fi

# 4. Add import for ProviderState
if ! grep -q 'import "pkg/metrics/proto/provider_state.proto"' pkg/metrics/proto/provider_status.proto; then
    package_line=$(grep -n "^package " pkg/metrics/proto/provider_status.proto | head -1 | cut -d: -f1)
    if [ -n "$package_line" ]; then
        sed -i '' "${package_line}a\\
import \"pkg/metrics/proto/provider_state.proto\";\\
" pkg/metrics/proto/provider_status.proto
    fi
fi

# 5. Create missing TLS and API key config updates for security
if [ ! -f "pkg/metrics/proto/tls_config_update.proto" ]; then
cat > pkg/metrics/proto/tls_config_update.proto << 'EOF'
// file: pkg/metrics/proto/tls_config_update.proto
// version: 1.0.0
// guid: d3e4f5a6-789a-123b-4567-890123456789

edition = "2023";

package gcommon.v1.metrics;

option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

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
EOF
fi

if [ ! -f "pkg/metrics/proto/api_key_config_update.proto" ]; then
cat > pkg/metrics/proto/api_key_config_update.proto << 'EOF'
// file: pkg/metrics/proto/api_key_config_update.proto
// version: 1.0.0
// guid: e4f5a6b7-890b-234c-5678-901234567890

edition = "2023";

package gcommon.v1.metrics;

option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

message APIKeyConfigUpdate {
  // API key
  string api_key = 1;

  // Key header name
  string header_name = 2;
}
EOF
fi

# 6. Add imports for security config update
if ! grep -q 'import "pkg/metrics/proto/tls_config_update.proto"' pkg/metrics/proto/security_config_update.proto; then
    package_line=$(grep -n "^package " pkg/metrics/proto/security_config_update.proto | head -1 | cut -d: -f1)
    if [ -n "$package_line" ]; then
        sed -i '' "${package_line}a\\
import \"pkg/metrics/proto/tls_config_update.proto\";\\
" pkg/metrics/proto/security_config_update.proto
    fi
fi

if ! grep -q 'import "pkg/metrics/proto/api_key_config_update.proto"' pkg/metrics/proto/security_config_update.proto; then
    package_line=$(grep -n "^package " pkg/metrics/proto/security_config_update.proto | head -1 | cut -d: -f1)
    if [ -n "$package_line" ]; then
        sed -i '' "${package_line}a\\
import \"pkg/metrics/proto/api_key_config_update.proto\";\\
" pkg/metrics/proto/security_config_update.proto
    fi
fi

# 7. Add missing import for HistogramBucket in metric_value.proto
if ! grep -q 'import "pkg/metrics/proto/histogram_bucket.proto"' pkg/metrics/proto/metric_value.proto; then
    package_line=$(grep -n "^package " pkg/metrics/proto/metric_value.proto | head -1 | cut -d: -f1)
    if [ -n "$package_line" ]; then
        sed -i '' "${package_line}a\\
import \"pkg/metrics/proto/histogram_bucket.proto\";\\
" pkg/metrics/proto/metric_value.proto
    fi
fi

# 8. Create missing TimeRange for queue module
if [ ! -f "pkg/queue/proto/time_range.proto" ]; then
cat > pkg/queue/proto/time_range.proto << 'EOF'
// file: pkg/queue/proto/time_range.proto
// version: 1.0.0
// guid: f5a6b7c8-901c-345d-6789-012345678901

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/timestamp.proto";

option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

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

# 9. Add import for queue TimeRange
if ! grep -q 'import "pkg/queue/proto/time_range.proto"' pkg/queue/proto/queue_monitoring_service.proto; then
    package_line=$(grep -n "^package " pkg/queue/proto/queue_monitoring_service.proto | head -1 | cut -d: -f1)
    if [ -n "$package_line" ]; then
        sed -i '' "${package_line}a\\
import \"pkg/queue/proto/time_range.proto\";\\
" pkg/queue/proto/queue_monitoring_service.proto
    fi
fi

echo "✅ All final issues fixed"
echo "Running final test..."

if buf generate > /tmp/buf_ultimate_test.log 2>&1; then
    echo "🎉🎉🎉 ULTIMATE SUCCESS! ALL PROTOBUF COMPILATION ISSUES ARE NOW COMPLETELY FIXED! 🎉🎉🎉"
    echo "Generated $(find . -name "*.pb.go" | wc -l | tr -d ' ') Go files successfully!"
    rm -f /tmp/buf_ultimate_test.log
else
    echo "⚠️  Final issues that need manual attention:"
    cat /tmp/buf_ultimate_test.log
fi
