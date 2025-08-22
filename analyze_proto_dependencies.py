#!/usr/bin/env python3
# file: analyze_proto_dependencies.py
# version: 1.0.0
# guid: abc12345-6789-def0-1234-567890abcdef

"""
Analyze protobuf file dependencies and generate a comprehensive report.
This script will help identify cyclical dependencies and files that need to be moved.
"""

import os
import re
from collections import defaultdict
from pathlib import Path


def extract_imports_from_proto(file_path):
    """Extract all gcommon imports from a proto file."""
    imports = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            # Find all import statements that reference gcommon
            import_pattern = r'import\s+"(gcommon/v1/[^"]+)"'
            matches = re.findall(import_pattern, content)
            imports.extend(matches)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    return imports


def get_package_from_path(file_path):
    """Extract package name from file path."""
    # Convert path like ./proto/gcommon/v1/media/file.proto to "media"
    parts = Path(file_path).parts
    if len(parts) >= 4 and parts[2] == "v1":
        return parts[3]  # Return the package name (media, queue, etc.)
    return "unknown"


def analyze_proto_dependencies():
    """Analyze all proto files and their dependencies."""
    proto_files = []

    # Find all proto files
    for root, dirs, files in os.walk("./proto"):
        for file in files:
            if file.endswith(".proto"):
                file_path = os.path.join(root, file)
                proto_files.append(file_path)

    # Build dependency map
    file_imports = {}
    imported_by = defaultdict(list)
    package_stats = defaultdict(lambda: {"files": 0, "imports": 0, "imported_by": 0})

    for file_path in proto_files:
        # Normalize path
        norm_path = file_path.replace("./proto/", "").replace(".proto", "")
        package = get_package_from_path(file_path)

        # Get imports for this file
        imports = extract_imports_from_proto(file_path)
        file_imports[norm_path] = imports

        # Track what imports this file
        for imported_file in imports:
            imported_by[imported_file].append(norm_path)

        # Update package stats
        package_stats[package]["files"] += 1
        package_stats[package]["imports"] += len(imports)

    # Update imported_by counts
    for imported_file, importers in imported_by.items():
        package = get_package_from_path(f"./proto/{imported_file}.proto")
        package_stats[package]["imported_by"] += len(importers)

    return file_imports, imported_by, package_stats, proto_files


def find_cross_package_dependencies(file_imports):
    """Find files that import from different packages."""
    cross_deps = []

    for file_path, imports in file_imports.items():
        file_package = get_package_from_path(f"./proto/{file_path}.proto")

        for imported_file in imports:
            imported_package = get_package_from_path(f"./proto/{imported_file}.proto")

            # Skip common package imports (everything can import from common)
            if imported_package == "common":
                continue

            # Find cross-package dependencies
            if file_package != imported_package:
                cross_deps.append(
                    {
                        "file": file_path,
                        "file_package": file_package,
                        "imports": imported_file,
                        "imported_package": imported_package,
                    }
                )

    return cross_deps


