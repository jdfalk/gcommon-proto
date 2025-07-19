# Protobuf Implementation Strategy & Guidelines

## Table of Contents

1. [Overview](#overview)
2. [Repository Structure](#repository-structure)
3. [1-1-1 Design Pattern](#1-1-1-design-pattern)
4. [Types Package Strategy](#types-package-strategy)
5. [Implementation Guidelines](#implementation-guidelines)
6. [Subtitle Manager Strategy](#subtitle-manager-strategy)
7. [GCommon Strategy](#gcommon-strategy)
8. [Troubleshooting Guide](#troubleshooting-guide)
9. [Junior Developer Checklist](#junior-developer-checklist)

## Overview

We are implementing a modern, scalable protobuf architecture across two main repositories:

- **gcommon**: Shared protobuf definitions for distributed systems
- **subtitle-manager**: Subtitle processing service with specific protobuf needs

### Key Principles

1. **1-1-1 Pattern**: One message per file, one enum per file, one service per file
2. **Types First**: Define basic types in `types/` packages, import everywhere else
3. **Backwards Compatibility**: Maintain compatibility during migration
4. **Edition 2023**: Use modern protobuf editions for all new files

## Repository Structure

### GCommon Structure

```
pkg/
├── auth/proto/
│   ├── services/          # 1-1-1 service definitions
│   ├── messages/          # 1-1-1 message definitions
│   ├── enums/             # 1-1-1 enum definitions
│   ├── types/             # Basic types for import
│   ├── requests/          # Request message definitions
│   └── responses/         # Response message definitions
├── config/proto/
│   ├── services/
│   ├── messages/
│   ├── enums/
│   └── types/
├── database/proto/
├── metrics/proto/
├── storage/proto/
└── common/proto/          # Shared common types
```

### Subtitle Manager Structure

```
proto/
├── subtitle/
│   ├── services/          # Subtitle processing services
│   ├── messages/          # Subtitle data structures
│   ├── enums/             # Subtitle-related enums
│   └── types/             # Basic subtitle types
├── conversion/
├── validation/
└── common/                # Service-specific common types
```

## 1-1-1 Design Pattern

### What is 1-1-1?

Each protobuf file contains exactly ONE of:

- One message definition
- One enum definition
- One service definition

### Benefits

- **Modularity**: Easy to find and modify specific types
- **Dependency Management**: Clear import relationships
- **Code Generation**: Cleaner generated code
- **Team Collaboration**: Reduces merge conflicts

### Example Structure

```
# GOOD - 1-1-1 Pattern
pkg/auth/proto/messages/user_info.proto         # Contains: UserInfo message
pkg/auth/proto/enums/user_status.proto          # Contains: UserStatus enum
pkg/auth/proto/services/auth_service.proto      # Contains: AuthService service

# BAD - Monolithic
pkg/auth/proto/auth.proto                       # Contains: Multiple messages, enums, services
```

## Types Package Strategy

### Purpose

The `types/` directory contains fundamental, reusable types that are imported by other protobuf files.

### Types Directory Structure

```
pkg/module/proto/types/
├── basic_types.proto       # Fundamental data types
├── common_enums.proto      # Shared enumerations
├── error_types.proto       # Error definitions
├── timestamp_types.proto   # Time-related types
└── metadata_types.proto    # Metadata structures
```

### Types Implementation Pattern

#### 1. Define Basic Types First

```protobuf
// pkg/auth/proto/types/user_status.proto
edition = "2023";
package gcommon.v1.auth;

enum UserStatus {
  USER_STATUS_UNSPECIFIED = 0;
  USER_STATUS_ACTIVE = 1;
  USER_STATUS_INACTIVE = 2;
  USER_STATUS_SUSPENDED = 3;
}
```

#### 2. Import Types in Messages

```protobuf
// pkg/auth/proto/messages/user_info.proto
edition = "2023";
package gcommon.v1.auth;

import "pkg/auth/proto/types/user_status.proto";

message UserInfo {
  string user_id = 1;
  UserStatus status = 2;  // Imported type
}
```

#### 3. Avoid Duplication

- **NEVER** redefine types that exist in `types/`
- **ALWAYS** import from the canonical `types/` location
- **CHECK** existing types before creating new ones

## Implementation Guidelines

### File Naming Conventions

- **Services**: `{service_name}_service.proto`
- **Messages**: `{message_name}.proto` (snake_case)
- **Enums**: `{enum_name}.proto` (snake_case)
- **Types**: `{type_category}_types.proto`

### Required File Headers

Every protobuf file MUST include:

```protobuf
// file: pkg/module/proto/category/filename.proto
// version: 1.0.0
// guid: {unique-guid}

edition = "2023";

package gcommon.v1.module;

option go_package = "github.com/jdfalk/gcommon/pkg/module/proto;modulepb";
```

### Import Guidelines

1. **Standard imports first**:

   ```protobuf
   import "google/protobuf/timestamp.proto";
   import "google/protobuf/duration.proto";
   ```

2. **Types imports second**:

   ```protobuf
   import "pkg/common/proto/types/error_types.proto";
   import "pkg/auth/proto/types/user_status.proto";
   ```

3. **Other module imports third**:
   ```protobuf
   import "pkg/auth/proto/messages/user_info.proto";
   ```

### Message Design Patterns

#### Standard Message Structure

```protobuf
message ExampleMessage {
  // Required fields first (1-10)
  string id = 1;
  string name = 2;

  // Optional fields (11-50)
  string description = 11;
  map<string, string> metadata = 12;

  // Timestamps (51-60)
  google.protobuf.Timestamp created_at = 51;
  google.protobuf.Timestamp updated_at = 52;

  // Status/error fields (61-70)
  MessageStatus status = 61;
  Error error = 62;
}
```

#### Request/Response Pattern

```protobuf
// Request
message CreateUserRequest {
  UserInfo user_info = 1;
  CreateOptions options = 2;
}

// Response
message CreateUserResponse {
  UserInfo user = 1;
  ResponseStatus status = 2;
  Error error = 3;
}
```

## Subtitle Manager Strategy

### Current Status

- **Migration Phase**: Converting from monolithic to 1-1-1 pattern
- **Key Services**: SubtitleService, ConversionService, ValidationService
- **Formats Supported**: SRT, VTT, ASS, SSA, etc.

### Implementation Plan

1. **Phase 1**: Create types package

   ```
   proto/subtitle/types/
   ├── subtitle_format.proto
   ├── timestamp_types.proto
   ├── style_types.proto
   └── validation_types.proto
   ```

2. **Phase 2**: Migrate services to 1-1-1
3. **Phase 3**: Implement message definitions
4. **Phase 4**: Add enum definitions

### Subtitle-Specific Guidelines

- **Timestamps**: Use precise timing for subtitle sync
- **Encoding**: Support UTF-8 and legacy encodings
- **Styling**: Maintain format-specific styling options
- **Validation**: Implement comprehensive validation rules

## GCommon Strategy

### Current Status

- **1005 protobuf files** currently in repository
- **Mixed patterns**: Some 1-1-1, some monolithic
- **Build Issues**: Type duplication and missing imports

### Migration Strategy

#### Priority Order

1. **Fix Type Duplications**: Remove duplicate type definitions
2. **Create Missing Types**: Implement missing basic types
3. **Complete 1-1-1 Migration**: Convert remaining monolithic files
4. **Validate Imports**: Ensure all imports are correct

#### Module Priority

1. **auth** - User authentication (HIGH)
2. **config** - Configuration management (HIGH)
3. **database** - Database operations (MEDIUM)
4. **metrics** - Monitoring and metrics (MEDIUM)
5. **storage** - File storage (LOW)

### Critical Issues to Fix

#### Type Duplication Pattern

**Problem**: Same type defined in multiple files

```
pkg/metrics/proto/types/recording_stats.proto:14:9     # Definition 1
pkg/metrics/proto/responses/record_histogram_response.proto:88:9  # Duplicate!
```

**Solution**:

1. Keep definition in `types/`
2. Import in other files
3. Remove duplicate definitions

## Troubleshooting Guide

### Common Build Errors

#### 1. "symbol already defined"

```
symbol "gcommon.v1.metrics.RecordingStats" already defined
```

**Fix**: Remove duplicate definition, import from types/

#### 2. "file does not exist"

```
import "pkg/metrics/proto/enums/retention_policy.proto": file does not exist
```

**Fix**: Create the missing file with proper 1-1-1 structure

#### 3. "unknown type"

```
field gcommon.v1.metrics.MetricDefinition.retention: unknown type RetentionPolicy
```

**Fix**: Import the type or create it in types/

### Debugging Commands

```bash
# Check for missing files
buf lint 2>&1 | grep "file does not exist"

# Check for type conflicts
buf lint 2>&1 | grep "already defined"

# Validate specific module
buf lint --path pkg/auth/proto/

# Generate code
buf generate
```

## Junior Developer Checklist

### Before Starting

- [ ] Read this entire document
- [ ] Understand 1-1-1 pattern
- [ ] Set up buf CLI tool
- [ ] Understand protobuf editions

### For Each Missing File

- [ ] Determine if it should be in `types/` or specific category
- [ ] Check if similar type already exists
- [ ] Follow file naming conventions
- [ ] Add required file header
- [ ] Use edition = "2023"
- [ ] Set correct package name
- [ ] Add appropriate imports
- [ ] Test with `buf lint`

### Quality Checks

- [ ] No duplicate type definitions
- [ ] All imports resolve correctly
- [ ] Follows 1-1-1 pattern
- [ ] Has proper documentation
- [ ] Builds with `buf generate`

### Communication

- [ ] Create PR for each logical group of files
- [ ] Document any design decisions
- [ ] Test generated code compiles
- [ ] Ask questions early and often

## Validation Commands

### Local Testing

```bash
# Lint specific file
buf lint path/to/file.proto

# Lint entire module
buf lint --path pkg/module/proto/

# Generate code
buf generate

# Check for type conflicts
buf lint 2>&1 | grep "already defined" | sort | uniq
```

### Integration Testing

```bash
# Test Go code generation
go build ./...

# Test imports
go mod tidy

# Validate no circular dependencies
go mod graph | grep cycle
```

This documentation should be referenced for all protobuf work and updated as patterns evolve.
