# Protobuf Consolidation and Lint Fixes - Status Report

## 🎯 Current Status

We have made significant progress fixing protobuf import issues and starting enum consolidation, but there is still work remaining to fully consolidate duplicate enums and resolve all lint issues.

## ✅ Completed Work

### Import Issues Fixed
- ✅ Fixed all missing import type errors (AppenderType, FormatterType, ResourceReference, etc.)
- ✅ Renamed `o_auth2_flow_type.proto` to `oauth2_flow_type.proto` and updated imports
- ✅ Fixed corrupted protobuf files (circuit_breaker_config.proto)
- ✅ Added missing imports for queue services (QueueStreamMetricsRequest, QueueSubscribeRequest)
- ✅ Added lint exclusions for some common enum files

### Enum Consolidation Started
- ✅ Fixed queue priority_level.proto enum naming (added QUEUE_ prefix)
- ✅ Identified duplicate enums across packages that need consolidation

## 🚧 Remaining Work - Agent Instructions

### 1. ENUM CONSOLIDATION - CRITICAL PRIORITY

**Consolidate duplicate enums into common versions:**

The common package has canonical enum definitions that should be used everywhere:
- `proto/gcommon/v1/common/enums/health_status.proto`
- `proto/gcommon/v1/common/enums/compression_type.proto`
- `proto/gcommon/v1/common/enums/alert_severity.proto`
- `proto/gcommon/v1/common/enums/export_format.proto`

**DUPLICATES TO REMOVE:**
```bash
# These files are duplicates and should be DELETED:
proto/gcommon/v1/queue/enums/health_status.proto
proto/gcommon/v1/queue/enums/alert_severity.proto
proto/gcommon/v1/queue/enums/export_format.proto
proto/gcommon/v1/metrics/enums/health_status.proto
proto/gcommon/v1/metrics/enums/compression_type.proto
proto/gcommon/v1/config/enums/compression_type.proto
proto/gcommon/v1/database/enums/compression_type.proto (if exists)
```

**BEFORE DELETING - UPDATE IMPORTS:**
1. Find all files that import the duplicate enums
2. Change imports to use common versions
3. Update enum type references in the files
4. Then delete the duplicate files

**Example:**
```protobuf
// CHANGE FROM:
import "gcommon/v1/queue/enums/health_status.proto";
QueueHealthStatus status = 1;

// CHANGE TO:
import "gcommon/v1/common/enums/health_status.proto";
CommonHealthStatus status = 1;
```

### 2. LINT EXCLUSIONS - DO NOT CHANGE COMMON ENUM NAMES

**CRITICAL: DO NOT rename any enum values in common/*.proto files**

Add lint exclusions to ALL common enum files:
```protobuf
// Add this comment before each enum definition in common files:
// buf:lint:ignore ENUM_VALUE_PREFIX
enum CommonHealthStatus {
  HEALTH_STATUS_UNSPECIFIED = 0;  // KEEP THIS NAME
  // ... rest unchanged
}
```

**Files that need lint exclusions:**
- `proto/gcommon/v1/common/enums/auth_method.proto` (already done)
- `proto/gcommon/v1/common/enums/compression_type.proto` (already done)
- `proto/gcommon/v1/common/enums/filter_type.proto` (already done)
- `proto/gcommon/v1/common/enums/health_status.proto` (already done)
- `proto/gcommon/v1/common/enums/permission_level.proto`
- `proto/gcommon/v1/common/enums/provider_type.proto`
- `proto/gcommon/v1/common/enums/session_state.proto`
- `proto/gcommon/v1/common/enums/subject_type.proto`
- `proto/gcommon/v1/common/enums/two_fa_type.proto`
- `proto/gcommon/v1/common/enums/verification_type.proto`
- `proto/gcommon/v1/common/enums/oauth2_flow_type.proto`

### 3. FINAL VALIDATION & CODE GENERATION

**Install buf if needed:**
```bash
# If buf not available, either:
# Option 1: Install our utility
curl -L https://github.com/jdfalk/copilot-agent-util-rust/releases/latest/download/copilot-agent-util-linux-x86_64 -o copilot-agent-util
chmod +x copilot-agent-util

# Option 2: Install buf directly
curl -sSL "https://github.com/bufbuild/buf/releases/latest/download/buf-$(uname -s)-$(uname -m)" -o /usr/local/bin/buf
chmod +x /usr/local/bin/buf
```

**Validation commands:**
```bash
cd /Users/jdfalk/repos/github.com/jdfalk/gcommon

# 1. Check all lint issues are resolved
buf lint

# 2. Generate complete SDK for Python and Go
buf generate

# 3. Verify no import errors
buf build

# 4. Check final status
echo "Final lint status:"
buf lint | grep -E "(error|Error)" | wc -l
echo "Should be 0 errors"
```

### 4. SPECIFIC ENUM FIXES NEEDED

**Config enums that should be prefixed:**
- `proto/gcommon/v1/config/enums/alert_severity.proto` → Add `CONFIG_ALERT_SEVERITY_` prefix
- `proto/gcommon/v1/config/enums/conflict_resolution.proto` → Add `CONFIG_CONFLICT_RESOLUTION_` prefix
- `proto/gcommon/v1/config/enums/filter_type.proto` → Add `CONFIG_FILTER_TYPE_` prefix

**Database enums that should be prefixed:**
- `proto/gcommon/v1/database/enums/consistency_level.proto` → Add `DATABASE_CONSISTENCY_LEVEL_` prefix
- `proto/gcommon/v1/database/enums/isolation_level.proto` → Add `DATABASE_ISOLATION_LEVEL_` prefix

**Metrics enums that should be prefixed:**
- `proto/gcommon/v1/metrics/enums/change_type.proto` → Add `METRICS_CHANGE_TYPE_` prefix
- `proto/gcommon/v1/metrics/enums/metric_type.proto` → Add `METRICS_METRIC_TYPE_` prefix

### 5. INLINE ENUM FIXES

Many message files have inline enum definitions that need proper prefixes. Search for files with inline enums and fix them:

```bash
grep -r "enum.*{" proto/gcommon/v1/common/messages/ | grep -v "\.proto:"
```

## 🎯 Success Criteria

1. ✅ `buf lint` reports 0 errors
2. ✅ `buf generate` completes successfully
3. ✅ All duplicate enums removed and consolidated to common versions
4. ✅ Complete Python and Go SDK generated
5. ✅ All imports resolve correctly
6. ✅ Common enum names remain unchanged (with lint exclusions)

## 📋 Agent Execution Checklist

- [ ] Add lint exclusions to all common enum files
- [ ] Find and update all imports using duplicate enums
- [ ] Delete duplicate enum files after import updates
- [ ] Fix remaining enum naming for non-common packages
- [ ] Fix inline enum definitions in message files
- [ ] Run final buf lint and buf generate validation
- [ ] Generate complete Python and Go SDKs

## 🔧 Tools Available

The agent should use these existing files:
- `/Users/jdfalk/repos/github.com/jdfalk/gcommon/updated-needs-prefix-fixing` - Current lint issues
- `/Users/jdfalk/repos/github.com/jdfalk/gcommon/buf.yaml` - Buf configuration
- `/Users/jdfalk/repos/github.com/jdfalk/gcommon/buf.gen.yaml` - Code generation config

**REMEMBER: The goal is consolidation and consistency, not just fixing lint warnings!**
