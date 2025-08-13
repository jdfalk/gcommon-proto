#!/usr/bin/env python3
# file: check_proto_naming.py
# version: 1.0.0
# guid: 8b7a6c5d-4e3f-2a1b-9c8d-7e6f5a4b3c2d

"""
Proto File Naming Standards Checker

Checks all .proto files against the naming standards in protobuf.instructions.md:
- Use lower_snake_case.proto for filenames
- Services: {service_name}_service.proto
- Messages: {message_name}.proto (snake_case)
- Enums: {enum_name}.proto (snake_case)
- Types: {type_category}.proto for shared types
"""

import os
import re
from pathlib import Path
from typing import Dict, List


def to_snake_case(name: str) -> str:
    """Convert CamelCase to snake_case"""
    s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1).lower()


def parse_proto_file(file_path: Path) -> Dict[str, List[str]]:
    """Parse a proto file and extract definitions"""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception:
        return {"messages": [], "services": [], "enums": []}

    # Extract definitions
    messages = re.findall(r"message\s+(\w+)\s*\{", content)
    services = re.findall(r"service\s+(\w+)\s*\{", content)
    enums = re.findall(r"enum\s+(\w+)\s*\{", content)

    return {"messages": messages, "services": services, "enums": enums}


def check_filename_standards(
    file_path: Path, definitions: Dict[str, List[str]]
) -> List[str]:
    """Check if filename follows naming standards"""
    issues = []
    filename = file_path.stem  # Without .proto extension

    # Get all definitions
    all_definitions = (
        definitions["messages"] + definitions["services"] + definitions["enums"]
    )

    if not all_definitions:
        issues.append("No definitions found in file")
        return issues

    # Check if multiple definitions (violates 1-1-1 pattern)
    if len(all_definitions) > 1:
        issues.append(
            f"Multiple definitions found: {', '.join(all_definitions)} (violates 1-1-1 pattern)"
        )

    # Check naming based on definition type
    if definitions["services"]:
        service_name = definitions["services"][0]
        snake_name = to_snake_case(service_name)
        # Don't duplicate _service if it already ends with it
        if snake_name.endswith("_service"):
            expected_name = snake_name
        else:
            expected_name = snake_name + "_service"
        if filename != expected_name:
            issues.append(
                f"Service file should be named '{expected_name}.proto', not '{filename}.proto'"
            )

    elif definitions["messages"]:
        message_name = definitions["messages"][0]
        expected_name = to_snake_case(message_name)
        if filename != expected_name:
            issues.append(
                f"Message file should be named '{expected_name}.proto', not '{filename}.proto'"
            )

    elif definitions["enums"]:
        enum_name = definitions["enums"][0]
        expected_name = to_snake_case(enum_name)
        if filename != expected_name:
            issues.append(
                f"Enum file should be named '{expected_name}.proto', not '{filename}.proto'"
            )

    # Check for snake_case
    if not re.match(r"^[a-z][a-z0-9_]*$", filename):
        issues.append(
            f"Filename should be in snake_case: '{filename}' -> '{to_snake_case(filename)}'"
        )

    return issues


def generate_rename_commands(
    file_path: Path, definitions: Dict[str, List[str]]
) -> List[str]:
    """Generate the correct rename command for this file"""
    commands = []

    if (
        not definitions["messages"]
        and not definitions["services"]
        and not definitions["enums"]
    ):
        return commands

    current_name = file_path.name

    # Determine correct name
    if definitions["services"] and len(definitions["services"]) == 1:
        service_name = definitions["services"][0]
        snake_name = to_snake_case(service_name)
        # Don't duplicate _service if it already ends with it
        if snake_name.endswith("_service"):
            correct_name = snake_name + ".proto"
        else:
            correct_name = snake_name + "_service.proto"
    elif definitions["messages"] and len(definitions["messages"]) == 1:
        message_name = definitions["messages"][0]
        correct_name = to_snake_case(message_name) + ".proto"
    elif definitions["enums"] and len(definitions["enums"]) == 1:
        enum_name = definitions["enums"][0]
        correct_name = to_snake_case(enum_name) + ".proto"
    else:
        return commands  # Multiple definitions, can't determine single correct name

    if current_name != correct_name:
        old_path = str(file_path)
        new_path = str(file_path.parent / correct_name)
        commands.append(f"mv '{old_path}' '{new_path}'")

    return commands


