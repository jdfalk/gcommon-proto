// file: cmd/microservice-template/main.go
// version: 1.0.0
// guid: 8d489f9b-5eed-4b00-98ae-93f4d6ed0478

package main

import (
	"flag"
	"fmt"
	"os"
	"path/filepath"
	"strings"
)

func main() {
	tmpl := flag.String("template", "", "template name")
	target := flag.String("target", "", "target directory")
	name := flag.String("name", "", "service name for replacement")
	flag.Parse()

	if *tmpl == "" || *target == "" || *name == "" {
		fmt.Println("usage: microservice-template -template <name> -target <dir> -name <service>")
		os.Exit(1)
	}

	templateDir := filepath.Join("templates", *tmpl)
	if err := copyTemplate(templateDir, *target, *tmpl, *name); err != nil {
		fmt.Fprintf(os.Stderr, "error: %v\n", err)
		os.Exit(1)
	}
}

func copyTemplate(src, dst, tmplName, svcName string) error {
	return filepath.Walk(src, func(path string, info os.FileInfo, err error) error {
		if err != nil {
			return err
		}
		rel, err := filepath.Rel(src, path)
		if err != nil {
			return err
		}
		targetPath := filepath.Join(dst, strings.ReplaceAll(rel, tmplName, svcName))
		if info.IsDir() {
			return os.MkdirAll(targetPath, 0o755)
		}
		data, err := os.ReadFile(path)
		if err != nil {
			return err
		}
		content := strings.ReplaceAll(string(data), tmplName, svcName)
		return os.WriteFile(targetPath, []byte(content), info.Mode())
	})
}

// CopyFile is exposed for testing.
func CopyFile(src, dst, tmplName, svcName string) error {
	return copyTemplate(src, dst, tmplName, svcName)
}
