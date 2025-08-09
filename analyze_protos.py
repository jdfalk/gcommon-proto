#!/usr/bin/env python3
# file: analyze_protos.py
# version: 1.1.0
# guid: 123e4567-e89b-12d3-a456-426614174005

"""
Proto Analysis Tool

Generates a comprehensive markdown document of all protocol buffer files
in the repository, with proper organization, escaping, and easy navigation.

Can generate either:
1. Single comprehensive report (default)
2. Modular documentation structure with interconnected files (--generate-docs flag)
"""

import argparse
import glob
import os
import re
from datetime import datetime


def escape_markdown(text):
    """Escape special markdown characters in text."""
    # Escape backticks and other markdown special chars
    text = text.replace("`", "\\`")
    text = text.replace("*", "\\*")
    text = text.replace("_", "\\_")
    text = text.replace("[", "\\[")
    text = text.replace("]", "\\]")
    text = text.replace("(", "\\(")
    text = text.replace(")", "\\)")
    text = text.replace("#", "\\#")
    text = text.replace("+", "\\+")
    text = text.replace("-", "\\-")
    text = text.replace(".", "\\.")
    text = text.replace("!", "\\!")
    text = text.replace("|", "\\|")
    return text


def find_todos_and_issues(content):
    """Find TODO comments, incomplete sections, and other issues in proto content."""
    issues = []
    lines = content.split("\n")

    for i, line in enumerate(lines, 1):
        line_lower = line.lower()

        # Look for TODO comments
        if "todo" in line_lower:
            issues.append(f"Line {i}: TODO - {line.strip()}")

        # Look for "commented out for now" patterns
        if any(
            phrase in line_lower
            for phrase in [
                "commented out for now",
                "uncomment when",
                "disabled for now",
                "placeholder",
                "not implemented",
                "implement later",
            ]
        ):
            issues.append(f"Line {i}: Implementation needed - {line.strip()}")

        # Look for empty message definitions
        if re.match(r"^\s*message\s+\w+\s*{\s*$", line):
            # Check if next few lines are just closing brace or comments
            next_lines = lines[i : i + 5] if i < len(lines) - 5 else lines[i:]
            content_lines = [
                line.strip()
                for line in next_lines
                if line.strip() and not line.strip().startswith("//")
            ]
            if len(content_lines) == 1 and content_lines[0] == "}":
                issues.append(f"Line {i}: Empty message - {line.strip()}")

        # Look for commented out field definitions
        if re.match(r"^\s*//\s*\w+.*=\s*\d+;", line):
            issues.append(f"Line {i}: Commented field - {line.strip()}")

    return issues


def analyze_proto_file(file_path):
    """Analyze a single proto file and return structured information."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Extract basic info
        package_match = re.search(r"package\s+([^;]+);", content)
        package_name = package_match.group(1) if package_match else "Unknown"

        # Find messages and services
        messages = re.findall(r"message\s+(\w+)\s*{", content)
        services = re.findall(r"service\s+(\w+)\s*{", content)
        enums = re.findall(r"enum\s+(\w+)\s*{", content)

        # Find imports
        imports = re.findall(r'import\s+"([^"]+)";', content)

        # Find issues
        issues = find_todos_and_issues(content)

        return {
            "path": file_path,
            "package": package_name,
            "messages": messages,
            "services": services,
            "enums": enums,
            "imports": imports,
            "issues": issues,
            "content": content,
            "line_count": len(content.split("\n")),
        }
    except Exception as e:
        return {
            "path": file_path,
            "error": str(e),
            "content": f"Error reading file: {e}",
        }


def generate_toc(proto_files):
    """Generate table of contents."""
    toc = ["# Table of Contents\n"]

    # Group by package
    packages = {}
    for proto in proto_files:
        if "error" in proto:
            continue
        pkg = (
            proto["package"].split(".")[0]
            if "." in proto["package"]
            else proto["package"]
        )
        if pkg not in packages:
            packages[pkg] = []
        packages[pkg].append(proto)

    for pkg_name in sorted(packages.keys()):
        toc.append(f"## {pkg_name}")
        for proto in sorted(packages[pkg_name], key=lambda x: x["path"]):
            file_name = os.path.basename(proto["path"])
            anchor = file_name.replace(".", "").replace("_", "").lower()
            toc.append(f"- [{file_name}](#{anchor})")
            if proto["issues"]:
                toc.append(f"  - ⚠️ {len(proto['issues'])} issues found")
        toc.append("")

    return "\n".join(toc)


def generate_summary(proto_files):
    """Generate summary statistics."""
    total_files = len(proto_files)
    total_lines = sum(p.get("line_count", 0) for p in proto_files if "error" not in p)
    total_messages = sum(
        len(p.get("messages", [])) for p in proto_files if "error" not in p
    )
    total_services = sum(
        len(p.get("services", [])) for p in proto_files if "error" not in p
    )
    total_enums = sum(len(p.get("enums", [])) for p in proto_files if "error" not in p)
    total_issues = sum(
        len(p.get("issues", [])) for p in proto_files if "error" not in p
    )
    files_with_issues = len(
        [p for p in proto_files if p.get("issues") and "error" not in p]
    )

    summary = f"""# Protocol Buffer Analysis Report

