// file: pkg/web/routing/router_test.go
// version: 1.0.0
// guid: 2af3c1d2-e3f4-5a6b-7c8d-9e0f1a2b3c4d

package routing

import (
	"net/http"
	"net/http/httptest"
	"testing"
)

func TestRouterMatch(t *testing.T) {
	r := NewRouter()
	r.Register(http.MethodGet, "/users/:id", http.HandlerFunc(func(w http.ResponseWriter, req *http.Request) {
		params := Params(req)
		if params["id"] != "42" {
			t.Fatalf("expected id 42, got %s", params["id"])
		}
		w.WriteHeader(http.StatusOK)
	}))

	req := httptest.NewRequest(http.MethodGet, "/users/42", nil)
	rec := httptest.NewRecorder()
	r.ServeHTTP(rec, req)
	if rec.Code != http.StatusOK {
		t.Fatalf("expected 200, got %d", rec.Code)
	}
}

func TestRouterNotFound(t *testing.T) {
	r := NewRouter()
	req := httptest.NewRequest(http.MethodGet, "/unknown", nil)
	rec := httptest.NewRecorder()
	r.ServeHTTP(rec, req)
	if rec.Code != http.StatusNotFound {
		t.Fatalf("expected 404, got %d", rec.Code)
	}
}

func TestRouterMethod(t *testing.T) {
	r := NewRouter()
	r.Register(http.MethodPost, "/thing", http.HandlerFunc(func(w http.ResponseWriter, req *http.Request) {
		w.WriteHeader(http.StatusCreated)
	}))
	// GET should not match
	req := httptest.NewRequest(http.MethodGet, "/thing", nil)
	rec := httptest.NewRecorder()
	r.ServeHTTP(rec, req)
	if rec.Code != http.StatusNotFound {
		t.Fatalf("expected 404, got %d", rec.Code)
	}
	// POST should match
	req = httptest.NewRequest(http.MethodPost, "/thing", nil)
	rec = httptest.NewRecorder()
	r.ServeHTTP(rec, req)
	if rec.Code != http.StatusCreated {
		t.Fatalf("expected 201, got %d", rec.Code)
	}
}
