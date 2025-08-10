// file: security/audit/analyzer.go
// version: 1.1.0
// guid: 1947a62e-e301-437f-b59f-5e1da516a039

package audit

import (
	"go/ast"
	"go/parser"
	"go/token"
	"os"
	"path/filepath"
	"strings"
)

// ASTRule defines a rule applied during AST analysis.
type ASTRule struct {
	Description string
	Severity    Severity
	Match       func(*ast.CallExpr) bool
}

// Analyzer evaluates source code for potential security threats using AST rules.
type Analyzer struct {
	Rules []ASTRule
}

// NewAnalyzer returns an Analyzer with a standard set of rules.
func NewAnalyzer() *Analyzer {
	rules := []ASTRule{
		{
			Description: "use of insecure MD5 hashing",
			Severity:    SeverityHigh,
			Match: func(call *ast.CallExpr) bool {
				if sel, ok := call.Fun.(*ast.SelectorExpr); ok {
					if ident, ok := sel.X.(*ast.Ident); ok {
						return ident.Name == "md5" && sel.Sel.Name == "New"
					}
				}
				return false
			},
		},
		{
			Description: "use of math/rand for security-sensitive randomness",
			Severity:    SeverityMedium,
			Match: func(call *ast.CallExpr) bool {
				if sel, ok := call.Fun.(*ast.SelectorExpr); ok {
					if ident, ok := sel.X.(*ast.Ident); ok {
						return ident.Name == "rand" && (sel.Sel.Name == "Int" || sel.Sel.Name == "Read")
					}
				}
				return false
			},
		},
		{
			Description: "HTTP request made over insecure protocol",
			Severity:    SeverityMedium,
			Match: func(call *ast.CallExpr) bool {
				if fun, ok := call.Fun.(*ast.SelectorExpr); ok {
					if ident, ok := fun.X.(*ast.Ident); ok && ident.Name == "http" {
						if fun.Sel.Name == "Get" && len(call.Args) > 0 {
							if lit, ok := call.Args[0].(*ast.BasicLit); ok && strings.HasPrefix(strings.Trim(lit.Value, "\""), "http://") {
								return true
							}
						}
						if fun.Sel.Name == "ListenAndServe" && len(call.Args) > 0 {
							// arg0 is address string, "": no TLS
							if _, ok := call.Args[0].(*ast.BasicLit); ok {
								return true
							}
						}
					}
				}
				return false
			},
		},
	}
	return &Analyzer{Rules: rules}
}

// AnalyzeDir analyzes all Go files under root and returns any findings.
func (a *Analyzer) AnalyzeDir(root string) ([]Finding, error) {
	findings := []Finding{}
	err := filepath.WalkDir(root, func(path string, d os.DirEntry, err error) error {
		if err != nil {
			return err
		}
		if d.IsDir() {
			return nil
		}
		if !strings.HasSuffix(path, ".go") {
			return nil
		}
		fs, err := a.AnalyzeFile(path)
		if err != nil {
			return err
		}
		findings = append(findings, fs...)
		return nil
	})
	return findings, err
}

// AnalyzeFile analyzes a single Go source file.
func (a *Analyzer) AnalyzeFile(path string) ([]Finding, error) {
	fset := token.NewFileSet()
	node, err := parser.ParseFile(fset, path, nil, 0)
	if err != nil {
		return nil, err
	}
	findings := []Finding{}
	ast.Inspect(node, func(n ast.Node) bool {
		call, ok := n.(*ast.CallExpr)
		if !ok {
			return true
		}
		for _, rule := range a.Rules {
			if rule.Match(call) {
				pos := fset.Position(call.Pos())
				findings = append(findings, Finding{
					File:        path,
					Line:        pos.Line,
					Description: rule.Description,
					Severity:    rule.Severity,
				})
			}
		}
		return true
	})
	return findings, nil
}