Generated on: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

## Summary Statistics

- **Total Proto Files**: {total_files}
- **Total Lines of Code**: {total_lines:,}
- **Total Messages**: {total_messages}
- **Total Services**: {total_services}
- **Total Enums**: {total_enums}
- **Total Issues Found**: {total_issues}
- **Files with Issues**: {files_with_issues}

## Issues Overview

"""

    if total_issues > 0:
        summary += "### 🚨 Files Requiring Attention\n\n"
        for proto in proto_files:
            if proto.get("issues") and "error" not in proto:
                file_name = os.path.basename(proto["path"])
                anchor = file_name.replace(".", "").replace("_", "").lower()
                summary += (
                    f"- [{file_name}](#{anchor}) - {len(proto['issues'])} issues\n"
                )
        summary += "\n"
    else:
        summary += "✅ No issues found in any proto files!\n\n"

    return summary


def sanitize_filename(name):
    """Sanitize a string to be safe for use as a filename."""
    # Replace problematic characters with underscores
    sanitized = re.sub(r'[<>:"/\\|?*]', "_", name)
    # Remove or replace other special characters
    sanitized = re.sub(r"[^\w\-_.]", "_", sanitized)
    # Remove multiple consecutive underscores
    sanitized = re.sub(r"_+", "_", sanitized)
    # Remove leading/trailing underscores
    return sanitized.strip("_")


def generate_module_docs(proto_files, output_dir):
    """Generate modular documentation with interconnected markdown files."""
    os.makedirs(output_dir, exist_ok=True)

    # Group by package/module
    modules = {}
    for proto in proto_files:
        if "error" in proto:
            continue

        # Extract module name (first part of package)
        pkg = proto["package"]
        module_name = pkg.split(".")[0] if "." in pkg else pkg
        if not module_name or module_name == "Unknown":
            module_name = "misc"

        if module_name not in modules:
            modules[module_name] = []
        modules[module_name].append(proto)

    # Generate index file
    generate_index_file(modules, output_dir)

    # Generate module-specific files
    for module_name, module_protos in modules.items():
        generate_module_file(module_name, module_protos, modules, output_dir)

    print(f"✅ Modular documentation generated in: {output_dir}")
    print(f"📁 Generated {len(modules)} module documents plus index")


def generate_index_file(modules, output_dir):
    """Generate the central index.md file."""
    index_path = os.path.join(output_dir, "index.md")

    total_files = sum(len(protos) for protos in modules.values())
    total_messages = sum(
        sum(len(p.get("messages", [])) for p in protos) for protos in modules.values()
    )
    total_services = sum(
        sum(len(p.get("services", [])) for p in protos) for protos in modules.values()
    )
    total_issues = sum(
        sum(len(p.get("issues", [])) for p in protos) for protos in modules.values()
    )

    with open(index_path, "w", encoding="utf-8") as f:
        f.write("# Protocol Buffer Documentation\n\n")
        f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

        f.write("## Overview\n\n")
        f.write(f"This documentation covers {total_files} protocol buffer files ")
        f.write(f"organized into {len(modules)} modules, containing:\n\n")
        f.write(f"- **{total_messages}** message definitions\n")
        f.write(f"- **{total_services}** service definitions\n")

        if total_issues > 0:
            f.write(f"- ⚠️ **{total_issues}** issues requiring attention\n")

        f.write("\n## Modules\n\n")

        for module_name in sorted(modules.keys()):
            module_protos = modules[module_name]
            module_file = f"{sanitize_filename(module_name)}.md"

            module_messages = sum(len(p.get("messages", [])) for p in module_protos)
            module_services = sum(len(p.get("services", [])) for p in module_protos)
            module_issues = sum(len(p.get("issues", [])) for p in module_protos)

            f.write(f"### [{module_name}](./{module_file})\n\n")
            f.write(f"- **Files**: {len(module_protos)}\n")
            f.write(f"- **Messages**: {module_messages}\n")
            f.write(f"- **Services**: {module_services}\n")

            if module_issues > 0:
                f.write(f"- ⚠️ **Issues**: {module_issues}\n")

            # List proto files in this module
            f.write("\n**Proto Files**:\n")
            for proto in sorted(module_protos, key=lambda x: x["path"]):
                file_name = os.path.basename(proto["path"])
                anchor = sanitize_filename(file_name.replace(".proto", ""))
                f.write(f"- [{file_name}](./{module_file}#{anchor})")
                if proto.get("issues"):
                    f.write(f" ⚠️ {len(proto['issues'])} issues")
                f.write("\n")

            f.write("\n")

        f.write("## Quick Navigation\n\n")
        f.write("- [All Messages](#all-messages)\n")
        f.write("- [All Services](#all-services)\n")
        f.write("- [Issues Summary](#issues-summary)\n\n")

        # All messages index
        f.write("## All Messages\n\n")
        for module_name in sorted(modules.keys()):
            module_file = f"{sanitize_filename(module_name)}.md"
            for proto in sorted(modules[module_name], key=lambda x: x["path"]):
                if proto.get("messages"):
                    file_name = os.path.basename(proto["path"])
                    anchor = sanitize_filename(file_name.replace(".proto", ""))
                    for message in proto["messages"]:
                        f.write(
                            f"- `{message}` - [{file_name}](./{module_file}#{anchor})\n"
                        )

        # All services index
        f.write("\n## All Services\n\n")
        for module_name in sorted(modules.keys()):
            module_file = f"{sanitize_filename(module_name)}.md"
            for proto in sorted(modules[module_name], key=lambda x: x["path"]):
                if proto.get("services"):
                    file_name = os.path.basename(proto["path"])
                    anchor = sanitize_filename(file_name.replace(".proto", ""))
                    for service in proto["services"]:
                        f.write(
                            f"- `{service}` - [{file_name}](./{module_file}#{anchor})\n"
                        )

        # Issues summary
        if total_issues > 0:
            f.write("\n## Issues Summary\n\n")
            for module_name in sorted(modules.keys()):
                module_file = f"{sanitize_filename(module_name)}.md"
                module_issues = sum(
                    len(p.get("issues", [])) for p in modules[module_name]
                )
                if module_issues > 0:
                    f.write(
                        f"### [{module_name}](./{module_file}) - {module_issues} issues\n\n"
                    )
                    for proto in modules[module_name]:
                        if proto.get("issues"):
                            file_name = os.path.basename(proto["path"])
                            anchor = sanitize_filename(file_name.replace(".proto", ""))
                            f.write(
                                f"- [{file_name}](./{module_file}#{anchor}) - {len(proto['issues'])} issues\n"
                            )
                    f.write("\n")


def generate_module_file(module_name, module_protos, all_modules, output_dir):
    """Generate a module-specific documentation file."""
    module_file = f"{sanitize_filename(module_name)}.md"
    module_path = os.path.join(output_dir, module_file)

    with open(module_path, "w", encoding="utf-8") as f:
        f.write(f"# {module_name} Module\n\n")
        f.write("[← Back to Index](./index.md)\n\n")

        # Module summary
        total_messages = sum(len(p.get("messages", [])) for p in module_protos)
        total_services = sum(len(p.get("services", [])) for p in module_protos)
        total_enums = sum(len(p.get("enums", [])) for p in module_protos)
        total_issues = sum(len(p.get("issues", [])) for p in module_protos)

        f.write("## Module Overview\n\n")
        f.write(f"- **Proto Files**: {len(module_protos)}\n")
        f.write(f"- **Messages**: {total_messages}\n")
        f.write(f"- **Services**: {total_services}\n")
        f.write(f"- **Enums**: {total_enums}\n")

        if total_issues > 0:
            f.write(f"- ⚠️ **Issues**: {total_issues}\n")

        f.write("\n")

        # Table of contents for this module
        f.write("## Files in this Module\n\n")
        for proto in sorted(module_protos, key=lambda x: x["path"]):
            file_name = os.path.basename(proto["path"])
            anchor = sanitize_filename(file_name.replace(".proto", ""))
            f.write(f"- [{file_name}](#{anchor})")
            if proto.get("issues"):
                f.write(f" ⚠️ {len(proto['issues'])} issues")
            f.write("\n")

        f.write("\n")

        # Cross-module references
        dependencies = set()
        dependents = set()

        for proto in module_protos:
            for import_path in proto.get("imports", []):
                # Check if this import belongs to another module
                for other_module, other_protos in all_modules.items():
                    if other_module != module_name:
                        for other_proto in other_protos:
                            if import_path in other_proto["path"] or os.path.basename(
                                import_path
                            ) == os.path.basename(other_proto["path"]):
                                dependencies.add(other_module)

        # Find modules that depend on this one
        for other_module, other_protos in all_modules.items():
            if other_module != module_name:
                for other_proto in other_protos:
                    for import_path in other_proto.get("imports", []):
                        for proto in module_protos:
                            if import_path in proto["path"] or os.path.basename(
                                import_path
                            ) == os.path.basename(proto["path"]):
                                dependents.add(other_module)

        if dependencies or dependents:
            f.write("## Module Dependencies\n\n")

            if dependencies:
                f.write("**This module depends on**:\n")
                for dep in sorted(dependencies):
                    dep_file = f"{sanitize_filename(dep)}.md"
                    f.write(f"- [{dep}](./{dep_file})\n")
                f.write("\n")

            if dependents:
                f.write("**Modules that depend on this one**:\n")
                for dep in sorted(dependents):
                    dep_file = f"{sanitize_filename(dep)}.md"
                    f.write(f"- [{dep}](./{dep_file})\n")
                f.write("\n")

        # Detailed file documentation
        f.write("---\n\n")
        f.write("## Detailed Documentation\n\n")

        for proto in sorted(module_protos, key=lambda x: x["path"]):
            file_name = os.path.basename(proto["path"])
            anchor = sanitize_filename(file_name.replace(".proto", ""))

            f.write(f"### {file_name} {{#{anchor}}}\n\n")
            f.write(f"**Path**: `{proto['path']}`\n")
            f.write(f"**Package**: `{proto['package']}`\n")
            f.write(f"**Lines**: {proto.get('line_count', 0)}\n\n")

            # Components
            if proto.get("messages"):
                f.write(f"**Messages** ({len(proto['messages'])}): ")
                f.write(", ".join(f"`{m}`" for m in proto["messages"]))
                f.write("\n\n")

            if proto.get("services"):
                f.write(f"**Services** ({len(proto['services'])}): ")
                f.write(", ".join(f"`{s}`" for s in proto["services"]))
                f.write("\n\n")

            if proto.get("enums"):
                f.write(f"**Enums** ({len(proto['enums'])}): ")
                f.write(", ".join(f"`{e}`" for e in proto["enums"]))
                f.write("\n\n")

            if proto.get("imports"):
                f.write(f"**Imports** ({len(proto['imports'])}):\n")
                for imp in proto["imports"]:
                    f.write(f"- `{imp}`")

                    # Try to find which module this import belongs to
                    for other_module, other_protos in all_modules.items():
                        for other_proto in other_protos:
                            if imp in other_proto["path"] or os.path.basename(
                                imp
                            ) == os.path.basename(other_proto["path"]):
                                if other_module != module_name:
                                    other_file = f"{sanitize_filename(other_module)}.md"
                                    other_anchor = sanitize_filename(
                                        os.path.basename(other_proto["path"]).replace(
                                            ".proto", ""
                                        )
                                    )
                                    f.write(
                                        f" → [{other_module}](./{other_file}#{other_anchor})"
                                    )
                                break
                    f.write("\n")
                f.write("\n")

            # Issues
            if proto.get("issues"):
                f.write(f"#### ⚠️ Issues Found ({len(proto['issues'])})\n\n")
                for issue in proto["issues"]:
                    f.write(f"- {issue}\n")
                f.write("\n")

            # Source code
            f.write("#### Source Code\n\n")
            f.write("```protobuf\n")
            f.write(proto.get("content", ""))
            f.write("\n```\n\n")

            f.write("---\n\n")


def main():
    """Main function to generate the proto analysis report."""
    parser = argparse.ArgumentParser(
        description="Generate protocol buffer documentation",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python analyze_protos.py                    # Generate single comprehensive report
  python analyze_protos.py --generate-docs    # Generate modular documentation
  python analyze_protos.py --generate-docs --output-dir ./proto-docs
        """,
    )

    parser.add_argument(
        "--generate-docs",
        action="store_true",
        help="Generate modular documentation with interconnected files instead of single report",
    )

    parser.add_argument(
        "--output-dir",
        default="proto-docs",
        help="Output directory for modular documentation (default: proto-docs)",
    )

    args = parser.parse_args()

    # Find all proto files
    proto_pattern = os.path.join("pkg", "**", "*.proto")
    proto_files_paths = glob.glob(proto_pattern, recursive=True)

    print(f"Found {len(proto_files_paths)} proto files")

    if not proto_files_paths:
        print("❌ No proto files found in pkg/ directory")
        return

    # Analyze each file
    proto_files = []
    for file_path in sorted(proto_files_paths):
        print(f"Analyzing {file_path}...")
        proto_files.append(analyze_proto_file(file_path))

    if args.generate_docs:
        # Generate modular documentation
        generate_module_docs(proto_files, args.output_dir)
    else:
        # Generate single comprehensive report (original behavior)
        output_file = "proto_analysis_report.md"

        with open(output_file, "w", encoding="utf-8") as f:
            # Write summary
            f.write(generate_summary(proto_files))

            # Write table of contents
            f.write(generate_toc(proto_files))

            # Write detailed analysis
            f.write("\n---\n\n# Detailed File Analysis\n\n")

            for proto in proto_files:
                file_name = os.path.basename(proto["path"])
                anchor = file_name.replace(".", "").replace("_", "").lower()

                f.write(f"## {file_name} {{#{anchor}}}\n\n")
                f.write(f"**Path**: `{proto['path']}`\n\n")

                if "error" in proto:
                    f.write(f"❌ **Error**: {proto['error']}\n\n")
                    continue

                # Basic info
                f.write(f"**Package**: `{proto['package']}`\n")
                f.write(f"**Lines**: {proto['line_count']}\n\n")

                # Components
                if proto["messages"]:
                    f.write(
                        f"**Messages** ({len(proto['messages'])}): {', '.join(f'`{m}`' for m in proto['messages'])}\n"
                    )

                if proto["services"]:
                    f.write(
                        f"**Services** ({len(proto['services'])}): {', '.join(f'`{s}`' for s in proto['services'])}\n"
                    )

                if proto["enums"]:
                    f.write(
                        f"**Enums** ({len(proto['enums'])}): {', '.join(f'`{e}`' for e in proto['enums'])}\n"
                    )

                if proto["imports"]:
                    f.write(
                        f"**Imports** ({len(proto['imports'])}): {', '.join(f'`{i}`' for i in proto['imports'])}\n"
                    )

                f.write("\n")

                # Issues
                if proto["issues"]:
                    f.write(f"### ⚠️ Issues Found ({len(proto['issues'])})\n\n")
                    for issue in proto["issues"]:
                        f.write(f"- {issue}\n")
                    f.write("\n")

                # Full content
                f.write("### File Content\n\n")
                f.write("```protobuf\n")
                f.write(proto["content"])
                f.write("\n```\n\n")
                f.write("---\n\n")

        print(f"\n✅ Analysis complete! Report saved to: {output_file}")

    # Print summary statistics
    total_issues = sum(
        len(p.get("issues", [])) for p in proto_files if "error" not in p
    )
    files_with_issues = len(
        [p for p in proto_files if p.get("issues") and "error" not in p]
    )
    print(f"📊 Found {total_issues} total issues across {files_with_issues} files")


if __name__ == "__main__":
    main()
