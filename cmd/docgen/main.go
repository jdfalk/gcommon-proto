// file: cmd/docgen/main.go
// version: 0.1.0
// guid: acacacac-acac-4cac-8cac-acacacacacac

package main

import (
	"os"

	"github.com/jdfalk/gcommon/pkg/docsystem"
)

func main() {
	os.Exit(docsystem.CLI(os.Args[1:]))
}
