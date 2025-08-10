// file: pkg/plugins/bus_test.go
// version: 1.0.0
// guid: c7d66be5-1e44-4c8e-9ffd-3b7056eeff0c

package plugins

import "testing"

func TestInMemoryBusPublishSubscribe(t *testing.T) {
	bus := NewInMemoryBus()
	received := make(chan Message, 1)
	bus.Subscribe("topic", func(m Message) { received <- m })
	bus.Publish(Message{Topic: "topic", Data: "hello"})
	msg := <-received
	if msg.Data != "hello" {
		t.Fatalf("unexpected data %v", msg.Data)
	}
}
