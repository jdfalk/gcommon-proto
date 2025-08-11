// file: monitoring/exporters/elastic_test.go
// version: 1.0.0
// guid: 41ad2f9c-3b3a-4b8e-b0a4-6a09ae3b5f22

package exporters

import (
	"context"
	"encoding/json"
	"net/http"
	"net/http/httptest"
	"testing"
	"time"
)

// TestElasticExporter sends a log document to a test server.
func TestElasticExporter(t *testing.T) {
	var received LogDocument
	srv := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		if err := json.NewDecoder(r.Body).Decode(&received); err != nil {
			t.Errorf("decode: %v", err)
		}
	}))
	defer srv.Close()

	exp := NewElasticExporter(srv.URL)
	doc := LogDocument{Timestamp: time.Now(), Level: "INFO", Message: "hello"}
	if err := exp.ExportLog(context.Background(), doc); err != nil {
		t.Fatalf("ExportLog: %v", err)
	}
	if received.Message != "hello" {
		t.Fatalf("unexpected message: %s", received.Message)
	}
}
