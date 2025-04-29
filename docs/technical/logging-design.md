# Logging Module Technical Design

## Overview

The logging module provides a unified interface for logging across various backends, with support for structured logging, different log levels, and contextual information. This design document outlines the architecture, interfaces, and implementation details for the logging module.

## Goals

- Provide a consistent API across different logging backends
- Support structured logging with fields
- Enable contextual logging with correlation IDs
- Allow for runtime configuration of log levels
- Support different output formats (JSON, text)
- Enable integration with other modules (e.g., metrics)
- Minimize performance impact of logging
- Support log rotation and management

## Architecture

### Core Components

```text
              +-----------------+
              |     Logger      |
              +--------+--------+
                       |
    +------------------+-------------------+
    |                  |                   |
+---+----+      +------+------+      +-----+-----+
| Levels |      | Formatters  |      |  Outputs  |
+--------+      +-------------+      +-----------+
```

### Component Design

#### Logger Interface

The core of the module is the `Logger` interface, which defines the common operations for logging.

#### Log Levels

The module supports the following log levels:
- **Debug**: Detailed information for debugging
- **Info**: General operational information
- **Warn**: Warning events that might need attention
- **Error**: Error events that might still allow the application to continue
- **Fatal**: Very severe error events that will lead the application to abort

#### Formatters

Formatters define how log entries are formatted:
- **Text**: Human-readable format
- **JSON**: Machine-parseable format
- **Custom**: User-defined formats

#### Outputs

Outputs define where logs are sent:
- **Console**: Standard output/error
- **File**: Local file system
- **Remote**: Remote logging systems (e.g., syslog)

## Interface Design

### Logger

```go
// Logger represents a logger.
type Logger interface {
    // Debug logs a debug message.
    Debug(msg string, fields ...Field)

    // Info logs an info message.
    Info(msg string, fields ...Field)

    // Warn logs a warning message.
    Warn(msg string, fields ...Field)

    // Error logs an error message.
    Error(msg string, fields ...Field)

    // Fatal logs a fatal message and exits.
    Fatal(msg string, fields ...Field)

    // With creates a new logger with the given fields.
    With(fields ...Field) Logger

    // WithContext creates a new logger with the given context.
    WithContext(ctx context.Context) Logger

    // SetLevel sets the logging level.
    SetLevel(level Level)

    // GetLevel returns the current logging level.
    GetLevel() Level
}
```

### Field

```go
// Field represents a log field.
type Field struct {
    Key   string
    Value interface{}
}
```

### Level

```go
// Level represents a logging level.
type Level int

const (
    // DebugLevel is the lowest level, used for debugging.
    DebugLevel Level = iota

    // InfoLevel is for general operational information.
    InfoLevel

    // WarnLevel is for warning events.
    WarnLevel

    // ErrorLevel is for error events.
    ErrorLevel

    // FatalLevel is for very severe error events.
    FatalLevel
)
```

### Provider

```go
// Provider represents a logger provider.
type Provider interface {
    // NewLogger creates a new logger.
    NewLogger(name string) Logger

    // Configure configures the logger.
    Configure(config Config) error

    // Flush ensures all logs are written.
    Flush() error
}
```

## Configuration

### Config Structure

```go
// Config represents the logging configuration.
type Config struct {
    // Level is the minimum level to log.
    Level string

    // Format is the log format (text, json).
    Format string

    // OutputPaths are the paths to write logs to.
    OutputPaths []string

    // ErrorOutputPaths are the paths to write errors to.
    ErrorOutputPaths []string

    // Development enables development mode.
    Development bool

    // Sampling configures log sampling.
    Sampling *SamplingConfig

    // Encoding configures log encoding.
    Encoding EncodingConfig

    // DisableCaller disables caller information.
    DisableCaller bool

    // DisableStacktrace disables stacktrace capture.
    DisableStacktrace bool

    // AddSource adds source code information.
    AddSource bool
}

// SamplingConfig configures log sampling.
type SamplingConfig struct {
    // Initial is the initial sampling rate.
    Initial int

    // Thereafter is the sampling rate thereafter.
    Thereafter int
}

// EncodingConfig configures log encoding.
type EncodingConfig struct {
    // TimeKey is the key for timestamps.
    TimeKey string

    // LevelKey is the key for log levels.
    LevelKey string

    // NameKey is the key for logger names.
    NameKey string

    // CallerKey is the key for caller information.
    CallerKey string

    // MessageKey is the key for log messages.
    MessageKey string

    // StacktraceKey is the key for error stacktraces.
    StacktraceKey string

    // TimeFormat is the format for timestamps.
    TimeFormat string
}
```

## Implementation Details

### Standard Library Implementation

The standard library implementation uses the built-in `log` package and provides a lightweight logging solution with basic functionality.

