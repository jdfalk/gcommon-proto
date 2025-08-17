# organization Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 13
- **Messages**: 39
- **Services**: 0
- **Enums**: 5

## Files in this Module

- [department.proto](#department)
- [hierarchy_type.proto](#hierarchy_type)
- [isolation_level.proto](#isolation_level)
- [member_role.proto](#member_role)
- [organization.proto](#organization)
- [organization_hierarchy.proto](#organization_hierarchy)
- [organization_member.proto](#organization_member)
- [organization_status.proto](#organization_status)
- [team.proto](#team)
- [tenant.proto](#tenant)
- [tenant_isolation.proto](#tenant_isolation)
- [tenant_quota.proto](#tenant_quota)
- [tenant_status.proto](#tenant_status)

## Module Dependencies

**This module depends on**:

- [common](./common.md)
- [database](./database.md)

**Modules that depend on this one**:

- [database](./database.md)
- [organization_api_1](./organization_api_1.md)
- [organization_api_2](./organization_api_2.md)
- [organization_config](./organization_config.md)

---

## Detailed Documentation

### department.proto {#department}

**Path**: `pkg/organization/proto/department.proto` **Package**: `gcommon.v1.organization` **Lines**: 85

**Messages** (1): `Department`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/key_value.proto` → [common](./common.md#key_value)

#### Source Code

```protobuf
// file: pkg/organization/proto/messages/department.proto
edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/common/proto/key_value.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

/**
 * Department message representing an organizational department.
 * Departments provide hierarchical organization structure and
 * can contain teams and individual members.
 */
message Department {
  // Unique department identifier
  string id = 1;

  // Organization identifier
  string organization_id = 2;

  // Department name
  string name = 3;

  // URL-friendly slug for the department
  string slug = 4;

  // Department description or purpose
  string description = 5;

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
  google.protobuf.Timestamp created_at = 11 [lazy = true];

  // Last update timestamp
  google.protobuf.Timestamp updated_at = 12 [lazy = true];

  // User ID who created this department
  string created_by = 13;

  // User ID who last updated this department
  string updated_by = 14;

  // Whether this department is currently active
  bool active = 15;

  // Department's email address for external communications
  string contact_email = 16;

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

### hierarchy_type.proto {#hierarchy_type}

**Path**: `pkg/organization/proto/hierarchy_type.proto` **Package**: `gcommon.v1.organization` **Lines**: 40

**Enums** (1): `HierarchyType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/organization/proto/enums/hierarchy_type.proto
edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

/**
 * Hierarchy type enumeration defining the type of organizational structure.
 * Used to categorize different organizational units and their relationships.
 */
enum HierarchyType {
  // Default value indicating no hierarchy type was specified
  HIERARCHY_TYPE_UNSPECIFIED = 0;

  // Department-based hierarchical structure
  HIERARCHY_TYPE_DEPARTMENT = 1;

  // Team-based organizational structure
  HIERARCHY_TYPE_TEAM = 2;

  // Project-based organizational structure
  HIERARCHY_TYPE_PROJECT = 3;

  // Geographic/location-based structure
  HIERARCHY_TYPE_GEOGRAPHIC = 4;

  // Functional role-based structure
  HIERARCHY_TYPE_FUNCTIONAL = 5;

  // Matrix organizational structure (multi-dimensional)
  HIERARCHY_TYPE_MATRIX = 6;

  // Flat organizational structure (minimal hierarchy)
  HIERARCHY_TYPE_FLAT = 7;
}

```

---

### isolation_level.proto {#isolation_level}

**Path**: `pkg/organization/proto/isolation_level.proto` **Package**: `gcommon.v1.organization` **Lines**: 34

**Enums** (1): `IsolationLevel`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/organization/proto/enums/isolation_level.proto
edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

/**
 * Isolation level enumeration defining the degree of tenant isolation.
 * Used in multi-tenant architectures to control data and resource separation.
 */
enum IsolationLevel {
  // Default value indicating no isolation level was specified
  ISOLATION_LEVEL_UNSPECIFIED = 0;

  // Shared infrastructure with logical separation (lowest cost, shared resources)
  ISOLATION_LEVEL_SHARED = 1;

  // Dedicated database/schema per tenant (medium isolation)
  ISOLATION_LEVEL_DATABASE = 2;

  // Dedicated infrastructure per tenant (highest isolation)
  ISOLATION_LEVEL_INFRASTRUCTURE = 3;

  // Virtual private cloud isolation (network-level separation)
  ISOLATION_LEVEL_NETWORK = 4;

  // Physical server isolation (hardware-level separation)
  ISOLATION_LEVEL_PHYSICAL = 5;
}

```

---

### member_role.proto {#member_role}

**Path**: `pkg/organization/proto/member_role.proto` **Package**: `gcommon.v1.organization` **Lines**: 22

**Enums** (1): `MemberRole`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/organization/proto/member_role.proto
// version: 1.0.0
// guid: b6c7d8e9-012b-467a-1234-789012345678

edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

enum MemberRole {
  MEMBER_ROLE_UNSPECIFIED = 0;
  MEMBER_ROLE_OWNER = 1;
  MEMBER_ROLE_ADMIN = 2;
  MEMBER_ROLE_MEMBER = 3;
  MEMBER_ROLE_VIEWER = 4;
  MEMBER_ROLE_GUEST = 5;
}

```

---

### organization.proto {#organization}

**Path**: `pkg/organization/proto/organization.proto` **Package**: `gcommon.v1.organization` **Lines**: 89

**Messages** (1): `Organization`

**Imports** (4):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/key_value.proto` → [common](./common.md#key_value)
- `pkg/organization/proto/organization_status.proto`

#### Source Code

```protobuf
// file: pkg/organization/proto/organization.proto
// version: 1.0.0
// guid: 67890def-1234-5678-9abc-def012345678

edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/common/proto/key_value.proto";
import "pkg/organization/proto/organization_status.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

/**
 * Organization message representing a complete organizational entity.
 * Contains all core information needed for organization management,
 * including metadata, settings, and administrative information.
 */
message Organization {
  // Unique organization identifier (immutable)
  string id = 1;

  // Organization name (human-readable identifier)
  string name = 2;

  // URL-friendly slug for the organization (e.g., for subdomains)
  string slug = 3;

  // Organization description or mission statement
  string description = 4;

  // Primary website URL for the organization
  string website = 5;

  // Primary contact email for the organization
  string contact_email = 6;

  // Organization's physical address or headquarters location
  string address = 7;

  // Phone number for organization contact
  string phone = 8;

  // Tax identifier or business registration number
  string tax_id = 9;

  // Organization's industry or business sector
  string industry = 10;

  // Current operational status of the organization
  OrganizationStatus status = 11;

  // Organization metadata and custom attributes
  repeated gcommon.v1.common.KeyValue metadata = 12 [lazy = true];

  // Organization creation timestamp (immutable)
  google.protobuf.Timestamp created_at = 13 [lazy = true];

  // Last update timestamp
  google.protobuf.Timestamp updated_at = 14 [lazy = true];

  // User ID who created this organization
  string created_by = 15;

  // User ID who last updated this organization
  string updated_by = 16;

  // Organization's timezone (IANA timezone identifier)
  string timezone = 17;

  // Organization's primary language/locale
  string locale = 18;

  // Maximum number of members allowed in this organization
  int32 max_members = 19;

  // Whether this organization supports multi-tenancy
  bool multi_tenant_enabled = 20;

  // Organization's logo or avatar URL
  string avatar_url = 21;

  // Organization's billing contact email (if different from contact_email)
  string billing_email = 22;
}

```

---

### organization_hierarchy.proto {#organization_hierarchy}

**Path**: `pkg/organization/proto/organization_hierarchy.proto` **Package**: `gcommon.v1.organization` **Lines**: 119

**Messages** (3): `OrganizationHierarchy`, `HierarchyNode`, `HierarchyPath`

**Imports** (4):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/key_value.proto` → [common](./common.md#key_value)
- `pkg/organization/proto/hierarchy_type.proto`

#### Source Code

```protobuf
// file: pkg/organization/proto/organization_hierarchy.proto
// version: 1.0.0
// guid: 78901abc-2345-6789-abcd-ef0123456789

edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/common/proto/key_value.proto";
import "pkg/organization/proto/hierarchy_type.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

/**
 * OrganizationHierarchy message representing the hierarchical structure of an organization.
 * Defines parent-child relationships between organizational units and supports
 * multiple hierarchy types (department, team, project, geographic, etc.).
 */
message OrganizationHierarchy {
  // Unique hierarchy identifier
  string id = 1;

  // Organization identifier
  string organization_id = 2;

  // Type of hierarchy structure
  HierarchyType hierarchy_type = 3;

  // Name of this hierarchy configuration
  string name = 4;

  // Description of this hierarchy structure
  string description = 5;

  // Root node of the hierarchy (typically the organization itself)
  HierarchyNode root_node = 6;

  // Whether this hierarchy is currently active/primary
  bool active = 7;

  // Hierarchy metadata and configuration
  repeated gcommon.v1.common.KeyValue metadata = 8 [lazy = true];

  // Hierarchy creation timestamp
  google.protobuf.Timestamp created_at = 9 [lazy = true];

  // Last update timestamp
  google.protobuf.Timestamp updated_at = 10 [lazy = true];

  // User ID who created this hierarchy
  string created_by = 11;

  // User ID who last updated this hierarchy
  string updated_by = 12;
}

/**
 * HierarchyNode message representing a single node in the organizational hierarchy.
 * Can represent departments, teams, projects, or any other organizational unit.
 */
message HierarchyNode {
  // Unique node identifier
  string id = 1;

  // Node name
  string name = 2;

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

/**
 * HierarchyPath message representing a complete path in the organizational hierarchy.
 * Used for efficient hierarchy traversal and relationship queries.
 */
message HierarchyPath {
  // Descendant node ID
  string descendant_id = 1;

  // Ancestor node ID
  string ancestor_id = 2;

  // Distance between ancestor and descendant (1 = direct parent-child)
  int32 distance = 3;

  // Complete path from ancestor to descendant
  repeated string path_nodes = 4;
}

```

---

### organization_member.proto {#organization_member}

**Path**: `pkg/organization/proto/organization_member.proto` **Package**: `gcommon.v1.organization` **Lines**: 91

**Messages** (1): `OrganizationMember`

**Imports** (4):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/key_value.proto` → [common](./common.md#key_value)
- `pkg/organization/proto/member_role.proto`

#### Source Code

```protobuf
// file: pkg/organization/proto/messages/organization_member.proto
edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/common/proto/key_value.proto";
import "pkg/organization/proto/member_role.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

/**
 * OrganizationMember message representing a user's membership in an organization.
 * Contains role information, permissions, and membership metadata.
 */
message OrganizationMember {
  // Unique membership identifier
  string id = 1;

  // Organization identifier
  string organization_id = 2;

  // User identifier from the auth system
  string user_id = 3;

  // User's email address (cached for quick access)
  string email = 4;

  // User's display name (cached for quick access)
  string display_name = 5;

  // Primary role of the user in this organization
  MemberRole role = 6;

  // Additional roles the user may have
  repeated MemberRole additional_roles = 7;

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
  google.protobuf.Timestamp created_at = 13 [lazy = true];

  // Last update timestamp
  google.protobuf.Timestamp updated_at = 14 [lazy = true];

  // Last activity timestamp (when user was last active in organization)
  google.protobuf.Timestamp last_active_at = 15 [lazy = true];

  // User ID who added this member to the organization
  string invited_by = 16;

  // User ID who last updated this member's information
  string updated_by = 17;

  // Whether this member is currently active
  bool active = 18;

  // Member's job title within the organization
  string job_title = 19;

  // Member's manager's user ID (if applicable)
  string manager_id = 20;

  // Member's direct reports' user IDs
  repeated string direct_report_ids = 21;

  // Member's avatar/profile picture URL
  string avatar_url = 22;

  // Member's phone number (organization context)
  string phone = 23;

  // Member's office location or workspace
  string location = 24;
}

```

---

### organization_status.proto {#organization_status}

**Path**: `pkg/organization/proto/organization_status.proto` **Package**: `gcommon.v1.organization` **Lines**: 37

**Enums** (1): `OrganizationStatus`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/organization/proto/enums/organization_status.proto
edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

/**
 * Organization status enumeration defining the state of an organization.
 * Used to track organization lifecycle, operational status, and access permissions.
 */
enum OrganizationStatus {
  // Default value indicating no status was specified
  ORGANIZATION_STATUS_UNSPECIFIED = 0;

  // Organization is active and operational
  ORGANIZATION_STATUS_ACTIVE = 1;

  // Organization is inactive (temporarily suspended operations)
  ORGANIZATION_STATUS_INACTIVE = 2;

  // Organization is suspended due to policy violations or billing issues
  ORGANIZATION_STATUS_SUSPENDED = 3;

  // Organization is pending verification or onboarding completion
  ORGANIZATION_STATUS_PENDING = 4;

  // Organization is archived (read-only access, no new operations)
  ORGANIZATION_STATUS_ARCHIVED = 5;

  // Organization is marked for deletion and undergoing cleanup
  ORGANIZATION_STATUS_DELETED = 6;
}

```

---

### team.proto {#team}

**Path**: `pkg/organization/proto/team.proto` **Package**: `gcommon.v1.organization` **Lines**: 94

**Messages** (1): `Team`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/key_value.proto` → [common](./common.md#key_value)

#### Source Code

```protobuf
// file: pkg/organization/proto/messages/team.proto
edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/common/proto/key_value.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

/**
 * Team message representing a team within an organization or department.
 * Teams are smaller organizational units focused on specific projects,
 * functions, or objectives.
 */
message Team {
  // Unique team identifier
  string id = 1;

  // Organization identifier
  string organization_id = 2;

  // Department identifier (teams can belong to departments)
  string department_id = 3;

  // Team name
  string name = 4;

  // URL-friendly slug for the team
  string slug = 5;

  // Team description or purpose
  string description = 6;

  // Team lead/manager user ID
  string lead_id = 7;

  // Team type or category (e.g., "engineering", "marketing", "sales")
  string team_type = 8;

  // Team's primary focus area or mission
  string focus_area = 9;

  // Team metadata and custom attributes
  repeated gcommon.v1.common.KeyValue metadata = 10 [lazy = true];

  // Team creation timestamp
  google.protobuf.Timestamp created_at = 11 [lazy = true];

  // Last update timestamp
  google.protobuf.Timestamp updated_at = 12 [lazy = true];

  // User ID who created this team
  string created_by = 13;

  // User ID who last updated this team
  string updated_by = 14;

  // Whether this team is currently active
  bool active = 15;

  // Team's email address for external communications
  string contact_email = 16;

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

**Path**: `pkg/organization/proto/tenant.proto` **Package**: `gcommon.v1.organization` **Lines**: 82

**Messages** (1): `Tenant`

**Imports** (6):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/key_value.proto` → [common](./common.md#key_value)
- `pkg/organization/proto/isolation_level.proto` → [database](./database.md#isolation_level)
- `pkg/organization/proto/tenant_quota.proto`
- `pkg/organization/proto/tenant_status.proto`

#### Source Code

```protobuf
// file: pkg/organization/proto/messages/tenant.proto
edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/common/proto/key_value.proto";
import "pkg/organization/proto/isolation_level.proto";
import "pkg/organization/proto/tenant_quota.proto";
import "pkg/organization/proto/tenant_status.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

/**
 * Tenant message representing a tenant within an organization.
 * Supports multi-tenant architecture with configurable isolation levels,
 * resource quotas, and tenant-specific settings.
 */
message Tenant {
  // Unique tenant identifier (immutable)
  string id = 1;

  // Parent organization identifier
  string organization_id = 2;

  // Tenant name (human-readable identifier)
  string name = 3;

  // URL-friendly slug for the tenant (e.g., for subdomains)
  string slug = 4;

  // Tenant description
  string description = 5;

  // Current status of the tenant
  TenantStatus status = 6;

  // Isolation level for this tenant
  IsolationLevel isolation_level = 7;

  // Tenant metadata and custom attributes
  repeated gcommon.v1.common.KeyValue metadata = 8 [lazy = true];

  // Tenant creation timestamp (immutable)
  google.protobuf.Timestamp created_at = 9 [lazy = true];

  // Last update timestamp
  google.protobuf.Timestamp updated_at = 10 [lazy = true];

  // User ID who created this tenant
  string created_by = 11;

  // User ID who last updated this tenant
  string updated_by = 12;

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

**Path**: `pkg/organization/proto/tenant_isolation.proto` **Package**: `gcommon.v1.organization` **Lines**: 590

**Messages** (30): `TenantIsolation`, `DatabaseIsolation`, `NetworkIsolation`, `StorageIsolation`, `ComputeIsolation`, `EncryptionConfig`, `AccessControl`, `AuditConfig`, `BackupConfig`, `NetworkACLRule`, `LoadBalancerConfig`, `CDNConfig`,
`DomainConfig`, `StorageEncryption`, `StoragePolicy`, `StorageBackupConfig`, `StorageQuota`, `CPUAllocation`, `MemoryAllocation`, `ResourceLimits`, `AutoScalingConfig`, `TimeRestriction`, `AuditAlert`, `HealthCheckConfig`, `SSLConfig`,
`CacheBehavior`, `OriginConfig`, `DNSConfig`, `DNSRecord`, `CacheKeyPolicy`

**Imports** (4):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/key_value.proto` → [common](./common.md#key_value)
- `pkg/organization/proto/isolation_level.proto` → [database](./database.md#isolation_level)

#### Source Code

```protobuf
// file: pkg/organization/proto/types/tenant_isolation.proto
edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/common/proto/key_value.proto";
import "pkg/organization/proto/isolation_level.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

/**
 * TenantIsolation type defining the isolation configuration for a tenant.
 * Specifies how tenant data and resources are separated from other tenants.
 */
message TenantIsolation {
  // Tenant identifier
  string tenant_id = 1;

  // Isolation level for this tenant
  IsolationLevel level = 2;

  // Database isolation configuration
  DatabaseIsolation database = 3;

  // Network isolation configuration
  NetworkIsolation network = 4;

  // Storage isolation configuration
  StorageIsolation storage = 5;

  // Compute isolation configuration
  ComputeIsolation compute = 6;

  // Encryption configuration for tenant data
  EncryptionConfig encryption = 7;

  // Access control configuration
  AccessControl access_control = 8;

  // Audit and compliance configuration
  AuditConfig audit = 9;

  // Isolation metadata and custom settings
  repeated gcommon.v1.common.KeyValue metadata = 10 [lazy = true];

  // Isolation configuration creation timestamp
  google.protobuf.Timestamp created_at = 11 [lazy = true];

  // Last update timestamp
  google.protobuf.Timestamp updated_at = 12 [lazy = true];

  // User ID who configured this isolation
  string configured_by = 13;
}

/**
 * DatabaseIsolation type defining database-level isolation for a tenant.
 */
message DatabaseIsolation {
  // Database instance identifier (for INFRASTRUCTURE isolation)
  string database_instance = 1;

  // Schema or database name for this tenant
  string schema_name = 2;

  // Database connection parameters
  repeated gcommon.v1.common.KeyValue connection_params = 3 [lazy = true];

  // Whether tenant has dedicated database
  bool dedicated_database = 4;

  // Database backup configuration
  BackupConfig backup = 5;

  // Database access restrictions
  repeated string allowed_operations = 6;

  // Maximum connections allowed for this tenant
  int32 max_connections = 7;

  // Query timeout in seconds
  int32 query_timeout_seconds = 8;
}

/**
 * NetworkIsolation type defining network-level isolation for a tenant.
 */
message NetworkIsolation {
  // Virtual private cloud (VPC) identifier
  string vpc_id = 1;

  // Subnet identifier for this tenant
  string subnet_id = 2;

  // Security group identifiers
  repeated string security_group_ids = 3;

  // Network access control list (ACL) rules
  repeated NetworkACLRule acl_rules = 4;

  // Whether tenant has dedicated network
  bool dedicated_network = 5;

  // Load balancer configuration for this tenant
  LoadBalancerConfig load_balancer = 6;

  // CDN configuration for this tenant
  CDNConfig cdn = 7;

  // Custom domain configuration
  DomainConfig domain = 8;
}

/**
 * StorageIsolation type defining storage-level isolation for a tenant.
 */
message StorageIsolation {
  // Storage bucket or container identifier
  string storage_bucket = 1;

  // Storage path prefix for this tenant
  string path_prefix = 2;

  // Whether tenant has dedicated storage
  bool dedicated_storage = 3;

  // Storage encryption configuration
  StorageEncryption encryption = 4;

  // Storage access policies
  repeated StoragePolicy policies = 5;

  // Backup and replication configuration
  StorageBackupConfig backup = 6;

  // Storage quota limits
  StorageQuota quota = 7;
}

/**
 * ComputeIsolation type defining compute-level isolation for a tenant.
 */
message ComputeIsolation {
  // Dedicated compute instance identifier
  string compute_instance = 1;

  // Container or namespace identifier
  string namespace = 2;

  // CPU allocation for this tenant
  CPUAllocation cpu = 3;

  // Memory allocation for this tenant
  MemoryAllocation memory = 4;

  // Whether tenant has dedicated compute resources
  bool dedicated_compute = 5;

  // Resource limits and quotas
  ResourceLimits limits = 6;

  // Auto-scaling configuration
  AutoScalingConfig auto_scaling = 7;
}

/**
 * Supporting message types for isolation configuration.
 */
message EncryptionConfig {
  // Whether encryption at rest is enabled
  bool encryption_at_rest = 1;

  // Whether encryption in transit is enabled
  bool encryption_in_transit = 2;

  // Encryption key management service
  string key_management_service = 3;

  // Customer-managed encryption key ID
  string customer_key_id = 4;

  // Encryption algorithm used
  string encryption_algorithm = 5;
}

message AccessControl {
  // IP address whitelist for tenant access
  repeated string ip_whitelist = 1;

  // Allowed authentication methods
  repeated string auth_methods = 2;

  // Session timeout in minutes
  int32 session_timeout = 3;

  // Maximum concurrent sessions
  int32 max_concurrent_sessions = 4;

  // Geographic access restrictions
  repeated string allowed_countries = 5;

  // Time-based access restrictions
  repeated TimeRestriction time_restrictions = 6;
}

message AuditConfig {
  // Whether audit logging is enabled
  bool audit_enabled = 1;

  // Audit log retention period in days
  int32 retention_days = 2;

  // Audit log storage location
  string storage_location = 3;

  // Events to audit
  repeated string audited_events = 4;

  // Whether real-time monitoring is enabled
  bool real_time_monitoring = 5;

  // Alert configuration for audit events
  repeated AuditAlert alerts = 6;
}

message BackupConfig {
  // Whether automated backups are enabled
  bool enabled = 1;

  // Backup frequency (hourly, daily, weekly)
  string frequency = 2;

  // Backup retention period in days
  int32 retention_days = 3;

  // Backup storage location
  string storage_location = 4;

  // Whether point-in-time recovery is enabled
  bool point_in_time_recovery = 5;
}

message NetworkACLRule {
  // Rule action (allow, deny)
  string action = 1;

  // Source IP or CIDR block
  string source = 2;

  // Destination IP or CIDR block
  string destination = 3;

  // Protocol (TCP, UDP, ICMP)
  string protocol = 4;

  // Port range
  string port_range = 5;

  // Rule priority
  int32 priority = 6;
}

message LoadBalancerConfig {
  // Load balancer type (application, network)
  string type = 1;

  // Load balancing algorithm
  string algorithm = 2;

  // Health check configuration
  HealthCheckConfig health_check = 3;

  // SSL/TLS configuration
  SSLConfig ssl = 4;
}

message CDNConfig {
  // CDN provider
  string provider = 1;

  // CDN distribution ID
  string distribution_id = 2;

  // Cache behavior settings
  repeated CacheBehavior cache_behaviors = 3;

  // Origin configuration
  OriginConfig origin = 4;
}

message DomainConfig {
  // Custom domain name
  string domain_name = 1;

  // SSL certificate ARN or ID
  string ssl_certificate = 2;

  // DNS configuration
  DNSConfig dns = 3;

  // Domain validation status
  string validation_status = 4;
}

message StorageEncryption {
  // Encryption type (AES256, KMS)
  string type = 1;

  // Key ID for KMS encryption
  string key_id = 2;

  // Whether server-side encryption is enabled
  bool server_side = 3;

  // Whether client-side encryption is enabled
  bool client_side = 4;
}

message StoragePolicy {
  // Policy name
  string name = 1;

  // Policy statement (JSON)
  string statement = 2;

  // Policy effect (Allow, Deny)
  string effect = 3;

  // Resources covered by this policy
  repeated string resources = 4;

  // Actions covered by this policy
  repeated string actions = 5;
}

message StorageBackupConfig {
  // Whether backup is enabled
  bool enabled = 1;

  // Backup schedule (cron expression)
  string schedule = 2;

  // Backup retention period
  int32 retention_days = 3;

  // Cross-region backup enabled
  bool cross_region = 4;

  // Backup encryption enabled
  bool encryption_enabled = 5;
}

message StorageQuota {
  // Maximum storage size in bytes
  int64 max_size_bytes = 1;

  // Maximum number of objects
  int64 max_objects = 2;

  // Maximum request rate per second
  int32 max_requests_per_second = 3;

  // Transfer quota in bytes per month
  int64 transfer_quota_bytes = 4;
}

message CPUAllocation {
  // Number of CPU cores
  int32 cores = 1;

  // CPU frequency in MHz
  int32 frequency_mhz = 2;

  // CPU usage limit percentage
  int32 usage_limit_percent = 3;

  // CPU priority
  int32 priority = 4;
}

message MemoryAllocation {
  // Memory size in MB
  int64 size_mb = 1;

  // Memory usage limit percentage
  int32 usage_limit_percent = 2;

  // Swap allocation in MB
  int64 swap_mb = 3;
}

message ResourceLimits {
  // Maximum CPU usage percentage
  int32 max_cpu_percent = 1;

  // Maximum memory usage in MB
  int64 max_memory_mb = 2;

  // Maximum disk I/O operations per second
  int32 max_disk_iops = 3;

  // Maximum network bandwidth in Mbps
  int32 max_network_mbps = 4;

  // Maximum number of processes
  int32 max_processes = 5;

  // Maximum number of file descriptors
  int32 max_file_descriptors = 6;
}

message AutoScalingConfig {
  // Whether auto-scaling is enabled
  bool enabled = 1;

  // Minimum number of instances
  int32 min_instances = 2;

  // Maximum number of instances
  int32 max_instances = 3;

  // Target CPU utilization percentage
  int32 target_cpu_percent = 4;

  // Target memory utilization percentage
  int32 target_memory_percent = 5;

  // Scale-up cooldown period in seconds
  int32 scale_up_cooldown = 6;

  // Scale-down cooldown period in seconds
  int32 scale_down_cooldown = 7;
}

message TimeRestriction {
  // Day of week (0-6, 0=Sunday)
  int32 day_of_week = 1;

  // Start time (24-hour format, e.g., "09:00")
  string start_time = 2;

  // End time (24-hour format, e.g., "17:00")
  string end_time = 3;

  // Timezone for this restriction
  string timezone = 4;
}

message AuditAlert {
  // Alert name
  string name = 1;

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

message HealthCheckConfig {
  // Health check path
  string path = 1;

  // Health check port
  int32 port = 2;

  // Health check protocol (HTTP, HTTPS, TCP)
  string protocol = 3;

  // Health check interval in seconds
  int32 interval_seconds = 4;

  // Health check timeout in seconds
  int32 timeout_seconds = 5;

  // Healthy threshold
  int32 healthy_threshold = 6;

  // Unhealthy threshold
  int32 unhealthy_threshold = 7;
}

message SSLConfig {
  // SSL certificate ARN or ID
  string certificate_id = 1;

  // SSL policy
  string ssl_policy = 2;

  // Whether to redirect HTTP to HTTPS
  bool redirect_http = 3;

  // Minimum TLS version
  string min_tls_version = 4;
}

message CacheBehavior {
  // Path pattern for this behavior
  string path_pattern = 1;

  // Cache TTL in seconds
  int64 ttl_seconds = 2;

  // Whether to compress objects
  bool compress = 3;

  // Allowed HTTP methods
  repeated string allowed_methods = 4;

  // Cache key policy
  CacheKeyPolicy cache_key = 5;
}

message OriginConfig {
  // Origin domain name
  string domain_name = 1;

  // Origin path
  string origin_path = 2;

  // Origin protocol policy
  string protocol_policy = 3;

  // Custom headers to send to origin
  repeated gcommon.v1.common.KeyValue custom_headers = 4;
}

message DNSConfig {
  // DNS provider
  string provider = 1;

  // DNS zone ID
  string zone_id = 2;

  // DNS records
  repeated DNSRecord records = 3;

  // TTL for DNS records
  int32 ttl = 4;
}

message DNSRecord {
  // Record type (A, CNAME, TXT, etc.)
  string type = 1;

  // Record name
  string name = 2;

  // Record value
  string value = 3;

  // Record TTL
  int32 ttl = 4;

  // Record priority (for MX records)
  int32 priority = 5;
}

message CacheKeyPolicy {
  // Whether to include query strings in cache key
  bool include_query_strings = 1;

  // Query string whitelist
  repeated string query_string_whitelist = 2;

  // Whether to include headers in cache key
  bool include_headers = 3;

  // Header whitelist
  repeated string header_whitelist = 4;

  // Whether to include cookies in cache key
  bool include_cookies = 5;

  // Cookie whitelist
  repeated string cookie_whitelist = 6;
}

```

---

### tenant_quota.proto {#tenant_quota}

**Path**: `pkg/organization/proto/tenant_quota.proto` **Package**: `gcommon.v1.organization` **Lines**: 41

**Messages** (1): `TenantQuota`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/organization/proto/tenant_quota.proto
// Tenant quota message definition

edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

/**
 * TenantQuota defines resource limits and quotas for a tenant.
 */
message TenantQuota {
  // Tenant ID this quota applies to
  string tenant_id = 1;

  // Maximum number of users
  int32 max_users = 2;

  // Maximum storage in bytes
  int64 max_storage_bytes = 3;

  // Maximum API requests per hour
  int32 max_api_requests_per_hour = 4;

  // Maximum number of projects
  int32 max_projects = 5;

  // Maximum bandwidth in bytes per month
  int64 max_bandwidth_bytes_per_month = 6;

  // Whether the tenant can create sub-tenants
  bool can_create_sub_tenants = 7;

  // Custom quota attributes
  map<string, string> custom_quotas = 8;
}

```

---

### tenant_status.proto {#tenant_status}

**Path**: `pkg/organization/proto/tenant_status.proto` **Package**: `gcommon.v1.organization` **Lines**: 43

**Enums** (1): `TenantStatus`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/organization/proto/enums/tenant_status.proto
edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

/**
 * Tenant status enumeration defining the state of a tenant within an organization.
 * Used for multi-tenant architecture to control tenant access and operations.
 */
enum TenantStatus {
  // Default value indicating no status was specified
  TENANT_STATUS_UNSPECIFIED = 0;

  // Tenant is active and operational
  TENANT_STATUS_ACTIVE = 1;

  // Tenant is inactive (temporarily disabled)
  TENANT_STATUS_INACTIVE = 2;

  // Tenant is suspended due to policy violations or resource limits
  TENANT_STATUS_SUSPENDED = 3;

  // Tenant is pending setup or verification
  TENANT_STATUS_PENDING = 4;

  // Tenant has exceeded resource quotas and is throttled
  TENANT_STATUS_QUOTA_EXCEEDED = 5;

  // Tenant is in trial period with limited features
  TENANT_STATUS_TRIAL = 6;

  // Tenant is archived (read-only access)
  TENANT_STATUS_ARCHIVED = 7;

  // Tenant is marked for deletion
  TENANT_STATUS_DELETED = 8;
}

```

---
