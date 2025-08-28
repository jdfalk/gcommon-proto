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
---


## Detailed Documentation

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

