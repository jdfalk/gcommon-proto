<!-- file: pkg/config/README.md -->
<!-- version: 1.0.0 -->
<!-- guid: ae4a9c20-7378-4546-acf1-0bf9d3e6c956 -->

# Config Module

This module provides a pluggable configuration system with a provider factory.

## Quick Start

```go
p, _ := config.NewProvider("env", nil)
value, _ := p.Get("EXAMPLE_KEY")
```

## Providers

- **env**: uses environment variables
- **file**: reads and writes JSON configuration files
