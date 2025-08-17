<!-- file: CODING_AGENT_INSTRUCTIONS.md -->
<!-- version: 1.0.0 -->
<!-- guid: 8d9e7f6a-5b4c-3d2e-1f0a-9b8c7d6e5f4a -->

# 🚀 PROTOBUF COMPLETION PROJECT - CODING AGENT INSTRUCTIONS

## PROJECT OVERVIEW

This project needs to complete the protobuf implementation for a comprehensive Go microservices framework. We are currently at **76% module generation success rate (10/13 modules passing)** and need to reach **100% success with all protobuf
modules building cleanly**.

## CURRENT STATUS (as of August 14, 2025)

### ✅ MODULES CURRENTLY PASSING (10/13)

- auth ✅
- cache ✅
- common ✅
- config ✅
- db ✅
- health ✅
- log ✅
- media ✅
- notification ✅
- web ✅

### ❌ MODULES STILL FAILING (3/13)

1. **metrics** - Import path issues with retention_policy.proto
2. **organization** - Missing access_control.proto import
3. **queue** - Multiple type qualification issues

## CRITICAL RULES AND GUIDELINES

### 🔥 MANDATORY: READ ALL INSTRUCTIONS FIRST

You MUST read and follow these comprehensive protobuf guidelines:

**EMBEDDED PROTOBUF INSTRUCTIONS** (file: `.github/instructions/protobuf.instructions.md`):

````markdown
<!-- file: .github/instructions/protobuf.instructions.md -->
<!-- version: 3.0.0 -->
<!-- guid: 7d6c5b4a-3c2d-1e0f-9a8b-7c6d5e4f3a2b -->

## Core Principles

- Follow the 1-1-1 Best Practice - one top-level entity per file
- Use Edition 2023 for all new files: `edition = "2023";`
- Use module prefixes for ALL messages: `{Module}{MessageName}`
- Import order: Google imports, types imports, other modules

## Module Prefix Rules (MANDATORY)

ALL messages MUST include module prefix to avoid conflicts:

| Module         | Prefix         | Examples                                                         |
| -------------- | -------------- | ---------------------------------------------------------------- |
| `auth`         | `Auth`         | `AuthUserInfo`, `AuthSessionData`, `AuthLoginRequest`            |
| `metrics`      | `Metrics`      | `MetricsHealthStatus`, `MetricsBatchOptions`, `MetricsTimeRange` |
| `organization` | `Organization` | `OrganizationAccessControl`, `OrganizationResourceLimits`        |
| `queue`        | `Queue`        | `QueueSubscriptionInfo`, `QueueMessage`, `QueueConfiguration`    |
| `database`     | `Database`     | `DatabaseHealthStatus`, `DatabaseConnection`                     |
| `web`          | `Web`          | `WebHealthResponse`, `WebConfiguration`                          |
| `common`       | `Common`       | `CommonError`, `CommonPagination`                                |

## Cross-Package Type References

When referencing types from other packages, use FULL QUALIFICATION:

```protobuf
// ✅ CORRECT
message MyMessage {
  gcommon.v1.metrics.MetricsHealthStatus status = 1;
  gcommon.v1.organization.OrganizationAccessControl access = 2;
}

// ❌ WRONG
message MyMessage {
  MetricsHealthStatus status = 1;  // Unqualified
  OrganizationAccessControl access = 2;  // Unqualified
}
```
````

## Required File Header

```protobuf
// file: path/to/file.proto
// version: 1.0.0
// guid: 123e4567-e89b-12d3-a456-426614174000

edition = "2023";

package gcommon.v1.module;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/module/proto";
```

````

### 🛠 TOOLS AND WORKFLOWS

**MANDATORY: Use VS Code Tasks and Rust Utility**

- **ALWAYS use VS Code tasks** instead of manual terminal commands
- Use the rust utility wrapper: `copilot-agent-util` for consistent logging
- Check task logs in `logs/` folder after execution
- Available tasks:
  - `Buf Generate Per Module` - Run per-module generation with detailed reporting
  - `Git Add All` - Stage all changes
  - `Git Push` - Push to remote

**Per-Module Generation Script**: `scripts/buf-generate-per-module.sh`
- Generates each module individually with detailed error reporting
- Creates logs for each module: `logs/buf_generate_{module}_{timestamp}.log`
- Provides actionable error summaries

