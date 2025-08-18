#!/bin/bash
# file: batch_commit.sh
# version: 1.0.0
# guid: a1b2c3d4-e5f6-7890-abcd-ef1234567890

set -e

echo "Analyzing and batch committing protobuf fixes..."

# Function to commit files matching a pattern
commit_batch() {
    local pattern="$1"
    local commit_msg="$2"
    local files=$(git status --porcelain | grep "^M" | awk '{print $2}' | grep -E "$pattern" || true)

    if [ -n "$files" ]; then
        echo "Committing batch: $commit_msg"
        echo "$files" | head -5  # Show first 5 files as preview
        if [ $(echo "$files" | wc -l) -gt 5 ]; then
            echo "... and $(( $(echo "$files" | wc -l) - 5 )) more files"
        fi
        echo "$files" | xargs git add
        git commit -m "$commit_msg"
        echo "✅ Committed $(echo "$files" | wc -l) files"
        echo
    else
        echo "No files found for pattern: $pattern"
    fi
}

# 1. Proto definition fixes (source files)
echo "=== Batch 1: Protocol Buffer Definition Fixes ==="
commit_batch "\.proto$" "fix(protobuf): correct import paths and remove duplicate imports

- Remove duplicate and malformed import statements
- Fix circular import dependencies
- Correct go_package option paths for all modules
- Remove invalid protobuf feature options
- Standardize edition declarations"

# 2. Common module generated code
echo "=== Batch 2: Common Module Generated Code ==="
commit_batch "pkg/common/proto/.*\.pb\.go$" "feat(protobuf): generate common module Go bindings

- Generate Go code for shared common types
- Include Error, RequestMetadata, HealthStatus definitions
- Add KeyValue and ConfigValue type bindings
- Update all common protobuf Go interfaces"

# 3. Auth module generated code
echo "=== Batch 3: Auth Module Generated Code ==="
commit_batch "pkg/auth/proto/.*\.pb\.go$" "feat(protobuf): generate auth module Go bindings

- Generate Go code for authentication types
- Include User, Role, Permission definitions
- Add Session and Token management bindings
- Update auth service interfaces"

# 4. Health module generated code
echo "=== Batch 4: Health Module Generated Code ==="
commit_batch "pkg/health/proto/.*\.pb\.go$" "feat(protobuf): generate health module Go bindings

- Generate Go code for health checking types
- Include HealthCheckRequest and response definitions
- Add health status monitoring bindings
- Update health service interfaces"

# 5. Organization module generated code
echo "=== Batch 5: Organization Module Generated Code ==="
commit_batch "pkg/organization/proto/.*\.pb\.go$" "feat(protobuf): generate organization module Go bindings

- Generate Go code for organization management
- Include Tenant, Team, Department definitions
- Add organization member and role bindings
- Update organization service interfaces"

# 6. Database module generated code
echo "=== Batch 6: Database Module Generated Code ==="
commit_batch "pkg/db/proto/.*\.pb\.go$" "feat(protobuf): generate database module Go bindings

- Generate Go code for database operations
- Include transaction and connection types
- Add database status monitoring bindings
- Update database service interfaces"

# 7. Config module generated code
echo "=== Batch 7: Config Module Generated Code ==="
commit_batch "pkg/config/proto/.*\.pb\.go$" "feat(protobuf): generate config module Go bindings

- Generate Go code for configuration management
- Include config entry and validation types
- Add configuration service bindings
- Update config management interfaces"

# 8. Cache module generated code
echo "=== Batch 8: Cache Module Generated Code ==="
commit_batch "pkg/cache/proto/.*\.pb\.go$" "feat(protobuf): generate cache module Go bindings

- Generate Go code for caching operations
- Include cache entry and statistics types
- Add cache management service bindings
- Update cache operation interfaces"

# 9. Metrics module generated code
echo "=== Batch 9: Metrics Module Generated Code ==="
commit_batch "pkg/metrics/proto/.*\.pb\.go$" "feat(protobuf): generate metrics module Go bindings

- Generate Go code for metrics collection
- Include metric data and metadata types
- Add scrape configuration bindings
- Update metrics service interfaces"

# 10. Queue module generated code
echo "=== Batch 10: Queue Module Generated Code ==="
commit_batch "pkg/queue/proto/.*\.pb\.go$" "feat(protobuf): generate queue module Go bindings

- Generate Go code for queue management
- Include job and task definition types
- Add queue statistics and status bindings
- Update queue service interfaces"

# 11. Web module generated code
echo "=== Batch 11: Web Module Generated Code ==="
commit_batch "pkg/web/proto/.*\.pb\.go$" "feat(protobuf): generate web module Go bindings

- Generate Go code for web service types
- Include HTTP request/response definitions
- Add web service configuration bindings
- Update web API interfaces"

# 12. Notification module generated code
echo "=== Batch 12: Notification Module Generated Code ==="
commit_batch "pkg/notification/proto/.*\.pb\.go$" "feat(protobuf): generate notification module Go bindings

- Generate Go code for notification services
- Include message and channel definitions
- Add notification delivery bindings
- Update notification service interfaces"

# 13. Media module generated code (if exists)
echo "=== Batch 13: Media Module Generated Code ==="
commit_batch "pkg/media/proto/.*\.pb\.go$" "feat(protobuf): generate media module Go bindings

- Generate Go code for media management
- Include media metadata and quality types
- Add media processing bindings
- Update media service interfaces"

# 14. Log module generated code (if exists)
echo "=== Batch 14: Log Module Generated Code ==="
commit_batch "pkg/log/proto/.*\.pb\.go$" "feat(protobuf): generate log module Go bindings

- Generate Go code for logging services
- Include log entry and configuration types
- Add log management bindings
- Update logging service interfaces"

# 15. Any remaining generated files
echo "=== Batch 15: Remaining Generated Files ==="
commit_batch ".*\.pb\.go$" "feat(protobuf): generate remaining module Go bindings

- Generate Go code for any remaining modules
- Complete protobuf compilation process
- Update all remaining service interfaces"

# 16. Any remaining proto files
echo "=== Batch 16: Remaining Proto Definition Updates ==="
commit_batch "\.proto$" "fix(protobuf): finalize remaining proto definition updates

- Complete any remaining protobuf definition fixes
- Ensure all modules have correct configuration
- Finalize protobuf compilation setup"

# Final check
echo "=== Final Status Check ==="
remaining=$(git status --porcelain | wc -l)
if [ "$remaining" -gt 0 ]; then
    echo "⚠️  Warning: $remaining files still uncommitted"
    echo "Remaining files:"
    git status --porcelain | head -10
    if [ "$remaining" -gt 10 ]; then
        echo "... and $(( remaining - 10 )) more"
    fi

    # Commit any remaining files
    echo "Committing all remaining files..."
    git add .
    git commit -m "fix(protobuf): commit any remaining protobuf-related changes

- Ensure all protobuf compilation artifacts are committed
- Complete the protobuf generation and fix process
- Include any miscellaneous files from the buf generate process"
else
    echo "✅ All files committed successfully!"
fi

echo "🎉 Batch commit process complete!"
