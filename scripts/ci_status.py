#!/usr/bin/env python3
# file: scripts/ci_status.py
# version: 1.0.0
# guid: 9e1a2b3c-4d5e-6f7a-8b9c-0d1e2f3a4b5d

import sys

def print_status(msg: str):
    print(f"::notice ::[STATUS] {msg}")

def print_error(msg: str):
    print(f"::error ::[ERROR] {msg}", file=sys.stderr)

def print_success(msg: str):
    print(f"::notice ::[SUCCESS] {msg}")

def print_summary(msg: str):
    print(f"::notice ::[SUMMARY] {msg}")

# Usage:
# print_status("Starting job...")
# print_error("Failed to process file")
# print_success("Job completed successfully")
# print_summary("Processed 5 files, 2 errors")
