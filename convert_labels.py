#!/usr/bin/env python3
# file: convert_labels.py
# version: 1.0.1
# guid: a1b2c3d4-e5f6-7890-abcd-ef1234567890

import json


def hex_to_ansi_bg(hex_color):
    """Convert hex color to ANSI background color for visual representation"""
    hex_color = hex_color.lstrip("#")
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    return f"\033[48;2;{r};{g};{b}m   \033[0m"


def extract_json_from_markdown(content):
    """Extract JSON arrays from the markdown content"""
    sections = {}
    current_section = None

    lines = content.split("\n")
    for line in lines:
        if line.startswith("## "):
            current_section = line[3:].strip()
            sections[current_section] = ""
        elif current_section and line.strip().startswith("["):
            # Find the complete JSON array
            json_start = content.find(line.strip())
            json_end = content.find("\n\n", json_start)
            if json_end == -1:
                json_end = len(content)

            json_str = content[json_start:json_end].strip()
            try:
                sections[current_section] = json.loads(json_str)
            except json.JSONDecodeError as e:
                print(f"Error parsing JSON for {current_section}: {e}")
                sections[current_section] = []

    return sections


def format_labels_as_markdown(sections):
    """Convert label data to nicely formatted markdown"""
    md_content = """<!-- file: repository_labels.md -->
<!-- version: 1.1.0 -->
<!-- guid: f1e2d3c4-b5a6-9780-cdef-abc123456789 -->

# Repository Labels

This document provides a comprehensive overview of all labels across our repositories, organized by repository and categorized by type.

"""

    for repo_name, labels in sections.items():
        if not labels:
            continue

        md_content += f"## {repo_name}\n\n"
        md_content += f"**Total Labels:** {len(labels)}\n\n"

        # Categorize labels
        categories = {
            "Priority": [],
            "Type": [],
            "Module": [],
            "Size": [],
            "Status": [],
            "Technology": [],
            "Workflow": [],
            "Project": [],
            "Default GitHub": [],
            "Other": [],
        }

        for label in labels:
            name = label["name"]
            if (
                name.startswith("priority:")
                or name.startswith("priority-")
                or name in ["critical", "high", "medium", "low"]
            ):
                categories["Priority"].append(label)
            elif name.startswith("type:") or name in [
                "bug",
                "enhancement",
                "documentation",
                "feature",
                "bugfix",
                "refactor",
                "testing",
            ]:
                categories["Type"].append(label)
            elif name.startswith("module:") or name in [
                "auth",
                "cache",
                "config",
                "database",
                "metrics",
                "queue",
                "web",
                "api",
                "backend",
                "frontend",
                "ui",
            ]:
                categories["Module"].append(label)
            elif name.startswith("size:") or name in [
                "small",
                "medium",
                "large",
                "epic",
            ]:
                categories["Size"].append(label)
            elif name.startswith("status:") or name in [
                "blocked",
                "in-progress",
                "needs-review",
                "ready",
                "todo",
                "duplicate",
                "wontfix",
            ]:
                categories["Status"].append(label)
            elif (
                name.startswith("tech:")
                or name.startswith("workflow:")
                or name
                in [
                    "go",
                    "python",
                    "javascript",
                    "docker",
                    "kubernetes",
                    "protobuf",
                    "grpc",
                ]
            ):
                if name.startswith("workflow:"):
                    categories["Workflow"].append(label)
                else:
                    categories["Technology"].append(label)
            elif name.startswith("project:"):
                categories["Project"].append(label)
            elif label["isDefault"]:
                categories["Default GitHub"].append(label)
            else:
                categories["Other"].append(label)

        # Output each category
        for category, category_labels in categories.items():
            if not category_labels:
                continue

            md_content += f"### {category} Labels ({len(category_labels)})\n\n"
            md_content += "| Color | Name | Description |\n"
            md_content += "|-------|------|-------------|\n"

            # Sort labels by name
            category_labels.sort(key=lambda x: x["name"])

            for label in category_labels:
                color_preview = hex_to_ansi_bg(label["color"])
                color_hex = f"#{label['color']}"
                name = label["name"]
                description = (
                    label.get("description", "").replace("|", "\\|")
                    or "*No description*"
                )

                # Create color cell with both hex and visual representation
                color_cell = f"`{color_hex}` {color_preview}"

                md_content += f"| {color_cell} | `{name}` | {description} |\n"

            md_content += "\n"

        md_content += "---\n\n"

    # Add summary
    md_content += "## Summary\n\n"
    total_labels = sum(len(labels) for labels in sections.values() if labels)
    md_content += f"**Total labels across all repositories:** {total_labels}\n\n"

    for repo_name, labels in sections.items():
        if labels:
            md_content += f"- **{repo_name}:** {len(labels)} labels\n"

    md_content += "\n---\n\n"
    md_content += "*Generated automatically from GitHub API data*\n"

    return md_content


def main():
    # Read the current markdown file
    with open("repository_labels.md", "r") as f:
        content = f.read()

    # Extract JSON data
    sections = extract_json_from_markdown(content)

    # Convert to formatted markdown
    formatted_md = format_labels_as_markdown(sections)

    # Write the new file
    with open("repository_labels.md", "w") as f:
        f.write(formatted_md)

    print("✅ Successfully converted repository_labels.md to formatted markdown!")
    print(f"📊 Processed {len(sections)} repositories")
    total_labels = sum(len(labels) for labels in sections.values() if labels)
    print(f"🏷️  Total labels: {total_labels}")


if __name__ == "__main__":
    main()
