// file: examples/modules/web/basic-server/main.go
// version: 1.0.0
// guid: ab7f444d-5887-4349-b17f-e34dc1e4204a

package main

import (
	"context"
	"fmt"
)

// TODO: Complete basic-server example

func setup(ctx context.Context) error {
	// TODO: implement setup for basic-server
	return nil
}

func run(ctx context.Context) error {
	// TODO: run basic-server logic
	fmt.Println("TODO: run basic-server")
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
