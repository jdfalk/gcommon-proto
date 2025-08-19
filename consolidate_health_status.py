#!/usr/bin/env python3
# file: consolidate_health_status.py
# version: 1.0.0
# guid: 12345678-9abc-def0-1234-56789abcdef0

"""
Consolidate all health status imports to use the common version.
"""

import os
import re

def fix_health_status_imports():
    """Fix all files that import non-existent metrics health_status to use common version."""
    
    # Files that need fixing
    files_to_fix = [
        "proto/gcommon/v1/common/messages/health_check_response.proto",
        "proto/gcommon/v1/common/messages/run_check_response.proto", 
        "proto/gcommon/v1/common/messages/set_health_request.proto",
        "proto/gcommon/v1/common/messages/set_health_response.proto",
        "proto/gcommon/v1/config/enums/config_environment.proto",
        "proto/gcommon/v1/database/messages/health_check_response.proto",
        "proto/gcommon/v1/metrics/messages/health_check_response.proto",
        "proto/gcommon/v1/metrics/messages/metric_health.proto",
        "proto/gcommon/v1/metrics/messages/metrics_health_info.proto",
        "proto/gcommon/v1/queue/messages/cluster_health.proto",
        "proto/gcommon/v1/queue/messages/health_check_response.proto",
        "proto/gcommon/v1/queue/messages/queue_health.proto",
        "proto/gcommon/v1/web/messages/health_check_response.proto"
    ]
    
    for file_path in files_to_fix:
        if not os.path.exists(file_path):
            print(f"❌ File not found: {file_path}")
            continue
            
        with open(file_path, "r") as f:
            content = f.read()
            
        original_content = content
        
        # Fix import statement
        content = re.sub(
            r'import "gcommon/v1/metrics/enums/health_status\.proto";',
            'import "gcommon/v1/common/enums/health_status.proto";',
            content
        )
        
        # Fix type references - both fully qualified and short form
        content = re.sub(
            r'gcommon\.v1\.metrics\.MetricsHealthStatus',
            'gcommon.v1.common.CommonHealthStatus',
            content
        )
        
        # Fix short form type references  
        content = re.sub(
            r'\bMetricsHealthStatus\b',
            'gcommon.v1.common.CommonHealthStatus',
            content
        )
        
        if content != original_content:
            with open(file_path, "w") as f:
                f.write(content)
            print(f"✅ Fixed health status imports in {file_path}")
        else:
            print(f"ℹ️  No changes needed in {file_path}")

if __name__ == "__main__":
    fix_health_status_imports()