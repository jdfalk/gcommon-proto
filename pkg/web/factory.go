// file: pkg/web/factory.go
// version: 1.0.0
// guid: 3e9a918b-9bd2-4c18-9650-e3e2f8f8c1ad

package web

import proto "github.com/jdfalk/gcommon/pkg/web/proto"

// NewServer creates a new Server from the provided configuration.
func NewServer(cfg *proto.ServerConfig) Server {
	return NewHTTPServer(cfg)
}
