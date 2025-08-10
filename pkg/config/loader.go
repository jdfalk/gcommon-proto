// file: pkg/config/loader.go
// version: 1.0.0
// guid: 11111111-2222-3333-4444-555555555555

package config

import (
	"fmt"
	"sync"

	"github.com/jdfalk/gcommon/pkg/config/formats"
)

// Loader coordinates loading configuration from multiple sources using a decoder.
type Loader struct {
	mu      sync.Mutex
	sources []ConfigSource
	decoder formats.Decoder
}

// NewLoader creates a Loader with provided decoder and sources.
func NewLoader(dec formats.Decoder, srcs ...ConfigSource) *Loader {
	return &Loader{decoder: dec, sources: srcs}
}

// AddSource appends a new ConfigSource to the loader.
func (l *Loader) AddSource(src ConfigSource) {
	l.mu.Lock()
	defer l.mu.Unlock()
	l.sources = append(l.sources, src)
}

// Load reads configuration from all sources and merges them.
func (l *Loader) Load() (map[string]interface{}, error) {
	l.mu.Lock()
	defer l.mu.Unlock()
	result := make(map[string]interface{})
	for _, src := range l.sources {
		data, err := src.Load()
		if err != nil {
			return nil, fmt.Errorf("load source: %w", err)
		}
		if err := mergeMaps(result, data); err != nil {
			return nil, fmt.Errorf("merge source: %w", err)
		}
	}
	return result, nil
}

// mergeMaps merges src into dst overriding duplicate keys.
func mergeMaps(dst, src map[string]interface{}) error {
	for k, v := range src {
		dst[k] = v
	}
	return nil
}

// TODO:
//  - Support configuration format auto-detection
//  - Allow per-source decoders overriding the default
//  - Validate configuration while loading to fail fast
//  - Add context support for cancellation and deadlines
//  - Stream large configuration files to reduce memory usage
//  - Provide hooks for pre- and post-processing of loaded data
//  - Track source metadata for debugging and provenance
//  - Implement parallel loading for performance
//  - Retry failed sources with exponential backoff
//  - Expose progress metrics and logging
//  - Cache loaded configurations to minimize I/O
//  - Support encrypted configuration sources
//  - Implement pluggable decryption mechanisms
//  - Add examples for loading from multiple formats simultaneously
//  - Provide CLI for manual load and inspection
//  - Integrate with watcher for auto-reload
//  - Handle circular references in configuration files
//  - Offer template expansion for configuration values
//  - Document recommended directory layout for files
//  - Benchmark loading performance across formats
