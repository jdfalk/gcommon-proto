// file: examples/getting-started/first-app/main.go
// version: 1.0.0
// guid: a2eaf657-6cd4-4015-88b7-456534fdd008

package main

import (
	"context"
	"fmt"
)

// TODO: Complete first-app example

func setup(ctx context.Context) error {
	// TODO: implement setup for first-app
	return nil
}

func run(ctx context.Context) error {
	// TODO: run first-app logic
	fmt.Println("TODO: run first-app")
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
