// file: examples/getting-started/basic-setup/main.go
// version: 1.0.0
// guid: f47dcc6d-2d49-421d-bfce-b39ae5779d50

package main

import (
	"context"
	"fmt"
)

// TODO: Complete basic-setup example

func setup(ctx context.Context) error {
	// TODO: implement setup for basic-setup
	return nil
}

func run(ctx context.Context) error {
	// TODO: run basic-setup logic
	fmt.Println("TODO: run basic-setup")
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
