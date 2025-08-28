# organization Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 34
- **Messages**: 34
- **Services**: 0
- **Enums**: 0

## Files in this Module

- [audit_alert.proto](#audit_alert)
- [billing_settings.proto](#billing_settings)
- [cache_behavior.proto](#cache_behavior)
- [cache_key_policy.proto](#cache_key_policy)
- [compute_isolation.proto](#compute_isolation)
- [cpu_allocation.proto](#cpu_allocation)
- [database_isolation.proto](#database_isolation)
- [department.proto](#department)
- [dns_record.proto](#dns_record)
- [email_template.proto](#email_template)
- [feature_flag.proto](#feature_flag)
- [hierarchy_node.proto](#hierarchy_node)
- [hierarchy_path.proto](#hierarchy_path)
- [integration.proto](#integration)
- [integration_settings.proto](#integration_settings)
- [memory_allocation.proto](#memory_allocation)
- [network_acl_rule.proto](#network_acl_rule)
- [network_isolation.proto](#network_isolation)
- [notification_frequency.proto](#notification_frequency)
- [organization.proto](#organization)
- [organization_hierarchy.proto](#organization_hierarchy)
- [organization_member.proto](#organization_member)
- [organization_settings.proto](#organization_settings)
- [security_settings.proto](#security_settings)
- [storage_encryption.proto](#storage_encryption)
- [storage_isolation.proto](#storage_isolation)
- [storage_policy.proto](#storage_policy)
- [storage_quota.proto](#storage_quota)
- [team.proto](#team)
- [tenant.proto](#tenant)
- [tenant_isolation.proto](#tenant_isolation)
- [tenant_quota.proto](#tenant_quota)
- [time_restriction.proto](#time_restriction)
- [ui_settings.proto](#ui_settings)
---


## Detailed Documentation

### audit_alert.proto {#audit_alert}

**Path**: `gcommon/v1/organization/audit_alert.proto` **Package**: `gcommon.v1.organization` **Lines**: 36

**Messages** (1): `AuditAlert`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/audit_alert.proto
// version: 1.0.0
// guid: e9593ddf-e9d4-4f3a-b0e5-3d3e5d5ad8f7

edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message AuditAlert {
  // Alert name
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Event patterns to match
  repeated string event_patterns = 2;

  // Alert severity level
  string severity = 3;

  // Notification channels for this alert
  repeated string notification_channels = 4;

  // Alert threshold (if applicable)
  int32 threshold = 5;

  // Time window for threshold evaluation in minutes
  int32 time_window_minutes = 6;
}
```

---

### billing_settings.proto {#billing_settings}

**Path**: `gcommon/v1/organization/billing_settings.proto` **Package**: `gcommon.v1.organization` **Lines**: 30

**Messages** (1): `BillingSettings`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/billing_settings.proto
// version: 1.0.0
// guid: 839c1259-f26c-4f40-8970-daf8fdead8e3

edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message BillingSettings {
  // Billing contact email
  string billing_email = 1 [ (buf.validate.field).string.email = true ];

  // Billing address
  string billing_address = 2;

  // Tax ID for billing
  string tax_id = 3;

  // Preferred currency for billing
  string currency = 4;

  // Billing cycle (monthly, annual, etc.)
  string billing_cycle = 5;
}
```

---

### cache_behavior.proto {#cache_behavior}

**Path**: `gcommon/v1/organization/cache_behavior.proto` **Package**: `gcommon.v1.organization` **Lines**: 32

**Messages** (1): `CacheBehavior`

**Imports** (3):

- `gcommon/v1/organization/cache_key_policy.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/cache_behavior.proto
// version: 1.0.0
// guid: e71b878c-7505-4ea2-af2b-59a9f9a155ca

edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/organization/cache_key_policy.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message CacheBehavior {
  // Path pattern for this behavior
  string path_pattern = 1 [(buf.validate.field).string.min_len = 1];

  // Cache TTL in seconds
  int64 ttl_seconds = 2 [(buf.validate.field).int64.gte = 0];

  // Whether to compress objects
  bool compress = 3;

  // Allowed HTTP methods
  repeated string allowed_methods = 4 [(buf.validate.field).repeated.min_items = 1];

  // Cache key policy
  CacheKeyPolicy cache_key = 5;
}
```

---

### cache_key_policy.proto {#cache_key_policy}

**Path**: `gcommon/v1/organization/cache_key_policy.proto` **Package**: `gcommon.v1.organization` **Lines**: 34

**Messages** (1): `CacheKeyPolicy`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/cache_key_policy.proto
// version: 1.0.0
// guid: 79bc7887-310b-4ecf-a948-fd2e09760466

edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message CacheKeyPolicy {
  // Whether to include query strings in cache key
  bool include_query_strings = 1;

  // Query string whitelist
  repeated string query_string_whitelist = 2 [(buf.validate.field).repeated.min_items = 1];

  // Whether to include headers in cache key
  bool include_headers = 3;

  // Header whitelist
  repeated string header_whitelist = 4 [(buf.validate.field).repeated.min_items = 1];

  // Whether to include cookies in cache key
  bool include_cookies = 5;

  // Cookie whitelist
  repeated string cookie_whitelist = 6 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### compute_isolation.proto {#compute_isolation}

**Path**: `gcommon/v1/organization/compute_isolation.proto` **Package**: `gcommon.v1.organization` **Lines**: 41

**Messages** (1): `ComputeIsolation`

**Imports** (6):

- `gcommon/v1/common/organization_resource_limits.proto`
- `gcommon/v1/organization/auto_scaling_config.proto`
- `gcommon/v1/organization/cpu_allocation.proto`
- `gcommon/v1/organization/memory_allocation.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/compute_isolation.proto
// version: 1.0.0
// guid: 4d8711b4-c65d-43b7-a0ae-8453f4ffa71f

edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/common/organization_resource_limits.proto";
import "gcommon/v1/organization/auto_scaling_config.proto";
import "gcommon/v1/organization/cpu_allocation.proto";
import "gcommon/v1/organization/memory_allocation.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message ComputeIsolation {
  // Dedicated compute instance identifier
  string compute_instance = 1 [(buf.validate.field).string.min_len = 1];

  // Container or namespace identifier
  string namespace = 2 [(buf.validate.field).string.min_len = 1];

  // CPU allocation for this tenant
  CPUAllocation cpu = 3;

  // Memory allocation for this tenant
  MemoryAllocation memory = 4;

  // Whether tenant has dedicated compute resources
  bool dedicated_compute = 5;

  // Resource limits and quotas
  gcommon.v1.common.OrganizationResourceLimits limits = 6;

  // Auto-scaling configuration
  AutoScalingConfig auto_scaling = 7;
}
```

---

### cpu_allocation.proto {#cpu_allocation}

**Path**: `gcommon/v1/organization/cpu_allocation.proto` **Package**: `gcommon.v1.organization` **Lines**: 28

**Messages** (1): `CPUAllocation`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/cpu_allocation.proto
// version: 1.0.0
// guid: 6794d9c6-3233-4479-b8be-39a3fa3dbe66

edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message CPUAllocation {
  // Number of CPU cores
  int32 cores = 1 [(buf.validate.field).int32.gte = 0];

  // CPU frequency in MHz
  int32 frequency_mhz = 2 [(buf.validate.field).int32.gte = 0];

  // CPU usage limit percentage
  int32 usage_limit_percent = 3 [(buf.validate.field).int32.gte = 0, (buf.validate.field).int32.lte = 150];

  // CPU priority
  int32 priority = 4 [(buf.validate.field).int32.gte = 0];
}
```

---

### database_isolation.proto {#database_isolation}

**Path**: `gcommon/v1/organization/database_isolation.proto` **Package**: `gcommon.v1.organization` **Lines**: 44

**Messages** (1): `DatabaseIsolation`

**Imports** (4):

- `gcommon/v1/common/key_value.proto`
- `gcommon/v1/organization/backup_config.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/database_isolation.proto
// version: 1.0.0
// guid: 3719d310-ed72-4d75-8760-a91686438853

edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/common/key_value.proto";
import "gcommon/v1/organization/backup_config.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message DatabaseIsolation {
  // Database instance identifier (for INFRASTRUCTURE isolation)
  string database_instance = 1;

  // Schema or database name for this tenant
  string schema_name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Database connection parameters
  repeated gcommon.v1.common.KeyValue connection_params = 3 [lazy = true];

  // Whether tenant has dedicated database
  bool dedicated_database = 4;

  // Database backup configuration
  OrganizationBackupConfig backup = 5;

  // Database access restrictions
  repeated string allowed_operations = 6;

  // Maximum connections allowed for this tenant
  int32 max_connections = 7;

  // Query timeout in seconds
  int32 query_timeout_seconds = 8;
}
```

---

### department.proto {#department}

**Path**: `gcommon/v1/organization/department.proto` **Package**: `gcommon.v1.organization` **Lines**: 96

**Messages** (1): `Department`

**Imports** (4):

- `gcommon/v1/common/key_value.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/department.proto
// version: 1.0.0
// guid: 11b263a9-b479-44a3-89ad-5cc707425f8d
edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/common/key_value.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

/**
 * Department message representing an organizational department.
 * Departments provide hierarchical organization structure and
 * can contain teams and individual members.
 */
message Department {
  // Unique department identifier
  string id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Organization identifier
  string organization_id = 2 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Department name
  string name = 3 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // URL-friendly slug for the department
  string slug = 4;

  // Department description or purpose
  string description = 5 [ (buf.validate.field).string.max_len = 1000 ];

  // Parent department ID (for nested departments)
  string parent_department_id = 6;

  // Department head/manager user ID
  string manager_id = 7;

  // Department cost center or budget code
  string cost_center = 8;

  // Physical location or office for this department
  string location = 9;

  // Department metadata and custom attributes
  repeated gcommon.v1.common.KeyValue metadata = 10 [lazy = true];

  // Department creation timestamp
  google.protobuf.Timestamp created_at = 11 [lazy = true, (buf.validate.field).required = true];

  // Last update timestamp
  google.protobuf.Timestamp updated_at = 12 [lazy = true];

  // User ID who created this department
  string created_by = 13 [ (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$" ];

  // User ID who last updated this department
  string updated_by = 14 [ (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$" ];

  // Whether this department is currently active
  bool active = 15;

  // Department's email address for external communications
  string contact_email = 16 [ (buf.validate.field).string.email = true ];

  // Department's phone number
  string phone = 17;

  // Maximum number of members in this department
  int32 max_members = 18;

  // Department's annual budget (in organization's currency)
  double annual_budget = 19;

  // Department's timezone (inherits from organization if not set)
  string timezone = 20;

  // List of child department IDs
  repeated string child_department_ids = 21;

  // List of team IDs that belong to this department
  repeated string team_ids = 22;
}
```

---

### dns_record.proto {#dns_record}

**Path**: `gcommon/v1/organization/dns_record.proto` **Package**: `gcommon.v1.organization` **Lines**: 33

**Messages** (1): `DNSRecord`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/dns_record.proto
// version: 1.0.0
// guid: a84713b6-c765-4b50-99a0-e129f9325dcd

edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message DNSRecord {
  // Record type (A, CNAME, TXT, etc.)
  string type = 1;

  // Record name
  string name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Record value
  string value = 3;

  // Record TTL
  int32 ttl = 4;

  // Record priority (for MX records)
  int32 priority = 5;
}
```

---

### email_template.proto {#email_template}

**Path**: `gcommon/v1/organization/email_template.proto` **Package**: `gcommon.v1.organization` **Lines**: 30

**Messages** (1): `EmailTemplate`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/email_template.proto
// version: 1.0.0
// guid: 03debb46-12b4-4099-9c8f-99523c435029

edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message EmailTemplate {
  // Template name/type (e.g., "welcome", "password_reset")
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Email subject template
  string subject = 2;

  // Email body template (HTML)
  string body_html = 3;

  // Email body template (plain text)
  string body_text = 4;
}
```

---

### feature_flag.proto {#feature_flag}

**Path**: `gcommon/v1/organization/feature_flag.proto` **Package**: `gcommon.v1.organization` **Lines**: 30

**Messages** (1): `FeatureFlag`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/feature_flag.proto
// version: 1.0.0
// guid: 3674ee1a-e166-44d0-97f8-2a41ecf03059

edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message FeatureFlag {
  // Feature flag name
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Whether the feature is enabled
  bool enabled = 2;

  // Feature flag description
  string description = 3 [ (buf.validate.field).string.max_len = 1000 ];

  // Rollout percentage (0-100)
  int32 rollout_percentage = 4;
}
```

---

### hierarchy_node.proto {#hierarchy_node}

**Path**: `gcommon/v1/organization/hierarchy_node.proto` **Package**: `gcommon.v1.organization` **Lines**: 58

**Messages** (1): `HierarchyNode`

**Imports** (3):

- `gcommon/v1/common/key_value.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/hierarchy_node.proto
// version: 1.0.0
// guid: bf24d24c-7e3c-4f4c-b4ea-a8b73c331ed7

edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/common/key_value.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message HierarchyNode {
  // Unique node identifier
  string id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Node name
  string name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Type of organizational unit (department, team, project, etc.)
  string node_type = 3;

  // Reference ID to the actual entity (department_id, team_id, etc.)
  string entity_id = 4;

  // Parent node ID (null for root node)
  string parent_id = 5;

  // List of direct child node IDs
  repeated string child_ids = 6;

  // Node level in the hierarchy (0 for root)
  int32 level = 7;

  // Node position among siblings (for ordering)
  int32 position = 8;

  // Node path from root (e.g., "/org/dept1/team1")
  string path = 9;

  // Manager or responsible person for this node
  string manager_id = 10;

  // Node metadata and custom attributes
  repeated gcommon.v1.common.KeyValue metadata = 11 [lazy = true];

  // Whether this node is currently active
  bool active = 12;
}
```

---

### hierarchy_path.proto {#hierarchy_path}

**Path**: `gcommon/v1/organization/hierarchy_path.proto` **Package**: `gcommon.v1.organization` **Lines**: 28

**Messages** (1): `HierarchyPath`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/hierarchy_path.proto
// version: 1.0.0
// guid: f805b922-255a-475f-86d7-a4420903d7ad

edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message HierarchyPath {
  // Descendant node ID
  string descendant_id = 1 [(buf.validate.field).string.min_len = 1];

  // Ancestor node ID
  string ancestor_id = 2 [(buf.validate.field).string.min_len = 1];

  // Distance between ancestor and descendant (1 = direct parent-child)
  int32 distance = 3 [(buf.validate.field).int32.gte = 0];

  // Complete path from ancestor to descendant
  repeated string path_nodes = 4 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### integration.proto {#integration}

**Path**: `gcommon/v1/organization/integration.proto` **Package**: `gcommon.v1.organization` **Lines**: 35

**Messages** (1): `Integration`

**Imports** (4):

- `gcommon/v1/common/key_value.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/integration.proto
// version: 1.0.0
// guid: 6090f563-98ae-4180-8e95-a161c4e6b658

edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/common/key_value.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message Integration {
  // Integration name (e.g., "slack", "github", "jira")
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Whether this integration is currently enabled
  bool enabled = 2;

  // Integration-specific configuration
  repeated gcommon.v1.common.KeyValue config = 3 [lazy = true];

  // Integration creation timestamp
  google.protobuf.Timestamp created_at = 4 [lazy = true, (buf.validate.field).required = true];

  // User ID who configured this integration
  string configured_by = 5;
}
```

---

### integration_settings.proto {#integration_settings}

**Path**: `gcommon/v1/organization/integration_settings.proto` **Package**: `gcommon.v1.organization` **Lines**: 32

**Messages** (1): `IntegrationSettings`

**Imports** (6):

- `gcommon/v1/common/metrics_api_key_config.proto`
- `gcommon/v1/organization/integration.proto`
- `gcommon/v1/organization/o_auth_app_config.proto`
- `gcommon/v1/organization/webhook_config.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/integration_settings.proto
// version: 1.0.1
// guid: eb075ee2-2fa4-4809-a4b1-66199758b188

edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/common/metrics_api_key_config.proto";
import "gcommon/v1/organization/integration.proto";
import "gcommon/v1/organization/o_auth_app_config.proto";
import "gcommon/v1/organization/webhook_config.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message IntegrationSettings {
  // Enabled third-party integrations
  repeated Integration enabled_integrations = 1 [(buf.validate.field).repeated.min_items = 1];

  // Webhook configuration for external notifications
  repeated WebhookConfig webhooks = 2 [(buf.validate.field).repeated.min_items = 1];

  // API keys for external services
  repeated gcommon.v1.common.MetricsAPIKeyConfig api_keys = 3 [lazy = true, (buf.validate.field).repeated.min_items = 1];

  // OAuth applications registered for this organization
  repeated OAuthAppConfig oauth_apps = 4 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### memory_allocation.proto {#memory_allocation}

**Path**: `gcommon/v1/organization/memory_allocation.proto` **Package**: `gcommon.v1.organization` **Lines**: 25

**Messages** (1): `MemoryAllocation`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/memory_allocation.proto
// version: 1.0.0
// guid: b8114ab9-1c29-4549-ab06-3cad6a44ccf1

edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message MemoryAllocation {
  // Memory size in MB
  int64 size_mb = 1 [(buf.validate.field).int64.gte = 0];

  // Memory usage limit percentage
  int32 usage_limit_percent = 2 [(buf.validate.field).int32.gte = 0, (buf.validate.field).int32.lte = 150];

  // Swap allocation in MB
  int64 swap_mb = 3 [(buf.validate.field).int64.gte = 0];
}
```

---

### network_acl_rule.proto {#network_acl_rule}

**Path**: `gcommon/v1/organization/network_acl_rule.proto` **Package**: `gcommon.v1.organization` **Lines**: 34

**Messages** (1): `NetworkACLRule`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/network_acl_rule.proto
// version: 1.0.0
// guid: 409bba51-1b42-4988-accf-6e848e8862e2

edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message NetworkACLRule {
  // Rule action (allow, deny)
  string action = 1 [(buf.validate.field).string.min_len = 1];

  // Source IP or CIDR block
  string source = 2 [(buf.validate.field).string.min_len = 1];

  // Destination IP or CIDR block
  string destination = 3 [(buf.validate.field).string.min_len = 1];

  // Protocol (TCP, UDP, ICMP)
  string protocol = 4 [(buf.validate.field).string.min_len = 1];

  // Port range
  string port_range = 5 [(buf.validate.field).string.min_len = 1];

  // Rule priority
  int32 priority = 6 [(buf.validate.field).int32.gte = 0];
}
```

---

### network_isolation.proto {#network_isolation}

**Path**: `gcommon/v1/organization/network_isolation.proto` **Package**: `gcommon.v1.organization` **Lines**: 44

**Messages** (1): `NetworkIsolation`

**Imports** (6):

- `gcommon/v1/organization/cdn_config.proto`
- `gcommon/v1/organization/domain_config.proto`
- `gcommon/v1/organization/load_balancer_config.proto`
- `gcommon/v1/organization/network_acl_rule.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/network_isolation.proto
// version: 1.0.0
// guid: d005d972-e2a8-443e-ae8a-dcc1d5be7bd6

edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/organization/cdn_config.proto";
import "gcommon/v1/organization/domain_config.proto";
import "gcommon/v1/organization/load_balancer_config.proto";
import "gcommon/v1/organization/network_acl_rule.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message NetworkIsolation {
  // Virtual private cloud (VPC) identifier
  string vpc_id = 1 [(buf.validate.field).string.min_len = 1];

  // Subnet identifier for this tenant
  string subnet_id = 2 [(buf.validate.field).string.min_len = 1];

  // Security group identifiers
  repeated string security_group_ids = 3 [(buf.validate.field).repeated.min_items = 1];

  // Network access control list (ACL) rules
  repeated NetworkACLRule acl_rules = 4 [(buf.validate.field).repeated.min_items = 1];

  // Whether tenant has dedicated network
  bool dedicated_network = 5;

  // Load balancer configuration for this tenant
  OrganizationLoadBalancerConfig load_balancer = 6;

  // CDN configuration for this tenant
  CDNConfig cdn = 7;

  // Custom domain configuration
  DomainConfig domain = 8;
}
```

---

### notification_frequency.proto {#notification_frequency}

**Path**: `gcommon/v1/organization/notification_frequency.proto` **Package**: `gcommon.v1.organization` **Lines**: 31

**Messages** (1): `NotificationFrequency`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/notification_frequency.proto
// version: 1.0.0
// guid: 49798a1d-bd35-44a3-bcdc-4e5d2bfaa330

edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message NotificationFrequency {
  // Daily digest enabled
  bool daily_digest = 1;

  // Weekly summary enabled
  bool weekly_summary = 2;

  // Instant notifications enabled
  bool instant_notifications = 3;

  // Quiet hours start time (24-hour format, e.g., "22:00")
  string quiet_hours_start = 4 [(buf.validate.field).string.min_len = 1];

  // Quiet hours end time (24-hour format, e.g., "08:00")
  string quiet_hours_end = 5 [(buf.validate.field).string.min_len = 1];
}
```

---

### organization.proto {#organization}

**Path**: `gcommon/v1/organization/organization.proto` **Package**: `gcommon.v1.organization` **Lines**: 113

**Messages** (1): `Organization`

**Imports** (5):

- `buf/validate/validate.proto`
- `gcommon/v1/common/key_value.proto`
- `gcommon/v1/common/organization_status.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/organization.proto
// version: 1.1.0
// guid: 67890def-1234-5678-9abc-def012345678

edition = "2023";

package gcommon.v1.organization;

import "buf/validate/validate.proto";
import "gcommon/v1/common/key_value.proto";
import "gcommon/v1/common/organization_status.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

/**
 * Organization message representing a complete organizational entity.
 * Contains all core information needed for organization management,
 * including metadata, settings, and administrative information.
 */
message Organization {
  // Unique organization identifier (immutable) - must be valid UUID
  string id = 1 [(buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$"];

  // Organization name (human-readable identifier) - required, 1-100 characters
  string name = 2 [
    (buf.validate.field).required = true,
    (buf.validate.field).string.min_len = 1,
    (buf.validate.field).string.max_len = 100
  ];

  // URL-friendly slug for the organization (e.g., for subdomains) - required, alphanumeric with hyphens
  string slug = 3 [
    (buf.validate.field).required = true,
    (buf.validate.field).string.pattern = "^[a-z0-9]([a-z0-9-]*[a-z0-9])?$",
    (buf.validate.field).string.min_len = 2,
    (buf.validate.field).string.max_len = 50
  ];

  // Organization description or mission statement - max 1000 characters
  string description = 4 [(buf.validate.field).string.max_len = 1000];

  // Primary website URL for the organization - must be valid URL if provided
  string website = 5 [(buf.validate.field).string.uri = true];

  // Primary contact email for the organization - must be valid email if provided
  string contact_email = 6 [(buf.validate.field).string.email = true];

  // Organization's physical address or headquarters location - max 500 characters
  string address = 7 [(buf.validate.field).string.max_len = 500];

  // Phone number for organization contact - basic phone format validation
  string phone = 8 [(buf.validate.field).string.pattern = "^[\\+]?[1-9]?[0-9]{7,15}$"];

  // Tax identifier or business registration number - alphanumeric only, max 50 characters
  string tax_id = 9 [
    (buf.validate.field).string.pattern = "^[a-zA-Z0-9]*$",
    (buf.validate.field).string.max_len = 50
  ];

  // Organization's industry or business sector - max 100 characters
  string industry = 10 [(buf.validate.field).string.max_len = 100];

  // Current operational status of the organization - required
  gcommon.v1.common.OrganizationStatus status = 11 [(buf.validate.field).required = true];

  // Organization metadata and custom attributes - max 50 entries
  repeated gcommon.v1.common.KeyValue metadata = 12 [
    lazy = true,
    (buf.validate.field).repeated.max_items = 50
  ];

  // Organization creation timestamp (immutable) - required
  google.protobuf.Timestamp created_at = 13 [
    lazy = true,
    (buf.validate.field).required = true
  ];

  // Last update timestamp - required
  google.protobuf.Timestamp updated_at = 14 [
    lazy = true,
    (buf.validate.field).required = true
  ];

  // User ID who created this organization - must be valid UUID
  string created_by = 15 [(buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$"];

  // User ID who last updated this organization - must be valid UUID
  string updated_by = 16 [(buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$"];

  // Organization's timezone (IANA timezone identifier) - must be valid timezone format
  string timezone = 17 [(buf.validate.field).string.pattern = "^[A-Za-z]+\\/[A-Za-z_]+([A-Za-z_\\/]*)$"];

  // Organization's primary language/locale - must be valid locale format (e.g., en-US, fr-FR)
  string locale = 18 [(buf.validate.field).string.pattern = "^[a-z]{2}(-[A-Z]{2})?$"];

  // Maximum number of members allowed in this organization - must be positive
  int32 max_members = 19 [
    (buf.validate.field).int32.gte = 1,
    (buf.validate.field).int32.lte = 100000
  ];

  // Whether this organization supports multi-tenancy
  bool multi_tenant_enabled = 20;

  // Organization's logo or avatar URL - must be valid URL if provided
  string avatar_url = 21 [(buf.validate.field).string.uri = true];

  // Organization's billing contact email (if different from contact_email) - must be valid email if provided
  string billing_email = 22 [(buf.validate.field).string.email = true];
}
```

---

### organization_hierarchy.proto {#organization_hierarchy}

**Path**: `gcommon/v1/organization/organization_hierarchy.proto` **Package**: `gcommon.v1.organization` **Lines**: 64

**Messages** (1): `OrganizationHierarchy`

**Imports** (6):

- `gcommon/v1/common/hierarchy_type.proto`
- `gcommon/v1/common/key_value.proto`
- `gcommon/v1/organization/hierarchy_node.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/organization_hierarchy.proto
// version: 1.0.0
// guid: 2f0bea22-4f4d-4ac2-99bf-2b65d15ebebd

edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/common/hierarchy_type.proto";
import "gcommon/v1/common/key_value.proto";
import "gcommon/v1/organization/hierarchy_node.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message OrganizationHierarchy {
  // Unique hierarchy identifier
  string id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Organization identifier
  string organization_id = 2 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Type of hierarchy structure
  gcommon.v1.common.HierarchyType hierarchy_type = 3;

  // Name of this hierarchy configuration
  string name = 4 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Description of this hierarchy structure
  string description = 5 [ (buf.validate.field).string.max_len = 1000 ];

  // Root node of the hierarchy (typically the organization itself)
  HierarchyNode root_node = 6;

  // Whether this hierarchy is currently active/primary
  bool active = 7;

  // Hierarchy metadata and configuration
  repeated gcommon.v1.common.KeyValue metadata = 8 [lazy = true];

  // Hierarchy creation timestamp
  google.protobuf.Timestamp created_at = 9 [lazy = true, (buf.validate.field).required = true];

  // Last update timestamp
  google.protobuf.Timestamp updated_at = 10 [lazy = true];

  // User ID who created this hierarchy
  string created_by = 11 [ (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$" ];

  // User ID who last updated this hierarchy
  string updated_by = 12 [ (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$" ];
}
```

---

### organization_member.proto {#organization_member}

**Path**: `gcommon/v1/organization/organization_member.proto` **Package**: `gcommon.v1.organization` **Lines**: 105

**Messages** (1): `OrganizationMember`

**Imports** (5):

- `gcommon/v1/common/key_value.proto`
- `gcommon/v1/common/member_role.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/organization_member.proto
// version: 1.0.0
// guid: 74375b8f-7a0b-4243-94fe-3c59ed01f5c4
edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/common/key_value.proto";
import "gcommon/v1/common/member_role.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

/**
 * OrganizationMember message representing a user's membership in an organization.
 * Contains role information, permissions, and membership metadata.
 */
message OrganizationMember {
  // Unique membership identifier
  string id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Organization identifier
  string organization_id = 2 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // User identifier from the auth system
  string user_id = 3 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // User's email address (cached for quick access)
  string email = 4 [ (buf.validate.field).string.email = true ];

  // User's display name (cached for quick access)
  string display_name = 5 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Primary role of the user in this organization
  gcommon.v1.common.MemberRole role = 6;

  // Additional roles the user may have
  repeated gcommon.v1.common.MemberRole additional_roles = 7;

  // Specific permissions granted to this member
  repeated string permissions = 8;

  // Department IDs this member belongs to
  repeated string department_ids = 9;

  // Team IDs this member belongs to
  repeated string team_ids = 10;

  // Tenant IDs this member has access to (for multi-tenant organizations)
  repeated string tenant_ids = 11;

  // Member metadata and custom attributes
  repeated gcommon.v1.common.KeyValue metadata = 12 [lazy = true];

  // Membership creation timestamp (when user joined organization)
  google.protobuf.Timestamp created_at = 13 [lazy = true, (buf.validate.field).required = true];

  // Last update timestamp
  google.protobuf.Timestamp updated_at = 14 [lazy = true];

  // Last activity timestamp (when user was last active in organization)
  google.protobuf.Timestamp last_active_at = 15 [lazy = true];

  // User ID who added this member to the organization
  string invited_by = 16;

  // User ID who last updated this member's information
  string updated_by = 17 [ (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$" ];

  // Whether this member is currently active
  bool active = 18;

  // Member's job title within the organization
  string job_title = 19;

  // Member's manager's user ID (if applicable)
  string manager_id = 20;

  // Member's direct reports' user IDs
  repeated string direct_report_ids = 21;

  // Member's avatar/profile picture URL
  string avatar_url = 22 [ (buf.validate.field).string.uri = true ];

  // Member's phone number (organization context)
  string phone = 23;

  // Member's office location or workspace
  string location = 24;
}
```

---

### organization_settings.proto {#organization_settings}

**Path**: `gcommon/v1/organization/organization_settings.proto` **Package**: `gcommon.v1.organization` **Lines**: 60

**Messages** (1): `OrganizationSettings`

**Imports** (11):

- `gcommon/v1/common/key_value.proto`
- `gcommon/v1/common/organization_compliance_settings.proto`
- `gcommon/v1/common/organization_notification_settings.proto`
- `gcommon/v1/organization/billing_settings.proto`
- `gcommon/v1/organization/feature_flag.proto`
- `gcommon/v1/organization/integration_settings.proto`
- `gcommon/v1/organization/security_settings.proto`
- `gcommon/v1/organization/ui_settings.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/organization_settings.proto
// version: 1.0.0
// guid: 16cd3cd6-4780-44b7-96c0-facf112a08bc

edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/common/key_value.proto";
import "gcommon/v1/common/organization_compliance_settings.proto";
import "gcommon/v1/common/organization_notification_settings.proto";
import "gcommon/v1/organization/billing_settings.proto";
import "gcommon/v1/organization/feature_flag.proto";
import "gcommon/v1/organization/integration_settings.proto";
import "gcommon/v1/organization/security_settings.proto";
import "gcommon/v1/organization/ui_settings.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message OrganizationSettings {
  // Organization identifier
  string organization_id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Security and authentication settings
  SecuritySettings security = 2;

  // User interface and experience settings
  UISettings ui = 3;

  // Integration and API settings
  IntegrationSettings integrations = 4;

  // Notification and communication settings
  gcommon.v1.common.OrganizationNotificationSettings notifications = 5;

  // Billing and subscription settings
  BillingSettings billing = 6;

  // Data retention and compliance settings
  gcommon.v1.common.OrganizationComplianceSettings compliance = 7;

  // Feature flags and experimental features
  repeated FeatureFlag feature_flags = 8;

  // Custom organization-specific settings
  repeated gcommon.v1.common.KeyValue custom_settings = 9 [lazy = true];

  // Settings last update timestamp
  google.protobuf.Timestamp updated_at = 10 [lazy = true];

  // User ID who last updated these settings
  string updated_by = 11 [ (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$" ];
}
```

---

### security_settings.proto {#security_settings}

**Path**: `gcommon/v1/organization/security_settings.proto` **Package**: `gcommon.v1.organization` **Lines**: 50

**Messages** (1): `SecuritySettings`

**Imports** (3):

- `gcommon/v1/organization/rate_limit_config.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/security_settings.proto
// version: 1.0.0
// guid: 89b40ea9-8cb2-44a5-ba5e-9cbd6aeb4e24

edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/organization/rate_limit_config.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message SecuritySettings {
  // Whether multi-factor authentication is required for all users
  bool require_mfa = 1;

  // Minimum password length requirement
  int32 min_password_length = 2 [(buf.validate.field).int32.gte = 0];

  // Whether password complexity rules are enforced
  bool require_password_complexity = 3;

  // Password expiration period in days (0 = no expiration)
  int32 password_expiry_days = 4 [(buf.validate.field).int32.gte = 0];

  // Session timeout in minutes
  int32 session_timeout_minutes = 5 [(buf.validate.field).int32.gt = 0];

  // Whether single sign-on (SSO) is enabled
  bool sso_enabled = 6;

  // Allowed SSO providers
  repeated string sso_providers = 7 [(buf.validate.field).repeated.min_items = 1];

  // IP address whitelist for organization access
  repeated string ip_whitelist = 8 [(buf.validate.field).repeated.min_items = 1];

  // Whether API access is enabled
  bool api_access_enabled = 9;

  // API rate limiting configuration
  OrganizationRateLimitConfig api_rate_limit = 10;

  // Audit log retention period in days
  int32 audit_log_retention_days = 11 [(buf.validate.field).int32.gte = 0];
}
```

---

### storage_encryption.proto {#storage_encryption}

**Path**: `gcommon/v1/organization/storage_encryption.proto` **Package**: `gcommon.v1.organization` **Lines**: 28

**Messages** (1): `StorageEncryption`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/storage_encryption.proto
// version: 1.0.0
// guid: 3d3d43d3-d498-4554-9651-d85b30a777c7

edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message StorageEncryption {
  // Encryption type (AES256, KMS)
  string type = 1 [(buf.validate.field).string.min_len = 1];

  // Key ID for KMS encryption
  string key_id = 2 [(buf.validate.field).string.min_len = 1];

  // Whether server-side encryption is enabled
  bool server_side = 3;

  // Whether client-side encryption is enabled
  bool client_side = 4;
}
```

---

### storage_isolation.proto {#storage_isolation}

**Path**: `gcommon/v1/organization/storage_isolation.proto` **Package**: `gcommon.v1.organization` **Lines**: 41

**Messages** (1): `StorageIsolation`

**Imports** (6):

- `gcommon/v1/organization/storage_backup_config.proto`
- `gcommon/v1/organization/storage_encryption.proto`
- `gcommon/v1/organization/storage_policy.proto`
- `gcommon/v1/organization/storage_quota.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/storage_isolation.proto
// version: 1.0.0
// guid: 45bc9c83-d152-457b-b9d4-f5ea0a861fc0

edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/organization/storage_backup_config.proto";
import "gcommon/v1/organization/storage_encryption.proto";
import "gcommon/v1/organization/storage_policy.proto";
import "gcommon/v1/organization/storage_quota.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message StorageIsolation {
  // Storage bucket or container identifier
  string storage_bucket = 1 [(buf.validate.field).string.min_len = 1];

  // Storage path prefix for this tenant
  string path_prefix = 2 [(buf.validate.field).string.min_len = 1];

  // Whether tenant has dedicated storage
  bool dedicated_storage = 3;

  // Storage encryption configuration
  StorageEncryption encryption = 4;

  // Storage access policies
  repeated StoragePolicy policies = 5 [(buf.validate.field).repeated.min_items = 1];

  // Backup and replication configuration
  StorageBackupConfig backup = 6;

  // Storage quota limits
  StorageQuota quota = 7;
}
```

---

### storage_policy.proto {#storage_policy}

**Path**: `gcommon/v1/organization/storage_policy.proto` **Package**: `gcommon.v1.organization` **Lines**: 33

**Messages** (1): `StoragePolicy`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/storage_policy.proto
// version: 1.0.0
// guid: 7a5f99b0-8434-408a-9c22-199f4ea471af

edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message StoragePolicy {
  // Policy name
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Policy statement (JSON)
  string statement = 2;

  // Policy effect (Allow, Deny)
  string effect = 3;

  // Resources covered by this policy
  repeated string resources = 4;

  // Actions covered by this policy
  repeated string actions = 5;
}
```

---

### storage_quota.proto {#storage_quota}

**Path**: `gcommon/v1/organization/storage_quota.proto` **Package**: `gcommon.v1.organization` **Lines**: 28

**Messages** (1): `StorageQuota`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/storage_quota.proto
// version: 1.0.0
// guid: d87a1435-3bce-4513-adf6-2be8c493d5f1

edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message StorageQuota {
  // Maximum storage size in bytes
  int64 max_size_bytes = 1 [(buf.validate.field).int64.gte = 0];

  // Maximum number of objects
  int64 max_objects = 2 [(buf.validate.field).int64.gte = 0];

  // Maximum request rate per second
  int32 max_requests_per_second = 3 [(buf.validate.field).int32.gte = 0];

  // Transfer quota in bytes per month
  int64 transfer_quota_bytes = 4 [(buf.validate.field).int64.gte = 0];
}
```

---

### team.proto {#team}

**Path**: `gcommon/v1/organization/team.proto` **Package**: `gcommon.v1.organization` **Lines**: 105

**Messages** (1): `Team`

**Imports** (4):

- `gcommon/v1/common/key_value.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/team.proto
// version: 1.0.0
// guid: 6af03494-7f90-4ad9-9e30-cb8eaa7ef367
edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/common/key_value.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

/**
 * Team message representing a team within an organization or department.
 * Teams are smaller organizational units focused on specific projects,
 * functions, or objectives.
 */
message Team {
  // Unique team identifier
  string id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Organization identifier
  string organization_id = 2 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Department identifier (teams can belong to departments)
  string department_id = 3;

  // Team name
  string name = 4 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // URL-friendly slug for the team
  string slug = 5;

  // Team description or purpose
  string description = 6 [ (buf.validate.field).string.max_len = 1000 ];

  // Team lead/manager user ID
  string lead_id = 7;

  // Team type or category (e.g., "engineering", "marketing", "sales")
  string team_type = 8;

  // Team's primary focus area or mission
  string focus_area = 9;

  // Team metadata and custom attributes
  repeated gcommon.v1.common.KeyValue metadata = 10 [lazy = true];

  // Team creation timestamp
  google.protobuf.Timestamp created_at = 11 [lazy = true, (buf.validate.field).required = true];

  // Last update timestamp
  google.protobuf.Timestamp updated_at = 12 [lazy = true];

  // User ID who created this team
  string created_by = 13 [ (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$" ];

  // User ID who last updated this team
  string updated_by = 14 [ (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$" ];

  // Whether this team is currently active
  bool active = 15;

  // Team's email address for external communications
  string contact_email = 16 [ (buf.validate.field).string.email = true ];

  // Team's communication channel (e.g., Slack channel, Discord server)
  string communication_channel = 17;

  // Maximum number of members in this team
  int32 max_members = 18;

  // Team's budget allocation (in organization's currency)
  double budget_allocation = 19;

  // Team's timezone (inherits from department/organization if not set)
  string timezone = 20;

  // List of member user IDs in this team
  repeated string member_ids = 21;

  // List of project IDs this team is responsible for
  repeated string project_ids = 22;

  // Team's goals or objectives for the current period
  repeated string objectives = 23;

  // Team's key performance indicators or metrics
  repeated string kpis = 24;

  // Whether this team is cross-functional (spans multiple departments)
  bool cross_functional = 25;
}
```

---

### tenant.proto {#tenant}

**Path**: `gcommon/v1/organization/tenant.proto` **Package**: `gcommon.v1.organization` **Lines**: 93

**Messages** (1): `Tenant`

**Imports** (7):

- `gcommon/v1/common/isolation_level.proto`
- `gcommon/v1/common/key_value.proto`
- `gcommon/v1/common/tenant_status.proto`
- `gcommon/v1/organization/tenant_quota.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/tenant.proto
// version: 1.0.0
// guid: 560b99c3-131a-4c92-bcaf-034974f1561a
edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/common/isolation_level.proto";
import "gcommon/v1/common/key_value.proto";
import "gcommon/v1/common/tenant_status.proto";
import "gcommon/v1/organization/tenant_quota.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

/**
 * Tenant message representing a tenant within an organization.
 * Supports multi-tenant architecture with configurable isolation levels,
 * resource quotas, and tenant-specific settings.
 */
message Tenant {
  // Unique tenant identifier (immutable)
  string id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Parent organization identifier
  string organization_id = 2 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Tenant name (human-readable identifier)
  string name = 3 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // URL-friendly slug for the tenant (e.g., for subdomains)
  string slug = 4;

  // Tenant description
  string description = 5 [ (buf.validate.field).string.max_len = 1000 ];

  // Current status of the tenant
  gcommon.v1.common.TenantStatus status = 6;

  // Isolation level for this tenant
  gcommon.v1.common.OrganizationIsolationLevel isolation_level = 7;

  // Tenant metadata and custom attributes
  repeated gcommon.v1.common.KeyValue metadata = 8 [lazy = true];

  // Tenant creation timestamp (immutable)
  google.protobuf.Timestamp created_at = 9 [lazy = true, (buf.validate.field).required = true];

  // Last update timestamp
  google.protobuf.Timestamp updated_at = 10 [lazy = true];

  // User ID who created this tenant
  string created_by = 11 [ (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$" ];

  // User ID who last updated this tenant
  string updated_by = 12 [ (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$" ];

  // Database connection string or identifier (for DATABASE isolation)
  string database_config = 13;

  // Network configuration (for NETWORK isolation)
  string network_config = 14;

  // Resource quotas for this tenant
  TenantQuota quota = 15;

  // Custom domain for this tenant (if applicable)
  string custom_domain = 16;

  // Tenant's timezone override (inherits from organization if not set)
  string timezone = 17;

  // Tenant's locale override (inherits from organization if not set)
  string locale = 18;

  // Whether this tenant is in trial mode
  bool trial_mode = 19;

  // Trial expiration timestamp (if trial_mode is true)
  google.protobuf.Timestamp trial_expires_at = 20 [lazy = true];
}
```

---

### tenant_isolation.proto {#tenant_isolation}

**Path**: `gcommon/v1/organization/tenant_isolation.proto` **Package**: `gcommon.v1.organization` **Lines**: 64

**Messages** (1): `TenantIsolation`

**Imports** (12):

- `gcommon/v1/common/isolation_level.proto`
- `gcommon/v1/common/key_value.proto`
- `gcommon/v1/common/organization_access_control.proto`
- `gcommon/v1/organization/audit_config.proto`
- `gcommon/v1/organization/compute_isolation.proto`
- `gcommon/v1/organization/database_isolation.proto`
- `gcommon/v1/organization/encryption_config.proto`
- `gcommon/v1/organization/network_isolation.proto`
- `gcommon/v1/organization/storage_isolation.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/tenant_isolation.proto
// version: 1.0.0
// guid: 182f08bf-4180-421a-935c-aa065bea181a

edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/common/isolation_level.proto";
import "gcommon/v1/common/key_value.proto";
import "gcommon/v1/common/organization_access_control.proto";
import "gcommon/v1/organization/audit_config.proto";
import "gcommon/v1/organization/compute_isolation.proto";
import "gcommon/v1/organization/database_isolation.proto";
import "gcommon/v1/organization/encryption_config.proto";
import "gcommon/v1/organization/network_isolation.proto";
import "gcommon/v1/organization/storage_isolation.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message TenantIsolation {
  // Tenant identifier
  string tenant_id = 1;

  // Isolation level for this tenant
  gcommon.v1.common.OrganizationIsolationLevel level = 2;

  // Database isolation configuration
  DatabaseIsolation database = 3;

  // Network isolation configuration
  NetworkIsolation network = 4;

  // Storage isolation configuration
  StorageIsolation storage = 5;

  // Compute isolation configuration
  ComputeIsolation compute = 6;

  // Encryption configuration for tenant data
  OrganizationEncryptionConfig encryption = 7;

  // Access control configuration
  gcommon.v1.common.OrganizationAccessControl access_control = 8;

  // Audit and compliance configuration
  AuditConfig audit = 9;

  // Isolation metadata and custom settings
  repeated gcommon.v1.common.KeyValue metadata = 10 [lazy = true];

  // Isolation configuration creation timestamp
  google.protobuf.Timestamp created_at = 11 [lazy = true, (buf.validate.field).required = true];

  // Last update timestamp
  google.protobuf.Timestamp updated_at = 12 [lazy = true];

  // User ID who configured this isolation
  string configured_by = 13;
}
```

---

### tenant_quota.proto {#tenant_quota}

**Path**: `gcommon/v1/organization/tenant_quota.proto` **Package**: `gcommon.v1.organization` **Lines**: 44

**Messages** (1): `TenantQuota`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/tenant_quota.proto
// version: 1.0.0
// guid: 00b319b2-df4a-4664-9a2e-7eb13cb80bf1
// Tenant quota message definition

edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

/**
 * TenantQuota defines resource limits and quotas for a tenant.
 */
message TenantQuota {
  // Tenant ID this quota applies to
  string tenant_id = 1 [(buf.validate.field).string.min_len = 1];

  // Maximum number of users
  int32 max_users = 2 [(buf.validate.field).int32.gte = 0];

  // Maximum storage in bytes
  int64 max_storage_bytes = 3 [(buf.validate.field).int64.gte = 0];

  // Maximum API requests per hour
  int32 max_api_requests_per_hour = 4 [(buf.validate.field).int32.gte = 0];

  // Maximum number of projects
  int32 max_projects = 5 [(buf.validate.field).int32.gte = 0];

  // Maximum bandwidth in bytes per month
  int64 max_bandwidth_bytes_per_month = 6 [(buf.validate.field).int64.gte = 0];

  // Whether the tenant can create sub-tenants
  bool can_create_sub_tenants = 7;

  // Custom quota attributes
  map<string, string> custom_quotas = 8;
}
```

---

### time_restriction.proto {#time_restriction}

**Path**: `gcommon/v1/organization/time_restriction.proto` **Package**: `gcommon.v1.organization` **Lines**: 28

**Messages** (1): `TimeRestriction`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/time_restriction.proto
// version: 1.0.0
// guid: e1c0e36e-397a-42c1-a74a-e7aeca18ade2

edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message TimeRestriction {
  // Day of week (0-6, 0=Sunday)
  int32 day_of_week = 1 [(buf.validate.field).int32.gte = 0];

  // Start time (24-hour format, e.g., "09:00")
  string start_time = 2 [(buf.validate.field).string.min_len = 1];

  // End time (24-hour format, e.g., "17:00")
  string end_time = 3 [(buf.validate.field).string.min_len = 1];

  // Timezone for this restriction
  string timezone = 4 [(buf.validate.field).string.min_len = 1];
}
```

---

### ui_settings.proto {#ui_settings}

**Path**: `gcommon/v1/organization/ui_settings.proto` **Package**: `gcommon.v1.organization` **Lines**: 45

**Messages** (1): `UISettings`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/ui_settings.proto
// version: 1.0.0
// guid: e3ed3da1-f827-4d15-974d-f19dd591a248

edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message UISettings {
  // Organization's primary brand color (hex code)
  string primary_color = 1;

  // Organization's secondary brand color (hex code)
  string secondary_color = 2;

  // Organization's logo URL
  string logo_url = 3 [ (buf.validate.field).string.uri = true ];

  // Organization's favicon URL
  string favicon_url = 4 [ (buf.validate.field).string.uri = true ];

  // Custom CSS for organization branding
  string custom_css = 5;

  // Default language/locale for organization
  string default_locale = 6;

  // Default timezone for organization
  string default_timezone = 7;

  // Date format preference (e.g., "MM/DD/YYYY", "DD/MM/YYYY")
  string date_format = 8;

  // Time format preference (12-hour or 24-hour)
  string time_format = 9;

  // Whether dark mode is enabled by default
  bool dark_mode_default = 10;
}
```

---

