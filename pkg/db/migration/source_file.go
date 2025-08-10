// file: pkg/db/migration/source_file.go
// version: 1.0.0
// guid: c1d2e3f4-5678-4abc-90de-f123456789ab

package migration

import (
	"context"
	"fmt"
	"os"
	"path/filepath"
	"regexp"
)

var filePattern = regexp.MustCompile(`^(\d+)_([a-zA-Z0-9_]+)\.(up|down)\.sql$`)

// FileSource loads migrations from a directory on disk.
type FileSource struct {
	Dir string
	DB  DBType
}

// Load reads all migrations from the directory.
func (s FileSource) Load(ctx context.Context) ([]Migration, error) {
	_ = ctx
	entries, err := os.ReadDir(s.Dir)
	if err != nil {
		return nil, fmt.Errorf("read dir: %w", err)
	}

	type pair struct {
		up   string
		down string
	}

	files := map[int]*pair{}

	for _, e := range entries {
		name := e.Name()
		matches := filePattern.FindStringSubmatch(name)
		if len(matches) != 4 {
			continue
		}
		version := atoi(matches[1])
		mig, ok := files[version]
		if !ok {
			mig = &pair{}
			files[version] = mig
		}
		path := filepath.Join(s.Dir, name)
		if matches[3] == "up" {
			mig.up = path
		} else {
			mig.down = path
		}
	}

	var migrations []Migration
	for v, p := range files {
		name := extractName(p.up, v)
		if p.up == "" || p.down == "" {
			return nil, fmt.Errorf("migration %d missing up or down file", v)
		}
		upStmts, err := ParseSQLFile(p.up)
		if err != nil {
			return nil, err
		}
		downStmts, err := ParseSQLFile(p.down)
		if err != nil {
			return nil, err
		}
		migrations = append(migrations, Migration{
			Version: v,
			Name:    name,
			DB:      s.DB,
			Up:      upStmts,
			Down:    downStmts,
			Source:  s.Dir,
		})
	}

	SortMigrations(migrations)
	return migrations, nil
}

// atoi converts string to int ignoring errors.
func atoi(s string) int {
	var n int
	for _, r := range s {
		n = n*10 + int(r-'0')
	}
	return n
}

// extractName infers migration name from path.
func extractName(path string, version int) string {
	base := filepath.Base(path)
	matches := filePattern.FindStringSubmatch(base)
	if len(matches) == 4 {
		return matches[2]
	}
	return fmt.Sprintf("migration_%d", version)
}
