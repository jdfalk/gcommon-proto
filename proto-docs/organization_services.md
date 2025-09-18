# Organization Services Documentation

[← Back to Index](./README.md)

## Module Overview

- **Proto Files**: 3
- **Services**: 3

## Table of Contents

### Services

- [`HierarchyService`](#hierarchy_service) - from hierarchy_service.proto
- [`OrganizationService`](#organization_service) - from organization_service.proto
- [`TenantService`](#tenant_service) - from tenant_service.proto

### Files in this Module

- [hierarchy_service.proto](#hierarchy_service)
- [organization_service.proto](#organization_service)
- [tenant_service.proto](#tenant_service)

---

## Services Documentation

### hierarchy_service.proto {#hierarchy_service}

**Path**: `gcommon/v1/organization/hierarchy_service.proto` **Package**: `gcommon.v1.organization` **Lines**: 78

**Services** (1): `HierarchyService`

**Imports** (25):

- `gcommon/v1/organization/create_department_request.proto`
- `gcommon/v1/organization/create_department_response.proto`
- `gcommon/v1/organization/create_team_request.proto`
- `gcommon/v1/organization/create_team_response.proto`
- `gcommon/v1/organization/delete_department_request.proto`
- `gcommon/v1/organization/delete_department_response.proto`
- `gcommon/v1/organization/delete_team_request.proto`
- `gcommon/v1/organization/delete_team_response.proto`
- `gcommon/v1/organization/get_department_request.proto`
- `gcommon/v1/organization/get_department_response.proto`
- `gcommon/v1/organization/get_hierarchy_request.proto`
- `gcommon/v1/organization/get_hierarchy_response.proto`
- `gcommon/v1/organization/get_team_request.proto`
- `gcommon/v1/organization/get_team_response.proto`
- `gcommon/v1/organization/list_departments_request.proto`
- `gcommon/v1/organization/list_departments_response.proto`
- `gcommon/v1/organization/list_teams_request.proto`
- `gcommon/v1/organization/list_teams_response.proto`
- `gcommon/v1/organization/update_department_request.proto`
- `gcommon/v1/organization/update_department_response.proto`
- `gcommon/v1/organization/update_hierarchy_request.proto`
- `gcommon/v1/organization/update_hierarchy_response.proto`
- `gcommon/v1/organization/update_team_request.proto`
- `gcommon/v1/organization/update_team_response.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/hierarchy_service.proto
// version: 1.0.1
// guid: 93046f12-5400-4c2e-b2c2-d6707242bcdf
edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/organization/create_department_request.proto";
import "gcommon/v1/organization/create_department_response.proto";
import "gcommon/v1/organization/create_team_request.proto";
import "gcommon/v1/organization/create_team_response.proto";
import "gcommon/v1/organization/delete_department_request.proto";
import "gcommon/v1/organization/delete_department_response.proto";
import "gcommon/v1/organization/delete_team_request.proto";
import "gcommon/v1/organization/delete_team_response.proto";
import "gcommon/v1/organization/get_department_request.proto";
import "gcommon/v1/organization/get_department_response.proto";
import "gcommon/v1/organization/get_hierarchy_request.proto";
import "gcommon/v1/organization/get_hierarchy_response.proto";
import "gcommon/v1/organization/get_team_request.proto";
import "gcommon/v1/organization/get_team_response.proto";
import "gcommon/v1/organization/list_departments_request.proto";
import "gcommon/v1/organization/list_departments_response.proto";
import "gcommon/v1/organization/list_teams_request.proto";
import "gcommon/v1/organization/list_teams_response.proto";
import "gcommon/v1/organization/update_department_request.proto";
import "gcommon/v1/organization/update_department_response.proto";
import "gcommon/v1/organization/update_hierarchy_request.proto";
import "gcommon/v1/organization/update_hierarchy_response.proto";
import "gcommon/v1/organization/update_team_request.proto";
import "gcommon/v1/organization/update_team_response.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

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

**Path**: `gcommon/v1/organization/organization_service.proto` **Package**: `gcommon.v1.organization` **Lines**: 73

**Services** (1): `OrganizationService`

**Imports** (23):

- `gcommon/v1/organization/add_member_request.proto`
- `gcommon/v1/organization/add_member_response.proto`
- `gcommon/v1/organization/create_organization_request.proto`
- `gcommon/v1/organization/create_organization_response.proto`
- `gcommon/v1/organization/delete_organization_request.proto`
- `gcommon/v1/organization/delete_organization_response.proto`
- `gcommon/v1/organization/get_organization_request.proto`
- `gcommon/v1/organization/get_organization_response.proto`
- `gcommon/v1/organization/get_organization_settings_request.proto`
- `gcommon/v1/organization/get_organization_settings_response.proto`
- `gcommon/v1/organization/list_members_request.proto`
- `gcommon/v1/organization/list_members_response.proto`
- `gcommon/v1/organization/list_organizations_request.proto`
- `gcommon/v1/organization/list_organizations_response.proto`
- `gcommon/v1/organization/remove_member_request.proto`
- `gcommon/v1/organization/remove_member_response.proto`
- `gcommon/v1/organization/update_member_request.proto`
- `gcommon/v1/organization/update_member_response.proto`
- `gcommon/v1/organization/update_organization_request.proto`
- `gcommon/v1/organization/update_organization_response.proto`
- `gcommon/v1/organization/update_organization_settings_request.proto`
- `gcommon/v1/organization/update_organization_settings_response.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/organization_service.proto
// version: 1.0.1
// guid: 7a327e8c-286f-4bf2-9d3d-7917e6de4f86
edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/organization/add_member_request.proto";
import "gcommon/v1/organization/add_member_response.proto";
import "gcommon/v1/organization/create_organization_request.proto";
import "gcommon/v1/organization/create_organization_response.proto";
import "gcommon/v1/organization/delete_organization_request.proto";
import "gcommon/v1/organization/delete_organization_response.proto";
import "gcommon/v1/organization/get_organization_request.proto";
import "gcommon/v1/organization/get_organization_response.proto";
import "gcommon/v1/organization/get_organization_settings_request.proto";
import "gcommon/v1/organization/get_organization_settings_response.proto";
import "gcommon/v1/organization/list_members_request.proto";
import "gcommon/v1/organization/list_members_response.proto";
import "gcommon/v1/organization/list_organizations_request.proto";
import "gcommon/v1/organization/list_organizations_response.proto";
import "gcommon/v1/organization/remove_member_request.proto";
import "gcommon/v1/organization/remove_member_response.proto";
import "gcommon/v1/organization/update_member_request.proto";
import "gcommon/v1/organization/update_member_response.proto";
import "gcommon/v1/organization/update_organization_request.proto";
import "gcommon/v1/organization/update_organization_response.proto";
import "gcommon/v1/organization/update_organization_settings_request.proto";
import "gcommon/v1/organization/update_organization_settings_response.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

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

**Path**: `gcommon/v1/organization/tenant_service.proto` **Package**: `gcommon.v1.organization` **Lines**: 63

**Services** (1): `TenantService`

**Imports** (19):

- `gcommon/v1/organization/configure_tenant_isolation_request.proto`
- `gcommon/v1/organization/configure_tenant_isolation_response.proto`
- `gcommon/v1/organization/create_tenant_request.proto`
- `gcommon/v1/organization/create_tenant_response.proto`
- `gcommon/v1/organization/delete_tenant_request.proto`
- `gcommon/v1/organization/delete_tenant_response.proto`
- `gcommon/v1/organization/get_tenant_isolation_request.proto`
- `gcommon/v1/organization/get_tenant_isolation_response.proto`
- `gcommon/v1/organization/get_tenant_request.proto`
- `gcommon/v1/organization/get_tenant_response.proto`
- `gcommon/v1/organization/get_tenant_usage_request.proto`
- `gcommon/v1/organization/get_tenant_usage_response.proto`
- `gcommon/v1/organization/list_tenants_request.proto`
- `gcommon/v1/organization/list_tenants_response.proto`
- `gcommon/v1/organization/update_tenant_quota_request.proto`
- `gcommon/v1/organization/update_tenant_quota_response.proto`
- `gcommon/v1/organization/update_tenant_request.proto`
- `gcommon/v1/organization/update_tenant_response.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/tenant_service.proto
// version: 1.0.1
// guid: 56bd37e6-4e4a-4a15-82a6-b392bed64d95
edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/organization/configure_tenant_isolation_request.proto";
import "gcommon/v1/organization/configure_tenant_isolation_response.proto";
import "gcommon/v1/organization/create_tenant_request.proto";
import "gcommon/v1/organization/create_tenant_response.proto";
import "gcommon/v1/organization/delete_tenant_request.proto";
import "gcommon/v1/organization/delete_tenant_response.proto";
import "gcommon/v1/organization/get_tenant_isolation_request.proto";
import "gcommon/v1/organization/get_tenant_isolation_response.proto";
import "gcommon/v1/organization/get_tenant_request.proto";
import "gcommon/v1/organization/get_tenant_response.proto";
import "gcommon/v1/organization/get_tenant_usage_request.proto";
import "gcommon/v1/organization/get_tenant_usage_response.proto";
import "gcommon/v1/organization/list_tenants_request.proto";
import "gcommon/v1/organization/list_tenants_response.proto";
import "gcommon/v1/organization/update_tenant_quota_request.proto";
import "gcommon/v1/organization/update_tenant_quota_response.proto";
import "gcommon/v1/organization/update_tenant_request.proto";
import "gcommon/v1/organization/update_tenant_response.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

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
