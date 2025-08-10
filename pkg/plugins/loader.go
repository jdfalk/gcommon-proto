// file: pkg/plugins/loader.go
// version: 1.0.0
// guid: 9108a4e0-b6ed-43bc-8e7b-885394f2255f

package plugins

import (
	"errors"
	"plugin"
)

// Load dynamically loads a plugin descriptor from a shared object file.
func Load(path string) (Descriptor, error) {
	p, err := plugin.Open(path)
	if err != nil {
		return Descriptor{}, err
	}
	sym, err := p.Lookup("Descriptor")
	if err != nil {
		return Descriptor{}, err
	}
	d, ok := sym.(*Descriptor)
	if !ok {
		return Descriptor{}, errors.New("symbol Descriptor has wrong type")
	}
	return *d, nil
}
