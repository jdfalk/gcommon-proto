// file: pkg/notification/templates/parser.go
// version: 1.0.0
// guid: 77777777-7777-7777-7777-777777777777

package templates

import pb "github.com/jdfalk/gcommon/pkg/notification/proto"

// Parse provides a helper for parsing templates.
func Parse(tmpl string) (*pb.Template, error) {
	return New().ParseTemplate(tmpl)
}
