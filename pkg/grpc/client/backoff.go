// file: pkg/grpc/client/backoff.go
// version: 1.0.0
// guid: 0b3cb7db-08ab-4db0-844d-0e3d6d0b9092

package client

import (
	"math"
	"math/rand"
	"time"
)

// Backoff defines the interface for calculating retry intervals.
type Backoff interface {
	// Next returns the duration to wait before the next retry attempt.
	Next(attempt uint) time.Duration
}

// ExponentialBackoff provides exponential backoff with optional jitter.
type ExponentialBackoff struct {
	BaseDelay  time.Duration // initial delay
	MaxDelay   time.Duration // maximum delay
	Multiplier float64       // growth factor for each attempt
	Jitter     float64       // randomization factor between 0 and 1
	rand       *rand.Rand    // source for jitter randomness
}

// NewExponentialBackoff creates a new ExponentialBackoff with defaults.
func NewExponentialBackoff() *ExponentialBackoff {
	return &ExponentialBackoff{
		BaseDelay:  time.Millisecond * 100,
		MaxDelay:   time.Second * 5,
		Multiplier: 2,
		Jitter:     0.2,
		rand:       rand.New(rand.NewSource(time.Now().UnixNano())),
	}
}

// Next implements Backoff by returning exponentially increasing delays.
func (b *ExponentialBackoff) Next(attempt uint) time.Duration {
	if b.BaseDelay <= 0 {
		b.BaseDelay = time.Millisecond * 100
	}
	if b.MaxDelay <= 0 {
		b.MaxDelay = time.Second * 5
	}
	if b.Multiplier <= 1 {
		b.Multiplier = 2
	}
	if b.Jitter < 0 || b.Jitter > 1 {
		b.Jitter = 0.2
	}
	// Calculate exponential delay
	delay := float64(b.BaseDelay) * math.Pow(b.Multiplier, float64(attempt))
	if delay > float64(b.MaxDelay) {
		delay = float64(b.MaxDelay)
	}
	// Apply jitter
	if b.Jitter > 0 {
		jitter := 1 + (b.rand.Float64()*2-1)*b.Jitter
		delay = delay * jitter
	}
	return time.Duration(delay)
}

// ConstantBackoff returns the same delay each time.
type ConstantBackoff struct {
	Delay time.Duration
}

// Next implements Backoff for ConstantBackoff.
func (c ConstantBackoff) Next(uint) time.Duration {
	if c.Delay <= 0 {
		return time.Millisecond * 100
	}
	return c.Delay
}
