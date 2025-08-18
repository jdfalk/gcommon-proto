#!/usr/bin/env python3
# file: split_proto_files.py
# version: 1.0.0
# guid: 9a8b7c6d-5e4f-3a2b-1c0d-9e8f7a6b5c4d

"""
Proto File 1-1-1 Pattern Enforcer

This script analyzes all .proto files and splits any that violate the 1-1-1 pattern
(one message/service/enum per file) into individual files following the protobuf
instructions guidelines.
"""

import os
import re
import sys
import uuid
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Set


@dataclass
class ProtoDefinition:
    """Represents a protobuf definition (message, service, enum)"""

    name: str
    type: str  # 'message', 'service', 'enum'
    content: str
    start_line: int
    end_line: int
    nested_types: List["ProtoDefinition"] = None

    def __post_init__(self):
        if self.nested_types is None:
            self.nested_types = []


@dataclass
class ProtoFile:
    """Represents a parsed protobuf file"""

    path: Path
    header: str  # File header (comments, edition, package, imports, options)
    definitions: List[ProtoDefinition]
    package: str
    imports: List[str]
    options: List[str]
    original_content: str


class ProtoParser:
    """Parses protobuf files and extracts definitions"""

    def __init__(self):
        # Regex patterns for proto parsing
        self.message_pattern = re.compile(r"^(\s*)message\s+(\w+)\s*\{", re.MULTILINE)
        self.service_pattern = re.compile(r"^(\s*)service\s+(\w+)\s*\{", re.MULTILINE)
        self.enum_pattern = re.compile(r"^(\s*)enum\s+(\w+)\s*\{", re.MULTILINE)
        self.package_pattern = re.compile(r"^package\s+([\w.]+)\s*;", re.MULTILINE)
        self.import_pattern = re.compile(r'^import\s+"([^"]+)"\s*;', re.MULTILINE)
        self.option_pattern = re.compile(r"^option\s+[^;]+;", re.MULTILINE)

    def parse_file(self, file_path: Path) -> ProtoFile:
        """Parse a protobuf file and extract all definitions"""
        print(f"Parsing {file_path}")

        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Extract package
        package_match = self.package_pattern.search(content)
        package = package_match.group(1) if package_match else ""

        # Extract imports
        imports = [match.group(1) for match in self.import_pattern.finditer(content)]

        # Extract options
        options = [match.group(0) for match in self.option_pattern.finditer(content)]

        # Find all definitions
        definitions = []

        # Find messages
        for match in self.message_pattern.finditer(content):
            definition = self._extract_definition(content, match, "message")
            if definition:
                definitions.append(definition)

        # Find services
        for match in self.service_pattern.finditer(content):
            definition = self._extract_definition(content, match, "service")
            if definition:
                definitions.append(definition)

        # Find enums
        for match in self.enum_pattern.finditer(content):
            definition = self._extract_definition(content, match, "enum")
            if definition:
                definitions.append(definition)

        # Extract header (everything before first definition)
        header_end = (
            min([d.start_line for d in definitions])
            if definitions
            else len(content.split("\n"))
        )
        header_lines = content.split("\n")[: header_end - 1]
        header = "\n".join(header_lines)

        return ProtoFile(
            path=file_path,
            header=header,
            definitions=definitions,
            package=package,
            imports=imports,
            options=options,
            original_content=content,
        )

    def _extract_definition(
        self, content: str, match: re.Match, def_type: str
    ) -> Optional[ProtoDefinition]:
        """Extract a complete definition (message/service/enum) with proper brace matching"""
        lines = content.split("\n")
        start_line = content[: match.start()].count("\n") + 1

        # Find the opening brace
        brace_line = start_line - 1
        while brace_line < len(lines) and "{" not in lines[brace_line]:
            brace_line += 1

        if brace_line >= len(lines):
            return None

        # Count braces to find the end
        brace_count = 0
        end_line = brace_line

        for line_num in range(brace_line, len(lines)):
            line = lines[line_num]
            # Count braces, but ignore those in comments or strings
            in_string = False
            in_comment = False
            i = 0
            while i < len(line):
                if not in_string and not in_comment:
                    if line[i : i + 2] == "//":
                        in_comment = True
                        i += 2
                        continue
                    elif line[i : i + 2] == "/*":
                        in_comment = True
                        i += 2
                        continue
                    elif line[i] == '"':
                        in_string = True
                    elif line[i] == "{":
                        brace_count += 1
                    elif line[i] == "}":
                        brace_count -= 1
                        if brace_count == 0:
                            end_line = line_num + 1
                            break
                elif in_string and line[i] == '"' and (i == 0 or line[i - 1] != "\\"):
                    in_string = False
                elif in_comment and line[i : i + 2] == "*/":
                    in_comment = False
                    i += 1
                i += 1

            if brace_count == 0:
                break

        if brace_count != 0:
            print(f"Warning: Unmatched braces in {def_type} {match.group(2)}")
            return None

        # Extract the content
        definition_lines = lines[start_line - 1 : end_line]
        definition_content = "\n".join(definition_lines)

        return ProtoDefinition(
            name=match.group(2),
            type=def_type,
            content=definition_content,
            start_line=start_line,
            end_line=end_line,
        )


