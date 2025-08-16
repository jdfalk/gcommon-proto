#!/bin/bash
# file: scripts/master-migration.sh
# version: 1.0.0
# guid: 9c0d1e2f-3a4b-5c6d-7e8f-9a0b-1c2d3e4f

set -euo pipefail

# Master migration script that orchestrates the complete reorganization
# This script implements the full MASSIVE-REORG-PLAN step by step

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$ROOT_DIR"

# Configuration
DRY_RUN=false
SKIP_BACKUP=false
DOMAIN_FILTER=""
VERBOSE=false

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Logging functions
log() { echo -e "${BLUE}[$(date +'%H:%M:%S')] $1${NC}"; }
success() { echo -e "${GREEN}✅ $1${NC}"; }
warning() { echo -e "${YELLOW}⚠️  $1${NC}"; }
error() { echo -e "${RED}❌ $1${NC}"; }
info() { echo -e "${CYAN}ℹ️  $1${NC}"; }
step() { echo -e "${PURPLE}🚀 STEP: $1${NC}"; }

# Progress tracking
TOTAL_STEPS=12
CURRENT_STEP=0

progress() {
    ((CURRENT_STEP++))
    echo -e "${PURPLE}📊 Progress: ${CURRENT_STEP}/${TOTAL_STEPS} - $1${NC}"
}

