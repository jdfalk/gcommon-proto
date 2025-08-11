// file: monitoring/collectors/logs.go
// version: 1.1.0
// guid: 47a7ce9e-1c6f-4c57-a3fb-9a93c9a4b6df

package collectors

import (
	"context"
	"fmt"
	"io"
	"log"
	"sync"
	"time"
)

// LogLevel represents the severity of a log message.
type LogLevel string

// Predefined log levels.
const (
	LevelDebug LogLevel = "DEBUG"
	LevelInfo  LogLevel = "INFO"
	LevelWarn  LogLevel = "WARN"
	LevelError LogLevel = "ERROR"
)

// LogEntry represents a structured log event captured by the collector.
type LogEntry struct {
	Timestamp time.Time      // Time the log was recorded
	Level     LogLevel       // Severity level
	Message   string         // Log message
	Fields    map[string]any // Additional contextual fields
}

// LogsCollector provides a fan-out log dispatcher. Components emit logs to the
// collector which can then forward them to multiple subscribers for processing
// or export.
type LogsCollector struct {
	mu          sync.RWMutex
	subscribers []chan LogEntry
	ch          chan LogEntry
	wg          sync.WaitGroup
	closed      bool
}

// NewLogsCollector creates a new collector with the given buffer size for the
// internal channel.
func NewLogsCollector(buffer int) *LogsCollector {
	return &LogsCollector{ch: make(chan LogEntry, buffer)}
}

// Start begins a goroutine that fan-outs log entries to all active subscribers.
// It should be called once and will run until the provided context is cancelled
// or the collector is closed.
func (l *LogsCollector) Start(ctx context.Context) {
	l.wg.Add(1)
	go func() {
		defer l.wg.Done()
		for {
			select {
			case <-ctx.Done():
				return
			case entry, ok := <-l.ch:
				if !ok {
					return
				}
				l.mu.RLock()
				for _, sub := range l.subscribers {
					select {
					case sub <- entry:
					default:
						// Drop logs if subscriber is slow.
					}
				}
				l.mu.RUnlock()
			}
		}
	}()
}

// Subscribe registers a new subscriber channel that will receive log entries.
// The returned channel will be closed when the collector is closed.
func (l *LogsCollector) Subscribe(buffer int) <-chan LogEntry {
	ch := make(chan LogEntry, buffer)
	l.mu.Lock()
	defer l.mu.Unlock()
	if l.closed {
		close(ch)
		return ch
	}
	l.subscribers = append(l.subscribers, ch)
	return ch
}

// Emit records a new log entry. If the collector is closed the call is ignored.
func (l *LogsCollector) Emit(level LogLevel, msg string, fields map[string]any) {
	l.mu.RLock()
	defer l.mu.RUnlock()
	if l.closed {
		return
	}
	l.ch <- LogEntry{Timestamp: time.Now(), Level: level, Message: msg, Fields: fields}
}

// Close gracefully shuts down the collector and all subscribers.
func (l *LogsCollector) Close() {
	l.mu.Lock()
	if l.closed {
		l.mu.Unlock()
		return
	}
	l.closed = true
	close(l.ch)
	subs := l.subscribers
	l.subscribers = nil
	l.mu.Unlock()
	for _, sub := range subs {
		close(sub)
	}
	l.wg.Wait()
}

// StdLogger returns a log.Logger that writes to the collector with the specified
// level and static fields. It can be used to redirect standard library logging
// output into the structured collector system.
func (l *LogsCollector) StdLogger(level LogLevel, fields map[string]any) *log.Logger {
	pr, pw := io.Pipe()
	logger := log.New(pw, "", 0)
	l.wg.Add(1)
	go func() {
		defer l.wg.Done()
		buf := make([]byte, 1024)
		for {
			n, err := pr.Read(buf)
			if n > 0 {
				l.Emit(level, string(buf[:n]), fields)
			}
			if err != nil {
				return
			}
		}
	}()
	return logger
}

// RedirectStandardLibrary replaces the default standard library logger output
// with one backed by the collector. This enables capturing third-party library
// logs that rely on the global log package.
func (l *LogsCollector) RedirectStandardLibrary(level LogLevel) {
	logger := l.StdLogger(level, nil)
	log.SetOutput(logger.Writer())
}

// Example demonstrates usage of the log collector by emitting a few sample
// messages and writing them to standard output.
func exampleLogsCollector() {
	ctx, cancel := context.WithCancel(context.Background())
	defer cancel()

	collector := NewLogsCollector(100)
	collector.Start(ctx)

	sub := collector.Subscribe(10)
	go func() {
		for entry := range sub {
			fmt.Printf("%s [%s] %s\n", entry.Timestamp.Format(time.RFC3339), entry.Level, entry.Message)
		}
	}()

	collector.Emit(LevelInfo, "collector started", nil)
	collector.Emit(LevelError, "something went wrong", map[string]any{"code": 42})

	time.Sleep(100 * time.Millisecond)
	collector.Close()
}
