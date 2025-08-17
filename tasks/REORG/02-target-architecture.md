# 2. Target Architecture

## 2.1 New Directory Structure

The target structure follows Buf's recommended practices:

```
gcommon/
├── proto/                           # NEW: All proto files
│   └── gcommon/                     # Organization namespace
│       └── v1/                      # API version
│           ├── common/              # Common types and enums
│           │   ├── enums/
│           │   ├── messages/
│           │   └── services/
│           ├── config/              # Configuration domain
│           │   ├── v1/             # Config API v1
│           │   ├── v2/             # Config API v2 (if needed)
│           │   └── services/
│           ├── database/           # Database domain
│           │   ├── config/
│           │   └── services/
│           ├── media/              # Media domain
│           │   ├── types/
│           │   ├── metadata/
│           │   └── services/
│           ├── metrics/            # Metrics domain
│           │   ├── v1/
│           │   ├── v2/
│           │   └── services/
│           ├── organization/       # Organization domain
│           │   ├── api/
│           │   ├── config/
│           │   └── services/
│           ├── queue/              # Queue domain
│           │   ├── api/
│           │   ├── config/
│           │   └── services/
│           └── web/                # Web domain
│               ├── api/
│               ├── config/
│               ├── events/
│               └── services/
├── pkg/                            # Generated Go code ONLY
│   └── [generated subdirectories]
├── sdks/                           # Generated SDKs
│   ├── python/
│   ├── rust/                       # Future
│   └── typescript/                 # Future
├── buf.yaml                        # Updated configuration
├── buf.gen.yaml                   # Updated generation config
└── proto-docs/                    # Generated documentation
```

## 2.2 Package Naming Convention

**Format:** `gcommon.v1.{domain}.{subdomain}`

Examples:

- `gcommon.v1.common` - Common types
- `gcommon.v1.config.api` - Configuration API
- `gcommon.v1.database.services` - Database services
- `gcommon.v1.media.metadata` - Media metadata types
- `gcommon.v1.organization.api.v1` - Organization API v1

## 2.3 Go Package Generation Strategy

**Managed Mode Configuration:**

- **Default go_package_prefix:** `github.com/jdfalk/gcommon/pkg`
- **Generated structure:** `pkg/{domain}/{subdomain}/`
- **Example outputs:**
  - `pkg/common/` - Common types
  - `pkg/database/services/` - Database services

## 2.4 Detailed Domain Architecture

### 2.4.1 Common Domain Structure

```
proto/gcommon/v1/common/
├── enums/
│   ├── audit_result.proto       # Audit status enumerations
│   ├── error_codes.proto        # System error codes
│   ├── status_types.proto       # Generic status types
│   └── severity_levels.proto    # Logging severity levels
├── messages/
│   ├── base_types.proto         # Fundamental types (ID, timestamp wrappers)
│   ├── pagination.proto         # Pagination request/response types
│   ├── metadata.proto           # Generic metadata structures
│   └── error_details.proto      # Error detail message types
└── services/
    ├── health_check.proto       # Health checking service
    └── version_info.proto       # Version information service
```

**Package Names:**

- `gcommon.v1.common.enums`
- `gcommon.v1.common.messages`
- `gcommon.v1.common.services`

**Generated Go Packages:**

- `pkg/common/enums/`
- `pkg/common/messages/`
- `pkg/common/services/`

### 2.4.2 Config Domain Structure

```
proto/gcommon/v1/config/
├── api/
│   ├── v1/
│   │   ├── config_service.proto     # Configuration management API v1
│   │   ├── config_types.proto       # Core configuration types v1
│   │   └── config_validation.proto  # Validation rules v1
│   └── v2/
│       ├── config_service.proto     # Configuration management API v2
│       ├── config_types.proto       # Enhanced configuration types v2
│       └── config_schemas.proto     # Schema definition support v2
├── types/
│   ├── application_config.proto     # Application-level configuration
│   ├── database_config.proto        # Database configuration types
│   ├── logging_config.proto         # Logging configuration
│   ├── security_config.proto        # Security configuration
│   └── feature_flags.proto          # Feature flag definitions
└── services/
    ├── config_provider.proto        # Configuration provider service
    ├── config_watcher.proto          # Configuration change watcher
    └── config_validator.proto        # Configuration validation service
```

