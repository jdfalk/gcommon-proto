# organization_config Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 18
- **Messages**: 18
- **Services**: 0
- **Enums**: 0

## Files in this Module

- [api_key_config.proto](#api_key_config)
- [audit_config.proto](#audit_config)
- [auto_scaling_config.proto](#auto_scaling_config)
- [backup_config.proto](#backup_config)
- [cdn_config.proto](#cdn_config)
- [configure_tenant_isolation_request.proto](#configure_tenant_isolation_request)
- [configure_tenant_isolation_response.proto](#configure_tenant_isolation_response)
- [dns_config.proto](#dns_config)
- [domain_config.proto](#domain_config)
- [encryption_config.proto](#encryption_config)
- [health_check_config.proto](#health_check_config)
- [load_balancer_config.proto](#load_balancer_config)
- [o_auth_app_config.proto](#o_auth_app_config)
- [origin_config.proto](#origin_config)
- [rate_limit_config.proto](#rate_limit_config)
- [ssl_config.proto](#ssl_config)
- [storage_backup_config.proto](#storage_backup_config)
- [webhook_config.proto](#webhook_config)
---


## Detailed Documentation

### api_key_config.proto {#api_key_config}

**Path**: `gcommon/v1/organization/api_key_config.proto` **Package**: `gcommon.v1.organization` **Lines**: 31

**Messages** (1): `OrganizationAPIKeyConfig`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/api_key_config.proto
// version: 1.0.0
// guid: 28bb1e15-1e3c-4ae1-bb4f-9daa15fcdf1b

edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message OrganizationAPIKeyConfig {
  // API key name/identifier
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Masked API key (for display purposes)
  string masked_key = 2;

  // API key permissions/scopes
  repeated string scopes = 3;

  // API key expiration date
  google.protobuf.Timestamp expires_at = 4 [lazy = true];
}
```

---

### audit_config.proto {#audit_config}

**Path**: `gcommon/v1/organization/audit_config.proto` **Package**: `gcommon.v1.organization` **Lines**: 35

**Messages** (1): `AuditConfig`

**Imports** (3):

- `gcommon/v1/organization/audit_alert.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/audit_config.proto
// version: 1.0.0
// guid: 404c83b0-6f95-4a24-8f22-55baffc8e465

edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/organization/audit_alert.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message AuditConfig {
  // Whether audit logging is enabled
  bool audit_enabled = 1;

  // Audit log retention period in days
  int32 retention_days = 2 [(buf.validate.field).int32.gte = 0];

  // Audit log storage location
  string storage_location = 3 [(buf.validate.field).string.min_len = 1];

  // Events to audit
  repeated string audited_events = 4 [(buf.validate.field).repeated.min_items = 1];

  // Whether real-time monitoring is enabled
  bool real_time_monitoring = 5;

  // Alert configuration for audit events
  repeated AuditAlert alerts = 6 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### auto_scaling_config.proto {#auto_scaling_config}

**Path**: `gcommon/v1/organization/auto_scaling_config.proto` **Package**: `gcommon.v1.organization` **Lines**: 37

**Messages** (1): `AutoScalingConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/auto_scaling_config.proto
// version: 1.0.0
// guid: 81c51445-10c2-48b8-a056-a652df4f2d64

edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message AutoScalingConfig {
  // Whether auto-scaling is enabled
  bool enabled = 1;

  // Minimum number of instances
  int32 min_instances = 2 [(buf.validate.field).int32.gte = 0];

  // Maximum number of instances
  int32 max_instances = 3 [(buf.validate.field).int32.gte = 0];

  // Target CPU utilization percentage
  int32 target_cpu_percent = 4 [(buf.validate.field).int32.gte = 0];

  // Target memory utilization percentage
  int32 target_memory_percent = 5 [(buf.validate.field).int32.gte = 0];

  // Scale-up cooldown period in seconds
  int32 scale_up_cooldown = 6 [(buf.validate.field).int32.gte = 0];

  // Scale-down cooldown period in seconds
  int32 scale_down_cooldown = 7 [(buf.validate.field).int32.gte = 0];
}
```

---

### backup_config.proto {#backup_config}

**Path**: `gcommon/v1/organization/backup_config.proto` **Package**: `gcommon.v1.organization` **Lines**: 31

**Messages** (1): `OrganizationBackupConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/backup_config.proto
// version: 1.0.0
// guid: af98b66c-3106-4a09-9b66-b3fd3908267e

edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message OrganizationBackupConfig {
  // Whether automated backups are enabled
  bool enabled = 1;

  // Backup frequency (hourly, daily, weekly)
  string frequency = 2 [(buf.validate.field).string.min_len = 1];

  // Backup retention period in days
  int32 retention_days = 3 [(buf.validate.field).int32.gte = 0];

  // Backup storage location
  string storage_location = 4 [(buf.validate.field).string.min_len = 1];

  // Whether point-in-time recovery is enabled
  bool point_in_time_recovery = 5;
}
```

---

### cdn_config.proto {#cdn_config}

**Path**: `gcommon/v1/organization/cdn_config.proto` **Package**: `gcommon.v1.organization` **Lines**: 30

**Messages** (1): `CDNConfig`

**Imports** (4):

- `gcommon/v1/organization/cache_behavior.proto`
- `gcommon/v1/organization/origin_config.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/cdn_config.proto
// version: 1.0.0
// guid: 07ac4644-4b99-4ae2-a2c7-2fb5bcd47e0f

edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/organization/cache_behavior.proto";
import "gcommon/v1/organization/origin_config.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message CDNConfig {
  // CDN provider
  string provider = 1 [(buf.validate.field).string.min_len = 1];

  // CDN distribution ID
  string distribution_id = 2 [(buf.validate.field).string.min_len = 1];

  // Cache behavior settings
  repeated CacheBehavior cache_behaviors = 3 [(buf.validate.field).repeated.min_items = 1];

  // Origin configuration
  OriginConfig origin = 4;
}
```

---

### configure_tenant_isolation_request.proto {#configure_tenant_isolation_request}

**Path**: `gcommon/v1/organization/configure_tenant_isolation_request.proto` **Package**: `gcommon.v1.organization` **Lines**: 27

**Messages** (1): `ConfigureTenantIsolationRequest`

**Imports** (4):

- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/organization/tenant_isolation.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/configure_tenant_isolation_request.proto
// version: 1.0.0
// guid: ea4e2f71-cbce-4d87-9a60-96a9893190b0

edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/organization/tenant_isolation.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message ConfigureTenantIsolationRequest {
  // Request metadata for tracing and context
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Tenant identifier
  string tenant_id = 2 [(buf.validate.field).string.min_len = 1];

  // Isolation configuration to apply
  TenantIsolation isolation = 3;
}
```

---

### configure_tenant_isolation_response.proto {#configure_tenant_isolation_response}

**Path**: `gcommon/v1/organization/configure_tenant_isolation_response.proto` **Package**: `gcommon.v1.organization` **Lines**: 26

**Messages** (1): `ConfigureTenantIsolationResponse`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/organization/tenant_isolation.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/configure_tenant_isolation_response.proto
// version: 1.0.0
// guid: 8bfb868a-9352-4ca3-9e89-57d201252ebc
edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/organization/tenant_isolation.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message ConfigureTenantIsolationResponse {
  // Any errors encountered
  repeated gcommon.v1.common.Error errors = 1 [(buf.validate.field).repeated.min_items = 1];

  // Success status
  bool success = 2;

  // Applied isolation configuration
  TenantIsolation isolation = 3 [lazy = true];
}
```

---

### dns_config.proto {#dns_config}

**Path**: `gcommon/v1/organization/dns_config.proto` **Package**: `gcommon.v1.organization` **Lines**: 29

**Messages** (1): `DNSConfig`

**Imports** (3):

- `gcommon/v1/organization/dns_record.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/dns_config.proto
// version: 1.0.0
// guid: 4ce13993-ded9-4ed1-852c-8e73989b5baa

edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/organization/dns_record.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message DNSConfig {
  // DNS provider
  string provider = 1 [(buf.validate.field).string.min_len = 1];

  // DNS zone ID
  string zone_id = 2 [(buf.validate.field).string.min_len = 1];

  // DNS records
  repeated DNSRecord records = 3 [(buf.validate.field).repeated.min_items = 1];

  // TTL for DNS records
  int32 ttl = 4 [(buf.validate.field).int32.gte = 0];
}
```

---

### domain_config.proto {#domain_config}

**Path**: `gcommon/v1/organization/domain_config.proto` **Package**: `gcommon.v1.organization` **Lines**: 31

**Messages** (1): `DomainConfig`

**Imports** (3):

- `gcommon/v1/organization/dns_config.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/domain_config.proto
// version: 1.0.0
// guid: ee8bb6b4-f822-496b-8109-9bd6ffdbdf7b

edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/organization/dns_config.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message DomainConfig {
  // Custom domain name
  string domain_name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // SSL certificate ARN or ID
  string ssl_certificate = 2;

  // DNS configuration
  DNSConfig dns = 3;

  // Domain validation status
  string validation_status = 4;
}
```

---

### encryption_config.proto {#encryption_config}

**Path**: `gcommon/v1/organization/encryption_config.proto` **Package**: `gcommon.v1.organization` **Lines**: 31

**Messages** (1): `OrganizationEncryptionConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/encryption_config.proto
// version: 1.0.0
// guid: c6adca37-10ae-4aed-9ce2-eb555767c937

edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message OrganizationEncryptionConfig {
  // Whether encryption at rest is enabled
  bool encryption_at_rest = 1;

  // Whether encryption in transit is enabled
  bool encryption_in_transit = 2;

  // Encryption key management service
  string key_management_service = 3 [(buf.validate.field).string.min_len = 1];

  // Customer-managed encryption key ID
  string customer_key_id = 4 [(buf.validate.field).string.min_len = 1];

  // Encryption algorithm used
  string encryption_algorithm = 5 [(buf.validate.field).string.min_len = 1];
}
```

---

### health_check_config.proto {#health_check_config}

**Path**: `gcommon/v1/organization/health_check_config.proto` **Package**: `gcommon.v1.organization` **Lines**: 37

**Messages** (1): `OrganizationHealthCheckConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/health_check_config.proto
// version: 1.0.0
// guid: 3d161671-ebd9-42de-857a-2aef7ff4b62a

edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message OrganizationHealthCheckConfig {
  // Health check path
  string path = 1 [(buf.validate.field).string.min_len = 1];

  // Health check port
  int32 port = 2 [(buf.validate.field).int32.gte = 1, (buf.validate.field).int32.lte = 65535];

  // Health check protocol (HTTP, HTTPS, TCP)
  string protocol = 3 [(buf.validate.field).string.min_len = 1];

  // Health check interval in seconds
  int32 interval_seconds = 4 [(buf.validate.field).int32.gte = 0];

  // Health check timeout in seconds
  int32 timeout_seconds = 5 [(buf.validate.field).int32.gt = 0];

  // Healthy threshold
  int32 healthy_threshold = 6 [(buf.validate.field).int32.gte = 0];

  // Unhealthy threshold
  int32 unhealthy_threshold = 7 [(buf.validate.field).int32.gte = 0];
}
```

---

### load_balancer_config.proto {#load_balancer_config}

**Path**: `gcommon/v1/organization/load_balancer_config.proto` **Package**: `gcommon.v1.organization` **Lines**: 30

**Messages** (1): `OrganizationLoadBalancerConfig`

**Imports** (4):

- `gcommon/v1/organization/health_check_config.proto`
- `gcommon/v1/organization/ssl_config.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/load_balancer_config.proto
// version: 1.0.0
// guid: 9e0df8a1-fd1a-4173-89ed-7bcdc82cdb6f

edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/organization/health_check_config.proto";
import "gcommon/v1/organization/ssl_config.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message OrganizationLoadBalancerConfig {
  // Load balancer type (application, network)
  string type = 1 [(buf.validate.field).string.min_len = 1];

  // Load balancing algorithm
  string algorithm = 2 [(buf.validate.field).string.min_len = 1];

  // Health check configuration
  OrganizationHealthCheckConfig health_check = 3;

  // SSL/TLS configuration
  SSLConfig ssl = 4;
}
```

---

### o_auth_app_config.proto {#o_auth_app_config}

**Path**: `gcommon/v1/organization/o_auth_app_config.proto` **Package**: `gcommon.v1.organization` **Lines**: 30

**Messages** (1): `OAuthAppConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/o_auth_app_config.proto
// version: 1.0.0
// guid: 3db5888f-b55c-4810-82a3-0690f6604cf9

edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message OAuthAppConfig {
  // OAuth application name
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // OAuth client ID
  string client_id = 2;

  // OAuth redirect URIs
  repeated string redirect_uris = 3;

  // OAuth scopes
  repeated string scopes = 4;
}
```

---

### origin_config.proto {#origin_config}

**Path**: `gcommon/v1/organization/origin_config.proto` **Package**: `gcommon.v1.organization` **Lines**: 31

**Messages** (1): `OriginConfig`

**Imports** (3):

- `gcommon/v1/common/key_value.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/origin_config.proto
// version: 1.0.0
// guid: b84e3243-3ef5-4beb-94d1-db2bb8831611

edition = "2023";

package gcommon.v1.organization;

import "gcommon/v1/common/key_value.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message OriginConfig {
  // Origin domain name
  string domain_name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Origin path
  string origin_path = 2;

  // Origin protocol policy
  string protocol_policy = 3;

  // Custom headers to send to origin
  repeated gcommon.v1.common.KeyValue custom_headers = 4;
}
```

---

### rate_limit_config.proto {#rate_limit_config}

**Path**: `gcommon/v1/organization/rate_limit_config.proto` **Package**: `gcommon.v1.organization` **Lines**: 25

**Messages** (1): `OrganizationRateLimitConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/rate_limit_config.proto
// version: 1.0.0
// guid: cd85c64c-3fc8-4e12-a37f-b5171af08896

edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message OrganizationRateLimitConfig {
  // Maximum requests per minute
  int32 requests_per_minute = 1 [(buf.validate.field).int32.gte = 0];

  // Maximum requests per hour
  int32 requests_per_hour = 2 [(buf.validate.field).int32.gte = 0];

  // Maximum requests per day
  int32 requests_per_day = 3 [(buf.validate.field).int32.gte = 0];
}
```

---

### ssl_config.proto {#ssl_config}

**Path**: `gcommon/v1/organization/ssl_config.proto` **Package**: `gcommon.v1.organization` **Lines**: 28

**Messages** (1): `SSLConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/ssl_config.proto
// version: 1.0.0
// guid: 9945eeeb-d22e-4d57-a7f8-7e7220e847ce

edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message SSLConfig {
  // SSL certificate ARN or ID
  string certificate_id = 1 [(buf.validate.field).string.min_len = 1];

  // SSL policy
  string ssl_policy = 2 [(buf.validate.field).string.min_len = 1];

  // Whether to redirect HTTP to HTTPS
  bool redirect_http = 3;

  // Minimum TLS version
  string min_tls_version = 4 [(buf.validate.field).string.pattern = "^v?\\d+\\.\\d+\\.\\d+"];
}
```

---

### storage_backup_config.proto {#storage_backup_config}

**Path**: `gcommon/v1/organization/storage_backup_config.proto` **Package**: `gcommon.v1.organization` **Lines**: 31

**Messages** (1): `StorageBackupConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/storage_backup_config.proto
// version: 1.0.0
// guid: 374d573f-8428-4748-8c1a-65ccfb6995ad

edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message StorageBackupConfig {
  // Whether backup is enabled
  bool enabled = 1;

  // Backup schedule (cron expression)
  string schedule = 2 [(buf.validate.field).string.min_len = 1];

  // Backup retention period
  int32 retention_days = 3 [(buf.validate.field).int32.gte = 0];

  // Cross-region backup enabled
  bool cross_region = 4;

  // Backup encryption enabled
  bool encryption_enabled = 5;
}
```

---

### webhook_config.proto {#webhook_config}

**Path**: `gcommon/v1/organization/webhook_config.proto` **Package**: `gcommon.v1.organization` **Lines**: 28

**Messages** (1): `WebhookConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/webhook_config.proto
// version: 1.0.0
// guid: 831d7bab-450b-45fb-b41f-63cde7f89926

edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/organization";

message WebhookConfig {
  // Webhook URL
  string url = 1 [(buf.validate.field).string.uri = true];

  // Events to trigger this webhook
  repeated string events = 2 [(buf.validate.field).repeated.min_items = 1];

  // Whether this webhook is active
  bool active = 3;

  // Webhook secret for signature verification
  string secret = 4 [(buf.validate.field).string.min_len = 1];
}
```

---

