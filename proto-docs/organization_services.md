# organization_services Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 3
- **Messages**: 0
- **Services**: 3
- **Enums**: 0

## Files in this Module

- [hierarchy_service.proto](#hierarchy_service)
- [organization_service.proto](#organization_service)
- [tenant_service.proto](#tenant_service)

## Module Dependencies

**This module depends on**:

- [organization_api_1](./organization_api_1.md)
- [organization_api_2](./organization_api_2.md)
- [organization_config](./organization_config.md)

---

## Detailed Documentation

### hierarchy_service.proto {#hierarchy_service}

**Path**: `pkg/organization/proto/hierarchy_service.proto` **Package**:
`gcommon.v1.organization` **Lines**: 77

**Services** (1): `HierarchyService`

**Imports** (25):

- `google/protobuf/go_features.proto`
- `pkg/organization/proto/create_department_request.proto` →
  [organization_api_1](./organization_api_1.md#create_department_request)
- `pkg/organization/proto/create_department_response.proto` →
  [organization_api_1](./organization_api_1.md#create_department_response)
- `pkg/organization/proto/create_team_request.proto` →
  [organization_api_1](./organization_api_1.md#create_team_request)
- `pkg/organization/proto/create_team_response.proto` →
  [organization_api_1](./organization_api_1.md#create_team_response)
- `pkg/organization/proto/delete_department_request.proto` →
  [organization_api_1](./organization_api_1.md#delete_department_request)
- `pkg/organization/proto/delete_department_response.proto` →
  [organization_api_1](./organization_api_1.md#delete_department_response)
- `pkg/organization/proto/delete_team_request.proto` →
  [organization_api_1](./organization_api_1.md#delete_team_request)
- `pkg/organization/proto/delete_team_response.proto` →
  [organization_api_1](./organization_api_1.md#delete_team_response)
- `pkg/organization/proto/get_department_request.proto` →
  [organization_api_1](./organization_api_1.md#get_department_request)
- `pkg/organization/proto/get_department_response.proto` →
  [organization_api_1](./organization_api_1.md#get_department_response)
- `pkg/organization/proto/get_hierarchy_request.proto` →
  [organization_api_1](./organization_api_1.md#get_hierarchy_request)
- `pkg/organization/proto/get_hierarchy_response.proto` →
  [organization_api_1](./organization_api_1.md#get_hierarchy_response)
- `pkg/organization/proto/get_team_request.proto` →
  [organization_api_1](./organization_api_1.md#get_team_request)
- `pkg/organization/proto/get_team_response.proto` →
  [organization_api_1](./organization_api_1.md#get_team_response)
- `pkg/organization/proto/list_departments_request.proto` →
  [organization_api_1](./organization_api_1.md#list_departments_request)
- `pkg/organization/proto/list_departments_response.proto` →
  [organization_api_1](./organization_api_1.md#list_departments_response)
- `pkg/organization/proto/list_teams_request.proto` →
  [organization_api_1](./organization_api_1.md#list_teams_request)
- `pkg/organization/proto/list_teams_response.proto` →
  [organization_api_1](./organization_api_1.md#list_teams_response)
- `pkg/organization/proto/update_department_request.proto` →
  [organization_api_1](./organization_api_1.md#update_department_request)
- `pkg/organization/proto/update_department_response.proto` →
  [organization_api_1](./organization_api_1.md#update_department_response)
- `pkg/organization/proto/update_hierarchy_request.proto` →
  [organization_api_1](./organization_api_1.md#update_hierarchy_request)
- `pkg/organization/proto/update_hierarchy_response.proto` →
  [organization_api_1](./organization_api_1.md#update_hierarchy_response)
- `pkg/organization/proto/update_team_request.proto` →
  [organization_api_2](./organization_api_2.md#update_team_request)
- `pkg/organization/proto/update_team_response.proto` →
  [organization_api_2](./organization_api_2.md#update_team_response)

#### Source Code

```protobuf
// file: pkg/organization/proto/services/hierarchy_service.proto
edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "pkg/organization/proto/create_department_request.proto";
import "pkg/organization/proto/create_department_response.proto";
import "pkg/organization/proto/create_team_request.proto";
import "pkg/organization/proto/create_team_response.proto";
import "pkg/organization/proto/delete_department_request.proto";
import "pkg/organization/proto/delete_department_response.proto";
import "pkg/organization/proto/delete_team_request.proto";
import "pkg/organization/proto/delete_team_response.proto";
import "pkg/organization/proto/get_department_request.proto";
import "pkg/organization/proto/get_department_response.proto";
import "pkg/organization/proto/get_hierarchy_request.proto";
import "pkg/organization/proto/get_hierarchy_response.proto";
import "pkg/organization/proto/get_team_request.proto";
import "pkg/organization/proto/get_team_response.proto";
import "pkg/organization/proto/list_departments_request.proto";
import "pkg/organization/proto/list_departments_response.proto";
import "pkg/organization/proto/list_teams_request.proto";
import "pkg/organization/proto/list_teams_response.proto";
import "pkg/organization/proto/update_department_request.proto";
import "pkg/organization/proto/update_department_response.proto";
import "pkg/organization/proto/update_hierarchy_request.proto";
import "pkg/organization/proto/update_hierarchy_response.proto";
import "pkg/organization/proto/update_team_request.proto";
import "pkg/organization/proto/update_team_response.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

/**
 * HierarchyService provides comprehensive organizational hierarchy management.
 * Handles department and team operations, hierarchical relationships,
 * and organizational structure administration.
 */
service HierarchyService {
  // Create a new department
  rpc CreateDepartment(CreateDepartmentRequest) returns (CreateDepartmentResponse);

  // Get a department by ID
  rpc GetDepartment(GetDepartmentRequest) returns (GetDepartmentResponse);

  // Update an existing department
  rpc UpdateDepartment(UpdateDepartmentRequest) returns (UpdateDepartmentResponse);

  // Delete a department (soft delete)
  rpc DeleteDepartment(DeleteDepartmentRequest) returns (DeleteDepartmentResponse);

  // List departments within an organization (with pagination and filtering)
  rpc ListDepartments(ListDepartmentsRequest) returns (ListDepartmentsResponse);

  // Create a new team
  rpc CreateTeam(CreateTeamRequest) returns (CreateTeamResponse);

  // Get a team by ID
  rpc GetTeam(GetTeamRequest) returns (GetTeamResponse);

  // Update an existing team
  rpc UpdateTeam(UpdateTeamRequest) returns (UpdateTeamResponse);

  // Delete a team (soft delete)
  rpc DeleteTeam(DeleteTeamRequest) returns (DeleteTeamResponse);

  // List teams within an organization or department (with pagination and filtering)
  rpc ListTeams(ListTeamsRequest) returns (ListTeamsResponse);

  // Get organizational hierarchy structure
  rpc GetHierarchy(GetHierarchyRequest) returns (GetHierarchyResponse);

  // Update organizational hierarchy structure
  rpc UpdateHierarchy(UpdateHierarchyRequest) returns (UpdateHierarchyResponse);
}

```

---

### organization_service.proto {#organization_service}

**Path**: `pkg/organization/proto/organization_service.proto` **Package**:
`gcommon.v1.organization` **Lines**: 72

**Services** (1): `OrganizationService`

**Imports** (23):

- `google/protobuf/go_features.proto`
- `pkg/organization/proto/add_member_request.proto` →
  [organization_api_1](./organization_api_1.md#add_member_request)
- `pkg/organization/proto/add_member_response.proto` →
  [organization_api_1](./organization_api_1.md#add_member_response)
- `pkg/organization/proto/create_organization_request.proto` →
  [organization_api_1](./organization_api_1.md#create_organization_request)
- `pkg/organization/proto/create_organization_response.proto` →
  [organization_api_1](./organization_api_1.md#create_organization_response)
- `pkg/organization/proto/delete_organization_request.proto` →
  [organization_api_1](./organization_api_1.md#delete_organization_request)
- `pkg/organization/proto/delete_organization_response.proto` →
  [organization_api_1](./organization_api_1.md#delete_organization_response)
- `pkg/organization/proto/get_organization_request.proto` →
  [organization_api_1](./organization_api_1.md#get_organization_request)
- `pkg/organization/proto/get_organization_response.proto` →
  [organization_api_1](./organization_api_1.md#get_organization_response)
- `pkg/organization/proto/get_organization_settings_request.proto` →
  [organization_config](./organization_config.md#get_organization_settings_request)
- `pkg/organization/proto/get_organization_settings_response.proto` →
  [organization_config](./organization_config.md#get_organization_settings_response)
- `pkg/organization/proto/list_members_request.proto` →
  [organization_api_1](./organization_api_1.md#list_members_request)
- `pkg/organization/proto/list_members_response.proto` →
  [organization_api_1](./organization_api_1.md#list_members_response)
- `pkg/organization/proto/list_organizations_request.proto` →
  [organization_api_1](./organization_api_1.md#list_organizations_request)
- `pkg/organization/proto/list_organizations_response.proto` →
  [organization_api_1](./organization_api_1.md#list_organizations_response)
- `pkg/organization/proto/remove_member_request.proto` →
  [organization_api_1](./organization_api_1.md#remove_member_request)
- `pkg/organization/proto/remove_member_response.proto` →
  [organization_api_1](./organization_api_1.md#remove_member_response)
- `pkg/organization/proto/update_member_request.proto` →
  [organization_api_1](./organization_api_1.md#update_member_request)
- `pkg/organization/proto/update_member_response.proto` →
  [organization_api_1](./organization_api_1.md#update_member_response)
- `pkg/organization/proto/update_organization_request.proto` →
  [organization_api_2](./organization_api_2.md#update_organization_request)
- `pkg/organization/proto/update_organization_response.proto` →
  [organization_api_2](./organization_api_2.md#update_organization_response)
- `pkg/organization/proto/update_organization_settings_request.proto` →
  [organization_config](./organization_config.md#update_organization_settings_request)
- `pkg/organization/proto/update_organization_settings_response.proto` →
  [organization_config](./organization_config.md#update_organization_settings_response)

#### Source Code

```protobuf
// file: pkg/organization/proto/services/organization_service.proto
edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "pkg/organization/proto/add_member_request.proto";
import "pkg/organization/proto/add_member_response.proto";
import "pkg/organization/proto/create_organization_request.proto";
import "pkg/organization/proto/create_organization_response.proto";
import "pkg/organization/proto/delete_organization_request.proto";
import "pkg/organization/proto/delete_organization_response.proto";
import "pkg/organization/proto/get_organization_request.proto";
import "pkg/organization/proto/get_organization_response.proto";
import "pkg/organization/proto/get_organization_settings_request.proto";
import "pkg/organization/proto/get_organization_settings_response.proto";
import "pkg/organization/proto/list_members_request.proto";
import "pkg/organization/proto/list_members_response.proto";
import "pkg/organization/proto/list_organizations_request.proto";
import "pkg/organization/proto/list_organizations_response.proto";
import "pkg/organization/proto/remove_member_request.proto";
import "pkg/organization/proto/remove_member_response.proto";
import "pkg/organization/proto/update_member_request.proto";
import "pkg/organization/proto/update_member_response.proto";
import "pkg/organization/proto/update_organization_request.proto";
import "pkg/organization/proto/update_organization_response.proto";
import "pkg/organization/proto/update_organization_settings_request.proto";
import "pkg/organization/proto/update_organization_settings_response.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

/**
 * OrganizationService provides comprehensive organization management capabilities.
 * Handles organization CRUD operations, member management, settings configuration,
 * and organizational structure administration.
 */
service OrganizationService {
  // Create a new organization
  rpc CreateOrganization(CreateOrganizationRequest) returns (CreateOrganizationResponse);

  // Get an organization by ID
  rpc GetOrganization(GetOrganizationRequest) returns (GetOrganizationResponse);

  // Update an existing organization
  rpc UpdateOrganization(UpdateOrganizationRequest) returns (UpdateOrganizationResponse);

  // Delete an organization (soft delete)
  rpc DeleteOrganization(DeleteOrganizationRequest) returns (DeleteOrganizationResponse);

  // List organizations (with pagination and filtering)
  rpc ListOrganizations(ListOrganizationsRequest) returns (ListOrganizationsResponse);

  // Add a member to an organization
  rpc AddMember(AddMemberRequest) returns (AddMemberResponse);

  // Remove a member from an organization
  rpc RemoveMember(RemoveMemberRequest) returns (RemoveMemberResponse);

  // Update a member's information or permissions
  rpc UpdateMember(UpdateMemberRequest) returns (UpdateMemberResponse);

  // List organization members (with pagination and filtering)
  rpc ListMembers(ListMembersRequest) returns (ListMembersResponse);

  // Get organization settings
  rpc GetOrganizationSettings(GetOrganizationSettingsRequest) returns (GetOrganizationSettingsResponse);

  // Update organization settings
  rpc UpdateOrganizationSettings(UpdateOrganizationSettingsRequest) returns (UpdateOrganizationSettingsResponse);
}

```

---

### tenant_service.proto {#tenant_service}

**Path**: `pkg/organization/proto/tenant_service.proto` **Package**:
`gcommon.v1.organization` **Lines**: 62

**Services** (1): `TenantService`

**Imports** (19):

- `google/protobuf/go_features.proto`
- `pkg/organization/proto/configure_tenant_isolation_request.proto` →
  [organization_config](./organization_config.md#configure_tenant_isolation_request)
- `pkg/organization/proto/configure_tenant_isolation_response.proto` →
  [organization_config](./organization_config.md#configure_tenant_isolation_response)
- `pkg/organization/proto/create_tenant_request.proto` →
  [organization_api_1](./organization_api_1.md#create_tenant_request)
- `pkg/organization/proto/create_tenant_response.proto` →
  [organization_api_1](./organization_api_1.md#create_tenant_response)
- `pkg/organization/proto/delete_tenant_request.proto` →
  [organization_api_1](./organization_api_1.md#delete_tenant_request)
- `pkg/organization/proto/delete_tenant_response.proto` →
  [organization_api_1](./organization_api_1.md#delete_tenant_response)
- `pkg/organization/proto/get_tenant_isolation_request.proto` →
  [organization_api_1](./organization_api_1.md#get_tenant_isolation_request)
- `pkg/organization/proto/get_tenant_isolation_response.proto` →
  [organization_api_1](./organization_api_1.md#get_tenant_isolation_response)
- `pkg/organization/proto/get_tenant_request.proto` →
  [organization_api_1](./organization_api_1.md#get_tenant_request)
- `pkg/organization/proto/get_tenant_response.proto` →
  [organization_api_1](./organization_api_1.md#get_tenant_response)
- `pkg/organization/proto/get_tenant_usage_request.proto` →
  [organization_api_1](./organization_api_1.md#get_tenant_usage_request)
- `pkg/organization/proto/get_tenant_usage_response.proto` →
  [organization_api_1](./organization_api_1.md#get_tenant_usage_response)
- `pkg/organization/proto/list_tenants_request.proto` →
  [organization_api_1](./organization_api_1.md#list_tenants_request)
- `pkg/organization/proto/list_tenants_response.proto` →
  [organization_api_1](./organization_api_1.md#list_tenants_response)
- `pkg/organization/proto/update_tenant_quota_request.proto` →
  [organization_api_2](./organization_api_2.md#update_tenant_quota_request)
- `pkg/organization/proto/update_tenant_quota_response.proto` →
  [organization_api_2](./organization_api_2.md#update_tenant_quota_response)
- `pkg/organization/proto/update_tenant_request.proto` →
  [organization_api_2](./organization_api_2.md#update_tenant_request)
- `pkg/organization/proto/update_tenant_response.proto` →
  [organization_api_2](./organization_api_2.md#update_tenant_response)

#### Source Code

```protobuf
// file: pkg/organization/proto/services/tenant_service.proto
edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "pkg/organization/proto/configure_tenant_isolation_request.proto";
import "pkg/organization/proto/configure_tenant_isolation_response.proto";
import "pkg/organization/proto/create_tenant_request.proto";
import "pkg/organization/proto/create_tenant_response.proto";
import "pkg/organization/proto/delete_tenant_request.proto";
import "pkg/organization/proto/delete_tenant_response.proto";
import "pkg/organization/proto/get_tenant_isolation_request.proto";
import "pkg/organization/proto/get_tenant_isolation_response.proto";
import "pkg/organization/proto/get_tenant_request.proto";
import "pkg/organization/proto/get_tenant_response.proto";
import "pkg/organization/proto/get_tenant_usage_request.proto";
import "pkg/organization/proto/get_tenant_usage_response.proto";
import "pkg/organization/proto/list_tenants_request.proto";
import "pkg/organization/proto/list_tenants_response.proto";
import "pkg/organization/proto/update_tenant_quota_request.proto";
import "pkg/organization/proto/update_tenant_quota_response.proto";
import "pkg/organization/proto/update_tenant_request.proto";
import "pkg/organization/proto/update_tenant_response.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

/**
 * TenantService provides comprehensive tenant management capabilities.
 * Handles tenant CRUD operations, isolation configuration, quota management,
 * and multi-tenant resource administration.
 */
service TenantService {
  // Create a new tenant within an organization
  rpc CreateTenant(CreateTenantRequest) returns (CreateTenantResponse);

  // Get a tenant by ID
  rpc GetTenant(GetTenantRequest) returns (GetTenantResponse);

  // Update an existing tenant
  rpc UpdateTenant(UpdateTenantRequest) returns (UpdateTenantResponse);

  // Delete a tenant (soft delete)
  rpc DeleteTenant(DeleteTenantRequest) returns (DeleteTenantResponse);

  // List tenants within an organization (with pagination and filtering)
  rpc ListTenants(ListTenantsRequest) returns (ListTenantsResponse);

  // Configure tenant isolation settings
  rpc ConfigureTenantIsolation(ConfigureTenantIsolationRequest) returns (ConfigureTenantIsolationResponse);

  // Get tenant isolation configuration
  rpc GetTenantIsolation(GetTenantIsolationRequest) returns (GetTenantIsolationResponse);

  // Update tenant resource quotas
  rpc UpdateTenantQuota(UpdateTenantQuotaRequest) returns (UpdateTenantQuotaResponse);

  // Get tenant resource usage statistics
  rpc GetTenantUsage(GetTenantUsageRequest) returns (GetTenantUsageResponse);
}

```

---
