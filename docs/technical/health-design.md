# Health Module Technical Design

## Overview

The health module provides a unified interface for application health checking and monitoring with support for both internal and external health checks. This design document outlines the architecture, interfaces, and implementation details for the health module.

## Goals

- Provide a consistent API for health checking
- Support both liveness and readiness probes
- Enable custom health checks for application components
- Support hierarchical health check organization
- Allow integration with monitoring systems
- Support automatic remediation actions
- Enable health check metrics collection
- Provide HTTP endpoints for health status
- Support dependency health monitoring
- Support customizable health check thresholds and timeouts

## Architecture

### Core Components

```plaintext
              +-----------------+
              |     Provider    |
              +-------+---------+
                      |
   +------------------+-------------------+
   |                  |                   |
+--+------+    +------+------+     +------+------+
| Checks  |    |  Registry   |     |  Reporter   |
+---------+    +-------------+     +-------------+
   |                  |                   |
   |                  |                   |
+--+------+    +------+------+     +------+------+
| Built-in/|   | Hierarchical|     | HTTP/Metric |
| Custom   |   | Organization|     | Output      |
+---------+    +-------------+     +-------------+
```

### Component Design

#### Provider Interface

The core of the module is the `Provider` interface, which defines the common operations for health check management.

#### Check Types

The module supports different types of health checks:

- **Liveness**: Indicates if the application is running (for auto-restart)
- **Readiness**: Indicates if the application can serve requests (for load balancing)
- **Component**: Check specific application components
- **Dependency**: Check external dependencies

#### Registry

The registry manages the registration and organization of health checks.

#### Reporter

The reporter handles reporting health check results through various channels (HTTP, metrics, etc.).

## Interface Design

### Provider

```go
// Provider represents a health check provider.
type Provider interface {
    // Register registers a health check.
    Register(name string, check Check, options ...CheckOption) error

    // Unregister removes a health check.
    Unregister(name string) error

    // Get retrieves a health check.
    Get(name string) (Check, bool)

    // CheckAll runs all health checks.
    CheckAll(ctx context.Context) (Result, error)

    // CheckLiveness runs liveness checks.
    CheckLiveness(ctx context.Context) (Result, error)

    // CheckReadiness runs readiness checks.
    CheckReadiness(ctx context.Context) (Result, error)

    // Handler returns an HTTP handler for health checks.
    Handler() http.Handler

    // Start starts background health checking.
    Start(ctx context.Context) error

    // Stop stops background health checking.
    Stop(ctx context.Context) error

    // AddListener adds a listener for health status changes.
    AddListener(listener Listener) error

    // RemoveListener removes a listener.
    RemoveListener(listener Listener) error
}
```

### Check

```go
// Check represents a health check.
type Check interface {
    // Execute runs the health check.
    Execute(ctx context.Context) (Result, error)

    // Name returns the check name.
    Name() string

    // Type returns the check type.
    Type() CheckType

    // Timeout returns the check timeout.
    Timeout() time.Duration

    // Interval returns the check interval.
    Interval() time.Duration

    // Enabled returns whether the check is enabled.
    Enabled() bool

    // SetEnabled sets whether the check is enabled.
    SetEnabled(enabled bool)
}
```

### Result

```go
// Result represents a health check result.
type Result interface {
    // Status returns the health status.
    Status() Status

    // Details returns the health details.
    Details() map[string]interface{}

    // Error returns the health check error.
    Error() error

    // Timestamp returns the check timestamp.
    Timestamp() time.Time

    // Duration returns the check duration.
    Duration() time.Duration

    // Check returns the check that produced this result.
    Check() Check

    // Children returns child results.
    Children() []Result

    // WithError sets an error for the result.
    WithError(err error) Result

    // WithDetails adds details to the result.
    WithDetails(details map[string]interface{}) Result
}
```

### Status

