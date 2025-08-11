// file: pkg/queue/context.go
// version: 1.0.0
// guid: ff7f0b20-04ef-455b-8305-bdbad15665fc

package queue

import "context"

// queueNameKey is an unexported type for context keys defined in this package.
type queueNameKey struct{}

// WithQueueName returns a new context with the provided queue name associated
// with it. Providers can use QueueNameFromContext to retrieve the name and route
// messages accordingly.
func WithQueueName(ctx context.Context, name string) context.Context {
	return context.WithValue(ctx, queueNameKey{}, name)
}

// QueueNameFromContext extracts a queue name from context. The boolean return
// value indicates whether a queue name was present.
func QueueNameFromContext(ctx context.Context) (string, bool) {
	v, ok := ctx.Value(queueNameKey{}).(string)
	return v, ok && v != ""
}
