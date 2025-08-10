// file: pkg/config/examples/simple.go
// version: 1.0.0
// guid: cccccccc-cccc-cccc-cccc-cccccccccccc

package examples

import (
	"fmt"

	"github.com/jdfalk/gcommon/pkg/config/providers"
)

// This example demonstrates basic usage of the configuration module
// TODO: Expand with error handling and advanced features
// TODO: Convert to executable example tests
func ExampleSimple() {
	p, _ := providers.NewEnvProvider("APP_")
	_ = p.Set("NAME", "gcommon")
	v, _ := p.Get("NAME")
	fmt.Println(v)
	// Output:
	// gcommon
	_ = p.Close()
}

// EOF
