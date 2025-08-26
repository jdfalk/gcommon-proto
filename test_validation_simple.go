// file: test_validation_simple.go
// version: 1.0.0
// guid: 4c5d6e7f-8a9b-0c1d-2e3f-4a5b6c7d8e9f

// Simple validation test without importing SDK packages
package main

import (
	"fmt"
	"log"

	"buf.build/go/protovalidate"
)

func main() {
	fmt.Println("Testing protovalidate runtime validation...")
	fmt.Println("=== Testing Validator Creation ===")

	// Create a validator
	validator, err := protovalidate.New()
	if err != nil {
		log.Fatalf("❌ Failed to create validator: %v", err)
	}

	fmt.Println("✅ Protovalidate validator created successfully!")
	fmt.Printf("   Validator type: %T\n", validator)

	fmt.Println("\n=== Validation Setup Complete ===")
	fmt.Println("✅ protovalidate runtime library is properly installed and working")
	fmt.Println("✅ Ready to validate protobuf messages with validation rules")
	fmt.Println("\nNote: Full message validation requires resolving import cycles in generated code")
}
