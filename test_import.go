// file: test_import.go
// version: 1.0.0
// guid: 9a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d

package main

import (
	"fmt"

	"github.com/jdfalk/gcommon/proto/common"
)

func main() {
	// Test that we can import and use types from our generated modules
	fmt.Printf("Testing import of common module\n")

	// Create an instance of a generated type to verify the import works
	logLevel := common.LogLevel_LOG_LEVEL_INFO
	fmt.Printf("Log level: %v\n", logLevel)
}
