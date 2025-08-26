// file: examples/go.mod
// version: 1.0.0
// guid: 3c4d5e6f-7a8b-9c0d-1e2f-3a4b5c6d7e8f

module github.com/jdfalk/gcommon/examples

go 1.23.0

toolchain go1.24.6

require (
	buf.build/go/protovalidate v0.14.0
	github.com/jdfalk/gcommon/sdks/go/v1/queue v1.3.0
)

require (
	buf.build/gen/go/bufbuild/protovalidate/protocolbuffers/go v1.36.6-20250717165733-d22d418d82d8.1 // indirect
	cel.dev/expr v0.23.1 // indirect
	github.com/antlr4-go/antlr/v4 v4.13.0 // indirect
	github.com/google/cel-go v0.25.0 // indirect
	github.com/jdfalk/gcommon/sdks/go/v1/common v1.3.0 // indirect
	github.com/jdfalk/gcommon/sdks/go/v1/metrics v1.3.0 // indirect
	github.com/jdfalk/gcommon/sdks/go/v1/organization v1.3.0 // indirect
	github.com/stoewer/go-strcase v1.3.0 // indirect
	golang.org/x/exp v0.0.0-20240325151524-a685a6edb6d8 // indirect
	golang.org/x/net v0.28.0 // indirect
	golang.org/x/sys v0.24.0 // indirect
	golang.org/x/text v0.23.0 // indirect
	google.golang.org/genproto/googleapis/api v0.0.0-20240826202546-f6391c0de4c7 // indirect
	google.golang.org/genproto/googleapis/rpc v0.0.0-20240826202546-f6391c0de4c7 // indirect
	google.golang.org/grpc v1.65.0 // indirect
	google.golang.org/protobuf v1.36.6 // indirect
)

replace github.com/jdfalk/gcommon/sdks/go => ../sdks/go
