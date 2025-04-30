# Logging Module Technical Design

## Overview

The logging module provides a unified interface for application logging with support for multiple logging backends. This design document outlines the architecture, interfaces, and implementation details for the logging module.

## Goals

- Provide a consistent API for logging across applications
- Support multiple logging backends (standard library, zap, logrus, etc.)
- Enable structured logging with key-value pairs
- Support multiple log levels with fine-grained control
- Allow context-aware logging
- Enable log rotation and management
- Support log output to multiple destinations
- Provide performance optimized logging
- Enable correlation of logs across services
- Support custom log formatters and hooks

## Architecture

### Core Components

```
              +------------------+
              |     Logger       |
              +--------+---------+
                       |
   +------------------+-------------------+
   |                  |                   |
+--+------+    +------+------+     +------+------+
|Providers|    | Formatters  |     |  Writers    |
+---------+    +-------------+     +-------------+
   |                  |                   |
   |                  |                   |
+--+------+    +------+------+     +------+------+
| Std/Zap/|    |JSON/Text/   |     |File/Console/|
| Logrus  |    |Custom       |     |Remote/etc   |
+---------+    +-------------+     +-------------+
```

### Component Design

#### Logger Interface

The core of the module is the `Logger` interface, which defines the common operations for logging.

#### Providers

Providers implement the `Logger` interface for different logging backends:
- **Standard**: Go standard library logger
- **Zap**: High-performance structured logging
- **Logrus**: Feature-rich structured logging
- **Multi**: Sends logs to multiple providers
- **Noop**: No-operation logger for testing

#### Formatters

Formatters handle the conversion of log entries to output formats:
- **Text**: Human-readable text format
- **JSON**: Machine-readable JSON format
- **Console**: Colored console output
- **Custom**: Custom formatters for specific needs

#### Writers

Writers handle the destination of log output:
- **Console**: Standard output/error streams
- **File**: Local file system
- **Rotating**: File rotation based on size or time
- **Remote**: HTTP, syslog, or other remote endpoints
- **Buffer**: In-memory buffered logging

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

    // WithFields returns a logger with the given fields.
    WithFields(fields ...Field) Logger

    // WithContext returns a logger with the given context.
    WithContext(ctx context.Context) Logger

    // WithLevel returns a logger with the given level.
    WithLevel(level Level) Logger

    // GetLevel returns the logger level.
    GetLevel() Level

    // SetLevel sets the logger level.
    SetLevel(level Level)

    // Sync flushes buffered logs.
    Sync() error

    // Writer returns a writer for the given level.
    Writer(level Level) io.Writer
}
```

### Field

```go
// Field represents a log field.
type Field struct {
    // Key is the field key.
    Key string

    // Value is the field value.
    Value interface{}
}
```

### Level

```go
// Level represents a log level.
type Level int

const (
    // DebugLevel is the debug log level.
    DebugLevel Level = iota

    // InfoLevel is the info log level.
    InfoLevel

    // WarnLevel is the warn log level.
    WarnLevel

    // ErrorLevel is the error log level.
    ErrorLevel

    // FatalLevel is the fatal log level.
    FatalLevel
)
```

### Provider

```go
// Provider represents a logger provider.
type Provider interface {
    // GetLogger returns a logger.
    GetLogger(name string) Logger

    // SetLevel sets the level for all loggers.
    SetLevel(level Level)

    // Close closes the provider.
    Close() error
}
```

## Configuration

### Config Structure

```go
// Config represents the logging configuration.
type Config struct {
    // Provider specifies the logging provider to use.
    // Supported values: "std", "zap", "logrus", "multi", "noop"
    Provider string

    // Level is the minimum log level.
    Level string

    // Format is the log format.
    // Supported values: "json", "text", "console"
    Format string

    // TimeFormat is the time format.
    TimeFormat string

    // CallerReportingEnabled enables caller reporting.
    CallerReportingEnabled bool

    // CallerSkipFrames is the number of frames to skip when reporting callers.
    CallerSkipFrames int

    // StackTraceEnabled enables stack trace reporting.
    StackTraceEnabled bool

    // StackTraceLevel is the minimum level for stack traces.
    StackTraceLevel string

    // Fields are the default fields for all logs.
    Fields map[string]interface{}

    // OutputPaths are the output paths.
    OutputPaths []string

    // ErrorOutputPaths are the error output paths.
    ErrorOutputPaths []string

    // FileConfig contains file-specific configuration.
    FileConfig *FileConfig

    // ZapConfig contains Zap-specific configuration.
    ZapConfig *ZapConfig

    // LogrusConfig contains Logrus-specific configuration.
    LogrusConfig *LogrusConfig
}

