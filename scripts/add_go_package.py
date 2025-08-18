#!/usr/bin/env python3
# file: add_go_package.py
# version: 1.0.0
# guid: 6a7b8c9d-0e1f-2a3b-4c5d-6e7f8a9b0c1d

import glob
import os
import re


def add_go_package_option(file_path):
    """Add go_package option to a proto file if it doesn't exist."""
    with open(file_path, "r") as f:
        content = f.read()

    # Skip if go_package already exists
    if "option go_package" in content:
        return False

    # Extract package from proto file
    package_match = re.search(r"package\s+([^;]+);", content)
    if not package_match:
        print(f"Warning: No package found in {file_path}")
        return False

    proto_package = package_match.group(1)

    # Convert proto package to Go package
    # gcommon.v1.common -> github.com/jdfalk/gcommon/pkg/common/proto/commonpb
    if "common" in proto_package:
        go_package = "github.com/jdfalk/gcommon/pkg/common/proto/commonpb"
    elif "config" in proto_package:
        go_package = "github.com/jdfalk/gcommon/pkg/config/proto/configpb"
    elif "auth" in proto_package:
        go_package = "github.com/jdfalk/gcommon/pkg/auth/proto/authpb"
    elif "cache" in proto_package:
        go_package = "github.com/jdfalk/gcommon/pkg/cache/proto/cachepb"
    elif "db" in proto_package:
        go_package = "github.com/jdfalk/gcommon/pkg/db/proto/dbpb"
    elif "health" in proto_package:
        go_package = "github.com/jdfalk/gcommon/pkg/health/proto/healthpb"
    elif "metrics" in proto_package:
        go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto/metricspb"
    elif "notification" in proto_package:
        go_package = "github.com/jdfalk/gcommon/pkg/notification/proto/notificationpb"
    elif "organization" in proto_package:
        go_package = "github.com/jdfalk/gcommon/pkg/organization/proto/organizationpb"
    elif "queue" in proto_package:
        go_package = "github.com/jdfalk/gcommon/pkg/queue/proto/queuepb"
    elif "web" in proto_package:
        go_package = "github.com/jdfalk/gcommon/pkg/web/proto/webpb"
    else:
        print(f"Warning: Unknown package type in {file_path}: {proto_package}")
        return False

    # Find the position to insert go_package option (after package declaration)
    package_line_match = re.search(r"(package\s+[^;]+;\s*\n)", content)
    if not package_line_match:
        print(f"Warning: Could not find package line in {file_path}")
        return False

    # Insert go_package option after package line and any imports
    import_section_end = content.find("option features.(pb.go).api_level")
    if import_section_end == -1:
        # Find end of imports
        import_matches = list(re.finditer(r'import\s+"[^"]+";', content))
        if import_matches:
            import_section_end = import_matches[-1].end()
        else:
            import_section_end = package_line_match.end()

    # Insert go_package option
    go_package_line = f'\noption go_package = "{go_package}";\n'

    # Insert after imports but before other options
    insertion_point = import_section_end
    content = content[:insertion_point] + go_package_line + content[insertion_point:]

    # Write back to file
    with open(file_path, "w") as f:
        f.write(content)

    print(f"Added go_package to {file_path}")
    return True


def main():
    # Process all proto files in the common module first
    common_files = glob.glob(
        "/Users/jdfalk/repos/github.com/jdfalk/gcommon/pkg/common/proto/**/*.proto",
        recursive=True,
    )

    for file_path in common_files:
        if os.path.isfile(file_path):
            add_go_package_option(file_path)


if __name__ == "__main__":
    main()