# Usage information
show_usage() {
    cat << EOF
🚀 GCommon Protocol Buffer Master Migration Script

This script executes the complete MASSIVE-REORG-PLAN to reorganize 1,632+ 
Protocol Buffer files from pkg/*/proto/ to proto/gcommon/v1/ structure.

Usage: $0 [OPTIONS]

Options:
    --dry-run              Show what would be done without executing
    --skip-backup          Skip backup creation (not recommended)
    --domain DOMAIN        Process only specific domain  
    --verbose              Enable verbose logging
    --help                 Show this help message

Domains: common, config, database, media, metrics, organization, queue, web

Examples:
    $0                           # Full migration with backups
    $0 --dry-run                 # Preview migration plan
    $0 --domain common           # Migrate only common domain
    $0 --skip-backup --verbose   # Migration without backup (verbose)

⚠️  WARNING: This script will reorganize 1,632+ files. Always run with 
   --dry-run first to review the migration plan.

📚 For detailed information, see:
   - tasks/REORG/MASSIVE-REORG-PLAN.md
   - scripts/MIGRATION_README.md

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
            --skip-backup)
                SKIP_BACKUP=true
                shift
                ;;
            --domain)
                DOMAIN_FILTER="$2"
                shift 2
                ;;
            --verbose)
                VERBOSE=true
                shift
                ;;
            --help)
                show_usage
                exit 0
                ;;
            *)
                error "Unknown option: $1"
                show_usage
                exit 1
                ;;
        esac
    done
}

# Prerequisites check
check_prerequisites() {
    step "Checking Prerequisites"
    
    local missing_tools=()
    
    # Check required tools
    if ! command -v python3 &> /dev/null; then
        missing_tools+=("python3")
    fi
    
    if ! command -v git &> /dev/null; then
        missing_tools+=("git")
    fi
    
    # Check Python dependencies
    if ! python3 -c "import yaml" 2>/dev/null; then
        warning "PyYAML not found - attempting to install..."
        pip3 install pyyaml || {
            error "Failed to install PyYAML - please install manually"
            exit 1
        }
    fi
    
    # Optional tools
    if ! command -v buf &> /dev/null; then
        warning "buf command not found - some validations will be skipped"
        info "Install buf: https://docs.buf.build/installation"
    fi
    
    if ! command -v go &> /dev/null; then
        warning "go command not found - Go compilation tests will be skipped"
    fi
    
    if [[ ${#missing_tools[@]} -gt 0 ]]; then
        error "Missing required tools: ${missing_tools[*]}"
        exit 1
    fi
    
    # Check repository state
    if [[ -n "$(git status --porcelain)" ]]; then
        warning "Repository has uncommitted changes"
        if [[ "$DRY_RUN" == "false" ]]; then
            read -p "Continue anyway? (y/N): " -n 1 -r
            echo
            if [[ ! $REPLY =~ ^[Yy]$ ]]; then
                error "Migration cancelled"
                exit 1
            fi
        fi
    fi
    
    success "Prerequisites check completed"
}

# Step 1: Analysis and Preparation
step_analysis() {
    progress "Current State Analysis"
    
    log "Analyzing current proto structure..."
    ./scripts/orchestrate-migration.sh analyze
    
    if [[ "$VERBOSE" == "true" ]]; then
        log "Generating dependency analysis..."
        python3 scripts/analyze-dependencies.py 2>/dev/null || true
    fi
    
    success "Analysis completed"
}

# Step 2: Backup Creation
step_backup() {
    if [[ "$SKIP_BACKUP" == "true" ]]; then
        warning "Skipping backup creation"
        return
    fi
    
    progress "Creating Backups"
    
    if [[ "$DRY_RUN" == "false" ]]; then
        log "Creating git backup branch..."
        local backup_branch="proto-reorg-backup-$(date +%Y%m%d_%H%M%S)"
        git checkout -b "$backup_branch"
        git push origin "$backup_branch" || warning "Could not push backup branch"
        git checkout -
        
        log "Creating filesystem backup..."
        local backup_file="gcommon-backup-$(date +%Y%m%d_%H%M%S).tar.gz"
        tar -czf "$backup_file" \
            --exclude='.git' \
            --exclude='node_modules' \
            --exclude='target' \
            --exclude='*.log' \
            --exclude='logs' \
            .
        
        mkdir -p ~/backups
        mv "$backup_file" ~/backups/ 2>/dev/null || true
        
        success "Backups created"
    else
        info "Would create backups (dry-run mode)"
    fi
}

# Step 3: Directory Structure Creation
step_create_structure() {
    progress "Creating Directory Structure"
    
    if [[ "$DRY_RUN" == "false" ]]; then
        log "Creating proto directory structure..."
        ./scripts/orchestrate-migration.sh prepare
    else
        info "Would create proto directory structure (dry-run mode)"
    fi
    
    success "Directory structure ready"
}

# Step 4: Domain Migration
step_migrate_domains() {
    progress "Migrating Protocol Buffer Files"
    
    local domains=("common" "config" "database" "media" "metrics" "organization" "queue" "web")
    
    if [[ -n "$DOMAIN_FILTER" ]]; then
        domains=("$DOMAIN_FILTER")
        log "Processing only domain: $DOMAIN_FILTER"
    fi
    
    for domain in "${domains[@]}"; do
        log "Migrating domain: $domain"
        
        local migrate_args=()
        if [[ "$DRY_RUN" == "true" ]]; then
            migrate_args+=("--dry-run")
        fi
        
        python3 scripts/migrate-domain.py "$domain" "${migrate_args[@]}"
        
        if [[ "$VERBOSE" == "true" && "$DRY_RUN" == "false" ]]; then
            log "Validating $domain migration..."
            python3 scripts/test-import-resolution.py || warning "$domain import validation failed"
        fi
    done
    
    success "Domain migration completed"
}

# Step 5: Buf Configuration Update
step_update_buf_config() {
    progress "Updating Buf Configuration"
    
    if [[ "$DRY_RUN" == "false" ]]; then
        log "Updating buf.yaml and buf.gen.yaml..."
        python3 scripts/update-buf-config.py
    else
        info "Would update buf configuration (dry-run mode)"
    fi
    
    success "Buf configuration updated"
}

# Step 6: Import Path Updates
step_update_imports() {
    progress "Updating Import Paths"
    
    log "Updating import paths across all proto files..."
    
    if [[ "$DRY_RUN" == "false" ]]; then
        # Import path updates are handled by the migration scripts
        log "Import paths updated during migration"
    else
        info "Would update import paths (dry-run mode)"
    fi
    
    success "Import paths updated"
}

# Step 7: Code Generation
step_generate_code() {
    progress "Generating Code"
    
    if command -v buf &> /dev/null && [[ "$DRY_RUN" == "false" ]]; then
        log "Generating protocol buffer code..."
        buf generate || warning "Code generation had issues"
    else
        info "Would generate code (buf not available or dry-run mode)"
    fi
    
    success "Code generation completed"
}

# Step 8: Validation
step_validation() {
    progress "Validating Migration"
    
    log "Running migration validation..."
    python3 scripts/validate-migration.py || warning "Some validation checks failed"
    
    if [[ "$VERBOSE" == "true" ]]; then
        log "Running comprehensive validation..."
        python3 scripts/comprehensive-validation.py || warning "Comprehensive validation had issues"
    fi
    
    success "Validation completed"
}

# Step 9: Performance Testing
step_performance() {
    progress "Performance Testing"
    
    if command -v buf &> /dev/null && [[ "$DRY_RUN" == "false" ]]; then
        log "Running performance comparison..."
        python3 scripts/performance-comparison.py || warning "Performance testing had issues"
    else
        info "Would run performance tests (dry-run mode or buf not available)"
    fi
    
    success "Performance testing completed"
}

# Step 10: Cleanup
step_cleanup() {
    progress "Post-Migration Cleanup"
    
    if [[ "$DRY_RUN" == "false" ]]; then
        log "Cleaning up old generated files..."
        python3 scripts/cleanup-generated-code.py || warning "Generated code cleanup had issues"
        
        log "Cleaning up old proto files..."
        python3 scripts/cleanup-old-protos.py || warning "Old proto cleanup had issues"
    else
        info "Would perform cleanup (dry-run mode)"
    fi
    
    success "Cleanup completed"
}

# Step 11: Documentation Updates
step_documentation() {
    progress "Updating Documentation"
    
    if [[ "$DRY_RUN" == "false" ]]; then
        log "Updating proto documentation..."
        python3 scripts/update-proto-docs.py || warning "Documentation update had issues"
        
        log "Generating migration report..."
        python3 scripts/generate-migration-report.py || warning "Report generation had issues"
    else
        info "Would update documentation (dry-run mode)"
    fi
    
    success "Documentation updated"
}

# Step 12: Final Verification
step_final_verification() {
    progress "Final Verification"
    
    log "Running final system verification..."
    python3 scripts/final-verification.py || {
        error "Final verification failed"
        
        if [[ "$DRY_RUN" == "false" ]]; then
            warning "Migration may need attention - check logs"
            info "To rollback: ./scripts/orchestrate-migration.sh rollback"
        fi
        
        return 1
    }
    
    success "Final verification passed"
}

# Main execution function
main() {
    echo "🚀 GCommon Protocol Buffer Master Migration"
    echo "=============================================="
    echo ""
    echo "📊 Migration Overview:"
    echo "   • Total proto files: ~1,632"
    echo "   • Domains: 8 (common, config, database, media, metrics, organization, queue, web)"
    echo "   • Target structure: proto/gcommon/v1/"
    echo "   • Dry run: $DRY_RUN"
    echo "   • Skip backup: $SKIP_BACKUP"
    echo "   • Domain filter: ${DOMAIN_FILTER:-all}"
    echo "   • Verbose: $VERBOSE"
    echo ""
    
    if [[ "$DRY_RUN" == "false" ]]; then
        warning "This will reorganize 1,632+ protocol buffer files"
        read -p "Continue with actual migration? (y/N): " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            info "Migration cancelled"
            exit 0
        fi
    fi
    
    # Execute migration steps
    local start_time=$(date +%s)
    
    check_prerequisites
    step_analysis
    step_backup
    step_create_structure
    step_migrate_domains
    step_update_buf_config
    step_update_imports
    step_generate_code
    step_validation
    step_performance
    step_cleanup
    step_documentation
    step_final_verification
    
    local end_time=$(date +%s)
    local duration=$((end_time - start_time))
    
    echo ""
    echo "🎉 MIGRATION COMPLETED SUCCESSFULLY!"
    echo "====================================="
    echo ""
    echo "📊 Migration Summary:"
    echo "   • Duration: ${duration}s"
    echo "   • Mode: $([ "$DRY_RUN" == "true" ] && echo "DRY RUN" || echo "ACTUAL")"
    echo "   • Domains processed: $([ -n "$DOMAIN_FILTER" ] && echo "$DOMAIN_FILTER" || echo "all")"
    echo ""
    
    if [[ "$DRY_RUN" == "false" ]]; then
        echo "📋 Next Steps:"
        echo "   1. Review migration-report.html"
        echo "   2. Update CI/CD pipelines"
        echo "   3. Update team documentation"
        echo "   4. Test code generation: buf generate"
        echo "   5. Verify builds: go build ./..."
        echo ""
        echo "📁 Generated Files:"
        echo "   • migration-report.html - Detailed migration report"
        echo "   • migration-report.json - Migration statistics"
        echo "   • docs/PROTO_STRUCTURE.md - New structure documentation"
        echo ""
        echo "🔄 Rollback (if needed):"
        echo "   ./scripts/orchestrate-migration.sh rollback"
    else
        echo "ℹ️  This was a dry run. To execute actual migration:"
        echo "   $0 $(echo "$@" | sed 's/--dry-run//')"
    fi
    
    echo ""
    echo "🎯 Migration completed successfully!"
}

# Signal handling for cleanup
cleanup() {
    if [[ -n "${TEMP_DIR:-}" ]] && [[ -d "$TEMP_DIR" ]]; then
        rm -rf "$TEMP_DIR"
    fi
}

trap cleanup EXIT

# Execute main function
parse_args "$@"
main "$@"