// file: pkg/errors/formatting.go
// version: 1.0.0
// guid: d6b9a3b4-9c5f-4c18-badf-0ef123456789

package errors

import (
	"fmt"
	"sort"
	"strings"
)

// FormatError returns a human-friendly representation of an Error.
func FormatError(err Error) string {
	if err == nil {
		return ""
	}
	var b strings.Builder
	b.WriteString(err.Error())
	if c := err.Component(); c != "" {
		b.WriteString(fmt.Sprintf(" component=%s", c))
	}
	if o := err.Operation(); o != "" {
		b.WriteString(fmt.Sprintf(" operation=%s", o))
	}
	if len(err.Details()) > 0 {
		keys := make([]string, 0, len(err.Details()))
		for k := range err.Details() {
			keys = append(keys, k)
		}
		sort.Strings(keys)
		b.WriteString(" details=")
		for i, k := range keys {
			if i > 0 {
				b.WriteString(",")
			}
			b.WriteString(fmt.Sprintf("%s=%v", k, err.Details()[k]))
		}
	}
	return b.String()
}
