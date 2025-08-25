// file: go.mod
// version: 1.2.0
// guid: f1e2d3c4-b5a6-9798-8c7b-6a5958473629

module github.com/jdfalk/gcommon

go 1.23

replace github.com/jdfalk/gcommon/proto => ./sdks/go/v1

require google.golang.org/protobuf v1.36.8 // indirect