**Package Names:**

- `gcommon.v1.config.api.v1`
- `gcommon.v1.config.api.v2`
- `gcommon.v1.config.types`
- `gcommon.v1.config.services`

### 2.4.3 Database Domain Structure

```
proto/gcommon/v1/database/
├── config/
│   ├── connection.proto             # Database connection configuration
│   ├── pool_settings.proto          # Connection pool settings
│   └── migration_config.proto       # Database migration configuration
├── services/
│   ├── migration_service.proto      # Database migration service
│   ├── backup_service.proto         # Database backup service
│   ├── monitoring_service.proto     # Database monitoring service
│   └── health_service.proto         # Database health checking
└── types/
    ├── query_types.proto            # Query-related types
    ├── transaction_types.proto      # Transaction management types
    └── schema_types.proto           # Schema definition types
```

**Package Names:**

- `gcommon.v1.database.config`
- `gcommon.v1.database.services`
- `gcommon.v1.database.types`

### 2.4.4 Media Domain Structure

```
proto/gcommon/v1/media/
├── types/
│   ├── audio_types.proto            # Audio-specific types and enums
│   ├── video_types.proto            # Video-specific types and enums
│   ├── image_types.proto            # Image-specific types and enums
│   └── media_formats.proto          # Media format definitions
├── metadata/
│   ├── audio_metadata.proto         # Audio metadata structures
│   ├── video_metadata.proto         # Video metadata structures
│   ├── image_metadata.proto         # Image metadata structures
│   └── generic_metadata.proto       # Generic media metadata
└── services/
    ├── media_processor.proto        # Media processing service
    ├── metadata_extractor.proto     # Metadata extraction service
    ├── format_converter.proto       # Format conversion service
    └── thumbnail_generator.proto    # Thumbnail generation service
```

**Package Names:**

- `gcommon.v1.media.types`
- `gcommon.v1.media.metadata`
- `gcommon.v1.media.services`

### 2.4.5 Metrics Domain Structure

```
proto/gcommon/v1/metrics/
├── api/
│   ├── v1/
│   │   ├── metrics_service.proto    # Metrics collection API v1
│   │   ├── metrics_types.proto      # Basic metrics types v1
│   │   └── aggregation.proto        # Simple aggregation methods v1
│   └── v2/
│       ├── metrics_service.proto    # Enhanced metrics API v2
│       ├── metrics_types.proto      # Advanced metrics types v2
│       ├── aggregation.proto        # Complex aggregation methods v2
│       └── streaming.proto          # Streaming metrics support v2
├── types/
│   ├── measurement_types.proto      # Measurement value types
│   ├── time_series.proto            # Time series data structures
│   ├── labels.proto                 # Metric labeling system
│   └── units.proto                  # Measurement units and conversions
└── services/
    ├── collector.proto              # Metrics collection service
    ├── aggregator.proto             # Metrics aggregation service
    ├── storage.proto                # Metrics storage service
    └── query.proto                  # Metrics query service
```

**Package Names:**

- `gcommon.v1.metrics.api.v1`
- `gcommon.v1.metrics.api.v2`
- `gcommon.v1.metrics.types`
- `gcommon.v1.metrics.services`

### 2.4.6 Organization Domain Structure

