// file: examples/modules/notification/templates/main.go
// version: 1.0.0
// guid: ea1574a6-7374-4711-8656-e5810f166f60

package main

import (
	"context"
	"fmt"
)

// TODO: Complete templates example

func setup(ctx context.Context) error {
	// TODO: implement setup for templates
	return nil
}

func run(ctx context.Context) error {
	// TODO: run templates logic
	fmt.Println("TODO: run templates")
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
