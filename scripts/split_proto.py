#!/usr/bin/env python3
# file: split_proto_working.py
# version: 1.0.0
# guid: f4a5b6c7-8d9e-0f1a-2b3c-4d5e6f7a8b9c

"""
Working Python script to split protobuf files following the 1-1-1 pattern.
Each file should contain only one definition (one enum, one message, etc.).
"""

import argparse
import re
import sys
import uuid
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Set, Tuple


def camel_to_snake(name: str) -> str:
    """Convert CamelCase to snake_case."""
    # Insert underscore before capital letters, then lowercase
    s1 = re.sub("([a-z0-9])([A-Z])", r"\1_\2", name)
    return s1.lower()


def generate_guid() -> str:
    """Generate a new GUID for file headers."""
    return str(uuid.uuid4())


def extract_header_info(content: str) -> Dict[str, str]:
    """Extract header information from proto file."""
    lines = content.split("\n")
    info = {}

    for line in lines:
        line = line.strip()
        if line.startswith("edition ="):
            info["edition"] = line
        elif line.startswith("package "):
            info["package"] = line
        elif line.startswith("import "):
            info.setdefault("imports", []).append(line)
        elif line.startswith("option "):
            info.setdefault("options", []).append(line)

    return info


def extract_definitions(
    content: str,
) -> Tuple[List[Tuple[str, str]], List[Tuple[str, str]]]:
    """
    Extract enum and message definitions from proto content.
    Returns (enums, messages) where each is a list of (name, definition) tuples.
    """
    enums = []
    messages = []

    # Find enum definitions
    enum_pattern = r"(\/\*\*[^*]*\*+(?:[^/*][^*]*\*+)*\/\s*)?(enum\s+(\w+)\s*\{[^}]*\})"
    for match in re.finditer(enum_pattern, content, re.DOTALL):
        comment = match.group(1) or ""
        definition = match.group(2)
        name = match.group(3)
        full_def = comment + definition
        enums.append((name, full_def.strip()))

    # Find message definitions
    message_pattern = (
        r"(\/\*\*[^*]*\*+(?:[^/*][^*]*\*+)*\/\s*)?(message\s+(\w+)\s*\{[^}]*\})"
    )
    for match in re.finditer(message_pattern, content, re.DOTALL):
        comment = match.group(1) or ""
        definition = match.group(2)
        name = match.group(3)
        full_def = comment + definition
        messages.append((name, full_def.strip()))

    return enums, messages


def find_dependencies(message_def: str, enum_names: Set[str]) -> Set[str]:
    """Find which enum types are referenced in a message definition."""
    dependencies = set()

    for enum_name in enum_names:
        # Look for enum name as a type in field definitions
        if re.search(rf"\b{enum_name}\b", message_def):
            dependencies.add(enum_name)

    return dependencies


def create_proto_file(
    name: str,
    definition: str,
    header_info: Dict[str, str],
    dependencies: Set[str],
    output_dir: Path,
    module: str,
) -> str:
    """Create a proto file with the given definition."""
    filename = f"{camel_to_snake(name)}.proto"
    filepath = output_dir / filename
    guid = generate_guid()

    # Calculate relative path from repo root for the header
    relative_path = str(filepath)

    # Build content
    content_parts = [
        f"// file: {relative_path}",
        "// version: 1.0.0",
        f"// guid: {guid}",
        "",
        header_info.get("edition", 'edition = "2023";'),
        "",
        header_info.get("package", f"package gcommon.v1.{module};"),
        "",
        'import "google/protobuf/go_features.proto";',
    ]

    # Add dependency imports
    for dep in sorted(dependencies):
        dep_filename = camel_to_snake(dep)
        content_parts.append(f'import "pkg/{module}/proto/{dep_filename}.proto";')

    # Add other imports if needed
    if "imports" in header_info:
        for imp in header_info["imports"]:
            if "go_features" not in imp:  # Don't duplicate
                content_parts.append(imp)

    content_parts.extend(
        [
            "",
            "option features.(pb.go).api_level = API_OPAQUE;",
            f'option go_package = "github.com/jdfalk/gcommon/pkg/{module}/proto;{module}pb";',
            "",
            definition,
        ]
    )

    with open(filepath, "w") as f:
        f.write("\n".join(content_parts))

    return str(filepath)


def split_proto_file(proto_path: Path) -> bool:
    """
    Split a proto file into separate files following 1-1-1 pattern.
    Returns True if splitting was performed, False if not needed.
    """
    print(f"Processing: {proto_path}")

    # Read the file
    with open(proto_path, "r") as f:
        content = f.read()

    # Extract definitions
    enums, messages = extract_definitions(content)
    total_definitions = len(enums) + len(messages)

    print(
        f"  Found: {len(enums)} enums, {len(messages)} messages, {total_definitions} total"
    )

    if total_definitions <= 1:
        print("  ✓ Already follows 1-1-1 pattern, skipping")
        return False

    # Create backup
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = proto_path.with_suffix(f".proto.backup.{timestamp}")
    backup_path.write_text(content)
    print(f"  ✓ Backup created: {backup_path}")

    # Extract header info
    header_info = extract_header_info(content)

    # Determine module from path
    path_parts = proto_path.parts
    if "pkg" in path_parts:
        pkg_idx = path_parts.index("pkg")
        if pkg_idx + 1 < len(path_parts):
            module = path_parts[pkg_idx + 1]
        else:
            module = "common"
    else:
        module = "common"

    output_dir = proto_path.parent
    enum_names = {name for name, _ in enums}
    created_files = []

    # Create enum files
    for enum_name, enum_def in enums:
        filepath = create_proto_file(
            enum_name, enum_def, header_info, set(), output_dir, module
        )
        created_files.append(filepath)
        print(f"  ✓ Created: {filepath}")

    # Create message files
    for message_name, message_def in messages:
        dependencies = find_dependencies(message_def, enum_names)
        filepath = create_proto_file(
            message_name, message_def, header_info, dependencies, output_dir, module
        )
        created_files.append(filepath)
        print(f"  ✓ Created: {filepath}")

    # Remove original file
    proto_path.unlink()
    print(f"  ✓ Removed original file: {proto_path}")

    print(f"  ✅ Split completed! Created {len(created_files)} files")
    return True


def main():
    parser = argparse.ArgumentParser(
        description="Split protobuf files following 1-1-1 pattern"
    )
    parser.add_argument("proto_file", help="Path to the proto file to split")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be done without making changes",
    )

    args = parser.parse_args()

    proto_path = Path(args.proto_file)

    if not proto_path.exists():
        print(f"Error: File {proto_path} not found")
        sys.exit(1)

    if not proto_path.suffix == ".proto":
        print(f"Error: File {proto_path} is not a .proto file")
        sys.exit(1)

    print("=== Proto File Splitter (Python) ===")
    print(f"Target: {proto_path}")

    if args.dry_run:
        print("DRY RUN MODE - no files will be modified")
        # TODO: Add dry run logic
        return

    try:
        success = split_proto_file(proto_path)
        if success:
            print("\n🎉 Splitting completed successfully!")
            print("\nNext steps:")
            print("1. Review the created files")
            print("2. Test compilation: buf generate")
            print("3. Remove backup if everything works")
        else:
            print("\n✓ No splitting needed")

    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
