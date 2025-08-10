// file: examples/modules/auth/middleware/main.go
// version: 1.0.0
// guid: 634e58e7-6cc3-4907-86de-b828484127aa

package main

import (
	"context"
	"fmt"
)

// TODO: Complete middleware example

func setup(ctx context.Context) error {
	// TODO: implement setup for middleware
	return nil
}

func run(ctx context.Context) error {
	// TODO: run middleware logic
	fmt.Println("TODO: run middleware")
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
