// file: pkg/db/migration/source_remote.go
// version: 1.0.0
// guid: f6a7b8c9-d0e1-4f2a-b3c4-d567890e1f23

package migration

import (
	"context"
	"encoding/json"
	"fmt"
	"net/http"
)

// RemoteSource fetches migrations from a remote HTTP endpoint.
// The endpoint should return JSON array of objects {version,name,up,down,db}.
type RemoteSource struct {
	Client *http.Client
	URL    string
}

// Load retrieves migrations from the remote server.
func (s RemoteSource) Load(ctx context.Context) ([]Migration, error) {
	req, err := http.NewRequestWithContext(ctx, http.MethodGet, s.URL, nil)
	if err != nil {
		return nil, fmt.Errorf("new request: %w", err)
	}
	resp, err := s.Client.Do(req)
	if err != nil {
		return nil, fmt.Errorf("do request: %w", err)
	}
	defer resp.Body.Close()
	if resp.StatusCode != http.StatusOK {
		return nil, fmt.Errorf("unexpected status: %s", resp.Status)
	}
	var data []struct {
		Version int      `json:"version"`
		Name    string   `json:"name"`
		DB      DBType   `json:"db"`
		Up      []string `json:"up"`
		Down    []string `json:"down"`
	}
	if err := json.NewDecoder(resp.Body).Decode(&data); err != nil {
		return nil, fmt.Errorf("decode: %w", err)
	}
	var migrations []Migration
	for _, d := range data {
		migrations = append(migrations, Migration{
			Version: d.Version,
			Name:    d.Name,
			DB:      d.DB,
			Up:      d.Up,
			Down:    d.Down,
			Source:  s.URL,
		})
	}
	SortMigrations(migrations)
	return migrations, nil
}
