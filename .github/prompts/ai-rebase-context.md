<!-- file: .github/prompts/ai-rebase-context.md -->
<!-- version: 1.0.0 -->
<!-- guid: 8f9e0d1c-6b5a-4c3d-2e1f-7a6b5c4d3e2f -->

# Repository Context for AI Rebase

## Project Overview

This is the **GCommon** repository, a comprehensive Go library collection and Protocol Buffer definitions for distributed systems. The project focuses on:

- Common Go utilities and libraries for microservices
- Extensive Protocol Buffer definitions for gRPC services
- Modular architecture with separate packages for different concerns
- Integration libraries for databases, messaging, and web services
- Performance-optimized data structures and algorithms

## Coding Standards

- Follow Go conventions: exported functions use PascalCase, unexported use camelCase
- Use standard file header format with path, version, and GUID
- Protocol Buffer files follow Google's style guide
- All Go packages include comprehensive package documentation
- Use conventional commit message format: `type(scope): description`
- gRPC services follow consistent naming and error handling patterns
- Include extensive unit tests with table-driven test patterns

## Key Files to Reference

### README.md

Project overview explaining the modular architecture and package organization for the common Go libraries.

### .github/instructions/general-coding.instructions.md

Standard coding guidelines including file headers, version management, and documentation requirements.

### go.mod

Go module definition showing dependencies on gRPC, protobuf, database drivers, and other core libraries.

### buf.yaml and buf.gen.yaml

Protocol Buffer configuration files defining linting rules, breaking change detection, and code generation settings.

## Common Conflict Patterns

### Protocol Buffer Conflicts

When resolving `.proto` file conflicts:

- Preserve both message field additions (ensure no field number conflicts)
- Combine service method additions from both branches
- Merge enum value additions while maintaining consistent numbering
- Keep both package imports when they serve different purposes
- Preserve breaking change annotations and deprecation comments

### Go Library Conflicts

For Go package conflicts:

- Combine interface method additions from both branches
- Merge struct field additions while maintaining backward compatibility
- Preserve both constructor function variations when they serve different use cases
- Keep both test cases when they test different scenarios
- Combine error handling improvements and validation logic

### Module Organization Conflicts

For package structure conflicts:

- Preserve both new package additions when they serve different domains
- Merge go.mod dependency additions from both branches
- Combine Makefile target additions for different build scenarios
- Keep both documentation additions in different areas

## Dependencies and Imports

- **Core gRPC**: `google.golang.org/grpc`, `google.golang.org/protobuf`
- **Database libraries**: PostgreSQL, Redis, and other data store clients
- **Monitoring**: Prometheus metrics, structured logging libraries
- **Networking**: HTTP/2, WebSocket, and connection pooling utilities
- **Serialization**: Protocol Buffers, JSON, and binary encoding
- **Testing**: Testify, mock generation, and integration test helpers
- **Build tools**: Buf for protobuf management, golangci-lint for code quality

## Project Structure

- `pkg/` - Core Go library packages organized by domain
- `proto/` - Protocol Buffer definitions organized by service area
- `cmd/examples/` - Example applications demonstrating library usage
- `internal/` - Internal packages not exposed to external consumers
- `docs/` - Documentation including architecture decisions and API guides
- `scripts/` - Build and development automation scripts
- `config/` - Configuration templates and examples

## Protocol Buffer Organization

### Module Structure

The protobuf definitions are organized into logical modules:

- **Auth Module**: 109 files for authentication and authorization
- **Cache Module**: 36 files for caching and data storage
- **Config Module**: 20 files for configuration management
- **Metrics Module**: 95 files for monitoring and observability
- **Queue Module**: 175 files for message queuing and async processing
- **Web Module**: 176 files for web services and HTTP handling

### Implementation Status

Currently **626 protobuf files are empty** and need implementation. When resolving conflicts:

- Preserve both message definition attempts when they don't conflict
- Combine field definitions from different branches intelligently
- Maintain consistent service patterns across modules
- Keep both documentation improvements for better API understanding

### Code Generation

The project uses `buf` for:

- **Linting**: Ensuring consistent protobuf style
- **Breaking Change Detection**: Preventing API compatibility issues
- **Code Generation**: Creating Go bindings for all protobuf definitions
- **Documentation**: Generating API documentation from protobuf comments

When resolving conflicts in generated code, prefer regenerating from the merged `.proto` files rather than manually merging generated Go code.
