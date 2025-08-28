# config_2 Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 10
- **Messages**: 10
- **Services**: 0
- **Enums**: 0

## Files in this Module

- [value_usage_statistics.proto](#value_usage_statistics)
- [value_usage_trend.proto](#value_usage_trend)
- [value_validation_result.proto](#value_validation_result)
- [version_artifact.proto](#version_artifact)
- [version_compatibility_info.proto](#version_compatibility_info)
- [version_dependency.proto](#version_dependency)
- [version_deployment_info.proto](#version_deployment_info)
- [version_quality_issue.proto](#version_quality_issue)
- [version_quality_metrics.proto](#version_quality_metrics)
- [versioning_settings.proto](#versioning_settings)
---


## Detailed Documentation

### value_usage_statistics.proto {#value_usage_statistics}

**Path**: `gcommon/v1/config/value_usage_statistics.proto` **Package**: `gcommon.v1.config` **Lines**: 51

**Messages** (1): `ValueUsageStatistics`

**Imports** (4):

- `gcommon/v1/config/value_usage_trend.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/value_usage_statistics.proto
// version: 1.0.0
// guid: 3e5f0d64-7329-474a-9bd9-17d7f8fdf4b5

edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/config/value_usage_trend.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message ValueUsageStatistics {
  // Total read count
  int64 read_count = 1 [(buf.validate.field).int64.gte = 0];

  // Total write count
  int64 write_count = 2 [(buf.validate.field).int64.gte = 0];

  // Last read timestamp
  google.protobuf.Timestamp last_read_at = 3;

  // Last write timestamp
  google.protobuf.Timestamp last_written_at = 4;

  // Read frequency (reads per day)
  double read_frequency = 5 [(buf.validate.field).double.gte = 0.0];

  // Write frequency (writes per day)
  double write_frequency = 6 [(buf.validate.field).double.gte = 0.0];

  // Unique readers count
  int64 unique_readers = 7 [(buf.validate.field).int64.gte = 0];

  // Unique writers count
  int64 unique_writers = 8 [(buf.validate.field).int64.gte = 0];

  // Peak usage timestamp
  google.protobuf.Timestamp peak_usage_at = 9;

  // Peak usage count
  int64 peak_usage_count = 10 [(buf.validate.field).int64.gte = 0];

  // Usage trends
  repeated gcommon.v1.config.ValueUsageTrend trends = 11 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### value_usage_trend.proto {#value_usage_trend}

**Path**: `gcommon/v1/config/value_usage_trend.proto` **Package**: `gcommon.v1.config` **Lines**: 32

**Messages** (1): `ValueUsageTrend`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/value_usage_trend.proto
// version: 1.0.0
// guid: 77c2eae0-a102-4079-971c-4294d89bef5d

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message ValueUsageTrend {
  // Trend period
  string period = 1 [(buf.validate.field).string.min_len = 1];

  // Read count
  int64 read_count = 2 [(buf.validate.field).int64.gte = 0];

  // Write count
  int64 write_count = 3 [(buf.validate.field).int64.gte = 0];

  // Trend timestamp
  google.protobuf.Timestamp timestamp = 4;

  // Trend metadata
  map<string, string> metadata = 5;
}
```

---

### value_validation_result.proto {#value_validation_result}

**Path**: `gcommon/v1/config/value_validation_result.proto` **Package**: `gcommon.v1.config` **Lines**: 45

**Messages** (1): `ValueValidationResult`

**Imports** (5):

- `gcommon/v1/common/value_validation_result_type.proto`
- `gcommon/v1/common/value_validation_severity.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/value_validation_result.proto
// version: 1.0.0
// guid: 01a83346-1423-44d3-a9c9-c97dc0cb3f4f

edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/common/value_validation_result_type.proto";
import "gcommon/v1/common/value_validation_severity.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message ValueValidationResult {
  // Validation name
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Validation result
  gcommon.v1.common.ValueValidationResultType result = 2;

  // Validation message
  string message = 3;

  // Validation severity
  gcommon.v1.common.ValueValidationSeverity severity = 4;

  // Validation timestamp
  google.protobuf.Timestamp timestamp = 5;

  // Validation details
  map<string, string> details = 6;

  // Validation rule
  string rule = 7;

  // Validation context
  string context = 8;
}
```

---

### version_artifact.proto {#version_artifact}

**Path**: `gcommon/v1/config/version_artifact.proto` **Package**: `gcommon.v1.config` **Lines**: 40

**Messages** (1): `VersionArtifact`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/version_artifact.proto
// version: 1.0.0
// guid: 7cbe5a72-963f-4b03-b61e-7cd392e571c8

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message VersionArtifact {
  // Artifact name
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Artifact type
  string type = 2;

  // Artifact path
  string path = 3;

  // Artifact size
  int64 size = 4;

  // Artifact checksum
  string checksum = 5;

  // Artifact metadata
  map<string, string> metadata = 6;

  // Artifact timestamp
  google.protobuf.Timestamp timestamp = 7;
}
```

---

### version_compatibility_info.proto {#version_compatibility_info}

**Path**: `gcommon/v1/config/version_compatibility_info.proto` **Package**: `gcommon.v1.config` **Lines**: 40

**Messages** (1): `VersionCompatibilityInfo`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/version_compatibility_info.proto
// version: 1.0.0
// guid: bdb10c96-0338-4ab3-877b-f10ea821efe9

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message VersionCompatibilityInfo {
  // Backward compatible
  bool backward_compatible = 1;

  // Forward compatible
  bool forward_compatible = 2;

  // Breaking changes
  repeated string breaking_changes = 3 [(buf.validate.field).repeated.min_items = 1];

  // Compatibility notes
  string notes = 4 [(buf.validate.field).string.min_len = 1];

  // Minimum version
  string min_version = 5 [(buf.validate.field).string.pattern = "^v?\\d+\\.\\d+\\.\\d+"];

  // Maximum version
  string max_version = 6 [(buf.validate.field).string.pattern = "^v?\\d+\\.\\d+\\.\\d+"];

  // Deprecated features
  repeated string deprecated_features = 7 [(buf.validate.field).repeated.min_items = 1];

  // Migration guide
  string migration_guide = 8 [(buf.validate.field).string.min_len = 1];
}
```

---

### version_dependency.proto {#version_dependency}

**Path**: `gcommon/v1/config/version_dependency.proto` **Package**: `gcommon.v1.config` **Lines**: 39

**Messages** (1): `VersionDependency`

**Imports** (3):

- `gcommon/v1/common/version_dependency_type.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/version_dependency.proto
// version: 1.0.0
// guid: c6e48e5f-19bf-49eb-ae5b-2360c1e11fe1

edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/common/version_dependency_type.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message VersionDependency {
  // Dependency name
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Dependency version
  string version = 2;

  // Dependency type
  gcommon.v1.common.VersionDependencyType type = 3;

  // Dependency scope
  string scope = 4;

  // Dependency bool optional = 5;

  // Dependency constraints
  repeated string constraints = 6;

  // Dependency metadata
  map<string, string> metadata = 7;
}
```

---

### version_deployment_info.proto {#version_deployment_info}

**Path**: `gcommon/v1/config/version_deployment_info.proto` **Package**: `gcommon.v1.config` **Lines**: 46

**Messages** (1): `VersionDeploymentInfo`

**Imports** (5):

- `gcommon/v1/common/version_deployment_status.proto`
- `gcommon/v1/common/version_health_status.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/version_deployment_info.proto
// version: 1.0.0
// guid: 194328f1-30ba-459e-b106-f6b99ece3ee3

edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/common/version_deployment_status.proto";
import "gcommon/v1/common/version_health_status.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message VersionDeploymentInfo {
  // Deployment status
  gcommon.v1.common.VersionDeploymentStatus status = 1;

  // Deployment timestamp
  google.protobuf.Timestamp deployed_at = 2;

  // Deployment environment
  string environment = 3 [(buf.validate.field).string.min_len = 1];

  // Deployment method
  string method = 4 [(buf.validate.field).string.min_len = 1];

  // Deployment user
  string deployed_by = 5 [(buf.validate.field).string.min_len = 1];

  // Deployment configuration
  map<string, string> config = 6;

  // Deployment artifacts
  repeated string artifacts = 7 [(buf.validate.field).repeated.min_items = 1];

  // Deployment health
  gcommon.v1.common.VersionHealthStatus health = 8;

  // Deployment metrics
  map<string, double> metrics = 9;
}
```

---

### version_quality_issue.proto {#version_quality_issue}

**Path**: `gcommon/v1/config/version_quality_issue.proto` **Package**: `gcommon.v1.config` **Lines**: 33

**Messages** (1): `VersionQualityIssue`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/version_quality_issue.proto
// version: 1.0.0
// guid: 98aad520-640b-4663-a48a-ec3928c41c6a

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message VersionQualityIssue {
  // Issue type
  string type = 1;

  // Issue severity
  string severity = 2;

  // Issue description
  string description = 3 [ (buf.validate.field).string.max_len = 1000 ];

  // Issue location
  string location = 4;

  // Issue rule
  string rule = 5;

  // Issue fix suggestion
  string fix_suggestion = 6;
}
```

---

### version_quality_metrics.proto {#version_quality_metrics}

**Path**: `gcommon/v1/config/version_quality_metrics.proto` **Package**: `gcommon.v1.config` **Lines**: 45

**Messages** (1): `VersionQualityMetrics`

**Imports** (4):

- `gcommon/v1/config/version_quality_issue.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/version_quality_metrics.proto
// version: 1.0.0
// guid: 2326770b-b97a-4a96-93aa-b093931437a7

edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/config/version_quality_issue.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message VersionQualityMetrics {
  // Code quality score
  double quality_score = 1 [(buf.validate.field).double.gte = 0.0];

  // Test coverage
  double test_coverage = 2 [(buf.validate.field).double.gte = 0.0];

  // Security score
  double security_score = 3 [(buf.validate.field).double.gte = 0.0];

  // Performance score
  double performance_score = 4 [(buf.validate.field).double.gte = 0.0];

  // Complexity score
  double complexity_score = 5 [(buf.validate.field).double.gte = 0.0];

  // Technical debt score
  double technical_debt_score = 6 [(buf.validate.field).double.gte = 0.0];

  // Quality gate status
  bool quality_gate_passed = 7;

  // Quality issues
  repeated VersionQualityIssue issues = 8 [(buf.validate.field).repeated.min_items = 1];

  // Quality metrics timestamp
  google.protobuf.Timestamp timestamp = 9;
}
```

---

### versioning_settings.proto {#versioning_settings}

**Path**: `gcommon/v1/config/versioning_settings.proto` **Package**: `gcommon.v1.config` **Lines**: 37

**Messages** (1): `VersioningSettings`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/v1/versioning_settings.proto
// version: 1.0.0
// guid: 8ed86af7-67dd-4efb-abe6-bd383a4a4720

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message VersioningSettings {
  // Whether versioning is enabled
  bool enabled = 1;

  // Maximum number of versions to keep
  int32 max_versions = 2 [(buf.validate.field).int32.gte = 0];

  // Version retention period in days
  int32 retention_days = 3 [(buf.validate.field).int32.gte = 0];

  // Whether to create versions on change
  bool version_on_change = 4;

  // Whether to create versions on schedule
  bool version_on_schedule = 5;

  // Versioning schedule
  string schedule = 6 [(buf.validate.field).string.min_len = 1];

  // Version metadata
  map<string, string> metadata = 7;
}
```

---

