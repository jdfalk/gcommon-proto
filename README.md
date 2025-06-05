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

| Module       | Completion | Ready for Production | gRPC Services |
| ------------ | ---------- | -------------------- | ------------- |
| **Health**   | ✅ 100%     | ✅ Yes                | ✅ Complete    |
| **Metrics**  | 🔄 70%      | ⚠️ Partial            | 🔄 In Progress |
| **Logging**  | 🔄 50%      | ❌ No                 | ❌ Planned     |
| **Auth**     | 🔄 40%      | ❌ No                 | ❌ Planned     |
| **Database** | 🔄 30%      | ❌ No                 | ❌ Planned     |
| **Cache**    | 🔄 20%      | ❌ No                 | ❌ Planned     |
| **Config**   | 🔄 20%      | ❌ No                 | ❌ Planned     |
| **Queue**    | 🔄 10%      | ❌ No                 | ❌ Planned     |
| **Web**      | 🔄 10%      | ❌ No                 | ❌ Planned     |

**⚠️ Development Status**: This project is under active development. Only the Health module is production-ready.

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
