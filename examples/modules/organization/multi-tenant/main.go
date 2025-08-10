// file: examples/modules/organization/multi-tenant/main.go
// version: 1.0.0
// guid: 95476e9a-bf81-480f-a3d4-48851dcf03c4

package main

import (
	"context"
	"fmt"
)

// TODO: Complete multi-tenant example

func setup(ctx context.Context) error {
	// TODO: implement setup for multi-tenant
	return nil
}

func run(ctx context.Context) error {
	// TODO: run multi-tenant logic
	fmt.Println("TODO: run multi-tenant")
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
