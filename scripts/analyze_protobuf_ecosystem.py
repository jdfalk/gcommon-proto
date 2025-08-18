#!/usr/bin/env python3
# file: analyze_protobuf_ecosystem.py
# version: 1.0.0
# guid: 9a8b7c6d-5e4f-3d2c-1b0a-9e8d7c6b5a4f

"""
Comprehensive Protobuf Ecosystem Analyzer for GCommon

This script analyzes all protobuf files in the repository, maps their dependencies,
and identifies missing files. It outputs the analysis in three formats:
1. Detailed list format
2. ASCII diagram
3. Interactive HTML visualization (surprise!)
"""

import argparse
import json
import os
import re
from collections import defaultdict, deque
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple


class ProtobufFile:
    """Represents a single protobuf file and its metadata."""

    def __init__(self, path: str):
        self.path = path
        self.relative_path = path
        self.exists = os.path.exists(path)
        self.package = ""
        self.imports = []
        self.messages = []
        self.enums = []
        self.services = []
        self.errors = []

        if self.exists:
            self._parse_file()

    def _parse_file(self):
        """Parse the protobuf file to extract metadata."""
        try:
            with open(self.path, "r", encoding="utf-8") as f:
                content = f.read()

            # Extract package
            package_match = re.search(r"package\s+([^;]+);", content)
            if package_match:
                self.package = package_match.group(1).strip()

            # Extract imports
            import_matches = re.findall(r'import\s+"([^"]+)";', content)
            self.imports = [imp.strip() for imp in import_matches]

            # Extract messages
            message_matches = re.findall(r"message\s+(\w+)\s*{", content)
            self.messages = message_matches

            # Extract enums
            enum_matches = re.findall(r"enum\s+(\w+)\s*{", content)
            self.enums = enum_matches

            # Extract services
            service_matches = re.findall(r"service\s+(\w+)\s*{", content)
            self.services = service_matches

        except Exception as e:
            self.errors.append(f"Parse error: {str(e)}")

    def get_definition_count(self) -> int:
        """Get total number of definitions in this file."""
        return len(self.messages) + len(self.enums) + len(self.services)

    def follows_1_1_1_pattern(self) -> bool:
        """Check if file follows 1-1-1 pattern (one definition per file)."""
        return self.get_definition_count() <= 1

    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization."""
        return {
            "path": self.path,
            "relative_path": self.relative_path,
            "exists": self.exists,
            "package": self.package,
            "imports": self.imports,
            "messages": self.messages,
            "enums": self.enums,
            "services": self.services,
            "errors": self.errors,
            "definition_count": self.get_definition_count(),
            "follows_1_1_1": self.follows_1_1_1_pattern(),
        }


class ProtobufEcosystemAnalyzer:
    """Main analyzer class for the protobuf ecosystem."""

    def __init__(self, root_path: str = "."):
        self.root_path = Path(root_path)
        self.proto_files: Dict[str, ProtobufFile] = {}
        self.missing_files: Set[str] = set()
        self.dependency_graph: Dict[str, List[str]] = defaultdict(list)
        self.reverse_deps: Dict[str, List[str]] = defaultdict(list)

    def discover_proto_files(self):
        """Discover all .proto files in the repository."""
        print("🔍 Discovering protobuf files...")

        for proto_path in self.root_path.rglob("*.proto"):
            relative_path = str(proto_path.relative_to(self.root_path))
            self.proto_files[relative_path] = ProtobufFile(str(proto_path))

        print(f"📁 Found {len(self.proto_files)} protobuf files")

    def analyze_dependencies(self):
        """Analyze import dependencies and identify missing files."""
        print("🔗 Analyzing dependencies...")

        for file_path, proto_file in self.proto_files.items():
            if not proto_file.exists:
                continue

            for import_path in proto_file.imports:
                # Skip standard protobuf imports
                if import_path.startswith("google/protobuf/"):
                    continue

                # Normalize import path
                normalized_import = self._normalize_import_path(import_path)

                # Add to dependency graph
                self.dependency_graph[file_path].append(normalized_import)
                self.reverse_deps[normalized_import].append(file_path)

                # Check if imported file exists
                if normalized_import not in self.proto_files:
                    # Check if file exists on disk but wasn't discovered
                    full_import_path = self.root_path / normalized_import
                    if full_import_path.exists():
                        # Add to our tracking
                        self.proto_files[normalized_import] = ProtobufFile(
                            str(full_import_path)
                        )
                    else:
                        self.missing_files.add(normalized_import)

    def _normalize_import_path(self, import_path: str) -> str:
        """Normalize import path to be relative to repository root."""
        # Remove leading slashes and normalize
        normalized = import_path.lstrip("/")
        return normalized

    def generate_list_report(self) -> str:
        """Generate detailed list format report."""
        report = []
        report.append("=" * 80)
        report.append("🔍 PROTOBUF ECOSYSTEM ANALYSIS - LIST FORMAT")
        report.append("=" * 80)
        report.append("")

        # Summary statistics
        total_files = len(self.proto_files)
        existing_files = sum(1 for pf in self.proto_files.values() if pf.exists)
        missing_count = len(self.missing_files)
        files_with_1_1_1 = sum(
            1
            for pf in self.proto_files.values()
            if pf.exists and pf.follows_1_1_1_pattern()
        )

        report.append("📊 SUMMARY STATISTICS")
        report.append("-" * 40)
        report.append(f"Total proto files discovered: {total_files}")
        report.append(f"Existing files: {existing_files}")
        report.append(f"Missing files: {missing_count}")
        report.append(
            f"Files following 1-1-1 pattern: {files_with_1_1_1}/{existing_files}"
        )
        report.append("")

        # Missing files section
        if self.missing_files:
            report.append("❌ MISSING FILES")
            report.append("-" * 40)
            for missing_file in sorted(self.missing_files):
                report.append(f"  📄 {missing_file}")
                # Show which files import this missing file
                importers = self.reverse_deps.get(missing_file, [])
                if importers:
                    report.append(
                        f"     ↳ Imported by: {', '.join(importers[:3])}{'...' if len(importers) > 3 else ''}"
                    )
            report.append("")

        # Files by module
        modules = defaultdict(list)
        for file_path, proto_file in self.proto_files.items():
            if proto_file.exists:
                # Extract module from path
                parts = file_path.split("/")
                if len(parts) >= 2 and parts[0] == "pkg":
                    module = parts[1]
                else:
                    module = parts[0] if parts else "root"
                modules[module].append((file_path, proto_file))

        report.append("📦 FILES BY MODULE")
        report.append("-" * 40)
        for module, files in sorted(modules.items()):
            report.append(f"\n🔷 {module.upper()} ({len(files)} files)")
            for file_path, proto_file in sorted(files):
                status = "✅" if proto_file.exists else "❌"
                pattern = "1-1-1" if proto_file.follows_1_1_1_pattern() else "MULTI"
                defs = proto_file.get_definition_count()

                report.append(f"  {status} {file_path} [{pattern}] ({defs} defs)")

                if proto_file.package:
                    report.append(f"     📦 Package: {proto_file.package}")

                if proto_file.imports:
                    report.append(f"     📥 Imports: {len(proto_file.imports)}")
                    for imp in proto_file.imports[:3]:  # Show first 3 imports
                        missing_marker = " ❌" if imp in self.missing_files else ""
                        report.append(f"       • {imp}{missing_marker}")
                    if len(proto_file.imports) > 3:
                        report.append(
                            f"       ... and {len(proto_file.imports) - 3} more"
                        )

                if proto_file.messages or proto_file.enums or proto_file.services:
                    definitions = []
                    if proto_file.messages:
                        definitions.append(f"{len(proto_file.messages)} messages")
                    if proto_file.enums:
                        definitions.append(f"{len(proto_file.enums)} enums")
                    if proto_file.services:
                        definitions.append(f"{len(proto_file.services)} services")
                    report.append(f"     🔧 Defines: {', '.join(definitions)}")

                if proto_file.errors:
                    report.append(f"     ⚠️  Errors: {'; '.join(proto_file.errors)}")

        # Dependency cycles
        cycles = self._find_dependency_cycles()
        if cycles:
            report.append("\n🔄 DEPENDENCY CYCLES")
            report.append("-" * 40)
            for i, cycle in enumerate(cycles[:5]):  # Show first 5 cycles
                report.append(f"  Cycle {i + 1}: {' → '.join(cycle + [cycle[0]])}")

        return "\n".join(report)

    def generate_ascii_diagram(self) -> str:
        """Generate ASCII diagram of the dependency structure."""
        diagram = []
        diagram.append("=" * 100)
        diagram.append("🎯 PROTOBUF ECOSYSTEM ANALYSIS - ASCII DIAGRAM")
        diagram.append("=" * 100)
        diagram.append("")

        # Create a hierarchical view by module
        modules = defaultdict(lambda: defaultdict(list))

        for file_path, proto_file in self.proto_files.items():
            if not proto_file.exists:
                continue

            # Parse module and category from path
            parts = file_path.split("/")
            if len(parts) >= 3 and parts[0] == "pkg":
                module = parts[1]
                category = parts[3] if len(parts) > 3 else "root"
            else:
                module = "other"
                category = "root"

            modules[module][category].append((file_path, proto_file))

        # Generate diagram
        for module_name, categories in sorted(modules.items()):
            diagram.append(f"📦 {module_name.upper()}")
            diagram.append("│")

            category_list = list(categories.items())
            for i, (category, files) in enumerate(category_list):
                is_last_category = i == len(category_list) - 1
                category_prefix = "└─" if is_last_category else "├─"

                diagram.append(f"{category_prefix} 📁 {category}/")

                for j, (file_path, proto_file) in enumerate(sorted(files)):
                    is_last_file = j == len(files) - 1
                    file_prefix = (
                        "   └─"
                        if is_last_category
                        else "│  └─"
                        if is_last_file
                        else "│  ├─"
                    )
                    if not is_last_category and is_last_file:
                        file_prefix = "│  └─"
                    elif not is_last_category:
                        file_prefix = "│  ├─"

                    # File info
                    status = "✅" if proto_file.exists else "❌"
                    pattern = (
                        "[1-1-1]" if proto_file.follows_1_1_1_pattern() else "[MULTI]"
                    )
                    filename = os.path.basename(file_path)

                    diagram.append(f"{file_prefix} {status} {filename} {pattern}")

                    # Show imports for this file
                    if proto_file.imports:
                        for k, imp in enumerate(
                            proto_file.imports[:2]
                        ):  # Show first 2 imports
                            is_last_import = k == len(proto_file.imports[:2]) - 1
                            continuation = "   " if is_last_category else "│  "
                            import_prefix = (
                                f"{continuation}   └─"
                                if is_last_import
                                else f"{continuation}   ├─"
                            )
                            missing_marker = " ❌" if imp in self.missing_files else ""
                            diagram.append(
                                f"{import_prefix} 📥 {os.path.basename(imp)}{missing_marker}"
                            )

                        if len(proto_file.imports) > 2:
                            continuation = "   " if is_last_category else "│  "
                            diagram.append(
                                f"{continuation}   └─ 📥 ... +{len(proto_file.imports) - 2} more"
                            )

            diagram.append("│")

        # Add missing files summary
        if self.missing_files:
            diagram.append("❌ MISSING FILES SUMMARY")
            diagram.append("│")
            for missing in sorted(list(self.missing_files)[:10]):  # Show first 10
                diagram.append(f"├─ 📄 {missing}")
                importers = self.reverse_deps.get(missing, [])
                if importers:
                    diagram.append(
                        f"│  └─ 👈 Needed by: {', '.join([os.path.basename(imp) for imp in importers[:2]])}"
                    )

            if len(self.missing_files) > 10:
                diagram.append(
                    f"└─ ... and {len(self.missing_files) - 10} more missing files"
                )

        return "\n".join(diagram)

    def generate_html_visualization(self) -> str:
        """Generate interactive HTML visualization (the surprise!)."""
        html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GCommon Protobuf Ecosystem Explorer</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: #333;
        }}
        .container {{
            max-width: 1400px;
            margin: 0 auto;
            background: white;
            border-radius: 15px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
            overflow: hidden;
        }}
        .header {{
            background: linear-gradient(90deg, #4CAF50, #2196F3);
            color: white;
            padding: 30px;
            text-align: center;
        }}
        .header h1 {{
            margin: 0;
            font-size: 2.5em;
            font-weight: 300;
        }}
        .stats {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            padding: 30px;
            background: #f8f9fa;
        }}
        .stat-card {{
            background: white;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            box-shadow: 0 5px 15px rgba(0,0,0,0.08);
            transition: transform 0.3s ease;
        }}
        .stat-card:hover {{
            transform: translateY(-5px);
        }}
        .stat-number {{
            font-size: 2.5em;
            font-weight: bold;
            color: #2196F3;
        }}
        .stat-label {{
            color: #666;
            margin-top: 10px;
        }}
        .content {{
            padding: 30px;
        }}
        .module-section {{
            margin-bottom: 40px;
            border: 1px solid #e0e0e0;
            border-radius: 10px;
            overflow: hidden;
        }}
        .module-header {{
            background: linear-gradient(90deg, #FF6B6B, #4ECDC4);
            color: white;
            padding: 15px 20px;
            font-weight: bold;
            font-size: 1.2em;
        }}
        .file-list {{
            padding: 0;
        }}
        .file-item {{
            padding: 15px 20px;
            border-bottom: 1px solid #f0f0f0;
            display: flex;
            align-items: center;
            transition: background 0.3s ease;
        }}
        .file-item:hover {{
            background: #f8f9fa;
        }}
        .file-item:last-child {{
            border-bottom: none;
        }}
        .file-status {{
            width: 20px;
            height: 20px;
            border-radius: 50%;
            margin-right: 15px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-weight: bold;
            font-size: 12px;
        }}
        .status-exists {{
            background: #4CAF50;
        }}
        .status-missing {{
            background: #f44336;
        }}
        .file-name {{
            flex: 1;
            font-weight: 500;
        }}
        .file-meta {{
            display: flex;
            gap: 10px;
            font-size: 0.9em;
            color: #666;
        }}
        .badge {{
            background: #e3f2fd;
            color: #1976d2;
            padding: 4px 8px;
            border-radius: 4px;
            font-size: 0.8em;
        }}
        .badge.multi {{
            background: #fff3e0;
            color: #f57c00;
        }}
        .missing-section {{
            background: #ffebee;
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 30px;
        }}
        .missing-title {{
            color: #c62828;
            font-weight: bold;
            margin-bottom: 15px;
            font-size: 1.2em;
        }}
        .missing-file {{
            background: white;
            margin: 5px 0;
            padding: 10px;
            border-radius: 5px;
            border-left: 4px solid #f44336;
        }}
        .search-box {{
            width: 100%;
            padding: 15px;
            font-size: 16px;
            border: 2px solid #e0e0e0;
            border-radius: 10px;
            margin-bottom: 20px;
            box-sizing: border-box;
        }}
        .search-box:focus {{
            outline: none;
            border-color: #2196F3;
        }}
        @media (max-width: 768px) {{
            .stats {{
                grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
                gap: 15px;
                padding: 20px;
            }}
            .content {{
                padding: 20px;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🎯 GCommon Protobuf Ecosystem Explorer</h1>
            <p>Interactive analysis of protobuf dependencies and structure</p>
        </div>

        <div class="stats">
            <div class="stat-card">
                <div class="stat-number">{len(self.proto_files)}</div>
                <div class="stat-label">Total Proto Files</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">{sum(1 for pf in self.proto_files.values() if pf.exists)}</div>
                <div class="stat-label">Existing Files</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">{len(self.missing_files)}</div>
                <div class="stat-label">Missing Files</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">{sum(1 for pf in self.proto_files.values() if pf.exists and pf.follows_1_1_1_pattern())}</div>
                <div class="stat-label">Following 1-1-1</div>
            </div>
        </div>

        <div class="content">
            <input type="text" class="search-box" placeholder="🔍 Search files, modules, or types..." id="searchBox">

            {self._generate_missing_files_html()}

            {self._generate_modules_html()}
        </div>
    </div>

    <script>
        // Search functionality
        document.getElementById('searchBox').addEventListener('input', function(e) {{
            const searchTerm = e.target.value.toLowerCase();
            const fileItems = document.querySelectorAll('.file-item');
            const moduleHeaders = document.querySelectorAll('.module-header');

            fileItems.forEach(item => {{
                const text = item.textContent.toLowerCase();
                if (text.includes(searchTerm)) {{
                    item.style.display = 'flex';
                }} else {{
                    item.style.display = 'none';
                }}
            }});

            // Hide empty modules
            document.querySelectorAll('.module-section').forEach(module => {{
                const visibleFiles = module.querySelectorAll('.file-item[style*="flex"]');
                if (visibleFiles.length === 0 && searchTerm) {{
                    module.style.display = 'none';
                }} else {{
                    module.style.display = 'block';
                }}
            }});
        }});

        // Add click handlers for file items
        document.querySelectorAll('.file-item').forEach(item => {{
            item.addEventListener('click', function() {{
                const fileName = this.querySelector('.file-name').textContent;
                alert(`File: ${{fileName}}\\n\\nThis would normally open file details or navigate to the file in your editor.`);
            }});
            item.style.cursor = 'pointer';
        }});
    </script>
</body>
</html>
"""
        return html

    def _generate_missing_files_html(self) -> str:
        """Generate HTML for missing files section."""
        if not self.missing_files:
            return ""

        html = ['<div class="missing-section">']
        html.append(
            '<div class="missing-title">❌ Missing Files (Click to see which files need them)</div>'
        )

        for missing_file in sorted(list(self.missing_files)[:20]):  # Show first 20
            importers = self.reverse_deps.get(missing_file, [])
            importers_text = f"Needed by: {', '.join([os.path.basename(imp) for imp in importers[:3]])}"
            if len(importers) > 3:
                importers_text += f" and {len(importers) - 3} more"

            html.append(f'<div class="missing-file">')
            html.append(f"<strong>{missing_file}</strong><br>")
            html.append(f"<small>{importers_text}</small>")
            html.append("</div>")

        if len(self.missing_files) > 20:
            html.append(
                f'<div class="missing-file"><em>... and {len(self.missing_files) - 20} more missing files</em></div>'
            )

        html.append("</div>")
        return "\n".join(html)

    def _generate_modules_html(self) -> str:
        """Generate HTML for modules section."""
        modules = defaultdict(list)

        for file_path, proto_file in self.proto_files.items():
            # Extract module from path
            parts = file_path.split("/")
            if len(parts) >= 2 and parts[0] == "pkg":
                module = parts[1]
            else:
                module = parts[0] if parts else "root"
            modules[module].append((file_path, proto_file))

        html = []
        for module_name, files in sorted(modules.items()):
            html.append(f'<div class="module-section">')
            html.append(
                f'<div class="module-header">📦 {module_name.upper()} Module ({len(files)} files)</div>'
            )
            html.append('<div class="file-list">')

            for file_path, proto_file in sorted(files):
                status_class = (
                    "status-exists" if proto_file.exists else "status-missing"
                )
                status_symbol = "✓" if proto_file.exists else "✗"

                pattern_badge = (
                    "1-1-1" if proto_file.follows_1_1_1_pattern() else "MULTI"
                )
                pattern_class = "" if proto_file.follows_1_1_1_pattern() else "multi"

                html.append('<div class="file-item">')
                html.append(
                    f'<div class="file-status {status_class}">{status_symbol}</div>'
                )
                html.append(
                    f'<div class="file-name">{os.path.basename(file_path)}</div>'
                )
                html.append('<div class="file-meta">')
                html.append(
                    f'<span class="badge {pattern_class}">{pattern_badge}</span>'
                )
                if proto_file.exists:
                    html.append(
                        f'<span class="badge">{proto_file.get_definition_count()} defs</span>'
                    )
                    if proto_file.imports:
                        html.append(
                            f'<span class="badge">{len(proto_file.imports)} imports</span>'
                        )
                html.append("</div>")
                html.append("</div>")

            html.append("</div>")
            html.append("</div>")

        return "\n".join(html)

    def _find_dependency_cycles(self) -> List[List[str]]:
        """Find dependency cycles in the import graph."""
        cycles = []
        visited = set()
        rec_stack = set()

        def dfs(node, path):
            if node in rec_stack:
                # Found a cycle
                cycle_start = path.index(node)
                cycles.append(path[cycle_start:])
                return

            if node in visited:
                return

            visited.add(node)
            rec_stack.add(node)
            path.append(node)

            for neighbor in self.dependency_graph.get(node, []):
                if neighbor in self.proto_files:  # Only follow existing files
                    dfs(neighbor, path[:])

            rec_stack.remove(node)
            path.pop()

        for file_path in self.proto_files:
            if file_path not in visited:
                dfs(file_path, [])

        return cycles[:10]  # Return first 10 cycles

    def save_reports(self, output_dir: str = "protobuf_analysis"):
        """Save all three reports to files."""
        os.makedirs(output_dir, exist_ok=True)

        # Save list report
        with open(f"{output_dir}/detailed_list.txt", "w") as f:
            f.write(self.generate_list_report())

        # Save ASCII diagram
        with open(f"{output_dir}/ascii_diagram.txt", "w") as f:
            f.write(self.generate_ascii_diagram())

        # Save HTML visualization
        with open(f"{output_dir}/interactive_explorer.html", "w") as f:
            f.write(self.generate_html_visualization())

        # Save JSON data for programmatic access
        json_data = {
            "summary": {
                "total_files": len(self.proto_files),
                "existing_files": sum(
                    1 for pf in self.proto_files.values() if pf.exists
                ),
                "missing_files": len(self.missing_files),
                "files_with_1_1_1": sum(
                    1
                    for pf in self.proto_files.values()
                    if pf.exists and pf.follows_1_1_1_pattern()
                ),
            },
            "files": {
                path: proto.to_dict() for path, proto in self.proto_files.items()
            },
            "missing_files": list(self.missing_files),
            "dependency_graph": dict(self.dependency_graph),
            "reverse_dependencies": dict(self.reverse_deps),
        }

        with open(f"{output_dir}/ecosystem_data.json", "w") as f:
            json.dump(json_data, f, indent=2)

        print(f"\n📊 Analysis complete! Reports saved to '{output_dir}/':")
        print(f"   📄 detailed_list.txt - Comprehensive list format")
        print(f"   🎨 ascii_diagram.txt - Visual ASCII diagram")
        print(f"   🌐 interactive_explorer.html - Interactive HTML visualization")
        print(f"   📊 ecosystem_data.json - Raw data for programmatic access")

        return output_dir


