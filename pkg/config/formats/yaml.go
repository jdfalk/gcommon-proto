// file: pkg/config/formats/yaml.go
// version: 1.0.0
// guid: eeeeeeee-ffff-1111-2222-333333333333

package formats

import "gopkg.in/yaml.v3"

// YAMLDecoder decodes YAML configuration data.
type YAMLDecoder struct{}

// Decode converts YAML bytes into a map.
func (YAMLDecoder) Decode(b []byte) (map[string]interface{}, error) {
	var m map[string]interface{}
	if err := yaml.Unmarshal(b, &m); err != nil {
		return nil, err
	}
	return m, nil
}

// TODO:
//  - Support custom struct tags and strict mode
//  - Implement schema validation while decoding
//  - Preserve YAML anchors and aliases
//  - Provide detailed error messages with line numbers
//  - Handle large files with streaming decoder
//  - Offer options for case sensitivity
//  - Add examples showcasing complex YAML structures
//  - Benchmark decoding performance
//  - Support merging multiple YAML documents
//  - Investigate security considerations for untrusted YAML
