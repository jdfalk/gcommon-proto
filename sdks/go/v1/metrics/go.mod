// file: sdks/go/v1/metrics/go.mod
// version: 1.3.0
// guid: abcdef01-2345-6789-abcd-ef0123456789

module github.com/jdfalk/gcommon/sdks/go/v1/metrics

go 1.23.0

toolchain go1.23.12

require (
	buf.build/gen/go/bufbuild/protovalidate/protocolbuffers/go v1.36.6-20250717165733-d22d418d82d8.1
	github.com/jdfalk/gcommon/sdks/go/v1/common v1.3.0
	google.golang.org/grpc v1.75.0
	google.golang.org/protobuf v1.36.8
)

require (
	golang.org/x/net v0.43.0 // indirect
	golang.org/x/sys v0.35.0 // indirect
	golang.org/x/text v0.28.0 // indirect
	google.golang.org/genproto/googleapis/rpc v0.0.0-20250707201910-8d1bb00bc6a7 // indirect
)

replace github.com/jdfalk/gcommon/sdks/go/v1/common => ../common
