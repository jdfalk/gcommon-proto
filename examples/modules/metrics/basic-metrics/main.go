// file: examples/modules/metrics/basic-metrics/main.go
// version: 1.0.0
// guid: 085a36c1-0992-4b71-be20-339d80353c42

package main

import (
	"context"
	"fmt"
)

// TODO: Complete basic-metrics example

func setup(ctx context.Context) error {
	// TODO: implement setup for basic-metrics
	return nil
}

func run(ctx context.Context) error {
	// TODO: run basic-metrics logic
	fmt.Println("TODO: run basic-metrics")
	return nil
}

func main() {
	ctx := context.Background()
	if err := setup(ctx); err != nil {
		panic(err)
	}
	if err := run(ctx); err != nil {
		panic(err)
	}
}
