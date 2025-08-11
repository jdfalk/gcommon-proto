// file: perf/benchmarks/web_bench.go
// version: 1.1.0
// guid: 0e03a6a3-7b39-4696-ab4f-bbffb0c789c9

package benchmarks

import (
	"net/http"
	"net/http/httptest"
	"testing"
)

// BenchmarkHTTPThroughput measures HTTP request handling throughput.
func BenchmarkHTTPThroughput(b *testing.B) {
	srv := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		w.WriteHeader(http.StatusOK)
	}))
	defer srv.Close()
	client := srv.Client()
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		resp, err := client.Get(srv.URL)
		if err != nil {
			b.Fatalf("get: %v", err)
		}
		resp.Body.Close()
	}
}

// BenchmarkMiddlewareOverhead measures middleware chain overhead.
func BenchmarkMiddlewareOverhead(b *testing.B) {
	handler := http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {})
	mw := func(h http.Handler) http.Handler {
		return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
			h.ServeHTTP(w, r)
		})
	}
	wrapped := mw(mw(handler))
	req := httptest.NewRequest(http.MethodGet, "/", nil)
	w := httptest.NewRecorder()
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		wrapped.ServeHTTP(w, req)
	}
}

// BenchmarkSessionManagement measures session management performance.
func BenchmarkSessionManagement(b *testing.B) {
	sessions := make(map[string]string)
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		sessions["id"] = "value"
		_ = sessions["id"]
	}
}

// BenchmarkConcurrentConnections measures concurrent connection handling.
func BenchmarkConcurrentConnections(b *testing.B) {
	srv := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		w.WriteHeader(http.StatusOK)
	}))
	defer srv.Close()
	client := srv.Client()
	b.RunParallel(func(pb *testing.PB) {
		for pb.Next() {
			resp, err := client.Get(srv.URL)
			if err == nil {
				resp.Body.Close()
			}
		}
	})
}
