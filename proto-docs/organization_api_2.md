# organization_api_2 Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 8
- **Messages**: 8
- **Services**: 0
- **Enums**: 0

## Files in this Module

- [update_organization_request.proto](#update_organization_request)
- [update_organization_response.proto](#update_organization_response)
- [update_team_request.proto](#update_team_request)
- [update_team_response.proto](#update_team_response)
- [update_tenant_quota_request.proto](#update_tenant_quota_request)
- [update_tenant_quota_response.proto](#update_tenant_quota_response)
- [update_tenant_request.proto](#update_tenant_request)
- [update_tenant_response.proto](#update_tenant_response)

## Module Dependencies

**This module depends on**:

- [common](./common.md)
- [organization](./organization.md)

**Modules that depend on this one**:

- [organization_services](./organization_services.md)

---

## Detailed Documentation

### update_organization_request.proto {#update_organization_request}

**Path**: `pkg/organization/proto/update_organization_request.proto`
**Package**: `gcommon.v1.organization` **Lines**: 27

**Messages** (1): `UpdateOrganizationRequest`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)
- `pkg/organization/proto/organization.proto` →
  [organization](./organization.md#organization)

#### Source Code

```protobuf
// file: pkg/organization/proto/requests/update_organization_request.proto

edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";
import "pkg/organization/proto/organization.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

message UpdateOrganizationRequest {
  // Request metadata for tracing and context
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Organization ID to update
  string organization_id = 2;

  // Updated organization information
  Organization organization = 3;

  // Fields to update (field mask)
  repeated string update_fields = 4;
}

```

---

### update_organization_response.proto {#update_organization_response}

**Path**: `pkg/organization/proto/update_organization_response.proto`
**Package**: `gcommon.v1.organization` **Lines**: 26

**Messages** (1): `UpdateOrganizationResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/organization/proto/organization.proto` →
  [organization](./organization.md#organization)

#### Source Code

```protobuf
// file: pkg/organization/proto/responses/update_organization_response.proto
edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";
import "pkg/organization/proto/organization.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

/**
 * UpdateOrganizationResponse message returning the result of organization update.
 */
message UpdateOrganizationResponse {
  // Updated organization
  Organization organization = 1;

  // Any errors encountered during update
  repeated gcommon.v1.common.Error errors = 2;

  // Success status
  bool success = 3;
}

```

---

### update_team_request.proto {#update_team_request}

**Path**: `pkg/organization/proto/update_team_request.proto` **Package**:
`gcommon.v1.organization` **Lines**: 31

**Messages** (1): `UpdateTeamRequest`

**Imports** (4):

- `google/protobuf/field_mask.proto`
- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)
- `pkg/organization/proto/team.proto` → [organization](./organization.md#team)

#### Source Code

```protobuf
// file: pkg/organization/proto/requests/update_team_request.proto

edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/field_mask.proto";
import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";
import "pkg/organization/proto/team.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

message UpdateTeamRequest {
  // Request metadata for tracing and context
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Team identifier to update
  string team_id = 2;

  // Updated team information
  gcommon.v1.organization.Team team = 3;

  // Fields to update in partial mode
  google.protobuf.FieldMask update_mask = 4;

  // Validate only without persisting if true
  bool validate_only = 5;
}

```

---

### update_team_response.proto {#update_team_response}

**Path**: `pkg/organization/proto/update_team_response.proto` **Package**:
`gcommon.v1.organization` **Lines**: 23

**Messages** (1): `UpdateTeamResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/organization/proto/team.proto` → [organization](./organization.md#team)

#### Source Code

```protobuf
// file: pkg/organization/proto/responses/update_team_response.proto
edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";
import "pkg/organization/proto/team.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

message UpdateTeamResponse {
  // Any errors encountered
  repeated gcommon.v1.common.Error errors = 1;

  // Success status
  bool success = 2;

  // Updated team information
  gcommon.v1.organization.Team team = 3;
}

```

---

### update_tenant_quota_request.proto {#update_tenant_quota_request}

**Path**: `pkg/organization/proto/update_tenant_quota_request.proto`
**Package**: `gcommon.v1.organization` **Lines**: 24

**Messages** (1): `UpdateTenantQuotaRequest`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)
- `pkg/organization/proto/tenant_quota.proto` →
  [organization](./organization.md#tenant_quota)

#### Source Code

```protobuf
// file: pkg/organization/proto/requests/update_tenant_quota_request.proto

edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";
import "pkg/organization/proto/tenant_quota.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

message UpdateTenantQuotaRequest {
  // Request metadata for tracing and context
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Tenant identifier
  string tenant_id = 2;

  // Updated quota configuration
  gcommon.v1.organization.TenantQuota quota = 3;
}

```

---

### update_tenant_quota_response.proto {#update_tenant_quota_response}

**Path**: `pkg/organization/proto/update_tenant_quota_response.proto`
**Package**: `gcommon.v1.organization` **Lines**: 23

**Messages** (1): `UpdateTenantQuotaResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/organization/proto/tenant_quota.proto` →
  [organization](./organization.md#tenant_quota)

#### Source Code

```protobuf
// file: pkg/organization/proto/responses/update_tenant_quota_response.proto
edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";
import "pkg/organization/proto/tenant_quota.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

message UpdateTenantQuotaResponse {
  // Any errors encountered
  repeated gcommon.v1.common.Error errors = 1;

  // Success status
  bool success = 2;

  // Updated quota configuration
  gcommon.v1.organization.TenantQuota quota = 3;
}

```

---

### update_tenant_request.proto {#update_tenant_request}

**Path**: `pkg/organization/proto/update_tenant_request.proto` **Package**:
`gcommon.v1.organization` **Lines**: 31

**Messages** (1): `UpdateTenantRequest`

**Imports** (4):

- `google/protobuf/field_mask.proto`
- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)
- `pkg/organization/proto/tenant.proto` →
  [organization](./organization.md#tenant)

#### Source Code

```protobuf
// file: pkg/organization/proto/requests/update_tenant_request.proto

edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/field_mask.proto";
import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";
import "pkg/organization/proto/tenant.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

message UpdateTenantRequest {
  // Request metadata for tracing and context
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Tenant identifier to update
  string tenant_id = 2;

  // Updated tenant information
  gcommon.v1.organization.Tenant tenant = 3;

  // Fields to update in partial mode
  google.protobuf.FieldMask update_mask = 4;

  // Validate only without persisting if true
  bool validate_only = 5;
}

```

---

### update_tenant_response.proto {#update_tenant_response}

**Path**: `pkg/organization/proto/update_tenant_response.proto` **Package**:
`gcommon.v1.organization` **Lines**: 23

**Messages** (1): `UpdateTenantResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/organization/proto/tenant.proto` →
  [organization](./organization.md#tenant)

#### Source Code

```protobuf
// file: pkg/organization/proto/responses/update_tenant_response.proto
edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";
import "pkg/organization/proto/tenant.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

message UpdateTenantResponse {
  // Any errors encountered
  repeated gcommon.v1.common.Error errors = 1;

  // Success status
  bool success = 2;

  // Updated tenant details
  gcommon.v1.organization.Tenant tenant = 3;
}

```

---
