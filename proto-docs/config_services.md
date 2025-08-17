# config_services Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 2
- **Messages**: 0
- **Services**: 2
- **Enums**: 0

## Files in this Module

- [config_admin_service.proto](#config_admin_service)
- [config_service.proto](#config_service)

## Module Dependencies

**This module depends on**:

- [auth_api_2](./auth_api_2.md)
- [cache_api_1](./cache_api_1.md)
- [config_api](./config_api.md)
- [config_config_1](./config_config_1.md)
- [config_config_2](./config_config_2.md)
- [database_api](./database_api.md)
- [health](./health.md)
- [metrics_api_1](./metrics_api_1.md)
- [queue_api_2](./queue_api_2.md)
- [web_api_2](./web_api_2.md)

---

## Detailed Documentation

### config_admin_service.proto {#config_admin_service}

**Path**: `pkg/config/proto/config_admin_service.proto` **Package**: `gcommon.v1.config` **Lines**: 68

**Services** (1): `ConfigAdminService`

**Imports** (18):

- `google/protobuf/empty.proto`
- `google/protobuf/go_features.proto`
- `pkg/config/proto/backup_config_request.proto` → [config_config_1](./config_config_1.md#backup_config_request)
- `pkg/config/proto/config_backup.proto` → [config_config_1](./config_config_1.md#config_backup)
- `pkg/config/proto/config_snapshot.proto` → [config_config_1](./config_config_1.md#config_snapshot)
- `pkg/config/proto/export_config_request.proto` → [config_config_1](./config_config_1.md#export_config_request)
- `pkg/config/proto/get_config_history_request.proto` → [config_config_1](./config_config_1.md#get_config_history_request)
- `pkg/config/proto/get_config_history_response.proto` → [config_config_1](./config_config_1.md#get_config_history_response)
- `pkg/config/proto/get_config_stats_request.proto` → [config_config_1](./config_config_1.md#get_config_stats_request)
- `pkg/config/proto/get_config_stats_response.proto` → [config_config_1](./config_config_1.md#get_config_stats_response)
- `pkg/config/proto/health_check_request.proto` → [auth_api_2](./auth_api_2.md#health_check_request) → [cache_api_1](./cache_api_1.md#health_check_request) → [config_api](./config_api.md#health_check_request) →
  [database_api](./database_api.md#health_check_request) → [health](./health.md#health_check_request) → [metrics_api_1](./metrics_api_1.md#health_check_request) → [queue_api_2](./queue_api_2.md#health_check_request) →
  [web_api_2](./web_api_2.md#health_check_request)
- `pkg/config/proto/health_check_response.proto` → [auth_api_2](./auth_api_2.md#health_check_response) → [config_api](./config_api.md#health_check_response) → [database_api](./database_api.md#health_check_response) →
  [health](./health.md#health_check_response) → [metrics_api_1](./metrics_api_1.md#health_check_response) → [queue_api_2](./queue_api_2.md#health_check_response) → [web_api_2](./web_api_2.md#health_check_response)
- `pkg/config/proto/import_config_request.proto` → [config_config_1](./config_config_1.md#import_config_request)
- `pkg/config/proto/reload_config_request.proto` → [config_config_1](./config_config_1.md#reload_config_request)
- `pkg/config/proto/restore_config_request.proto` → [config_config_1](./config_config_1.md#restore_config_request)
- `pkg/config/proto/rollback_config_request.proto` → [config_config_1](./config_config_1.md#rollback_config_request)
- `pkg/config/proto/set_config_schema_request.proto` → [config_config_1](./config_config_1.md#set_config_schema_request)
- `pkg/config/proto/unwatch_config_request.proto` → [config_config_2](./config_config_2.md#unwatch_config_request)

#### Source Code

```protobuf
// file: pkg/config/proto/services/config_admin_service.proto
// version: 1.0.0
// guid: 115f65c3-94f2-4c4d-892d-27eb6c9fcece

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/empty.proto";
import "google/protobuf/go_features.proto";
import "pkg/config/proto/backup_config_request.proto";
import "pkg/config/proto/config_backup.proto";
import "pkg/config/proto/config_snapshot.proto";
import "pkg/config/proto/export_config_request.proto";
import "pkg/config/proto/get_config_history_request.proto";
import "pkg/config/proto/get_config_history_response.proto";
import "pkg/config/proto/get_config_stats_request.proto";
import "pkg/config/proto/get_config_stats_response.proto";
import "pkg/config/proto/health_check_request.proto";
import "pkg/config/proto/health_check_response.proto";
import "pkg/config/proto/import_config_request.proto";
import "pkg/config/proto/reload_config_request.proto";
import "pkg/config/proto/restore_config_request.proto";
import "pkg/config/proto/rollback_config_request.proto";
import "pkg/config/proto/set_config_schema_request.proto";
import "pkg/config/proto/unwatch_config_request.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

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
  rpc HealthCheck(HealthCheckRequest) returns (HealthCheckResponse);

  // Stop watching configuration changes
  rpc UnwatchConfig(UnwatchConfigRequest) returns (google.protobuf.Empty);
}

```

---

### config_service.proto {#config_service}

**Path**: `pkg/config/proto/config_service.proto` **Package**: `gcommon.v1.config` **Lines**: 61

**Services** (1): `ConfigService`

**Imports** (19):

- `google/protobuf/empty.proto`
- `google/protobuf/go_features.proto`
- `pkg/config/proto/delete_config_request.proto` → [config_config_1](./config_config_1.md#delete_config_request)
- `pkg/config/proto/get_config_request.proto` → [config_config_1](./config_config_1.md#get_config_request)
- `pkg/config/proto/get_config_response.proto` → [config_config_1](./config_config_1.md#get_config_response)
- `pkg/config/proto/get_multiple_config_request.proto` → [config_config_1](./config_config_1.md#get_multiple_config_request)
- `pkg/config/proto/get_multiple_config_response.proto` → [config_config_1](./config_config_1.md#get_multiple_config_response)
- `pkg/config/proto/get_schema_request.proto` → [config_api](./config_api.md#get_schema_request)
- `pkg/config/proto/get_schema_response.proto` → [config_api](./config_api.md#get_schema_response)
- `pkg/config/proto/list_config_request.proto` → [config_config_1](./config_config_1.md#list_config_request)
- `pkg/config/proto/list_config_response.proto` → [config_config_1](./config_config_1.md#list_config_response)
- `pkg/config/proto/set_config_request.proto` → [config_config_1](./config_config_1.md#set_config_request)
- `pkg/config/proto/set_config_response.proto` → [config_config_1](./config_config_1.md#set_config_response)
- `pkg/config/proto/set_multiple_config_request.proto` → [config_config_1](./config_config_1.md#set_multiple_config_request)
- `pkg/config/proto/set_multiple_config_response.proto` → [config_config_1](./config_config_1.md#set_multiple_config_response)
- `pkg/config/proto/validate_config_request.proto` → [config_config_2](./config_config_2.md#validate_config_request)
- `pkg/config/proto/validate_config_response.proto` → [config_config_2](./config_config_2.md#validate_config_response)
- `pkg/config/proto/watch_config_request.proto` → [config_config_2](./config_config_2.md#watch_config_request)
- `pkg/config/proto/watch_config_response.proto` → [config_config_2](./config_config_2.md#watch_config_response)

#### Source Code

```protobuf
// file: config/proto/services/config_service.proto
edition = "2023";

package gcommon.v1.config;

import "google/protobuf/empty.proto";
import "google/protobuf/go_features.proto";
import "pkg/config/proto/delete_config_request.proto";
import "pkg/config/proto/get_config_request.proto";
import "pkg/config/proto/get_config_response.proto";
import "pkg/config/proto/get_multiple_config_request.proto";
import "pkg/config/proto/get_multiple_config_response.proto";
import "pkg/config/proto/get_schema_request.proto";
import "pkg/config/proto/get_schema_response.proto";
import "pkg/config/proto/list_config_request.proto";
import "pkg/config/proto/list_config_response.proto";
import "pkg/config/proto/set_config_request.proto";
import "pkg/config/proto/set_config_response.proto";
import "pkg/config/proto/set_multiple_config_request.proto";
import "pkg/config/proto/set_multiple_config_response.proto";
import "pkg/config/proto/validate_config_request.proto";
import "pkg/config/proto/validate_config_response.proto";
import "pkg/config/proto/watch_config_request.proto";
import "pkg/config/proto/watch_config_response.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

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
