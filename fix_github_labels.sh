#!/bin/bash

# File: fix_github_labels.sh
# Purpose: Fix missing GitHub labels and update existing issues

set -e

echo "=== Fixing GitHub Labels and Issues ==="

# Function to create a label if it doesn't exist
create_label_if_not_exists() {
    local name="$1"
    local description="$2"
    local color="$3"

    if ! gh label list --search "$name" | grep -q "^$name"; then
        echo "Creating label: $name"
        gh label create "$name" --description "$description" --color "$color"
    else
        echo "Label already exists: $name"
    fi
}

# Create missing priority labels
echo "--- Creating Priority Labels ---"
create_label_if_not_exists "priority:high" "High priority" "D93F0B"
create_label_if_not_exists "priority:medium" "Medium priority" "FBCA04"
create_label_if_not_exists "priority:low" "Low priority" "1D76DB"

# Create missing size labels
echo "--- Creating Size Labels ---"
create_label_if_not_exists "size:small" "< 1 day work" "C2E0C6"
create_label_if_not_exists "size:medium" "1-3 days work" "FEF2C0"
create_label_if_not_exists "size:large" "1+ weeks work" "BFD4F2"

# Create missing type labels
echo "--- Creating Type Labels ---"
create_label_if_not_exists "type:performance" "Performance optimization" "C5DEF5"
create_label_if_not_exists "type:infrastructure" "Infrastructure and tooling" "E99695"

# Create missing status labels
echo "--- Creating Status Labels ---"
create_label_if_not_exists "status:in-progress" "Currently being worked on" "FBCA04"
create_label_if_not_exists "status:needs-review" "Needs review" "0075CA"

echo "--- Updating Existing Issues ---"

# Define issue mappings (issue_number:labels_to_add)
declare -A issue_labels
issue_labels[4]="module:auth,type:protobuf,priority:high,size:medium"
issue_labels[5]="module:auth,type:grpc,priority:high,size:large"
issue_labels[6]="module:auth,type:provider,priority:medium,size:large"
issue_labels[7]="module:auth,type:testing,priority:medium,size:medium"
issue_labels[8]="module:cache,type:protobuf,priority:high,size:medium"
issue_labels[9]="module:cache,type:grpc,priority:high,size:large"
issue_labels[10]="module:cache,type:provider,priority:medium,size:large"
issue_labels[11]="module:cache,type:testing,priority:medium,size:medium"
issue_labels[12]="module:config,type:protobuf,priority:high,size:medium"
issue_labels[13]="module:config,type:grpc,priority:high,size:large"
issue_labels[14]="module:config,type:provider,priority:high,size:large"
issue_labels[15]="module:config,type:testing,priority:medium,size:medium"
issue_labels[16]="module:database,type:protobuf,priority:high,size:medium"
issue_labels[17]="module:database,type:grpc,priority:high,size:large"
issue_labels[18]="module:database,type:provider,priority:high,size:large"
issue_labels[19]="module:database,type:testing,priority:high,size:medium"
issue_labels[20]="module:health,type:protobuf,priority:medium,size:small"
issue_labels[21]="module:health,type:grpc,priority:medium,size:medium"
issue_labels[22]="module:health,type:provider,priority:medium,size:medium"
issue_labels[23]="module:health,type:testing,priority:medium,size:small"
issue_labels[24]="module:logging,type:protobuf,priority:high,size:medium"
issue_labels[25]="module:logging,type:grpc,priority:high,size:large"
issue_labels[26]="module:logging,type:provider,priority:high,size:large"
issue_labels[27]="module:logging,type:testing,priority:medium,size:medium"
issue_labels[28]="module:metrics,type:protobuf,priority:high,size:medium"
issue_labels[29]="module:metrics,type:grpc,priority:high,size:large"
issue_labels[30]="module:metrics,type:provider,priority:high,size:large"
issue_labels[31]="module:metrics,type:testing,priority:medium,size:medium"
issue_labels[32]="module:queue,type:protobuf,priority:medium,size:medium"
issue_labels[33]="module:queue,type:grpc,priority:medium,size:large"
issue_labels[34]="module:queue,type:provider,priority:medium,size:large"
issue_labels[35]="module:queue,type:testing,priority:medium,size:medium"
issue_labels[36]="module:web,type:protobuf,priority:high,size:medium"
issue_labels[37]="module:web,type:grpc,priority:high,size:large"
issue_labels[38]="module:web,type:provider,priority:high,size:large"
issue_labels[39]="module:web,type:testing,priority:medium,size:medium"
issue_labels[40]="type:docs,priority:medium,size:medium"
issue_labels[41]="type:infrastructure,priority:high,size:large"

# Update each issue with its labels
for issue in "${!issue_labels[@]}"; do
    labels="${issue_labels[$issue]}"
    echo "Adding labels to issue #$issue: $labels"

    # Convert comma-separated labels to space-separated for gh CLI
    label_args=""
    IFS=',' read -ra LABEL_ARRAY <<< "$labels"
    for label in "${LABEL_ARRAY[@]}"; do
        label_args="$label_args --add-label $label"
    done

    # Add labels to issue
    eval "gh issue edit $issue $label_args"
done

echo "=== Label Fix Complete ==="
echo "Next: Create GitHub project manually or with updated CLI"
