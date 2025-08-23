# file: sdks/README.md
# version: 1.0.0
# guid: 56789012-5678-9012-def0-567890123456

# gcommon SDKs

This directory contains language-specific SDKs for the gcommon protobuf packages.

## Available SDKs

### Go SDK (`sdks/go/`)

Import gcommon packages in your Go applications:

```go
import (
    "github.com/jdfalk/gcommon/sdks/go/gcommon/v1/common"
    "github.com/jdfalk/gcommon/sdks/go/gcommon/v1/queue"
    "github.com/jdfalk/gcommon/sdks/go/gcommon/v1/config"
    // ... other packages
)
```

**Installation:**
```bash
go mod init your-project
go get github.com/jdfalk/gcommon/sdks/go
```

### Python SDK (`sdks/python/`)

Import gcommon packages in your Python applications:

```python
from gcommon.v1.common import common_pb2
from gcommon.v1.queue import queue_pb2
from gcommon.v1.config import config_pb2
# ... other packages
```

**Installation:**
```bash
pip install ./sdks/python
# or for development:
pip install -e ./sdks/python
```

## Generated Packages

All SDKs include the following protobuf packages:

- **common** - Common data types and utilities
- **queue** - Message queue and streaming systems
- **config** - Configuration management
- **database** - Database operations and schemas
- **media** - Media processing and metadata
- **metrics** - System metrics and monitoring
- **organization** - Organization and user management
- **web** - Web services and HTTP handling

## Usage Examples

See the `examples/` directory for complete usage examples in each language.

## Build Information

These SDKs are automatically generated from the protobuf definitions in the `pkg/` directory using `buf generate`. The generation process:

1. Reads protobuf files from `pkg/`
2. Generates language-specific code using buf plugins
3. Outputs to language-specific SDK directories
4. Creates proper module/package structure for each language

To regenerate the SDKs after protobuf changes:

```bash
buf generate
```
