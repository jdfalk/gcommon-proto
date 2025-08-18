#!/usr/bin/env python3
# file: scripts/reorganize-to-three-categories.py
# version: 1.0.0
# guid: 1a2b3c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d

"""
Reorganize Protocol Buffer files into a simplified 3-category structure:
- enums: All enum definitions
- messages: All message types (requests, responses, configs, etc.)
- services: All service definitions

This script consolidates the fragmented api, config, types directories into the simplified structure.
"""

import argparse
import json
import os
import re
import shutil
from pathlib import Path
from typing import Dict, List


class ProtoReorganizer:
    def __init__(self, proto_root: str, dry_run: bool = False):
        self.proto_root = Path(proto_root)
        self.dry_run = dry_run
        self.moves = []
        self.deletions = []
        self.import_updates = {}

        # Domains to process
        self.domains = [
            "common",
            "config",
            "database",
            "media",
            "metrics",
            "organization",
            "queue",
            "web",
        ]

        # Categories to eliminate and consolidate
        self.categories_to_remove = ["api", "config", "types"]
        self.target_categories = ["enums", "messages", "services"]

    def analyze_proto_file(self, file_path: Path) -> str:
        """Analyze a proto file to determine if it contains enums, messages, or services."""
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            # Remove comments and strings to avoid false matches
            # Remove line comments
            content = re.sub(r"//.*", "", content)
            # Remove block comments
            content = re.sub(r"/\*.*?\*/", "", content, flags=re.DOTALL)
            # Remove string literals
            content = re.sub(r'"[^"]*"', "", content)

            # Count different types of definitions with more precise patterns
            # Look for actual definitions at the start of lines (allowing whitespace)
            enum_count = len(re.findall(r"^\s*enum\s+\w+\s*{", content, re.MULTILINE))
            message_count = len(
                re.findall(r"^\s*message\s+\w+\s*{", content, re.MULTILINE)
            )
            service_count = len(
                re.findall(r"^\s*service\s+\w+\s*{", content, re.MULTILINE)
            )

            # Determine primary category
            if service_count > 0:
                return "services"
            elif enum_count > 0 and message_count == 0:
                return "enums"
            else:
                return "messages"  # Default for mixed or message-only files

        except Exception as e:
            print(f"Warning: Could not analyze {file_path}: {e}")
            return "messages"  # Safe default

    def get_file_moves_for_domain(self, domain: str) -> List[Dict]:
        """Get all file moves needed for a specific domain."""
        domain_path = self.proto_root / domain
        if not domain_path.exists():
            print(f"Warning: Domain {domain} does not exist at {domain_path}")
            return []

        moves = []

        # Process files in categories that need to be eliminated
        for category in self.categories_to_remove:
            category_path = domain_path / category
            if not category_path.exists():
                continue

            # Get ALL proto files in this category (including subdirectories)
            for proto_file in category_path.rglob("*.proto"):
                target_category = self.analyze_proto_file(proto_file)
                target_path = domain_path / target_category / proto_file.name

                # Ensure unique filename in target directory
                counter = 1
                original_target = target_path
                while target_path.exists():
                    stem = original_target.stem
                    suffix = original_target.suffix
                    target_path = original_target.parent / f"{stem}_{counter}{suffix}"
                    counter += 1

                moves.append(
                    {
                        "source": proto_file,
                        "target": target_path,
                        "domain": domain,
                        "old_category": category,
                        "new_category": target_category,
                    }
                )

        # Also check files in existing target categories to fix misplaced files
        for category in self.target_categories:
            category_path = domain_path / category
            if not category_path.exists():
                continue

            # Get ALL proto files in this category
            for proto_file in category_path.rglob("*.proto"):
                correct_category = self.analyze_proto_file(proto_file)

                # Only move if the file is in the wrong category
                if correct_category != category:
                    target_path = domain_path / correct_category / proto_file.name

                    # Ensure unique filename in target directory
                    counter = 1
                    original_target = target_path
                    while target_path.exists():
                        stem = original_target.stem
                        suffix = original_target.suffix
                        target_path = (
                            original_target.parent / f"{stem}_{counter}{suffix}"
                        )
                        counter += 1

                    moves.append(
                        {
                            "source": proto_file,
                            "target": target_path,
                            "domain": domain,
                            "old_category": category,
                            "new_category": correct_category,
                        }
                    )

        return moves

    def ensure_target_directories(self):
        """Ensure all target directories exist."""
        for domain in self.domains:
            domain_path = self.proto_root / domain
            if not domain_path.exists():
                continue

            for category in self.target_categories:
                category_path = domain_path / category
                if not category_path.exists():
                    if not self.dry_run:
                        category_path.mkdir(parents=True, exist_ok=True)
                    print(
                        f"{'[DRY RUN] ' if self.dry_run else ''}Created directory: {category_path}"
                    )

    def move_files(self, moves: List[Dict]):
        """Execute the file moves."""
        for move in moves:
            source = move["source"]
            target = move["target"]

            if not self.dry_run:
                # Ensure target directory exists
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.move(str(source), str(target))

            print(f"{'[DRY RUN] ' if self.dry_run else ''}Moved: {source} -> {target}")

    def remove_empty_directories(self):
        """Remove empty directories from eliminated categories."""
        for domain in self.domains:
            domain_path = self.proto_root / domain
            if not domain_path.exists():
                continue

            for category in self.categories_to_remove:
                category_path = domain_path / category
                if category_path.exists():
                    try:
                        # Remove all empty subdirectories first (bottom-up)
                        for root, dirs, files in os.walk(category_path, topdown=False):
                            root_path = Path(root)
                            if not files and not dirs:  # Empty directory
                                if not self.dry_run:
                                    root_path.rmdir()
                                print(
                                    f"{'[DRY RUN] ' if self.dry_run else ''}Removed empty directory: {root_path}"
                                )

                        # Finally remove the main category directory if empty
                        if not any(category_path.iterdir()):
                            if not self.dry_run:
                                category_path.rmdir()
                            print(
                                f"{'[DRY RUN] ' if self.dry_run else ''}Removed empty directory: {category_path}"
                            )
                        else:
                            print(
                                f"Warning: Directory not empty, skipping: {category_path}"
                            )
                            # List remaining files (limit to avoid spam)
                            remaining = list(category_path.rglob("*"))
                            for item in remaining[:10]:  # Limit to first 10 items
                                print(f"  Remaining: {item}")
                            if len(remaining) > 10:
                                print(f"  ... and {len(remaining) - 10} more files")
                    except Exception as e:
                        print(
                            f"Warning: Could not remove directory {category_path}: {e}"
                        )

    def update_import_paths(self, moves: List[Dict]):
        """Update import paths in all proto files to reflect new structure."""
        # Build mapping of old paths to new paths
        path_mapping = {}
        for move in moves:
            old_import = f"gcommon/v1/{move['domain']}/{move['old_category']}/{move['source'].name}"
            new_import = f"gcommon/v1/{move['domain']}/{move['new_category']}/{move['source'].name}"
            path_mapping[old_import] = new_import

        # Update all proto files
        all_proto_files = []
        for domain in self.domains:
            domain_path = self.proto_root / domain
            if domain_path.exists():
                all_proto_files.extend(domain_path.rglob("*.proto"))

        for proto_file in all_proto_files:
            self.update_imports_in_file(proto_file, path_mapping)

    def update_imports_in_file(self, file_path: Path, path_mapping: Dict[str, str]):
        """Update import statements in a single proto file."""
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            original_content = content

            # Update import statements
            for old_path, new_path in path_mapping.items():
                # Match import statements with the old path
                import_pattern = rf'import\s+"({re.escape(old_path)})";'
                replacement = f'import "{new_path}";'
                content = re.sub(import_pattern, replacement, content)

            if content != original_content:
                if not self.dry_run:
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(content)
                print(
                    f"{'[DRY RUN] ' if self.dry_run else ''}Updated imports in: {file_path}"
                )

        except Exception as e:
            print(f"Warning: Could not update imports in {file_path}: {e}")

    def generate_report(self, all_moves: List[Dict]) -> Dict:
        """Generate a summary report of the reorganization."""
        report = {
            "total_files_moved": len(all_moves),
            "domains_processed": len(self.domains),
            "categories_eliminated": self.categories_to_remove,
            "target_categories": self.target_categories,
            "moves_by_domain": {},
            "moves_by_category": {},
        }

        # Group by domain
        for domain in self.domains:
            domain_moves = [m for m in all_moves if m["domain"] == domain]
            report["moves_by_domain"][domain] = len(domain_moves)

        # Group by target category
        for category in self.target_categories:
            category_moves = [m for m in all_moves if m["new_category"] == category]
            report["moves_by_category"][category] = len(category_moves)

        return report

    def run_reorganization(self):
        """Execute the complete reorganization process."""
        print("🔄 Starting Protocol Buffer Reorganization to 3-Category Structure")
        print(f"Proto root: {self.proto_root}")
        print(f"Dry run: {self.dry_run}")
        print(f"Domains: {', '.join(self.domains)}")
        print(f"Eliminating categories: {', '.join(self.categories_to_remove)}")
        print(f"Target categories: {', '.join(self.target_categories)}")
        print()

        # Step 1: Analyze all moves needed
        print("📊 Step 1: Analyzing file moves...")
        all_moves = []
        for domain in self.domains:
            domain_moves = self.get_file_moves_for_domain(domain)
            all_moves.extend(domain_moves)
            print(f"  {domain}: {len(domain_moves)} files to move")

        if not all_moves:
            print("✅ No files need to be moved. Structure already simplified.")
            return

        print(f"Total files to move: {len(all_moves)}")
        print()

        # Step 2: Ensure target directories exist
        print("📁 Step 2: Creating target directories...")
        self.ensure_target_directories()
        print()

        # Step 3: Move files
        print("🚚 Step 3: Moving files to new categories...")
        self.move_files(all_moves)
        print()

        # Step 4: Update import paths
        print("🔗 Step 4: Updating import paths...")
        self.update_import_paths(all_moves)
        print()

        # Step 5: Remove empty directories
        print("🗑️  Step 5: Removing empty directories...")
        self.remove_empty_directories()
        print()

        # Step 6: Generate report
        print("📋 Step 6: Generating report...")
        report = self.generate_report(all_moves)

        # Save report
        report_path = self.proto_root.parent / "reorganization_report.json"
        if not self.dry_run:
            with open(report_path, "w") as f:
                json.dump(report, f, indent=2)

        print("✅ Reorganization {'simulation ' if self.dry_run else ''}complete!")
        print("📊 Summary:")
        print(f"  - Files moved: {report['total_files_moved']}")
        print(f"  - Domains processed: {report['domains_processed']}")
        print(f"  - Categories eliminated: {len(self.categories_to_remove)}")
        print(f"  - Final structure: {', '.join(self.target_categories)}")
        print()

        print("📈 Moves by domain:")
        for domain, count in report["moves_by_domain"].items():
            print(f"  {domain}: {count} files")

        print()
        print("📈 Moves by target category:")
        for category, count in report["moves_by_category"].items():
            print(f"  {category}: {count} files")

        if not self.dry_run:
            print(f"\n📄 Detailed report saved to: {report_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Reorganize proto files into 3-category structure"
    )
    parser.add_argument(
        "--proto-root",
        default="proto/gcommon/v1",
        help="Root directory of proto files (default: proto/gcommon/v1)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be done without making changes",
    )
    parser.add_argument(
        "--domain", help="Process only a specific domain (default: all domains)"
    )

    args = parser.parse_args()

    # Resolve proto root path
    proto_root = Path(args.proto_root)
    if not proto_root.is_absolute():
        proto_root = Path.cwd() / proto_root

    if not proto_root.exists():
        print(f"Error: Proto root directory does not exist: {proto_root}")
        return 1

    # Create reorganizer
    reorganizer = ProtoReorganizer(proto_root, args.dry_run)

    # Filter to specific domain if requested
    if args.domain:
        if args.domain not in reorganizer.domains:
            print(
                f"Error: Unknown domain '{args.domain}'. Available: {', '.join(reorganizer.domains)}"
            )
            return 1
        reorganizer.domains = [args.domain]

    # Run reorganization
    try:
        reorganizer.run_reorganization()
        return 0
    except Exception as e:
        print(f"Error during reorganization: {e}")
        import traceback

        traceback.print_exc()
        return 1


if __name__ == "__main__":
    exit(main())