### Zap Implementation

The Zap implementation uses uber-go/zap, which offers high-performance, structured logging with minimal allocations.

### Logrus Implementation

The Logrus implementation uses sirupsen/logrus, which provides structured logging with hooks and a more traditional interface.

### Context Integration

The context integration allows for propagating logging information through the call stack, including:

- Request IDs
- User information
- Session information
- Correlation IDs

### Error Handling

The error handling includes:

- Structured error logging
- Stacktrace capture
- Error wrapping with context
- Error classification

## Usage Examples

### Basic Logging

```go
config := log.Config{
    Level:       "info",
    Format:      "json",
    OutputPaths: []string{"stdout", "/var/log/app.log"},
}

provider, err := log.NewProvider(config)
if err != nil {
    panic(err)
}

logger := provider.NewLogger("app")

logger.Info("Application started", log.String("version", "1.0.0"))
logger.Debug("Debug information", log.Int("connections", 10))
logger.Error("Failed to connect", log.Error(err))
```

### Contextual Logging

```go
func handleRequest(ctx context.Context, logger log.Logger, req *http.Request) {
    // Extract request ID from request or generate a new one
    requestID := req.Header.Get("X-Request-ID")
    if requestID == "" {
        requestID = uuid.New().String()
    }

    // Create a context-aware logger
    ctxLogger := logger.With(log.String("request_id", requestID))

    // Add to context
    ctx = log.ContextWithLogger(ctx, ctxLogger)

    // Use throughout request handling
    ctxLogger.Info("Request received", log.String("path", req.URL.Path))

    // Process request...

    ctxLogger.Info("Request completed", log.Int("status", 200))
}
```

### Integration with HTTP Handlers

```go
func loggingMiddleware(logger log.Logger) func(http.Handler) http.Handler {
    return func(next http.Handler) http.Handler {
        return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
            // Extract or generate request ID
            requestID := r.Header.Get("X-Request-ID")
            if requestID == "" {
                requestID = uuid.New().String()
            }

            // Create request-specific logger
            reqLogger := logger.With(
                log.String("request_id", requestID),
                log.String("method", r.Method),
                log.String("path", r.URL.Path),
                log.String("remote_addr", r.RemoteAddr),
                log.String("user_agent", r.UserAgent()),
            )

            // Add logger to context
            ctx := log.ContextWithLogger(r.Context(), reqLogger)

            // Record start time
            start := time.Now()

            // Create response wrapper to capture status code
            ww := middleware.NewWrapResponseWriter(w, r.ProtoMajor)

            // Process request
            next.ServeHTTP(ww, r.WithContext(ctx))

            // Log request completion
            duration := time.Since(start)
            reqLogger.Info("Request completed",
                log.Int("status", ww.Status()),
                log.Int("bytes", ww.BytesWritten()),
                log.Duration("duration", duration),
            )
        })
    }
}
```

### Structured Logging with Contextual Data

```go
func processItem(ctx context.Context, item *Item) error {
    // Get logger from context
    logger := log.FromContext(ctx)
    if logger == nil {
        logger = defaultLogger
    }

    // Add item-specific fields
    itemLogger := logger.With(log.String("item_id", item.ID))

    itemLogger.Debug("Processing item", log.String("type", item.Type))

    // Process item...

    if err != nil {
        itemLogger.Error("Failed to process item",
            log.Error(err),
            log.String("step", "validation"),
        )
        return err
    }

    itemLogger.Info("Item processed successfully",
        log.Duration("process_time", time.Since(start)),
    )
    return nil
}
```

## Field Constructors

The module provides helper functions for creating structured log fields:

```go
// String creates a string field.
func String(key, value string) Field

// Int creates an int field.
func Int(key string, value int) Field

// Int64 creates an int64 field.
func Int64(key string, value int64) Field

// Float64 creates a float64 field.
func Float64(key string, value float64) Field

// Bool creates a bool field.
func Bool(key string, value bool) Field

// Time creates a time field.
func Time(key string, value time.Time) Field

// Duration creates a duration field.
func Duration(key string, value time.Duration) Field

// Any creates a field with any value.
func Any(key string, value interface{}) Field

// Error creates an error field.
func Error(err error) Field

// Stack creates a stacktrace field.
func Stack() Field
```

## Testing Strategy

- Unit tests for each logger implementation
- Integration tests for context propagation
- Benchmarks for performance measurement
- Mock implementations for higher-level tests

## Security Considerations

- Sensitive data handling (redaction, masking)
- Log file permissions and access controls
- Logging infrastructure security
- PII and compliance considerations

## Performance Considerations

- Efficient structured logging with minimal allocations
- Log level filtering at the source
- Asynchronous logging where appropriate
- Buffer management and flushing strategies
- Sampling for high-volume logs
