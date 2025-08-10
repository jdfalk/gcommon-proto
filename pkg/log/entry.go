// file: pkg/log/entry.go
// version: 1.0.0
// guid: 286abf98-3bd1-414a-af86-b2d39fced4c3

package log

import "time"

// LogEntry represents a standardized log entry with correlation metadata.
type LogEntry struct {
	Timestamp     time.Time
	Level         Level
	Message       string
	Module        string
	Component     string
	Operation     string
	CorrelationID string
	UserID        string
	RequestID     string
	Fields        map[string]interface{}
	Error         error
	Stack         []string
}
