#!/usr/bin/env python3
# file: scripts/generate_proto_status.py
# version: 1.0.0
# guid: 1a2b3c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d

"""
Generate comprehensive proto validation status report.
Analyzes all proto files for validation import and field validation coverage.
"""

import os
import re
from datetime import datetime
from pathlib import Path
from typing import Dict, List, NamedTuple, Tuple


class FieldInfo(NamedTuple):
    name: str
    type: str
    number: int
    has_validation: bool
    validation_rules: List[str]


class ProtoFileInfo(NamedTuple):
    path: str
    relative_path: str
    has_validate_import: bool
    messages: List[str]
    total_fields: int
    validated_fields: int
    validation_coverage: float
    field_details: List[FieldInfo]
    issues: List[str]


def analyze_proto_file(file_path: Path, base_path: Path) -> ProtoFileInfo:
    """Analyze a single proto file for validation status."""
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    relative_path = str(file_path.relative_to(base_path))

    # Check for validate import
    has_validate_import = bool(
        re.search(r'import\s+"buf/validate/validate\.proto"', content)
    )

    # Find all messages
    message_pattern = r"message\s+(\w+)\s*\{"
    messages = re.findall(message_pattern, content)

    # Analyze fields
    field_details = []
    total_fields = 0
    validated_fields = 0
    issues = []

    # Extract all field definitions with validation
    field_pattern = r"(\w+)\s+(\w+)\s*=\s*(\d+)\s*(?:\[([^\]]*)\])?;"
    fields = re.findall(field_pattern, content, re.MULTILINE)

    for field_type, field_name, field_number, field_options in fields:
        if field_name in [
            "state",
            "sizeCache",
            "unknownFields",
        ]:  # Skip generated fields
            continue

        total_fields += 1
        has_validation = False
        validation_rules = []

        if field_options:
            # Check for buf.validate rules
            if "buf.validate.field" in field_options:
                has_validation = True
                validated_fields += 1

                # Extract specific validation rules
                validation_patterns = [
                    r"required\s*=\s*true",
                    r"string\.min_len\s*=\s*\d+",
                    r"string\.max_len\s*=\s*\d+",
                    r'string\.pattern\s*=\s*"[^"]*"',
                    r"string\.email\s*=\s*true",
                    r"string\.uuid\s*=\s*true",
                    r"int32\.gte\s*=\s*\d+",
                    r"int32\.lte\s*=\s*\d+",
                    r"uint32\.gte\s*=\s*\d+",
                    r"uint32\.lte\s*=\s*\d+",
                    r"repeated\.min_items\s*=\s*\d+",
                    r"repeated\.max_items\s*=\s*\d+",
                ]

                for pattern in validation_patterns:
                    matches = re.findall(pattern, field_options)
                    validation_rules.extend(matches)

        field_details.append(
            FieldInfo(
                name=field_name,
                type=field_type,
                number=int(field_number),
                has_validation=has_validation,
                validation_rules=validation_rules,
            )
        )

    # Calculate validation coverage
    validation_coverage = (
        (validated_fields / total_fields * 100) if total_fields > 0 else 0
    )

    # Check for common issues
    if not has_validate_import and validated_fields > 0:
        issues.append("Has validation rules but missing validate import")
    if has_validate_import and validated_fields == 0:
        issues.append("Has validate import but no validation rules")
    if total_fields > 0 and validation_coverage < 50:
        issues.append(f"Low validation coverage ({validation_coverage:.1f}%)")

    return ProtoFileInfo(
        path=str(file_path),
        relative_path=relative_path,
        has_validate_import=has_validate_import,
        messages=messages,
        total_fields=total_fields,
        validated_fields=validated_fields,
        validation_coverage=validation_coverage,
        field_details=field_details,
        issues=issues,
    )


