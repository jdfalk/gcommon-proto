// file: go.mod
// version: 1.2.0
// guid: f1e2d3c4-b5a6-9798-8c7b-6a5958473629

module github.com/jdfalk/gcommon

go 1.23

replace github.com/jdfalk/gcommon/proto => ./sdks/go/gcommon/v1

require (
	github.com/jdfalk/gcommon/proto v0.0.0-00010101000000-000000000000
	google.golang.org/protobuf v1.36.7
	google.golang.org/grpc v1.69.2
)
