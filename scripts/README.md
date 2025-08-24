# file: scripts/README.md

# version: 1.0.0

# guid: c3d4e5f6-a7b8-9012-cdef-345678901234

# Scripts Directory

This directory contains utility scripts for managing the gcommon repository.

## Code Scanning Alert Management

### dismiss_sdk_unused_import_alerts.py

A Python script to automatically dismiss code scanning alerts for unused imports in the SDK folder.

**Features:**

- Finds all open code scanning alerts for unused imports/variables in `sdks/` folder
- Supports dry-run mode to preview what would be dismissed
- Configurable dismiss reason
- Detailed logging and progress reporting

**Usage:**

```bash
# Preview what would be dismissed (recommended first step)
python3 scripts/dismiss_sdk_unused_import_alerts.py --dry-run

# Dismiss alerts with default reason ("used in library")
python3 scripts/dismiss_sdk_unused_import_alerts.py

# Dismiss alerts with custom reason
python3 scripts/dismiss_sdk_unused_import_alerts.py --reason "false positive"

# Show help
python3 scripts/dismiss_sdk_unused_import_alerts.py --help
```

**Dismiss Reasons:**

- `used in library` (default) - For imports that are actually used but not detected
- `false positive` - For incorrect alerts
- `wont fix` - For alerts that won't be addressed

### dismiss-sdk-alerts.sh

A simple bash wrapper for the Python script that provides a more convenient interface.

**Usage:**

```bash
# Dry run
./scripts/dismiss-sdk-alerts.sh --dry-run

# Dismiss alerts
./scripts/dismiss-sdk-alerts.sh

# Custom reason
./scripts/dismiss-sdk-alerts.sh --reason "false positive"
```

## Why Dismiss SDK Alerts?

The SDK files in the `sdks/` folder are auto-generated from protocol buffer definitions. These generated files often contain imports that:

1. Are required by the protobuf runtime but appear unused to static analysis
2. Are imported for type annotations that may not be directly referenced
3. Are part of the generated API surface but not used in the specific file

Since these are generated files that shouldn't be manually edited, dismissing these specific alerts is appropriate and helps keep the code scanning results focused on actual source code issues.

## Requirements

- Python 3.6+
- GitHub CLI (`gh`) installed and authenticated
- Repository write access for dismissing alerts
