// file: pkg/log/monitoring/analysis.go
// version: 1.0.0
// guid: a1b2c3d4-e5f6-4789-0abc-1234567890ef

package monitoring

import (
	"strings"

	"github.com/jdfalk/gcommon/pkg/log"
)

// Analyzer performs simple analysis on log entries.
type Analyzer struct{}

// CountByLevel returns the number of entries for each level.
func (Analyzer) CountByLevel(entries []log.LogEntry) map[log.Level]int {
	counts := make(map[log.Level]int)
	for _, e := range entries {
		counts[e.Level]++
	}
	return counts
}

// Search returns entries whose message contains the substring.
func (Analyzer) Search(entries []log.LogEntry, substr string) []log.LogEntry {
	out := make([]log.LogEntry, 0)
	for _, e := range entries {
		if strings.Contains(e.Message, substr) {
			out = append(out, e)
		}
	}
	return out
}
