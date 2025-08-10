// file: pkg/errors/reporter.go
// version: 1.0.0
// guid: e2a91c7d-58dc-4dbb-9ae1-1234567890ab

package errors

import (
	"context"
	"sync"
)

// ErrorReporter defines an interface for reporting and tracking errors.
type ErrorReporter interface {
	ReportError(ctx context.Context, err Error)
	ReportErrorWithTags(ctx context.Context, err Error, tags map[string]string)
	GetErrorStats() *ErrorStats
	Reset()
}

// ErrorStats aggregates statistics about reported errors.
type ErrorStats struct {
	TotalErrors    int64
	ErrorsByCode   map[ErrorCode]int64
	ErrorsByModule map[string]int64
	RecentErrors   []Error
}

// MemoryReporter is an in-memory implementation of ErrorReporter.
type MemoryReporter struct {
	mu    sync.Mutex
	stats ErrorStats
}

// NewMemoryReporter creates a new MemoryReporter.
func NewMemoryReporter() *MemoryReporter {
	return &MemoryReporter{
		stats: ErrorStats{
			ErrorsByCode:   map[ErrorCode]int64{},
			ErrorsByModule: map[string]int64{},
			RecentErrors:   []Error{},
		},
	}
}

// ReportError records an error without additional tags.
func (r *MemoryReporter) ReportError(ctx context.Context, err Error) {
	r.ReportErrorWithTags(ctx, err, map[string]string{})
}

// ReportErrorWithTags records an error and associated tags.
func (r *MemoryReporter) ReportErrorWithTags(ctx context.Context, err Error, tags map[string]string) {
	if err == nil {
		return
	}
	r.mu.Lock()
	defer r.mu.Unlock()
	r.stats.TotalErrors++
	r.stats.ErrorsByCode[err.Code()]++
	r.stats.ErrorsByModule[err.Component()]++
	if len(r.stats.RecentErrors) >= 10 {
		r.stats.RecentErrors = r.stats.RecentErrors[1:]
	}
	r.stats.RecentErrors = append(r.stats.RecentErrors, err)
}

// GetErrorStats returns a copy of the current statistics.
func (r *MemoryReporter) GetErrorStats() *ErrorStats {
	r.mu.Lock()
	defer r.mu.Unlock()
	stats := r.stats
	return &stats
}

// Reset clears all collected statistics.
func (r *MemoryReporter) Reset() {
	r.mu.Lock()
	defer r.mu.Unlock()
	r.stats = ErrorStats{
		ErrorsByCode:   map[ErrorCode]int64{},
		ErrorsByModule: map[string]int64{},
		RecentErrors:   []Error{},
	}
}
