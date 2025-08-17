# config_2 Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 41
- **Messages**: 22
- **Services**: 0
- **Enums**: 19
- ⚠️ **Issues**: 3

## Files in this Module

- [secret_validation_result_type.proto](#secret_validation_result_type)
- [secret_validation_severity.proto](#secret_validation_severity)
- [synchronization_frequency.proto](#synchronization_frequency)
- [synchronization_target.proto](#synchronization_target)
- [template_change.proto](#template_change)
- [template_format.proto](#template_format)
- [template_hook.proto](#template_hook)
- [template_output.proto](#template_output)
- [template_parameter.proto](#template_parameter) ⚠️ 2 issues
- [template_status.proto](#template_status)
- [transformation_step.proto](#transformation_step)
- [transformation_type.proto](#transformation_type)
- [usage_statistics.proto](#usage_statistics)
- [usage_trend.proto](#usage_trend)
- [validation_result.proto](#validation_result)
- [validation_result_type.proto](#validation_result_type)
- [validation_rule.proto](#validation_rule)
- [validation_rule_severity.proto](#validation_rule_severity)
- [validation_rule_type.proto](#validation_rule_type)
- [validation_severity.proto](#validation_severity)
- [value_dependency.proto](#value_dependency)
- [value_history_entry.proto](#value_history_entry)
- [value_reference.proto](#value_reference)
- [value_source.proto](#value_source)
- [value_status.proto](#value_status)
- [value_usage_statistics.proto](#value_usage_statistics)
- [value_usage_trend.proto](#value_usage_trend)
- [value_validation_result.proto](#value_validation_result)
- [value_validation_result_type.proto](#value_validation_result_type)
- [value_validation_severity.proto](#value_validation_severity)
- [version_artifact.proto](#version_artifact)
- [version_compatibility_info.proto](#version_compatibility_info)
- [version_dependency.proto](#version_dependency) ⚠️ 1 issues
- [version_dependency_type.proto](#version_dependency_type)
- [version_deployment_info.proto](#version_deployment_info)
- [version_deployment_status.proto](#version_deployment_status)
- [version_health_status.proto](#version_health_status)
- [version_quality_issue.proto](#version_quality_issue)
- [version_quality_metrics.proto](#version_quality_metrics)
- [version_status.proto](#version_status)
- [version_type.proto](#version_type)

## Module Dependencies

**This module depends on**:

- [auth_events](./auth_events.md)
- [common](./common.md)
- [config_1](./config_1.md)
- [config_events](./config_events.md)
- [metrics_1](./metrics_1.md)

**Modules that depend on this one**:

- [config_1](./config_1.md)
- [config_config_1](./config_config_1.md)
- [config_config_2](./config_config_2.md)
- [metrics_1](./metrics_1.md)
- [metrics_2](./metrics_2.md)
- [metrics_api_1](./metrics_api_1.md)
- [metrics_api_2](./metrics_api_2.md)
- [metrics_config](./metrics_config.md)

---

## Detailed Documentation

### secret_validation_result_type.proto {#secret_validation_result_type}

**Path**: `pkg/config/proto/secret_validation_result_type.proto` **Package**: `gcommon.v1.config` **Lines**: 22

**Enums** (1): `SecretValidationResultType`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/secret_validation_result_type.proto
// version: 1.0.0
// guid: b6bb65eb-d0bd-40b2-ad57-22253970cb05

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

enum SecretValidationResultType {
  SECRET_VALIDATION_RESULT_TYPE_UNSPECIFIED = 0;
  SECRET_VALIDATION_RESULT_TYPE_PASS = 1;
  SECRET_VALIDATION_RESULT_TYPE_FAIL = 2;
  SECRET_VALIDATION_RESULT_TYPE_WARNING = 3;
  SECRET_VALIDATION_RESULT_TYPE_SKIP = 4;
}

```

---

### secret_validation_severity.proto {#secret_validation_severity}

**Path**: `pkg/config/proto/secret_validation_severity.proto` **Package**: `gcommon.v1.config` **Lines**: 22

**Enums** (1): `SecretValidationSeverity`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/secret_validation_severity.proto
// version: 1.0.0
// guid: 8dc44dbd-dedb-4dfd-b5f9-ad2256d6a6c6

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

enum SecretValidationSeverity {
  SECRET_VALIDATION_SEVERITY_UNSPECIFIED = 0;
  SECRET_VALIDATION_SEVERITY_INFO = 1;
  SECRET_VALIDATION_SEVERITY_WARNING = 2;
  SECRET_VALIDATION_SEVERITY_ERROR = 3;
  SECRET_VALIDATION_SEVERITY_CRITICAL = 4;
}

```

---

### synchronization_frequency.proto {#synchronization_frequency}

**Path**: `pkg/config/proto/synchronization_frequency.proto` **Package**: `gcommon.v1.config` **Lines**: 24

**Enums** (1): `SynchronizationFrequency`

**Imports** (3):

- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/synchronization_frequency.proto
// version: 1.0.0
// guid: 939438cc-2704-4ba7-ab8a-8ed45e882d94

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

enum SynchronizationFrequency {
  SYNCHRONIZATION_FREQUENCY_UNSPECIFIED = 0;
  SYNCHRONIZATION_FREQUENCY_REAL_TIME = 1;
  SYNCHRONIZATION_FREQUENCY_HOURLY = 2;
  SYNCHRONIZATION_FREQUENCY_DAILY = 3;
  SYNCHRONIZATION_FREQUENCY_WEEKLY = 4;
  SYNCHRONIZATION_FREQUENCY_ON_CHANGE = 5;
}

```

---

### synchronization_target.proto {#synchronization_target}

**Path**: `pkg/config/proto/synchronization_target.proto` **Package**: `gcommon.v1.config` **Lines**: 32

**Messages** (1): `SynchronizationTarget`

**Imports** (3):

- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/synchronization_target.proto
// version: 1.0.0
// guid: cefe82ce-a5cb-44d8-a069-e773d0b9658d

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message SynchronizationTarget {
  // Target name
  string name = 1;

  // Target type
  string type = 2;

  // Target configuration
  map<string, string> config = 3;

  // Target enabled
  bool enabled = 4;

  // Target priority
  int32 priority = 5;
}

```

---

### template_change.proto {#template_change}

**Path**: `pkg/config/proto/template_change.proto` **Package**: `gcommon.v1.config` **Lines**: 41

**Messages** (1): `TemplateChange`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/config/proto/change_type.proto` → [config_1](./config_1.md#change_type) → [metrics_1](./metrics_1.md#change_type)

#### Source Code

```protobuf
// file: pkg/config/proto/template_change.proto
// version: 1.0.0
// guid: 801fc1c2-3a27-4a37-a1e2-0d540b0f4dd8

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/config/proto/change_type.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message TemplateChange {
  // Change version
  string version = 1;

  // Change description
  string description = 2;

  // Change author
  string author = 3;

  // Change timestamp
  google.protobuf.Timestamp timestamp = 4;

  // Change type
  ChangeType type = 5;

  // Breaking change flag
  bool breaking = 6;

  // Change details
  repeated string details = 7;

  // Migration notes
  string migration_notes = 8;
}

```

---

### template_format.proto {#template_format}

**Path**: `pkg/config/proto/template_format.proto` **Package**: `gcommon.v1.config` **Lines**: 25

**Enums** (1): `TemplateFormat`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/template_format.proto
// version: 1.0.0
// guid: 5633815c-6ddb-47f1-b36e-a761ce96bd90

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

enum TemplateFormat {
  TEMPLATE_FORMAT_UNSPECIFIED = 0;
  TEMPLATE_FORMAT_JSON = 1;
  TEMPLATE_FORMAT_YAML = 2;
  TEMPLATE_FORMAT_TOML = 3;
  TEMPLATE_FORMAT_XML = 4;
  TEMPLATE_FORMAT_PROPERTIES = 5;
  TEMPLATE_FORMAT_INI = 6;
  TEMPLATE_FORMAT_CUSTOM = 7;
}

```

---

### template_hook.proto {#template_hook}

**Path**: `pkg/config/proto/template_hook.proto` **Package**: `gcommon.v1.config` **Lines**: 42

**Messages** (1): `TemplateHook`

**Imports** (4):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/config/proto/hook_error_handling.proto` → [config_1](./config_1.md#hook_error_handling)
- `pkg/config/proto/hook_type.proto` → [config_1](./config_1.md#hook_type)

#### Source Code

```protobuf
// file: pkg/config/proto/template_hook.proto
// version: 1.0.0
// guid: 48a58147-b1e9-4c28-ad50-58952adc0ffe

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/config/proto/hook_error_handling.proto";
import "pkg/config/proto/hook_type.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message TemplateHook {
  // Hook name
  string name = 1;

  // Hook type
  HookType type = 2;

  // Hook command or script
  string command = 3;

  // Hook timeout
  int32 timeout_seconds = 4;

  // Hook working directory
  string working_directory = 5;

  // Hook environment variables
  map<string, string> environment = 6;

  // Hook conditions
  map<string, string> conditions = 7;

  // Hook error handling
  HookErrorHandling error_handling = 8;
}

```

---

### template_output.proto {#template_output}

**Path**: `pkg/config/proto/template_output.proto` **Package**: `gcommon.v1.config` **Lines**: 40

**Messages** (1): `TemplateOutput`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/template_output.proto
// version: 1.0.0
// guid: 579f8ac6-c06e-4a4f-9e96-232802698bc1

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message TemplateOutput {
  // Output name
  string name = 1;

  // Output description
  string description = 2;

  // Output type
  string type = 3;

  // Output value expression
  string value = 4;

  // Whether output is sensitive
  bool sensitive = 5;

  // Output group
  string group = 6;

  // Output format
  string format = 7;

  // Output examples
  repeated string examples = 8;
}

```

---

### template_parameter.proto {#template_parameter}

**Path**: `pkg/config/proto/template_parameter.proto` **Package**: `gcommon.v1.config` **Lines**: 63

**Messages** (1): `TemplateParameter`

**Imports** (4):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/config/proto/parameter_constraints.proto` → [config_1](./config_1.md#parameter_constraints)
- `pkg/config/proto/parameter_type.proto` → [config_1](./config_1.md#parameter_type)

#### ⚠️ Issues Found (2)

- Line 60: Implementation needed - // Parameter placeholder text
- Line 61: Implementation needed - string placeholder = 15;

#### Source Code

```protobuf
// file: pkg/config/proto/template_parameter.proto
// version: 1.0.0
// guid: 800be7b5-ca05-4137-a8d2-7d1a3fe5cc97

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/config/proto/parameter_constraints.proto";
import "pkg/config/proto/parameter_type.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message TemplateParameter {
  // Parameter name
  string name = 1;

  // Parameter description
  string description = 2;

  // Parameter type
  ParameterType type = 3;

  // Whether parameter is required
  bool required = 4;

  // Default value
  string default_value = 5;

  // Allowed values (for enum types)
  repeated string allowed_values = 6;

  // Parameter constraints
  ParameterConstraints constraints = 7;

  // Parameter group
  string group = 8;

  // Display order
  int32 order = 9;

  // Whether parameter is sensitive
  bool sensitive = 10;

  // Parameter validation pattern
  string validation_pattern = 11;

  // Parameter examples
  repeated string examples = 12;

  // Parameter documentation
  string documentation = 13;

  // Parameter display name
  string display_name = 14;

  // Parameter placeholder text
  string placeholder = 15;
}

```

---

### template_status.proto {#template_status}

**Path**: `pkg/config/proto/template_status.proto` **Package**: `gcommon.v1.config` **Lines**: 23

**Enums** (1): `TemplateStatus`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/template_status.proto
// version: 1.0.0
// guid: fcaf0275-1145-4c6c-af44-a4386dd4c2a7

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

enum TemplateStatus {
  TEMPLATE_STATUS_UNSPECIFIED = 0;
  TEMPLATE_STATUS_DRAFT = 1;
  TEMPLATE_STATUS_ACTIVE = 2;
  TEMPLATE_STATUS_DEPRECATED = 3;
  TEMPLATE_STATUS_ARCHIVED = 4;
  TEMPLATE_STATUS_DELETED = 5;
}

```

---

### transformation_step.proto {#transformation_step}

**Path**: `pkg/config/proto/transformation_step.proto` **Package**: `gcommon.v1.config` **Lines**: 36

**Messages** (1): `TransformationStep`

**Imports** (4):

- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/config/proto/transformation_type.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/transformation_step.proto
// version: 1.0.0
// guid: 4b3c1c96-82eb-4c1d-84ac-362e461d5793

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/config/proto/transformation_type.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message TransformationStep {
  // Step name
  string name = 1;

  // Step type
  TransformationType type = 2;

  // Step expression
  string expression = 3;

  // Step parameters
  map<string, string> parameters = 4;

  // Step enabled
  bool enabled = 5;

  // Step order
  int32 order = 6;
}

```

---

### transformation_type.proto {#transformation_type}

**Path**: `pkg/config/proto/transformation_type.proto` **Package**: `gcommon.v1.config` **Lines**: 26

**Enums** (1): `TransformationType`

**Imports** (3):

- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/transformation_type.proto
// version: 1.0.0
// guid: 9c4d5ef1-c4a7-4f98-9315-43c2517e6f41

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

enum TransformationType {
  TRANSFORMATION_TYPE_UNSPECIFIED = 0;
  TRANSFORMATION_TYPE_TEMPLATE = 1;
  TRANSFORMATION_TYPE_FUNCTION = 2;
  TRANSFORMATION_TYPE_SCRIPT = 3;
  TRANSFORMATION_TYPE_REGEX = 4;
  TRANSFORMATION_TYPE_JSONPATH = 5;
  TRANSFORMATION_TYPE_XPATH = 6;
  TRANSFORMATION_TYPE_CUSTOM = 7;
}

```

---

### usage_statistics.proto {#usage_statistics}

**Path**: `pkg/config/proto/usage_statistics.proto` **Package**: `gcommon.v1.config` **Lines**: 47

**Messages** (1): `UsageStatistics`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/config/proto/usage_trend.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/usage_statistics.proto
// version: 1.0.0
// guid: cc21dcd3-5d5b-42a8-9602-b3b08c2ff649

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/config/proto/usage_trend.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message UsageStatistics {
  // Total access count
  int64 total_access_count = 1;

  // Access count in last 24 hours
  int64 access_count_24h = 2;

  // Access count in last 7 days
  int64 access_count_7d = 3;

  // Access count in last 30 days
  int64 access_count_30d = 4;

  // Unique users count
  int64 unique_users_count = 5;

  // Unique services count
  int64 unique_services_count = 6;

  // Average access frequency per day
  double avg_access_frequency = 7;

  // Peak access timestamp
  google.protobuf.Timestamp peak_access_at = 8;

  // Peak access count
  int64 peak_access_count = 9;

  // Usage trends
  repeated UsageTrend trends = 10;
}

```

---

### usage_trend.proto {#usage_trend}

**Path**: `pkg/config/proto/usage_trend.proto` **Package**: `gcommon.v1.config` **Lines**: 25

**Messages** (1): `UsageTrend`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/usage_trend.proto
// version: 1.0.0
// guid: d9e0f1a2-3456-789a-3456-901234567890

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message UsageTrend {
  // Timestamp
  google.protobuf.Timestamp timestamp = 1;

  // Usage count
  int64 usage_count = 2;

  // Trend direction
  string direction = 3;
}

```

---

### validation_result.proto {#validation_result}

**Path**: `pkg/config/proto/validation_result.proto` **Package**: `gcommon.v1.config` **Lines**: 39

**Messages** (1): `ValidationResult`

**Imports** (7):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/config/proto/approval_status.proto` → [config_1](./config_1.md#approval_status)
- `pkg/config/proto/audit_operation_type.proto` → [config_events](./config_events.md#audit_operation_type)
- `pkg/config/proto/rollback_method.proto` → [config_1](./config_1.md#rollback_method)
- `pkg/config/proto/validation_result_type.proto`
- `pkg/config/proto/validation_severity.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/validation_result.proto
// version: 1.0.0
// guid: 24d2ce27-6b21-4f7b-82f6-2a7b060fe004

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/config/proto/approval_status.proto";
import "pkg/config/proto/audit_operation_type.proto";
import "pkg/config/proto/rollback_method.proto";
import "pkg/config/proto/validation_result_type.proto";
import "pkg/config/proto/validation_severity.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message ValidationResult {
  // Validation rule name
  string rule_name = 1;

  // Validation result
  ValidationResultType result = 2;

  // Validation message
  string message = 3;

  // Severity level
  ValidationSeverity severity = 4;

  // Field that was validated
  string field = 5;

  // Additional context
  map<string, string> context = 6;
}

```

---

### validation_result_type.proto {#validation_result_type}

**Path**: `pkg/config/proto/validation_result_type.proto` **Package**: `gcommon.v1.config` **Lines**: 34

**Enums** (1): `ValidationResultType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/validation_result_type.proto
// version: 1.0.0
// guid: e7f8a9b0-c1d2-3e4f-5a6b-7c8d9e0f1a2b

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

/**
 * ValidationResultType represents the result of validation.
 * Specifies the outcome of configuration validation checks.
 */
enum ValidationResultType {
  // Unspecified validation result
  VALIDATION_RESULT_TYPE_UNSPECIFIED = 0;

  // Validation passed
  VALIDATION_RESULT_TYPE_PASS = 1;

  // Validation failed
  VALIDATION_RESULT_TYPE_FAIL = 2;

  // Validation completed with warnings
  VALIDATION_RESULT_TYPE_WARNING = 3;

  // Validation was skipped
  VALIDATION_RESULT_TYPE_SKIP = 4;
}

```

---

### validation_rule.proto {#validation_rule}

**Path**: `pkg/config/proto/validation_rule.proto` **Package**: `gcommon.v1.config` **Lines**: 38

**Messages** (1): `ValidationRule`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/config/proto/validation_severity.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/validation_rule.proto
// version: 1.0.0
// guid: 6cc709c2-996e-4e1c-aa4d-0c7741fadb21

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/config/proto/validation_severity.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message ValidationRule {
  // Rule name
  string name = 1;

  // Rule description
  string description = 2;

  // Rule expression
  string expression = 3;

  // Error message if validation fails
  string error_message = 4;

  // Rule severity
  ValidationSeverity severity = 5;

  // Parameters this rule applies to
  repeated string parameters = 6;

  // Rule conditions
  map<string, string> conditions = 7;
}

```

---

### validation_rule_severity.proto {#validation_rule_severity}

**Path**: `pkg/config/proto/validation_rule_severity.proto` **Package**: `gcommon.v1.config` **Lines**: 23

**Enums** (1): `ValidationRuleSeverity`

**Imports** (3):

- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/validation_rule_severity.proto
// version: 1.0.0
// guid: 49607ba0-0d79-4402-a891-1a5d80c4286f

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

enum ValidationRuleSeverity {
  VALIDATION_RULE_SEVERITY_UNSPECIFIED = 0;
  VALIDATION_RULE_SEVERITY_INFO = 1;
  VALIDATION_RULE_SEVERITY_WARNING = 2;
  VALIDATION_RULE_SEVERITY_ERROR = 3;
  VALIDATION_RULE_SEVERITY_CRITICAL = 4;
}

```

---

### validation_rule_type.proto {#validation_rule_type}

**Path**: `pkg/config/proto/validation_rule_type.proto` **Package**: `gcommon.v1.config` **Lines**: 27

**Enums** (1): `ValidationRuleType`

**Imports** (3):

- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/validation_rule_type.proto
// version: 1.0.0
// guid: 604ea5f1-2b57-45ce-9711-be0f342bde10

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

enum ValidationRuleType {
  VALIDATION_RULE_TYPE_UNSPECIFIED = 0;
  VALIDATION_RULE_TYPE_REGEX = 1;
  VALIDATION_RULE_TYPE_RANGE = 2;
  VALIDATION_RULE_TYPE_LENGTH = 3;
  VALIDATION_RULE_TYPE_FORMAT = 4;
  VALIDATION_RULE_TYPE_ENUM = 5;
  VALIDATION_RULE_TYPE_CUSTOM = 6;
  VALIDATION_RULE_TYPE_FUNCTION = 7;
  VALIDATION_RULE_TYPE_SCHEMA = 8;
}

```

---

### validation_severity.proto {#validation_severity}

**Path**: `pkg/config/proto/validation_severity.proto` **Package**: `gcommon.v1.config` **Lines**: 21

**Enums** (1): `ValidationSeverity`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/validation_severity.proto
// version: 1.0.0
// guid: e0f1a2b3-4567-890b-4567-012345678901

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

enum ValidationSeverity {
  VALIDATION_SEVERITY_UNSPECIFIED = 0;
  VALIDATION_SEVERITY_INFO = 1;
  VALIDATION_SEVERITY_WARNING = 2;
  VALIDATION_SEVERITY_ERROR = 3;
  VALIDATION_SEVERITY_CRITICAL = 4;
}

```

---

### value_dependency.proto {#value_dependency}

**Path**: `pkg/config/proto/value_dependency.proto` **Package**: `gcommon.v1.config` **Lines**: 33

**Messages** (1): `ValueDependency`

**Imports** (4):

- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/config/proto/dependency_type.proto` → [config_1](./config_1.md#dependency_type)

#### Source Code

```protobuf
// file: pkg/config/proto/value_dependency.proto
// version: 1.0.0
// guid: ceefe5a4-8fbf-4555-9535-c57437357bef

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/config/proto/dependency_type.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message ValueDependency {
  // Dependency type
  DependencyType type = 1;

  // Dependent value key
  string dependent_key = 2;

  // Dependency key
  string dependency_key = 3;

  // Dependency condition
  string condition = 4;

  // Dependency metadata
  map<string, string> metadata = 5;
}

```

---

### value_history_entry.proto {#value_history_entry}

**Path**: `pkg/config/proto/value_history_entry.proto` **Package**: `gcommon.v1.config` **Lines**: 42

**Messages** (1): `ValueHistoryEntry`

**Imports** (4):

- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/config/proto/change_type.proto` → [config_1](./config_1.md#change_type) → [metrics_1](./metrics_1.md#change_type)

#### Source Code

```protobuf
// file: pkg/config/proto/value_history_entry.proto
// version: 1.0.0
// guid: 842c89c0-e045-4b46-8c03-f19d4383edb0

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/config/proto/change_type.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message ValueHistoryEntry {
  // Entry ID
  string entry_id = 1;

  // Previous value
  string previous_value = 2;

  // New value
  string new_value = 3;

  // Change timestamp
  google.protobuf.Timestamp timestamp = 4;

  // User who made the change
  string changed_by = 5;

  // Change reason
  string reason = 6;

  // Change type (using ChangeType from config_template.proto)
  ChangeType change_type = 7;

  // Change metadata
  map<string, string> metadata = 8;
}

```

---

### value_reference.proto {#value_reference}

**Path**: `pkg/config/proto/value_reference.proto` **Package**: `gcommon.v1.config` **Lines**: 30

**Messages** (1): `ValueReference`

**Imports** (4):

- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/config/proto/reference_type.proto` → [config_1](./config_1.md#reference_type)

#### Source Code

```protobuf
// file: pkg/config/proto/value_reference.proto
// version: 1.0.0
// guid: b56910e9-5a31-46b6-b2ac-3c854f87e332

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/config/proto/reference_type.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message ValueReference {
  // Reference type
  ReferenceType type = 1;

  // Referenced value key
  string referenced_key = 2;

  // Reference path
  string path = 3;

  // Reference metadata
  map<string, string> metadata = 4;
}

```

---

### value_source.proto {#value_source}

**Path**: `pkg/config/proto/value_source.proto` **Package**: `gcommon.v1.config` **Lines**: 39

**Enums** (1): `ValueSource`

**Imports** (3):

- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/value_source.proto
// version: 1.0.0
// guid: a06a0eb7-f579-4539-87e5-4f5bf9181601

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

enum ValueSource {
  VALUE_SOURCE_UNSPECIFIED = 0;
  VALUE_SOURCE_DEFAULT = 1;
  VALUE_SOURCE_ENVIRONMENT = 2;
  VALUE_SOURCE_FILE = 3;
  VALUE_SOURCE_DATABASE = 4;
  VALUE_SOURCE_CONSUL = 5;
  VALUE_SOURCE_ETCD = 6;
  VALUE_SOURCE_KUBERNETES = 7;
  VALUE_SOURCE_VAULT = 8;
  VALUE_SOURCE_AWS_PARAMETER_STORE = 9;
  VALUE_SOURCE_AWS_SECRETS_MANAGER = 10;
  VALUE_SOURCE_AZURE_KEY_VAULT = 11;
  VALUE_SOURCE_GCP_SECRET_MANAGER = 12;
  VALUE_SOURCE_REDIS = 13;
  VALUE_SOURCE_API = 14;
  VALUE_SOURCE_COMMAND_LINE = 15;
  VALUE_SOURCE_REMOTE = 16;
  VALUE_SOURCE_COMPUTED = 17;
  VALUE_SOURCE_INHERITED = 18;
  VALUE_SOURCE_OVERRIDE = 19;
  VALUE_SOURCE_CUSTOM = 20;
}

```

---

### value_status.proto {#value_status}

**Path**: `pkg/config/proto/value_status.proto` **Package**: `gcommon.v1.config` **Lines**: 28

**Enums** (1): `ValueStatus`

**Imports** (3):

- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/value_status.proto
// version: 1.0.0
// guid: cd97b900-15cf-474b-a899-146f0e687253

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

enum ValueStatus {
  VALUE_STATUS_UNSPECIFIED = 0;
  VALUE_STATUS_ACTIVE = 1;
  VALUE_STATUS_INACTIVE = 2;
  VALUE_STATUS_DRAFT = 3;
  VALUE_STATUS_DEPRECATED = 4;
  VALUE_STATUS_DELETED = 5;
  VALUE_STATUS_ERROR = 6;
  VALUE_STATUS_PENDING = 7;
  VALUE_STATUS_SYNCING = 8;
  VALUE_STATUS_VALIDATING = 9;
}

```

---

### value_usage_statistics.proto {#value_usage_statistics}

**Path**: `pkg/config/proto/value_usage_statistics.proto` **Package**: `gcommon.v1.config` **Lines**: 51

**Messages** (1): `ValueUsageStatistics`

**Imports** (4):

- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/config/proto/value_usage_trend.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/value_usage_statistics.proto
// version: 1.0.0
// guid: 3e5f0d64-7329-474a-9bd9-17d7f8fdf4b5

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/config/proto/value_usage_trend.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message ValueUsageStatistics {
  // Total read count
  int64 read_count = 1;

  // Total write count
  int64 write_count = 2;

  // Last read timestamp
  google.protobuf.Timestamp last_read_at = 3;

  // Last write timestamp
  google.protobuf.Timestamp last_written_at = 4;

  // Read frequency (reads per day)
  double read_frequency = 5;

  // Write frequency (writes per day)
  double write_frequency = 6;

  // Unique readers count
  int64 unique_readers = 7;

  // Unique writers count
  int64 unique_writers = 8;

  // Peak usage timestamp
  google.protobuf.Timestamp peak_usage_at = 9;

  // Peak usage count
  int64 peak_usage_count = 10;

  // Usage trends
  repeated ValueUsageTrend trends = 11;
}

```

---

### value_usage_trend.proto {#value_usage_trend}

**Path**: `pkg/config/proto/value_usage_trend.proto` **Package**: `gcommon.v1.config` **Lines**: 32

**Messages** (1): `ValueUsageTrend`

**Imports** (3):

- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/value_usage_trend.proto
// version: 1.0.0
// guid: 77c2eae0-a102-4079-971c-4294d89bef5d

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message ValueUsageTrend {
  // Trend period
  string period = 1;

  // Read count
  int64 read_count = 2;

  // Write count
  int64 write_count = 3;

  // Trend timestamp
  google.protobuf.Timestamp timestamp = 4;

  // Trend metadata
  map<string, string> metadata = 5;
}

```

---

### value_validation_result.proto {#value_validation_result}

**Path**: `pkg/config/proto/value_validation_result.proto` **Package**: `gcommon.v1.config` **Lines**: 43

**Messages** (1): `ValueValidationResult`

**Imports** (5):

- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/config/proto/value_validation_result_type.proto`
- `pkg/config/proto/value_validation_severity.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/value_validation_result.proto
// version: 1.0.0
// guid: 01a83346-1423-44d3-a9c9-c97dc0cb3f4f

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/config/proto/value_validation_result_type.proto";
import "pkg/config/proto/value_validation_severity.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message ValueValidationResult {
  // Validation name
  string name = 1;

  // Validation result
  ValueValidationResultType result = 2;

  // Validation message
  string message = 3;

  // Validation severity
  ValueValidationSeverity severity = 4;

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

### value_validation_result_type.proto {#value_validation_result_type}

**Path**: `pkg/config/proto/value_validation_result_type.proto` **Package**: `gcommon.v1.config` **Lines**: 23

**Enums** (1): `ValueValidationResultType`

**Imports** (3):

- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/value_validation_result_type.proto
// version: 1.0.0
// guid: 6558f48c-96da-4dc8-b0f1-691f0e0e8999

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

enum ValueValidationResultType {
  VALUE_VALIDATION_RESULT_TYPE_UNSPECIFIED = 0;
  VALUE_VALIDATION_RESULT_TYPE_PASS = 1;
  VALUE_VALIDATION_RESULT_TYPE_FAIL = 2;
  VALUE_VALIDATION_RESULT_TYPE_WARNING = 3;
  VALUE_VALIDATION_RESULT_TYPE_SKIP = 4;
}

```

---

### value_validation_severity.proto {#value_validation_severity}

**Path**: `pkg/config/proto/value_validation_severity.proto` **Package**: `gcommon.v1.config` **Lines**: 23

**Enums** (1): `ValueValidationSeverity`

**Imports** (3):

- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/value_validation_severity.proto
// version: 1.0.0
// guid: 55cd1c6a-887d-49f5-b248-9025dc9f5084

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

enum ValueValidationSeverity {
  VALUE_VALIDATION_SEVERITY_UNSPECIFIED = 0;
  VALUE_VALIDATION_SEVERITY_INFO = 1;
  VALUE_VALIDATION_SEVERITY_WARNING = 2;
  VALUE_VALIDATION_SEVERITY_ERROR = 3;
  VALUE_VALIDATION_SEVERITY_CRITICAL = 4;
}

```

---

### version_artifact.proto {#version_artifact}

**Path**: `pkg/config/proto/version_artifact.proto` **Package**: `gcommon.v1.config` **Lines**: 38

**Messages** (1): `VersionArtifact`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/audit_log.proto` → [auth_events](./auth_events.md#audit_log) → [common](./common.md#audit_log)

#### Source Code

```protobuf
// file: pkg/config/proto/version_artifact.proto
// version: 1.0.0
// guid: 7cbe5a72-963f-4b03-b61e-7cd392e571c8

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/common/proto/audit_log.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message VersionArtifact {
  // Artifact name
  string name = 1;

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

**Path**: `pkg/config/proto/version_compatibility_info.proto` **Package**: `gcommon.v1.config` **Lines**: 41

**Messages** (1): `VersionCompatibilityInfo`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/audit_log.proto` → [auth_events](./auth_events.md#audit_log) → [common](./common.md#audit_log)

#### Source Code

```protobuf
// file: pkg/config/proto/version_compatibility_info.proto
// version: 1.0.0
// guid: bdb10c96-0338-4ab3-877b-f10ea821efe9

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/common/proto/audit_log.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message VersionCompatibilityInfo {
  // Backward compatible
  bool backward_compatible = 1;

  // Forward compatible
  bool forward_compatible = 2;

  // Breaking changes
  repeated string breaking_changes = 3;

  // Compatibility notes
  string notes = 4;

  // Minimum version
  string min_version = 5;

  // Maximum version
  string max_version = 6;

  // Deprecated features
  repeated string deprecated_features = 7;

  // Migration guide
  string migration_guide = 8;
}

```

---

### version_dependency.proto {#version_dependency}

**Path**: `pkg/config/proto/version_dependency.proto` **Package**: `gcommon.v1.config` **Lines**: 38

**Messages** (1): `VersionDependency`

**Imports** (4):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/audit_log.proto` → [auth_events](./auth_events.md#audit_log) → [common](./common.md#audit_log)
- `pkg/config/proto/version_dependency_type.proto`

#### ⚠️ Issues Found (1)

- Line 30: Commented field - // Dependency bool optional = 5;

#### Source Code

```protobuf
// file: pkg/config/proto/version_dependency.proto
// version: 1.0.0
// guid: c6e48e5f-19bf-49eb-ae5b-2360c1e11fe1

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/common/proto/audit_log.proto";
import "pkg/config/proto/version_dependency_type.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message VersionDependency {
  // Dependency name
  string name = 1;

  // Dependency version
  string version = 2;

  // Dependency type
  VersionDependencyType type = 3;

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

### version_dependency_type.proto {#version_dependency_type}

**Path**: `pkg/config/proto/version_dependency_type.proto` **Package**: `gcommon.v1.config` **Lines**: 25

**Enums** (1): `VersionDependencyType`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/audit_log.proto` → [auth_events](./auth_events.md#audit_log) → [common](./common.md#audit_log)

#### Source Code

```protobuf
// file: pkg/config/proto/version_dependency_type.proto
// version: 1.0.0
// guid: 34850372-1489-45d0-9f83-e262d595215b

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/common/proto/audit_log.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

enum VersionDependencyType {
  VERSION_DEPENDENCY_TYPE_UNSPECIFIED = 0;
  VERSION_DEPENDENCY_TYPE_RUNTIME = 1;
  VERSION_DEPENDENCY_TYPE_BUILD = 2;
  VERSION_DEPENDENCY_TYPE_TEST = 3;
  VERSION_DEPENDENCY_TYPE_DEV = 4;
  VERSION_DEPENDENCY_TYPE_PEER = 5;
  VERSION_DEPENDENCY_TYPE_OPTIONAL = 6;
}

```

---

### version_deployment_info.proto {#version_deployment_info}

**Path**: `pkg/config/proto/version_deployment_info.proto` **Package**: `gcommon.v1.config` **Lines**: 46

**Messages** (1): `VersionDeploymentInfo`

**Imports** (5):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/audit_log.proto` → [auth_events](./auth_events.md#audit_log) → [common](./common.md#audit_log)
- `pkg/config/proto/version_deployment_status.proto`
- `pkg/config/proto/version_health_status.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/version_deployment_info.proto
// version: 1.0.0
// guid: 194328f1-30ba-459e-b106-f6b99ece3ee3

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/common/proto/audit_log.proto";
import "pkg/config/proto/version_deployment_status.proto";
import "pkg/config/proto/version_health_status.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message VersionDeploymentInfo {
  // Deployment status
  VersionDeploymentStatus status = 1;

  // Deployment timestamp
  google.protobuf.Timestamp deployed_at = 2;

  // Deployment environment
  string environment = 3;

  // Deployment method
  string method = 4;

  // Deployment user
  string deployed_by = 5;

  // Deployment configuration
  map<string, string> config = 6;

  // Deployment artifacts
  repeated string artifacts = 7;

  // Deployment health
  VersionHealthStatus health = 8;

  // Deployment metrics
  map<string, double> metrics = 9;
}

```

---

### version_deployment_status.proto {#version_deployment_status}

**Path**: `pkg/config/proto/version_deployment_status.proto` **Package**: `gcommon.v1.config` **Lines**: 25

**Enums** (1): `VersionDeploymentStatus`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/audit_log.proto` → [auth_events](./auth_events.md#audit_log) → [common](./common.md#audit_log)

#### Source Code

```protobuf
// file: pkg/config/proto/version_deployment_status.proto
// version: 1.0.0
// guid: ff99e66b-873a-415d-8f2e-df2a6b1a25c2

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/common/proto/audit_log.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

enum VersionDeploymentStatus {
  VERSION_DEPLOYMENT_STATUS_UNSPECIFIED = 0;
  VERSION_DEPLOYMENT_STATUS_PENDING = 1;
  VERSION_DEPLOYMENT_STATUS_IN_PROGRESS = 2;
  VERSION_DEPLOYMENT_STATUS_SUCCESS = 3;
  VERSION_DEPLOYMENT_STATUS_FAILED = 4;
  VERSION_DEPLOYMENT_STATUS_ROLLED_BACK = 5;
  VERSION_DEPLOYMENT_STATUS_CANCELLED = 6;
}

```

---

### version_health_status.proto {#version_health_status}

**Path**: `pkg/config/proto/version_health_status.proto` **Package**: `gcommon.v1.config` **Lines**: 23

**Enums** (1): `VersionHealthStatus`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/audit_log.proto` → [auth_events](./auth_events.md#audit_log) → [common](./common.md#audit_log)

#### Source Code

```protobuf
// file: pkg/config/proto/version_health_status.proto
// version: 1.0.0
// guid: 71f9e59c-35f1-439c-9785-8149f061e4d9

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/common/proto/audit_log.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

enum VersionHealthStatus {
  VERSION_HEALTH_STATUS_UNSPECIFIED = 0;
  VERSION_HEALTH_STATUS_HEALTHY = 1;
  VERSION_HEALTH_STATUS_DEGRADED = 2;
  VERSION_HEALTH_STATUS_UNHEALTHY = 3;
  VERSION_HEALTH_STATUS_UNKNOWN = 4;
}

```

---

### version_quality_issue.proto {#version_quality_issue}

**Path**: `pkg/config/proto/version_quality_issue.proto` **Package**: `gcommon.v1.config` **Lines**: 35

**Messages** (1): `VersionQualityIssue`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/audit_log.proto` → [auth_events](./auth_events.md#audit_log) → [common](./common.md#audit_log)

#### Source Code

```protobuf
// file: pkg/config/proto/version_quality_issue.proto
// version: 1.0.0
// guid: 98aad520-640b-4663-a48a-ec3928c41c6a

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/common/proto/audit_log.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message VersionQualityIssue {
  // Issue type
  string type = 1;

  // Issue severity
  string severity = 2;

  // Issue description
  string description = 3;

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

**Path**: `pkg/config/proto/version_quality_metrics.proto` **Package**: `gcommon.v1.config` **Lines**: 45

**Messages** (1): `VersionQualityMetrics`

**Imports** (4):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/audit_log.proto` → [auth_events](./auth_events.md#audit_log) → [common](./common.md#audit_log)
- `pkg/config/proto/version_quality_issue.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/version_quality_metrics.proto
// version: 1.0.0
// guid: 2326770b-b97a-4a96-93aa-b093931437a7

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/common/proto/audit_log.proto";
import "pkg/config/proto/version_quality_issue.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message VersionQualityMetrics {
  // Code quality score
  double quality_score = 1;

  // Test coverage
  double test_coverage = 2;

  // Security score
  double security_score = 3;

  // Performance score
  double performance_score = 4;

  // Complexity score
  double complexity_score = 5;

  // Technical debt score
  double technical_debt_score = 6;

  // Quality gate status
  bool quality_gate_passed = 7;

  // Quality issues
  repeated VersionQualityIssue issues = 8;

  // Quality metrics timestamp
  google.protobuf.Timestamp timestamp = 9;
}

```

---

### version_status.proto {#version_status}

**Path**: `pkg/config/proto/version_status.proto` **Package**: `gcommon.v1.config` **Lines**: 27

**Enums** (1): `VersionStatus`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/audit_log.proto` → [auth_events](./auth_events.md#audit_log) → [common](./common.md#audit_log)

#### Source Code

```protobuf
// file: pkg/config/proto/version_status.proto
// version: 1.0.0
// guid: 55704401-46f6-4b87-94a8-11020525cfe4

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/common/proto/audit_log.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

enum VersionStatus {
  VERSION_STATUS_UNSPECIFIED = 0;
  VERSION_STATUS_DRAFT = 1;
  VERSION_STATUS_PENDING = 2;
  VERSION_STATUS_ACTIVE = 3;
  VERSION_STATUS_DEPRECATED = 4;
  VERSION_STATUS_ARCHIVED = 5;
  VERSION_STATUS_DELETED = 6;
  VERSION_STATUS_FAILED = 7;
  VERSION_STATUS_CANCELLED = 8;
}

```

---

### version_type.proto {#version_type}

**Path**: `pkg/config/proto/version_type.proto` **Package**: `gcommon.v1.config` **Lines**: 27

**Enums** (1): `VersionType`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/audit_log.proto` → [auth_events](./auth_events.md#audit_log) → [common](./common.md#audit_log)

#### Source Code

```protobuf
// file: pkg/config/proto/version_type.proto
// version: 1.0.0
// guid: 38337d79-8f7d-4d84-bc08-cf277adfd568

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/common/proto/audit_log.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

enum VersionType {
  VERSION_TYPE_UNSPECIFIED = 0;
  VERSION_TYPE_MAJOR = 1;
  VERSION_TYPE_MINOR = 2;
  VERSION_TYPE_PATCH = 3;
  VERSION_TYPE_HOTFIX = 4;
  VERSION_TYPE_PRERELEASE = 5;
  VERSION_TYPE_SNAPSHOT = 6;
  VERSION_TYPE_BRANCH = 7;
  VERSION_TYPE_TAG = 8;
}

```

---