def generate_markdown_report(file_imports, imported_by, package_stats, cross_deps):
    """Generate a comprehensive markdown report."""

    report = []
    report.append("# Protobuf Dependency Analysis Report")
    report.append("")
    report.append(
        "This report analyzes all protobuf file dependencies to identify cyclical imports and files that need reorganization."
    )
    report.append("")

    # Package Statistics
    report.append("## Package Statistics")
    report.append("")
    report.append("| Package | Files | Total Imports | Times Imported By Others |")
    report.append("|---------|-------|---------------|--------------------------|")

    for package, stats in sorted(package_stats.items()):
        report.append(
            f"| {package} | {stats['files']} | {stats['imports']} | {stats['imported_by']} |"
        )

    report.append("")

    # Cross-Package Dependencies (The Problem!)
    report.append("## 🚨 Cross-Package Dependencies (MUST BE FIXED)")
    report.append("")
    report.append(
        "These files import from packages other than 'common' and their own package:"
    )
    report.append("")

    if cross_deps:
        report.append("| File | File Package | Imports From | Imported Package |")
        report.append("|------|--------------|--------------|------------------|")

        for dep in cross_deps:
            report.append(
                f"| {dep['file']} | {dep['file_package']} | {dep['imports']} | {dep['imported_package']} |"
            )

        report.append("")
        report.append("### Recommended Actions:")
        report.append("")

        # Group by what needs to be moved
        move_to_common = defaultdict(list)
        for dep in cross_deps:
            move_to_common[dep["imported_package"]].append(dep["imports"])

        for package, files in move_to_common.items():
            unique_files = list(set(files))
            report.append(f"**Move from {package} to common:**")
            for file in unique_files:
                report.append(f"- {file}")
            report.append("")
    else:
        report.append("✅ No cross-package dependencies found!")

    report.append("")

    # Full Dependency Table
    report.append("## Complete File Dependencies")
    report.append("")
    report.append("| File | Package | Imports | Imported By |")
    report.append("|------|---------|---------|-------------|")

    # Sort files by package then name
    sorted_files = sorted(
        file_imports.keys(),
        key=lambda x: (get_package_from_path(f"./proto/{x}.proto"), x),
    )

    for file_path in sorted_files:
        package = get_package_from_path(f"./proto/{file_path}.proto")
        imports = file_imports[file_path]
        imports_str = "<br>".join(imports) if imports else "None"

        # Get what imports this file
        imported_by_list = imported_by.get(file_path, [])
        imported_by_str = "<br>".join(imported_by_list) if imported_by_list else "None"

        report.append(
            f"| {file_path} | {package} | {imports_str} | {imported_by_str} |"
        )

    report.append("")

    # Files that could be moved to common
    report.append("## Highly Referenced Files (Consider Moving to Common)")
    report.append("")
    report.append(
        "Files that are imported by many others (good candidates for common package):"
    )
    report.append("")

    # Find files imported by multiple others, excluding those already in common
    high_ref_files = []
    for file_path, importers in imported_by.items():
        package = get_package_from_path(f"./proto/{file_path}.proto")
        if package != "common" and len(importers) > 1:
            high_ref_files.append((file_path, package, len(importers), importers))

    # Sort by reference count
    high_ref_files.sort(key=lambda x: x[2], reverse=True)

    if high_ref_files:
        report.append("| File | Current Package | Reference Count | Referenced By |")
        report.append("|------|-----------------|-----------------|---------------|")

        for file_path, package, count, importers in high_ref_files:
            importers_str = "<br>".join(importers)
            report.append(f"| {file_path} | {package} | {count} | {importers_str} |")
    else:
        report.append("No files found with multiple references outside common package.")

    report.append("")
    report.append("---")
    report.append(f"Report generated on {os.popen('date').read().strip()}")

    return "\n".join(report)


def main():
    """Main function to run the analysis."""
    print("Analyzing protobuf dependencies...")

    # Change to the correct directory
    if not os.path.exists("./proto"):
        print(
            "Error: proto directory not found. Run this script from the repository root."
        )
        return

    # Analyze dependencies
    file_imports, imported_by, package_stats, proto_files = analyze_proto_dependencies()

    # Find cross-package dependencies
    cross_deps = find_cross_package_dependencies(file_imports)

    # Generate report
    report = generate_markdown_report(
        file_imports, imported_by, package_stats, cross_deps
    )

    # Write to file
    output_file = "proto_dependency_analysis.md"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(report)

    print(f"Analysis complete! Report written to {output_file}")

    # Print summary
    print("\nSummary:")
    print(f"- Total proto files: {len(proto_files)}")
    print(f"- Cross-package dependencies: {len(cross_deps)}")
    print(f"- Packages: {', '.join(sorted(package_stats.keys()))}")

    if cross_deps:
        print(
            f"\n🚨 ATTENTION: Found {len(cross_deps)} cross-package dependencies that need fixing!"
        )
        packages_with_issues = set(dep["imported_package"] for dep in cross_deps)
        print(
            f"Packages that need files moved to common: {', '.join(sorted(packages_with_issues))}"
        )


if __name__ == "__main__":
    main()
