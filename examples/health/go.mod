module github.com/jdfalk/gcommon/examples/health

go 1.21

require (
	github.com/jdfalk/gcommon v0.0.0
	github.com/prometheus/client_golang v1.19.0
	google.golang.org/grpc v1.60.1
	k8s.io/api v0.29.0
	k8s.io/apimachinery v0.29.0
	k8s.io/client-go v0.29.0
)

replace github.com/jdfalk/gcommon => ../..
