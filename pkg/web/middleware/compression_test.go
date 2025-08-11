// file: pkg/web/middleware/compression_test.go
// version: 1.0.0
// guid: f1a2b3c4-d5e6-7f8a-9b0c-1234567890ab

package middleware

import (
	"bytes"
	"compress/gzip"
	"io"
	"net/http"
	"net/http/httptest"
	"testing"
)

func TestCompressionMiddleware(t *testing.T) {
	m := Compression(gzip.DefaultCompression)
	handler := m.Handle(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		w.Write([]byte("hello"))
	}))
	req := httptest.NewRequest(http.MethodGet, "/", nil)
	req.Header.Set("Accept-Encoding", "gzip")
	rec := httptest.NewRecorder()
	handler.ServeHTTP(rec, req)
	if rec.Header().Get("Content-Encoding") != "gzip" {
		t.Fatalf("expected gzip encoding")
	}
	zr, err := gzip.NewReader(bytes.NewReader(rec.Body.Bytes()))
	if err != nil {
		t.Fatalf("new reader: %v", err)
	}
	data, err := io.ReadAll(zr)
	if err != nil {
		t.Fatalf("read: %v", err)
	}
	if string(data) != "hello" {
		t.Fatalf("unexpected body: %s", data)
	}
}

func TestCompressionMiddlewareSkips(t *testing.T) {
	m := Compression(gzip.DefaultCompression)
	handler := m.Handle(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		w.Write([]byte("hi"))
	}))
	req := httptest.NewRequest(http.MethodGet, "/", nil)
	rec := httptest.NewRecorder()
	handler.ServeHTTP(rec, req)
	if rec.Header().Get("Content-Encoding") != "" {
		t.Fatalf("expected no encoding")
	}
	if rec.Body.String() != "hi" {
		t.Fatalf("unexpected body: %s", rec.Body.String())
	}
}
