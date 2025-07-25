#!/usr/bin/env python3
# file: analyze_all_modules.py
# version: 1.0.0
# guid: 8f9e0d1c-2b3a-4e5f-6789-0123456789ab

"""
Comprehensive analysis of all protobuf modules in gcommon.
Provides detailed implementation status, TODO analysis, and content depth assessment.
"""

import json
import os
import re
from collections import defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Dict, List, Optional, Set


@dataclass
class ProtoFile:
    path: str
    relative_path: str
    has_todos: bool
    todo_count: int
    line_count: int
    message_count: int
    service_count: int
    enum_count: int
    rpc_count: int
    field_count: int
    import_count: int
    is_placeholder: bool
    content_summary: str


@dataclass
class ModuleAnalysis:
    name: str
    total_files: int
    todo_files: int
    total_todos: int
    total_lines: int
    placeholder_files: int
    implemented_files: int
    messages: int
    services: int
    enums: int
    requests: int
    responses: int
    types: int
    rpcs: int
    total_fields: int
    avg_fields_per_message: float
    completion_estimate: str
    critical_issues: List[str]
    sample_files: List[ProtoFile]


class ProtobufAnalyzer:
    def __init__(self, root_path: str = "."):
        self.root_path = Path(root_path)
        self.modules = {}

    def analyze_proto_file(self, file_path: Path) -> ProtoFile:
        """Analyze a single proto file for content and implementation depth."""
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            return None

        lines = content.split("\n")
        line_count = len(lines)

        # Count various elements
        todo_matches = re.findall(r"TODO", content, re.IGNORECASE)
        todo_count = len(todo_matches)
        has_todos = todo_count > 0

        message_count = len(re.findall(r"^message\s+\w+", content, re.MULTILINE))
        service_count = len(re.findall(r"^service\s+\w+", content, re.MULTILINE))
        enum_count = len(re.findall(r"^enum\s+\w+", content, re.MULTILINE))
        rpc_count = len(re.findall(r"^\s*rpc\s+\w+", content, re.MULTILINE))

        # Count fields (simple heuristic: lines with field numbers)
        field_matches = re.findall(r"^\s*\w+.*=\s*\d+;", content, re.MULTILINE)
        field_count = len(field_matches)

        import_count = len(re.findall(r"^import\s+", content, re.MULTILINE))

        # Determine if it's a placeholder
        is_placeholder = (
            todo_count > 0
            and message_count == 0
            and service_count == 0
            and enum_count == 0
        ) or (
            "placeholder" in content.lower()
            or "implement actual" in content.lower()
            or (line_count < 25 and message_count == 0 and service_count == 0)
        )

        # Create content summary
        if is_placeholder:
            content_summary = "PLACEHOLDER - needs implementation"
        elif message_count == 0 and service_count == 0 and enum_count == 0:
            content_summary = "EMPTY - no definitions"
        elif field_count == 0:
            content_summary = "SKELETON - definitions but no fields"
        elif field_count < (message_count * 2):
            content_summary = "MINIMAL - few fields per message"
        else:
            content_summary = "IMPLEMENTED - has substantial content"

        relative_path = str(file_path.relative_to(self.root_path))

        return ProtoFile(
            path=str(file_path),
            relative_path=relative_path,
            has_todos=has_todos,
            todo_count=todo_count,
            line_count=line_count,
            message_count=message_count,
            service_count=service_count,
            enum_count=enum_count,
            rpc_count=rpc_count,
            field_count=field_count,
            import_count=import_count,
            is_placeholder=is_placeholder,
            content_summary=content_summary,
        )

    def categorize_file(self, file_path: Path) -> str:
        """Categorize proto file by its path structure."""
        parts = file_path.parts
        if "messages" in parts:
            return "messages"
        elif "requests" in parts:
            return "requests"
        elif "responses" in parts:
            return "responses"
        elif "services" in parts:
            return "services"
        elif "enums" in parts:
            return "enums"
        elif "types" in parts:
            return "types"
        else:
            return "other"

    def analyze_module(self, module_path: Path) -> ModuleAnalysis:
        """Analyze a complete module directory."""
        module_name = module_path.name
        proto_files = list(module_path.rglob("*.proto"))

        if not proto_files:
            return None

        analyzed_files = []
        for proto_file in proto_files:
            analysis = self.analyze_proto_file(proto_file)
            if analysis:
                analyzed_files.append(analysis)

        if not analyzed_files:
            return None

        # Calculate statistics
        total_files = len(analyzed_files)
        todo_files = sum(1 for f in analyzed_files if f.has_todos)
        total_todos = sum(f.todo_count for f in analyzed_files)
        total_lines = sum(f.line_count for f in analyzed_files)
        placeholder_files = sum(1 for f in analyzed_files if f.is_placeholder)
        implemented_files = total_files - placeholder_files

        # Count by category
        messages = sum(f.message_count for f in analyzed_files)
        services = sum(f.service_count for f in analyzed_files)
        enums = sum(f.enum_count for f in analyzed_files)
        rpcs = sum(f.rpc_count for f in analyzed_files)
        total_fields = sum(f.field_count for f in analyzed_files)

        # Count by file type
        requests = len([f for f in analyzed_files if "requests" in f.relative_path])
        responses = len([f for f in analyzed_files if "responses" in f.relative_path])
        types = len([f for f in analyzed_files if "types" in f.relative_path])

        # Calculate average fields per message
        avg_fields_per_message = total_fields / messages if messages > 0 else 0

        # Estimate completion status
        placeholder_ratio = placeholder_files / total_files
        if placeholder_ratio > 0.8:
            completion_estimate = "❌ MOSTLY PLACEHOLDER"
        elif placeholder_ratio > 0.5:
            completion_estimate = "⚠️ NEEDS MAJOR WORK"
        elif placeholder_ratio > 0.2:
            completion_estimate = "🔄 IN PROGRESS"
        elif todo_files > total_files * 0.3:
            completion_estimate = "🔄 IN PROGRESS"
        elif avg_fields_per_message < 2:
            completion_estimate = "🔄 IN PROGRESS (minimal fields)"
        else:
            completion_estimate = "✅ WELL IMPLEMENTED"

        # Identify critical issues
        critical_issues = []
        if placeholder_ratio > 0.5:
            critical_issues.append(
                f"{placeholder_files} placeholder files need implementation"
            )
        if total_todos > 50:
            critical_issues.append(f"{total_todos} TODO comments need attention")
        if avg_fields_per_message < 2 and messages > 0:
            critical_issues.append(
                f"Messages have minimal fields (avg {avg_fields_per_message:.1f})"
            )
        if services > 0 and rpcs == 0:
            critical_issues.append("Services defined but no RPC methods")

        # Sample files for detailed review
        sample_files = []
        # Get some placeholder files
        placeholder_samples = [f for f in analyzed_files if f.is_placeholder][:3]
        # Get some implemented files
        implemented_samples = [f for f in analyzed_files if not f.is_placeholder][:3]
        sample_files.extend(placeholder_samples + implemented_samples)

        return ModuleAnalysis(
            name=module_name,
            total_files=total_files,
            todo_files=todo_files,
            total_todos=total_todos,
            total_lines=total_lines,
            placeholder_files=placeholder_files,
            implemented_files=implemented_files,
            messages=messages,
            services=services,
            enums=enums,
            requests=requests,
            responses=responses,
            types=types,
            rpcs=rpcs,
            total_fields=total_fields,
            avg_fields_per_message=avg_fields_per_message,
            completion_estimate=completion_estimate,
            critical_issues=critical_issues,
            sample_files=sample_files[:6],  # Limit to 6 samples
        )

    def analyze_all_modules(self) -> Dict[str, ModuleAnalysis]:
        """Analyze all modules in the pkg directory."""
        pkg_dir = self.root_path / "pkg"
        if not pkg_dir.exists():
            print(f"Package directory not found: {pkg_dir}")
            return {}

        modules = {}
        for module_dir in pkg_dir.iterdir():
            if module_dir.is_dir() and not module_dir.name.startswith("."):
                analysis = self.analyze_module(module_dir)
                if analysis:
                    modules[module_dir.name] = analysis

        return modules

    def generate_report(self, modules: Dict[str, ModuleAnalysis]) -> str:
        """Generate a comprehensive text report."""
        report = []
        report.append("# COMPREHENSIVE PROTOBUF MODULE ANALYSIS")
        report.append("=" * 60)
        report.append("")

        # Summary table
        report.append("## EXECUTIVE SUMMARY")
        report.append("")
        report.append(
            "| Module       | Files | Placeholder | TODOs | Fields | Avg F/M | Status |"
        )
        report.append(
            "|--------------|-------|-------------|-------|--------|---------|--------|"
        )

        total_files = 0
        total_placeholder = 0
        total_todos = 0

        for name, module in sorted(modules.items()):
            total_files += module.total_files
            total_placeholder += module.placeholder_files
            total_todos += module.total_todos

            report.append(
                f"| {name:<12} | {module.total_files:>5} | {module.placeholder_files:>11} | {module.total_todos:>5} | {module.total_fields:>6} | {module.avg_fields_per_message:>7.1f} | {module.completion_estimate} |"
            )

        report.append(
            f"| **TOTALS**   | {total_files:>5} | {total_placeholder:>11} | {total_todos:>5} | - | - | - |"
        )
        report.append("")

        # Key findings
        placeholder_ratio = total_placeholder / total_files if total_files > 0 else 0
        report.append("## KEY FINDINGS")
        report.append("")
        report.append(f"- **Total Files**: {total_files}")
        report.append(
            f"- **Placeholder Files**: {total_placeholder} ({placeholder_ratio:.1%})"
        )
        report.append(f"- **Total TODOs**: {total_todos}")
        report.append(
            f"- **Reality Check**: {placeholder_ratio:.1%} of files are placeholders or need major work"
        )
        report.append("")

        # Priority recommendations
        report.append("## PRIORITY RECOMMENDATIONS")
        report.append("")

        # Sort modules by work needed (placeholder ratio + todo count)
        work_needed = [
            (name, module, module.placeholder_files + module.total_todos / 10)
            for name, module in modules.items()
        ]
        work_needed.sort(key=lambda x: x[2], reverse=True)

        for i, (name, module, _) in enumerate(work_needed[:5], 1):
            report.append(
                f"{i}. **{name.upper()} MODULE**: {module.completion_estimate}"
            )
            for issue in module.critical_issues:
                report.append(f"   - {issue}")
            report.append("")

        # Detailed module analysis
        report.append("## DETAILED MODULE ANALYSIS")
        report.append("")

        for name, module in sorted(modules.items()):
            report.append(f"### {name.upper()} MODULE")
            report.append("")
            report.append(f"**Status**: {module.completion_estimate}")
            report.append(
                f"**Files**: {module.total_files} total, {module.implemented_files} implemented, {module.placeholder_files} placeholder"
            )
            report.append(
                f"**Content**: {module.messages} messages, {module.services} services, {module.enums} enums, {module.rpcs} RPCs"
            )
            report.append(
                f"**Quality**: {module.total_fields} total fields, {module.avg_fields_per_message:.1f} avg fields/message"
            )

            if module.critical_issues:
                report.append("")
                report.append("**Critical Issues**:")
                for issue in module.critical_issues:
                    report.append(f"- {issue}")

            if module.sample_files:
                report.append("")
                report.append("**Sample Files**:")
                for sample in module.sample_files:
                    report.append(
                        f"- `{sample.relative_path}`: {sample.content_summary}"
                    )

            report.append("")
            report.append("-" * 40)
            report.append("")

        return "\n".join(report)


