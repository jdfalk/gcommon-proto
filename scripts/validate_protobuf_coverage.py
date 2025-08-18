#!/usr/bin/env python3
"""
Protobuf coverage validation for GCommon project.
Validates that all protobuf files are tracked and provides implementation status.
"""

from scripts.ci_status import print_status, print_error, print_success, print_summary

import json
import glob
from typing import Dict, List, Set
from collections import defaultdict

def get_all_proto_files() -> Set[str]:
    """Get all protobuf files in the repository."""
    proto_files = set()
    for proto_file in glob.glob('pkg/**/*.proto', recursive=True):
        proto_files.add(proto_file)
    return proto_files

def load_empty_protos() -> Set[str]:
    """Load list of empty protobuf files."""
    try:
        with open('empty_protos.txt', 'r') as f:
            return {line.strip() for line in f if line.strip()}
    except FileNotFoundError:
        print("⚠️  empty_protos.txt not found - assuming no empty files tracked")
        return set()

def load_non_empty_protos() -> Set[str]:
    """Load list of implemented protobuf files."""
    try:
        with open('non_empty_protos.txt', 'r') as f:
            return {line.strip() for line in f if line.strip()}
    except FileNotFoundError:
        print("⚠️  non_empty_protos.txt not found - assuming no implemented files tracked")
        return set()

def analyze_module_status(proto_files: Set[str], empty_protos: Set[str], non_empty_protos: Set[str]) -> Dict:
    """Analyze implementation status by module."""
    modules = defaultdict(lambda: {'total': 0, 'empty': 0, 'implemented': 0})

    for proto_file in proto_files:
        parts = proto_file.split('/')
        if len(parts) >= 2:
            module = parts[1]
            modules[module]['total'] += 1

            if proto_file in empty_protos:
                modules[module]['empty'] += 1
            elif proto_file in non_empty_protos:
                modules[module]['implemented'] += 1

    # Calculate completion percentages
    for module_data in modules.values():
        if module_data['total'] > 0:
            module_data['completion_percent'] = round(
                (module_data['implemented'] / module_data['total']) * 100, 1
            )
        else:
            module_data['completion_percent'] = 0.0

    return dict(modules)

def print_status_report(modules: Dict, empty_protos: Set[str], non_empty_protos: Set[str]):
    """Print a comprehensive status report."""
    total_files = len(empty_protos) + len(non_empty_protos)
    overall_completion = round((len(non_empty_protos) / total_files) * 100, 1) if total_files > 0 else 0

    print("🚀 GCommon Protobuf Implementation Status")
    print("==========================================")
    print(f"📊 Overall: {len(non_empty_protos)}/{total_files} files ({overall_completion}% complete)")
    print(f"✅ Implemented: {len(non_empty_protos)}")
    print(f"❌ Empty: {len(empty_protos)}")
    print()

    print("📋 Module Status:")
    print("=" * 80)

    # Sort modules by completion percentage
    sorted_modules = sorted(modules.items(), key=lambda x: x[1]['completion_percent'], reverse=True)

    for module, data in sorted_modules:
        completion = data['completion_percent']
        status_icon = "✅" if completion == 100 else "🔄" if completion > 0 else "❌"

        print(f"{status_icon} {module.upper():12} {data['implemented']:3}/{data['total']:3} files ({completion:5.1f}%)")

    print()

    # Priority recommendations
    high_priority = [m for m, d in modules.items() if d['completion_percent'] < 50 and d['total'] > 10]
    if high_priority:
        print("🎯 High Priority Modules (>10 files, <50% complete):")
        for module in sorted(high_priority, key=lambda m: modules[m]['total'], reverse=True):
            data = modules[module]
            print(f"   🔴 {module}: {data['empty']} files need implementation")
        print()

def main():
    """Main function to run protobuf coverage validation."""
    try:
        # Load data
        all_protos = get_all_proto_files()
        empty_protos = load_empty_protos()
        non_empty_protos = load_non_empty_protos()

        # Analyze by module
        modules = analyze_module_status(all_protos, empty_protos, non_empty_protos)

        # Print report
        print_status_report(modules, empty_protos, non_empty_protos)

        # Check for untracked files
        tracked_files = empty_protos | non_empty_protos
        untracked = all_protos - tracked_files

        if untracked:
            print("⚠️  UNTRACKED FILES FOUND:")
            for file in sorted(untracked):
                print(f"   📄 {file}")
            print(f"\n💡 Add these {len(untracked)} files to empty_protos.txt or non_empty_protos.txt")
        else:
            print("✅ All protobuf files are properly tracked!")

    except Exception as e:
        print(f"❌ Error: {e}")
        return 1

    return 0

if __name__ == "__main__":
    exit(main())

