#!/usr/bin/env python3
# file: fix_unused_imports.py
# version: 1.0.0
# guid: 7f8a4990-b647-4e5b-8ff8-c0eafe246789

"""
Fix unused imports in protobuf files based on buf lint output.

This script:
1. Removes unused buf/validate imports from files that don't use validation
2. Adds basic validation rules to files that should have them
3. Removes other unused imports
"""

import os
from pathlib import Path

# Files with unused buf/validate imports that should get validation rules
FILES_TO_ADD_VALIDATION = {
    "analysis_options.proto": [
        # Boolean fields don't need validation for basic usage
    ],
    "audio_extraction_options.proto": [
        (
            "string output_format = 1",
            "string output_format = 1 [(buf.validate.field).string.min_len = 1]",
        ),
        ("int32 bitrate = 2", "int32 bitrate = 2 [(buf.validate.field).int32.gte = 0]"),
        (
            "int32 sample_rate = 3",
            "int32 sample_rate = 3 [(buf.validate.field).int32.gte = 0]",
        ),
    ],
    "chapter_detection_options.proto": [
        # Will check the actual content
    ],
    "normalization_options.proto": [
        # Will check the actual content
    ],
    "subtitle_extraction_options.proto": [
        # Will check the actual content
    ],
    "upload_media_request.proto": [
        # Will check the actual content
    ],
}

# Files with unused imports that should be removed
FILES_TO_REMOVE_IMPORTS = {
    "audio_analysis.proto": [
        'import "gcommon/v1/media/media_quality.proto";',
        'import "google/protobuf/duration.proto";',
    ],
    "audio_stream_info.proto": [
        'import "gcommon/v1/media/media_quality.proto";',
        'import "google/protobuf/duration.proto";',
    ],
    "media_analysis.proto": ['import "google/protobuf/duration.proto";'],
    "scene_detection.proto": ['import "gcommon/v1/media/media_quality.proto";'],
    "silent_segment.proto": ['import "gcommon/v1/media/media_quality.proto";'],
    "split_audio_request.proto": ['import "google/protobuf/duration.proto";'],
    "subtitle_stream_info.proto": [
        'import "gcommon/v1/media/media_quality.proto";',
        'import "google/protobuf/duration.proto";',
    ],
    "technical_metadata.proto": ['import "gcommon/v1/media/media_quality.proto";'],
    "thumbnail_info.proto": ['import "gcommon/v1/media/media_quality.proto";'],
    "upload_media_request.proto": ['import "gcommon/v1/media/media_metadata.proto";'],
    "video_stream_info.proto": [
        'import "gcommon/v1/media/media_quality.proto";',
        'import "google/protobuf/duration.proto";',
    ],
}

# Files that should have unused buf/validate import removed (no validation needed)
FILES_TO_REMOVE_VALIDATION_IMPORT = [
    "analysis_options.proto",  # Boolean fields don't need validation
    "chapter_detection_options.proto",
    "normalization_options.proto",
    "silent_segment.proto",
    "split_audio_request.proto",
    "subtitle_extraction_options.proto",
    "upload_media_request.proto",
]


def read_file(filepath):
    """Read file content."""
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


def write_file(filepath, content):
    """Write file content."""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)


def add_validation_rules(content, filename):
    """Add validation rules to fields that need them."""
    if filename not in FILES_TO_ADD_VALIDATION:
        return content

    lines = content.split("\n")
    modified_lines = []

    for line in lines:
        line_modified = False

        # Apply specific field replacements
        for old_pattern, new_pattern in FILES_TO_ADD_VALIDATION[filename]:
            if old_pattern in line:
                modified_lines.append(line.replace(old_pattern, new_pattern))
                print(f"Added validation to {filename}: {old_pattern}")
                line_modified = True
                break

        if not line_modified:
            modified_lines.append(line)

    return "\n".join(modified_lines)


def remove_unused_imports(content, filename):
    """Remove unused imports."""
    if filename not in FILES_TO_REMOVE_IMPORTS:
        return content

    lines = content.split("\n")
    modified_lines = []

    for line in lines:
        should_remove = False
        for import_to_remove in FILES_TO_REMOVE_IMPORTS[filename]:
            if import_to_remove.strip() in line.strip():
                should_remove = True
                print(f"Removed import from {filename}: {import_to_remove.strip()}")
                break

        if not should_remove:
            modified_lines.append(line)

    return "\n".join(modified_lines)


def remove_validation_import(content, filename):
    """Remove unused buf/validate import."""
    if filename not in FILES_TO_REMOVE_VALIDATION_IMPORT:
        return content

    lines = content.split("\n")
    modified_lines = []

    for line in lines:
        if 'import "buf/validate/validate.proto";' in line:
            print(f"Removed unused validation import from {filename}")
            continue
        modified_lines.append(line)

    return "\n".join(modified_lines)


def process_file(filepath):
    """Process a single protobuf file."""
    filename = os.path.basename(filepath)
    print(f"\nProcessing {filename}...")

    try:
        content = read_file(filepath)
        original_content = content

        # Remove unused imports first
        content = remove_unused_imports(content, filename)

        # Remove unused validation imports if needed
        content = remove_validation_import(content, filename)

        # Add validation rules if needed
        content = add_validation_rules(content, filename)

        # Only write if content changed
        if content != original_content:
            write_file(filepath, content)
            print(f"Updated {filename}")
        else:
            print(f"No changes needed for {filename}")

    except Exception as e:
        print(f"Error processing {filename}: {e}")


def main():
    """Main function."""
    proto_dir = Path("proto/gcommon/v1/media")

    if not proto_dir.exists():
        print(f"Proto directory not found: {proto_dir}")
        return

    # Get all proto files mentioned in the lint errors
    all_files = set()
    all_files.update(FILES_TO_ADD_VALIDATION.keys())
    all_files.update(FILES_TO_REMOVE_IMPORTS.keys())
    all_files.update(FILES_TO_REMOVE_VALIDATION_IMPORT)

    processed_count = 0
    for filename in sorted(all_files):
        filepath = proto_dir / filename
        if filepath.exists():
            process_file(filepath)
            processed_count += 1
        else:
            print(f"File not found: {filepath}")

    print(f"\nProcessed {processed_count} files")
    print("Run 'make lint' to verify the fixes")


if __name__ == "__main__":
    main()