class ProtoSplitter:
    """Splits proto files following the 1-1-1 pattern"""

    def __init__(self, base_path: Path):
        self.base_path = base_path
        self.processed_files: Set[Path] = set()
        self.created_files: List[Path] = []

    def split_proto_file(self, proto_file: ProtoFile) -> List[Path]:
        """Split a proto file into individual 1-1-1 files"""
        if len(proto_file.definitions) <= 1:
            print(f"✓ {proto_file.path.name} already follows 1-1-1 pattern")
            return []

        print(
            f"📂 Splitting {proto_file.path.name} ({len(proto_file.definitions)} definitions)"
        )

        created_files = []

        # Determine target directories based on definition types
        base_dir = proto_file.path.parent

        for definition in proto_file.definitions:
            new_file_path = self._get_target_path(base_dir, definition)
            new_content = self._generate_file_content(proto_file, definition)

            # Create directory if it doesn't exist
            new_file_path.parent.mkdir(parents=True, exist_ok=True)

            # Write the new file
            with open(new_file_path, "w", encoding="utf-8") as f:
                f.write(new_content)

            created_files.append(new_file_path)
            print(f"  ✓ Created {new_file_path.relative_to(self.base_path)}")

        # Mark original file for deletion/archiving
        if len(created_files) > 0:
            self._archive_original_file(proto_file.path)

        self.created_files.extend(created_files)
        return created_files

    def _get_target_path(self, base_dir: Path, definition: ProtoDefinition) -> Path:
        """Determine target path based on definition type and naming conventions"""
        name_snake = self._to_snake_case(definition.name)

        if definition.type == "service":
            return base_dir / "services" / f"{name_snake}.proto"
        elif definition.type == "enum":
            return base_dir / "enums" / f"{name_snake}.proto"
        elif definition.type == "message":
            # Determine if it's a request/response or general message
            if definition.name.endswith("Request"):
                return base_dir / "requests" / f"{name_snake}.proto"
            elif definition.name.endswith("Response"):
                return base_dir / "responses" / f"{name_snake}.proto"
            else:
                return base_dir / "messages" / f"{name_snake}.proto"
        else:
            return base_dir / f"{name_snake}.proto"

    def _to_snake_case(self, name: str) -> str:
        """Convert CamelCase to snake_case"""
        s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
        return re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1).lower()

    def _generate_file_content(
        self, proto_file: ProtoFile, definition: ProtoDefinition
    ) -> str:
        """Generate content for a new 1-1-1 proto file"""
        lines = []

        # File header
        target_path = self._get_target_path(proto_file.path.parent, definition)
        relative_path = target_path.relative_to(self.base_path)

        lines.append(f"// file: {relative_path}")
        lines.append("// version: 1.0.0")
        lines.append(f"// guid: {str(uuid.uuid4())}")
        lines.append("")

        # Edition
        lines.append('edition = "2023";')
        lines.append("")

        # Package
        if proto_file.package:
            lines.append(f"package {proto_file.package};")
            lines.append("")

        # Imports - filter to only necessary ones
        necessary_imports = self._get_necessary_imports(proto_file, definition)
        for import_line in necessary_imports:
            lines.append(f'import "{import_line}";')

        if necessary_imports:
            lines.append("")

        # Options
        for option in proto_file.options:
            lines.append(option)

        if proto_file.options:
            lines.append("")

        # Definition content
        lines.append(definition.content)
        lines.append("")

        return "\n".join(lines)

    def _get_necessary_imports(
        self, proto_file: ProtoFile, definition: ProtoDefinition
    ) -> List[str]:
        """Determine which imports are actually needed for this definition"""
        # For now, include all imports. In a more sophisticated version,
        # we could parse the definition content to see which types are actually used.
        necessary = []

        # Always include google protobuf imports if they exist
        for imp in proto_file.imports:
            if imp.startswith("google/protobuf/"):
                necessary.append(imp)

        # Add other imports that might be referenced in the definition
        # This is a simplified approach - could be enhanced with proper parsing
        for imp in proto_file.imports:
            if not imp.startswith("google/protobuf/"):
                # Check if any part of the import path appears in the definition
                import_parts = imp.split("/")
                if any(
                    part.lower() in definition.content.lower() for part in import_parts
                ):
                    necessary.append(imp)

        return necessary

    def _archive_original_file(self, file_path: Path):
        """Archive the original file by renaming it"""
        archive_path = file_path.with_suffix(".proto.original")
        if not archive_path.exists():
            file_path.rename(archive_path)
            print(f"  📦 Archived original to {archive_path.name}")


