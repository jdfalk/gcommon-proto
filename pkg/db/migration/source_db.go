// file: pkg/db/migration/source_db.go
// version: 1.0.0
// guid: e5f6a7b8-c9d0-4e1f-a2b3-c4567890def1

package migration

import (
	"context"
	"database/sql"
	"fmt"
	"strings"
)

// DatabaseSource loads migrations stored in a database table.
// The table schema:
//
//	CREATE TABLE migrations (version INTEGER PRIMARY KEY, name TEXT, up TEXT, down TEXT);
type DatabaseSource struct {
	DB     *sql.DB
	Table  string
	DBType DBType
}

// Load retrieves migrations from the database.
func (s DatabaseSource) Load(ctx context.Context) ([]Migration, error) {
	query := fmt.Sprintf("SELECT version, name, up, down FROM %s ORDER BY version", s.Table)
	rows, err := s.DB.QueryContext(ctx, query)
	if err != nil {
		return nil, fmt.Errorf("query migrations: %w", err)
	}
	defer rows.Close()

	var migrations []Migration
	for rows.Next() {
		var m Migration
		var up, down string
		if err := rows.Scan(&m.Version, &m.Name, &up, &down); err != nil {
			return nil, fmt.Errorf("scan: %w", err)
		}
		m.DB = s.DBType
		m.Up = strings.Split(up, "\n--statement--\n")
		m.Down = strings.Split(down, "\n--statement--\n")
		m.Source = s.Table
		migrations = append(migrations, m)
	}
	if err := rows.Err(); err != nil {
		return nil, fmt.Errorf("rows: %w", err)
	}
	return migrations, nil
}
