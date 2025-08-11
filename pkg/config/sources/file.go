// file: pkg/config/sources/file.go
// version: 1.2.1
// guid: 88888888-9999-aaaa-bbbb-cccccccccccc

package sources

import (
	"fmt"
	"io"
	"net/http"
	"os"
	"path/filepath"
	"strings"

	"github.com/jdfalk/gcommon/pkg/config"
	"github.com/jdfalk/gcommon/pkg/config/formats"
)

// FileSource loads configuration from one or more files or URLs using a
// decoder. When multiple files are specified, configurations are merged in the
// order provided with later files taking precedence.
type FileSource struct {
	Path    string   // single path (deprecated in favour of Paths)
	Paths   []string // multiple paths or glob patterns
	Decoder formats.Decoder
	Client  *http.Client // optional HTTP client for remote files
}

// Load reads and decodes all configured files. If a path contains glob
// patterns, all matching files are processed. Remote HTTP/HTTPS URLs are
// retrieved using the provided client or http.DefaultClient.
func (f FileSource) Load() (map[string]interface{}, error) {
	paths := make([]string, 0, len(f.Paths)+1)
	if f.Path != "" {
		paths = append(paths, f.Path)
	}
	paths = append(paths, f.Paths...)
	if len(paths) == 0 {
		return nil, fmt.Errorf("no configuration paths provided")
	}

	result := make(map[string]interface{})
	for _, p := range paths {
		matches, err := expandPath(p)
		if err != nil {
			return nil, err
		}
		for _, m := range matches {
			data, err := f.read(m)
			if err != nil {
				return nil, err
			}
			dec := f.Decoder
			if dec == nil {
				dec = decoderForPath(m)
				if dec == nil {
					return nil, fmt.Errorf("unsupported configuration format: %s", m)
				}
			}
			cfg, err := dec.Decode(data)
			if err != nil {
				return nil, err
			}
			if err := mergeMaps(result, cfg); err != nil {
				return nil, err
			}
		}
	}
	return result, nil
}

// read returns file contents from local disk or remote URL.
func (f FileSource) read(path string) ([]byte, error) {
	if strings.HasPrefix(path, "http://") || strings.HasPrefix(path, "https://") {
		client := f.Client
		if client == nil {
			client = http.DefaultClient
		}
		resp, err := client.Get(path)
		if err != nil {
			return nil, err
		}
		defer resp.Body.Close()
		return io.ReadAll(resp.Body)
	}
	return os.ReadFile(filepath.Clean(path))
}

// decoderForPath picks a decoder based on file extension.
func decoderForPath(path string) formats.Decoder {
	switch strings.ToLower(filepath.Ext(path)) {
	case ".yaml", ".yml":
		return formats.YAMLDecoder{}
	case ".json":
		return formats.JSONDecoder{}
	case ".toml":
		return formats.TOMLDecoder{}
	case ".env":
		return formats.EnvDecoder{}
	default:
		return nil
	}
}

// expandPath expands glob patterns. If no pattern characters are present the
// original path is returned.
func expandPath(p string) ([]string, error) {
	if strings.ContainsAny(p, "*?[") {
		matches, err := filepath.Glob(p)
		if err != nil {
			return nil, err
		}
		return matches, nil
	}
	return []string{p}, nil
}

// mergeMaps merges src into dst with src taking precedence on conflicts.
func mergeMaps(dst, src map[string]interface{}) error {
	for k, v := range src {
		dst[k] = v
	}
	return nil
}

// TODO:
//  - Allow specifying file permission expectations
//  - Provide options for atomic file reads
//  - Detect file format automatically based on extension
//  - Handle encrypted files with pluggable decryptors
//  - Emit file change events for dynamic reloads
//  - Document performance considerations for large files
//  - Offer include directives for composing configurations
//  - Validate file paths to prevent directory traversal
//  - Add unit tests covering missing files and permissions
//  - Provide examples for layering multiple file sources
//  - Integrate with watcher for real-time updates
//  - Implement checksum verification to detect corruption
//  - Allow custom file decoding per directory
//  - Provide CLI tool to inspect file configuration
//  - Cache file contents to reduce disk I/O
//  - Expose metrics for load duration and file size
//  - Add context support for cancellation
//  - Evaluate memory-mapped file reading for performance

var _ config.ConfigSource = (*FileSource)(nil)