def find_proto_files(base_path: Path) -> List[Path]:
    """Find all .proto files"""
    proto_files = []
    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.endswith(".proto") and not file.endswith(".original"):
                proto_files.append(Path(root) / file)
    return proto_files


def main():
    base_path = Path("pkg/")

    print("🔍 CHECKING PROTO NAMING STANDARDS")
    print("=" * 60)

    proto_files = find_proto_files(base_path)
    print(f"Found {len(proto_files)} proto files to check\n")

    issues_found = 0
    structural_issues = 0
    rename_commands = []

    # Group by module for better organization
    modules = {}
    for file_path in proto_files:
        module = str(file_path.parts[1])  # pkg/MODULE/proto/...
        if module not in modules:
            modules[module] = []
        modules[module].append(file_path)

    for module, files in sorted(modules.items()):
        print(f"📦 MODULE: {module}")
        print("-" * 40)

        module_issues = 0
        module_structural = 0
        for file_path in sorted(files):
            definitions = parse_proto_file(file_path)
            issues = check_filename_standards(file_path, definitions)

            # Separate naming issues from structural issues
            naming_issues = []
            structural_file_issues = []

            for issue in issues:
                if "violates 1-1-1 pattern" in issue or "No definitions found" in issue:
                    structural_file_issues.append(issue)
                else:
                    naming_issues.append(issue)

            if issues:
                issues_found += len(naming_issues)
                structural_issues += len(structural_file_issues)

                print(f"❌ {file_path.relative_to(base_path)}")

                if naming_issues:
                    for issue in naming_issues:
                        print(f"   📝 NAMING: {issue}")

                if structural_file_issues:
                    for issue in structural_file_issues:
                        print(f"   🏗️  STRUCTURE: {issue}")

                # Generate rename commands only for naming issues
                if naming_issues:
                    commands = generate_rename_commands(file_path, definitions)
                    rename_commands.extend(commands)
                print()
            else:
                print(f"✅ {file_path.relative_to(base_path)}")

        if module_issues == 0 and module_structural == 0:
            print("   All files in this module follow naming standards!")
        print()

    print("📊 SUMMARY:")
    print(f"Total files checked: {len(proto_files)}")
    print(f"Naming issues found: {issues_found}")
    print(f"Structural issues found: {structural_issues}")
    print(f"Files needing rename: {len(rename_commands)}")

    if structural_issues > 0:
        print("\n🏗️  STRUCTURAL ISSUES:")
        print(
            f"   {structural_issues} files violate the 1-1-1 pattern or have no definitions"
        )
        print("   These need to be split or fixed manually")

    if issues_found == 0 and structural_issues == 0:
        print("\n✅ All proto files follow naming and structural standards!")
    elif issues_found == 0:
        print("\n✅ All proto files follow naming standards!")
        print("⚠️  Some structural issues remain (see above)")
    elif structural_issues == 0:
        print("✅ All proto files follow structural standards!")
        print("⚠️  Some naming issues remain (see below)")
    if rename_commands:
        print("\n🔧 RENAME COMMANDS:")
        print("Run these commands to fix naming issues:")
        print("-" * 40)
        for cmd in rename_commands:
            print(cmd)

        # Offer to create a script
        script_path = Path("fix_proto_naming.sh")
        with open(script_path, "w") as f:
            f.write("#!/bin/bash\n")
            f.write("# Auto-generated script to fix proto file naming\n\n")
            for cmd in rename_commands:
                f.write(cmd + "\n")

        script_path.chmod(0o755)
        print(f"\n💾 Created executable script: {script_path}")
        print("Run './fix_proto_naming.sh' to apply all renames")

    else:
        print("\n✅ All proto files follow naming standards!")


if __name__ == "__main__":
    main()
