#!/usr/bin/env python3
# file: add_go_package_all.py
# version: 1.0.0
# guid: 8c9d0e1f-2a3b-4c5d-6e7f-8a9b0c1d2e3f

import glob
import os
import re


def add_go_package_option(file_path):
    """Add go_package option to a proto file if it doesn't exist."""
    with open(file_path, "r") as f:
        content = f.read()

    # Skip if go_package already exists
    if "option go_package" in content:
        print(f"Skipping {file_path} - go_package already exists")
        return False

    # Extract package from proto file
    package_match = re.search(r"package\s+([^;]+);", content)
    if not package_match:
        print(f"Warning: No package found in {file_path}")
        return False

    proto_package = package_match.group(1)

    # Determine the Go package path based on the proto package and file path
    if "common" in proto_package:
        go_package = "github.com/jdfalk/gcommon/pkg/common/proto"
    elif "config" in proto_package:
        go_package = "github.com/jdfalk/gcommon/pkg/config/proto"
    elif "auth" in proto_package:
        go_package = "github.com/jdfalk/gcommon/pkg/auth/proto"
    elif "cache" in proto_package:
        go_package = "github.com/jdfalk/gcommon/pkg/cache/proto"
    elif "db" in proto_package:
        go_package = "github.com/jdfalk/gcommon/pkg/db/proto"
    elif "health" in proto_package:
        go_package = "github.com/jdfalk/gcommon/pkg/health/proto"
    elif "metrics" in proto_package:
        go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto"
    elif "notification" in proto_package:
        go_package = "github.com/jdfalk/gcommon/pkg/notification/proto"
    elif "organization" in proto_package:
        go_package = "github.com/jdfalk/gcommon/pkg/organization/proto"
    elif "queue" in proto_package:
        go_package = "github.com/jdfalk/gcommon/pkg/queue/proto"
    elif "web" in proto_package:
        go_package = "github.com/jdfalk/gcommon/pkg/web/proto"
    else:
        print(f"Warning: Unknown package type in {file_path}: {proto_package}")
        return False

    # Find the position to insert go_package option
    # Look for the package line
    package_line_match = re.search(r"(package\s+[^;]+;\s*\n)", content)
    if not package_line_match:
        print(f"Warning: Could not find package line in {file_path}")
        return False

    # Find end of imports section
    import_section_end = package_line_match.end()

    # Look for imports and find the end
    import_matches = list(re.finditer(r'import\s+"[^"]+";', content))
    if import_matches:
        import_section_end = import_matches[-1].end()
        # Add newline after last import
        if not content[import_section_end : import_section_end + 1] == "\n":
            import_section_end += 1

    # Insert go_package option
    go_package_line = f'\noption go_package = "{go_package}";\n'

    # Insert the go_package option
    content = (
        content[:import_section_end] + go_package_line + content[import_section_end:]
    )

    # Write back to file
    with open(file_path, "w") as f:
        f.write(content)

    print(f"Added go_package to {file_path}")
    return True


def main():
    # Process all proto files in all modules
    all_proto_files = glob.glob(
        "/Users/jdfalk/repos/github.com/jdfalk/gcommon/pkg/**/proto/**/*.proto",
        recursive=True,
    )

    added_count = 0
    skipped_count = 0

    for file_path in all_proto_files:
        if os.path.isfile(file_path):
            result = add_go_package_option(file_path)
            if result:
                added_count += 1
            else:
                skipped_count += 1

    print("\nSummary:")
    print(f"Added go_package to {added_count} files")
    print(f"Skipped {skipped_count} files (already had go_package)")


if __name__ == "__main__":
    main()