```go
// Status represents a health status.
type Status int

const (
    // StatusUp indicates the component is healthy.
    StatusUp Status = iota

    // StatusDown indicates the component is unhealthy.
    StatusDown

    // StatusDegraded indicates the component is partially healthy.
    StatusDegraded

    // StatusUnknown indicates the component health is unknown.
    StatusUnknown
)
```

### CheckType

```go
// CheckType represents a health check type.
type CheckType int

const (
    // TypeLiveness indicates a liveness check.
    TypeLiveness CheckType = iota

    // TypeReadiness indicates a readiness check.
    TypeReadiness

    // TypeComponent indicates a component check.
    TypeComponent

    // TypeDependency indicates a dependency check.
    TypeDependency
)
```

### Listener

```go
// Listener represents a health status change listener.
type Listener interface {
    // OnStatusChange is called when a health status changes.
    OnStatusChange(name string, previous, current Result)
}
```

## Configuration

### Config Structure

```go
// Config represents the health configuration.
type Config struct {
    // Enabled specifies whether health checking is enabled.
    Enabled bool

    // Endpoint is the HTTP endpoint for health checks.
    Endpoint string

    // CheckInterval is the interval for background health checking.
    CheckInterval time.Duration

    // DefaultTimeout is the default timeout for health checks.
    DefaultTimeout time.Duration

    // EnableLivenessEndpoint enables the liveness endpoint.
    EnableLivenessEndpoint bool

    // EnableReadinessEndpoint enables the readiness endpoint.
    EnableReadinessEndpoint bool

    // LivenessPath is the path for liveness checks.
    LivenessPath string

    // ReadinessPath is the path for readiness checks.
    ReadinessPath string

    // MetricsEnabled enables health check metrics.
    MetricsEnabled bool

    // LogStatusChanges indicates whether to log status changes.
    LogStatusChanges bool

    // AutoRemediationEnabled enables automatic remediation.
    AutoRemediationEnabled bool

    // RequireAuthentication requires authentication for detailed health checks.
    RequireAuthentication bool
}
```

## Implementation Details

### Built-in Health Checks

The module includes built-in health checks for:

#### System Checks

- **Memory**: Memory usage check
- **CPU**: CPU usage check
- **Disk**: Disk usage check
- **Goroutines**: Number of active goroutines
- **Uptime**: Application uptime

#### Dependency Checks

- **HTTP**: HTTP dependency check
- **TCP**: TCP connection check
- **Database**: Database connection check
- **Redis**: Redis connection check
- **GRPC**: gRPC service check

### Custom Health Checks

Custom health checks can be implemented by providing a function that returns a health status.

```go
func CustomCheck(ctx context.Context) (health.Result, error) {
    // Custom check logic
    if allOK {
        return health.NewResult(health.StatusUp), nil
    }
    return health.NewResult(health.StatusDown).WithError(errors.New("custom check failed")), nil
}
```

### Custom Health Check Examples

```go
// Register a custom health check
provider.Register("cache", health.CheckFunc(func(ctx context.Context) (health.Result, error) {
    if err := cacheClient.Ping(ctx); err != nil {
        return health.NewResult(health.StatusDown).WithError(err), nil
    }

    stats := cacheClient.Stats()
    return health.NewResult(health.StatusUp).WithDetails(map[string]interface{}{
        "hits":     stats.Hits,
        "misses":   stats.Misses,
        "hitRate":  stats.HitRate,
        "memoryUsage": stats.MemoryUsage,
    }), nil
}), health.WithType(health.TypeComponent))
```

### HTTP Endpoints

The health module provides HTTP endpoints for health status:

- **GET /health**: Overall health status
- **GET /health/live**: Liveness status
- **GET /health/ready**: Readiness status
- **GET /health/details**: Detailed health information (with auth)

### Metrics Integration

The health module integrates with the metrics module to provide:

- Health check status metrics
- Health check duration metrics
- Health check success/failure counts
- Health check status change counts

