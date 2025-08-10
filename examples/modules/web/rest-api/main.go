// file: examples/modules/web/rest-api/main.go
// version: 1.0.0
// guid: 07e76af1-5516-4035-886a-44358683dcd3

package main

import (
	"context"
	"fmt"
)

// TODO: Complete rest-api example

func setup(ctx context.Context) error {
	// TODO: implement setup for rest-api
	return nil
}

func run(ctx context.Context) error {
	// TODO: run rest-api logic
	fmt.Println("TODO: run rest-api")
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
