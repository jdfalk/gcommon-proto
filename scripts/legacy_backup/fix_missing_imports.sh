#!/bin/bash
# Auto-generated script to fix missing proto imports

# Fix imports for metrics/proto/get_metrics_request.proto
sed -i '/^import.*proto";$/a import "metrics/proto/metric_aggregation.proto";' 'pkg/metrics/proto/get_metrics_request.proto'

# Fix imports for metrics/proto/metric_config.proto
sed -i '/^import.*proto";$/a import "metrics/proto/export_config.proto";' 'pkg/metrics/proto/metric_config.proto'
