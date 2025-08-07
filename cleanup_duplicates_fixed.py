#!/usr/bin/env python3
# file: cleanup_duplicates.py
# version: 1.0.0
# guid: 4d7e8f9a-1b2c-3d4e-5f6a-7b8c9d0e1f2a

import glob
import os
import re


def check_file_exists(filepath):
    """Check if a file exists before attempting operations"""
    return os.path.exists(filepath)


def is_duplicate_content(filepath):
    """Check if file contains only basic placeholder content"""
    if not check_file_exists(filepath):
        return False

    try:
        with open(filepath, "r") as f:
            content = f.read()

        # Check if it's a basic placeholder with minimal content
        lines = content.strip().split("\n")
        non_comment_lines = [
            line for line in lines if not line.strip().startswith("//") and line.strip()
        ]

        # If it has less than 8 non-comment lines and no message definitions, it's likely a duplicate
        has_message = any("message " in line for line in non_comment_lines)
        has_enum = any("enum " in line for line in non_comment_lines)
        has_service = any("service " in line for line in non_comment_lines)

        return len(non_comment_lines) < 8 and not (
            has_message or has_enum or has_service
        )
    except Exception as e:
        print(f"Error checking {filepath}: {e}")
        return False


# Files that should be removed (duplicates created by mistake)
potential_duplicate_files = [
    "pkg/common/proto/ack_mode.proto",
    "pkg/common/proto/audit_log.proto",
    "pkg/common/proto/batch_operation.proto",
    "pkg/common/proto/cache_policy.proto",
    "pkg/common/proto/circuit_breaker_config.proto",
    "pkg/common/proto/config_value.proto",
    "pkg/common/proto/filter_options.proto",
    "pkg/common/proto/filter_value.proto",
    "pkg/common/proto/retry_policy.proto",
    "pkg/common/proto/subscription_info.proto",
    "pkg/common/proto/subscription_options.proto",
    "pkg/common/proto/time_range.proto",
    "pkg/config/proto/access_restriction.proto",
    "pkg/config/proto/restriction_type.proto",
    "pkg/organization/proto/tenant_quota.proto",
]


def main():
    print("🔍 Checking for duplicate files...")

    # Check each potential duplicate
    files_to_remove = []
    for filepath in potential_duplicate_files:
        if check_file_exists(filepath):
            if is_duplicate_content(filepath):
                files_to_remove.append(filepath)
                print(f"  ❌ {filepath} - marked for removal (duplicate/placeholder)")
            else:
                print(f"  ✅ {filepath} - keeping (has real content)")
        else:
            print(f"  ⚠️  {filepath} - doesn't exist")

    # Remove duplicates if any found
    if files_to_remove:
        print(f"\n🗑️  Removing {len(files_to_remove)} duplicate files...")
        for filepath in files_to_remove:
            try:
                os.remove(filepath)
                print(f"  ✅ Removed {filepath}")
            except Exception as e:
                print(f"  ❌ Failed to remove {filepath}: {e}")
    else:
        print("✅ No duplicate files found to remove")

    # Clean up duplicate imports in all proto files
    print("\n🧹 Cleaning duplicate imports...")
    proto_files = glob.glob("pkg/**/*.proto", recursive=True)

    for filepath in proto_files:
        if not check_file_exists(filepath):
            continue

        try:
            with open(filepath, "r") as f:
                lines = f.readlines()

            # Track seen imports and keep only first occurrence
            seen_imports = set()
            cleaned_lines = []
            changed = False

            for line in lines:
                # Check if this is an import line
                if line.strip().startswith('import "'):
                    import_match = re.search(r'import "([^"]+)"', line)
                    if import_match:
                        import_path = import_match.group(1)
                        if import_path not in seen_imports:
                            seen_imports.add(import_path)
                            cleaned_lines.append(line)
                        else:
                            changed = True  # Skip duplicate imports
                    else:
                        cleaned_lines.append(line)
                else:
                    cleaned_lines.append(line)

            # Only write if we made changes
            if changed:
                with open(filepath, "w") as f:
                    f.writelines(cleaned_lines)
                print(f"  ✅ Cleaned imports in {filepath}")

        except Exception as e:
            print(f"  ❌ Error processing {filepath}: {e}")

    print("\n🎉 Cleanup complete!")


if __name__ == "__main__":
    main()