def find_proto_files(base_path: Path) -> List[Path]:
    """Find all .proto files in the given path"""
    proto_files = []
    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.endswith(".proto"):
                proto_files.append(Path(root) / file)
    return proto_files


def analyze_proto_violations(base_path: Path) -> Dict[str, List[Path]]:
    """Analyze all proto files and find 1-1-1 violations"""
    parser = ProtoParser()
    violations = {"multiple_definitions": [], "mixed_types": [], "complex_files": []}

    proto_files = find_proto_files(base_path)
    print(f"Found {len(proto_files)} proto files to analyze")

    for file_path in proto_files:
        try:
            proto_file = parser.parse_file(file_path)

            if len(proto_file.definitions) > 1:
                violations["multiple_definitions"].append(file_path)

                # Check if it has mixed types
                types = set(d.type for d in proto_file.definitions)
                if len(types) > 1:
                    violations["mixed_types"].append(file_path)

                # Check if it's very complex
                if len(proto_file.definitions) > 5:
                    violations["complex_files"].append(file_path)

        except Exception as e:
            print(f"Error parsing {file_path}: {e}")

    return violations


def main():
    """Main function to analyze and split proto files"""
    if len(sys.argv) > 1:
        base_path = Path(sys.argv[1])
    else:
        base_path = Path(".")

    print(f"Analyzing proto files in: {base_path.absolute()}")
    print("=" * 60)

    # Find violations
    violations = analyze_proto_violations(base_path)

    print("\n📊 ANALYSIS RESULTS:")
    print(f"Files with multiple definitions: {len(violations['multiple_definitions'])}")
    print(f"Files with mixed types: {len(violations['mixed_types'])}")
    print(f"Complex files (>5 definitions): {len(violations['complex_files'])}")

    if not violations["multiple_definitions"]:
        print("\n✅ All proto files already follow the 1-1-1 pattern!")
        return

    print("\n🔧 FILES TO SPLIT:")
    for file_path in violations["multiple_definitions"]:
        parser = ProtoParser()
        proto_file = parser.parse_file(file_path)
        types_summary = {}
        for d in proto_file.definitions:
            types_summary[d.type] = types_summary.get(d.type, 0) + 1

        summary = ", ".join(
            [
                f"{count} {dtype}{'s' if count > 1 else ''}"
                for dtype, count in types_summary.items()
            ]
        )
        print(f"  📄 {file_path.relative_to(base_path)}: {summary}")

    # Ask for confirmation
    response = (
        input(f"\nSplit {len(violations['multiple_definitions'])} files? [y/N]: ")
        .strip()
        .lower()
    )
    if response != "y":
        print("Aborted.")
        return

    # Split the files
    print("\n🚀 SPLITTING FILES:")
    print("=" * 60)

    parser = ProtoParser()
    splitter = ProtoSplitter(base_path)

    total_created = 0
    for file_path in violations["multiple_definitions"]:
        try:
            proto_file = parser.parse_file(file_path)
            created_files = splitter.split_proto_file(proto_file)
            total_created += len(created_files)
        except Exception as e:
            print(f"❌ Error splitting {file_path}: {e}")

    print("\n✅ COMPLETED:")
    print(f"Split {len(violations['multiple_definitions'])} files")
    print(f"Created {total_created} new 1-1-1 proto files")
    print(f"Archived {len(violations['multiple_definitions'])} original files")

    print("\n📋 NEXT STEPS:")
    print("1. Review the generated files")
    print("2. Update import statements in other files")
    print("3. Run 'buf generate' to regenerate Go code")
    print("4. Test the build")
    print("5. Remove .original files if everything works")


if __name__ == "__main__":
    main()