```
proto/gcommon/v1/organization/
├── api/
│   ├── v1/
│   │   ├── organization_service.proto   # Organization management API v1
│   │   ├── user_service.proto           # User management API v1
│   │   └── role_service.proto           # Role management API v1
│   └── v2/
│       ├── organization_service.proto   # Enhanced organization API v2
│       ├── user_service.proto           # Enhanced user API v2
│       ├── role_service.proto           # Enhanced role API v2
│       └── team_service.proto           # Team management API v2
├── config/
│   ├── organization_config.proto        # Organization configuration
│   ├── user_preferences.proto           # User preference configuration
│   ├── role_definitions.proto           # Role definition configuration
│   └── access_policies.proto            # Access policy configuration
├── types/
│   ├── organization_types.proto         # Organization entity types
│   ├── user_types.proto                 # User entity types
│   ├── role_types.proto                 # Role and permission types
│   ├── team_types.proto                 # Team entity types
│   └── hierarchy_types.proto            # Organizational hierarchy types
└── services/
    ├── membership_service.proto         # Membership management
    ├── permission_service.proto         # Permission checking service
    ├── hierarchy_service.proto          # Organizational hierarchy service
    └── audit_service.proto              # Organization audit service
```

**Package Names:**

- `gcommon.v1.organization.api.v1`
- `gcommon.v1.organization.api.v2`
- `gcommon.v1.organization.config`
- `gcommon.v1.organization.types`
- `gcommon.v1.organization.services`

### 2.4.7 Queue Domain Structure

```
proto/gcommon/v1/queue/
├── api/
│   ├── v1/
│   │   ├── queue_service.proto          # Queue management API v1
│   │   ├── message_service.proto        # Message handling API v1
│   │   └── subscriber_service.proto     # Subscription API v1
│   ├── v2/
│   │   ├── queue_service.proto          # Enhanced queue API v2
│   │   ├── message_service.proto        # Enhanced message API v2
│   │   ├── subscriber_service.proto     # Enhanced subscription API v2
│   │   └── routing_service.proto        # Message routing API v2
│   └── v3/
│       ├── queue_service.proto          # Advanced queue API v3
│       ├── message_service.proto        # Advanced message API v3
│       ├── stream_service.proto         # Streaming API v3
│       └── batch_service.proto          # Batch processing API v3
├── config/
│   ├── queue_config.proto               # Queue configuration
│   ├── routing_config.proto             # Message routing configuration
│   ├── subscriber_config.proto          # Subscriber configuration
│   └── retention_config.proto           # Message retention configuration
├── types/
│   ├── queue_types.proto                # Queue entity types
│   ├── message_types.proto              # Message structure types
│   ├── routing_types.proto              # Message routing types
│   ├── delivery_types.proto             # Delivery guarantee types
│   └── status_types.proto               # Queue status and health types
└── services/
    ├── broker_service.proto             # Message broker service
    ├── routing_service.proto            # Message routing service
    ├── dead_letter_service.proto        # Dead letter handling
    └── monitoring_service.proto         # Queue monitoring service
```

**Package Names:**

- `gcommon.v1.queue.api.v1`
- `gcommon.v1.queue.api.v2`
- `gcommon.v1.queue.api.v3`
- `gcommon.v1.queue.config`
- `gcommon.v1.queue.types`
- `gcommon.v1.queue.services`

### 2.4.8 Web Domain Structure

