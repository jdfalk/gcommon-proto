# log Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 14
- **Messages**: 9
- **Services**: 0
- **Enums**: 7

## Files in this Module

- [appender_config.proto](#appender_config)
- [appender_type.proto](#appender_type)
- [archive_criteria.proto](#archive_criteria)
- [compression_type.proto](#compression_type)
- [error_info.proto](#error_info)
- [filter_type.proto](#filter_type)
- [formatter_type.proto](#formatter_type)
- [log_entry.proto](#log_entry)
- [log_level.proto](#log_level)
- [log_sort_field.proto](#log_sort_field)
- [log_statistics.proto](#log_statistics)
- [logger_config.proto](#logger_config)
- [logger_status.proto](#logger_status)
- [source_location.proto](#source_location)

## Module Dependencies

**This module depends on**:

- [common](./common.md)

**Modules that depend on this one**:

- [config_1](./config_1.md)
- [web_config_1](./web_config_1.md)

---

## Detailed Documentation

### appender_config.proto {#appender_config}

**Path**: `pkg/log/proto/appender_config.proto` **Package**: `gcommon.v1.log` **Lines**: 51

**Messages** (3): `AppenderConfig`, `OutputConfig`, `FormatterConfig`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/log/proto/appender_type.proto`
- `pkg/log/proto/formatter_type.proto`

#### Source Code

```protobuf
// file: pkg/log/proto/messages/appender_config.proto
// version: 1.0.0
// guid: fbec1110-0be5-48a4-8a3a-e748a66b4764

edition = "2023";

package gcommon.v1.log;

import "google/protobuf/go_features.proto";
import "pkg/log/proto/appender_type.proto";
import "pkg/log/proto/formatter_type.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/log/proto";

// AppenderConfig describes how logs are output
message AppenderConfig {
  // Unique appender name
  string name = 1;

  // Appender backend type
  AppenderType type = 2;

  // Output destination details
  OutputConfig output = 3;

  // Formatting configuration
  FormatterConfig formatter = 4;

  // Arbitrary appender properties
  map<string, string> properties = 5;

  // OutputConfig defines the destination for log entries
  message OutputConfig {
    // Output target (file path, network address, etc.)
    string target = 1;

    // Additional output options
    map<string, string> options = 2;
  }

  // FormatterConfig defines how log entries are formatted
  message FormatterConfig {
    // Formatting strategy
    FormatterType type = 1;

    // Optional format pattern
    string pattern = 2;
  }
}

```

---

### appender_type.proto {#appender_type}

**Path**: `pkg/log/proto/appender_type.proto` **Package**: `gcommon.v1.log` **Lines**: 24

**Enums** (1): `AppenderType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/log/proto/enums/appender_type.proto
// version: 1.0.0
// guid: 5e2f63bf-35c4-4a2a-b35a-54017c979940

edition = "2023";

package gcommon.v1.log;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/log/proto";

// AppenderType enumerates logging output backends
enum AppenderType {
  APPENDER_TYPE_UNSPECIFIED = 0;
  APPENDER_TYPE_CONSOLE = 1;
  APPENDER_TYPE_FILE = 2;
  APPENDER_TYPE_ROLLING_FILE = 3;
  APPENDER_TYPE_SYSLOG = 4;
  APPENDER_TYPE_NETWORK = 5;
  APPENDER_TYPE_DATABASE = 6;
}

```

---

### archive_criteria.proto {#archive_criteria}

**Path**: `pkg/log/proto/archive_criteria.proto` **Package**: `gcommon.v1.log` **Lines**: 23

**Messages** (1): `ArchiveCriteria`

**Imports** (2):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/log/proto/messages/archive_criteria.proto
// version: 1.0.0
// guid: b7d23f2c-0017-462f-a6d2-51ca4405bc2c

edition = "2023";

package gcommon.v1.log;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/log/proto";

// ArchiveCriteria defines rules for selecting log files to archive
message ArchiveCriteria {
  // Only archive logs older than this duration
  google.protobuf.Duration older_than = 1;

  // Minimum size threshold in bytes
  int64 size_threshold_bytes = 2;
}

```

---

### compression_type.proto {#compression_type}

**Path**: `pkg/log/proto/compression_type.proto` **Package**: `gcommon.v1.log` **Lines**: 23

**Enums** (1): `CompressionType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/log/proto/enums/compression_type.proto
// version: 1.0.0
// guid: 357b1a04-97e4-4d82-86a3-b6672180ce22

edition = "2023";

package gcommon.v1.log;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/log/proto";

// CompressionType enumerates archive compression formats
enum CompressionType {
  COMPRESSION_TYPE_UNSPECIFIED = 0;
  COMPRESSION_TYPE_NONE = 1;
  COMPRESSION_TYPE_GZIP = 2;
  COMPRESSION_TYPE_ZIP = 3;
  COMPRESSION_TYPE_BZIP2 = 4;
  COMPRESSION_TYPE_TAR_GZ = 5;
}

```

---

### error_info.proto {#error_info}

**Path**: `pkg/log/proto/error_info.proto` **Package**: `gcommon.v1.log` **Lines**: 34

**Messages** (1): `ErrorInfo`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/log/proto/messages/error_info.proto
// version: 1.0.0
// guid: ba36f77a-0141-43fc-a77e-fde479168a40

edition = "2023";

package gcommon.v1.log;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/log/proto";

// ErrorInfo provides structured error details for log entries
message ErrorInfo {
  // Error message
  string message = 1;

  // Error type or class name
  string type = 2;

  // Full stack trace if available
  string stack_trace = 3;

  // Application-specific error code
  string code = 4;

  // Arbitrary key/value context information
  map<string, string> context = 5;

  // Nested causes for error propagation
  repeated ErrorInfo causes = 6;
}

```

---

### filter_type.proto {#filter_type}

**Path**: `pkg/log/proto/filter_type.proto` **Package**: `gcommon.v1.log` **Lines**: 22

**Enums** (1): `FilterType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/log/proto/enums/filter_type.proto
// version: 1.0.0
// guid: eb317c45-0d04-48fb-ab44-ab82262f995b

edition = "2023";

package gcommon.v1.log;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/log/proto";

// FilterType enumerates log filter strategies
enum FilterType {
  FILTER_TYPE_UNSPECIFIED = 0;
  FILTER_TYPE_LEVEL = 1;
  FILTER_TYPE_LOGGER = 2;
  FILTER_TYPE_MESSAGE = 3;
  FILTER_TYPE_FIELD = 4;
}

```

---

### formatter_type.proto {#formatter_type}

**Path**: `pkg/log/proto/formatter_type.proto` **Package**: `gcommon.v1.log` **Lines**: 22

**Enums** (1): `FormatterType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/log/proto/enums/formatter_type.proto
// version: 1.0.0
// guid: 0d49c8f5-9abd-4a9e-8d96-ddab6f45249b

edition = "2023";

package gcommon.v1.log;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/log/proto";

// FormatterType enumerates log formatting strategies
enum FormatterType {
  FORMATTER_TYPE_UNSPECIFIED = 0;
  FORMATTER_TYPE_TEXT = 1;
  FORMATTER_TYPE_JSON = 2;
  FORMATTER_TYPE_XML = 3;
  FORMATTER_TYPE_CUSTOM = 4;
}

```

---

### log_entry.proto {#log_entry}

**Path**: `pkg/log/proto/log_entry.proto` **Package**: `gcommon.v1.log` **Lines**: 61

**Messages** (1): `LogEntry`

**Imports** (7):

- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/log/proto/error_info.proto`
- `pkg/log/proto/log_level.proto`
- `pkg/log/proto/source_location.proto`

#### Source Code

```protobuf
// file: pkg/log/proto/messages/log_entry.proto
// version: 1.0.0
// guid: 86cfa864-b9da-428c-9ca9-78f614600049

edition = "2023";

package gcommon.v1.log;

import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/common/proto/error.proto";
import "pkg/log/proto/error_info.proto";
import "pkg/log/proto/log_level.proto";
import "pkg/log/proto/source_location.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/log/proto";

// LogEntry represents a single structured log event
message LogEntry {
  // Log level
  LogLevel level = 1;

  // Log message
  string message = 2;

  // Timestamp of the log event
  google.protobuf.Timestamp timestamp = 3;

  // Logger name
  string logger = 4;

  // Thread or goroutine identifier
  string thread = 5;

  // Source code location
  SourceLocation source = 6;

  // Structured fields for context
  map<string, google.protobuf.Any> fields = 7;

  // Tags for categorization
  repeated string tags = 8;

  // Trace ID for distributed tracing
  string trace_id = 9;

  // Span ID for distributed tracing
  string span_id = 10;

  // User ID associated with the log
  string user_id = 11;

  // Request ID for correlation
  string request_id = 12;

  // Detailed error information
  ErrorInfo error_info = 13;
}

```

---

### log_level.proto {#log_level}

**Path**: `pkg/log/proto/log_level.proto` **Package**: `gcommon.v1.log` **Lines**: 24

**Enums** (1): `LogLevel`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/log/proto/enums/log_level.proto
// version: 1.0.0
// guid: ef4e8667-0bff-4dda-bb43-56d0a1ef8421

edition = "2023";

package gcommon.v1.log;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/log/proto";

// LogLevel defines severity levels for log entries
enum LogLevel {
  LOG_LEVEL_UNSPECIFIED = 0;
  LOG_LEVEL_TRACE = 1;
  LOG_LEVEL_DEBUG = 2;
  LOG_LEVEL_INFO = 3;
  LOG_LEVEL_WARN = 4;
  LOG_LEVEL_ERROR = 5;
  LOG_LEVEL_FATAL = 6;
}

```

---

### log_sort_field.proto {#log_sort_field}

**Path**: `pkg/log/proto/log_sort_field.proto` **Package**: `gcommon.v1.log` **Lines**: 22

**Enums** (1): `LogSortField`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/log/proto/enums/log_sort_field.proto
// version: 1.0.0
// guid: 8d1776a3-51f0-43c4-8199-698ee5ba98e7

edition = "2023";

package gcommon.v1.log;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/log/proto";

// LogSortField enumerates fields usable for log sorting
enum LogSortField {
  LOG_SORT_FIELD_UNSPECIFIED = 0;
  LOG_SORT_FIELD_TIMESTAMP = 1;
  LOG_SORT_FIELD_LEVEL = 2;
  LOG_SORT_FIELD_LOGGER = 3;
  LOG_SORT_FIELD_MESSAGE = 4;
}

```

---

### log_statistics.proto {#log_statistics}

**Path**: `pkg/log/proto/log_statistics.proto` **Package**: `gcommon.v1.log` **Lines**: 34

**Messages** (1): `LogStatistics`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/log/proto/messages/log_statistics.proto
// version: 1.0.0
// guid: 98acfd30-4a7f-43f6-ac8d-f10a598a805a

edition = "2023";

package gcommon.v1.log;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/log/proto";

// LogStatistics provides aggregated metrics about log entries
message LogStatistics {
  // Total log entries
  int64 total_entries = 1;

  // Entries per second
  double entries_per_second = 2;

  // Average entry size
  int64 average_size = 3;

  // Total size of all log entries
  int64 total_size = 4;

  // Count of log entries with level ERROR
  int64 error_count = 5;

  // Count of log entries with level WARNING
  int64 warning_count = 6;
}

```

---

### logger_config.proto {#logger_config}

**Path**: `pkg/log/proto/logger_config.proto` **Package**: `gcommon.v1.log` **Lines**: 33

**Messages** (1): `LoggerConfig`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/log/proto/appender_config.proto`
- `pkg/log/proto/log_level.proto`

#### Source Code

```protobuf
// file: pkg/log/proto/messages/logger_config.proto
// version: 1.0.0
// guid: 37c6c755-fc97-46c2-8116-248fc5a0ce3c

edition = "2023";

package gcommon.v1.log;

import "google/protobuf/go_features.proto";
import "pkg/log/proto/appender_config.proto";
import "pkg/log/proto/log_level.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/log/proto";

// LoggerConfig defines configuration for a logger instance
message LoggerConfig {
  // Minimum log level for this logger
  LogLevel level = 1;

  // Output appenders used by this logger
  repeated AppenderConfig appenders = 2;

  // Inherit appenders from parent logger
  bool inherit_appenders = 3;

  // Propagate log entries to parent logger
  bool propagate = 4;

  // Additional logger properties
  map<string, string> properties = 5;
}

```

---

### logger_status.proto {#logger_status}

**Path**: `pkg/log/proto/logger_status.proto` **Package**: `gcommon.v1.log` **Lines**: 21

**Enums** (1): `LoggerStatus`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/log/proto/enums/logger_status.proto
// version: 1.0.0
// guid: c65806e5-27c2-4c3e-8f3b-e23b66bca610

edition = "2023";

package gcommon.v1.log;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/log/proto";

// LoggerStatus represents health of a logger instance
enum LoggerStatus {
  LOGGER_STATUS_UNSPECIFIED = 0;
  LOGGER_STATUS_ACTIVE = 1;
  LOGGER_STATUS_INACTIVE = 2;
  LOGGER_STATUS_ERROR = 3;
}

```

---

### source_location.proto {#source_location}

**Path**: `pkg/log/proto/source_location.proto` **Package**: `gcommon.v1.log` **Lines**: 28

**Messages** (1): `SourceLocation`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/log/proto/messages/source_location.proto
// version: 1.0.0
// guid: b529bc13-5c0e-4b3e-9d64-5025a5889fa2

edition = "2023";

package gcommon.v1.log;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/log/proto";

// SourceLocation describes the origin of a log entry
message SourceLocation {
  // File name where the log occurred
  string file = 1;

  // Line number in the source file
  int32 line = 2;

  // Function name
  string function = 3;

  // Package or module name
  string package = 4;
}

```

---
