# GCommon - Common Go Modules

[![Go Version](https://img.shields.io/badge/go-1.21+-blue.svg)](https://golang.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)](https://github.com/jdfalk/gcommon)

> **🚨 MAJOR BREAKING CHANGES COMING**: Version 0.2.0 will introduce significant protobuf message structure changes. See [CHANGELOG.md](CHANGELOG.md) for migration details.

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

    // Initialize metrics (70% complete)
    metricsProvider := metrics.NewPrometheusProvider()

    // Initialize logging (50% complete)
    logger := log.NewZapLogger()

    // More modules coming soon...
    // Database, Cache, Config, Auth, Queue, Web modules in development
}
```

## 📦 Current Module Status

| Module       | Completion | Ready for Production | gRPC Services | Recent Progress                           |
| ------------ | ---------- | -------------------- | ------------- | ----------------------------------------- |
| **Health**   | ✅ 100%     | ✅ Yes                | ✅ Complete    | Stable and production-ready               |
| **Common**   | ✅ 100%     | ✅ Yes                | ✅ Complete    | **✅ 39 shared types implemented**         |
| **Database** | ✅ 100%     | ✅ Yes                | ✅ Complete    | **✅ Complete 1-1-1 migration (51 types)** |
| **Auth**     | 🔄 33%      | ⚠️ Partial            | 🔄 Partial     | **🔄 16/48 types migrated**                |
| **Metrics**  | 🔄 17%      | ❌ No                 | 🔄 In Progress | **626 empty proto files identified**      |
| **Cache**    | 🔄 15%      | ❌ No                 | ❌ Planned     | Basic structure in place                  |
| **Config**   | 🔄 9%       | ❌ No                 | ❌ Planned     | Service definitions complete              |
| **Logging**  | 🔄 0%       | ❌ No                 | ❌ Planned     | **❌ All 50 types need implementation**    |
| **Queue**    | 🔄 1%       | ❌ No                 | ❌ Planned     | **❌ 142/143 types need implementation**   |
| **Web**      | 🔄 1%       | ❌ No                 | ❌ Planned     | **❌ 122/123 types need implementation**   |

**⚠️ Development Status**: This project is under active development. Only the Health module is production-ready.

## 🎉 Recent Achievements

### June 2025: Critical Protobuf Analysis & Implementation Roadmap ✅

We've completed a comprehensive analysis of the protobuf structure and identified the current implementation state:

**Major Discoveries:**

- **📊 Total Proto Files**: 754 protobuf files across all modules
- **🔄 Implementation Status**: 128 files implemented (17%), 626 files empty (83%)
- **✅ Foundation Complete**: Common module with 39 shared types fully implemented
- **🔧 Services Defined**: 29 services across 9 modules with clear interfaces

**Current Module Status:**

- **✅ Database Module**: 100% migrated (51/51 types) - **Gold Standard**
- **🔄 Auth Module**: 33% complete (16/48 types) - Good progress
- **⚠️ Other Modules**: 0-15% complete - Require immediate attention

**Next Implementation Phase:**

- **Priority 1**: Complete empty protobuf implementations (626 files)
- **Priority 2**: Standardize error handling with common types
- **Priority 3**: Add request metadata to all services
- **Priority 4**: Enable gRPC services across all modules

**Critical Finding**: The protobuf migration from monolithic to 1-1-1 structure revealed **631 total types** requiring implementation - significantly more extensive than initially estimated.

## 🔧 Installation & Setup

### Prerequisites

- **Go 1.21+** (required)
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

## 📚 Essential Documentation

### New Users Start Here

- **[Getting Started Guide](docs/user/getting-started.md)** - Complete setup and first steps
- **[Health Module Guide](docs/user/health-kubernetes.md)** - Production-ready health monitoring
- **[Basic Examples](examples/)** - Working code examples for each module

### For Developers

- **[Project Roadmap](TODO.md)** - Implementation status and plans
- **[Technical Architecture](CHANGELOG.md)** - Detailed technical documentation
- **[Protobuf API Design](docs/technical/protobuf-grpc-design.md)** - gRPC service definitions

### Module-Specific Guides

- [Metrics Collection](docs/user/metrics.md) (70% complete)
- [Logging](docs/user/logging.md) (50% complete)
- [Database Operations](docs/user/database.md) (30% complete)
- [Caching](docs/user/cache.md) (20% complete)
- [Configuration Management](docs/user/config.md) (20% complete)

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

1. **Completing Metrics Module** (70% → 100%)
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
