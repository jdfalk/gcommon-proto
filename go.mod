module github.com/jdfalk/gcommon

go 1.22

replace github.com/jdfalk/gcommon/proto => ./sdks/go/v1

require (
	github.com/jdfalk/gcommon/proto v0.0.0-00010101000000-000000000000
	google.golang.org/protobuf v1.36.7
	google.golang.org/grpc v1.69.2
)