def load_github_issues() -> List[Dict]:
    """Load GitHub issues from issues.json."""
    try:
        with open('issues.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def analyze_protobuf_coverage(proto_files: Set[str], empty_protos: Set[str], non_empty_protos: Set[str]) -> Dict:
    """Analyze protobuf file coverage and identify gaps."""

    # Files that exist but aren't in our tracking lists
    untracked_files = proto_files - empty_protos - non_empty_protos

    # Files in tracking lists but don't exist
    missing_empty = empty_protos - proto_files
    missing_non_empty = non_empty_protos - proto_files

    # Module breakdown
    module_analysis = defaultdict(lambda: {'total': 0, 'empty': 0, 'implemented': 0, 'untracked': 0})

    for proto_file in proto_files:
        parts = proto_file.split('/')
        if len(parts) >= 2:
            module = parts[1]
            module_analysis[module]['total'] += 1

            if proto_file in empty_protos:
                module_analysis[module]['empty'] += 1
            elif proto_file in non_empty_protos:
                module_analysis[module]['implemented'] += 1
            else:
                module_analysis[module]['untracked'] += 1

    return {
        'total_files_found': len(proto_files),
        'tracked_empty': len(empty_protos),
        'tracked_implemented': len(non_empty_protos),
        'untracked_files': untracked_files,
        'missing_empty': missing_empty,
        'missing_non_empty': missing_non_empty,
        'module_breakdown': dict(module_analysis)
    }

def analyze_github_issues(issues: List[Dict]) -> Dict:
    """Analyze GitHub issues for protobuf coverage."""

    protobuf_issues = []
    issue_coverage = defaultdict(list)

    for issue in issues:
        title = issue.get('title', '')
        if 'protobuf' in title.lower() or 'proto' in title.lower():
            protobuf_issues.append(issue)

            # Extract module from title
            if 'Metrics' in title:
                issue_coverage['metrics'].append(title)
            elif 'Cache' in title:
                issue_coverage['cache'].append(title)
            elif 'Auth' in title:
                issue_coverage['auth'].append(title)
            elif 'Config' in title:
                issue_coverage['config'].append(title)
            elif 'Web' in title:
                issue_coverage['web'].append(title)
            elif 'Health' in title:
                issue_coverage['health'].append(title)
            elif 'Queue' in title:
                issue_coverage['queue'].append(title)

    return {
        'total_protobuf_issues': len(protobuf_issues),
        'by_module': dict(issue_coverage),
        'protobuf_issues': protobuf_issues
    }

def check_issue_implementation_coverage(issues: List[Dict], empty_protos: Set[str]) -> Dict:
    """Check if GitHub issues cover all empty protobuf files."""

    covered_files = set()
    uncovered_files = set(empty_protos)

    for issue in issues:
        body = issue.get('body', '')
        if 'protobuf' in issue.get('title', '').lower():
            # Extract file paths from issue body
            lines = body.split('\n')
            for line in lines:
                if '- [ ]' in line and '.proto' in line:
                    # Extract proto file path
                    if '`' in line:
                        start = line.find('`') + 1
                        end = line.find('`', start)
                        if start > 0 and end > start:
                            proto_path = line[start:end]
                            covered_files.add(proto_path)
                            uncovered_files.discard(proto_path)

    return {
        'covered_files': len(covered_files),
        'uncovered_files': len(uncovered_files),
        'coverage_percentage': (len(covered_files) / len(empty_protos)) * 100 if empty_protos else 0,
        'uncovered_list': list(uncovered_files)
    }

def generate_recommendations(coverage_analysis: Dict, issue_analysis: Dict, implementation_coverage: Dict) -> List[str]:
    """Generate actionable recommendations based on analysis."""

    recommendations = []

    # Check for untracked files
    if coverage_analysis['untracked_files']:
        recommendations.append(
            f"🔍 UNTRACKED FILES: Found {len(coverage_analysis['untracked_files'])} protobuf files not in tracking lists. "
            f"Update empty_protos.txt or non_empty_protos.txt."
        )

    # Check for missing files
    if coverage_analysis['missing_empty'] or coverage_analysis['missing_non_empty']:
        total_missing = len(coverage_analysis['missing_empty']) + len(coverage_analysis['missing_non_empty'])
        recommendations.append(
            f"📁 MISSING FILES: {total_missing} files listed in tracking files but not found in repository. "
            f"Clean up tracking files or create missing files."
        )

    # Check issue coverage
    if implementation_coverage['coverage_percentage'] < 95:
        recommendations.append(
            f"📋 INCOMPLETE ISSUE COVERAGE: Only {implementation_coverage['coverage_percentage']:.1f}% of empty protobuf files "
            f"are covered by GitHub issues. Create issues for remaining {implementation_coverage['uncovered_files']} files."
        )

    # Module-specific recommendations
    for module, stats in coverage_analysis['module_breakdown'].items():
        empty_percentage = (stats['empty'] / stats['total']) * 100 if stats['total'] > 0 else 0
        if empty_percentage > 50:
            recommendations.append(
                f"🏗️ {module.upper()} MODULE: {empty_percentage:.1f}% files empty ({stats['empty']}/{stats['total']}). "
                f"High priority for implementation."
            )

    # Priority recommendations
    if issue_analysis['total_protobuf_issues'] < 20:
        recommendations.append(
            f"⚡ LOW ISSUE COUNT: Only {issue_analysis['total_protobuf_issues']} protobuf issues found. "
            f"Consider creating more granular issues for better task management."
        )

    return recommendations

def create_next_steps_plan(coverage_analysis: Dict, issue_analysis: Dict) -> List[str]:
    """Create a detailed next steps plan."""

    steps = [
        "🎯 IMMEDIATE NEXT STEPS (Priority Order):",
        "",
        "1. 🔧 VALIDATE PROTOBUF COMPILATION",
        "   - Run: make proto-compile (create this target if missing)",
        "   - Fix any compilation errors in existing proto files",
        "   - Set up automated validation in CI/CD",
        "",
        "2. 📋 ORGANIZE GITHUB PROJECT",
        "   - Visit: https://github.com/users/jdfalk/projects/3",
        "   - Set up Kanban columns: Todo, In Progress, Review, Done",
        "   - Move issues to appropriate columns based on priority",
        "",
        "3. 🚀 START HIGH-PRIORITY IMPLEMENTATION",
        "   - Begin with critical validation pipeline issue",
        "   - Focus on modules with highest empty file percentages",
        "   - Implement in order: Metrics → Queue → Web → Auth",
        "",
        "4. 🔄 ITERATIVE DEVELOPMENT PROCESS",
        "   - Pick one module category at a time (e.g., 'Metrics Messages')",
        "   - Implement all files in that category",
        "   - Test compilation after each category",
        "   - Move to next category/module",
        "",
        "5. 🧪 CONTINUOUS VALIDATION",
        "   - Test protobuf compilation after each implementation",
        "   - Validate cross-module imports work correctly",
        "   - Update documentation as you go"
    ]

    # Add module-specific priorities
    module_priorities = []
    for module, stats in coverage_analysis['module_breakdown'].items():
        if stats['empty'] > 0:
            priority = "HIGH" if stats['empty'] > 20 else "MEDIUM" if stats['empty'] > 5 else "LOW"
            module_priorities.append(f"   - {module.title()}: {stats['empty']} files ({priority} priority)")

    if module_priorities:
        steps.extend([
            "",
            "📊 MODULE IMPLEMENTATION PRIORITIES:",
            *module_priorities
        ])

    return steps

def main():
    """Run comprehensive validation and generate report."""

    print_status("GCommon Protobuf Coverage Validation")
    print_status("Analyzing protobuf files...")
    proto_files = get_all_proto_files()
    empty_protos = load_empty_protos()
    non_empty_protos = load_non_empty_protos()

    print_status("Analyzing GitHub issues...")
    github_issues = load_github_issues()

    coverage_analysis = analyze_protobuf_coverage(proto_files, empty_protos, non_empty_protos)
    issue_analysis = analyze_github_issues(github_issues)
    implementation_coverage = check_issue_implementation_coverage(github_issues, empty_protos)

    print_summary("COVERAGE ANALYSIS RESULTS")
    print_summary(f"Total protobuf files found: {coverage_analysis['total_files_found']}")
    print_summary(f"Files tracked as empty: {coverage_analysis['tracked_empty']}")
    print_summary(f"Files tracked as implemented: {coverage_analysis['tracked_implemented']}")
    print_summary(f"Untracked files: {len(coverage_analysis['untracked_files'])}")

    print_summary(f"GitHub Issues: {len(github_issues)} total, {issue_analysis['total_protobuf_issues']} protobuf-related")
    print_summary(f"Issue coverage: {implementation_coverage['coverage_percentage']:.1f}% of empty files covered")

    print_summary("MODULE BREAKDOWN")
    for module, stats in sorted(coverage_analysis['module_breakdown'].items()):
        completion = ((stats['implemented'] / stats['total']) * 100) if stats['total'] > 0 else 0
        print_summary(f"{module:10} | Total: {stats['total']:3} | Empty: {stats['empty']:3} | Done: {stats['implemented']:3} | Complete: {completion:5.1f}%")

    recommendations = generate_recommendations(coverage_analysis, issue_analysis, implementation_coverage)
    if recommendations:
        print_error("RECOMMENDATIONS:")
        for rec in recommendations:
            print_error(rec)

    next_steps = create_next_steps_plan(coverage_analysis, issue_analysis)
    print_summary("Next Steps:")
    for step in next_steps:
        print_summary(step)

    detailed_report = {
        'timestamp': '2025-06-08',
        'coverage_analysis': coverage_analysis,
        'issue_analysis': issue_analysis,
        'implementation_coverage': implementation_coverage,
        'recommendations': recommendations,
        'next_steps': next_steps
    }
    with open('protobuf_validation_report.json', 'w') as f:
        json.dump(detailed_report, f, indent=2, default=str)
    print_success("Detailed report saved to: protobuf_validation_report.json")

    critical_issues = []
    if coverage_analysis['untracked_files']:
        critical_issues.append("Untracked protobuf files detected")
    if implementation_coverage['coverage_percentage'] < 80:
        critical_issues.append("Low GitHub issue coverage")

    if critical_issues:
        print_error("CRITICAL ISSUES DETECTED:")
        for issue in critical_issues:
            print_error(f"   - {issue}")
        return 1
    else:
        print_success("Validation complete! Ready to proceed with implementation.")
        return 0

if __name__ == "__main__":
    exit(main())
