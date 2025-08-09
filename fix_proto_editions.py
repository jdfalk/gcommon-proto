#!/usr/bin/env python3
# file: fix_proto_editions.py
# version: 1.0.0
# guid: b2c3d4e5-f6a7-8901-bcde-f23456789012

"""
Fix protobuf files to be compatible with Edition 2023.
Replace 'optional' with proper field features.
"""

import os
import re


def fix_optional_fields(content: str) -> str:
    """Replace 'optional' keyword with proper field syntax for Edition 2023."""
    # In Edition 2023, just remove 'optional' keyword - implicit presence is default
    optional_pattern = r"(\s+)optional\s+(\w+)\s+(\w+)\s*=\s*(\d+);"

    def replace_optional(match):
        indent = match.group(1)
        field_type = match.group(2)
        field_name = match.group(3)
        field_number = match.group(4)

        # Just remove 'optional' - in Edition 2023, fields are implicitly optional
        return f"{indent}{field_type} {field_name} = {field_number};"

    return re.sub(optional_pattern, replace_optional, content)


def remove_duplicate_definitions(content: str) -> str:
    """Remove duplicate message definitions that conflict with existing ones."""
    lines = content.split("\n")
    new_lines = []
    skip_until_brace = False
    brace_count = 0

    i = 0
    while i < len(lines):
        line = lines[i]

        # Skip specific duplicate definitions that we know conflict
        should_skip = False

        # Check for known duplicates in specific files
        if (
            "message Permission {" in line
            and "list_permissions_response.proto" in content
            and "Permission permissions" in content
        ):
            should_skip = True
        elif (
            "message Topic {" in line
            and "list_topics_response.proto" in content
            and "Topic topics" in content
        ):
            should_skip = True
        elif (
            "message ListTopicsResponse {" in line
            and i > 0
            and any("ListTopicsResponse" in prev_line for prev_line in lines[:i])
        ):
            should_skip = True
        elif (
            "message DeleteQueueRequest {" in line
            and i > 0
            and any("DeleteQueueRequest" in prev_line for prev_line in lines[:i])
        ):
            should_skip = True
        elif (
            "message DeleteTopicRequest {" in line
            and i > 0
            and any("DeleteTopicRequest" in prev_line for prev_line in lines[:i])
        ):
            should_skip = True

        if should_skip:
            skip_until_brace = True
            brace_count = 1
            i += 1
            continue

        if skip_until_brace:
            if "{" in line:
                brace_count += line.count("{")
            if "}" in line:
                brace_count -= line.count("}")
                if brace_count <= 0:
                    skip_until_brace = False
            i += 1
            continue

        new_lines.append(line)
        i += 1

    return "\n".join(new_lines)


def add_missing_enum_definitions(content: str) -> str:
    """Add missing enum definitions that are referenced but not defined."""
    if "MfaMethod" in content and "enum MfaMethod" not in content:
        # Add MfaMethod enum definition
        enum_def = """
enum MfaMethod {
  MFA_METHOD_UNSPECIFIED = 0;
  MFA_METHOD_SMS = 1;
  MFA_METHOD_EMAIL = 2;
  MFA_METHOD_TOTP = 3;
  MFA_METHOD_HARDWARE_KEY = 4;
}
"""
        # Insert after the options but before any message definitions
        lines = content.split("\n")
        new_lines = []
        inserted = False

        for line in lines:
            new_lines.append(line)
            if (
                "option features.(pb.go).api_level = API_OPAQUE;" in line
                and not inserted
            ):
                new_lines.append(enum_def)
                inserted = True

        content = "\n".join(new_lines)

    return content


def fix_proto_file(file_path: str) -> bool:
    """Fix a single proto file for Edition 2023 compatibility."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        original_content = content

        # Apply fixes
        content = fix_optional_fields(content)
        content = remove_duplicate_definitions(content)
        content = add_missing_enum_definitions(content)

        if content != original_content:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"✅ Fixed {file_path}")
            return True
        else:
            return False

    except Exception as e:
        print(f"❌ Error fixing {file_path}: {e}")
        return False


def main():
    """Main function to fix all proto files."""
    base_dir = "/Users/jdfalk/repos/github.com/jdfalk/gcommon/pkg"

    print("🔧 Fixing proto files for Edition 2023 compatibility...")

    # Get all proto files
    proto_files = []
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith(".proto"):
                proto_files.append(os.path.join(root, file))

    fixed_count = 0

    for file_path in proto_files:
        if fix_proto_file(file_path):
            fixed_count += 1

    print(f"\n📊 Fixed {fixed_count} proto files")

    # Run buf generate to validate
    print("\n🔧 Running buf generate to validate fixes...")
    import subprocess

    try:
        result = subprocess.run(
            ["buf", "generate"],
            cwd="/Users/jdfalk/repos/github.com/jdfalk/gcommon",
            capture_output=True,
            text=True,
        )
        if result.returncode == 0:
            print("✅ buf generate successful - all proto files are valid!")
        else:
            print(f"❌ buf generate failed:\n{result.stderr}")
    except Exception as e:
        print(f"❌ Error running buf generate: {e}")


if __name__ == "__main__":
    main()
