# Config Services Documentation

[← Back to Index](./README.md)

## Module Overview

- **Proto Files**: 2
- **Services**: 2

## Table of Contents

### Services

- [`ConfigAdminService`](#config_admin_service) - from config_admin_service.proto
- [`ConfigService`](#config_service) - from config_service.proto

### Files in this Module

- [config_admin_service.proto](#config_admin_service)
- [config_service.proto](#config_service)

---


## Services Documentation

### config_admin_service.proto {#config_admin_service}

**Path**: `gcommon/v1/config/config_admin_service.proto` **Package**: `gcommon.v1.config` **Lines**: 67

**Services** (1): `ConfigAdminService`

**Imports** (18):

- `gcommon/v1/config/backup_config_request.proto`
- `gcommon/v1/config/config_backup.proto`
- `gcommon/v1/config/config_snapshot.proto`
- `gcommon/v1/config/export_config_request.proto`
- `gcommon/v1/config/get_config_history_request.proto`
- `gcommon/v1/config/get_config_history_response.proto`
- `gcommon/v1/config/get_config_stats_request.proto`
- `gcommon/v1/config/get_config_stats_response.proto`
- `gcommon/v1/config/health_check_request.proto`
- `gcommon/v1/config/health_check_response.proto`
- `gcommon/v1/config/import_config_request.proto`
- `gcommon/v1/config/reload_config_request.proto`
- `gcommon/v1/config/restore_config_request.proto`
- `gcommon/v1/config/rollback_config_request.proto`
- `gcommon/v1/config/set_config_schema_request.proto`
- `gcommon/v1/config/unwatch_config_request.proto`
- `google/protobuf/empty.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/v1/config_admin_service.proto
// version: 1.0.1
// guid: 115f65c3-94f2-4c4d-892d-27eb6c9fcece

edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/config/backup_config_request.proto";
import "gcommon/v1/config/config_backup.proto";
import "gcommon/v1/config/config_snapshot.proto";
import "gcommon/v1/config/export_config_request.proto";
import "gcommon/v1/config/get_config_history_request.proto";
import "gcommon/v1/config/get_config_history_response.proto";
import "gcommon/v1/config/get_config_stats_request.proto";
import "gcommon/v1/config/get_config_stats_response.proto";
import "gcommon/v1/config/health_check_request.proto";
import "gcommon/v1/config/health_check_response.proto";
import "gcommon/v1/config/import_config_request.proto";
import "gcommon/v1/config/reload_config_request.proto";
import "gcommon/v1/config/restore_config_request.proto";
import "gcommon/v1/config/rollback_config_request.proto";
import "gcommon/v1/config/set_config_schema_request.proto";
import "gcommon/v1/config/unwatch_config_request.proto";
import "google/protobuf/empty.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

/**
 * ConfigAdminService provides administrative configuration operations.
 */
service ConfigAdminService {
  // Create a configuration backup
  rpc BackupConfig(BackupConfigRequest) returns (ConfigBackup);

  // Restore configuration from a backup or restore point
  rpc RestoreConfig(RestoreConfigRequest) returns (google.protobuf.Empty);

  // Import configuration values
  rpc ImportConfig(ImportConfigRequest) returns (google.protobuf.Empty);

  // Export configuration snapshot
  rpc ExportConfig(ExportConfigRequest) returns (ConfigSnapshot);

  // Reload configuration from persistent storage
  rpc ReloadConfig(ReloadConfigRequest) returns (google.protobuf.Empty);

  // Roll back configuration to a previous restore point
  rpc RollbackConfig(RollbackConfigRequest) returns (google.protobuf.Empty);

  // Update configuration schema
  rpc SetConfigSchema(SetConfigSchemaRequest) returns (google.protobuf.Empty);

  // Retrieve configuration change history
  rpc GetConfigHistory(GetConfigHistoryRequest) returns (GetConfigHistoryResponse);

  // Retrieve configuration statistics
  rpc GetConfigStats(GetConfigStatsRequest) returns (GetConfigStatsResponse);

  // Perform service health check
  rpc HealthCheck(ConfigHealthCheckRequest) returns (ConfigHealthCheckResponse);

  // Stop watching configuration changes
  rpc UnwatchConfig(UnwatchConfigRequest) returns (google.protobuf.Empty);
}
```

---

### config_service.proto {#config_service}

**Path**: `gcommon/v1/config/config_service.proto` **Package**: `gcommon.v1.config` **Lines**: 62

**Services** (1): `ConfigService`

**Imports** (19):

- `gcommon/v1/config/delete_config_request.proto`
- `gcommon/v1/config/get_config_request.proto`
- `gcommon/v1/config/get_config_response.proto`
- `gcommon/v1/config/get_multiple_config_request.proto`
- `gcommon/v1/config/get_multiple_config_response.proto`
- `gcommon/v1/config/get_schema_request.proto`
- `gcommon/v1/config/get_schema_response.proto`
- `gcommon/v1/config/list_config_request.proto`
- `gcommon/v1/config/list_config_response.proto`
- `gcommon/v1/config/set_config_request.proto`
- `gcommon/v1/config/set_config_response.proto`
- `gcommon/v1/config/set_multiple_config_request.proto`
- `gcommon/v1/config/set_multiple_config_response.proto`
- `gcommon/v1/config/validate_config_request.proto`
- `gcommon/v1/config/validate_config_response.proto`
- `gcommon/v1/config/watch_config_request.proto`
- `gcommon/v1/config/watch_config_response.proto`
- `google/protobuf/empty.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/v1/config_service.proto
// version: 1.0.1
// guid: 25a56c3e-a656-4d5c-9dde-10fa021e7db6
edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/config/delete_config_request.proto";
import "gcommon/v1/config/get_config_request.proto";
import "gcommon/v1/config/get_config_response.proto";
import "gcommon/v1/config/get_multiple_config_request.proto";
import "gcommon/v1/config/get_multiple_config_response.proto";
import "gcommon/v1/config/get_schema_request.proto";
import "gcommon/v1/config/get_schema_response.proto";
import "gcommon/v1/config/list_config_request.proto";
import "gcommon/v1/config/list_config_response.proto";
import "gcommon/v1/config/set_config_request.proto";
import "gcommon/v1/config/set_config_response.proto";
import "gcommon/v1/config/set_multiple_config_request.proto";
import "gcommon/v1/config/set_multiple_config_response.proto";
import "gcommon/v1/config/validate_config_request.proto";
import "gcommon/v1/config/validate_config_response.proto";
import "gcommon/v1/config/watch_config_request.proto";
import "gcommon/v1/config/watch_config_response.proto";
import "google/protobuf/empty.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

/**
 * ConfigService provides configuration management capabilities.
 * Supports hierarchical configuration, validation, and real-time updates.
 */
service ConfigService {
  // Get retrieves a configuration value
  rpc Get(GetConfigRequest) returns (GetConfigResponse);

  // Set stores a configuration value
  rpc Set(SetConfigRequest) returns (SetConfigResponse);

  // Delete removes a configuration value
  rpc Delete(DeleteConfigRequest) returns (google.protobuf.Empty);

  // List configuration keys with optional filtering
  rpc List(ListConfigRequest) returns (ListConfigResponse);

  // Watch for configuration changes
  rpc Watch(WatchConfigRequest) returns (stream WatchConfigResponse);

  // GetMultiple retrieves multiple configuration values
  rpc GetMultiple(GetMultipleConfigRequest) returns (GetMultipleConfigResponse);

  // SetMultiple stores multiple configuration values
  rpc SetMultiple(SetMultipleConfigRequest) returns (SetMultipleConfigResponse);

  // Validate configuration values
  rpc Validate(ValidateConfigRequest) returns (ValidateConfigResponse);

  // GetSchema retrieves configuration schema
  rpc GetSchema(GetSchemaRequest) returns (GetSchemaResponse);
}
```

---

