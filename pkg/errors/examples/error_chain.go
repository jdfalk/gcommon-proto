// file: pkg/errors/examples/error_chain.go
// version: 1.0.0
// guid: c3d4e5f6-a7b8-4901-abcd-3456789023cd

package examples

import (
	"errors"
	"fmt"

	errpkg "github.com/jdfalk/gcommon/pkg/errors"
)

// ExampleErrorChain demonstrates wrapping an existing error.
func ExampleErrorChain() {
	base := errors.New("disk failure")
	wrapped := errpkg.WrapWithCode(base, errpkg.ErrCodeInternal, "storage", "write")
	fmt.Println(errpkg.FormatError(wrapped))
	// Output:
	// disk failure component=storage operation=write
}
