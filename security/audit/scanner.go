// file: security/audit/scanner.go
// version: 1.1.0
// guid: e79da614-b347-4351-991c-e09236fd7f35

// Package audit provides tools for assessing code and dependencies.
package audit

import (
	"bufio"
	"os"
	"path/filepath"
	"regexp"
	"strings"
)

// Rule defines a pattern to search for within source files.
type Rule struct {
	Pattern     *regexp.Regexp
	Description string
	Severity    Severity
}

// Scanner performs pattern based security scans over a directory tree.
type Scanner struct {
	Rules    []Rule
	Findings []Finding
}

// NewScanner creates a scanner with the provided rules.
func NewScanner(rules []Rule) *Scanner {
	return &Scanner{Rules: rules, Findings: []Finding{}}
}

// ScanDir walks the provided directory and records any rule violations.
func (s *Scanner) ScanDir(root string) error {
	return filepath.WalkDir(root, func(path string, d os.DirEntry, err error) error {
		if err != nil {
			return err
		}
		if d.IsDir() {
			return nil
		}
		if !strings.HasSuffix(d.Name(), ".go") {
			return nil
		}
		return s.scanFile(path)
	})
}

// scanFile applies all rules to the specified file.
func (s *Scanner) scanFile(path string) error {
	f, err := os.Open(path)
	if err != nil {
		return err
	}
	defer f.Close()

	scanner := bufio.NewScanner(f)
	line := 0
	for scanner.Scan() {
		line++
		text := scanner.Text()
		for _, r := range s.Rules {
			if r.Pattern.MatchString(text) {
				s.Findings = append(s.Findings, Finding{
					File:        path,
					Line:        line,
					Description: r.Description,
					Severity:    r.Severity,
				})
			}
		}
	}
	return scanner.Err()
}

// Report builds a report from the scanner findings.
func (s *Scanner) Report() Report {
	r := NewReport()
	for _, f := range s.Findings {
		r.AddFinding(f)
	}
	return r
}
