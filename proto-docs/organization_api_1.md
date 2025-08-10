# organization_api_1 Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 50
- **Messages**: 50
- **Services**: 0
- **Enums**: 0

## Files in this Module

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

## Module Dependencies

**This module depends on**:

- [common](./common.md)
- [organization](./organization.md)
- [organization_config](./organization_config.md)

**Modules that depend on this one**:

- [organization_services](./organization_services.md)

---

## Detailed Documentation

### add_member_request.proto {#add_member_request}

**Path**: `pkg/organization/proto/add_member_request.proto` **Package**:
`gcommon.v1.organization` **Lines**: 27

**Messages** (1): `AddMemberRequest`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)
- `pkg/organization/proto/organization_member.proto` →
  [organization](./organization.md#organization_member)

#### Source Code

```protobuf
// file: pkg/organization/proto/requests/add_member_request.proto

edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";
import "pkg/organization/proto/organization_member.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

message AddMemberRequest {
  // Request metadata for tracing and context
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Organization identifier
  string organization_id = 2;

  // Member information to add
  gcommon.v1.organization.OrganizationMember member = 3;

  // Send invitation email if true
  bool send_invite = 4;
}

```

---

### add_member_response.proto {#add_member_response}

**Path**: `pkg/organization/proto/add_member_response.proto` **Package**:
`gcommon.v1.organization` **Lines**: 23

**Messages** (1): `AddMemberResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/organization/proto/organization_member.proto` →
  [organization](./organization.md#organization_member)

#### Source Code

```protobuf
// file: pkg/organization/proto/responses/add_member_response.proto
edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";
import "pkg/organization/proto/organization_member.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

message AddMemberResponse {
  // Any errors encountered
  repeated gcommon.v1.common.Error errors = 1;

  // Success status
  bool success = 2;

  // Newly added member information
  gcommon.v1.organization.OrganizationMember member = 3;
}

```

---

### create_department_request.proto {#create_department_request}

**Path**: `pkg/organization/proto/create_department_request.proto` **Package**:
`gcommon.v1.organization` **Lines**: 24

**Messages** (1): `CreateDepartmentRequest`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)
- `pkg/organization/proto/department.proto` →
  [organization](./organization.md#department)

#### Source Code

```protobuf
// file: pkg/organization/proto/requests/create_department_request.proto

edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";
import "pkg/organization/proto/department.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

message CreateDepartmentRequest {
  // Request metadata for tracing and context
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Department information to create
  gcommon.v1.organization.Department department = 2;

  // Validate only without persisting if true
  bool validate_only = 3;
}

```

---

### create_department_response.proto {#create_department_response}

**Path**: `pkg/organization/proto/create_department_response.proto` **Package**:
`gcommon.v1.organization` **Lines**: 23

**Messages** (1): `CreateDepartmentResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/organization/proto/department.proto` →
  [organization](./organization.md#department)

#### Source Code

```protobuf
// file: pkg/organization/proto/responses/create_department_response.proto
edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";
import "pkg/organization/proto/department.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

message CreateDepartmentResponse {
  // Any errors encountered
  repeated gcommon.v1.common.Error errors = 1;

  // Success status
  bool success = 2;

  // Newly created department information
  gcommon.v1.organization.Department department = 3;
}

```

---

### create_organization_request.proto {#create_organization_request}

**Path**: `pkg/organization/proto/create_organization_request.proto`
**Package**: `gcommon.v1.organization` **Lines**: 38

**Messages** (1): `CreateOrganizationRequest`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)
- `pkg/organization/proto/organization.proto` →
  [organization](./organization.md#organization)

#### Source Code

```protobuf
// file: pkg/organization/proto/create_organization_request.proto
// version: 1.0.0
// guid: 56789abc-def0-1234-5678-9abcdef01234

edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";
import "pkg/organization/proto/organization.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

message CreateOrganizationRequest {
  // Request metadata for tracing and context
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Organization information to create
  Organization organization = 2;

  // Whether to create a default tenant for this organization
  bool create_default_tenant = 3;

  // Initial organization settings (optional)
  string initial_settings_json = 4;

  // Owner user ID (will be added as organization owner)
  string owner_user_id = 5;

  // Whether to send welcome email to owner
  bool send_welcome_email = 6;

  // Template to use for organization creation (if applicable)
  string organization_template = 7;
}

```

---

### create_organization_response.proto {#create_organization_response}

**Path**: `pkg/organization/proto/create_organization_response.proto`
**Package**: `gcommon.v1.organization` **Lines**: 37

**Messages** (1): `CreateOrganizationResponse`

**Imports** (4):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/organization/proto/organization.proto` →
  [organization](./organization.md#organization)
- `pkg/organization/proto/tenant.proto` →
  [organization](./organization.md#tenant)

#### Source Code

```protobuf
// file: pkg/organization/proto/responses/create_organization_response.proto
edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";
import "pkg/organization/proto/organization.proto";
import "pkg/organization/proto/tenant.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

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
  string owner_member_id = 3;

  // Any errors encountered during creation
  repeated gcommon.v1.common.Error errors = 4;

  // Success status
  bool success = 5;

  // Additional information about the creation process
  string message = 6;
}

```

---

### create_team_request.proto {#create_team_request}

**Path**: `pkg/organization/proto/create_team_request.proto` **Package**:
`gcommon.v1.organization` **Lines**: 24

**Messages** (1): `CreateTeamRequest`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)
- `pkg/organization/proto/team.proto` → [organization](./organization.md#team)

#### Source Code

```protobuf
// file: pkg/organization/proto/requests/create_team_request.proto

edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";
import "pkg/organization/proto/team.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

message CreateTeamRequest {
  // Request metadata for tracing and context
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Team details to create
  gcommon.v1.organization.Team team = 2;

  // Validate only without persisting if true
  bool validate_only = 3;
}

```

---

### create_team_response.proto {#create_team_response}

**Path**: `pkg/organization/proto/create_team_response.proto` **Package**:
`gcommon.v1.organization` **Lines**: 23

**Messages** (1): `CreateTeamResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/organization/proto/team.proto` → [organization](./organization.md#team)

#### Source Code

```protobuf
// file: pkg/organization/proto/responses/create_team_response.proto
edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";
import "pkg/organization/proto/team.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

message CreateTeamResponse {
  // Any errors encountered
  repeated gcommon.v1.common.Error errors = 1;

  // Success status
  bool success = 2;

  // Newly created team information
  gcommon.v1.organization.Team team = 3;
}

```

---

### create_tenant_request.proto {#create_tenant_request}

**Path**: `pkg/organization/proto/create_tenant_request.proto` **Package**:
`gcommon.v1.organization` **Lines**: 23

**Messages** (1): `CreateTenantRequest`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)
- `pkg/organization/proto/tenant.proto` →
  [organization](./organization.md#tenant)

#### Source Code

```protobuf
// file: pkg/organization/proto/requests/create_tenant_request.proto

edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";
import "pkg/organization/proto/tenant.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

message CreateTenantRequest {
  // Request metadata for tracing and context
  gcommon.v1.common.RequestMetadata metadata = 1;
  // Tenant information to create
  gcommon.v1.organization.Tenant tenant = 2;

  // Validate only without persisting if true
  bool validate_only = 3;
}

```

---

### create_tenant_response.proto {#create_tenant_response}

**Path**: `pkg/organization/proto/create_tenant_response.proto` **Package**:
`gcommon.v1.organization` **Lines**: 23

**Messages** (1): `CreateTenantResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/organization/proto/tenant.proto` →
  [organization](./organization.md#tenant)

#### Source Code

```protobuf
// file: pkg/organization/proto/responses/create_tenant_response.proto
edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";
import "pkg/organization/proto/tenant.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

message CreateTenantResponse {
  // Any errors encountered
  repeated gcommon.v1.common.Error errors = 1;

  // Success status
  bool success = 2;

  // Newly created tenant details
  gcommon.v1.organization.Tenant tenant = 3;
}

```

---

### delete_department_request.proto {#delete_department_request}

**Path**: `pkg/organization/proto/delete_department_request.proto` **Package**:
`gcommon.v1.organization` **Lines**: 20

**Messages** (1): `DeleteDepartmentRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/organization/proto/requests/delete_department_request.proto

edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

message DeleteDepartmentRequest {
  // Request metadata for tracing and context
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Department identifier to delete
  string department_id = 2;
}

```

---

### delete_department_response.proto {#delete_department_response}

**Path**: `pkg/organization/proto/delete_department_response.proto` **Package**:
`gcommon.v1.organization` **Lines**: 19

**Messages** (1): `DeleteDepartmentResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)

#### Source Code

```protobuf
// file: pkg/organization/proto/responses/delete_department_response.proto
edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

message DeleteDepartmentResponse {
  // Any errors encountered
  repeated gcommon.v1.common.Error errors = 1;

  // Success status
  bool success = 2;
}

```

---

### delete_organization_request.proto {#delete_organization_request}

**Path**: `pkg/organization/proto/delete_organization_request.proto`
**Package**: `gcommon.v1.organization` **Lines**: 20

**Messages** (1): `DeleteOrganizationRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/organization/proto/requests/delete_organization_request.proto

edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

message DeleteOrganizationRequest {
  // Request metadata for tracing and context
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Organization identifier to delete
  string organization_id = 2;
}

```

---

### delete_organization_response.proto {#delete_organization_response}

**Path**: `pkg/organization/proto/delete_organization_response.proto`
**Package**: `gcommon.v1.organization` **Lines**: 19

**Messages** (1): `DeleteOrganizationResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)

#### Source Code

```protobuf
// file: pkg/organization/proto/responses/delete_organization_response.proto
edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

message DeleteOrganizationResponse {
  // Any errors encountered
  repeated gcommon.v1.common.Error errors = 1;

  // Success status
  bool success = 2;
}

```

---

### delete_team_request.proto {#delete_team_request}

**Path**: `pkg/organization/proto/delete_team_request.proto` **Package**:
`gcommon.v1.organization` **Lines**: 23

**Messages** (1): `DeleteTeamRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/organization/proto/requests/delete_team_request.proto

edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

message DeleteTeamRequest {
  // Request metadata for tracing and context
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Identifier of the team to delete
  string team_id = 2;

  // Force delete even if team has members
  bool force = 3;
}

```

---

### delete_team_response.proto {#delete_team_response}

**Path**: `pkg/organization/proto/delete_team_response.proto` **Package**:
`gcommon.v1.organization` **Lines**: 19

**Messages** (1): `DeleteTeamResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)