def generate_status_report(base_path: Path) -> str:
    """Generate the complete proto status report."""
    proto_files = []

    # Find all proto files
    for proto_file in base_path.rglob("proto/**/*.proto"):
        if proto_file.is_file():
            proto_info = analyze_proto_file(proto_file, base_path)
            proto_files.append(proto_info)

    # Sort by relative path for consistent ordering
    proto_files.sort(key=lambda x: x.relative_path)

    # Generate report
    report = f"""# Protocol Buffer Validation Status Report

**Generated:** {datetime.now().strftime("%B %d, %Y at %H:%M:%S")}
**Total Proto Files:** {len(proto_files)}
**Repository:** gcommon

## Summary Statistics

"""

    # Calculate summary stats
    total_files = len(proto_files)
    files_with_import = sum(1 for f in proto_files if f.has_validate_import)
    files_with_validation = sum(1 for f in proto_files if f.validated_fields > 0)
    total_fields = sum(f.total_fields for f in proto_files)
    total_validated = sum(f.validated_fields for f in proto_files)
    overall_coverage = (total_validated / total_fields * 100) if total_fields > 0 else 0

    report += f"""- **Files with validate import:** {files_with_import}/{total_files} ({files_with_import / total_files * 100:.1f}%)
- **Files with validation rules:** {files_with_validation}/{total_files} ({files_with_validation / total_files * 100:.1f}%)
- **Total fields:** {total_fields}
- **Validated fields:** {total_validated}
- **Overall validation coverage:** {overall_coverage:.1f}%

## Validation Status by File

| File | Import | Messages | Fields | Validated | Coverage | Issues |
|------|--------|----------|--------|-----------|----------|--------|
"""

    # Add table rows
    for proto_info in proto_files:
        import_status = "✅" if proto_info.has_validate_import else "❌"
        coverage_emoji = (
            "🟢"
            if proto_info.validation_coverage >= 80
            else "🟡"
            if proto_info.validation_coverage >= 50
            else "🔴"
        )
        issues_text = "; ".join(proto_info.issues) if proto_info.issues else "None"

        report += f"| `{proto_info.relative_path}` | {import_status} | {len(proto_info.messages)} | {proto_info.total_fields} | {proto_info.validated_fields} | {coverage_emoji} {proto_info.validation_coverage:.1f}% | {issues_text} |\n"

    # Add detailed field analysis
    report += f"""

## Detailed Field Analysis

### Files Needing Attention

"""

    # Files with issues
    problematic_files = [
        f for f in proto_files if f.issues or f.validation_coverage < 100
    ]

    for proto_info in problematic_files:
        report += f"""
#### `{proto_info.relative_path}`

- **Messages:** {", ".join(proto_info.messages) if proto_info.messages else "None"}
- **Total Fields:** {proto_info.total_fields}
- **Validated Fields:** {proto_info.validated_fields}
- **Coverage:** {proto_info.validation_coverage:.1f}%
- **Issues:** {"; ".join(proto_info.issues) if proto_info.issues else "None"}

**Field Details:**
"""

        if proto_info.field_details:
            report += "| Field | Type | Validated | Rules |\n"
            report += "|-------|------|-----------|-------|\n"

            for field in proto_info.field_details:
                validation_status = "✅" if field.has_validation else "❌"
                rules_text = (
                    ", ".join(field.validation_rules)
                    if field.validation_rules
                    else "None"
                )
                report += f"| `{field.name}` | {field.type} | {validation_status} | {rules_text} |\n"
        else:
            report += "No fields found in this file.\n"

    # Add recommendations
    report += f"""

## Recommendations

### Priority Actions

1. **Missing Validate Imports:** {len([f for f in proto_files if not f.has_validate_import and f.total_fields > 0])} files need `import "buf/validate/validate.proto"`
2. **Unvalidated Fields:** {total_fields - total_validated} fields across all files need validation rules
3. **Low Coverage Files:** {len([f for f in proto_files if f.validation_coverage < 80 and f.total_fields > 0])} files have less than 80% validation coverage

### Validation Rules to Consider

Common validation patterns that should be applied:

- **String fields:** `min_len`, `max_len`, `pattern` for format validation
- **Email fields:** `string.email = true`
- **UUID fields:** `string.uuid = true`
- **Required fields:** `required = true`
- **Numeric ranges:** `gte`, `lte` for min/max values
- **Repeated fields:** `min_items`, `max_items` for array constraints

### Files Ready for MCP/Agent Processing

Files that need validation work (sorted by priority):

"""

    # List files that need work, sorted by priority
    needs_work = sorted(
        [f for f in proto_files if f.validation_coverage < 100 or f.issues],
        key=lambda x: (
            not x.has_validate_import,
            -x.validation_coverage,
            x.total_fields,
        ),
    )

    for i, proto_info in enumerate(needs_work[:10], 1):  # Top 10 priority files
        priority = (
            "HIGH"
            if not proto_info.has_validate_import or proto_info.validation_coverage < 50
            else "MEDIUM"
        )
        report += f"{i}. **{priority}:** `{proto_info.relative_path}` - {proto_info.total_fields - proto_info.validated_fields} unvalidated fields\n"

    if len(needs_work) > 10:
        report += f"\n... and {len(needs_work) - 10} more files needing attention.\n"

    report += f"""

---
*Report generated by `scripts/generate_proto_status.py`*
*To update this report, run: `python scripts/generate_proto_status.py`*
"""

    return report


def main():
    """Main function to generate and write the status report."""
    base_path = Path(__file__).parent.parent
    report_path = base_path / "PROTO_STATUS.md"

    print(f"Analyzing proto files in {base_path}...")
    report_content = generate_status_report(base_path)

    print(f"Writing status report to {report_path}...")
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report_content)

    print("✅ Proto validation status report generated successfully!")
    print(f"📄 Report available at: {report_path}")


if __name__ == "__main__":
    main()