## SPECIFIC TASKS TO COMPLETE

### 🎯 TASK 1: Fix Remaining 3 Failing Modules (CRITICAL)

#### Metrics Module Issues
**Error**: `pkg/metrics/proto/health_check_result.proto:14:8:import "pkg/metrics/proto/..s/retention_policy.proto": parse error: invalid relative path`

**Actions Required**:
1. Find the malformed import path in `pkg/metrics/proto/health_check_result.proto`
2. Fix the import to proper path (likely `pkg/metrics/proto/retention_policy.proto`)
3. Ensure `RetentionPolicy` message has correct module prefix: `MetricsRetentionPolicy`

#### Organization Module Issues
**Error**: `pkg/organization/proto/tenant_isolation.proto:33:3:field gcommon.v1.organization.TenantIsolation.access_control: unknown type OrganizationAccessControl`

**Actions Required**:
1. Add missing import: `import "pkg/organization/proto/access_control.proto";`
2. Verify `OrganizationAccessControl` message exists in that file
3. Use fully qualified type: `gcommon.v1.organization.OrganizationAccessControl`

#### Queue Module Issues
**Error**: Multiple unknown types: `NotificationChannelType`, `AlertSeverityLevel`, `QueueAlertSeverity`, `QueueNotificationChannel`

**Actions Required**:
1. Fix import paths in `pkg/queue/proto/alerting_config.proto`
2. Use correct qualified types:
   - `gcommon.v1.metrics.MetricsAlertSeverity` (not `QueueAlertSeverity`)
   - `gcommon.v1.queue.QueueNotificationChannel` (if defined in queue module)
3. Ensure all cross-package references are fully qualified

### 🎯 TASK 2: Ensure All Protobuf Modules Build (CRITICAL)

**Success Criteria**: `Buf Generate Per Module` task shows **13/13 modules passing (100% success rate)**

**Validation Steps**:
1. Run `Buf Generate Per Module` VS Code task
2. Check output shows all modules as ✅ SUCCESS
3. Verify no errors in individual module logs in `logs/` directory
4. Confirm generated Go and Python files compile without errors

### 🎯 TASK 3: Verify 1-1-1 Pattern Compliance (HIGH PRIORITY)

**Requirements**:
- Each `.proto` file contains exactly ONE of: message, enum, or service definition
- Files follow naming convention: `{message_name}.proto` (snake_case filename, TitleCase message)
- All messages use module prefixes: `{Module}{MessageName}`

**Validation**:
```bash
# Count messages per file (should be 1)
find pkg -name "*.proto" -exec grep -l "^message " {} \; | while read file; do
  count=$(grep -c "^message " "$file")
  if [ $count -ne 1 ]; then
    echo "VIOLATION: $file has $count messages"
  fi
done
````

### 🎯 TASK 4: Go Code Integration (MEDIUM PRIORITY)

**Goal**: Ensure non-generated Go code uses protobuf types instead of custom structs

**Actions Required**:

1. **Audit Go Files**: Find Go files defining custom types that duplicate protobuf messages
2. **Replace Custom Types**: Use generated protobuf types in Go code
3. **Update Imports**: Change imports to use generated protobuf packages
4. **Embedding Pattern**: For Go-specific functionality, embed protobuf types in structs:

```go
// ✅ CORRECT: Embed protobuf type
type UserService struct {
    *pb.AuthUserInfo  // Embed generated protobuf type
    db *sql.DB        // Add Go-specific fields
}

