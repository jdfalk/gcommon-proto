// file: pkg/db/migration/source.go
// version: 1.0.0
// guid: b2f4f5a6-7e8d-4c9b-8c1d-0e0f1a2b3c4d

package migration

import "context"

// Source provides migrations from a storage mechanism.
type Source interface {
	Load(context.Context) ([]Migration, error)
}
