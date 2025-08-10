// file: security/audit/dependencies.go
// version: 1.1.0
// guid: cec74a0f-22c8-4ddf-9ba0-dfb1f76b0c2a

package audit

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

// VulnerableDep describes a known vulnerable dependency constraint.
type VulnerableDep struct {
	Module      string
	MinVersion  string
	Severity    Severity
	Description string
}

// Example vulnerability database.
var knownVulnerabilities = []VulnerableDep{
	{Module: "github.com/example/legacy", MinVersion: "v1.2.0", Severity: SeverityHigh, Description: "remote code execution"},
	{Module: "golang.org/x/crypto", MinVersion: "v0.35.0", Severity: SeverityMedium, Description: "multiple CVEs"},
}

// AuditDependencies checks project dependencies for known vulnerabilities.
func AuditDependencies(modPath string) ([]Finding, error) {
	file, err := os.Open(modPath)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	findings := []Finding{}
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := strings.TrimSpace(scanner.Text())
		if !strings.HasPrefix(line, "require") {
			continue
		}
		parts := strings.Fields(line)
		for _, vuln := range knownVulnerabilities {
			if len(parts) >= 3 && strings.Contains(parts[1], vuln.Module) {
				version := parts[2]
				if strings.Trim(version, "()") < vuln.MinVersion {
					findings = append(findings, Finding{
						File:        modPath,
						Line:        0,
						Description: fmt.Sprintf("dependency %s is below secure version %s", vuln.Module, vuln.MinVersion),
						Severity:    vuln.Severity,
					})
				}
			}
		}
	}
	return findings, scanner.Err()
}