## Usage Examples

### Basic Usage

```go
config := health.Config{
    Enabled:        true,
    Endpoint:       "/health",
    CheckInterval:  30 * time.Second,
    DefaultTimeout: 5 * time.Second,
}

provider, err := health.NewProvider(config)
if err != nil {
    log.Fatal(err)
}

// Register a liveness check
provider.Register("process", health.NewProcessCheck(),
    health.WithType(health.TypeLiveness),
)

// Register a readiness check
provider.Register("database", health.NewDatabaseCheck(dbPool),
    health.WithType(health.TypeReadiness),
)

// Start background health checking
ctx := context.Background()
if err := provider.Start(ctx); err != nil {
    log.Fatal(err)
}
defer provider.Stop(ctx)

// Add to HTTP server
http.Handle("/health", provider.Handler())
```

### Custom Health Checks

```go
// Register a custom health check
provider.Register("cache", health.CheckFunc(func(ctx context.Context) (health.Result, error) {
    if err := cacheClient.Ping(ctx); err != nil {
        return health.NewResult(health.StatusDown).WithError(err), nil
    }

    stats := cacheClient.Stats()
    return health.NewResult(health.StatusUp).WithDetails(map[string]interface{}{
        "hits":     stats.Hits,
        "misses":   stats.Misses,
        "hitRate":  stats.HitRate,
        "memoryUsage": stats.MemoryUsage,
    }), nil
}), health.WithType(health.TypeComponent))
```

### Dependency Checks

```go
// Register a dependency HTTP check
provider.Register("auth-service", health.NewHTTPCheck("https://auth.example.com/health"),
    health.WithType(health.TypeDependency),
    health.WithTimeout(2*time.Second),
    health.WithInterval(1*time.Minute),
)

// Register a TCP check
provider.Register("redis", health.NewTCPCheck("redis.example.com:6379"),
    health.WithType(health.TypeDependency),
)
```

### Status Listeners

```go
// Create a status change listener
type statusLogger struct {
    logger log.Logger
}

func (s *statusLogger) OnStatusChange(name string, previous, current health.Result) {
    s.logger.Info("Health status changed",
        "check", name,
        "from", previous.Status(),
        "to", current.Status(),
        "details", current.Details(),
    )

    if current.Status() == health.StatusDown && previous.Status() != health.StatusDown {
        // Send alert
        s.logger.Error("Service is down", "check", name, "error", current.Error())
    }
}

// Register the listener
provider.AddListener(&statusLogger{logger: logger})
```

### Hierarchical Health Checks

```go
// Create a composite health check
databaseCheck := health.NewCompositeCheck("database")

// Add child checks
databaseCheck.AddChecks(
    health.NewDatabaseConnectionCheck(dbPool),
    health.NewDatabaseQueryCheck(dbPool, "SELECT 1"),
    health.NewDatabaseLatencyCheck(dbPool),
)

// Register the composite check
provider.Register("database", databaseCheck, health.WithType(health.TypeReadiness))
```

### Auto-Remediation

```go
// Register a check with auto-remediation
provider.Register("connection-pool", health.NewDatabaseConnectionCheck(dbPool),
    health.WithType(health.TypeComponent),
    health.WithRemediation(func(ctx context.Context, result health.Result) error {
        log.Info("Resetting database connection pool due to health check failure")
        return dbPool.Reset()
    }),
)
```

## Testing Strategy

- Unit tests for each health check implementation
- Integration tests for dependency checks
- Mock implementations for testing
- Benchmarks for performance measurement

## Security Considerations

- Authentication for detailed health endpoints
- Information disclosure in health check details
- Resource usage of health checks
- Rate limiting for health endpoints

## Performance Considerations

- Asynchronous health check execution
- Caching of health check results
- Timeouts for all checks
- Resource usage monitoring
- Concurrency control for parallel checks
- Circuit breaking for failing dependencies