def main():
    parser = argparse.ArgumentParser(description="Analyze protobuf ecosystem")
    parser.add_argument("--root", default=".", help="Root directory to analyze")
    parser.add_argument(
        "--output", default="protobuf_analysis", help="Output directory"
    )
    parser.add_argument(
        "--print-list", action="store_true", help="Print list report to console"
    )
    parser.add_argument(
        "--print-diagram", action="store_true", help="Print ASCII diagram to console"
    )

    args = parser.parse_args()

    analyzer = ProtobufEcosystemAnalyzer(args.root)
    analyzer.discover_proto_files()
    analyzer.analyze_dependencies()

    if args.print_list:
        print(analyzer.generate_list_report())
        print()

    if args.print_diagram:
        print(analyzer.generate_ascii_diagram())
        print()

    analyzer.save_reports(args.output)

    # Print quick summary
    print(f"\n🎯 QUICK SUMMARY:")
    print(f"   Total files: {len(analyzer.proto_files)}")
    print(f"   Missing files: {len(analyzer.missing_files)}")
    print(
        f"   Files needing 1-1-1 migration: {sum(1 for pf in analyzer.proto_files.values() if pf.exists and not pf.follows_1_1_1_pattern())}"
    )

    if analyzer.missing_files:
        print(f"\n🔥 TOP MISSING FILES:")
        # Sort by how many files depend on them
        missing_by_importance = sorted(
            analyzer.missing_files,
            key=lambda x: len(analyzer.reverse_deps.get(x, [])),
            reverse=True,
        )
        for missing in missing_by_importance[:10]:
            dep_count = len(analyzer.reverse_deps.get(missing, []))
            print(f"   📄 {missing} (needed by {dep_count} files)")


if __name__ == "__main__":
    main()
