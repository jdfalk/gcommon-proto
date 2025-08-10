// file: pkg/plugins/examples/extension/hello/hello_test.go
// version: 1.0.0
// guid: 8712ad79-36ab-4f70-9de4-e6f8f507b2d7

package hello

import (
	"testing"

	"github.com/jdfalk/gcommon/pkg/plugins"
)

func TestHelloExtend(t *testing.T) {
	p := New()
	m := plugins.NewManager(nil, nil, nil)
	received := make(chan plugins.Message, 1)
	m.Bus().Subscribe("hello", func(msg plugins.Message) { received <- msg })
	if err := p.Extend(m); err != nil {
		t.Fatalf("extend: %v", err)
	}
	msg := <-received
	if msg.Data != "world" {
		t.Fatalf("unexpected data %v", msg.Data)
	}
}
