# GCommon Changelog

<!-- file: CHANGELOG.md -->
<!-- version: 1.1.1 -->
<!-- guid: a1b2c3d4-e5f6-7a8b-9c0d-1e2f3a4b5c6d -->

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to
[Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Added examples for config and queue modules (Task 11).

### Added

- Added in-memory metrics provider

### Added\n\n- Add comprehensive example directory skeleton

### Added\n- Skeleton Go examples for modules, integration, and production

### Added

- Add skeleton database migration framework

### Added

- Standardized logging across modules with providers, middleware, aggregation, monitoring, and tracing

- Completed remaining auth module protobuf definitions

### Added

- Added skeleton for integration test environment

### Added

- Expand monitoring and observability with collectors, alerts, exporters, and dashboards

### Added

- Add initial error handling framework

Added docsystem scaffolding

### Added

- Add skeletons for multi-language client SDKs

Added comprehensive containerization and deployment templates with monitoring and automation

### Added\n\n- Expand performance testing framework with runner, benchmarks, load, stress, and regression modules

### Added

- Add performance testing framework skeleton

### Added

- Added automated API documentation generation script

Implemented organization module service layer with gRPC services

### Added

- Introduced CI/CD pipeline skeleton and quality gate workflow

- auth: add OAuth2 and LDAP providers with token blacklist

### Added

- Added performance testing framework

### Added\n\n- Implement comprehensive database migration system with versioning, rollback, and multi-database support

### Added

- Completed cache module implementation and verification

### Added

- Implemented comprehensive monitoring and observability with collectors, exporters, alerts, and dashboards

### Added\n- Implemented advanced gRPC client resilience with token bucket rate limiting, bulkhead concurrency control, and request hedging.

feat: unify gRPC server and service registration across modules

### Added

- Add Dockerfile and Kubernetes deployment templates

### Fixed

- Fixed create-issue-update script requiring GH_TOKEN or git remote

### Added

- Add Code of Conduct for community guidelines

### Added

- Implemented notification gRPC service layer with admin operations

### Added\n- Scaffold dependency optimization, security scanning, version policy, and metrics tools for Task 18

Enhanced dependency audit script with license checks and conflict detection

### Added\n\n- Expanded auth module with JWT provider, token refresh/validation, ABAC policy engine, gRPC services, middleware, and examples

### Added

- Added SDK generation scaffolding

### Added\n- Introduced basic HTTP server, logging middleware, and memory session store for web module

### Added

- Enhanced environment and file configuration sources with file watching

### Added

- Added initial auth service skeleton with local provider and JWT handling

### Added

- Initial queue service layer with memory and redis providers

### Added

- Added initial module documentation skeleton

### Added

- Added memcached cache provider and extended cache service operations

### Added

- Add standardized LogEntry struct for structured logging

### Added

- Add logging wrappers for config, queue, and auth modules for standardized logging

### Added

- Add advanced gRPC client utilities with retries and circuit breaker

### Added

- Added production readiness checklist for gcommon modules

Pin otlptranslator dependency and update collectors to new OTel APIs

### Added

- Add initial performance testing framework skeleton

feat(queue): implement queue service layer with memory and redis providers, scheduler, and monitoring

### Added

- Add comprehensive deployment stack with Docker, Kubernetes, Helm, automation, and monitoring

### Added

- Add basic getting started example

### Added

- Document completion of Task 05 web module implementation

### Added

- Scaffold documentation skeleton for module documentation system

### Added

- Added comprehensive logging module with providers, middleware, aggregation, and monitoring

### Added

- Add configuration management system enhancements with file source auto detection and TOML support

### Added

- Introduce initial microservice template scaffolding

### Added

- Document completion of error handling standardization

### Added

- Implemented comprehensive error handling framework across modules

### Added

- Track automated API documentation generation pipeline (see issue: API Docs: Automated generation)

### Added

- Add JWT auth and basic cache examples

### Added

- Added Python and TypeScript SDK implementations and Rust skeleton.

Add organization service layer with in-memory tenant management

Add comprehensive configuration management system skeleton with loaders, watchers, sources and examples

### Added

- Add buf plugins for generating multi-language SDKs

### Added

- Implemented database migration system with multi-database support and rollback

### Added

- Add notification service layer skeleton

### Added

- Implemented security audit framework with policies, monitoring, and cryptographic tools across modules.

### Added

- Add end-to-end integration test scenarios and workflows

### Changed\n\n- Expanded in-memory metrics provider to handle histograms, summaries, and timers

### Added

- Added monitoring infrastructure scaffolding

### Added

- Introduce security module scaffolding

### Added\n\n- Implemented comprehensive integration testing framework.

### Added

- Add deployment templates and monitoring configuration

### Added\n\n- Added integration testing framework structure with placeholders

### Added

- Add API documentation generation scaffolding

### Added

- Added gRPC client resilience interceptor combining retries and circuit breaking (Refs #882)

- Added gRPC MigrationService server and client

### Added

- Added microservice templates and generator

### Added

- Enhanced CI/CD pipeline with multi-stage testing, quality gates, release automation, environment management, and reporting

Added cache service layer with in-memory provider and gRPC service implementation

### Added\n\n- Expanded Auth module documentation with detailed guides

Added redis and distributed cache providers, eviction policies, serialization, metrics, and examples

### Changed

- Marked plugin architecture task as complete in tasks documentation.


### Added

- Add unified gRPC service registration scaffold

### Added\n- Added config module service skeleton

### Added

- Refine gRPC server registration and lifecycle management

### Added\n- Introduced integration testing framework for module and cross-module validation

Added skeleton metrics exporters

### Added

- Expanded web module with Redis-backed sessions, parametric router, compression middleware, and admin gRPC service

### Added

- Add configuration manager skeleton

### Added

- Implemented comprehensive security module

### Added\n\n- Enhanced integration test environment with mock services and utilities.

### Added\n\n- Complete notification module with providers, templates, delivery tracking, and gRPC services

### Added

- Enhanced CI/CD pipeline with multi-stage testing and quality gates

### Added\n- Expanded web module with server factory, middleware, session manager, handlers, routing, gRPC skeleton, and examples

### Added

- Add security scanning workflow for Go and Node dependencies

### Added\n- Implemented organization service layer with tenant, hierarchy, and team management

### Added

- Added integration test environment scaffolding.

### Changed

- Marked plugin architecture task as complete in tasks documentation.


### Added

- Added extensible plugin architecture with security, communication bus, SDK, and examples
- Add dependency audit script and management policy
- Add Go vulnerability scanning workflow
- Introduce plugin framework skeleton
- Add initial config provider factory with file and env providers
- Expanded module documentation skeletons for all modules

**🚀 MAJOR PROTOBUF IMPLEMENTATION MILESTONE (August 2025)**

**🚀 MASSIVE PROTOBUF EXPANSION**: Completed comprehensive 1-1-1 pattern
implementation across all modules

- **1,279+ Protobuf Files**: Expanded from ~754 to 1,279+ individual proto files
  following 1-1-1 pattern
- **Complete Config Module**: 155 proto files (split from 7 large files into
  individual enum/message files)
- **Complete Queue Module**: 216 proto files (most complex module with
  comprehensive message definitions)
- **Complete Metrics Module**: 172 proto files (full metrics collection and
  provider management)
- **Complete Auth Module**: 172 proto files (comprehensive authentication and
  authorization)
- **Complete Web Module**: 224 proto files (full web server and middleware
  management)
- **Complete Cache Module**: 72 proto files (full caching layer implementation)
- **Expanded Organization Module**: 80 proto files (team and tenant management)
- **Enhanced Notification Module**: 22 proto files (notification delivery
  system)

**🔧 1-1-1 PATTERN AUTOMATION**:

- Created `split_proto.py` for automated proto file splitting
- Implemented `analyze_proto_files.sh` for validation and analysis
- Documented complete splitting process in `PROTO_SPLITTING_GUIDE.md`
- Successfully split 16 large monolithic files into 180+ individual files

**📊 MODULE COMPLETION STATUS**:

- **Config Module**: 100% protobuf structure complete (155/155 files)
- **Queue Module**: 100% protobuf structure complete (216/216 files)
- **Metrics Module**: 100% protobuf structure complete (172/172 files)
- **Auth Module**: 100% protobuf structure complete (172/172 files)
- **Web Module**: 100% protobuf structure complete (224/224 files)
- **Cache Module**: 100% protobuf structure complete (72/72 files)
- **Health Module**: 100% complete and production-ready (35/35 files)
- **Common Module**: 100% complete foundation types (40/40 files)
- **Database Module**: 100% complete and production-ready (52/52 files)
- **Log Module**: 100% complete minimal implementation (14/14 files)

**Previous Achievements**:
- Implemented all Metrics request and response protobufs
- Added DatabaseStatus message and DatabaseStatusCode enum for database module
- Implemented web module message definitions
- Added MediaFile and related types for subtitle-manager support
- Implemented remaining organization protobuf messages
- Implemented metrics request and response protobufs
- Verified completion of all cache protobufs
- Started migrating log protobufs to 1-1-1
- Implemented initial queue configuration messages and enums
- Implemented new auth protobufs: refresh token, security policy, audit event
- Implemented session management protobufs for web module
- Implemented web cache configuration message and admin service
- Verified database module protobufs complete
- Implemented MarkAsRead and Delete notification protobufs
- Implemented Web HealthCheckConfig protobuf
- Implemented additional queue protobufs for listing and pull operations
- Implemented core permission and auth context protobufs
- Added MySQLConfig and MySQLStatus protobuf messages
- Added CockroachDB config protobuf
- Added PebbleConfig protobuf for Pebble driver
- Implemented initial web configuration messages and middleware update request/response

### Changed

- Verified common module protobufs fully implemented

### BREAKING: Protobuf Strategy Migration

**🚨 CRITICAL ARCHITECTURAL CHANGE**: Based on Go best practices research, we
are migrating away from `import public` aggregator files to direct imports of
specific proto files.

**Why This Change Is Necessary**:

- `import public` is a C++-centric feature that creates complexity in Go
- Go protobuf compiler must generate type aliases (e.g., `type Foo = foopb.Foo`)
  for backward compatibility
- This feature is obscure and not well-supported across all protobuf backends
- Direct imports make dependencies explicit and easier to understand
- Follows Go's philosophy of explicit over implicit

**Migration Plan**:

1. **Phase 1**: Deprecate aggregator files (auth.proto, cache.proto, etc.) as
   import-only
2. **Phase 2**: Update all consuming code to import specific proto files
   directly
3. **Phase 3**: Remove aggregator files entirely in v0.3.0
4. **Phase 4**: Update buf.yaml to restore IMPORT_NO_PUBLIC lint rule

**Example Migration**:

```protobuf
// OLD (deprecated):
import "pkg/auth/proto/auth.proto";  // Imports everything via public imports

// NEW (recommended):
import "pkg/auth/proto/messages/user.proto";
import "pkg/auth/proto/requests/login_request.proto";
import "pkg/auth/proto/responses/login_response.proto";
```

**Timeline**:

- v0.2.0: Deprecation warnings
- v0.3.0: Remove aggregator files (BREAKING)

### Added

- Database drivers expose GRPCService() registration - closes #132
- Implemented initial auth provider and password reset protobufs
- Implemented Web module protobufs
- Implemented core web protobuf definitions
- Implemented queue acknowledgment messages and types
- Implemented additional metrics message definitions
- Implemented Config module request protobufs
- Completed Cache module protobufs and updated aggregator
- Implemented initial metrics protobufs
- Added 10 log protobuf files and migrated log.proto to aggregator

- Implemented initial auth configuration and API key messages
- Implemented initial Queue protobufs (QueueMessage, DeliveryOptions,
  SendMessageRequest, SendMessageResponse, MessageState)
- Implemented initial metrics protobuf definitions (alerts, stats)
- Organized GitHub project board with standard columns
- Added improved GitHub project setup script with automatic authentication and
  issue linking
- Add shared pagination and sort proto types
- Removed custom add-to-project workflow in favor of built-in GitHub automation
- Added protobuf validation workflow
- Marked Health and Organization protobuf modules complete
- Implemented Web module enumerations
- **Protobuf Foundation**: Complete mapping for all 9 modules with 29 services
  and 754 protobuf files
- **Common Types Module**: 39 shared message types implemented for consistency
  across modules
- **Database Module**: Complete 1-1-1 migration (51/51 types) serving as gold
  standard
- **Health Module**: Complete 1-1-1 migration (36/36 types) with full protobuf
  implementation
- **Auth Module**: Partial implementation (16/48 types) with core authentication
  services functional
- **Documentation**: Comprehensive technical design documents and implementation
  guides
- **Automated Issue Management**: GitHub Actions workflow for programmatic issue
  updates via JSON files
- **gRPC Metrics Middleware**: Unary and streaming interceptors for metrics
  collection
- **Database gRPC Services**: SQLite and CockroachDB drivers expose
  `GRPCService()`

### Changed

- **Issue Management Process**: Now supports automated issue creation, updates,
  and closure via `issue_updates.json`
- **Development Workflow**: Enhanced with automated issue tracking requiring
  status updates for all work

### Current Implementation Status (June 2025)

#### Completed Modules

- **✅ Database Module**: 100% complete - All 51 types migrated to 1-1-1
  structure
- **✅ Common Module**: 100% complete - 39 shared types implemented
- **✅ Health Module**: 100% complete - All 36 types migrated to 1-1-1 structure
- **✅ Log Module**: 100% complete - Minimal logging implementation

#### In Progress Modules

- **🔄 Auth Module**: 33% complete (16/48 types implemented)
- **🔄 Cache Module**: 15% complete (7/46 types implemented)
- **🔄 Config Module**: 9% complete (2/23 types implemented)
- **🔄 Notification Module**: 10% complete (initial message types defined)

#### Pending Implementation

- **❌ Metrics Module**: 1% complete - 94/95 types require implementation
- **❌ Logging Module**: 0% complete - All 50 types require implementation
- **❌ Queue Module**: 1% complete - 142/143 types require implementation
- **❌ Web Module**: 1% complete - 122/123 types require implementation

### Critical Discovery (June 2025)

**⚠️ Major Implementation Gap Identified**: Analysis revealed **626 empty
protobuf files** (83% of 754 total files) requiring immediate implementation.
This represents a significantly larger scope than initially estimated.

**Immediate Priorities**:

1. Complete protobuf message implementations for all modules
2. Enable gRPC service functionality across the stack
3. Standardize error handling with common types
4. Add request metadata to all service methods

### Developer Workflow (June 2025)

**🤖 Automated Issue Management**: All work now requires proper issue status
tracking using the automated GitHub Actions workflow.

**Required Process for All Development Work**:

1. **Start Task**: Assign issue to yourself, mark "in-progress"
2. **During Work**: Reference issue numbers in commits, update progress
3. **Complete Task**: Close issue with completion summary, mark "completed"

**Issue Updates via JSON**: Create `issue_updates.json` with actions (create,
update, delete) and push to main branch for automatic processing.

**Example Workflow**:

```bash
# Starting work on issue #68
echo '[{"action": "update", "number": 68, "assignees": ["username"], "labels": ["in-progress"]}]' > issue_updates.json
git add . && git commit -m "Start work on issue #68: Metrics Messages" && git push

# Completing work
echo '[{"action": "update", "number": 68, "state": "closed", "labels": ["completed"]}]' > issue_updates.json
git add . && git commit -m "Complete issue #68: Implemented all metrics message types" && git push
```

### Fixed

- **Protobuf Compilation Issues**: Resolved all import path and syntax errors
  across auth and common packages
  - Fixed 8+ protobuf files with import path errors (`gcommon/v1/` → `pkg/`
    relative paths)
  - Corrected invalid `[lazy = true]` field options on primitive types (strings,
    repeated strings)
  - Removed unused imports (`google/protobuf/duration.proto`,
    `google/protobuf/empty.proto`)
  - Standardized import paths across all auth and common package protobuf files
- **Service Definition Cleanup**: Systematically commented out incomplete
  service methods while preserving working functionality
  - AuthService: 2 working methods (`Authenticate`, `ValidateToken`)
  - SessionService: 1 working method (`CreateSession`)
  - AuthorizationService: Temporarily disabled (awaiting missing message types)
- **Protobuf Import Consistency**: All proto files now use consistent relative
  import paths for cross-module dependencies

### Technical Documentation

#### Protobuf Architecture

- **Common Types**: 25+ shared message types for consistency across all modules
- **Service Definitions**: 21 total services distributed across 9 modules
- **Message Catalog**: 400+ message definitions covering all functionality
- **Implementation Phases**: 4-phase rollout strategy for systematic
  implementation

#### Module Architecture Details

##### Health Module (100% Complete)

- **Services**: HealthService with 10 methods
- **Messages**: 25+ request/response pairs
- **Features**: Kubernetes probes, Prometheus metrics, remediation actions
- **Integrations**: Full observability stack integration

##### Authentication Module (45% Complete)

- **Services**: AuthService, AuthorizationService, SessionService (23 methods
  total)
- **Messages**: 60+ message definitions (most complex module)
- **Features**: Multi-factor auth, RBAC, session management, token lifecycle
- **Security**: Built-in rate limiting, audit logging, secure defaults
- **Status**: Protobuf definitions complete, compilation issues resolved, core
  service methods functional (Authenticate, ValidateToken, CreateSession)

##### Database Module (30% Complete)

- **Services**: DatabaseService, TransactionService, SchemaService,
  MigrationService (22 methods)
- **Messages**: 50+ message definitions
- **Backends**: SQLite, PostgreSQL, CockroachDB, Pebble support
- **Features**: ACID transactions, schema migrations, connection pooling

##### Cache Module (20% Complete)

- **Services**: CacheService, CacheManagementService (18 methods)
- **Messages**: 35+ message definitions
- **Backends**: Redis, Memcached, in-memory support planned
- **Features**: TTL management, batch operations, statistics

##### Configuration Module (20% Complete)

- **Services**: ConfigService, ConfigSchemaService (13 methods)
- **Messages**: 30+ message definitions
- **Features**: Hot reload, schema validation, environment management
- **Sources**: File, environment, remote configuration support

##### Logging Module (50% Complete)

- **Services**: LogService, LogManagementService (13 methods)
- **Messages**: 30+ message definitions
- **Backends**: Standard library, Zap, Logrus support
- **Features**: Structured logging, log aggregation, filtering

##### Metrics Module (70% Complete)

- **Services**: MetricsService, MetricsManagementService (13 methods)
- **Messages**: 35+ message definitions
- **Backends**: Prometheus, OpenTelemetry support
- **Features**: Custom metrics, aggregation, alerting integration

##### Queue Module (10% Complete)

- **Services**: QueueService, QueueManagementService (18 methods)
- **Messages**: 30+ message definitions
- **Backends**: RabbitMQ, NATS, AWS SQS support planned
- **Features**: Batch processing, dead letter queues, retry logic

##### Web Module (10% Complete)

- **Services**: WebService, MiddlewareService, WebSocketService (19 methods)
- **Messages**: 40+ message definitions
- **Features**: Middleware chain, WebSocket support, security headers
- **Integrations**: Authentication, metrics, logging built-in

### Implementation Strategy

#### Phase 1: Foundation (Weeks 1-4)

1. **Common Types Enhancement**: Add remaining 6 message types to common.proto
2. **Protobuf Standardization**: Update all existing proto files to use common
   types
3. **Health Module Optimization**: Performance improvements and additional
   checks
4. **Metrics Module Completion**: Finish OpenTelemetry integration

#### Phase 2: Core Services (Weeks 5-12)

1. **Database Module**: Complete all 4 services with full backend support
2. **Cache Module**: Implement all backends and management features
3. **Configuration Module**: Hot reload and schema validation
4. **Logging Module**: Complete gRPC services and aggregation

#### Phase 3: Advanced Services (Weeks 13-20)

1. **Authentication Module**: Complete RBAC and session management
2. **Queue Module**: Implement all backends and batch processing
3. **Web Module**: Complete middleware system and WebSocket support

#### Phase 4: Production Readiness (Weeks 21-24)

1. **Performance Optimization**: Benchmarking and optimization across all
   modules
2. **Integration Testing**: End-to-end testing with real-world scenarios
3. **Documentation**: Complete API documentation and examples
4. **Security Audit**: Security review and penetration testing

### Breaking Changes

- **v0.2.0**: Protobuf message structure changes (planned)
- **v0.3.0**: Authentication API changes (planned)

### Migration Guides

- Will be added as breaking changes are introduced

## [0.1.0] - 2024-12-15

### Added

- Initial project structure
- Health module with basic functionality
- Metrics module foundation
- Logging module interfaces
- Basic examples and documentation

### Technical Foundation

- go 1.23+ requirement
- Protocol Buffers for service definitions
- gRPC for network services
- OpenTelemetry for observability
- MIT License

---

## Development Notes

### Code Quality Standards

- 90%+ test coverage for all modules
- Comprehensive documentation for all public APIs
- Consistent error handling patterns
- Performance benchmarks for critical paths

### Observability Integration

- All modules integrate with metrics collection
- Structured logging with correlation IDs
- Distributed tracing support
- Health checks for all services

### Production Considerations

- Graceful shutdown handling
- Configuration validation
- Rate limiting and circuit breakers
- Security best practices
- Kubernetes deployment examples

---

_This changelog consolidates technical documentation that would otherwise be
scattered across multiple files, following the GCommon documentation
organization policy._

## Changelog

- **Feature**: Added DebugInfo message for enhanced debugging metadata
- **Feature**: Added TransactionService and MigrationService with new
  request/response messages
