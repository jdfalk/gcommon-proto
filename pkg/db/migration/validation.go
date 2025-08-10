// file: pkg/db/migration/validation.go
// version: 1.0.0
// guid: 3f9d8c7b-6a5e-4d3c-8b2a-1c0d9e8f7a6b

package migration

import "fmt"

// Validator validates migrations before execution.
type Validator interface {
	Validate(Migration) error
}

// BasicValidator performs simple checks on migrations.
type BasicValidator struct{}

// Validate ensures migration fields are populated and SQL is present.
func (BasicValidator) Validate(m Migration) error {
	if err := m.Validate(); err != nil {
		return err
	}
	if m.DB == "" {
		return fmt.Errorf("db type required")
	}
	return nil
}
