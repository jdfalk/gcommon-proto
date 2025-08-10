// file: security/audit/reports.go
// version: 1.1.0
// guid: 6c6558e9-516d-43f0-88f0-9cca2357285c

package audit

import (
	"encoding/json"
	"fmt"
	"strings"
	"time"
)

// Severity represents the seriousness of a finding.
type Severity string

// Severity levels for findings.
const (
	SeverityLow      Severity = "LOW"
	SeverityMedium   Severity = "MEDIUM"
	SeverityHigh     Severity = "HIGH"
	SeverityCritical Severity = "CRITICAL"
)

// Finding represents an individual security issue discovered during an audit.
type Finding struct {
	File        string   `json:"file"`
	Line        int      `json:"line"`
	Description string   `json:"description"`
	Severity    Severity `json:"severity"`
}

// Report represents a security audit report containing all findings.
type Report struct {
	GeneratedAt time.Time `json:"generated_at"`
	Findings    []Finding `json:"findings"`
}

// AddFinding appends a finding to the report.
func (r *Report) AddFinding(f Finding) {
	r.Findings = append(r.Findings, f)
}

// Summary returns a human readable summary of the report.
func (r Report) Summary() string {
	var b strings.Builder
	fmt.Fprintf(&b, "Security Report generated at %s\n", r.GeneratedAt.Format(time.RFC3339))
	for _, f := range r.Findings {
		fmt.Fprintf(&b, "%s:%d [%s] %s\n", f.File, f.Line, f.Severity, f.Description)
	}
	return b.String()
}

// ToJSON marshals the report to JSON for exporting.
func (r Report) ToJSON() ([]byte, error) {
	return json.MarshalIndent(r, "", "  ")
}

// NewReport creates a new report with the current timestamp.
func NewReport() Report {
	return Report{GeneratedAt: time.Now().UTC(), Findings: []Finding{}}
}
