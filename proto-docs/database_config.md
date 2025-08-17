# database_config Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 3
- **Messages**: 3
- **Services**: 0
- **Enums**: 0

## Files in this Module

- [cockroach_config.proto](#cockroach_config)
- [mysql_config.proto](#mysql_config)
- [pebble_config.proto](#pebble_config)

---

## Detailed Documentation

### cockroach_config.proto {#cockroach_config}

**Path**: `pkg/db/proto/cockroach_config.proto` **Package**: `gcommon.v1.database` **Lines**: 46

**Messages** (1): `CockroachConfig`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/db/proto/messages/cockroach_config.proto
// version: 1.0.0
// guid: a505881e-946a-4a19-9fd5-1e81405e1f73

edition = "2023";

package gcommon.v1.database;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/db/proto";

/**
 * CockroachConfig provides CockroachDB-specific connection configuration.
 * Includes retry behavior and identification options for robust connections.
 */
message CockroachConfig {
  // Host is the database host.
  string host = 1;

  // Port is the database port.
  int32 port = 2;

  // User is the database user.
  string user = 3;

  // Password is the database password.
  string password = 4;

  // Database is the database name.
  string database = 5;

  // SSLMode is the SSL mode.
  string ssl_mode = 6;

  // ApplicationName is the application name.
  string application_name = 7;

  // RetryBackoffFactor is the retry backoff factor.
  float retry_backoff_factor = 8;

  // MaxRetries is the maximum number of retries.
  int32 max_retries = 9;
}

```

---

### mysql_config.proto {#mysql_config}

**Path**: `pkg/db/proto/mysql_config.proto` **Package**: `gcommon.v1.database` **Lines**: 27

**Messages** (1): `MySQLConfig`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/db/proto/messages/mysql_config.proto
edition = "2023";

package gcommon.v1.database;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/db/proto";

/**
 * MySQLConfig defines connection parameters for MySQL databases.
 */
message MySQLConfig {
  // MySQL connection DSN string
  string dsn = 1;

  // Maximum number of open connections
  int32 max_open_conns = 2;

  // Maximum number of idle connections
  int32 max_idle_conns = 3;

  // Connection timeout in seconds
  int32 connect_timeout_seconds = 4;
}

```

---

### pebble_config.proto {#pebble_config}

**Path**: `pkg/db/proto/pebble_config.proto` **Package**: `gcommon.v1.database` **Lines**: 34

**Messages** (1): `PebbleConfig`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/db/proto/types/pebble_config.proto
// version: 1.0.0
// guid: 3d548f91-9c4d-4fe7-b610-fd2cafd073ef

edition = "2023";

package gcommon.v1.database;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/db/proto";

/**
 * PebbleConfig represents Pebble-specific configuration options
 * for the embedded key-value store driver.
 */
message PebbleConfig {
  // Path is the directory where the database files are stored
  string path = 1;

  // CacheSize is the size of the block cache in bytes
  int64 cache_size = 2;

  // MemtableSize is the memtable size in bytes
  int64 memtable_size = 3;

  // MaxOpenFiles is the maximum number of open files
  int32 max_open_files = 4;

  // Compression enables on-disk compression when true
  bool compression = 5;
}

```

---
