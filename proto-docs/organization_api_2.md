# organization_api_2 Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 12
- **Messages**: 12
- **Services**: 0
- **Enums**: 0

## Files in this Module

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
---


## Detailed Documentation

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

