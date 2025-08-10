// file: pkg/notification/templates/engine.go
// version: 1.1.0
// guid: 66666666-6666-6666-6666-666666666666

package templates

import (
	"bytes"
	"text/template"

	notification "github.com/jdfalk/gcommon/pkg/notification"
	pb "github.com/jdfalk/gcommon/pkg/notification/proto"
)

// BasicEngine implements notification.TemplateEngine.
type BasicEngine struct{}

// New creates a new BasicEngine.
func New() notification.TemplateEngine {
	return &BasicEngine{}
}

// ParseTemplate parses raw template text.
func (e *BasicEngine) ParseTemplate(tmpl string) (*pb.Template, error) {
	if err := e.ValidateTemplate(tmpl); err != nil {
		return nil, err
	}
	t := &pb.Template{}
	t.SetBody(tmpl)
	return t, nil
}

// RenderTemplate renders a template with data.
func (e *BasicEngine) RenderTemplate(tmpl *pb.Template, data map[string]any) (string, error) {
	tpl, err := template.New("tmpl").Parse(tmpl.GetBody())
	if err != nil {
		return "", err
	}
	var buf bytes.Buffer
	if err := tpl.Execute(&buf, data); err != nil {
		return "", err
	}
	return buf.String(), nil
}

// ValidateTemplate ensures template is valid.
func (e *BasicEngine) ValidateTemplate(tmpl string) error {
	_, err := template.New("tmpl").Parse(tmpl)
	return err
}
