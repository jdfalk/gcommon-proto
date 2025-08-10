# organization_config Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 7
- **Messages**: 21
- **Services**: 0
- **Enums**: 0

## Files in this Module

- [configure_tenant_isolation_request.proto](#configure_tenant_isolation_request)
- [configure_tenant_isolation_response.proto](#configure_tenant_isolation_response)
- [get_organization_settings_request.proto](#get_organization_settings_request)
- [get_organization_settings_response.proto](#get_organization_settings_response)
- [organization_settings.proto](#organization_settings)
- [update_organization_settings_request.proto](#update_organization_settings_request)
- [update_organization_settings_response.proto](#update_organization_settings_response)

## Module Dependencies

**This module depends on**:

- [common](./common.md)
- [organization](./organization.md)

**Modules that depend on this one**:

- [organization_api_1](./organization_api_1.md)
- [organization_services](./organization_services.md)

---

## Detailed Documentation

### configure_tenant_isolation_request.proto {#configure_tenant_isolation_request}

**Path**: `pkg/organization/proto/configure_tenant_isolation_request.proto`
**Package**: `gcommon.v1.organization` **Lines**: 24

**Messages** (1): `ConfigureTenantIsolationRequest`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)
- `pkg/organization/proto/tenant_isolation.proto` →
  [organization](./organization.md#tenant_isolation)

#### Source Code

```protobuf
// file: pkg/organization/proto/requests/configure_tenant_isolation_request.proto

edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";
import "pkg/organization/proto/tenant_isolation.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

message ConfigureTenantIsolationRequest {
  // Request metadata for tracing and context
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Tenant identifier
  string tenant_id = 2;

  // Isolation configuration to apply
  gcommon.v1.organization.TenantIsolation isolation = 3;
}

```

---

### configure_tenant_isolation_response.proto {#configure_tenant_isolation_response}

**Path**: `pkg/organization/proto/configure_tenant_isolation_response.proto`
**Package**: `gcommon.v1.organization` **Lines**: 23

**Messages** (1): `ConfigureTenantIsolationResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/organization/proto/tenant_isolation.proto` →
  [organization](./organization.md#tenant_isolation)

#### Source Code

```protobuf
// file: pkg/organization/proto/responses/configure_tenant_isolation_response.proto
edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";
import "pkg/organization/proto/tenant_isolation.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

message ConfigureTenantIsolationResponse {
  // Any errors encountered
  repeated gcommon.v1.common.Error errors = 1;

  // Success status
  bool success = 2;

  // Applied isolation configuration
  gcommon.v1.organization.TenantIsolation isolation = 3 [lazy = true];
}

```

---

### get_organization_settings_request.proto {#get_organization_settings_request}

**Path**: `pkg/organization/proto/get_organization_settings_request.proto`
**Package**: `gcommon.v1.organization` **Lines**: 20

**Messages** (1): `GetOrganizationSettingsRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/organization/proto/requests/get_organization_settings_request.proto

edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

message GetOrganizationSettingsRequest {
  // Request metadata for tracing and context
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Organization identifier
  string organization_id = 2;
}

```

---

### get_organization_settings_response.proto {#get_organization_settings_response}

**Path**: `pkg/organization/proto/get_organization_settings_response.proto`
**Package**: `gcommon.v1.organization` **Lines**: 23

**Messages** (1): `GetOrganizationSettingsResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/organization/proto/organization_settings.proto`

#### Source Code

```protobuf
// file: pkg/organization/proto/responses/get_organization_settings_response.proto
edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";
import "pkg/organization/proto/organization_settings.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

message GetOrganizationSettingsResponse {
  // Any errors encountered
  repeated gcommon.v1.common.Error errors = 1;

  // Success status
  bool success = 2;

  // Retrieved settings data
  gcommon.v1.organization.OrganizationSettings settings = 3 [lazy = true];
}

```

---

### organization_settings.proto {#organization_settings}

**Path**: `pkg/organization/proto/organization_settings.proto` **Package**:
`gcommon.v1.organization` **Lines**: 323

**Messages** (15): `OrganizationSettings`, `SecuritySettings`, `UISettings`,
`IntegrationSettings`, `Integration`, `NotificationSettings`, `RateLimitConfig`,
`WebhookConfig`, `APIKeyConfig`, `OAuthAppConfig`, `BillingSettings`,
`ComplianceSettings`, `FeatureFlag`, `EmailTemplate`, `NotificationFrequency`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/key_value.proto` → [common](./common.md#key_value)

#### Source Code

```protobuf
// file: pkg/organization/proto/messages/organization_settings.proto
edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/common/proto/key_value.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

/**
 * OrganizationSettings message containing configuration and preferences
 * for an organization. Includes security policies, UI preferences,
 * integration settings, and operational parameters.
 */
message OrganizationSettings {
  // Organization identifier
  string organization_id = 1;

  // Security and authentication settings
  SecuritySettings security = 2;

  // User interface and experience settings
  UISettings ui = 3;

  // Integration and API settings
  IntegrationSettings integrations = 4;

  // Notification and communication settings
  NotificationSettings notifications = 5;

  // Billing and subscription settings
  BillingSettings billing = 6;

  // Data retention and compliance settings
  ComplianceSettings compliance = 7;

  // Feature flags and experimental features
  repeated FeatureFlag feature_flags = 8;

  // Custom organization-specific settings
  repeated gcommon.v1.common.KeyValue custom_settings = 9 [lazy = true];

  // Settings last update timestamp
  google.protobuf.Timestamp updated_at = 10 [lazy = true];

  // User ID who last updated these settings
  string updated_by = 11;
}

/**
 * SecuritySettings message defining security policies and authentication requirements.
 */
message SecuritySettings {
  // Whether multi-factor authentication is required for all users
  bool require_mfa = 1;

  // Minimum password length requirement
  int32 min_password_length = 2;

  // Whether password complexity rules are enforced
  bool require_password_complexity = 3;

  // Password expiration period in days (0 = no expiration)
  int32 password_expiry_days = 4;

  // Session timeout in minutes
  int32 session_timeout_minutes = 5;

  // Whether single sign-on (SSO) is enabled
  bool sso_enabled = 6;

  // Allowed SSO providers
  repeated string sso_providers = 7;

  // IP address whitelist for organization access
  repeated string ip_whitelist = 8;

  // Whether API access is enabled
  bool api_access_enabled = 9;

  // API rate limiting configuration
  RateLimitConfig api_rate_limit = 10;

  // Audit log retention period in days
  int32 audit_log_retention_days = 11;
}

/**
 * UISettings message containing user interface preferences and branding.
 */
message UISettings {
  // Organization's primary brand color (hex code)
  string primary_color = 1;

  // Organization's secondary brand color (hex code)
  string secondary_color = 2;

  // Organization's logo URL
  string logo_url = 3;

  // Organization's favicon URL
  string favicon_url = 4;

  // Custom CSS for organization branding
  string custom_css = 5;

  // Default language/locale for organization
  string default_locale = 6;

  // Default timezone for organization
  string default_timezone = 7;

  // Date format preference (e.g., "MM/DD/YYYY", "DD/MM/YYYY")
  string date_format = 8;

  // Time format preference (12-hour or 24-hour)
  string time_format = 9;

  // Whether dark mode is enabled by default
  bool dark_mode_default = 10;
}

/**
 * IntegrationSettings message containing third-party integration configurations.
 */
message IntegrationSettings {
  // Enabled third-party integrations
  repeated Integration enabled_integrations = 1;

  // Webhook configuration for external notifications
  repeated WebhookConfig webhooks = 2;

  // API keys for external services
  repeated APIKeyConfig api_keys = 3 [lazy = true];

  // OAuth applications registered for this organization
  repeated OAuthAppConfig oauth_apps = 4;
}

/**
 * Integration message representing a third-party service integration.
 */
message Integration {
  // Integration name (e.g., "slack", "github", "jira")
  string name = 1;

  // Whether this integration is currently enabled
  bool enabled = 2;

  // Integration-specific configuration
  repeated gcommon.v1.common.KeyValue config = 3 [lazy = true];

  // Integration creation timestamp
  google.protobuf.Timestamp created_at = 4 [lazy = true];

  // User ID who configured this integration
  string configured_by = 5;
}

/**
 * NotificationSettings message defining how the organization handles notifications.
 */
message NotificationSettings {
  // Default email sender address for organization notifications
  string sender_email = 1;

  // Default email sender name
  string sender_name = 2;

  // Whether email notifications are enabled
  bool email_enabled = 3;

  // Whether SMS notifications are enabled
  bool sms_enabled = 4;

  // Whether in-app notifications are enabled
  bool in_app_enabled = 5;

  // Email template customizations
  repeated EmailTemplate email_templates = 6;

  // Notification frequency settings
  NotificationFrequency frequency = 7;
}

/**
 * Additional supporting message types for settings configuration.
 */
message RateLimitConfig {
  // Maximum requests per minute
  int32 requests_per_minute = 1;

  // Maximum requests per hour
  int32 requests_per_hour = 2;

  // Maximum requests per day
  int32 requests_per_day = 3;
}

message WebhookConfig {
  // Webhook URL
  string url = 1;

  // Events to trigger this webhook
  repeated string events = 2;

  // Whether this webhook is active
  bool active = 3;

  // Webhook secret for signature verification
  string secret = 4;
}

message APIKeyConfig {
  // API key name/identifier
  string name = 1;

  // Masked API key (for display purposes)
  string masked_key = 2;

  // API key permissions/scopes
  repeated string scopes = 3;

  // API key expiration date
  google.protobuf.Timestamp expires_at = 4 [lazy = true];
}

message OAuthAppConfig {
  // OAuth application name
  string name = 1;

  // OAuth client ID
  string client_id = 2;

  // OAuth redirect URIs
  repeated string redirect_uris = 3;

  // OAuth scopes
  repeated string scopes = 4;
}

message BillingSettings {
  // Billing contact email
  string billing_email = 1;

  // Billing address
  string billing_address = 2;

  // Tax ID for billing
  string tax_id = 3;

  // Preferred currency for billing
  string currency = 4;

  // Billing cycle (monthly, annual, etc.)
  string billing_cycle = 5;
}

message ComplianceSettings {
  // GDPR compliance enabled
  bool gdpr_enabled = 1;

  // Data retention period in days
  int32 data_retention_days = 2;

  // Whether data export is allowed
  bool data_export_enabled = 3;

  // Whether data deletion is allowed
  bool data_deletion_enabled = 4;

  // Compliance certifications
  repeated string certifications = 5;
}

message FeatureFlag {
  // Feature flag name
  string name = 1;

  // Whether the feature is enabled
  bool enabled = 2;

  // Feature flag description
  string description = 3;

  // Rollout percentage (0-100)
  int32 rollout_percentage = 4;
}

message EmailTemplate {
  // Template name/type (e.g., "welcome", "password_reset")
  string name = 1;

  // Email subject template
  string subject = 2;

  // Email body template (HTML)
  string body_html = 3;

  // Email body template (plain text)
  string body_text = 4;
}

message NotificationFrequency {
  // Daily digest enabled
  bool daily_digest = 1;

  // Weekly summary enabled
  bool weekly_summary = 2;

  // Instant notifications enabled
  bool instant_notifications = 3;

  // Quiet hours start time (24-hour format, e.g., "22:00")
  string quiet_hours_start = 4;

  // Quiet hours end time (24-hour format, e.g., "08:00")
  string quiet_hours_end = 5;
}

```

---

### update_organization_settings_request.proto {#update_organization_settings_request}

**Path**: `pkg/organization/proto/update_organization_settings_request.proto`
**Package**: `gcommon.v1.organization` **Lines**: 31

**Messages** (1): `UpdateOrganizationSettingsRequest`

**Imports** (4):

- `google/protobuf/field_mask.proto`
- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)
- `pkg/organization/proto/organization_settings.proto`

#### Source Code

```protobuf
// file: pkg/organization/proto/requests/update_organization_settings_request.proto

edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/field_mask.proto";
import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";
import "pkg/organization/proto/organization_settings.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

message UpdateOrganizationSettingsRequest {
  // Request metadata for tracing and context
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Organization identifier
  string organization_id = 2;

  // Updated settings
  gcommon.v1.organization.OrganizationSettings settings = 3;

  // Fields to update
  google.protobuf.FieldMask update_mask = 4;

  // Validate only without persisting if true
  bool validate_only = 5;
}

```

---

### update_organization_settings_response.proto {#update_organization_settings_response}

**Path**: `pkg/organization/proto/update_organization_settings_response.proto`
**Package**: `gcommon.v1.organization` **Lines**: 23

**Messages** (1): `UpdateOrganizationSettingsResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/organization/proto/organization_settings.proto`

#### Source Code

```protobuf
// file: pkg/organization/proto/responses/update_organization_settings_response.proto
edition = "2023";

package gcommon.v1.organization;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";
import "pkg/organization/proto/organization_settings.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/organization/proto";

message UpdateOrganizationSettingsResponse {
  // Any errors encountered
  repeated gcommon.v1.common.Error errors = 1;

  // Success status
  bool success = 2;

  // Updated settings data
  gcommon.v1.organization.OrganizationSettings settings = 3 [lazy = true];
}

```

---