// FileConfig represents file-specific configuration.
type FileConfig struct {
    // Path is the file path.
    Path string

    // RotationMaxSize is the maximum file size in megabytes.
    RotationMaxSize int

    // RotationMaxAge is the maximum file age in days.
    RotationMaxAge int

    // RotationMaxBackups is the maximum number of backups.
    RotationMaxBackups int

    // RotationCompress enables compression of rotated files.
    RotationCompress bool

    // RotationLocalTime uses local time for rotation.
    RotationLocalTime bool
}

// ZapConfig represents Zap-specific configuration.
type ZapConfig struct {
    // Development enables development mode.
    Development bool

    // Sampling enables sampling.
    Sampling bool

    // SamplingInitial is the initial sampling rate.
    SamplingInitial int

    // SamplingThereafter is the sampling rate thereafter.
    SamplingThereafter int

    // EncoderConfig is the encoder configuration.
    EncoderConfig *zapcore.EncoderConfig
}

// LogrusConfig represents Logrus-specific configuration.
type LogrusConfig struct {
    // ReportCaller enables caller reporting.
    ReportCaller bool

    // ExitFunc is the exit function for Fatal logs.
    ExitFunc func(int)

    // Hooks are the logrus hooks.
    Hooks []logrus.Hook
}
```

## Implementation Details

### Standard Library Implementation

The standard library implementation uses the `log` package with custom formatting to match the structured logging interface.

### Zap Implementation

The Zap implementation uses the `go.uber.org/zap` package, which provides high-performance, structured logging.

### Logrus Implementation

The Logrus implementation uses the `github.com/sirupsen/logrus` package, which provides feature-rich structured logging.

### Context Integration

The logging module integrates with the Go context package to allow for context-aware logging, including trace identifiers and other contextual information.

### Performance Considerations

The module uses various techniques to ensure high-performance logging:
- Zero-allocation logging when possible
- Level checking before formatting
- Buffered I/O
- Asynchronous logging options
- Sampling for high-volume logs

## Usage Examples

### Basic Usage

```go
config := log.Config{
    Provider:   "zap",
    Level:      "info",
    Format:     "json",
    TimeFormat: time.RFC3339,
    Fields: map[string]interface{}{
        "service": "api",
        "version": "1.0.0",
    },
    OutputPaths: []string{"stdout", "file:/var/log/myapp.log"},
}

provider, err := log.NewProvider(config)
if err != nil {
    panic(err)
}
defer provider.Close()

logger := provider.GetLogger("main")

logger.Info("Server starting", log.String("addr", ":8080"))

// Later...
logger.Error("Failed to process request",
    log.String("method", "GET"),
    log.String("path", "/users"),
    log.Int("status", 500),
    log.Error(err),
)
```

### Structured Logging

```go
// Create fields
userID := log.String("user_id", "123")
requestID := log.String("request_id", "abc-456")
duration := log.Duration("duration", time.Millisecond * 42)

// Log with fields
logger.Info("Request processed", userID, requestID, duration)

// Use fluent API
logger.WithFields(userID, requestID).Info("User authenticated")
```

### Levels

```go
// Check if level is enabled before expensive operations
if logger.GetLevel() <= log.DebugLevel {
    details := expensiveOperation()
    logger.Debug("Operation details", log.Any("details", details))
}

// Create a logger with a specific level
debugLogger := logger.WithLevel(log.DebugLevel)
infoLogger := logger.WithLevel(log.InfoLevel)

// Only logs if the logger level is set accordingly
debugLogger.Debug("This may or may not appear")
infoLogger.Info("This will appear if level is info or lower")
```

### Context-Aware Logging

```go
// Create a context with values
ctx := context.Background()
ctx = log.ContextWithRequestID(ctx, "req-123")
ctx = log.ContextWithUserID(ctx, "user-456")

// Get a logger with context
ctxLogger := logger.WithContext(ctx)

