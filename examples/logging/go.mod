module github.com/jdfalk/gcommon/examples/logging

go 1.21

require (
	github.com/jdfalk/gcommon v0.0.0
	github.com/sirupsen/logrus v1.9.3
	go.uber.org/zap v1.26.0
)

replace github.com/jdfalk/gcommon => ../..
