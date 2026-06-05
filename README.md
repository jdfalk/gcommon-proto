<!-- file: README.md -->
<!-- version: 2.0.0 -->
<!-- guid: 1a2b3c4d-e5f6-7a8b-9c0d-1e2f3a4b5c6d -->

# GCommon - Protocol Buffer Definitions for Common Services

[![Buf](https://img.shields.io/badge/buf-build%2Fjdfalk%2Fgcommon-blue)](https://buf.build/falkcorp/gcommon)
[![CI](https://github.com/falkcorp/gcommon/workflows/ci/badge.svg)](https://github.com/falkcorp/gcommon/actions)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

**GCommon** is a centralized repository of Protocol Buffer definitions for common business services. It provides standardized gRPC service definitions and message types that can be used across multiple applications and languages.

## 🚀 Quick Start

### Using the Buf Schema Registry (BSR)

The easiest way to use GCommon is through the [Buf Schema Registry](https://buf.build/falkcorp/gcommon):

```yaml
# buf.yaml
version: v2
deps:
  - buf.build/falkcorp/gcommon
```

### Language-Specific SDKs

- **Go**: [github.com/falkcorp/gcommon-go](https://github.com/falkcorp/gcommon-go)
- **Python**: [github.com/falkcorp/gcommon-py](https://github.com/falkcorp/gcommon-py)

## 📦 Module Overview

GCommon provides **9 core modules** with **1,734 protocol buffer definitions**:

| Module           | Files | Description                                                |
| ---------------- | ----- | ---------------------------------------------------------- |
| **common**       | 509   | Shared types, errors, pagination, and utility messages     |
| **config**       | 114   | Configuration management and settings                      |
| **database**     | 139   | Database operations, migrations, and connection management |
| **health**       | 36    | Health checks, monitoring, and service status              |
| **media**        | 75    | Media processing, subtitles, and content management        |
| **metrics**      | 220   | System metrics, alerting, and performance monitoring       |
| **organization** | 117   | Multi-tenant organization and user management              |
| **queue**        | 322   | Message queuing, job processing, and task management       |
| **web**          | 202   | HTTP services, middleware, and web application utilities   |

## 🏗️ Repository Structure

```text
gcommon/
├── common/v1/           # Shared types and utilities
├── config/v1/           # Configuration management
├── database/v1/         # Database operations
├── health/v1/           # Health monitoring
├── media/v1/            # Media processing
├── metrics/v1/          # System metrics
├── organization/v1/     # Organization management
├── queue/v1/            # Message queuing
├── web/v1/              # Web services
├── buf.yaml             # Buf configuration
└── proto-docs/          # Generated documentation
```

## 🔧 Development

### Prerequisites

- [Buf CLI](https://buf.build/docs/installation) v1.28.0+
- [Protocol Buffers](https://protobuf.dev/downloads/) v25.0+

### Local Development

```bash
# Clone the repository
git clone https://github.com/falkcorp/gcommon.git
cd gcommon

# Lint protocol buffers
buf lint

# Generate documentation
buf generate
```

### Adding New Definitions

1. Add your `.proto` files to the appropriate module directory (`module/v1/`)
2. Update imports to use the new module structure: `import "common/v1/error.proto";`
3. Ensure `go_package` options follow the pattern: `option go_package = "github.com/falkcorp/gcommon/module/v1";`
4. Run `buf lint` to validate
5. Submit a pull request

## 📖 Documentation

- **[API Documentation](proto-docs/)** - Generated from protocol buffers
- **[Buf Schema Registry](https://buf.build/falkcorp/gcommon)** - Browse definitions online
- **[Contributing Guide](CONTRIBUTING.md)** - How to contribute
- **[Changelog](CHANGELOG.md)** - Version history

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Need Help?

- **Issues**: [GitHub Issues](https://github.com/falkcorp/gcommon/issues)
- **Discussions**: [GitHub Discussions](https://github.com/falkcorp/gcommon/discussions)
- **Documentation**: [proto-docs/](proto-docs/)
