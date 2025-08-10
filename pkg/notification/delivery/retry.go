// file: pkg/notification/delivery/retry.go
// version: 1.0.0
// guid: aaaabbbb-cccc-dddd-eeee-ffff00000002

package delivery

import (
	"context"
	"fmt"
	"time"
)

// Retry executes fn with retries and backoff.
func Retry(ctx context.Context, attempts int, delay time.Duration, fn func() error) error {
	for i := 0; i < attempts; i++ {
		if err := fn(); err == nil {
			return nil
		}
		select {
		case <-time.After(delay * time.Duration(i+1)):
		case <-ctx.Done():
			return ctx.Err()
		}
	}
	return fmt.Errorf("exceeded retries")
}
