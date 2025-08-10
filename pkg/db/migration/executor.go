// file: pkg/db/migration/executor.go
// version: 1.0.0
// guid: 2a4c11fb-61d6-4a5e-8c5f-b9425e75fd0b

package migration

import "context"

// Executor runs and lists migrations.
type Executor interface {
	Execute(context.Context, Migration) error
	Rollback(context.Context, Migration) error
	List(context.Context) ([]Migration, error)
}
