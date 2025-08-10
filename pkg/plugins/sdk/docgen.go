// file: pkg/plugins/sdk/docgen.go
// version: 1.0.0
// guid: 07c06a88-6c73-4d5e-9fcf-c406f88bb758

package sdk

import (
	"io"

	"github.com/jdfalk/gcommon/pkg/plugins"
)

// GenerateMarkdown writes plugin documentation in Markdown format.
func GenerateMarkdown(w io.Writer, md plugins.Metadata) error {
	_, err := io.WriteString(w, GenerateDocumentation(md))
	return err
}
