// file: sdks/go/v1/database/go.mod
// version: 1.2.0
// guid: abcdef01-2345-6789-abcd-ef0123456789

module github.com/jdfalk/gcommon/sdks/go/v1/database

go 1.23

require (
	google.golang.org/protobuf v1.34.2
	google.golang.org/grpc v1.65.0
	github.com/jdfalk/gcommon/sdks/go/v1/common v1.3.0
)

require (
	golang.org/x/net v0.28.0 // indirect
	golang.org/x/sys v0.24.0 // indirect
	golang.org/x/text v0.17.0 // indirect
	google.golang.org/genproto/googleapis/rpc v0.0.0-20240730163845-b1a4ccb954bf // indirect
)

replace (
	github.com/jdfalk/gcommon/sdks/go/v1/common => ../common
)
