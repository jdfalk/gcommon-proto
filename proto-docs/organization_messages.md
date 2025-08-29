# Organization Messages Documentation

[← Back to Index](./README.md)

## Module Overview

- **Proto Files**: 114
- **Messages**: 114

## Table of Contents

### Messages

- [`AddMemberRequest`](#add_member_request) - from add_member_request.proto
- [`AddMemberResponse`](#add_member_response) - from add_member_response.proto
- [`AuditAlert`](#audit_alert) - from audit_alert.proto
- [`AuditConfig`](#audit_config) - from audit_config.proto
- [`AutoScalingConfig`](#auto_scaling_config) - from auto_scaling_config.proto
- [`BillingSettings`](#billing_settings) - from billing_settings.proto
- [`CDNConfig`](#cdn_config) - from cdn_config.proto
- [`CPUAllocation`](#cpu_allocation) - from cpu_allocation.proto
- [`CacheBehavior`](#cache_behavior) - from cache_behavior.proto
- [`CacheKeyPolicy`](#cache_key_policy) - from cache_key_policy.proto
- [`ComputeIsolation`](#compute_isolation) - from compute_isolation.proto
- [`ConfigureTenantIsolationRequest`](#configure_tenant_isolation_request) - from configure_tenant_isolation_request.proto
- [`ConfigureTenantIsolationResponse`](#configure_tenant_isolation_response) - from configure_tenant_isolation_response.proto
- [`CreateDepartmentRequest`](#create_department_request) - from create_department_request.proto
- [`CreateDepartmentResponse`](#create_department_response) - from create_department_response.proto
- [`CreateOrganizationRequest`](#create_organization_request) - from create_organization_request.proto
- [`CreateOrganizationResponse`](#create_organization_response) - from create_organization_response.proto
- [`CreateTeamRequest`](#create_team_request) - from create_team_request.proto
- [`CreateTeamResponse`](#create_team_response) - from create_team_response.proto
- [`CreateTenantRequest`](#create_tenant_request) - from create_tenant_request.proto
- [`CreateTenantResponse`](#create_tenant_response) - from create_tenant_response.proto
- [`DNSConfig`](#dns_config) - from dns_config.proto
- [`DNSRecord`](#dns_record) - from dns_record.proto
- [`DatabaseIsolation`](#database_isolation) - from database_isolation.proto
- [`DeleteDepartmentRequest`](#delete_department_request) - from delete_department_request.proto
- [`DeleteDepartmentResponse`](#delete_department_response) - from delete_department_response.proto
- [`DeleteOrganizationRequest`](#delete_organization_request) - from delete_organization_request.proto
- [`DeleteOrganizationResponse`](#delete_organization_response) - from delete_organization_response.proto
- [`DeleteTeamRequest`](#delete_team_request) - from delete_team_request.proto
- [`DeleteTeamResponse`](#delete_team_response) - from delete_team_response.proto
- [`DeleteTenantRequest`](#delete_tenant_request) - from delete_tenant_request.proto
- [`DeleteTenantResponse`](#delete_tenant_response) - from delete_tenant_response.proto
- [`Department`](#department) - from department.proto
- [`DomainConfig`](#domain_config) - from domain_config.proto
- [`EmailTemplate`](#email_template) - from email_template.proto
- [`FeatureFlag`](#feature_flag) - from feature_flag.proto
- [`GetDepartmentRequest`](#get_department_request) - from get_department_request.proto
- [`GetDepartmentResponse`](#get_department_response) - from get_department_response.proto
- [`GetHierarchyRequest`](#get_hierarchy_request) - from get_hierarchy_request.proto
- [`GetHierarchyResponse`](#get_hierarchy_response) - from get_hierarchy_response.proto
- [`GetOrganizationRequest`](#get_organization_request) - from get_organization_request.proto
- [`GetOrganizationResponse`](#get_organization_response) - from get_organization_response.proto
- [`GetOrganizationSettingsRequest`](#get_organization_settings_request) - from get_organization_settings_request.proto
- [`GetOrganizationSettingsResponse`](#get_organization_settings_response) - from get_organization_settings_response.proto
- [`GetTeamRequest`](#get_team_request) - from get_team_request.proto
- [`GetTeamResponse`](#get_team_response) - from get_team_response.proto
- [`GetTenantIsolationRequest`](#get_tenant_isolation_request) - from get_tenant_isolation_request.proto
- [`GetTenantIsolationResponse`](#get_tenant_isolation_response) - from get_tenant_isolation_response.proto
- [`GetTenantRequest`](#get_tenant_request) - from get_tenant_request.proto
- [`GetTenantResponse`](#get_tenant_response) - from get_tenant_response.proto
- [`GetTenantUsageRequest`](#get_tenant_usage_request) - from get_tenant_usage_request.proto
- [`GetTenantUsageResponse`](#get_tenant_usage_response) - from get_tenant_usage_response.proto
- [`HierarchyNode`](#hierarchy_node) - from hierarchy_node.proto
- [`HierarchyPath`](#hierarchy_path) - from hierarchy_path.proto
- [`Integration`](#integration) - from integration.proto
- [`IntegrationSettings`](#integration_settings) - from integration_settings.proto
- [`ListDepartmentsRequest`](#list_departments_request) - from list_departments_request.proto
- [`ListDepartmentsResponse`](#list_departments_response) - from list_departments_response.proto
- [`ListMembersRequest`](#list_members_request) - from list_members_request.proto
- [`ListMembersResponse`](#list_members_response) - from list_members_response.proto
- [`ListOrganizationsRequest`](#list_organizations_request) - from list_organizations_request.proto
- [`ListOrganizationsResponse`](#list_organizations_response) - from list_organizations_response.proto
- [`ListTeamsRequest`](#list_teams_request) - from list_teams_request.proto
- [`ListTeamsResponse`](#list_teams_response) - from list_teams_response.proto
- [`ListTenantsRequest`](#list_tenants_request) - from list_tenants_request.proto
- [`ListTenantsResponse`](#list_tenants_response) - from list_tenants_response.proto
- [`MemoryAllocation`](#memory_allocation) - from memory_allocation.proto
- [`NetworkACLRule`](#network_acl_rule) - from network_acl_rule.proto
- [`NetworkIsolation`](#network_isolation) - from network_isolation.proto
- [`NotificationFrequency`](#notification_frequency) - from notification_frequency.proto
- [`OAuthAppConfig`](#o_auth_app_config) - from o_auth_app_config.proto
- [`Organization`](#organization) - from organization.proto
- [`OrganizationAPIKeyConfig`](#api_key_config) - from api_key_config.proto
- [`OrganizationBackupConfig`](#backup_config) - from backup_config.proto
- [`OrganizationEncryptionConfig`](#encryption_config) - from encryption_config.proto
- [`OrganizationHealthCheckConfig`](#health_check_config) - from health_check_config.proto
- [`OrganizationHierarchy`](#organization_hierarchy) - from organization_hierarchy.proto
- [`OrganizationLoadBalancerConfig`](#load_balancer_config) - from load_balancer_config.proto
- [`OrganizationMember`](#organization_member) - from organization_member.proto
- [`OrganizationRateLimitConfig`](#rate_limit_config) - from rate_limit_config.proto
- [`OrganizationSettings`](#organization_settings) - from organization_settings.proto
- [`OriginConfig`](#origin_config) - from origin_config.proto
- [`RemoveMemberRequest`](#remove_member_request) - from remove_member_request.proto
- [`RemoveMemberResponse`](#remove_member_response) - from remove_member_response.proto
- [`SSLConfig`](#ssl_config) - from ssl_config.proto
- [`SecuritySettings`](#security_settings) - from security_settings.proto
- [`StorageBackupConfig`](#storage_backup_config) - from storage_backup_config.proto
- [`StorageEncryption`](#storage_encryption) - from storage_encryption.proto
- [`StorageIsolation`](#storage_isolation) - from storage_isolation.proto
- [`StoragePolicy`](#storage_policy) - from storage_policy.proto
- [`StorageQuota`](#storage_quota) - from storage_quota.proto
- [`Team`](#team) - from team.proto
- [`Tenant`](#tenant) - from tenant.proto
- [`TenantIsolation`](#tenant_isolation) - from tenant_isolation.proto
- [`TenantQuota`](#tenant_quota) - from tenant_quota.proto
- [`TimeRestriction`](#time_restriction) - from time_restriction.proto
- [`UISettings`](#ui_settings) - from ui_settings.proto
- [`UpdateDepartmentRequest`](#update_department_request) - from update_department_request.proto
- [`UpdateDepartmentResponse`](#update_department_response) - from update_department_response.proto
- [`UpdateHierarchyRequest`](#update_hierarchy_request) - from update_hierarchy_request.proto
- [`UpdateHierarchyResponse`](#update_hierarchy_response) - from update_hierarchy_response.proto
- [`UpdateMemberRequest`](#update_member_request) - from update_member_request.proto
- [`UpdateMemberResponse`](#update_member_response) - from update_member_response.proto
- [`UpdateOrganizationRequest`](#update_organization_request) - from update_organization_request.proto
- [`UpdateOrganizationResponse`](#update_organization_response) - from update_organization_response.proto
- [`UpdateOrganizationSettingsRequest`](#update_organization_settings_request) - from update_organization_settings_request.proto
- [`UpdateOrganizationSettingsResponse`](#update_organization_settings_response) - from update_organization_settings_response.proto
- [`UpdateTeamRequest`](#update_team_request) - from update_team_request.proto
- [`UpdateTeamResponse`](#update_team_response) - from update_team_response.proto
- [`UpdateTenantQuotaRequest`](#update_tenant_quota_request) - from update_tenant_quota_request.proto
- [`UpdateTenantQuotaResponse`](#update_tenant_quota_response) - from update_tenant_quota_response.proto
- [`UpdateTenantRequest`](#update_tenant_request) - from update_tenant_request.proto
- [`UpdateTenantResponse`](#update_tenant_response) - from update_tenant_response.proto
- [`WebhookConfig`](#webhook_config) - from webhook_config.proto

### Files in this Module

- [add_member_request.proto](#add_member_request)
- [add_member_response.proto](#add_member_response)
- [create_department_request.proto](#create_department_request)
- [create_department_response.proto](#create_department_response)
- [create_organization_request.proto](#create_organization_request)
- [create_organization_response.proto](#create_organization_response)
- [create_team_request.proto](#create_team_request)
- [create_team_response.proto](#create_team_response)
- [create_tenant_request.proto](#create_tenant_request)
- [create_tenant_response.proto](#create_tenant_response)
- [delete_department_request.proto](#delete_department_request)
- [delete_department_response.proto](#delete_department_response)
- [delete_organization_request.proto](#delete_organization_request)
- [delete_organization_response.proto](#delete_organization_response)
- [delete_team_request.proto](#delete_team_request)
- [delete_team_response.proto](#delete_team_response)
- [delete_tenant_request.proto](#delete_tenant_request)
- [delete_tenant_response.proto](#delete_tenant_response)
- [get_department_request.proto](#get_department_request)
- [get_department_response.proto](#get_department_response)
- [get_hierarchy_request.proto](#get_hierarchy_request)
- [get_hierarchy_response.proto](#get_hierarchy_response)
- [get_organization_request.proto](#get_organization_request)
- [get_organization_response.proto](#get_organization_response)
- [get_organization_settings_request.proto](#get_organization_settings_request)
- [get_organization_settings_response.proto](#get_organization_settings_response)
- [get_team_request.proto](#get_team_request)
- [get_team_response.proto](#get_team_response)
- [get_tenant_isolation_request.proto](#get_tenant_isolation_request)
- [get_tenant_isolation_response.proto](#get_tenant_isolation_response)
- [get_tenant_request.proto](#get_tenant_request)
- [get_tenant_response.proto](#get_tenant_response)
- [get_tenant_usage_request.proto](#get_tenant_usage_request)
- [get_tenant_usage_response.proto](#get_tenant_usage_response)
- [list_departments_request.proto](#list_departments_request)
- [list_departments_response.proto](#list_departments_response)
- [list_members_request.proto](#list_members_request)
- [list_members_response.proto](#list_members_response)
- [list_organizations_request.proto](#list_organizations_request)
- [list_organizations_response.proto](#list_organizations_response)
- [list_teams_request.proto](#list_teams_request)
- [list_teams_response.proto](#list_teams_response)
- [list_tenants_request.proto](#list_tenants_request)
- [list_tenants_response.proto](#list_tenants_response)
- [remove_member_request.proto](#remove_member_request)
- [remove_member_response.proto](#remove_member_response)
- [update_department_request.proto](#update_department_request)
- [update_department_response.proto](#update_department_response)
- [update_hierarchy_request.proto](#update_hierarchy_request)
- [update_hierarchy_response.proto](#update_hierarchy_response)
- [update_member_request.proto](#update_member_request)
- [update_member_response.proto](#update_member_response)
- [update_organization_request.proto](#update_organization_request)
- [update_organization_response.proto](#update_organization_response)
- [update_organization_settings_request.proto](#update_organization_settings_request)
- [update_organization_settings_response.proto](#update_organization_settings_response)
- [update_team_request.proto](#update_team_request)
- [update_team_response.proto](#update_team_response)
- [update_tenant_quota_request.proto](#update_tenant_quota_request)
- [update_tenant_quota_response.proto](#update_tenant_quota_response)
- [update_tenant_request.proto](#update_tenant_request)
- [update_tenant_response.proto](#update_tenant_response)
- [api_key_config.proto](#api_key_config)
- [audit_config.proto](#audit_config)
- [auto_scaling_config.proto](#auto_scaling_config)
- [backup_config.proto](#backup_config)
- [cdn_config.proto](#cdn_config)
- [configure_tenant_isolation_request.proto](#configure_tenant_isolation_request)
- [configure_tenant_isolation_response.proto](#configure_tenant_isolation_response)
- [dns_config.proto](#dns_config)
- [domain_config.proto](#domain_config)
- [encryption_config.proto](#encryption_config)
- [health_check_config.proto](#health_check_config)
- [load_balancer_config.proto](#load_balancer_config)
- [o_auth_app_config.proto](#o_auth_app_config)
- [origin_config.proto](#origin_config)
- [rate_limit_config.proto](#rate_limit_config)
- [ssl_config.proto](#ssl_config)
- [storage_backup_config.proto](#storage_backup_config)
- [webhook_config.proto](#webhook_config)
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


## Messages Documentation

### add_member_request.proto {#add_member_request}

**Path**: `gcommon/v1/organization/add_member_request.proto` **Package**: `gcommon.v1.organization` **Lines**: 32

**Messages** (1): `AddMemberRequest`

**Imports** (4):

- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/organization/organization_member.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/add_member_request.proto
// version: 1.0.0
// guid: a3f32353-366f-45a4-ae2f-7c8493c5dfca

edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/organization/organization_member.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message AddMemberRequest {
  // Request metadata for tracing and context
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Organization identifier
  string organization_id = 2 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Member information to add
  OrganizationMember member = 3;

  // Send invitation email if true
  bool send_invite = 4;
}
```

---

### add_member_response.proto {#add_member_response}

**Path**: `gcommon/v1/organization/add_member_response.proto` **Package**: `gcommon.v1.organization` **Lines**: 26

**Messages** (1): `AddMemberResponse`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/organization/organization_member.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/add_member_response.proto
// version: 1.0.0
// guid: 33d9c949-572d-4466-b0cf-885572c420a1
edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/organization/organization_member.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message AddMemberResponse {
  // Any errors encountered
  repeated gcommon.v1.common.Error errors = 1 [(buf.validate.field).repeated.min_items = 1];

  // Success status
  bool success = 2;

  // Newly added member information
  OrganizationMember member = 3;
}
```

---

### create_department_request.proto {#create_department_request}

**Path**: `gcommon/v1/organization/create_department_request.proto` **Package**: `gcommon.v1.organization` **Lines**: 25

**Messages** (1): `CreateDepartmentRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/organization/department.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/create_department_request.proto
// version: 1.0.1
// guid: d34e33ab-0a04-4f46-960f-5d5fd3b7cdcb

edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/organization/department.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message CreateDepartmentRequest {
  // Request metadata for tracing and context
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Department information to create
  Department department = 2;

  // Validate only without persisting if true
  bool validate_only = 3;
}
```

---

### create_department_response.proto {#create_department_response}

**Path**: `gcommon/v1/organization/create_department_response.proto` **Package**: `gcommon.v1.organization` **Lines**: 26

**Messages** (1): `CreateDepartmentResponse`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/organization/department.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/create_department_response.proto
// version: 1.0.0
// guid: 38a42c2a-fd4b-4805-9fd8-6c87d4959f99
edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/organization/department.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message CreateDepartmentResponse {
  // Any errors encountered
  repeated gcommon.v1.common.Error errors = 1 [(buf.validate.field).repeated.min_items = 1];

  // Success status
  bool success = 2;

  // Newly created department information
  Department department = 3;
}
```

---

### create_organization_request.proto {#create_organization_request}

**Path**: `gcommon/v1/organization/create_organization_request.proto` **Package**: `gcommon.v1.organization` **Lines**: 48

**Messages** (1): `CreateOrganizationRequest`

**Imports** (4):

- `buf/validate/validate.proto`
- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/organization/organization.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/create_organization_request.proto
// version: 1.1.0
// guid: 56789abc-def0-1234-5678-9abcdef01234

edition = "2023";

package gcommon.v1.organization;

import "buf/validate/validate.proto";
import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/organization/organization.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message CreateOrganizationRequest {
  // Request metadata for tracing and context - required
  gcommon.v1.common.RequestMetadata metadata = 1 [(buf.validate.field).required = true];

  // Organization information to create - required
  Organization organization = 2 [(buf.validate.field).required = true];

  // Whether to create a default tenant for this organization
  bool create_default_tenant = 3;

  // Initial organization settings (optional) - must be valid JSON if provided
  string initial_settings_json = 4 [(buf.validate.field).cel = {
    id: "initial_settings_json.valid_json"
    message: "Initial settings must be valid JSON if provided."
    expression: "this == '' || this.matches(r'^\\s*[\\{\\[].*[\\}\\]]\\s*$')"
  }];

  // Owner user ID (will be added as organization owner) - required, must be valid UUID format
  string owner_user_id = 5 [
    (buf.validate.field).required = true,
    (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$"
  ];

  // Whether to send welcome email to owner
  bool send_welcome_email = 6;

  // Template to use for organization creation (if applicable) - alphanumeric with underscores only
  string organization_template = 7 [(buf.validate.field).string = {
    pattern: "^[a-zA-Z0-9_]*$"
    max_len: 100
  }];
}
```

---

### create_organization_response.proto {#create_organization_response}

**Path**: `gcommon/v1/organization/create_organization_response.proto` **Package**: `gcommon.v1.organization` **Lines**: 40

**Messages** (1): `CreateOrganizationResponse`

**Imports** (5):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/organization/organization.proto`
- `gcommon/v1/organization/tenant.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/create_organization_response.proto
// version: 1.0.0
// guid: 42a09f2a-9157-45ed-a470-6b5c755e4e15
edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/organization/organization.proto";
import "gcommon/v1/organization/tenant.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

/**
 * CreateOrganizationResponse message returning the result of organization creation.
 * Contains the created organization and any related entities.
 */
message CreateOrganizationResponse {
  // Created organization
  Organization organization = 1;

  // Default tenant (if created)
  Tenant default_tenant = 2;

  // Organization member record for the owner
  string owner_member_id = 3 [(buf.validate.field).string.min_len = 1];

  // Any errors encountered during creation
  repeated gcommon.v1.common.Error errors = 4 [(buf.validate.field).repeated.min_items = 1];

  // Success status
  bool success = 5;

  // Additional information about the creation process
  string message = 6 [(buf.validate.field).string.min_len = 1];
}
```

---

### create_team_request.proto {#create_team_request}

**Path**: `gcommon/v1/organization/create_team_request.proto` **Package**: `gcommon.v1.organization` **Lines**: 25

**Messages** (1): `CreateTeamRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/organization/team.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/create_team_request.proto
// version: 1.0.1
// guid: 21cf9d30-d222-4d27-95dc-6dc71cf4a89f

edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/organization/team.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message CreateTeamRequest {
  // Request metadata for tracing and context
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Team details to create
  Team team = 2;

  // Validate only without persisting if true
  bool validate_only = 3;
}
```

---

### create_team_response.proto {#create_team_response}

**Path**: `gcommon/v1/organization/create_team_response.proto` **Package**: `gcommon.v1.organization` **Lines**: 26

**Messages** (1): `CreateTeamResponse`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/organization/team.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/create_team_response.proto
// version: 1.0.0
// guid: 58d56337-9058-4fc8-907a-062ae264e556
edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/organization/team.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message CreateTeamResponse {
  // Any errors encountered
  repeated gcommon.v1.common.Error errors = 1 [(buf.validate.field).repeated.min_items = 1];

  // Success status
  bool success = 2;

  // Newly created team information
  Team team = 3;
}
```

---

### create_tenant_request.proto {#create_tenant_request}

**Path**: `gcommon/v1/organization/create_tenant_request.proto` **Package**: `gcommon.v1.organization` **Lines**: 24

**Messages** (1): `CreateTenantRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/organization/tenant.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/create_tenant_request.proto
// version: 1.0.1
// guid: bff082b5-49b8-4b48-808c-5d8a7af3463b

edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/organization/tenant.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message CreateTenantRequest {
  // Request metadata for tracing and context
  gcommon.v1.common.RequestMetadata metadata = 1;
  // The tenant to create.
  Tenant tenant = 2;

  // Validate only without persisting if true
  bool validate_only = 3;
}
```

---

### create_tenant_response.proto {#create_tenant_response}

**Path**: `gcommon/v1/organization/create_tenant_response.proto` **Package**: `gcommon.v1.organization` **Lines**: 26

**Messages** (1): `CreateTenantResponse`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/organization/tenant.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/create_tenant_response.proto
// version: 1.0.0
// guid: 4c1b8703-1137-44ee-b243-49b82281f749
edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/organization/tenant.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message CreateTenantResponse {
  // Any errors encountered
  repeated gcommon.v1.common.Error errors = 1 [(buf.validate.field).repeated.min_items = 1];

  // Success status
  bool success = 2;

  // Newly created tenant details
  Tenant tenant = 3;
}
```

---

### delete_department_request.proto {#delete_department_request}

**Path**: `gcommon/v1/organization/delete_department_request.proto` **Package**: `gcommon.v1.organization` **Lines**: 23

**Messages** (1): `DeleteDepartmentRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/delete_department_request.proto
// version: 1.0.0
// guid: 2b15b8b7-144c-4c84-9424-630b1919eaad

edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message DeleteDepartmentRequest {
  // Request metadata for tracing and context
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Department identifier to delete
  string department_id = 2 [(buf.validate.field).string.min_len = 1];
}
```

---

### delete_department_response.proto {#delete_department_response}

**Path**: `gcommon/v1/organization/delete_department_response.proto` **Package**: `gcommon.v1.organization` **Lines**: 22

**Messages** (1): `DeleteDepartmentResponse`

**Imports** (3):

- `gcommon/v1/common/error.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/delete_department_response.proto
// version: 1.0.0
// guid: 96c06d37-d7ce-44e0-b105-416b410807dd
edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/common/error.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message DeleteDepartmentResponse {
  // Any errors encountered
  repeated gcommon.v1.common.Error errors = 1 [(buf.validate.field).repeated.min_items = 1];

  // Success status
  bool success = 2;
}
```

---

### delete_organization_request.proto {#delete_organization_request}

**Path**: `gcommon/v1/organization/delete_organization_request.proto` **Package**: `gcommon.v1.organization` **Lines**: 25

**Messages** (1): `DeleteOrganizationRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/delete_organization_request.proto
// version: 1.0.0
// guid: 60f56333-7919-43ba-aef1-0d0b46757352

edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message DeleteOrganizationRequest {
  // Request metadata for tracing and context
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Organization identifier to delete
  string organization_id = 2 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];
}
```

---

### delete_organization_response.proto {#delete_organization_response}

**Path**: `gcommon/v1/organization/delete_organization_response.proto` **Package**: `gcommon.v1.organization` **Lines**: 22

**Messages** (1): `DeleteOrganizationResponse`

**Imports** (3):

- `gcommon/v1/common/error.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/delete_organization_response.proto
// version: 1.0.0
// guid: abf1a483-14a7-4ddd-952c-f8bd5f93ddf3
edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/common/error.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message DeleteOrganizationResponse {
  // Any errors encountered
  repeated gcommon.v1.common.Error errors = 1 [(buf.validate.field).repeated.min_items = 1];

  // Success status
  bool success = 2;
}
```

---

### delete_team_request.proto {#delete_team_request}

**Path**: `gcommon/v1/organization/delete_team_request.proto` **Package**: `gcommon.v1.organization` **Lines**: 26

**Messages** (1): `DeleteTeamRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/delete_team_request.proto
// version: 1.0.0
// guid: 9f3757bb-554f-4098-afee-2450a9336a21

edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message DeleteTeamRequest {
  // Request metadata for tracing and context
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Identifier of the team to delete
  string team_id = 2 [(buf.validate.field).string.min_len = 1];

  // Force delete even if team has members
  bool force = 3;
}
```

---

### delete_team_response.proto {#delete_team_response}

**Path**: `gcommon/v1/organization/delete_team_response.proto` **Package**: `gcommon.v1.organization` **Lines**: 22

**Messages** (1): `DeleteTeamResponse`

**Imports** (3):

- `gcommon/v1/common/error.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/delete_team_response.proto
// version: 1.0.0
// guid: 69568dc0-2615-41c3-9244-1665554ae4ea
edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/common/error.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message DeleteTeamResponse {
  // Any errors encountered
  repeated gcommon.v1.common.Error errors = 1 [(buf.validate.field).repeated.min_items = 1];

  // Success status
  bool success = 2;
}
```

---

### delete_tenant_request.proto {#delete_tenant_request}

**Path**: `gcommon/v1/organization/delete_tenant_request.proto` **Package**: `gcommon.v1.organization` **Lines**: 23

**Messages** (1): `DeleteTenantRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/delete_tenant_request.proto
// version: 1.0.0
// guid: 0e0169f4-fdfc-49a6-96d0-a9bec15912d4

edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message DeleteTenantRequest {
  // Request metadata for tracing and context
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Tenant identifier to delete
  string tenant_id = 2 [(buf.validate.field).string.min_len = 1];
}
```

---

### delete_tenant_response.proto {#delete_tenant_response}

**Path**: `gcommon/v1/organization/delete_tenant_response.proto` **Package**: `gcommon.v1.organization` **Lines**: 22

**Messages** (1): `DeleteTenantResponse`

**Imports** (3):

- `gcommon/v1/common/error.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/delete_tenant_response.proto
// version: 1.0.0
// guid: 4c300220-de58-467e-b7b7-cf2c88ba7bf2
edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/common/error.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message DeleteTenantResponse {
  // Any errors encountered
  repeated gcommon.v1.common.Error errors = 1 [(buf.validate.field).repeated.min_items = 1];

  // Success status
  bool success = 2;
}
```

---

### get_department_request.proto {#get_department_request}

**Path**: `gcommon/v1/organization/get_department_request.proto` **Package**: `gcommon.v1.organization` **Lines**: 23

**Messages** (1): `GetDepartmentRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/get_department_request.proto
// version: 1.0.0
// guid: be0e4bd4-963f-49c4-b1a7-30b6473ab1d3

edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message GetDepartmentRequest {
  // Request metadata for tracing and context
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Department identifier
  string department_id = 2 [(buf.validate.field).string.min_len = 1];
}
```

---

### get_department_response.proto {#get_department_response}

**Path**: `gcommon/v1/organization/get_department_response.proto` **Package**: `gcommon.v1.organization` **Lines**: 26

**Messages** (1): `GetDepartmentResponse`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/organization/department.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/get_department_response.proto
// version: 1.0.0
// guid: ef416978-0a01-495e-bca1-833833179337
edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/organization/department.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message GetDepartmentResponse {
  // Any errors encountered
  repeated gcommon.v1.common.Error errors = 1 [(buf.validate.field).repeated.min_items = 1];

  // Success status
  bool success = 2;

  // Department information
  Department department = 3;
}
```

---

### get_hierarchy_request.proto {#get_hierarchy_request}

**Path**: `gcommon/v1/organization/get_hierarchy_request.proto` **Package**: `gcommon.v1.organization` **Lines**: 28

**Messages** (1): `GetHierarchyRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/get_hierarchy_request.proto
// version: 1.0.0
// guid: bf55fe81-30b5-4e35-80fb-3197068030bd

edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message GetHierarchyRequest {
  // Request metadata for tracing and context
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Organization identifier
  string organization_id = 2 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Hierarchy identifier
  string hierarchy_id = 3;
}
```

---

### get_hierarchy_response.proto {#get_hierarchy_response}

**Path**: `gcommon/v1/organization/get_hierarchy_response.proto` **Package**: `gcommon.v1.organization` **Lines**: 26

**Messages** (1): `GetHierarchyResponse`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/organization/organization_hierarchy.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/get_hierarchy_response.proto
// version: 1.0.0
// guid: 544cb8ef-e8c5-4f3d-9713-9a97b01edc38
edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/organization/organization_hierarchy.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message GetHierarchyResponse {
  // Any errors encountered
  repeated gcommon.v1.common.Error errors = 1 [(buf.validate.field).repeated.min_items = 1];

  // Success status
  bool success = 2;

  // Retrieved hierarchy data
  OrganizationHierarchy hierarchy = 3 [lazy = true];
}
```

---

### get_organization_request.proto {#get_organization_request}

**Path**: `gcommon/v1/organization/get_organization_request.proto` **Package**: `gcommon.v1.organization` **Lines**: 34

**Messages** (1): `GetOrganizationRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/get_organization_request.proto
// version: 1.0.0
// guid: ac85671a-6c97-4089-a922-a3aef359407e

edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message GetOrganizationRequest {
  // Request metadata for tracing and context
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Organization ID to retrieve
  string organization_id = 2 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Whether to include organization settings in response
  bool include_settings = 3;

  // Whether to include member count in response
  bool include_member_count = 4;

  // Whether to include tenant information
  bool include_tenants = 5;
}
```

---

### get_organization_response.proto {#get_organization_response}

**Path**: `gcommon/v1/organization/get_organization_response.proto` **Package**: `gcommon.v1.organization` **Lines**: 41

**Messages** (1): `GetOrganizationResponse`

**Imports** (6):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/organization/organization.proto`
- `gcommon/v1/organization/organization_settings.proto`
- `gcommon/v1/organization/tenant.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/get_organization_response.proto
// version: 1.0.0
// guid: 89012bcd-3456-789a-bcde-f01234567890

edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/organization/organization.proto";
import "gcommon/v1/organization/organization_settings.proto";
import "gcommon/v1/organization/tenant.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

/**
 * GetOrganizationResponse message returning organization information.
 */
message GetOrganizationResponse {
  // Organization information
  Organization organization = 1;

  // Organization settings (if requested)
  OrganizationSettings settings = 2;

  // Number of members in organization (if requested)
  int32 member_count = 3 [(buf.validate.field).int32.gte = 0];

  // List of tenants in organization (if requested)
  repeated Tenant tenants = 4 [(buf.validate.field).repeated.min_items = 1];

  // Any errors encountered during retrieval
  repeated gcommon.v1.common.Error errors = 5 [(buf.validate.field).repeated.min_items = 1];

  // Success status
  bool success = 6;
}
```

---

### get_organization_settings_request.proto {#get_organization_settings_request}

**Path**: `gcommon/v1/organization/get_organization_settings_request.proto` **Package**: `gcommon.v1.organization` **Lines**: 25

**Messages** (1): `GetOrganizationSettingsRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/get_organization_settings_request.proto
// version: 1.0.0
// guid: ad16db7e-8c7c-4a8a-b261-362207ddb779

edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message GetOrganizationSettingsRequest {
  // Request metadata for tracing and context
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Organization identifier
  string organization_id = 2 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];
}
```

---

### get_organization_settings_response.proto {#get_organization_settings_response}

**Path**: `gcommon/v1/organization/get_organization_settings_response.proto` **Package**: `gcommon.v1.organization` **Lines**: 26

**Messages** (1): `GetOrganizationSettingsResponse`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/organization/organization_settings.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/get_organization_settings_response.proto
// version: 1.0.0
// guid: cb31e0a3-f5db-43e7-8e24-3a0669bf515c
edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/organization/organization_settings.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message GetOrganizationSettingsResponse {
  // Any errors encountered
  repeated gcommon.v1.common.Error errors = 1 [(buf.validate.field).repeated.min_items = 1];

  // Success status
  bool success = 2;

  // Retrieved settings data
  OrganizationSettings settings = 3 [lazy = true];
}
```

---

### get_team_request.proto {#get_team_request}

**Path**: `gcommon/v1/organization/get_team_request.proto` **Package**: `gcommon.v1.organization` **Lines**: 23

**Messages** (1): `GetTeamRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/get_team_request.proto
// version: 1.0.0
// guid: fbed9098-fc8c-4afe-8d21-dd883fd0faee

edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message GetTeamRequest {
  // Request metadata for tracing and context
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Team identifier
  string team_id = 2 [(buf.validate.field).string.min_len = 1];
}
```

---

### get_team_response.proto {#get_team_response}

**Path**: `gcommon/v1/organization/get_team_response.proto` **Package**: `gcommon.v1.organization` **Lines**: 26

**Messages** (1): `GetTeamResponse`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/organization/team.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/get_team_response.proto
// version: 1.0.0
// guid: bd5b83ed-94f6-4276-bbd6-92c5e4314b9a
edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/organization/team.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message GetTeamResponse {
  // Any errors encountered
  repeated gcommon.v1.common.Error errors = 1 [(buf.validate.field).repeated.min_items = 1];

  // Success status
  bool success = 2;

  // Team information
  Team team = 3;
}
```

---

### get_tenant_isolation_request.proto {#get_tenant_isolation_request}

**Path**: `gcommon/v1/organization/get_tenant_isolation_request.proto` **Package**: `gcommon.v1.organization` **Lines**: 23

**Messages** (1): `GetTenantIsolationRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/get_tenant_isolation_request.proto
// version: 1.0.0
// guid: 81d19893-5428-407d-8b0d-29ce71a3f67c

edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message GetTenantIsolationRequest {
  // Request metadata for tracing and context
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Tenant identifier
  string tenant_id = 2 [(buf.validate.field).string.min_len = 1];
}
```

---

### get_tenant_isolation_response.proto {#get_tenant_isolation_response}

**Path**: `gcommon/v1/organization/get_tenant_isolation_response.proto` **Package**: `gcommon.v1.organization` **Lines**: 26

**Messages** (1): `GetTenantIsolationResponse`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/organization/tenant_isolation.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/get_tenant_isolation_response.proto
// version: 1.0.0
// guid: 75f44d74-ae44-4d4c-ac6b-92a9d1b7d643
edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/organization/tenant_isolation.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message GetTenantIsolationResponse {
  // Any errors encountered
  repeated gcommon.v1.common.Error errors = 1 [(buf.validate.field).repeated.min_items = 1];

  // Success status
  bool success = 2;

  // Current isolation configuration
  TenantIsolation isolation = 3 [lazy = true];
}
```

---

### get_tenant_request.proto {#get_tenant_request}

**Path**: `gcommon/v1/organization/get_tenant_request.proto` **Package**: `gcommon.v1.organization` **Lines**: 23

**Messages** (1): `GetTenantRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/get_tenant_request.proto
// version: 1.0.0
// guid: f2b2309c-363b-4df2-9303-d72a3b424faf

edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message GetTenantRequest {
  // Request metadata for tracing and context
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Tenant identifier
  string tenant_id = 2 [(buf.validate.field).string.min_len = 1];
}
```

---

### get_tenant_response.proto {#get_tenant_response}

**Path**: `gcommon/v1/organization/get_tenant_response.proto` **Package**: `gcommon.v1.organization` **Lines**: 26

**Messages** (1): `GetTenantResponse`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/organization/tenant.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/get_tenant_response.proto
// version: 1.0.0
// guid: c877593d-f248-4b07-87c2-8a0d1ea084c9
edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/organization/tenant.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message GetTenantResponse {
  // Any errors encountered
  repeated gcommon.v1.common.Error errors = 1 [(buf.validate.field).repeated.min_items = 1];

  // Success status
  bool success = 2;

  // The tenant information.
  Tenant tenant = 3;
}
```

---

### get_tenant_usage_request.proto {#get_tenant_usage_request}

**Path**: `gcommon/v1/organization/get_tenant_usage_request.proto` **Package**: `gcommon.v1.organization` **Lines**: 23

**Messages** (1): `GetTenantUsageRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/get_tenant_usage_request.proto
// version: 1.0.0
// guid: 84976640-c11e-47c5-a862-5afb5bca2480

edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message GetTenantUsageRequest {
  // Request metadata for tracing and context
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Tenant identifier
  string tenant_id = 2 [(buf.validate.field).string.min_len = 1];
}
```

---

### get_tenant_usage_response.proto {#get_tenant_usage_response}

**Path**: `gcommon/v1/organization/get_tenant_usage_response.proto` **Package**: `gcommon.v1.organization` **Lines**: 26

**Messages** (1): `GetTenantUsageResponse`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/key_value.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/get_tenant_usage_response.proto
// version: 1.0.1
// guid: c93fcd4c-7090-4c96-9c04-1e2b77a10337
edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/key_value.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message GetTenantUsageResponse {
  // Any errors encountered
  repeated gcommon.v1.common.Error errors = 1 [(buf.validate.field).repeated.min_items = 1];

  // Success status
  bool success = 2;

  // Usage statistics for the tenant
  repeated gcommon.v1.common.KeyValue usage_stats = 3 [lazy = true, (buf.validate.field).repeated.min_items = 1];
}
```

---

### list_departments_request.proto {#list_departments_request}

**Path**: `gcommon/v1/organization/list_departments_request.proto` **Package**: `gcommon.v1.organization` **Lines**: 34

**Messages** (1): `ListDepartmentsRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/list_departments_request.proto
// version: 1.0.0
// guid: 874d0e66-c98b-40cc-b0b2-ffb5f57d2d0f

edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message ListDepartmentsRequest {
  // Request metadata for tracing and context
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Organization identifier to list departments for
  string organization_id = 2 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Pagination size (max results per page)
  int32 page_size = 3;

  // Pagination token from previous response
  string page_token = 4;

  // Optional filter expression
  string filter = 5;
}
```

---

### list_departments_response.proto {#list_departments_response}

**Path**: `gcommon/v1/organization/list_departments_response.proto` **Package**: `gcommon.v1.organization` **Lines**: 30

**Messages** (1): `ListDepartmentsResponse`

**Imports** (5):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/paginated_response.proto`
- `gcommon/v1/organization/department.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/list_departments_response.proto
// version: 1.0.1
// guid: 7b9579ba-6f96-40bb-b38c-79de470de2ff
edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/paginated_response.proto";
import "gcommon/v1/organization/department.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message ListDepartmentsResponse {
  // Any errors encountered
  repeated gcommon.v1.common.Error errors = 1 [(buf.validate.field).repeated.min_items = 1];

  // Success status
  bool success = 2;

  // List of departments returned
  repeated Department departments = 3 [lazy = true, (buf.validate.field).repeated.min_items = 1];

  // Pagination metadata
  gcommon.v1.common.PaginatedResponse pagination = 4;
}
```

---

### list_members_request.proto {#list_members_request}

**Path**: `gcommon/v1/organization/list_members_request.proto` **Package**: `gcommon.v1.organization` **Lines**: 40

**Messages** (1): `ListMembersRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/list_members_request.proto
// version: 1.0.0
// guid: 406d6cd1-34df-4a3a-9fd9-f479ec2dbfdb

edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message ListMembersRequest {
  // Request metadata for tracing and context
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Organization identifier
  string organization_id = 2 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Optional team identifier to filter
  string team_id = 3;

  // Optional department identifier
  string department_id = 4;

  // Pagination size
  int32 page_size = 5;

  // Pagination token from previous response
  string page_token = 6;

  // Optional filter expression
  string filter = 7;
}
```

---

### list_members_response.proto {#list_members_response}

**Path**: `gcommon/v1/organization/list_members_response.proto` **Package**: `gcommon.v1.organization` **Lines**: 30

**Messages** (1): `ListMembersResponse`

**Imports** (5):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/paginated_response.proto`
- `gcommon/v1/organization/organization_member.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/list_members_response.proto
// version: 1.0.1
// guid: b11659ab-afa5-4b48-a417-b3b28ade628a
edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/paginated_response.proto";
import "gcommon/v1/organization/organization_member.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message ListMembersResponse {
  // Any errors encountered
  repeated gcommon.v1.common.Error errors = 1 [(buf.validate.field).repeated.min_items = 1];

  // Success status
  bool success = 2;

  // List of members returned
  repeated OrganizationMember members = 3 [lazy = true, (buf.validate.field).repeated.min_items = 1];

  // Pagination metadata
  gcommon.v1.common.PaginatedResponse pagination = 4;
}
```

---

### list_organizations_request.proto {#list_organizations_request}

**Path**: `gcommon/v1/organization/list_organizations_request.proto` **Package**: `gcommon.v1.organization` **Lines**: 29

**Messages** (1): `ListOrganizationsRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/list_organizations_request.proto
// version: 1.0.0
// guid: cdeed5f8-bf7f-4184-9599-edc8ff33cabe

edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message ListOrganizationsRequest {
  // Request metadata for tracing and context
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Pagination size
  int32 page_size = 2 [(buf.validate.field).int32.gte = 0, (buf.validate.field).int32.lte = 150];

  // Pagination token from previous response
  string page_token = 3 [(buf.validate.field).string.min_len = 1];

  // Optional filter expression
  string filter = 4 [(buf.validate.field).string.min_len = 1];
}
```

---

### list_organizations_response.proto {#list_organizations_response}

**Path**: `gcommon/v1/organization/list_organizations_response.proto` **Package**: `gcommon.v1.organization` **Lines**: 30

**Messages** (1): `ListOrganizationsResponse`

**Imports** (5):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/paginated_response.proto`
- `gcommon/v1/organization/organization.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/list_organizations_response.proto
// version: 1.0.1
// guid: 3da96ff2-b3f3-479b-86e8-77a5ae8bcd5d
edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/paginated_response.proto";
import "gcommon/v1/organization/organization.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message ListOrganizationsResponse {
  // Any errors encountered
  repeated gcommon.v1.common.Error errors = 1 [(buf.validate.field).repeated.min_items = 1];

  // Success status
  bool success = 2;

  // List of organizations returned
  repeated Organization organizations = 3 [lazy = true, (buf.validate.field).repeated.min_items = 1];

  // Pagination metadata
  gcommon.v1.common.PaginatedResponse pagination = 4;
}
```

---

### list_teams_request.proto {#list_teams_request}

**Path**: `gcommon/v1/organization/list_teams_request.proto` **Package**: `gcommon.v1.organization` **Lines**: 37

**Messages** (1): `ListTeamsRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/list_teams_request.proto
// version: 1.0.0
// guid: 7ce907a1-9e89-4305-86e1-5ab7a8ab83aa

edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message ListTeamsRequest {
  // Request metadata for tracing and context
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Organization identifier
  string organization_id = 2 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Optional department identifier to scope teams
  string department_id = 3;

  // Maximum number of teams to return
  int32 page_size = 4;

  // Pagination token from previous response
  string page_token = 5;

  // Optional filter expression
  string filter = 6;
}
```

---

### list_teams_response.proto {#list_teams_response}

**Path**: `gcommon/v1/organization/list_teams_response.proto` **Package**: `gcommon.v1.organization` **Lines**: 30

**Messages** (1): `ListTeamsResponse`

**Imports** (5):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/paginated_response.proto`
- `gcommon/v1/organization/team.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/list_teams_response.proto
// version: 1.0.1
// guid: 0707cfbc-2147-4295-9e5f-f42fb515a73c
edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/paginated_response.proto";
import "gcommon/v1/organization/team.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message ListTeamsResponse {
  // Any errors encountered
  repeated gcommon.v1.common.Error errors = 1 [(buf.validate.field).repeated.min_items = 1];

  // Success status
  bool success = 2;

  // List of teams returned
  repeated Team teams = 3 [lazy = true, (buf.validate.field).repeated.min_items = 1];

  // Pagination metadata
  gcommon.v1.common.PaginatedResponse pagination = 4;
}
```

---

### list_tenants_request.proto {#list_tenants_request}

**Path**: `gcommon/v1/organization/list_tenants_request.proto` **Package**: `gcommon.v1.organization` **Lines**: 34

**Messages** (1): `ListTenantsRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/list_tenants_request.proto
// version: 1.0.0
// guid: c1f36d36-4e24-4b8e-93d3-5365249b0888

edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message ListTenantsRequest {
  // Request metadata for tracing and context
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Organization identifier
  string organization_id = 2 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Pagination size
  int32 page_size = 3;

  // Pagination token from previous response
  string page_token = 4;

  // Optional filter expression
  string filter = 5;
}
```

---

### list_tenants_response.proto {#list_tenants_response}

**Path**: `gcommon/v1/organization/list_tenants_response.proto` **Package**: `gcommon.v1.organization` **Lines**: 30

**Messages** (1): `ListTenantsResponse`

**Imports** (5):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/paginated_response.proto`
- `gcommon/v1/organization/tenant.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/list_tenants_response.proto
// version: 1.0.0
// guid: ea50c027-6fc4-450e-911b-8b34c268b827
edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/paginated_response.proto";
import "gcommon/v1/organization/tenant.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message ListTenantsResponse {
  // Any errors encountered
  repeated gcommon.v1.common.Error errors = 1 [(buf.validate.field).repeated.min_items = 1];

  // Success status
  bool success = 2;

  // List of tenants returned
  repeated Tenant tenants = 3 [(buf.validate.field).repeated.min_items = 1];

  // Pagination metadata
  gcommon.v1.common.PaginatedResponse pagination = 4;
}
```

---

### remove_member_request.proto {#remove_member_request}

**Path**: `gcommon/v1/organization/remove_member_request.proto` **Package**: `gcommon.v1.organization` **Lines**: 28

**Messages** (1): `RemoveMemberRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/remove_member_request.proto
// version: 1.0.0
// guid: 872a8e4b-2348-48e1-b9f0-24da3693fce2

edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message RemoveMemberRequest {
  // Request metadata for tracing and context
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Organization identifier
  string organization_id = 2 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Member identifier to remove
  string member_id = 3;
}
```

---

### remove_member_response.proto {#remove_member_response}

**Path**: `gcommon/v1/organization/remove_member_response.proto` **Package**: `gcommon.v1.organization` **Lines**: 22

**Messages** (1): `RemoveMemberResponse`

**Imports** (3):

- `gcommon/v1/common/error.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/remove_member_response.proto
// version: 1.0.0
// guid: 183c4904-d0fd-47bd-b54c-5be727d87cbd
edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/common/error.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message RemoveMemberResponse {
  // Any errors encountered
  repeated gcommon.v1.common.Error errors = 1 [(buf.validate.field).repeated.min_items = 1];

  // Success status
  bool success = 2;
}
```

---

### update_department_request.proto {#update_department_request}

**Path**: `gcommon/v1/organization/update_department_request.proto` **Package**: `gcommon.v1.organization` **Lines**: 34

**Messages** (1): `UpdateDepartmentRequest`

**Imports** (5):

- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/organization/department.proto`
- `google/protobuf/field_mask.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/update_department_request.proto
// version: 1.0.0
// guid: a8012f3b-6cf3-4b2d-ba62-d9b6a56fed3a

edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/organization/department.proto";
import "google/protobuf/field_mask.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message UpdateDepartmentRequest {
  // Request metadata for tracing and context
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Department identifier to update
  string department_id = 2 [(buf.validate.field).string.min_len = 1];

  // Updated department information
  Department department = 3;

  // Fields to update in partial mode
  google.protobuf.FieldMask update_mask = 4;

  // Validate only without persisting if true
  bool validate_only = 5;
}
```

---

### update_department_response.proto {#update_department_response}

**Path**: `gcommon/v1/organization/update_department_response.proto` **Package**: `gcommon.v1.organization` **Lines**: 26

**Messages** (1): `UpdateDepartmentResponse`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/organization/department.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/update_department_response.proto
// version: 1.0.0
// guid: 3bcf5ff1-e62a-4e1d-9067-70ee328252d0
edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/organization/department.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message UpdateDepartmentResponse {
  // Any errors encountered
  repeated gcommon.v1.common.Error errors = 1 [(buf.validate.field).repeated.min_items = 1];

  // Success status
  bool success = 2;

  // Updated department information
  Department department = 3;
}
```

---

### update_hierarchy_request.proto {#update_hierarchy_request}

**Path**: `gcommon/v1/organization/update_hierarchy_request.proto` **Package**: `gcommon.v1.organization` **Lines**: 36

**Messages** (1): `UpdateHierarchyRequest`

**Imports** (5):

- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/organization/organization_hierarchy.proto`
- `google/protobuf/field_mask.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/update_hierarchy_request.proto
// version: 1.0.0
// guid: 6bd1b024-7f93-4cc5-87d2-568e9a8c4fae

edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/organization/organization_hierarchy.proto";
import "google/protobuf/field_mask.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message UpdateHierarchyRequest {
  // Request metadata for tracing and context
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Organization identifier
  string organization_id = 2 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Updated hierarchy data
  OrganizationHierarchy hierarchy = 3;

  // Fields to update
  google.protobuf.FieldMask update_mask = 4;

  // Validate only without persisting if true
  bool validate_only = 5;
}
```

---

### update_hierarchy_response.proto {#update_hierarchy_response}

**Path**: `gcommon/v1/organization/update_hierarchy_response.proto` **Package**: `gcommon.v1.organization` **Lines**: 26

**Messages** (1): `UpdateHierarchyResponse`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/organization/organization_hierarchy.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/update_hierarchy_response.proto
// version: 1.0.0
// guid: 3452f3c8-811a-405b-9429-bc43e5b5e66d
edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/organization/organization_hierarchy.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message UpdateHierarchyResponse {
  // Any errors encountered
  repeated gcommon.v1.common.Error errors = 1 [(buf.validate.field).repeated.min_items = 1];

  // Success status
  bool success = 2;

  // Updated hierarchy data
  OrganizationHierarchy hierarchy = 3 [lazy = true];
}
```

---

### update_member_request.proto {#update_member_request}

**Path**: `gcommon/v1/organization/update_member_request.proto` **Package**: `gcommon.v1.organization` **Lines**: 31

**Messages** (1): `UpdateMemberRequest`

**Imports** (5):

- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/organization/organization_member.proto`
- `google/protobuf/field_mask.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/update_member_request.proto
// version: 1.0.0
// guid: c91064f2-6854-4e07-83e6-dc6dd90127b9

edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/organization/organization_member.proto";
import "google/protobuf/field_mask.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message UpdateMemberRequest {
  // Request metadata for tracing and context
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Identifier of the member to update
  string member_id = 2 [(buf.validate.field).string.min_len = 1];

  // Updated member information
  OrganizationMember member = 3;

  // Fields to update for partial updates
  google.protobuf.FieldMask update_mask = 4;
}
```

---

### update_member_response.proto {#update_member_response}

**Path**: `gcommon/v1/organization/update_member_response.proto` **Package**: `gcommon.v1.organization` **Lines**: 26

**Messages** (1): `UpdateMemberResponse`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/organization/organization_member.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/update_member_response.proto
// version: 1.0.0
// guid: 2fbbf7bc-2367-4682-bd06-3dc49bb463ec
edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/organization/organization_member.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message UpdateMemberResponse {
  // Any errors encountered
  repeated gcommon.v1.common.Error errors = 1 [(buf.validate.field).repeated.min_items = 1];

  // Success status
  bool success = 2;

  // Updated member details
  OrganizationMember member = 3;
}
```

---

### update_organization_request.proto {#update_organization_request}

**Path**: `gcommon/v1/organization/update_organization_request.proto` **Package**: `gcommon.v1.organization` **Lines**: 32

**Messages** (1): `UpdateOrganizationRequest`

**Imports** (4):

- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/organization/organization.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/update_organization_request.proto
// version: 1.0.0
// guid: eb0d52f9-280c-4cd7-99f9-cc5e2bf6f4e9

edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/organization/organization.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message UpdateOrganizationRequest {
  // Request metadata for tracing and context
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Organization ID to update
  string organization_id = 2 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Updated organization information
  Organization organization = 3;

  // Fields to update (field mask)
  repeated string update_fields = 4;
}
```

---

### update_organization_response.proto {#update_organization_response}

**Path**: `gcommon/v1/organization/update_organization_response.proto` **Package**: `gcommon.v1.organization` **Lines**: 29

**Messages** (1): `UpdateOrganizationResponse`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/organization/organization.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/update_organization_response.proto
// version: 1.0.0
// guid: 68d40e74-1416-4e2a-978a-5cca7cc3a71a
edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/organization/organization.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

/**
 * UpdateOrganizationResponse message returning the result of organization update.
 */
message UpdateOrganizationResponse {
  // Updated organization
  Organization organization = 1;

  // Any errors encountered during update
  repeated gcommon.v1.common.Error errors = 2 [(buf.validate.field).repeated.min_items = 1];

  // Success status
  bool success = 3;
}
```

---

### update_organization_settings_request.proto {#update_organization_settings_request}

**Path**: `gcommon/v1/organization/update_organization_settings_request.proto` **Package**: `gcommon.v1.organization` **Lines**: 36

**Messages** (1): `UpdateOrganizationSettingsRequest`

**Imports** (5):

- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/organization/organization_settings.proto`
- `google/protobuf/field_mask.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/update_organization_settings_request.proto
// version: 1.0.0
// guid: 1a45386c-fda8-459c-b1bb-60c097f611ba

edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/organization/organization_settings.proto";
import "google/protobuf/field_mask.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message UpdateOrganizationSettingsRequest {
  // Request metadata for tracing and context
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Organization identifier
  string organization_id = 2 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Updated settings
  OrganizationSettings settings = 3;

  // Fields to update
  google.protobuf.FieldMask update_mask = 4;

  // Validate only without persisting if true
  bool validate_only = 5;
}
```

---

### update_organization_settings_response.proto {#update_organization_settings_response}

**Path**: `gcommon/v1/organization/update_organization_settings_response.proto` **Package**: `gcommon.v1.organization` **Lines**: 26

**Messages** (1): `UpdateOrganizationSettingsResponse`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/organization/organization_settings.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/update_organization_settings_response.proto
// version: 1.0.0
// guid: 3710df70-cb31-43a6-bd37-7443736307f4
edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/organization/organization_settings.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message UpdateOrganizationSettingsResponse {
  // Any errors encountered
  repeated gcommon.v1.common.Error errors = 1 [(buf.validate.field).repeated.min_items = 1];

  // Success status
  bool success = 2;

  // Updated settings data
  OrganizationSettings settings = 3 [lazy = true];
}
```

---

### update_team_request.proto {#update_team_request}

**Path**: `gcommon/v1/organization/update_team_request.proto` **Package**: `gcommon.v1.organization` **Lines**: 34

**Messages** (1): `UpdateTeamRequest`

**Imports** (5):

- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/organization/team.proto`
- `google/protobuf/field_mask.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/update_team_request.proto
// version: 1.0.0
// guid: c613ff0c-caef-4ec5-a856-de0a5ee8605c

edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/organization/team.proto";
import "google/protobuf/field_mask.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message UpdateTeamRequest {
  // Request metadata for tracing and context
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Team identifier to update
  string team_id = 2 [(buf.validate.field).string.min_len = 1];

  // Updated team information
  Team team = 3;

  // Fields to update in partial mode
  google.protobuf.FieldMask update_mask = 4;

  // Validate only without persisting if true
  bool validate_only = 5;
}
```

---

### update_team_response.proto {#update_team_response}

**Path**: `gcommon/v1/organization/update_team_response.proto` **Package**: `gcommon.v1.organization` **Lines**: 26

**Messages** (1): `UpdateTeamResponse`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/organization/team.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/update_team_response.proto
// version: 1.0.0
// guid: a06b35ad-8345-4bc2-99ce-2ef490c40a58
edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/organization/team.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message UpdateTeamResponse {
  // Any errors encountered
  repeated gcommon.v1.common.Error errors = 1 [(buf.validate.field).repeated.min_items = 1];

  // Success status
  bool success = 2;

  // Updated team information
  Team team = 3;
}
```

---

### update_tenant_quota_request.proto {#update_tenant_quota_request}

**Path**: `gcommon/v1/organization/update_tenant_quota_request.proto` **Package**: `gcommon.v1.organization` **Lines**: 27

**Messages** (1): `UpdateTenantQuotaRequest`

**Imports** (4):

- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/organization/tenant_quota.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/update_tenant_quota_request.proto
// version: 1.0.0
// guid: 3b0b2b76-0e29-4471-8cce-e2f7b4c4f3cf

edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/organization/tenant_quota.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message UpdateTenantQuotaRequest {
  // Request metadata for tracing and context
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Tenant identifier
  string tenant_id = 2 [(buf.validate.field).string.min_len = 1];

  // New quota configuration
  TenantQuota quota = 3;
}
```

---

### update_tenant_quota_response.proto {#update_tenant_quota_response}

**Path**: `gcommon/v1/organization/update_tenant_quota_response.proto` **Package**: `gcommon.v1.organization` **Lines**: 26

**Messages** (1): `UpdateTenantQuotaResponse`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/organization/tenant_quota.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/update_tenant_quota_response.proto
// version: 1.0.0
// guid: 53710858-87c4-40d7-98e7-905122f9d2b4
edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/organization/tenant_quota.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message UpdateTenantQuotaResponse {
  // Any errors encountered
  repeated gcommon.v1.common.Error errors = 1 [(buf.validate.field).repeated.min_items = 1];

  // Success status
  bool success = 2;

  // Updated quota configuration
  TenantQuota quota = 3;
}
```

---

### update_tenant_request.proto {#update_tenant_request}

**Path**: `gcommon/v1/organization/update_tenant_request.proto` **Package**: `gcommon.v1.organization` **Lines**: 34

**Messages** (1): `UpdateTenantRequest`

**Imports** (5):

- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/organization/tenant.proto`
- `google/protobuf/field_mask.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/update_tenant_request.proto
// version: 1.0.0
// guid: 1c9d8c7e-4c50-47b6-b6ff-c2dd363bbd5c

edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/organization/tenant.proto";
import "google/protobuf/field_mask.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message UpdateTenantRequest {
  // Request metadata for tracing and context
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Tenant identifier to update
  string tenant_id = 2 [(buf.validate.field).string.min_len = 1];

  // Updated tenant information
  Tenant tenant = 3;

  // Fields to update in partial mode
  google.protobuf.FieldMask update_mask = 4;

  // Validate only without persisting if true
  bool validate_only = 5;
}
```

---

### update_tenant_response.proto {#update_tenant_response}

**Path**: `gcommon/v1/organization/update_tenant_response.proto` **Package**: `gcommon.v1.organization` **Lines**: 26

**Messages** (1): `UpdateTenantResponse`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/organization/tenant.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/update_tenant_response.proto
// version: 1.0.0
// guid: 24a81e2b-b245-41df-b2f8-fd967f0655d0
edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/organization/tenant.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message UpdateTenantResponse {
  // Any errors encountered
  repeated gcommon.v1.common.Error errors = 1 [(buf.validate.field).repeated.min_items = 1];

  // Success status
  bool success = 2;

  // Updated tenant details
  Tenant tenant = 3;
}
```

---

### api_key_config.proto {#api_key_config}

**Path**: `gcommon/v1/organization/api_key_config.proto` **Package**: `gcommon.v1.organization` **Lines**: 31

**Messages** (1): `OrganizationAPIKeyConfig`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/api_key_config.proto
// version: 1.0.0
// guid: 28bb1e15-1e3c-4ae1-bb4f-9daa15fcdf1b

edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message OrganizationAPIKeyConfig {
  // API key name/identifier
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Masked API key (for display purposes)
  string masked_key = 2;

  // API key permissions/scopes
  repeated string scopes = 3;

  // API key expiration date
  google.protobuf.Timestamp expires_at = 4 [lazy = true];
}
```

---

### audit_config.proto {#audit_config}

**Path**: `gcommon/v1/organization/audit_config.proto` **Package**: `gcommon.v1.organization` **Lines**: 35

**Messages** (1): `AuditConfig`

**Imports** (3):

- `gcommon/v1/organization/audit_alert.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/audit_config.proto
// version: 1.0.0
// guid: 404c83b0-6f95-4a24-8f22-55baffc8e465

edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/organization/audit_alert.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message AuditConfig {
  // Whether audit logging is enabled
  bool audit_enabled = 1;

  // Audit log retention period in days
  int32 retention_days = 2 [(buf.validate.field).int32.gte = 0];

  // Audit log storage location
  string storage_location = 3 [(buf.validate.field).string.min_len = 1];

  // Events to audit
  repeated string audited_events = 4 [(buf.validate.field).repeated.min_items = 1];

  // Whether real-time monitoring is enabled
  bool real_time_monitoring = 5;

  // Alert configuration for audit events
  repeated AuditAlert alerts = 6 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### auto_scaling_config.proto {#auto_scaling_config}

**Path**: `gcommon/v1/organization/auto_scaling_config.proto` **Package**: `gcommon.v1.organization` **Lines**: 37

**Messages** (1): `AutoScalingConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/auto_scaling_config.proto
// version: 1.0.0
// guid: 81c51445-10c2-48b8-a056-a652df4f2d64

edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message AutoScalingConfig {
  // Whether auto-scaling is enabled
  bool enabled = 1;

  // Minimum number of instances
  int32 min_instances = 2 [(buf.validate.field).int32.gte = 0];

  // Maximum number of instances
  int32 max_instances = 3 [(buf.validate.field).int32.gte = 0];

  // Target CPU utilization percentage
  int32 target_cpu_percent = 4 [(buf.validate.field).int32.gte = 0];

  // Target memory utilization percentage
  int32 target_memory_percent = 5 [(buf.validate.field).int32.gte = 0];

  // Scale-up cooldown period in seconds
  int32 scale_up_cooldown = 6 [(buf.validate.field).int32.gte = 0];

  // Scale-down cooldown period in seconds
  int32 scale_down_cooldown = 7 [(buf.validate.field).int32.gte = 0];
}
```

---

### backup_config.proto {#backup_config}

**Path**: `gcommon/v1/organization/backup_config.proto` **Package**: `gcommon.v1.organization` **Lines**: 31

**Messages** (1): `OrganizationBackupConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/backup_config.proto
// version: 1.0.0
// guid: af98b66c-3106-4a09-9b66-b3fd3908267e

edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message OrganizationBackupConfig {
  // Whether automated backups are enabled
  bool enabled = 1;

  // Backup frequency (hourly, daily, weekly)
  string frequency = 2 [(buf.validate.field).string.min_len = 1];

  // Backup retention period in days
  int32 retention_days = 3 [(buf.validate.field).int32.gte = 0];

  // Backup storage location
  string storage_location = 4 [(buf.validate.field).string.min_len = 1];

  // Whether point-in-time recovery is enabled
  bool point_in_time_recovery = 5;
}
```

---

### cdn_config.proto {#cdn_config}

**Path**: `gcommon/v1/organization/cdn_config.proto` **Package**: `gcommon.v1.organization` **Lines**: 30

**Messages** (1): `CDNConfig`

**Imports** (4):

- `gcommon/v1/organization/cache_behavior.proto`
- `gcommon/v1/organization/origin_config.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/cdn_config.proto
// version: 1.0.0
// guid: 07ac4644-4b99-4ae2-a2c7-2fb5bcd47e0f

edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/organization/cache_behavior.proto";
import "gcommon/v1/organization/origin_config.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message CDNConfig {
  // CDN provider
  string provider = 1 [(buf.validate.field).string.min_len = 1];

  // CDN distribution ID
  string distribution_id = 2 [(buf.validate.field).string.min_len = 1];

  // Cache behavior settings
  repeated CacheBehavior cache_behaviors = 3 [(buf.validate.field).repeated.min_items = 1];

  // Origin configuration
  OriginConfig origin = 4;
}
```

---

### configure_tenant_isolation_request.proto {#configure_tenant_isolation_request}

**Path**: `gcommon/v1/organization/configure_tenant_isolation_request.proto` **Package**: `gcommon.v1.organization` **Lines**: 27

**Messages** (1): `ConfigureTenantIsolationRequest`

**Imports** (4):

- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/organization/tenant_isolation.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/configure_tenant_isolation_request.proto
// version: 1.0.0
// guid: ea4e2f71-cbce-4d87-9a60-96a9893190b0

edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/organization/tenant_isolation.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message ConfigureTenantIsolationRequest {
  // Request metadata for tracing and context
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Tenant identifier
  string tenant_id = 2 [(buf.validate.field).string.min_len = 1];

  // Isolation configuration to apply
  TenantIsolation isolation = 3;
}
```

---

### configure_tenant_isolation_response.proto {#configure_tenant_isolation_response}

**Path**: `gcommon/v1/organization/configure_tenant_isolation_response.proto` **Package**: `gcommon.v1.organization` **Lines**: 26

**Messages** (1): `ConfigureTenantIsolationResponse`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/organization/tenant_isolation.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/configure_tenant_isolation_response.proto
// version: 1.0.0
// guid: 8bfb868a-9352-4ca3-9e89-57d201252ebc
edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/organization/tenant_isolation.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message ConfigureTenantIsolationResponse {
  // Any errors encountered
  repeated gcommon.v1.common.Error errors = 1 [(buf.validate.field).repeated.min_items = 1];

  // Success status
  bool success = 2;

  // Applied isolation configuration
  TenantIsolation isolation = 3 [lazy = true];
}
```

---

### dns_config.proto {#dns_config}

**Path**: `gcommon/v1/organization/dns_config.proto` **Package**: `gcommon.v1.organization` **Lines**: 29

**Messages** (1): `DNSConfig`

**Imports** (3):

- `gcommon/v1/organization/dns_record.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/dns_config.proto
// version: 1.0.0
// guid: 4ce13993-ded9-4ed1-852c-8e73989b5baa

edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/organization/dns_record.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message DNSConfig {
  // DNS provider
  string provider = 1 [(buf.validate.field).string.min_len = 1];

  // DNS zone ID
  string zone_id = 2 [(buf.validate.field).string.min_len = 1];

  // DNS records
  repeated DNSRecord records = 3 [(buf.validate.field).repeated.min_items = 1];

  // TTL for DNS records
  int32 ttl = 4 [(buf.validate.field).int32.gte = 0];
}
```

---

### domain_config.proto {#domain_config}

**Path**: `gcommon/v1/organization/domain_config.proto` **Package**: `gcommon.v1.organization` **Lines**: 31

**Messages** (1): `DomainConfig`

**Imports** (3):

- `gcommon/v1/organization/dns_config.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/domain_config.proto
// version: 1.0.0
// guid: ee8bb6b4-f822-496b-8109-9bd6ffdbdf7b

edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/organization/dns_config.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message DomainConfig {
  // Custom domain name
  string domain_name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // SSL certificate ARN or ID
  string ssl_certificate = 2;

  // DNS configuration
  DNSConfig dns = 3;

  // Domain validation status
  string validation_status = 4;
}
```

---

### encryption_config.proto {#encryption_config}

**Path**: `gcommon/v1/organization/encryption_config.proto` **Package**: `gcommon.v1.organization` **Lines**: 31

**Messages** (1): `OrganizationEncryptionConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/encryption_config.proto
// version: 1.0.0
// guid: c6adca37-10ae-4aed-9ce2-eb555767c937

edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message OrganizationEncryptionConfig {
  // Whether encryption at rest is enabled
  bool encryption_at_rest = 1;

  // Whether encryption in transit is enabled
  bool encryption_in_transit = 2;

  // Encryption key management service
  string key_management_service = 3 [(buf.validate.field).string.min_len = 1];

  // Customer-managed encryption key ID
  string customer_key_id = 4 [(buf.validate.field).string.min_len = 1];

  // Encryption algorithm used
  string encryption_algorithm = 5 [(buf.validate.field).string.min_len = 1];
}
```

---

### health_check_config.proto {#health_check_config}

**Path**: `gcommon/v1/organization/health_check_config.proto` **Package**: `gcommon.v1.organization` **Lines**: 37

**Messages** (1): `OrganizationHealthCheckConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/health_check_config.proto
// version: 1.0.0
// guid: 3d161671-ebd9-42de-857a-2aef7ff4b62a

edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message OrganizationHealthCheckConfig {
  // Health check path
  string path = 1 [(buf.validate.field).string.min_len = 1];

  // Health check port
  int32 port = 2 [(buf.validate.field).int32.gte = 1, (buf.validate.field).int32.lte = 65535];

  // Health check protocol (HTTP, HTTPS, TCP)
  string protocol = 3 [(buf.validate.field).string.min_len = 1];

  // Health check interval in seconds
  int32 interval_seconds = 4 [(buf.validate.field).int32.gte = 0];

  // Health check timeout in seconds
  int32 timeout_seconds = 5 [(buf.validate.field).int32.gt = 0];

  // Healthy threshold
  int32 healthy_threshold = 6 [(buf.validate.field).int32.gte = 0];

  // Unhealthy threshold
  int32 unhealthy_threshold = 7 [(buf.validate.field).int32.gte = 0];
}
```

---

### load_balancer_config.proto {#load_balancer_config}

**Path**: `gcommon/v1/organization/load_balancer_config.proto` **Package**: `gcommon.v1.organization` **Lines**: 30

**Messages** (1): `OrganizationLoadBalancerConfig`

**Imports** (4):

- `gcommon/v1/organization/health_check_config.proto`
- `gcommon/v1/organization/ssl_config.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/load_balancer_config.proto
// version: 1.0.0
// guid: 9e0df8a1-fd1a-4173-89ed-7bcdc82cdb6f

edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/organization/health_check_config.proto";
import "gcommon/v1/organization/ssl_config.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message OrganizationLoadBalancerConfig {
  // Load balancer type (application, network)
  string type = 1 [(buf.validate.field).string.min_len = 1];

  // Load balancing algorithm
  string algorithm = 2 [(buf.validate.field).string.min_len = 1];

  // Health check configuration
  OrganizationHealthCheckConfig health_check = 3;

  // SSL/TLS configuration
  SSLConfig ssl = 4;
}
```

---

### o_auth_app_config.proto {#o_auth_app_config}

**Path**: `gcommon/v1/organization/o_auth_app_config.proto` **Package**: `gcommon.v1.organization` **Lines**: 30

**Messages** (1): `OAuthAppConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/o_auth_app_config.proto
// version: 1.0.0
// guid: 3db5888f-b55c-4810-82a3-0690f6604cf9

edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message OAuthAppConfig {
  // OAuth application name
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // OAuth client ID
  string client_id = 2;

  // OAuth redirect URIs
  repeated string redirect_uris = 3;

  // OAuth scopes
  repeated string scopes = 4;
}
```

---

### origin_config.proto {#origin_config}

**Path**: `gcommon/v1/organization/origin_config.proto` **Package**: `gcommon.v1.organization` **Lines**: 31

**Messages** (1): `OriginConfig`

**Imports** (3):

- `gcommon/v1/common/key_value.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/origin_config.proto
// version: 1.0.0
// guid: b84e3243-3ef5-4beb-94d1-db2bb8831611

edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/common/key_value.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message OriginConfig {
  // Origin domain name
  string domain_name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Origin path
  string origin_path = 2;

  // Origin protocol policy
  string protocol_policy = 3;

  // Custom headers to send to origin
  repeated gcommon.v1.common.KeyValue custom_headers = 4;
}
```

---

### rate_limit_config.proto {#rate_limit_config}

**Path**: `gcommon/v1/organization/rate_limit_config.proto` **Package**: `gcommon.v1.organization` **Lines**: 25

**Messages** (1): `OrganizationRateLimitConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/rate_limit_config.proto
// version: 1.0.0
// guid: cd85c64c-3fc8-4e12-a37f-b5171af08896

edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message OrganizationRateLimitConfig {
  // Maximum requests per minute
  int32 requests_per_minute = 1 [(buf.validate.field).int32.gte = 0];

  // Maximum requests per hour
  int32 requests_per_hour = 2 [(buf.validate.field).int32.gte = 0];

  // Maximum requests per day
  int32 requests_per_day = 3 [(buf.validate.field).int32.gte = 0];
}
```

---

### ssl_config.proto {#ssl_config}

**Path**: `gcommon/v1/organization/ssl_config.proto` **Package**: `gcommon.v1.organization` **Lines**: 28

**Messages** (1): `SSLConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/ssl_config.proto
// version: 1.0.0
// guid: 9945eeeb-d22e-4d57-a7f8-7e7220e847ce

edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message SSLConfig {
  // SSL certificate ARN or ID
  string certificate_id = 1 [(buf.validate.field).string.min_len = 1];

  // SSL policy
  string ssl_policy = 2 [(buf.validate.field).string.min_len = 1];

  // Whether to redirect HTTP to HTTPS
  bool redirect_http = 3;

  // Minimum TLS version
  string min_tls_version = 4 [(buf.validate.field).string.pattern = "^v?\\d+\\.\\d+\\.\\d+"];
}
```

---

### storage_backup_config.proto {#storage_backup_config}

**Path**: `gcommon/v1/organization/storage_backup_config.proto` **Package**: `gcommon.v1.organization` **Lines**: 31

**Messages** (1): `StorageBackupConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/storage_backup_config.proto
// version: 1.0.0
// guid: 374d573f-8428-4748-8c1a-65ccfb6995ad

edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message StorageBackupConfig {
  // Whether backup is enabled
  bool enabled = 1;

  // Backup schedule (cron expression)
  string schedule = 2 [(buf.validate.field).string.min_len = 1];

  // Backup retention period
  int32 retention_days = 3 [(buf.validate.field).int32.gte = 0];

  // Cross-region backup enabled
  bool cross_region = 4;

  // Backup encryption enabled
  bool encryption_enabled = 5;
}
```

---

### webhook_config.proto {#webhook_config}

**Path**: `gcommon/v1/organization/webhook_config.proto` **Package**: `gcommon.v1.organization` **Lines**: 28

**Messages** (1): `WebhookConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/webhook_config.proto
// version: 1.0.0
// guid: 831d7bab-450b-45fb-b41f-63cde7f89926

edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message WebhookConfig {
  // Webhook URL
  string url = 1 [(buf.validate.field).string.uri = true];

  // Events to trigger this webhook
  repeated string events = 2 [(buf.validate.field).repeated.min_items = 1];

  // Whether this webhook is active
  bool active = 3;

  // Webhook secret for signature verification
  string secret = 4 [(buf.validate.field).string.min_len = 1];
}
```

---

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

