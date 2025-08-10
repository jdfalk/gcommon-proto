// file: examples/modules/web/middleware-chain/main.go
// version: 1.0.0
// guid: 741c7190-08b8-4e06-9e6b-eb983ea61e5b

package main

import (
	"context"
	"fmt"
)

// TODO: Complete middleware-chain example

func setup(ctx context.Context) error {
	// TODO: implement setup for middleware-chain
	return nil
}

func run(ctx context.Context) error {
	// TODO: run middleware-chain logic
	fmt.Println("TODO: run middleware-chain")
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
