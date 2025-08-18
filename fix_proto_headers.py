#!/usr/bin/env python3
# file: fix_proto_headers.py
# version: 1.0.0
# guid: 12345678-1234-5678-9abc-def012345678

import glob
import os
import re
import uuid


def generate_guid():
    """Generate a new GUID"""
    return str(uuid.uuid4())


def extract_package_from_path(proto_path):
    """Extract expected package name from file path"""
    # Remove 'proto/' prefix and '.proto' suffix
    path_parts = proto_path.replace("proto/", "").replace(".proto", "").split("/")
    return ".".join(path_parts)


def extract_go_package_from_path(proto_path):
    """Extract expected go_package from file path"""
    # Remove '.proto' suffix
    path_without_ext = proto_path.replace(".proto", "")
    return f"github.com/jdfalk/gcommon/proto/{path_without_ext}"


def fix_proto_file(file_path):
    """Fix a single proto file's header and package declarations"""

    # Calculate relative path from repo root
    repo_root = "/Users/jdfalk/repos/github.com/jdfalk/gcommon"
    rel_path = os.path.relpath(file_path, repo_root)

    with open(file_path, "r") as f:
        content = f.read()

    lines = content.split("\n")

    # Extract expected values from path
    expected_package = extract_package_from_path(rel_path)
    expected_go_package = extract_go_package_from_path(rel_path)

    # Track what we need to fix
    needs_file_header = True
    needs_version = True
    needs_guid = True
    needs_package_fix = False
    needs_go_package_fix = False

    # Find existing headers and check package
    file_header_line = -1
    version_line = -1
    guid_line = -1
    package_line = -1
    go_package_line = -1

    for i, line in enumerate(lines):
        if line.startswith("// file:"):
            file_header_line = i
            # Check if path is correct
            current_path = line.replace("// file: ", "").strip()
            if current_path != rel_path:
                needs_file_header = True
            else:
                needs_file_header = False

        elif line.startswith("// version:"):
            version_line = i
            needs_version = False

        elif line.startswith("// guid:"):
            guid_line = i
            needs_guid = False

        elif line.startswith("package "):
            package_line = i
            current_package = line.replace("package ", "").replace(";", "").strip()
            if current_package != expected_package:
                needs_package_fix = True

        elif "option go_package" in line:
            go_package_line = i
            # Extract current go_package value
            match = re.search(r'option go_package = "([^"]+)"', line)
            if match:
                current_go_package = match.group(1)
                if current_go_package != expected_go_package:
                    needs_go_package_fix = True

    # Apply fixes
    modified = False

    # Fix file header
    if needs_file_header:
        if file_header_line >= 0:
            lines[file_header_line] = f"// file: {rel_path}"
        else:
            # Insert at beginning
            lines.insert(0, f"// file: {rel_path}")
            # Adjust other line numbers
            if version_line >= 0:
                version_line += 1
            if guid_line >= 0:
                guid_line += 1
            if package_line >= 0:
                package_line += 1
            if go_package_line >= 0:
                go_package_line += 1
        modified = True

    # Add version if missing
    if needs_version:
        if version_line >= 0:
            # Version exists but may need updating - skip for now
            pass
        else:
            # Find insertion point (after file header)
            insert_pos = 1 if file_header_line >= 0 or needs_file_header else 0
            lines.insert(insert_pos, "// version: 1.0.0")
            # Adjust other line numbers
            if guid_line >= 0:
                guid_line += 1
            if package_line >= 0:
                package_line += 1
            if go_package_line >= 0:
                go_package_line += 1
        modified = True

    # Add GUID if missing
    if needs_guid:
        if guid_line >= 0:
            # GUID exists but may need updating - skip for now
            pass
        else:
            # Find insertion point (after version)
            insert_pos = (
                2
                if (file_header_line >= 0 or needs_file_header)
                and (version_line >= 0 or needs_version)
                else 1
            )
            lines.insert(insert_pos, f"// guid: {generate_guid()}")
            # Adjust other line numbers
            if package_line >= 0:
                package_line += 1
            if go_package_line >= 0:
                go_package_line += 1
        modified = True

    # Fix package declaration
    if needs_package_fix and package_line >= 0:
        lines[package_line] = f"package {expected_package};"
        modified = True

    # Fix go_package option
    if needs_go_package_fix and go_package_line >= 0:
        # Preserve the line structure, just replace the package value
        lines[go_package_line] = re.sub(
            r'option go_package = "[^"]+";',
            f'option go_package = "{expected_go_package}";',
            lines[go_package_line],
        )
        modified = True

    # Write back if modified
    if modified:
        with open(file_path, "w") as f:
            f.write("\n".join(lines))
        print(f"Fixed: {rel_path}")
        return True
    else:
        print(f"No changes needed: {rel_path}")
        return False


def main():
    """Main function to process all proto files"""
    repo_root = "/Users/jdfalk/repos/github.com/jdfalk/gcommon"
    proto_pattern = os.path.join(repo_root, "proto", "**", "*.proto")

    proto_files = glob.glob(proto_pattern, recursive=True)
    print(f"Found {len(proto_files)} proto files")

    fixed_count = 0
    for proto_file in proto_files:
        try:
            if fix_proto_file(proto_file):
                fixed_count += 1
        except Exception as e:
            print(f"Error processing {proto_file}: {e}")

    print(f"\nFixed {fixed_count} files out of {len(proto_files)} total files")


if __name__ == "__main__":
    main()
