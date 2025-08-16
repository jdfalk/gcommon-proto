#!/bin/bash
# file: scripts/orchestrate-migration.sh
# version: 1.0.0
# guid: 0d1e2f3a-4b5c-6d7e-8f9a-0b1c2d3e4f5a

set -euo pipefail

# Migration orchestration script for Protocol Buffer reorganization
# This script manages the complete migration process following the MASSIVE-REORG-PLAN

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$ROOT_DIR"

# Configuration
DRY_RUN=false
DOMAIN_FILTER=""
BACKUP_CREATED=false
ROLLBACK_MODE=false

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Logging
log() {
    echo -e "${BLUE}[$(date +'%Y-%m-%d %H:%M:%S')] $1${NC}"
}

success() {
    echo -e "${GREEN}✅ $1${NC}"
}

warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

error() {
    echo -e "${RED}❌ $1${NC}"
}

# Usage information
show_usage() {
    cat << EOF
Protocol Buffer Migration Orchestrator

Usage: $0 [OPTIONS] COMMAND

Commands:
    analyze     - Analyze current proto structure
    prepare     - Prepare for migration (create directories, backups)
    migrate     - Execute the migration
    validate    - Validate migration results
    rollback    - Rollback migration (if needed)
    full        - Execute complete migration pipeline

Options:
    --dry-run           Show what would be done without executing
    --domain DOMAIN     Process only specific domain
    --help             Show this help message

Domains: common, config, database, media, metrics, organization, queue, web

Examples:
    $0 analyze                    # Analyze current structure
    $0 prepare                    # Prepare for migration
    $0 migrate --domain common    # Migrate only common domain
    $0 full --dry-run            # Show full migration plan
    $0 rollback                  # Rollback changes

EOF
}

# Parse command line arguments
parse_args() {
    while [[ $# -gt 0 ]]; do
        case $1 in
            --dry-run)
                DRY_RUN=true
                shift
                ;;
            --domain)
                DOMAIN_FILTER="$2"
                shift 2
                ;;
            --help)
                show_usage
                exit 0
                ;;
            analyze|prepare|migrate|validate|rollback|full)
                COMMAND="$1"
                shift
                ;;
            *)
                error "Unknown option: $1"
                show_usage
                exit 1
                ;;
        esac
    done

    if [[ -z "${COMMAND:-}" ]]; then
        error "No command specified"
        show_usage
        exit 1
    fi
}

