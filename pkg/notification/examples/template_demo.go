// file: pkg/notification/examples/template_demo.go
// version: 1.0.0
// guid: 99998888-7777-6666-5555-444433332222

package examples

import (
	"fmt"

	"github.com/jdfalk/gcommon/pkg/notification/templates"
)

// ExampleTemplate demonstrates template rendering.
func ExampleTemplate() {
	tmpl, _ := templates.Parse("Hello {{.Name}}")
	out, _ := templates.Render(tmpl, map[string]any{"Name": "World"})
	fmt.Println(out)
}
