// file: examples/test_validation.go
// version: 1.0.0
// guid: 2b3c4d5e-6f7a-8b9c-0d1e-2f3a4b5c6d7e

// Test validation functionality with actual protovalidate runtime validation.
// This verifies that validation rules in proto files actually work at runtime.
package main

import (
	"fmt"
	"log"

	"buf.build/go/protovalidate"
	queuev1 "github.com/jdfalk/gcommon/sdks/go/v1/queue"
)

func testGoValidation() {
	fmt.Println("=== Testing Go Validation ===")

	// Create a validator
	validator, err := protovalidate.New()
	if err != nil {
		log.Fatalf("Failed to create validator: %v", err)
	}

	// Test 1: Valid message should pass
	fmt.Println("1. Testing valid message...")
	validRequest := &queuev1.QueuePublishRequest{}
	validRequest.SetTopicName("valid-topic-name") // Should meet validation rules (3-255 chars, alphanumeric with dots/hyphens)

	if err := validator.Validate(validRequest); err != nil {
		fmt.Printf("   ❌ Valid message failed: %v\n", err)
	} else {
		fmt.Println("   ✅ Valid message passed validation")
	}

	// Test 2: Invalid message should fail
	fmt.Println("2. Testing invalid message...")
	invalidRequest := &queuev1.QueuePublishRequest{}
	invalidRequest.SetTopicName("") // Empty topic should fail validation (required, min 3 chars)

	if err := validator.Validate(invalidRequest); err != nil {
		fmt.Printf("   ✅ Invalid message correctly failed: %v\n", err)
	} else {
		fmt.Println("   ❌ Invalid message passed validation (should have failed)")
	}
}

func main() {
	fmt.Println("Testing protovalidate runtime validation...")
	testGoValidation()
}
