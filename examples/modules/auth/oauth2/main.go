// file: examples/modules/auth/oauth2/main.go
// version: 1.0.0
// guid: 071678a6-d2b4-4e69-a4b5-097c638da1f9

package main

import (
	"context"
	"fmt"
)

// TODO: Complete oauth2 example

func setup(ctx context.Context) error {
	// TODO: implement setup for oauth2
	return nil
}

func run(ctx context.Context) error {
	// TODO: run oauth2 logic
	fmt.Println("TODO: run oauth2")
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
