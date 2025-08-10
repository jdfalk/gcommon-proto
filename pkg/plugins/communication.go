// file: pkg/plugins/communication.go
// version: 1.0.0
// guid: 61ca0091-811b-4a3f-9b5a-76fdc3bfe4db

package plugins

import "sync"

// Message represents a communication payload between plugins.
type Message struct {
	Topic string
	Data  interface{}
}

// Bus defines plugin messaging operations.
type Bus interface {
	Publish(msg Message) error
	Subscribe(topic string, handler func(Message)) error
}

// InMemoryBus provides a simple pub/sub message bus for plugins.
type InMemoryBus struct {
	mu   sync.RWMutex
	subs map[string][]func(Message)
}

// NewInMemoryBus creates an empty message bus.
func NewInMemoryBus() *InMemoryBus {
	return &InMemoryBus{subs: make(map[string][]func(Message))}
}

// Publish sends a message to all subscribers of the topic.
func (b *InMemoryBus) Publish(msg Message) error {
	b.mu.RLock()
	handlers := append([]func(Message){}, b.subs[msg.Topic]...)
	b.mu.RUnlock()
	for _, h := range handlers {
		h(msg)
	}
	return nil
}

// Subscribe registers a handler for a topic.
func (b *InMemoryBus) Subscribe(topic string, handler func(Message)) error {
	b.mu.Lock()
	b.subs[topic] = append(b.subs[topic], handler)
	b.mu.Unlock()
	return nil
}
