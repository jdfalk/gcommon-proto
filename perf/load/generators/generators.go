// file: perf/load/generators/generators.go
// version: 1.0.0
// guid: 9e819fd0-172f-46fd-9a3c-1ff30221fceb

// Package generators provides load generators.
package generators

// Generator produces load against the system under test.
type Generator interface {
	Start() error
	Stop() error
}
