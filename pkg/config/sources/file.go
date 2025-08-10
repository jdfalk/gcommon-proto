// file: pkg/config/sources/file.go
// version: 1.0.0
// guid: 88888888-9999-aaaa-bbbb-cccccccccccc

package sources

import (
	"io/ioutil"
	"path/filepath"

	"github.com/jdfalk/gcommon/pkg/config"
	"github.com/jdfalk/gcommon/pkg/config/formats"
)

// FileSource loads configuration from a file using a decoder.
type FileSource struct {
	Path    string
	Decoder formats.Decoder
}

// Load reads and decodes the file.
func (f FileSource) Load() (map[string]interface{}, error) {
	data, err := ioutil.ReadFile(filepath.Clean(f.Path))
	if err != nil {
		return nil, err
	}
	if f.Decoder == nil {
		return nil, nil
	}
	return f.Decoder.Decode(data)
}

// TODO:
//  - Support glob patterns to load multiple files
//  - Allow specifying file permission expectations
//  - Provide options for atomic file reads
//  - Detect file format automatically based on extension
//  - Handle encrypted files with pluggable decryptors
//  - Emit file change events for dynamic reloads
//  - Document performance considerations for large files
//  - Offer include directives for composing configurations
//  - Validate file paths to prevent directory traversal
//  - Support remote file retrieval over HTTP/HTTPS
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
