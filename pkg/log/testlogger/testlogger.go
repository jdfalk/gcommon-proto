// file: pkg/log/testlogger/testlogger.go
// version: 1.0.0
// guid: 12c89763-a62a-4ce2-9cf4-f89ba0cbf7e7

package testlogger

import (
	"context"
	"sync"

	"github.com/jdfalk/gcommon/pkg/log"
)

// Entry represents a recorded log entry for verification in tests.
type Entry struct {
	Level   log.Level
	Message string
	Fields  []log.Field
}

// Logger implements log.Logger and records all log entries.
type Logger struct {
	mu      sync.Mutex
	entries *[]Entry
	base    []log.Field
	level   log.Level
}

// New creates a new test logger with DebugLevel by default.
func New() *Logger {
	e := []Entry{}
	return &Logger{level: log.DebugLevel, entries: &e}
}

// Entries returns a copy of all recorded log entries.
func (l *Logger) Entries() []Entry {
	l.mu.Lock()
	defer l.mu.Unlock()
	out := make([]Entry, len(*l.entries))
	copy(out, *l.entries)
	return out
}

// record adds a log entry if the level is enabled.
func (l *Logger) record(level log.Level, msg string, fields []log.Field) {
	if level < l.level {
		return
	}
	l.mu.Lock()
	combined := append(append([]log.Field(nil), l.base...), fields...)
	*l.entries = append(*l.entries, Entry{Level: level, Message: msg, Fields: combined})
	l.mu.Unlock()
}

// Debug logs a debug message.
func (l *Logger) Debug(msg string, fields ...log.Field) { l.record(log.DebugLevel, msg, fields) }

// DebugContext logs a debug message with context.
func (l *Logger) DebugContext(ctx context.Context, msg string, fields ...log.Field) {
	l.Debug(msg, fields...)
}

// Info logs an info message.
func (l *Logger) Info(msg string, fields ...log.Field) { l.record(log.InfoLevel, msg, fields) }

// InfoContext logs an info message with context.
func (l *Logger) InfoContext(ctx context.Context, msg string, fields ...log.Field) {
	l.Info(msg, fields...)
}

// Warn logs a warning message.
func (l *Logger) Warn(msg string, fields ...log.Field) { l.record(log.WarnLevel, msg, fields) }

// WarnContext logs a warning message with context.
func (l *Logger) WarnContext(ctx context.Context, msg string, fields ...log.Field) {
	l.Warn(msg, fields...)
}

// Error logs an error message.
func (l *Logger) Error(msg string, fields ...log.Field) { l.record(log.ErrorLevel, msg, fields) }

// ErrorContext logs an error message with context.
func (l *Logger) ErrorContext(ctx context.Context, msg string, fields ...log.Field) {
	l.Error(msg, fields...)
}

// Fatal logs a fatal message. The test logger does not exit.
func (l *Logger) Fatal(msg string, fields ...log.Field) { l.record(log.FatalLevel, msg, fields) }

// FatalContext logs a fatal message with context.
func (l *Logger) FatalContext(ctx context.Context, msg string, fields ...log.Field) {
	l.Fatal(msg, fields...)
}

// With returns a new logger carrying additional base fields.
func (l *Logger) With(fields ...log.Field) log.Logger {
	nl := *l
	nl.base = append(append([]log.Field(nil), l.base...), fields...)
	return &nl
}

// WithContext returns the same logger for context compatibility.
func (l *Logger) WithContext(ctx context.Context) log.Logger { return l }

// SetLevel sets the active log level.
func (l *Logger) SetLevel(level log.Level) { l.level = level }

// GetLevel returns the current log level.
func (l *Logger) GetLevel() log.Level { return l.level }