# Prerequisites check
check_prerequisites() {
    log "Checking prerequisites..."
    
    # Check required tools
    local missing_tools=()
    
    if ! command -v python3 &> /dev/null; then
        missing_tools+=("python3")
    fi
    
    if ! command -v git &> /dev/null; then
        missing_tools+=("git")
    fi
    
    # buf is optional but recommended
    if ! command -v buf &> /dev/null; then
        warning "buf command not found - some validations will be skipped"
    fi
    
    if [[ ${#missing_tools[@]} -gt 0 ]]; then
        error "Missing required tools: ${missing_tools[*]}"
        exit 1
    fi
    
    # Check Python dependencies
    if ! python3 -c "import yaml" 2>/dev/null; then
        warning "PyYAML not found - installing..."
        pip3 install pyyaml || {
            error "Failed to install PyYAML"
            exit 1
        }
    fi
    
    success "Prerequisites check passed"
}

# Create backup
create_backup() {
    if [[ "$BACKUP_CREATED" == "true" ]]; then
        log "Backup already created"
        return
    fi
    
    log "Creating backup..."
    
    # Create git backup branch
    local backup_branch="proto-reorg-backup-$(date +%Y%m%d_%H%M%S)"
    git checkout -b "$backup_branch"
    git push origin "$backup_branch" || warning "Could not push backup branch"
    git checkout -
    
    # Create filesystem backup
    local backup_file="gcommon-backup-$(date +%Y%m%d_%H%M%S).tar.gz"
    tar -czf "$backup_file" \
        --exclude='.git' \
        --exclude='node_modules' \
        --exclude='target' \
        --exclude='*.log' \
        --exclude='logs' \
        .
    
    mkdir -p ~/backups
    mv "$backup_file" ~/backups/ || {
        warning "Could not move backup to ~/backups"
    }
    
    BACKUP_CREATED=true
    success "Backup created: ~/backups/$backup_file"
}

# Analyze current structure
analyze_structure() {
    log "Analyzing current proto structure..."
    
    local proto_count=$(find pkg -name "*.proto" 2>/dev/null | wc -l)
    local domains=$(find pkg -type d -name proto -exec dirname {} \; | sed 's|pkg/||' | sort -u)
    
    echo "📊 Current Structure Analysis:"
    echo "   Total proto files: $proto_count"
    echo "   Domains found:"
    
    while IFS= read -r domain; do
        if [[ -n "$domain" ]]; then
            local count=$(find "pkg/$domain/proto" -name "*.proto" 2>/dev/null | wc -l)
            echo "     $domain: $count files"
        fi
    done <<< "$domains"
    
    # Check for issues
    echo "   Checking for issues..."
    local issues=0
    
    # Check for old import paths
    if grep -r 'import "pkg/' pkg/ --include="*.proto" >/dev/null 2>&1; then
        echo "     ⚠️  Found files with old import paths"
        ((issues++))
    fi
    
    # Check for missing package declarations
    local missing_package=$(find pkg -name "*.proto" -exec grep -L "package " {} \; | wc -l)
    if [[ "$missing_package" -gt 0 ]]; then
        echo "     ⚠️  Found $missing_package files missing package declarations"
        ((issues++))
    fi
    
    if [[ "$issues" -eq 0 ]]; then
        success "No critical issues found"
    else
        warning "Found $issues types of issues"
    fi
}

# Prepare for migration
prepare_migration() {
    log "Preparing for migration..."
    
    # Create backup
    create_backup
    
    # Create proto directory structure
    log "Creating proto directory structure..."
    python3 -c "
import os
domains = ['common', 'config', 'database', 'media', 'metrics', 'organization', 'queue', 'web']
subdirs = ['api', 'config', 'services', 'types', 'messages']

for domain in domains:
    for subdir in subdirs:
        path = f'proto/gcommon/v1/{domain}/{subdir}'
        os.makedirs(path, exist_ok=True)
        print(f'Created: {path}')
"
    
    success "Migration preparation completed"
}

# Execute migration
execute_migration() {
    log "Executing proto file migration..."
    
    local migrate_args=()
    
    if [[ "$DRY_RUN" == "true" ]]; then
        migrate_args+=("--dry-run")
    fi
    
    if [[ -n "$DOMAIN_FILTER" ]]; then
        migrate_args+=("--domain" "$DOMAIN_FILTER")
    fi
    
    # Run migration script
    python3 scripts/migrate-proto-files.py "${migrate_args[@]}"
    
    if [[ "$DRY_RUN" == "false" ]]; then
        success "Migration executed"
    else
        success "Migration plan displayed (dry-run mode)"
    fi
}

# Update buf configuration
update_buf_config() {
    if [[ "$DRY_RUN" == "true" ]]; then
        log "Would update buf configuration (dry-run mode)"
        return
    fi
    
    log "Updating buf configuration..."
    python3 scripts/update-buf-config.py
    success "Buf configuration updated"
}

# Validate migration
validate_migration() {
    log "Validating migration results..."
    python3 scripts/validate-migration.py
}

# Rollback migration
rollback_migration() {
    log "Rolling back migration..."
    
    if [[ ! -f "buf.yaml.backup" ]] || [[ ! -f "buf.gen.yaml.backup" ]]; then
        error "Backup files not found - cannot rollback"
        exit 1
    fi
    
    # Restore buf configuration
    mv buf.yaml.backup buf.yaml
    mv buf.gen.yaml.backup buf.gen.yaml
    
    # Remove proto directory
    if [[ -d "proto" ]]; then
        rm -rf proto
    fi
    
    success "Migration rolled back"
}

# Full migration pipeline
full_migration() {
    log "Starting full migration pipeline..."
    
    check_prerequisites
    analyze_structure
    prepare_migration
    execute_migration
    
    if [[ "$DRY_RUN" == "false" ]]; then
        update_buf_config
        validate_migration
    fi
    
    success "Full migration pipeline completed"
}

# Signal handlers for cleanup
cleanup() {
    if [[ -n "${TEMP_DIR:-}" ]] && [[ -d "$TEMP_DIR" ]]; then
        rm -rf "$TEMP_DIR"
    fi
}

trap cleanup EXIT

# Main execution
main() {
    parse_args "$@"
    
    echo "🚀 Protocol Buffer Migration Orchestrator"
    echo "   Command: $COMMAND"
    echo "   Dry run: $DRY_RUN"
    echo "   Domain filter: ${DOMAIN_FILTER:-all}"
    echo ""
    
    case "$COMMAND" in
        analyze)
            check_prerequisites
            analyze_structure
            ;;
        prepare)
            check_prerequisites
            prepare_migration
            ;;
        migrate)
            check_prerequisites
            execute_migration
            ;;
        validate)
            check_prerequisites
            validate_migration
            ;;
        rollback)
            rollback_migration
            ;;
        full)
            full_migration
            ;;
        *)
            error "Unknown command: $COMMAND"
            exit 1
            ;;
    esac
}

# Execute main function
main "$@"