def main():
    """Main analysis function."""
    print("🔍 Starting comprehensive protobuf analysis...")

    analyzer = ProtobufAnalyzer()
    modules = analyzer.analyze_all_modules()

    if not modules:
        print("❌ No modules found to analyze")
        return

    print(f"✅ Analyzed {len(modules)} modules")

    # Generate report
    report = analyzer.generate_report(modules)

    # Save report to file
    with open("protobuf_analysis_report.txt", "w") as f:
        f.write(report)

    # Save detailed JSON data
    json_data = {name: asdict(module) for name, module in modules.items()}
    with open("protobuf_analysis_data.json", "w") as f:
        json.dump(json_data, f, indent=2)

    print("📊 Analysis complete!")
    print("📄 Report saved to: protobuf_analysis_report.txt")
    print("📄 Data saved to: protobuf_analysis_data.json")
    print("")
    print("=== EXECUTIVE SUMMARY ===")

    # Print key stats
    total_files = sum(m.total_files for m in modules.values())
    total_placeholder = sum(m.placeholder_files for m in modules.values())
    total_todos = sum(m.total_todos for m in modules.values())

    print(f"Total files: {total_files}")
    print(
        f"Placeholder files: {total_placeholder} ({total_placeholder / total_files:.1%})"
    )
    print(f"Total TODOs: {total_todos}")
    print("")

    # Print top priority modules
    work_needed = [
        (
            name,
            module.completion_estimate,
            module.placeholder_files + module.total_todos,
        )
        for name, module in modules.items()
    ]
    work_needed.sort(key=lambda x: x[2], reverse=True)

    print("Top 5 modules needing work:")
    for i, (name, status, _) in enumerate(work_needed[:5], 1):
        print(f"{i}. {name}: {status}")


if __name__ == "__main__":
    main()