#### Source Code

```protobuf
// file: pkg/organization/proto/responses/delete_team_response.proto
edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

message DeleteTeamResponse {
  // Any errors encountered
  repeated gcommon.v1.common.Error errors = 1;

  // Success status
  bool success = 2;
}

```

---

### delete_tenant_request.proto {#delete_tenant_request}

**Path**: `pkg/organization/proto/delete_tenant_request.proto` **Package**:
`gcommon.v1.organization` **Lines**: 20

**Messages** (1): `DeleteTenantRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/organization/proto/requests/delete_tenant_request.proto

edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

message DeleteTenantRequest {
  // Request metadata for tracing and context
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Tenant identifier to delete
  string tenant_id = 2;
}

```

---

### delete_tenant_response.proto {#delete_tenant_response}

**Path**: `pkg/organization/proto/delete_tenant_response.proto` **Package**:
`gcommon.v1.organization` **Lines**: 19

**Messages** (1): `DeleteTenantResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)

#### Source Code

```protobuf
// file: pkg/organization/proto/responses/delete_tenant_response.proto
edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

message DeleteTenantResponse {
  // Any errors encountered
  repeated gcommon.v1.common.Error errors = 1;

  // Success status
  bool success = 2;
}

```

---

### get_department_request.proto {#get_department_request}

**Path**: `pkg/organization/proto/get_department_request.proto` **Package**:
`gcommon.v1.organization` **Lines**: 20

**Messages** (1): `GetDepartmentRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/organization/proto/requests/get_department_request.proto

edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

message GetDepartmentRequest {
  // Request metadata for tracing and context
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Department identifier
  string department_id = 2;
}

```

---

### get_department_response.proto {#get_department_response}

**Path**: `pkg/organization/proto/get_department_response.proto` **Package**:
`gcommon.v1.organization` **Lines**: 23

**Messages** (1): `GetDepartmentResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/organization/proto/department.proto` →
  [organization](./organization.md#department)

#### Source Code

```protobuf
// file: pkg/organization/proto/responses/get_department_response.proto
edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";
import "pkg/organization/proto/department.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

message GetDepartmentResponse {
  // Any errors encountered
  repeated gcommon.v1.common.Error errors = 1;

  // Success status
  bool success = 2;

  // Department information
  gcommon.v1.organization.Department department = 3;
}

```

---

### get_hierarchy_request.proto {#get_hierarchy_request}

**Path**: `pkg/organization/proto/get_hierarchy_request.proto` **Package**:
`gcommon.v1.organization` **Lines**: 23

**Messages** (1): `GetHierarchyRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/organization/proto/requests/get_hierarchy_request.proto

edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

message GetHierarchyRequest {
  // Request metadata for tracing and context
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Organization identifier
  string organization_id = 2;

  // Hierarchy identifier
  string hierarchy_id = 3;
}

