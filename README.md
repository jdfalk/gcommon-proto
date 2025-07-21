<!-- file: README.md -->
<!-- version: 1.0.1 -->
<!-- guid: a1b2c3d4-e5f6-7890-abcd-ef0123456789 -->

# GCommon - Common Go Modules

[![Go Version](https://img.shields.io/badge/go-1.21+-blue.svg)](https://golang.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)](https://github.com/jdfalk/gcommon)

> **🚨 MAJOR BREAKING CHANGES COMING**: Version 0.2.0 will introduce significant protobuf message structure changes. See [CHANGELOG.md](CHANGELOG.md) for migration details.

## 📚 Essential Documentation

### New Users Start Here

- **[Getting Started Guide](docs/user/getting-started.md)** - Complete setup and first steps
- **[Health Module Guide](docs/user/health-kubernetes.md)** - Production-ready health monitoring
- **[Basic Examples](examples/)** - Working code examples for each module

### For Developers

- **[Project Roadmap](TODO.md)** - Implementation status and plans
- **[Issue Management Workflow](ISSUE_MANAGEMENT.md)** - Required process for all development work
- **[Technical Architecture](CHANGELOG.md)** - Detailed technical documentation
- **[Protobuf API Design](docs/technical/protobuf-grpc-design.md)** - gRPC service definitions

## � Overview

GCommon is a comprehensive library of common Go modules designed for building robust, scalable applications. It provides consistent APIs across authentication, caching, configuration, database operations, health checking, logging, metrics, message queuing, and web services.

## 🚀 Quick Start

### Installation

```bash
go get github.com/jdfalk/gcommon
```

### Basic Health Check Example

```go
package main

import (
    "context"
    "log"

    "github.com/jdfalk/gcommon/pkg/health"
)

func main() {
    // Create a health provider
    provider := health.NewProvider()

    // Register a simple check
    provider.RegisterCheck("database", func(ctx context.Context) health.Result {
        // Your database health check logic here
        return health.Result{
            Status:  health.StatusHealthy,
            Message: "Database connection OK",
        }
    })

    // Check health
    result := provider.Check(context.Background(), "database")
    log.Printf("Health check result: %s - %s", result.Status, result.Message)
}
```

### gRPC Metrics Interceptor Example

```go
server := grpc.NewServer(
    grpc.UnaryInterceptor(
        middleware.UnaryServerMetrics(middleware.GRPCMetricsOptions{Provider: metricsProvider}),
    ),
)
```

### Database gRPC Service Example

```go
db, _ := sqlite.Open(sqlite.Config{Path: "app.db"})
grpcServer := grpc.NewServer()
db.GRPCService().Register(grpcServer)
```

### Multi-Module Example

```go
package main

import (
    "github.com/jdfalk/gcommon/pkg/health"
    "github.com/jdfalk/gcommon/pkg/metrics"
    "github.com/jdfalk/gcommon/pkg/log"
)

func main() {
    // Initialize health checking
    healthProvider := health.NewProvider()

    // Initialize metrics (75% complete)
    metricsProvider := metrics.NewPrometheusProvider()

    // Initialize logging (50% complete)
    logger := log.NewZapLogger()

    // More modules coming soon...
    // Database, Cache, Config, Auth, Queue, Web modules in development
}
```

## 📦 Current Module Status

| Module           | Completion | Ready for Production | gRPC Services | Recent Progress                           |
| ---------------- | ---------- | -------------------- | ------------- | ----------------------------------------- |
| **Health**       | ✅ 100%     | ✅ Yes                | ✅ Complete    | **✅ Complete 1-1-1 migration (36 types)** |
| **Common**       | ✅ 100%     | ✅ Yes                | ✅ Complete    | **✅ 40 shared types implemented**         |
| **Database**     | ✅ 100%     | ✅ Yes                | ✅ Complete    | **✅ Complete 1-1-1 migration (52 types)** |
| **Log**          | ✅ 100%     | ✅ Yes                | ✅ Complete    | **✅ Minimal logging implementation**      |
| **Auth**         | 🔄 13.5%    | ⚠️ Partial            | 🔄 Partial     | **🔄 17/126 files implemented**            |
| **Cache**        | 🔄 18.2%    | ❌ No                 | 🔄 In Progress | **🔄 8/44 files implemented**              |
| **Config**       | 🔄 13.0%    | ❌ No                 | ❌ Planned     | **🔄 3/23 files implemented**              |
| **Notification** | 🔄 25%      | ❌ No                 | ❌ Planned     | **🔄 Initial message types defined**       |
| **Metrics**      | 🔄 2.1%     | ❌ No                 | 🔄 In Progress | **❌ 95/97 files need implementation**     |
| **Queue**        | 🔄 1.1%     | ❌ No                 | ❌ Planned     | **❌ 175/177 files need implementation**   |
| **Web**          | 🔄 1.1%     | ❌ No                 | ❌ Planned     | **❌ 176/178 files need implementation**   |

**⚠️ Development Status**: This project is under active development. Only the Health, Common, and Database modules are production-ready.

## 🎉 Recent Achievements

### June 8, 2025: Complete Protobuf Implementation Roadmap ✅

We've completed comprehensive analysis and created a detailed implementation plan for all 754 protobuf files:

**🚀 Ready for Implementation:**

- **📊 Total Coverage**: 754 protobuf files analyzed and tracked
- **📋 GitHub Issues**: 39 detailed implementation issues created covering 625 empty files
- **🎯 Implementation Plan**: Detailed priority order and workflow established
- **✅ 100% Issue Coverage**: Every empty protobuf file has a corresponding GitHub issue
- **📝 Open Issues**: 58 currently active

**Current Module Status (June 8, 2025):**

- **✅ Common Module**: 100% complete (40/40 files) - **Shared Types Foundation**
- **✅ Database Module**: 100% complete (52/52 files) - **Gold Standard Reference**
- **✅ Log Module**: 100% complete (1/1 files) - **Minimal Implementation**
- **🔄 Auth Module**: 13.5% complete (17/126 files) - 109 files need implementation
- **🔄 Cache Module**: 18.2% complete (8/44 files) - 36 files need implementation
- **🔄 Config Module**: 13.0% complete (3/23 files) - 20 files need implementation
- **✅ Health Module**: 100% complete (16/16 files) - Stable and production-ready
- **❌ Metrics Module**: 2.1% complete (2/97 files) - **95 files need implementation**
- **❌ Queue Module**: 1.1% complete (2/177 files) - **175 files need implementation**
- **❌ Web Module**: 1.1% complete (2/178 files) - **176 files need implementation**

**Ready to Start:**

- **📍 GitHub Project**: [GCommon Development Board](https://github.com/users/jdfalk/projects/3)
- **📋 Next Step**: Start with Issue #67 (Protobuf Validation Pipeline)
- **🎯 Priority Order**: Metrics → Queue → Web → Auth → Cache → Config → Health
- **Priority 3**: Add request metadata to all services
- **Priority 4**: Enable gRPC services across all modules

**Critical Finding**: The protobuf migration from monolithic to 1-1-1 structure revealed **631 total types** requiring implementation - significantly more extensive than initially estimated.

## 🔧 Installation & Setup

### Prerequisites

- **go 1.23+** (required)
- **Protocol Buffers compiler** (`protoc`) - for gRPC development
- **Git** - for version control

### Quick Setup

```bash
# Clone the repository
git clone https://github.com/jdfalk/gcommon.git
cd gcommon

# Install dependencies
go mod download

# Generate protobuf code (if developing)
./generate.sh

# Run tests
go test ./...

# Try the health example
cd examples/health && go run .
```

### Development Tools (Optional)

```bash
# Install protobuf tools for gRPC development
go install google.golang.org/protobuf/cmd/protoc-gen-go@latest
go install google.golang.org/grpc/cmd/protoc-gen-go-grpc@latest

# Install mockery for testing
go install github.com/vektra/mockery/v2@latest
```

## 🤖 Automated Issue Management

This repository uses GitHub Actions for automated issue management. When working on features or bugs, **always update issue status** to maintain accurate project tracking.

### Issue Status Updates

To programmatically update GitHub issues, create an `issue_updates.json` file in the repository root and push to main:

```json
[
  {
    "action": "create",
    "title": "New Feature",
    "body": "Description",
    "labels": ["enhancement"]
  },
  {
    "action": "update",
    "number": 42,
    "state": "closed",
    "labels": ["completed"]
  },
  { "action": "update", "number": 43, "assignees": ["username"] }
]
```

**Supported Actions:**

- `create` - Create new issues with title, body, labels, assignees
- `update` - Modify existing issues by number (state, labels, assignees, etc.)
- `delete` - Remove issues (use sparingly)

**Required Workflow:**

1. 🚀 **Start Work**: Assign yourself to the issue and move to "In Progress"
2. 🔄 **During Work**: Update issue with progress comments as needed
3. ✅ **Complete Work**: Close issue and move to "Done" with completion summary

### Example Workflow

```bash
# When starting work on issue #68
echo '[{"action": "update", "number": 68, "assignees": ["your-username"], "labels": ["in-progress"]}]' > issue_updates.json
git add issue_updates.json && git commit -m "Start work on issue #68" && git push

# When completing work
echo '[{"action": "update", "number": 68, "state": "closed", "labels": ["completed"]}]' > issue_updates.json
git add issue_updates.json && git commit -m "Complete issue #68: Metrics Messages" && git push
```

The GitHub Actions workflow automatically processes these updates on every push to main.

## 🏗️ Architecture Overview

```text
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Go Interfaces │    │ gRPC Services   │    │ Common Types    │
│                 │    │                 │    │                 │
│ • Clean APIs    │◄──►│ • Protobuf      │◄──►│ • Shared Models │
│ • Provider      │    │ • Cross-language│    │ • Consistency   │
│   Pattern       │    │ • Streaming     │    │ • Validation    │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

**Key Principles:**

- **Interface-First Design**: Clean Go interfaces before implementation
- **Protocol Buffers Foundation**: All services defined using protobuf
- **Dual API Support**: Both Go interfaces and gRPC for maximum flexibility
- **Common Types**: Shared definitions for consistency across modules

## 🤝 Contributing

We welcome contributions! Current priority areas:

1. **Completing Metrics Module** (75% → 100%)
2. **Finishing Logging Module** (50% → 100%)
3. **Documentation improvements**
4. **Example applications**

See our [contribution guidelines](.github/CONTRIBUTING.md) for code style, testing requirements, and development workflow.

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

## 🆘 Need Help?

- **📖 Documentation**: [docs/](docs/) directory
- **💡 Examples**: [examples/](examples/) directory
- **🐛 Issues**: [GitHub Issues](https://github.com/jdfalk/gcommon/issues)
- **💬 Discussions**: [GitHub Discussions](https://github.com/jdfalk/gcommon/discussions)

The updated setup script automatically authenticates using `gh auth token` and links open issues by module labels.

### GitHub Projects

This repository now uses a dedicated GitHub Project board for each major module (Metrics, Queue, Web, Auth, Cache, Config). Run the unified project manager to create these boards and automatically add issues by label:

```bash
python3 /path/to/ghcommon/scripts/unified_github_project_manager_v2.py
```

See `scripts/MIGRATION-NOTICE.md` for migration details.

Implemented initial auth configuration and API key messages
Logging module migrated to 1-1-1 structure with 10 new protobuf files
Implemented initial metrics protobufs
### July 22, 2025: Cache module complete
Updated config module progress
- Added DebugInfo message for advanced debugging
Implemented TransactionService and MigrationService protobufs

# Metrics

| **Metrics**      | 🔄 7%     | ❌ No                 | 🔄 In Progress | **❌ 90/97 files need implementation**     |
