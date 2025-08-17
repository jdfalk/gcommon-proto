# Configuration Module

## Overview

The GCommon Configuration module provides a unified interface for managing application configuration with support for multiple sources and formats. It enables hierarchical configuration, environment variable integration, command-line flags,
defaults, validation, and hot reloading capabilities. The module is built on top of [Viper](https://github.com/spf13/viper) for configuration management and [Cobra](https://github.com/spf13/cobra) for command-line interface functionality,
providing a simplified and enhanced API while leveraging these battle-tested libraries.

## Features

- **Multiple Sources**: Load configuration from files, environment variables, command-line flags, and in-code defaults
- **Multiple Formats**: Support for YAML, JSON, TOML, and HCL
- **Hierarchical Structure**: Access nested configuration using dot notation
- **Environment Variable Integration**: Override configuration with environment variables
- **Command-Line Flag Integration**: Override configuration with command-line flags
- **Defaults**: Provide fallback values for configuration
- **Validation**: Validate configuration against schemas
- **Hot Reloading**: Automatically reload configuration when source files change
- **Type Conversion**: Convert configuration values to specific types
- **Strongly Typed Config**: Map configuration to strongly typed structs

## Installation

The configuration module is part of the GCommon library:

```bash
go get github.com/jdfalk/gcommon@latest
```

## Basic Usage

### Loading Configuration

```go
import (
    "fmt"
    "github.com/jdfalk/gcommon/pkg/config"
)

func main() {
    // Load configuration from a file with environment variable overrides
    cfg, err := config.Load(
        "config.yaml",
        config.WithEnv(),
        config.WithDefaults(map[string]interface{}{
            "server.port": 8080,
        }),
    )
    if err != nil {
        fmt.Printf("Failed to load config: %v\n", err)
        return
    }

    // Access configuration values
    port := cfg.GetInt("server.port")
    host := cfg.GetString("server.host")

    fmt.Printf("Server will listen on %s:%d\n", host, port)
}
```

### Configuration File Example

```yaml
# config.yaml
server:
  host: localhost
  port: 9000
  timeout: 30s

database:
  driver: postgres
  dsn: postgres://user:password@localhost/mydb
  maxOpenConns: 10
  maxIdleConns: 5
  connMaxLifetime: 5m

logging:
  level: info
  format: json
  output: stdout

metrics:
  enabled: true
  provider: prometheus
  endpoint: /metrics
```

### Accessing Configuration

```go
// Get values with type conversion
host := cfg.GetString("server.host")               // "localhost"
port := cfg.GetInt("server.port")                  // 9000
timeout := cfg.GetDuration("server.timeout")       // 30 seconds
metricsEnabled := cfg.GetBool("metrics.enabled")   // true

// Get nested configuration as a sub-config
dbConfig := cfg.Sub("database")
driver := dbConfig.GetString("driver")             // "postgres"
dsn := dbConfig.GetString("dsn")                   // "postgres://user:password@localhost/mydb"

// Get with default fallback
debugMode := cfg.GetBool("server.debug", false)    // false (not defined in config)
```

## Advanced Usage

### Environment Variables Integration

You can override configuration values using environment variables:

```go
cfg, err := config.Load(
    "config.yaml",
    config.WithEnv(),
    config.WithEnvPrefix("APP"),
)
```

With this configuration:

- Environment variable `APP_SERVER_PORT=8080` would override `server.port` in the config file
- Environment variable `APP_DATABASE_DSN=postgres://localhost/testdb` would override `database.dsn`

### Command-Line Flag Integration

You can override configuration values using command-line flags. The configuration module integrates with both standard Go flag package and the more powerful Cobra library for command-line interfaces:

#### Standard flag package

```go
import (
    "flag"
    "github.com/jdfalk/gcommon/pkg/config"
)

func main() {
    // Define flags
    serverPort := flag.Int("port", 0, "Server port")
    logLevel := flag.String("log-level", "", "Log level")
    flag.Parse()

    // Load configuration with flag overrides
    cfg, err := config.Load(
        "config.yaml",
        config.WithEnv(),
        config.WithFlags(map[string]interface{}{
            "server.port": *serverPort,
            "logging.level": *logLevel,
        }),
    )

    // Only non-zero/non-empty flag values will override the configuration
}
```

#### Cobra CLI integration

For more advanced command-line interfaces, the module seamlessly integrates with Cobra:

```go
import (
    "github.com/jdfalk/gcommon/pkg/config"
    "github.com/spf13/cobra"
)

func main() {
    // Create a root command
    rootCmd := &cobra.Command{
        Use:   "myapp",
        Short: "My application description",
        Run: func(cmd *cobra.Command, args []string) {
            // Load configuration with Cobra flag bindings
            cfg, err := config.Load(
                "config.yaml",
                config.WithEnv(),
                config.WithCobra(cmd),
            )
            if err != nil {
                cmd.PrintErr(err)
                return
            }

            // Run your application with config
            if err := runApp(cfg); err != nil {
                cmd.PrintErr(err)
            }
        },
    }

    // Define persistent flags for all commands
    rootCmd.PersistentFlags().String("config", "config.yaml", "Config file path")
    rootCmd.PersistentFlags().Int("port", 8080, "Server port")
    rootCmd.PersistentFlags().String("log-level", "info", "Logging level")

    // Add subcommands
    rootCmd.AddCommand(newServerCmd())

    // Execute the command
    if err := rootCmd.Execute(); err != nil {
        os.Exit(1)
    }
}

func newServerCmd() *cobra.Command {
    cmd := &cobra.Command{
        Use:   "server",
        Short: "Run the server",
        Run: func(cmd *cobra.Command, args []string) {
            // Load configuration with Cobra flag bindings
            cfg, err := config.Load(
                cmd.Flag("config").Value.String(),
                config.WithEnv(),
                config.WithCobra(cmd),
            )
            if err != nil {
                cmd.PrintErr(err)
                return
            }

            // Run server with config
            if err := runServer(cfg); err != nil {
                cmd.PrintErr(err)
            }
        },
    }

    // Add server-specific flags
    cmd.Flags().Int("timeout", 30, "Server timeout in seconds")

    return cmd
}
```

### Structured Configuration

You can map configuration to strongly typed structs:

```go
// Define configuration structs
type AppConfig struct {
    Server   ServerConfig   `mapstructure:"server"`
    Database DatabaseConfig `mapstructure:"database"`
    Logging  LoggingConfig  `mapstructure:"logging"`
}

type ServerConfig struct {
    Host    string        `mapstructure:"host"`
    Port    int           `mapstructure:"port"`
    Timeout time.Duration `mapstructure:"timeout"`
    Debug   bool          `mapstructure:"debug"`
}

type DatabaseConfig struct {
    Driver         string        `mapstructure:"driver"`
    DSN            string        `mapstructure:"dsn"`
    MaxOpenConns   int           `mapstructure:"maxOpenConns"`
    MaxIdleConns   int           `mapstructure:"maxIdleConns"`
    ConnMaxLifetime time.Duration `mapstructure:"connMaxLifetime"`
}

type LoggingConfig struct {
    Level  string `mapstructure:"level"`
    Format string `mapstructure:"format"`
    Output string `mapstructure:"output"`
}

// Load configuration into structs
cfg, err := config.Load("config.yaml")
if err != nil {
    // Handle error
}

var appConfig AppConfig
if err := cfg.Unmarshal(&appConfig); err != nil {
    // Handle error
}

// Access typed configuration
fmt.Printf("Server will listen on %s:%d\n", appConfig.Server.Host, appConfig.Server.Port)
```

### Configuration Validation

You can validate configuration against a schema:

```go
// Define validation schema using go-playground/validator syntax
schema := map[string]string{
    "server.port":      "required,min=1024,max=65535",
    "server.host":      "required",
    "database.driver":  "required,oneof=sqlite postgres cockroach",
    "database.dsn":     "required",
    "logging.level":    "required,oneof=debug info warn error fatal",
}

cfg, err := config.Load(
    "config.yaml",
    config.WithValidation(schema),
)
if err != nil {
    // Error will be returned if validation fails
}
```

### Hot Reloading

You can enable hot reloading to automatically reload configuration when the source file changes:

```go
cfg, err := config.Load(
    "config.yaml",
    config.WithHotReload(true),
)
if err != nil {
    // Handle error
}

// Register callback for configuration changes
cfg.OnChange(func() {
    fmt.Println("Configuration reloaded!")
    // Update application state based on new configuration
    newPort := cfg.GetInt("server.port")
    fmt.Printf("New server port: %d\n", newPort)
})
```

### Multiple Configuration Files

You can load configuration from multiple files:

```go
cfg, err := config.Load(
    []string{
        "config.yaml",      // Base configuration
        "config.local.yaml", // Local overrides
    },
    config.WithEnv(),
)
```

Later files in the list override values from earlier files.

### Secret Management

You can integrate with secret management systems:

```go
cfg, err := config.Load(
    "config.yaml",
    config.WithSecretProvider(
        NewVaultSecretProvider("https://vault.example.com"),
    ),
)

// Then in your config file, you can reference secrets:
// database:
//   dsn: "{{vault:database/credentials/myapp}}"
```

## Viper and Cobra Integration

The GCommon Configuration module is built on top of two powerful Go libraries:

### Viper Integration

[Viper](https://github.com/spf13/viper) is used under the hood to provide:

- Configuration from multiple sources (files, environment variables, flags)
- Support for multiple configuration formats (YAML, JSON, TOML, HCL)
- Hierarchical configuration structure
- Real-time watching and re-reading of config files
- Live watching for changes in etcd or Consul

The GCommon Configuration module extends Viper's capabilities with:

- A simpler, more intuitive API
- Enhanced validation
- Better integration with other GCommon components
- Simplified secret management
- Structured configuration with strong typing

### Cobra Integration

[Cobra](https://github.com/spf13/cobra) is used to provide robust command-line interface capabilities:

- Easy subcommand-based CLIs: `app server start`, `app config validate`
- Fully POSIX-compliant flags (including short & long versions)
- Nested commands
- Global and local flags
- Intelligent suggestions (`app srver` → `Did you mean app server?`)
- Automatic help generation
- Custom help and usage text
- Shell completions (Bash, Zsh, fish, PowerShell)

The GCommon Configuration module integrates seamlessly with Cobra through:

- The `WithCobra()` option for binding Cobra commands to configuration
- Automatic mapping between command flags and configuration keys
- Unified help documentation

For more advanced CLI applications, you can directly access the underlying Cobra command structure:

```go
import (
    "github.com/jdfalk/gcommon/pkg/config"
)

func main() {
    app := config.NewApp("myapp", "1.0.0", "My amazing application")

    // Get the root Cobra command to customize
    rootCmd := app.GetRootCommand()

    // Add more custom commands
    migrateCmd := &cobra.Command{
        Use:   "migrate",
        Short: "Database migration commands",
    }
    migrateCmd.AddCommand(
        newMigrateUpCommand(),
        newMigrateDownCommand(),
    )
    rootCmd.AddCommand(migrateCmd)

    // Run the app
    app.Run()
}
```

## Best Practices

### Configuration Organization

- Group related configuration settings under common prefixes
- Use descriptive names for configuration keys
- Document each configuration option
- Provide reasonable defaults for all configuration options

### Environment-Specific Configuration

Use different files for different environments:

```bash
config.yaml          # Common configuration
config.dev.yaml      # Development-specific overrides
config.staging.yaml  # Staging-specific overrides
config.prod.yaml     # Production-specific overrides
```

Load the appropriate file based on the environment:

```go
env := os.Getenv("APP_ENV")
if env == "" {
    env = "dev" // Default to development
}

cfg, err := config.Load(
    []string{
        "config.yaml",
        fmt.Sprintf("config.%s.yaml", env),
    },
    config.WithEnv(),
)
```

### Sensitive Information

- Never store sensitive information like passwords or API keys directly in configuration files
- Use environment variables or secret management systems for sensitive information
- Consider using the `config.WithSecretProvider()` option to integrate with secret management systems

### Testing

For testing with configuration:

```go
// Create a test configuration
testCfg := config.New()
testCfg.Set("server.port", 8081)
testCfg.Set("database.driver", "sqlite")
testCfg.Set("database.dsn", ":memory:")

// Use the test configuration for your tests
server := NewServer(testCfg)
```

## Complete Example

```go
package main

import (
    "fmt"
    "log"
    "os"
    "time"

    "github.com/jdfalk/gcommon/pkg/config"
)

type AppConfig struct {
    Server   ServerConfig   `mapstructure:"server"`
    Database DatabaseConfig `mapstructure:"database"`
    Logging  LoggingConfig  `mapstructure:"logging"`
}

type ServerConfig struct {
    Host    string        `mapstructure:"host"`
    Port    int           `mapstructure:"port"`
    Timeout time.Duration `mapstructure:"timeout"`
}

type DatabaseConfig struct {
    Driver  string `mapstructure:"driver"`
    DSN     string `mapstructure:"dsn"`
}

type LoggingConfig struct {
    Level  string `mapstructure:"level"`
    Format string `mapstructure:"format"`
    Output string `mapstructure:"output"`
}

func main() {
    // Determine environment
    env := os.Getenv("APP_ENV")
    if env == "" {
        env = "dev"
    }

    // Define defaults
    defaults := map[string]interface{}{
        "server.host":      "localhost",
        "server.port":      8080,
        "server.timeout":   "30s",
        "logging.level":    "info",
        "logging.format":   "json",
        "logging.output":   "stdout",
        "database.driver":  "sqlite",
        "database.dsn":     ":memory:",
    }

    // Define validation
    validation := map[string]string{
        "server.port":     "required,min=1024,max=65535",
        "server.host":     "required",
        "database.driver": "required,oneof=sqlite postgres cockroach",
        "database.dsn":    "required",
        "logging.level":   "required,oneof=debug info warn error fatal",
    }

    // Load configuration
    cfg, err := config.Load(
        []string{
            "config.yaml",
            fmt.Sprintf("config.%s.yaml", env),
        },
        config.WithDefaults(defaults),
        config.WithEnv(),
        config.WithEnvPrefix("APP"),
        config.WithValidation(validation),
        config.WithHotReload(true),
    )
    if err != nil {
        log.Fatalf("Failed to load configuration: %v", err)
    }

    // Handle configuration reloading
    cfg.OnChange(func() {
        log.Println("Configuration reloaded")
        // Update application state
    })

    // Map to structured config
    var appConfig AppConfig
    if err := cfg.Unmarshal(&appConfig); err != nil {
        log.Fatalf("Failed to unmarshal configuration: %v", err)
    }

    // Use the configuration
    fmt.Printf("Server configuration: %+v\n", appConfig.Server)
    fmt.Printf("Database driver: %s\n", appConfig.Database.Driver)
    fmt.Printf("Log level: %s\n", appConfig.Logging.Level)
}
```

## Reference

### Configuration Methods

| Method                                                               | Description                                   |
| -------------------------------------------------------------------- | --------------------------------------------- |
| `GetString(key string, defaultVal ...string) string`                 | Get a string value                            |
| `GetInt(key string, defaultVal ...int) int`                          | Get an integer value                          |
| `GetInt32(key string, defaultVal ...int32) int32`                    | Get a 32-bit integer value                    |
| `GetInt64(key string, defaultVal ...int64) int64`                    | Get a 64-bit integer value                    |
| `GetUint(key string, defaultVal ...uint) uint`                       | Get an unsigned integer value                 |
| `GetUint32(key string, defaultVal ...uint32) uint32`                 | Get a 32-bit unsigned integer value           |
| `GetUint64(key string, defaultVal ...uint64) uint64`                 | Get a 64-bit unsigned integer value           |
| `GetFloat32(key string, defaultVal ...float32) float32`              | Get a 32-bit float value                      |
| `GetFloat64(key string, defaultVal ...float64) float64`              | Get a 64-bit float value                      |
| `GetBool(key string, defaultVal ...bool) bool`                       | Get a boolean value                           |
| `GetDuration(key string, defaultVal ...time.Duration) time.Duration` | Get a duration value                          |
| `GetTime(key string, defaultVal ...time.Time) time.Time`             | Get a time value                              |
| `GetStringSlice(key string, defaultVal ...[]string) []string`        | Get a string slice                            |
| `GetIntSlice(key string, defaultVal ...[]int) []int`                 | Get an integer slice                          |
| `GetStringMap(key string) map[string]interface{}`                    | Get a map with string keys                    |
| `GetStringMapString(key string) map[string]string`                   | Get a map with string keys and values         |
| `Get(key string, defaultVal ...interface{}) interface{}`             | Get a value as interface{}                    |
| `Set(key string, value interface{})`                                 | Set a configuration value                     |
| `Has(key string) bool`                                               | Check if a key exists                         |
| `Sub(key string) Config`                                             | Get a sub-configuration                       |
| `Keys() []string`                                                    | Get all keys at the current level             |
| `AllKeys() []string`                                                 | Get all keys at all levels                    |
| `AllSettings() map[string]interface{}`                               | Get all settings as a map                     |
| `Unmarshal(v interface{}) error`                                     | Unmarshal configuration into a struct         |
| `MarshalJSON() ([]byte, error)`                                      | Marshal configuration to JSON                 |
| `OnChange(func())`                                                   | Register a callback for configuration changes |
| `WatchKey(key string, callback func(interface{}))`                   | Watch a specific key for changes              |

### Load Options

| Option                                          | Description                            |
| ----------------------------------------------- | -------------------------------------- |
| `WithEnv()`                                     | Enable environment variable overrides  |
| `WithEnvPrefix(prefix string)`                  | Set a prefix for environment variables |
| `WithDefaults(defaults map[string]interface{})` | Set default values                     |
| `WithFlags(flags map[string]interface{})`       | Override with command-line flags       |
| `WithCobra(cmd *cobra.Command)`                 | Integrate with Cobra command           |
| `WithValidation(rules map[string]string)`       | Validate configuration                 |
| `WithHotReload(enable bool)`                    | Enable hot reloading                   |
| `WithSecretProvider(provider SecretProvider)`   | Integrate with a secret provider       |
| `WithConfigType(configType string)`             | Specify configuration file type        |
| `WithErrorOnMissing(errorOnMissing bool)`       | Error if a required file is missing    |
