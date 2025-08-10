// file: pkg/db/migration/migration.go
// version: 1.0.0
// guid: 8f0c2d7e-3c31-4db2-8e5e-73a7aefd1f1c

package migration

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"path/filepath"
	"sort"
	"strings"
)

// DBType represents a supported database engine.
type DBType string

const (
	// Postgres represents PostgreSQL database.
	Postgres DBType = "postgres"
	// SQLite represents SQLite database.
	SQLite DBType = "sqlite"
	// Cockroach represents CockroachDB database.
	Cockroach DBType = "cockroach"
	// MySQL represents MySQL database.
	MySQL DBType = "mysql"
)

// Migration defines a single database migration step.
// Each migration consists of a set of SQL statements for moving forward (Up)
// and backward (Down) through schema versions.
type Migration struct {
	Version int
	Name    string
	DB      DBType
	Up      []string
	Down    []string
	Source  string
}

// SortMigrations orders migrations by version.
func SortMigrations(migs []Migration) {
	sort.Slice(migs, func(i, j int) bool {
		return migs[i].Version < migs[j].Version
	})
}

// ParseSQLFile reads a SQL file and splits statements by semicolon.
// Empty lines and comments starting with "--" are ignored.
func ParseSQLFile(path string) ([]string, error) {
	f, err := os.Open(path)
	if err != nil {
		return nil, fmt.Errorf("open sql file: %w", err)
	}
	defer f.Close()

	return readSQLStatements(f)
}

// readSQLStatements reads SQL statements from r.
func readSQLStatements(r io.Reader) ([]string, error) {
	var stmts []string
	var b strings.Builder
	scanner := bufio.NewScanner(r)
	for scanner.Scan() {
		line := strings.TrimSpace(scanner.Text())
		if line == "" || strings.HasPrefix(line, "--") {
			continue
		}
		b.WriteString(line)
		if strings.HasSuffix(line, ";") {
			stmts = append(stmts, strings.TrimSuffix(b.String(), ";"))
			b.Reset()
		} else {
			b.WriteRune(' ')
		}
	}
	if err := scanner.Err(); err != nil {
		return nil, fmt.Errorf("scan sql: %w", err)
	}
	if b.Len() > 0 {
		stmts = append(stmts, strings.TrimSpace(b.String()))
	}
	return stmts, nil
}

// LoadMigrationFromDir loads a migration given a base path and version/name.
// It expects files in format `<version>_<name>.up.sql` and `<version>_<name>.down.sql`.
func LoadMigrationFromDir(dir string, version int, name string, db DBType) (Migration, error) {
	base := fmt.Sprintf("%03d_%s", version, name)
	upPath := filepath.Join(dir, base+".up.sql")
	downPath := filepath.Join(dir, base+".down.sql")

	upStmts, err := ParseSQLFile(upPath)
	if err != nil {
		return Migration{}, err
	}
	downStmts, err := ParseSQLFile(downPath)
	if err != nil {
		return Migration{}, err
	}
	return Migration{
		Version: version,
		Name:    name,
		DB:      db,
		Up:      upStmts,
		Down:    downStmts,
		Source:  dir,
	}, nil
}

// String returns a human-readable representation of the migration.
func (m Migration) String() string {
	return fmt.Sprintf("%d_%s", m.Version, m.Name)
}

// Validate ensures migration has required fields.
func (m Migration) Validate() error {
	if m.Version <= 0 {
		return fmt.Errorf("version must be positive")
	}
	if m.Name == "" {
		return fmt.Errorf("name required")
	}
	if len(m.Up) == 0 {
		return fmt.Errorf("up statements required")
	}
	if len(m.Down) == 0 {
		return fmt.Errorf("down statements required")
	}
	return nil
}

// Reverse returns a copy of the migration with Up and Down swapped.
func (m Migration) Reverse() Migration {
	return Migration{
		Version: m.Version,
		Name:    m.Name,
		DB:      m.DB,
		Up:      append([]string{}, m.Down...),
		Down:    append([]string{}, m.Up...),
		Source:  m.Source,
	}
}
