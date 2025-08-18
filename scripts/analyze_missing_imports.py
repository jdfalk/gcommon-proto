#!/usr/bin/env python3
# file: analyze_missing_imports.py
# version: 1.0.0
# guid: 9c8b7a6d-5e4f-3a2b-1c0d-9e8f7a6b5c4d

"""
Missing Proto Imports Analyzer

This script analyzes all .proto files and identifies missing imports by:
1. Finding all type references in each proto file
2. Checking if those types are imported or defined locally
3. Searching for where the missing types are actually defined
4. Grouping results by missing proto file for efficient batch fixing
"""

import os
import re
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Set, Tuple


class ProtoAnalyzer:
    def __init__(self, base_path: Path):
        self.base_path = base_path
        self.proto_files = self._find_proto_files()
        self.type_definitions: Dict[
            str, List[Path]
        ] = {}  # type_name -> [files that define it]
        self.file_imports: Dict[Path, Set[str]] = {}  # file -> set of imported files
        self.file_types: Dict[
            Path, Set[str]
        ] = {}  # file -> set of types defined in file
        self.missing_imports: Dict[str, List[Tuple[Path, List[str]]]] = defaultdict(
            list
        )

    def _find_proto_files(self) -> List[Path]:
        """Find all .proto files"""
        proto_files = []
        for root, dirs, files in os.walk(self.base_path):
            for file in files:
                if file.endswith(".proto") and not file.endswith(".original"):
                    proto_files.append(Path(root) / file)
        return proto_files

    def _extract_types_from_file(
        self, file_path: Path
    ) -> Tuple[Set[str], Set[str], Set[str]]:
        """Extract defined types, referenced types, and imports from a proto file"""
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            return set(), set(), set()

        # Extract defined types (messages, enums, services)
        defined_types = set()

        # Only count top-level definitions (not nested)
        lines = content.split("\n")
        brace_depth = 0

        for line in lines:
            stripped = line.strip()

            # Track brace depth to identify top-level vs nested
            brace_depth += stripped.count("{") - stripped.count("}")

            # Only capture definitions at brace_depth 0 (top-level)
            if brace_depth == 0 or (brace_depth == 1 and ("{" in stripped)):
                # Check for top-level definitions
                msg_match = re.match(r"\s*message\s+(\w+)", stripped)
                svc_match = re.match(r"\s*service\s+(\w+)", stripped)
                enum_match = re.match(r"\s*enum\s+(\w+)", stripped)

                if msg_match:
                    defined_types.add(msg_match.group(1))
                elif svc_match:
                    defined_types.add(svc_match.group(1))
                elif enum_match:
                    defined_types.add(enum_match.group(1))

        # Extract imports
        imports = set()
        import_pattern = re.compile(r'import\s+"([^"]+)";')
        for match in import_pattern.finditer(content):
            imports.add(match.group(1))

        # Extract referenced types (types used in fields, parameters, etc.)
        referenced_types = set()

        # Pattern to match field declarations and RPC parameters/returns
        field_patterns = [
            r"^\s+(\w+)\s+\w+\s*=",  # message field: Type field_name =
            r"^\s+rpc\s+\w+\s*\(\s*(\w+)\s*\)",  # RPC parameter: rpc Method(RequestType)
            r"^\s+rpc\s+\w+\s*\(\s*\w+\s*\)\s*returns\s*\(\s*(\w+)\s*\)",  # RPC return: returns (ResponseType)
            r"^\s+rpc\s+\w+\s*\(\s*\w+\s*\)\s*returns\s*\(\s*stream\s+(\w+)\s*\)",  # RPC stream return: returns (stream Type)
            r"^\s+repeated\s+(\w+)\s+\w+\s*=",  # repeated field: repeated Type field =
            r"^\s+map<\w+,\s*(\w+)>\s+\w+\s*=",  # map value type: map<string, ValueType>
            r"^\s+map<(\w+),\s*\w+>\s+\w+\s*=",  # map key type: map<KeyType, string>
            r"^\s+optional\s+(\w+)\s+\w+\s*=",  # optional field: optional Type field =
            r"^\s+stream\s+(\w+)\s+\w+\s*=",  # stream field: stream Type field =
        ]

        # Split content into lines to process more carefully
        lines = content.split("\n")
        for line in lines:
            # Skip comment lines and option lines
            stripped = line.strip()
            if (
                stripped.startswith("//")
                or stripped.startswith("option")
                or stripped.startswith("import")
                or stripped.startswith("package")
            ):
                continue

            for pattern in field_patterns:
                for match in re.finditer(pattern, line):
                    type_name = match.group(1)
                    # Filter out primitive types, well-known types, and protobuf keywords
                    if not self._is_primitive_type(
                        type_name
                    ) and not self._is_protobuf_keyword(type_name):
                        referenced_types.add(type_name)

        return defined_types, referenced_types, imports

    def _is_primitive_type(self, type_name: str) -> bool:
        """Check if a type is a primitive or well-known type"""
        primitives = {
            "bool",
            "int32",
            "int64",
            "uint32",
            "uint64",
            "sint32",
            "sint64",
            "fixed32",
            "fixed64",
            "sfixed32",
            "sfixed64",
            "float",
            "double",
            "string",
            "bytes",
            "Any",
            "Timestamp",
            "Duration",
            "Empty",
        }
        return type_name in primitives

    def _is_protobuf_keyword(self, type_name: str) -> bool:
        """Check if a type is a protobuf keyword that should not be treated as a missing type"""
        keywords = {
            "option",
            "import",
            "package",
            "syntax",
            "edition",
            "message",
            "service",
            "enum",
            "rpc",
            "returns",
            "stream",
            "repeated",
            "optional",
            "required",
            "map",
            "oneof",
            "reserved",
            "extensions",
            "extend",
            "group",
            "public",
            "weak",
            "true",
            "false",
            "max",
            "to",
            "inf",
            "nan",
            "features",
            "deprecated",
            "packed",
            "lazy",
            "unverified_lazy",
            "retention",
            "target",
            "targets",
            "TYPE_DOUBLE",
            "TYPE_FLOAT",
            "TYPE_INT64",
            "TYPE_UINT64",
            "TYPE_INT32",
            "TYPE_FIXED64",
            "TYPE_FIXED32",
            "TYPE_BOOL",
            "TYPE_STRING",
            "TYPE_GROUP",
            "TYPE_MESSAGE",
            "TYPE_BYTES",
            "TYPE_UINT32",
            "TYPE_ENUM",
            "TYPE_SFIXED32",
            "TYPE_SFIXED64",
            "TYPE_SINT32",
            "TYPE_SINT64",
        }
        return type_name in keywords

    def build_type_index(self):
        """Build an index of all types and where they're defined"""
        print("🔍 Building type index from all proto files...")

        for file_path in self.proto_files:
            defined_types, referenced_types, imports = self._extract_types_from_file(
                file_path
            )

            # Store file's defined types and imports
            self.file_types[file_path] = defined_types
            self.file_imports[file_path] = imports

            # Build global type index
            for type_name in defined_types:
                if type_name not in self.type_definitions:
                    self.type_definitions[type_name] = []
                self.type_definitions[type_name].append(file_path)

        print(
            f"   Found {len(self.type_definitions)} unique types across {len(self.proto_files)} files"
        )

    def analyze_missing_imports(self):
        """Analyze each file for missing imports"""
        print("\n🔍 Analyzing missing imports...")

        for file_path in self.proto_files:
            defined_types, referenced_types, imports = self._extract_types_from_file(
                file_path
            )

            # Find types that are referenced but not defined locally or imported
            missing_types = []

            for ref_type in referenced_types:
                # Skip if defined in the same file
                if ref_type in defined_types:
                    continue

                # Check if the type is available through imports
                type_available = False

                # Check if any imported file defines this type
                for import_path in imports:
                    # Convert import path to actual file path
                    full_import_path = self.base_path / import_path
                    if full_import_path in self.file_types:
                        if ref_type in self.file_types[full_import_path]:
                            type_available = True
                            break

                if not type_available:
                    # Find where this type is actually defined
                    if ref_type in self.type_definitions:
                        defining_files = self.type_definitions[ref_type]
                        missing_types.append(ref_type)

                        # For each defining file, note that this file needs to import it
                        for defining_file in defining_files:
                            # Convert absolute path to import path
                            try:
                                import_path = defining_file.relative_to(self.base_path)
                                import_path_str = str(import_path)

                                if import_path_str not in self.missing_imports:
                                    self.missing_imports[import_path_str] = []

                                # Check if this file is already in the list for this import
                                existing_entry = None
                                for entry in self.missing_imports[import_path_str]:
                                    if entry[0] == file_path:
                                        existing_entry = entry
                                        break

                                if existing_entry:
                                    existing_entry[1].append(ref_type)
                                else:
                                    self.missing_imports[import_path_str].append(
                                        (file_path, [ref_type])
                                    )
                            except ValueError:
                                # File is outside base_path
                                continue
                    else:
                        # Type not found anywhere - might be an external type or error
                        print(
                            f"⚠️  Type '{ref_type}' referenced in {file_path.relative_to(self.base_path)} but not found anywhere"
                        )

    def generate_report(self):
        """Generate a comprehensive report of missing imports"""
        print("\n📊 MISSING IMPORTS ANALYSIS")
        print("=" * 80)

        if not self.missing_imports:
            print("✅ No missing imports found!")
            return

        # Sort by number of files that need each import (most needed first)
        sorted_imports = sorted(
            self.missing_imports.items(), key=lambda x: len(x[1]), reverse=True
        )

        print(f"Found {len(self.missing_imports)} proto files that need to be imported")
        print(
            f"Total files with missing imports: {sum(len(files) for _, files in self.missing_imports.items())}"
        )

        print("\n🔧 IMPORTS TO ADD (sorted by impact):")
        print("-" * 80)

        for import_path, needing_files in sorted_imports:
            print(f"\n📦 IMPORT: {import_path}")
            print(f"   Needed by {len(needing_files)} files:")

            for file_path, missing_types in needing_files:
                rel_path = file_path.relative_to(self.base_path)
                types_str = ", ".join(sorted(missing_types))
                print(f"   • {rel_path} → {types_str}")

    def generate_fix_commands(self):
        """Generate commands to fix the missing imports"""
        if not self.missing_imports:
            return

        print("\n🔧 AUTOMATED FIX COMMANDS:")
        print("-" * 80)

        # Group files by the imports they need
        file_fixes: Dict[Path, List[str]] = defaultdict(list)

        for import_path, needing_files in self.missing_imports.items():
            for file_path, missing_types in needing_files:
                file_fixes[file_path].append(import_path)

        # Generate sed commands to add imports
        script_lines = [
            "#!/bin/bash",
            "# Auto-generated script to fix missing proto imports",
            "",
        ]

        for file_path, needed_imports in file_fixes.items():
            script_lines.append(
                f"# Fix imports for {file_path.relative_to(self.base_path)}"
            )

            for import_path in needed_imports:
                # Add import after the last existing import or after package declaration
                sed_cmd = (
                    f'sed -i \'/^import.*proto";$/a import "{import_path}";'
                    + f"' '{file_path}'"
                )
                script_lines.append(sed_cmd)

            script_lines.append("")

        # Write fix script
        fix_script = Path("fix_missing_imports.sh")
        with open(fix_script, "w") as f:
            f.write("\n".join(script_lines))

        fix_script.chmod(0o755)
        print(f"💾 Created fix script: {fix_script}")
        print("   Run './fix_missing_imports.sh' to automatically add missing imports")


def main():
    base_path = Path("pkg/")

    print("🔍 PROTOBUF MISSING IMPORTS ANALYZER")
    print("=" * 60)
    print(f"Analyzing proto files in: {base_path.absolute()}\n")

    analyzer = ProtoAnalyzer(base_path)

    # Step 1: Build index of all types
    analyzer.build_type_index()

    # Step 2: Find missing imports
    analyzer.analyze_missing_imports()

    # Step 3: Generate report
    analyzer.generate_report()

    # Step 4: Generate fix commands
    analyzer.generate_fix_commands()


if __name__ == "__main__":
    main()
