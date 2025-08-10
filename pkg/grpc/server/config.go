// file: pkg/grpc/server/config.go
// version: 1.0.0
// guid: 96fc0ab4-11ca-43cc-9132-1e6b69be0c27

package server

import "google.golang.org/grpc"

// Config captures basic gRPC server configuration.
type Config struct {
	Address    string
	UnaryInts  []grpc.UnaryServerInterceptor
	StreamInts []grpc.StreamServerInterceptor
	ServerOpts []grpc.ServerOption
}

// Build constructs a GRPCServer based on the configuration.
func (c Config) Build() *Server {
	opts := append([]grpc.ServerOption{}, c.ServerOpts...)
	if len(c.UnaryInts) > 0 {
		opts = append(opts, grpc.ChainUnaryInterceptor(c.UnaryInts...))
	}
	if len(c.StreamInts) > 0 {
		opts = append(opts, grpc.ChainStreamInterceptor(c.StreamInts...))
	}
	return NewServer(c.Address, opts...)
}
