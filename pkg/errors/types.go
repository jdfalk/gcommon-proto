// file: pkg/errors/types.go
// version: 1.1.0
// guid: 37832aac-5f14-4afb-a369-4f83256e11b6

package errors

import (
	"fmt"
	"runtime"
)

// Error is the base interface for all gcommon errors with rich context.
type Error interface {
	error
	Code() ErrorCode
	Component() string
	Operation() string
	Details() map[string]interface{}
	Cause() error
	Stack() []string
	Temporary() bool
	Retryable() bool
}

// BaseError provides a default implementation of the Error interface.
type BaseError struct {
	code      ErrorCode
	component string
	operation string
	message   string
	details   map[string]interface{}
	cause     error
	stack     []string
	temporary bool
	retryable bool
}

// Error implements the error interface.
func (e *BaseError) Error() string {
	return e.message
}

// Code returns the error code.
func (e *BaseError) Code() ErrorCode {
	return e.code
}

// Component returns the component where the error originated.
func (e *BaseError) Component() string {
	return e.component
}

// Operation returns the operation that failed.
func (e *BaseError) Operation() string {
	return e.operation
}

// Details returns additional error details.
func (e *BaseError) Details() map[string]interface{} {
	return e.details
}

// Cause returns the underlying error cause.
func (e *BaseError) Cause() error {
	return e.cause
}

// Stack returns the stack trace at error creation.
func (e *BaseError) Stack() []string {
	return e.stack
}

// Temporary reports whether the error is temporary.
func (e *BaseError) Temporary() bool {
	return e.temporary
}

// Retryable reports whether the operation may be retried.
func (e *BaseError) Retryable() bool {
	return e.retryable
}

// newBaseError creates a BaseError with captured stack information.
func newBaseError(code ErrorCode, component, operation, message string) *BaseError {
	return &BaseError{
		code:      code,
		component: component,
		operation: operation,
		message:   message,
		details:   map[string]interface{}{},
		stack:     captureStack(),
	}
}

// captureStack records the current call stack as a slice of strings.
func captureStack() []string {
	const depth = 32
	pcs := make([]uintptr, depth)
	n := runtime.Callers(3, pcs)
	frames := runtime.CallersFrames(pcs[:n])
	stack := make([]string, 0, n)
	for {
		frame, more := frames.Next()
		stack = append(stack, fmt.Sprintf("%s:%d", frame.Function, frame.Line))
		if !more {
			break
		}
	}
	return stack
}

// ConfigError represents configuration-related failures.
type ConfigError struct {
	BaseError
	ConfigKey   string
	ConfigValue interface{}
}

// NewConfigError constructs a ConfigError.
func NewConfigError(code ErrorCode, key string, value interface{}, message string) *ConfigError {
	return &ConfigError{
		BaseError:   *newBaseError(code, "config", "", message),
		ConfigKey:   key,
		ConfigValue: value,
	}
}

// QueueError represents queue processing failures.
type QueueError struct {
	BaseError
	QueueName string
	MessageID string
}

// NewQueueError constructs a QueueError.
func NewQueueError(code ErrorCode, queue, msgID, message string) *QueueError {
	return &QueueError{
		BaseError: *newBaseError(code, "queue", "", message),
		QueueName: queue,
		MessageID: msgID,
	}
}

// AuthError represents authentication and authorization failures.
type AuthError struct {
	BaseError
	UserID   string
	Resource string
	Action   string
}

// NewAuthError constructs an AuthError.
func NewAuthError(code ErrorCode, userID, resource, action, message string) *AuthError {
	return &AuthError{
		BaseError: *newBaseError(code, "auth", "", message),
		UserID:    userID,
		Resource:  resource,
		Action:    action,
	}
}

// MetricsError represents metric collection and export failures.
type MetricsError struct {
	BaseError
	MetricName string
}

// NewMetricsError constructs a MetricsError.
func NewMetricsError(code ErrorCode, metric, message string) *MetricsError {
	return &MetricsError{
		BaseError:  *newBaseError(code, "metrics", "", message),
		MetricName: metric,
	}
}

// CacheError represents cache access failures.
type CacheError struct {
	BaseError
	Key string
}

// NewCacheError constructs a CacheError.
func NewCacheError(code ErrorCode, key, message string) *CacheError {
	return &CacheError{
		BaseError: *newBaseError(code, "cache", "", message),
		Key:       key,
	}
}

// WebError represents web module failures.
type WebError struct {
	BaseError
	Route string
}

// NewWebError constructs a WebError.
func NewWebError(code ErrorCode, route, message string) *WebError {
	return &WebError{
		BaseError: *newBaseError(code, "web", "", message),
		Route:     route,
	}
}

// DBError represents database query failures.
type DBError struct {
	BaseError
	Query string
}

// NewDBError constructs a DBError.
func NewDBError(code ErrorCode, query, message string) *DBError {
	return &DBError{
		BaseError: *newBaseError(code, "db", "", message),
		Query:     query,
	}
}

// LogError represents logging failures.
type LogError struct {
	BaseError
	Logger string
}

// NewLogError constructs a LogError.
func NewLogError(code ErrorCode, logger, message string) *LogError {
	return &LogError{
		BaseError: *newBaseError(code, "log", "", message),
		Logger:    logger,
	}
}
