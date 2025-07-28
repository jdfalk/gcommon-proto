// file: pkg/log/interfaces.go

package log

import (
	"context"
	"io"
)

// Logger defines the interface for structured logging across GCommon modules
type Logger interface {
	// Debug logs debug-level messages
	Debug(msg string, fields ...Field)
	DebugContext(ctx context.Context, msg string, fields ...Field)

	// Info logs info-level messages
	Info(msg string, fields ...Field)
	InfoContext(ctx context.Context, msg string, fields ...Field)

	// Warn logs warning-level messages
	Warn(msg string, fields ...Field)
	WarnContext(ctx context.Context, msg string, fields ...Field)

	// Error logs error-level messages
	Error(msg string, fields ...Field)
	ErrorContext(ctx context.Context, msg string, fields ...Field)

	// Fatal logs fatal-level messages and exits
	Fatal(msg string, fields ...Field)
	FatalContext(ctx context.Context, msg string, fields ...Field)

	// With returns a new logger with additional fields
	With(fields ...Field) Logger

	// WithContext returns a new logger with context
	WithContext(ctx context.Context) Logger

	// SetLevel sets the logging level
	SetLevel(level Level)

	// GetLevel returns the current logging level
	GetLevel() Level
}

// Provider defines the interface for log providers
type Provider interface {
	Logger

	// Name returns the provider name
	Name() string

	// Close closes the provider and flushes any pending logs
	Close() error

	// Sync ensures all logs are written
	Sync() error

	// SetOutput sets the output destination
	SetOutput(w io.Writer)

	// AddHook adds a logging hook
	AddHook(hook Hook) error
}

// Hook defines the interface for logging hooks
type Hook interface {
	// Levels returns the log levels this hook is interested in
	Levels() []Level

	// Fire is called when a log entry matches the hook's levels
	Fire(entry Entry) error
}

// Entry represents a log entry
type Entry interface {
	// Level returns the log level
	Level() Level

	// Message returns the log message
	Message() string

	// Fields returns the log fields
	Fields() map[string]interface{}

	// Time returns the log timestamp
	Time() int64

	// Context returns the log context
	Context() context.Context
}

// Field represents a structured log field
type Field struct {
	Key   string
	Value interface{}
}

// Level represents logging levels
type Level int

const (
	DebugLevel Level = iota
	InfoLevel
	WarnLevel
	ErrorLevel
	FatalLevel
)

// String returns the string representation of the level
func (l Level) String() string {
	switch l {
	case DebugLevel:
		return "debug"
	case InfoLevel:
		return "info"
	case WarnLevel:
		return "warn"
	case ErrorLevel:
		return "error"
	case FatalLevel:
		return "fatal"
	default:
		return "unknown"
	}
}

// Config represents the logging configuration.
type Config struct {
	// Provider specifies the logging provider to use.
	// Supported values: "std", "zap", "logrus", "multi", "noop"
	Provider string

	// Level is the minimum log level.
	Level string

	// Format is the log format. Supported values: "json", "text", "console"
	Format string

	// TimeFormat is the time format for log timestamps.
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
	EncoderConfig interface{}
}

// LogrusConfig represents Logrus-specific configuration.
type LogrusConfig struct {
	// ReportCaller enables caller reporting.
	ReportCaller bool

	// ExitFunc is the exit function for Fatal logs.
	ExitFunc func(int)

	// Hooks are the logrus hooks.
	Hooks []interface{}
}
