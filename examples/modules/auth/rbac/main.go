// file: examples/modules/auth/rbac/main.go
// version: 1.0.0
// guid: a0c64564-2845-4701-9fe6-5d84fc2de0d6

package main

import (
	"context"
	"fmt"
)

// TODO: Complete rbac example

func setup(ctx context.Context) error {
	// TODO: implement setup for rbac
	return nil
}

func run(ctx context.Context) error {
	// TODO: run rbac logic
	fmt.Println("TODO: run rbac")
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
