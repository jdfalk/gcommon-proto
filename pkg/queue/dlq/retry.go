// file: pkg/queue/dlq/retry.go
// version: 1.0.0
// guid: 251099cb-bf0d-43c6-9c96-689119b05d10

package dlq

import "time"

type RetryStrategy struct {
	Attempts int
	Delay    time.Duration
}