```
proto/gcommon/v1/web/
├── api/
│   ├── v1/
│   │   ├── rest_api.proto               # REST API definitions v1
│   │   ├── auth_api.proto               # Authentication API v1
│   │   └── session_api.proto            # Session management API v1
│   ├── v2/
│   │   ├── rest_api.proto               # Enhanced REST API v2
│   │   ├── auth_api.proto               # Enhanced authentication v2
│   │   ├── session_api.proto            # Enhanced session management v2
│   │   └── websocket_api.proto          # WebSocket API v2
│   └── v3/
│       ├── graphql_api.proto            # GraphQL API definitions v3
│       ├── rest_api.proto               # Advanced REST API v3
│       ├── realtime_api.proto           # Real-time communication v3
│       └── streaming_api.proto          # Streaming API v3
├── config/
│   ├── v1/
│   │   ├── server_config.proto          # Web server configuration v1
│   │   └── security_config.proto        # Security configuration v1
│   └── v2/
│       ├── server_config.proto          # Enhanced server config v2
│       ├── security_config.proto        # Enhanced security config v2
│       ├── routing_config.proto         # Request routing configuration v2
│       └── middleware_config.proto      # Middleware configuration v2
├── events/
│   ├── user_events.proto                # User interaction events
│   ├── system_events.proto              # System-level events
│   ├── security_events.proto            # Security-related events
│   └── analytics_events.proto           # Analytics tracking events
└── services/
    ├── request_handler.proto            # HTTP request handling service
    ├── session_manager.proto            # Session management service
    ├── auth_provider.proto              # Authentication provider service
    ├── middleware_service.proto         # Middleware processing service
    └── event_dispatcher.proto           # Event dispatching service
```

**Package Names:**

- `gcommon.v1.web.api.v1`
- `gcommon.v1.web.api.v2`
- `gcommon.v1.web.api.v3`
- `gcommon.v1.web.config.v1`
- `gcommon.v1.web.config.v2`
- `gcommon.v1.web.events`
- `gcommon.v1.web.services`

## 2.5 Import Path Strategy

### 2.5.1 New Import Patterns

All imports will use the new proto structure:

```proto
// OLD (current)
import "pkg/common/proto/base_types.proto";
import "pkg/media/proto/audio_track.proto";

// NEW (target)
import "gcommon/v1/common/messages/base_types.proto";
import "gcommon/v1/media/types/audio_types.proto";
```

### 2.5.2 Google APIs Integration

Managed mode will handle googleapis dependencies:

```proto
// Automatic through managed mode
import "google/protobuf/timestamp.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/any.proto";
```

### 2.5.3 Cross-Domain Import Guidelines

- Common domain imports are allowed from any domain
- Database domain can import from common, config
- Media domain can import from common only
- Organization domain can import from common, config, database
- Queue domain can import from common, config, organization
- Web domain can import from any domain (highest level)

## 2.6 Generated Code Architecture

### 2.6.1 Go Package Structure

```
pkg/
├── common/
│   ├── enums/              # Common enumerations
│   ├── messages/           # Common message types
│   └── services/           # Common service interfaces
├── config/
│   ├── api/
│   │   ├── v1/            # Config API v1 Go packages
│   │   └── v2/            # Config API v2 Go packages
│   ├── types/             # Configuration types
│   └── services/          # Configuration services
├── database/
│   ├── config/            # Database configuration Go types
│   ├── services/          # Database service interfaces
│   └── types/             # Database-related types
├── media/
│   ├── types/             # Media type definitions
│   ├── metadata/          # Media metadata types
│   └── services/          # Media service interfaces
├── metrics/
│   ├── api/
│   │   ├── v1/            # Metrics API v1 Go packages
│   │   └── v2/            # Metrics API v2 Go packages
│   ├── types/             # Metrics type definitions
│   └── services/          # Metrics service interfaces
├── organization/
│   ├── api/
│   │   ├── v1/            # Organization API v1 Go packages
│   │   └── v2/            # Organization API v2 Go packages
│   ├── config/            # Organization configuration types
│   ├── types/             # Organization entity types
│   └── services/          # Organization service interfaces
├── queue/
│   ├── api/
│   │   ├── v1/            # Queue API v1 Go packages
│   │   ├── v2/            # Queue API v2 Go packages
│   │   └── v3/            # Queue API v3 Go packages
│   ├── config/            # Queue configuration types
│   ├── types/             # Queue-related types
│   └── services/          # Queue service interfaces
└── web/
    ├── api/
    │   ├── v1/            # Web API v1 Go packages
    │   ├── v2/            # Web API v2 Go packages
    │   └── v3/            # Web API v3 Go packages
    ├── config/
    │   ├── v1/            # Web config v1 Go packages
    │   └── v2/            # Web config v2 Go packages
    ├── events/            # Web event types
    └── services/          # Web service interfaces
```

