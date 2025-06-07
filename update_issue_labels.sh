#!/bin/bash

# File: update_issue_labels.sh
# Purpose: Add missing labels to existing GitHub issues

set -e

echo "=== Adding Labels to Existing Issues ==="

# Function to add labels to an issue
add_labels_to_issue() {
    local issue_num="$1"
    shift
    local labels=("$@")

    echo "Adding labels to issue #$issue_num: ${labels[*]}"

    # Build gh command with all labels
    local cmd="gh issue edit $issue_num"
    for label in "${labels[@]}"; do
        cmd="$cmd --add-label $label"
    done

    # Execute the command
    eval "$cmd"
}

# Update issues with their appropriate labels
add_labels_to_issue 4 "module:auth" "type:protobuf" "priority:high" "size:medium"
add_labels_to_issue 5 "module:auth" "type:grpc" "priority:high" "size:large"
add_labels_to_issue 6 "module:auth" "type:provider" "priority:medium" "size:large"
add_labels_to_issue 7 "module:auth" "type:testing" "priority:medium" "size:medium"
add_labels_to_issue 8 "module:cache" "type:protobuf" "priority:high" "size:medium"
add_labels_to_issue 9 "module:cache" "type:grpc" "priority:high" "size:large"
add_labels_to_issue 10 "module:cache" "type:provider" "priority:medium" "size:large"
add_labels_to_issue 11 "module:cache" "type:testing" "priority:medium" "size:medium"
add_labels_to_issue 12 "module:config" "type:protobuf" "priority:high" "size:medium"
add_labels_to_issue 13 "module:config" "type:grpc" "priority:high" "size:large"
add_labels_to_issue 14 "module:config" "type:provider" "priority:high" "size:large"
add_labels_to_issue 15 "module:config" "type:testing" "priority:medium" "size:medium"
add_labels_to_issue 16 "module:database" "type:protobuf" "priority:high" "size:medium"
add_labels_to_issue 17 "module:database" "type:grpc" "priority:high" "size:large"
add_labels_to_issue 18 "module:database" "type:provider" "priority:high" "size:large"
add_labels_to_issue 19 "module:database" "type:testing" "priority:high" "size:medium"
add_labels_to_issue 20 "module:health" "type:protobuf" "priority:medium" "size:small"
add_labels_to_issue 21 "module:health" "type:grpc" "priority:medium" "size:medium"
add_labels_to_issue 22 "module:health" "type:provider" "priority:medium" "size:medium"
add_labels_to_issue 23 "module:health" "type:testing" "priority:medium" "size:small"
add_labels_to_issue 24 "module:logging" "type:protobuf" "priority:high" "size:medium"
add_labels_to_issue 25 "module:logging" "type:grpc" "priority:high" "size:large"
add_labels_to_issue 26 "module:logging" "type:provider" "priority:high" "size:large"
add_labels_to_issue 27 "module:logging" "type:testing" "priority:medium" "size:medium"
add_labels_to_issue 28 "module:metrics" "type:protobuf" "priority:high" "size:medium"
add_labels_to_issue 29 "module:metrics" "type:grpc" "priority:high" "size:large"
add_labels_to_issue 30 "module:metrics" "type:provider" "priority:high" "size:large"
add_labels_to_issue 31 "module:metrics" "type:testing" "priority:medium" "size:medium"
add_labels_to_issue 32 "module:queue" "type:protobuf" "priority:medium" "size:medium"
add_labels_to_issue 33 "module:queue" "type:grpc" "priority:medium" "size:large"
add_labels_to_issue 34 "module:queue" "type:provider" "priority:medium" "size:large"
add_labels_to_issue 35 "module:queue" "type:testing" "priority:medium" "size:medium"
add_labels_to_issue 36 "module:web" "type:protobuf" "priority:high" "size:medium"
add_labels_to_issue 37 "module:web" "type:grpc" "priority:high" "size:large"
add_labels_to_issue 38 "module:web" "type:provider" "priority:high" "size:large"
add_labels_to_issue 39 "module:web" "type:testing" "priority:medium" "size:medium"
add_labels_to_issue 40 "type:docs" "priority:medium" "size:medium"
add_labels_to_issue 41 "type:infrastructure" "priority:high" "size:large"

echo "=== Label Updates Complete ==="
