// file: pkg/db/migration/source_embed.go
// version: 1.0.0
// guid: d4e5f6a7-b8c9-4d0e-af01-b23456789cde

package migration

import (
	"context"
	"embed"
	"fmt"
	"io/fs"
	"path/filepath"
)

// EmbedSource loads migrations from an embedded filesystem.
type EmbedSource struct {
	FS  embed.FS
	Dir string
	DB  DBType
}

// Load reads migrations from the embedded filesystem.
func (s EmbedSource) Load(ctx context.Context) ([]Migration, error) {
	_ = ctx
	entries, err := fs.ReadDir(s.FS, s.Dir)
	if err != nil {
		return nil, fmt.Errorf("readdir: %w", err)
	}
	type pair struct{ up, down string }
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
		upFile, err := s.FS.Open(p.up)
		if err != nil {
			return nil, err
		}
		upStmts, err := readSQLStatements(upFile)
		upFile.Close()
		if err != nil {
			return nil, err
		}
		downFile, err := s.FS.Open(p.down)
		if err != nil {
			return nil, err
		}
		downStmts, err := readSQLStatements(downFile)
		downFile.Close()
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

// No additional helpers required; reuse atoi and extractName from file source.
