#!/usr/bin/env python3
# file: tools/protovalidate-adder.py
# version: 1.0.0
# guid: 123e4567-e89b-12d3-a456-426614174000

"""
Protovalidate Integration Tool for gcommon Repository

This tool automatically adds protovalidate validation rules to protobuf files
based on intelligent field analysis and semantic recognition patterns.

Key Features:
- Processes thousands of proto files efficiently
- Intelligent rule generation based on field semantics
- Dry-run mode for safe preview of changes
- Compatibility mode for environments without protovalidate
- Preserves existing validation rules
- Automatic import detection and addition

Usage:
    python3 tools/protovalidate-adder.py                     # Process all files
    python3 tools/protovalidate-adder.py --dry-run           # Preview changes
    python3 tools/protovalidate-adder.py --file path.proto   # Process specific file
    python3 tools/protovalidate-adder.py --compatibility-mode # Add as comments
"""

import argparse
import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple
import logging


class ProtoValidateAdder:
    """Main class for adding protovalidate rules to proto files."""
    
    def __init__(self, dry_run: bool = False, compatibility_mode: bool = False):
        self.dry_run = dry_run
        self.compatibility_mode = compatibility_mode
        self.processed_files = 0
        self.modified_files = 0
        self.errors = []
        
        # Setup logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)
        
        # Validation rule patterns based on field semantics
        self.field_patterns = {
            # ID fields - require minimum length
            r'.*_id$|^id$': {
                'string': '[(validate.rules).string.min_len = 1]'
            },
            
            # Email fields - email validation
            r'.*email.*': {
                'string': '[(validate.rules).string.pattern = "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\\\.[a-zA-Z]{2,}$"]'
            },
            
            # Age fields - reasonable range
            r'.*age.*': {
                'int32': '[(validate.rules).int32.gte = 0, (validate.rules).int32.lte = 150]'
            },
            
            # URL fields - URI validation
            r'.*url.*|.*uri.*': {
                'string': '[(validate.rules).string.uri = true]'
            },
            
            # Port fields - valid port range
            r'.*port.*': {
                'int32': '[(validate.rules).int32.gte = 1, (validate.rules).int32.lte = 65535]'
            },
            
            # Percentage fields - 0-100 range
            r'.*percent.*|.*percentage.*': {
                'float': '[(validate.rules).float.gte = 0.0, (validate.rules).float.lte = 100.0]',
                'double': '[(validate.rules).double.gte = 0.0, (validate.rules).double.lte = 100.0]'
            },
            
            # Phone fields - basic pattern
            r'.*phone.*': {
                'string': '[(validate.rules).string.pattern = "^\\\\+?[1-9]\\\\d{1,14}$"]'
            },
            
            # Name fields - minimum length
            r'.*name.*|.*title.*': {
                'string': '[(validate.rules).string.min_len = 1]'
            },
            
            # Password fields - minimum length and pattern
            r'.*password.*': {
                'string': '[(validate.rules).string.min_len = 8]'
            },
            
            # Token fields - minimum length
            r'.*token.*': {
                'string': '[(validate.rules).string.min_len = 1]'
            },
            
            # Version fields - semantic version pattern
            r'.*version.*': {
                'string': '[(validate.rules).string.pattern = "^v?\\\\d+\\\\.\\\\d+\\\\.\\\\d+"]'
            },
            
            # Count/size fields - non-negative
            r'.*count.*|.*size.*|.*length.*': {
                'int32': '[(validate.rules).int32.gte = 0]',
                'int64': '[(validate.rules).int64.gte = 0]'
            },
            
            # Timeout fields - positive values
            r'.*timeout.*|.*duration.*': {
                'int32': '[(validate.rules).int32.gt = 0]',
                'int64': '[(validate.rules).int64.gt = 0]'
            },
            
            # Code fields (like TFA codes) - specific length requirements
            r'.*code.*': {
                'string': '[(validate.rules).string.min_len = 1]'
            }
        }
        
        # Default validation rules for field types
        self.default_rules = {
            'string': '[(validate.rules).string.min_len = 1]',
            'repeated': '[(validate.rules).repeated.min_items = 1]',
            'int32': '[(validate.rules).int32.gte = 0]',
            'int64': '[(validate.rules).int64.gte = 0]',
            'uint32': '[(validate.rules).uint32.gte = 0]',
            'uint64': '[(validate.rules).uint64.gte = 0]',
            'float': '[(validate.rules).float.gte = 0.0]',
            'double': '[(validate.rules).double.gte = 0.0]'
        }

    def find_proto_files(self, root_dir: str, specific_file: Optional[str] = None) -> List[Path]:
        """Find all proto files to process."""
        if specific_file:
            if os.path.exists(specific_file):
                return [Path(specific_file)]
            else:
                self.logger.error(f"Specified file not found: {specific_file}")
                return []
        
        proto_files = []
        root_path = Path(root_dir)
        
        for proto_file in root_path.rglob("*.proto"):
            proto_files.append(proto_file)
        
        self.logger.info(f"Found {len(proto_files)} proto files to process")
        return proto_files

    def has_validation_import(self, content: str) -> bool:
        """Check if the file already has the protovalidate import."""
        return 'import "buf/validate/validate.proto"' in content

    def has_existing_validation_rules(self, content: str) -> bool:
        """Check if the file already has validation rules."""
        return 'validate.rules' in content

    def add_validation_import(self, content: str) -> str:
        """Add the protovalidate import if missing."""
        if self.has_validation_import(content):
            return content
        
        lines = content.split('\n')
        insert_index = -1
        
        # Find the best place to insert the import (after existing imports)
        for i, line in enumerate(lines):
            if line.strip().startswith('import "'):
                insert_index = i + 1
            elif line.strip().startswith('option ') and insert_index == -1:
                insert_index = i
                break
        
        if insert_index == -1:
            # Find package declaration and insert after
            for i, line in enumerate(lines):
                if line.strip().startswith('package '):
                    insert_index = i + 2  # After package and blank line
                    break
        
        if insert_index != -1:
            import_line = 'import "buf/validate/validate.proto";'
            if self.compatibility_mode:
                import_line = f'// {import_line}  // Compatibility mode: uncomment when protovalidate is available'
            
            lines.insert(insert_index, import_line)
            lines.insert(insert_index + 1, '')  # Add blank line
        
        return '\n'.join(lines)

    def analyze_field(self, field_line: str) -> Tuple[Optional[str], Optional[str], Optional[str]]:
        """Analyze a field line and extract type, name, and existing validation."""
        # Match field patterns: [repeated] type name = number [options];
        field_pattern = r'^\s*(?:(repeated)\s+)?(\w+(?:\.\w+)*)\s+(\w+)\s*=\s*\d+(?:\s*\[(.*?)\])?\s*;?\s*$'
        match = re.match(field_pattern, field_line.strip())
        
        if not match:
            return None, None, None
        
        repeated, field_type, field_name, existing_options = match.groups()
        
        # Check if validation rules already exist
        if existing_options and 'validate.rules' in existing_options:
            return field_type, field_name, existing_options
        
        return field_type, field_name, None

    def generate_validation_rule(self, field_type: str, field_name: str, is_repeated: bool = False) -> Optional[str]:
        """Generate appropriate validation rule for a field."""
        # Skip fields that are likely to be optional or complex types
        skip_patterns = [
            r'.*metadata.*', r'.*timestamp.*', r'.*any.*'
        ]
        
        for pattern in skip_patterns:
            if re.match(pattern, field_name, re.IGNORECASE):
                return None
        
        # Handle repeated fields
        if is_repeated:
            return self.default_rules.get('repeated')
        
        # Check for pattern-based rules
        for pattern, rules in self.field_patterns.items():
            if re.match(pattern, field_name, re.IGNORECASE):
                if field_type in rules:
                    return rules[field_type]
        
        # Use default rules for basic types
        if field_type in self.default_rules:
            return self.default_rules[field_type]
        
        return None

    def process_message_fields(self, content: str) -> str:
        """Process all fields in messages and add validation rules."""
        lines = content.split('\n')
        modified = False
        in_message = False
        
        for i, line in enumerate(lines):
            stripped = line.strip()
            
            # Track message boundaries
            if stripped.startswith('message ') and stripped.endswith('{'):
                in_message = True
                continue
            elif stripped == '}' and in_message:
                in_message = False
                continue
            
            # Process field lines within messages
            if in_message and not stripped.startswith('//') and not stripped.startswith('/*'):
                field_type, field_name, existing_validation = self.analyze_field(line)
                
                if field_type and field_name and not existing_validation:
                    is_repeated = 'repeated' in line
                    validation_rule = self.generate_validation_rule(field_type, field_name, is_repeated)
                    
                    if validation_rule:
                        # Add validation rule to the field
                        if line.rstrip().endswith(';'):
                            # Replace the semicolon with validation rule
                            new_line = line.rstrip()[:-1] + f' {validation_rule};'
                        else:
                            # Add validation rule before any existing options
                            new_line = line.rstrip() + f' {validation_rule}'
                        
                        if self.compatibility_mode:
                            # Add as comment
                            new_line = line.rstrip() + f'  // Validation: {validation_rule}'
                        
                        lines[i] = new_line
                        modified = True
                        
                        self.logger.debug(f"Added validation to {field_name}: {validation_rule}")
        
        return '\n'.join(lines) if modified else content

    def process_file(self, file_path: Path) -> bool:
        """Process a single proto file."""
        try:
            self.logger.info(f"Processing: {file_path}")
            
            # Read file content
            with open(file_path, 'r', encoding='utf-8') as f:
                original_content = f.read()
            
            # Skip if already has validation rules and not in compatibility mode
            if self.has_existing_validation_rules(original_content) and not self.compatibility_mode:
                self.logger.info(f"Skipping {file_path} (already has validation rules)")
                return False
            
            content = original_content
            
            # Add import if needed
            if not self.compatibility_mode:
                content = self.add_validation_import(content)
            
            # Process message fields
            content = self.process_message_fields(content)
            
            # Check if content was modified
            if content != original_content:
                if self.dry_run:
                    self.logger.info(f"Would modify: {file_path}")
                    print(f"\n--- Changes for {file_path} ---")
                    self._show_diff(original_content, content)
                else:
                    # Write modified content
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    self.logger.info(f"Modified: {file_path}")
                
                return True
            else:
                self.logger.debug(f"No changes needed for: {file_path}")
                return False
                
        except Exception as e:
            error_msg = f"Error processing {file_path}: {str(e)}"
            self.logger.error(error_msg)
            self.errors.append(error_msg)
            return False

    def _show_diff(self, original: str, modified: str):
        """Show a simple diff between original and modified content."""
        orig_lines = original.split('\n')
        mod_lines = modified.split('\n')
        
        for i, (orig, mod) in enumerate(zip(orig_lines, mod_lines)):
            if orig != mod:
                print(f"Line {i+1}:")
                print(f"  - {orig}")
                print(f"  + {mod}")

    def run(self, root_dir: str = "proto", specific_file: Optional[str] = None) -> bool:
        """Run the protovalidate adder."""
        self.logger.info("Starting protovalidate integration")
        
        if self.dry_run:
            self.logger.info("Running in DRY-RUN mode - no files will be modified")
        
        if self.compatibility_mode:
            self.logger.info("Running in COMPATIBILITY mode - validation rules will be added as comments")
        
        # Find proto files
        proto_files = self.find_proto_files(root_dir, specific_file)
        
        if not proto_files:
            self.logger.warning("No proto files found to process")
            return False
        
        # Process each file
        for proto_file in proto_files:
            self.processed_files += 1
            if self.process_file(proto_file):
                self.modified_files += 1
        
        # Report results
        self.logger.info(f"Processing complete:")
        self.logger.info(f"  Files processed: {self.processed_files}")
        self.logger.info(f"  Files modified: {self.modified_files}")
        
        if self.errors:
            self.logger.error(f"  Errors encountered: {len(self.errors)}")
            for error in self.errors:
                self.logger.error(f"    {error}")
            return False
        
        return True


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Add protovalidate validation rules to protobuf files",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                          # Process all proto files
  %(prog)s --dry-run                # Preview changes without modification
  %(prog)s --file path/to/file.proto # Process specific file
  %(prog)s --compatibility-mode     # Add rules as comments
  %(prog)s --root-dir custom/proto   # Use custom proto directory
        """
    )
    
    parser.add_argument(
        '--dry-run', 
        action='store_true',
        help='Preview changes without modifying files'
    )
    
    parser.add_argument(
        '--compatibility-mode',
        action='store_true', 
        help='Add validation rules as comments for environments without protovalidate'
    )
    
    parser.add_argument(
        '--file',
        help='Process specific proto file instead of all files'
    )
    
    parser.add_argument(
        '--root-dir',
        default='proto',
        help='Root directory containing proto files (default: proto)'
    )
    
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Enable verbose logging'
    )
    
    args = parser.parse_args()
    
    # Set logging level
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    # Create and run the adder
    adder = ProtoValidateAdder(
        dry_run=args.dry_run,
        compatibility_mode=args.compatibility_mode
    )
    
    success = adder.run(
        root_dir=args.root_dir,
        specific_file=args.file
    )
    
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()