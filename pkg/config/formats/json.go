// file: pkg/config/formats/json.go
// version: 1.0.0
// guid: ffffffff-1111-2222-3333-444444444444

package formats

import "encoding/json"

// JSONDecoder decodes JSON configuration data.
type JSONDecoder struct{}

// Decode converts JSON bytes into a map.
func (JSONDecoder) Decode(b []byte) (map[string]interface{}, error) {
	var m map[string]interface{}
	if err := json.Unmarshal(b, &m); err != nil {
		return nil, err
	}
	return m, nil
}

// TODO:
//  - Support decoding into strongly typed structures
//  - Validate against JSON Schema
//  - Allow custom number parsing behavior
//  - Provide options for strict and lenient modes
//  - Add examples for nested and array-based configs
//  - Stream large JSON files to reduce memory usage
//  - Offer error paths to indicate location of failures
//  - Integrate with environment variable expansion
//  - Benchmark decoding performance vs other formats
//  - Document security considerations for untrusted JSON
