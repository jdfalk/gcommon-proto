# Protocol Buffer Reorganization - Migration Guide

This directory contains the complete implementation of the comprehensive Protocol Buffer reorganization plan for the GCommon repository.

## Overview

The migration reorganizes 1,632+ Protocol Buffer files from the scattered `pkg/*/proto/` structure to a clean, organized `proto/gcommon/v1/` structure following Buf's best practices and implementing managed mode.

## Target Architecture

### Before (Current State)

```
pkg/
├── common/proto/           # 40+ files
├── config_*/proto/         # 150+ files (scattered across config_1, config_2, etc.)
├── database*/proto/        # 680+ files
├── media/proto/            # 890+ files
├── metrics*/proto/         # 230+ files
├── organization*/proto/    # 150+ files
├── queue*/proto/           # 180+ files
└── web*/proto/             # 200+ files
```

### After (Target State)

```
proto/gcommon/v1/
├── common/
│   ├── types/              # Basic types, entities, errors
│   ├── messages/           # Audit, events, notifications
│   ├── enums/              # Status enums, levels
│   └── services/           # Common services
├── config/
│   ├── api/                # Configuration APIs
│   ├── v1/                 # Version 1 configs
│   ├── v2/                 # Version 2 configs
│   └── services/           # Config services
├── database/
│   ├── config/             # DB configuration
│   ├── services/           # DB services
│   ├── types/              # DB types
│   └── schema/             # Schema definitions
├── media/
│   ├── types/              # Audio, video, image types
│   ├── metadata/           # Media metadata
│   ├── services/           # Media services
│   └── processing/         # Processing definitions
├── metrics/
│   ├── v1/                 # Metrics v1
│   ├── v2/                 # Metrics v2
│   ├── services/           # Metrics services
│   └── types/              # Metrics types
├── organization/
│   ├── api/                # Organization APIs
│   ├── config/             # Org configuration
│   ├── services/           # Org services
│   └── types/              # Users, roles, teams
├── queue/
│   ├── api/                # Queue APIs
│   ├── config/             # Queue configuration
│   ├── services/           # Queue services
│   └── types/              # Messages, topics
└── web/
    ├── api/                # Web APIs
    ├── config/             # Web configuration
    ├── events/             # Web events, webhooks
    └── services/           # Web services
```

## Migration Scripts

### Core Scripts

1. **`orchestrate-migration.sh`** - Main orchestration script
   - Manages the complete migration pipeline
   - Supports dry-run mode and domain filtering
   - Handles backups and rollback

2. **`migrate-proto-files.py`** - Comprehensive migration script
   - Analyzes current proto structure
   - Performs systematic file migration
   - Updates import paths and package names

3. **`migrate-domain.py`** - Domain-specific migration
   - Handles individual domain migrations
   - Domain-specific categorization logic
   - Business logic for each domain type

4. **`update-buf-config.py`** - Buf configuration updater
   - Updates buf.yaml for new structure
   - Configures buf.gen.yaml with managed mode
   - Sets up proper dependencies

5. **`validate-migration.py`** - Migration validation
   - Validates directory structure
   - Checks proto file consistency
   - Tests buf compilation

## Usage

### Quick Start (Recommended)

```bash
# Analyze current structure
./scripts/orchestrate-migration.sh analyze

# Run complete migration (dry-run first)
./scripts/orchestrate-migration.sh full --dry-run

# Execute actual migration
./scripts/orchestrate-migration.sh full
```

### Step-by-Step Migration

```bash
# 1. Analyze current state
./scripts/orchestrate-migration.sh analyze

# 2. Prepare for migration (creates backups)
./scripts/orchestrate-migration.sh prepare

# 3. Execute migration by domain
./scripts/orchestrate-migration.sh migrate --domain common
./scripts/orchestrate-migration.sh migrate --domain config
./scripts/orchestrate-migration.sh migrate --domain database
# ... etc for each domain

# 4. Validate results
./scripts/orchestrate-migration.sh validate
```

### Domain-Specific Migration

```bash
# Migrate only specific domains
python3 scripts/migrate-domain.py common --dry-run
python3 scripts/migrate-domain.py config
python3 scripts/migrate-domain.py database
```

### Rollback (If Needed)

```bash
# Rollback changes
./scripts/orchestrate-migration.sh rollback
```

## Migration Process Details

### Phase 1: Analysis and Preparation

1. **Structure Analysis**: Discovers all proto files and their dependencies
2. **Domain Mapping**: Maps scattered domains to organized structure
3. **Backup Creation**: Creates git branch and filesystem backups
4. **Directory Creation**: Sets up new proto/ directory structure

### Phase 2: File Migration

1. **Domain Processing**: Processes domains in dependency order
2. **File Categorization**: Categorizes files into appropriate subdirectories
3. **Content Updates**: Updates file headers, packages, and import paths
4. **Path Resolution**: Converts all old import paths to new structure

### Phase 3: Configuration Updates

1. **Buf Configuration**: Updates buf.yaml for new module structure
2. **Managed Mode**: Enables buf managed mode with Go package mappings
3. **Plugin Configuration**: Configures code generation plugins
4. **Dependency Management**: Sets up proper protobuf dependencies

### Phase 4: Validation and Testing

1. **Structure Validation**: Ensures all directories and files are correct
2. **Import Validation**: Verifies all import paths resolve correctly
3. **Buf Compilation**: Tests buf build and generation
4. **Content Validation**: Checks package names and go_package options

---

For detailed implementation, see the individual script files and the comprehensive MASSIVE-REORG-PLAN.md.
