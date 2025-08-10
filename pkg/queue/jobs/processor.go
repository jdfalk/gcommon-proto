// file: pkg/queue/jobs/processor.go
// version: 1.0.0
// guid: 046ecf06-4e0b-4867-9707-67622e1a904e

package jobs

import "context"

// Processor defines job processing logic.
type Processor func(ctx context.Context, job *Job) error
