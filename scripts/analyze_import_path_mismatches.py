#!/usr/bin/env python3
# file: analyze_import_path_mismatches.py
# version: 1.0.0
# guid: 8d7c6b5a-4e3f-2a1b-9c0d-8e7f6a5b4c3d

"""
Import Path Mismatch Analyzer

This script identifies mismatches between:
1. Actual file paths
2. File paths declared in header comments
3. Import statements referencing these files

The goal is to create a mapping of what files need to be moved or what import
statements need to be updated to resolve all missing import issues.
"""

import os
import re
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Set, Tuple


class ImportPathAnalyzer:
    def __init__(self, base_path: Path):
        self.base_path = base_path
        self.proto_files = self._find_proto_files()
        self.file_to_header_path: Dict[
            Path, str
        ] = {}  # actual_path -> header_declared_path
        self.header_path_to_file: Dict[
            str, Path
        ] = {}  # header_declared_path -> actual_path
        self.import_references: Dict[str, List[Path]] = defaultdict(
            list
        )  # imported_path -> [files_that_import_it]
        self.mismatches = []

    def _find_proto_files(self) -> List[Path]:
        """Find all .proto files"""
        proto_files = []
        for root, dirs, files in os.walk(self.base_path):
            for file in files:
                if file.endswith(".proto") and not file.endswith(".original"):
                    proto_files.append(Path(root) / file)
        return proto_files

    def _extract_header_path(self, file_path: Path) -> str:
        """Extract the file path declared in the header comment"""
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            # Look for file header comment
            header_match = re.search(r"//\s*file:\s*([^\n]+)", content)
            if header_match:
                return header_match.group(1).strip()
        except Exception as e:
            print(f"Error reading {file_path}: {e}")

        return ""

    def _extract_imports(self, file_path: Path) -> Set[str]:
        """Extract all import statements from a proto file"""
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            return set()

        imports = set()
        import_pattern = re.compile(r'import\s+"([^"]+)";')
        for match in import_pattern.finditer(content):
            import_path = match.group(1)
            # Skip google protobuf imports
            if not import_path.startswith("google/protobuf/"):
                imports.add(import_path)

        return imports

    def analyze(self):
        """Perform the complete analysis"""
        print("🔍 ANALYZING IMPORT PATH MISMATCHES")
        print("=" * 60)

        # Step 1: Build mappings
        print("\n📂 Building file path mappings...")
        for file_path in self.proto_files:
            # Get relative path from base
            rel_path = file_path.relative_to(self.base_path)

            # Extract header declared path
            header_path = self._extract_header_path(file_path)

            if header_path:
                self.file_to_header_path[rel_path] = header_path
                self.header_path_to_file[header_path] = rel_path

                # Check for mismatch
                if str(rel_path) != header_path:
                    self.mismatches.append(
                        {
                            "actual_path": str(rel_path),
                            "header_path": header_path,
                            "file_path": file_path,
                        }
                    )

        # Step 2: Collect all import references
        print("📋 Collecting import references...")
        for file_path in self.proto_files:
            rel_path = file_path.relative_to(self.base_path)
            imports = self._extract_imports(file_path)

            for import_path in imports:
                self.import_references[import_path].append(rel_path)

        # Step 3: Report findings
        self._report_findings()

    def _report_findings(self):
        """Report all findings"""
        print(f"\n📊 ANALYSIS RESULTS")
        print("=" * 60)
        print(f"Total proto files analyzed: {len(self.proto_files)}")
        print(f"Files with header path mismatches: {len(self.mismatches)}")
        print(f"Unique import paths referenced: {len(self.import_references)}")

        print(f"\n🚨 PATH MISMATCHES ({len(self.mismatches)} issues):")
        print("-" * 40)

        for mismatch in self.mismatches:
            print(f"📁 File: {mismatch['actual_path']}")
            print(f"   Header declares: {mismatch['header_path']}")
            print(f"   Actual location: {mismatch['actual_path']}")
            print()

        print(f"\n🔍 MISSING IMPORT ANALYSIS:")
        print("-" * 40)

        missing_files = []
        existing_but_wrong_path = []

        for import_path, referring_files in self.import_references.items():
            # Check if this import path exists as an actual file
            actual_file_path = self.base_path / import_path

            if actual_file_path.exists():
                # File exists at expected location
                continue
            elif import_path in self.header_path_to_file:
                # File exists but at different location than header declares
                actual_location = self.header_path_to_file[import_path]
                existing_but_wrong_path.append(
                    {
                        "import_path": import_path,
                        "actual_location": str(actual_location),
                        "referring_files": referring_files,
                    }
                )
            else:
                # Check if file exists anywhere with this name
                filename = Path(import_path).name
                found_files = []
                for file_path in self.proto_files:
                    if file_path.name == filename:
                        found_files.append(file_path.relative_to(self.base_path))

                missing_files.append(
                    {
                        "import_path": import_path,
                        "referring_files": referring_files,
                        "potential_matches": found_files,
                    }
                )

        print(
            f"\n📋 FILES THAT EXIST BUT IMPORT PATH IS WRONG ({len(existing_but_wrong_path)} issues):"
        )
        for item in existing_but_wrong_path:
            print(f"📁 Import: {item['import_path']}")
            print(f"   Actually at: {item['actual_location']}")
            print(f"   Referenced by: {len(item['referring_files'])} files")
            for ref_file in item["referring_files"][:3]:  # Show first 3
                print(f"     • {ref_file}")
            if len(item["referring_files"]) > 3:
                print(f"     ... and {len(item['referring_files']) - 3} more")
            print()

        print(f"\n📋 COMPLETELY MISSING FILES ({len(missing_files)} issues):")
        for item in missing_files:
            print(f"📁 Missing: {item['import_path']}")
            print(f"   Referenced by: {len(item['referring_files'])} files")
            if item["potential_matches"]:
                print(f"   Potential matches found:")
                for match in item["potential_matches"]:
                    print(f"     • {match}")
            for ref_file in item["referring_files"][:3]:  # Show first 3
                print(f"     Referenced by: {ref_file}")
            if len(item["referring_files"]) > 3:
                print(f"     ... and {len(item['referring_files']) - 3} more")
            print()

        # Generate fix suggestions
        self._generate_fix_suggestions(existing_but_wrong_path, missing_files)

    def _generate_fix_suggestions(self, wrong_path_files, missing_files):
        """Generate specific fix suggestions"""
        print(f"\n🔧 FIX SUGGESTIONS:")
        print("=" * 60)

        print(f"\n1️⃣ MOVE FILES TO MATCH THEIR DECLARED HEADER PATHS:")
        print("-" * 50)
        for mismatch in self.mismatches:
            print(f"mv '{mismatch['actual_path']}' '{mismatch['header_path']}'")

        print(f"\n2️⃣ OR UPDATE HEADER PATHS TO MATCH ACTUAL LOCATIONS:")
        print("-" * 50)
        for mismatch in self.mismatches:
            print(f"# In file {mismatch['actual_path']}:")
            print(f"# Change: // file: {mismatch['header_path']}")
            print(f"# To:     // file: {mismatch['actual_path']}")
            print()

        print(f"\n3️⃣ UPDATE IMPORT STATEMENTS FOR EXISTING FILES:")
        print("-" * 50)
        for item in wrong_path_files:
            print(
                f"# Files importing '{item['import_path']}' should import '{item['actual_location']}':"
            )
            for ref_file in item["referring_files"]:
                print(f"# In {ref_file}: change import path")
            print()

        print(f"\n4️⃣ CREATE MISSING FILES:")
        print("-" * 50)
        for item in missing_files:
            if not item["potential_matches"]:
                print(f"# Create missing file: {item['import_path']}")
                print(
                    f"# Required by: {', '.join(str(f) for f in item['referring_files'][:3])}"
                )
                print()


def main():
    base_path = Path(".")
    analyzer = ImportPathAnalyzer(base_path)
    analyzer.analyze()


if __name__ == "__main__":
    main()
