// file: pkg/notification/templates/engine_test.go
// version: 1.0.0
// guid: 23232323-4545-5656-6767-787878787878

package templates

import "testing"

func TestEngineRender(t *testing.T) {
	eng := New()
	tmpl, err := eng.ParseTemplate("Hello {{.Name}}")
	if err != nil {
		t.Fatalf("ParseTemplate: %v", err)
	}
	out, err := eng.RenderTemplate(tmpl, map[string]any{"Name": "World"})
	if err != nil {
		t.Fatalf("RenderTemplate: %v", err)
	}
	if out != "Hello World" {
		t.Fatalf("expected Hello World, got %s", out)
	}
}
