#!/usr/bin/env python3
"""
Smart proto conflict resolver that only fixes actual conflicts within the same go_package.
"""

import os
import re
import subprocess
from collections import defaultdict
from pathlib import Path


def extract_proto_info(filepath):
    """Extract go_package and purpose from a proto file."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        # Extract go_package
        go_package_match = re.search(r'option\s+go_package\s*=\s*"([^"]+)"', content)
        go_package = go_package_match.group(1) if go_package_match else "UNKNOWN"

        # Extract package
        package_match = re.search(r"package\s+([^;]+);", content)
        proto_package = package_match.group(1) if package_match else "UNKNOWN"

        # Determine purpose from content
        purpose = "UNKNOWN"

        # Check for CONFLICT_DISABLED
        if "CONFLICT_DISABLED" in content:
            purpose = "CONFLICT_DISABLED"
        elif re.search(r"message\s+\w+", content):
            purpose = "MESSAGES"
        elif re.search(r"enum\s+\w+", content):
            purpose = "ENUMS"
        elif re.search(r"service\s+\w+", content):
            purpose = "SERVICES"
        elif "Request" in filepath or "Response" in filepath:
            purpose = "REQUESTS"
        elif "/types/" in filepath:
            purpose = "TYPES"

        # Get actual message/enum/service names
        entities = []
        entities.extend(re.findall(r"message\s+(\w+)", content))
        entities.extend(re.findall(r"enum\s+(\w+)", content))
        entities.extend(re.findall(r"service\s+(\w+)", content))

        return {
            "filepath": filepath,
            "go_package": go_package,
            "proto_package": proto_package,
            "purpose": purpose,
            "entities": entities,
            "has_content": len(entities) > 0,
            "is_conflict_disabled": "CONFLICT_DISABLED" in content,
        }
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return None


def find_all_protos():
    """Find all proto files and group by basename."""
    proto_files = []
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".proto"):
                filepath = os.path.join(root, file)
                proto_files.append(filepath)

    return proto_files


def group_by_basename_and_package(proto_files):
    """Group proto files by basename and go_package to find real conflicts."""
    basename_groups = defaultdict(list)

    for filepath in proto_files:
        info = extract_proto_info(filepath)
        if info:
            basename = os.path.basename(filepath)
            basename_groups[basename].append(info)

    return basename_groups


def analyze_conflicts():
    """Analyze and categorize conflicts."""
    print("🔍 Analyzing proto file conflicts...")

    proto_files = find_all_protos()
    basename_groups = group_by_basename_and_package(proto_files)

    conflicts = {}
    no_conflicts = {}

    for basename, files in basename_groups.items():
        if len(files) > 1:
            # Group by go_package to see if there are real conflicts
            package_groups = defaultdict(list)
            for file_info in files:
                package_groups[file_info["go_package"]].append(file_info)

            # Check if any package has multiple files with same basename
            has_real_conflict = any(len(group) > 1 for group in package_groups.values())

            if has_real_conflict:
                conflicts[basename] = {
                    "files": files,
                    "package_groups": dict(package_groups),
                }
            else:
                no_conflicts[basename] = {
                    "files": files,
                    "package_groups": dict(package_groups),
                }
        else:
            no_conflicts[basename] = {
                "files": files,
                "package_groups": {files[0]["go_package"]: files},
            }

    return conflicts, no_conflicts


def print_analysis(conflicts, no_conflicts):
    """Print detailed analysis."""
    print(f"\n📊 ANALYSIS RESULTS:")
    print(f"   Real conflicts (same basename + same go_package): {len(conflicts)}")
    print(f"   No conflicts (different go_packages): {len(no_conflicts)}")

    if conflicts:
        print(f"\n🚨 REAL CONFLICTS that need fixing:")
        for basename, conflict_info in conflicts.items():
            print(f"\n   📄 {basename}:")
            for go_package, files in conflict_info["package_groups"].items():
                if len(files) > 1:
                    print(f"      🎯 go_package: {go_package}")
                    for file_info in files:
                        entities_str = (
                            ", ".join(file_info["entities"])
                            if file_info["entities"]
                            else "NO_ENTITIES"
                        )
                        status = (
                            "⚠️ DISABLED"
                            if file_info["is_conflict_disabled"]
                            else "✅ ACTIVE"
                        )
                        print(f"         {status} {file_info['filepath']}")
                        print(f"             Purpose: {file_info['purpose']}")
                        print(f"             Entities: {entities_str}")

    print(f"\n✅ Files with same basename but different go_packages (NO conflict):")
    sample_shown = 0
    for basename, info in no_conflicts.items():
        if len(info["files"]) > 1 and sample_shown < 5:
            print(f"   📄 {basename}:")
            for file_info in info["files"]:
                print(f"      {file_info['go_package']} -> {file_info['filepath']}")
            sample_shown += 1

    if len(no_conflicts) > 5:
        print(f"   ... and {len(no_conflicts) - 5} more")


def fix_conflicts(conflicts):
    """Fix the real conflicts."""
    print(f"\n🔧 FIXING CONFLICTS...")

    for basename, conflict_info in conflicts.items():
        for go_package, files in conflict_info["package_groups"].items():
            if len(files) > 1:
                print(f"\n   Fixing conflict in {basename} for package {go_package}")

                # Separate active and disabled files
                active_files = [f for f in files if not f["is_conflict_disabled"]]
                disabled_files = [f for f in files if f["is_conflict_disabled"]]

                # Remove disabled files
                for file_info in disabled_files:
                    print(f"      🗑️  Removing disabled file: {file_info['filepath']}")
                    try:
                        os.remove(file_info["filepath"])
                    except Exception as e:
                        print(f"         Error removing file: {e}")

                # If multiple active files, rename based on purpose/entities
                if len(active_files) > 1:
                    for i, file_info in enumerate(active_files):
                        if i == 0:
                            continue  # Keep first file as-is

                        # Generate new name based on purpose or entities
                        base_name = basename.replace(".proto", "")
                        if file_info["entities"]:
                            # Use first entity name
                            new_name = (
                                f"{base_name}_{file_info['entities'][0].lower()}.proto"
                            )
                        else:
                            # Use purpose
                            new_name = (
                                f"{base_name}_{file_info['purpose'].lower()}.proto"
                            )

                        old_path = file_info["filepath"]
                        new_path = os.path.join(os.path.dirname(old_path), new_name)

                        print(f"      📝 Renaming: {old_path} -> {new_path}")

                        try:
                            os.rename(old_path, new_path)
                            # Update file header
                            update_file_header(new_path, new_name)
                        except Exception as e:
                            print(f"         Error renaming file: {e}")


def update_file_header(filepath, new_filename):
    """Update the file header with new filename."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        # Update file path in header
        relative_path = filepath.replace("./", "")
        content = re.sub(r"// file: [^\n]+", f"// file: {relative_path}", content)
        content = re.sub(
            r"// filepath: [^\n]+", f"// filepath: {relative_path}", content
        )

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

    except Exception as e:
        print(f"Error updating header for {filepath}: {e}")


if __name__ == "__main__":
    conflicts, no_conflicts = analyze_conflicts()
    print_analysis(conflicts, no_conflicts)

    if conflicts:
        response = input(f"\n❓ Fix {len(conflicts)} conflicts? (y/n): ")
        if response.lower() == "y":
            fix_conflicts(conflicts)
            print(f"\n✅ Conflicts fixed! Run 'buf generate' to test.")
        else:
            print(f"\n❌ No changes made.")
    else:
        print(f"\n🎉 No real conflicts found! All files are in different go_packages.")
