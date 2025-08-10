// file: pkg/config/formats/decoder.go
// version: 1.0.0
// guid: dddddddd-eeee-ffff-1111-222222222222

package formats

// Decoder converts raw bytes into a configuration map.
type Decoder interface {
	Decode([]byte) (map[string]interface{}, error)
}