### 2.6.2 SDK Generation Strategy

Future multi-language SDK support:

```
sdks/
├── python/
│   ├── gcommon/
│   │   └── v1/            # Python package structure mirrors proto
│   ├── setup.py
│   └── requirements.txt
├── rust/                  # Future implementation
│   ├── Cargo.toml
│   └── src/
│       └── lib.rs
└── typescript/            # Future implementation
    ├── package.json
    └── src/
        └── index.ts
```

## 2.7 Buf Configuration Strategy

### 2.7.1 Target buf.yaml Configuration

```yaml
version: v2
modules:
  - path: proto
    name: buf.build/jdfalk/gcommon
deps:
  - buf.build/googleapis/googleapis
lint:
  use:
    - DEFAULT
    - COMMENTS
    - FILE_LAYOUT
  except:
    - ENUM_ZERO_VALUE_SUFFIX
    - SERVICE_SUFFIX
breaking:
  use:
    - FILE
  except:
    - EXTENSION_NO_DELETE
    - FIELD_NO_DELETE
    - MESSAGE_NO_DELETE
```

### 2.7.2 Target buf.gen.yaml Configuration

```yaml
version: v2
managed:
  enabled: true
  disable:
    - file_option: go_package_prefix
      module: buf.build/googleapis/googleapis
  override:
    - file_option: go_package_prefix
      value: github.com/jdfalk/gcommon/pkg
plugins:
  - plugin: buf.build/protocolbuffers/go
    out: .
    opt:
      - paths=source_relative
  - plugin: buf.build/grpc/go
    out: .
    opt:
      - paths=source_relative
      - require_unimplemented_servers=false
  - plugin: buf.build/bufbuild/doc
    out: proto-docs
    opt:
      - html,index.html
```

## 2.8 Migration Validation Architecture

### 2.8.1 Validation Framework

- **Pre-migration**: Comprehensive analysis and validation
- **During migration**: Real-time validation and rollback capability
- **Post-migration**: Full compatibility and performance validation

### 2.8.2 Automated Testing Strategy

- Unit tests for each migrated domain
- Integration tests for cross-domain dependencies
- Performance benchmarks for generation times
- Compatibility tests for existing consumers

### 2.8.3 Rollback Architecture

- Parallel structure maintenance during migration
- Automated rollback scripts for each migration phase
- Checkpoint creation at each successful domain migration
- Full repository state restoration capability

## 2.9 Performance Optimization Strategy

### 2.9.1 Code Generation Optimization

- Parallel generation for independent domains
- Incremental generation for modified files only
- Optimized import resolution through managed mode
- Reduced redundant type generation

### 2.9.2 Build Time Optimization

- Separated proto and Go code directories
- Optimized buf configuration for faster linting
- Parallel linting of independent domain modules
- Cached generation results where possible

### 2.9.3 Runtime Performance Considerations

- Optimized package import paths
- Reduced import dependency chains
- Efficient message serialization through proper field ordering
- Memory usage optimization through managed mode

## 2.10 Security and Access Control

### 2.10.1 Repository Security

- Proto files in dedicated directory with clear access patterns
- Generated code separated from source proto definitions
- Version control optimized for proto file changes
- Clear separation between source and generated artifacts

### 2.10.2 API Security Architecture

- Consistent authentication patterns across all domains
- Authorization model embedded in service definitions
- Security configuration centralized in config domain
- Audit trails defined in organization domain

### 2.10.3 Dependency Security

- Managed googleapis dependencies through buf
- Version pinning for all external dependencies
- Security scanning integration for generated code
- Dependency vulnerability monitoring
