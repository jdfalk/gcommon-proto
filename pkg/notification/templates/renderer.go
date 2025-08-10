// file: pkg/notification/templates/renderer.go
// version: 1.0.0
// guid: 88888888-8888-8888-8888-888888888888

package templates

import pb "github.com/jdfalk/gcommon/pkg/notification/proto"

// Render renders a template with data using the default engine.
func Render(tmpl *pb.Template, data map[string]any) (string, error) {
	return New().RenderTemplate(tmpl, data)
}
