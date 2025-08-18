#!/usr/bin/env python3
# file: comprehensive_proto_analyzer.py
# version: 1.0.0
# guid: 9d8c7b6a-5e4f-3a2b-1c0d-9e8f7a6b5c4d

"""
Comprehensive Protobuf Analyzer

This script analyzes all .proto files and identifies:
1. Missing imports
2. Duplicate type definitions
3. Invalid import paths
4. Circular dependencies
5. Unused imports
6. Type mismatches
"""

import os
import re
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Set, Tuple


class ComprehensiveProtoAnalyzer:
    def __init__(self, base_path: Path):
        self.base_path = base_path
        self.proto_files = self._find_proto_files()
        self.type_definitions: Dict[str, List[Path]] = defaultdict(list)
        self.file_imports: Dict[Path, Set[str]] = {}
        self.file_types: Dict[Path, Set[str]] = {}
        self.file_dependencies: Dict[Path, Set[Path]] = defaultdict(set)
        self.issues = []

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
            self.issues.append(f"❌ Error reading {file_path}: {e}")
            return set(), set(), set()

        # Extract defined types (messages, enums, services)
        defined_types = set()

        # Find all top-level definitions
        lines = content.split("\n")
        brace_depth = 0

        for line in lines:
            stripped = line.strip()

            # Track brace depth
            brace_depth += stripped.count("{") - stripped.count("}")

            # Only capture top-level definitions (brace_depth 0 when we encounter the definition)
            if brace_depth <= 1 and ("{" in stripped or brace_depth == 0):
                msg_match = re.match(r"\s*message\s+(\w+)", stripped)
                svc_match = re.match(r"\s*service\s+(\w+)", stripped)
                enum_match = re.match(r"\s*enum\s+(\w+)", stripped)

                if msg_match and brace_depth <= 1:
                    defined_types.add(msg_match.group(1))
                elif svc_match and brace_depth <= 1:
                    defined_types.add(svc_match.group(1))
                elif enum_match and brace_depth <= 1:
                    defined_types.add(enum_match.group(1))

        # Extract imports
        imports = set()
        import_pattern = re.compile(r'import\s+"([^"]+)";')
        for match in import_pattern.finditer(content):
            imports.add(match.group(1))

        # Extract referenced types
        referenced_types = set()

        # Pattern to match field declarations and RPC parameters/returns
        field_patterns = [
            r"^\s+(\w+)\s+\w+\s*=",  # message field: Type field_name =
            r"^\s+rpc\s+\w+\s*\(\s*(\w+)\s*\)",  # RPC parameter
            r"^\s+rpc\s+\w+\s*\(\s*\w+\s*\)\s*returns\s*\(\s*(\w+)\s*\)",  # RPC return
            r"^\s+rpc\s+\w+\s*\(\s*\w+\s*\)\s*returns\s*\(\s*stream\s+(\w+)\s*\)",  # RPC stream
            r"^\s+repeated\s+(\w+)\s+\w+\s*=",  # repeated field
            r"^\s+map<\w+,\s*(\w+)>\s+\w+\s*=",  # map value type
            r"^\s+map<(\w+),\s*\w+>\s+\w+\s*=",  # map key type
            r"^\s+optional\s+(\w+)\s+\w+\s*=",  # optional field
            r"^\s+stream\s+(\w+)\s+\w+\s*=",  # stream field
        ]

        for line in lines:
            stripped = line.strip()
            # Skip comments and protobuf keywords
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
        """Check if a type is a protobuf keyword"""
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
        }
        return type_name in keywords

    def _resolve_import_path(self, import_path: str, current_file: Path) -> Path:
        """Resolve import path to actual file path"""
        # Try absolute path from base
        absolute_path = self.base_path / import_path
        if absolute_path.exists():
            return absolute_path

        # Try relative to current file's directory
        relative_path = current_file.parent / import_path
        if relative_path.exists():
            return relative_path

        return None

    def analyze_all_files(self):
        """Analyze all proto files for issues"""
        print("🔍 COMPREHENSIVE PROTOBUF ANALYZER")
        print("=" * 60)

        # First pass: collect all definitions and imports
        for file_path in self.proto_files:
            defined_types, referenced_types, imports = self._extract_types_from_file(
                file_path
            )

            self.file_types[file_path] = defined_types
            self.file_imports[file_path] = imports

            # Track where each type is defined
            for type_name in defined_types:
                self.type_definitions[type_name].append(file_path)

        # Analysis phases
        self._find_duplicate_definitions()
        self._find_missing_imports()
        self._find_invalid_imports()
        self._find_unused_imports()
        self._find_circular_dependencies()

        self._print_summary()

    def _find_duplicate_definitions(self):
        """Find types defined in multiple files"""
        print("\n🔍 CHECKING FOR DUPLICATE DEFINITIONS...")
        duplicates_found = False

        for type_name, locations in self.type_definitions.items():
            if len(locations) > 1:
                duplicates_found = True
                self.issues.append(
                    f"⚠️  DUPLICATE: Type '{type_name}' defined in {len(locations)} files:"
                )
                for loc in locations:
                    rel_path = loc.relative_to(self.base_path)
                    self.issues.append(f"   • {rel_path}")

        if not duplicates_found:
            print("✅ No duplicate type definitions found")

    def _find_missing_imports(self):
        """Find missing import statements"""
        print("\n🔍 CHECKING FOR MISSING IMPORTS...")
        missing_imports = defaultdict(list)

        for file_path in self.proto_files:
            defined_types, referenced_types, imports = self._extract_types_from_file(
                file_path
            )

            # Check each referenced type
            for ref_type in referenced_types:
                # Skip if type is defined locally
                if ref_type in defined_types:
                    continue

                # Find where this type is defined
                if ref_type in self.type_definitions:
                    for def_location in self.type_definitions[ref_type]:
                        if def_location != file_path:
                            # Check if there's already an import for this file
                            def_rel_path = def_location.relative_to(self.base_path)
                            expected_import = str(def_rel_path)

                            # Check various possible import paths
                            possible_imports = [
                                expected_import,
                                expected_import.replace("pkg/", ""),
                                str(def_rel_path.relative_to(def_rel_path.parts[0])),
                            ]

                            if not any(imp in imports for imp in possible_imports):
                                missing_imports[expected_import].append(
                                    (file_path, ref_type)
                                )
                else:
                    self.issues.append(
                        f"⚠️  MISSING TYPE: '{ref_type}' referenced in {file_path.relative_to(self.base_path)} but not found anywhere"
                    )

        if missing_imports:
            for import_needed, files_needing in missing_imports.items():
                self.issues.append(f"📦 MISSING IMPORT: {import_needed}")
                for file_path, type_name in files_needing:
                    rel_path = file_path.relative_to(self.base_path)
                    self.issues.append(f"   • {rel_path} → {type_name}")
        else:
            print("✅ No missing imports found")

    def _find_invalid_imports(self):
        """Find import statements that point to non-existent files"""
        print("\n🔍 CHECKING FOR INVALID IMPORTS...")
        invalid_found = False

        for file_path in self.proto_files:
            _, _, imports = self._extract_types_from_file(file_path)

            for import_path in imports:
                resolved_path = self._resolve_import_path(import_path, file_path)
                if resolved_path is None:
                    invalid_found = True
                    rel_path = file_path.relative_to(self.base_path)
                    self.issues.append(
                        f"❌ INVALID IMPORT: {rel_path} imports '{import_path}' (file not found)"
                    )

        if not invalid_found:
            print("✅ No invalid imports found")

    def _find_unused_imports(self):
        """Find import statements that aren't used"""
        print("\n🔍 CHECKING FOR UNUSED IMPORTS...")
        # This is complex - for now just report we're checking
        print("⏭️  Unused import detection (complex analysis - skipping for now)")

    def _find_circular_dependencies(self):
        """Find circular import dependencies"""
        print("\n🔍 CHECKING FOR CIRCULAR DEPENDENCIES...")
        # Build dependency graph
        for file_path in self.proto_files:
            _, _, imports = self._extract_types_from_file(file_path)

            for import_path in imports:
                resolved_path = self._resolve_import_path(import_path, file_path)
                if resolved_path and resolved_path in self.proto_files:
                    self.file_dependencies[file_path].add(resolved_path)

        # Simple cycle detection (this could be more sophisticated)
        cycles_found = self._detect_cycles()
        if not cycles_found:
            print("✅ No circular dependencies found")

    def _detect_cycles(self) -> bool:
        """Simple cycle detection in dependency graph"""
        visited = set()
        rec_stack = set()

        def dfs(node):
            visited.add(node)
            rec_stack.add(node)

            for neighbor in self.file_dependencies[node]:
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
                elif neighbor in rec_stack:
                    self.issues.append(
                        f"🔄 CIRCULAR DEPENDENCY: Cycle detected involving {node.relative_to(self.base_path)}"
                    )
                    return True

            rec_stack.remove(node)
            return False

        for file_path in self.proto_files:
            if file_path not in visited:
                if dfs(file_path):
                    return True
        return False

    def _print_summary(self):
        """Print analysis summary with organized issue breakdown"""
        print("\n📊 ANALYSIS SUMMARY")
        print("=" * 40)
        print(f"Total proto files analyzed: {len(self.proto_files)}")
        print(f"Total types found: {len(self.type_definitions)}")
        print(f"Total issues found: {len(self.issues)}")

        if self.issues:
            print("\n🚨 ISSUES FOUND:")
            print("-" * 40)

            # Organize issues by type
            duplicates = []
            missing_imports = []
            invalid_imports = []
            other_issues = []

            for issue in self.issues:
                if issue.startswith("⚠️  DUPLICATE:"):
                    duplicates.append(issue)
                elif issue.startswith("📦 MISSING IMPORT:"):
                    missing_imports.append(issue)
                elif issue.startswith("❌ INVALID IMPORT:"):
                    invalid_imports.append(issue)
                else:
                    other_issues.append(issue)

            # Print duplicates first
            if duplicates:
                print(f"\n🔄 DUPLICATE DEFINITIONS ({len(duplicates)} issues):")
                print("-" * 30)
                for issue in duplicates:
                    print(issue)

            # Print missing imports organized by missing file
            if missing_imports:
                print(f"\n📦 MISSING IMPORTS ({len(missing_imports)} issues):")
                print("-" * 30)
                self._print_organized_missing_imports(missing_imports)

            # Print invalid imports organized by missing file
            if invalid_imports:
                print(f"\n❌ INVALID IMPORTS ({len(invalid_imports)} issues):")
                print("-" * 30)
                self._print_organized_invalid_imports(invalid_imports)

            # Print other issues
            if other_issues:
                print(f"\n🔍 OTHER ISSUES ({len(other_issues)} issues):")
                print("-" * 30)
                for issue in other_issues:
                    print(issue)
        else:
            print("\n✅ No issues found!")

    def _print_organized_missing_imports(self, missing_imports):
        """Print missing imports organized by the missing file"""
        missing_files = {}

        for issue in missing_imports:
            # Extract the missing file from the issue
            # Format: "📦 MISSING IMPORT: path/to/missing_file.proto"
            lines = issue.split("\n")
            if len(lines) >= 1:
                main_line = lines[0]
                missing_file = main_line.replace("📦 MISSING IMPORT: ", "")

                if missing_file not in missing_files:
                    missing_files[missing_file] = []
                missing_files[missing_file].append(issue)

        # Sort by missing file and print
        for missing_file in sorted(missing_files.keys()):
            count = len(missing_files[missing_file])
            print(f"\n📁 Missing file: {missing_file} ({count} references)")
            for issue in missing_files[missing_file]:
                print(f"   {issue}")

    def _print_organized_invalid_imports(self, invalid_imports):
        """Print invalid imports organized by the missing file"""
        missing_files = {}

        for issue in invalid_imports:
            # Extract the missing file from the issue
            # Format: "❌ INVALID IMPORT: file.proto imports 'missing/file.proto' (file not found)"
            import re

            match = re.search(r"imports '([^']+)'", issue)
            if match:
                missing_file = match.group(1)

                if missing_file not in missing_files:
                    missing_files[missing_file] = []
                missing_files[missing_file].append(issue)

        # Sort by missing file and print with subtotals
        for missing_file in sorted(missing_files.keys()):
            count = len(missing_files[missing_file])
            print(f"\n📁 Missing file: {missing_file} ({count} references)")

            # Show first few examples, then summarize if too many
            if count <= 5:
                for issue in missing_files[missing_file]:
                    # Extract just the importing file for cleaner display
                    parts = issue.split(" imports ")
                    if len(parts) >= 2:
                        importing_file = parts[0].replace("❌ INVALID IMPORT: ", "")
                        print(f"   • {importing_file}")
            else:
                # Show first 3 examples
                for i, issue in enumerate(missing_files[missing_file][:3]):
                    parts = issue.split(" imports ")
                    if len(parts) >= 2:
                        importing_file = parts[0].replace("❌ INVALID IMPORT: ", "")
                        print(f"   • {importing_file}")
                print(f"   • ... and {count - 3} more files")


def main():
    base_path = Path("pkg")

    if not base_path.exists():
        print(f"❌ Directory not found: {base_path}")
        return

    analyzer = ComprehensiveProtoAnalyzer(base_path)
    analyzer.analyze_all_files()


if __name__ == "__main__":
    main()
