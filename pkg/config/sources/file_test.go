// file: pkg/config/sources/file_test.go
// version: 1.0.0
// guid: 9c9e5e3b-5ba4-4fc6-9cb0-97a8821c6f91

package sources

import (
	"fmt"
	"os"
	"testing"

	"github.com/jdfalk/gcommon/pkg/config/formats"
)

// writeTempFile creates a temporary file with the given content and
// extension. The caller is responsible for cleaning up the file.
func writeTempFile(t *testing.T, ext, content string) string {
	t.Helper()
	f, err := os.CreateTemp(t.TempDir(), "cfg-*"+ext)
	if err != nil {
		t.Fatalf("CreateTemp failed: %v", err)
	}
	if _, err := f.WriteString(content); err != nil {
		t.Fatalf("WriteString failed: %v", err)
	}
	if err := f.Close(); err != nil {
		t.Fatalf("Close failed: %v", err)
	}
	return f.Name()
}

// TestFileSourceAutoDetect verifies that FileSource picks a decoder based on
// file extension when none is explicitly provided.
func TestFileSourceAutoDetect(t *testing.T) {
	cases := []struct {
		ext     string
		content string
		key     string
		value   interface{}
	}{
		{".yaml", "a: 1", "a", 1},
		{".yml", "a: 1", "a", 1},
		{".json", "{\"a\":2}", "a", float64(2)},
		{".toml", "a = 3", "a", float64(3)},
		{".env", "A=4", "A", "4"},
	}

	for _, c := range cases {
		path := writeTempFile(t, c.ext, c.content)
		fs := FileSource{Path: path}
		m, err := fs.Load()
		if err != nil {
			t.Fatalf("Load failed for %s: %v", c.ext, err)
		}
		if fmt.Sprint(m[c.key]) != fmt.Sprint(c.value) {
			t.Fatalf("expected %v for %s, got %v", c.value, c.ext, m[c.key])
		}
	}
}

// TestFileSourceCustomDecoder verifies providing a custom decoder overrides
// extension based detection.
func TestFileSourceCustomDecoder(t *testing.T) {
	path := writeTempFile(t, ".yaml", "ignored: true")
	fs := FileSource{Path: path, Decoder: formats.JSONDecoder{}}
	if _, err := fs.Load(); err == nil {
		t.Fatalf("expected decoder error but got nil")
	}
}

// TODO: add tests for error scenarios such as unsupported extensions,
// unreadable files, and invalid contents.
