// file: examples/modules/notification/multi-channel/main.go
// version: 1.0.0
// guid: 05c1b122-1352-4fe9-9d8f-936bd8a98c07

package main

import (
	"context"
	"fmt"
)

// TODO: Complete multi-channel example

func setup(ctx context.Context) error {
	// TODO: implement setup for multi-channel
	return nil
}

func run(ctx context.Context) error {
	// TODO: run multi-channel logic
	fmt.Println("TODO: run multi-channel")
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
