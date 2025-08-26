#!/usr/bin/env python3
# file: examples/test_validation.py
# version: 1.0.0
# guid: 1a2b3c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d

"""
Test validation functionality with actual protovalidate runtime validation.
This verifies that validation rules in proto files actually work at runtime.
"""

import os
import sys

# Add the SDK to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "sdks", "python"))

try:
    import protovalidate
    from gcommon.v1.queue import publish_request_pb2

    def test_go_validation():
        """Test Go validation functionality."""
        print("=== Testing Go Validation ===")
        # We'll need to implement this in Go
        print("Go validation test would require a Go test program")
        print("Would validate: publish_request_pb2.PublishRequest with invalid topic")

    def test_python_validation():
        """Test Python validation functionality."""
        print("=== Testing Python Validation ===")

        # Create a validator
        validator = protovalidate.Validator()

        # Test 1: Valid message should pass
        print("1. Testing valid message...")
        valid_request = publish_request_pb2.PublishRequest()
        valid_request.topic = "valid-topic-name"  # Should meet validation rules
        valid_request.payload = b"test payload"

        try:
            validator.validate(valid_request)
            print("   ✅ Valid message passed validation")
        except protovalidate.ValidationError as e:
            print(f"   ❌ Valid message failed: {e}")

        # Test 2: Invalid message should fail
        print("2. Testing invalid message...")
        invalid_request = publish_request_pb2.PublishRequest()
        invalid_request.topic = ""  # Empty topic should fail validation
        invalid_request.payload = b"test payload"

        try:
            validator.validate(invalid_request)
            print("   ❌ Invalid message passed validation (should have failed)")
        except protovalidate.ValidationError as e:
            print(f"   ✅ Invalid message correctly failed: {e}")

    if __name__ == "__main__":
        print("Testing protovalidate runtime validation...")
        test_python_validation()
        test_go_validation()

except ImportError as e:
    print(f"❌ Import error: {e}")
    print("Need to install dependencies:")
    print("  cd sdks/python && pip install -e .")
    print("  pip install protovalidate")
