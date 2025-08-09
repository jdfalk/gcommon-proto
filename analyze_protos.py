#!/usr/bin/env python3
# file: analyze_protos.py
# version: 1.0.0
# guid: 123e4567-e89b-12d3-a456-426614174005

"""
Proto Analysis Tool

Generates a comprehensive markdown document of all protocol buffer files
in the repository, with proper organization, escaping, and easy navigation.
"""

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


def main():
    """Main function to generate the proto analysis report."""
    # Find all proto files
    proto_pattern = os.path.join("pkg", "**", "*.proto")
    proto_files_paths = glob.glob(proto_pattern, recursive=True)

    print(f"Found {len(proto_files_paths)} proto files")

    # Analyze each file
    proto_files = []
    for file_path in sorted(proto_files_paths):
        print(f"Analyzing {file_path}...")
        proto_files.append(analyze_proto_file(file_path))

    # Generate markdown report
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
    print(
        f"📊 Found {sum(len(p.get('issues', [])) for p in proto_files)} total issues across {len([p for p in proto_files if p.get('issues')])} files"
    )


if __name__ == "__main__":
    main()
