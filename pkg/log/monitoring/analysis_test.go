// file: pkg/log/monitoring/analysis_test.go
// version: 1.0.0
// guid: 33b7c9d5-6f0e-4ac8-9c89-d6c1a4e9f3b0

package monitoring

import (
	"testing"

	"github.com/jdfalk/gcommon/pkg/log"
)

// TestAnalyzer verifies counting and searching of log entries.
func TestAnalyzer(t *testing.T) {
	entries := []log.LogEntry{{Level: log.InfoLevel, Message: "startup"}, {Level: log.ErrorLevel, Message: "fail"}}
	a := Analyzer{}
	counts := a.CountByLevel(entries)
	if counts[log.InfoLevel] != 1 || counts[log.ErrorLevel] != 1 {
		t.Fatalf("unexpected counts: %+v", counts)
	}
	found := a.Search(entries, "fail")
	if len(found) != 1 || found[0].Message != "fail" {
		t.Fatalf("unexpected search result: %+v", found)
	}
}
