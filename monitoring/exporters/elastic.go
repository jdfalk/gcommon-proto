// file: monitoring/exporters/elastic.go
// version: 1.1.0
// guid: 7a8b9c0d-1e2f-3a4b-5c6d-7e8f9a0b1c2d

package exporters

import (
	"bytes"
	"context"
	"encoding/json"
	"fmt"
	"net/http"
	"time"
)

// ElasticExporter sends structured logs to an Elasticsearch-compatible endpoint.
type ElasticExporter struct {
	endpoint string
	client   *http.Client
}

// NewElasticExporter creates a new exporter with the provided endpoint URL.
func NewElasticExporter(endpoint string) *ElasticExporter {
	return &ElasticExporter{
		endpoint: endpoint,
		client:   &http.Client{Timeout: 5 * time.Second},
	}
}

// LogDocument represents the structure sent to Elasticsearch.
type LogDocument struct {
	Timestamp time.Time      `json:"@timestamp"`
	Level     string         `json:"level"`
	Message   string         `json:"message"`
	Fields    map[string]any `json:"fields,omitempty"`
}

// ExportLog sends a log document to Elasticsearch. Errors are returned if the
// request fails or Elasticsearch responds with a non-200 status.
func (e *ElasticExporter) ExportLog(ctx context.Context, doc LogDocument) error {
	body, err := json.Marshal(doc)
	if err != nil {
		return err
	}
	req, err := http.NewRequestWithContext(ctx, http.MethodPost, e.endpoint, bytes.NewReader(body))
	if err != nil {
		return err
	}
	req.Header.Set("Content-Type", "application/json")
	resp, err := e.client.Do(req)
	if err != nil {
		return err
	}
	defer resp.Body.Close()
	if resp.StatusCode/100 != 2 {
		return fmt.Errorf("unexpected status: %s", resp.Status)
	}
	return nil
}