// Logs automatically include context values
ctxLogger.Info("Processing request")
// Output includes request_id=req-123 user_id=user-456
```

### HTTP Request Logging

```go
// Create an HTTP middleware that logs requests
func LogMiddleware(logger log.Logger) func(http.Handler) http.Handler {
    return func(next http.Handler) http.Handler {
        return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
            start := time.Now()

            // Extract request ID from header or generate a new one
            requestID := r.Header.Get("X-Request-ID")
            if requestID == "" {
                requestID = uuid.New().String()
                r.Header.Set("X-Request-ID", requestID)
            }

            // Create a context with the request ID
            ctx := log.ContextWithRequestID(r.Context(), requestID)
            r = r.WithContext(ctx)

            // Use a response wrapper to capture status code
            ww := newWrappedResponseWriter(w)

            // Pre-request logging
            logger.WithContext(ctx).Info("Request started",
                log.String("method", r.Method),
                log.String("path", r.URL.Path),
                log.String("remote_addr", r.RemoteAddr),
            )

            // Call the next handler
            next.ServeHTTP(ww, r)

            // Post-request logging
            logger.WithContext(ctx).Info("Request completed",
                log.String("method", r.Method),
                log.String("path", r.URL.Path),
                log.Int("status", ww.statusCode),
                log.Duration("duration", time.Since(start)),
                log.Int("bytes", ww.bytesWritten),
            )
        })
    }
}

// Use the middleware
http.Handle("/", LogMiddleware(logger)(myHandler))
```

### File Rotation

```go
config := log.Config{
    Provider: "zap",
    Level:    "info",
    Format:   "json",
    FileConfig: &log.FileConfig{
        Path:              "/var/log/myapp.log",
        RotationMaxSize:   10, // 10 MB
        RotationMaxAge:    7,  // 7 days
        RotationMaxBackups: 5,  // Keep 5 backups
        RotationCompress:  true,
        RotationLocalTime: true,
    },
}

provider, err := log.NewProvider(config)
if err != nil {
    panic(err)
}
defer provider.Close()

logger := provider.GetLogger("main")
```

### Multiple Outputs

```go
config := log.Config{
    Provider: "zap",
    Level:    "info",
    Format:   "json",
    OutputPaths: []string{
        "stdout",
        "file:/var/log/myapp.log",
        "syslog://local0",
    },
    ErrorOutputPaths: []string{
        "stderr",
        "file:/var/log/myapp.error.log",
    },
}

provider, err := log.NewProvider(config)
if err != nil {
    panic(err)
}

logger := provider.GetLogger("main")
```

### Custom Hooks (Logrus Example)

```go
// Create a custom hook
type MetricsHook struct {
    metrics metrics.Provider
}

func (h *MetricsHook) Levels() []logrus.Level {
    return []logrus.Level{
        logrus.WarnLevel,
        logrus.ErrorLevel,
        logrus.FatalLevel,
    }
}

func (h *MetricsHook) Fire(entry *logrus.Entry) error {
    level := entry.Level.String()
    h.metrics.Counter("log_entries_total").
        WithTags(metrics.Tag{Key: "level", Value: level}).
        Inc()
    return nil
}

// Configure logger with the hook
config := log.Config{
    Provider: "logrus",
    LogrusConfig: &log.LogrusConfig{
        Hooks: []logrus.Hook{
            &MetricsHook{metrics: metricsProvider},
        },
    },
}

provider, err := log.NewProvider(config)
if err != nil {
    panic(err)
}

logger := provider.GetLogger("main")
```

### Integration with Other Modules

```go
// Database integration
db, err := database.Open(dbConfig)
if err != nil {
    logger.Fatal("Failed to connect to database", log.Error(err))
}

// Configure database to use the logger
db.SetLogger(logger.WithFields(log.String("component", "database")))

// HTTP server integration
server := &http.Server{
    Addr:     ":8080",
    Handler:  handlers,
    ErrorLog: log.NewStdLogAdapter(logger.WithFields(log.String("component", "http"))),
}
```

## Testing Strategy

- Unit tests for each logger implementation
- Integration tests with actual backends
- Performance benchmarks for logging operations
- Concurrency tests for thread safety
- Mock loggers for testing application code

## Security Considerations

- Sensitive data masking in logs
- Log access control
- Tamper-evident logging
- Secure transmission of logs
- Proper handling of errors and exceptions
- Protection against log injection

## Performance Considerations

- Level filtering before formatting
- Field allocation optimization
- Buffered writes
- Asynchronous logging options
- Log sampling for high-volume environments
- Minimal allocations in hot paths
- Efficient serialization of structured data
