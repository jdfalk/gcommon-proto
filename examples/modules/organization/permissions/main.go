// file: examples/modules/organization/permissions/main.go
// version: 1.0.0
// guid: e7d0afdf-22b6-4061-bd43-2b5a8a9f274c

package main

import (
	"context"
	"fmt"
)

// TODO: Complete permissions example

func setup(ctx context.Context) error {
	// TODO: implement setup for permissions
	return nil
}

func run(ctx context.Context) error {
	// TODO: run permissions logic
	fmt.Println("TODO: run permissions")
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
