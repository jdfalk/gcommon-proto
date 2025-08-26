#!/bin/bash
# file: scripts/add-protovalidate.sh
# version: 1.0.0
# guid: 123e4567-e89b-12d3-a456-426614174001

set -euo pipefail

# Protovalidate Integration Wrapper Script
#
# This script provides a user-friendly interface to the protovalidate-adder.py tool
# for adding validation rules to protobuf files in the gcommon repository.

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
TOOL_PATH="$PROJECT_ROOT/tools/protovalidate-adder.py"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Print colored output
print_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

# Show usage information
show_usage() {
    cat << EOF
🚀 Protovalidate Integration Tool for gcommon

USAGE:
    $0 [OPTIONS]

OPTIONS:
    --all               Process all proto files in the repository
    --dry-run           Preview changes without modifying files
    --compatibility     Add validation rules as comments (for environments without protovalidate)
    --file <path>       Process specific proto file
    --help, -h          Show this help message

EXAMPLES:
    $0 --all                                    # Process all proto files
    $0 --dry-run                               # Preview changes for all files
    $0 --file proto/gcommon/v1/auth/user.proto # Process specific file
    $0 --compatibility --all                   # Add rules as comments

FEATURES:
    • Intelligent validation rule generation based on field semantics
    • Automatic import detection and addition
    • Preservation of existing validation rules
    • Safe dry-run mode for previewing changes
    • Compatibility mode for gradual adoption
    • Mass processing of thousands of files

For more information, see: PROTOVALIDATE_INTEGRATION.md
EOF
}

# Check if the Python tool exists
check_tool() {
    if [[ ! -f "$TOOL_PATH" ]]; then
        print_error "Python tool not found at: $TOOL_PATH"
        print_info "Please ensure the protovalidate-adder.py tool is available"
        exit 1
    fi

    if [[ ! -x "$TOOL_PATH" ]]; then
        print_warning "Making tool executable..."
        chmod +x "$TOOL_PATH"
    fi
}

# Main function
main() {
    local args=()
    local dry_run=false
    local show_help=false
    local file_mode=false
    local compatibility_mode=false

    # Parse arguments
    while [[ $# -gt 0 ]]; do
        case $1 in
            --all)
                # Default behavior, process all files
                shift
                ;;
            --dry-run)
                args+=("--dry-run")
                dry_run=true
                shift
                ;;
            --compatibility)
                args+=("--compatibility-mode")
                compatibility_mode=true
                shift
                ;;
            --file)
                if [[ -z "${2:-}" ]]; then
                    print_error "Option --file requires a file path"
                    exit 1
                fi
                args+=("--file" "$2")
                file_mode=true
                shift 2
                ;;
            --help|-h)
                show_help=true
                shift
                ;;
            --verbose|-v)
                args+=("--verbose")
                shift
                ;;
            *)
                print_error "Unknown option: $1"
                print_info "Use --help for usage information"
                exit 1
                ;;
        esac
    done

    # Show help if requested
    if [[ "$show_help" == true ]]; then
        show_usage
        exit 0
    fi

    # Check tool availability
    check_tool

    # Change to project root
    cd "$PROJECT_ROOT"

    # Show operation info
    if [[ "$dry_run" == true ]]; then
        print_info "Running in DRY-RUN mode - no files will be modified"
    fi

    if [[ "$compatibility_mode" == true ]]; then
        print_info "Running in COMPATIBILITY mode - validation rules will be added as comments"
    fi

    if [[ "$file_mode" == true ]]; then
        print_info "Processing specific file"
    else
        print_info "Processing all proto files in the repository"
        echo
        print_warning "This will process 1600+ proto files. Continue? (y/N)"
        read -r response
        if [[ ! "$response" =~ ^[Yy]$ ]]; then
            print_info "Operation cancelled"
            exit 0
        fi
    fi

    # Run the Python tool
    print_info "Starting protovalidate integration..."
    echo

    # Handle empty args array properly
    if [[ ${#args[@]} -eq 0 ]]; then
        python3 "$TOOL_PATH"
    else
        python3 "$TOOL_PATH" "${args[@]}"
    fi

    local exit_code=$?
    if [[ $exit_code -eq 0 ]]; then
        echo
        print_success "Protovalidate integration completed successfully!"

        if [[ "$dry_run" == false ]]; then
            print_info "Next steps:"
            print_info "  1. Review the changes: git diff"
            print_info "  2. Test the build: make generate"
            print_info "  3. Commit the changes: git add . && git commit"
        fi
    else
        echo
        print_error "Protovalidate integration failed!"
        print_info "Check the error messages above for details"
        exit 1
    fi
}

# Run main function with all arguments
main "$@"