// ❌ WRONG: Duplicate protobuf definition
type UserInfo struct {
    UserID string    // This duplicates AuthUserInfo
    Email  string
}
```

### 🎯 TASK 5: Subtitle Manager Integration (MEDIUM PRIORITY)

**Context**: There's a separate `subtitle-manager` repository that may need additional protobuf definitions.

**Actions Required**:

1. **Review TODO.md**: Check for subtitle-specific protobuf requirements
2. **Check Related Repos**: Look for markdown files describing subtitle manager protobuf needs
3. **Implement Missing Protos**: Create any required subtitle-related protobuf definitions
4. **Cross-Repository**: Ensure subtitle-manager can import from gcommon protobuf definitions

## DETAILED IMPLEMENTATION STEPS

### Step 1: Environment Setup

1. Ensure you're in the correct workspace: `/Users/jdfalk/repos/github.com/jdfalk/gcommon`
2. Verify buf is authenticated (user mentioned they logged in)
3. Run initial status check: `Buf Generate Per Module` task

### Step 2: Fix Metrics Module

1. Open `pkg/metrics/proto/health_check_result.proto`
2. Find malformed import line (contains `..s/retention_policy.proto`)
3. Fix to correct path: `pkg/metrics/proto/retention_policy.proto`
4. Verify target file exists and contains `MetricsRetentionPolicy` message
5. Test: Run `buf generate --path pkg/metrics/proto/`

### Step 3: Fix Organization Module

1. Open `pkg/organization/proto/tenant_isolation.proto`
2. Add missing import: `import "pkg/organization/proto/access_control.proto";`
3. Verify field uses qualified type: `gcommon.v1.organization.OrganizationAccessControl access_control = X;`
4. Check that `OrganizationAccessControl` message exists in access_control.proto
5. Test: Run `buf generate --path pkg/organization/proto/`

### Step 4: Fix Queue Module

1. Open `pkg/queue/proto/alerting_config.proto`
2. Review all import statements for correctness
3. Update type references to use proper qualification:
   - Alert severity: `gcommon.v1.metrics.MetricsAlertSeverity`
   - Notification channels: `gcommon.v1.queue.QueueNotificationChannel` (if queue-specific)
4. Add missing imports as needed
5. Test: Run `buf generate --path pkg/queue/proto/`

### Step 5: Comprehensive Validation

1. Run `Buf Generate Per Module` task
2. Verify 13/13 modules pass (100% success rate)
3. Check generated files compile:
   ```bash
   go build ./...  # Should succeed without errors
   ```
4. Commit all changes with descriptive message

### Step 6: Go Code Audit

1. Search for custom type definitions that duplicate protobuf:
   ```bash
   grep -r "type.*struct" --include="*.go" . | grep -v ".pb.go"
   ```
2. Identify types that should use protobuf instead
3. Refactor to use generated protobuf types
4. Update imports and method signatures

### Step 7: Documentation and Completion

1. Update TODO.md with completion status
2. Create summary of changes made
3. Verify all tests pass
4. Push final changes

## ERROR HANDLING AND DEBUGGING

### Common Issues and Solutions

**Import Cycles**:

- Move shared types to `common` module
- Use forward declarations where possible
- Review import dependencies carefully

**Unknown Types**:

- Always use fully qualified type names for cross-package references
- Verify import paths are correct
- Check target message exists in imported file

**Module Prefix Violations**:

- All messages must have module prefix: `{Module}{MessageName}`
- Services use module prefix: `{Module}Service`
- Enums may omit prefix if no conflicts exist

**Field Presence Issues (Edition 2023)**:

- Don't use `optional` keyword
- Use `[features.field_presence = EXPLICIT]` for nullable fields

## SUCCESS CRITERIA

### ✅ COMPLETION CHECKLIST

**Phase 1: Protobuf Compilation (Critical)**

- [ ] All 13 modules pass buf generation (100% success rate)
- [ ] No import errors or unknown type references
- [ ] Generated Go and Python files compile without errors
- [ ] All proto files follow 1-1-1 pattern
- [ ] All messages use correct module prefixes

**Phase 2: Go Integration (High Priority)**

- [ ] Non-generated Go code uses protobuf types
- [ ] No duplicate type definitions between Go and protobuf
- [ ] All imports reference generated protobuf packages
- [ ] Tests pass with protobuf integration

**Phase 3: Documentation and Validation (Medium Priority)**

- [ ] TODO.md updated with completion status
- [ ] All protobuf files have proper documentation
- [ ] Integration tests validate cross-module functionality
- [ ] Performance benchmarks show acceptable performance

## FINAL NOTES

This is a comprehensive protobuf implementation project that requires attention to detail and systematic debugging. The framework already has excellent tooling in place - use the VS Code tasks and rust utility for consistent execution.

The user will be away, so work autonomously and commit frequently with descriptive messages. Focus on getting the remaining 3 modules to pass first, then work on the broader integration tasks.

**Remember**: This is not just about making the build pass - it's about creating a production-ready, scalable protobuf framework that follows best practices and avoids common pitfalls.