```

---

### get_hierarchy_response.proto {#get_hierarchy_response}

**Path**: `pkg/organization/proto/get_hierarchy_response.proto` **Package**:
`gcommon.v1.organization` **Lines**: 23

**Messages** (1): `GetHierarchyResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/organization/proto/organization_hierarchy.proto` →
  [organization](./organization.md#organization_hierarchy)

#### Source Code

```protobuf
// file: pkg/organization/proto/responses/get_hierarchy_response.proto
edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";
import "pkg/organization/proto/organization_hierarchy.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

message GetHierarchyResponse {
  // Any errors encountered
  repeated gcommon.v1.common.Error errors = 1;

  // Success status
  bool success = 2;

  // Retrieved hierarchy data
  gcommon.v1.organization.OrganizationHierarchy hierarchy = 3 [lazy = true];
}

```

---

### get_organization_request.proto {#get_organization_request}

**Path**: `pkg/organization/proto/get_organization_request.proto` **Package**:
`gcommon.v1.organization` **Lines**: 29

**Messages** (1): `GetOrganizationRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/organization/proto/requests/get_organization_request.proto

edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

message GetOrganizationRequest {
  // Request metadata for tracing and context
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Organization ID to retrieve
  string organization_id = 2;

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

**Path**: `pkg/organization/proto/get_organization_response.proto` **Package**:
`gcommon.v1.organization` **Lines**: 40

**Messages** (1): `GetOrganizationResponse`

**Imports** (5):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/organization/proto/organization.proto` →
  [organization](./organization.md#organization)
- `pkg/organization/proto/organization_settings.proto` →
  [organization_config](./organization_config.md#organization_settings)
- `pkg/organization/proto/tenant.proto` →
  [organization](./organization.md#tenant)

#### Source Code

```protobuf
// file: pkg/organization/proto/get_organization_response.proto
// version: 1.0.0
// guid: 89012bcd-3456-789a-bcde-f01234567890

edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";
import "pkg/organization/proto/organization.proto";
import "pkg/organization/proto/organization_settings.proto";
import "pkg/organization/proto/tenant.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

/**
 * GetOrganizationResponse message returning organization information.
 */
message GetOrganizationResponse {
  // Organization information
  Organization organization = 1;

  // Organization settings (if requested)
  OrganizationSettings settings = 2;

  // Number of members in organization (if requested)
  int32 member_count = 3;

  // List of tenants in organization (if requested)
  repeated Tenant tenants = 4;

  // Any errors encountered during retrieval
  repeated gcommon.v1.common.Error errors = 5;

  // Success status
  bool success = 6;
}

```

---

### get_team_request.proto {#get_team_request}

**Path**: `pkg/organization/proto/get_team_request.proto` **Package**:
`gcommon.v1.organization` **Lines**: 20

**Messages** (1): `GetTeamRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/organization/proto/requests/get_team_request.proto

edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

message GetTeamRequest {
  // Request metadata for tracing and context
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Team identifier
  string team_id = 2;
}

```

---

### get_team_response.proto {#get_team_response}

**Path**: `pkg/organization/proto/get_team_response.proto` **Package**:
`gcommon.v1.organization` **Lines**: 23

**Messages** (1): `GetTeamResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/organization/proto/team.proto` → [organization](./organization.md#team)

#### Source Code

```protobuf
// file: pkg/organization/proto/responses/get_team_response.proto
edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";
import "pkg/organization/proto/team.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

message GetTeamResponse {
  // Any errors encountered
  repeated gcommon.v1.common.Error errors = 1;

  // Success status
  bool success = 2;

  // Team information
  gcommon.v1.organization.Team team = 3;
}

```

---

### get_tenant_isolation_request.proto {#get_tenant_isolation_request}

**Path**: `pkg/organization/proto/get_tenant_isolation_request.proto`
**Package**: `gcommon.v1.organization` **Lines**: 20

**Messages** (1): `GetTenantIsolationRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/organization/proto/requests/get_tenant_isolation_request.proto

edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

message GetTenantIsolationRequest {
  // Request metadata for tracing and context
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Tenant identifier
  string tenant_id = 2;
}

```

---

### get_tenant_isolation_response.proto {#get_tenant_isolation_response}

**Path**: `pkg/organization/proto/get_tenant_isolation_response.proto`
**Package**: `gcommon.v1.organization` **Lines**: 23

**Messages** (1): `GetTenantIsolationResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/organization/proto/tenant_isolation.proto` →
  [organization](./organization.md#tenant_isolation)

#### Source Code

```protobuf
// file: pkg/organization/proto/responses/get_tenant_isolation_response.proto
edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";
import "pkg/organization/proto/tenant_isolation.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

message GetTenantIsolationResponse {
  // Any errors encountered
  repeated gcommon.v1.common.Error errors = 1;

  // Success status
  bool success = 2;

  // Current isolation configuration
  gcommon.v1.organization.TenantIsolation isolation = 3 [lazy = true];
}

```

---

### get_tenant_request.proto {#get_tenant_request}

**Path**: `pkg/organization/proto/get_tenant_request.proto` **Package**:
`gcommon.v1.organization` **Lines**: 20

**Messages** (1): `GetTenantRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/organization/proto/requests/get_tenant_request.proto

edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

message GetTenantRequest {
  // Request metadata for tracing and context
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Tenant identifier
  string tenant_id = 2;
}

```

---

### get_tenant_response.proto {#get_tenant_response}

**Path**: `pkg/organization/proto/get_tenant_response.proto` **Package**:
`gcommon.v1.organization` **Lines**: 23

**Messages** (1): `GetTenantResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/organization/proto/tenant.proto` →
  [organization](./organization.md#tenant)

#### Source Code

```protobuf
// file: pkg/organization/proto/responses/get_tenant_response.proto
edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";
import "pkg/organization/proto/tenant.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

message GetTenantResponse {
  // Any errors encountered
  repeated gcommon.v1.common.Error errors = 1;

  // Success status
  bool success = 2;

  // Tenant information
  gcommon.v1.organization.Tenant tenant = 3;
}

```

---

### get_tenant_usage_request.proto {#get_tenant_usage_request}

**Path**: `pkg/organization/proto/get_tenant_usage_request.proto` **Package**:
`gcommon.v1.organization` **Lines**: 20

**Messages** (1): `GetTenantUsageRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/organization/proto/requests/get_tenant_usage_request.proto

edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

message GetTenantUsageRequest {
  // Request metadata for tracing and context
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Tenant identifier
  string tenant_id = 2;
}

```

---

### get_tenant_usage_response.proto {#get_tenant_usage_response}

**Path**: `pkg/organization/proto/get_tenant_usage_response.proto` **Package**:
`gcommon.v1.organization` **Lines**: 23

**Messages** (1): `GetTenantUsageResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/common/proto/key_value.proto` → [common](./common.md#key_value)

#### Source Code

```protobuf
// file: pkg/organization/proto/responses/get_tenant_usage_response.proto
edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";
import "pkg/common/proto/key_value.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

message GetTenantUsageResponse {
  // Any errors encountered
  repeated gcommon.v1.common.Error errors = 1;

  // Success status
  bool success = 2;

  // Usage statistics for the tenant
  repeated gcommon.v1.common.KeyValue usage_stats = 3 [lazy = true];
}

```

---

### list_departments_request.proto {#list_departments_request}

**Path**: `pkg/organization/proto/list_departments_request.proto` **Package**:
`gcommon.v1.organization` **Lines**: 29

**Messages** (1): `ListDepartmentsRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/organization/proto/requests/list_departments_request.proto

edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

message ListDepartmentsRequest {
  // Request metadata for tracing and context
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Organization identifier to list departments for
  string organization_id = 2;

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

**Path**: `pkg/organization/proto/list_departments_response.proto` **Package**:
`gcommon.v1.organization` **Lines**: 27

**Messages** (1): `ListDepartmentsResponse`

**Imports** (4):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/common/proto/paginated_response.proto` →
  [common](./common.md#paginated_response)
- `pkg/organization/proto/department.proto` →
  [organization](./organization.md#department)

#### Source Code

```protobuf
// file: pkg/organization/proto/responses/list_departments_response.proto
edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";
import "pkg/common/proto/paginated_response.proto";
import "pkg/organization/proto/department.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

message ListDepartmentsResponse {
  // Any errors encountered
  repeated gcommon.v1.common.Error errors = 1;

  // Success status
  bool success = 2;

  // List of departments returned
  repeated gcommon.v1.organization.Department departments = 3 [lazy = true];

  // Pagination metadata
  gcommon.v1.common.PaginatedResponse pagination = 4;
}

```

---

### list_members_request.proto {#list_members_request}

**Path**: `pkg/organization/proto/list_members_request.proto` **Package**:
`gcommon.v1.organization` **Lines**: 35

**Messages** (1): `ListMembersRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/organization/proto/requests/list_members_request.proto

edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

message ListMembersRequest {
  // Request metadata for tracing and context
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Organization identifier
  string organization_id = 2;

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

**Path**: `pkg/organization/proto/list_members_response.proto` **Package**:
`gcommon.v1.organization` **Lines**: 27

**Messages** (1): `ListMembersResponse`

**Imports** (4):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/common/proto/paginated_response.proto` →
  [common](./common.md#paginated_response)
- `pkg/organization/proto/organization_member.proto` →
  [organization](./organization.md#organization_member)

#### Source Code

```protobuf
// file: pkg/organization/proto/responses/list_members_response.proto
edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";
import "pkg/common/proto/paginated_response.proto";
import "pkg/organization/proto/organization_member.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

message ListMembersResponse {
  // Any errors encountered
  repeated gcommon.v1.common.Error errors = 1;

  // Success status
  bool success = 2;

  // List of members returned
  repeated gcommon.v1.organization.OrganizationMember members = 3 [lazy = true];

  // Pagination metadata
  gcommon.v1.common.PaginatedResponse pagination = 4;
}

```

---

### list_organizations_request.proto {#list_organizations_request}

**Path**: `pkg/organization/proto/list_organizations_request.proto` **Package**:
`gcommon.v1.organization` **Lines**: 26

**Messages** (1): `ListOrganizationsRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/organization/proto/requests/list_organizations_request.proto

edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

message ListOrganizationsRequest {
  // Request metadata for tracing and context
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Pagination size
  int32 page_size = 2;

  // Pagination token from previous response
  string page_token = 3;

  // Optional filter expression
  string filter = 4;
}

```

---

### list_organizations_response.proto {#list_organizations_response}

**Path**: `pkg/organization/proto/list_organizations_response.proto`
**Package**: `gcommon.v1.organization` **Lines**: 27

**Messages** (1): `ListOrganizationsResponse`

**Imports** (4):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/common/proto/paginated_response.proto` →
  [common](./common.md#paginated_response)
- `pkg/organization/proto/organization.proto` →
  [organization](./organization.md#organization)

#### Source Code

```protobuf
// file: pkg/organization/proto/responses/list_organizations_response.proto
edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";
import "pkg/common/proto/paginated_response.proto";
import "pkg/organization/proto/organization.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

message ListOrganizationsResponse {
  // Any errors encountered
  repeated gcommon.v1.common.Error errors = 1;

  // Success status
  bool success = 2;

  // List of organizations returned
  repeated gcommon.v1.organization.Organization organizations = 3 [lazy = true];

  // Pagination metadata
  gcommon.v1.common.PaginatedResponse pagination = 4;
}

```

---

### list_teams_request.proto {#list_teams_request}

**Path**: `pkg/organization/proto/list_teams_request.proto` **Package**:
`gcommon.v1.organization` **Lines**: 32

**Messages** (1): `ListTeamsRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/organization/proto/requests/list_teams_request.proto

edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

message ListTeamsRequest {
  // Request metadata for tracing and context
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Organization identifier
  string organization_id = 2;

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

**Path**: `pkg/organization/proto/list_teams_response.proto` **Package**:
`gcommon.v1.organization` **Lines**: 27

**Messages** (1): `ListTeamsResponse`

**Imports** (4):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/common/proto/paginated_response.proto` →
  [common](./common.md#paginated_response)
- `pkg/organization/proto/team.proto` → [organization](./organization.md#team)

#### Source Code

```protobuf
// file: pkg/organization/proto/responses/list_teams_response.proto
edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";
import "pkg/common/proto/paginated_response.proto";
import "pkg/organization/proto/team.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

message ListTeamsResponse {
  // Any errors encountered
  repeated gcommon.v1.common.Error errors = 1;

  // Success status
  bool success = 2;

  // List of teams returned
  repeated gcommon.v1.organization.Team teams = 3 [lazy = true];

  // Pagination metadata
  gcommon.v1.common.PaginatedResponse pagination = 4;
}

```

---

### list_tenants_request.proto {#list_tenants_request}

**Path**: `pkg/organization/proto/list_tenants_request.proto` **Package**:
`gcommon.v1.organization` **Lines**: 29

**Messages** (1): `ListTenantsRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/organization/proto/requests/list_tenants_request.proto

edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

message ListTenantsRequest {
  // Request metadata for tracing and context
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Organization identifier
  string organization_id = 2;

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

**Path**: `pkg/organization/proto/list_tenants_response.proto` **Package**:
`gcommon.v1.organization` **Lines**: 27

**Messages** (1): `ListTenantsResponse`

**Imports** (4):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/common/proto/paginated_response.proto` →
  [common](./common.md#paginated_response)
- `pkg/organization/proto/tenant.proto` →
  [organization](./organization.md#tenant)

#### Source Code

```protobuf
// file: pkg/organization/proto/responses/list_tenants_response.proto
edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";
import "pkg/common/proto/paginated_response.proto";
import "pkg/organization/proto/tenant.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

message ListTenantsResponse {
  // Any errors encountered
  repeated gcommon.v1.common.Error errors = 1;

  // Success status
  bool success = 2;

  // List of tenants returned
  repeated gcommon.v1.organization.Tenant tenants = 3 [lazy = true];

  // Pagination metadata
  gcommon.v1.common.PaginatedResponse pagination = 4;
}

```

---

### remove_member_request.proto {#remove_member_request}

**Path**: `pkg/organization/proto/remove_member_request.proto` **Package**:
`gcommon.v1.organization` **Lines**: 23

**Messages** (1): `RemoveMemberRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/organization/proto/requests/remove_member_request.proto

edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

message RemoveMemberRequest {
  // Request metadata for tracing and context
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Organization identifier
  string organization_id = 2;

  // Member identifier to remove
  string member_id = 3;
}

```

---

### remove_member_response.proto {#remove_member_response}

**Path**: `pkg/organization/proto/remove_member_response.proto` **Package**:
`gcommon.v1.organization` **Lines**: 19

**Messages** (1): `RemoveMemberResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)

#### Source Code

```protobuf
// file: pkg/organization/proto/responses/remove_member_response.proto
edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

message RemoveMemberResponse {
  // Any errors encountered
  repeated gcommon.v1.common.Error errors = 1;

  // Success status
  bool success = 2;
}

```

---

### update_department_request.proto {#update_department_request}

**Path**: `pkg/organization/proto/update_department_request.proto` **Package**:
`gcommon.v1.organization` **Lines**: 31

**Messages** (1): `UpdateDepartmentRequest`

**Imports** (4):

- `google/protobuf/field_mask.proto`
- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)
- `pkg/organization/proto/department.proto` →
  [organization](./organization.md#department)

#### Source Code

```protobuf
// file: pkg/organization/proto/requests/update_department_request.proto

edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/field_mask.proto";
import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";
import "pkg/organization/proto/department.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

message UpdateDepartmentRequest {
  // Request metadata for tracing and context
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Department identifier to update
  string department_id = 2;

  // Updated department information
  gcommon.v1.organization.Department department = 3;

  // Fields to update in partial mode
  google.protobuf.FieldMask update_mask = 4;

  // Validate only without persisting if true
  bool validate_only = 5;
}

```

---

### update_department_response.proto {#update_department_response}

**Path**: `pkg/organization/proto/update_department_response.proto` **Package**:
`gcommon.v1.organization` **Lines**: 23

**Messages** (1): `UpdateDepartmentResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/organization/proto/department.proto` →
  [organization](./organization.md#department)

#### Source Code

```protobuf
// file: pkg/organization/proto/responses/update_department_response.proto
edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";
import "pkg/organization/proto/department.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

message UpdateDepartmentResponse {
  // Any errors encountered
  repeated gcommon.v1.common.Error errors = 1;

  // Success status
  bool success = 2;

  // Updated department information
  gcommon.v1.organization.Department department = 3;
}

```

---

### update_hierarchy_request.proto {#update_hierarchy_request}

**Path**: `pkg/organization/proto/update_hierarchy_request.proto` **Package**:
`gcommon.v1.organization` **Lines**: 31

**Messages** (1): `UpdateHierarchyRequest`

**Imports** (4):

- `google/protobuf/field_mask.proto`
- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)
- `pkg/organization/proto/organization_hierarchy.proto` →
  [organization](./organization.md#organization_hierarchy)

#### Source Code

```protobuf
// file: pkg/organization/proto/requests/update_hierarchy_request.proto

edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/field_mask.proto";
import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";
import "pkg/organization/proto/organization_hierarchy.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

message UpdateHierarchyRequest {
  // Request metadata for tracing and context
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Organization identifier
  string organization_id = 2;

  // Updated hierarchy data
  gcommon.v1.organization.OrganizationHierarchy hierarchy = 3;

  // Fields to update
  google.protobuf.FieldMask update_mask = 4;

  // Validate only without persisting if true
  bool validate_only = 5;
}

```

---

### update_hierarchy_response.proto {#update_hierarchy_response}

**Path**: `pkg/organization/proto/update_hierarchy_response.proto` **Package**:
`gcommon.v1.organization` **Lines**: 23

**Messages** (1): `UpdateHierarchyResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/organization/proto/organization_hierarchy.proto` →
  [organization](./organization.md#organization_hierarchy)

#### Source Code

```protobuf
// file: pkg/organization/proto/responses/update_hierarchy_response.proto
edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";
import "pkg/organization/proto/organization_hierarchy.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

message UpdateHierarchyResponse {
  // Any errors encountered
  repeated gcommon.v1.common.Error errors = 1;

  // Success status
  bool success = 2;

  // Updated hierarchy data
  gcommon.v1.organization.OrganizationHierarchy hierarchy = 3 [lazy = true];
}

```

---

### update_member_request.proto {#update_member_request}

**Path**: `pkg/organization/proto/update_member_request.proto` **Package**:
`gcommon.v1.organization` **Lines**: 28

**Messages** (1): `UpdateMemberRequest`

**Imports** (4):

- `google/protobuf/field_mask.proto`
- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)
- `pkg/organization/proto/organization_member.proto` →
  [organization](./organization.md#organization_member)

#### Source Code

```protobuf
// file: pkg/organization/proto/requests/update_member_request.proto

edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/field_mask.proto";
import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";
import "pkg/organization/proto/organization_member.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

message UpdateMemberRequest {
  // Request metadata for tracing and context
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Identifier of the member to update
  string member_id = 2;

  // Updated member information
  gcommon.v1.organization.OrganizationMember member = 3;

  // Fields to update for partial updates
  google.protobuf.FieldMask update_mask = 4;
}

```

---

### update_member_response.proto {#update_member_response}

**Path**: `pkg/organization/proto/update_member_response.proto` **Package**:
`gcommon.v1.organization` **Lines**: 23

**Messages** (1): `UpdateMemberResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/organization/proto/organization_member.proto` →
  [organization](./organization.md#organization_member)

#### Source Code

```protobuf
// file: pkg/organization/proto/responses/update_member_response.proto
edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";
import "pkg/organization/proto/organization_member.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

message UpdateMemberResponse {
  // Any errors encountered
  repeated gcommon.v1.common.Error errors = 1;

  // Success status
  bool success = 2;

  // Updated member details
  gcommon.v1.organization.OrganizationMember member = 3;
}

```

---
