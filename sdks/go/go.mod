// file: sdks/go/go.mod
// version: 1.0.0
// guid: 3b7a6f29-9c4e-4b9e-8c1a-2b6f9d1e7a2c

module github.com/jdfalk/gcommon/sdks/go

go 1.24.0

toolchain go1.24.6

require (
	buf.build/gen/go/bufbuild/protovalidate/protocolbuffers/go v1.36.9-20250912141014-52f32327d4b0.1
	google.golang.org/grpc v1.75.1
	google.golang.org/protobuf v1.36.9
)

require (
	golang.org/x/net v0.44.0 // indirect
	golang.org/x/sys v0.36.0 // indirect
	golang.org/x/text v0.29.0 // indirect
	google.golang.org/genproto/googleapis/rpc v0.0.0-20250908214217-97024824d090 // indirect
)
