// file: pkg/errors/examples/basic_errors.go
// version: 1.0.0
// guid: a1b2c3d4-e5f6-4789-abcd-1234567890ef

package examples

import (
	"context"
	"fmt"

	errpkg "github.com/jdfalk/gcommon/pkg/errors"
)

// ExampleBasic demonstrates basic error creation and formatting.
func ExampleBasic() {
	err := errpkg.NewError(context.Background(), errpkg.ErrCodeInternal, "something broke")
	fmt.Println(errpkg.FormatError(err))
	// Output:
	// something broke
}
