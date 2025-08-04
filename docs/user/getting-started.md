# Getting Started with GCommon

## Introduction

GCommon is a comprehensive collection of reusable Go modules designed to
accelerate application development by providing common functionality that most
Go applications require. The library is built with flexibility, performance, and
ease-of-use in mind, allowing developers to focus on building
application-specific features rather than reimplementing common patterns.

## Installation

To use GCommon in your project, add it as a dependency using Go modules:

```bash
go get github.com/jdfalk/gcommon@latest
```

You can also pin to a specific version:

```bash
go get github.com/jdfalk/gcommon@v1.0.0
```

## Core Modules

GCommon consists of several core modules that you can use independently or
together:

- **Database** - A unified interface for database operations with support for
  SQLite, PostgreSQL, CockroachDB, and Pebble
- **Logging** - A flexible logging framework with support for multiple backends
  (standard library, zap, logrus)
- **Metrics** - A comprehensive metrics collection system with support for
  Prometheus and OpenTelemetry
- **Web Server** - A robust HTTP server with middleware, routing, and template
  support
- **Config** - A unified configuration system with support for multiple sources
  and formats
- **Cache** - A caching layer with multiple backend options
- **Auth** - Authentication and authorization functionality
- **Queue** - A message queue abstraction with multiple implementations
- **Health** - Health checking functionality for services

Each module is designed to work seamlessly with the others but can also be used
standalone.

## Quick Start Example

Here's a simple example that uses several GCommon modules to create a web
service with database access, logging, and metrics:

```go
package main

import (
 "context"
 "fmt"
 "net/http"
 "os"
 "time"

 "github.com/jdfalk/gcommon/pkg/config"
 "github.com/jdfalk/gcommon/pkg/db"
 "github.com/jdfalk/gcommon/pkg/log"
 "github.com/jdfalk/gcommon/pkg/metrics"
 "github.com/jdfalk/gcommon/pkg/web"
)

func main() {
 // Initialize configuration
 cfg, err := config.Load("config.yaml", config.WithEnv(), config.WithDefaults())
 if err != nil {
  fmt.Printf("Failed to load config: %v\n", err)
  os.Exit(1)
 }

 // Initialize logger
 logCfg := cfg.Sub("logging").(*log.Config)
 logger, err := log.NewProvider(*logCfg)
 if err != nil {
  fmt.Printf("Failed to initialize logger: %v\n", err)
  os.Exit(1)
 }
 defer logger.Close()

 // Get the main logger instance
 mainLogger := logger.GetLogger("main")
 mainLogger.Info("Starting application")

 // Initialize metrics
 metricsCfg := cfg.Sub("metrics").(*metrics.Config)
 metricsProvider, err := metrics.NewProvider(context.Background(), *metricsCfg)
 if err != nil {
  mainLogger.Error("Failed to initialize metrics", log.Error(err))
  os.Exit(1)
 }
 defer metricsProvider.Stop(context.Background())

 // Initialize database
 dbCfg := cfg.Sub("database").(*db.Config)
 database, err := db.Open(*dbCfg)
 if err != nil {
  mainLogger.Error("Failed to connect to database", log.Error(err))
  os.Exit(1)
 }
 defer database.Close()

 // Add logger to database
 database = database.WithLogger(logger.GetLogger("database"))

 // Initialize web server
 webCfg := cfg.Sub("web").(*web.Config)
 server := web.NewServer(*webCfg)

 // Add middleware
 server.Use(web.Recovery())
 server.Use(web.Logger(logger.GetLogger("web")))
 server.Use(web.Metrics(metricsProvider))

 // Define routes
 server.GET("/", func(c web.Context) error {
  return c.String(http.StatusOK, "Hello, World!")
 })

 // Define an API route that uses the database
 server.GET("/users/:id", func(c web.Context) error {
  id := c.Param("id")

  var user struct {
   ID    string `db:"id" json:"id"`
   Name  string `db:"name" json:"name"`
   Email string `db:"email" json:"email"`
  }

  err := database.QueryRow(
   c.Request().Context(),
   "SELECT id, name, email FROM users WHERE id = $1",
   id,
  ).ScanStruct(&user)

  if err != nil {
   if err == db.ErrNoRows {
    return c.JSON(http.StatusNotFound, map[string]string{"error": "User not found"})
   }
   mainLogger.Error("Failed to query user", log.Error(err), log.String("id", id))
   return c.JSON(http.StatusInternalServerError, map[string]string{"error": "Internal server error"})
  }

  return c.JSON(http.StatusOK, user)
 })

 // Start the server
 mainLogger.Info("Starting web server", log.String("address", webCfg.Address))
 if err := server.Start(); err != nil {
  mainLogger.Error("Server failed", log.Error(err))
  os.Exit(1)
 }
}
```

## Module-Specific Documentation

For more detailed information on each module, see the following documentation:

- [Database](database.md)
- [Logging](logging.md)
- [Metrics](metrics.md)
- [Web Server](webserver.md)
- [Config](config.md)
- [Cache](cache.md)

## Configuration

GCommon modules can be configured through a variety of methods:

- YAML/JSON/TOML configuration files
- Environment variables
- Command-line flags
- In-code defaults

See the [Config documentation](config.md) for more detailed information.

## Best Practices

### Error Handling

GCommon follows standard Go error handling patterns. Always check errors
returned from GCommon functions and handle them appropriately:

```go
result, err := database.Exec(ctx, "INSERT INTO users (name) VALUES ($1)", "John")
if err != nil {
    // Handle the error appropriately
    logger.Error("Failed to insert user", log.Error(err))
    return err
}
```

### Resource Management

Many GCommon components require proper cleanup. Always use `defer` to ensure
resources are released:

```go
database, err := db.Open(config)
if err != nil {
    // Handle error
}
defer database.Close()

// Use database...
```

### Context Propagation

GCommon extensively uses Go's context package for cancellation, timeouts, and
value propagation. Always pass appropriate context values:

```go
ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
defer cancel()

rows, err := database.Query(ctx, "SELECT * FROM users")
```

### Concurrency

GCommon components are generally thread-safe, but refer to specific module
documentation for any concurrency limitations or requirements.

## Contributing

We welcome contributions to GCommon! See
[CONTRIBUTING.md](../../CONTRIBUTING.md) for guidelines.

## License

GCommon is available under the [MIT License](../../LICENSE).
