// file: pkg/config/formats/toml.go
// version: 1.1.0
// guid: 11111111-2222-3333-4444-aaaaaaaabbbb

package formats

import "github.com/pelletier/go-toml/v2"

// TOMLDecoder decodes TOML configuration data using the
// `github.com/pelletier/go-toml/v2` package. The decoder converts raw
// TOML bytes into a generic `map[string]interface{}` for further
// processing by the configuration system.
//
// This implementation intentionally keeps the returned structure very
// simple to avoid imposing strong typing assumptions on callers. The
// resulting map can later be mapped to strongly typed structs if
// required by specific modules.
type TOMLDecoder struct{}

// Decode converts TOML bytes into a map.
func (TOMLDecoder) Decode(b []byte) (map[string]interface{}, error) {
	var m map[string]interface{}
	if err := toml.Unmarshal(b, &m); err != nil {
		return nil, err
	}
	return m, nil
}

// TODO:
//  - Evaluate available TOML libraries and select one with minimal dependencies
//  - Support float, integer, boolean, array, and table types
//  - Preserve comments and ordering when round-tripping
//  - Allow custom struct tags for mapping to strongly typed configs
//  - Provide detailed error messages with line numbers
//  - Handle large files efficiently with streaming decoder
//  - Add examples demonstrating nested structures
//  - Write tests for edge cases such as multiline strings
//  - Document differences between TOML versions
//  - Support environment variable expansion in values
//  - Consider including schema validation via JSON schema
//  - Integrate with watch system for dynamic reloads
//  - Expose options for using alternate key delimiters
//  - Provide migration helpers for converting from YAML/JSON
//  - Add benchmarks comparing decoding performance
//  - Handle circular references gracefully
//  - Support custom value transformers
//  - Offer helper for merging multiple TOML documents
//  - Include utility to marshal config back to TOML
//  - Assess security implications of untrusted input
